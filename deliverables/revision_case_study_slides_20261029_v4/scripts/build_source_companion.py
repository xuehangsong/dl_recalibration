"""Create a five-slide companion containing byte-exact manuscript figures.

Original images remain complete and unmodified. Titles/captions/notes are
separate editable PowerPoint text; no content is overlaid on an image.
"""
from pathlib import Path
from zipfile import ZipFile
import hashlib
import io
import json
import sys

sys.path.insert(0, '/tmp/dl_slides_20261029_python')
from lxml import etree
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
SOURCE = REPO / 'method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx'
STEM = 'Yilin_original_figures_20261029'
ORIGINALS = ROOT / 'sources/original_figures'
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def accepted_text(paragraph):
    return ''.join(t.text or '' for t in paragraph.findall('.//w:t', NS)
                   if not any(a.tag in {'{' + NS['w'] + '}del',
                                        '{' + NS['w'] + '}moveFrom'}
                              for a in t.iterancestors()))


def text(slide, value, x, y, w, h, size, color=(35, 50, 60), bold=False):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    p.text = value
    p.font.name = 'Arial'
    p.font.size = Pt(size)
    p.font.bold = bold
    p.font.color.rgb = RGBColor(*color)
    p.space_before = p.space_after = Pt(0)
    return shape


def fit_original(slide, path, box=(.55, 1.48, 12.23, 4.80)):
    with Image.open(path) as im:
        width, height = im.size
    x, y, max_w, max_h = box
    ratio = min(max_w / width, max_h / height)
    w, h = width * ratio, height * ratio
    return slide.shapes.add_picture(str(path), Inches(x + (max_w - w) / 2),
                                   Inches(y + (max_h - h) / 2),
                                   width=Inches(w), height=Inches(h))


def build():
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    (ROOT / 'qa').mkdir(exist_ok=True)
    manuscript_hash = digest(SOURCE.read_bytes())
    figures = []
    with ZipFile(SOURCE) as source_zip:
        document = etree.fromstring(source_zip.read('word/document.xml'))
        relationships = etree.fromstring(source_zip.read('word/_rels/document.xml.rels'))
        rels = {r.get('Id'): r.get('Target') for r in relationships}
        paragraphs = document.findall('.//w:body/w:p', NS)
        for number in range(1, 6):
            part = f'word/media/image{number}.png'
            data = source_zip.read(part)
            matches = []
            for index, paragraph in enumerate(paragraphs):
                for blip in paragraph.findall('.//a:blip', NS):
                    rid = blip.get('{' + NS['r'] + '}embed')
                    if rels.get(rid) == f'media/image{number}.png':
                        caption = accepted_text(paragraphs[index + 1])
                        matches.append((rid, index, caption))
            assert len(matches) == 1, (number, matches)
            rid, paragraph_index, caption = matches[0]
            assert caption.startswith(f'Figure {number}.'), (number, caption)
            destination = ORIGINALS / f'figure_{number:02d}_original.png'
            destination.write_bytes(data)
            assert destination.read_bytes() == data
            with Image.open(io.BytesIO(data)) as im:
                dimensions = list(im.size)
            figures.append({'manuscript_figure': number,
                            'docx_part': part, 'relationship_id': rid,
                            'body_paragraph_index_zero_based': paragraph_index,
                            'original_caption': caption, 'source_part_sha256': digest(data),
                            'extracted_path': str(destination.relative_to(ROOT)),
                            'dimensions_px': dimensions,
                            'treatment': 'Complete original image, byte-exact extraction; no crop, recoloring, relabeling, or reconstruction.'})

    titles = [
        'Original Figure 1 — Mass90 regime selection',
        'Original Figure 2 — Static-model performance and plume fields',
        'Original Figure 3 — Fine-tuning comparisons',
        'Original Figure 4 — Update configurations and plume recovery',
        'Original Figure 5 — Adaptive replay and the acceptance region',
    ]
    captions = [
        'Complete source figure. The Mass90 score defines historical and rare response regimes retrospectively.',
        'Complete source figure. Historical and rare spatial examples use different concentration and error scales.',
        'Source-only comparison: panel baselines, Model C identity, and the 25%/30% criteria require reconciliation.',
        'Complete source figure. The historical physical-metric panel label differs from its manuscript caption.',
        "Complete source figure. The 30% / 85% screen is illustrative; panel (a)'s threshold placement is unresolved.",
    ]
    notes_extra = [
        'The historical cutoff is the 40th percentile, s=0.133; the rare cutoff is the 97th percentile, s=0.329. The source title, histogram, annotations, and ensemble identifiers are retained as supplied. This requires reference plume information at t and t+1 and is not a prospective detector.',
        'The v4 main-deck rare triplet is a pixel-faithful crop from panel(b) of this figure. This complete image also retains panel(a) distributions and the historical spatial triplet. Historical concentrations reach917.9 ug/L and signed errors span±19.1 ug/L; the rare concentration maximum is813.6 ug/L and signed errors span±169.4 ug/L. Do not compare colors between regimes as if they share scales.',
        'Preserved for source audit, not pooled into the main-deck ranking. Figure3(a) displays baseline historical/rare RMSE0.49/9.2, whereas Figure3(c) displays0.58/10.04. Figure3(c) labels a full-network ModelC pair0.64/0.99; its relationship to Figure4 configurations is unresolved. Figure3(b) uses a25% historical degradation boundary, while Figure5 uses30%/85%. The main deck keeps these protocols separate.',
        'Main-deck RMSE and rare physical-metric replots use only the directly labeled numbers in panel(a). The image labels the historical physical metric Peak error(hist,%), but the Figure4 caption calls it historical Mass90 error. That ambiguous historical column is omitted from main-deck replotting. Panel(c) is an original spatial comparison; raw arrays/sample identifier are unavailable. Colors and annotation crowding are preserved as supplied.',
        'Main-deck controller coordinates use panel(b) labels and match panel(c): fixed replay (80.4,88.9), threshold adaptive/forgetting (26.5,85.8), loss-balanced (21.1,85.5), and loss-balanced+floor (38.1,87.3), as historical degradation %, rare improvement %. The current replot retains these values and directions but changes colors/markers and zooms the axes. Panel(a) is preserved as the original image, not reconstructed from an inferred numeric trajectory. Its magenta dotted line is labeled Acceptance threshold (30%) but lies near the red forgetting-axis zero tick, below20%, rather than between20% and40%. The threshold placement or axis normalization is unresolved; the plotting code is unavailable, so this is an observed source-plot inconsistency rather than a diagnosed code error. The main deck uses the clearly displayed replay-ratio cap, not the suspect threshold trace. The high replay cap alone does not isolate adaptive scheduling benefit. Passing the illustrative panel(c) screen does not establish deployment readiness.',
    ]
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333333), Inches(7.5)
    notes_md = []
    for number, item in enumerate(figures, 1):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = RGBColor(255, 255, 255)
        title = text(slide, titles[number - 1], .60, .43, 12.10, .95, 26,
                     (32, 45, 55), bold=True)
        title.name = 'Source figure title'
        picture = fit_original(slide, ROOT / item['extracted_path'])
        picture.name = f'Original manuscript Figure {number}'
        picture._element.nvPicPr.cNvPr.set('descr', item['original_caption'])
        caption = text(slide, captions[number - 1], .65, 6.49, 12, .48, 14,
                       (55, 68, 76))
        caption.name = 'Separate source context'
        source_text = f'Source: Yilin manuscript, file version 2026_09_09; Figure {number}; complete original image.'
        text(slide, source_text, .65, 7.10, 11.8, .20, 9, (104, 114, 122)).name = 'Source attribution'
        text(slide, str(number), 12.46, 7.10, .25, .20, 9, (104, 114, 122)).name = 'Source slide number'
        notes = (item['original_caption'] + '\n\n' + notes_extra[number - 1] +
                 '\n\nSource: ' + str(SOURCE.relative_to(REPO)) +
                 '\nFile version label: 2026_09_09 (filename label; not an asserted revision or publication date).' +
                 '\nDOCX SHA-256: ' + manuscript_hash +
                 '\nImage part: ' + item['docx_part'] +
                 '\nImage SHA-256: ' + item['source_part_sha256'])
        slide.notes_slide.notes_text_frame.text = notes
        notes_md.append(f'## Source Figure {number}\n\n{notes}\n')
    prs.core_properties.title = 'Yilin original manuscript figures — source companion'
    prs.core_properties.subject = 'Complete, unmodified source figures for provenance review'
    prs.core_properties.author = 'Xuehang Song'
    out = ROOT / f'{STEM}.pptx'
    prs.save(out)
    (ROOT / f'{STEM}_speaker_notes.md').write_text('\n'.join(notes_md))
    manifest = {'source_docx': str(SOURCE.relative_to(REPO)),
                'source_filename_version': '2026_09_09',
                'version_label_semantics': 'Filename label only; not an asserted revision or publication date.',
                'source_docx_sha256': manuscript_hash,
                'source_figures': figures,
                'output_pptx': out.name, 'output_pptx_sha256': digest(out.read_bytes())}
    (ORIGINALS / 'source_manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')

    # Verify the embedded assets, not merely the extraction directory.
    reopened = Presentation(out)
    assert len(reopened.slides) == 5
    for slide, item in zip(reopened.slides, figures):
        pictures = [s for s in slide.shapes if s.shape_type == MSO_SHAPE_TYPE.PICTURE]
        assert len(pictures) == 1
        picture = pictures[0]
        assert digest(picture.image.blob) == item['source_part_sha256']
        assert picture.crop_left == picture.crop_right == picture.crop_top == picture.crop_bottom == 0
        pxw, pxh = item['dimensions_px']
        assert abs(picture.width / picture.height - pxw / pxh) < 1e-5
        for shape in slide.shapes:
            assert 0 <= shape.left and 0 <= shape.top
            assert shape.left + shape.width <= reopened.slide_width
            assert shape.top + shape.height <= reopened.slide_height
    (ROOT / 'qa/source_companion_build_verification.json').write_text(json.dumps({
        'slides': 5, 'one_picture_per_slide': True,
        'all_five_embedded_picture_hashes_match_docx_parts': True,
        'no_image_cropping': True, 'original_aspect_ratios_preserved': True,
        'all_shapes_in_bounds': True, 'full_original_captions_in_notes': True,
        'native_render_pending': True}, indent=2) + '\n')
    print(out, flush=True)


if __name__ == '__main__':
    build()

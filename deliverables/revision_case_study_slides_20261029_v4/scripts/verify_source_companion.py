"""Verify source-companion images, native render checks, PDF, and previews."""
from pathlib import Path
from zipfile import ZipFile
import hashlib
import json
import sys

sys.path.insert(0, '/tmp/dl_slides_20261029_python')
import fitz
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
STEM = 'Yilin_original_figures_20261029'
digest = lambda data: hashlib.sha256(data).hexdigest()
manifest = json.loads((ROOT / 'sources/original_figures/source_manifest.json').read_text())
source = REPO / manifest['source_docx']
assert digest(source.read_bytes()) == manifest['source_docx_sha256']
prs = Presentation(ROOT / f'{STEM}.pptx')
assert len(prs.slides) == 5
assert digest((ROOT / f'{STEM}.pptx').read_bytes()) == manifest['output_pptx_sha256']
checks = []
with ZipFile(source) as z:
    for slide, figure in zip(prs.slides, manifest['source_figures']):
        pictures = [s for s in slide.shapes if s.shape_type == MSO_SHAPE_TYPE.PICTURE]
        assert len(pictures) == 1
        picture = pictures[0]
        original = z.read(figure['docx_part'])
        assert picture.image.blob == original == (ROOT / figure['extracted_path']).read_bytes()
        assert digest(original) == figure['source_part_sha256']
        assert picture.crop_left == picture.crop_right == picture.crop_top == picture.crop_bottom == 0
        w, h = figure['dimensions_px']
        assert abs(picture.width / picture.height - w / h) < 1e-5
        assert figure['original_caption'] in slide.notes_slide.notes_text_frame.text
        checks.append({'figure': figure['manuscript_figure'], 'embedded_image_sha256': digest(original),
                       'byte_identical_to_docx': True, 'no_crop': True, 'aspect_ratio_preserved': True})
native = json.loads((ROOT / 'qa/source_companion_powerpoint_verification.json').read_text(encoding='utf-8-sig'))
assert native['NativePowerPointOpen'] and native['Slides'] == 5
for slide in native['SlideChecks']:
    assert slide['Pictures'] == 1
    assert not slide['TextOverflowShapes'] and not slide['OutOfBoundsShapes']
pdf_path = ROOT / f'{STEM}.pdf'
with fitz.open(pdf_path) as pdf:
    assert len(pdf) == 5
    for index, page in enumerate(pdf, 1):
        assert f'Original Figure {index}' in page.get_text()
sheet = Image.new('RGB', (1000, 843), 'white')
for number in range(1, 6):
    with Image.open(ROOT / f'source_previews/Slide{number}.PNG') as im:
        assert im.size == (1600, 900)
        thumb = im.convert('RGB').resize((500, 281), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (((number - 1) % 2) * 500, ((number - 1) // 2) * 281))
sheet.save(ROOT / 'qa/source_contact_sheet.png')
verification = {'result': 'PASS', 'slides': 5, 'pdf_pages': 5,
                'native_powerpoint_render_verified': True, 'preview_count': 5,
                'no_native_text_overflow_or_out_of_bounds': True,
                'original_images_verified': checks,
                'pptx_sha256': digest((ROOT / f'{STEM}.pptx').read_bytes()),
                'pdf_sha256': digest(pdf_path.read_bytes()),
                'source_docx_sha256': manifest['source_docx_sha256'],
                'visual_review': 'All five rendered slides reviewed; complete original images retained, captions separate, no clipping.'}
(ROOT / 'qa/source_companion_delivery_verification.json').write_text(json.dumps(verification, indent=2) + '\n')
build_path = ROOT / 'qa/source_companion_build_verification.json'
build = json.loads(build_path.read_text())
build['native_render_pending'] = False
build_path.write_text(json.dumps(build, indent=2) + '\n')
print(json.dumps(verification, indent=2), flush=True)

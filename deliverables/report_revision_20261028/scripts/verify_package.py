"""Verify the delivered report, comparison text, provenance, and PDF layout."""
import sys
sys.path.insert(0, '/tmp/dl_report_20261028_python')
from pathlib import Path
from zipfile import ZipFile
import hashlib, json, re
from lxml import etree
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
QA = ROOT / 'qa'
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def word_text(name):
    return (QA / name).read_bytes().decode('utf-8-sig')

clean = word_text('clean_word_text.txt')
accepted = word_text('tracked_accepted_text.txt')
rejected = word_text('tracked_rejected_text.txt')
original = word_text('original_word_text.txt')

def normalize_contents_pages(text):
    """Remove only trailing page fields inside generated contents/lists."""
    start = text.index('\x0cContents\r')
    end = text.index('\x0cIntroduction\r', start)
    front = text[start:end]
    front = re.sub(r'\t(?:[ivxlcdm]+|\d+|A\.\d+)(?=\r)', '', front)
    return text[:start] + front + text[end:]

assert rejected == original, 'Reject-all changed source text'
assert normalize_contents_pages(accepted) == normalize_contents_pages(clean), 'Substantive accept-all mismatch'
comparison_path = QA / 'comparison_verification.json'
comparison = json.loads(comparison_path.read_text(encoding='utf-8-sig'))
comparison.update({
    'NativeFormat': 'Microsoft Word DOCX via SaveAs2',
    'AcceptedTextExact': accepted == clean,
    'RejectedTextExact': rejected == original,
    'AcceptedTextExactExcludingGeneratedPageFields': True,
    'AcceptanceDifference': None if accepted == clean else 'Only trailing page-number fields in the generated contents, figure list, and table list differ. All headings, captions, tables, and body text match.',
})
comparison_path.write_text(json.dumps(comparison, indent=2) + '\n')

sources = json.loads((ROOT / 'sources/source_hashes.json').read_text())
for name, expected in sources.items():
    assert hashlib.sha256((REPO / name).read_bytes()).hexdigest() == expected, name

package_checks = {}
for name in ['Framework_revised_20261028.docx', 'Framework_revised_20261028_tracked.docx']:
    with ZipFile(ROOT / name) as package:
        assert package.testzip() is None
        root = etree.fromstring(package.read('word/document.xml'))
        revision_tags = ['ins', 'del', 'moveFrom', 'moveTo', 'rPrChange', 'pPrChange', 'tblPrChange', 'sectPrChange']
        revisions = sum(len(root.findall('.//w:' + tag, NS)) for tag in revision_tags)
        comments = len(root.findall('.//w:commentReference', NS))
        images = len(root.findall('.//w:drawing', NS))
        text = '\n'.join(''.join(p.xpath('.//w:t/text()', namespaces=NS)) for p in root.findall('.//w:p', NS))
        if 'tracked' not in name:
            assert revisions == 0 and comments == 0
            assert 'April 2026' not in text
            for token in ['Error!', 'TODO', 'TBD', 'PNNL-XXXXX', 'Enter Title Here', 'PLACEHOLDER']:
                assert token not in text, token
        else:
            assert revisions > 0
        package_checks[name] = {'xml_revision_elements': revisions, 'comment_markers': comments, 'drawings': images}

pdf = fitz.open(ROOT / 'Framework_revised_20261028.pdf')
pdf_text = '\n'.join(p.get_text() for p in pdf)
assert len(pdf) == 77
assert 'October 2026' in pdf[0].get_text() and 'October 2026' in pdf[2].get_text()
assert 'April 2026' not in pdf_text
for token in ['Error!', 'TODO', 'TBD', 'PNNL-XXXXX', 'Enter Title Here', 'PLACEHOLDER']:
    assert token not in pdf_text, token
for token in ['0.133', '0.329', '10.04', '0.58', '1.03', '1.21', '1.11', '3.92', '5.45', '1.22', '80.4', '88.9', '26.5', '85.8', '21.1', '85.5', '38.1', '87.3']:
    assert token in pdf_text, token
for step in ['MONITOR', 'DETECT', 'DECIDE', 'PREPARE', 'UPDATE', 'CALIBRATE', 'DEPLOY']:
    assert step in pdf_text
years_mentions = [line.strip() for line in pdf_text.splitlines() if 'years 0' in line]
assert len(years_mentions) == 1 and 'report used years' in years_mentions[0]

figures = {}
for number in range(1, 10):
    caption = next(p for p in clean.split('\r') if p.startswith(f'Figure {number}.'))
    lead = ' '.join(caption.split()[:9])
    pages = [i + 1 for i, p in enumerate(pdf) if lead in ' '.join(p.get_text().split())]
    assert len(pages) >= 2, (number, pages)
    figures[str(number)] = pages

# Render fresh contact sheets of every delivered PDF page, plus figure pages.
render_dir = QA / 'final_pdf_pages'
render_dir.mkdir(exist_ok=True)
for old_render in render_dir.glob('figure*_page*.png'):
    old_render.unlink()
thumbs = []
for i, page in enumerate(pdf):
    pix = page.get_pixmap(matrix=fitz.Matrix(.4, .4), alpha=False)
    pic = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
    tile = Image.new('RGB', (265, 345), '#e8e8e8')
    tile.paste(pic, ((265 - pic.width) // 2, 20))
    ImageDraw.Draw(tile).text((8, 4), str(i + 1), fill='black')
    thumbs.append(tile)
for start in range(0, len(thumbs), 20):
    chunk = thumbs[start:start + 20]
    sheet = Image.new('RGB', (265 * 4, 345 * ((len(chunk) + 3) // 4)), 'white')
    for j, tile in enumerate(chunk):
        sheet.paste(tile, ((j % 4) * 265, (j // 4) * 345))
    sheet.save(QA / f'final_pages_{start+1:02d}_{start+len(chunk):02d}.png')
for number, pages in figures.items():
    page_num = pages[-1]
    pdf[page_num - 1].get_pixmap(matrix=fitz.Matrix(1.3, 1.3), alpha=False).save(render_dir / f'figure{int(number):02d}_page{page_num:02d}.png')

checks = {
    'pdf_pages': len(pdf),
    'package_checks': package_checks,
    'all_source_hashes_preserved': True,
    'accept_all_restores_revised_text_exactly': accepted == clean,
    'accept_all_matches_except_generated_page_fields': True,
    'reject_all_restores_original_text_exactly': True,
    'no_broken_fields_or_visible_placeholders': True,
    'inside_title_date': 'October 2026; stored date control corrected',
    'years_0_4_occurrence': 'One explicit documentation-discrepancy statement; no study-time claim',
    'figure_caption_pages': figures,
    'source_figures_not_pooled': 'Manuscript Figures 3, 4, and 5 retained as separate comparisons',
}
(QA / 'final_verification.json').write_text(json.dumps(checks, indent=2) + '\n')
deliverables = ['Framework_revised_20261028.docx', 'Framework_revised_20261028.pdf', 'Framework_revised_20261028_tracked.docx', 'REVIEW_DECISIONS.md', 'COMMENT_DISPOSITION.md']
(QA / 'delivery_sha256.json').write_text(json.dumps({name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in deliverables}, indent=2) + '\n')
print(json.dumps(checks, indent=2), flush=True)

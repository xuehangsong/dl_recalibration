"""Check native slide output and record deliverable/source integrity."""
from pathlib import Path
import sys
sys.path.insert(0, '/tmp/dl_slides_20261029_python')
import hashlib, json
from zipfile import ZipFile
import pymupdf
from PIL import Image, ImageOps, ImageDraw
import numpy as np
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
pdf=pymupdf.open(ROOT/'Updated_case_study_20261029_v2.pdf')
prs=Presentation(ROOT/'Updated_case_study_20261029_v2.pptx')
assert len(pdf)==len(prs.slides)==7
native=json.loads((ROOT/'qa/powerpoint_verification.json').read_text(encoding='utf-8-sig'))
assert native['NativePowerPointOpen'] and native['Slides']==7
assert all(r['Pictures']==1 and not r['TextOverflowShapes'] for r in native['SlideChecks'])
slide_checks=[]
for i,(slide,page) in enumerate(zip(prs.slides,pdf),1):
    assert sum(s.shape_type==MSO_SHAPE_TYPE.PICTURE for s in slide.shapes)==1
    assert len(slide.notes_slide.notes_text_frame.text)>300
    assert len(page.get_images())>=1
    title=next(s.text for s in slide.shapes if s.has_text_frame and len(s.text)>45)
    assert ' '.join(title.split()) in ' '.join(page.get_text().split())
    for forbidden in ['TODO','TBD','Missing image','Choose an item.','Error!']:
        assert forbidden not in page.get_text()
    slide_checks.append({'slide':i,'one_picture':True,'title_rendered':True,'notes_present':True})

source_hashes=json.loads((ROOT/'sources/input_sha256.json').read_text())
for name,expected in source_hashes.items():
    if name.startswith('manuscript/embedded_figure'):
        continue
    assert hashlib.sha256((REPO/name).read_bytes()).hexdigest()==expected,name

crop_record=json.loads((ROOT/'sources/spatial_crop.json').read_text())
source_image=Image.open(REPO/crop_record['source']).convert('RGB')
expected_crop=source_image.crop(crop_record['crop_box_ltrb'])
delivered_crop=Image.open(ROOT/'figures/03_rare_spatial_example.png').convert('RGB')
assert np.array_equal(np.asarray(expected_crop),np.asarray(delivered_crop))
slide3=prs.slides[2]
pic=next(s for s in slide3.shapes if s.shape_type==MSO_SHAPE_TYPE.PICTURE)
assert abs(pic.width/pic.height-delivered_crop.width/delivered_crop.height)<1e-5

tiles=[]
for i in range(1,8):
    path=ROOT/f'previews/Slide{i}.PNG'
    im=Image.open(path).convert('RGB')
    assert im.size==(1600,900)
    im.thumbnail((640,360))
    tile=Image.new('RGB',(664,395),'#e9edf0')
    tile.paste(im,(12,24));ImageDraw.Draw(tile).text((12,6),str(i),fill='#253b4b')
    tiles.append(tile)
sheet=Image.new('RGB',(1328,1580),'white')
for i,tile in enumerate(tiles):sheet.paste(tile,((i%2)*664,(i//2)*395))
sheet.save(ROOT/'previews/contact_sheet.png')

delivery=['Updated_case_study_20261029_v2.pptx','Updated_case_study_20261029_v2.pdf','speaker_notes.md','FIGURE_AUDIT.md']
(ROOT/'qa/delivery_sha256.json').write_text(json.dumps({p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in delivery},indent=2)+'\n')
result={'slides':7,'native_powerpoint_rendered':True,'pdf_pages':len(pdf),'one_image_per_slide':True,
        'embedded_notes_verified':True,'text_overflow':False,'source_files_unchanged':True,
        'spatial_crop_pixel_exact':True,'spatial_crop_aspect_ratio_preserved':True,
        'previous_deck_and_frozen_report_preserved':True,
        'slide_checks':slide_checks}
(ROOT/'qa/final_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)

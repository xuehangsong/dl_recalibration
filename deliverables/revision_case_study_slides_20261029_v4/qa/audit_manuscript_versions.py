from pathlib import Path
from zipfile import ZipFile, BadZipFile
from hashlib import sha256
from xml.etree import ElementTree as ET
import json,re,difflib
O = Path(__file__).resolve().parent
R = O.parents[2]
manuscript_dirs = [R / 'method_manuscript', R / 'archive/20261118_superseded/method_manuscript']
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}';A='{http://schemas.openxmlformats.org/drawingml/2006/main}';REL='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}';PK='{http://schemas.openxmlformats.org/package/2006/relationships}'
def txt(e):
 if e.tag in [W+'del',W+'moveFrom',W+'instrText']:return ''
 if e.tag==W+'t':return e.text or ''
 if e.tag==W+'tab':return ' '
 return ''.join(txt(c) for c in e)
def media_info(z,n):return {'member':n,'bytes':len(z.read(n)),'sha256':sha256(z.read(n)).hexdigest()}
def scan(p):
 rec={'file':str(p.relative_to(R)),'file_sha256':sha256(p.read_bytes()).hexdigest()}
 with ZipFile(p) as z:
  rec['media']=[media_info(z,n) for n in z.namelist() if n.startswith('word/media/')]
  rec['charts']=[n for n in z.namelist() if n.startswith('word/charts/')]
  root=ET.fromstring(z.read('word/document.xml'));parents={c:e for e in root.iter() for c in e}
  rels=ET.fromstring(z.read('word/_rels/document.xml.rels'));relmap={x.get('Id'):x.get('Target') for x in rels}
  media_hash={x['member']:x['sha256'] for x in rec['media']};caps=[];refs=[]
  for i,pn in enumerate(root.iter(W+'p'),1):
   ancestors=[];cur=pn
   while cur in parents:cur=parents[cur];ancestors.append(cur.tag)
   if W+'del' in ancestors or W+'moveFrom' in ancestors:continue
   t=' '.join(txt(pn).split())
   for b in pn.iter(A+'blip'):
    rr=b.get(REL+'embed');target=relmap.get(rr,'');mem='word/'+target if target and not target.startswith('/') else target.lstrip('/')
    refs.append({'paragraph':i,'target':mem,'sha256':media_hash.get(mem)})
   ma=re.match(r'^Figure\s+([1-5])\s*[.:]',t)
   if ma:caps.append({'figure':int(ma.group(1)),'paragraph':i,'text':t})
  rec['accepted_figure_captions']=caps;rec['document_image_references']=refs
 return rec
recs=[]
for directory in manuscript_dirs:
    for p in sorted(directory.glob('*.docx')):
        if p.name.startswith('~$'):
            continue
        try:
            recs.append(scan(p))
        except Exception as e:
            recs.append({'file': str(p.relative_to(R)), 'error': str(e)})
base=next(x for x in recs if x['file'].endswith('/Adaptive_Replay_Manuscript_2026_09_09.docx'))
bmap={int(re.search(r'image([1-5])\.',x['member']).group(1)):x['sha256'] for x in base['media'] if re.search(r'image([1-5])\.',x['member'])}
bcaps={x['figure']:x['text'] for x in base['accepted_figure_captions']}
for x in recs:
 if 'error'in x:continue
 hs={v['sha256'] for v in x['media']};x['baseline_figures_present_byte_identical']={str(i):h in hs for i,h in bmap.items()};x['all_five_figures_byte_identical']=all(x['baseline_figures_present_byte_identical'].values())
 x['extra_media_hashes']=sorted(hs-set(bmap.values()))
 cc={v['figure']:v['text'] for v in x['accepted_figure_captions']}
 x['caption_identity']={str(i):cc.get(i)==t for i,t in bcaps.items()}
 x['caption_differences']={str(i):{'base':t,'variant':cc.get(i),'diff':list(difflib.ndiff([t],[cc.get(i,'<absent>')]))} for i,t in bcaps.items() if cc.get(i)!=t}
out={'audit_date':'2026-10-29','scope':'All22 nonlock DOCX files across method_manuscript and archive/20261118_superseded/method_manuscript; empirical image hashes and accepted-view Figure1–5 captions only. No conclusion based on filenames or modified dates.','baseline':base['file'],'baseline_figure_sha256':bmap,'files':recs,'summary':{'files_scanned':len(recs),'all_five_figures_identical_count':sum(x.get('all_five_figures_byte_identical',False) for x in recs),'files_with_different_or_missing_figures':[x['file'] for x in recs if not x.get('all_five_figures_byte_identical',False)],'files_with_caption_differences':[x['file'] for x in recs if x.get('caption_differences')]}}
(O/'manuscript_version_figure_lineage.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out['summary'],indent=2))
for x in recs:
 print(Path(x['file']).name,len(x.get('media',[])),x.get('all_five_figures_byte_identical'),list(x.get('caption_differences',{})),len(x.get('extra_media_hashes',[])))

from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,'/tmp/dl_slides_20261029_python')
from lxml import etree
from zipfile import ZipFile
src=Path('method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx')
out=Path('deliverables/revision_case_study_slides_20261029_v3/sources')
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
W='{'+ns['w']+'}'; M='{'+ns['m']+'}'
def name(e):return etree.QName(e).localname

def txt(e):
 if e is None:return ""
 if e.tag in [W+'del',W+'moveFrom',W+'instrText']:return ''
 if e.tag in [W+'t',M+'t']:return e.text or ''
 if e.tag==W+'tab':return '\t'
 if e.tag in [W+'br',W+'cr']:return '\n'
 if e.tag==M+'f':return '('+txt(e.find(M+'num'))+')/('+txt(e.find(M+'den'))+')'
 if e.tag==M+'sSub':return txt(e.find(M+'e'))+'_{'+txt(e.find(M+'sub'))+'}'
 if e.tag==M+'sSup':return txt(e.find(M+'e'))+'^{'+txt(e.find(M+'sup'))+'}'
 if e.tag==M+'sSubSup':return txt(e.find(M+'e'))+'_{'+txt(e.find(M+'sub'))+'}^{'+txt(e.find(M+'sup'))+'}'
 if e.tag==M+'rad':return 'sqrt('+txt(e.find(M+'e'))+')'
 if e.tag==M+'d':return '('+''.join(txt(c) for c in e if c.tag==M+'e')+')'
 if e.tag==M+'nary':
  chars=e.xpath('./m:naryPr/m:chr/@m:val',namespaces=ns)
  return (chars[0] if chars else 'SUM')+'_{'+txt(e.find(M+'sub'))+'}^{'+txt(e.find(M+'sup'))+'}('+txt(e.find(M+'e'))+')'
 if e.tag==M+'acc':
  chars=e.xpath('./m:accPr/m:chr/@m:val',namespaces=ns)
  return 'accent['+(''.join(chars))+']('+txt(e.find(M+'e'))+')'
 if e.tag==M+'bar':return 'bar('+txt(e.find(M+'e'))+')'
 return ''.join(txt(c) for c in e)
with ZipFile(src) as z:
 root=etree.fromstring(z.read('word/document.xml'))
 rels=etree.fromstring(z.read('word/_rels/document.xml.rels'))
 relmap={r.get('Id'):r.get('Target') for r in rels}
 records=[];eqs=[]
 for i,p in enumerate(root.xpath('./w:body//w:p',namespaces=ns),1):
  if p.xpath('ancestor::w:del|ancestor::w:moveFrom',namespaces=ns):continue
  st=p.xpath('./w:pPr/w:pStyle/@w:val',namespaces=ns)
  anchor=f'P{i:04d}';text=txt(p)
  tables=p.xpath('ancestor::w:tbl',namespaces=ns)
  images=p.xpath('.//a:blip/@r:embed',namespaces=ns)
  rec={'anchor':anchor,'style':st,'table':bool(tables),'text':text,'images':[relmap.get(x,x) for x in images]}
  for m in p.xpath('.//m:oMath[not(ancestor::w:del) and not(ancestor::w:moveFrom)]',namespaces=ns):
   eqs.append({'paragraph':anchor,'linear':txt(m),'xml':etree.tostring(m,encoding='unicode')})
  records.append(rec)
 (out/'manuscript_accepted_paragraphs.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
 (out/'manuscript_equations.json').write_text(json.dumps(eqs,indent=2,ensure_ascii=False)+'\n')
 lines=[f'SOURCE: {src}\nSHA256: {hashlib.sha256(src.read_bytes()).hexdigest()}\nAccepted view: w:del and w:moveFrom excluded; insertions retained. Mathematical notation linearized from OMML.\n']
 for r in records:
  if r['text'].strip() or r['images']:
   lines.append('['+r['anchor']+'] '+('TABLE ' if r['table'] else '')+('STYLE='+','.join(r['style'])+' ' if r['style'] else '')+r['text']+(' [IMAGES: '+','.join(r['images'])+']' if r['images'] else ''))
 (out/'manuscript_accepted_full.txt').write_text('\n\n'.join(lines)+'\n')
 print('paragraphs',len(records),'equations',len(eqs),'tables',len(root.xpath('./w:body//w:tbl',namespaces=ns)))

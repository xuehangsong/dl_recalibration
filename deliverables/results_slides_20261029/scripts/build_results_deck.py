"""Build a seven-slide internal-results deck from audited reported aggregates."""
from pathlib import Path
import sys
sys.path.insert(0, '/tmp/dl_slides_20261029_python')
import csv, hashlib, importlib.util, json, math, shutil
from zipfile import ZipFile
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
REPORT = REPO / 'deliverables/report_revision_20261028'
ANALYSIS = REPO / 'analyses/seven_step_lifecycle_20261007'
for folder in ['figures', 'sources', 'qa']:
    (ROOT / folder).mkdir(exist_ok=True)

def rows(path):
    with path.open(newline='') as stream:
        return list(csv.DictReader(stream))

f4 = rows(ANALYSIS / 'derived/figure4_metric_values.csv')
f5 = rows(ANALYSIS / 'derived/figure5_controller_values.csv')
expected_rmse = [[.58,10.04], [1.11,3.92], [1.03,1.21], [5.45,1.22]]
assert [[float(r['historical_rmse']), float(r['rare_rmse'])] for r in f4] == expected_rmse
assert [(float(r['historical_degradation_percent']), float(r['rare_improvement_percent'])) for r in f5] == [(80.4,88.9),(26.5,85.8),(21.1,85.5),(38.1,87.3)]
assert [r['method'] for r in f4] == ['Baseline','Simple_FT','Fixed_replay','EWC']
report_text = (REPORT / 'section5_20261028.md').read_text()
for values in expected_rmse:
    assert all(f'{value:.2f}' in report_text for value in values)
for r in f5:
    for key in ['historical_degradation_percent','rare_improvement_percent']:
        assert r[key] in report_text

inputs = [REPORT / 'Framework_revised_20261028.docx', REPORT / 'Framework_revised_20261028.pdf',
          REPORT / 'section5_20261028.md', REPORT / 'REVIEW_DECISIONS.md',
          REPO / 'method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx',
          REPO / 'drafts/final/section5_FINAL_20261008_FROZEN.md',
          ANALYSIS / 'derived/figure4_metric_values.csv', ANALYSIS / 'derived/figure5_controller_values.csv',
          ANALYSIS / 'derived/figure5_acceptance_margins.csv']
hashes = {str(p.relative_to(REPO)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
assert hashes['drafts/final/section5_FINAL_20261008_FROZEN.md'] == 'ea4075935fced71a3abc39954f4de15fde04cbb3803537edaad40ac793aba563'
with ZipFile(inputs[4]) as source:
    for number in [4,5]:
        embedded = source.read(f'word/media/image{number}.png')
        archived = (ANALYSIS / f'source_extracts/embedded_figures/image{number}.png').read_bytes()
        assert hashlib.sha256(embedded).hexdigest() == hashlib.sha256(archived).hexdigest()
        hashes[f'manuscript/embedded_figure{number}.png'] = hashlib.sha256(embedded).hexdigest()
for path in inputs[-3:]:
    shutil.copy2(path, ROOT / 'sources' / path.name)
(ROOT / 'sources/input_sha256.json').write_text(json.dumps(hashes, indent=2) + '\n')

INK, BLUE, ORANGE, TEAL, PURPLE, GREY = '#1f2d3a','#27688a','#c57732','#247f79','#806397','#7d858d'
LIGHT, GRID = '#eaf0f3','#e3e8eb'
METHOD_COLORS = [GREY, ORANGE, BLUE, PURPLE]
METHODS = ['Baseline', 'Simple fine-tuning', 'Fixed replay', 'EWC']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'axes.labelsize':17,
    'xtick.labelsize':15,'ytick.labelsize':17,'axes.edgecolor':'#8a9299',
    'axes.spines.top':False,'axes.spines.right':False,'axes.linewidth':.8,
    'text.color':INK,'axes.labelcolor':INK,'xtick.color':INK,'ytick.color':INK,
    'figure.facecolor':'white','savefig.facecolor':'white','pdf.fonttype':42,'svg.fonttype':'none'})
figure_audit = []

def save(fig, name, source, treatment):
    assert not any(ax.get_title() for ax in fig.axes), 'No overarching figure titles'
    assert getattr(fig, '_suptitle', None) is None
    for ext in ['png','svg','pdf']:
        fig.savefig(ROOT / f'figures/{name}.{ext}', dpi=220, facecolor='white')
    figure_audit.append({'figure':name,'source':source,'treatment':treatment})
    plt.close(fig)

def tidy(ax):
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='y',length=0,pad=10)
    ax.xaxis.grid(True,color=GRID,lw=.75)
    ax.set_axisbelow(True)

# One result per visual. Values remain the rounded labels from the source.
fig, ax = plt.subplots(figsize=(12,4.65))
fig.subplots_adjust(left=.18,right=.93,top=.90,bottom=.20)
values = [.58,10.04]
ax.barh([1,0],values,color=[BLUE,ORANGE],height=.46)
ax.set_yticks([1,0],['Historical','Rare'])
ax.set_xlim(0,11.6);ax.set_xticks([0,2,4,6,8,10]);ax.set_xlabel('Baseline RMSE (µg/L)',labelpad=12)
for y,v in zip([1,0],values):ax.text(v+.18,y,f'{v:.2f}',va='center',fontsize=23,fontweight='bold')
tidy(ax)
save(fig,'01_baseline','Manuscript Fig. 4; revised report §5.2','Replot two baseline aggregates on a common zero-based axis; derive 17.3× as 10.04/0.58. No uncertainty bars invented.')

fig, axes = plt.subplots(1,2,figsize=(12,4.65),sharey=True)
fig.subplots_adjust(left=.20,right=.96,top=.94,bottom=.21,wspace=.27)
for ax,key,limit,ticks,label in zip(axes,['historical_rmse','rare_rmse'],[6.35,11.6],[[0,2,4,6],[0,2,4,6,8,10]],['Historical RMSE (µg/L)','Rare RMSE (µg/L)']):
    values=[float(r[key]) for r in f4]
    ax.barh(np.arange(4),values,color=METHOD_COLORS,height=.55)
    ax.set_yticks(np.arange(4),METHODS);ax.set_xlim(0,limit);ax.set_xticks(ticks);ax.set_xlabel(label,labelpad=12)
    for y,v in enumerate(values):ax.text(v+limit*.025,y,f'{v:.2f}',va='center',fontsize=17,fontweight='bold' if y==2 else 'normal')
    tidy(ax)
axes[0].invert_yaxis();axes[1].tick_params(labelleft=False)
save(fig,'02_rmse_comparison','Manuscript Fig. 4; revised report Table 10','Two panels make historical errors readable. Both start at zero; different numerical limits are explicit. No Figure 5 controller values are pooled.')

fig, axes = plt.subplots(1,3,figsize=(12,4.65),sharey=True)
fig.subplots_adjust(left=.20,right=.975,top=.94,bottom=.23,wspace=.30)
for ax,key,limit,ticks,label in zip(axes,['rare_mass_error','rare_peak_error','rare_mass90_error'],[38,17,8.6],[[0,10,20,30],[0,5,10,15],[0,2,4,6,8]],['Plume-mass error (%)','Peak error (%)','Mass90 error (%)']):
    values=[float(r[key]) for r in f4]
    ax.barh(np.arange(4),values,color=METHOD_COLORS,height=.55)
    ax.set_yticks(np.arange(4),METHODS);ax.set_xlim(0,limit);ax.set_xticks(ticks);ax.set_xlabel(label,labelpad=12,fontsize=15)
    for y,v in enumerate(values):ax.text(v+limit*.035,y,f'{v:.2f}',va='center',fontsize=15,fontweight='bold' if y==2 else 'normal')
    tidy(ax)
axes[0].invert_yaxis()
save(fig,'03_rare_plume_metrics','Manuscript Fig. 4; revised report Table 11','Replot only the three unambiguous rare-regime metrics. Omit the inconsistent historical peak/Mass90 label. All axes start at zero; exact metric normalization still needs code.')

fig, ax = plt.subplots(figsize=(12,4.65))
fig.subplots_adjust(left=.12,right=.975,top=.93,bottom=.20)
ax.add_patch(Rectangle((0,85),30,5,facecolor=TEAL,alpha=.08,edgecolor='none'))
ax.axvline(30,color=GREY,ls='--',lw=1.25);ax.axhline(85,color=GREY,ls='--',lw=1.25)
names=['Fixed replay','Threshold adaptive','Loss-balanced','Loss-balanced + floor']
colors=[BLUE,TEAL,PURPLE,ORANGE];markers=['s','o','^','D']
label_positions=[(69,87.9),(34,83.7),(5,86.2),(43,87.4)]
align=['left','left','left','left']
for r,name,color,marker,label_position,ha in zip(f5,names,colors,markers,label_positions,align):
    x=float(r['historical_degradation_percent']);y=float(r['rare_improvement_percent'])
    ax.scatter(x,y,s=145,c=color,marker=marker,edgecolors='white',linewidths=1.2,zorder=5)
    ax.annotate(f'{name}\n({x:.1f}, {y:.1f})',(x,y),xytext=label_position,textcoords='data',ha=ha,va='center',fontsize=14,color=INK,
                arrowprops={'arrowstyle':'-','color':color,'lw':.8,'shrinkA':6,'shrinkB':9})
ax.set_xlim(0,90);ax.set_ylim(80,90);ax.set_xticks([0,15,30,45,60,75,90]);ax.set_yticks([80,82,84,85,86,88,90])
ax.set_xlabel('Historical RMSE increase (%)',labelpad=10);ax.set_ylabel('Rare RMSE reduction (%)',labelpad=10)
ax.grid(color=GRID,lw=.6);ax.set_axisbelow(True)
save(fig,'04_controller_screen','Manuscript Fig. 5; revised report Table 9','Replot all four controller outcomes and the illustrative 30%/85% region. Direct labels replace a distant legend. The y-axis range is explicit; this is a screening plot, not deployment evidence.')

passed=[r for r in f5 if r['passes_figure5_region']=='YES']
margins=[float(r['rare_improvement_percent'])-85 for r in passed]
assert np.allclose(margins,[.8,.5])
fig,ax=plt.subplots(figsize=(12,4.65))
fig.subplots_adjust(left=.25,right=.93,top=.90,bottom=.23)
ax.barh([1,0],margins,color=[TEAL,PURPLE],height=.46)
ax.set_yticks([1,0],['Threshold adaptive','Loss-balanced']);ax.set_xlim(0,1.0);ax.set_xticks(np.arange(0,1.01,.2))
ax.set_xlabel('Margin above the 85% rare-improvement requirement\n(percentage points)',labelpad=12,fontsize=16)
for y,v in zip([1,0],margins):ax.text(v+.025,y,f'+{v:.1f}',va='center',fontsize=23,fontweight='bold')
tidy(ax)
save(fig,'05_acceptance_margins','Manuscript Fig. 5; derived/figure5_acceptance_margins.csv','Subtract 85 from each passing reported rare-improvement label. This is arithmetic on rounded aggregate values, not an uncertainty or significance estimate.')

historical_change=(1.03/.58-1)*100
rare_change=(1-1.21/10.04)*100
fig,ax=plt.subplots(figsize=(12,4.65));ax.set_xlim(0,12);ax.set_ylim(0,4.65);ax.axis('off')
for x,label in [(6.7,'Historical RMSE\nincrease (%)'),(10.0,'Rare RMSE\nreduction (%)')]:ax.text(x,3.9,label,ha='center',va='center',fontsize=19)
for y,label,values,color in [(2.65,'RMSE comparison\nManuscript Fig. 4',[historical_change,rare_change],BLUE),(1.2,'Controller comparison\nManuscript Fig. 5',[80.4,88.9],TEAL)]:
    ax.add_patch(Rectangle((.6,y-.57),10.8,1.14,facecolor='#f1f5f7',edgecolor='none'))
    ax.text(.85,y,label,ha='left',va='center',fontsize=20,color=color)
    for x,value in zip([6.7,10.0],values):ax.text(x,y,f'{value:.1f}',ha='center',va='center',fontsize=34,fontweight='bold',color=color)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
save(fig,'06_comparison_provenance','Manuscript Figs. 4 and 5; revised report §5.6','Display the fixed-replay percentages separately: Fig. 4 is calculated from rounded RMSE labels; Fig. 5 is directly reported. Do not silently reconcile the discrepancy.')

fig,ax=plt.subplots(figsize=(12,4.65));ax.set_xlim(0,12);ax.set_ylim(0,4.65);ax.axis('off')
def box(x,y,w,h,text,color,fill='white',dashed=False):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=.025,rounding_size=.08',facecolor=fill,edgecolor=color,lw=1.6,linestyle='--' if dashed else '-'))
    ax.text(x,y,text,ha='center',va='center',fontsize=17,color=color)
def arrow(start,end,color=GREY):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=15,lw=1.3,color=color))
box(1.75,3.2,2.6,.85,'Threshold adaptive',TEAL,'#eef6f4')
box(1.75,1.5,2.6,.85,'Loss-balanced',PURPLE,'#f4f0f7')
arrow((3.08,3.2),(4.1,2.35));arrow((3.08,1.5),(4.1,2.35))
for x,label in [(5.15,'Uncertainty\ncalibration'),(7.9,'Untouched\nfinal test'),(10.65,'Promotion\nreview')]:
    box(x,2.35,2.05,1.22,label,GREY,dashed=True)
arrow((6.22,2.35),(6.82,2.35));arrow((8.97,2.35),(9.57,2.35))
ax.plot([.58,.95],[.3,.3],color=BLUE,lw=2);ax.text(1.08,.3,'Reported candidates',va='center',fontsize=14)
ax.plot([4.35,4.72],[.3,.3],color=GREY,lw=2,ls='--');ax.text(4.85,.3,'Required evidence / review',va='center',fontsize=14)
fig.subplots_adjust(left=0,right=1,bottom=.05,top=.98)
save(fig,'07_candidate_status','Revised report §§5.7–5.9; no calibration or final-test record supplied','Diagram of the supported endpoint. Solid candidate nodes reflect the illustrative screen only; dashed nodes are pending requirements. No operational deployment is implied.')

slides = [
    dict(title='Baseline rare-regime RMSE is 17.3× historical RMSE',image='01_baseline',
         caption='Reported baseline: 0.58 µg/L on historical cases and 10.04 µg/L on rare cases.',
         source='Source: adaptive-replay manuscript, Fig. 4; revised report §5.2.',
         notes='Start with the reliability problem. The ratio is 10.04/0.58 = 17.31, calculated from rounded labels in the September 9, 2026 internal adaptive-replay manuscript. These are reported aggregate results, not a new training run or an independently reproduced test. The rare and historical subsets were selected by a retrospective Mass90 response score. They do not represent a prospective detector evaluation. The reported 128 × 100 grid and one to five wells describe the case-study setting; no physical time interval is asserted here.'),
    dict(title='Fixed replay recovers rare accuracy, with a historical cost',image='02_rmse_comparison',
         caption='Fixed replay: rare RMSE falls 87.9%; historical RMSE rises 77.6%.',
         source='Source: adaptive-replay manuscript, Fig. 4; revised report Table 10.',
         notes='Read the historical and rare panels together. Baseline: 0.58/10.04 µg/L; simple fine-tuning: 1.11/3.92; fixed replay: 1.03/1.21; EWC: 5.45/1.22. Fixed replay has lower RMSE in both regimes than simple fine-tuning or EWC in this comparison, but historical performance remains worse than the baseline. The percentages are calculated from these rounded values. Panel limits differ to preserve readability, and both axes start at zero. EWC means elastic weight consolidation. The full-network 0.64/0.99 pair from manuscript Figure 3 is excluded because its model/configuration identity and protocol equivalence remain unresolved. Do not merge Figure 5 controllers into this ranking.'),
    dict(title='Replay reduces three additional rare-plume error metrics',image='03_rare_plume_metrics',
         caption='Fixed replay reduces rare mass, peak, and Mass90 errors by 94.4%, 75.8%, and 73.4%.',
         source='Source: adaptive-replay manuscript, Fig. 4; revised report Table 11.',
         notes='These three panels remain within the same Figure 4 comparison. Fixed replay changes plume-mass error from 32.30% to 1.82%, peak-concentration error from 14.20% to 3.43%, and Mass90 error from 7.11% to 1.89%. EWC has slightly lower peak and Mass90 errors but much worse historical RMSE; this is why rare-regime metrics alone are insufficient. Values and metric names are reproduced from the unambiguous source panels. Exact normalization and aggregation still require metric-generation code. The historical plume-metric column is omitted because the source caption/prose and panel labels conflict. These aggregate errors do not establish performance at actual compliance wells.'),
    dict(title='Two controllers pass the illustrative 30% / 85% screen',image='04_controller_screen',
         caption='Screen: historical RMSE increase ≤30% and rare RMSE reduction ≥85%.',
         source='Source: adaptive-replay manuscript, Fig. 5; revised report Table 9.',
         notes='This is a separate controller comparison. Fixed replay: 80.4% historical increase and 88.9% rare reduction. Threshold adaptive forgetting: 26.5% and 85.8%. Loss-balanced: 21.1% and 85.5%. Loss-balanced with floor: 38.1% and 87.3%. The shaded upper-left region satisfies both illustrative conditions. Only threshold adaptive forgetting and loss-balanced satisfy them. A variant with a replay floor fails the historical limit, so a blanket claim that adaptive replay passes would be incorrect. The limits are illustrative rather than approved or preregistered deployment criteria. No uncertainty bars are available for the displayed aggregates.'),
    dict(title='The rare-improvement margins are only 0.5–0.8 points',image='05_acceptance_margins',
         caption='Margins use rounded reported values; repeated-run uncertainty is unavailable.',
         source='Source: manuscript Fig. 5; audited acceptance-margin calculations.',
         notes='For the two candidates, subtract the illustrative 85% rare-improvement threshold: 85.8 - 85 = 0.8 percentage points and 85.5 - 85 = 0.5. Their historical margins are 30 - 26.5 = 3.5 points and 30 - 21.1 = 8.9 points. The rare-side margins are small, which makes independent testing and repeated-run evaluation important. These numbers are deterministic arithmetic on rounded labels, not confidence intervals, significance tests, or proof that either result is unstable. No raw replicate-level predictions were supplied with the evidence package.'),
    dict(title='Keep the two reported comparisons separate',image='06_comparison_provenance',
         caption='Fixed replay appears in both comparisons, but the reported percentage pairs differ.',
         source='Source: manuscript Figs. 4 and 5; revised report §5.6.',
         notes='For fixed replay, Figure 4 rounded RMSE gives (1.03/0.58 - 1) × 100 = 77.6% historical increase and (1 - 1.21/10.04) × 100 = 87.9% rare reduction. Figure 5 reports 80.4% and 88.9%. Do not replace either pair or assume rounding explains the discrepancy. Executed configurations, evaluation partitions, denominators, seeds, and historical/new exposure are needed to reconcile the comparisons. The displayed adaptive replay trajectory reaches r = 0.8 for most of 100 epochs; without controller logs we do not re-create that curve. A matched fixed-ratio-0.8 comparison is still needed to isolate the contribution of adaptive scheduling. That is a limitation of the current results, not a new experiment shown here.'),
    dict(title='Two candidates remain awaiting independent validation',image='07_candidate_status',
         caption='Passing the illustrative screen does not establish calibrated uncertainty or deployment readiness.',
         source='Source: revised report §§5.7–5.9.',
         notes='The current result is a controlled offline update assessment that identifies two candidate controller outcomes under the illustrative screen. No independent uncertainty-calibration result, untouched final-test record, or versioned promotion decision accompanies these aggregates. The dashed stages show the evidence still required; they are not completed operations. The candidate names are controller outcomes, not verified production checkpoints. Before stronger claims, resolve trajectory partitions and figure-specific protocols, evaluate matched controls, calibrate uncertainty, and test independently. This deck stays focused on updated result interpretation and does not claim new training, prospective drift detection, active-learning gains, or field deployment.'),
]

# Reuse the established evidence-deck builder, then apply the result-only layout.
skill_script=Path('/home/song884/.codex/skills/evidence-deck-builder/scripts/build_evidence_deck.py')
loader=importlib.util.spec_from_file_location('evidence_deck_builder',skill_script)
builder=importlib.util.module_from_spec(loader);loader.loader.exec_module(builder)
spec={'title':'Updated U-Net / adaptive-replay results','footer':None,'slides':[]}
for item in slides:
    spec['slides'].append({'layout':'image','title':item['title'],'kicker':'Updated results · internal discussion',
        'image':str(ROOT / f"figures/{item['image']}.png"),'notes':item['notes']+'\n\n'+item['source']})
(ROOT/'deck_spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
output=ROOT/'Updated_results_20261029.pptx'
builder.build_deck(spec,output,ROOT/'speaker_notes.md')
prs=Presentation(output)
for i,(slide,item) in enumerate(zip(prs.slides,slides),1):
    # Keep the image, titles, and labels as independent editable slide objects.
    for shape in list(slide.shapes):
        if shape.shape_type != MSO_SHAPE_TYPE.PICTURE:
            shape._element.getparent().remove(shape._element)
    slide.background.fill.solid();slide.background.fill.fore_color.rgb=RGBColor(255,255,255)
    pic=next(s for s in slide.shapes if s.shape_type==MSO_SHAPE_TYPE.PICTURE)
    pic.left=Inches(.55);pic.top=Inches(1.50);pic.width=Inches(12.23);pic.height=Inches(4.74)
    pic.name='Key image — '+item['image']
    pic._element.nvPicPr.cNvPr.set('descr',item['caption'])
    builder.add_text(slide,'UPDATED RESULTS  /  INTERNAL DISCUSSION',Inches(.62),Inches(.32),Inches(11),Inches(.25),size=11,bold=True,color=RGBColor(39,104,138))
    title=builder.add_text(slide,item['title'],Inches(.62),Inches(.77),Inches(12.05),Inches(.78),size=27,bold=True,color=RGBColor(31,45,58))
    title.text_frame.word_wrap=True
    builder.add_text(slide,item['caption'],Inches(.65),Inches(6.48),Inches(12),Inches(.47),size=15,color=RGBColor(52,67,79))
    builder.add_text(slide,item['source'],Inches(.65),Inches(7.06),Inches(11.8),Inches(.22),size=10,color=RGBColor(105,114,122))
    builder.add_text(slide,str(i),Inches(12.42),Inches(7.06),Inches(.25),Inches(.22),size=10,color=RGBColor(105,114,122))
    for shape in slide.shapes:
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                for run in p.runs:run.font.name='Arial'
    slide.notes_slide.notes_text_frame.text=item['notes']+'\n\n'+item['source']+'\nSource report: deliverables/report_revision_20261028/Framework_revised_20261028.docx.\nNo new experiment or independent reproduction is represented.'
prs.core_properties.title='Updated U-Net / adaptive-replay results'
prs.core_properties.subject='Internal discussion of reported update evidence; October 29, 2026'
prs.core_properties.author='Xuehang Song'
prs.save(output)

check=Presentation(output)
assert len(check.slides)==7
for i,slide in enumerate(check.slides,1):
    assert sum(s.shape_type==MSO_SHAPE_TYPE.PICTURE for s in slide.shapes)==1
    assert len(slide.notes_slide.notes_text_frame.text)>300
    for s in slide.shapes:
        assert s.left>=0 and s.top>=0 and s.left+s.width<=check.slide_width and s.top+s.height<=check.slide_height,(i,s.name)
with ZipFile(output) as archive:assert archive.testzip() is None

(ROOT/'sources/figure_audit.json').write_text(json.dumps(figure_audit,ensure_ascii=False,indent=2)+'\n')
(ROOT/'qa/build_verification.json').write_text(json.dumps({'slides':7,'pictures_per_slide':1,
    'speaker_notes_embedded':True,'source_hashes_recorded':True,'manuscript_embedded_figures_match_archive':True,
    'all_slide_shapes_within_bounds':True,'metric_values_match_revised_section5':True,
    'figure_titles':False,'baseline_ratio':10.04/.58,'fixed_replay_fig4_percentages':[historical_change,rare_change],
    'passing_rare_margins_pp':margins},indent=2)+'\n')
print(f'Built {output}; 7 slides, one image each, embedded notes.',flush=True)

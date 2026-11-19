"""Scientific case-study deck: planned lifecycle, reported evidence, next test."""
from pathlib import Path
import sys, csv, json, hashlib, importlib.util, shutil
sys.path.insert(0, '/tmp/dl_slides_20261029_python')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from PIL import Image
from zipfile import ZipFile
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE_TYPE

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
REPORT=REPO/'deliverables/report_revision_20261028'
ANALYSIS=REPO/'analyses/seven_step_lifecycle_20261007'
STEM='Updated_case_study_20261029_v2'
for d in ['figures','sources','qa','previews']:(ROOT/d).mkdir(exist_ok=True)

def rows(path):
    with path.open(newline='') as f:return list(csv.DictReader(f))
f4=rows(ANALYSIS/'derived/figure4_metric_values.csv')
f5=rows(ANALYSIS/'derived/figure5_controller_values.csv')
assert [(float(r['historical_rmse']),float(r['rare_rmse'])) for r in f4]==[(.58,10.04),(1.11,3.92),(1.03,1.21),(5.45,1.22)]
assert [(float(r['historical_degradation_percent']),float(r['rare_improvement_percent'])) for r in f5]==[(80.4,88.9),(26.5,85.8),(21.1,85.5),(38.1,87.3)]
source_paths=[
    REPORT/'Framework_revised_20261028.docx',REPORT/'section5_20261028.md',
    REPO/'method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx',
    REPO/'drafts/final/section5_FINAL_20261008_FROZEN.md',
    REPO/'plans/handoffs/trigger_uq_prototype_workflow_handoff.md',
    ANALYSIS/'analysis_specification.md',ANALYSIS/'derived/figure4_metric_values.csv',
    ANALYSIS/'derived/figure5_controller_values.csv',
    REPO/'deliverables/results_slides_20261029/Updated_results_20261029.pptx',
]
hashes={str(p.relative_to(REPO)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}
assert hashes['drafts/final/section5_FINAL_20261008_FROZEN.md']=='ea4075935fced71a3abc39954f4de15fde04cbb3803537edaad40ac793aba563'
with ZipFile(source_paths[2]) as z:embedded=z.read('word/media/image2.png')
source_image=ANALYSIS/'source_extracts/embedded_figures/image2.png'
assert embedded==source_image.read_bytes()
hashes[str(source_image.relative_to(REPO))]=hashlib.sha256(embedded).hexdigest()
(ROOT/'sources/input_sha256.json').write_text(json.dumps(hashes,indent=2)+'\n')
for p in source_paths[6:8]:shutil.copy2(p,ROOT/'sources'/p.name)

INK='#23323c';BLUE='#286787';TEAL='#277e78';ORANGE='#ba773b';PURPLE='#806796';GREY='#77828b';GRID='#e2e7ea'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'axes.labelsize':17,'xtick.labelsize':14,'ytick.labelsize':14,
    'axes.spines.top':False,'axes.spines.right':False,'axes.linewidth':.8,'axes.edgecolor':'#7c878f','text.color':INK,
    'axes.labelcolor':INK,'xtick.color':INK,'ytick.color':INK,'figure.facecolor':'white','savefig.facecolor':'white',
    'pdf.fonttype':42,'svg.fonttype':'none'})
audit=[]
def canvas():
    fig,ax=plt.subplots(figsize=(12.5,4.6))
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax.set_xlim(0,12.5);ax.set_ylim(0,4.6);ax.axis('off')
    return fig,ax
def box(ax,x,y,w,h,label,color=GREY,fill='white',dashed=False,fs=15):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=.02,rounding_size=.035',
        facecolor=fill,edgecolor=color,lw=1.3,linestyle='--' if dashed else '-'))
    ax.text(x,y,label,ha='center',va='center',fontsize=fs,color=INK)
def arrow(ax,a,b,color=GREY,style='-|>'):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle=style,mutation_scale=13,lw=1,color=color))
def save(fig,name,source,treatment):
    assert fig._suptitle is None and all(not a.get_title() for a in fig.axes)
    for ext in ['png','svg','pdf']:fig.savefig(ROOT/f'figures/{name}.{ext}',dpi=220,facecolor='white')
    audit.append({'figure':name,'source':source,'treatment':treatment})
    plt.close(fig)

# 1. Evidence types are explicit; color does not mean that a lifecycle step is completed.
fig,ax=canvas()
steps=['MONITOR','DETECT','DECIDE','PREPARE','UPDATE','CALIBRATE','DEPLOY']
evidence=['Baseline\naggregates','Retrospective\nMass90','Illustrative\nscreen','Rare cases\n+ replay','Update\ncomparisons','Interval\ncalibration','Final test\n+ review']
xs=np.linspace(.93,11.57,7)
ax.text(.25,4.15,'Planned lifecycle',fontsize=16)
ax.text(.25,2.35,'Evidence in the revised case study',fontsize=16)
for i,(x,s,e) in enumerate(zip(xs,steps,evidence)):
    box(ax,x,3.45,1.5,.63,s,color=GREY,fs=11.5)
    if i<6:arrow(ax,(x+.77,3.45),(xs[i+1]-.77,3.45))
    color=BLUE if i in [0,3,4] else ORANGE if i in [1,2] else GREY
    box(ax,x,1.48,1.5,.95,e,color=color,fill='#f3f7f9' if i<5 else 'white',dashed=i>=5,fs=12)
    ax.plot([x,x],[3.1,2.85],color=GREY,lw=.8)
    ax.plot([x,x],[2.0,2.15],color=color,lw=.8)
for x,color,label,dash in [(.3,BLUE,'Reported offline evidence',False),(4.7,ORANGE,'Retrospective / illustrative',False),(9.1,GREY,'Still required',True)]:
    ax.plot([x,x+.45],[.38,.38],color=color,lw=2,ls='--' if dash else '-')
    ax.text(x+.57,.38,label,va='center',fontsize=11.5)
save(fig,'01_plan_and_evidence','Revised report §§2.2, 5.9','Align intended workflow with evidence types. Reported offline evidence is not the same as completed operational execution.')

# 2. Model and stress-selection dependencies. No invented plume or distribution.
fig,ax=canvas()
box(ax,1.3,3.37,2.05,.80,'Plume at t\n+ pumping input',BLUE,'#f3f7f9',fs=14)
box(ax,4.2,3.37,1.65,.80,'U-Net',BLUE,'#f3f7f9',fs=17)
box(ax,7.05,3.37,2.0,.80,'Predicted plume\nat t + 1',BLUE,'#f3f7f9',fs=14)
box(ax,10.65,3.37,2.05,.80,'Errors against\nreference',GREY,fs=14)
arrow(ax,(2.35,3.37),(3.34,3.37));arrow(ax,(5.04,3.37),(6.03,3.37));arrow(ax,(8.07,3.37),(9.60,3.37))
box(ax,1.35,1.13,2.15,.85,'Reference plumes\nat t and t + 1',GREY,fs=13)
box(ax,4.17,1.13,1.85,.85,'Mass90\nchange score',ORANGE,'#fbf7f1',fs=14)
box(ax,7.15,1.71,2.35,.72,'Historical: bottom 40%\ns ≤ 0.133',BLUE,'#f3f7f9',fs=11.5)
box(ax,7.15,.56,2.35,.72,'Rare: top 3%\ns ≥ 0.329',ORANGE,'#fbf7f1',fs=12)
box(ax,10.7,1.13,2.0,.85,'Controlled\nupdate',TEAL,'#f3f7f9',fs=14)
arrow(ax,(2.45,1.13),(3.22,1.13),ORANGE)
arrow(ax,(5.12,1.23),(5.95,1.67),BLUE);arrow(ax,(5.12,1.03),(5.95,.60),ORANGE)
arrow(ax,(8.34,1.71),(9.67,1.35),BLUE);arrow(ax,(8.34,.56),(9.67,.91),ORANGE)
ax.text(9.0,1.93,'replay',ha='center',fontsize=12,color=BLUE)
ax.text(9.0,.33,'learning',ha='center',fontsize=12,color=ORANGE)
save(fig,'02_controlled_stress_test','Revised report §§5.1–5.5','The pumping input uses Thiem preprocessing. The score requires the next reference plume and cannot provide prospective warning. Exact time units and executed partitions remain unresolved.')

# 3. Preserve all pixels/scales of one original scientific example; never infer arrays from colors.
crop_box=(950,600,1893,1259)
original=Image.open(source_image).convert('RGB')
assert original.size==(1893,1259)
crop=original.crop(crop_box)
crop.save(ROOT/'figures/03_rare_spatial_example.png')
crop.save(ROOT/'figures/03_rare_spatial_example.pdf',resolution=150)
(ROOT/'sources/spatial_crop.json').write_text(json.dumps({
    'source':str(source_image.relative_to(REPO)),'source_size':list(original.size),
    'crop_box_ltrb':list(crop_box),'modifications':'Crop only; all in-crop pixels, axes, labels, aspect ratio, and colorbars retained.',
    'source_caption_role':'Rare-regime full-order reference, static U-Net prediction, and prediction-minus-reference error.',
    'concentration_max_ugL':813.6,'signed_error_colorbar_limits_ugL':[-169.4,169.4],
    'raw_arrays_and_sample_id':'Not provided in the report evidence package'},indent=2)+'\n')
audit.append({'figure':'03_rare_spatial_example','source':'Manuscript Fig. 2(b), rare-regime triplet',
    'treatment':'Crop only. Preserve original color maps, axes, scale bars, and aspect ratio. Representative source example; no independent spatial reproduction.'})

# 4. Two performance objectives on the same plane; no invented training trajectory.
fig,ax=plt.subplots(figsize=(12.5,4.6));fig.subplots_adjust(left=.11,right=.95,top=.93,bottom=.20)
names=['Baseline','Simple fine-tuning','Fixed replay','EWC']
colors=[GREY,ORANGE,BLUE,PURPLE];markers=['o','s','D','^']
positions=[(1.0,10.0),(1.65,4.1),(1.60,1.45),(4.1,2.65)]
for r,name,color,marker,pos in zip(f4,names,colors,markers,positions):
    x=float(r['historical_rmse']);y=float(r['rare_rmse'])
    ax.scatter(x,y,s=150,c=color,marker=marker,edgecolors='white',lw=1.1,zorder=5)
    ax.annotate(f'{name}\n({x:.2f}, {y:.2f})',(x,y),xytext=pos,textcoords='data',fontsize=14,va='center',
        arrowprops={'arrowstyle':'-','color':color,'lw':.8,'shrinkA':7,'shrinkB':9})
ax.set_xlim(0,6.2);ax.set_ylim(0,11.3);ax.set_xticks([0,1,2,3,4,5,6]);ax.set_yticks([0,2,4,6,8,10])
ax.set_xlabel('Historical RMSE (µg/L)',labelpad=9);ax.set_ylabel('Rare RMSE (µg/L)',labelpad=9)
ax.grid(color=GRID,lw=.65);ax.set_axisbelow(True)
save(fig,'04_joint_rmse','Manuscript Fig. 4; revised report Table 10','Replot reported historical/rare RMSE pairs together. No connecting trajectory, replicate distribution, or uncertainty is invented.')

# 5. Separate controller protocol: preserve the illustrative two-condition screen.
fig,ax=plt.subplots(figsize=(12.5,4.6));fig.subplots_adjust(left=.11,right=.96,top=.93,bottom=.20)
ax.add_patch(Rectangle((0,85),30,5,facecolor=TEAL,alpha=.08,edgecolor='none'))
ax.axvline(30,color=GREY,ls='--',lw=1.2);ax.axhline(85,color=GREY,ls='--',lw=1.2)
labels=['Fixed replay','Threshold adaptive','Loss-balanced','Loss-balanced + floor']
colors=[BLUE,TEAL,PURPLE,ORANGE];markers=['s','o','^','D']
positions=[(68,87.8),(34,83.7),(4,86.1),(42,87.4)]
for r,label,color,marker,pos in zip(f5,labels,colors,markers,positions):
    x=float(r['historical_degradation_percent']);y=float(r['rare_improvement_percent'])
    ax.scatter(x,y,s=145,c=color,marker=marker,edgecolors='white',lw=1.1,zorder=5)
    ax.annotate(f'{label}\n({x:.1f}, {y:.1f})',(x,y),xytext=pos,textcoords='data',fontsize=13.5,va='center',
        arrowprops={'arrowstyle':'-','color':color,'lw':.8,'shrinkA':7,'shrinkB':9})
ax.set_xlim(0,90);ax.set_ylim(80,90);ax.set_xticks([0,15,30,45,60,75,90]);ax.set_yticks([80,82,84,85,86,88,90])
ax.set_xlabel('Historical RMSE increase (%)',labelpad=9);ax.set_ylabel('Rare RMSE reduction (%)',labelpad=9)
ax.grid(color=GRID,lw=.65);ax.set_axisbelow(True)
save(fig,'05_controller_screen','Manuscript Fig. 5; revised report Table 9','Keep all four controller outcomes separate from Figure 4. The 30%/85% region identifies candidates, not approved deployments.')

# 6. Separate data roles make the missing evidence concrete, rather than a generic hold label.
fig,ax=canvas()
columns=[(1.62,'Controller\nselection','Two candidate\noutcomes',TEAL,False),
         (4.65,'Independent\ncalibration data','Coverage\n+ interval width',GREY,True),
         (7.68,'Untouched\nfinal-test data','Accuracy, UQ\n+ consistency',GREY,True),
         (10.71,'Versioned\nevidence record','Promotion\nreview',GREY,True)]
for i,(x,upper,lower,color,pending) in enumerate(columns):
    box(ax,x,3.25,2.45,.82,upper,color,'#f4f8f9' if not pending else 'white',pending,fs=14)
    box(ax,x,1.75,2.45,.82,lower,color,'#f4f8f9' if not pending else 'white',pending,fs=14)
    arrow(ax,(x,2.82),(x,2.19),color)
    if i<3:arrow(ax,(x+1.24,1.75),(columns[i+1][0]-1.24,1.75))
ax.plot([.42,.88],[.48,.48],color=TEAL,lw=2);ax.text(1.03,.48,'Reported screen',va='center',fontsize=13)
ax.plot([4.0,4.46],[.48,.48],color=GREY,lw=2,ls='--');ax.text(4.61,.48,'Required evidence',va='center',fontsize=13)
save(fig,'06_validation_boundary','Revised report §§5.7–5.9','Distinguish controller selection, independent UQ calibration, untouched final testing, and a versioned promotion record. These roles are not verified dataset partitions in the present study.')

# 7. The next experiment closes the original plan's causal/evidence chain. No simulated time trace.
fig,ax=canvas()
items=[('Declared\nchange',BLUE),('Ordered\ntrajectories',BLUE),('Frozen detector\n+ decision',ORANGE),
       ('Matched\nupdates',TEAL),('Independent\ncalibration',GREY),('Final test\n+ review',GREY)]
xs=np.linspace(1.05,11.45,6)
for i,((label,color),x) in enumerate(zip(items,xs)):
    box(ax,x,2.9,1.78,.96,label,color,fs=13)
    if i<5:arrow(ax,(x+.91,2.9),(xs[i+1]-.91,2.9))
box(ax,7.29,1.25,2.3,.66,'Adaptive replay',TEAL,fs=13)
box(ax,4.65,1.25,2.3,.66,'Fixed replay r = 0.8',GREY,fs=12)
arrow(ax,(4.65,1.60),(7.29,2.39),GREY)
arrow(ax,(7.29,1.60),(7.29,2.39),TEAL)
ax.text(5.95,.45,'Matched seeds, update budget, and exposure',ha='center',va='center',fontsize=13)
save(fig,'07_next_demonstration','Revised report §5.10; analysis specification; original trigger/UQ plan','Planned experiment only. The original aim is a trigger-to-validated-update demonstration. Fixed-r=0.8 is a needed control, not a completed result.')

slides=[
dict(title='The revision connects the planned cycle to a controlled update case',
 image='01_plan_and_evidence',source='Revised report §§2.2, 5.9.',
 caption='The update supplies offline evidence for the middle of the lifecycle; it does not complete an operational cycle.',
 notes='The original plan was to demonstrate a change in conditions, detect consequential degradation, justify and prepare an update, retain historical performance, calibrate uncertainty, and independently review deployment. The updated report now maps an existing controlled U-Net study onto that plan. MONITOR has baseline aggregates; DETECT is a retrospective response label; DECIDE uses an illustrative screen; PREPARE is regime-selected; UPDATE has the strongest reported evidence. None of those labels establishes operational monitoring or an approved decision record. CALIBRATE and DEPLOY remain requirements. This is the report revision contribution, not a claim of new experiments.'),
dict(title='The case study tests adaptation to rare plume changes',
 image='02_controlled_stress_test',source='Revised report §§5.1–5.5; manuscript Fig. 1.',
 caption='Mass90 uses reference states at t and t + 1. Rare-case learning and historical replay form the controlled update.',
 notes='The reported case is a pump-and-treat U-Net on a 128 × 100 grid with 1–5 extraction wells and a dataset described as 10,000 physics simulations. Pumping input is represented through Thiem preprocessing. Time is kept indexed because older descriptions disagree on days versus years. Historical cases are the bottom 40% of the Mass90 size-change response score, with cutoff 0.133; rare cases are the top 3%, starting at 0.329. This score requires the reference next state and is not a prospective warning signal. It can miss plume translation that leaves the footprint size unchanged. Rare cases and historical replay define the update problem; trajectory splits, middle-57% handling, controller exposure, and active-learning selection are not verified.'),
dict(title='The rare-case example locates the baseline prediction error',
 image='03_rare_spatial_example',source='Manuscript Fig. 2(b), rare-regime triplet; source crop.',
 caption='Reference concentration, static U-Net prediction, and prediction-minus-reference error in one reported example.',
 notes='This is a faithful crop of the original manuscript rare-regime triplet. The caption identifies the reference as the full-order physics field and the prediction as the static U-Net result. All pixels, original labels, axes, aspect ratio, and colorbars are preserved; this is not a numerical replot. Concentration ranges to 813.6 µg/L and signed error spans ±169.4 µg/L in the displayed source. The field shows localized residual structure around the plume. No sample identifier or raw arrays accompany it, so this is illustrative of the physical error mechanism and not an independently verified distributional result. Historical and rare source panels use different scales; only the internally consistent rare triplet is shown. No synthetic plume or recolored pixel-derived field has been created.'),
dict(title='Rare-regime recovery comes with a historical-retention tradeoff',
 image='04_joint_rmse',source='Manuscript Fig. 4; revised report Table 10.',
 caption='Fixed replay changes historical/rare RMSE from 0.58/10.04 to 1.03/1.21 µg/L in this reported comparison.',
 notes='Compare both objectives: baseline 0.58/10.04, simple fine-tuning 1.11/3.92, fixed replay 1.03/1.21, and EWC 5.45/1.22 µg/L. Fixed replay has lower errors than simple fine-tuning or EWC in this particular comparison, while remaining worse than the baseline on historical conditions. It reduces rare RMSE by 87.9% and raises historical RMSE by 77.6%. Supporting rare-plume metrics change from 32.30 to 1.82% for mass, 14.20 to 3.43% for peak, and 7.11 to 1.89% for Mass90. Exact normalization requires code. The ambiguous historical plume-metric column is omitted. No line between points is drawn because training trajectories are unavailable. The Figure 3 full-network 0.64/0.99 pair is not pooled here because Model C and protocols remain unresolved.'),
dict(title='An explicit screen retains two controller outcomes for further evaluation',
 image='05_controller_screen',source='Manuscript Fig. 5; revised report Table 9.',
 caption='The 30% / 85% limits are illustrative. The two passing outcomes clear the rare-improvement limit by only 0.8 and 0.5 points.',
 notes='This is a separate Figure 5 controller comparison. Fixed replay is 80.4/88.9%, threshold adaptive forgetting 26.5/85.8%, loss-balanced 21.1/85.5%, and loss-balanced with floor 38.1/87.3%, where coordinates are historical increase and rare reduction. The shaded region meets historical increase ≤30% and rare reduction ≥85%. The two passing variants are candidates under this illustrative screen, not approved deployments. Historical margins are 3.5 and 8.9 points; rare margins are 0.8 and 0.5 points. Replicate uncertainty is absent, so significance or robustness cannot be inferred. Figure 4 fixed-replay changes 77.6/87.9 differ from Figure 5 80.4/88.9; keep those comparisons separate until denominators, splits, and executed configurations are reconciled.'),
dict(title='The evidence stops before calibration and final validation',
 image='06_validation_boundary',source='Revised report §§5.7–5.9.',
 caption='Controller selection, uncertainty calibration, and the final test require distinct data roles and evidence records.',
 notes='The report reaches a defensible result: retain two controller outcomes for further evaluation, then hold for missing evidence. There are no predictive intervals, calibrated coverage/width results, independent calibration parameters, untouched final-test record, checkpoint identity, or versioned promotion decision for these outcomes. The figure labels required roles rather than claiming verified independent partitions. A deterministic model could use residual-based conformal calibration when suitable data and assumptions exist; coverage is not inferred from RMSE. This is an offline evidence assessment, not an operational rollback event. If an operational incumbent becomes invalid, withdrawal and governed retraining policy applies.'),
dict(title='The next demonstration must connect a known change to a validated update',
 image='07_next_demonstration',source='Revised report §5.10; analysis specification; original trigger/UQ plan.',
 caption='Planned next test: a known change, ordered evidence, a frozen decision rule, matched updates, and independent validation.',
 notes='Return to the original demonstration purpose. First resolve the time axis and trajectory manifest and archive executed configurations and predictions. Define a known controlled change, evaluate the detector prospectively on ordered trajectories, and freeze thresholds and an acceptance contract before final testing. Compare adaptive scheduling with fixed replay at r = 0.8 under matched seeds, update budget, and historical/new exposure; the displayed adaptive trajectory reaches that cap, which alone cannot isolate scheduling benefit. Calibrate independently and evaluate an untouched final test once, then record model version and reviewer decision. The diagram is an experiment plan, not an achieved result. Field deployment and long-duration monitoring remain subsequent validation, and no cost/speedup or active-learning gain is claimed.'),
]

# Reuse the established builder, then apply a plain scientific slide layout.
skill=Path('/home/song884/.codex/skills/evidence-deck-builder/scripts/build_evidence_deck.py')
modspec=importlib.util.spec_from_file_location('deck_builder',skill)
builder=importlib.util.module_from_spec(modspec);modspec.loader.exec_module(builder)
spec={'slides':[{'layout':'image','title':s['title'],'image':str(ROOT/f"figures/{s['image']}.png"),
                'notes':s['notes']+'\n\nSource: '+s['source']} for s in slides]}
(ROOT/'deck_spec.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
builder.build_deck(spec,ROOT/f'{STEM}.pptx',ROOT/'speaker_notes.md')
prs=Presentation(ROOT/f'{STEM}.pptx')
for i,(slide,item) in enumerate(zip(prs.slides,slides),1):
    for shape in list(slide.shapes):
        shape._element.getparent().remove(shape._element)
    slide.background.fill.solid();slide.background.fill.fore_color.rgb=RGBColor(255,255,255)
    title=builder.add_text(slide,item['title'],Inches(.60),Inches(.43),Inches(12.10),Inches(.95),
        size=26,bold=True,color=RGBColor(32,45,55))
    title.name='Slide claim';title.text_frame.word_wrap=True
    builder.add_image(slide,str(ROOT/f"figures/{item['image']}.png"),Inches(.55),Inches(1.48),Inches(12.23),Inches(4.80))
    pic=next(s for s in slide.shapes if s.shape_type==MSO_SHAPE_TYPE.PICTURE)
    pic.name='Key scientific figure';pic._element.nvPicPr.cNvPr.set('descr',item['caption'])
    builder.add_text(slide,item['caption'],Inches(.65),Inches(6.49),Inches(12),Inches(.48),
        size=14,color=RGBColor(55,68,76))
    builder.add_text(slide,'Source: '+item['source'],Inches(.65),Inches(7.10),Inches(11.8),Inches(.20),
        size=9,color=RGBColor(104,114,122))
    builder.add_text(slide,str(i),Inches(12.45),Inches(7.10),Inches(.25),Inches(.20),
        size=9,color=RGBColor(104,114,122))
    for shape in slide.shapes:
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                for r in p.runs:r.font.name='Arial'
    slide.notes_slide.notes_text_frame.text=item['notes']+'\n\nSource: '+item['source']+'\nSource report: deliverables/report_revision_20261028/Framework_revised_20261028.docx.'
prs.core_properties.title='Revised U-Net case study: planned lifecycle and available evidence'
prs.core_properties.subject='Internal meeting, October 29, 2026; revised scientific storyline'
prs.core_properties.author='Xuehang Song'
prs.save(ROOT/f'{STEM}.pptx')
check=Presentation(ROOT/f'{STEM}.pptx')
assert len(check.slides)==7
for s in check.slides:
    assert sum(sh.shape_type==MSO_SHAPE_TYPE.PICTURE for sh in s.shapes)==1
    for sh in s.shapes:
        assert sh.left>=0 and sh.top>=0 and sh.left+sh.width<=check.slide_width and sh.top+sh.height<=check.slide_height
with ZipFile(ROOT/f'{STEM}.pptx') as z:assert z.testzip() is None
(ROOT/'sources/figure_audit.json').write_text(json.dumps(audit,indent=2,ensure_ascii=False)+'\n')
(ROOT/'qa/build_verification.json').write_text(json.dumps({
    'slides':7,'one_image_per_slide':True,'no_bar_charts':True,'figure_titles':False,
    'source_hashes_recorded':True,'crop_pixels_unchanged':True,'crop_aspect_ratio_preserved':True,
    'speaker_notes_embedded':True,'source_comparisons_not_pooled':True},indent=2)+'\n')
print('Built '+str(ROOT/f'{STEM}.pptx'),flush=True)

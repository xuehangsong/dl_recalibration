"""Scientific case-study deck: planned lifecycle, reported evidence, next test."""
from pathlib import Path
import sys, csv, json, hashlib, importlib.util, shutil
sys.path.insert(0, '/tmp/dl_slides_20261029_python')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
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
STEM='Updated_case_study_20261029_v4'
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
    REPO/'deliverables/revision_case_study_slides_20261029_v2/Updated_case_study_20261029_v2.pptx',
    REPO/'deliverables/revision_case_study_slides_20261029_v2/Updated_case_study_20261029_v2.pdf',
    REPO/'deliverables/revision_case_study_slides_20261029_v3/Updated_case_study_20261029_v3.pptx',
    REPO/'deliverables/revision_case_study_slides_20261029_v3/Updated_case_study_20261029_v3.pdf',
]

hashes={str(p.relative_to(REPO)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}
assert hashes['drafts/final/section5_FINAL_20261008_FROZEN.md']=='ea4075935fced71a3abc39954f4de15fde04cbb3803537edaad40ac793aba563'
with ZipFile(source_paths[2]) as z:embedded=z.read('word/media/image2.png')
source_image=ANALYSIS/'source_extracts/embedded_figures/image2.png'
assert embedded==source_image.read_bytes()
hashes[str(source_image.relative_to(REPO))]=hashlib.sha256(embedded).hexdigest()
with ZipFile(source_paths[2]) as z:
    for i in range(1,6):
        p=ANALYSIS/f'source_extracts/embedded_figures/image{i}.png'
        assert z.read(f'word/media/image{i}.png')==p.read_bytes()
        hashes[str(p.relative_to(REPO))]=hashlib.sha256(p.read_bytes()).hexdigest()
(ROOT/'sources/input_sha256.json').write_text(json.dumps(hashes,indent=2)+'\n')
for p in source_paths[6:8]:shutil.copy2(p,ROOT/'sources'/p.name)

INK='#23323c';BLUE='#286787';TEAL='#277e78';ORANGE='#ba773b';PURPLE='#806796';GREY='#77828b';GRID='#e2e7ea'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'axes.labelsize':17,'xtick.labelsize':14,'ytick.labelsize':14,
    'axes.spines.top':False,'axes.spines.right':False,'axes.linewidth':.8,'axes.edgecolor':'#7c878f','text.color':INK,
    'axes.labelcolor':INK,'xtick.color':INK,'ytick.color':INK,'figure.facecolor':'white','savefig.facecolor':'white',
    'pdf.fonttype':42,'svg.fonttype':'none'})
audit=[]
def save(fig,name,source,treatment):
    assert fig._suptitle is None and all(not a.get_title() for a in fig.axes)
    for ext in ['png','svg','pdf']:fig.savefig(ROOT/f'figures/{name}.{ext}',dpi=220,facecolor='white')
    audit.append({'figure':name,'source':source,'treatment':treatment})
    plt.close(fig)

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
audit.append({'figure':'03_rare_spatial_example','source':'Yilin manuscript Fig. 2(b), rare-regime triplet',
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
save(fig,'04_joint_rmse','Yilin manuscript Fig. 4; revised report Table 10','Replot reported historical/rare RMSE pairs together. No connecting trajectory, replicate distribution, or uncertainty is invented.')

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
save(fig,'05_controller_screen','Yilin manuscript Fig. 5; revised report Table 9','Keep all four controller outcomes separate from Figure 4. The 30%/85% region identifies candidates, not approved deployments.')

# Physical errors from the SAME Figure 4 comparison. No bars or assumed uncertainty.
fig,axs=plt.subplots(1,3,figsize=(12.5,4.6),sharey=True)
fig.subplots_adjust(left=.18,right=.96,top=.91,bottom=.24,wspace=.20)
names=['Baseline','Simple fine-tuning','Fixed replay','EWC']
colors=[GREY,ORANGE,BLUE,PURPLE];markers=['o','s','D','^']
metrics=[('rare_mass_error','Plume-mass error (%)',38,[0,10,20,30]),
         ('rare_peak_error','Peak-concentration error (%)',17,[0,5,10,15]),
         ('rare_mass90_error','Mass90 error (%)',8.8,[0,2,4,6,8])]
for ax,(key,label,xmax,ticks) in zip(axs,metrics):
    for y,r,c,m in zip(range(4),f4,colors,markers):
        value=float(r[key])
        ax.scatter(value,y,s=115,c=c,marker=m,edgecolors='white',lw=1,zorder=3)
        ax.annotate(f'{value:.2f}',(value,y),xytext=(8,0),textcoords='offset points',
                    va='center',fontsize=12,color=c)
    ax.set_xlim(0,xmax);ax.set_xticks(ticks);ax.set_ylim(3.5,-.5)
    ax.set_xlabel(label,labelpad=12,fontsize=14)
    ax.grid(axis='x',color=GRID,lw=.65);ax.set_axisbelow(True)
    ax.spines['left'].set_visible(False);ax.tick_params(axis='y',length=0)
axs[0].set_yticks(range(4),names,fontsize=14)
save(fig,'05_rare_physical_errors','Yilin manuscript Fig. 4(a); revised report Table 11',
     'Three aligned point panels reproduce rare-regime mass, peak, and Mass90 errors. Each metric has its own labeled linear scale. No uncertainties or time trajectories are inferred.')

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
 image='03_rare_spatial_example',source='Yilin manuscript Fig. 2(b), rare-regime triplet; source crop.',
 caption='Reference concentration, static U-Net prediction, and prediction-minus-reference error in one reported example.',
 notes='This is a faithful crop of the original manuscript rare-regime triplet. The caption identifies the reference as the full-order physics field and the prediction as the static U-Net result. All pixels, original labels, axes, aspect ratio, and colorbars are preserved; this is not a numerical replot. Concentration ranges to 813.6 µg/L and signed error spans ±169.4 µg/L in the displayed source. The field shows localized residual structure around the plume. No sample identifier or raw arrays accompany it, so this is illustrative of the physical error mechanism and not an independently verified distributional result. Historical and rare source panels use different scales; only the internally consistent rare triplet is shown. No synthetic plume or recolored pixel-derived field has been created.'),
dict(title='Rare-regime recovery comes with a historical-retention tradeoff',
 image='04_joint_rmse',source='Yilin manuscript Fig. 4; revised report Table 10.',
 caption='Fixed replay changes historical/rare RMSE from 0.58/10.04 to 1.03/1.21 µg/L in this reported comparison.',
 notes='Compare both objectives: baseline 0.58/10.04, simple fine-tuning 1.11/3.92, fixed replay 1.03/1.21, and EWC 5.45/1.22 µg/L. Fixed replay has lower errors than simple fine-tuning or EWC in this particular comparison, while remaining worse than the baseline on historical conditions. It reduces rare RMSE by 87.9% and raises historical RMSE by 77.6%. Supporting rare-plume metrics change from 32.30 to 1.82% for mass, 14.20 to 3.43% for peak, and 7.11 to 1.89% for Mass90. Exact normalization requires code. The ambiguous historical plume-metric column is omitted. No line between points is drawn because training trajectories are unavailable. The Figure 3 full-network 0.64/0.99 pair is not pooled here because Model C and protocols remain unresolved.'),
dict(title='An explicit screen retains two controller outcomes for further evaluation',
 image='05_controller_screen',source='Yilin manuscript Fig. 5; revised report Table 9.',
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

# Enrich the v2 argument with directly audited manuscript evidence.
for item,key in [(slides[0],'plan'),(slides[1],'stress'),(slides[5],'boundary'),(slides[6],'next')]:
    item.pop('image');item['diagram']=key
slides[1]['notes']+=' Direct manuscript anchors: P0008–P0024 and Eq. (1), P0063–P0066. Mass90 is the number of cells enclosing 90% of reference mass, not a distance traveled by the plume.'
slides[2]['notes']+=' Direct manuscript anchors P0137–P0140 locate residuals around plume bodies, gradients, and boundaries. This supports showing where error occurs; it does not establish a universal failure mechanism from one case.'
slides[3]['caption']='Fixed replay changes historical/rare RMSE from 0.58/10.04 to 1.03/1.21 µg/L; update configurations also differ in trainable layers.'
slides[3]['notes']+=' Direct manuscript anchors: P0146–P0150 and Figure 4. Table 1 (P0042, P0047, P0052) lists last-decoder/output updates for simple fine-tuning and full-network updates for replay/EWC; this does not isolate replay as the sole cause. EWC means elastic weight consolidation.'
slides[4]['notes']+=' Direct manuscript anchors: P0152–P0156 and Figure 5. Methods P0126 instead illustrates 5% historical degradation and 20% rare improvement, while Figure 3 uses 25% historical tolerance. Thus Figure 5 is used as a panel-specific illustrative screen, not a preregistered contract.'
slides[5]['notes']+=' Direct manuscript Table 2, P0104–P0116, distinguishes validation feedback from final testing, but the executed split identities are not supplied. Missing interval results are not supplied by deterministic RMSE.'
physical=dict(
    title='Rare-plume recovery extends to mass, peak, and footprint errors',
    image='05_rare_physical_errors',source='Yilin manuscript Fig. 4(a); revised report Table 11.',
    caption='Fixed replay and EWC have similar rare-plume errors, while their historical RMSE differs sharply.',
    notes='This panel follows the RMSE comparison and keeps the exact same four Figure 4 configurations. Reported mass / peak / Mass90 errors are baseline 32.30 / 14.20 / 7.11%, simple fine-tuning 9.86 / 7.70 / 3.59%, fixed replay 1.82 / 3.43 / 1.89%, and EWC 1.88 / 3.40 / 1.64%. Direct manuscript anchors P0123–P0124 define the physical quantities, and P0146–P0150 with Figure 4 supply the results. Fixed replay and EWC have similar rare physical errors despite very different historical RMSE, so physical recovery alone cannot resolve historical retention. Mass90 denotes a footprint cell count containing 90% of mass, not spatial overlap or plume translation. These are rounded aggregate source labels without replicate uncertainty. The three panels use separately labeled linear axes. Metric normalization and aggregation require the executed code. The ambiguous historical physical-metric column is excluded. Proposed center-of-mass and exceedance-area metrics are mentioned in Methods but have no reported numerical results; they are not plotted. No compliance-well or remedy performance outcome is inferred.')
replay=dict(
    title='Adaptive replay adjusts the training mix using validation feedback',
    diagram='replay',source='Manuscript Eq. (1), adaptive-replay methods, Table 2, and Fig. 5(a).',
    caption='The reported trajectory reaches r = 0.8 for most epochs; a matched fixed-ratio control is needed to isolate scheduling benefit.',
    notes='Direct manuscript evidence: P0063–P0066 defines the mixed update batch as r B_old + (1−r) B_new, with historical low-change examples and rare high-change examples. This diagram represents the reported controller structure, not a complete executable specification. P0077–P0081 defines historical forgetting as updated historical validation RMSE divided by baseline historical validation RMSE, minus one, evaluated on the same historical validation set. The threshold controller increases replay above an upper forgetting tolerance; it decreases replay only when forgetting is below a lower tolerance AND rare validation loss is improving. This precise condition is narrower than general motivation language in P0075. The loss-balanced variant uses normalized historical and rare validation losses (P0097–P0103); its Eq. (5), P0093, is incomplete, so no repaired formula or parameter values are invented. Validation drives feedback; final-test performance is outside this loop (Table 2, P0111–P0116). Figure 5(a), discussed at P0152–P0156, shows the adaptive ratio reaching its cap r = 0.8 for most of 100 plotted epochs. The sampled historical exposure is not independently verified from logs. These results support studying the allocation tradeoff, but cannot by themselves attribute improvements to adaptive scheduling rather than high replay. The next test needs a fixed-ratio-0.8 control with matched initialization, seeds, update budget, and exposure accounting.')
slides[4:4]=[physical,replay]

# v4 retains the style and empirical values; provenance is explicit on every slide.
sources=[
    'Diagram from revised report §§2.2, 5.9; evidence mapping by this revision.',
    'Diagram from Yilin manuscript §2.2 and Fig. 1; reported stress-selection thresholds.',
    'Yilin manuscript Fig. 2(b), rare-regime panels; original pixels, crop only.',
    'Replotted from Yilin manuscript Fig. 4(a), printed RMSE values; raw predictions unavailable.',
    'Replotted from Yilin manuscript Fig. 4(a), printed rare-plume errors; no added data.',
    'Diagram from Yilin manuscript Eq. (1), adaptive-replay methods, and Table 2.',
    'Replotted from Yilin manuscript Fig. 5(b); boundaries from Fig. 5(c).',
    'Diagram from revised report §§5.7–5.9; unfulfilled validation requirements.',
    'Planned experiment from revised report §5.10 and the original trigger/UQ plan.',
]
for s,source in zip(slides,sources):
    s['source']=source
    s['notes']+=' Audit provenance: empirical values are transcribed from the original manuscript figure labels, not independently recomputed from simulation outputs. Original Figures 1–5 are reproduced without alteration in Yilin_original_figures_20261029.pptx. Diagrams synthesize source methods or planned steps and are not additional experimental data.'
slides[6]['notes']+=' For this replot, Figure 5(b) supplies the eight printed percentages and Figure 5(c) supplies the two boundaries. Historical degradation is relabeled historical RMSE increase and rare improvement is relabeled rare RMSE reduction. The plot uses x=0–90% and y=80–90% to separate the four points; source panel (c) has a broader view, so the limits are design choices rather than new measurements. Numeric labels and coordinates are unchanged. Derived passing margins use percentage points, not relative percentages. Figure 4 fixed-replay changes and Figure 5 labels cannot be reconciled by the displayed rounding precision alone.'
slides[0]['notes']+=' Historical plan: plans/handoffs/trigger_uq_prototype_workflow_handoff.md, dated June 11, 2026 (Git 8496417), and the prototype text at Git 29bf982:drafts/final/section5_FINAL.md. These are planned objectives, not evidence of executed experiments.'
slides[1]['notes']+=' The source describes a homogeneous synthetic aquifer with uniform porosity and hydraulic conductivity (P0016). Rounded percentile labels do not establish exact executable cutoffs or independent trajectory counts.'
slides[7]['notes']=slides[7]['notes'].replace('There are no predictive intervals', 'The reviewed manuscript and report package provide no predictive intervals')
slides[8]['notes']+=' The June 11 handoff supplies the original trigger/UQ demonstration agenda. The matched fixed-ratio-0.8 control is proposed in the October evidence review and revised Section 5, motivated by manuscript Figure 5(a); it is not an executed control or a June-plan result.'

# Use the established deck builder for native slide text and figure placement.
skill=Path('/home/song884/.codex/skills/evidence-deck-builder/scripts/build_evidence_deck.py')
modspec=importlib.util.spec_from_file_location('deck_builder',skill)
builder=importlib.util.module_from_spec(modspec);modspec.loader.exec_module(builder)
import native_diagrams
drawers={key:getattr(native_diagrams,'draw_'+key) for key in ['plan','stress','replay','boundary','next']}
prs=Presentation();prs.slide_width=Inches(13.333);prs.slide_height=Inches(7.5)
(ROOT/'deck_spec.json').write_text(json.dumps({'slides':slides},indent=2,ensure_ascii=False)+'\n')
diagram_checks=[]
for i,item in enumerate(slides,1):
    slide=prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid();slide.background.fill.fore_color.rgb=RGBColor(255,255,255)
    title=builder.add_text(slide,item['title'],Inches(.60),Inches(.43),Inches(12.10),Inches(.95),
        size=26,bold=True,color=RGBColor(32,45,55))
    title.name='Slide claim';title.text_frame.word_wrap=True
    if 'diagram' in item:
        drawers[item['diagram']](slide)
        audit.append({'figure':item['diagram'],'source':item['source'],
            'treatment':'Native editable PowerPoint nodes, text, and attached connectors. Diagram is synthesized from source evidence; no experimental trajectory is inferred.'})
    else:
        builder.add_image(slide,str(ROOT/f"figures/{item['image']}.png"),Inches(.55),Inches(1.48),Inches(12.23),Inches(4.80))
        pic=next(s for s in slide.shapes if s.shape_type==MSO_SHAPE_TYPE.PICTURE)
        pic.name='Key scientific figure';pic._element.nvPicPr.cNvPr.set('descr',item['caption'])
    caption=builder.add_text(slide,item['caption'],Inches(.65),Inches(6.49),Inches(12),Inches(.48),
        size=14,color=RGBColor(55,68,76));caption.name='Figure caption'
    builder.add_text(slide,'Source: '+item['source'],Inches(.65),Inches(7.10),Inches(11.8),Inches(.20),
        size=9,color=RGBColor(104,114,122))
    builder.add_text(slide,str(i),Inches(12.45),Inches(7.10),Inches(.25),Inches(.20),
        size=9,color=RGBColor(104,114,122))
    for shape in slide.shapes:
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                for r in p.runs:r.font.name='Arial'
    slide.notes_slide.notes_text_frame.text=item['notes']+'\n\nSource: '+item['source']+'\nDirect accepted-view extraction: sources/manuscript_accepted_full.txt. Primary source: method_manuscript/Adaptive_Replay_Manuscript_2026_09_09.docx (file version used for this audit).\nSource report: deliverables/report_revision_20261028/Framework_revised_20261028.docx.'
prs.core_properties.title='Updated U-Net case study: evidence, replay, and validation'
prs.core_properties.subject='Internal meeting, October 29, 2026; manuscript-grounded revision with editable diagrams'
prs.core_properties.author='Xuehang Song'
prs.save(ROOT/f'{STEM}.pptx')
(ROOT/'speaker_notes.md').write_text('\n\n'.join(f"## {i}. {s['title']}\n\n{s['caption']}\n\n{s['notes']}\n\nSource: {s['source']}" for i,s in enumerate(slides,1))+'\n')
check=Presentation(ROOT/f'{STEM}.pptx')
assert len(check.slides)==9
for i,(slide,item) in enumerate(zip(check.slides,slides),1):
    pictures=sum(s.shape_type==MSO_SHAPE_TYPE.PICTURE for s in slide.shapes)
    assert pictures==(0 if 'diagram' in item else 1)
    for sh in slide.shapes:
        assert sh.left>=0 and sh.top>=0 and sh.left+sh.width<=check.slide_width and sh.top+sh.height<=check.slide_height,(i,sh.name)
    connectors=slide._element.xpath('.//p:cxnSp')
    attached=[c for c in connectors if c.xpath('./p:nvCxnSpPr/p:cNvCxnSpPr/a:stCxn') and c.xpath('./p:nvCxnSpPr/p:cNvCxnSpPr/a:endCxn')]
    if 'diagram' in item:assert len(attached)>=2,(i,'No actual connected PowerPoint flowchart')
    diagram_checks.append({'slide':i,'pictures':pictures,'connectors':len(connectors),'fully_attached_connectors':len(attached)})
with ZipFile(ROOT/f'{STEM}.pptx') as z:assert z.testzip() is None
(ROOT/'sources/figure_audit.json').write_text(json.dumps(audit,indent=2,ensure_ascii=False)+'\n')
(ROOT/'qa/build_verification.json').write_text(json.dumps({
    'slides':9,'native_flowcharts':[1,2,6,8,9],'scientific_figure_slides':[3,4,5,7],
    'no_bar_charts':True,'figure_titles':False,'source_hashes_recorded':True,
    'speaker_notes_embedded':True,'source_comparisons_not_pooled':True,'slide_checks':diagram_checks},indent=2)+'\n')
print('Built '+str(ROOT/f'{STEM}.pptx'),flush=True)

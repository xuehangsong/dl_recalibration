"""Build a new report from the saved Word revision, preserving all source files."""
import sys
sys.path.insert(0, '/tmp/dl_report_20261028_python')
from pathlib import Path
from copy import deepcopy
import json, re, csv, hashlib
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree
from docx import Document
from docx.text.paragraph import Paragraph
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT=Path(__file__).resolve().parents[1]; REPO=ROOT.parents[1]
SOURCE=REPO/'final report/Framework_revision.docx'
doc=Document(SOURCE)
ps=doc.element.body.xpath('.//w:p')
audit=[]

def text(el):return ''.join(el.xpath('.//w:t/text()'))

def rewrite(el, new, reason='', record=True):
    old=text(el)
    starts=[deepcopy(b) for b in el.xpath('./w:bookmarkStart')]
    ends=[deepcopy(b) for b in el.xpath('./w:bookmarkEnd')]
    # Inherit the first actual text run, not the first run with formatting:
    # the latter may be a later exponent, subscript, or comment marker.
    first=next((r for r in el.xpath('./w:r') if r.xpath('./w:t/text()')),None)
    prop=first.find(qn('w:rPr')) if first is not None else None
    rpr=deepcopy(prop) if prop is not None else None
    style=el.xpath('./w:pPr/w:pStyle/@w:val')
    if rpr is not None and (not style or style[0] not in ('PNNLCoverSubtitle','PNNLTitle-PageText')):
        for tag in ['b','bCs','i','iCs','u','vertAlign']:
            for e in rpr.findall(qn('w:'+tag)):rpr.remove(e)
    for child in list(el):
        if child.tag!=qn('w:pPr'):el.remove(child)
    for b in starts:el.append(b)
    run=OxmlElement('w:r')
    if rpr is not None:run.append(rpr)
    t=OxmlElement('w:t');t.set(qn('xml:space'),'preserve');t.text=new;run.append(t);el.append(run)
    for b in ends:el.append(b)
    if record and old!=new:audit.append({'source_paragraph':next((i for i,p in enumerate(ps) if p is el),None),'old':old,'new':new,'reason':reason})

def edit(i,new,reason):rewrite(ps[i],new,reason)
def sub(i,old,new,reason):
    s=text(ps[i]);assert old in s,(i,old);edit(i,s.replace(old,new),reason)

title='Maintaining Deep-Learning Surrogate Accuracy for Long-Term Groundwater Remediation: Framework and Controlled Update Evidence'
edit(6,title,'Align title with the revised evidence scope')
edit(57,title,'Align title with the revised evidence scope')
edit(61,'October 2026 — Revision draft','Identify the review copy without claiming formal reissue')
for i,p in enumerate(ps[:80]):
    if text(p).strip()=='April 2026':edit(i,'October 2026 — Revision draft','Revision date')
# Word regenerates date controls from their stored date when opening the file.
# Update that value as well as the visible text so the title page stays current.
for date in doc.element.body.xpath('.//w:sdtPr/w:date'):
    if date.get(qn('w:fullDate'),'').startswith('2026-04-01'):
        date.set(qn('w:fullDate'),'2026-10-01T00:00:00Z')
doc.core_properties.title=title
doc.core_properties.subject='Integrated review draft; controlled offline U-Net update evidence and seven-step lifecycle'

edits={
82:'Deep-learning surrogates can accelerate groundwater simulations and make large scenario studies more practical. Their value for long-term remediation depends on maintaining reliability as the conditions they predict change.',
83:'Pumping systems, contaminant sources, boundary conditions, and conceptual site models can evolve over the years and decades typical of DOE environmental management. A surrogate trained on historical conditions may then encounter behavior outside its evaluated domain. Monitoring and evidence-based review are needed to determine whether it remains suitable for use.',
84:'This report connects model maintenance to the governance and quality assurance expectations of environmental decision support: when to intervene, how to assess an update, and what evidence permits deployment.',
85:'This revised report develops that process through a three-pillar framework and a controlled pump-and-treat U-Net case study. The central questions are when an update is warranted, how the update can preserve useful historical behavior, and what evidence is required before the candidate may be used. The three complementary pillars are:',
86:'Governance defines acceptance criteria, recalibration triggers, configuration control, and decision authority. Surrogates support screening and planning; high-fidelity physics-based analysis remains authoritative for final regulatory and remedy decisions.',
87:'Modeling engines provide physics-based reference predictions and fast surrogate approximations. Published applications motivate their potential efficiency, while the end-to-end cost of the present recalibration workflow remains to be measured.',
88:'Recalibration mechanisms provide uncertainty quantification, drift detection, continual learning, and active learning. Their suitability must be evaluated for the intended conditions.',
89:'The pillars are connected through MONITOR → DETECT → DECIDE → PREPARE → UPDATE → CALIBRATE → DEPLOY. Continuous monitoring and human review identify whether intervention is warranted; a triggered response prepares data, updates the model, calibrates uncertainty, and evaluates the candidate for promotion. Acceptance criteria and documented decisions connect each step.',
90:'The U-Net case study provides measured evidence for the update decision. In one reported comparison, fixed replay reduces rare-regime RMSE from 10.04 to 1.21 µg/L while historical RMSE rises from 0.58 to 1.03 µg/L. A separate controller comparison identifies two candidate outcomes that satisfy illustrative adaptation–retention conditions. These results show why rare-regime improvement must be assessed together with historical retention; the comparisons are not a single verified test protocol.',
91:'The report therefore advances from a conceptual framework and prototype plan to an evidence-backed account of a controlled model-maintenance decision. Prospective drift detection, independent uncertainty calibration, and untouched final-test promotion remain undemonstrated. The candidates are held for further evaluation, and the report specifies the evidence needed to complete a reproducible, governed lifecycle.',
93:'Deep-learning (DL) surrogates can accelerate groundwater flow and transport predictions, making large scenario sets and uncertainty analyses more practical. Their reliability can change as pumping systems, source conditions, boundary conditions, or conceptual models change. This report connects a governance-aware framework for managing those changes to a controlled U-Net update case study for pump-and-treat plume prediction. The intended role remains screening, scenario exploration, and planning support within DOE environmental management.',
100:'The workflow has seven distinct steps. MONITOR collects performance and uncertainty evidence; DETECT evaluates possible degradation; DECIDE records the human judgment that an update is warranted. PREPARE assembles traceable data; UPDATE produces a candidate; CALIBRATE assesses and adjusts its predictive uncertainty; DEPLOY applies an independent final test and records the promotion decision. These are framework requirements, and the case study explicitly identifies which requirements have evidence and which remain to be demonstrated.',
101:'The case study uses reported U-Net/adaptive-replay results to examine rare-regime recovery and historical retention. Mass90 response changes define a retrospective stress condition, and reported update comparisons quantify the resulting tradeoff. An illustrative decision screen retains selected controller outcomes for further evaluation. No interval-calibration or final-promotion artifact is available, so the supported endpoint is a candidate awaiting calibration and final validation.',
102:'The report makes three connected contributions: a three-pillar governance and methods framework, a quantitative offline update case study mapped to its seven steps, and a concrete evidence specification for advancing toward an operational demonstration. The contribution is the connection between measured performance, decision criteria, and the next required evidence.',
103:'The current maturity is a defined framework with controlled update evidence. Prospective detector performance, independent uncertainty calibration, final-test promotion, and long-duration use with field data remain unverified. Physics-model limitations, data independence, measurement noise, irregular sampling, and operational complexity must be addressed as the framework progresses. The roadmap prioritizes those gaps while preserving human decision authority.',
270:'The practical challenge is to connect established machine-learning methods with the governance and quality assurance requirements of environmental decision support. Uncertainty quantification, drift detection, continual learning, and active learning each address part of surrogate maintenance. Their integration must establish when action is justified, how a candidate is evaluated, and who can approve its use. This report addresses that connection for EM groundwater applications.',
271:'The report defines a structured framework for surrogate monitoring and lifecycle management and evaluates its update decision using available pump-and-treat U-Net evidence. It distinguishes completed offline comparisons from the prospective detection, uncertainty calibration, and independent promotion records needed for operational use.',
284:'Section 5.0 presents the controlled pump-and-treat U-Net case study, connects the reported update results to all seven lifecycle steps, and identifies the evidence required beyond the present calibration and deployment hold.',
285:'Section 6.0 discusses the measured findings, current limitations, remaining validation tasks, and conclusions. Appendix A provides the curated surrogate-literature table supporting Section 3.2.3.',
314:'Figure 2 shows the seven-step cycle organized into two phases. Phase 1, Continuous Monitoring, encompasses MONITOR, DETECT, and DECIDE. Phase 2, Triggered Response, encompasses PREPARE, UPDATE, CALIBRATE, and DEPLOY and begins when governance approves an update. The figure describes the intended operational workflow; the evidence status of its implementation is assessed in Section 5.0.',
346:'CALIBRATE fits or assesses the uncertainty procedure using held-out calibration data that are separate from training and controller selection, then reports empirical coverage, interval width, and reliability across relevant regimes and locations. Calibration parameters and the applicable assumptions are archived. An untouched final test remains reserved for DEPLOY.',
353:'DEPLOY draws from Pillar A for acceptance criteria, review authority, audit requirements, and withdrawal procedures, and from Pillar B for model versioning and artifact management. Its output is either an approved model with a complete record or a documented hold or escalation decision. Routine calculations may be automated, while intervention and promotion remain governed decisions.',
485:'Published groundwater and subsurface applications demonstrate the breadth of DL surrogate methods and their potential to accelerate numerical-model predictions (Luo et al. 2023; Xu and Zhang 2024). Figure 3 summarizes publication years in the curated literature table used here. This selected sample supplies methodological context; its counts are not a census or an estimate of field-wide publication growth.',
488:'The curated table retains 45 representative entries spanning five primary surrogate families (Appendix A, Table A.1). Figure 4 groups those entries by publication year and inherited primary family. The table includes journal articles and preprints and is intended to illustrate methodological diversity. Ambiguous source mappings were excluded from the plotted counts rather than assigned an inferred identity.',
491:'Figure 5 identifies the five model families discussed below. Their suitability depends on the prediction target, available data, temporal structure, and uncertainty requirements; the associated applications and limitations are described in the text.',
501:'Variational autoencoders, generative adversarial networks, and diffusion models can represent ensembles of states or parameter fields for probabilistic inversion and uncertainty quantification. Representative applications include Bayesian inversion of generative models for CO₂ storage (Graham and Chen 2020), diffusion models for multivariate subsurface property fields (Miele and Linde 2025), pretrained diffusion for subsurface flow (Wang et al. 2025b), and conditional diffusion for geological CO₂ storage prediction (Wang et al. 2025a). Physical and observational consistency depend on the model construction and validation.',
505:'Figure 6 summarizes the 45 retained entries by primary family, application, and project domain. In this selected table, classical surrogates are concentrated in design and optimization, while operator-learning examples are concentrated in forward emulation. Convolutional, sequence, and generative examples cover other combinations. These descriptive counts organize the examples; they do not establish method superiority or field-wide prevalence.',
506:'The table emphasizes contaminant remediation and groundwater flow, with additional examples from CO₂ storage, coastal aquifers, and general scientific computing. These examples motivate considering a range of architectures; their appearance across domains does not itself demonstrate transferability to a new site or task.',
517:'Uncertainty quantification supports evaluation of predictive reliability in both surrogate modeling and data assimilation. Surrogate uncertainty and physics-model uncertainty address different sources of error and should be reported separately. Their estimates can inform monitoring and update decisions, but physical consistency and interval calibration must be checked rather than inferred from the presence of an uncertainty method.',
530:'Provides marginal prediction-interval coverage under stated assumptions such as exchangeability; distribution shift and temporal dependence require additional care',
627:'Continual-learning reviews describe opportunities and limitations in predictive maintenance and energy-management applications (Hurtado et al. 2023; Sayed et al. 2025). Groundwater surrogate reviews and active-learning studies provide complementary context for model refinement (Asher et al. 2015; Wang et al. 2023). These sources motivate evaluating update strategies; they do not establish that a particular replay ratio, update schedule, or computational saving transfers to groundwater plume prediction. Section 5.0 provides the report-specific update evidence.',
629:'Step 1: Assemble Update Dataset. Assemble a traceable update dataset from relevant new simulations or validated observations and historical replay. Approximately 70–75% historical replay is the framework’s illustrative starting guidance, not a universal optimum or a verified composition for the present study. The ratio should be assessed against paired historical/new validation outcomes; replay itself is supported by the continual-learning literature (De Lange et al. 2021).',
632:'Step 4: Uncertainty Recalibration. Recalibrate predictive intervals using independent held-out data and evaluate empirical coverage and interval width. Deep ensembles or other uncertainty estimators supply candidate predictive distributions; calibration and final testing remain distinct tasks. Apply the surrogate-level UQ methods in Section 3.3.1 under their stated assumptions (Lakshminarayanan et al. 2017; Zhu and Zabaras 2018).',
633:'Step 5: Governance Review. Prepare a record of pre- and post-update performance, trigger evidence, data provenance, and uncertainty diagnostics under Section 3.1. Promote the candidate only after all applicable acceptance conditions are met. A failed candidate remains unapproved; when the incumbent’s operational validity is in question, surrogate use is withdrawn and the governed retraining policy in Section 3.1.5 applies. Archiving a prior model does not authorize its continued use.',
653:'Step 2: Apply Diversity Constraints and Select Batch. Apply diversity constraints so that selected scenarios span relevant hydraulic gradients, hydrostratigraphic units, and forcing conditions, limiting redundant sampling. Select a batch intended to improve information coverage under the simulation budget, and record its scores and rationale. Simulation designs in related subsurface applications provide context for such coverage (Wen et al. 2021); their results do not establish an optimum batch size for this workflow.',
658:'Combining low-fidelity ensembles with targeted high-fidelity data can reduce data-generation cost when the fidelity relationship is informative. The achieved accuracy and savings depend on the fidelity gap, validation design, and computational budget and must be measured for the application. The strategies below describe ways to integrate these information sources (Asher et al. 2015).',
731:'The first development phase aims to complete a reproducible lifecycle demonstration on a controlled test case. Section 5.0 supplies the current offline U-Net update evidence; prospective detector evaluation, independent uncertainty calibration, and final-test promotion are the remaining milestones.',
732:'The current prototype uses the pump-and-treat U-Net trained on synthetic physics-model outputs. The next increment will preserve trajectory identity, resolve the time axis and sampling protocol, freeze detection and acceptance criteria, and compare candidate updates under a common evaluation design. It will then calibrate predictive uncertainty and evaluate an untouched final test. These steps can be executed manually with reproducible scripts and an explicit reviewer record before a persistent monitoring service is developed.',
733:'The next deliverable is a reproducible evidence package containing executed configurations, split manifests, predictions, detector diagnostics, update comparisons, calibration outputs, and the final decision. A candidate that fails a gate remains unapproved. Completion is defined by a documented and scientifically valid evaluation, not by assuming that every candidate must pass.',
734:'Phase 1 success requires traceability across MONITOR → DETECT → DECIDE → PREPARE → UPDATE → CALIBRATE → DEPLOY and a justified promotion or hold decision. The present study reaches a quantitative update comparison and a calibration/final-validation hold; the missing evidence is listed in Section 5.0.',
748:'Physics simulations and surrogate training require resources matched to problem size and solver or network configuration. Large training ensembles should run through HPC batch scheduling. The simulation-driven PREPARE pathway uses approximately 6–10 targeted runs as an illustrative initial batch, with expansion governed by the evidence and budget. Training, update, inference, and uncertainty-processing times must be benchmarked on specified hardware; the current adaptive-replay evidence does not supply an end-to-end cost comparison.',
749:'Inference and diagnostic calculations may be less costly than physics simulations, but their operational cost depends on model size, monitoring frequency, ensemble size, and data volume. Resource planning should use measured throughput and include uncertainty-processing and data-transfer costs.',
767:'The roadmap defines how adaptive surrogate maintenance could be implemented with appropriate scientific and governance controls. Its operational benefits remain objectives to be demonstrated through the phased evidence requirements. The current case study supplies update comparisons and identifies the remaining validation work.',
844:'The case study advances the framework with a quantitative offline update comparison and a documented boundary on what can be concluded. This section interprets that evidence, distinguishes the remaining scientific and operational requirements, and connects the next validation tasks to the roadmap in Section 4.0.',
851:'The framework is defined and the U-Net case study supplies controlled update evidence. The available results remain rounded aggregate manuscript values rather than independently reproduced trajectory-level tests. Prospective detection, an independent calibration result, a verified untouched final test, and a model-version promotion record are absent. Field validation with measurement noise, irregular sampling, data gaps, and site complexity also remains to be demonstrated. A retrospective response-based stress partition does not by itself establish an operational regime change.',
853:'The roadmap in Section 4.0 defines development phases, and Section 5.0 identifies the current evidence and its limits. The immediate scientific priorities are to verify the time axis and trajectory split, reconcile panel-specific model configurations, evaluate a matched fixed-replay control, and complete uncertainty calibration and independent final testing. Broader questions concern detector design, multi-fidelity fusion, transferability, and scalability.',
866:'Potential operational benefits include faster scenario exploration and a reduced need to regenerate complete training ensembles when a targeted update is sufficient. Published surrogate applications motivate that possibility, but the current study does not quantify full-lifecycle speedup, physics-run savings, memory, or training cost. Those benefits should be evaluated under a common workload by comparing physics-only analysis, a static surrogate, and the hybrid recalibration workflow.',
868:'The report connects three management domains and seven lifecycle steps to an evidence-based model-maintenance decision. The measured case study shows a material tradeoff between rare-regime recovery and historical retention. The uncertainty and governance gates specify why a candidate that improves point predictions may still require further evaluation. The scientific contribution is this explicit connection between performance evidence, acceptance conditions, and the next action.',
870:'The framework may be adapted to other contaminants, sites, and scientific surrogates, but transferability requires application-specific data, error limits, and governance decisions. Long-horizon forecasting and digital-twin applications are possible extensions rather than results established here. Reusable code and demonstration datasets, when documented and cleared for release, can support independent evaluation and broader adoption.',
872:'Five conclusions follow from the framework and controlled update evidence:',
873:'Surrogate maintenance is a lifecycle problem. Monitoring, evidence-based intervention, uncertainty assessment, and review must accompany model updating when conditions move beyond the evaluated domain.',
874:'Physics-based analysis remains authoritative for final remedy decisions. Surrogates support efficient screening and scenario exploration, while their approximation errors and the limitations of the underlying physics model must both be assessed.',
875:'Historical retention and rare-regime recovery must be evaluated jointly. In the reported comparison, fixed replay reduces rare RMSE from 10.04 to 1.21 µg/L while historical RMSE increases from 0.58 to 1.03 µg/L. That tradeoff makes a pre-established acceptance contract necessary.',
876:'The illustrative controller screen identifies candidates, not approved deployments. Two displayed controller outcomes satisfy the 30%/85% conditions, but uncertainty, matched-control, and independent-test evidence remain necessary to interpret and confirm their performance.',
877:'A documented hold is a valid lifecycle outcome. The current candidates remain awaiting uncertainty calibration and final validation. Completing those records, together with a traceable model version and reviewer decision, is the next step toward a reproducible operational demonstration.',
878:'This revised report moves from a conceptual framework and prototype plan to an evidence-backed account of how a groundwater surrogate update should be assessed. It connects a measured adaptation–retention tradeoff to the seven-step workflow and clearly specifies the evidence still required for promotion. The immediate objective is to complete that evidence chain; reliable long-term field use remains the longer-term validation goal.',
997:'The literature table is a curated selection used to illustrate surrogate families and applications; it is not a systematic review or an exhaustive publication census. The original draft combined an annual Web of Science plot, inconsistent search-window descriptions, and a classified example table. Because the search export and reproducible query record were unavailable for this revision, Figures 3, 4, and 6 are reconstructed from the retained table entries only.',
998:'The retained set contains 45 entries across five model families and includes both journal publications and preprints. Two inherited rows with unresolved author–year mappings were excluded: a generative-model entry labeled Yang et al. (2018) and a monitoring entry labeled Chen et al. (2022). A duplicated Tang et al. (2020) citation was removed from the Majumder and Eldho row, and the Wang et al. (2025a) conditional-diffusion entry was classified as generative. The remaining primary labels are descriptive and should not be interpreted as an independently re-screened or statistically representative sample. Reviews by Razavi et al. (2012) and Asher et al. (2015) supply broader context.',
}
for i,new in edits.items():edit(i,new,'Align evidence, governance, scope, or source traceability')
# Keep the conclusions concise: the final numbered takeaway already states the
# next action, so a second closing paragraph would only repeat it.
audit.append({'source_paragraph':878,'old':text(ps[878]),'new':'','reason':'Remove repetitive closing paragraph after the five conclusions'})
ps[878].getparent().remove(ps[878])
for el in ps:
    st=el.xpath('./w:pPr/w:pStyle/@w:val')
    if st and st[0]=='Acronyms':
        para=Paragraph(el,doc)
        para.paragraph_format.space_before=Pt(0)
        para.paragraph_format.space_after=Pt(0)
        para.paragraph_format.line_spacing=1
        for r in para.runs:r.font.size=Pt(10)
sub(456,'Genuchten 2016','Šimůnek and van Genuchten 2016','Correct chapter author citation using source BibTeX')
sub(495,'Mo et al. 2019','Mo et al. 2019b','Disambiguate the multiphase-flow paper')
sub(509,'Mo et al. 2019','Mo et al. 2019b','Disambiguate the multiphase-flow paper')
sub(622,'is flags','is flagged','Correct grammar')
sub(497,'resolutioninvariant surrogates that generalize across boundary and parameter configurations','surrogates that can be evaluated across discretizations, subject to architecture and training-domain limits','Bound operator-generalization claim')
sub(497,'105speedup','10⁵ speedup','Restore exponent and spacing')
sub(332,'prepareupdate-calibrate-deploy','prepare–update–calibrate–deploy','Correct word join')
sub(281,'sevenstep','seven-step','Correct word join')

# Correct bibliography, preserving existing entries and adding only sourced items.
sub(941,'. 2019.','. 2019a.','Assign suffix to autoregressive inversion paper')
sub(942,'. 2019.','. 2019b.','Assign suffix to convolutional multiphase paper')
sub(972,'. 2025.','. 2025b.','Assign suffix to pretrained diffusion paper')
sub(973,'. 2025.','. 2025a.','Assign suffix to conditional diffusion paper')
edit(904,'Šimůnek, J., and M. Th. van Genuchten. 2016. “Contaminant Transport in the Unsaturated Zone: Theory and Modeling.” In The Handbook of Groundwater Engineering, 3rd ed., 221–254. CRC Press.','Correct authors from literature/references.bib')
# Move corrected chapter to its alphabetical position, before Siade/Song references.
ref_anchor=next(p for p in ps[881:992] if text(p).startswith('Siade,'))
ref_anchor.addprevious(ps[904])
for anchor,new in [
    (ps[881], 'Adaptive Replay for U-Net Groundwater Plume Surrogates: Learning Rare Pump-and-Treat Dynamics Without Forgetting. 2026. Internal manuscript, version dated September 9, 2026. Project source: Adaptive_Replay_Manuscript_2026_09_09.docx.'),
    (next(p for p in ps[881:992] if text(p).startswith('Rogers,')), 'Razavi, S., B. A. Tolson, and D. H. Burn. 2012. “Review of Surrogate Modeling in Water Resources.” Water Resources Research 48 (7). https://doi.org/10.1029/2011WR011527')]:
    p=OxmlElement('w:p');ppr=deepcopy(ps[883].find(qn('w:pPr')))
    if ppr is not None:p.append(ppr)
    rewrite(p,new,record=False);anchor.addprevious(p)
    audit.append({'old':'','new':new,'reason':'Add source reference used in report'})

# Replace Appendix A table with the exact data behind the descriptive graphics.
table=doc.tables[-1]
for row in list(table.rows)[1:]:table._tbl.remove(row._tr)
with (ROOT/'sources/literature_curated.csv').open() as f:
    for row in csv.DictReader(f):
        cells=table.add_row().cells
        for cell,value in zip(cells,row.values()):
            cell.text=value
            for p in cell.paragraphs:
                p.style=doc.styles['Table Text'] if 'Table Text' in doc.styles else doc.styles['Normal']
                p.paragraph_format.space_before=Pt(1)
                p.paragraph_format.space_after=Pt(1)
                p.paragraph_format.line_spacing=1
                for r in p.runs:r.font.size=Pt(9)

def caption(el,kind,number,description,appendix=False):
    names=[(b.get(qn('w:id')),b.get(qn('w:name'))) for b in el.xpath('./w:bookmarkStart')]
    for c in list(el):
        if c.tag!=qn('w:pPr'):el.remove(c)
    for bid,name in names:
        b=OxmlElement('w:bookmarkStart');b.set(qn('w:id'),bid);b.set(qn('w:name'),name);el.append(b)
    p=Paragraph(el,doc);p.add_run(kind+' ')
    fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),f' SEQ {kind} \\* ARABIC ')
    r=OxmlElement('w:r');t=OxmlElement('w:t');t.text=str(number);r.append(t);fld.append(r);el.append(fld)
    for bid,_ in names:
        e=OxmlElement('w:bookmarkEnd');e.set(qn('w:id'),bid);el.append(e)
    p.add_run('. '+description)

captexts={
312:('Figure',1,'Three complementary management domains. Governance sets the rules and decision authority, modeling engines provide the physics-based reference and surrogate, and recalibration mechanisms supply methods for evaluation and updating. The arrows show their principal information exchanges.'),
317:('Figure',2,'Seven-step recalibration workflow. MONITOR, DETECT, and DECIDE form continuous monitoring; PREPARE, UPDATE, CALIBRATE, and DEPLOY form the triggered response. DECIDE is the human governance gate. A successful deployment returns to monitoring. Full retraining is a governed escalation path, not an additional lifecycle step.'),
487:('Figure',3,'Publication years of the 45 retained entries in Appendix A, Table A.1. Entries from 1994–2016 are grouped. The curated sample illustrates the literature used in this report; it is not a field-wide publication census or a measure of publication-growth rates.'),
490:('Figure',4,'Primary surrogate families by publication year in the 45-entry curated table. Each retained row contributes once under its primary label. The sample includes journal publications and preprints; counts describe the retained table rather than a systematic literature search.'),
493:('Figure',5,'Five surrogate-model families used to organize the methods discussion. Input–output relationships, representative applications, and limitations are described in Section 3.2.3.'),
508:('Figure',6,'Descriptive counts in the retained literature table by primary surrogate family and application (top) or project domain (bottom). Each retained entry contributes once to each panel. These classifications summarize the curated sample and do not establish relative method performance or field-wide prevalence.'),
}
for i,args in captexts.items():caption(ps[i],*args)
rewrite(ps[999],'Table A.1. Retained curated entries used for the descriptive literature figures. The selection includes journal articles and preprints; classifications are illustrative.',record=True)

for i,name in [(311,'figure01_pillars'),(316,'figure02_workflow'),(486,'figure03_curated_years'),(489,'figure04_curated_families'),(492,'figure05_families'),(507,'figure06_curated_matrix')]:
    p=Paragraph(ps[i],doc)
    for c in list(p._p):
        if c.tag!=qn('w:pPr'):p._p.remove(c)
    p.add_run().add_picture(str(ROOT/'figures'/f'{name}.png'),width=Inches(6.35))
    p.paragraph_format.left_indent=Inches(0);p.paragraph_format.right_indent=Inches(0)
    p.paragraph_format.keep_with_next=True

# Replace both the old Section 5 and the incomplete duplicate, keeping the chapter anchor.
chapter=ps[768];end=ps[843]
removed=[];node=chapter.getnext()
while node is not end:
    nxt=node.getnext();removed.append(node);node.getparent().remove(node);node=nxt
rewrite(chapter,'Prototype Demonstration and Pump-and-Treat Lifecycle Case Study','Replace duplicate/legacy Section 5 with the complete case study')
md=(ROOT/'section5_20261028.md').read_text();blocks=re.split(r'\n\s*\n',md.strip())
new_elements=[]
for block in blocks[1:]:
    if block.startswith('|'):
        rows=[[s.strip() for s in row.strip().strip('|').split('|')] for row in block.splitlines()]
        rows=[row for row in rows if not all(re.fullmatch(r'[:\- ]+',s or '-') for s in row)]
        tbl=doc.add_table(rows=0,cols=len(rows[0]));tbl.autofit=False
        widths=([1.65,1.15,1.15,1.15,1.2] if len(rows[0])==5 else [2.5]+[4/(len(rows[0])-1)]*(len(rows[0])-1))
        if len(rows[0])==3:widths=[.9,2.75,2.85]
        for vals in rows:
            cells=tbl.add_row().cells
            for c,val,w in zip(cells,vals,widths):
                c.width=Inches(w);c.text=val
                for p in c.paragraphs:
                    p.paragraph_format.space_before=Pt(3);p.paragraph_format.space_after=Pt(3)
                    for r in p.runs:r.font.name='Arial';r.font.size=Pt(9)
            trpr=tbl.rows[-1]._tr.get_or_add_trPr();trpr.append(OxmlElement('w:cantSplit'))
        head=tbl.rows[0]._tr.get_or_add_trPr();head.append(OxmlElement('w:tblHeader'))
        for c in tbl.rows[0].cells:
            sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'E8EEF2');c._tc.get_or_add_tcPr().append(sh)
            for p in c.paragraphs:
                for r in p.runs:r.bold=True
        # These are small result/evidence tables. Keep each complete table with
        # its caption rather than leaving the last data row on a new page.
        for row in tbl.rows[:-1]:
            for cell in row.cells:
                for p in cell.paragraphs:p.paragraph_format.keep_with_next=True
        new_elements.append(tbl._tbl);end.addprevious(tbl._tbl)
        continue
    p=doc.add_paragraph(style='Body Text');new_elements.append(p._p);end.addprevious(p._p)
    if block.startswith('## '):p.style='Heading 2';p.add_run(block[3:])
    elif block.startswith('!['):
        name=block[2:-1];p.style='Figure';p.add_run().add_picture(str(ROOT/'figures'/f'{name}.png'),width=Inches(6.35))
        p.paragraph_format.left_indent=Inches(0);p.paragraph_format.right_indent=Inches(0)
    elif re.match(r'^(Figure|Table) \d+\.',block):
        m=re.match(r'^(Figure|Table) (\d+)\. (.*)',block,flags=re.S)
        p.style='Caption-Fig' if m[1]=='Figure' else 'Caption-Tab';caption(p._p,m[1],int(m[2]),m[3])
    else:
        for j,part in enumerate(re.split(r'\*([^*]+)\*',block.replace('\n',' '))):p.add_run(part).italic=bool(j%2)

# Repair surviving references into removed legacy subsections by anchoring them
# to the new case-study chapter; TOC entries are regenerated by Word.
remaining_names={b.get(qn('w:name')) for b in doc.element.body.xpath('.//w:bookmarkStart')}
instructions=' '.join(doc.element.body.xpath('.//w:instrText/text()')+[e.get(qn('w:instr'),'') for e in doc.element.body.xpath('.//w:fldSimple')])
refnames=set(re.findall(r'\bREF\s+(_Ref\w+)',instructions))
missing=refnames-remaining_names
maxid=max(int(b.get(qn('w:id'))) for b in doc.element.body.xpath('.//w:bookmarkStart'))+1
for name in sorted(missing):
    if not any(name==b.get(qn('w:name')) for e in removed for b in e.xpath('.//w:bookmarkStart')):
        raise RuntimeError('Unexpected missing cross-reference '+name)
    s=OxmlElement('w:bookmarkStart');s.set(qn('w:id'),str(maxid));s.set(qn('w:name'),name)
    e=OxmlElement('w:bookmarkEnd');e.set(qn('w:id'),str(maxid));chapter.insert(1,s);chapter.append(e);maxid+=1

# Remove inherited review markup only in the new clean copy. Original comments
# and their anchors remain in the source snapshot and disposition ledger.
for element in doc.element.body.xpath('.//w:commentRangeStart|.//w:commentRangeEnd|.//w:commentReference'):
    element.getparent().remove(element)
for el in doc.settings.element.xpath('./w:trackRevisions'):doc.settings.element.remove(el)
settings=doc.settings.element
for old in settings.xpath('./w:updateFields'):settings.remove(old)
uf=OxmlElement('w:updateFields');uf.set(qn('w:val'),'false');settings.append(uf)
intermediate=ROOT/'qa/Framework_20261028_before_word.docx'
doc.save(intermediate)
# Strip orphaned comment parts, while preserving all unrelated package content.
with ZipFile(intermediate) as z:data={n:z.read(n) for n in z.namelist()}
for n in data:
    if n.endswith('.xml'):
        data[n]=data[n].replace(b'PNNL-XXXXX',b'Revision draft')
        data[n]=data[n].replace(b'April 2026','October 2026 — Revision draft'.encode('utf-8'))
        if n.startswith('customXml/'):
            data[n]=data[n].replace(b'2026-04-01T00:00:00',b'2026-10-01T00:00:00')
removed_parts=[n for n in data if n.startswith('word/comments')]
for n in removed_parts:del data[n]
for n in ['[Content_Types].xml','word/_rels/document.xml.rels']:
    tree=etree.fromstring(data[n])
    for e in list(tree):
        target=e.get('PartName','').lstrip('/') if n.startswith('[') else 'word/'+e.get('Target','')
        if target in removed_parts:tree.remove(e)
    data[n]=etree.tostring(tree,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile(intermediate,'w',ZIP_DEFLATED) as z:
    for n,b in data.items():z.writestr(n,b)
(ROOT/'qa/text_change_log.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
(ROOT/'qa/assembly.json').write_text(json.dumps({'source':str(SOURCE),'output':str(intermediate),'paragraph_edits':len(audit),'section5_blocks':len(new_elements),'redirected_cross_references':sorted(missing),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest()},indent=2))
print('Built',intermediate,'with',len(audit),'documented edits and',len(new_elements),'new Section 5 blocks.')

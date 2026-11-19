"""Reproducible report graphics: labels only; explanations belong in captions."""
from pathlib import Path
import json, csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
OUT = ROOT / 'figures'
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10, 'axes.labelsize':10,
    'axes.spines.top':False, 'axes.spines.right':False, 'axes.linewidth':.7,
    'xtick.labelsize':9, 'ytick.labelsize':9, 'savefig.facecolor':'white',
    'pdf.fonttype':42, 'svg.fonttype':'none'})
BLUE, ORANGE, GREEN, PURPLE, GREY = '#28658a','#c87832','#3b8074','#8571a8','#777777'

def save(fig, name):
    for ext in ['png','pdf','svg']:
        fig.savefig(OUT/f'{name}.{ext}', dpi=300, bbox_inches='tight', pad_inches=.08)
    plt.close(fig)

def canvas(w,h):
    fig, ax=plt.subplots(figsize=(w,h)); ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    return fig,ax

def box(ax,x,y,w,h,label,edge=BLUE,fill='#f1f5f7',fs=10):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.012,rounding_size=0.018',
                 linewidth=1.1,edgecolor=edge,facecolor=fill,zorder=3))
    ax.text(x,y,label,ha='center',va='center',fontsize=fs,zorder=4)

def arrow(ax,a,b,color='#555555',style='-|>',rad=0):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle=style,mutation_scale=11,lw=1,
                 color=color,connectionstyle=f'arc3,rad={rad}',zorder=2))

# Figure 1: the three management domains; no internal prose or headline.
fig,ax=canvas(6.4,3)
box(ax,.5,.78,.38,.21,'A  Conceptual design\n& governance')
box(ax,.23,.22,.36,.21,'B  Modeling engines')
box(ax,.77,.22,.36,.21,'C  Recalibration\nmechanisms')
arrow(ax,(.40,.66),(.27,.34)); arrow(ax,(.60,.66),(.73,.34))
arrow(ax,(.43,.22),(.57,.22),style='<->')
save(fig,'figure01_pillars')

# Figure 2: a single seven-step cycle with explicit governance and escalation.
fig,ax=canvas(6.5,3.6)
positions=[(.13,.77),(.43,.77),(.76,.77),(.87,.29),(.62,.29),(.37,.29),(.12,.29)]
labels=['1  MONITOR','2  DETECT','3  DECIDE','4  PREPARE','5  UPDATE','6  CALIBRATE','7  DEPLOY']
for k,((x,y),label) in enumerate(zip(positions,labels)):
    box(ax,x,y,.205,.17,label,edge=BLUE if k<3 else GREEN,
        fill='#e6eef3' if k==2 else '#ffffff',fs=9)
arrow(ax,(.245,.77),(.315,.77));arrow(ax,(.545,.77),(.645,.77))
arrow(ax,(.81,.67),(.86,.395))
for a,b in zip([.755,.505,.255],[.735,.485,.235]): arrow(ax,(a,.29),(b,.29))
arrow(ax,(.12,.395),(.13,.665))
box(ax,.51,.51,.31,.12,'Full retraining',edge=GREY,fill='#ffffff',fs=9)
arrow(ax,(.70,.665),(.61,.58),color=GREY)
arrow(ax,(.51,.44),(.61,.395),color=GREY)
save(fig,'figure02_workflow')

# Retain only unambiguous entries from the inherited curated literature table.
rows=json.loads((ROOT/'sources/literature_table.json').read_text())[1:]
clean=[]; excluded=[]
for row in rows:
    year,family,application,domain,ref=row
    if ref=='Yang et al. 2018' or (ref=='Chen et al. 2022' and application=='Monitoring & time-series prediction'):
        excluded.append(row);continue
    if ref=='Majumder and Eldho 2020; Tang et al. 2020':ref='Majumder and Eldho 2020'
    if ref=='Moet al. 2019':ref='Mo et al. 2019b'
    if ref=='Wang et al. 2025':ref='Wang et al. 2025a';family='Generative models'
    clean.append([year,family,application,domain,ref])
assert len(clean)==45
with (ROOT/'sources/literature_curated.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['year','family','application','domain','reference']);w.writerows(clean)
(ROOT/'sources/literature_excluded.json').write_text(json.dumps(excluded,indent=2))
families=['Regression & classical surrogates','Conv encoder-decoder','Operator-learning','Sequence models','Generative models']
short=['Regression / classical','Conv. encoder–decoder','Operator learning','Sequence models','Generative models']
colors=[GREY,BLUE,GREEN,ORANGE,PURPLE]
years=['1994–2016']+[str(y) for y in range(2017,2026)]
counts=np.zeros((len(families),len(years)),dtype=int)
for y,fam,*_ in clean:counts[families.index(fam),0 if int(y)<=2016 else int(y)-2016]+=1
assert counts.sum()==45
fig,ax=plt.subplots(figsize=(6.4,2.8)); ax.bar(years,counts.sum(axis=0),width=.68,color=BLUE)
ax.set_ylabel('Curated entries'); ax.set_xlabel('Publication year');ax.set_ylim(0,10)
ax.set_yticks(range(0,11,2));ax.tick_params(axis='x',rotation=40);ax.yaxis.grid(True,color='#eeeeee');ax.set_axisbelow(True)
save(fig,'figure03_curated_years')
fig,ax=plt.subplots(figsize=(6.4,3.3));bottom=np.zeros(len(years))
for values,label,color in zip(counts,short,colors):ax.bar(years,values,bottom=bottom,width=.68,label=label,color=color);bottom+=values
ax.set_ylabel('Curated entries');ax.set_xlabel('Publication year');ax.set_ylim(0,10);ax.set_yticks(range(0,11,2))
ax.tick_params(axis='x',rotation=40);ax.legend(frameon=False,ncol=2,loc='lower left',bbox_to_anchor=(0,1.01),fontsize=8)
save(fig,'figure04_curated_families')

fig,ax=canvas(6.4,3.6)
box(ax,.5,.5,.26,.18,'Surrogate models',fill='#e6eef3')
for x,y,label in [(.2,.82,'Convolutional\nencoder–decoder'),(.8,.82,'Operator learning'),(.87,.25,'Sequence models'),(.50,.10,'Generative models'),(.13,.25,'Regression /\nclassical')]:
    arrow(ax,(.5,.5),(x,y),style='-');box(ax,x,y,.235,.15,label,fs=9)
save(fig,'figure05_families')

apps=sorted(set(r[2] for r in clean));domains=sorted(set(r[3] for r in clean))
app_labels={'Design & optimization':'Design /\noptimization','Forward emulation':'Forward\nemulation','Inverse & calibration':'Inverse /\ncalibration','Monitoring & time-series prediction':'Monitoring /\nforecasting','UQ & ensemble generation':'UQ /\nensembles'}
domain_labels={'CO2 storage / geoenergy':'CO₂ storage /\ngeoenergy','Coastal aquifers / seawater intrusion':'Coastal\naquifers','Contaminant hydrogeology / remediation':'Contaminant\nremediation','General scientific computing':'Scientific\ncomputing','Groundwater flow / fluid mechanics':'Groundwater\nflow','Groundwater monitoring & forecasting':'Groundwater\nmonitoring'}
fig,axes=plt.subplots(2,1,figsize=(6.4,5.3),layout='constrained')
for ax,cats,col,labmap in zip(axes,[apps,domains],[2,3],[app_labels,domain_labels]):
    mat=np.zeros((5,len(cats)),int)
    for row in clean:mat[families.index(row[1]),cats.index(row[col])]+=1
    im=ax.imshow(mat,cmap='Blues',vmin=0,vmax=14,aspect='auto')
    ax.set_xticks(range(len(cats)),[labmap[c] for c in cats],fontsize=8)
    ax.set_yticks(range(5),short,fontsize=8);ax.tick_params(length=0)
    for (i,j),v in np.ndenumerate(mat):ax.text(j,i,str(v),ha='center',va='center',fontsize=8,color='white' if v>7 else '#333333')
fig.colorbar(im,ax=axes,shrink=.75,label='Curated entries',ticks=[0,4,8,12,14])
save(fig,'figure06_curated_matrix')

# Case-study schematic: only model inputs, outputs, and functional labels.
fig,ax=canvas(6.4,3.4)
box(ax,.16,.82,.24,.15,'Plume at t')
box(ax,.16,.30,.24,.15,'Pumping wells')
box(ax,.43,.30,.22,.15,'Thiem field')
box(ax,.54,.69,.20,.18,'U-Net')
box(ax,.85,.69,.24,.18,'Predicted plume\nat t + 1')
box(ax,.85,.29,.24,.15,'Error metrics')
box(ax,.55,.07,.25,.12,'Reference plume')
arrow(ax,(.29,.80),(.43,.73));arrow(ax,(.29,.30),(.31,.30))
arrow(ax,(.45,.39),(.51,.59));arrow(ax,(.65,.69),(.72,.69))
arrow(ax,(.85,.59),(.85,.38));arrow(ax,(.69,.10),(.80,.21))
save(fig,'figure07_unet')

analysis=REPO/'analyses/seven_step_lifecycle_20261007/derived'
with (analysis/'figure5_controller_values.csv').open() as f:gate=list(csv.DictReader(f))
fig,ax=plt.subplots(figsize=(6.1,3.8))
ax.axvspan(0,30,ymin=(85-80)/12,ymax=1,color='#eff4f1',zorder=0)
ax.axvline(30,color=GREY,lw=1,ls='--');ax.axhline(85,color=GREY,lw=1,ls='--')
for row,label,color,marker in zip(gate,['Fixed replay','Threshold adaptive','Loss-balanced','Loss-balanced + floor'],[GREY,BLUE,GREEN,ORANGE],['s','o','^','D']):
    ax.scatter(float(row['historical_degradation_percent']),float(row['rare_improvement_percent']),label=label,s=55,c=color,marker=marker,edgecolors='white',linewidths=.5,zorder=3)
ax.set(xlim=(0,90),ylim=(80,92),xlabel='Historical RMSE increase (%)',ylabel='Rare RMSE reduction (%)')
ax.set_xticks(range(0,91,15));ax.set_yticks(range(80,93,2));ax.legend(frameon=False,ncol=2,loc='lower left',bbox_to_anchor=(0,1.02),fontsize=9)
save(fig,'figure08_acceptance')

with (analysis/'figure4_metric_values.csv').open() as f:metrics=list(csv.DictReader(f))
fig,ax=plt.subplots(figsize=(6.1,3.6));x=np.arange(4)
ax.bar(x-.18,[float(r['historical_rmse']) for r in metrics],.34,color=BLUE,label='Historical')
ax.bar(x+.18,[float(r['rare_rmse']) for r in metrics],.34,color=ORANGE,label='Rare')
ax.set_xticks(x,['Baseline','Simple\nfine-tuning','Fixed replay','EWC']);ax.set_ylabel('RMSE (µg/L)')
ax.set_ylim(0,11);ax.set_yticks([0,2,4,6,8,10]);ax.legend(frameon=False,loc='upper right')
ax.yaxis.grid(True,color='#eeeeee');ax.set_axisbelow(True)
save(fig,'figure09_rmse')
print('Created nine figures in PNG, PDF, and SVG; curated literature count = 45.')

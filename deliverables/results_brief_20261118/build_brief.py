"""Build the meeting brief from the frozen pilot and existing replay results."""
import base64
import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import rankdata

OUT = Path(__file__).resolve().parent
REPO = OUT.parents[1]
PILOT = REPO / 'analyses/monitoring_pilot_20261118'
OLD = REPO / 'deliverables/results_slides_20261029'
METHODS = [('sparse_rms', 'sensor_rms', '16-location concentration change', '#b75b22'),
           ('previous_full_field_mass90_change', 'previous_change', 'Full-field footprint change', '#17677a')]


def embed(path):
    return 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode()


def main():
    for line in (PILOT/'outputs.sha256').read_text().splitlines():
        expected, name = line.split()
        assert hashlib.sha256((PILOT/name).read_bytes()).hexdigest() == expected
    result = json.loads((PILOT/'result.json').read_text())
    cases = np.genfromtxt(PILOT/'case_scores.csv', delimiter=',', names=True, dtype=None, encoding='utf8')
    assert np.array_equal(cases['case_id'], np.arange(10000))
    reference = cases[cases['partition']=='reference']
    test = cases[cases['partition']=='evaluation']
    assert len(reference) == len(test) == 5000
    for data in (reference, test):
        for name, first, last in [('previous_change', 'size90_1','size90_2'), ('next_change','size90_2','size90_3')]:
            np.testing.assert_allclose(data[name], abs(data[last]-data[first])/data[first])
    cutoff = np.quantile(reference['next_change'], .97)
    assert cutoff == result['event_cutoff']
    truth = test['next_change'] >= cutoff
    assert np.array_equal(truth, test['event'])
    assert np.all(test['size90_3'][truth] < test['size90_2'][truth])
    metrics = result['metrics']
    fig, (ax, bx) = plt.subplots(1,2,figsize=(9.5,3.75),layout='constrained')
    for key, column, label, color in METHODS:
        row = metrics[key]
        limit = np.quantile(reference[column][reference['next_change']<cutoff], .95)
        assert limit == row['alarm_threshold']
        scores = test[column]
        alarm = scores > limit
        for name, mask in [('tp',alarm & truth),('fp',alarm & ~truth),('fn',~alarm & truth),('tn',~alarm & ~truth)]:
            assert int(mask.sum()) == row[name]
        # Rank-based AUC handles ties. Each threshold on the plot includes its entire tie group.
        pos, neg = truth.sum(), (~truth).sum()
        auc = (rankdata(scores)[truth].sum()-pos*(pos+1)/2)/(pos*neg)
        np.testing.assert_allclose(auc,row['roc_auc'])
        order = np.argsort(-scores)
        ends = np.r_[np.flatnonzero(np.diff(scores[order])!=0),len(order)-1]
        ax.plot(np.r_[0,np.cumsum(~truth[order])[ends]/neg],np.r_[0,np.cumsum(truth[order])[ends]/pos],
                color=color,linewidth=2,label=label)
        ax.scatter(row['false_alarm_rate'],row['sensitivity'],s=42,color=color,edgecolor='black',linewidth=.6,zorder=4,clip_on=False)
    ax.plot([0,1],[0,1],color='.6',linestyle=':',zorder=0)
    ax.set(xlabel='False-positive rate',ylabel='Sensitivity',xlim=(-.015,1.015),ylim=(-.025,1.025))
    ax.legend(fontsize=8,frameon=False,loc='center',bbox_to_anchor=(.52,.47))
    bins=np.arange(0, 1.025, .025)
    for mask,color,label in [(~truth,'#72838c','Other trajectories'),(truth,'#17677a','Large next change')]:
        values=test['previous_change'][mask]
        assert values.max() <= bins[-1]
        bx.stairs(np.histogram(values,bins)[0]*100/len(values),bins,label=label,color=color,linewidth=2)
    bx.axvline(metrics[METHODS[1][0]]['alarm_threshold'],color='.35',ls='--',lw=1,label='Alarm threshold')
    bx.set(xlabel='Previous relative footprint change',ylabel='Trajectories in group (%)',xlim=(0,.62))
    bx.legend(frameon=False,fontsize=8)
    for axis, letter in [(ax,'a'),(bx,'b')]:
        axis.text(-.12,1.03,letter,transform=axis.transAxes,fontweight='bold')
        axis.spines[['top','right']].set_visible(False)
    for ext in ['png','pdf']:
        fig.savefig(OUT/f'monitoring_trigger.{ext}',dpi=200,bbox_inches='tight')
    plt.close(fig)
    med_event, med_other = [round(float(np.median(test['sensor_rms'][mask])),1) for mask in (truth,~truth)]
    assert (int(truth.sum()),med_event,med_other)==(142,15.1,27.5)
    assert (metrics['sparse_rms']['tp'],metrics['sparse_rms']['fp'],
            metrics['previous_full_field_mass90_change']['tp'],metrics['previous_full_field_mass90_change']['fp']) == (0,229,140,230)
    with (OLD/'sources/figure4_metric_values.csv').open() as f:
        rows={r['method']:r for r in csv.DictReader(f)}
    assert [(rows[k]['historical_rmse'],rows[k]['rare_rmse']) for k in ('Baseline','Fixed_replay')]==[('0.58','10.04'),('1.03','1.21')]
    template=(OUT/'template.html').read_text()
    page=template.replace('{{pilot}}',embed(OUT/'monitoring_trigger.png')).replace('{{replay}}',embed(OLD/'figures/02_rmse_comparison.png'))
    assert '{{' not in page
    (OUT/'index.html').write_text(page)


if __name__=='__main__':
    main()

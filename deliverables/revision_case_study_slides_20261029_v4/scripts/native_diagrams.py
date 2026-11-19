"""Editable PowerPoint diagrams for the revised case-study deck.

Public functions accept a python-pptx slide and return one native GroupShape.
Geometry follows the v2 figure canvas. All semantic links have attached start
and end connection points; their names start with ``Link:``. Legend rules are
decorative and start with ``Legend:``. No raster or SVG content is inserted.
"""

from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Inches, Pt


INK = '#23323c'
BLUE = '#286787'
TEAL = '#277e78'
ORANGE = '#ba773b'
GREY = '#77828b'
SCALE = 12.23 / 12.5
LEFT = .55
TOP = 1.48 + (4.80 - 4.6 * SCALE) / 2


def _rgb(color):
    return RGBColor.from_string(color.lstrip('#'))


def _flat(shape):
    """Override the PowerPoint theme's default drop shadow on new shapes."""
    for ref in shape._element.xpath('./p:style/a:effectRef'):
        ref.set('idx', '0')
    sp_pr = shape._element.spPr
    for effects in list(sp_pr.xpath('./a:effectLst | ./a:effectDag')):
        sp_pr.remove(effects)
    sp_pr.append(OxmlElement('a:effectLst'))
    return shape


def _point(x, y):
    return Inches(LEFT + SCALE * x), Inches(TOP + SCALE * (4.6 - y))


def _rect(x, y, w, h):
    left, top = _point(x - w / 2, y + h / 2)
    return left, top, Inches(SCALE * w), Inches(SCALE * h)


def _group(slide, name):
    group = slide.shapes.add_group_shape()
    group.name = name
    group._element.nvGrpSpPr.cNvPr.set('descr',
        'Native editable scientific diagram with attached PowerPoint connectors.')
    return group


def _format_text(shape, text, fs, color=INK, align=PP_ALIGN.CENTER):
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = False
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(.035)
    tf.margin_top = tf.margin_bottom = Inches(.012)
    for i, line in enumerate(text.split('\n')):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.alignment = align
        p.space_before = Pt(0)
        p.space_after = Pt(0)
        p.line_spacing = 1.0
        p.font.name = 'Arial'
        p.font.size = Pt(fs * SCALE)
        p.font.color.rgb = _rgb(color)


def _box(group, x, y, w, h, label, color=GREY, fill='white',
         dashed=False, fs=15):
    shape = group.shapes.add_shape(MSO_SHAPE.RECTANGLE, *_rect(x, y, w, h))
    shape.name = 'Node: ' + label.replace('\n', ' / ')
    shape.fill.solid()
    shape.fill.fore_color.rgb = _rgb('#ffffff' if fill == 'white' else fill)
    shape.line.color.rgb = _rgb(color)
    shape.line.width = Pt(1.3)
    if dashed:
        shape.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    _format_text(shape, label, fs)
    return _flat(shape)


def _text(group, x, y, w, h, text, fs=13, color=INK,
          align=PP_ALIGN.CENTER, opaque=False):
    shape = group.shapes.add_textbox(*_rect(x, y, w, h))
    shape.name = 'Label: ' + text.replace('\n', ' / ')
    if opaque:
        shape.fill.solid()
        shape.fill.fore_color.rgb = _rgb('#ffffff')
    _format_text(shape, text, fs, color, align)
    return _flat(shape)


def _link(group, source, target, source_site=3, target_site=1,
          color=GREY, arrow=True, dashed=False, name=None):
    # Rectangle connection sites: top=0, left=1, bottom=2, right=3.
    conn = group.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, 0, 0, 1, 1)
    conn.name = 'Link: ' + (name or f'{source.name[6:]} -> {target.name[6:]}')
    conn.begin_connect(source, source_site)
    conn.end_connect(target, target_site)
    conn.line.color.rgb = _rgb(color)
    conn.line.width = Pt(1.0 if arrow else .8)
    if dashed:
        conn.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    if arrow:
        # DrawingML tailEnd is the connector's ending (target) arrowhead.
        tail = OxmlElement('a:tailEnd')
        tail.set('type', 'triangle')
        tail.set('w', 'sm')
        tail.set('len', 'sm')
        conn._element.spPr.get_or_add_ln().append(tail)
    # Links stay behind editable nodes and labels, including the row-label mask.
    group._element.remove(conn._element)
    group._element.insert(2, conn._element)
    return _flat(conn)


def _legend(group, x, y, color, label, fs=12, dashed=False):
    a = _point(x, y)
    b = _point(x + .45, y)
    line = group.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, *a, *b)
    line.name = 'Legend: ' + label
    line.line.color.rgb = _rgb(color)
    line.line.width = Pt(2)
    if dashed:
        line.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    _flat(line)
    width = min(3.6, 12.3 - (x + .57))
    _text(group, x + .57 + width / 2, y, width, .35, label, fs,
          align=PP_ALIGN.LEFT)


def draw_plan(slide):
    """Map the planned lifecycle to the types of evidence in the revision."""
    group = _group(slide, 'Key scientific figure: planned lifecycle and evidence')
    steps = ['MONITOR', 'DETECT', 'DECIDE', 'PREPARE', 'UPDATE', 'CALIBRATE', 'DEPLOY']
    evidence = ['Baseline\naggregates', 'Retrospective\nMass90', 'Illustrative\nscreen',
                'Rare cases\n+ replay', 'Update\ncomparisons', 'Interval\ncalibration',
                'Final test\n+ review']
    xs = [.93 + i * (11.57 - .93) / 6 for i in range(7)]
    upper, lower = [], []
    for i, (x, stage, result) in enumerate(zip(xs, steps, evidence)):
        upper.append(_box(group, x, 3.45, 1.5, .63, stage, fs=11.5))
        color = BLUE if i in (0, 3, 4) else ORANGE if i in (1, 2) else GREY
        lower.append(_box(group, x, 1.48, 1.5, .95, result, color,
                          '#f3f7f9' if i < 5 else 'white', i >= 5, fs=12))
        _link(group, upper[-1], lower[-1], 2, 0, color=color, arrow=False,
              name=f'{stage} evidence mapping')
        if i:
            _link(group, upper[-2], upper[-1])
    _text(group, 6.15, 4.20, 11.8, .38, 'Planned lifecycle', 16,
          align=PP_ALIGN.LEFT)
    _text(group, 6.15, 2.45, 11.8, .45, 'Evidence in the revised case study', 16,
          align=PP_ALIGN.LEFT, opaque=True)
    _legend(group, .3, .38, BLUE, 'Reported offline evidence', 11.5)
    _legend(group, 4.7, .38, ORANGE, 'Retrospective / illustrative', 11.5)
    _legend(group, 9.1, .38, GREY, 'Still required', 11.5, dashed=True)
    return group


def draw_stress(slide):
    """Show U-Net prediction and retrospective stress-regime selection."""
    group = _group(slide, 'Key scientific figure: controlled stress test')
    top = [
        _box(group, 1.3, 3.37, 2.05, .80, 'Plume at t\n+ pumping input', BLUE, '#f3f7f9', fs=14),
        _box(group, 4.2, 3.37, 1.65, .80, 'U-Net', BLUE, '#f3f7f9', fs=17),
        _box(group, 7.05, 3.37, 2.0, .80, 'Predicted plume\nat t + 1', BLUE, '#f3f7f9', fs=14),
        _box(group, 10.65, 3.37, 2.05, .80, 'Errors against\nreference', fs=14),
    ]
    for a, b in zip(top, top[1:]):
        _link(group, a, b)
    ref = _box(group, 1.35, 1.13, 2.15, .85, 'Reference plumes\nat t and t + 1', fs=13)
    score = _box(group, 4.17, 1.13, 1.85, .85, 'Mass90\nchange score', ORANGE, '#fbf7f1', fs=14)
    old = _box(group, 7.15, 1.71, 2.35, .72, 'Historical: bottom 40%\ns ≤ 0.133', BLUE, '#f3f7f9', fs=11.5)
    rare = _box(group, 7.15, .56, 2.35, .72, 'Rare: top 3%\ns ≥ 0.329', ORANGE, '#fbf7f1', fs=12)
    update = _box(group, 10.7, 1.13, 2.0, .85, 'Controlled\nupdate', TEAL, '#f3f7f9', fs=14)
    _link(group, ref, score, color=ORANGE)
    _link(group, score, old, color=BLUE)
    _link(group, score, rare, color=ORANGE)
    _link(group, old, update, color=BLUE)
    _link(group, rare, update, color=ORANGE)
    _text(group, 9.0, 2.01, 1.25, .30, 'replay', 12, BLUE)
    _text(group, 9.0, .40, 1.25, .30, 'learning', 12, ORANGE)
    return group


def draw_boundary(slide):
    """Separate the reported screen from required calibration and test roles."""
    group = _group(slide, 'Key scientific figure: validation boundary')
    items = [(1.62, 'Controller\nselection', 'Two candidate\noutcomes', TEAL, False),
             (4.65, 'Independent\ncalibration data', 'Coverage\n+ interval width', GREY, True),
             (7.68, 'Untouched\nfinal-test data', 'Accuracy, UQ\n+ consistency', GREY, True),
             (10.71, 'Versioned\nevidence record', 'Promotion\nreview', GREY, True)]
    lower = []
    for x, upper_label, lower_label, color, pending in items:
        fill = 'white' if pending else '#f4f8f9'
        upper = _box(group, x, 3.25, 2.45, .82, upper_label, color, fill, pending, fs=14)
        lower.append(_box(group, x, 1.75, 2.45, .82, lower_label, color, fill, pending, fs=14))
        _link(group, upper, lower[-1], 2, 0, color)
        if len(lower) > 1:
            _link(group, lower[-2], lower[-1])
    _legend(group, .42, .48, TEAL, 'Reported screen', 13)
    _legend(group, 4.0, .48, GREY, 'Required evidence', 13, dashed=True)
    return group


def draw_next(slide):
    """Show the planned matched experiment; no control outcome is implied."""
    group = _group(slide, 'Key scientific figure: next demonstration')
    items = [('Declared\nchange', BLUE), ('Ordered\ntrajectories', BLUE),
             ('Frozen detector\n+ decision', ORANGE), ('Matched\nupdates', TEAL),
             ('Independent\ncalibration', GREY), ('Final test\n+ review', GREY)]
    nodes = []
    for i, (label, color) in enumerate(items):
        x = 1.05 + i * (11.45 - 1.05) / 5
        nodes.append(_box(group, x, 2.9, 1.78, .96, label, color, fs=13))
        if i:
            _link(group, nodes[-2], nodes[-1])
    adaptive = _box(group, 7.29, 1.25, 2.3, .66, 'Adaptive replay', TEAL, fs=13)
    fixed = _box(group, 4.65, 1.25, 2.3, .66, 'Fixed replay r = 0.8', fs=12)
    _link(group, fixed, nodes[3], 0, 2)
    _link(group, adaptive, nodes[3], 0, 2, TEAL)
    _text(group, 5.95, .45, 8.0, .40, 'Matched seeds, update budget, and exposure', 13)
    return group


def draw_replay(slide):
    """Conceptual replay feedback from the manuscript method, not an execution log.

    The caption/notes must define r as the historical fraction of the update
    batch and qualify the available trajectory evidence. Final-test data never
    feed this validation/controller loop.
    """
    group = _group(slide, 'Key scientific figure: adaptive replay feedback')
    historical = _box(group, 1.40, 3.25, 2.10, .85, 'Historical data', BLUE, '#f3f7f9', fs=14)
    rare = _box(group, 1.40, 1.75, 2.10, .85, 'Rare data', ORANGE, '#fbf7f1', fs=14)
    mix = _box(group, 4.40, 2.50, 1.80, .90, 'Mixed\nupdate batch', GREY, fs=14)
    model = _box(group, 7.20, 2.50, 1.90, .90, 'U-Net\nupdate', BLUE, '#f3f7f9', fs=14)
    validation = _box(group, 10.45, 2.50, 2.50, .95, 'Historical + rare\nvalidation', TEAL, '#f3f7f9', fs=14)
    controller = _box(group, 7.20, .82, 2.50, .80, 'Replay\ncontroller', TEAL, '#f3f7f9', fs=14)
    _link(group, historical, mix, color=BLUE)
    _link(group, rare, mix, color=ORANGE)
    _link(group, mix, model)
    _link(group, model, validation)
    _link(group, validation, controller, 2, 3, TEAL)
    _link(group, controller, mix, 1, 2, TEAL,
          name='Replay controller -> next mixed update batch')
    _text(group, 2.95, 3.20, .75, .30, 'r', 14, BLUE)
    _text(group, 2.95, 1.80, .90, .30, '1 − r', 14, ORANGE)
    _text(group, 4.70, 1.05, 1.2, .35, 'next r', 13, TEAL)
    return group


__all__ = ['draw_plan', 'draw_stress', 'draw_boundary', 'draw_next', 'draw_replay']

"""People, waist-up. Age reads through height, posture, build and hair, not props."""

INK = "#1B1038"
SK = {'fair': '#F2D4B8', 'olive': '#DCAE86', 'tan': '#C98E5E', 'brown': '#A06A42', 'deep': '#6F4526'}
HR = {'white': '#DEDBE2', 'steel': '#A9A8B5', 'ash': '#8C8A98',
      'dark': '#332D43', 'brown': '#5E3D29', 'black': '#211C2E'}


def head(cx, cy, skin, hair, style, tilt=0, aged=False):
    g = [f'<g transform="rotate({tilt} {cx} {cy+28})">']

    # mass behind the skull, a little wider than the head
    if style == "bob":
        g.append(f'<path d="M {cx-31} {cy+36} C {cx-33} {cy-14} {cx-21} {cy-35} {cx} {cy-35} '
                 f'C {cx+21} {cy-35} {cx+33} {cy-14} {cx+31} {cy+36} Z" fill="{hair}"/>')
    elif style == "bun":
        g.append(f'<ellipse cx="{cx}" cy="{cy-38}" rx="13" ry="12" fill="{hair}"/>')
        g.append(f'<ellipse cx="{cx}" cy="{cy-2}" rx="30" ry="33" fill="{hair}"/>')
    elif style == "curl":
        g.append(f'<ellipse cx="{cx}" cy="{cy-5}" rx="33" ry="34" fill="{hair}"/>')
    elif style == "crop":
        g.append(f'<ellipse cx="{cx}" cy="{cy-2}" rx="29" ry="32" fill="{hair}"/>')
    elif style == "sparse":
        g.append(f'<path d="M {cx-29} {cy+16} C {cx-31} {cy-10} {cx-20} {cy-28} {cx} {cy-28} '
                 f'C {cx+20} {cy-28} {cx+31} {cy-10} {cx+29} {cy+16} Z" fill="{hair}"/>')

    g.append(f'<ellipse cx="{cx-26}" cy="{cy+6}" rx="6" ry="8" fill="{skin}"/>')
    g.append(f'<ellipse cx="{cx+26}" cy="{cy+6}" rx="6" ry="8" fill="{skin}"/>')
    g.append(f'<ellipse cx="{cx}" cy="{cy}" rx="26" ry="30" fill="{skin}"/>')

    # fringe in front, with a hairline
    if style == "sparse":
        g.append(f'<path d="M {cx-28} {cy+11} C {cx-30} {cy-12} {cx-19} {cy-30} {cx} {cy-30} '
                 f'C {cx+19} {cy-30} {cx+30} {cy-12} {cx+28} {cy+11} '
                 f'C {cx+25} {cy-2} {cx+21} {cy-16} {cx+6} {cy-19} '
                 f'C {cx-7} {cy-21} {cx-20} {cy-13} {cx-25} {cy-1} Z" fill="{hair}"/>')
    elif style == "curl":
        g.append(f'<path d="M {cx-31} {cy+8} q -3 -14 6 -19 q -2 -14 11 -17 q 3 -12 14 -11 '
                 f'q 11 -1 14 11 q 13 3 11 17 q 9 5 6 19 '
                 f'C {cx+26} {cy-5} {cx+18} {cy-15} {cx} {cy-16} '
                 f'C {cx-18} {cy-15} {cx-26} {cy-5} {cx-31} {cy+8} Z" fill="{hair}"/>')
    else:
        side = 34 if style == "bob" else 7
        g.append(f'<path d="M {cx-28} {cy+side} C {cx-30} {cy-16} {cx-19} {cy-33} {cx} {cy-33} '
                 f'C {cx+19} {cy-33} {cx+30} {cy-16} {cx+28} {cy+side} '
                 f'L {cx+21} {cy+side} C {cx+24} {cy-4} {cx+18} {cy-14} {cx+2} {cy-15} '
                 f'C {cx-16} {cy-16} {cx-22} {cy-5} {cx-21} {cy+side} Z" fill="{hair}"/>')

    g += [f'<circle cx="{cx-10}" cy="{cy+3}" r="2.6" fill="{INK}"/>',
          f'<circle cx="{cx+10}" cy="{cy+3}" r="2.6" fill="{INK}"/>',
          f'<path d="M {cx-8} {cy+16} q 8 7 16 0" fill="none" stroke="{INK}" stroke-width="2.8" '
          f'stroke-linecap="round"/>']
    if aged:   # soft lines beside the mouth and at the outer eye
        g.append(f'<g fill="none" stroke="{INK}" stroke-width="1.8" stroke-linecap="round" opacity="0.38">'
                 f'<path d="M {cx-15} {cy+9} q -2 6 1 10"/><path d="M {cx+15} {cy+9} q 2 6 -1 10"/>'
                 f'<path d="M {cx-19} {cy+1} l -4 -2"/><path d="M {cx+19} {cy+1} l 4 -2"/></g>')
    g.append('</g>')
    return "".join(g)


def neck(cx, head_cy, torso_top, skin):
    return (f'<rect x="{cx-12}" y="{head_cy+14}" width="24" height="{torso_top-head_cy+6}" '
            f'rx="10" fill="{skin}"/>')


def torso(cx, top, bottom, w, cloth, slope=0):
    r = 30
    return (f'<path d="M {cx-w} {bottom} L {cx-w} {top+r+slope} Q {cx-w} {top+slope} {cx-w+r} {top+slope} '
            f'L {cx+w-r} {top} Q {cx+w} {top} {cx+w} {top+r} L {cx+w} {bottom} Z" fill="{cloth}"/>')


def limb(d, cloth, w=20):
    return f'<path d="{d}" fill="none" stroke="{cloth}" stroke-width="{w}" stroke-linecap="round"/>'


def hand(x, y, skin, r=11):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{skin}"/>'


def panel(w, h, bg, floor, body, rx=24, cid="a", label=""):
    return (f'<svg class="art" viewBox="0 0 {w} {h}" role="img" aria-label="{label}" '
            f'xmlns="http://www.w3.org/2000/svg">'
            f'<defs><clipPath id="cl{cid}"><rect x="0" y="0" width="{w}" height="{h}" rx="{rx}"/></clipPath></defs>'
            f'<rect x="0" y="0" width="{w}" height="{h}" rx="{rx}" class="{bg}"/>'
            f'<g clip-path="url(#cl{cid})">'
            f'<rect x="0" y="{floor}" width="{w}" height="{h-floor}" class="osurf"/>{body}</g></svg>')


OLD, CARER, CLIN_C = 'var(--c-older)', 'var(--c-carer)', 'var(--c-clin)'

# ---------------------------------------------------------------- hero: mother and daughter
B = 400
g = [limb('M 152 240 C 134 276 132 316 138 358', OLD) + hand(139, 362, SK['olive']),
     torso(188, 222, B, 40, OLD, slope=18),
     neck(188, 180, 222, SK['olive']),
     head(188, 180, SK['olive'], HR['white'], 'bob', tilt=6, aged=True),
     limb('M 348 168 C 370 214 372 290 360 354', CARER) + hand(359, 358, SK['tan']),
     torso(298, 150, B, 49, CARER),
     neck(298, 108, 150, SK['tan']),
     head(298, 108, SK['tan'], HR['black'], 'bun', tilt=-6),
     limb('M 258 168 C 224 172 196 192 166 216', CARER) + hand(162, 219, SK['tan'], 12)]
HERO = panel(460, 460, 'pnl', B - 22, "".join(g), 24, "h",
             "Illustration of a woman with her arm around her older mother")

# ---------------------------------------------------------------- families: carer and older man
B = 330
g = [limb('M 124 222 C 108 252 110 278 122 298', OLD) + hand(124, 302, SK['deep']),
     torso(160, 206, B, 39, OLD, slope=18),
     neck(160, 164, 206, SK['deep']),
     head(160, 164, SK['deep'], HR['steel'], 'curl', tilt=9, aged=True),
     limb('M 348 164 C 366 206 364 262 352 294', CARER) + hand(351, 298, SK['fair']),
     torso(302, 146, B, 47, CARER),
     neck(302, 104, 146, SK['fair']),
     head(302, 104, SK['fair'], HR['brown'], 'crop', tilt=-10),
     limb('M 262 176 C 228 204 194 238 168 256', CARER) + hand(164, 258, SK['fair'], 12)]
FAM = panel(440, 380, 'pnlw', B - 22, "".join(g), 20, "f",
            "Illustration of a carer with a hand on an older man's arm")
FAM = FAM.replace('class="art"', 'class="art art-warm"', 1)

# ---------------------------------------------------------------- clinicians
B = 330
g = [limb('M 346 226 C 362 254 358 280 346 300', OLD) + hand(345, 304, SK['fair']),
     torso(308, 210, B, 39, OLD, slope=17),
     neck(308, 168, 210, SK['fair']),
     head(308, 168, SK['fair'], HR['white'], 'sparse', tilt=-8, aged=True),
     limb('M 90 178 C 72 218 80 260 98 288', CLIN_C) + hand(101, 292, SK['brown']),
     torso(136, 158, B, 47, CLIN_C, slope=-3),
     neck(136, 112, 158, SK['brown']),
     head(136, 112, SK['brown'], HR['black'], 'crop', tilt=11),
     '<path d="M 120 152 L 136 204 L 152 152" fill="none" class="o1r" stroke-width="5"/>'
     '<rect x="126" y="202" width="21" height="27" rx="4" class="o1r"/>',
     limb('M 180 186 C 218 204 242 232 252 258', CLIN_C) + hand(254, 261, SK['brown'], 12)]
CLIN = panel(440, 380, 'pnl', B - 22, "".join(g), 20, "c",
             "Illustration of a clinician leaning in to listen to an older patient")

# ---------------------------------------------------------------- at home, on a call
B = 300
g = ['<g transform="translate(58 128)">'
     '<rect x="0" y="0" width="152" height="104" rx="9" class="o1"/>'
     '<rect x="9" y="9" width="134" height="78" rx="5" class="o3"/>'
     '<circle cx="58" cy="36" r="15" class="o2"/>'
     '<path d="M 36 80 q 0 -18 22 -18 q 22 0 22 18 Z" class="o2"/>'
     '<g class="o1r" fill="none" stroke-width="5" stroke-linecap="round">'
     '<path d="M 96 30 h 32"/><path d="M 96 46 h 24"/><path d="M 96 62 h 32"/></g>'
     '<path d="M -14 104 h 180 l -10 14 h -160 Z" class="o1"/></g>',
     limb('M 278 180 C 260 206 262 230 274 246', OLD) + hand(276, 250, SK['tan']),
     torso(314, 164, B, 40, OLD, slope=16),
     neck(314, 122, 164, SK['tan']),
     head(314, 122, SK['tan'], HR['ash'], 'bob', tilt=-6, aged=True)]
STEP = panel(440, 300, 'pnl', B - 22, "".join(g), 20, "s",
             "Illustration of an older woman at home talking to a clinician by video")

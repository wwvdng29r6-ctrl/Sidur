#!/usr/bin/env python3
"""בונה את שתי הגרסאות מקובץ מקור אחד:
  admin  -> /home/claude/sidur-avoda.html     (הגרסה המלאה של המנהל)
  member -> /home/claude/sidur-mefakdim.html  (גרסת המפקדים)
סימונים: /*@admin*/ ... /*/@admin*/  ו-<!--@admin--> ... <!--/@admin-->  (וכך גם @member).
קטע שמסומן לתפקיד אחד נמחק מהגרסה של התפקיד השני; הסימונים עצמם נמחקים מכל גרסה."""
import re, sys
SRC = '/home/claude/src/sidur.src.html'
OUT = {'admin': '/home/claude/sidur-avoda.html', 'member': '/home/claude/sidur-mefakdim.html'}
ROLES = ('admin', 'member')


def build(src, role):
    other = [r for r in ROLES if r != role][0]
    s = src
    for pat in (r'/\*@%s\*/.*?/\*/@%s\*/', r'<!--@%s-->.*?<!--/@%s-->'):
        s = re.sub(pat % (other, other), '', s, flags=re.S)
    for m in ('/*@%s*/', '/*/@%s*/', '<!--@%s-->', '<!--/@%s-->'):
        s = s.replace(m % role, '')
    for r in ROLES:
        for m in ('/*@%s*/', '/*/@%s*/', '<!--@%s-->', '<!--/@%s-->'):
            assert (m % r) not in s, (role, 'leftover marker', m % r)
    return s


def main():
    src = open(SRC, encoding='utf-8').read()
    # every opening marker has a closing one, in order, without nesting of the same role
    for r in ROLES:
        for o, c in (('/*@%s*/' % r, '/*/@%s*/' % r), ('<!--@%s-->' % r, '<!--/@%s-->' % r)):
            seq = re.findall(re.escape(o) + '|' + re.escape(c), src)
            assert len(seq) % 2 == 0 and all(seq[i] == o and seq[i + 1] == c for i in range(0, len(seq), 2)), ('unbalanced markers', r, o)
    for role in ROLES:
        out = build(src, role)
        open(OUT[role], 'w', encoding='utf-8').write(out)
        print(role, '->', OUT[role], len(out.encode('utf-8')), 'bytes')


if __name__ == '__main__':
    main()

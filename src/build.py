#!/usr/bin/env python3
"""בונה את שתי הגרסאות מקובץ מקור אחד (הנתיבים יחסיים לריפו, מכל תיקייה שמריצים):
  admin  -> index.html            (הגרסה המלאה של המנהל)
  member -> mefakdim/index.html   (גרסת המפקדים)
סימונים: /*@admin*/ ... /*/@admin*/  ו-<!--@admin--> ... <!--/@admin-->  (וכך גם @member).
קטע שמסומן לתפקיד אחד נמחק מהגרסה של התפקיד השני; הסימונים עצמם נמחקים מכל גרסה.

  python3 src/build.py           בונה וכותב את שני הקבצים
  python3 src/build.py --check   רק בודק שהקבצים בריפו תואמים למקור (בלי לכתוב); נכשל אם לא"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src', 'sidur.src.html')
OUT = {'admin': os.path.join(ROOT, 'index.html'), 'member': os.path.join(ROOT, 'mefakdim', 'index.html')}
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
    check = '--check' in sys.argv[1:]
    src = open(SRC, encoding='utf-8').read()
    # every opening marker has a closing one, in order, without nesting of the same role
    for r in ROLES:
        for o, c in (('/*@%s*/' % r, '/*/@%s*/' % r), ('<!--@%s-->' % r, '<!--/@%s-->' % r)):
            seq = re.findall(re.escape(o) + '|' + re.escape(c), src)
            assert len(seq) % 2 == 0 and all(seq[i] == o and seq[i + 1] == c for i in range(0, len(seq), 2)), ('unbalanced markers', r, o)
    stale = []
    for role in ROLES:
        out = build(src, role).encode('utf-8')
        path = OUT[role]
        rel = os.path.relpath(path, ROOT)
        if check:
            cur = open(path, 'rb').read() if os.path.exists(path) else None
            if cur != out:
                stale.append(rel)
            print(role, '->', rel, 'OK' if cur == out else 'STALE')
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, 'wb').write(out)
            print(role, '->', rel, len(out), 'bytes')
    if stale:
        print('\nהקבצים האלה לא תואמים ל-src/sidur.src.html:', ', '.join(stale))
        print('צריך להריץ: python3 src/build.py — ולשמור את התוצאה (לא לערוך אותם ישירות).')
        sys.exit(1)


if __name__ == '__main__':
    main()

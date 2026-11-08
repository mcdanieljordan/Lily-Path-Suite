"""Compact helper: one question per line  code|difficulty|prompt|right|wrong1|wrong2|wrong3|explanation"""
def load(B, text):
    for n, line in enumerate(text.strip().splitlines(), 1):
        line = line.strip()
        if not line or line.startswith('#'): continue
        p = [x.strip() for x in line.split('|')]
        if len(p) != 8: raise SystemExit("bad line %d (%d fields): %s" % (n, len(p), line[:60]))
        B.hand(p[0], int(p[1]), p[2], p[3], p[4:7], p[7])

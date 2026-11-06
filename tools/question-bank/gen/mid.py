"""Shared helpers for the grade 6-8 generators (negative numbers, fractions, equal-value filter)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from fractions import Fraction as F
from math import gcd

NM = ["Ava", "Ben", "Cara", "Dev", "Eli", "Fay", "Gus", "Hana", "Ivan", "Jo", "Kai", "Lena", "Max", "Nia", "Omar", "Pia", "Raj", "Sam", "Tia", "Zoe"]
MINUS = "−"

def sg(n):                          # integer/number -> text with a true minus sign
    s = str(n)
    return MINUS + s[1:] if s.startswith('-') else s
def sgc(expr):                      # chk text that gives the same thing as sg()
    return "str(%s).replace('-', '\\u2212')" % expr
def fs(a, b): return f"{a}/{b}"
def ms(x):                          # Fraction -> mixed number text (negative allowed, true minus)
    x = F(x); neg = x < 0; x = abs(x)
    w, r = divmod(x.numerator, x.denominator)
    if r == 0: t = str(w)
    else:
        f = f"{r}/{x.denominator}"
        t = f if w == 0 else f"{w} {f}"
    return (MINUS + t) if neg and t != "0" else t
def ims(x):                         # Fraction -> improper fraction / integer text
    x = F(x)
    return sg(x.numerator) if x.denominator == 1 else sg(f"{x.numerator}/{x.denominator}")
def pv(s):                          # text -> Fraction (handles mixed numbers and the minus sign)
    s = str(s).strip().replace(MINUS, '-')
    neg = s.startswith('-'); s = s.lstrip('-')
    v = sum((F(p) for p in s.split()), F(0))
    return -v if neg else v
def dec(x, places=None):            # Fraction/number -> decimal text, true minus
    x = F(x)
    if places is None:
        n = 0
        while (x * 10 ** n).denominator != 1 and n < 4: n += 1
        places = n
    v = round(abs(x) * 10 ** places)
    t = f"{v // 10 ** places}.{v % 10 ** places:0{places}d}" if places else str(v)
    return (MINUS + t) if x < 0 and v != 0 else t
def decchk(expr, places):           # chk text for a Fraction/number -> decimal with fixed places (non-negative only)
    return "f'{round(abs(%s)*%d)//%d}.{round(abs(%s)*%d)%%%d:0%dd}'" % (expr, 10 ** places, 10 ** places, expr, 10 ** places, 10 ** places, places)
def coprime(a, b): return gcd(a, b) == 1

_V = re.compile(r'(-?)(\$?)(\d[\d,]*(?:\.\d+)?)(?: (\d+)/(\d+)|/(\d+))?(%?)(°?)(?:\s+([A-Za-z][A-Za-z ]*))?')
_RT = re.compile(r'(\d+):(\d+)')
def vkey(x):
    s = str(x).strip().replace(MINUS, '-')
    m = _RT.fullmatch(s)
    if m and int(m.group(2)): return ('ratio', F(int(m.group(1)), int(m.group(2))))
    m = _V.fullmatch(s)
    if not m: return None
    sgn, dl, num, n2, d2, d1, pc, dg, unit = m.groups()
    v = F(num.replace(',', ''))
    if d1: v = v / int(d1)
    if n2: v = v + F(int(n2), int(d2))
    if sgn: v = -v
    return (v, dl + pc + dg + (unit or '').strip())

def setup(prefix, seed, own, no_neg=False):
    B = Bank(prefix, seed, no_neg=no_neg, own=own)
    base = B.mk
    def mk(code, d, q, right, wrong, e, chk=None, need=3):      # drops wrong choices equal in value to the right one (or to each other)
        kr = vkey(right); seen = {kr} if kr else set(); out = []
        for w in wrong:
            k = vkey(w)
            if k is not None:
                if k in seen: continue
                seen.add(k)
            out.append(w)
        return base(code, d, q, right, out, e, chk, need)
    return B, mk

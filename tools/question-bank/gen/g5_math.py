#!/usr/bin/env python3
"""Grade 5 Mathematics (TEKS 111.7.b) - original questions. Run: python3 gen/g5_math.py  -> batches/g5_math.jsonl"""
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from fractions import Fraction as F

B = Bank('111.7.b.', 505, no_neg=True, own='g5_math.jsonl')
R, H, rep = B.R, B.hand, B.rep
from math import gcd
_NUM = re.compile(r'(\$?)(\d[\d,]*(?:\.\d+)?)(¢?)(?:\s+([A-Za-z][A-Za-z ]*))?')
def _key(x):
    m = _NUM.fullmatch(str(x).strip())
    return (float(m.group(2).replace(',', '')), m.group(1) + m.group(3) + (m.group(4) or '').strip()) if m else None
_SUM = re.compile(r'[\d.]+( \+ [\d.]+)+')
def _sv(x):
    x = str(x)
    return sum((F(t) for t in x.split(' + ')), F(0)) if _SUM.fullmatch(x) else None
_mk0 = B.mk
def mk(code, d, q, right, wrong, e, chk=None, need=3):      # drop wrong choices that equal the right answer in value (64.8 vs 64.80)
    kr = _key(right); seen_k = {kr} if kr else set(); out = []
    vr = _sv(right)
    wrong = [w for w in wrong if vr is None or _sv(w) != vr]
    for w in wrong:
        k = _key(w)
        if k is not None:
            if k in seen_k: continue
            seen_k.add(k)
        out.append(w)
    return _mk0(code, d, q, right, out, e, chk, need)
LT, GT, EQ = "less than (<)", "greater than (>)", "equal to (=)"
NM = ["Ava", "Ben", "Cara", "Dev", "Eli", "Fay", "Gus", "Hana", "Ivan", "Jo", "Kai", "Lena", "Max", "Nia", "Omar", "Pia", "Raj", "Sam", "Tia", "Zoe"]
def who(): return R.choice(NM)
def fs(a, b): return f"{a}/{b}"
def fmt(n, p):                     # integer n in units of 10^-p  ->  decimal text
    return f"{n // 10 ** p}.{n % 10 ** p:0{p}d}" if p else str(n)
def dchk(expr, p):                 # chk text for an integer expression in units of 10^-p
    return "f'{(%s)//%d}.{(%s)%%%d:0%dd}'" % (expr, 10 ** p, expr, 10 ** p, p)
def dol(c): return f"${c // 100:,}.{c % 100:02d}"
def dolchk(expr): return "f'${(%s)//100:,}.{(%s)%%100:02d}'" % (expr, expr)
def ms(x):                         # fraction -> mixed number text
    x = F(x); w, r = divmod(x.numerator, x.denominator)
    if r == 0: return str(w)
    f = f"{r}/{x.denominator}"
    return f if w == 0 else f"{w} {f}"
def pv(s):                         # text -> Fraction
    return sum((F(p) for p in str(s).split()), F(0))
def neq(right, cands):
    v = pv(right); out = []
    for c in cands:
        try:
            if pv(c) != v and c not in out: out.append(c)
        except Exception: pass
    return out
def est_ok(actual, right, wrongs):
    dr = abs(right - actual); ok = [w for w in wrongs if w != right and abs(w - actual) >= 2 * dr + 1e-9]
    return ok

# ================================================================ 2.A decimals through thousandths
def a_val():
    w = R.randint(1, 99); x, y, z = R.sample(range(1, 10), 3); n = f"{w}.{x}{y}{z}"
    pos = R.choice([0, 1, 2]); d = (x, y, z)[pos]
    right = ["0." + str(d), "0.0" + str(d), "0.00" + str(d)][pos]
    wrong = [v for v in ["0." + str(d), "0.0" + str(d), "0.00" + str(d), str(d), f"{d}0"] if v != right]
    place = ["tenths", "hundredths", "thousandths"][pos]
    return mk('2.A', 3, f"What is the value of the digit {d} in {n}?", right, wrong, f"The {d} is in the {place} place, so its value is {right}.")
def a_exp():
    w = R.randint(1, 99); x, y, z = R.sample(range(1, 10), 3); n = f"{w}.{x}{y}{z}"
    right = f"{w} + 0.{x} + 0.0{y} + 0.00{z}"
    wrong = [f"{w} + 0.0{x} + 0.00{y} + 0.000{z}", f"{w} + {x} + {y} + {z}", f"{w} + 0.{x} + 0.{y} + 0.{z}", f"{w} + 0.{z} + 0.0{y} + 0.00{x}"]
    return mk('2.A', 3, f"Which is the expanded notation for {n}?", right, wrong, f"Tenths, hundredths, and thousandths: {right} = {n}.")
def a_num():
    w = R.randint(1, 9); x, y, z = R.choice([0, 0, 1, 2, 3]), R.randint(1, 9), R.randint(1, 9)
    if x == 0: terms = f"{w} + 0.0{y} + 0.00{z}"
    else: terms = f"{w} + 0.{x} + 0.0{y} + 0.00{z}"
    right = f"{w}.{x}{y}{z}"
    wrong = [f"{w}.{y}{z}", f"{w}.{x}0{y}{z}", f"{w}.{z}{y}{x}", f"{w}{x}.{y}{z}", f"{w}.0{x}{y}{z}"]
    return mk('2.A', 3, f"Which number is equal to {terms}?", right, wrong, f"Write each digit in its place: {right}.")
def a_frac():
    w = R.randint(1, 9); x, y, z = R.sample(range(1, 10), 3)
    right = f"{w}.{x}{y}{z}"
    return mk('2.A', 4, f"Which number is equal to {w} + {x}/10 + {y}/100 + {z}/1000?", right, [f"{w}.{z}{y}{x}", f"{w}.{x}{y}", f"{w}.{x}0{y}{z}", f"{w}{x}.{y}{z}"], f"{x}/10 = 0.{x}, {y}/100 = 0.0{y}, {z}/1000 = 0.00{z}.")
rep(4, a_val); rep(3, a_exp); rep(4, a_num); rep(2, a_frac)

# ================================================================ 2.B compare and order decimals
def cmp_dec():
    kind = R.randint(0, 3); w = R.randint(0, 9)
    t = R.randint(2, 9); h = R.randint(1, 9); k = R.randint(1, 9)
    if kind == 0: a, b = f"{w}.{t}", f"{w}.{t - 1}{R.randint(5, 9)}"
    elif kind == 1: a, b = f"{w}.{t}", f"{w}.{t}0"
    elif kind == 2: a, b = f"{w}.{t}{h}", f"{w}.{t}{h}{k}"
    else: a, b = f"{w}.{t}{h}{k}", f"{w}.{t}{k}{h}"
    if a == b: return False
    if R.random() < .5: a, b = b, a
    va, vb = F(a), F(b)
    ans = GT if va > vb else LT if va < vb else EQ
    return mk('2.B', 3, f"Which symbol makes the statement true?   {a} ___ {b}", ans, [x for x in (LT, GT, EQ) if x != ans], f"Line up the decimal points and compare place by place: {a} is {ans.split(' (')[0]} {b}.", need=2)
def ord_dec():
    t = R.randint(3, 8); h = R.randint(5, 9); k = R.randint(1, 9)
    vals = [f"0.{t}", f"0.{t - 1}{h}", f"0.{t}0{k}"]           # 0.t, 0.(t-1)h, 0.t0k
    srt = sorted(vals, key=F)
    least = R.random() < .6
    if not least: srt = srt[::-1]
    import itertools
    shown = vals[:]; R.shuffle(shown)
    ans = ', '.join(srt)
    wr = [', '.join(perm) for perm in itertools.permutations(vals) if list(perm) != srt]
    return mk('2.B', 4, f"Which list shows the numbers in order from {'least to greatest' if least else 'greatest to least'}?   {', '.join(shown)}", ans, wr, "Compare the tenths first, then the hundredths, then the thousandths.")
def tf_dec():
    t = R.randint(2, 8); h = R.randint(1, 9)
    pairs = [(f"0.{t}", f"0.{t}{h}"), (f"0.{t}", f"0.{t - 1}{h}"), (f"0.{t}0", f"0.{t}"), (f"0.{t}{h}", f"0.{t}{h}0")]
    x, y = R.choice(pairs)
    sym = '>' if F(x) > F(y) else '<' if F(x) < F(y) else '='
    other = [s_ for s_ in '<>=' if s_ != sym]
    return mk('2.B', 4, "Which comparison is true?", f"{x} {sym} {y}", [f"{x} {o} {y}" for o in other] + [f"{y} {sym} {x}" if sym != '=' else f"{y} < {x}"], "Add zeros so both numbers have the same number of decimal places, then compare.")
rep(5, cmp_dec); rep(3, ord_dec); rep(2, tf_dec)

# ================================================================ 2.C rounding decimals
def rnd_t():
    n = R.randint(101, 9999)           # hundredths
    t = (n + 5) // 10
    right = fmt(t, 1)
    return mk('2.C', 3, f"Round {fmt(n, 2)} to the nearest tenth.", right, [fmt(n // 10, 1), fmt(t + 1, 1) if t + 1 != t else right, fmt(t - 1, 1) if t > 1 else fmt(t + 2, 1), fmt(n, 2)[:-1] + '0' if False else fmt((n + 50) // 100 * 10, 1)], f"Look at the hundredths digit {n % 10}: {'round up' if n % 10 >= 5 else 'keep the tenths digit'}. The answer is {right}.", dchk(f"({n}+5)//10", 1) if False else "f'{((%d+5)//10)//10}.{((%d+5)//10)%%10}'" % (n, n))
def rnd_h():
    n = R.randint(1001, 99999)         # thousandths
    h = (n + 5) // 10
    right = fmt(h, 2)
    return mk('2.C', 3, f"Round {fmt(n, 3)} to the nearest hundredth.", right, [fmt(n // 10, 2), fmt(h + 1, 2), fmt(h - 1, 2), fmt((n + 50) // 100, 1)], f"Look at the thousandths digit {n % 10}: {'round up' if n % 10 >= 5 else 'keep the hundredths digit'}. The answer is {right}.", dchk(f"({n}+5)//10", 2))
def rnd_money():
    nm = who(); n = R.randint(1999, 4999); right = fmt((n + 5) // 10, 2)
    return mk('2.C', 4, f"{nm}'s gas pump shows a price of ${fmt(n, 3)} per gallon. Rounded to the nearest hundredth of a dollar, what is the price?", f"${right}", [f"${fmt(n // 10, 2)}", f"${fmt((n + 5) // 10 + 1, 2)}", f"${fmt((n + 50) // 100, 1)}", f"${fmt(n, 3)}"], f"Check the thousandths digit {n % 10}: {'round up' if n % 10 >= 5 else 'round down'}.")
def rnd_tf():
    n = R.randint(100, 999) * 10 + R.choice([0, 1, 4, 5, 6, 9])
    return False
rep(5, rnd_t); rep(5, rnd_h); rep(3, rnd_money)

# ================================================================ 3.A estimation
def est_add():
    p = R.choice([10, 100, 1000]); lo, hi = {10: (21, 99), 100: (201, 999), 1000: (2001, 9999)}[p]
    a, b = R.randint(lo, hi), R.randint(lo, hi); sub = R.random() < .4
    if sub and a < b: a, b = b, a
    ra, rb = (a + p // 2) // p * p, (b + p // 2) // p * p
    est = ra - rb if sub else ra + rb; actual = a - b if sub else a + b
    if est <= 0: return False
    w = est_ok(actual, est, [est + 2 * p, est - 2 * p, est + p * 10, est // 10 if est >= 10 else est * 10, est + 3 * p])
    w = [x for x in w if x > 0]
    nm = who(); th = R.choice(["stickers", "cards", "marbles", "beads"])
    pn = {10: "ten", 100: "hundred", 1000: "thousand"}[p]
    if R.random() < .5:
        q = f"Estimate {cm(a)} {'−' if sub else '+'} {cm(b)} by rounding each number to the nearest {pn}."
    else:
        q = (f"{nm} has {cm(a)} {th}. A friend has {cm(b)} {th}. About how many {th} do they have altogether? Round each number to the nearest {pn} to estimate." if not sub else
             f"{nm} had {cm(a)} {th} and gave away {cm(b)}. About how many {th} are left? Round each number to the nearest {pn} to estimate.")
    return mk('3.A', 3, q, cm(est), [cm(x) for x in w], f"{cm(ra)} {'−' if sub else '+'} {cm(rb)} = {cm(est)}.", CK(f"{ra}{'-' if sub else '+'}{rb}"))
def est_mul():
    a = R.randint(21, 99) if R.random() < .5 else R.randint(201, 899); b = R.randint(21, 99)
    pa = 10 if a < 100 else 100
    ra, rb = (a + pa // 2) // pa * pa, (b + 5) // 10 * 10
    est = ra * rb; actual = a * b
    w = est_ok(actual, est, [est * 10, est // 10, est + ra * 10, est - rb * 10, est * 2])
    nm = who(); th = R.choice(["boxes", "rows", "bags", "trays"])
    return mk('3.A', 4, f"Estimate the product of {cm(a)} × {b} by rounding {cm(a)} to the nearest {'ten' if pa == 10 else 'hundred'} and {b} to the nearest ten.", cm(est), [cm(x) for x in w if x > 0], f"{cm(ra)} × {rb} = {cm(est)}.", CK(f"{ra}*{rb}"))
def est_div():
    d0 = R.randint(2, 9) * 10; q0 = R.randint(3, 90); a = q0 * d0 + R.randint(-d0 // 2 + 1, d0 // 2 - 1); d = d0 + R.randint(-3, 3)
    if a < 100 or d == d0: return False
    actual = a / d
    w = est_ok(actual, q0, [q0 * 10, q0 // 10 if q0 >= 10 else q0 + 7, q0 + 20, max(q0 - 20, 1), q0 * 2])
    est_a = q0 * d0
    return mk('3.A', 4, f"Estimate {cm(a)} ÷ {d} by using compatible numbers.", cm(q0), [cm(x) for x in w], f"{cm(est_a)} ÷ {d0} = {q0}.", CK(f"{q0}"))
rep(5, est_add); rep(3, est_mul); rep(3, est_div)

# ================================================================ 3.B multiply 3-digit by 2-digit
def mul32():
    a, b = R.randint(101, 999), R.randint(11, 99)
    if b % 10 == 0 or a % 10 == 0 and R.random() < .6: return False
    p = a * b; ones, tens = a * (b % 10), a * (b // 10)
    wr = [ones + tens, tens * 10 + ones // 10 if False else p + 10, p - 100, p + 1000 if p + 1000 != p else p, ones + tens * 100, p - 10]
    return mk('3.B', 3, f"What is {a} × {b}?", cm(p), [cm(x) for x in wr], f"{a} × {b % 10} = {cm(ones)} and {a} × {b // 10 * 10} = {cm(tens * 10)}. {cm(ones)} + {cm(tens * 10)} = {cm(p)}.", CK(f"{a}*{b}"))
def mul_word():
    nm = who(); a, b = R.randint(110, 480), R.randint(12, 48)
    th = R.choice([("seats", "rows"), ("pages", "books"), ("cans", "cases"), ("bricks", "pallets"), ("nails", "boxes")])
    p = a * b
    return mk('3.B', 4, f"A school ordered {b} {th[1]}. Each one has {a} {th[0]}. How many {th[0]} did the school order in all?", cm(p), [cm(p + 100), cm(p - 10), cm(a + b), cm(a * (b % 10) + a * (b // 10))], f"{a} × {b} = {cm(p)}.", CK(f"{a}*{b}"))
rep(8, mul32); rep(4, mul_word)

# ================================================================ 3.C divide up to 4-digit by 2-digit
def div_exact():
    d = R.randint(11, 49); q = R.randint(12, 200)
    if d * q > 9999: return False
    a = d * q
    return mk('3.C', 3, f"What is {cm(a)} ÷ {d}?", cm(q), [cm(q + 1), cm(q - 1), cm(q + 10), cm(q - 10), cm(q * 10) if q * 10 < 5000 else cm(q + 100)], f"{d} × {q} = {cm(a)}, so {cm(a)} ÷ {d} = {q}.", CK(f"{q}"))
def div_rem():
    d = R.randint(11, 49); q = R.randint(10, 190); r = R.randint(1, d - 1); a = d * q + r
    if a > 9999: return False
    right = f"{q} R {r}"
    return mk('3.C', 4, f"What is {cm(a)} ÷ {d}?", right, [f"{q} R {r + 1}" if r + 1 < d else f"{q} R {r - 1}", f"{q + 1} R {r}", f"{q} R {d - r}" if d - r != r else f"{q + 10} R {r}", f"{r} R {q}" if r != q and q < d else f"{q - 1} R {r}"], f"{d} × {q} = {cm(d * q)}, and {cm(a)} − {cm(d * q)} = {r}.", f"f'{{{q}}} R {{{r}}}'")
def div_word():
    nm = who(); d = R.randint(12, 36); q = R.randint(15, 120); a = d * q
    th = R.choice([("students", "buses"), ("pencils", "boxes"), ("pages", "chapters"), ("cookies", "trays"), ("seeds", "pots")])
    if a > 9999: return False
    return mk('3.C', 4, f"{cm(a)} {th[0]} are shared equally among {d} {th[1]}. How many {th[0]} go in each?", cm(q), [cm(q + 1), cm(q - 1), cm(q + 10), cm(a - d)], f"{cm(a)} ÷ {d} = {q}.", CK(f"{q}"))
def div_rem_word():
    nm = who(); d = R.choice([12, 15, 16, 18, 20, 24, 25, 36]); q = R.randint(12, 150); r = R.randint(1, d - 1); a = d * q + r
    if a > 9999: return False
    return mk('3.C', 4, f"{nm} packs {cm(a)} muffins into boxes that hold {d} each. How many muffins are left over after {nm} fills as many boxes as possible?", r, [r + 1 if r + 1 < d else r - 1, q, d - r if d - r != r else r + 2, d], f"{cm(a)} ÷ {d} = {q} R {r}.", CS(f"{r}"))
rep(6, div_exact); rep(4, div_rem); rep(2, div_word); rep(3, div_rem_word)

# ================================================================ 3.D area models for decimal multiplication
def dm_grid():
    a, b = R.randint(2, 9), R.randint(2, 9); nm = who()
    return mk('3.D', 3, f"A 10-by-10 grid is one whole. {nm} shades 0.{a} of the width and 0.{b} of the height to make a rectangle. How many of the 100 small squares are in the rectangle?", a * b, [a + b, a * b * 10, a * b + 10, (a + b) * 10], f"The rectangle is {a} tenths by {b} tenths = {a * b} hundredths, so {a * b} squares.", CS(f"{a * b}"))
def dm_model():
    a, b = R.randint(2, 9), R.randint(2, 9)
    p = a * b
    return mk('3.D', 3, f"An area model shows 0.{a} × 0.{b}. What decimal is the shaded area?", fmt(p, 2), [fmt(p, 1) if p < 100 else fmt(p, 2), fmt(p, 3), fmt(a + b, 2), fmt(p * 10, 2)], f"{a} tenths × {b} tenths = {p} hundredths = {fmt(p, 2)}.", dchk(f"{p}", 2))
def dm_expr():
    a, b = R.randint(2, 9), R.randint(2, 9)
    return mk('3.D', 4, f"A rectangle model has a length of 0.{a} and a width of 0.{b}. Which multiplication sentence matches the shaded area?", f"0.{a} × 0.{b} = {fmt(a * b, 2)}", [f"0.{a} × 0.{b} = {fmt(a * b, 1) if a * b < 100 else fmt(a * b, 2)}", f"0.{a} × 0.{b} = {fmt(a * b, 3)}", f"0.{a} + 0.{b} = {fmt(a * b, 2)}", f"0.{a} × 0.{b} = {fmt(a + b, 2)}"], f"{a} × {b} = {a * b}, and tenths × tenths is hundredths: {fmt(a * b, 2)}.")
rep(4, dm_grid); rep(3, dm_model); rep(3, dm_expr)

# ================================================================ 3.E multiply decimals (products to hundredths)
def me_tt():
    a, b = R.randint(2, 9), R.randint(2, 9)
    if a * b < 10: return False
    return mk('3.E', 3, f"What is 0.{a} × 0.{b}?", fmt(a * b, 2), [fmt(a * b, 1), fmt(a * b, 3), str(a * b), fmt(a + b, 2)], f"{a} × {b} = {a * b}, and two decimal places make {fmt(a * b, 2)}.", dchk(f"{a * b}", 2))
def me_wt():
    a = R.randint(2, 12); b = R.randint(11, 99)
    if b % 10 == 0: return False
    p = a * b
    return mk('3.E', 3, f"What is {a} × {fmt(b, 1)}?", fmt(p, 1), [fmt(p, 2), fmt(p, 0) if p < 0 else fmt(p * 10, 1), fmt(p, 1)[:-1] + str((p % 10 + 1) % 10), str(p)], f"{a} × {b} = {p}, and one decimal place gives {fmt(p, 1)}.", dchk(f"{p}", 1))
def me_wh():
    a = R.randint(2, 9); b = R.randint(101, 999)
    if b % 10 == 0: return False
    p = a * b
    return mk('3.E', 3, f"What is {a} × {fmt(b, 2)}?", fmt(p, 2), [fmt(p, 1), fmt(p, 3), fmt(p * 10, 2), fmt(p + 10, 2)], f"{a} × {b} = {p}, and two decimal places give {fmt(p, 2)}.", dchk(f"{p}", 2))
PRICES = [("notebooks", 199, 899), ("pens", 89, 399), ("packs of gum", 99, 299), ("juice boxes", 79, 249), ("sticker sheets", 49, 349), ("folders", 129, 499), ("granola bars", 75, 199), ("toy cars", 199, 799), ("water bottles", 249, 899)]
def me_money():
    nm = who(); n = R.randint(3, 12); th, lo, hi = R.choice(PRICES); c = R.randint(lo, hi)
    if c % 100 == 0: return False
    tot = n * c
    return mk('3.E', 3, f"{nm} buys {n} {th} that cost {dol(c)} each. What is the total cost?", dol(tot), [dol(tot + 10), dol(tot - 100), dol(tot * 10), dol(n * 100 + c)], f"{n} × {dol(c)} = {dol(tot)}.", dolchk(f"{n}*{c}"))
def me_tw():
    a = R.randint(11, 99); b = R.randint(2, 9)
    if a % 10 == 0: return False
    p = a * b
    return mk('3.E', 4, f"What is {fmt(a, 2)} × 0.{b}? Give the answer to the thousandths.", fmt(p, 3), [fmt(p, 2), fmt(p, 1) if p < 1000 else fmt(p, 3), fmt(p * 10, 3), fmt(a + b, 3)], f"{a} × {b} = {p}; two decimal places plus one decimal place is three places: {fmt(p, 3)}.", dchk(f"{p}", 3)) if False else False
rep(4, me_tt); rep(4, me_wt); rep(3, me_wh); rep(4, me_money)

# ================================================================ 3.F decimal division with models
def df_model():
    n = R.randint(2, 9) * R.randint(2, 4); k = R.choice([2, 3, 4, 5]); n = k * R.randint(2, 9); p = n // k
    nm = who()
    return mk('3.F', 3, f"A model shows {fmt(n, 1)} (that is {n} tenths) shared equally into {k} groups. How much is in each group?", fmt(p, 1), [fmt(p, 2), str(p), fmt(n * k, 1) if n * k < 100 else fmt(n + k, 1), fmt(p + 1, 1)], f"{n} tenths ÷ {k} = {p} tenths = {fmt(p, 1)}.", dchk(f"{p}", 1))
def df_money():
    nm = who(); k = R.choice([2, 4, 5, 10]); c = k * R.randint(5, 40)
    if c % 100 == 0: return False
    th = R.choice(["dimes", "friends", "cups", "siblings"])
    return mk('3.F', 3, f"{nm} shares {dol(c)} equally among {k} {R.choice(['friends', 'cousins', 'teammates'])}. A grid or coin model shows the amount each person gets. How much is it?", dol(c // k), [dol(c // k + 10), dol(c // k * 10), dol(c - k), dol(c // k - 5) if c // k > 5 else dol(c // k + 20)], f"{dol(c)} ÷ {k} = {dol(c // k)}.", dolchk(f"{c}//{k}"))
def df_whole():
    k = R.randint(3, 9); n = R.randint(2, 9) * k; nm = who()
    return mk('3.F', 4, f"{nm} cuts a ribbon that is {fmt(n, 1)} meters long into {k} equal pieces. How long is each piece?", f"{fmt(n // k, 1) if n // k < 100 else n // k} meters", [f"{fmt(n // k, 2)} meters", f"{n // k * 10} meters", f"{fmt(n * k, 1)} meters", f"{fmt(n // k + k, 1)} meters"], f"{n} tenths ÷ {k} = {n // k} tenths.")
rep(4, df_model); rep(3, df_money); rep(2, df_whole)

# ================================================================ 3.G divide decimals
def dg_calc():
    d = R.randint(11, 49); q = R.randint(101, 999)          # q in hundredths
    if q % 10 == 0: return False
    a = d * q                                                 # dividend in hundredths
    if a > 99999: return False
    return mk('3.G', 4, f"What is {fmt(a, 2)} ÷ {d}?", fmt(q, 2), [fmt(q, 1) if q < 1000 else fmt(q * 10, 2), fmt(q, 3), fmt(q * 10, 2), fmt(q + 1, 2)], f"{fmt(a, 2)} ÷ {d} = {fmt(q, 2)}. Check: {d} × {fmt(q, 2)} = {fmt(a, 2)}.", dchk(f"{q}", 2))
def dg_tenths():
    d = R.randint(3, 9); q = R.randint(12, 99); a = d * q
    if q % 10 == 0: return False
    return mk('3.G', 3, f"What is {fmt(a, 1)} ÷ {d}?", fmt(q, 1), [fmt(q, 2), str(q), fmt(q * 10, 1), fmt(q + 1, 1)], f"{a} tenths ÷ {d} = {q} tenths = {fmt(q, 1)}.", dchk(f"{q}", 1))
def dg_money():
    nm = who(); k = R.randint(6, 24); c = R.randint(45, 400)
    if c % 5: return False
    tot = k * c; th = R.choice(["gift", "pizza party", "class trip snack order", "game"])
    return mk('3.G', 3, f"{nm}'s group pays {dol(tot)} for a {th}. The cost is shared equally among {k} people. How much does each person pay?", dol(c), [dol(c + 25), dol(c * 10), dol(c - 10), dol(tot // 10)], f"{dol(tot)} ÷ {k} = {dol(c)}.", dolchk(f"{c}"))
def dg_whole():
    d = R.randint(12, 35); q = R.randint(5, 80); a = d * q
    return mk('3.G', 4, f"A rope that is {fmt(a * 10 // 10, 0)}.0 meters long is cut into {d} equal pieces... ", "x", ["y", "z", "w"], "x") if False else False
rep(5, dg_calc); rep(4, dg_tenths); rep(4, dg_money)

# ================================================================ 3.H add / subtract fractions with unequal denominators
DEN = [2, 3, 4, 5, 6, 8, 10, 12]
def fh_addsub():
    b, d = R.sample(DEN, 2); a = R.randint(1, b - 1); c = R.randint(1, d - 1); add = R.random() < .6
    if gcd(a, b) != 1 or gcd(c, d) != 1: return False
    x, y = F(a, b), F(c, d)
    if not add and x < y: a, b, c, d = c, d, a, b; x, y = y, x
    if x == y and not add: return False
    res = x + y if add else x - y
    if res <= 0: return False
    L = (b * d) // __import__('math').gcd(b, d)
    wr = [fs(a + c, b + d) if add else fs(abs(a - c), abs(b - d) or b), fs(a + c if add else abs(a - c), L), ms(res + F(1, L)), ms(abs(res - F(1, L))) if res > F(1, L) else ms(res + F(2, L)), ms(F(a + c, b)) if add else ms(F(abs(a - c), d))]
    wr = neq(ms(res), wr)
    op = '+' if add else '−'
    chk = f"fr(F({a},{b}){'+' if add else '-'}F({c},{d}))" if res < 1 else None
    return mk('3.H', 3 if L in (b, d) else 4, f"What is {fs(a, b)} {op} {fs(c, d)}? Give the answer in simplest form.", ms(res), wr, f"Use a common denominator of {L}: {fs(a * L // b, L)} {op} {fs(c * L // d, L)} = {fs(abs(a * L // b + (1 if add else -1) * c * L // d), L)}{'' if ms(res) == fs(abs(a * L // b + (1 if add else -1) * c * L // d), L) else ', which is ' + ms(res) + ' in simplest form'}.", chk)
UNITS = [("gallon", "of paint"), ("pound", "of trail mix"), ("cup", "of flour"), ("quart", "of soup"), ("liter", "of juice")]
def fh_word():
    b, d = R.sample([2, 3, 4, 5, 6, 8], 2); a = R.randint(1, b - 1); c = R.randint(1, d - 1); nm = who()
    if gcd(a, b) != 1 or gcd(c, d) != 1: return False
    x, y = F(a, b), F(c, d); res = x + y
    u, nn = R.choice(UNITS)
    wr = neq(ms(res), [fs(a + c, b + d), ms(F(a + c, max(b, d))), ms(res + F(1, b * d)), ms(abs(x - y)) if x != y else ms(res + F(1, d))])
    return mk('3.H', 4, f"{nm} used {fs(a, b)} {u} {nn} on Monday and {fs(c, d)} {u} {nn} on Tuesday. How many {u}s {nn} did {nm} use in all?", ms(res), wr, f"{fs(a, b)} + {fs(c, d)} = {ms(res)}.")
def fh_model():
    b = R.choice([2, 3, 4]); k = R.choice([2, 3]); d = b * k; a = R.randint(1, b - 1); c = R.randint(1, d - 1); nm = who()
    res = F(a, b) + F(c, d)
    wr = neq(ms(res), [fs(a + c, b + d), fs(a + c, b), fs(a + c, d), ms(res + F(1, d))])
    return mk('3.H', 3, f"{nm} folds a paper strip into {b} equal parts and shades {a}. Then {nm} folds each part again so the strip has {d} equal parts and shades {c} more of those small parts. What fraction of the strip is shaded now?", ms(res), wr, f"{fs(a, b)} = {fs(a * k, d)}, so the total is {fs(a * k + c, d)}{'' if ms(res) == fs(a * k + c, d) else ' = ' + ms(res)}.")
rep(7, fh_addsub); rep(3, fh_word); rep(2, fh_model)

# ================================================================ 3.I whole number x fraction
def fi_calc():
    n = R.randint(2, 9); b = R.choice([2, 3, 4, 5, 6, 8]); a = R.randint(1, b - 1)
    res = F(n * a, b);
    wr = neq(ms(res), [fs(n * a, b * n) if False else fs(a, b * n), fs(n + a, b), ms(F(n, b) + a) if False else fs(n * a, b + n), fs(a, n * b), ms(res + 1), ms(F(n * b, a)) if a else "0"])
    return mk('3.I', 3, f"What is {n} × {fs(a, b)}? Give the answer in simplest form.", ms(res), wr, f"{n} × {fs(a, b)} = {fs(n * a, b)}{'' if ms(res) == fs(n * a, b) else ' = ' + ms(res)}.")
def fi_word():
    n = R.randint(3, 9); b = R.choice([2, 3, 4, 5, 8]); a = R.randint(1, b - 1); nm = who()
    if gcd(a, b) != 1: return False
    th = R.choice([("glass", "cup", "glasses"), ("bag", "pound", "bags"), ("jar", "cup", "jars"), ("bottle", "liter", "bottles")])
    res = F(n * a, b)
    wr = neq(ms(res), [fs(a, b * n), fs(n + a, b), ms(F(n * b, a)), fs(a * n, b * n)])
    return mk('3.I', 4, f"{nm} fills {n} {th[2]}. Each one holds {fs(a, b)} {th[1]}. How many {th[1]}s in all?", ms(res), wr, f"{n} × {fs(a, b)} = {fs(n * a, b)} = {ms(res)}.")
def fi_area():
    n = R.randint(2, 6); b = R.choice([3, 4, 5, 6]); a = R.randint(1, b - 1); res = F(n * a, b)
    if gcd(a, b) != 1: return False
    wr = neq(ms(res), [fs(a, b * n), fs(n + a, b), fs(n * a, b * n), ms(res + F(1, b))])
    return mk('3.I', 3, f"An area model shows {n} groups, and each group is {fs(a, b)} of a bar shaded. How much of a whole bar is shaded in all?", ms(res), wr, f"{n} × {fs(a, b)} = {fs(n * a, b)} = {ms(res)}.")
rep(4, fi_calc); rep(3, fi_word); rep(2, fi_area)

# ================================================================ 3.J division with unit fractions (models, stories)  /  3.L solve
def fj_story1():
    n = R.randint(2, 9); b = R.choice([2, 3, 4, 5, 6, 8]); nm = who(); th = R.choice([("cups of rice", "cup"), ("pounds of nuts", "pound"), ("liters of juice", "liter")])
    return mk('3.J', 3, f"{nm} has {n} {th[0]}. {nm} wants to fill small scoops that each hold {fs(1, b)} {th[1]}. A model shows {n} wholes each cut into {b} equal parts. How many scoops can {nm} fill?", n * b, [n + b, n, F(n, b).numerator if False else n * b + b, b], f"Each whole has {b} parts, so {n} wholes have {n} × {b} = {n * b} parts.", CS(f"{n}*{b}"))
def fj_story2():
    b = R.choice([2, 3, 4, 5]); k = R.randint(2, 8); nm = who(); th = R.choice(["a pan of brownies", "a pizza", "a sheet of stickers", "a garden bed"])
    return mk('3.J', 4, f"{fs(1, b)} of {th} is left. {nm} and {k - 1} friends share it equally ({k} people in all). What fraction of the whole is each person's share?", fs(1, b * k), [fs(1, b + k), fs(k, b), fs(b, k), fs(1, k)], f"{fs(1, b)} ÷ {k} = {fs(1, b * k)}.", f"'1/{b * k}'")
def fj_model():
    n = R.randint(2, 6); b = R.choice([3, 4, 6, 8])
    return mk('3.J', 3, f"Which division sentence matches this question: How many {fs(1, b)}-size pieces are in {n} wholes?", f"{n} ÷ {fs(1, b)}", [f"{fs(1, b)} ÷ {n}", f"{n} × {fs(1, b)}", f"{n} − {fs(1, b)}"], f"Counting how many {fs(1, b)} pieces fit in {n} is {n} ÷ {fs(1, b)}.")
def fl_whole():
    n = R.randint(2, 12); b = R.choice([2, 3, 4, 5, 6, 8, 10])
    return mk('3.L', 3, f"What is {n} ÷ {fs(1, b)}?", n * b, [n + b, F(n, b).numerator if n % b == 0 else fs(n, b), n * b + n, n * b - b if n * b - b > 0 else n * b + 1, fs(1, n * b)], f"There are {b} unit fractions in each whole, so {n} × {b} = {n * b}.", CS(f"{n * b}"))
def fl_unit():
    b = R.choice([2, 3, 4, 5, 6, 8]); k = R.randint(2, 9)
    return mk('3.L', 3, f"What is {fs(1, b)} ÷ {k}?", fs(1, b * k), [fs(k, b), fs(b, k), fs(1, b + k), fs(1, b * k + b)], f"Dividing {fs(1, b)} into {k} equal parts gives {fs(1, b * k)}.", f"'1/{b * k}'")
rep(3, fj_story1); rep(3, fj_story2); rep(2, fj_model); rep(5, fl_whole); rep(5, fl_unit)

# ================================================================ 3.K add / subtract positive rational numbers
def fk_mixed():
    b, d = R.sample([2, 3, 4, 5, 6, 8], 2); w1, w2 = R.randint(1, 6), R.randint(1, 5); a = R.randint(1, b - 1); c = R.randint(1, d - 1)
    if gcd(a, b) != 1 or gcd(c, d) != 1: return False
    x, y = w1 + F(a, b), w2 + F(c, d); add = R.random() < .5
    if not add and x < y: x, y = y, x; w1, w2, a, b, c, d = w2, w1, c, d, a, b
    res = x + y if add else x - y
    if res <= 0: return False
    op = '+' if add else '−'
    wr = neq(ms(res), [ms(res + 1), ms(abs(res - 1)) if res > 1 else ms(res + 2), ms(res + F(1, b * d)), ms(F(abs(w1 - w2) + (w1 + w2 - abs(w1 - w2) if add else 0), 1) + F(a + c if add else abs(a - c), b + d) if False else (w1 + w2 if add else abs(w1 - w2)) + F(a + c if add else abs(a - c), b + d))])
    return mk('3.K', 4, f"What is {w1} {fs(a, b)} {op} {w2} {fs(c, d)}? Give the answer in simplest form.", ms(res), wr, f"Use common denominators for the fractions, then {'add' if add else 'subtract'} the whole numbers and fractions: {ms(res)}.")
def trim(n):                                       # thousandths -> shortest decimal text (at least one decimal place)
    s_ = fmt(n, 3).rstrip('0')
    return s_ + '0' if s_.endswith('.') else s_
def fk_dec():
    pa, pb = R.choice([(2, 1), (1, 2), (2, 2), (3, 2), (2, 3), (1, 3), (3, 1)])
    ar, br = R.randint(101, 9999), R.randint(11, 999)
    if ar % 10 == 0 or br % 10 == 0: return False
    A, Bv = ar * 10 ** (3 - pa), br * 10 ** (3 - pb); add = R.random() < .5
    if not add and A <= Bv: A, Bv, pa, pb, ar, br = Bv, A, pb, pa, br, ar
    if not add and A == Bv: return False
    res = A + Bv if add else A - Bv
    sa, sb = fmt(ar, pa), fmt(br, pb); right = trim(res)
    pr = len(right.split('.')[1]); u = 10 ** (3 - pr)
    mis = br * 10 ** (3 - pa) if pb < pa else Bv                      # digits lined up by the right edge instead of the decimal point
    cand = [trim(res + u), trim(res - u) if res > u else trim(res + 2 * u), trim(res + 10 * u), trim(res - 10 * u) if res > 10 * u else trim(res + 20 * u), trim(A + mis if add else abs(A - mis))]
    return mk('3.K', 3 if max(pa, pb) <= 2 else 4, f"What is {sa} {'+' if add else '−'} {sb}?", right, cand, f"Line up the decimal points and {'add' if add else 'subtract'}: {right}.")
def fk_frac():
    b = R.choice([6, 8, 10, 12]); d = R.choice([x for x in (2, 3, 4, 5) if b % x == 0 or True]); a = R.randint(1, b - 1); c = R.randint(1, d - 1)
    x, y = F(a, b), F(c, d)
    if x == y: return False
    add = R.random() < .5
    if not add and x < y: x, y = y, x
    res = x + y if add else x - y
    if res <= 0: return False
    nm = who()
    story = f"{nm} walked {fs(x.numerator, x.denominator)} mile in the morning and {fs(y.numerator, y.denominator)} mile after school. How many miles in all?" if add else f"{nm} had {fs(x.numerator, x.denominator)} of a tank of gas and used {fs(y.numerator, y.denominator)} of a tank. How much of a tank is left?"
    wr = neq(ms(res), [fs(x.numerator + y.numerator, x.denominator + y.denominator), ms(res + F(1, x.denominator * y.denominator)), ms(abs(x - y)) if add else ms(x + y), ms(res * 2)])
    return mk('3.K', 4, story + (" Give the answer in simplest form."), ms(res), wr, f"{ms(x)} {'+' if add else '−'} {ms(y)} = {ms(res)}.")
rep(5, fk_mixed); rep(5, fk_dec); rep(3, fk_frac)

# ================================================================ 4.A prime and composite
PR = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
CO = [n for n in range(4, 100) if n not in PR]
def pc_prime():
    p = R.choice(PR[3:]); cs = R.sample([c for c in CO if abs(c - p) < 25], 3)
    return mk('4.A', 3, "Which number is prime?", p, cs, f"{p} has exactly two factors, 1 and {p}. The others have more factors.")
def pc_comp():
    c = R.choice(CO); ps = R.sample([p for p in PR if abs(p - c) < 30 and p > 3], 3)
    fac = next(f for f in range(2, c) if c % f == 0)
    return mk('4.A', 3, "Which number is composite?", c, ps, f"{c} = {fac} × {c // fac}, so it has more than two factors.")
def pc_list():
    ps = R.sample(PR[2:], 3); bad = R.choice([n for n in CO if n % 2 and n < 60]);
    right = ', '.join(map(str, sorted(ps)))
    wr = []
    for _ in range(3):
        l = R.sample(PR[2:], 2) + [R.choice([n for n in CO if n % 2 and n < 60])]; R.shuffle(l); wr.append(', '.join(map(str, l)))
    return mk('4.A', 4, "Which list has only prime numbers?", right, wr, "A prime number has exactly two factors: 1 and itself.")
rep(5, pc_prime); rep(5, pc_comp); rep(3, pc_list)
H('4.A', 3, "Which number is neither prime nor composite?", "1", ["2", "9", "11"], "1 has only one factor, so it is neither prime nor composite.")
H('4.A', 3, "What is the only even prime number?", "2", ["4", "6", "1"], "2 has exactly two factors, 1 and 2. All other even numbers have 2 as an extra factor.")
H('4.A', 4, "A student says 51 is prime because it is odd. What is the best reply?", "51 is composite because 3 × 17 = 51", ["51 is prime because no even number divides it", "51 is prime because it ends in 1", "51 is neither prime nor composite"], "Being odd does not make a number prime. 51 has factors 3 and 17 besides 1 and 51.")

# ================================================================ 4.B multi-step equations with a letter
def eq_build():
    nm = who(); a = R.randint(40, 120); k = R.randint(2, 6); p = R.randint(3, 15); e = R.randint(2, 20)
    if a - k * p - e <= 0: return False
    th = R.choice(["books", "shirts", "tickets", "toys"])
    right = f"{a} − {k} × {p} − {e} = n"
    return mk('4.B', 4, f"{nm} has ${a}. {nm} buys {k} {th} that cost ${p} each and then spends ${e} on lunch. Let n be the money left. Which equation can be used to find n?", right, [f"{a} − {k} − {p} − {e} = n", f"{a} + {k} × {p} − {e} = n", f"({a} − {k}) × {p} − {e} = n", f"{a} − {k} × ({p} − {e}) = n"], f"Subtract the cost of {k} items ({k} × {p}) and the lunch from {a}.")
def eq_build2():
    nm = who(); a = R.randint(2, 9); b = R.randint(4, 12); c = R.randint(2, 15)
    th = R.choice(["rows", "boxes", "shelves"])
    right = f"{a} × {b} + {c} = t"
    return mk('4.B', 4, f"{nm} sets up {a} {th} with {b} books on each, and then adds {c} more books to a table. Let t be the total number of books. Which equation can be used to find t?", right, [f"{a} + {b} + {c} = t", f"{a} × ({b} + {c}) = t", f"{a} × {b} − {c} = t", f"{a} + {b} × {c} = t"], f"{a} × {b} is the books on the {th}, and then add {c} more.")
def eq_solve():
    n = R.randint(5, 40); a = R.randint(2, 9); b = R.randint(2, 20); form = R.randint(0, 2)
    if form == 0: q = f"{a} × n + {b} = {a * n + b}"; e = f"{a * n + b} − {b} = {a * n}, and {a * n} ÷ {a} = {n}."
    elif form == 1: q = f"{a} × n − {b} = {a * n - b}"; e = f"{a * n - b} + {b} = {a * n}, and {a * n} ÷ {a} = {n}."
    else: q = f"n ÷ {a} + {b} = {n // a * 0 + n + b}" if False else f"{a} × ({n} + {b}) = {a * (n + b)}"; e = None
    if form == 2:
        q = f"{a} × (n + {b}) = {a * (n + b)}"; e = f"{a * (n + b)} ÷ {a} = {n + b}, and {n + b} − {b} = {n}."
    return mk('4.B', 4, f"What value of n makes this equation true?   {q}", n, [n + 1, n - 1, n + b, n * a if n * a != n else n + 2, a * n + b if form != 2 else a * (n + b)], e, CS(f"{n}"))
def eq_word():
    nm = who(); box = R.randint(6, 18); g = R.randint(3, 9); extra = R.randint(2, 15); t = box * g + extra
    th = R.choice(["cans", "pencils", "stickers"])
    return mk('4.B', 4, f"{nm} packs {th} into {g} boxes with the same number in each box. {extra} {th} are left over, so {nm} had {t} {th} in all. Let n be the number in each box: {g} × n + {extra} = {t}. What is n?", box, [box + 1, box - 1, t - extra, (t + extra) // g if (t + extra) % g == 0 else box + g], f"{t} − {extra} = {g * box}, and {g * box} ÷ {g} = {box}.", CS(f"{box}"))
rep(3, eq_build); rep(3, eq_build2); rep(5, eq_solve); rep(3, eq_word)

# ================================================================ 4.C patterns from rules
def pat_list():
    mult = R.random() < .5; a = R.randint(2, 9) if mult else R.randint(2, 15); xs = [1, 2, 3, 4]
    ys = [a * x if mult else x + a for x in xs]
    q = f"Use the rule y = {a}x" if mult else f"Use the rule y = x + {a}"
    wr = []
    wr.append(', '.join(str(a * x if not mult else x + a) for x in xs))
    wr.append(', '.join(str(y + 1) for y in ys))
    wr.append(', '.join(str(a * x + 1 if mult else x * 2 + a) for x in xs))
    wr.append(', '.join(str((a + 1) * x if mult else x + a + 1) for x in xs))
    return mk('4.C', 3, f"{q}. What are the y-values when x = 1, 2, 3, 4?", ', '.join(map(str, ys)), wr, f"Put each x into the rule: {', '.join(map(str, ys))}.")
def pat_pair():
    mult = R.random() < .5; a = R.randint(2, 9) if mult else R.randint(2, 12); x = R.randint(3, 12); y = a * x if mult else x + a
    rule = f"y = {a}x" if mult else f"y = x + {a}"
    return mk('4.C', 3, f"Which ordered pair (x, y) follows the rule {rule}?", f"({x}, {y})", [f"({y}, {x})", f"({x}, {y + 1})", f"({x}, {x + a if mult else a * x})", f"({x + 1}, {y})"], f"With x = {x}: y = {y}.", f"'({x}, {y})'")
def pat_next():
    mult = R.random() < .5; a = R.randint(2, 9); s = R.randint(1, 6)
    seq = [s * a ** 0 * 0 + a * (i + 1) for i in range(5)] if mult else [s + a * i for i in range(5)]
    return False
def pat_missing():
    mult = R.random() < .5; a = R.randint(2, 9) if mult else R.randint(2, 12); xs = [2, 4, 6, 8]; ys = [a * x if mult else x + a for x in xs]; k = R.randint(1, 3)
    rule = f"y = {a}x" if mult else f"y = x + {a}"
    row = ' | '.join(f"{x}→{'__' if i == k else y}" for i, (x, y) in enumerate(zip(xs, ys)))
    return mk('4.C', 3, f"The rule is {rule}. Which number goes in the blank?   x→y:  {row}", ys[k], [ys[k] + 1, ys[k] - 1, ys[k] + a, xs[k]], f"For x = {xs[k]}, y = {ys[k]}.", CS(f"{ys[k]}"))
rep(5, pat_list); rep(4, pat_pair); rep(3, pat_missing)

# ================================================================ 4.D additive vs multiplicative
def pd_rule():
    mult = R.random() < .5; a = R.randint(2, 8); xs = [1, 2, 3, 4]; ys = [a * x if mult else x + a for x in xs]
    tab = '   '.join(f"x={x},y={y}" for x, y in zip(xs, ys))
    right = f"y = {a}x" if mult else f"y = x + {a}"
    wr = [f"y = x + {a}" if mult else f"y = {a}x", f"y = x + {a + 1}" if not mult else f"y = {a + 1}x", f"y = {a}x + 1" , f"y = x + {a * 2}" if mult else f"y = {a + 1}x"]
    return mk('4.D', 3, f"A table shows these pairs:   {tab}.   Which rule matches the table?", right, wr, f"{'Each y is ' + str(a) + ' times x' if mult else 'Each y is ' + str(a) + ' more than x'}.")
def pd_kind():
    mult = R.random() < .5; a = R.randint(2, 6); s = R.randint(1, 4)
    if mult: seq = [s * a ** i for i in range(4)] if False else [a * (i + 1) for i in range(5)]
    else: seq = [s + a * i for i in range(5)]
    return False
def pd_tables():
    a = R.randint(2, 6); c = R.randint(2, 9); xs = [1, 2, 3, 4]
    mt = '   '.join(f"({x}, {a * x})" for x in xs); at = '   '.join(f"({x}, {x + c})" for x in xs)
    right_is_mult = R.random() < .5
    q = "Which set of ordered pairs shows a multiplicative pattern (each y is a number times x)?" if right_is_mult else "Which set of ordered pairs shows an additive pattern (each y is x plus a number)?"
    right = mt if right_is_mult else at
    wr = [at if right_is_mult else mt, '   '.join(f"({x}, {a * x + 1 if x % 2 else a * x})" for x in xs), '   '.join(f"({x}, {x * x})" for x in xs)]
    return mk('4.D', 4, q, right, wr, "Multiplicative: y = a × x. Additive: y = x + a.")
def pd_word():
    nm = who(); a = R.randint(2, 9)
    return mk('4.D', 3, f"{nm} earns ${a} for every dog walked. Is the pattern for money earned (y) by dogs walked (x) additive or multiplicative?", f"multiplicative, y = {a}x", [f"additive, y = x + {a}", f"additive, y = {a}x", f"multiplicative, y = x + {a}"], f"Each dog adds the same amount, so earnings are {a} times the number of dogs.")
def pd_word2():
    nm = who(); a = R.randint(2, 9)
    return mk('4.D', 3, f"{nm} is {a} years older than a cousin. Is the pattern for {nm}'s age (y) by the cousin's age (x) additive or multiplicative?", f"additive, y = x + {a}", [f"multiplicative, y = {a}x", f"multiplicative, y = x + {a}", f"additive, y = {a}x"], f"The difference stays the same each year, so add {a}.")
rep(4, pd_rule); rep(4, pd_tables); rep(3, pd_word); rep(3, pd_word2)

# ================================================================ 4.E meaning of parentheses and brackets
def pe_first():
    a, b, c = R.sample(range(2, 12), 3); op = R.choice(["×", "−", "+"])
    exprs = [(f"{a} × ({b} + {c})", f"add {b} and {c} first"), (f"({a} + {b}) × {c}", f"add {a} and {b} first")] if True else []
    e, ans = R.choice(exprs)
    wr = [f"multiply {a} and {b} first", f"multiply by {c} first", f"subtract first", f"multiply {b} and {c} first", f"add {a} and {c} first"]
    wr = [w for w in wr if w != ans]
    return mk('4.E', 2, f"In the expression {e}, what do the parentheses tell you to do first?", ans, wr, "Parentheses show which operation to do first.")
def pe_write():
    a, b, c = R.sample(range(2, 10), 3)
    f1 = R.choice(["add", "subtract"])
    if f1 == "add":
        return mk('4.E', 3, f"Which expression means add {b} and {c}, and then multiply the sum by {a}?", f"{a} × ({b} + {c})", [f"{a} × {b} + {c}", f"{a} + {b} × {c}", f"({a} × {b}) + {c}", f"{a} + ({b} × {c})"], f"The sum {b} + {c} is in parentheses, then multiplied by {a}.")
    b, c = max(b, c) + 1, min(b, c)
    return mk('4.E', 3, f"Which expression means subtract {c} from {b}, and then multiply the difference by {a}?", f"({b} − {c}) × {a}", [f"{b} − {c} × {a}", f"{b} − ({c} × {a})", f"({b} × {a}) − {c}", f"{a} − ({b} − {c})"], f"The difference {b} − {c} is in parentheses, then multiplied by {a}.")
def pe_words():
    a, b, c = R.sample(range(2, 10), 3)
    return mk('4.E', 3, f"Which phrase describes the expression [{a} × ({b} + {c})] − {a}?", f"add {b} and {c}, multiply the sum by {a}, then subtract {a}", [f"multiply {a} and {b}, add {c}, then subtract {a}", f"subtract {a} from {b}, then add {c}, then multiply by {a}", f"add {a} and {b}, multiply by {c}, then subtract {a}"], "Work from the inside: the parentheses first, then the brackets, then subtract.")
def pe_same():
    a, b, c = R.sample(range(2, 10), 3)
    return mk('4.E', 4, f"Which statement explains why ({a} + {b}) × {c} and {a} + {b} × {c} can have different values?", "The parentheses change which operation is done first", ["Parentheses add more numbers", "Multiplication always comes last", "The numbers are in a different order"], "Without parentheses, you multiply first. With them, you add first.")
rep(4, pe_first); rep(3, pe_write); rep(2, pe_words); rep(2, pe_same)

# ================================================================ 4.F simplify numerical expressions (up to two levels of grouping)
def ltr(s):
    toks = re.findall(r'\d+|[+\-*/]', s.replace('×', '*').replace('−', '-').replace('÷', '/').replace('[', '').replace(']', '').replace('(', '').replace(')', ''))
    v = int(toks[0]); i = 1
    while i < len(toks):
        o, n = toks[i], int(toks[i + 1])
        v = v + n if o == '+' else v - n if o == '-' else v * n if o == '*' else v / n
        i += 2
    return v
def simp():
    a, b, d = R.randint(2, 9), R.randint(2, 9), R.randint(2, 6); c = d + R.randint(1, 6); m = R.randint(2, 6)
    forms = [f"{a} + [{b} × ({c} − {d})]", f"[{a} + {b}] × ({c} − {d})", f"{a} × [({b} + {c}) − {d}]", f"[{a} × ({b} + {c})] − {d}", f"({a} + {b}) × {c} − {d}", f"{a} × ({b} + {c}) + {d}",
             f"[{a} + ({b} × {c})] − {d}", f"{(b + c) * m} ÷ ({b} + {c}) + {d}", f"[{a} × {b}] − ({c} − {d})", f"{a} + {b} × ({c} − {d})", f"{(c - d) * m * a} ÷ [{a} × ({c} − {d})] + {b}"]
    e = R.choice(forms)
    py = e.replace('×', '*').replace('÷', '//').replace('−', '-').replace('[', '(').replace(']', ')')
    v = eval(py)
    if v <= 0 or v > 500: return False
    wr = [ltr(e), eval(re.sub(r'[\[\]\(\)]', '', py)) if '//' not in py else v + 2, v + 1, v - 1, v + 10, v * 2 if v < 250 else v + 3]
    wr = [int(w) for w in wr if isinstance(w, (int, float)) and w == int(w) and w > 0]
    lvl2 = '[' in e
    return mk('4.F', 4 if lvl2 else 3, f"What is the value of {e}?", v, wr, "Work inside the innermost parentheses first, then the brackets, then the rest.", f"str({py.replace('//', '//')})")
rep(12, simp, tries=300)

# ================================================================ 4.G volume formulas
H('4.G', 3, "Which formula finds the volume of a rectangular prism?", "V = l × w × h", ["V = l + w + h", "V = 2l + 2w", "V = l × w"], "Volume is length times width times height.")
H('4.G', 3, "Which formula finds the volume of a cube with side length s?", "V = s × s × s", ["V = 4 × s", "V = s × s", "V = 6 × s"], "A cube has equal length, width, and height.")
H('4.G', 3, "In the formula V = B × h, what does B stand for?", "the area of the base", ["the length of one edge", "the number of faces", "the perimeter of the base"], "B is the area of the base, and h is the height.")
H('4.G', 4, "Why does V = B × h work for a rectangular prism?", "each layer has B cubes and there are h layers", ["each layer has h cubes and there are B layers", "the cubes are all on the bottom", "the prism has B corners"], "The base layer holds B unit cubes, and h layers stack up.")
def vg_calc():
    l, w, h = R.randint(2, 12), R.randint(2, 9), R.randint(2, 10); B_ = l * w
    return mk('4.G', 3, f"A rectangular prism has a base that is {l} units by {w} units and a height of {h} units. What is its volume?", f"{B_ * h} cubic units", [f"{l + w + h} cubic units", f"{B_ + h} cubic units", f"{2 * (l * w + l * h + w * h)} cubic units", f"{B_} cubic units"], f"B = {l} × {w} = {B_}, and V = {B_} × {h} = {B_ * h}.", f"'{B_ * h} cubic units'")
def vg_cube():
    s = R.randint(2, 9)
    return mk('4.G', 3, f"What is the volume of a cube with a side length of {s} inches?", f"{s ** 3} cubic inches", [f"{s * s} cubic inches", f"{s * 3} cubic inches", f"{s * 6} cubic inches", f"{s ** 3 + s} cubic inches"], f"{s} × {s} × {s} = {s ** 3}.", f"'{s ** 3} cubic inches'")
def vg_B():
    B_ = R.randint(10, 60); h = R.randint(2, 9)
    return mk('4.G', 3, f"The area of the base of a prism is {B_} square centimeters. The height is {h} centimeters. What is the volume?", f"{B_ * h} cubic centimeters", [f"{B_ + h} cubic centimeters", f"{B_ * h} square centimeters", f"{B_ * h * 2} cubic centimeters", f"{B_ * (h + 1)} cubic centimeters"], f"V = B × h = {B_} × {h} = {B_ * h}.", f"'{B_ * h} cubic centimeters'")
rep(4, vg_calc); rep(3, vg_cube); rep(3, vg_B)

# ================================================================ 4.H perimeter / area / volume problems
def ph_area():
    l, w = R.randint(5, 30), R.randint(3, 20)
    if l == w: return False
    nm = who()
    return mk('4.H', 3, f"{nm}'s garden is a rectangle {l} feet long and {w} feet wide. What is the area of the garden?", f"{l * w} square feet", [f"{2 * (l + w)} square feet", f"{l + w} square feet", f"{l * w} feet", f"{l * w * 2} square feet"], f"Area = {l} × {w} = {l * w} square feet.", f"'{l * w} square feet'")
def ph_perim():
    l, w = R.randint(5, 30), R.randint(3, 20); nm = who()
    if l == w: return False
    return mk('4.H', 3, f"{nm} puts a fence around a rectangular pen that is {l} meters by {w} meters. How many meters of fence does {nm} need?", f"{2 * (l + w)} meters", [f"{l * w} meters", f"{l + w} meters", f"{2 * l + w} meters", f"{4 * (l + w)} meters"], f"Perimeter = 2 × ({l} + {w}) = {2 * (l + w)}.", f"'{2 * (l + w)} meters'")
def ph_missing():
    l, w = R.randint(6, 25), R.randint(3, 15); A = l * w
    if l == w: return False
    return mk('4.H', 4, f"A rectangle has an area of {A} square units and a length of {l} units. What is its perimeter?", f"{2 * (l + w)} units", [f"{l + w} units", f"{A} units", f"{2 * l + w} units", f"{2 * (A + l)} units"], f"The width is {A} ÷ {l} = {w}. Perimeter = 2 × ({l} + {w}) = {2 * (l + w)}.", f"'{2 * (l + w)} units'")
def ph_vol_miss():
    B_ = R.randint(6, 40); h = R.randint(3, 12); V = B_ * h; nm = who()
    return mk('4.H', 4, f"A box has a volume of {V} cubic inches. The area of its base is {B_} square inches. How tall is the box?", f"{h} inches", [f"{V - B_} inches", f"{V + B_} inches", f"{h + 1} inches", f"{V} inches"], f"h = V ÷ B = {V} ÷ {B_} = {h}.", f"'{h} inches'")
def ph_tank():
    l, w, h = R.randint(3, 10), R.randint(3, 8), R.randint(3, 9); nm = who()
    return mk('4.H', 4, f"A fish tank is {l} feet long, {w} feet wide, and {h} feet tall. How many cubic feet of water does it hold when it is full?", f"{l * w * h} cubic feet", [f"{l + w + h} cubic feet", f"{2 * (l * w + w * h + l * h)} cubic feet", f"{l * w} cubic feet", f"{l * w * h + l} cubic feet"], f"V = {l} × {w} × {h} = {l * w * h}.", f"'{l * w * h} cubic feet'")
def ph_L():
    l, w = R.randint(8, 20), R.randint(6, 15); c, d = R.randint(2, l - 3), R.randint(2, w - 3)
    A = l * w - c * d
    return mk('4.H', 5, f"A rectangular playground is {l} meters by {w} meters. A rectangular sandbox that is {c} meters by {d} meters is built inside it. What is the area of the playground that is NOT the sandbox?", f"{A} square meters", [f"{l * w} square meters", f"{c * d} square meters", f"{(l - c) * (w - d)} square meters", f"{l * w + c * d} square meters"], f"{l} × {w} = {l * w}, and {l * w} − {c * d} = {A}.", f"'{A} square meters'")
rep(3, ph_area); rep(3, ph_perim); rep(3, ph_missing); rep(3, ph_vol_miss); rep(3, ph_tank); rep(3, ph_L)

# ================================================================ 5 classify two-dimensional figures
H('5', 3, "Which statement is true?", "Every square is a rectangle.", ["Every rectangle is a square.", "Every triangle has four sides.", "Every quadrilateral is a square."], "A square has 4 right angles and opposite sides parallel, so it is a rectangle.")
H('5', 3, "Which statement is true?", "Every square is a rhombus.", ["Every rhombus is a square.", "Every rectangle is a rhombus.", "Every trapezoid is a square."], "A square has 4 equal sides, so it is a rhombus.")
H('5', 3, "Every rectangle is also a ___.", "parallelogram", ["square", "rhombus", "triangle"], "A rectangle has two pairs of parallel sides.")
H('5', 3, "Every rhombus is also a ___.", "parallelogram", ["rectangle", "square", "pentagon"], "A rhombus has two pairs of parallel sides.")
H('5', 3, "Every parallelogram is also a ___.", "quadrilateral", ["rectangle", "square", "rhombus"], "A parallelogram has 4 sides.")
H('5', 3, "Which attribute do ALL quadrilaterals share?", "4 sides", ["4 right angles", "4 equal sides", "2 pairs of parallel sides"], "Quadrilateral means 4 sides.")
H('5', 3, "Which figure has 4 equal sides but no right angles?", "a rhombus that is not a square", ["a rectangle", "a square", "a triangle"], "A rhombus has 4 equal sides. Only a square rhombus has right angles.")
H('5', 3, "Which figure belongs in the group 'parallelograms' but NOT in the group 'rectangles'?", "a rhombus with no right angles", ["a square", "a rectangle", "a triangle"], "A rhombus with slanted angles is a parallelogram but not a rectangle.")
H('5', 4, "A figure has 4 right angles and 4 equal sides. Which names does it have?", "square, rectangle, rhombus, parallelogram, quadrilateral", ["rectangle only", "square and triangle", "rhombus only"], "A square belongs to all of those sets.")
H('5', 3, "A figure has exactly 3 sides. What is it?", "triangle", ["quadrilateral", "pentagon", "parallelogram"], "Three sides make a triangle.")
H('5', 3, "A triangle has 3 sides of different lengths. What kind of triangle is it?", "scalene", ["equilateral", "isosceles", "quadrilateral"], "Scalene means no equal sides.")
H('5', 3, "A triangle has 3 sides of equal length. What kind of triangle is it?", "equilateral", ["scalene", "right", "quadrilateral"], "Equilateral means all sides equal.")
H('5', 3, "A triangle has a right angle. What kind of triangle is it?", "right triangle", ["equilateral triangle", "obtuse triangle", "acute triangle"], "A right triangle has one 90° angle.")
H('5', 4, "In a Venn diagram of quadrilaterals, where should the circle for squares go?", "inside the circle for rectangles", ["outside the circle for rectangles", "inside the circle for triangles", "so that it only touches the rectangle circle"], "Every square is a rectangle, so squares are a subset of rectangles.")
H('5', 3, "How many pairs of parallel sides does a parallelogram have?", "2", ["1", "3", "4"], "A parallelogram has two pairs of parallel sides.")
H('5', 4, "Why is a square NOT the same as every rectangle?", "a rectangle can have sides of different lengths", ["a rectangle has 3 sides", "a rectangle has no right angles", "a square has more than 4 sides"], "A rectangle's sides can be unequal, but a square's sides must all be equal.")
H('5', 3, "An angle that measures exactly 90 degrees is called what?", "a right angle", ["an acute angle", "an obtuse angle", "a straight angle"], "A right angle measures exactly 90 degrees.")
H('5', 4, "Which figure could NOT be a rhombus?", "a rectangle with one long side and one short side", ["a square", "a diamond shape with 4 equal sides", "a slanted shape with 4 equal sides"], "A rhombus needs 4 equal sides.")

# ================================================================ 6 volume with unit cubes
H('6.A', 2, "What is a unit cube?", "a cube with side length of 1 unit", ["a cube with side length of 10 units", "a flat square with side length of 1 unit", "any cube that is red"], "A unit cube has edges of 1 unit and a volume of 1 cubic unit.")
H('6.A', 3, "A unit cube has a volume of what?", "1 cubic unit", ["1 square unit", "1 unit", "6 cubic units"], "One unit cube has a volume of 1 cubic unit.")
H('6.A', 3, "Volume is measured in which type of units?", "cubic units", ["square units", "linear units", "degrees"], "Volume measures space inside, in cubic units.")
H('6.A', 3, "To find volume with cubes, how must the cubes fill the solid?", "with no gaps or overlaps", ["with some gaps", "with some overlapping", "only on the bottom"], "Unit cubes must fill the figure with no gaps and no overlaps.")
def vc_total():
    n = R.randint(12, 90); nm = who(); u = R.choice([("cubic centimeters", "1-centimeter cubes"), ("cubic inches", "1-inch cubes"), ("cubic feet", "1-foot cubes")])
    return mk('6.A', 3, f"{nm} fills a box completely with {n} {u[1]}, with no gaps or overlaps. What is the volume of the box?", f"{n} {u[0]}", [f"{n} {u[0].replace('cubic', 'square')}", f"{n + 10} {u[0]}", f"{n // 2} {u[0]}", f"{n * 2} {u[0]}"], f"Each cube is 1 cubic unit, so {n} cubes make {n} {u[0]}.", f"'{n} {u[0]}'")
def vc_layers():
    r, c, k = R.randint(2, 6), R.randint(2, 6), R.randint(2, 7); nm = who()
    return mk('6.B', 3, f"{nm} builds a prism from unit cubes. Each layer has {r} rows with {c} cubes in each row. There are {k} layers. What is the volume in cubic units?", r * c * k, [r + c + k, r * c + k, r * c, r * c * k + r], f"One layer has {r} × {c} = {r * c} cubes. {r * c} × {k} = {r * c * k}.", CS(f"{r * c * k}"))
def vc_base():
    B_ = R.randint(8, 40); k = R.randint(2, 9)
    return mk('6.B', 3, f"The bottom layer of a prism has {B_} unit cubes. The prism is {k} layers tall. What is its volume?", f"{B_ * k} cubic units", [f"{B_ + k} cubic units", f"{B_ * k} square units", f"{B_ * (k + 1)} cubic units", f"{B_} cubic units"], f"{B_} cubes per layer × {k} layers = {B_ * k}.", f"'{B_ * k} cubic units'")
def vc_find_h():
    r, c, k = R.randint(2, 6), R.randint(2, 6), R.randint(3, 8); V = r * c * k
    return mk('6.B', 4, f"A prism holds {V} unit cubes. The base has {r} rows with {c} cubes in each row. How many layers tall is the prism?", k, [k + 1, k - 1, V - r * c, r + c], f"Each layer has {r * c} cubes, so {V} ÷ {r * c} = {k}.", CS(f"{k}"))
rep(4, vc_total); rep(4, vc_layers); rep(3, vc_base); rep(3, vc_find_h)

# ================================================================ 7 unit conversions
CONV = [("feet", "inches", 12), ("yards", "feet", 3), ("gallons", "quarts", 4), ("quarts", "pints", 2), ("pints", "cups", 2), ("pounds", "ounces", 16), ("tons", "pounds", 2000), ("hours", "minutes", 60), ("minutes", "seconds", 60),
        ("meters", "centimeters", 100), ("kilometers", "meters", 1000), ("liters", "milliliters", 1000), ("kilograms", "grams", 1000), ("centimeters", "millimeters", 10), ("meters", "millimeters", 1000), ("gallons", "cups", 16), ("yards", "inches", 36)]
def cv_big():
    big, small, f = R.choice(CONV); n = R.randint(2, 15)
    if f >= 1000: n = R.randint(2, 9)
    r = n * f
    return mk('7', 3, f"{n} {big} = ___ {small}", cm(r), [cm(n), cm(n + f), cm(r + f), cm(r // 10 if r % 10 == 0 else r + 10), cm(f - n) if f > n else cm(r - 10)], f"1 {'foot' if big == 'feet' else big[:-1] if big.endswith('s') else big} = {cm(f)} {small}, so {n} × {cm(f)} = {cm(r)}.", CK(f"{n}*{f}"))
def cv_small():
    big, small, f = R.choice(CONV); n = R.randint(2, 12); r = n * f
    if f >= 1000: n = R.randint(2, 9); r = n * f
    return mk('7', 3, f"{cm(r)} {small} = ___ {big}", cm(n), [cm(r), cm(n + 1), cm(n * 10), cm(r - f) if r - f > 0 else cm(n + 2), cm(n * f * f) if n * f * f < 10 ** 6 else cm(n + 3)], f"{cm(r)} ÷ {cm(f)} = {n}.", CK(f"{n}"))
def cv_word():
    nm = who(); big, small, f = R.choice([c for c in CONV if c[2] <= 100]); n = R.randint(2, 12); r = n * f
    unit = {"feet": "ribbon", "yards": "rope", "meters": "string", "pounds": "bag of flour", "gallons": "tank of water", "liters": "bottle of juice", "hours": "movie", "kilograms": "box", "quarts": "pitcher", "pints": "jug", "kilometers": "trail", "tons": "truck load", "centimeters": "pencil", "minutes": "song"}
    q = f"{nm} has a {unit.get(big, 'container')} measuring {n} {big}. How many {small} is that?"
    return mk('7', 3, q, cm(r), [cm(n), cm(r + f), cm(r - f) if r > f else cm(r + 2 * f), cm(f)], f"{n} × {f} = {r}.", CK(f"{r}"))
def cv_dec():
    big, small, f = R.choice([("kilometers", "meters", 1000), ("liters", "milliliters", 1000), ("kilograms", "grams", 1000), ("meters", "centimeters", 100), ("meters", "millimeters", 1000)])
    n10 = R.randint(11, 99)                    # tenths
    if n10 % 10 == 0: return False
    r = n10 * f // 10
    return mk('7', 4, f"{fmt(n10, 1)} {big} = ___ {small}", cm(r), [cm(r * 10), cm(r // 10) if r % 10 == 0 else cm(r + f), cm(n10), cm(r + f // 10)], f"{fmt(n10, 1)} × {cm(f)} = {cm(r)}.", CK(f"{r}"))
def cv_compare():
    big, small, f = R.choice([c for c in CONV if c[2] <= 1000]); n = R.randint(2, 9); nm = who()
    m = n * f + R.choice([-1, 1, 0]) * R.randint(1, max(f // 4, 1))
    ans = GT if n * f > m else LT if n * f < m else EQ
    if n * f == m: return False
    return mk('7', 4, f"Which symbol makes this true?   {n} {big} ___ {cm(m)} {small}", ans, [x for x in (LT, GT, EQ) if x != ans], f"{n} {big} = {cm(n * f)} {small}, which is {ans.split(' (')[0]} {cm(m)} {small}.", need=2)
def cv_multi():
    nm = who(); g = R.randint(2, 6)
    return mk('7', 4, f"{nm} drinks 1 cup of water at a time. How many cups of water are in {g} gallons?", cm(g * 16), [cm(g * 4), cm(g * 8), cm(g * 12), cm(g * 32)], f"1 gallon = 4 quarts = 8 pints = 16 cups, so {g} × 16 = {g * 16}.", CK(f"{g * 16}"))
rep(5, cv_big); rep(5, cv_small); rep(4, cv_word); rep(4, cv_dec); rep(3, cv_compare); rep(2, cv_multi)

# ================================================================ 8 coordinate plane
H('8.A', 2, "In the coordinate plane, the two number lines that meet at right angles are called what?", "axes", ["origins", "ordered pairs", "grids"], "The horizontal x-axis and vertical y-axis are the axes.")
H('8.A', 3, "What are the coordinates of the origin?", "(0, 0)", ["(1, 1)", "(0, 1)", "(1, 0)"], "The origin is where the axes cross, at zero on each line.")
H('8.A', 3, "In an ordered pair (x, y), which number is the x-coordinate?", "the first number", ["the second number", "the larger number", "the number with the greater value"], "The x-coordinate comes first and tells the distance along the x-axis.")
H('8.A', 3, "The x-axis runs in which direction?", "horizontally (left to right)", ["vertically (up and down)", "diagonally", "in a circle"], "The x-axis is the horizontal number line.")
H('8.A', 3, "The y-coordinate tells you how far to move in which direction?", "up from the x-axis", ["right from the y-axis", "left from the origin", "down from the origin"], "The y-coordinate shows the vertical distance.")
H('8.A', 4, "In the first quadrant of the coordinate plane, which is true about both coordinates?", "both are positive (or zero)", ["both are negative", "x is negative and y is positive", "x is positive and y is negative"], "The first quadrant is the upper right area where x and y are 0 or greater.")
def cp_move():
    x, y = R.randint(1, 9), R.randint(1, 9)
    if x == y: return False
    return mk('8.B', 3, f"To graph the point ({x}, {y}), what should you do?", f"Start at (0, 0), move {x} right, then {y} up", [f"Start at (0, 0), move {y} right, then {x} up", f"Start at (0, 0), move {x} up, then {y} right", f"Start at (0, 0), move {x + y} right"], f"The first number is how far right (x), the second is how far up (y).")
def cp_read():
    x, y = R.randint(1, 9), R.randint(1, 9)
    if x == y: return False
    return mk('8.B', 3, f"A point is {pl(x, 'unit')} to the right of the origin and {pl(y, 'unit')} up. What is its ordered pair?", f"({x}, {y})", [f"({y}, {x})", f"({x}, {x})", f"({x + y}, 0)", f"({x}, {y + 1})"], f"Right is x and up is y: ({x}, {y}).", f"'({x}, {y})'")
def cp_pattern():
    mult = R.random() < .5; a = R.randint(2, 6); xs = [1, 2, 3, 4]; ys = [a * x if mult else x + a for x in xs]; rule = f"y = {a}x" if mult else f"y = x + {a}"
    right = ', '.join(f"({x}, {y})" for x, y in zip(xs, ys))
    wr = [', '.join(f"({y}, {x})" for x, y in zip(xs, ys)), ', '.join(f"({x}, {y + 1})" for x, y in zip(xs, ys)), ', '.join(f"({x}, {a * x if not mult else x + a})" for x in xs)]
    return mk('8.C', 4, f"Which ordered pairs can be graphed from the rule {rule} when x = 1, 2, 3, 4?", right, wr, f"Put each x into the rule to get y, and write (x, y).")
def cp_table():
    a = R.randint(2, 6); nm = who(); th = R.choice([("tickets", "dollars"), ("bags", "apples"), ("packs", "cards")]); x = R.randint(2, 9)
    return mk('8.C', 4, f"Each of {nm}'s {th[0]} costs {a} {th[1]}... ", "x", ["y", "z", "w"], "x") if False else False
def cp_input():
    a = R.randint(2, 8); x = R.randint(2, 9); y = a * x; nm = who()
    return mk('8.C', 4, f"In an input-output table, the output is always {a} times the input. If the input is {x}, which ordered pair (input, output) would be graphed?", f"({x}, {y})", [f"({y}, {x})", f"({x}, {x + a})", f"({x}, {y + a})", f"({x + a}, {y})"], f"{a} × {x} = {y}, so the point is ({x}, {y}).", f"'({x}, {y})'")
def cp_dist():
    x1, y = R.randint(1, 5), R.randint(1, 9); x2 = x1 + R.randint(2, 6)
    return mk('8.C', 4, f"Two points are graphed at ({x1}, {y}) and ({x2}, {y}). How far apart are they?", f"{pl(x2 - x1, 'unit')}", [f"{x2 + x1} units", f"{y} units", f"{x2 - x1 + 1} units", f"{x2 * y} units"], f"They have the same y-coordinate, so subtract the x-values: {x2} − {x1} = {x2 - x1}.", f"'{x2 - x1} units'")
rep(3, cp_move); rep(3, cp_read); rep(4, cp_pattern); rep(3, cp_input); rep(3, cp_dist)

# ================================================================ 9 data
H('9.A', 2, "Which display is best for showing how many students chose each favorite sport (categories)?", "bar graph", ["scatterplot", "stem-and-leaf plot", "number line"], "Bar graphs and frequency tables show categorical data.")
H('9.A', 3, "Which display is best for showing the lengths of pencils measured in fractions of an inch?", "dot plot", ["bar graph", "pie chart", "scatterplot"], "A dot plot shows numerical data such as measurements.")
H('9.A', 3, "A stem-and-leaf plot shows which kind of data?", "numerical data", ["only color names", "only shape names", "only pictures"], "A stem-and-leaf plot organizes numbers.")
H('9.A', 3, "Which data set is categorical?", "favorite pizza toppings", ["heights of plants in inches", "ages of students in years", "times of races in seconds"], "Categories like toppings are sorted into groups, not measured.")
H('9.A', 3, "A frequency table is used to show what?", "how many times each value or category appears", ["the average of the data", "the biggest number in a set", "the shape of an object"], "Frequency means how often.")
def dp_total():
    vals = sorted(R.sample([F(1, 4), F(1, 2), F(3, 4), F(1), F(5, 4)], 4)); cnts = [R.randint(1, 5) for _ in vals]
    unit = R.choice(["inches", "pounds", "cups"]); thing = {"inches": "worms", "pounds": "bags of potatoes", "cups": "bottles of juice"}[unit]
    rows = "   ".join(f"{ms(v)}: {'●' * c}" for v, c in zip(vals, cnts)); tot = sum(cnts); mx = max(cnts); big = vals[cnts.index(mx)]
    if R.random() < .5:
        return mk('9.C', 3, f"A dot plot shows the measures of {thing} in {unit}.   {rows}   How many are there in all?", tot, [tot + 1, tot - 1, mx, tot + 2], f"Count all the dots: {' + '.join(map(str, cnts))} = {tot}.", CS(f"{tot}"))
    k = R.randint(1, 3); sub = vals[k]; n_less = sum(c for v, c in zip(vals, cnts) if v < sub)
    return mk('9.C', 4, f"A dot plot shows the measures of {thing} in {unit}.   {rows}   How many measure less than {ms(sub)} {unit}?", n_less, [n_less + 1, n_less + cnts[k], max(n_less - 1, 0), tot], f"Add the dots for values less than {ms(sub)}: {n_less}.", CS(f"{n_less}"))
def sl_calc():
    stems = sorted(R.sample(range(1, 7), 3)); leaves = {s: sorted(R.sample(range(0, 10), R.randint(2, 5))) for s in stems}
    row = "   ".join(f"{s} | {' '.join(map(str, leaves[s]))}" for s in stems)
    vals = [s * 10 + l for s in stems for l in leaves[s]]; mx, mn = max(vals), min(vals); n = len(vals)
    k = R.randint(0, 2)
    unit = R.choice(["points", "minutes", "inches"]); nm = who()
    thr = R.choice(vals) + R.choice([0, 1]); cnt_ = sum(1 for v in vals if v > thr)
    form = R.randint(0, 2)
    if form == 0: return mk('9.C', 3, f"A stem-and-leaf plot shows scores in {unit}.   Stem | Leaves:   {row}   What is the greatest value?", mx, [mn, mx + 1, n, mx - 1], f"The last stem and its greatest leaf give {mx}.", CS(f"{mx}"))
    if form == 1: return mk('9.C', 3, f"A stem-and-leaf plot shows scores in {unit}.   Stem | Leaves:   {row}   How many values are in the data set?", n, [n + 1, n - 1, len(stems), mx], f"Count every leaf: {n}.", CS(f"{n}"))
    return mk('9.C', 4, f"A stem-and-leaf plot shows scores in {unit}.   Stem | Leaves:   {row}   How many values are greater than {thr}?", cnt_, [cnt_ + 1, max(cnt_ - 1, 0), n - cnt_ if n - cnt_ != cnt_ else cnt_ + 2, thr], f"Count the values above {thr}: {cnt_}.", CS(f"{cnt_}")) if cnt_ > 0 else False
def bar_calc():
    cats = R.sample(["soccer", "tennis", "swimming", "golf", "baseball", "karate"], 3); cnts = [R.randint(4, 20) for _ in cats]
    if len(set(cnts)) < 3: return False
    rows = "   ".join(f"{c}: {n}" for c, n in zip(cats, cnts)); i = cnts.index(max(cnts)); j = cnts.index(min(cnts)); diff = cnts[i] - cnts[j]
    if R.random() < .5:
        return mk('9.C', 4, f"A bar graph shows the number of students who chose each sport.   {rows}   How many more students chose {cats[i]} than {cats[j]}?", diff, [diff + 1, diff - 1, cnts[i], sum(cnts)], f"{cnts[i]} − {cnts[j]} = {diff}.", CS(f"{diff}"))
    tot = sum(cnts)
    return mk('9.C', 3, f"A bar graph shows the number of students who chose each sport.   {rows}   How many students are represented in all?", tot, [tot + 1, tot - 1, cnts[i], tot + 10], f"{' + '.join(map(str, cnts))} = {tot}.", CS(f"{tot}"))
def scat_pairs():
    nm = who(); pairs = sorted(R.sample(range(1, 9), 4)); ys = [R.randint(2, 9) for _ in pairs]
    k = R.randint(0, 3)
    return mk('9.B', 3, f"A scatterplot shows hours of practice (x) and the number of free throws made (y). One student practiced {pairs[k]} hours and made {ys[k]} free throws. Which ordered pair is graphed for this student?", f"({pairs[k]}, {ys[k]})", [f"({ys[k]}, {pairs[k]})", f"({pairs[k]}, {pairs[k]})", f"({ys[k]}, {ys[k]})" if ys[k] != pairs[k] else f"({pairs[k] + 1}, {ys[k]})", f"({pairs[k]}, {ys[k] + 1})"], f"Write the x-value first, then the y-value: ({pairs[k]}, {ys[k]}).", f"'({pairs[k]}, {ys[k]})'") if pairs[k] != ys[k] else False
H('9.B', 3, "What kind of data does a scatterplot show?", "paired data, where each point has an x and a y", ["only categories", "only one list of numbers", "only fractions"], "A scatterplot has one point for each pair of values.")
H('9.B', 3, "How many points are on a scatterplot if 12 students each have a (hours, score) pair?", "12", ["2", "6", "24"], "Each pair makes one point.")
rep(5, dp_total); rep(5, sl_calc); rep(4, bar_calc); rep(4, scat_pairs)

# ================================================================ 10 personal financial literacy
H('10.A', 3, "Which tax is added to the price of items you buy in a store?", "sales tax", ["income tax", "property tax", "payroll tax"], "Sales tax is collected when you buy goods.")
H('10.A', 3, "Which tax is paid by people who own land or buildings?", "property tax", ["sales tax", "payroll tax", "income tax"], "Property tax is based on what a person owns.")
H('10.A', 3, "Which tax is based on the money a person earns?", "income tax", ["property tax", "sales tax", "tax on groceries only"], "Income tax is a percent of earnings.")
H('10.A', 3, "Which tax is taken from a worker's paycheck to help pay for programs like Social Security and Medicare?", "payroll tax", ["property tax", "sales tax", "gas tax"], "Payroll taxes come out of paychecks.")
H('10.A', 4, "A family pays tax on their house every year. What kind of tax is that?", "property tax", ["sales tax", "payroll tax", "income tax"], "A tax on owned property is property tax.")
H('10.B', 3, "What is gross income?", "all the money earned before anything is taken out", ["money left after taxes", "money spent each month", "money saved in a bank"], "Gross income is the total before deductions such as taxes.")
H('10.B', 3, "What is net income?", "the money left after taxes and deductions are taken out", ["all the money earned before taxes", "the money you owe", "the price of an item"], "Net income is your take-home pay.")
def gn_calc():
    nm = who(); g = R.randint(10, 60) * 50; t = R.randint(2, 9) * 25
    if t >= g: return False
    return mk('10.B', 3, f"{nm}'s gross pay for the week is ${cm(g)}. Taxes and other deductions are ${cm(t)}. What is {nm}'s net pay?", f"${cm(g - t)}", [f"${cm(g + t)}", f"${cm(g - t + 100)}", f"${cm(t)}", f"${cm(g - t - 50)}" if g - t > 50 else f"${cm(g - t + 200)}"], f"Net pay = gross pay − deductions = {cm(g)} − {cm(t)} = {cm(g - t)}.", f"'${cm(g - t)}'" if False else f"'$' + f'{g - t:,}'")
H('10.C', 3, "Which payment method takes money directly from your bank account when you buy something?", "debit card", ["credit card", "a gift wrapper", "a coupon"], "A debit card pays with money you already have in the bank.")
H('10.C', 3, "Which payment method lets you borrow money that you must pay back later?", "credit card", ["debit card", "cash", "a gift card with money loaded"], "A credit card is a loan; you must pay it back, often with interest.")
H('10.C', 3, "What is one disadvantage of using a credit card?", "you may owe interest if you do not pay the full bill", ["it always takes money from your bank right away", "you can never buy anything", "it never needs to be paid"], "Unpaid credit card balances can grow with interest.")
H('10.C', 3, "What is one advantage of paying with cash?", "you can only spend the money you have", ["you can borrow more than you have", "it earns interest", "it leaves a record on your bank account"], "Cash helps you stay within what you have.")
H('10.C', 3, "A check is a written order for a bank to pay money from which place?", "your checking account", ["a store's cash register", "a credit card company's office", "the post office"], "A check pulls money from a checking account.")
H('10.C', 4, "Which is an advantage of paying electronically with a debit card or app?", "it is quick and leaves a record of the purchase", ["it never requires money in an account", "it can never be lost or misused", "it lets you spend without limit"], "Electronic payments are convenient and create records, but you still need the money.")
H('10.D', 3, "Why should a family keep records of bills and receipts?", "to track spending and prove payments", ["to make bills smaller", "to avoid paying taxes", "to get more money"], "Records help track money and show what was paid.")
H('10.D', 3, "Which is a good way to keep financial records organized?", "put bills and receipts in labeled folders or a spreadsheet", ["throw receipts away immediately", "keep them in a random pile", "never write anything down"], "Organized records are easy to find and use.")
H('10.D', 3, "How long should you keep a receipt for a big purchase you might need to return or use for a warranty?", "until the return or warranty period ends", ["one minute", "it never needs to be kept", "only until you get home and then toss it"], "Keep the receipt as proof while a return or warranty could apply.")
H('10.E', 3, "A family's expenses are more than its income. Which action could help balance the budget?", "cut back on spending", ["buy more things on credit", "ignore the bills", "spend more on wants"], "Lowering expenses or raising income helps balance a budget.")
H('10.E', 3, "A family's expenses are more than its income. Which action could help balance the budget?", "earn more income", ["spend more on wants", "pay bills late", "skip writing down expenses"], "More income can close the gap.")
H('10.E', 4, "Which choice would help a family with a budget shortage the MOST?", "spending less on wants while still paying for needs", ["spending less on needs like rent", "buying more things on credit", "ignoring the budget"], "Cut wants first; needs come first.")
H('10.D', 3, "Which record would show how much money a family spent on groceries last month?", "saved store receipts", ["a map of the neighborhood", "a school schedule", "a recipe book"], "Receipts show what was bought and what it cost.")
H('10.D', 4, "A family tracks income and spending in a spreadsheet. What is the main benefit?", "they can see where their money goes", ["they will never pay taxes", "their bills get smaller on their own", "they will earn more income by itself"], "Records help you see and plan your spending.")
H('10.E', 3, "A family's income is $2,000 a month and their expenses are $2,200. Which is a way to balance the budget?", "lower expenses by $200 or more", ["raise expenses by $200", "borrow $200 every month", "stop tracking the budget"], "Expenses must come down (or income go up) by at least the $200 gap.")
H('10.E', 3, "Which expense is easiest to cut back when money is short?", "eating out", ["rent", "electricity", "groceries"], "Wants like eating out are easier to cut than needs like rent and groceries.")
H('10.E', 4, "A family has $150 more in expenses than income. Which pair of actions could balance the budget?", "cut $100 from wants and earn $50 more", ["add $100 to wants and earn $50 more", "cut $50 from wants and add $100 in credit card debt", "do nothing for three months"], "$100 saved plus $50 earned closes the $150 gap.")
H('9.A', 3, "A bar graph shows the number of students in each grade. What does the height of each bar tell you?", "how many students are in that grade", ["the grade's name", "the teacher's name", "how tall the students are"], "The bar height shows the frequency (the count).")
H('9.A', 4, "Which display would best show the weights of 12 pet rabbits to the nearest quarter pound?", "a dot plot", ["a bar graph of rabbit names", "a map", "a pie chart of colors"], "A dot plot shows numerical measurements, including fractions.")
def budget_left():
    nm = who(); inc = R.randint(20, 45) * 100
    amts = [("rent", R.randint(60, 120) * 10)] + [(n_, R.randint(lo, hi) // 10 * 10) for n_, lo, hi in R.sample([("food", 250, 600), ("transportation", 100, 300), ("phone", 50, 150), ("savings", 100, 400), ("clothes", 80, 250)], 3)]
    tot = sum(a for _, a in amts)
    if tot >= inc: return False
    txt = ", ".join(f"{n_} ${cm(a)}" for n_, a in amts); left = inc - tot
    return mk('10.F', 4, f"{nm}'s family budget for a month: income ${cm(inc)}; expenses: {txt}. How much money is left after all the expenses?", f"${cm(left)}", [f"${cm(tot)}", f"${cm(inc + tot)}", f"${cm(left + amts[0][1])}", f"${cm(left - 50)}" if left > 50 else f"${cm(left + 100)}"], f"Add the expenses: {cm(tot)}. Then {cm(inc)} − {cm(tot)} = {cm(left)}.", "'$' + f'" + "{%d:,}'" % left)
def budget_short():
    nm = who(); a = R.randint(60, 120) * 10; b = R.randint(25, 60) * 10; c = R.randint(15, 60) * 10; tot = a + b + c; extra = R.randint(3, 15) * 10; inc = tot - extra
    return mk('10.F', 4, f"{nm}'s monthly income is ${cm(inc)}. Expenses are rent ${cm(a)}, food ${cm(b)}, and other costs ${cm(c)}. How much more are the expenses than the income? (This is how much must be cut to balance the budget.)", f"${cm(extra)}", [f"${cm(tot)}", f"${cm(inc)}", f"${cm(extra + 100)}", f"${cm(extra + 20)}"], f"Expenses: {cm(a)} + {cm(b)} + {cm(c)} = {cm(tot)}. {cm(tot)} − {cm(inc)} = {cm(extra)}.", "'$' + f'" + "{%d:,}'" % extra)
def budget_save():
    nm = who(); inc = R.randint(10, 30) * 100; pct = R.choice([10, 20, 25, 50]); sv = inc * pct // 100
    return mk('10.F', 4, f"{nm} wants to save {pct}% of a ${cm(inc)} monthly income. How much money will {nm} put into savings?", f"${cm(sv)}", [f"${cm(inc - sv)}", f"${cm(sv * 10)}", f"${cm(inc // pct)}", f"${cm(sv + 50)}"], f"{pct}% of {cm(inc)} = {cm(sv)}.", "'$' + f'" + "{%d:,}'" % sv) if False else False
rep(3, gn_calc); rep(5, budget_left); rep(3, budget_short)

n = B.save(os.path.join(os.path.dirname(__file__), '..', 'batches', 'g5_math.jsonl'))
print("wrote", n, "questions")

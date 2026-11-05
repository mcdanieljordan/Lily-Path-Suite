#!/usr/bin/env python3
"""Grade 4 Mathematics (TEKS 111.6.b) - original questions. Run: python3 gen/g4_math.py  -> batches/g4_math.jsonl"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from fractions import Fraction as F

B = Bank('111.6.b.', 404, no_neg=True, norm_dup=True)
R, mk, H, rep = B.R, B.mk, B.hand, B.rep
LT, GT, EQ = "less than (<)", "greater than (>)", "equal to (=)"
NM = ["Ava", "Ben", "Cara", "Dev", "Eli", "Fay", "Gus", "Hana", "Ivan", "Jo", "Kai", "Lena", "Max", "Nia", "Omar", "Pia", "Raj", "Sam", "Tia", "Zoe"]
PLACE = {10: 'ten', 100: 'hundred', 1000: 'thousand', 10000: 'ten thousand', 100000: 'hundred thousand'}
def who(): return R.choice(NM)
def dec(h, trim=False):
    s = f"{h / 100:.2f}"
    return s[:-1] if trim and s.endswith('0') else s
def fs(a, b): return f"{a}/{b}"
def dollars(c): return f"${c // 100}.{c % 100:02d}"
def chkd(expr): return "f'${(%s)//100}.{(%s)%%100:02d}'" % (expr, expr)

# ================================================================ strand 2 place value, decimals
def pv_times():
    d = R.randint(2, 9); a = R.randint(2, 8); b = R.randint(0, a - 1); k = a - b
    return mk('2.A', 2 if k == 1 else 3, f"The digit {d} in {cm(d * 10 ** a)} has a value that is how many times the value of the digit {d} in {cm(d * 10 ** b)}?",
              cm(10 ** k), [cm(10 ** j) for j in range(1, 7) if j != k], f"Each place is 10 times the place to its right. {k} {"place" if k == 1 else "places"} apart is {cm(10 ** k)} times.", CK(f"10**{k}"))

TXT = {"10 times as much": 10, "100 times as much": 100, "1/10 as much": F(1, 10), "1/100 as much": F(1, 100)}
def pv_frac():
    d = R.randint(2, 9); k = R.choice([1, 2])
    if R.random() < .5:
        a = R.randint(k, 5); big, small = d * 10 ** a, d * 10 ** (a - k); sb, ss = cm(big), cm(small)
    else:
        if k == 2: return False
        sb, ss = f"0.{d}", f"0.0{d}"
    if R.random() < .5:
        right = f"1/{10 ** k} as much"; q = f"The value of the digit {d} in {ss} is how much compared with the value of the digit {d} in {sb}?"
    else:
        right = f"{10 ** k} times as much"; q = f"The value of the digit {d} in {sb} is how much compared with the value of the digit {d} in {ss}?"
    return mk('2.A', 3, q, right, [t for t in TXT if t != right], "Moving one place to the left makes the value 10 times as much; one place to the right makes it 1/10 as much.")

def b_value():
    n = R.randint(7, 9); ds = R.sample(range(1, 10), n); pos = R.randint(0, n - 1); d = ds[pos]; s = ''.join(map(str, ds)); v = d * 10 ** (n - 1 - pos)
    names = ['ones', 'tens', 'hundreds', 'thousands', 'ten thousands', 'hundred thousands', 'millions', 'ten millions', 'hundred millions']
    return mk('2.B', 3, f"What is the value of the digit {d} in {cm(int(s))}?", cm(v), [cm(d * 10 ** (n - 1 - pos + j)) for j in (-1, 1, 2)] + [str(d)],
              f"The {d} is in the {names[n - 1 - pos]} place, so its value is {cm(v)}.", CK(f"{d}*10**{n - 1 - pos}"))

def b_expanded():
    n = R.randint(5, 9); ds = [R.randint(1, 9)] + [R.choice([0, 0, R.randint(1, 9)]) for _ in range(n - 1)]
    terms = [d * 10 ** (n - 1 - i) for i, d in enumerate(ds) if d]; num = int(''.join(map(str, ds)))
    if len(terms) < 3: return False
    f = lambda l: ' + '.join(cm(x) for x in l); wr = []
    for i in range(len(terms)):
        t2 = terms[:]; t2[i] *= 10; wr.append(f(t2))
        t3 = terms[:]; t3[i] //= 10 if t3[i] >= 10 else 1; wr.append(f(t3))
    return mk('2.B', 3, f"Which is the expanded notation for {cm(num)}?", f(terms), wr, "Write the value of each digit, then add.")

def b_dec_value():
    u, t, h = R.sample(range(1, 10), 3); pos = R.randint(0, 2); d = (u, t, h)[pos]; hv = (u * 100, t * 10, h)[pos]
    val = lambda x: f"{x / 100:.2f}".rstrip('0').rstrip('.')
    right = val(hv); wr = [val(x) for x in (d * 100, d * 10, d, d * 1000) if val(x) != right]
    place = ['ones', 'tenths', 'hundredths'][pos]
    return mk('2.B', 3, f"What is the value of the digit {d} in {u}.{t}{h}?", right, wr, f"The {d} is in the {place} place, so its value is {right}.")

def c_symbol():
    k = R.randint(0, 2)
    if k == 0:
        a = R.randint(100000, 999999999); s = list(str(a)); i = R.randint(1, len(s) - 1); s[i] = str((int(s[i]) + R.randint(1, 8)) % 10); b = int(''.join(s))
    elif k == 1:
        a = R.randint(10 ** 5, 10 ** 6 - 1); b = R.randint(10 ** 6, 5 * 10 ** 6)
        if R.random() < .5: a, b = b, a
    else:
        ds = R.sample(range(1, 10), 7); a = int(''.join(map(str, ds))); ds[4], ds[5] = ds[5], ds[4]; b = int(''.join(map(str, ds)))
    if a == b: return False
    right = LT if a < b else GT
    return mk('2.C', 3 if k == 0 else 2 if k == 1 else 3, f"Which symbol makes this statement true?  {cm(a)} ___ {cm(b)}", right, [LT, GT, EQ],
              f"Compare from the greatest place value. {cm(a)} is {'less' if a < b else 'greater'} than {cm(b)}.", need=2)

def c_order():
    base = R.randint(10, 900) * 10 ** R.randint(3, 6); ns = R.sample([base + R.randint(0, 99) * 10 ** R.randint(2, 5) for _ in range(10)], 3)
    if len(set(ns)) < 3: return False
    asc = sorted(ns); up = R.random() < .6; ans = asc if up else asc[::-1]
    f = lambda l: ', '.join(cm(x) for x in l)
    return mk('2.C', 3, f"Which list shows the numbers in order from {'least to greatest' if up else 'greatest to least'}?  {f(R.sample(ns, 3))}", f(ans),
              [f(ans[::-1]), f([ans[1], ans[0], ans[2]]), f([ans[0], ans[2], ans[1]])], "Compare the digits from the left, starting with the greatest place value.")

def d_round():
    u = R.choice([10, 100, 1000, 10000, 100000]); n = R.randint(u * 3 + 1, min(u * 400, 999999))
    if n % u == 0: return False
    right = (n + u // 2) // u * u; low = n // u * u
    return mk('2.D', 2 if u <= 100 else 3, f"What is {cm(n)} rounded to the nearest {PLACE[u]}?", cm(right), [cm(x) for x in (low, low + u, right + u, right - u, n if u == 10 else (n + u // 20) // (u // 10) * (u // 10), (n + u * 5) // (u * 10) * (u * 10))],
              f"Look at the digit to the right of the {PLACE[u]} place: {'5 or more rounds up' if right > low else 'less than 5 rounds down'}.", CK(f"({n}+{u // 2})//{u}*{u}"))

def e_grid():
    k = R.randint(3, 97); x = who()
    if R.random() < .5:
        return mk('2.E', 2, f"A hundreds grid has {k} of its 100 squares shaded. Which decimal names the shaded part?", dec(k), [dec(k * 10), dec(int(str(k)[::-1]) or 1), f"{k}.00", f"{k / 10:.1f}"], f"{k} out of 100 is {dec(k)}.")
    j = R.randint(1, 9)
    return mk('2.E', 2, f"A bar is split into 10 equal parts. {j} part{'s are' if j > 1 else ' is'} shaded. Which decimal names the shaded part?", dec(j * 10, True), [dec(j, False), f"{j}.0", dec((10 - j) * 10, True), f"1.{j}"], f"{j} out of 10 is {dec(j * 10, True)}.")

def e_money():
    d = R.randint(1, 9); p = R.randint(1, 9); x = who(); v = d * 10 + p
    return mk('2.E', 3, f"{x} has {d} dime{'s' if d > 1 else ''} and {p} {'pennies' if p > 1 else 'penny'}. What decimal shows the part of a dollar {x} has?", dec(v), [dec(p * 10 + d) if p != d else dec(v + 10), f"{d}.{p}", f"0.0{d}{p}", f"0.{d}"],
              f"{d} dimes is {d * 10} cents and {p} pennies is {p} cents: {v} cents = ${dec(v)}.")

def f_compare():
    a = R.randint(5, 399); b = a + R.choice([-30, -9, -1, 1, 5, 10, 40, 0]); tr = R.random() < .5
    if b <= 0 or a == b and R.random() < .6: return False
    right = LT if a < b else GT if a > b else EQ
    return mk('2.F', 3, f"Which symbol makes this statement true?  {dec(a, tr and a % 10 == 0)} ___ {dec(b, tr and b % 10 == 0)}", right, [LT, GT, EQ],
              "Line up the decimal points and compare place by place from the left.", need=2)

def f_order():
    base = R.randint(1, 8) * 100; hs = R.sample(range(base, base + 99), 3); asc = sorted(hs); up = R.random() < .6; ans = asc if up else asc[::-1]
    f = lambda l: ', '.join(dec(x) for x in l)
    return mk('2.F', 3, f"Which list shows the decimals in order from {'least to greatest' if up else 'greatest to least'}?  {f(R.sample(hs, 3))}", f(ans),
              [f(ans[::-1]), f([ans[1], ans[0], ans[2]]), f([ans[0], ans[2], ans[1]])], "Compare the digits from the left, one place at a time.")

def g_dec_frac():
    if R.random() < .5:
        k = R.randint(1, 9); right = fs(k, 10); d = dec(k * 10, True)
        return mk('2.G', 2, f"Which fraction is equal to {d}?", right, [fs(k, 100), fs(1, k) if k > 1 else fs(1, 9), fs(k * 10, 10), fs(k + 1, 10)], f"{d} is {k} tenths, which is {right}.")
    v = R.randint(11, 99)
    if v % 10 == 0: return False
    return mk('2.G', 3, f"Which fraction is equal to {dec(v)}?", fs(v, 100), [fs(v, 10), fs(v, 1000), fs(int(str(v)[::-1]), 100), fs(v + 1, 100)], f"{dec(v)} is {v} hundredths, which is {fs(v, 100)}.")

def g_frac_dec():
    if R.random() < .5:
        k = R.randint(1, 9)
        return mk('2.G', 2, f"Which decimal is equal to {fs(k, 10)}?", dec(k * 10, True), [dec(k), f"{k}.0", dec(k * 10 + 100, True), dec(k * 100)], f"{fs(k, 10)} is {k} tenths, which is {dec(k * 10, True)}.")
    v = R.randint(11, 99)
    if v % 10 == 0: return False
    return mk('2.G', 3, f"Which decimal is equal to {fs(v, 100)}?", dec(v), [dec(v * 10), dec(int(str(v)[::-1]) or 1), f"{v}.00", f"{v / 10:.1f}"], f"{fs(v, 100)} is {v} hundredths, which is {dec(v)}.")

def h_line():
    k = R.randint(1, 9)
    if R.random() < .5:
        return mk('2.H', 2, f"A number line from 0 to 1 is split into 10 equal parts. A point is on the {['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth'][k]} mark after 0. Which decimal names the point?", dec(k * 10, True),
                  [dec(k), f"{k}.0", dec((10 - k) * 10, True), f"1.{k}"], f"Each mark is 0.1, so {k} marks is {dec(k * 10, True)}.")
    a = R.randint(1, 8); tenth = f"0.{a}"
    return mk('2.H', 4, f"A number line from {tenth} to 0.{a + 1} is split into 10 equal parts. A point is on the {['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth'][k]} mark after {tenth}. Which decimal names the point?",
              f"0.{a}{k}", [f"0.{k}{a}", f"0.{a + 1}{k}" if a < 9 else f"0.{a}{k + 0}1", f"0.{a}", f"0.0{k}"], f"Each mark is 0.01, so the point is {k} hundredths past {tenth}: 0.{a}{k}.")

# ================================================================ strand 3 fractions
def f3A_sum():
    b = R.choice([3, 4, 5, 6, 8, 10, 12]); a = R.randint(2, b + 4)
    right = ' + '.join([fs(1, b)] * a)
    if a < 3 and R.random() < .5: return False
    return mk('3.A', 3, f"Which sum is equal to {fs(a, b)}?", right, [' + '.join([fs(1, b)] * (a + 1)), ' + '.join([fs(1, b)] * (a - 1)) if a > 2 else ' + '.join([fs(1, b)] * (a + 2)), ' + '.join([fs(1, b + 1)] * a), ' + '.join([fs(1, a)] * b) if a != b else ' + '.join([fs(1, b + 2)] * a)],
              f"{fs(a, b)} is {a} parts that are each {fs(1, b)}.")

def f3A_frac():
    b = R.choice([3, 4, 5, 6, 8]); a = R.randint(b + 1, b + 5)
    return mk('3.A', 3, f"Which fraction is equal to " + ' + '.join([fs(1, b)] * a) + "?", fs(a, b), [fs(b, a), fs(a, a + b), fs(1, a * b), fs(a - 1, b)] if a > 2 else [fs(b, a)], f"Adding {a} parts that are each {fs(1, b)} gives {fs(a, b)}.")

def f3B():
    b = R.choice([4, 5, 6, 8, 10, 12]); a = R.randint(3, b + 2); x = R.randint(1, a - 1); y = a - x
    right = f"{fs(x, b)} + {fs(y, b)}"
    wr = [f"{fs(x, b)} + {fs(y + 1, b)}", f"{fs(x, b)} + {fs(y, 2 * b)}", f"{fs(x + 1, b)} + {fs(y + 1, b)}", f"{fs(x, b)} + {fs(y - 1, b)}" if y > 1 else f"{fs(x + 2, b)} + {fs(y, b)}"]
    return mk('3.B', 3, f"Which shows {fs(a, b)} broken into a sum of fractions with the same denominator?", right, wr, f"{x} + {y} = {a}, so {fs(a, b)} = {right}.")

def f3C_eq():
    b = R.choice([2, 3, 4, 5, 6, 8]); a = R.randint(1, b - 1); k = R.choice([2, 3, 4, 5])
    if F(a, b).denominator != b: return False
    return mk('3.C', 3, f"Which fraction is equivalent to {fs(a, b)}?", fs(a * k, b * k), [fs(a + k, b + k), fs(a * k, b), fs(a, b * k), fs(a * k, b + k), fs(a + 1, b + 1)], f"Multiply the top and bottom by {k}: {fs(a, b)} = {fs(a * k, b * k)}.")

def f3C_yn():
    b = R.choice([2, 3, 4, 5, 6]); a = R.randint(1, b - 1); k = R.choice([2, 3, 4])
    if F(a, b).denominator != b: return False
    same = R.random() < .5; c, d = (a * k, b * k) if same else (a * k + 1, b * k)
    return mk('3.C', 3, f"Are {fs(a, b)} and {fs(c, d)} equivalent fractions?", "Yes" if same else "No", ["No" if same else "Yes"],
              f"{fs(a, b)} = {fs(a * k, b * k)}, so they are {'equivalent' if same else 'not equivalent'} to {fs(c, d)}." if same else f"{fs(a, b)} = {fs(a * k, b * k)}, which is not {fs(c, d)}.", need=1)

def f3D():
    for _ in range(30):
        b, d = R.sample([2, 3, 4, 5, 6, 8, 10, 12], 2); a = R.randint(1, b); c = R.randint(1, d)
        if a < b and c < d and F(a, b) != F(c, d): break
    else: return False
    x, y = F(a, b), F(c, d); right = LT if x < y else GT
    return mk('3.D', 3, f"Which symbol makes this statement true?  {fs(a, b)} ___ {fs(c, d)}", right, [LT, GT, EQ], f"Compare using a common denominator or benchmarks: {fs(a, b)} is {'less' if x < y else 'greater'} than {fs(c, d)}.", need=2)

def f3D_word():
    for _ in range(30):
        b, d = R.sample([2, 3, 4, 5, 6, 8, 10, 12], 2); a = R.randint(1, b - 1); c = R.randint(1, d - 1)
        if F(a, b) != F(c, d): break
    else: return False
    x, y = R.sample(NM, 2); big = x if F(a, b) > F(c, d) else y
    other = x if big == y else y
    return mk('3.D', 3, f"{x} walked {fs(a, b)} of a mile. {y} walked {fs(c, d)} of a mile. Which statement is true?", f"{big} walked farther.", [f"{other} walked farther.", "They walked the same distance."], f"{fs(a, b)} compared with {fs(c, d)}: {big} walked farther.", need=2)

def f3E_add():
    b = R.choice([3, 4, 5, 6, 8, 10, 12]); a = R.randint(1, b - 1); c = R.randint(1, b - 1); s = a + c
    wr = [fs(s, 2 * b), fs(abs(a - c) or a + 1, b), fs(s + 1, b), fs(a * c, b), fs(s, b + 1)]
    return mk('3.E', 2, f"What is {fs(a, b)} + {fs(c, b)}?", fs(s, b), wr, f"The denominators match, so add the numerators: {a} + {c} = {s}, and the denominator stays {b}.")

def f3E_sub():
    b = R.choice([4, 5, 6, 8, 10, 12]); a = R.randint(3, b + 2); c = R.randint(1, a - 1); s = a - c
    return mk('3.E', 2, f"What is {fs(a, b)} − {fs(c, b)}?", fs(s, b), [fs(a + c, b), fs(s, 2 * b), fs(s, b + 1), fs(s + 1, b)], f"Subtract the numerators: {a} − {c} = {s}. The denominator stays {b}.")

def f3E_word():
    b = R.choice([4, 5, 6, 8, 10]); a = R.randint(1, b - 2); c = R.randint(1, b - 1 - a); x, y = R.sample(NM, 2); it = R.choice(["pizza", "pan of brownies", "garden"])
    if R.random() < .5:
        return mk('3.E', 3, f"{x} ate {fs(a, b)} of a {it} and {y} ate {fs(c, b)} of the same {it}. How much of the {it} did they eat in all?", fs(a + c, b), [fs(a + c, 2 * b), fs(abs(a - c) or 1, b), fs(a + c + 1, b), fs(b - a - c or 1, b)], f"{fs(a, b)} + {fs(c, b)} = {fs(a + c, b)}.")
    return mk('3.E', 3, f"{x} ate {fs(a, b)} of a {it}. Then {y} ate {fs(c, b)} of the same {it}. How much of the {it} is left? (The whole {it} is {fs(b, b)}.)", fs(b - a - c, b), [fs(a + c, b), fs(b - a - c, 2 * b), fs(b - a, b), fs(b - c, b)] if True else [], f"{fs(b, b)} − {fs(a, b)} − {fs(c, b)} = {fs(b - a - c, b)}.")

BM = {1: "0", 2: "1/4", 3: "1/4", 4: "1/2", 5: "1/2", 6: "1/2", 7: "3/4", 8: "3/4", 9: "1"}
def f3F_near():
    k = R.randint(1, 9)
    return mk('3.F', 3, f"Which benchmark fraction (0, 1/4, 1/2, 3/4, 1) is closest to {fs(k, 10)}?", BM[k], [v for v in ("0", "1/4", "1/2", "3/4", "1") if v != BM[k]], f"{fs(k, 10)} = {k / 10:g}, and the closest benchmark is {BM[k]}.")

def f3F_est():
    a, c = R.randint(1, 4), R.randint(1, 5); s = F(BM[a].replace('0', '0/1') if BM[a] == '0' else BM[a]) + F(BM[c].replace('0', '0/1') if BM[c] == '0' else BM[c])
    if s > 1: return False
    out = "0" if s == 0 else str(s)
    return mk('3.F', 4, f"Estimate {fs(a, 10)} + {fs(c, 10)} by rounding each fraction to the closest benchmark (0, 1/4, 1/2, 3/4, or 1). What is the estimate?", out, [v for v in ("0", "1/4", "1/2", "3/4", "1") if v != out], f"{fs(a, 10)} is close to {BM[a]} and {fs(c, 10)} is close to {BM[c]}. {BM[a]} + {BM[c]} = {out}.")

def f3G():
    k = R.randint(1, 9)
    if R.random() < .5:
        return mk('3.G', 2, f"A number line from 0 to 1 is split into 10 equal parts. A point is on the mark that is {k} parts from 0. Which fraction names the point?", fs(k, 10), [fs(1, k) if k > 1 else fs(1, 9), fs(k, 100), fs(10 - k, 10), fs(k + 1, 10)], f"Each part is 1/10, so {k} parts is {fs(k, 10)}.")
    return mk('3.G', 2, f"A number line from 0 to 1 is split into 10 equal parts. A point is on the mark that is {k} parts from 0. Which decimal names the point?", dec(k * 10, True), [dec(k), f"{k}.0", dec((10 - k) * 10, True), f"1.{k}"], f"Each part is 0.1, so {k} parts is {dec(k * 10, True)}.")

# ================================================================ strand 4 operations
def o4A_add():
    a = R.randint(1200, 8999); b = R.randint(1100, 9999 - a + 1000); s = a + b
    return mk('4.A', 2, f"What is {cm(a)} + {cm(b)}?", cm(s), [cm(s + 10), cm(s - 10), cm(s + 100), cm(s - 100), cm(s + 1000)], f"Add place by place, regrouping when a place has 10 or more: {cm(a)} + {cm(b)} = {cm(s)}.", CK(f"{a}+{b}"))

def o4A_sub():
    a = R.randint(3000, 9999); b = R.randint(1100, a - 900); s = a - b
    return mk('4.A', 3, f"What is {cm(a)} − {cm(b)}?", cm(s), [cm(s + 10), cm(s - 10), cm(s + 100), cm(s - 100), cm(s + 1000)], f"Subtract place by place, regrouping when needed: {cm(a)} − {cm(b)} = {cm(s)}.", CK(f"{a}-{b}"))

def o4A_dec():
    a = R.randint(150, 2500); b = R.randint(150, 2500); add = R.random() < .5
    if not add and a < b: a, b = b, a
    if a == b: return False
    r = a + b if add else a - b
    sa, sb, sr = f"{a / 100:.2f}", f"{b / 100:.2f}", f"{r / 100:.2f}"
    return mk('4.A', 3, f"What is {sa} {'+' if add else '−'} {sb}?", sr, [f"{(r + 100) / 100:.2f}", f"{(r - 100) / 100:.2f}" if r > 100 else f"{(r + 200) / 100:.2f}", f"{(r + 10) / 100:.2f}", f"{(r * 10) / 100:.2f}"],
              f"Line up the decimal points and {'add' if add else 'subtract'}: {sa} {'+' if add else '−'} {sb} = {sr}.", "f'{(%d%s%d)/100:.2f}'" % (a, '+' if add else '-', b))

def o4B():
    n = R.randint(3, 98); k = R.choice([10, 100]); big = R.random() < .4
    if big: n *= 10
    right = n * k
    return mk('4.B', 2 if n < 100 else 3, f"What is {k} × {cm(n)}?" if R.random() < .5 else f"What is {cm(n)} × {k}?", cm(right), [cm(n * (100 if k == 10 else 10)), cm(n * 1000), cm(n + k), cm(n * k // 10 if n * k % 10 == 0 else n * k + 10)],
              f"Multiplying by {k} moves each digit {len(str(k)) - 1 + 1 - 1 + (1 if k == 10 else 2) - (1 if k == 10 else 1) + (0)} place{'s' if k == 100 else ''} to the left: {cm(right)}.".replace(f"{len(str(k)) - 1 + 1 - 1 + (1 if k == 10 else 2) - (1 if k == 10 else 1) + (0)}", "1" if k == 10 else "2"), CK(f"{n}*{k}"))

def o4C_area():
    a = R.randint(12, 49); b = R.randint(12, 49)
    if a // 10 == b // 10 and a % 10 == b % 10: return False
    ta, ua, tb, ub = a // 10 * 10, a % 10, b // 10 * 10, b % 10
    if ua == 0 or ub == 0: return False
    right = f"{ta} × {tb} + {ta} × {ub} + {ua} × {tb} + {ua} × {ub}"
    wr = [f"{ta} × {tb} + {ua} × {ub}", f"{ta} × {tb} + {ta} × {ub} + {ua} × {tb}", f"{ta} + {tb} + {ua} + {ub}", f"{ta} × {tb} + {ta} × {ub} + {ua} × {tb} + {ua} + {ub}"]
    return mk('4.C', 3, f"Which expression finds the total area of an area model for {a} × {b}, using the parts {ta} + {ua} and {tb} + {ub}?", right, wr, f"Multiply every part by every part: {right} = {a * b}.")

def o4C_sq():
    n = R.randint(4, 15); sq = n * n
    if R.random() < .5:
        nots = [x for x in range(20, 226) if int(x ** .5) ** 2 != x]
        return mk('4.C', 2, "Which number is a perfect square?", cm(sq), [cm(x) for x in R.sample(nots, 3)], f"{n} × {n} = {sq}, so {sq} is a perfect square.")
    return mk('4.C', 2, f"What is {n} × {n}?", cm(sq), [cm(sq + n), cm(sq - n), cm(2 * n), cm(sq + 10)], f"{n} × {n} = {sq}.", CK(f"{n}*{n}"))

def o4D_one():
    a = R.randint(1100, 9999); b = R.randint(3, 9); p = a * b
    return mk('4.D', 3, f"What is {cm(a)} × {b}?", cm(p), [cm(p + 100), cm(p - 100), cm(p + 1000), cm(p - 10), cm(a + b)], f"{cm(a)} × {b} = {cm(p)}.", CK(f"{a}*{b}"))

def o4D_two():
    a = R.randint(13, 98); b = R.randint(12, 89); p = a * b
    return mk('4.D', 3, f"What is {a} × {b}?", cm(p), [cm(p + 10), cm(p - 10), cm(p + 100), cm(p - 100), cm(a * (b // 10 * 10))], f"{a} × {b} = {cm(p)}.", CK(f"{a}*{b}"))

def o4D_word():
    a = R.randint(12, 48); b = R.randint(12, 36); x = who(); thing = R.choice([("boxes", "pencils"), ("rows", "chairs"), ("trays", "muffins")]); p = a * b
    return mk('4.D', 3, f"A school has {a} {thing[0]} with {b} {thing[1]} in each. How many {thing[1]} are there in all?", cm(p), [cm(p + 10), cm(p - 10), cm(p + 100), cm(a + b)], f"{a} × {b} = {cm(p)}.", CK(f"{a}*{b}"))

def o4E_eq():
    b = R.randint(3, 9); q = R.randint(12, 800); a = b * q
    return mk('4.E', 2, f"Which equation can be used to find {cm(a)} ÷ {b}?", f"{b} × □ = {cm(a)}", [f"□ × {cm(a)} = {b}", f"{cm(a)} × {b} = □", f"{b} + □ = {cm(a)}", f"{cm(a)} − □ = {b}"], f"Division asks what number times {b} makes {cm(a)}.")

def o4E_parts():
    b = R.randint(3, 9); q1 = R.randint(2, 9) * 10; q2 = R.randint(2, 9); a1, a2 = b * q1, b * q2; a = a1 + a2
    right = f"({a1} ÷ {b}) + ({a2} ÷ {b})"
    wr = [f"({a1} ÷ {b}) + ({a2 + 1} ÷ {b})", f"({a1} ÷ {b}) × ({a2} ÷ {b})", f"({a1 + b} ÷ {b}) + ({a2} ÷ {b})", f"({a1} − {b}) ÷ ({a2} × {b})"]
    return mk('4.E', 4, f"Which breaks {a} ÷ {b} into two easier divisions that give the right answer?", right, wr, f"{a} = {a1} + {a2}, and each part divides evenly by {b}: {q1} + {q2} = {q1 + q2}.")

def o4F_div():
    b = R.randint(3, 9); q = R.randint(13, 999) if R.random() < .6 else R.randint(1000, 1500); a = b * q
    if a > 9999: return False
    return mk('4.F', 3, f"What is {cm(a)} ÷ {b}?", cm(q), [cm(q + 10), cm(q - 10), cm(q + 100), cm(q - 1), cm(int(str(q).replace('0', '')) if '0' in str(q) and str(q).replace('0', '') else q + 2)], f"{cm(a)} ÷ {b} = {cm(q)}, because {b} × {cm(q)} = {cm(a)}.", CK(f"{a}//{b}"))

def o4F_word():
    b = R.randint(3, 9); q = R.randint(12, 250); a = b * q; x = who(); thing = R.choice([("apples", "bags"), ("stickers", "pages"), ("books", "shelves")])
    return mk('4.F', 3, f"{x} puts {cm(a)} {thing[0]} equally into {b} {thing[1]}. How many {thing[0]} go in each?", cm(q), [cm(q + 10), cm(q - 10), cm(q + 1), cm(a - b)], f"{cm(a)} ÷ {b} = {cm(q)}.", CK(f"{a}//{b}"))

def o4G_add():
    u = R.choice([10, 100]); a = R.randint(130, 960); b = R.randint(130, 960); ra, rb = (a + u // 2) // u * u, (b + u // 2) // u * u
    return mk('4.G', 2, f"Estimate {a} + {b} by rounding each number to the nearest {PLACE[u]}. What is the estimate?", cm(ra + rb), [cm(ra + rb + u), cm(ra + rb - u), cm(a + b + 100), cm(max(ra, rb))],
              f"{a} rounds to {ra} and {b} rounds to {rb}. {ra} + {rb} = {cm(ra + rb)}.", CK(f"{(a + u // 2) // u * u}+{(b + u // 2) // u * u}"))

def o4G_mul():
    a = R.randint(12, 89); b = R.randint(12, 89); ra, rb = (a + 5) // 10 * 10, (b + 5) // 10 * 10
    return mk('4.G', 3, f"Estimate {a} × {b} by rounding each number to the nearest ten. What is the estimate?", cm(ra * rb), [cm(ra * rb + 10 * ra), cm(ra * rb - 10 * rb), cm(ra + rb), cm(a * b + 100)], f"{a} rounds to {ra} and {b} rounds to {rb}. {ra} × {rb} = {cm(ra * rb)}.", CK(f"{ra}*{rb}"))

def o4G_div():
    b = R.choice([4, 5, 6, 8]); q = R.randint(2, 9) * 10; a = b * q + R.randint(1, b - 1) + R.choice([0, 0, b])
    base = b * q
    return mk('4.G', 3, f"Which compatible numbers help estimate {a} ÷ {b}?", f"{base} ÷ {b}", [f"{base + b * 10} ÷ {b}", f"{a} ÷ {b + 2}", f"{base - b * 10} ÷ {b}"] if base - b * 10 > 0 else [f"{base + b * 10} ÷ {b}", f"{a} ÷ {b + 2}", f"{base + b * 20} ÷ {b}"], f"{base} is close to {a} and divides evenly by {b}: {base} ÷ {b} = {q}.")

def o4H_div():
    b = R.randint(4, 9); a = R.randint(30, 200); x = who()
    if a % b == 0: return False
    k = R.randint(0, 2); thing = R.choice([("beads", "bracelet", "bracelets"), ("cookies", "box", "boxes"), ("students", "van", "vans")]); fl, rm = a // b, a % b
    if k == 0:
        return mk('4.H', 3, f"{x} has {a} {thing[0]}. Each {thing[1]} holds {b}. How many {thing[2]} can be filled completely?", fl, [fl + 1, rm, fl - 1, a - b], f"{a} ÷ {b} = {fl} R {rm}. Only {fl} are full.", CS(f"{a}//{b}"))
    if k == 1:
        return mk('4.H', 4, f"{x} has {a} {thing[0]}. Each {thing[1]} holds {b}. How many {thing[2]} are needed to hold all of them?", fl + 1, [fl, rm, fl + 2, a - b], f"{a} ÷ {b} = {fl} R {rm}. The extra {rm} need one more {thing[1]}, so {fl + 1}.", CS(f"-(-{a}//{b})"))
    return mk('4.H', 3, f"{x} has {a} {thing[0]} and puts {b} in each {thing[1]}. How many {thing[0]} are left over?", rm, [fl, b - rm, rm + 1, a - b], f"{a} ÷ {b} = {fl} R {rm}. {rm} are left over.", CS(f"{a}%{b}"))

def o4H_two():
    a = R.randint(3, 9); b = R.randint(12, 40); c = R.randint(2, 6); x = who()
    tot = a * b
    if tot % c == 0 or tot < 3 * c: return False
    return mk('4.H', 4, f"{x} buys {a} packs of {b} stickers. {x} shares the stickers equally among {c} friends. How many stickers does each friend get, with none broken up?", tot // c, [tot // c + 1, tot // c - 1, cm(a * b * c), tot % c],
              f"{a} × {b} = {tot}, and {tot} ÷ {c} = {tot // c} R {tot % c}. Each friend gets {tot // c}.", CS(f"{tot}//{c}"))

# ================================================================ strand 5 algebra and measurement
def s5A():
    k = R.randint(0, 2); x = who(); v = R.choice(['s', 't', 'n', 'm'])
    if k == 0:
        a = R.randint(20, 90); b = R.randint(2, 6); c = R.randint(3, 9)
        if len({b, c}) < 2: return False
        return mk('5.A', 4, f"{x} has {a} stickers and buys {b} packs with {c} stickers in each pack. Which equation can be used to find {v}, the total number of stickers {x} has now?", f"{v} = {a} + {b} × {c}",
                  [f"{v} = ({a} + {b}) × {c}", f"{v} = {a} × {b} + {c}", f"{v} = {a} + {b} + {c}", f"{v} = {a} + {b} − {c}"], f"The {b} packs hold {b} × {c} stickers, and then add the {a} stickers {x} already has.")
    if k == 1:
        a = R.randint(60, 150); b = R.randint(2, 6); c = R.randint(5, 12)
        if len({b, c}) < 2: return False
        return mk('5.A', 4, f"A store has {a} shirts. It sells {b} boxes with {c} shirts in each box. Which equation can be used to find {v}, the number of shirts left?", f"{v} = {a} − {b} × {c}",
                  [f"{v} = ({a} − {b}) × {c}", f"{v} = {a} − {b} − {c}", f"{v} = {a} × {b} − {c}", f"{v} = {a} − {b} + {c}"], f"The {b} boxes hold {b} × {c} shirts, and that amount is taken away from {a}.")
    b = R.randint(2, 6); c = R.randint(3, 9); p = R.randint(2, 8)
    if len({b, c, p}) < 3: return False
    return mk('5.A', 4, f"{x} buys {b} notebooks for ${c} each and one pen for ${p}. Which equation can be used to find {v}, the total cost in dollars?", f"{v} = {b} × {c} + {p}",
              [f"{v} = ({b} + {p}) × {c}", f"{v} = {b} + {c} + {p}", f"{v} = {b} × ({c} + {p})", f"{v} = {b} × {c} − {p}"], f"The notebooks cost {b} × {c}, and then add the ${p} pen.")

def s5B_out():
    t = R.randint(0, 2); x = R.randint(2, 9)
    if t == 0: k = R.randint(2, 9); rule, out = f"add {k}", x + k; wr = [x * k, x + k + 1, x - k if x > k else x + k + 2, k]
    elif t == 1: m = R.randint(2, 9); rule, out = f"multiply by {m}", x * m; wr = [x + m, x * m + 1, x * m - 1, m]
    else: m = R.randint(2, 5); c = R.randint(1, 5); rule, out = f"multiply by {m}, then add {c}", x * m + c; wr = [x * m, (x + c) * m, x + m + c, x * m - c]
    return mk('5.B', 2, f"An input-output table uses the rule “{rule}.” What is the output when the input is {x}?", out, wr, f"Apply the rule to {x}: {out}.")

def s5B_rule():
    kind = R.randint(0, 2); ins = sorted(R.sample(range(1, 9), 3))
    if kind == 0: k = R.randint(2, 9); f, name = (lambda v: v + k), f"add {k}"
    elif kind == 1: m = R.randint(2, 9); f, name = (lambda v: v * m), f"multiply by {m}"
    else: m = R.randint(2, 5); c = R.randint(1, 5); f, name = (lambda v: v * m + c), f"multiply by {m}, then add {c}"
    pool = [(f"add {k2}", (lambda k2: lambda v: v + k2)(k2)) for k2 in range(2, 10)] + [(f"multiply by {m2}", (lambda m2: lambda v: v * m2)(m2)) for m2 in range(2, 10)] \
        + [(f"multiply by {m2}, then add {c2}", (lambda m2, c2: lambda v: v * m2 + c2)(m2, c2)) for m2 in range(2, 6) for c2 in range(1, 6)]
    wr = [nm for nm, fn in pool if nm != name and not all(fn(v) == f(v) for v in ins)]
    pairs = ", ".join(f"({v}, {f(v)})" for v in ins)
    return mk('5.B', 3, f"An input-output table has these (input, output) pairs: {pairs}. Which rule matches the table?", name, R.sample(wr, 12)[:6], f"Test the rule on each pair: it works for {pairs}.")

def s5C_sq():
    s = R.randint(3, 20)
    if R.random() < .5:
        return mk('5.C', 2, f"The perimeter of a square is found with the formula P = 4s. What is the perimeter of a square with side length {s} cm?", f"{4 * s} cm", [f"{s * s} cm", f"{2 * s} cm", f"{s + 4} cm"], f"4 × {s} = {4 * s}.")
    l = R.randint(4, 15); w = R.randint(2, l - 1)
    return mk('5.C', 2, f"The area of a rectangle is found with the formula A = l × w. What is the area of a rectangle with length {l} cm and width {w} cm?", f"{l * w} square cm", [f"{2 * l + 2 * w} square cm", f"{l + w} square cm", f"{l * w + l} square cm"], f"{l} × {w} = {l * w} square cm.")

def s5D_peri():
    l = R.randint(6, 30); w = R.randint(3, l - 1); p = 2 * l + 2 * w
    return mk('5.D', 3, f"A rectangle has a perimeter of {p} feet and a length of {l} feet. What is its width?", f"{w} feet", [f"{p - l} feet", f"{p - 2 * l} feet", f"{p // 2 - l + 2} feet", f"{p // 2} feet"], f"Half the perimeter is {p // 2}. {p // 2} − {l} = {w}.", f"'{w} feet'" if False else f"f'{p // 2 - l} feet'")

def s5D_area():
    l = R.randint(4, 15); w = R.randint(3, 14); a = l * w
    if l == w: return False
    return mk('5.D', 3, f"A rectangle has an area of {a} square meters and a length of {l} meters. What is its width?", f"{w} meters", [f"{a - l} meters", f"{a + l} meters", f"{w + 2} meters", f"{w - 1} meters"], f"Width = area ÷ length = {a} ÷ {l} = {w}.", f"f'{a // l} meters'")

def s5D_word():
    l = R.randint(8, 30); w = R.randint(4, 20); x = who()
    if l == w: return False
    if R.random() < .5:
        return mk('5.D', 3, f"{x} puts a fence around a rectangular garden that is {l} feet long and {w} feet wide. How many feet of fence does {x} need?", f"{2 * l + 2 * w} feet", [f"{l * w} feet", f"{l + w} feet", f"{2 * l + w} feet", f"{2 * l + 2 * w + 4} feet"], f"Perimeter = 2 × {l} + 2 × {w} = {2 * l + 2 * w}.", f"f'{2 * l + 2 * w} feet'")
    return mk('5.D', 3, f"{x} covers a rectangular floor that is {l} feet long and {w} feet wide with tiles that are 1 square foot each. How many tiles are needed?", f"{l * w} tiles", [f"{2 * l + 2 * w} tiles", f"{l + w} tiles", f"{l * w + l} tiles", f"{l * w - w} tiles"], f"Area = {l} × {w} = {l * w}.", f"f'{l * w} tiles'")

# ================================================================ strand 6 geometry
def g6C():
    kind = R.choice(['acute', 'right', 'obtuse'])
    if kind == 'right': a = R.randrange(20, 70, 5); angs = [90, a, 90 - a]
    elif kind == 'acute':
        while True:
            a, b = R.randrange(35, 85, 5), R.randrange(35, 85, 5); c = 180 - a - b
            if 20 <= c < 90 and (a, b) != (60, 60): angs = [a, b, c]; break
    else: a = R.randrange(95, 140, 5); b = R.randrange(15, 180 - a - 10, 5); angs = [a, b, 180 - a - b]
    R.shuffle(angs)
    return mk('6.C', 3, f"A triangle has angles that measure {angs[0]}°, {angs[1]}°, and {angs[2]}°. What kind of triangle is it?", f"{kind} triangle", [f"{k} triangle" for k in ('acute', 'right', 'obtuse') if k != kind],
              {'right': "It has one right (90°) angle.", 'acute': "All three angles are less than 90°.", 'obtuse': "It has one angle greater than 90°."}[kind], need=2)

SYM = [("a square", 4), ("a rectangle that is not a square", 2), ("an equilateral triangle", 3), ("a regular pentagon", 5), ("a regular hexagon", 6), ("an isosceles triangle that is not equilateral", 1), ("a parallelogram with no right angles and unequal sides", 0), ("the capital letter H (block letters)", 2), ("the capital letter T (block letters)", 1)]
def g6B():
    nm_, n = R.choice(SYM)
    return mk('6.B', 2 if n in (1, 2, 4) else 3, f"How many lines of symmetry does {nm_} have?", n, [x for x in (0, 1, 2, 3, 4, 5, 6) if x != n], f"{nm_[0].upper() + nm_[1:]} has {n} line{'s' if n != 1 else ''} of symmetry.", CS(f"{n}"))

# ================================================================ strand 7 angles
DEG = [(F(1, 12), 30), (F(1, 8), 45), (F(1, 6), 60), (F(1, 4), 90), (F(1, 3), 120), (F(1, 2), 180)]
def a7A():
    fr, d = R.choice(DEG); f_txt = fs(fr.numerator, fr.denominator)
    if R.random() < .5:
        return mk('7.A', 3, f"An angle's rays cut out {f_txt} of a circle whose center is at the angle's vertex. What is the measure of the angle?", f"{d}°", [f"{x}°" for _, x in DEG if x != d] + [f"{d + 15}°"], f"A full circle is 360°. {f_txt} of 360° is {d}°.")
    return mk('7.A', 3, f"An angle measures {d}°. What fraction of a circle does it cut out?", f_txt, [fs(x.numerator, x.denominator) for x, _ in DEG if x != fr], f"{d}° out of 360° is {f_txt}.")

def a7B():
    n = R.choice([1, 5, 10, 15, 20, 25, 40, 50, 70, 75, 110, 135])
    return mk('7.B', 2, f"An angle cuts out {n}/360 of a circle whose center is at the vertex of the angle. What is the measure of the angle?", f"{n}°", [f"{n * 2}°", f"{360 - n}°", f"{n + 10}°", f"{n / 2:g}°"], f"One degree is 1/360 of a circle, so {n}/360 of a circle is {n}°.")

def a7C_class():
    d = R.choice([R.randrange(10, 90, 5), 90, R.randrange(95, 175, 5), 180]); right = 'acute' if d < 90 else 'right' if d == 90 else 'obtuse' if d < 180 else 'straight'
    return mk('7.C', 2, f"An angle measures {d}°. Which kind of angle is it?", right, [k for k in ('acute', 'right', 'obtuse', 'straight') if k != right], f"{'Less than 90° is acute.' if d < 90 else '90° is a right angle.' if d == 90 else 'Between 90° and 180° is obtuse.' if d < 180 else '180° is a straight angle.'}")

def a7C_read():
    d = R.randrange(15, 85, 5)
    return mk('7.C', 3, f"One ray of an angle lies on the 0° mark of a protractor scale. The other ray crosses that same scale at {d}°. What is the measure of the angle?", f"{d}°", [f"{180 - d}°", f"{d + 10}°", f"{d - 10}°", f"{d * 2}°"], f"Read the same scale that starts at 0°: the angle is {d}°.")

def a7E():
    a = R.randrange(10, 100, 5); b = R.randrange(10, 80, 5); t = a + b
    if R.random() < .5:
        return mk('7.E', 3, f"Angle ABC measures {a}° and angle CBD measures {b}°. They share ray BC and do not overlap. What is the measure of angle ABD?", f"{t}°", [f"{x}°" for x in (abs(a - b), t + 10, t - 10, 180 - t) if x >= 5], f"{a}° + {b}° = {t}°.", f"f'{t}°'")
    return mk('7.E', 4, f"Angle ABD measures {t}° and is made of angle ABC and angle CBD, which do not overlap. Angle ABC measures {a}°. What is the measure of angle CBD?", f"{b}°", [f"{x}°" for x in (t + a, b + 10, b - 10, a) if x >= 5], f"{t}° − {a}° = {b}°.", f"f'{b}°'")

# ================================================================ strand 8 measurement
CHAINS = [("length", ["inch", "foot", "yard", "mile"]), ("length", ["millimeter", "centimeter", "meter", "kilometer"]), ("weight", ["ounce", "pound", "ton"]), ("mass", ["gram", "kilogram"]),
          ("capacity", ["cup", "pint", "quart", "gallon"]), ("capacity", ["milliliter", "liter"]), ("time", ["second", "minute", "hour", "day"])]
def m8A():
    kind, units = R.choice(CHAINS); k = R.randint(2 if len(units) > 2 else 2, min(4, len(units))); pick = R.sample(units, k); big = R.random() < .5
    right = max(pick, key=units.index) if big else min(pick, key=units.index)
    if k < 3: return False
    return mk('8.A', 2, f"Which is the {'largest' if big else 'smallest'} unit of {kind}?", right, [u for u in pick if u != right], f"In order from smallest to largest: {', '.join(units)}.", need=k - 1)

CONV = [("feet", "inches", 12), ("yards", "feet", 3), ("pounds", "ounces", 16), ("gallons", "quarts", 4), ("quarts", "pints", 2), ("pints", "cups", 2), ("meters", "centimeters", 100),
        ("kilometers", "meters", 1000), ("kilograms", "grams", 1000), ("liters", "milliliters", 1000), ("hours", "minutes", 60), ("minutes", "seconds", 60), ("days", "hours", 24), ("centimeters", "millimeters", 10)]
SING = {"feet": "foot", "yards": "yard", "pounds": "pound", "gallons": "gallon", "quarts": "quart", "pints": "pint", "meters": "meter", "kilometers": "kilometer", "kilograms": "kilogram",
        "liters": "liter", "hours": "hour", "minutes": "minute", "days": "day", "centimeters": "centimeter"}
def m8B_down():
    big, small, f = R.choice(CONV); n = R.randint(2, 9 if f <= 24 else 12)
    return mk('8.B', 2 if f <= 12 else 3, f"{n} {big} = ___ {small}", f"{cm(n * f)}", [cm(n * f * 10), cm(n + f), cm(n * f // 10 if n * f % 10 == 0 else n * f + 10), cm(f)], f"There are {f} {small} in 1 {SING[big]}: {n} × {f} = {cm(n * f)}.", CK(f"{n}*{f}"))

def m8B_up():
    big, small, f = R.choice(CONV); n = R.randint(2, 9)
    return mk('8.B', 3, f"{cm(n * f)} {small} = ___ {big}", str(n), [str(n + 1), str(n - 1), cm(n * f * f) if n * f * f < 10 ** 6 else str(n * 10), cm(f)], f"There are {f} {small} in 1 {SING[big]}: {cm(n * f)} ÷ {f} = {n}.", CS(f"{n}"))

def m8C_end():
    h = R.randint(1, 9); m = R.choice([0, 10, 15, 20, 30, 40, 45, 50]); d = R.choice([25, 40, 55, 75, 90, 105, 130, 145, 170]); tm = h * 60 + m + d
    if tm // 60 > 12: return False
    x = who(); good = lambda t: 60 <= t < 13 * 60
    return mk('8.C', 3, f"{x}'s soccer practice starts at {clock(h * 60 + m)} and lasts {d} minutes. What time does practice end?", clock(tm), [clock(t) for t in (tm + 10, tm - 10, tm + 60, tm - 60, tm + 5) if good(t)],
              f"{clock(h * 60 + m)} plus {d} minutes ({d // 60} hour{'s' if d // 60 != 1 else ''} {d % 60} minutes) is {clock(tm)}.", f"'{clock(tm)}'")

def m8C_dur():
    h = R.randint(1, 8); m = R.choice([0, 10, 15, 20, 30, 40, 45, 50]); d = R.choice([25, 40, 55, 75, 90, 105, 130, 145]); tm = h * 60 + m + d
    return mk('8.C', 4, f"A movie starts at {clock(h * 60 + m)} and ends at {clock(tm)}. How many minutes long is the movie?", f"{d} minutes", [f"{d + 10} minutes", f"{d - 10} minutes", f"{d + 40} minutes", f"{d - 20} minutes"], f"From {clock(h * 60 + m)} to {clock(tm)} is {d} minutes.", f"'{d} minutes'")

def m8C_money():
    n = R.randint(2, 6); p = R.choice([125, 150, 225, 250, 325, 375, 450, 275]); bill = R.choice([2000, 2000, 1000]); x = who()
    if n * p >= bill: return False
    ch = bill - n * p
    return mk('8.C', 4, f"{x} buys {n} notebooks that cost {dollars(p)} each and pays with a {dollars(bill).replace('.00', '')} bill. How much change should {x} get?", dollars(ch),
              [dollars(ch + 100), dollars(ch - 50 if ch > 50 else ch + 150), dollars(n * p), dollars(bill - p)], f"{n} × {dollars(p)} = {dollars(n * p)}. {dollars(bill)} − {dollars(n * p)} = {dollars(ch)}.", chkd(f"{bill}-{n}*{p}"))

def m8C_liq():
    L = R.randint(2, 5); out = R.choice([150, 250, 350, 450, 650, 750, 850]); left = L * 1000 - out; x = who()
    return mk('8.C', 4, f"A pitcher holds {L} liters of juice. {x} pours out {out} milliliters. How many milliliters of juice are left?", f"{cm(left)} mL", [f"{cm(left + 100)} mL", f"{cm(L * 1000 + out)} mL", f"{cm(L * 100 - out) if L * 100 > out else cm(left - 500)} mL", f"{cm(L - out) if L > out else cm(left + 500)} mL"],
              f"{L} L = {cm(L * 1000)} mL. {cm(L * 1000)} − {out} = {cm(left)}.", f"f'{L * 1000 - out:,} mL'")

def m8C_mass():
    kg = R.randint(2, 6); used = R.choice([200, 300, 450, 600, 750, 1200, 1500]); left = kg * 1000 - used; x = who()
    return mk('8.C', 4, f"A bag of rice has a mass of {kg} kilograms. {x} uses {cm(used)} grams. How many grams of rice are left?", f"{cm(left)} g", [f"{cm(left + 100)} g", f"{cm(kg * 1000 + used)} g", f"{cm(kg - used) if kg > used else cm(left + 500)} g", f"{cm(left - 100)} g"],
              f"{kg} kg = {cm(kg * 1000)} g. {cm(kg * 1000)} − {cm(used)} = {cm(left)}.", f"f'{kg * 1000 - used:,} g'")

# ================================================================ strand 9 data
SLV = ["Stem | Leaves"]
def d9A_freq():
    vals = [R.choice([10, 12, 14, 15, 18]) for _ in range(R.randint(10, 14))]; t = R.choice(sorted(set(vals))); c = vals.count(t)
    return mk('9.A', 2, f"These scores were collected: {', '.join(map(str, vals))}. If the data are put in a frequency table, what is the frequency of {t}?", c, [c + 1, c - 1 if c > 1 else c + 2, c + 2, len(vals)], f"Count how many times {t} appears: {c}.", CS(f"{c}"))

def d9A_stem():
    st = R.randint(2, 8); lv = sorted(R.sample(range(0, 10), R.randint(3, 5))); vals = [st * 10 + l for l in lv]
    return mk('9.A', 2, f"In a stem-and-leaf plot, one row is  {st} | {' '.join(map(str, lv))}.  Which data values does this row show?", ', '.join(map(str, vals)),
              [', '.join(str(l) for l in lv), ', '.join(str(st + l) for l in lv), ', '.join(str(l * 10 + st) for l in lv)], f"The stem {st} is the tens digit and each leaf is a ones digit: {', '.join(map(str, vals))}.")

def d9A_stem2():
    st = R.randint(2, 8); lv = sorted(R.sample(range(0, 10), R.randint(3, 4))); vals = [st * 10 + l for l in lv]
    row = f"{st} | {' '.join(map(str, lv))}"
    wr = [f"{st} | {' '.join(str(l) for l in vals)}", f"{lv[0]} | {st} {' '.join(map(str, lv[1:]))}", f"{st} | {' '.join(map(str, lv[::-1]))} {R.randint(0, 9)}"]
    return mk('9.A', 3, f"Which stem-and-leaf row shows the data values {', '.join(map(str, vals))}?", row, wr, f"The stem {st} stands for the tens digit and the leaves are the ones digits.")

def d9B_stem():
    rows = {s: sorted(R.sample(range(0, 10), R.randint(2, 4))) for s in (1, 2, 3, 4)}; vals = [s * 10 + l for s, ls in rows.items() for l in ls]; t = R.choice([20, 25, 30])
    n = sum(1 for v in vals if v > t); x = '  '.join(f"{s} | {' '.join(map(str, ls))}" for s, ls in rows.items())
    return mk('9.B', 4, f"A stem-and-leaf plot shows the number of books students read:  {x}.  How many students read more than {t} books?", n, [n + 1, n - 1 if n > 1 else n + 3, len(vals), n + 2], f"Count the values greater than {t}: {n}.", CS(f"{n}"))

def d9B_dot():
    vals = [F(1, 4), F(1, 2), F(3, 4), F(1)]; cnt = [R.randint(1, 5) for _ in vals]; thr = R.choice([1, 2])
    fn = lambda v: "1" if v == 1 else fs(v.numerator, v.denominator)
    data = ', '.join(f"{c} dot{'s' if c > 1 else ''} at {fn(v)}" for v, c in zip(vals, cnt)); n = sum(cnt[thr + 1:]) if thr else sum(cnt[2:])
    t = vals[thr]; n = sum(c for v, c in zip(vals, cnt) if v > t)
    return mk('9.B', 4, f"A dot plot shows the lengths of pencils in inches. Each dot is one pencil: {data}. How many pencils are longer than {fn(t)} inch?", n, [n + 1, n - 1 if n > 1 else n + 3, sum(cnt), cnt[0] + n], f"Add the dots to the right of {fn(t)}: {n}.", CS(f"{n}"))

def d9B_freq():
    cats = R.choice([["red", "blue", "green", "yellow"], ["soccer", "swimming", "tennis", "track"], ["apples", "pears", "grapes", "plums"]]); vs = [R.randint(4, 19) for _ in cats]; i, j = R.sample(range(4), 2)
    data = ', '.join(f"{c} {v}" for c, v in zip(cats, vs))
    if R.random() < .5:
        return mk('9.B', 3, f"A frequency table shows: {data}. How many are in {cats[i]} and {cats[j]} together?", vs[i] + vs[j], [abs(vs[i] - vs[j]), vs[i] + vs[j] + 1, vs[i] + vs[j] - 1, sum(vs)], f"{vs[i]} + {vs[j]} = {vs[i] + vs[j]}.", CS(f"{vs[i]}+{vs[j]}"))
    t = sum(vs)
    return mk('9.B', 3, f"A frequency table shows: {data}. How many are there in all four categories?", t, [t + 10, t - 10, t + 1, t - vs[i]], f"{' + '.join(map(str, vs))} = {t}.", CS("+".join(map(str, vs))))

# ================================================================ run the generators
rep(3, pv_times); rep(3, pv_frac)
rep(3, b_value); rep(2, b_expanded); rep(2, b_dec_value)
rep(3, c_symbol); rep(2, c_order)
rep(5, d_round)
rep(3, e_grid); rep(2, e_money)
rep(3, f_compare); rep(2, f_order)
rep(2, g_dec_frac); rep(2, g_frac_dec)
rep(5, h_line)
rep(3, f3A_sum); rep(2, f3A_frac); rep(4, f3B); rep(3, f3C_eq); rep(2, f3C_yn); rep(4, f3D); rep(2, f3D_word)
rep(3, f3E_add); rep(3, f3E_sub); rep(3, f3E_word); rep(3, f3F_near); rep(2, f3F_est); rep(5, f3G)
rep(3, o4A_add); rep(3, o4A_sub); rep(3, o4A_dec); rep(4, o4B)
rep(3, o4C_area); rep(3, o4C_sq); rep(3, o4D_one); rep(3, o4D_two); rep(2, o4D_word)
rep(2, o4E_eq); rep(2, o4E_parts); rep(3, o4F_div); rep(2, o4F_word)
rep(2, o4G_add); rep(2, o4G_mul); rep(2, o4G_div); rep(4, o4H_div); rep(2, o4H_two)
rep(6, s5A); rep(2, s5B_out); rep(3, s5B_rule); rep(2, s5C_sq); rep(2, s5D_peri); rep(2, s5D_area); rep(2, s5D_word)
rep(4, g6C); rep(4, g6B)
rep(5, a7A); rep(4, a7B); rep(3, a7C_class); rep(2, a7C_read); rep(5, a7E)
rep(5, m8A); rep(3, m8B_down); rep(3, m8B_up); rep(2, m8C_end); rep(2, m8C_dur); rep(2, m8C_money); rep(2, m8C_liq); rep(2, m8C_mass)
rep(2, d9A_freq); rep(2, d9A_stem); rep(2, d9A_stem2); rep(2, d9B_stem); rep(2, d9B_dot); rep(3, d9B_freq)

# ================================================================ hand-written items (concepts that need wording)
H('3.F', 3, "Maya says 3/8 + 2/8 = 5/16. Which explains her mistake?", "When the denominators are the same, the denominator stays the same: the answer is 5/8.", ["She should have subtracted.", "She should have multiplied the numerators.", "She should have added the denominators."], "Add only the numerators when the denominators match.")
H('3.F', 3, "Eli adds 1/2 + 3/4. About how large is the sum?", "greater than 1", ["less than 1/2", "exactly 1/2", "less than 1"], "1/2 + 3/4 is more than 1/2 + 1/2 = 1, so the sum is greater than 1.")
H('3.C', 2, "Which statement about equivalent fractions is true?", "They name the same amount of the same whole.", ["They always have the same denominator.", "They always have the same numerator.", "They name different amounts."], "Equivalent fractions name the same point on the number line.")
H('3.D', 3, "Which comparison is true?", "1/2 > 3/8", ["1/2 < 3/8", "1/2 = 3/8", "3/8 > 5/8"], "1/2 = 4/8, and 4/8 is greater than 3/8.")
H('3.D', 3, "Which fraction is the greatest?", "3/4", ["1/2", "3/8", "1/4"], "3/4 is greater than 1/2, and 1/2 is greater than 3/8 and 1/4.")
H('3.D', 3, "A friend says 1/8 is greater than 1/4 because 8 is greater than 4. What is wrong?", "More equal parts means smaller parts, so 1/8 is less than 1/4.", ["Nothing is wrong.", "1/8 and 1/4 are equal.", "8 is not greater than 4."], "A bigger denominator (with the same numerator) means smaller pieces.")
H('3.E', 3, "Which equation is true?", "5/8 + 2/8 = 7/8", ["5/8 + 2/8 = 7/16", "5/8 + 2/8 = 3/8", "5/8 + 2/8 = 10/8"], "Add the numerators and keep the denominator: 5 + 2 = 7.")
H('4.E', 3, "A 3-row array has 24 counters in all. Which equation matches finding the number of counters in each row?", "24 ÷ 3 = □", ["24 × 3 = □", "24 + 3 = □", "3 − 24 = □"], "Splitting 24 into 3 equal rows is 24 ÷ 3.")
H('4.F', 3, "Maya divides 612 by 3 and gets 24. Which tells whether the answer is reasonable?", "No, because 3 × 24 = 72, which is not 612", ["Yes, because 24 is less than 612", "Yes, because 6 ÷ 3 = 2", "No, because 612 is odd"], "Check with multiplication: 3 × 24 = 72, not 612. The correct answer is 204.")
H('4.H', 3, "A remainder of 3 when dividing by 8 means:", "3 items are left over after making equal groups of 8", ["3 groups of 8 were made", "the answer is 3 more than 8", "the groups are not equal"], "A remainder is what is left after making as many equal groups as possible.")
H('5.C', 2, "Which formula can be used to find the perimeter of a rectangle with length l and width w?", "P = 2l + 2w", ["P = l × w", "P = l + w", "P = 4l"], "A rectangle has 2 lengths and 2 widths: 2l + 2w.")
H('5.C', 2, "Which formula can be used to find the area of a rectangle with length l and width w?", "A = l × w", ["A = l + w", "A = 2l + 2w", "A = 4s"], "Area counts the unit squares: length × width.")
H('5.C', 2, "Which formula can be used to find the perimeter of a square with side length s?", "P = 4s", ["P = s × s", "P = 2s", "P = s + 4"], "A square has 4 equal sides.")
H('5.C', 3, "Which two measurements have the same units?", "perimeter in feet and a side length in feet", ["area in square feet and perimeter in feet", "area in square feet and a side in feet", "area in feet and perimeter in square feet"], "Perimeter is a length, so it is measured in feet, like a side. Area uses square units.")
H('6.A', 2, "Which term names a straight path that goes on forever in both directions?", "line", ["ray", "line segment", "point"], "A line extends forever in both directions.")
H('6.A', 2, "Which term names part of a line with two endpoints?", "line segment", ["line", "ray", "angle"], "A line segment has 2 endpoints.")
H('6.A', 2, "Which term names part of a line that has one endpoint and goes on forever in one direction?", "ray", ["line segment", "line", "point"], "A ray has 1 endpoint.")
H('6.A', 2, "Two lines that never meet and stay the same distance apart are:", "parallel", ["perpendicular", "intersecting at a right angle", "rays"], "Parallel lines never cross.")
H('6.A', 2, "Two lines that cross to make a right angle are:", "perpendicular", ["parallel", "rays", "line segments"], "Perpendicular lines meet at 90°.")
H('6.A', 2, "What is formed when two rays share the same endpoint?", "an angle", ["a line segment", "a pair of parallel lines", "a point"], "An angle is made by two rays with a common endpoint (the vertex).")
H('6.A', 3, "The two rails of a straight train track are an example of:", "parallel lines", ["perpendicular lines", "a point", "a ray"], "The rails never meet and stay the same distance apart.")
H('6.A', 3, "The corner of a sheet of paper is an example of:", "a right angle", ["a ray", "parallel lines", "a point"], "The corner of a sheet of paper makes a 90° angle.")
H('6.D', 3, "Which quadrilateral always has 4 right angles?", "rectangle", ["rhombus", "trapezoid", "parallelogram"], "A rectangle has 4 right angles. A rhombus, trapezoid, or parallelogram does not always have any.")
H('6.D', 3, "Which figure has no parallel sides?", "triangle", ["square", "rectangle", "parallelogram"], "A triangle's 3 sides all meet each other, so none are parallel.")
H('6.D', 3, "Which quadrilateral has exactly one pair of parallel sides?", "trapezoid", ["rectangle", "square", "parallelogram"], "A trapezoid has just one pair of parallel sides.")
H('6.D', 3, "A triangle has one right angle. Which pair of its sides are perpendicular?", "the two sides that form the right angle", ["the two longest sides", "any two sides", "none of its sides"], "Perpendicular sides meet at a right angle.")
H('6.D', 4, "A shape has 4 equal sides and 2 pairs of parallel sides, but no right angles. Which shape is it?", "rhombus", ["rectangle", "square", "trapezoid"], "A rhombus has 4 equal sides but no right angles.")
H('7.D', 3, "When you use a protractor to draw a 60° angle, where do you place the center point of the protractor?", "on the vertex of the angle", ["on the end of the ray", "on the 60° mark", "anywhere on the paper"], "The center point of the protractor goes on the vertex.")
H('7.D', 3, "To draw an angle with a protractor, you line up one ray with the:", "0° mark on the baseline", ["60° mark", "180° mark only", "edge of the paper"], "One ray lies on the 0° line, and then you mark the needed degree.")
H('7.D', 3, "Which angle should be drawn to make a right angle?", "90°", ["45°", "120°", "180°"], "A right angle measures 90°.")
H('7.D', 3, "A 130° angle will look:", "wider than a right angle", ["narrower than a right angle", "exactly like a right angle", "like a straight line"], "130° is greater than 90°, so it is obtuse.")
H('7.C', 3, "A protractor shows an angle's ray at the 35° mark on the scale that starts at 0° on the ray's side. Which kind of angle is it?", "acute", ["obtuse", "right", "straight"], "35° is less than 90°, so it is acute.", need=3)
H('9.A', 2, "A dot plot has one dot for each student. If there are 3 dots above the number 5, what does this show?", "3 students had a value of 5", ["5 students had a value of 3", "3 students had values that add to 5", "5 is the total number of students"], "Each dot is one data value, and the dots above 5 show how many times 5 occurs.")
H('9.B', 3, "A frequency table shows 6 students chose soccer and 9 students chose swimming. How many more students chose swimming?", "3", ["15", "6", "54"], "9 − 6 = 3.")

n = B.save(os.path.join(os.path.dirname(__file__), '..', 'batches', 'g4_math.jsonl'))
print("wrote", n, "questions")

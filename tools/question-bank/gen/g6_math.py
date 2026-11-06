#!/usr/bin/env python3
"""Grade 6 Mathematics (TEKS 111.26.b) - original questions. Run: python3 gen/g6_math.py  -> batches/g6_math.jsonl"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from mid import *

B, mk = setup('111.26.b.', 606, 'g6_math.jsonl')
R, H, rep = B.R, B.hand, B.rep
def who(): return R.choice(NM)
LT, GT, EQ = "less than (<)", "greater than (>)", "equal to (=)"
def MSC(expr):                      # chk text: non-negative Fraction expression -> mixed number text
    return ("(lambda x: str(x.numerator//x.denominator) if x.numerator%x.denominator==0 else ((str(x.numerator//x.denominator)+' ' if x.numerator//x.denominator else '')+str(x.numerator%x.denominator)+'/'+str(x.denominator)))(" + expr + ")")
def nz(n): return sg(n)             # a number for display
def par(n): return f"({sg(n)})" if n < 0 else str(n)     # negative numbers get parentheses inside expressions
def rnd_frac(lo=1, hi=9, dmax=9, proper=True):
    while True:
        d = R.randint(2, dmax); n = R.randint(lo, min(hi, d - 1 if proper else hi))
        if coprime(n, d): return F(n, d)

# ================================================================ 2.A classify numbers
TYPE_TXT = {'w': "a whole number, an integer, and a rational number", 'i': "an integer and a rational number, but not a whole number",
            'q': "a rational number, but not an integer or a whole number"}
X_TXT = ["a whole number, but not an integer", "an integer, but not a rational number", "not a rational number"]
NUMS = [("0", 'w'), ("7", 'w'), ("12", 'w'), ("25", 'w'), ("4", 'w'), ("-4", 'i'), ("-9", 'i'), ("-15", 'i'), ("-1", 'i'), ("-23", 'i'),
        ("3/4", 'q'), ("-2.5", 'q'), ("0.6", 'q'), ("-1/3", 'q'), ("5/2", 'q'), ("1.75", 'q'), ("-6.2", 'q'), ("7/8", 'q'), ("-0.4", 'q'), ("2 1/2", 'q')]
def cls_num():
    s, t = R.choice(NUMS); right = TYPE_TXT[t]
    wrong = [v for k, v in TYPE_TXT.items() if k != t] + X_TXT
    return mk('2.A', 3, f"Which statement correctly describes the number {sg(s)}?", right, wrong, f"{sg(s)} is {right}.")
rep(6, cls_num)
H('2.A', 2, "Which statement is true?", "Every whole number is an integer.", ["Every integer is a whole number.", "Every rational number is an integer.", "No integer is a rational number."], "Whole numbers (0, 1, 2, ...) are all integers, but integers also include negative numbers.")
H('2.A', 3, "Which number belongs to the set of integers but NOT to the set of whole numbers?", "−8", ["0", "5", "3/4"], "−8 is an integer. It is less than 0, so it is not a whole number.")
H('2.A', 3, "Which number is rational but NOT an integer?", "2/3", ["−5", "0", "14"], "2/3 can be written as a fraction but is between 0 and 1, so it is not an integer.")
H('2.A', 3, "In a Venn diagram of number sets, where is the circle for whole numbers drawn?", "inside the circle for integers, which is inside the circle for rational numbers", ["outside the circle for integers", "inside the circle for fractions only", "overlapping the integers circle but not inside it"], "Every whole number is an integer, and every integer is a rational number, so the circles are nested.")
H('2.A', 4, "A Venn diagram shows whole numbers inside integers inside rational numbers. Where would 0.75 be placed?", "in the rational numbers circle but outside the integers circle", ["inside the whole numbers circle", "inside the integers circle but outside the whole numbers circle", "outside all three circles"], "0.75 = 3/4 is rational, but it is not an integer.")
H('2.A', 3, "Which number is a whole number?", "0", ["−1", "1/2", "−0.5"], "Whole numbers are 0, 1, 2, 3, and so on. Zero is a whole number.")
H('2.A', 3, "Which set of numbers contains only integers?", "−3, 0, 8", ["−3, 0.5, 8", "1/2, 0, 8", "−3, 0, 8.4"], "Integers have no fraction or decimal part.")
H('2.A', 4, "A student says, \"−6 is not a rational number because it is negative.\" What is the best reply?", "Rational numbers can be negative. −6 = −6/1, so it is rational.", ["That is correct, because rational numbers must be positive.", "That is correct, because rational numbers cannot be whole numbers.", "That is incorrect, because −6 is a whole number."], "A rational number is any number that can be written as a fraction of two integers, and −6 = −6/1.")

# ================================================================ 2.B opposite and absolute value
def opp_int():
    n = R.randint(2, 40) * R.choice([-1, 1])
    return mk('2.B', 2, f"What is the opposite of {sg(n)}?", sg(-n), [sg(n), "0", sg(F(1, abs(n)) if False else n + R.choice([1, -1]))], f"The opposite of {sg(n)} is {sg(-n)}; they are the same distance from 0 on opposite sides.", sgc(f"-({n})"))
def opp_dec():
    n = R.randint(11, 99) / 10 * R.choice([-1, 1]); n = round(n, 1)
    t = sg(f"{n:.1f}")
    return mk('2.B', 3, f"What is the opposite of {t}?", sg(f"{-n:.1f}"), [t, "0", sg(f"{n + 1:.1f}")], f"The opposite of {t} is {sg(f'{-n:.1f}')}.", sgc(f"'{-n:.1f}'")) if False else mk('2.B', 3, f"What is the opposite of {t}?", sg(f"{-n:.1f}"), [t, "0", sg(f"{n + 1:.1f}")], f"The opposite of {t} is {sg(f'{-n:.1f}')}.")
def abs_val():
    n = R.randint(2, 60) * R.choice([-1, 1]); a = abs(n)
    return mk('2.B', 2, f"What is |{sg(n)}|?", str(a), [sg(-a), "0", sg(n) if n > 0 else str(a + 1)], f"Absolute value is the distance from 0. |{sg(n)}| = {a}.", f"str(abs({n}))")
def abs_frac():
    f = rnd_frac(1, 7, 9) * R.choice([-1, 1])
    return mk('2.B', 3, f"What is |{ms(f)}|?", ms(abs(f)), [ms(-abs(f)), ms(abs(f) + 1), "0"], f"The distance from 0 to {ms(f)} is {ms(abs(f))}.")
def abs_max():
    vals = R.sample(range(2, 15), 4); a, b, c, d = vals
    exprs = [(f"|{sg(-a)}|", a), (sg(-b), -b), (f"{sg(-c)}", -c) if False else (f"−|{c}|", -c), (f"|{d}|", d)]
    best = max(v for _, v in exprs)
    if sum(1 for _, v in exprs if v == best) != 1: return False
    right = [t for t, v in exprs if v == best][0]
    return mk('2.B', 4, "Which expression has the greatest value?", right, [t for t, v in exprs if v != best], "Values: " + ", ".join(f"{t} = {sg(v)}" for t, v in exprs) + ".")
def abs_same():
    n = R.randint(2, 30); s = R.choice([-1, 1])
    return mk('2.B', 3, f"Which number, other than {sg(s * n)}, has an absolute value of {n}?", sg(-s * n), [sg(2 * n), sg(-2 * n), sg(F(1, n)) if False else str(n * n)], f"Both {n} and {sg(-n)} are {n} units from 0.")
rep(4, opp_int); rep(3, opp_dec); rep(4, abs_val); rep(3, abs_frac); rep(3, abs_max); rep(3, abs_same)
H('2.B', 3, "Which statement describes |−12|?", "the distance between −12 and 0 on a number line", ["the opposite of 12", "the number 12 less than 0 on the number line", "the product of −12 and 1"], "Absolute value is a number's distance from 0.")
H('2.B', 3, "A diver is at −35 feet (35 feet below sea level). What does |−35| tell you?", "the diver is 35 feet from sea level", ["the diver is 35 feet above sea level", "the diver is 0 feet from sea level", "the diver is 70 feet from sea level"], "The absolute value is the distance from sea level, 35 feet.")
H('2.B', 2, "What number is its own opposite?", "0", ["1", "−1", "10"], "0 is 0 units from 0, so its opposite is also 0.")
H('2.B', 4, "Which statement is true about the opposite of a negative number?", "It is positive.", ["It is negative.", "It is zero.", "It has the same sign as the original number."], "The opposite of a negative number is the positive number the same distance from 0.")

# ================================================================ 2.C compare and order on a number line
def rq(kind=None):
    k = kind or R.choice(['int', 'dec', 'frac'])
    if k == 'int': return F(R.randint(-12, 12))
    if k == 'dec': return F(R.randint(-60, 60), 10)
    d = R.choice([2, 3, 4, 5, 8]); return F(R.randint(-3 * d, 3 * d), d)
def rtxt(x, k):
    if k == 'int': return sg(int(x))
    if k == 'dec': return dec(x, 1)
    if x.denominator == 1: return sg(int(x))
    w, r = divmod(abs(x).numerator, abs(x).denominator)
    return (MINUS if x < 0 else "") + (f"{w} {r}/{x.denominator}" if w else f"{r}/{x.denominator}")
def cmp_rat():
    k = R.choice(['int', 'dec', 'frac']); a, b = rq(k), rq(k)
    if a == b: return False
    right = GT if a > b else LT
    return mk('2.C', 3, f"Which symbol makes the statement true?   {rtxt(a, k)} ___ {rtxt(b, k)}", right, [LT if right == GT else GT, EQ], f"On a number line {rtxt(a, k)} is {'to the right of' if a > b else 'to the left of'} {rtxt(b, k)}, so it is {'greater' if a > b else 'less'}.", need=2)
def cmp_mixed():
    f = rnd_frac(1, 7, 8); d = R.choice([x for x in (F(3, 10), F(1, 4), F(3, 4), F(1, 2), F(2, 5), F(7, 10), F(1, 5)) if x != f])
    s = R.choice([-1, 1]); a, b = s * f, s * d
    ta, tb = (MINUS if a < 0 else "") + f"{f.numerator}/{f.denominator}", (MINUS if b < 0 else "") + dec(abs(d), 2 if d.denominator in (4, 20) else 1)
    right = GT if a > b else LT
    return mk('2.C', 4, f"Which symbol makes the statement true?   {ta} ___ {tb}", right, [LT if right == GT else GT, EQ], f"As decimals, {sg(round(float(a), 4))} is {'greater' if a > b else 'less'} than {sg(round(float(b), 4))}.", need=2)
def order_rat():
    k = R.choice(['int', 'dec', 'frac']); vals = []
    while len(vals) < 4:
        v = rq(k)
        if v not in vals: vals.append(v)
    up = R.choice([True, False]); good = sorted(vals, reverse=not up)
    if sorted(vals) == vals or sorted(vals, reverse=True) == vals: return False
    t = lambda L: ", ".join(rtxt(v, k) for v in L)
    wrong = [t(sorted(vals, reverse=up)), t(sorted(vals, key=lambda v: (abs(v), v))), t(vals)]
    shuf = sorted(vals, key=lambda v: abs(v), reverse=True)
    wrong.append(t(shuf))
    return mk('2.C', 3, f"Which list shows the numbers in order from {'least to greatest' if up else 'greatest to least'}?   {t(vals)}", t(good), wrong, "Place each number on a number line; numbers farther left are less.")
def left_most():
    k = R.choice(['int', 'dec']); vals = []
    while len(vals) < 4:
        v = rq(k)
        if v not in vals: vals.append(v)
    lo = min(vals)
    return mk('2.C', 3, f"Four points are graphed on a number line at {', '.join(rtxt(v, k) for v in vals)}. Which point is farthest to the left?", rtxt(lo, k), [rtxt(v, k) for v in vals if v != lo], "The least number is farthest left.")
def move_nl():
    a = R.choice([-1, 1]) * R.randint(1, 12); step = R.randint(2, 9) * R.choice([-1, 1]); b = a + step
    return mk('2.C', 3, f"A point is graphed at {sg(a)} on a number line. It moves {abs(step)} units to the {'right' if step > 0 else 'left'}. Where is the point now?", sg(b), [sg(a - step), sg(-b), sg(a + abs(step) * (1 if step < 0 else -1))], f"{sg(a)} {'+' if step > 0 else '−'} {abs(step)} = {sg(b)}.", sgc(f"{a}+({step})"))
rep(6, cmp_rat); rep(3, cmp_mixed); rep(6, order_rat); rep(3, left_most); rep(4, move_nl)
H('2.C', 3, "On a horizontal number line, which statement is true?", "A number to the right is greater than a number to the left.", ["A number to the left is greater than a number to the right.", "Negative numbers are to the right of 0.", "All numbers are the same distance from 0."], "Numbers increase as you move to the right.")
H('2.C', 4, "Which number is between −3 and −2 on a number line?", "−2.5", ["−3.5", "−1.5", "−2"], "−2.5 is halfway between −3 and −2.")

# ================================================================ 2.D order rational numbers in context
CTX = [("temperatures", "°F", "coldest", "warmest", lambda v: f"{sg(v)}°F", (-20, 40), "Four cities reported temperatures of {L}."),
       ("elevations", " feet", "lowest", "highest", lambda v: f"{sg(v)} ft", (-150, 300), "Four locations have elevations of {L}."),
       ("account balances", "", "least money", "most money", lambda v: ("−$" if v < 0 else "$") + str(abs(v)), (-90, 120), "Four accounts have balances of {L}."),
       ("game scores", " points", "lowest score", "highest score", lambda v: sg(v), (-25, 40), "Four players have scores of {L}.")]
def ctx_order():
    nm, un, lo_w, hi_w, f, (lo, hi), tmpl = R.choice(CTX)
    vals = R.sample(range(lo, hi), 4)
    if min(vals) >= 0: return False
    up = R.choice([True, False]); good = sorted(vals, reverse=not up)
    L = ", ".join(f(v) for v in vals)
    wrong = [", ".join(f(v) for v in sorted(vals, reverse=up)), ", ".join(f(v) for v in sorted(vals, key=abs)), ", ".join(f(v) for v in vals)]
    return mk('2.D', 3, tmpl.format(L=L) + f" Which list orders them from {lo_w if up else hi_w} to {hi_w if up else lo_w}?", ", ".join(f(v) for v in good), wrong, f"The {lo_w} is the least value and the {hi_w} is the greatest.")
def ctx_pick():
    nm, un, lo_w, hi_w, f, (lo, hi), tmpl = R.choice(CTX)
    vals = R.sample(range(lo, hi), 4)
    if min(vals) >= 0: return False
    want_lo = R.choice([True, False]); t = min(vals) if want_lo else max(vals)
    return mk('2.D', 3, f"Which of these {nm} is the {lo_w if want_lo else hi_w}?", f(t), [f(v) for v in vals if v != t], f"On a number line the {'least' if want_lo else 'greatest'} value is {f(t)}.")
rep(6, ctx_order); rep(5, ctx_pick)
H('2.D', 4, "A golfer's scores compared with par on four holes were −2, +1, 0, and −3. Which hole had the best (lowest) score compared with par?", "−3", ["+1", "0", "−2"], "Lower scores are better in golf, and −3 is the least.")
H('2.D', 4, "Which is colder: −12°C or −8°C?", "−12°C", ["−8°C", "They are the same temperature.", "It cannot be told."], "−12 is farther below zero, so it is colder.")

# ================================================================ 2.E fractions as division
def f_as_div():
    a = R.randint(1, 15); b = R.randint(2, 15)
    if a == b: return False
    return mk('2.E', 3, f"Which expression is equal to {a}/{b}?", f"{a} ÷ {b}", [f"{b} ÷ {a}", f"{a} × {b}", f"{a} − {b}"], f"The fraction bar means division: {a}/{b} = {a} ÷ {b}.")
def share_frac():
    a = R.randint(1, 9); b = R.randint(a + 1, 12)
    if not coprime(a, b): return False
    thing = R.choice(["pizzas", "sandwiches", "pounds of trail mix", "liters of juice", "yards of ribbon"]); nm = who()
    who2 = R.choice(["friends", "classmates", "teammates", "cousins"])
    return mk('2.E', 3, f"{nm} shares {a} {thing} equally among {b} {who2}. What fraction of the total do they each get?" if False else f"{a} {thing} are shared equally among {b} {who2}. How much does each person get?", f"{a}/{b}", [f"{b}/{a}", sg(a - b), f"{a}/{a + b}"], f"Each person gets {a} ÷ {b} = {a}/{b}.")
def div_to_dec():
    b = R.choice([2, 4, 5, 8, 10, 20, 25]); a = R.randint(1, b - 1)
    if not coprime(a, b): return False
    right = dec(F(a, b));
    return mk('2.E', 3, f"What is {a} ÷ {b} written as a decimal?", right, [dec(F(b, a)) if a != 1 else dec(F(a, b) * 10), dec(F(a, b) / 10), dec(F(a, b) + F(1, 10))], f"{a} ÷ {b} = {a}/{b} = {right}.")
def div_to_frac():
    a = R.randint(1, 20); b = R.randint(2, 12)
    if a % b == 0 or not coprime(a, b): return False
    return mk('2.E', 4, f"Which fraction is equal to {a} ÷ {b}?", ms(F(a, b)) if a > b else f"{a}/{b}", [f"{b}/{a}", ms(F(a - 1, b)) if a > b + 1 else f"{a}/{b + 1}", f"{a + b}"], f"{a} ÷ {b} = {a}/{b}.") if a < b else mk('2.E', 4, f"Which fraction is equal to {a} ÷ {b}?", f"{a}/{b}", [f"{b}/{a}", f"{a - 1}/{b}", f"{a}/{b + 1}"], f"{a} ÷ {b} = {a}/{b}.")
rep(5, f_as_div); rep(5, share_frac); rep(4, div_to_dec); rep(3, div_to_frac)
H('2.E', 3, "What does the fraction bar mean in 7/9?", "division: 7 divided by 9", ["multiplication: 7 times 9", "subtraction: 7 minus 9", "addition: 7 plus 9"], "A fraction bar means “divided by.”")
H('2.E', 4, "The expression 3 ÷ 4 can also be written as 3/4. What is 3/4 as a decimal?", "0.75", ["0.34", "1.33", "0.43"], "3 ÷ 4 = 0.75.")

# ================================================================ 3.A reciprocals and dividing fractions
def recip_concept():
    a = R.randint(2, 9); b = R.randint(2, 11)
    if a == b or not coprime(a, b): return False
    return mk('3.A', 3, f"Dividing by {a}/{b} is the same as multiplying by what number?", f"{b}/{a}", [f"{a}/{b}", f"{b}/{a + 1}", f"{a + 1}/{b}"], f"Dividing by a fraction is the same as multiplying by its reciprocal. The reciprocal of {a}/{b} is {b}/{a}.")
def div_expr():
    p, q, r, s = R.randint(1, 8), R.randint(2, 9), R.randint(2, 8), R.randint(2, 9)
    if r == s or F(p, q) == F(r, s) or p == q or not (coprime(p, q) and coprime(r, s)): return False
    return mk('3.A', 3, f"Which expression has the same value as {p}/{q} ÷ {r}/{s}?", f"{p}/{q} × {s}/{r}", [f"{p}/{q} × {r}/{s}", f"{q}/{p} × {r}/{s}", f"{p}/{q} ÷ {s}/{r}"], f"Dividing by {r}/{s} is the same as multiplying by its reciprocal, {s}/{r}.")
def div_whole_expr():
    n = R.randint(2, 12); r, s = R.randint(1, 7), R.randint(2, 9)
    if r >= s or not coprime(r, s): return False
    return mk('3.A', 3, f"Which expression has the same value as {n} ÷ {r}/{s}?", f"{n} × {s}/{r}" if r > 1 else f"{n} × {s}", [f"{n} × {r}/{s}", f"{r}/{s} ÷ {n}", f"{n} + {s}/{r}"], f"Dividing by {r}/{s} is the same as multiplying by {s}/{r}.")
def div_frac_val():
    a = rnd_frac(1, 8, 10); b = rnd_frac(1, 8, 10); res = a / b
    if a == b or res.denominator > 40 or res.numerator > 60: return False
    return mk('3.A', 4, f"What is {fs(a.numerator, a.denominator)} ÷ {fs(b.numerator, b.denominator)}?", ms(res), [ms(a * b), ms(b / a), ms(1 / (a * b))], f"{a.numerator}/{a.denominator} × {b.denominator}/{b.numerator} = {ms(res)}.", MSC(f"F({a.numerator},{a.denominator})/F({b.numerator},{b.denominator})"))
def servings_div():
    n = R.randint(2, 9); d = R.choice([2, 3, 4, 5, 6, 8]); nm = who(); thing = R.choice(["cups of rice", "pounds of nuts", "liters of juice", "pints of berries"])
    return mk('3.A', 3, f"{nm} has {n} {thing}. Each serving is 1/{d} of a unit. How many servings can {nm} make?", str(n * d), [str(n + d), f"{n}/{d}", str(n * d + d)], f"{n} ÷ 1/{d} = {n} × {d} = {n * d}.", f"str({n * d})")
rep(4, recip_concept); rep(4, div_expr); rep(3, div_whole_expr); rep(6, div_frac_val); rep(4, servings_div)
H('3.A', 3, "Which number is the reciprocal of 5?", "1/5", ["5", "−5", "5/1 + 1"], "The reciprocal of 5 = 5/1 is 1/5, because 5 × 1/5 = 1.")

# ================================================================ 3.B multiplying by a fraction: bigger or smaller?
FACT = {'lt': ["3/4", "2/3", "4/5", "0.8", "1/2", "0.25", "5/8", "0.6"], 'gt': ["5/4", "1 1/2", "3/2", "1.2", "7/4", "2 1/3", "1.75", "9/8"], 'eq': ["1", "1.0", "5/5", "4/4"]}
def inc_dec():
    n = R.choice([8, 12, 15, 20, 24, 30, 36, 40, 48, 60]); kind = R.choice(['lt', 'gt', 'eq', 'lt', 'gt']); ft = R.choice(FACT[kind])
    txt = {'lt': "It is less than", 'gt': "It is greater than", 'eq': "It is equal to"}
    right = f"{txt[kind]} {n}."
    wrong = [f"{v} {n}." for k, v in txt.items() if k != kind] + [f"It cannot be told without calculating."]
    why = {'lt': "A number less than 1 makes the product smaller.", 'gt': "A number greater than 1 makes the product larger.", 'eq': "Multiplying by 1 leaves the number unchanged."}[kind]
    return mk('3.B', 3, f"Without calculating, how does the product {n} × {ft} compare with {n}?", right, wrong, why)
def which_gt():
    n = R.choice([12, 16, 20, 24, 30, 40, 60]); big = R.choice(FACT['gt']); smalls = R.sample(FACT['lt'] + FACT['eq'], 3)
    return mk('3.B', 3, f"Without calculating, which product is greater than {n}?", f"{n} × {big}", [f"{n} × {x}" for x in smalls], f"Only a factor greater than 1 makes {n} larger, and {big} is greater than 1.")
def which_lt():
    n = R.choice([12, 16, 20, 24, 30, 40, 60]); small = R.choice(FACT['lt']); bigs = R.sample(FACT['gt'] + FACT['eq'], 3)
    return mk('3.B', 3, f"Without calculating, which product is less than {n}?", f"{n} × {small}", [f"{n} × {x}" for x in bigs], f"Only a factor less than 1 makes {n} smaller, and {small} is less than 1.")
def recipe_scale():
    nm = who(); a = rnd_frac(1, 7, 8); f = R.choice([F(2, 3), F(3, 4), F(1, 2), F(3, 2), F(5, 4), F(4, 3)])
    more = f > 1
    return mk('3.B', 3, f"A recipe uses {a.numerator}/{a.denominator} cup of flour. {nm} makes {ms(f)} of the recipe. Will {nm} use more or less than {a.numerator}/{a.denominator} cup?", "more flour" if more else "less flour", ["less flour" if more else "more flour", "the same amount of flour", "exactly 1 cup of flour"], f"{ms(f)} is {'greater' if more else 'less'} than 1, so the amount is {'greater' if more else 'less'}.")
rep(7, inc_dec); rep(3, which_gt); rep(3, which_lt); rep(3, recipe_scale)

# ================================================================ 3.C integer operations with models
def counters_val():
    p, n = R.randint(1, 9), R.randint(1, 9)
    if p == n: return False
    return mk('3.C', 3, f"A model has {p} positive counters and {n} negative counters. Each positive-negative pair makes 0. What integer does the model show?", sg(p - n), [sg(n - p), sg(p + n), sg(-(p + n))], f"{min(p, n)} pairs make 0, leaving {abs(p - n)} {'positive' if p > n else 'negative'} counters.", sgc(f"{p}-{n}"))
def nl_equation():
    a = R.choice([-1, 1]) * R.randint(2, 9); m = R.choice([-1, 1]) * R.randint(2, 9)
    if a + m == 0: return False
    right = f"{sg(a)} + {par(m)} = {sg(a + m)}"
    wrong = [f"{sg(a)} + {par(-m)} = {sg(a - m)}", f"{sg(-a)} + {par(m)} = {sg(m - a)}", f"{sg(-a)} + {par(-m)} = {sg(-a - m)}"]
    return mk('3.C', 3, f"On a number line, a hiker starts at {sg(a)} and moves {abs(m)} units {'right' if m > 0 else 'left'}. Which equation shows this?", right, wrong, f"Moving {'right' if m > 0 else 'left'} means adding {sg(m)}: {right}.")
def remove_counters():
    p = R.randint(3, 9); q = R.randint(1, p - 1)
    return mk('3.C', 4, f"A model starts with {p} negative counters. {q} negative counters are taken away. Which equation matches the model?", f"−{p} − (−{q}) = −{p - q}", [f"−{p} + (−{q}) = −{p + q}", f"{p} − {q} = {p - q}", f"{p} + {q} = {p + q}"], f"Taking away {q} negative counters is subtracting −{q}, leaving {p - q} negative counters.")
def zero_pair_add():
    n = R.randint(2, 8)
    return mk('3.C', 3, f"Which model shows that {sg(-n)} + {n} = 0?", f"{n} negative counters and {n} positive counters, which pair up to make zero", [f"{n} negative counters and {n + 1} negative counters", f"{n} positive counters only", f"{n} negative counters and {n} positive counters, which make {2 * n}"], "Each positive counter and negative counter pair cancel to make 0.")
rep(4, counters_val); rep(4, nl_equation); rep(3, remove_counters); rep(2, zero_pair_add)

# ================================================================ 3.D integer operations fluently
def int_add():
    a = R.randint(-24, 24); b = R.randint(-24, 24)
    if a == 0 or b == 0 or (a > 0 and b > 0) or abs(a) == abs(b): return False
    r = a + b
    return mk('3.D', 3, f"What is {sg(a)} + {par(b)}?", sg(r), [sg(-r), sg(abs(a) + abs(b)), sg(a - b)], f"The signs are different, so subtract the absolute values and keep the sign of the number farther from 0: {sg(r)}.", sgc(f"{a}+({b})"))
def int_sub():
    a = R.randint(-20, 20); b = R.randint(-20, 20)
    if a == 0 or b == 0 or a == b: return False
    r = a - b
    return mk('3.D', 3, f"What is {sg(a)} − {par(b)}?", sg(r), [sg(a + b), sg(b - a), sg(-r)], f"Subtracting {sg(b)} is the same as adding {sg(-b)}: {sg(a)} + {par(-b)} = {sg(r)}.", sgc(f"{a}-({b})"))
def int_mul():
    a = R.randint(-12, 12); b = R.randint(-12, 12)
    if abs(a) < 2 or abs(b) < 2 or (a > 0 and b > 0): return False
    r = a * b
    return mk('3.D', 3, f"What is {sg(a)} × {par(b)}?", sg(r), [sg(-r), sg(a + b), sg(r + b)], f"{'Same signs give a positive product' if r > 0 else 'Different signs give a negative product'}: {sg(r)}.", sgc(f"{a}*({b})"))
def int_div():
    q = R.randint(-12, 12); b = R.randint(-12, 12)
    if abs(q) < 2 or abs(b) < 2 or (q > 0 and b > 0): return False
    a = q * b
    return mk('3.D', 3, f"What is {sg(a)} ÷ {par(b)}?", sg(q), [sg(-q), sg(a - b), sg(q + 1)], f"{'Same signs give a positive quotient' if q > 0 else 'Different signs give a negative quotient'}: {sg(q)}.", sgc(f"{a}//({b})"))
def int_word():
    k = R.randint(0, 5)
    if k == 0:
        a = R.randint(-8, 14); d = R.randint(5, 25); nm = R.choice(["Austin", "a town", "a ski lodge"]); 
        return mk('3.D', 3, f"At midnight the temperature was {sg(a)}°F. By morning it dropped {d} degrees. What was the temperature in the morning?", f"{sg(a - d)}°F", [f"{sg(a + d)}°F", f"{sg(d - a)}°F", f"{sg(-(a + d))}°F"], f"{sg(a)} − {d} = {sg(a - d)}.", f"{sgc(f'{a}-{d}')}+'\\u00b0F'")
    if k == 1:
        d = R.randint(30, 200); u = R.randint(10, d - 5)
        return mk('3.D', 3, f"A submarine is at −{d} feet. It rises {u} feet. What is its new elevation?", f"{sg(-d + u)} feet", [f"{sg(-d - u)} feet", f"{sg(d + u)} feet", f"{sg(d - u)} feet"], f"−{d} + {u} = {sg(-d + u)}.", f"{sgc(f'-{d}+{u}')}+' feet'")
    if k == 2:
        a = R.randint(10, 60); b = R.randint(a + 5, a + 70); nm = who()
        return mk('3.D', 3, f"{nm}'s account has ${a}. {nm} pays a ${b} bill. What is the new balance?", f"{sg(a - b)} dollars", [f"{a + b} dollars", f"{sg(b - a)} dollars" if False else f"{b - a} dollars", f"{sg(-(a + b))} dollars"], f"{a} − {b} = {sg(a - b)}.", f"{sgc(f'{a}-{b}')}+' dollars'")
    if k == 3:
        l = R.randint(3, 15); g = R.randint(2, 14)
        if l == g: return False
        return mk('3.D', 3, f"A football team loses {l} yards on one play and then gains {g} yards on the next play. What integer shows the net change?", f"{sg(g - l)} yards", [f"{sg(l - g)} yards", f"{sg(-(l + g))} yards", f"{l + g} yards"], f"−{l} + {g} = {sg(g - l)}.", f"{sgc(f'{g}-{l}')}+' yards'")
    if k == 4:
        r = R.randint(3, 12); m = R.randint(3, 9)
        return mk('3.D', 3, f"A diver goes down {r} feet each minute for {m} minutes. Which integer shows her total change in depth?", f"{sg(-r * m)} feet", [f"{r * m} feet", f"{sg(-(r + m))} feet", f"{sg(-r * m + r)} feet"], f"{m} × (−{r}) = {sg(-r * m)}.", f"{sgc(f'-{r*m}')}+' feet'")
    t = R.randint(2, 9); q = R.randint(4, 30)
    return mk('3.D', 3, f"A stock lost ${t * q} in value over {t} days, falling the same amount each day. Which integer shows the change in value each day?", f"{sg(-q)} dollars", [f"{q} dollars", f"{sg(-t * q)} dollars", f"{sg(-(q + t))} dollars"], f"{sg(-t * q)} ÷ {t} = {sg(-q)}.", f"{sgc(f'-{q}')}+' dollars'")
def neg_count():
    n = R.randint(2, 6); m = R.randint(0, 2)
    odd = n % 2 == 1
    return mk('3.D', 3, f"How does the product of {n} negative integers and {m} positive integers compare with 0?" if m else f"How does the product of {n} negative integers compare with 0?", "less than 0" if odd else "greater than 0", ["greater than 0" if odd else "less than 0", "equal to 0", "it cannot be told"], f"Each pair of negative factors makes a positive; with {n} negative factors the product is {'less' if odd else 'greater'} than 0.")
rep(7, int_add); rep(7, int_sub); rep(7, int_mul); rep(6, int_div); rep(10, int_word); rep(3, neg_count)
H('3.D', 3, "Which expression has the same value as 5 − (−3)?", "5 + 3", ["5 − 3", "−5 + 3", "−5 − 3"], "Subtracting a negative is the same as adding its opposite.")
H('3.D', 3, "What is the value of −15 + 15?", "0", ["30", "−30", "15"], "Opposites add to 0.")

# ================================================================ 3.E multiply and divide positive rational numbers
def fmul():
    a = rnd_frac(1, 8, 9); b = rnd_frac(1, 8, 9); r = a * b
    return mk('3.E', 3, f"What is {a.numerator}/{a.denominator} × {b.numerator}/{b.denominator}?", ms(r), [ms(a + b), ms(a * b + F(1, 10)) if False else ms(F(a.numerator * b.numerator, a.denominator + b.denominator)), ms(a / b)], f"Multiply the numerators and denominators, then simplify: {ms(r)}.", MSC(f"F({a.numerator},{a.denominator})*F({b.numerator},{b.denominator})"))
def mixed_mul():
    w = R.randint(1, 4); a = rnd_frac(1, 5, 6); n = R.randint(2, 8); x = w + a
    r = x * n
    return mk('3.E', 4, f"What is {w} {a.numerator}/{a.denominator} × {n}?", ms(r), [ms(w * n + a), ms(F(w * n) + a * n * 2) if False else ms(w * n), ms(x + n)], f"{w} {a.numerator}/{a.denominator} = {ms(x * a.denominator) if False else (w * a.denominator + a.numerator)}/{a.denominator}, and times {n} gives {ms(r)}.", MSC(f"(F({w})+F({a.numerator},{a.denominator}))*{n}"))
def mixed_div():
    n = R.randint(2, 6); a = rnd_frac(1, 7, 8); x = F(R.randint(2, 6)) + a
    r = x / n
    return mk('3.E', 4, f"What is {ms(x)} ÷ {n}?", ms(r), [ms(x * n), ms(F(x.numerator, x.denominator * 2 * n) if False else x - n), ms(n / x)], f"{ms(x)} ÷ {n} = {ims(x)} × 1/{n} = {ms(r)}.", MSC(f"(F({x.numerator},{x.denominator}))/{n}"))
def dec_mul():
    a = R.randint(12, 99) / 10; b = R.randint(2, 9) / 10 if R.random() < 0.5 else R.randint(12, 35) / 10
    A, Bb = round(a * 10), round(b * 10); r = A * Bb
    return mk('3.E', 3, f"What is {a:.1f} × {b:.1f}?", f"{r // 100}.{r % 100:02d}", [f"{r // 10}.{r % 10}", f"{r}.0" if False else f"{r / 1000:.3f}", f"{(A + Bb) // 10}.{(A + Bb) % 10}"], f"{A} × {Bb} = {r}, and there are 2 decimal places in all: {r // 100}.{r % 100:02d}.", f"'{r // 100}.' + '%02d' % ({r} % 100)")
def dec_div():
    d = R.choice([2, 4, 5, 8, 0.5, 0.2, 0.25]); q = R.randint(12, 90) / 10
    if d in (0.5, 0.2, 0.25):
        a = round(q * d, 3)
    else:
        a = round(q * d, 2)
    if not (0 < a < 400): return False
    right = f"{q:.1f}"
    return mk('3.E', 4, f"What is {a:g} ÷ {d:g}?", right, [f"{q * 10:.1f}", f"{q / 10:.2f}", f"{q + 1:.1f}"], f"{a:g} ÷ {d:g} = {right}.", f"'{right}'")
def frac_story():
    nm = who(); a = R.choice([F(3, 4), F(2, 3), F(5, 6), F(3, 8), F(1, 2), F(4, 5)]); n = R.randint(2, 9); r = a * n
    return mk('3.E', 3, f"{nm} walks {ms(a)} mile each day for {n} days. How many miles does {nm} walk in all?", f"{ms(r)} miles", [f"{ms(a + n)} miles", f"{ms(n / a)} miles", f"{ms(a / n)} miles"], f"{n} × {ms(a)} = {ms(r)}.", f"{MSC(f'F({a.numerator},{a.denominator})*{n}')}+' miles'")
def frac_story_div():
    nm = who(); a = R.choice([F(1, 2), F(1, 3), F(1, 4), F(3, 4), F(2, 3)]); n = R.randint(2, 9) * a.denominator // 1; 
    w = R.randint(2, 6)
    r = F(w) / a
    return mk('3.E', 4, f"{nm} has {w} pounds of trail mix. Each bag holds {ms(a)} pound. How many bags can {nm} fill?", f"{ms(r)} bags", [f"{ms(w * a)} bags", f"{ms(w + a)} bags", f"{ms(a / w)} bags"], f"{w} ÷ {ms(a)} = {ms(r)}.", f"{MSC(f'F({w})/F({a.numerator},{a.denominator})')}+' bags'")
def area_story():
    nm = who(); l = F(R.randint(3, 20), 2); w = F(R.randint(3, 12), 2); r = l * w
    return mk('3.E', 4, f"{nm}'s garden is {ms(l)} meters long and {ms(w)} meters wide. What is its area in square meters?", f"{ms(r)} square meters", [f"{ms(l + w)} square meters", f"{ms(2 * (l + w))} square meters", f"{ms(l / w)} square meters"], f"{ms(l)} × {ms(w)} = {ms(r)}.", f"{MSC(f'F({l.numerator},{l.denominator})*F({w.numerator},{w.denominator})')}+' square meters'")
rep(6, fmul); rep(4, mixed_mul); rep(4, mixed_div); rep(5, dec_mul); rep(4, dec_div); rep(3, frac_story); rep(3, frac_story_div); rep(3, area_story)

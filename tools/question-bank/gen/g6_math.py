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

# ================================================================ 4.A compare two rules
H('4.A', 3, "Rule 1 is y = 3x and Rule 2 is y = x + 3. When x = 5, how do the two outputs compare?", "Rule 1 gives 15 and Rule 2 gives 8, so Rule 1 is greater", ["Rule 1 gives 8 and Rule 2 gives 15, so Rule 2 is greater", "Both rules give 8", "Both rules give 15"], "Rule 1: 3 × 5 = 15. Rule 2: 5 + 3 = 8.")
H('4.A', 3, "Rule A is y = 2x and Rule B is y = x + 2. For which value of x do both rules give the same output?", "x = 2", ["x = 1", "x = 3", "x = 4"], "At x = 2, 2 × 2 = 4 and 2 + 2 = 4.")
H('4.A', 4, "A table shows x = 1, 2, 3, 4 and y = 4, 8, 12, 16. Which rule matches the table?", "y = 4x", ["y = x + 3", "y = x + 4", "y = 4 + 2x"], "Each y is 4 times x, so the rule is multiplication by 4.")
H('4.A', 4, "A table shows x = 1, 2, 3, 4 and y = 6, 7, 8, 9. Which rule matches the table?", "y = x + 5", ["y = 6x", "y = x + 6", "y = 5x"], "Each y is x plus 5.")
H('4.A', 3, "As x increases by 1, how does y change for the rule y = 5x?", "y increases by 5", ["y increases by 1", "y increases by 6", "y is multiplied by 5 each time"], "Multiplying by 5, so each step in x adds 5 to y.")
H('4.A', 3, "Which statement describes the graph of y = x + 4 compared with y = 4x?", "y = 4x grows faster as x gets larger", ["y = x + 4 grows faster as x gets larger", "They grow at the same rate", "Neither one grows"], "y = 4x rises 4 for each 1 in x, while y = x + 4 rises only 1.")
# ================================================================ 4.B prediction and comparison with ratios
H('4.B', 3, "A recipe uses 2 cups of rice for every 3 cups of water. If you use more rice but the same amount of water, the rice-to-water ratio will...", "increase", ["decrease", "stay the same", "become zero"], "More rice with the same water makes the first quantity larger relative to the second.")
H('4.B', 4, "The Hawks have 3 wins for every 2 losses. The Owls have 4 wins for every 4 losses. Which statement is true?", "The Hawks have the better win-to-loss ratio", ["The Owls have the better win-to-loss ratio", "The teams have equal ratios", "Neither ratio can be compared"], "The Hawks' ratio is 3/2 = 1.5 and the Owls' ratio is 4/4 = 1.")
H('4.B', 4, "A car travels 120 miles on 4 gallons. About how far should it travel on 10 gallons at the same rate?", "300 miles", ["240 miles", "480 miles", "30 miles"], "120 ÷ 4 = 30 miles per gallon, and 30 × 10 = 300.")
H('4.B', 3, "Which store has the better deal: 5 notebooks for $10 or 3 notebooks for $9?", "5 for $10", ["3 for $9", "They cost the same per notebook", "Not enough information"], "$10 ÷ 5 = $2 each; $9 ÷ 3 = $3 each.")
H('4.B', 3, "If the ratio of boys to girls is 2:3 and there are 12 boys, how many girls are there?", "18", ["8", "12", "30"], "12 ÷ 2 = 6 per part, and 3 × 6 = 18.")
# ================================================================ 4.C ratios
def ratio_q():
    a = R.randint(2, 9); b = R.randint(2, 9)
    if a == b: return False
    nm = R.choice(["red marbles", "cats", "apples", "pencils", "tickets"]); nm2 = R.choice(["blue marbles", "dogs", "oranges", "pens", "coupons"])
    return mk('4.C', 2, f"A bag has {a} {nm} and {b} {nm2}. What is the ratio of {nm} to {nm2}?", f"{a}:{b}", [f"{b}:{a}", f"{a}:{a + b}", f"{a + b}:{b}"], f"Put {nm} first, {nm2} second: {a}:{b}.")
rep(5, ratio_q)
H('4.C', 3, "Which situation is a multiplicative comparison of two quantities with the same attribute?", "There are 3 times as many fiction books as poetry books", ["A runner goes 6 miles in 1 hour", "A shirt costs $12", "A class has 25 students"], "A ratio of two amounts of the same kind (books to books) is a multiplicative comparison.")
H('4.C', 3, "A class has 12 girls and 16 boys. Which ratio is equivalent to girls to boys?", "3:4", ["4:3", "12:28", "16:12"], "12:16 simplifies to 3:4.")
H('4.C', 4, "A ratio of cats to dogs is 5:2. What does this tell you?", "For every 5 cats there are 2 dogs", ["There are 5 pets in all", "There are 2 more cats than dogs", "Every dog has 5 cats"], "The ratio compares the amount of cats to the amount of dogs.")
# ================================================================ 4.D rates
H('4.D', 2, "A rate is a comparison by division of two quantities that have...", "different attributes", ["the same attribute", "no units", "the same units"], "Rates compare unlike quantities, such as miles and hours.")
H('4.D', 3, "Which is a unit rate?", "60 miles per 1 hour", ["60 miles per 2 hours", "120 miles per 3 hours", "60 miles"], "A unit rate has 1 as the second quantity.")
def unit_rate():
    r = R.randint(3, 15); n = R.randint(3, 9); nm = who()
    return mk('4.D', 3, f"{nm} paid ${r * n} for {n} identical books. What is the price per book?", f"${r}", [f"${r * n + n}", f"${r + n}", f"${r * n * n}"], f"${r * n} ÷ {n} = ${r}.", f"'${r}'")
rep(5, unit_rate)
H('4.D', 4, "A snail moves 24 inches in 8 minutes. What is the unit rate in inches per minute?", "3", ["32", "192", "1/3"], "24 ÷ 8 = 3 inches per minute.")
H('4.D', 4, "A faucet fills 45 gallons in 9 minutes. How many gallons per minute is that?", "5", ["36", "405", "1/5"], "45 ÷ 9 = 5.")
# ================================================================ 4.E ratios and percents with models
H('4.E', 3, "A 10 × 10 grid has 35 squares shaded. What percent is shaded?", "35%", ["3.5%", "65%", "10%"], "35 out of 100 is 35%.")
H('4.E', 3, "A 10 × 10 grid has 35 squares shaded. Which decimal represents the shaded part?", "0.35", ["3.5", "0.035", "35"], "35/100 = 0.35.")
H('4.E', 3, "A bar is split into 5 equal parts and 2 are shaded. What percent is shaded?", "40%", ["25%", "20%", "2%"], "2/5 = 40/100 = 40%.")
H('4.E', 3, "Which fraction is equal to 60%?", "3/5", ["6/5", "1/6", "3/10"], "60/100 simplifies to 3/5.")
H('4.E', 3, "Which decimal is equal to 7%?", "0.07", ["0.7", "7.0", "0.007"], "7% = 7/100 = 0.07.")
H('4.E', 4, "A ratio table shows 2 red : 3 blue. Which ratio represents the same relationship?", "6:9", ["4:5", "5:6", "3:2"], "Multiply both parts by 3.")
# ================================================================ 4.F benchmark fractions and percents
H('4.F', 3, "Which percent is equal to 1/4?", "25%", ["14%", "40%", "4%"], "1/4 = 25/100.")
H('4.F', 3, "Which percent is equal to 1/10?", "10%", ["1%", "100%", "0.1%"], "1/10 = 10/100.")
H('4.F', 4, "On a number line from 0 to 1, where is 33 1/3% located?", "at 1/3 of the way from 0", ["at the halfway mark", "at 3/4 of the way from 0", "at 0.033"], "33 1/3% = 1/3.")
H('4.F', 4, "What is 50% of the way from 0 to 80 on a number line?", "40", ["50", "20", "30"], "50% is half of 80.")
H('4.F', 4, "Which percent is equal to 3/4?", "75%", ["34%", "60%", "43%"], "3 × 25% = 75%.")
H('4.F', 4, "20% of a double number line from 0 to 50 is at which value?", "10", ["20", "5", "25"], "20% is 1/5 of 50, which is 10.")
# ================================================================ 4.G equivalent forms
H('4.G', 3, "A store takes 25% off a $40 shirt. Which fraction of the price is taken off?", "1/4", ["1/25", "2/5", "25/4"], "25% = 1/4.")
H('4.G', 3, "A quiz score is 18 out of 20. What percent is that?", "90%", ["18%", "80%", "20%"], "18/20 = 90/100.")
H('4.G', 3, "Which is equivalent to 0.8?", "80%", ["8%", "0.8%", "800%"], "0.8 = 80/100.")
H('4.G', 4, "Which list is in order from least to greatest?", "0.4, 45%, 1/2", ["1/2, 45%, 0.4", "45%, 0.4, 1/2", "0.4, 1/2, 45%"], "0.4 = 40%, 45%, 1/2 = 50%.")
H('4.G', 4, "A tip is 15% of a bill. Which decimal would you multiply by the bill amount?", "0.15", ["1.5", "15", "0.015"], "15% = 0.15.")
H('4.G', 4, "7 out of 8 students passed. Which is closest to the percent who passed?", "87.5%", ["78%", "70%", "8.7%"], "7 ÷ 8 = 0.875.")
# ================================================================ 4.H convert units
H('4.H', 2, "How many inches are in 3 feet?", "36", ["12", "30", "9"], "3 × 12 = 36.")
H('4.H', 2, "How many centimeters are in 5 meters?", "500", ["50", "5,000", "0.05"], "1 m = 100 cm.")
H('4.H', 3, "How many quarts are in 4 gallons?", "16", ["8", "12", "32"], "1 gallon = 4 quarts.")
H('4.H', 3, "How many ounces are in 3 pounds?", "48", ["36", "30", "12"], "1 pound = 16 ounces.")
H('4.H', 3, "How many grams are in 2.5 kilograms?", "2,500", ["250", "25", "25,000"], "1 kg = 1,000 g.")
H('4.H', 4, "Which proportion can be used to find how many feet are in 84 inches?", "12/1 = 84/x", ["12/84 = x/1", "1/12 = x/84 with x inches", "84/12 = 1/x with x gallons"], "12 inches for each 1 foot, so 12/1 = 84/x gives 7 feet.")
H('4.H', 4, "A rope is 9 yards long. How many feet is that?", "27", ["3", "81", "18"], "1 yard = 3 feet.")
H('4.H', 4, "How many minutes are in 2.5 hours?", "150", ["25", "250", "125"], "2.5 × 60 = 150.")

# ================================================================ 5.A ratios and rates with tables, graphs, scale
H('5.A', 3, "A table shows 2 cups flour for 1 batch, 4 cups for 2 batches, 6 cups for 3 batches. How many cups of flour are needed for 5 batches?", "10", ["8", "12", "7"], "Each batch needs 2 cups: 5 × 2 = 10.")
H('5.A', 3, "On a map, 1 inch represents 20 miles. Two towns are 3.5 inches apart on the map. What is the real distance?", "70 miles", ["23.5 miles", "7 miles", "35 miles"], "3.5 × 20 = 70.")
H('5.A', 4, "A graph of a proportional relationship is a straight line that passes through which point?", "(0, 0)", ["(1, 1)", "(0, 1)", "(1, 0)"], "In a proportional relationship, 0 of one quantity goes with 0 of the other.")
H('5.A', 3, "A scale drawing uses a scale of 1 cm = 4 m. A wall is 5 cm long in the drawing. How long is the real wall?", "20 m", ["9 m", "1.25 m", "5 m"], "5 × 4 = 20.")
H('5.A', 4, "A double number line has 3 miles aligned with 45 minutes. Which time aligns with 6 miles at the same rate?", "90 minutes", ["48 minutes", "135 minutes", "60 minutes"], "6 miles is double 3 miles, so double 45 minutes.")
H('5.A', 4, "Which equation matches a rate of $6 for every 2 pounds of apples, where c is the cost and p is the pounds?", "c = 3p", ["c = 6p", "c = 2p", "c = p + 4"], "$6 ÷ 2 = $3 per pound, so c = 3p.")
# ================================================================ 5.B percent problems
def pct_of():
    p = R.choice([10, 20, 25, 30, 40, 50, 60, 75]); w = R.choice([40, 60, 80, 120, 200, 240, 400])
    r = p * w // 100
    if p * w % 100: return False
    return mk('5.B', 3, f"What is {p}% of {w}?", str(r), [str(w - r), str(p + w), str(r * 2)], f"{p}/100 × {w} = {r}.", f"str({p}*{w}//100)")
rep(6, pct_of)
def pct_whole():
    p = R.choice([10, 20, 25, 40, 50]); w = R.choice([40, 60, 80, 120, 200]); r = p * w // 100
    nm = who()
    return mk('5.B', 4, f"{nm} saved ${r}, which is {p}% of the goal. What is the goal?", f"${w}", [f"${r * p}", f"${w - r}", f"${w + r}"], f"{p}% of the goal is ${r}, so the goal is ${r} ÷ {p / 100:g} = ${w}.", f"'${w}'")
rep(4, pct_whole)
def pct_found():
    t = R.choice([20, 25, 40, 50, 80]); p = R.choice([10, 20, 25, 50, 75, 40, 60]); a = t * p // 100
    if t * p % 100: return False
    nm = who()
    return mk('5.B', 4, f"{nm} answered {a} of {t} questions correctly. What percent is correct?", f"{p}%", [f"{a}%", f"{100 - p}%", f"{t - a}%"], f"{a} ÷ {t} = {p / 100:g} = {p}%.", f"'{p}%'")
rep(4, pct_found)
H('5.B', 3, "A jacket costs $60 and is 25% off. What is the discount in dollars?", "$15", ["$25", "$45", "$35"], "25% of 60 = 15.")
H('5.B', 4, "A $40 meal has a 20% tip. How much is the tip?", "$8", ["$20", "$4", "$80"], "0.20 × 40 = 8.")
# ================================================================ 5.C equal parts of the same whole
H('5.C', 3, "Which three values show the same part of a whole?", "1/2, 0.5, 50%", ["1/2, 0.2, 20%", "1/4, 0.4, 40%", "1/10, 1.0, 10%"], "1/2 = 0.5 = 50%.")
H('5.C', 3, "Which values are equal?", "3/4, 0.75, 75%", ["3/4, 0.34, 34%", "3/5, 0.35, 35%", "4/3, 0.43, 43%"], "3 ÷ 4 = 0.75 = 75%.")
H('5.C', 3, "A pizza is cut in 8 equal slices and Eli eats 2. Which is NOT equal to the part he ate?", "0.5", ["1/4", "0.25", "25%"], "2/8 = 1/4 = 0.25 = 25%.")
H('5.C', 4, "A garden is 40% flowers. What fraction of the garden is flowers?", "2/5", ["4/5", "1/4", "4/10 of 40"], "40/100 simplifies to 2/5.")
H('5.C', 4, "Which statement is true about 1/5, 0.2 and 20%?", "They name the same part of a whole", ["They name three different amounts", "1/5 is greatest", "20% is least"], "1/5 = 0.2 = 20%.")
# ================================================================ 6.A independent and dependent quantities
H('6.A', 3, "A table shows hours worked (h) and money earned (m). Which quantity is the independent quantity?", "the time spent working", ["money earned", "the hourly rate only", "neither"], "Money depends on how many hours are worked.")
H('6.A', 3, "In the relationship between the number of tickets bought and the total cost, which is the dependent quantity?", "the amount of money owed", ["number of tickets", "ticket color", "the day of the week"], "The cost depends on the number of tickets.")
H('6.A', 3, "On a graph, which axis usually shows the independent quantity?", "the horizontal (x) axis", ["the vertical (y) axis", "neither axis", "both axes"], "The independent quantity goes on x.")
H('6.A', 4, "A graph shows the distance a bike travels over time. What is the dependent quantity?", "how far the bike has gone", ["time", "speed limit", "rider's name"], "Distance depends on how long the bike is ridden.")
H('6.A', 4, "A taxi charges by the mile. Which sentence is correct?", "The fare depends on the miles driven", ["The miles driven depend on the fare", "Neither depends on the other", "The fare is the independent quantity"], "Miles driven is independent; fare is dependent.")
# ================================================================ 6.B write an equation from a table
H('6.B', 4, "A table shows x = 1, 2, 3 and y = 5, 10, 15. Which equation represents the relationship?", "y = 5x", ["y = x + 4", "y = x + 5", "y = 15x"], "Each y is 5 times x.")
H('6.B', 4, "A table shows x = 2, 4, 6 and y = 5, 7, 9. Which equation represents the relationship?", "y = x + 3", ["y = 2.5x", "y = x + 5", "y = 3x"], "y is 3 more than x each time.")
H('6.B', 4, "A table shows n = 3, 6, 9 and c = 12, 24, 36. Which equation fits?", "c = 4n", ["c = n + 9", "c = 3n", "c = n + 4"], "12 ÷ 3 = 4.")
H('6.B', 4, "A table shows x = 5, 6, 7 and y = 2, 3, 4. Which equation fits?", "y = x − 3", ["y = x + 3", "y = 3x", "y = x − 2"], "Each y is 3 less than x.")
H('6.B', 4, "A table shows x = 1, 2, 3 and y = 7, 8, 9. Which statement is true?", "y = x + 6", ["y = 7x", "y = x + 7", "y = 6x"], "Each y is x plus 6.")
# ================================================================ 6.C representations y=kx, y=x+b
H('6.C', 3, "A gym charges $15 a month. Which equation gives the cost c for m months?", "c = 15m", ["c = m + 15", "c = 15 − m", "c = m ÷ 15"], "Cost is 15 times the number of months.")
H('6.C', 3, "A student has $20 and earns $4 each week. Which equation gives the total t after w weeks?", "t = 4w + 20", ["t = 24w", "t = 20w + 4", "t = 4w − 20"], "Starts at 20 and adds 4 per week.")
H('6.C', 4, "Ava is 5 years older than her cousin. If her cousin is c years old, which equation gives Ava's age a?", "a = c + 5", ["a = 5c", "a = c − 5", "a = c ÷ 5"], "Ava is 5 more than c.")
H('6.C', 4, "A table shows time (h) and miles (m): h = 1, 2, 3; m = 45, 90, 135. Which representation matches?", "m = 45h", ["m = h + 44", "m = 90h", "h = 45m"], "Each hour adds 45 miles from 0.")
H('6.C', 4, "A recipe uses 3 eggs per cake. Which graph description matches e = 3c?", "a straight line through (0, 0) and (1, 3)", ["a straight line through (0, 3) and (1, 4)", "a line through (3, 0)", "a curve that goes down"], "e = 3c passes through (0, 0), (1, 3), (2, 6).")
# ================================================================ 7.A order of operations and exponents
def order_ops():
    a = R.randint(2, 9); b = R.randint(2, 6); c = R.randint(2, 6); r = a + b * c
    return mk('7.A', 2, f"What is the value of {a} + {b} × {c}?", str(r), [str((a + b) * c), str(a + b + c), str(a * b + c)], f"Multiply first: {b} × {c} = {b * c}, then add {a} to get {r}.", f"str({a}+{b}*{c})")
rep(4, order_ops)
def exp_val():
    b = R.randint(2, 6); e = R.randint(2, 4); r = b ** e
    return mk('7.A', 2, f"What is {b}{'²³⁴'[e - 2]}?", str(r), [str(b * e), str(b + e), str(e ** b)], f"{b} is used as a factor {e} times: {r}.", f"str({b}**{e})")
rep(4, exp_val)
def paren_ops():
    a = R.randint(10, 40); b = R.randint(2, 8); c = R.randint(2, 5); r = (a - b) * c
    return mk('7.A', 3, f"What is the value of ({a} − {b}) × {c}?", str(r), [str(a - b * c), str(a - b + c), str((a + b) * c)], f"Parentheses first: {a - b} × {c} = {r}.", f"str(({a}-{b})*{c})")
rep(4, paren_ops)
H('7.A', 3, "Which is the prime factorization of 36?", "2 × 2 × 3 × 3", ["2 × 18", "6 × 6", "4 × 9"], "Prime factors are only primes: 2, 2, 3, 3.")
H('7.A', 3, "Which is the prime factorization of 20?", "2 × 2 × 5", ["4 × 5", "2 × 10", "2 × 5"], "20 = 2 × 2 × 5.")
H('7.A', 4, "Which expression is equivalent to 2³ + 4?", "12", ["10", "14", "16"], "2³ = 8, and 8 + 4 = 12.")
H('7.A', 4, "What is the value of 3 + 2² × 5?", "23", ["125", "35", "28"], "Exponent first: 4. Then multiply: 20. Then add 3.")
# ================================================================ 7.B expressions vs equations
H('7.B', 2, "Which is an equation?", "3x + 2 = 11", ["3x + 2", "5y", "4 × 7"], "An equation has an equal sign.")
H('7.B', 2, "Which is an expression?", "5n − 3", ["5n − 3 = 12", "n = 8", "2 + 2 = 4"], "An expression has no equal sign.")
H('7.B', 3, "The phrase “7 more than a number” can be written as which expression?", "n + 7", ["7n", "n − 7", "n = 7"], "More than means add.")
H('7.B', 3, "The phrase “the product of 6 and a number” is written as...", "6n", ["6 + n", "n − 6", "6 ÷ n"], "Product means multiply.")
H('7.B', 4, "Which statement is an equation?", "A number plus 5 is 12", ["A number plus 5", "Twice a number", "The sum of 4 and 9"], "“Is” signals equality.")
# ================================================================ 7.C equivalent expressions
H('7.C', 3, "Which expression is equivalent to x + x + x?", "3x", ["x³", "x + 3", "3 + x"], "Three x's add to 3x.")
H('7.C', 3, "Which expression is equivalent to 2(x + 4)?", "2x + 8", ["2x + 4", "x + 8", "2x + 6"], "Distribute the 2.")
H('7.C', 4, "Are 4(y + 1) and 4y + 1 equivalent?", "No, because 4(y + 1) = 4y + 4", ["Yes, they are the same", "Yes, if y = 0", "No, because 4(y + 1) = 5y"], "The 4 multiplies both terms.")
H('7.C', 4, "Which expression is NOT equivalent to 6a?", "a + 6", ["a × 6", "3a + 3a", "2a + 4a"], "a + 6 is not 6a (except at a = 1.2).")
H('7.C', 4, "Which expression is equivalent to 5n + 2n?", "7n", ["7n²", "10n", "n⁷"], "5n + 2n = 7n.")
# ================================================================ 7.D properties
H('7.D', 3, "Which property is shown: 8 + 3 = 3 + 8?", "commutative", ["associative", "distributive", "identity"], "Order changes but the sum is the same.")
H('7.D', 3, "Which property is shown: (2 + 3) + 4 = 2 + (3 + 4)?", "associative", ["commutative", "distributive", "inverse"], "Grouping changes but the sum is the same.")
H('7.D', 3, "Which property is shown: 7 × 1 = 7?", "identity", ["inverse", "commutative", "associative"], "Multiplying by 1 keeps the value.")
H('7.D', 3, "Which property is shown: 9 + (−9) = 0?", "inverse", ["identity", "distributive", "commutative"], "A number plus its opposite is 0.")
H('7.D', 4, "Which property is shown: 3(x + 5) = 3x + 15?", "distributive", ["commutative", "associative", "identity"], "3 is multiplied by each term inside the parentheses.")
# ================================================================ 8.A triangles
H('8.A', 2, "What is the sum of the angle measures in any triangle?", "180°", ["90°", "360°", "100°"], "Triangle angles add to 180°.")
def tri_angle():
    a = R.randint(30, 80); b = R.randint(30, 80); c = 180 - a - b
    if c < 20: return False
    return mk('8.A', 3, f"Two angles of a triangle measure {a}° and {b}°. What is the third angle?", f"{c}°", [f"{a + b}°", f"{360 - a - b}°", f"{c + 10}°"], f"180 − {a} − {b} = {c}.", f"'{c}°'")
rep(5, tri_angle)
H('8.A', 3, "Which sides can form a triangle?", "4, 5, 8", ["2, 3, 7", "1, 2, 5", "3, 3, 9"], "The two shorter sides must sum to more than the longest side: 4 + 5 > 8.")
H('8.A', 3, "Which sides CANNOT form a triangle?", "3, 4, 8", ["5, 6, 7", "4, 5, 8", "6, 6, 6"], "3 + 4 = 7 is less than 8.")
H('8.A', 3, "A triangle with three equal sides is called...", "equilateral", ["scalene", "right", "isosceles"], "Equilateral means all sides equal.")
H('8.A', 3, "A triangle with one 90° angle is called...", "a right triangle", ["an equilateral triangle", "an obtuse triangle", "a scalene triangle"], "A right triangle has one right angle.")
# ================================================================ 8.B model area formulas
H('8.B', 3, "A parallelogram can be cut and rearranged into a...", "rectangle", ["circle", "triangle", "hexagon"], "Cut off a right triangle and slide it to the other side.")
H('8.B', 4, "Two identical triangles can be joined to form a parallelogram. How does a triangle's area compare?", "It is half the area of the parallelogram", ["It is double", "It is the same", "It is a quarter"], "Two triangles make one parallelogram.")
H('8.B', 4, "Which formula gives the area of a triangle?", "A = ½bh", ["A = bh", "A = ½b + h", "A = 2bh"], "Half of base times height.")
H('8.B', 4, "A trapezoid can be decomposed into two triangles. Which formula follows?", "A = ½(b₁ + b₂)h", ["A = b₁b₂h", "A = (b₁ + b₂ + h)", "A = ½b₁h"], "The two triangles have bases b₁ and b₂, both with height h.")
H('8.B', 3, "Which formula gives the area of a parallelogram?", "A = bh", ["A = ½bh", "A = b + h", "A = 2b + 2h"], "Base times height.")
# ================================================================ 8.C equations for area
H('8.C', 4, "A rectangular garden is 12 ft long and w ft wide with area 84 ft². Which equation represents this?", "12w = 84", ["12 + w = 84", "w ÷ 12 = 84", "12 − w = 84"], "A = lw.")
H('8.C', 4, "A triangle has base 10 cm and height h cm. Its area is 35 cm². Which equation represents this?", "½ × 10 × h = 35", ["10h = 35", "10 + h = 35", "½ + 10h = 35"], "A = ½bh.")
H('8.C', 4, "A parallelogram has area 48 in² and height 6 in. If b is the base, which equation fits?", "6b = 48", ["6 + b = 48", "b ÷ 6 = 48", "48b = 6"], "A = bh.")
H('8.C', 4, "A trapezoid has bases 6 and 10 and area 40. Which equation finds the height h?", "½(6 + 10)h = 40", ["6 + 10 + h = 40", "(6)(10)h = 40", "½(6)(10) = h"], "A = ½(b₁ + b₂)h.")
# ================================================================ 8.D solve area problems
def tri_area():
    b = R.randint(4, 20); h = R.randint(3, 12)
    if (b * h) % 2: return False
    return mk('8.D', 3, f"What is the area of a triangle with base {b} cm and height {h} cm?", f"{b * h // 2} cm²", [f"{b * h} cm²", f"{b + h} cm²", f"{b * h // 2 + b} cm²"], f"½ × {b} × {h} = {b * h // 2}.", f"'{b*h//2} cm²'")
rep(5, tri_area)
def par_area():
    b = R.randint(4, 15); h = R.randint(3, 12)
    return mk('8.D', 3, f"A parallelogram has base {b} ft and height {h} ft. What is its area?", f"{b * h} ft²", [f"{b + h} ft²", f"{b * h // 2 if (b * h) % 2 == 0 else b * h + 1} ft²", f"{2 * (b + h)} ft²"], f"{b} × {h} = {b * h}.", f"'{b*h} ft²'")
rep(4, par_area)
def trap_area():
    b1 = R.randint(3, 10); b2 = b1 + R.randint(2, 8); h = R.randint(2, 8)
    if ((b1 + b2) * h) % 2: return False
    r = (b1 + b2) * h // 2
    return mk('8.D', 4, f"A trapezoid has bases {b1} m and {b2} m and height {h} m. What is its area?", f"{r} m²", [f"{b1 * b2 * h // 2 if (b1 * b2 * h) % 2 == 0 else b1 * b2 * h} m²", f"{(b1 + b2) * h} m²", f"{b1 + b2 + h} m²"], f"½({b1} + {b2}) × {h} = {r}.", f"'{r} m²'")
rep(4, trap_area)
H('8.D', 4, "A rectangle has area 96 cm² and width 8 cm. What is its length?", "12 cm", ["88 cm", "104 cm", "768 cm"], "96 ÷ 8 = 12.")
H('8.D', 4, "A triangular sail has area 30 ft² and base 10 ft. What is its height?", "6 ft", ["3 ft", "12 ft", "20 ft"], "½ × 10 × h = 30 gives h = 6.")
# ================================================================ 9.A write equations and inequalities
H('9.A', 3, "Ben has 14 stickers. After giving some away he has 9. Which equation shows this, with s the stickers given away?", "14 − s = 9", ["14 + s = 9", "s − 14 = 9", "14s = 9"], "14 minus given away equals 9.")
H('9.A', 3, "A bus holds at most 40 people. Which inequality shows the number of people p?", "p ≤ 40", ["p ≥ 40", "p < 40 only", "p > 40"], "At most means less than or equal to.")
H('9.A', 4, "You need at least 25 points to pass. Which inequality represents the points p?", "p ≥ 25", ["p ≤ 25", "p < 25", "p = 25"], "At least means greater than or equal to.")
H('9.A', 3, "Four friends share the cost equally, and each pays $9. Which equation shows the total cost t?", "t ÷ 4 = 9", ["t + 4 = 9", "4t = 9", "t − 4 = 9"], "Cost divided by 4 equals 9.")
H('9.A', 4, "A phone plan costs $5 plus $0.10 per text and must stay under $12. Which inequality fits, with t texts?", "5 + 0.10t < 12", ["5 − 0.10t < 12", "0.10t + 12 < 5", "5 × 0.10t < 12"], "Fixed fee plus per-text cost is less than 12.")
# ================================================================ 9.B number line solutions
H('9.B', 3, "How do you graph x > 4 on a number line?", "an open circle at 4 with an arrow to the right", ["a closed circle at 4 with an arrow to the right", "an open circle at 4 with an arrow to the left", "a closed circle at 4 with an arrow to the left"], "Greater than excludes 4 and goes right.")
H('9.B', 3, "How do you graph x ≤ 2 on a number line?", "a closed circle at 2 with an arrow to the left", ["an open circle at 2 with an arrow to the left", "a closed circle at 2 with an arrow to the right", "an open circle at 2 with an arrow to the right"], "Less than or equal includes 2 and goes left.")
H('9.B', 3, "The solution of x + 3 = 8 is graphed as a point at...", "5", ["3", "8", "11"], "x = 5.")
H('9.B', 4, "A number line shows a closed circle at 6 with an arrow to the right. Which inequality is graphed?", "x ≥ 6", ["x > 6", "x ≤ 6", "x < 6"], "Closed circle includes 6, arrow right means greater.")
H('9.B', 4, "A number line shows an open circle at −1 with an arrow to the left. Which inequality is graphed?", "x < −1", ["x ≤ −1", "x > −1", "x ≥ −1"], "Open circle excludes −1, arrow left means less.")
# ================================================================ 9.C write real-world problems
H('9.C', 4, "Which situation matches x + 6 = 15?", "A box holds some books; after adding 6 more there are 15", ["A box has 15 books and 6 are removed", "A box holds 6 groups of 15 books", "A box has 6 books and 15 are removed"], "Adding 6 more to x gives 15.")
H('9.C', 4, "Which situation matches 4n = 36?", "Four friends each collect n cards and have 36 in all", ["Four friends share 36 cards and have 4 left", "Someone has 36 cards and gets 4 more", "Four cards cost n dollars less than 36"], "4 groups of n make 36.")
H('9.C', 4, "Which situation matches x − 5 < 20?", "After spending $5, a student has less than $20", ["A student spends exactly $20", "A student has $5 more than $20", "A student saves at least $5"], "x − 5 is less than 20.")
H('9.C', 4, "Which situation matches y ÷ 3 = 8?", "A total is shared equally by 3 people and each gets 8", ["Three people each get 24", "A total is tripled to make 8", "Three more than a total is 8"], "Total divided by 3 is 8.")
# ================================================================ 10.A model and solve
def solve_add():
    x = R.randint(3, 30); a = R.randint(2, 25)
    return mk('10.A', 2, f"What is the solution of x + {a} = {x + a}?", f"x = {x}", [f"x = {x + 2 * a}", f"x = {x + a}", f"x = {a}"], f"Subtract {a} from both sides: {x + a} − {a} = {x}.", f"'x = {x}'")
rep(4, solve_add)
def solve_mul():
    x = R.randint(3, 15); a = R.randint(2, 9)
    return mk('10.A', 3, f"What is the solution of {a}x = {a * x}?", f"x = {x}", [f"x = {a * x - a}", f"x = {a * x * a}", f"x = {a}"], f"Divide both sides by {a}: {a * x} ÷ {a} = {x}.", f"'x = {x}'")
rep(4, solve_mul)
def solve_sub():
    x = R.randint(10, 40); a = R.randint(2, 9)
    return mk('10.A', 3, f"What is the solution of y − {a} = {x}?", f"y = {x + a}", [f"y = {x - a}", f"y = {a}", f"y = {x * a}"], f"Add {a} to both sides: {x} + {a} = {x + a}.", f"'y = {x + a}'")
rep(3, solve_sub)
H('10.A', 4, "What is the solution of n ÷ 4 = 7?", "n = 28", ["n = 3", "n = 11", "n = 1.75"], "Multiply both sides by 4.")
H('10.A', 4, "Which values of x make x + 5 > 12 true?", "x > 7", ["x < 7", "x > 17", "x < 17"], "Subtract 5 from both sides: x > 7.")
H('10.A', 4, "A rectangle has perimeter 30 and length 10. If w is the width, what is w?", "5", ["20", "10", "3"], "2(10 + w) = 30, so 10 + w = 15 and w = 5.")
# ================================================================ 10.B check solutions
H('10.B', 3, "Is x = 6 a solution of x + 4 = 10?", "Yes, because 6 + 4 = 10", ["No, because 6 + 4 = 12", "No, because 6 + 4 = 24", "Yes, because 6 − 4 = 10"], "Substitute 6 for x.")
H('10.B', 3, "Which value of n makes 3n = 21 true?", "7", ["6", "8", "18"], "3 × 7 = 21.")
H('10.B', 3, "Which value of x makes x − 4 < 3 true?", "x = 5", ["x = 7", "x = 8", "x = 10"], "5 − 4 = 1 < 3.")
H('10.B', 4, "Which values make y ≥ 9 true?", "9 and 12", ["8 and 9", "7 and 8", "6 and 10"], "9 and 12 are at least 9.")
H('10.B', 4, "Which value is NOT a solution of 2x + 1 = 11?", "x = 4", ["x = 5", "x = 5.0", "x = 10 ÷ 2"], "2(4) + 1 = 9, not 11.")

# ================================================================ 11 coordinate geometry
H('11', 2, "In the ordered pair (4, 7), which number is the x-coordinate?", "4", ["7", "11", "3"], "The x-coordinate comes first.")
H('11', 3, "Which point is in Quadrant II?", "(−3, 5)", ["(3, 5)", "(−3, −5)", "(3, −5)"], "Quadrant II has a negative x and a positive y.")
H('11', 3, "Which point is in Quadrant III?", "(−2, −6)", ["(2, 6)", "(−2, 6)", "(2, −6)"], "Both coordinates are negative.")
H('11', 3, "Point A is at (2, 3) and point B is at (2, 8). How far apart are they?", "5 units", ["6 units", "10 units", "11 units"], "They share an x-coordinate, so subtract the y-values: 8 − 3 = 5.")
H('11', 4, "A rectangle has vertices at (1, 1), (6, 1), (6, 4) and (1, 4). What is its perimeter?", "16 units", ["15 units", "8 units", "30 units"], "Length 5 and width 3: 2(5 + 3) = 16.")
H('11', 4, "A rectangle has vertices at (0, 0), (4, 0), (4, 3) and (0, 3). What is its area?", "12 square units", ["7 square units", "14 square units", "24 square units"], "4 × 3 = 12.")
H('11', 3, "Which point lies on the x-axis?", "(5, 0)", ["(0, 5)", "(5, 5)", "(−5, 5)"], "On the x-axis, y = 0.")
H('11', 3, "Which point lies on the y-axis?", "(0, −4)", ["(−4, 0)", "(4, 4)", "(4, −4)"], "On the y-axis, x = 0.")
# ================================================================ 12.A graphs of numeric data
H('12.A', 2, "Which graph shows each data value as a dot above a number line?", "dot plot", ["histogram", "box plot", "stem-and-leaf plot"], "A dot plot uses dots over a number line.")
H('12.A', 3, "A stem-and-leaf plot shows stem 3 with leaves 2, 5, 5. What data values does this represent?", "32, 35, 35", ["3, 2, 5, 5", "325", "8, 5, 5"], "The stem is the tens digit and each leaf is a ones digit.")
H('12.A', 3, "Which graph uses bars with no gaps to show how many values fall within intervals?", "histogram", ["dot plot", "stem-and-leaf plot", "bar graph with gaps"], "Histograms group numeric data into intervals.")
H('12.A', 4, "Which five numbers are needed to draw a box plot?", "minimum, Q1, median, Q3, maximum", ["mean, mode, range, minimum, maximum", "sum, count, mean, mode, range", "minimum, mean, median, mode, maximum"], "A box plot uses the five-number summary.")
H('12.A', 3, "A dot plot has 4 dots above 7. What does this tell you?", "The value 7 appears 4 times", ["The value 4 appears 7 times", "The mean is 7", "There are 7 data values"], "Each dot is one data value.")
# ================================================================ 12.B center, spread, shape
H('12.B', 3, "A dot plot has most dots at the right and a long tail on the left. How is the shape described?", "skewed left", ["skewed right", "symmetric", "uniform"], "The tail points to the left.")
H('12.B', 3, "A histogram is mirror-image on both sides of its center. The shape is...", "symmetric", ["skewed left", "skewed right", "bimodal only"], "Symmetric means the sides match.")
H('12.B', 4, "Data: 2, 2, 3, 3, 3, 4, 4. Which describes the center?", "around 3", ["around 7", "around 1", "around 10"], "Most values cluster at 3.")
H('12.B', 4, "Which data set has the greatest spread?", "10, 30, 50, 70", ["50, 51, 52, 53", "20, 21, 22, 23", "9, 9, 10, 10"], "Its values are the farthest apart.")
# ================================================================ 12.C mean, median, range, IQR
def mean_q():
    n = R.randint(4, 6); m = R.randint(5, 20); d = [R.randint(-4, 4) for _ in range(n - 1)]; d.append(-sum(d))
    vals = [m + x for x in d]
    if len(set(vals)) < 3 or min(vals) < 1: return False
    R.shuffle(vals)
    return mk('12.C', 3, f"What is the mean of {', '.join(map(str, vals))}?", str(m), [str(m + 1), str(m - 1), str(max(vals))], f"The sum is {sum(vals)}; {sum(vals)} ÷ {n} = {m}.", f"str({m})")
rep(5, mean_q)
def median_q():
    n = R.choice([5, 7]); vals = sorted(R.sample(range(2, 40), n)); med = vals[n // 2]
    shown = vals[:]; R.shuffle(shown)
    return mk('12.C', 3, f"What is the median of {', '.join(map(str, shown))}?", str(med), [str(vals[0]), str(vals[-1]), str(sum(vals) // n)], f"Order the values; the middle one is {med}.", f"str({med})")
rep(5, median_q)
def range_q():
    n = R.randint(5, 7); vals = R.sample(range(1, 60), n); r = max(vals) - min(vals)
    return mk('12.C', 2, f"What is the range of {', '.join(map(str, vals))}?", str(r), [str(max(vals)), str(r + 2), str(max(vals) + min(vals))], f"{max(vals)} − {min(vals)} = {r}.", f"str({r})")
rep(4, range_q)
H('12.C', 3, "Data: 4, 6, 8, 10, 12, 14, 16. What is the median?", "10", ["12", "8", "9"], "The middle value is 10.")
H('12.C', 4, "Q1 = 12 and Q3 = 20. What is the interquartile range (IQR)?", "8", ["32", "16", "4"], "20 − 12 = 8.")
H('12.C', 4, "What does the mean absolute deviation (MAD) measure?", "the average distance of values from the mean", ["the middle value", "the most common value", "the difference of largest and smallest"], "MAD is a measure of spread.")
H('12.C', 4, "Data: 3, 5, 5, 7, 20. Which measure of center is least affected by the 20?", "median", ["mean", "range", "sum"], "Extreme values pull the mean but not the median.")
# ================================================================ 12.D categorical data
H('12.D', 2, "In a lunch survey, 10 students chose pizza, 6 chose tacos, and 4 chose salad. The mode is the category with the...", "greatest number of votes", ["least number of votes", "average number of votes", "total of all votes"], "The mode is the most frequent category, pizza.")
H('12.D', 3, "In a survey of 20 students, 5 chose cats. What percent chose cats?", "25%", ["5%", "15%", "20%"], "5/20 = 25%.")
H('12.D', 3, "Which graph is best for showing the percent of values in each category?", "a pie or bar graph", ["a box plot", "a stem-and-leaf plot", "a dot plot only"], "Categorical data can be shown in bar or pie graphs.")
H('12.D', 3, "A bar graph shows colors of cars: red 8, blue 12, white 20. How many cars are in the sample?", "40", ["20", "12", "24"], "8 + 12 + 20 = 40.")
H('12.D', 4, "A class has 10 cat owners out of 25 students. What percent of the class owns cats?", "40%", ["10%", "25%", "35%"], "10/25 = 40%.")
# ================================================================ 13.A interpret numeric data
H('13.A', 3, "A box plot has median 40, Q1 = 30, Q3 = 55. What does the box show?", "the middle half of the data, from 30 to 55", ["all the data", "the top quarter only", "the mean"], "The box spans Q1 to Q3.")
H('13.A', 3, "A histogram shows the tallest bar for the interval 10–19. What does that mean?", "More values fall in 10–19 than in any other interval", ["The mean is 15", "Exactly 19 values were collected", "Nothing is in the other intervals"], "The tallest bar has the most data.")
H('13.A', 4, "A stem-and-leaf plot has stems 1, 2, 3 and most leaves on stem 2. What does this suggest?", "most values are in the 20s", ["most values are 2", "most values are 20", "there are no values in the 30s"], "Stem 2 means the twenties.")
H('13.A', 4, "A dot plot of quiz scores has a gap between 6 and 9. What does the gap tell you?", "no student scored 7 or 8", ["all students scored 7", "the mean is 7.5", "one student scored 6 and 9"], "A gap shows no values.")
H('13.A', 4, "A box plot shows a median much closer to Q1 than Q3. What can you say about the data?", "the upper half is more spread out than the lower half", ["the data are symmetric", "the mean is exactly the median", "there is no spread"], "The longer part of the box shows more spread.")
# ================================================================ 13.B variability
H('13.B', 3, "Which situation yields data with variability?", "the heights of students in a class", ["the number of days in a week", "the number of sides on a square", "the number of minutes in an hour"], "Heights vary from student to student.")
H('13.B', 3, "Which situation yields data WITHOUT variability?", "the number of legs on each chair in a classroom of 4-legged chairs", ["the shoe sizes in a classroom", "the ages of students", "the amount of rainfall each day"], "Every chair has the same number of legs.")
H('13.B', 3, "Which question is statistical, with answers that vary?", "How many pets does each student own?", ["How many days are in a week?", "What is 5 + 3?", "How many inches are in a foot?"], "Answers differ from student to student.")
H('13.B', 4, "Which question is NOT a statistical question?", "How many students are in room 12 today?", ["How many hours do students sleep?", "How tall are sixth graders?", "What are the students' favorite sports?"], "It has one fixed answer.")
# ================================================================ 14 personal financial literacy
H('14.A', 3, "Which feature is typical of a checking account?", "you can write checks and use a debit card", ["it earns a high interest rate for long-term savings", "you borrow money and pay interest", "it has a credit limit"], "Checking accounts are for everyday spending.")
H('14.A', 3, "When comparing checking accounts, which cost should you check?", "monthly fees", ["the bank's color", "the number of tellers", "the name of the president"], "Fees change the cost of an account.")
H('14.B', 3, "A debit card takes money from...", "your own bank account", ["a loan from the bank", "a credit limit", "the store's account"], "Debit spends money you already have.")
H('14.B', 3, "A credit card lets you...", "borrow money that must be repaid", ["spend only money in your account", "never pay interest", "get free money"], "Credit is a loan.")
H('14.B', 4, "Which is a key difference between debit and credit cards?", "Credit cards can create debt; debit cards use your own funds", ["Debit cards charge interest each month", "Credit cards are always free", "Debit cards have a credit limit"], "Credit means borrowing.")
def check_reg():
    s = R.randint(100, 400); d = R.randint(20, 150); w = R.randint(10, 80)
    return mk('14.C', 3, f"A check register starts with ${s}. A deposit of ${d} is made and a withdrawal of ${w} is made. What is the new balance?", f"${s + d - w}", [f"${s + d + w}", f"${s - d + w}", f"${s - d - w}"], f"{s} + {d} − {w} = {s + d - w}.", f"'${s + d - w}'")
rep(4, check_reg)
H('14.C', 4, "A transfer moves $50 from savings to checking. What happens to the checking balance?", "it increases by $50", ["it decreases by $50", "it stays the same", "it doubles"], "Money transferred in increases that account.")
H('14.D', 3, "Why is a positive credit history important?", "it helps you qualify for loans with better terms", ["it gives you free money", "it removes all debt", "it guarantees a job"], "Lenders use credit history to decide.")
H('14.D', 3, "Which habit helps build a positive credit history?", "paying bills on time", ["missing payments", "ignoring statements", "borrowing without repaying"], "On-time payments build trust.")
H('14.E', 3, "A credit report lists...", "your accounts and your payment history", ["your favorite stores", "your grades", "your medical records"], "It records credit accounts and payments.")
H('14.E', 4, "How long can most negative information stay on a credit report?", "about 7 years", ["1 week", "about 30 days", "forever, always"], "Many negative items remain for about 7 years.")
H('14.F', 3, "Lenders use credit reports to decide...", "whether to lend money", ["what to wear", "how tall you are", "which school you attend"], "Credit reports show borrowing behavior.")
H('14.F', 4, "A borrower benefits from checking their credit report because they can...", "find and correct errors", ["avoid all payments", "erase real debts", "raise their income"], "Mistakes can hurt a score.")
H('14.G', 3, "Which payment for college does NOT have to be paid back?", "a scholarship", ["a student loan", "a credit card balance", "a car loan"], "Scholarships and grants are gifts.")
H('14.G', 3, "Which is a way to pay for college?", "savings, grants, scholarships, student loans, or work-study", ["lottery winnings only", "skipping tuition", "borrowing from no one"], "Many sources can combine.")
H('14.G', 4, "A student loan is different from a grant because a loan...", "must be repaid, often with interest", ["is never paid back", "has no interest", "is given only for sports"], "Loans are borrowed money.")
H('14.H', 3, "Which usually leads to a higher annual salary?", "more education or training", ["less education", "no training", "skipping school"], "Education usually raises earning potential.")
H('14.H', 4, "A job pays $18 per hour for 40 hours per week for 50 weeks. What is the annual pay?", "$36,000", ["$7,200", "$3,600", "$900"], "18 × 40 × 50 = 36,000.")
H('14.H', 4, "A vocational program costs $8,000 and leads to a job paying $42,000 per year. A job with no training pays $28,000. How much more does the trained worker earn each year?", "$14,000", ["$20,000", "$70,000", "$8,000"], "42,000 − 28,000 = 14,000.")

# --- END
B.balance() if hasattr(B,"balance") and False else None
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "batches", "g6_math.jsonl"))
print("saved", len(B.out), "questions")

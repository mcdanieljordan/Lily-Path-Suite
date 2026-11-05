#!/usr/bin/env python3
"""Grade 3 Mathematics (TEKS 111.5.b) - original questions. Run: python3 gen/g3_math.py  -> batches/g3_math.jsonl"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from fractions import Fraction as F

B = Bank('111.5.b.', 303)
R, mk, H, rep = B.R, B.mk, B.hand, B.rep
DEN = [2, 3, 4, 6, 8]
ORD = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh'}

# ---------------------------------------------------------------- strand 2: place value
def g2A_compose():
    ds = R.sample(range(1, 10), 5); t, th, h, te, o = ds
    n = int(''.join(map(str, ds))); wr = []
    for i in R.sample(range(4), 3):
        d2 = ds[:]; d2[i], d2[i + 1] = d2[i + 1], d2[i]; wr.append(cm(int(''.join(map(str, d2)))))
    return mk('2.A', R.choice([2, 3]), f"Which number is {pl(t,'ten thousand')}, {pl(th,'thousand')}, {pl(h,'hundred')}, {pl(te,'ten')}, and {pl(o,'one')}?",
              cm(n), wr, f"Put each digit in its place: {cm(n)}.", CK(f"{t}*10000+{th}*1000+{h}*100+{te}*10+{o}"))

def g2A_sum():
    ds = R.sample(range(1, 10), 5); n = int(''.join(map(str, ds)))
    terms = [ds[i] * 10 ** (4 - i) for i in range(5)]
    right = ' + '.join(cm(x) for x in terms); wr = []
    for i in R.sample(range(5), 3):
        t2 = terms[:]; t2[i] = ds[i] * 10 ** (4 - i - 1) if i < 4 else ds[i] * 10
        wr.append(' + '.join(cm(x) for x in t2))
    return mk('2.A', 3, f"Which shows {cm(n)} written as a sum of its place values?", right, wr,
              "Each digit is multiplied by the value of its place, then the parts are added.")

def g2A_zero():
    t, h, o = R.sample(range(1, 10), 3); n = t * 10000 + h * 100 + o
    wr = [int(f"{t}{h}{o}"), t * 10000 + h * 1000 + o, t * 10000 + h * 100 + o * 10, t * 1000 + h * 100 + o]
    return mk('2.A', 3, f"A number has {pl(t,'ten thousand')}, {pl(h,'hundred')}, and {pl(o,'one')}. It has no thousands and no tens. What is the number?",
              cm(n), [cm(w) for w in wr], "Use a zero as a placeholder in the empty thousands and tens places.", CK(f"{t}*10000+{h}*100+{o}"))

def g2B_value():
    ds = R.sample(range(1, 10), 5); i = R.randrange(5); d = ds[i]; n = int(''.join(map(str, ds)))
    names = {4: 'ones', 3: 'tens', 2: 'hundreds', 1: 'thousands', 0: 'ten thousands'}
    wr = [cm(d * 10 ** k) for k in range(5) if k != 4 - i]
    return mk('2.B', 2 if i >= 2 else 3, f"In the number {cm(n)}, what is the value of the digit {d}?", cm(d * 10 ** (4 - i)), wr,
              f"The {d} is in the {names[i][:-1] if names[i]!='ones' else 'ones'} place, so its value is {cm(d * 10 ** (4 - i))}.", CK(f"{d}*{10 ** (4 - i)}"))

def g2B_ratio():
    a = R.randint(2, 4); b = R.randint(1, a - 1); d = R.randint(2, 9)
    return mk('2.B', 4, f"The digit {d} in {cm(d * 10 ** a)} has a value that is how many times the value of the digit {d} in {cm(d * 10 ** b)}?",
              cm(10 ** (a - b)), [cm(x) for x in (10, 100, 1000, 10000)], f"Each place to the left is worth 10 times as much; {a - b} place(s) apart is {cm(10 ** (a - b))} times.", CK(f"10**{a - b}"))

PL = ['one', 'ten', 'hundred', 'thousand', 'ten thousand', 'hundred thousand']
def g2B_make():
    i = R.randint(0, 3); j = i + R.randint(1, 3)
    if j > 5: return False
    return mk('2.B', 2 if j - i == 1 else 3, f"How many {PL[i]}s make 1 {PL[j]}?",
              cm(10 ** (j - i)), [cm(x) for x in (10, 100, 1000, 10000)], f"Each place is 10 times the place to its right, so {j - i} step(s) is {cm(10 ** (j - i))}.", CK(f"10**{j - i}"))

# ---------------------------------------------------------------- 2.C number line / between multiples
def g2C_between():
    u = R.choice([10, 100, 1000, 10000]); lo, hi = {10: (11, 99), 100: (101, 999), 1000: (1001, 9999), 10000: (10001, 99999)}[u]
    n = R.randint(lo, hi)
    if n % u == 0: return False
    low = n // u * u
    right = f"{cm(low)} and {cm(low + u)}"
    wr = [f"{cm(low + u)} and {cm(low + 2 * u)}", f"{cm(low + 2 * u)} and {cm(low + 3 * u)}"]
    wr.append(f"{cm(low - u)} and {cm(low)}" if low - u >= 0 else f"{cm(low + 3 * u)} and {cm(low + 4 * u)}")
    return mk('2.C', 2 if u <= 100 else 3, f"On a number line, {cm(n)} is between which two consecutive multiples of {cm(u)}?", right, wr,
              f"{cm(low)} ≤ {cm(n)} < {cm(low + u)}, and these are neighbors in the count by {cm(u)}s.")

def g2C_closest():
    u = R.choice([10, 100, 1000]); lo, hi = {10: (11, 99), 100: (101, 999), 1000: (1001, 9999)}[u]
    n = R.randint(lo, hi); r = n % u
    if r == 0 or abs(r - u / 2) < u * 0.08: return False
    low = n // u * u; right = low if r < u / 2 else low + u; other = low + u if right == low else low
    wr = [other, right - u if right - u > 0 else right + 2 * u, other + u if other > right else other - u if other - u > 0 else other + 2 * u]
    return mk('2.C', 3, f"Which multiple of {cm(u)} is closest to {cm(n)}?", cm(right), [cm(w) for w in wr],
              f"{cm(n)} is between {cm(low)} and {cm(low + u)} and is closer to {cm(right)}.", CK(f"({n}+{u // 2})//{u}*{u}"))

# ---------------------------------------------------------------- 2.D compare / order
LT, GT, EQ = "less than (<)", "greater than (>)", "equal to (=)"
def g2D_symbol():
    k = R.choice([0, 1, 2])
    if k == 0:
        a = R.randint(10000, 99999); s = list(str(a)); i = R.randint(1, 4); s[i] = str((int(s[i]) + R.randint(1, 8)) % 10); b = int(''.join(s))
        if a == b: return False
    elif k == 1:
        a = R.randint(1000, 9999); b = R.randint(10000, 40000)
        if R.random() < .5: a, b = b, a
    else:
        ds = R.sample(range(1, 10), 4); a = int(''.join(map(str, ds))); ds2 = ds[:]; ds2[2], ds2[3] = ds2[3], ds2[2]; b = int(''.join(map(str, ds2)))
    right = LT if a < b else GT if a > b else EQ
    return mk('2.D', 2 if k == 1 else 3, f"Which symbol makes this statement true?  {cm(a)} ___ {cm(b)}", right, [LT, GT, EQ],
              f"Compare from the greatest place value. {cm(a)} is {'less than' if a < b else 'greater than'} {cm(b)}.", need=2)

def g2D_equal():
    ds = R.sample(range(1, 10), 4); n = int(''.join(map(str, ds)))
    s = f"{cm(ds[0]*1000)} + {cm(ds[1]*100)} + {ds[2]*10} + {ds[3]}"
    s_bad = f"{cm(ds[0]*1000)} + {cm(ds[1]*100)} + {ds[2]} + {ds[3]*10}"
    from_bad = int(ds[0] * 1000 + ds[1] * 100 + ds[2] + ds[3] * 10)
    return mk('2.D', 4, f"Which symbol makes this statement true?  {cm(n)} ___ {s_bad}", GT if n > from_bad else LT, [LT, GT, EQ],
              f"Add the right side: {cm(ds[0]*1000)} + {cm(ds[1]*100)} + {ds[2]} + {ds[3]*10} = {cm(from_bad)}. Compare that with {cm(n)}.", need=2)

def g2D_order():
    base = R.randint(10, 90) * 1000; ns = R.sample([base + R.randint(0, 9) * 100 + R.randint(0, 9) * 10 + R.randint(0, 9) for _ in range(12)], 3)
    if len(set(ns)) < 3: return False
    asc = sorted(ns); up = R.random() < .6; ans = asc if up else asc[::-1]
    wr = [ans[::-1], [ans[1], ans[0], ans[2]], [ans[0], ans[2], ans[1]]]
    f = lambda l: ', '.join(cm(x) for x in l)
    return mk('2.D', 3, f"Which list shows the numbers in order from {'least to greatest' if up else 'greatest to least'}?", f(ans), [f(w) for w in wr],
              "Compare the digits from the left, starting with the greatest place value.")

def g2D_extreme():
    lead = R.randint(2, 8) * 10000; ns = [lead + R.choice([0, 1000, 2000, 3000]) + R.choice([0, 100, 200, 300, 400]) + R.randrange(0, 90, 10) for _ in range(6)]
    ns = list(dict.fromkeys(ns))[:4]
    if len(ns) < 4: return False
    big = R.random() < .5; ans = max(ns) if big else min(ns)
    return mk('2.D', 3, f"Which is the {'greatest' if big else 'least'} number?  " + ',  '.join(cm(x) for x in ns), cm(ans), [cm(x) for x in ns],
              "Line up the digits by place value and compare from the left.")

# ---------------------------------------------------------------- strand 3 fractions
OBJ = [("pizza", "slices", "eaten"), ("chocolate bar", "pieces", "eaten"), ("rectangle", "parts", "shaded"), ("garden", "sections", "planted with tomatoes"),
       ("ribbon", "pieces", "painted blue"), ("fraction strip", "parts", "shaded"), ("pie", "slices", "eaten"), ("banner", "sections", "colored red")]
def g3A():
    o, part, pp = R.choice(OBJ); b = R.choice(DEN); a = R.randint(1, b) if R.random() < .12 else R.randint(1, b - 1)
    wr = [f"{b - a}/{b}", f"{b}/{a}", f"{a}/{b + 2}", f"{a + 1}/{b}", f"{a}/{b - a}" if b - a > 0 else f"{a}/{b+1}"]
    return mk('3.A', 2, f"A {o} is split into {b} equal {part}. {a} of the {part} {'is' if a == 1 else 'are'} {pp}. What fraction of the {o} is {pp}?", f"{a}/{b}", wr,
              f"{a} out of {b} equal parts is {a}/{b}.")

def g3B_right():
    b = R.choice(DEN); m = R.randint(1, b - 1)
    wr = [f"{b - m}/{b}", f"{b}/{m}", f"{m + 1}/{b}", f"{m}/{b + 2}", f"{m}/{m + 1}"]
    return mk('3.B', 2, f"A number line from 0 to 1 is split into {b} equal parts. A point is {m} mark{'s' if m > 1 else ''} to the right of 0. Which fraction names the point?", f"{m}/{b}", wr,
              f"Each part is 1/{b}. {m} parts from 0 is {m}/{b}.")

def g3B_left():
    b = R.choice(DEN); k = R.randint(1, b - 1)
    wr = [f"{k}/{b}", f"{b - k}/{k}", f"{b - k + 1}/{b}", f"{b}/{b - k}", f"{b - k}/{b + 2}"]
    return mk('3.B', 3, f"A number line from 0 to 1 is split into {b} equal parts. A point is {k} mark{'s' if k > 1 else ''} to the left of 1. Which fraction names the point?", f"{b - k}/{b}", wr,
              f"Going back {k} part(s) from {b}/{b} leaves {b - k}/{b}.")

def g3C_unit():
    b = R.choice(DEN)
    wr = [f"{b}/1", f"1/{b + 1}", f"1/{b - 1}", f"{b - 1}/{b}"]
    return mk('3.C', 2, f"A whole is partitioned into {b} equal parts. Which fraction names exactly one of those parts?", f"1/{b}", wr,
              f"One part out of {b} equal parts is the unit fraction 1/{b}.")

def g3D_sum():
    b = R.choice([4, 6, 8]); a = R.randint(2, b - 1)
    ks = [k for k in range(2, 9) if k != a]
    wr = [' + '.join([f"1/{b}"] * k) for k in R.sample(ks, 3)]
    return mk('3.D', 3, f"Which sum is equal to {a}/{b}?", ' + '.join([f"1/{b}"] * a), wr, f"{a}/{b} is {a} parts that are each 1/{b}.")

def g3D_fraction():
    b = R.choice([3, 4, 6, 8]); a = R.randint(2, b)
    wr = [f"1/{a}", f"{b}/{a}", f"{a}/{b * 2}", f"{a + 1}/{b}", f"1/{b}"]
    return mk('3.D', 3, "Which fraction is equal to " + ' + '.join([f"1/{b}"] * a) + "?", f"{a}/{b}", wr, f"Adding {a} parts of size 1/{b} gives {a}/{b}.")

def g3E_kids():
    k = R.choice(DEN); thing = R.choice(["pizza", "sandwich", "ribbon", "candy bar", "pan of cornbread"])
    names = {2: 'two', 3: 'three', 4: 'four', 6: 'six', 8: 'eight'}
    wr = [f"{k}/1", f"1/{k + 1}", f"1/{k + 2}", f"{k - 1}/{k}"]
    return mk('3.E', 2, f"{names[k].capitalize()} friends share 1 {thing} equally. What fraction of the {thing} does each friend get?", f"1/{k}", wr,
              f"The {thing} is cut into {k} equal shares, so each share is 1/{k}.")

def g3E_set():
    k = R.choice([2, 3, 4, 6]); n = k * R.randint(2, 4); thing = R.choice(["stickers", "crayons", "marbles", "cards"])
    wr = [f"{k}/{n}", f"1/{n}", f"{n}/{k}", f"1/{k + 1}"]
    return mk('3.E', 3, f"{n} {thing} are shared equally among {k} children. What fraction of the {thing} does each child get?", f"1/{k}", wr,
              f"Each of the {k} children gets 1 of {k} equal shares, which is 1/{k}.")

def g3E_items():
    j, k = R.choice([(2, 4), (3, 6), (2, 6), (4, 8), (2, 8), (3, 4), (3, 8), (2, 3)]); fr = F(j, k)
    thing, one = R.choice([("sandwiches", "sandwich"), ("pizzas", "pizza"), ("ribbons", "ribbon"), ("pans of lasagna", "pan of lasagna")])
    right = f"{fr.numerator}/{fr.denominator}"
    wr = [f"{k}/{j}", f"1/{k}", f"{j + 1}/{k}", f"{j}/{k + 2}", f"{k - j}/{k}"]
    return mk('3.E', 4, f"{j} {thing} are shared equally by {k} people. What fraction of one {one} does each person get?", right, wr,
              f"{j} wholes shared by {k} people is {j}/{k}" + (f", which is {right}." if right != f"{j}/{k}" else "."))

EQV = {(1, 2): [(2, 4), (3, 6), (4, 8)], (1, 3): [(2, 6)], (1, 4): [(2, 8)], (2, 3): [(4, 6)], (3, 4): [(6, 8)], (2, 4): [(1, 2)], (2, 6): [(1, 3)], (4, 6): [(2, 3)], (6, 8): [(3, 4)], (3, 6): [(1, 2)], (4, 8): [(1, 2)], (2, 8): [(1, 4)]}
ALLF = [(a, b) for b in DEN for a in range(1, b)]
def g3F():
    (a, b) = R.choice(list(EQV)); (c, d) = R.choice(EQV[(a, b)])
    wr = [f"{x}/{y}" for (x, y) in R.sample(ALLF, len(ALLF)) if F(x, y) != F(a, b)][:6]
    if R.random() < .5:
        q = f"Which fraction is equivalent to {a}/{b}?"
    else:
        q = f"Which fraction names the same point on a number line as {a}/{b}?"
    return mk('3.F', 3, q, f"{c}/{d}", wr, f"{a}/{b} and {c}/{d} show the same amount of the same-size whole.")

def g3H_den():
    b = R.choice([4, 6, 8]); x, y = R.sample(range(1, b), 2) if b > 2 else (1, 2)
    right = LT if x < y else GT
    return mk('3.H', 2, f"Which symbol makes this statement true?  {x}/{b} ___ {y}/{b}", right, [LT, GT, EQ], "The wholes are split into the same number of equal parts, so compare how many parts there are.", need=2)

def g3H_num():
    a = R.randint(1, 3); d1, d2 = R.sample([x for x in DEN if x > a], 2)
    right = GT if d1 < d2 else LT
    return mk('3.H', 3, f"Which symbol makes this statement true?  {a}/{d1} ___ {a}/{d2}", right, [LT, GT, EQ], "With the same numerator, the fraction with the smaller denominator has larger pieces, so it is greater.", need=2)

def g3H_extreme():
    ds = R.sample(DEN, 4); big = R.random() < .5
    ans = min(ds) if big else max(ds)
    return mk('3.H', 3, f"Which fraction is {'greatest' if big else 'least'}?  " + ',  '.join(f"1/{d}" for d in ds), f"1/{ans}", [f"1/{d}" for d in ds],
              "When the numerators are equal, a smaller denominator means larger equal parts.")

# ---------------------------------------------------------------- strand 4
def g4A_add():
    a = R.randint(120, 690); b = R.randint(110, 999 - a); thing = R.choice([("books", "A library has {a} picture books and {b} chapter books. How many books does it have in all?"),
        ("stickers", "Kai has {a} stickers. His sister gives him {b} more. How many stickers does Kai have now?"), ("tickets", "A school sold {a} tickets on Friday and {b} tickets on Saturday. How many tickets were sold in all?")])
    s = a + b
    return mk('4.A', 2, thing[1].format(a=a, b=b), s, [s + 10, s - 10, s + 100, s - 100, abs(a - b)], f"{a} + {b} = {s}.", CS(f"{a}+{b}"))

def g4A_sub():
    a = R.randint(400, 990); b = R.randint(130, a - 120); s = a - b
    t = R.choice(["A farm stand had {a} apples. It sold {b} apples. How many apples are left?", "A bus route is {a} miles long. The bus has gone {b} miles. How many miles are left?", "There were {a} students at a game. {b} students went home. How many students stayed?"])
    return mk('4.A', 2, t.format(a=a, b=b), s, [s + 10, s - 10, s + 100, s - 100, a + b], f"{a} − {b} = {s}.", CS(f"{a}-{b}"))

def g4A_two():
    a = R.randint(150, 450); b = R.randint(120, 400); c = R.randint(60, a + b - 100); s = a + b - c
    t = R.choice(["A store had {a} red pens and {b} blue pens. It sold {c} pens. How many pens are left?", "Rosa read {a} pages last week and {b} pages this week. She needs to read {c} more pages to finish the book. How many pages are in the book?"])
    if t.startswith("Rosa"):
        s = a + b + c; wr = [a + b - c, s + 10, s - 10, a + b]
        return mk('4.A', 4, t.format(a=a, b=b, c=c), s, wr, f"{a} + {b} + {c} = {s}.", CS(f"{a}+{b}+{c}"))
    return mk('4.A', 4, t.format(a=a, b=b, c=c), s, [a + b + c, s + 10, s - 10, a - b - c if a - b - c > 0 else s + 100, s + 100], f"({a} + {b}) − {c} = {s}.", CS(f"{a}+{b}-{c}"))

def g4B_round():
    u = R.choice([10, 100]); n = R.randint(105, 989)
    if n % u == 0: return False
    right = (n + u // 2) // u * u; low = n // u * u
    wr = [low if right != low else low + u, right + u, right - u, (n + 50) // 100 * 100 if u == 10 else (n + 5) // 10 * 10]
    return mk('4.B', 2, f"What is {n} rounded to the nearest {u}?", right, wr, f"Look at the digit to the right of the {('tens' if u == 10 else 'hundreds')} place; 5 or more rounds up.", CS(f"({n}+{u // 2})//{u}*{u}"))

def g4B_est():
    a = R.randint(210, 790); b = R.randint(110, 690); op = R.choice(['+', '-']); u = R.choice([100, 10])
    if op == '-' and a < b: a, b = b, a
    ra, rb = (a + u // 2) // u * u, (b + u // 2) // u * u; est = ra + rb if op == '+' else ra - rb; exact = a + b if op == '+' else a - b
    if est == exact or est <= 0: return False
    wr = [exact, est + u, est - u if est - u > 0 else est + 2 * u, est + 2 * u]
    return mk('4.B', 3, f"Estimate {a} {op.replace('-', '−')} {b} by rounding each number to the nearest {u}. What is the estimate?", est, wr,
              f"{a} rounds to {ra} and {b} rounds to {rb}; {ra} {op.replace('-', '−')} {rb} = {est}.", CS(f"{ra}{op}{rb}"))

COIN = [("quarter", 25), ("dime", 10), ("nickel", 5), ("penny", 1)]
def g4C():
    k = R.choice([0, 1])
    if k == 0:
        picks = R.sample(COIN, R.choice([2, 3])); parts = []; expr = []; tot = 0
        for nm, v in picks:
            c = R.randint(1, 4) if nm != "penny" else R.randint(2, 6); parts.append(f"{c} {nm if c == 1 else ('pennies' if nm == 'penny' else nm + 's')}"); expr.append(f"{c}*{v}"); tot += c * v
        if tot > 140: return False
        txt = ", ".join(parts[:-1]) + (", and " if len(parts) > 2 else " and ") + parts[-1]
        wr = [tot + 5, tot - 5 if tot > 5 else tot + 15, tot + 10, tot + 25, tot - 10 if tot > 10 else tot + 30]
        return mk('4.C', 2, f"Ava has {txt}. How much money does Ava have?", money(tot), [money(w) for w in wr], f"Add the values: {' + '.join(x.replace('*', ' × ') for x in expr)} cents = {tot} cents.", mchk("+".join(expr), tot))
    bill = R.choice([("$1 bill", 100), ("$5 bill", 500), ("$10 bill", 1000)]); nb = R.randint(1, 2); picks = R.sample(COIN[:3], 2)
    c1, c2 = R.randint(1, 3), R.randint(1, 3); tot = nb * bill[1] + c1 * picks[0][1] + c2 * picks[1][1]
    parts = f"{nb} {bill[0]}{'s' if nb > 1 else ''}, {c1} {picks[0][0]}{'s' if c1 > 1 else ''}, and {c2} {picks[1][0]}{'s' if c2 > 1 else ''}"
    wr = [tot + 5, tot - 5, tot + 10, tot + 25, tot - 25]
    return mk('4.C', 3, f"Noah has {parts}. How much money does Noah have?", money(tot), [money(w) for w in wr],
              f"Bills: ${nb * bill[1] // 100}. Coins: {c1 * picks[0][1] + c2 * picks[1][1]} cents. Total {money(tot)}.", mchk(f"{nb * bill[1]}+{c1}*{picks[0][1]}+{c2}*{picks[1][1]}", tot))

def g4D():
    a, b = R.randint(2, 10), R.randint(2, 10)
    if a == b: return False
    t = R.choice([("A tray has {a} rows of muffins with {b} muffins in each row. How many muffins are on the tray?", "muffins"), ("There are {a} bags with {b} apples in each bag. How many apples are there in all?", "apples"),
                  ("A parking lot has {a} rows of cars. Each row has {b} cars. How many cars are in the lot?", "cars"), ("A shelf has {a} boxes. Each box holds {b} toy cars. How many toy cars are on the shelf?", "toy cars")])
    p = a * b
    return mk('4.D', 2, t[0].format(a=a, b=b), p, [a + b, p + a, p - b, p + 10, p - 10], f"{a} equal groups of {b} is {a} × {b} = {p}.", CS(f"{a}*{b}"))

def g4E_expr():
    a, b = R.sample(range(2, 10), 2)
    return mk('4.E', 2, f"Which expression shows {a} equal groups of {b}?", f"{a} × {b}", [f"{a} + {b}", f"{b} − {a}", f"{a} ÷ {b}"], f"{a} groups of {b} is multiplication: {a} × {b}.")

def g4E_repeat():
    a, b = R.sample(range(2, 9), 2); p = a * b
    right = ' + '.join([str(b)] * a)
    wr = [' + '.join([str(b)] * (a + 1)), ' + '.join([str(b)] * (a - 1)) if a > 2 else f"{a} + {b}", f"{a} + {b}", ' + '.join([str(a)] * (b - 1))]
    wr = [w for w in wr if sum(map(int, w.split(' + '))) != p]
    return mk('4.E', 3, f"Which repeated addition sentence matches {a} × {b}?", right, wr, f"{a} × {b} means {a} groups of {b}: {right} = {p}.")

def g4E_array():
    a, b = R.sample(range(3, 10), 2)
    return mk('4.E', 2, f"An array has {a} rows with {b} counters in each row. Which equation shows the total number of counters?", f"{a} × {b} = {a * b}", [f"{a} + {b} = {a + b}", f"{max(a, b)} − {min(a, b)} = {abs(b - a)}", f"{a} × {a} = {a * a}"] if a != b else [], f"Rows times counters in each row: {a} × {b} = {a * b}.")

def g4E_jump():
    a, b = R.randint(2, 9), R.randint(3, 9); p = a * b
    return mk('4.E', 3, f"Eli starts at 0 on a number line and makes {b} equal jumps of {a}. Where does he land?", p, [p + a, p - a, a + b, p + 2], f"{b} jumps of {a} is {b} × {a} = {p}.", CS(f"{b}*{a}"))

def g4F_mul():
    a, b = R.randint(2, 10), R.randint(2, 10); p = a * b
    return mk('4.F', 2 if min(a, b) <= 5 else 3, f"What is {a} × {b}?", p, [a * (b + 1), a * (b - 1), (a + 1) * b, (a - 1) * b, p + 10, a + b], f"{a} × {b} = {p}.", CS(f"{a}*{b}"))

def g4F_div():
    a, b = R.randint(2, 10), R.randint(2, 10); p = a * b
    return mk('4.F', 2 if min(a, b) <= 5 else 3, f"What is {p} ÷ {a}?", b, [b + 1, b - 1, a, a + b, b + 2], f"{a} × {b} = {p}, so {p} ÷ {a} = {b}.", CS(f"{p}//{a}"))

def g4G():
    k = R.choice([0, 1])
    if k == 0:
        n = R.randint(12, 49); d = R.randint(3, 9); p = n * d; t, o = n // 10, n % 10
        wr = [p + 10, p - 10, p - 20, int(f"{t * d}{o * d}"), t * d * 10 + (o * d) % 10]
        return mk('4.G', 3, f"What is {n} × {d}?", p, wr, f"{t * 10} × {d} = {t * 10 * d} and {o} × {d} = {o * d}; {t * 10 * d} + {o * d} = {p}.", CS(f"{n}*{d}"))
    n = R.randint(14, 48); d = R.randint(3, 9); p = n * d
    t = R.choice([("Each box holds {n} crayons. How many crayons are in {d} boxes?"), ("A garden has {d} rows of flowers with {n} flowers in each row. How many flowers are in the garden?"), ("A bus carries {n} students. How many students can {d} buses carry?")])
    return mk('4.G', 3, t.format(n=n, d=d), p, [p + 10, p - 10, p - 20, p + 100, n + d], f"{n} × {d} = {p}.", CS(f"{n}*{d}"))

def g4G_partial():
    n = R.randint(21, 59); d = R.randint(3, 8); t, o = n // 10 * 10, n % 10
    if o == 0: return False
    p = n * d
    return mk('4.G', 3, f"Rae finds {n} × {d} with partial products: ({t} × {d}) + ({o} × {d}). What is the total?", p, [p + 10, p - 10, t * d + o, t + o * d], f"{t * d} + {o * d} = {p}.", CS(f"{t}*{d}+{o}*{d}"))

def g4H():
    k = R.choice([0, 1]); b = R.randint(2, 9); q = R.randint(2, 10); a = b * q
    if k == 0:
        t = R.choice(["{a} stickers are shared equally among {b} friends. How many stickers does each friend get?", "A teacher puts {a} markers equally into {b} cups. How many markers are in each cup?", "{a} apples are packed equally into {b} bags. How many apples are in each bag?"])
        return mk('4.H', 2, t.format(a=a, b=b), q, [q + 1, q - 1, a - b, b, q + 2], f"{a} ÷ {b} = {q}.", CS(f"{a}//{b}"))
    t = R.choice(["{a} students are put into groups of {q}. How many groups are there?", "A baker packs {a} muffins with {q} muffins in each box. How many boxes does the baker fill?"])
    return mk('4.H', 3, t.format(a=a, q=q), b, [b + 1, b - 1, a - q, q, b + 2], f"{a} ÷ {q} = {b}.", CS(f"{a}//{q}"))

def g4I_pick():
    even = R.random() < .5
    odds = R.sample([n for n in range(11, 400) if n % 2], 4); evens = R.sample([n for n in range(10, 400) if n % 2 == 0], 4)
    if even: right, wr = evens[0], odds[:3]
    else: right, wr = odds[0], evens[:3]
    return mk('4.I', 2, f"Which number is {'even' if even else 'odd'}?", right, wr, f"Check the ones digit: a number is even when it ends in 0, 2, 4, 6, or 8.")

def g4I_why():
    n = R.randint(21, 399); od = n % 2
    right = ("Odd" if od else "Even") + f" — the ones digit is {n % 10}, so it {'cannot' if od else 'can'} be split into two equal groups"
    wrong_same = ("Even" if od else "Odd") + f" — the ones digit is {n % 10}, so it {'can' if od else 'cannot'} be split into two equal groups"
    wr = [wrong_same, ("Odd" if od else "Even") + " — because it has three digits", ("Even" if od else "Odd") + " — because the first digit is " + str(str(n)[0])]
    return mk('4.I', 3, f"Is {n} even or odd, and why?", right, wr, "A whole number is even if its ones digit is 0, 2, 4, 6, or 8; otherwise it is odd.")

def g4J():
    a, b = R.randint(3, 9), R.randint(3, 9)
    if a == b: return False
    p = a * b
    return mk('4.J', 3, f"Sam knows that {a} × {b} = {p}. What is {p} ÷ {a}?", b, [a, b + 1, b - 1, p - a], f"Multiplication and division undo each other: {p} ÷ {a} = {b}.", CS(f"{p}//{a}"))

def g4K_one():
    t = R.choice([0, 1]); a, b = R.randint(3, 9), R.randint(3, 9)
    if t == 0:
        p = a * b
        return mk('4.K', 2, f"A baker puts {b} cookies in each box. How many cookies are in {a} boxes?", p, [a + b, p + a, p - b, p + 10], f"{a} × {b} = {p}.", CS(f"{a}*{b}"))
    p = a * b
    return mk('4.K', 3, f"There are {p} books on shelves with {b} books on each shelf. How many shelves are there?", a, [a + 1, a - 1, b, p - b], f"{p} ÷ {b} = {a}.", CS(f"{p}//{b}"))

def g4K_two():
    k = R.choice([0, 1, 2]); a, b = R.randint(3, 9), R.randint(3, 9); p = a * b
    if k == 0:
        c = R.randint(2, 9)
        if p - c <= 0: return False
        return mk('4.K', 4, f"Maria buys {a} packs of pencils with {b} pencils in each pack. She gives {c} pencils to her sister. How many pencils does Maria have left?", p - c, [p + c, a * (b - c) if b > c else p + 2 * c, a + b - c, p - c + 10],
                  f"{a} × {b} = {p}, and {p} − {c} = {p - c}.", CS(f"{a}*{b}-{c}"))
    if k == 1:
        c = R.randint(2, 9)
        return mk('4.K', 4, f"A coach has {p} cones. She puts them into {a} equal piles and then adds {c} cones to one pile. How many cones are in that pile now?", b + c,
                  [p + c, a + c, b - c if b > c else b + 2 * c, b + c + 10], f"{p} ÷ {a} = {b}, and {b} + {c} = {b + c}.", CS(f"{p}//{a}+{c}"))
    c = R.randint(2, 6)
    return mk('4.K', 4, f"A store sells muffins in boxes of {b}. Pam buys {a} boxes and {c} extra muffins. How many muffins does Pam buy in all?", p + c, [p - c, a + b + c, a * (b + c), p + c + 10], f"{a} × {b} = {p}, and {p} + {c} = {p + c}.", CS(f"{a}*{b}+{c}"))

# ---------------------------------------------------------------- strand 5
def g5A_one():
    a = R.randint(150, 480); b = R.randint(40, 130); k = R.choice([0, 1])
    if k == 0:
        return mk('5.A', 2, f"Tara had {a + b} stickers. She gave {b} stickers away and has n stickers left. Which equation can she use to find n?", f"{a + b} − {b} = n", [f"{a + b} + {b} = n", f"{b} − {a + b} = n", f"n − {a + b} = {b}"], "She started with the greater number and took away the stickers she gave.")
    return mk('5.A', 2, f"A library had {a} books. It got {b} new books and now has t books. Which equation can be used to find t?", f"{a} + {b} = t", [f"{a} − {b} = t", f"{b} − {a} = t", f"t + {a} = {b}"], "New books are added, so the total is found by addition.")

def g5A_two():
    a = R.randint(100, 300); b = R.randint(40, 150); c = R.randint(20, 80)
    k = R.choice([0, 1])
    if k == 0:
        return mk('5.A', 4, f"Leo had {a} points. He earned {b} more points and then lost {c} points. Which equation finds p, the number of points Leo has now?", f"{a} + {b} − {c} = p", [f"{a} − {b} + {c} = p", f"{a} + {b} + {c} = p", f"{a} − {b} − {c} = p"], "He gains points first (add), then loses points (subtract).")
    return mk('5.A', 4, f"A school had {a} chairs. It bought {b} more chairs and then gave away {c} chairs. Which equation finds c, the number of chairs the school has now?".replace("finds c,", "finds n,"), f"{a} + {b} − {c} = n", [f"{a} − {b} − {c} = n", f"{a} + {b} + {c} = n", f"{a} − {b} + {c} = n"], "Add the chairs it bought, then subtract the chairs it gave away.")

def g5B_mul():
    a, b = R.sample(range(3, 10), 2)
    return mk('5.B', 2, f"There are {a} baskets with {b} apples in each basket. Which equation can be used to find t, the total number of apples?", f"{a} × {b} = t", [f"{a} + {b} = t", f"{b} − {a} = t", f"{a} ÷ {b} = t"], "Equal groups of the same size are found with multiplication.")

def g5B_div():
    a, b = R.randint(3, 9), R.randint(3, 9); p = a * b
    return mk('5.B', 3, f"{p} pencils are shared equally among {a} students. Which equation can be used to find n, the number of pencils each student gets?", f"{p} ÷ {a} = n", [f"{p} × {a} = n", f"{a} ÷ {p} = n", f"{p} − {a} = n"], "Sharing a total equally is division: total ÷ number of groups.")

def g5B_solve():
    a, b = R.randint(3, 9), R.randint(3, 9); p = a * b
    return mk('5.B', 3, f"A strip diagram shows {a} equal parts. Each part is {b}. What is the value of the whole strip?", p, [a + b, p - a, p + b, p + 10], f"{a} parts of {b} is {a} × {b} = {p}.", CS(f"{a}*{b}"))

def g5C():
    k = R.choice([0, 1, 2]); a, b = R.randint(2, 9), R.randint(11, 40)
    if k == 0:
        return mk('5.C', 3, f"What does {a} × {b} represent?", f"{a} times as much as {b}", [f"{a} more than {b}", f"{a} less than {b}", f"{b} divided by {a}"], f"{a} × {b} is a comparison: {a} times as many as {b}.")
    if k == 1:
        return mk('5.C', 3, f"Sam has {b} marbles. Tia has {a} times as many marbles as Sam. Which expression shows how many marbles Tia has?", f"{a} × {b}", [f"{a} + {b}", f"{b} − {a}", f"{b} ÷ {a}"], f"{a} times as many as {b} is {a} × {b}.")
    return mk('5.C', 3, f"Which expression shows {a} times as many as {b}?", f"{a} × {b}", [f"{a} + {b}", f"{b} − {a}", f"{b} ÷ {a}"], f"\"{a} times as many as {b}\" is {a} × {b}.")

def g5D():
    a, b = R.randint(3, 9), R.randint(3, 9); p = a * b; k = R.choice([0, 1, 2, 3])
    if k == 0: q, ans = f"What number makes this equation true?  □ × {a} = {p}", b
    elif k == 1: q, ans = f"What number makes this equation true?  {a} × □ = {p}", b
    elif k == 2: q, ans = f"What number makes this equation true?  {p} ÷ □ = {a}", b
    else: q, ans = f"What number makes this equation true?  □ ÷ {a} = {b}", p
    return mk('5.D', 2 if k < 2 else 3, q, ans, [ans + 1, ans - 1, a + b, p - a if p - a != ans else p + a, ans + 2], "Use the fact family: multiplication and division undo each other.", CS(f"{p}//{a}") if k < 3 else CS(f"{a}*{b}"))

def g5E_val():
    r = R.randint(2, 9); k = R.randint(5, 9); item = R.choice([("boxes", "pens"), ("bikes", "wheels"), ("packs", "cards"), ("tables", "chairs")])
    rows = ', '.join(f"{i} {item[0]} → {i * r} {item[1]}" for i in (1, 2, 3))
    return mk('5.E', 3, f"A table shows the number of {item[1]} for different numbers of {item[0]}: {rows}. If the pattern continues, how many {item[1]} are there for {k} {item[0]}?", k * r,
              [k + r, (k + 1) * r, (k - 1) * r, k * r + r // 2 + 1], f"Each of the {item[0]} has {r} {item[1]}, so {k} × {r} = {k * r}.", CS(f"{k}*{r}"))

def g5E_rule():
    r = R.randint(3, 8)
    ws = [f"multiply the first number by {r}", f"add {r} to the first number", f"multiply the first number by {r + 1}", f"subtract {r} from the first number", f"add {r + 1} to the first number"]
    ws = [w for w in ws]
    return mk('5.E', 4, f"The number pairs in a table are (1, {r}), (2, {2 * r}), and (3, {3 * r}). Which rule matches the table?", ws[0], ws[1:], f"1 × {r} = {r}, 2 × {r} = {2 * r}, 3 × {r} = {3 * r}.")

# ---------------------------------------------------------------- strand 6 geometry
def g6C():
    l, w = R.randint(3, 12), R.randint(3, 9)
    if l == w: return False
    k = R.choice([0, 1]); A = l * w
    if k == 0:
        return mk('6.C', 2, f"A rectangle is covered with {w} rows of unit squares. Each row has {l} unit squares. What is the area of the rectangle?", f"{A} square units", [f"{l + w} square units", f"{2 * (l + w)} square units", f"{A + l} square units", f"{A - w} square units"],
                  f"Rows × squares in each row: {w} × {l} = {A}.", f"f'{{{w}*{l}}} square units'")
    t = R.choice([("A garden is {l} feet long and {w} feet wide. What is its area?", "square feet"), ("A poster is {l} inches long and {w} inches wide. What is its area?", "square inches"), ("A classroom floor is {l} meters long and {w} meters wide. What is its area?", "square meters")])
    return mk('6.C', 3, t[0].format(l=l, w=w), f"{A} {t[1]}", [f"{l + w} {t[1]}", f"{2 * (l + w)} {t[1]}", f"{A + l} {t[1]}", f"{A - w} {t[1]}"], f"Area = length × width = {l} × {w} = {A}.", f"f'{{{l}*{w}}} {t[1]}'")

def g6D():
    a, b, c, d = R.randint(4, 9), R.randint(2, 5), R.randint(2, 5), R.randint(2, 4); A1, A2 = a * b, c * d; tot = A1 + A2
    t = R.choice(["An L-shaped figure is made of two rectangles that do not overlap. One rectangle is {a} units by {b} units. The other is {c} units by {d} units. What is the area of the whole figure?",
                  "A floor plan is made from two rectangles that share an edge. One room is {a} feet by {b} feet. The other is {c} feet by {d} feet. What is the total area?"])
    unit = "square units" if t.startswith("An L") else "square feet"
    return mk('6.D', 4, t.format(a=a, b=b, c=c, d=d), f"{tot} {unit}", [f"{(a + c) * (b + d)} {unit}", f"{A1} {unit}", f"{a + b + c + d} {unit}", f"{tot + 2} {unit}"], f"{a} × {b} = {A1} and {c} × {d} = {A2}; {A1} + {A2} = {tot}.", f"f'{{{a}*{b}+{c}*{d}}} {unit}'")

def g6E():
    b = R.choice([2, 3, 4, 6, 8]); shape = R.choice(["square", "rectangle", "sheet of paper", "tile"])
    return mk('6.E', 3, f"A {shape} is cut into {b} parts that all have the same area. Each part is what fraction of the whole {shape}?", f"1/{b}", [f"{b}/1", f"1/{b + 1}", f"{b - 1}/{b}", f"1/{b + 2}"], f"{b} equal-area parts make 1 whole, so each is 1/{b} of it.")

# ---------------------------------------------------------------- strand 7 measurement
def g7A():
    b = R.choice([2, 4, 8]); n = R.randint(1, b - 1); k = R.choice([0, 1])
    if k == 0:
        return mk('7.A', 2, f"A bug starts at 0 on a number line and hops {n} time{'s' if n > 1 else ''}. Each hop is 1/{b} unit long. How far from 0 is the bug?", f"{n}/{b}", [f"{n + 1}/{b}", f"{n}/{n + b}", f"1/{n * b}", f"{b}/{n}"], f"{n} hops of 1/{b} is {n}/{b}.")
    return mk('7.A', 2, f"On a number line, the distance from 0 to 1 is split into {b} equal parts. A point is {n} part{'s' if n > 1 else ''} from 0. What is the point's distance from 0?", f"{n}/{b}", [f"{n + 1}/{b}", f"{b - n}/{b}", f"{n}/{b + 2}", f"{b}/{n}"], f"Each part is 1/{b}, so {n} parts is {n}/{b}.")

def g7B_rect():
    l, w = R.randint(4, 15), R.randint(3, 11)
    if l == w: return False
    P = 2 * (l + w); k = R.choice([0, 1])
    if k == 0:
        return mk('7.B', 2, f"A rectangle is {l} cm long and {w} cm wide. What is its perimeter?", f"{P} cm", [f"{l * w} cm", f"{l + w} cm", f"{P - 2} cm", f"{P + 2} cm"], f"Add all four sides: {l} + {w} + {l} + {w} = {P}.", f"f'{{2*({l}+{w})}} cm'")
    return mk('7.B', 4, f"A rectangle has a perimeter of {P} cm. Its length is {l} cm. What is its width?", f"{w} cm", [f"{P - l} cm", f"{P - 2 * l} cm", f"{l - w if l > w else l + w} cm", f"{w + 2} cm"], f"Half the perimeter is {P // 2}, and {P // 2} − {l} = {w}.", f"f'{{{P}//2-{l}}} cm'")

def g7B_poly():
    k = R.choice([0, 1])
    if k == 0:
        a, b, c = R.randint(4, 12), R.randint(4, 12), R.randint(4, 12); P = a + b + c
        return mk('7.B', 2, f"A triangle has sides of {a} inches, {b} inches, and {c} inches. What is its perimeter?", f"{P} inches", [f"{P - 2} inches", f"{P + 3} inches", f"{a * b} inches", f"{a + b} inches"], f"{a} + {b} + {c} = {P}.", f"f'{{{a}+{b}+{c}}} inches'")
    a, b = R.randint(5, 12), R.randint(5, 12); c = R.randint(4, 10); P = a + b + c
    return mk('7.B', 4, f"A triangle has a perimeter of {P} cm. Two sides are {a} cm and {b} cm. What is the length of the third side?", f"{c} cm", [f"{P - a} cm", f"{P - b} cm", f"{a + b} cm", f"{P + a + b} cm"], f"{P} − {a} − {b} = {c}.", f"f'{{{P}-{a}-{b}}} cm'")

def g7B_sq():
    s = R.randint(4, 15); k = R.choice([0, 1])
    if k == 0: return mk('7.B', 2, f"A square has sides that are {s} feet long. What is its perimeter?", f"{4 * s} feet", [f"{s * s} feet", f"{2 * s} feet", f"{3 * s} feet", f"{4 * s + 4} feet"], f"A square has 4 equal sides: 4 × {s} = {4 * s}.", f"f'{{4*{s}}} feet'")
    n = R.choice([5, 6, 8]); nm = {5: 'pentagon', 6: 'hexagon', 8: 'octagon'}[n]
    return mk('7.B', 3, f"A regular {nm} has {n} sides that are each {s} cm long. What is its perimeter?", f"{n * s} cm", [f"{(n - 1) * s} cm", f"{(n + 1) * s} cm", f"{n + s} cm", f"{n * s + 10} cm"], f"{n} × {s} = {n * s}.", f"f'{{{n}*{s}}} cm'")

def g7C_end():
    h = R.randint(1, 9); m = R.randrange(0, 60, 5); x = R.choice([15, 20, 25, 30, 35, 40, 45, 50, 60]); y = R.choice([0, 0, 10, 15, 20, 25, 30])
    start = h * 60 + m; end = start + x + y
    if end > 719: return False
    if y == 0:
        q = f"Practice starts at {clock(start)} and lasts {x} minutes. What time does practice end?"; e = f"{clock(start)} plus {x} minutes is {clock(end)}."
    else:
        q = f"Dan starts homework at {clock(start)}. He spends {x} minutes on math and {y} minutes on reading. What time does he finish?"; e = f"{x} + {y} = {x + y} minutes; {clock(start)} plus {x + y} minutes is {clock(end)}."
    cands = [end + 10, end - 10, end + 60, end - 60, end + 5, end - 5, end + 15]
    wr = [clock(c) for c in cands if 60 <= c <= 719]
    return mk('7.C', 3, q, clock(end), wr, e, f"f'{{({start}+{x}+{y})//60}}:{{({start}+{x}+{y})%60:02d}}'")

def g7C_elapsed():
    h = R.randint(1, 8); m = R.randrange(0, 60, 5); dur = R.randrange(25, 125, 5); s = h * 60 + m; e = s + dur
    if e > 719: return False
    h2, m2 = divmod(e, 60); naive = (h2 - h) * 60 + abs(m2 - m)
    wr = [naive, dur + 10, dur - 10, dur + 20, dur + 30]
    return mk('7.C', 4, f"A movie starts at {clock(s)} and ends at {clock(e)}. How many minutes long is the movie?", f"{dur} minutes", [f"{w} minutes" for w in wr], f"From {clock(s)} to {clock(e)} is {dur} minutes.", f"f'{{({e})-({s})}} minutes'")

def g7C_add():
    x, y = R.choice([10, 15, 20, 25, 30, 35, 40, 45]), R.choice([15, 20, 25, 30, 35, 45])
    t = R.choice([("Mia spends {x} minutes on a walk and {y} minutes on a bike ride. How many minutes does she spend on both?"), ("A show has a {x}-minute first part and a {y}-minute second part. How long is the show?")])
    return mk('7.C', 2, t.format(x=x, y=y), f"{x + y} minutes", [f"{x + y + 10} minutes", f"{abs(x - y)} minutes", f"{x + y - 5} minutes", f"{x + y + 20} minutes"], f"{x} + {y} = {x + y} minutes.", f"f'{{{x}+{y}}} minutes'")

W_ITEMS = ["a bowling ball", "a bag of flour", "a backpack full of books", "a puppy", "a watermelon", "a laptop", "a bag of potatoes", "a pair of boots"]
L_ITEMS = ["a bottle of juice", "water in a fish tank", "milk in a glass", "soup in a pot", "paint in a can", "water in a bucket", "lemonade in a pitcher", "gasoline in a tank"]
def g7D():
    if R.random() < .5:
        return mk('7.D', 2, "Which should be measured using weight?", R.choice(W_ITEMS), R.sample(L_ITEMS, 3), "Solid objects are weighed; liquids are measured by how much space they fill (liquid volume).")
    return mk('7.D', 2, "Which should be measured using liquid volume (capacity)?", R.choice(L_ITEMS), R.sample(W_ITEMS, 3), "Liquids are measured by liquid volume; solid objects are weighed.")

def g7E_tool():
    if R.random() < .5:
        return mk('7.E', 2, "Which tool is best for finding the weight of an object?", R.choice(["a balance scale", "a bathroom scale"]), ["a measuring cup", "a ruler", "a clock"], "A scale or balance measures weight.")
    return mk('7.E', 2, "Which tool is best for measuring liquid volume?", "a measuring cup", ["a ruler", "a balance scale", "a clock"], "A measuring cup shows how much liquid fills it.")

def g7E_unit():
    items = [("the weight of a paper clip", "grams", ["kilograms", "liters", "milliliters"], 2), ("the weight of a bowling ball", "kilograms", ["grams", "liters", "milliliters"], 3), ("the weight of a pencil", "grams", ["kilograms", "liters", "milliliters"], 2),
             ("the liquid volume of a large bottle of soda", "liters", ["milliliters", "grams", "kilograms"], 3), ("the liquid volume of a spoonful of medicine", "milliliters", ["liters", "grams", "kilograms"], 3), ("the liquid volume of a big bucket of water", "liters", ["milliliters", "grams", "kilograms"], 3),
             ("the weight of a backpack full of books", "kilograms", ["grams", "liters", "milliliters"], 3)]
    w, r, wr, d = R.choice(items)
    return mk('7.E', d, f"Which metric unit is best for measuring {w}?", r, wr, f"{r.capitalize()} is the best-sized unit for this measurement.")

# ---------------------------------------------------------------- strand 8 data
CAT8 = [["soccer", "basketball", "swimming", "tennis"], ["dogs", "cats", "fish", "birds"], ["pizza", "tacos", "pasta", "salad"], ["red", "blue", "green", "yellow"], ["apples", "bananas", "grapes", "oranges"]]
def g8A_tally():
    cats = R.choice(CAT8)[:3]; n = R.randint(12, 18); votes = [R.choice(cats) for _ in range(n)]
    from collections import Counter
    c = Counter(votes)
    if len(c) < 3: return False
    pick = R.choice(cats); right = c[pick]
    return mk('8.A', 2, "Students voted for a favorite. The votes were: " + ', '.join(votes) + f". When the data are put in a frequency table, how many votes does \"{pick}\" get?", right, [right + 1, right - 1, right + 2, n - right], f"Count each time \"{pick}\" appears: {right}.", CS(f"{votes}.count('{pick}')") if False else None)

def g8A_picto():
    cat = R.choice(R.choice(CAT8)); k = R.choice([2, 4, 5, 10]); m = R.randint(3, 8)
    return mk('8.A', 2, f"In a pictograph, each ★ stands for {k} students. The row for {cat} has {m} ★. How many students does that row show?", k * m, [m, k + m, (m + 1) * k, (m - 1) * k], f"{m} stars × {k} = {k * m}.", CS(f"{m}*{k}"))

def g8A_bar():
    cat = R.choice(R.choice(CAT8)); s = R.choice([2, 5, 10]); j = R.randint(3, 8)
    return mk('8.A', 3, f"On a bar graph, each line on the scale counts by {s}s. The bar for {cat} reaches the {ORD.get(j, str(j) + 'th')} line above 0. What value does the bar show?", s * j, [j, s + j, s * (j + 1), s * (j - 1)], f"{j} lines × {s} = {s * j}.", CS(f"{j}*{s}"))

def g8A_dot():
    vals = [1, 2, 3, 4]; dots = [R.randint(1, 6) for _ in vals]; tot = sum(dots); k = R.choice([0, 1])
    desc = ', '.join(f"{v} book{'s' if v > 1 else ''}: {d} dot{'s' if d > 1 else ''}" for v, d in zip(vals, dots))
    if k == 0:
        return mk('8.A', 3, f"A dot plot shows how many books students read. Each dot is one student. {desc}. How many students are in the data?", tot, [sum(vals), tot - 1, tot + 2, max(dots)], f"Add the dots: {' + '.join(map(str, dots))} = {tot}.", CS("+".join(map(str, dots))))
    ge2 = sum(dots[1:])
    return mk('8.A', 3, f"A dot plot shows how many books students read. Each dot is one student. {desc}. How many students read 2 or more books?", ge2, [tot, ge2 + 1, ge2 - 1, dots[1]], f"Add the dots for 2, 3, and 4 books: {' + '.join(map(str, dots[1:]))} = {ge2}.", CS("+".join(map(str, dots[1:]))))

def g8B():
    cats = R.choice(CAT8); vals = [R.choice([5, 10, 15, 20, 25, 30, 35, 40, 45]) for _ in cats]
    if len(set(vals)) < 4: return False
    data = ', '.join(f"{c} {v}" for c, v in zip(cats, vals)); k = R.choice([0, 1, 2, 3])
    i, j = R.sample(range(4), 2)
    base = f"A bar graph with a scale that counts by 5s shows these totals: {data}."
    if k == 0:
        r = abs(vals[i] - vals[j]); hi, lo = (i, j) if vals[i] > vals[j] else (j, i)
        return mk('8.B', 2, base + f" How many more are in {cats[hi]} than in {cats[lo]}?", r, [vals[hi] + vals[lo], r + 5, max(r - 5, 5) if r - 5 != r else r + 10, vals[hi]], f"{vals[hi]} − {vals[lo]} = {r}.", CS(f"{vals[hi]}-{vals[lo]}"))
    if k == 1:
        s = vals[i] + vals[j]
        return mk('8.B', 2, base + f" How many are in {cats[i]} and {cats[j]} together?", s, [abs(vals[i] - vals[j]), s + 5, s - 5, sum(vals)], f"{vals[i]} + {vals[j]} = {s}.", CS(f"{vals[i]}+{vals[j]}"))
    if k == 2:
        t = sum(vals)
        return mk('8.B', 3, base + " What is the total number for all four categories?", t, [t + 5, t - 5, t + 10, t - vals[i]], f"{' + '.join(map(str, vals))} = {t}.", CS("+".join(map(str, vals))))
    a, b, c = R.sample(range(4), 3); r = vals[a] + vals[b] - vals[c]
    if r <= 0: return False
    return mk('8.B', 4, base + f" How many more are in {cats[a]} and {cats[b]} together than in {cats[c]}?", r, [vals[a] + vals[b] + vals[c], r + 5, r - 5 if r > 5 else r + 10, abs(vals[a] - vals[b]) + vals[c]], f"({vals[a]} + {vals[b]}) − {vals[c]} = {r}.", CS(f"{vals[a]}+{vals[b]}-{vals[c]}"))

# ================================================================= run the generators
rep(2, g2A_compose); rep(1, g2A_sum); rep(2, g2A_zero)
rep(2, g2B_value); rep(1, g2B_ratio); rep(2, g2B_make)
rep(4, g2C_between); rep(2, g2C_closest)
rep(3, g2D_symbol); rep(1, g2D_equal); rep(2, g2D_order); rep(2, g2D_extreme)
rep(5, g3A); rep(3, g3B_right); rep(2, g3B_left); rep(3, g3C_unit); rep(2, g3D_sum); rep(2, g3D_fraction)
rep(3, g3E_kids); rep(2, g3E_set); rep(2, g3E_items); rep(5, g3F)
rep(2, g3H_den); rep(2, g3H_num); rep(2, g3H_extreme)
rep(3, g4A_add); rep(3, g4A_sub); rep(3, g4A_two); rep(3, g4B_round); rep(3, g4B_est); rep(5, g4C); rep(4, g4D)
rep(3, g4E_expr); rep(2, g4E_repeat); rep(2, g4E_array); rep(2, g4E_jump)
rep(5, g4F_mul); rep(5, g4F_div); rep(4, g4G); rep(2, g4G_partial); rep(5, g4H); rep(3, g4I_pick); rep(2, g4I_why); rep(4, g4J)
rep(3, g4K_one); rep(4, g4K_two)
rep(2, g5A_one); rep(2, g5A_two); rep(2, g5B_mul); rep(2, g5B_div); rep(2, g5B_solve); rep(4, g5C); rep(5, g5D); rep(3, g5E_val); rep(2, g5E_rule)
rep(5, g6C); rep(4, g6D); rep(3, g6E)
rep(4, g7A); rep(3, g7B_rect); rep(2, g7B_poly); rep(2, g7B_sq); rep(3, g7C_end); rep(3, g7C_elapsed); rep(2, g7C_add); rep(4, g7D); rep(2, g7E_tool); rep(6, g7E_unit)
rep(3, g8A_tally); rep(2, g8A_picto); rep(2, g8A_bar); rep(3, g8A_dot); rep(7, g8B)

# ================================================================= hand-written items (concepts that need wording, not arithmetic)
H('2.B', 2, "Which statement about place value is true?", "Ten hundreds make one thousand.", ["Ten ones make one hundred.", "Ten tens make one thousand.", "Ten thousands make one hundred."], "10 hundreds = 1,000. Ten ones make a ten, ten tens make a hundred, and ten thousands make ten thousand.")
H('2.B', 3, "In the number 83,479, which digit is in the thousands place?", "3", ["8", "4", "7"], "From the right: 9 ones, 7 tens, 4 hundreds, 3 thousands, 8 ten thousands.")
H('3.C', 2, "In the fraction 1/6, what does the denominator 6 tell you?", "The whole is split into 6 equal parts.", ["Six parts are shaded.", "The fraction is 6 times as big as 1.", "Each part is 6 inches long."], "The denominator names how many equal parts the whole is partitioned into.")
H('3.C', 2, "Which fraction is a unit fraction?", "1/8", ["3/4", "2/8", "5/6"], "A unit fraction has a numerator of 1: one part of a whole split into equal parts.")
H('3.C', 3, "Fatima shades 1 part of a bar split into 4 equal parts. Ravi shades 1 part of an identical bar split into 8 equal parts. Whose shaded part is larger?", "Fatima's, because fourths are larger than eighths.", ["Ravi's, because 8 is greater than 4.", "They are the same size.", "It is impossible to tell."], "The more equal parts a whole is split into, the smaller each part is.")
H('3.G', 3, "Which statement explains why 2/4 and 1/2 are equivalent fractions?", "They name the same point on a number line.", ["They have the same denominator.", "They have the same numerator.", "Both are greater than 1."], "Equivalent fractions name the same point on the number line or the same amount of the same-size whole.")
H('3.G', 3, "Jada ate 3/6 of a pizza. Marco ate 1/2 of an identical pizza. Which statement is true?", "They ate the same amount of pizza.", ["Jada ate more, because 3 is greater than 1.", "Marco ate more, because 2 is less than 6.", "It is impossible to compare the amounts."], "3/6 and 1/2 name the same part of the same-size whole, so they are equivalent.")
H('3.G', 4, "Which pair of fractions is equivalent?", "2/3 and 4/6", ["1/3 and 1/6", "3/4 and 3/8", "1/2 and 2/3"], "Splitting each third into 2 equal parts makes 2/3 into 4/6.")
H('3.H', 3, "Mia ran 3/4 of a mile. Jon ran 3/8 of a mile. Who ran farther?", "Mia", ["Jon", "They ran the same distance.", "It is impossible to tell."], "The numerators are the same; fourths are larger parts than eighths, so 3/4 > 3/8.")
H('3.H', 2, "Which is greater, 1/3 or 1/6?", "1/3", ["1/6", "They are equal.", "It is impossible to tell."], "Thirds are larger pieces than sixths, so 1/3 > 1/6.")
H('4.I', 2, "Which rule can you use to tell if a whole number is even?", "It can be split into two equal groups with none left over.", ["Its digits add up to 10.", "It is greater than 10.", "It ends in 3, 5, or 7."], "Even numbers divide by 2 with nothing left over (they end in 0, 2, 4, 6, or 8).")
H('4.I', 3, "What is true about the sum of two odd numbers, such as 7 + 9?", "The sum is always even.", ["The sum is always odd.", "The sum is always a multiple of 5.", "The sum can be even or odd."], "Two odd numbers pair up their extra ones, leaving no leftover: the sum is even.")
H('5.C', 3, "Which statement matches the expression 5 × 12?", "5 times as many as 12", ["5 more than 12", "12 less than 5", "12 divided by 5"], "5 × 12 compares: 5 times as much as 12.")
H('6.A', 2, "Which three-dimensional figure has 6 square faces?", "cube", ["cylinder", "cone", "triangular prism"], "A cube has 6 faces, and every face is a square.")
H('6.A', 2, "Which figure has one flat circular face, one curved surface, and one vertex?", "cone", ["cylinder", "sphere", "cube"], "A cone has a circular base, a curved surface, and a point (vertex) at the top.")
H('6.A', 3, "Which figure has two circular faces and no vertices?", "cylinder", ["cone", "sphere", "rectangular prism"], "A cylinder has two flat circular faces joined by a curved surface.")
H('6.A', 2, "How many vertices does a rectangular prism have?", "8", ["6", "10", "12"], "A rectangular prism has 8 corners (vertices), 12 edges, and 6 faces.")
H('6.A', 3, "How many faces does a triangular prism have?", "5", ["3", "4", "6"], "A triangular prism has 2 triangular faces and 3 rectangular faces.")
H('6.A', 3, "How many edges does a cube have?", "12", ["6", "8", "10"], "A cube has 12 edges, 8 vertices, and 6 faces.")
H('6.A', 4, "Which figure does NOT belong with the others?", "cylinder", ["cube", "rectangular prism", "triangular prism"], "The cylinder has a curved surface. The other three have only flat faces.")
H('6.B', 2, "Which shape is NOT a quadrilateral?", "triangle", ["trapezoid", "rhombus", "parallelogram"], "A quadrilateral has exactly 4 sides; a triangle has 3.")
H('6.B', 3, "Which statement is true?", "Every square is also a rectangle.", ["Every rectangle is also a square.", "A trapezoid has 5 sides.", "A rhombus has only 3 sides."], "A square has 4 right angles, so it is a rectangle with all sides equal.")
H('6.B', 4, "A quadrilateral has 4 equal sides and 2 pairs of parallel sides, but it has no right angles. Which shape is it?", "rhombus", ["rectangle", "trapezoid", "square"], "Rectangles and squares have right angles, and a trapezoid has only one pair of parallel sides.")
H('6.B', 3, "Which quadrilateral has exactly one pair of parallel sides?", "trapezoid", ["rectangle", "square", "rhombus"], "A trapezoid has one pair of parallel sides.")
H('6.E', 3, "A square is cut into 2 triangles of equal area along a diagonal. Each triangle is what fraction of the square?", "1/2", ["1/4", "2/1", "1/3"], "Two equal parts make 1 whole, so each is 1/2.")
H('6.E', 4, "Two identical rectangles are each cut into 4 parts with equal areas, but in different ways. Which statement is true?", "Each part is 1/4 of its rectangle, even if the parts look different.", ["The parts cut differently cannot be fourths.", "Each part is 1/2 of its rectangle.", "The parts have different areas."], "Equal areas make equal shares: each of 4 equal-area parts is 1/4 of the whole.")
H('7.D', 3, "Which situation is best for measuring liquid volume?", "Finding how much water a pitcher holds", ["Finding how heavy a pitcher is when it is empty", "Finding how long a pitcher is", "Finding what time it is"], "Liquid volume tells how much liquid fits in a container.")
H('9.A', 2, "What does it mean when a person earns income from working?", "They receive money in exchange for their work.", ["They borrow money from a bank.", "They pay someone else to work for them.", "They put money into a savings account."], "Income is the money people earn for doing work (labor).")
H('9.A', 3, "A baker learns how to make wedding cakes and can now charge more for her work. Why can she earn more?", "Her new skills and knowledge make her work more valuable.", ["She borrowed money from a lender.", "She spent all her savings.", "She stopped working."], "Skills and knowledge (human capital) can raise the income a person earns.")
H('9.A', 2, "Which is an example of labor?", "A person painting houses for pay", ["A can of paint", "A ladder", "A paintbrush"], "Labor is the work people do. The other choices are tools and materials.")
H('9.B', 2, "A storm destroys many orange trees, so there are fewer oranges to sell. What usually happens to the price of oranges?", "The price goes up.", ["The price goes down.", "The price stays the same no matter what.", "The oranges become free."], "When a resource is scarce, its price usually rises.")
H('9.B', 2, "What does it mean when a resource is scarce?", "There is not enough of it for everyone who wants it.", ["There is more than enough for everyone.", "It costs nothing.", "It is very old."], "Scarcity means limited supply compared with what people want.")
H('9.B', 3, "Only a few copies of a popular toy are left in the store, and many people want one. Why might the store raise the price?", "Because the toy is scarce and many people want it.", ["Because the toy is plentiful.", "Because nobody wants the toy.", "Because the store wants to give it away."], "Scarce goods that many people want tend to cost more.")
H('9.C', 3, "Eli planned to save $20 for a book. At the store he buys a $15 toy he did not plan to buy. What is a cost of this unplanned spending?", "He no longer has enough saved for the book.", ["He earned more income.", "He got the book for free.", "He saved more money."], "Spending money on one thing means less money for something else.")
H('9.C', 2, "Which is a benefit of planned spending?", "You can make sure you have enough money for what you need.", ["You always spend more money.", "You buy things as soon as you see them.", "You never have to make choices."], "A spending plan helps you set aside money for needs and goals.")
H('9.C', 3, "Jo sees a toy on sale and buys it without thinking, even though her plan was to save for a bike. What kind of spending is this?", "Unplanned spending", ["Planned spending", "Earning income", "Charitable giving"], "Spending that was not part of the plan is unplanned spending.")
H('9.D', 2, "Sam borrows $30 from a lender and agrees to pay it back later with extra money added. What is the extra money called?", "interest", ["income", "savings", "a tax"], "Interest is the fee a borrower pays for using a lender's money.")
H('9.D', 2, "Who is responsible for paying back borrowed money?", "the borrower", ["the lender", "the cashier", "the person who sells the item"], "The borrower must repay the lender, usually with interest.")
H('9.D', 3, "When might a person use credit?", "When what they want or need costs more than the money they have right now", ["When they have much more money than they need", "When they never want to pay for anything", "When they are putting money away for later"], "Credit lets people buy now and pay later, but they must pay it back.")
H('9.E', 2, "Which is a good reason to save money?", "To have money for something important later, like college", ["To make sure you owe more money later", "To spend it all right away", "To make sure you cannot buy what you need"], "Saving sets money aside for future needs and goals.")
H('9.E', 2, "Ruby saves $5 every week. How much will she have saved after 4 weeks?", "$20", ["$9", "$25", "$15"], "4 × $5 = $20.")
H('9.E', 3, "What is a savings plan?", "A plan to set aside part of your money regularly for a goal", ["A plan to spend all your money on wants", "A loan from a bank", "A list of things you owe"], "A savings plan sets a goal and a regular amount to put away.")
H('9.F', 2, "Which choice is an example of charitable giving?", "Donating part of your allowance to a food bank", ["Buying yourself a new game", "Paying back a loan", "Putting money in your piggy bank"], "Charitable giving means giving money or goods to help others.")
H('9.F', 3, "Dani gets $10 allowance. She puts $4 in savings, spends $5 on a toy, and gives $1 to an animal shelter. How much does she save?", "$4", ["$5", "$1", "$10"], "The $4 put away is savings; $5 is spending and $1 is giving.")
H('9.F', 3, "Lena earns $12 for walking dogs. She spends $7 on a book and puts the rest in a jar for a new bike. Which decision is saving?", "Putting $5 in the jar for a bike", ["Buying the $7 book", "Walking the dogs", "Borrowing money from a friend"], "Saving means setting money aside for later: 12 − 7 = 5.")

n = B.save(os.path.join(os.path.dirname(__file__), '..', 'batches', 'g3_math.jsonl'))
print("wrote", n, "questions")

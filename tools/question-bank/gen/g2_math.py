#!/usr/bin/env python3
"""Grade 2 Mathematics (TEKS 111.4.b) - original questions. Run: python3 gen/g2_math.py  -> batches/g2_math.jsonl"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('111.4.b.', 202, no_neg=True)
R, mk, H, rep = B.R, B.mk, B.hand, B.rep
LT, GT, EQ = "less than (<)", "greater than (>)", "equal to (=)"
NM = ["Ava", "Ben", "Cara", "Dev", "Eli", "Fay", "Gus", "Hana", "Ivan", "Jo", "Kai", "Lena", "Max", "Nia", "Omar", "Pia", "Raj", "Sam", "Tia", "Zoe"]
ORD = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth'}
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def who(): return R.choice(NM)
def an(w): return 'an' if w[0] in 'aeiou' else 'a'
def dollars(c): return f"${c // 100}.{c % 100:02d}"
def wd(n):
    if n >= 1000: return wd(n // 1000) + ' thousand' + ('' if n % 1000 == 0 else ' ' + wd(n % 1000))
    if n < 20: return ONES[n]
    if n < 100: return TENS[n // 10] + ('' if n % 10 == 0 else '-' + ONES[n % 10])
    return ONES[n // 100] + ' hundred' + ('' if n % 100 == 0 else ' ' + wd(n % 100))

# ---------------------------------------------------------------- 2.A compose / decompose
def a_compose():
    n = R.randint(120, 1199); th, h, t, o = n // 1000, n // 100 % 10, n // 10 % 10, n % 10
    parts = ([pl(th, 'thousand')] if th else []) + [pl(h, 'hundred'), pl(t, 'ten'), pl(o, 'one')]
    txt = ', '.join(parts[:-1]) + ', and ' + parts[-1]
    cand = [n + 10, n - 10, n + 100, n - 100, int(f"{th or ''}{h}{o}{t}"), int(f"{th or ''}{t}{h}{o}")]
    wr = [cm(c) for c in cand if 100 <= c <= 1299 and c != n]
    return mk('2.A', 2, f"Which number is {txt}?", cm(n), wr, f"Put each digit in its place to get {cm(n)}.", CK(f"{th}*1000+{h}*100+{t}*10+{o}"))

def a_other_way():
    h = R.randint(2, 9); t = R.randint(1, 8); o = R.randint(1, 9); n = h * 100 + t * 10 + o
    s = lambda a, b, c: f"{pl(a, 'hundred')}, {pl(b, 'ten')}, {pl(c, 'one')}"
    return mk('2.A', 3, f"Which is another way to make {n}?", s(h - 1, t + 10, o),
              [s(h - 1, t + 1, o), s(h - 1, t + 10, o + 1), s(h + 1, t, o), s(h, t + 10, o), s(h - 1, t + 9, o)],
              f"{h - 1} hundreds is {(h - 1) * 100}, and {t + 10} tens is {(t + 10) * 10}. {(h - 1) * 100} + {(t + 10) * 10} + {o} = {n}.")

def a_fill():
    h, t, o = R.randint(1, 9), R.randint(1, 9), R.randint(1, 9); n = h * 100 + t * 10 + o
    return mk('2.A', 2, f"{n} = {h} hundreds + □ tens + {o} ones. What number goes in the box?", t, [o, h, t + 1, t * 10 if t * 10 != t else 5],
              f"The digit in the tens place of {n} is {t}.", CS(f"{t}"))

# ---------------------------------------------------------------- 2.B standard / word / expanded
def b_expanded():
    n = R.choice([R.randint(120, 999), R.randint(1001, 1199)])
    terms = [x for x in (n // 1000 * 1000, n // 100 % 10 * 100, n // 10 % 10 * 10, n % 10) if x]
    f = lambda l: ' + '.join(cm(x) for x in l)
    wr = []
    for i in range(len(terms)):
        t2 = terms[:]; t2[i] = t2[i] * 10 if t2[i] < 1000 else t2[i] // 10; wr.append(f(t2))
        if terms[i] >= 10:
            t3 = terms[:]; t3[i] = terms[i] // 10; wr.append(f(t3))
    return mk('2.B', 3, f"Which is the expanded form of {cm(n)}?", f(terms), wr, "Write the value of each digit and add the values.")

def b_from_words():
    n = R.randint(120, 1199)
    if n % 100 == 0: return False
    perms = sorted({int(''.join(p)) for p in itertools.permutations(str(n)) if p[0] != '0'} - {n})
    if len(perms) < 3: return False
    return mk('2.B', 3, f"Which number is written as “{wd(n)}”?", cm(n), [cm(p) for p in R.sample(perms, 3)], f"{wd(n)} is {cm(n)}.")

def b_to_words():
    n = R.randint(120, 1199)
    if n % 100 == 0: return False
    perms = sorted({int(''.join(p)) for p in itertools.permutations(str(n)) if p[0] != '0'} - {n})
    if len(perms) < 3: return False
    return mk('2.B', 3, f"Which is the word form of {cm(n)}?", wd(n), [wd(p) for p in R.sample(perms, 3)], f"{cm(n)} is written {wd(n)}.")

# ---------------------------------------------------------------- 2.C greater / less
def c_gl():
    n = R.randint(150, 1100); up = R.random() < .5
    if up:
        right = n + R.choice([7, 20, 55, 100, 230]); wr = [n, n - R.choice([3, 20]), n - R.choice([40, 90]), n - R.choice([110, 200])]
    else:
        right = n - R.choice([7, 20, 55, 100, 120]); wr = [n, n + R.choice([3, 20]), n + R.choice([40, 90]), n + R.choice([110, 200])]
    return mk('2.C', 2, f"Which number is {'greater' if up else 'less'} than {cm(n)}?", cm(right), [cm(w) for w in wr],
              f"{cm(right)} is {'greater' if up else 'less'} than {cm(n)}.")

# ---------------------------------------------------------------- 2.D compare / order
def d_symbol():
    k = R.randint(0, 2)
    if k == 0:
        a = R.randint(150, 1100); b = a + R.choice([-110, -10, -1, 1, 10, 100, 110]); sa, sb = cm(a), cm(b)
    elif k == 1:
        a = R.randint(150, 999); h, t, o = a // 100, a // 10 % 10, a % 10; b = a + R.choice([0, 0, 10, -10, 100])
        sa = f"{h * 100} + {t * 10} + {o}"; sb = cm(b)
    else:
        a = R.randint(1000, 1199); b = R.randint(900, 999); sa, sb = cm(a), cm(b)
        if R.random() < .5: a, b, sa, sb = b, a, sb, sa
    right = LT if a < b else GT if a > b else EQ
    return mk('2.D', 2 if k == 2 else 3, f"Which symbol makes this statement true?  {sa} ___ {sb}", right, [LT, GT, EQ],
              "Compare the digits from the greatest place value.", need=2)

def d_order():
    base = R.randint(1, 10) * 100; ns = R.sample(range(base, base + 99), 3)
    asc = sorted(ns); up = R.random() < .6; ans = asc if up else asc[::-1]
    wr = [ans[::-1], [ans[1], ans[0], ans[2]], [ans[0], ans[2], ans[1]]]
    f = lambda l: ', '.join(cm(x) for x in l)
    return mk('2.D', 3, f"Which list shows the numbers in order from {'least to greatest' if up else 'greatest to least'}?  {', '.join(cm(x) for x in R.sample(ns, 3))}", f(ans), [f(w) for w in wr],
              "Compare the digits from the left, starting with the greatest place value.")

def d_extreme():
    base = R.randint(2, 10) * 100; ns = R.sample(range(base, base + 99), 4)
    big = R.random() < .5
    return mk('2.D', 2, f"Which is the {'greatest' if big else 'least'} number?  " + ',  '.join(cm(x) for x in ns), cm(max(ns) if big else min(ns)), [cm(x) for x in ns],
              "Line up the digits by place value and compare from the left.")

# ---------------------------------------------------------------- 2.E / 2.F number line
def e_pos():
    lo = R.choice([0, 100, 200, 300, 500, 700, 900]); hi = lo + 100; spot = R.choice(['left', 'mid', 'right', 'out'])
    n = {'left': lo + R.choice([8, 10, 12]), 'mid': lo + R.choice([48, 50, 52]), 'right': lo + R.choice([88, 90, 92]), 'out': hi + R.choice([30, 60, 100])}[spot]
    opts = {'left': "near the left end", 'mid': "near the middle", 'right': "near the right end", 'out': "past the right end, so it does not fit"}
    why = {'left': f"{n} is just a little more than {lo}, so it is near the left end.", 'mid': f"{n} is about halfway between {lo} and {hi}.",
           'right': f"{n} is just a little less than {hi}, so it is near the right end.", 'out': f"{n} is greater than {hi}, so it is past the end of this number line."}
    return mk('2.E', 3, f"An open number line starts at {lo} on the left and ends at {hi} on the right. Where would you put {n}?", opts[spot],
              [v for k, v in opts.items() if k != spot], why[spot])

def e_between():
    lo = R.randrange(100, 1000, 20); hi = lo + R.choice([20, 40]); mid = (lo + hi) // 2
    wr = [lo - R.choice([5, 15]), hi + R.choice([5, 15]), hi + R.choice([60, 100]), lo - R.choice([40, 80])]
    return mk('2.E', 2, f"Which number belongs between {lo} and {hi} on a number line?", mid, wr, f"{mid} is greater than {lo} and less than {hi}.", CS(f"({lo}+{hi})//2"))

def f_name():
    step = R.choice([1, 2, 5, 10, 20, 25, 100]); k = R.randint(2, 8); start = step * R.randint(0, 6 if step >= 20 else 12)
    v = start + k * step
    if v > 1200: return False
    return mk('2.F', 3, f"A number line is marked by counting by {step}s. The first mark is {start}. A point is on the {ORD[k]} mark after {start}. What number does the point show?", v,
              [v - step, v + step, k * step, start + k], f"Count by {step}s {k} times from {start}: {v}.", CS(f"{start}+{k}*{step}"))

# ---------------------------------------------------------------- strand 3 fractions
SH = ["pizza", "sandwich", "ribbon", "pan of brownies", "sheet of paper", "garden bed"]
FR = {2: "a half", 4: "a fourth", 8: "an eighth"}; FP = {2: "halves", 4: "fourths", 8: "eighths"}
def p3A_name():
    n = R.choice([2, 4, 8]); s = R.choice(SH)
    return mk('3.A', 2, f"A {s} is split into {n} equal parts. What word names ONE of the parts?", FR[n], [v for k, v in FR.items() if k != n] + ["a whole"], f"{n} equal parts: each part is {FR[n]}.")

def p3A_count():
    n = R.choice([2, 4, 8]); s = R.choice(SH)
    return mk('3.A', 2, f"A {s} is cut into {FP[n]}. How many equal parts is it cut into?", n, [x for x in (2, 4, 8, 3, 6) if x != n], f"{FP[n].capitalize()} means {n} equal parts.", CS(f"{n}"))

def p3B():
    a, b = R.choice([(2, 4), (2, 8), (4, 8)]); x, y = R.sample(NM, 2); s = R.choice(["pizza", "sandwich", "pancake", "sheet cake"])
    if R.random() < .5: a, b = b, a
    right = f"{x}'s pieces" if a < b else f"{y}'s pieces"
    return mk('3.B', 3, f"{x} cuts a {s} into {a} equal pieces. {y} cuts an identical {s} into {b} equal pieces. Whose pieces are larger?", right,
              [f"{y}'s pieces" if a < b else f"{x}'s pieces", "The pieces are the same size."],
              "The more equal parts a whole is cut into, the smaller each part is.", need=2)

def p3C_cmp():
    d = R.choice([2, 4, 8]); n = R.choice([1, d - 1, d, d + 1, d + 2, d + 3]) if d > 2 else R.choice([1, 2, 3, 4]); x = who(); s = R.choice(["pizza", "sandwich", "cake"])
    right = "more than 1 whole" if n > d else "exactly 1 whole" if n == d else "less than 1 whole"
    return mk('3.C', 3, f"{x} eats {n} {FP[d] if n != 1 else FP[d][:-1] if d != 2 else 'half'} of a {s}. We know {d} {FP[d]} make 1 whole {s}. How much did {x} eat?", right,
              [v for v in ("more than 1 whole", "exactly 1 whole", "less than 1 whole") if v != right], f"{d} {FP[d]} make 1 whole. {n} compared with {d} is {right}.", need=2)

def p3C_whole():
    d = R.choice([2, 4, 8])
    return mk('3.C', 2, f"How many {FP[d]} does it take to make 1 whole?", d, [x for x in (2, 3, 4, 6, 8, 10) if x != d], f"It takes {d} {FP[d]} to make 1 whole.", CS(f"{d}"))

# ---------------------------------------------------------------- strand 4 add / subtract
def q4A_add():
    a = R.randint(6, 12); b = R.randint(20 - a - 6 if 20 - a - 6 > 3 else 3, 20 - a) if 20 - a >= 3 else 3; s = a + b
    if s > 20: return False
    return mk('4.A', 2, f"What is {a} + {b}?", s, [s + 1, s - 1, s + 2, s - 2, a - b if a > b else s + 10], f"{a} + {b} = {s}.", CS(f"{a}+{b}"))

def q4A_sub():
    a = R.randint(11, 20); b = R.randint(3, 9); s = a - b
    return mk('4.A', 2, f"What is {a} − {b}?", s, [s + 1, s - 1, s + 2, a + b if a + b <= 25 else s + 3], f"{a} − {b} = {s}.", CS(f"{a}-{b}"))

def q4A_miss():
    a = R.randint(4, 12); t = R.randint(a + 2, 20); b = t - a
    return mk('4.A', 3, f"What number makes this true?  {a} + □ = {t}", b, [b + 1, b - 1, t + a if t + a <= 30 else b + 2, t], f"{t} − {a} = {b}, so □ is {b}.", CS(f"{t}-{a}"))

def q4B_four():
    k = R.choice([3, 4]); ns = [R.randint(11, 49) for _ in range(k)]; s = sum(ns)
    return mk('4.B', 3, "What is " + ' + '.join(map(str, ns)) + "?", s, [s + 10, s - 10, s + 1, s - 1, s + 20], "Add the tens, add the ones, then put them together.", CS("+".join(map(str, ns))))

def q4B_sub():
    a = R.randint(51, 95); b = R.randint(18, a - 12)
    if a % 10 >= b % 10: return False
    s = a - b
    return mk('4.B', 3, f"What is {a} − {b}?", s, [s + 10, s - 10, s + 2, s - 2, b - a if b > a else s + 20, (a // 10 - b // 10) * 10 + abs(a % 10 - b % 10)], f"Regroup 1 ten as 10 ones: {a} − {b} = {s}.", CS(f"{a}-{b}"))

def q4C_one():
    a = R.randint(120, 690); b = R.randint(110, 999 - a); x = who()
    if R.random() < .5:
        s = a + b; q = R.choice([f"{x} has {a} stickers. A friend gives {x} {b} more. How many stickers does {x} have now?", f"A school sold {a} tickets on Friday and {b} tickets on Saturday. How many tickets were sold in all?"])
        return mk('4.C', 2, q, s, [s + 10, s - 10, s + 100, s - 100, abs(a - b)], f"{a} + {b} = {s}.", CS(f"{a}+{b}"))
    b = R.randint(110, a - 20); s = a - b
    q = R.choice([f"A farm stand had {a} apples. It sold {b} apples. How many apples are left?", f"There were {a} students at a game. {b} students went home. How many students stayed?"])
    return mk('4.C', 2, q, s, [s + 10, s - 10, s + 100, s - 100, a + b if a + b < 1000 else s + 1], f"{a} − {b} = {s}.", CS(f"{a}-{b}"))

def q4C_two():
    a = R.randint(150, 450); b = R.randint(120, 400); c = R.randint(60, a + b - 100); s = a + b - c
    q = R.choice([f"A store had {a} red pens and {b} blue pens. It sold {c} pens. How many pens are left?", f"A bakery made {a} muffins in the morning and {b} muffins in the afternoon. It sold {c} muffins. How many muffins are left?"])
    return mk('4.C', 4, q, s, [a + b + c if a + b + c < 1000 else s + 100, s + 10, s - 10, s + 100], f"({a} + {b}) − {c} = {s}.", CS(f"{a}+{b}-{c}"))

ADD_ST = ["{x} has {a} marbles and finds {b} more. How many marbles does {x} have now?", "A bag has {a} red beads and {b} blue beads. How many beads are in the bag?",
          "{x} saves {a} dollars one month and {b} dollars the next month. How many dollars has {x} saved in all?"]
SUB_ST = ["{x} has {a} cards and gives {b} cards away. How many cards are left?", "A shelf holds {a} books. {b} books are taken off. How many books are left on the shelf?",
          "{x} has {a} grapes and eats {b} of them. How many grapes are left?"]
def q4D_story():
    a = R.randint(150, 800); b = R.randint(60, 140); x = who(); plus = R.random() < .5
    right_pool, wrong_pool = (ADD_ST, SUB_ST) if plus else (SUB_ST, ADD_ST)
    sent = f"{a} {'+' if plus else '−'} {b}"
    return mk('4.D', 3, f"Which story can be solved with {sent}?", R.choice(right_pool).format(x=x, a=a, b=b), [s.format(x=x, a=a, b=b) for s in wrong_pool],
              f"{sent} " + ("joins two amounts together." if plus else "takes an amount away."))

# ---------------------------------------------------------------- strand 5 money
COIN = [("penny", 1, "pennies"), ("nickel", 5, "nickels"), ("dime", 10, "dimes"), ("quarter", 25, "quarters")]
def coin_set():
    picks = R.sample(COIN, R.choice([2, 3])); cs = [R.randint(1, 4) for _ in picks]
    tot = sum(c * p[1] for c, p in zip(cs, picks))
    parts = [f"{c} {p[0] if c == 1 else p[2]}" for c, p in zip(cs, picks)]
    txt = ", ".join(parts[:-1]) + (", and " if len(parts) > 2 else " and ") + parts[-1]
    return txt, tot, "+".join(f"{c}*{p[1]}" for c, p in zip(cs, picks))

def m5A():
    txt, tot, expr = coin_set()
    if not 11 <= tot <= 100: return False
    return mk('5.A', 2 if tot < 60 else 3, f"Ava has {txt}. How much money does Ava have?", money(tot), [money(w) for w in (tot + 5, tot - 5, tot + 10, tot - 10, tot + 1)],
              f"Add the coin values: {expr.replace('*', ' × ').replace('+', ' + ')} = {tot} cents.", mchk(expr, tot))

def m5B():
    txt, tot, expr = coin_set()
    if not 11 <= tot <= 99: return False
    return mk('5.B', 3, f"Ben has {txt}. Which shows his money using a dollar sign and a decimal point?", dollars(tot),
              [f"${tot}.00", f"${tot / 10:.2f}", f"${str(tot)[::-1][0]}.{str(tot)[::-1][1:]}" if False else f"$0.{str(tot)[::-1]}", f"{tot}¢"],
              f"{tot} cents is {dollars(tot)}.")

def m5B_conv():
    c = R.choice([15, 20, 35, 45, 60, 65, 75, 80, 95])
    return mk('5.B', 2, f"Which is another way to write {c}¢?", dollars(c), [f"${c}.00", f"${c / 10:.1f}0", f"${c}", "$0." + str(c)[::-1]], f"{c} cents is {dollars(c)}.")

def m5B_over():
    d = R.choice([1, 2]); r = R.choice([5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 75]); tot = d * 100 + r
    return mk('5.B', 4, f"Dev has {d} dollar {'bill' if d == 1 else 'bills'} and coins worth {r}¢. Which shows how much money Dev has?", dollars(tot), [f"${d}.{r}0" if r < 10 else f"${r}.{d}0", f"${d}{r}", f"${tot}.00", f"${d + 1}.{r:02d}"],
              f"{d} dollar{'s' if d > 1 else ''} + {r} cents = {dollars(tot)}.")

# ---------------------------------------------------------------- strand 6 multiplication / division situations
CT = [("plates", "cookies"), ("baskets", "apples"), ("vases", "flowers"), ("bags", "marbles"), ("boxes", "crayons"), ("shelves", "books")]
def x6A_add():
    g = R.randint(2, 5); s = R.choice([2, 3, 4, 5, 10]); c, t = R.choice(CT); tot = g * s
    right = ' + '.join([str(s)] * g) + f" = {tot}"
    wr = [' + '.join([str(s)] * (g + 1)) + f" = {tot + s}", (' + '.join([str(s)] * (g - 1)) + f" = {tot - s}") if g > 2 else (' + '.join([str(s)] * (g + 2)) + f" = {tot + 2 * s}"), f"{g} + {s} = {g + s}"]
    return mk('6.A', 3, f"There are {g} {c} with {s} {t} in each. Which addition sentence shows the total number of {t}?", right, wr, f"{g} equal groups of {s} is {' + '.join([str(s)] * g)} = {tot}.")

def x6A_total():
    g = R.randint(2, 5); s = R.choice([2, 3, 4, 5, 10]); c, t = R.choice(CT); tot = g * s
    return mk('6.A', 2, f"There are {g} {c} with {s} {t} in each. How many {t} are there in all?", tot, [g + s, tot + s, tot - s if tot - s > 0 else tot + 2, tot + 1], f"{g} groups of {s} is {tot}.", CS(f"{g}*{s}"))

def x6B_each():
    g = R.randint(2, 5); k = R.randint(2, 6); c, t = R.choice(CT); tot = g * k
    return mk('6.B', 2, f"{tot} {t} are shared equally among {g} {c}. How many {t} are on each?", k, [k + 1, k - 1, tot + g, g], f"{tot} ÷ {g} = {k}.", CS(f"{tot}//{g}"))

def x6B_groups():
    g = R.randint(2, 6); k = R.choice([2, 3, 4, 5]); tot = g * k; x = who()
    return mk('6.B', 2, f"{x} has {tot} stickers and puts {k} stickers on each card. How many cards does {x} fill?", g, [g + 1, g - 1, k, tot - k], f"{tot} ÷ {k} = {g}.", CS(f"{tot}//{k}"))

# ---------------------------------------------------------------- strand 7 number sense
def n7A():
    ev = R.random() < .5; pool = [n for n in range(2, 41)]
    right = R.choice([n for n in pool if (n % 2 == 0) == ev]); wr = R.sample([n for n in pool if (n % 2 == 0) != ev], 3)
    return mk('7.A', 2, f"Which number is {'even' if ev else 'odd'}?", right, wr,
              f"{right} {'can be put in pairs with none left over' if ev else 'has one left over when put in pairs'}, so it is {'even' if ev else 'odd'}.")

def n7A_pairs():
    n = R.randint(5, 39); x = who(); ev = n % 2 == 0; s = R.choice(["crayons", "shoes", "buttons", "stickers"])
    return mk('7.A', 2, f"{x} puts {n} {s} into pairs. Which statement is true?", f"{n} is {'even' if ev else 'odd'}.", [f"{n} is {'odd' if ev else 'even'}."],
              f"{n} " + ("makes pairs with none left over, so it is even." if ev else "leaves one {0} without a partner, so it is odd.".format(s[:-1])), need=1)

def n7B():
    n = R.randint(30, 1150); k = R.choice([10, 100]); up = R.random() < .5; sg = 1 if up else -1; v = n + sg * k
    if not 0 <= v <= 1200: return False
    wr = [n + sg, n + sg * (100 if k == 10 else 10), n - sg * k, v + 1]
    return mk('7.B', 2, f"What is {k} {'more' if up else 'less'} than {cm(n)}?", cm(v), [cm(w) for w in wr if 0 <= w <= 1300],
              f"{'Add' if up else 'Subtract'} {k} {'to' if up else 'from'} {cm(n)}: {cm(v)}.", CK(f"{n}{'+' if up else '-'}{k}"))

def n7C():
    k = R.randint(0, 3); a = R.randint(14, 60); b = R.randint(12, 50); c = a + b; x = who()
    if k == 0:
        q = f"{x} had {a} stickers. Then {x} got some more. Now {x} has {c} stickers. How many stickers did {x} get?"; right = b; wr = [c, a, c + a, b + 1]; ex = f"{c} − {a} = {b}"; ck = f"{c}-{a}"; ck = f"{c}-{a}"
    elif k == 1:
        q = f"{x} had some marbles. Then {x} found {b} more. Now {x} has {c} marbles. How many marbles did {x} have at first?"; right = a; wr = [c, b, c + b, a + 1]; ex = f"{c} − {b} = {a}"; ck = f"{c}-{b}"
    elif k == 2:
        q = f"{x} had {c} cards. {x} gave some cards away. Now {x} has {a} cards. How many cards did {x} give away?"; right = b; wr = [c, a, c + a, b - 1]; ex = f"{c} − {a} = {b}"; ck = f"{c}-{a}"
    else:
        q = f"{x} had some grapes. {x} ate {b} grapes. Now {x} has {a} grapes. How many grapes did {x} have at first?"; right = c; wr = [a, b, c - 1, c + 10]; ex = f"{a} + {b} = {c}"; ck = f"{a}+{b}"
    return mk('7.C', 2 + (k > 0), q, right, wr, ex + ".", CS(ck))

# ---------------------------------------------------------------- strand 8 geometry
POLY = [(3, "triangle"), (4, "quadrilateral"), (5, "pentagon"), (6, "hexagon"), (8, "octagon")]
def g8A():
    n, nmz = R.choice(POLY); wr = [p for k, p in POLY if k != n]
    return mk('8.A', 2, f"A shape has exactly {n} sides and {n} vertices. What is the shape called?", nmz, wr, f"A shape with {n} sides and {n} vertices is {an(nmz)} {nmz}.")

def g8C_vert():
    n, nmz = R.choice(POLY)
    return mk('8.C', 2, f"How many vertices does {an(nmz)} {nmz} have?", n, [x for x in (3, 4, 5, 6, 8, 10) if x != n], f"{an(nmz).capitalize()} {nmz} has {n} sides and {n} vertices.", CS(f"{n}"))

def g8C_most():
    ps = R.sample(POLY, 4); big = R.random() < .5; pick = max(ps) if big else min(ps)
    return mk('8.C', 3, f"Which shape has the {'most' if big else 'fewest'} sides?", pick[1], [p[1] for p in ps if p != pick], f"{an(pick[1]).capitalize()} {pick[1]} has {pick[0]} sides.")

SOL = ["sphere", "cone", "cylinder", "rectangular prism", "cube", "triangular prism"]
OBJS = [("a basketball", "sphere"), ("a globe", "sphere"), ("a soup can", "cylinder"), ("a drum", "cylinder"), ("a party hat", "cone"), ("an ice-cream cone", "cone"),
        ("a shoe box", "rectangular prism"), ("a brick", "rectangular prism"), ("a game die", "cube"), ("a square block with 6 equal square faces", "cube"), ("a camping tent shaped like a roof", "triangular prism")]
def g8B():
    o, s = R.choice(OBJS); pool = [x for x in SOL if x != s and not (s == "cube" and x == "rectangular prism") and not (s == "rectangular prism" and x == "cube")]
    return mk('8.B', 2, f"Which solid has the shape of {o}?", s, R.sample(pool, 3), f"{o.capitalize()} is shaped like a {s}.")

# ---------------------------------------------------------------- strand 9 measurement
UNITS = {"inch": ("inches", ["paper clips", "connecting cubes"]), "centimeter": ("centimeters", ["centimeter cubes", "unit blocks"]), "foot": ("feet", ["floor tiles", "wooden rulers"])}
def l9A():
    n = R.randint(4, 12); u = R.choice(list(UNITS)); pu, its = UNITS[u]; it = R.choice(its); ob = R.choice(["pencil", "ribbon", "strip of paper", "crayon"]) if u != "foot" else R.choice(["rug", "hallway mat", "bookshelf"])
    if R.random() < .5:
        return mk('9.A', 2, f"A {ob} is as long as {n} {it} lined up end to end with no gaps. Each one is 1 {u} long. How long is the {ob}?", f"{n} {pu}", [f"{n + 1} {pu}", f"{n - 1} {pu}", f"{n * 2} {pu}"], f"{n} pieces that are each 1 {u} long make {n} {pu}.")
    k = R.choice([2, 3, 5]); return mk('9.A', 3, f"A {ob} is as long as {n} {it} lined up end to end. Each one is {k} {pu} long. How long is the {ob}?", f"{n * k} {pu}", [f"{n + k} {pu}", f"{n} {pu}", f"{n * k + k} {pu}"], f"{n} × {k} = {n * k} {pu}.")

UP = [("inches", "feet"), ("feet", "yards"), ("centimeters", "meters"), ("inches", "yards")]
def l9B():
    s, l = R.choice(UP); x, y = R.sample(NM, 2); ob = R.choice(["desk", "hallway", "rug", "bookshelf"])
    if R.random() < .5: x, y = y, x
    return mk('9.B', 3, f"{x} measures a {ob} in {s}. {y} measures the same {ob} in {l}. Who gets the greater number?", f"{x}, because {s} are shorter units", [f"{y}, because {l} are shorter units", "They get the same number."],
              f"A shorter unit means you need more of them. {s.capitalize()} are shorter than {l}.", need=2)

def l9C_dist():
    a = R.randint(1, 30); b = R.randint(1, 40)
    if a == b: return False
    x = who()
    return mk('9.C', 3, f"A frog sits at {a} on a number line and hops to {b}. How far did the frog hop?", abs(b - a), [abs(b - a) + 1, abs(b - a) - 1 if abs(b - a) > 1 else 3, a + b, max(a, b)], f"The distance from {a} to {b} is {abs(b - a)}.", CS(f"abs({b}-{a})"))

def l9C_hop():
    a = R.randint(2, 30); d = R.randint(3, 15); r = R.random() < .5; v = a + d if r else a - d
    if v < 0: return False
    return mk('9.C', 3, f"A bug starts at {a} on a number line and hops {d} spaces to the {'right' if r else 'left'}. What number does it land on?", v, [a + d if not r else a - d, v + 1, v - 1, d], f"{a} {'+' if r else '−'} {d} = {v}.", CS(f"{a}{'+' if r else '-'}{d}"))

def l9D():
    k = R.randint(2, 9); near = R.choice([k, k + 1]); thing = R.choice(["leaf", "crayon", "straw", "key"])
    return mk('9.D', 3, f"A ruler is marked in inches. The end of a {thing} is between the {k} and {k + 1} marks, but closer to the {near} mark. To the nearest inch, how long is the {thing}?", f"{near} inches", [f"{k + 1 if near == k else k} inches", f"{k - 1} inches", f"{k + 2} inches"],
              f"The end is closest to the {near} mark, so the length is about {near} inches.")

def l9E_diff():
    a = R.randint(12, 40); b = R.randint(5, a - 4); u = R.choice(["feet", "inches", "yards", "meters"])
    return mk('9.E', 2, f"A rope is {a} {u} long. A second rope is {b} {u} long. How much longer is the first rope?", f"{a - b} {u}", [f"{a + b} {u}", f"{a - b + 2} {u}", f"{a - b - 2} {u}"], f"{a} − {b} = {a - b}.")

def l9E_sum():
    a = R.randint(12, 40); b = R.randint(5, 30); x = who(); u = R.choice(["feet", "yards", "meters"])
    return mk('9.E', 2, f"{x} walks {a} {u} and then {b} {u} more. How far did {x} walk in all?", f"{a + b} {u}", [f"{a - b} {u}", f"{a + b + 10} {u}", f"{a + b - 10} {u}"], f"{a} + {b} = {a + b}.")

def a9F():
    r = R.randint(2, 6); c = R.randint(2, 8)
    if r == c: return False
    return mk('9.F', 2, f"A rectangle is covered with {r} rows of {c} square tiles. There are no gaps or overlaps. What is the area of the rectangle?", f"{r * c} square units", [f"{r + c} square units", f"{r * c + c} square units", f"{r * c - r} square units"],
              f"{r} rows of {c} is {r} × {c} = {r * c} square units.")

# ---------------------------------------------------------------- 9.G time
def t9G_hands():
    h = R.randint(1, 12); m = R.randint(1, 11); mins = m * 5
    right = f"{h}:{mins:02d}"
    wr = [f"{m}:{h * 5 % 60:02d}" if h * 5 % 60 != mins or m != h else f"{h}:{(mins + 5) % 60:02d}", f"{h % 12 + 1}:{mins:02d}", f"{h}:{(mins + 5) % 60:02d}", f"{h}:{(mins - 5) % 60:02d}"]
    return mk('9.G', 3, f"The hour hand is between the {h} and the {h % 12 + 1}. The minute hand points to the {m}. What time does the clock show?", right, wr, f"The minute hand on the {m} means {mins} minutes after the hour, so the time is {right}.")

def t9G_marks():
    h = R.randint(1, 12); base = R.choice([0, 15, 30, 45]); k = R.randint(1, 4); mins = base + k
    return mk('9.G', 4, f"The hour hand is between the {h} and the {h % 12 + 1}. The minute hand is {k} small mark{'s' if k > 1 else ''} past the {base // 5 if base else 12}. What time is it?", f"{h}:{mins:02d}", [f"{h}:{mins + 5:02d}" if mins + 5 < 60 else f"{h}:{mins - 5:02d}", f"{h}:{base + 5 * k:02d}" if base + 5 * k < 60 and base + 5 * k != mins else f"{h}:{mins - 1:02d}", f"{h % 12 + 1}:{mins:02d}", f"{h}:{mins + 1:02d}"],
              f"Start at {base} minutes and count {k} more: {mins} minutes, so the time is {h}:{mins:02d}.")

def t9G_after():
    h = R.randint(2, 11); m = R.choice([0, 5, 10, 15, 20, 30, 35, 40]); d = R.choice([5, 8, 10, 12, 15, 17]); tm = h * 60 + m + d
    if tm % 60 >= 60 or tm // 60 > 12: return False
    s0 = clock(h * 60 + m); s1 = clock(tm)
    return mk('9.G', 3, f"What time is {d} minutes after {s0}?", s1, [clock(tm + 1), clock(tm - 1), clock(tm + 10), clock(tm - d)], f"{s0} plus {d} minutes is {s1}.", f"'{s1}'")

# ================================================================= run the generators
rep(3, a_compose); rep(2, a_other_way); rep(2, a_fill)
rep(2, b_expanded); rep(2, b_from_words); rep(2, b_to_words)
rep(4, c_gl)
rep(3, d_symbol); rep(2, d_order); rep(2, d_extreme)
rep(3, e_pos); rep(2, e_between); rep(5, f_name)
rep(2, p3A_name); rep(2, p3A_count); rep(3, p3B); rep(3, p3C_cmp); rep(2, p3C_whole)
rep(3, q4A_add); rep(3, q4A_sub); rep(2, q4A_miss); rep(3, q4B_four); rep(3, q4B_sub); rep(3, q4C_one); rep(2, q4C_two); rep(4, q4D_story)
rep(4, m5A); rep(3, m5B); rep(2, m5B_conv); rep(2, m5B_over)
rep(3, x6A_add); rep(2, x6A_total); rep(3, x6B_each); rep(3, x6B_groups)
rep(3, n7A); rep(2, n7A_pairs); rep(5, n7B); rep(5, n7C)
rep(3, g8A); rep(3, g8C_vert); rep(2, g8C_most); rep(5, g8B)
rep(3, l9A); rep(3, l9B); rep(2, l9C_dist); rep(2, l9C_hop); rep(3, l9D); rep(2, l9E_diff); rep(2, l9E_sum); rep(4, a9F)
rep(3, t9G_hands); rep(2, t9G_marks); rep(3, t9G_after)

# ================================================================= hand-written items (concepts that need wording)
H('3.D', 2, "Which shows a shape cut into fourths?", "A square cut into 4 equal parts", ["A square cut into 4 parts that are not equal", "A square cut into 2 equal parts", "A square cut into 3 equal parts"], "Fourths are 4 EQUAL parts.")
H('3.D', 2, "A pizza is cut into 8 parts, but the parts are not the same size. Are the parts eighths?", "No, because the parts are not equal.", ["Yes, because there are 8 parts.", "Yes, because it is a pizza.", "No, because eighths are too small."], "Eighths must be 8 EQUAL parts.", need=3)
H('3.D', 3, "Which is NOT an example of a half?", "A rectangle cut into 2 parts of different sizes", ["A circle cut into 2 equal parts", "A square cut into 2 equal parts", "A rectangle cut into 2 equal parts"], "A half is one of 2 EQUAL parts.")
H('3.D', 3, "Mia says a ribbon cut into 4 parts is cut into fourths. What must be true for Mia to be right?", "All 4 parts are the same size.", ["All 4 parts are different sizes.", "The ribbon is red.", "The parts are all shorter than 4 inches."], "Fourths are 4 equal-sized parts.")
H('3.D', 2, "Which shape is split into 2 equal parts (halves)?", "A circle with a line straight through its center", ["A circle with a line near one edge", "A square split into 3 parts", "A rectangle split into 4 equal parts"], "A line through the center of a circle makes 2 equal parts.")
H('3.B', 3, "A sandwich is cut into halves. Another identical sandwich is cut into fourths. Which piece is larger?", "one half", ["one fourth", "They are the same size.", "It is impossible to tell."], "Fewer equal parts means each part is larger, so a half is larger than a fourth.")
H('3.B', 3, "Which statement is true?", "One eighth of a pizza is smaller than one fourth of the same pizza.", ["One eighth of a pizza is larger than one fourth of the same pizza.", "One eighth and one fourth are the same size.", "One eighth is larger than one half of the same pizza."], "More parts means smaller parts: eighths are smaller than fourths.")
H('6.A', 3, "Which situation is multiplication, joining equal groups?", "4 bags with 3 apples in each bag, how many apples in all", ["12 apples shared equally among 4 bags", "7 apples and 3 more apples", "12 apples and 4 are eaten"], "Joining equal groups is multiplication.")
H('6.B', 3, "Which situation is division, splitting a set into equal groups?", "15 grapes are shared equally among 3 friends", ["3 friends each have 5 grapes, how many in all", "15 grapes and 3 more grapes", "3 groups of 5 grapes are put in a bowl"], "Sharing a set equally into groups is division.")
H('7.A', 2, "Which number is odd?", "17", ["14", "30", "26"], "17 leaves one left over when put into pairs.")
H('8.A', 3, "A shape has 4 sides and 4 vertices. Which shape could it be?", "a rectangle", ["a triangle", "a pentagon", "a circle"], "A rectangle has 4 sides and 4 vertices.")
H('8.A', 3, "Which shape has 3 sides and 3 vertices?", "triangle", ["rectangle", "pentagon", "hexagon"], "A triangle has 3 sides and 3 vertices.")
H('8.B', 3, "Which solid has no flat faces and no vertices?", "sphere", ["cone", "cylinder", "cube"], "A sphere is completely curved.")
H('8.B', 3, "Which solid has 2 flat circular faces and 1 curved surface?", "cylinder", ["cone", "sphere", "rectangular prism"], "A cylinder has two circular faces joined by a curved surface.")
H('8.B', 3, "Which solid has 6 faces that are all rectangles or squares?", "rectangular prism", ["cone", "triangular prism", "sphere"], "A rectangular prism has 6 rectangular faces (a cube's are all squares).")
H('8.C', 3, "Which polygon has 6 sides?", "hexagon", ["pentagon", "octagon", "triangle"], "A hexagon has 6 sides and 6 vertices.")
H('8.C', 3, "A polygon has 8 sides. How many vertices does it have?", "8", ["4", "6", "16"], "A polygon has the same number of vertices as sides.")
H('8.D', 3, "Two identical squares are put side by side so that they touch along one whole side, with no gaps. What shape is made?", "rectangle", ["triangle", "circle", "pentagon"], "Two squares joined along a side make a longer rectangle.")
H('8.D', 3, "Three identical squares are put in a row, touching side to side. How many sides does the new shape have?", "4", ["3", "6", "12"], "The new shape is a rectangle, and a rectangle has 4 sides.")
H('8.D', 4, "Which 2-D shapes make up the faces of a triangular prism?", "2 triangles and 3 rectangles", ["4 triangles", "6 squares", "2 circles and 1 rectangle"], "A triangular prism has 2 triangular ends and 3 rectangular sides.")
H('8.D', 3, "How many square faces does a cube have?", "6", ["4", "8", "12"], "A cube has 6 faces and each one is a square.")
H('8.E', 3, "A rectangle is cut from one corner to the opposite corner. What two shapes are made?", "2 triangles", ["2 squares", "2 circles", "1 triangle and 1 square"], "A diagonal cut splits a rectangle into 2 triangles.")
H('8.E', 3, "A rectangle is cut into 4 identical parts. Each part is what fraction of the rectangle?", "one fourth", ["one half", "one eighth", "one whole"], "4 equal parts: each is one fourth.")
H('8.E', 3, "A square is cut into 2 equal parts along a line from the middle of the top to the middle of the bottom. What shapes are made?", "2 rectangles", ["2 triangles", "2 circles", "4 squares"], "A straight cut down the middle makes 2 equal rectangles.")
H('9.B', 3, "A table is 6 feet long. Which measurement for the same table has the greatest number?", "72 inches", ["2 yards", "6 feet", "1 meter"], "Inches are the smallest unit here, so the number is the greatest: 6 feet = 72 inches.")
H('9.C', 3, "On a number line, 5 is at one point and 12 is at another. How far apart are the points?", "7", ["5", "17", "8"], "12 − 5 = 7.")
H('9.D', 2, "Which tool is best for measuring the length of a pencil?", "a ruler", ["a clock", "a measuring cup", "a balance scale"], "A ruler measures length in inches or centimeters.")
H('9.D', 2, "Which tool is best for measuring how far it is across the gym floor?", "a measuring tape", ["a ruler that is 12 inches long", "a clock", "a thermometer"], "A long measuring tape can measure long distances.")
H('9.E', 3, "Which is the best estimate for the length of a new pencil?", "7 inches", ["7 feet", "7 yards", "7 miles"], "A new pencil is about 7 inches long.")
H('9.E', 3, "Which is the best estimate for the height of a classroom door?", "7 feet", ["7 inches", "7 miles", "70 yards"], "A classroom door is about 7 feet tall.")
H('9.E', 3, "Which is the best estimate for the length of a paper clip?", "1 inch", ["1 foot", "1 yard", "1 mile"], "A paper clip is about 1 inch long.")
H('9.F', 2, "Area is the number of units that cover a flat shape with no gaps or overlaps. Which units measure area?", "square units", ["inches only", "cubic units", "hours"], "Area is counted in square units.")
H('9.F', 3, "A rectangle is 3 tiles long and 4 tiles wide. How many square tiles cover it?", "12", ["7", "14", "10"], "3 × 4 = 12 square tiles.")
H('9.G', 2, "Which time is best for eating breakfast?", "7:30 a.m.", ["7:30 p.m.", "12:30 a.m.", "2:30 a.m."], "Breakfast is the first meal in the morning (a.m.).")
H('9.G', 2, "Which time is best for going to bed on a school night?", "8:30 p.m.", ["8:30 a.m.", "12:30 p.m.", "6:00 a.m."], "Bedtime is in the evening (p.m.).")
H('9.G', 3, "School starts at 8:15 in the morning. Which shows the start time the right way?", "8:15 a.m.", ["8:15 p.m.", "20:15 a.m.", "8:15 noon"], "Morning times use a.m.")
H('9.G', 3, "Lunch is at 12:10 after the morning is over. Which shows this time?", "12:10 p.m.", ["12:10 a.m.", "10:12 p.m.", "1:20 p.m."], "Times after noon use p.m.")
H('9.G', 3, "The sun sets at 7:45 in the evening. Which shows this time?", "7:45 p.m.", ["7:45 a.m.", "5:47 p.m.", "7:54 a.m."], "Evening times use p.m.")

H('8.E', 3, "A square is cut along a line from one corner to the opposite corner. What two shapes are made?", "2 triangles", ["2 squares", "2 circles", "2 rectangles"], "A diagonal cut splits a square into 2 equal triangles.")
H('8.E', 4, "A rectangle is cut into 2 equal parts. Each part is what fraction of the rectangle?", "one half", ["one fourth", "one eighth", "one whole"], "2 equal parts: each part is one half.")
H('9.A', 2, "To measure the length of a desk with paper clips, how should you place the paper clips?", "end to end with no gaps or overlaps", ["in a stack", "with gaps between them", "overlapping each other"], "Units must go end to end with no gaps or overlaps.")
H('9.A', 3, "Lena measures a book with 1-inch cubes and uses 9 cubes in a row with no gaps. How long is the book?", "9 inches", ["10 inches", "18 inches", "9 feet"], "9 cubes that are each 1 inch long make 9 inches.")
H('5.A', 2, "Which coin is worth 10 cents?", "dime", ["penny", "nickel", "quarter"], "A dime is worth 10 cents.")
H('5.A', 2, "Which coin is worth the most?", "quarter", ["dime", "nickel", "penny"], "A quarter is worth 25 cents, more than a dime (10), nickel (5), or penny (1).")
H('5.A', 3, "Which group of coins is worth exactly 30 cents?", "1 quarter and 1 nickel", ["1 quarter and 1 dime", "3 nickels", "2 dimes and 1 penny"], "25 + 5 = 30 cents.")
H('2.C', 3, "Which number is greater than 540 but less than 560?", "550", ["535", "565", "540"], "550 is more than 540 and less than 560.")

n = B.save(os.path.join(os.path.dirname(__file__), '..', 'batches', 'g2_math.jsonl'))
print("wrote", n, "questions")

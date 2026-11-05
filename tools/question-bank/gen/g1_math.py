#!/usr/bin/env python3
"""Grade 1 Mathematics (TEKS 111.3.b) - original questions. Run: python3 gen/g1_math.py  -> batches/g1_math.jsonl"""
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('111.3.b.', 303, no_neg=True, own='g1_math.jsonl')
R, H, rep = B.R, B.hand, B.rep
from fractions import Fraction as F
_SUM = re.compile(r'[\d.]+( \+ [\d.]+)+')
def _sv(x):
    x = str(x)
    return sum((F(t) for t in x.split(' + ')), F(0)) if _SUM.fullmatch(x) else None
_mk0 = B.mk
def mk(code, d, q, right, wrong, e, chk=None, need=3):      # never leave a wrong choice that adds up to the same value as the right one
    vr = _sv(right)
    wrong = [w for w in wrong if vr is None or _sv(w) != vr]
    return _mk0(code, d, q, right, wrong, e, chk, need)
LT, GT, EQ = "less than (<)", "greater than (>)", "equal to (=)"
NM = ["Ava", "Ben", "Cara", "Dev", "Eli", "Fay", "Gus", "Hana", "Ivan", "Jo", "Kai", "Lena", "Max", "Nia", "Omar", "Pia", "Raj", "Sam", "Tia", "Zoe"]
THINGS = ["marbles", "stickers", "cards", "apples", "books", "crayons", "cookies", "balloons", "shells", "blocks"]
DIE = "⚀⚁⚂⚃⚄⚅"
def who(): return R.choice(NM)
def ws(r, ds=(1, -1, 2, -2, 3, -3, 10, -10), lo=0, hi=120):
    return [r + d for d in ds if lo <= r + d <= hi and r + d != r]
def sw(n):   # swap the digits of a two-digit number
    s = str(n); return int(s[::-1]) if len(s) == 2 and s[0] != s[1] and s[1] != '0' else None

# ---------------------------------------------------------------- 2.A recognize structured arrangements
def a_frame():
    n = R.randint(2, 10); nm = who()
    r1 = '🔴' * min(5, n) + '⚪' * (5 - min(5, n)); r2 = '🔴' * max(0, n - 5) + '⚪' * (5 - max(0, n - 5))
    return mk('2.A', 2, f"{nm} shows a ten frame:   {r1}  /  {r2}   How many red dots are in the ten frame?", n, ws(n, (1, -1, 2, -2), 0, 10), f"Count the red dots: {n}.", CS(f"{n}"))
def a_dice():
    x, y = R.randint(1, 6), R.randint(1, 6); nm = who()
    return mk('2.A', 3, f"{nm} rolls two dice and gets {DIE[x - 1]} and {DIE[y - 1]}.  How many dots are there in all?", x + y, ws(x + y, (1, -1, 2, -2), 2, 12), f"{x} + {y} = {x + y}.", CS(f"{x}+{y}"))
def a_full():
    n = R.randint(11, 20); nm = who()
    r1 = '🔴' * 10; r2 = '🔴' * (n - 10) + '⚪' * (20 - n)
    return mk('2.A', 3, f"{nm} fills one ten frame and starts a second:   {r1[:5]} {r1[5:]}  /  {r2}   How many red dots are there in all?", n, ws(n, (1, -1, 2, -2, 10), 11, 20), f"10 red dots in the full frame plus {n - 10} more is {n}.", CS(f"{n}"))
rep(3, a_frame); rep(2, a_dice); rep(2, a_full)

# ---------------------------------------------------------------- 2.B compose and decompose
def b_tens():
    n = R.randint(11, 99)
    if n % 10 == 0: return False
    t, o = n // 10, n % 10
    wr = [f"{o} tens and {t} ones", f"{t + 1} tens and {o} ones", f"{t} tens and {o + 1} ones", f"{max(t - 1, 0)} tens and {o} ones"]
    return mk('2.B', 2, f"Which shows {n} as tens and ones?", f"{t} tens and {o} ones", wr, f"{t} tens is {t * 10}, and {t * 10} + {o} = {n}.")
def b_other():
    n = R.randint(31, 99); t, o = n // 10, n % 10
    return mk('2.B', 3, f"Which is another way to make {n}?", f"{t - 1} tens and {o + 10} ones", [f"{t - 1} tens and {o + 1} ones", f"{t - 1} tens and {o} ones", f"{t + 1} tens and {o + 10} ones", f"{t - 1} tens and {o + 9} ones"],
              f"{t - 1} tens is {(t - 1) * 10}, and {(t - 1) * 10} + {o + 10} = {n}.")
def b_hund():
    n = R.randint(101, 120); t, o = (n - 100) // 10, (n - 100) % 10
    if t == o or t == 0 or o == 0: return False
    s = lambda a, b, c: f"{pl(a, 'hundred')}, {pl(b, 'ten')}, {pl(c, 'one')}"
    return mk('2.B', 3, f"Which shows {n} as hundreds, tens, and ones?", s(1, t, o), [s(t, 1, o), s(1, o, t), s(1, t + 1, o), s(1, t, o + 1)], f"100 + {t * 10} + {o} = {n}.")
rep(2, b_tens); rep(2, b_other); rep(2, b_hund)

# ---------------------------------------------------------------- 2.C expanded and standard forms
def c_exp():
    if R.random() < .5:
        n = R.randint(11, 99)
        if n % 10 == 0: return False
        t, o = n // 10, n % 10
        return mk('2.C', 2, f"Which is the expanded form of {n}?", f"{t * 10} + {o}", [f"{t} + {o}", f"{t * 10} + {o * 10}", f"{o * 10} + {t}", f"{t * 10 + 10} + {o}"], f"Write the value of each digit: {t * 10} + {o} = {n}.")
    n = R.randint(101, 120); t, o = (n - 100) // 10, (n - 100) % 10
    if o == 0: return False
    right = f"100 + {t * 10} + {o}" if t else f"100 + {o}"
    return mk('2.C', 3, f"Which is the expanded form of {n}?", right, [f"10 + {t * 10} + {o}" if t else f"10 + {o}", f"100 + {t} + {o}", f"100 + {o * 10} + {t}" if t else f"1 + {o}", f"100 + {t * 10 + 10} + {o}"], f"100 + {t * 10} + {o} = {n}.")
def c_standard():
    n = R.randint(11, 99)
    if n % 10 == 0: return False
    t, o = n // 10, n % 10
    if R.random() < .5:
        return mk('2.C', 2, f"What number is {t * 10} + {o}?", n, ws(n, (1, -1, 10, -10)) + ([sw(n)] if sw(n) else []), f"{t * 10} + {o} = {n}.", CS(f"{t * 10}+{o}"))
    return mk('2.C', 2, f"What number is {pl(t, 'ten')} and {pl(o, 'one')}?", n, ws(n, (1, -1, 10, -10)) + ([sw(n)] if sw(n) else []), f"{t * 10} + {o} = {n}.", CS(f"{t * 10}+{o}"))
rep(3, c_exp); rep(4, c_standard)

# ---------------------------------------------------------------- 2.D generate greater or less
def d_more():
    n = R.randint(10, 100); m = R.randint(n + 1, min(n + 25, 120)); wr = R.sample(range(max(n - 20, 0), n + 1), 3)
    return mk('2.D', 2, f"Which number is greater than {n}?", m, wr, f"{m} is greater than {n}.")
def d_less():
    n = R.randint(15, 110); m = R.randint(max(n - 25, 1), n - 1); wr = R.sample(range(n, min(n + 20, 120) + 1), 3)
    return mk('2.D', 2, f"Which number is less than {n}?", m, wr, f"{m} is less than {n}.")
def d_between():
    a = R.randint(10, 90); b = a + R.randint(6, 20); m = R.randint(a + 1, b - 1)
    wr = [a - R.randint(1, 5), b + R.randint(1, 5), a, b]
    return mk('2.D', 3, f"Which number is between {a} and {b}?", m, wr, f"{m} is greater than {a} and less than {b}.")
rep(2, d_more); rep(2, d_less); rep(3, d_between)

# ---------------------------------------------------------------- 2.E compare using place value
def e_cmp():
    t = R.randint(1, 9)
    if R.random() < .5:
        a, b = R.randint(11, 99), R.randint(11, 99)
        if a // 10 == b // 10: return False
    else:
        a, b = t * 10 + R.randint(0, 9), t * 10 + R.randint(0, 9)
    if a == b: return False
    big, small = max(a, b), min(a, b)
    why = f"Compare the tens first: {big // 10} tens is more than {small // 10} tens." if big // 10 != small // 10 else f"The tens are the same, so compare the ones: {big % 10} is more than {small % 10}."
    return mk('2.E', 3, f"Compare {a} and {b}.  Which sentence is true?", f"{big} is greater than {small}.", [f"{big} is less than {small}.", f"{big} is equal to {small}."], why, need=2)
rep(7, e_cmp)

# ---------------------------------------------------------------- 2.F order numbers
def f_order():
    nums = R.sample(range(10, 100), 3)
    if R.random() < .75:
        s = sorted(nums); lab = "least to greatest"
    else:
        s = sorted(nums, reverse=True); lab = "greatest to least"
    perms = [[nums[0], nums[1], nums[2]], [nums[1], nums[0], nums[2]], [nums[2], nums[1], nums[0]], [nums[0], nums[2], nums[1]], [nums[1], nums[2], nums[0]], [nums[2], nums[0], nums[1]]]
    fm = lambda l: ', '.join(map(str, l))
    wrong = [fm(p) for p in perms if p != s]
    return mk('2.F', 3, f"Which list shows the numbers in order from {lab}?  {fm(nums)}", fm(s), wrong, "Compare the tens first, then the ones.")
def f_line():
    zone = R.choice(["left", "middle", "right"]); n = {"left": R.randint(5, 20), "middle": R.randint(42, 58), "right": R.randint(82, 96)}[zone]
    ans = {"left": "near the left end", "middle": "near the middle", "right": "near the right end"}[zone]
    return mk('2.F', 3, f"An open number line starts at 0 on the left and ends at 100 on the right. Where would you put {n}?", ans, [v for v in ("near the left end", "near the middle", "near the right end", "past the right end, so it does not fit") if v != ans], f"{n} is {'close to 0' if zone == 'left' else 'about halfway between 0 and 100' if zone == 'middle' else 'close to 100'}.")
rep(4, f_order); rep(3, f_line)

# ---------------------------------------------------------------- 2.G symbols
def g_sym():
    a, b = R.randint(10, 99), R.randint(10, 99)
    if R.random() < .12: b = a
    ans = GT if a > b else LT if a < b else EQ
    return mk('2.G', 2, f"Which symbol makes this statement true?  {a} ___ {b}", ans, [x for x in (LT, GT, EQ) if x != ans], f"Compare the tens first, then the ones: {a} is {ans.split(' (')[0]} {b}.", need=2)
def g_true():
    a, b = R.sample(range(10, 100), 2)
    if a < b: a, b = b, a
    return mk('2.G', 3, f"Look at {a} and {b}.  Which comparison is true?", f"{a} > {b}", [f"{a} < {b}", f"{a} = {b}", f"{b} > {a}"], f"{a} is greater than {b}, so {a} > {b}.")
rep(4, g_sym); rep(3, g_true)

# ---------------------------------------------------------------- 3.A multiple of ten plus ones
def p_tens():
    t, o = R.randint(1, 9), R.randint(1, 9)
    return mk('3.A', 2, f"What is {t * 10} + {o}?", t * 10 + o, [t * 10 + o + 1, t * 10 + o - 1, t + o, o * 10 + t], f"{t} tens and {o} ones make {t * 10 + o}.", CS(f"{t * 10}+{o}"))
def p_bundle():
    t, o = R.randint(2, 9), R.randint(1, 9); nm = who(); th = R.choice(["sticks", "straws", "pencils", "crayons"])
    return mk('3.A', 3, f"{nm} has {t} bundles of 10 {th} and {o} more {th}. How many {th} does {nm} have?", t * 10 + o, [t * 10 + o + 10, t * 10 - o, t + o, t * 10 + o + 1], f"{t * 10} + {o} = {t * 10 + o}.", CS(f"{t * 10}+{o}"))
rep(4, p_tens); rep(3, p_bundle)

# ---------------------------------------------------------------- 3.B word problems within 20
def w_join():
    nm = who(); th = R.choice(THINGS); a = R.randint(3, 12); b = R.randint(2, 20 - a)
    return mk('3.B', 2, f"{nm} has {a} {th}. {nm} gets {b} more. How many {th} does {nm} have now?", a + b, ws(a + b, (1, -1, 2, -2), 0, 20) + [a, b], f"{a} + {b} = {a + b}.", CS(f"{a}+{b}"))
def w_sep():
    nm = who(); th = R.choice(THINGS); a = R.randint(8, 20); b = R.randint(2, a - 2)
    return mk('3.B', 2, f"{nm} has {a} {th}. {nm} gives {b} away. How many {th} does {nm} have left?", a - b, ws(a - b, (1, -1, 2, -2), 0, 20) + [a, b], f"{a} − {b} = {a - b}.", CS(f"{a}-{b}"))
def w_change():
    nm = who(); th = R.choice(THINGS); a = R.randint(3, 11); c = R.randint(a + 2, 20)
    return mk('3.B', 3, f"{nm} has {a} {th}. {nm} gets some more. Now {nm} has {c} {th}. How many did {nm} get?", c - a, ws(c - a, (1, -1, 2, -2), 1, 20) + [c, a], f"{c} − {a} = {c - a}.", CS(f"{c}-{a}"))
def w_start():
    nm = who(); th = R.choice(THINGS); b = R.randint(2, 9); c = R.randint(b + 3, 20)
    return mk('3.B', 4, f"{nm} had some {th}. {nm} found {b} more. Now {nm} has {c} {th}. How many {th} did {nm} have at first?", c - b, ws(c - b, (1, -1, 2, -2), 1, 20) + [c + b, b], f"{c} − {b} = {c - b}.", CS(f"{c}-{b}"))
def w_cmp():
    a, b = R.sample(NM, 2); th = R.choice(THINGS); x = R.randint(9, 19); y = R.randint(3, x - 2)
    return mk('3.B', 3, f"{a} has {x} {th}. {b} has {y} {th}. How many more {th} does {a} have than {b}?", x - y, ws(x - y, (1, -1, 2, -2), 1, 20) + [x + y], f"{x} − {y} = {x - y}.", CS(f"{x}-{y}"))
rep(1, w_join); rep(1, w_sep); rep(1, w_change); rep(2, w_start); rep(2, w_cmp)

def w_two():
    nm = who(); th = R.choice(THINGS); a = R.randint(5, 12); b = R.randint(2, 8); c = R.randint(2, 7)
    if a + b > 20 or a + b - c < 1: return False
    return mk('3.B', 4, f"{nm} has {a} {th}. {nm} gets {b} more and then gives {c} away. How many {th} does {nm} have now?", a + b - c, ws(a + b - c, (1, -1, 2, -2), 0, 20) + [a + b], f"{a} + {b} = {a + b}, then {a + b} − {c} = {a + b - c}.", CS(f"{a}+{b}-{c}"))
rep(4, w_two)

# ---------------------------------------------------------------- 3.C compose 10
def t_pair():
    a = R.randint(1, 9); pr = lambda x, y: f"{x} and {y}"
    wrong = []
    while len(wrong) < 3:
        x, y = R.randint(1, 9), R.randint(1, 9)
        if x + y != 10 and pr(x, y) not in wrong and pr(y, x) not in wrong: wrong.append(pr(x, y))
    return mk('3.C', 2, f"Which two numbers make 10?", pr(a, 10 - a), wrong, f"{a} + {10 - a} = 10.")
def t_three():
    a, b = R.randint(1, 5), R.randint(1, 4)
    if a + b >= 9: return False
    c = 10 - a - b
    return mk('3.C', 3, f"What number makes this true?  {a} + {b} + __ = 10", c, ws(c, (1, -1, 2, -2, 3), 0, 10) + [10], f"{a} + {b} = {a + b}, and {a + b} + {c} = 10.", CS(f"{c}"))
def t_rest():
    nm = who(); th = R.choice(THINGS); a = R.randint(2, 8)
    return mk('3.C', 2, f"{nm} has 10 {th}. {a} are red and the rest are blue. How many are blue?", 10 - a, ws(10 - a, (1, -1, 2, -2), 0, 10) + [10], f"{a} + {10 - a} = 10.", CS(f"{10 - a}"))
rep(2, t_pair); rep(3, t_three); rep(2, t_rest)

# ---------------------------------------------------------------- 3.D basic fact strategies
def d_sum():
    a, b = R.randint(2, 9), R.randint(2, 9)
    if a + b < 11: return False
    return mk('3.D', 2, f"What is {a} + {b}?", a + b, ws(a + b, (1, -1, 2, -2, 10), 0, 20), f"{a} + {b} = {a + b}.", CS(f"{a}+{b}"))
def d_diff():
    a, b = R.randint(11, 18), R.randint(2, 9)
    if a - b < 2: return False
    return mk('3.D', 2, f"What is {a} − {b}?", a - b, ws(a - b, (1, -1, 2, -2, 10), 0, 20), f"{a} − {b} = {a - b}.", CS(f"{a}-{b}"))
def d_ten():
    a = R.randint(7, 9); b = R.randint(11 - a + 1, 9); nm = who(); k = 10 - a
    return mk('3.D', 3, f"{nm} solves {a} + {b} by thinking: {a} + {k} = 10, then 10 + {b - k} more. What is {a} + {b}?", a + b, ws(a + b, (1, -1, 2, -2), 11, 20) + [10], f"10 + {b - k} = {a + b}.", CS(f"{a}+{b}"))
def d_step():
    a = R.randint(7, 9); b = R.randint(11 - a + 1, 9)
    return mk('3.D', 3, f"To make a ten when you solve {a} + {b}, what is a good first step?", f"{a} + {10 - a} = 10", [f"{a} + {b} = 10", f"{a} − {b} = {a - b}" if a > b else f"{b} − {a} = {b - a}", f"{b} + {b} = {2 * b}"], f"Add {10 - a} to {a} to make 10, then add the rest.")
rep(3, d_sum); rep(2, d_diff); rep(1, d_ten); rep(1, d_step)

# ---------------------------------------------------------------- 3.E explain strategies
SS = ["making ten", "doubles plus one", "counting on", "counting back", "using a related fact"]
def x_ten():
    nm = who(); a = R.randint(7, 9); b = R.randint(11 - a + 1, 9); k = 10 - a
    return mk('3.E', 3, f"{nm} solves {a} + {b} like this:  {a} + {k} = 10, then 10 + {b - k}. Which strategy did {nm} use?", "making ten", [s for s in SS if s != "making ten"], "Breaking apart a number to make 10 first is making ten.")
def x_double():
    nm = who(); x = R.randint(3, 9)
    return mk('3.E', 3, f"{nm} knows {x} + {x} = {2 * x}. {nm} uses it to solve {x} + {x + 1}. Which strategy did {nm} use?", "doubles plus one", [s for s in SS if s != "doubles plus one"], f"{x + 1} is one more than {x}, so the answer is one more than {2 * x}.")
def x_rel():
    nm = who(); a = R.randint(4, 9); b = R.randint(3, 9)
    return mk('3.E', 3, f"{nm} knows {a} + {b} = {a + b}. {nm} uses it to solve {a + b} − {b}. Which strategy did {nm} use?", "using a related fact", [s for s in SS if s != "using a related fact"], "Addition and subtraction facts are related.")
def x_back():
    nm = who(); a = R.randint(10, 18)
    return mk('3.E', 3, f"{nm} solves {a} − 3 by starting at {a} and saying {a - 1}, {a - 2}, {a - 3}. Which strategy did {nm} use?", "counting back", [s for s in SS if s != "counting back"], "Saying the numbers that come before is counting back.")
def x_on():
    nm = who(); a = R.randint(10, 16)
    return mk('3.E', 3, f"{nm} solves {a} + 3 by starting at {a} and saying {a + 1}, {a + 2}, {a + 3}. Which strategy did {nm} use?", "counting on", [s for s in SS if s != "counting on"], "Saying the numbers that come after is counting on.")
rep(2, x_ten); rep(1, x_double); rep(1, x_rel); rep(1, x_back); rep(1, x_on)

# ---------------------------------------------------------------- 3.F stories for a number sentence
def y_story():
    a, b = R.randint(6, 14), R.randint(2, 6); nm, n2 = R.sample(NM, 2); add = R.random() < .5
    th = R.choice(["cards", "grapes", "stickers", "marbles"])
    s_add = f"{nm} has {a} {th} and gets {b} more. How many {th} does {nm} have now?"
    s_sub = f"{nm} has {a} {th} and gives {b} away. How many {th} are left?"
    o_add = f"{n2} puts {a} red blocks and {b} blue blocks in a box. How many blocks are in the box?"
    o_sub = f"{n2} has {a} balloons and {b} pop. How many balloons are left?"
    if add and a + b <= 20:
        return mk('3.F', 3, f"Which story can be solved with {a} + {b}?", s_add, [s_sub, o_sub, f"{n2} has {a + b} stickers and gives {b} away. How many are left?"], f"{a} + {b} joins two amounts.")
    if not add:
        return mk('3.F', 3, f"Which story can be solved with {a} − {b}?", s_sub, [s_add, o_add, f"{n2} has {a} cards and finds {b} more. How many cards now?"], f"{a} − {b} takes an amount away.")
    return False
rep(6, y_story)

# ---------------------------------------------------------------- 4 money
for coin, c in [("penny", 1), ("nickel", 5), ("dime", 10), ("quarter", 25)]:
    H('4.A', 2, f"Which coin is worth {c} cent{'s' if c > 1 else ''}?", coin, [x for x in ("penny", "nickel", "dime", "quarter") if x != coin], f"A {coin} is worth {c} cent{'s' if c > 1 else ''}.")
H('4.A', 3, "How many pennies are worth the same as 1 nickel?", "5", ["1", "10", "25"], "A nickel is worth 5 cents, and each penny is 1 cent.")
H('4.A', 3, "How many pennies are worth the same as 1 dime?", "10", ["5", "2", "25"], "A dime is worth 10 cents, and each penny is 1 cent.")
H('4.A', 3, "How many nickels are worth the same as 1 quarter?", "5", ["2", "10", "25"], "A quarter is 25 cents, and 5 nickels are 5 × 5 = 25 cents.")
H('4.B', 2, "Which shows the value of a dime?", "10¢", ["1¢", "5¢", "25¢"], "A dime is worth 10 cents, written 10¢.")
H('4.B', 2, "Which shows the value of a nickel?", "5¢", ["1¢", "10¢", "25¢"], "A nickel is worth 5 cents, written 5¢.")
H('4.B', 2, "Which shows the value of a quarter?", "25¢", ["1¢", "5¢", "10¢"], "A quarter is worth 25 cents, written 25¢.")
H('4.B', 2, "Which shows the value of a penny?", "1¢", ["5¢", "10¢", "25¢"], "A penny is worth 1 cent, written 1¢.")
H('4.B', 3, "How do you write twenty-five cents with the cent symbol?", "25¢", ["52¢", "2.5¢", "$25"], "Twenty-five cents is 25¢.")
H('4.B', 3, "Which tells the value of 3 pennies?", "3¢", ["30¢", "13¢", "5¢"], "Each penny is 1¢, so 3 pennies are 3¢.")
def m_coins():
    nm = who()
    kinds = R.choice([(10, 5), (5, 1), (10, 1), (10, 5, 1)])
    cnt = {k: R.randint(1, 4) for k in kinds}
    one = {10: "dime", 5: "nickel", 1: "penny"}; many = {10: "dimes", 5: "nickels", 1: "pennies"}
    total = sum(k * v for k, v in cnt.items())
    parts = [f"{v} {one[k] if v == 1 else many[k]}" for k, v in cnt.items()]
    txt = ' and '.join(parts) if len(parts) == 2 else ', '.join(parts[:-1]) + ', and ' + parts[-1]
    wr = [total + 5, total - 5, total + 10, total + 1, total - 1, total - 10]
    return mk('4.C', 3, f"{nm} has {txt}. How much money does {nm} have?", f"{total}¢", [f"{w}¢" for w in wr if w > 0], f"Skip count and add the values: {total}¢.", f"'{total}¢'")
rep(7, m_coins)

# ---------------------------------------------------------------- 5.A recite numbers
def r_fwd():
    s = R.randint(8, 112)
    return mk('5.A', 2, f"What number comes next?  {s}, {s + 1}, {s + 2}, __", s + 3, ws(s + 3, (1, -1, 2, -2, 10), 1, 120), f"Counting forward: {s + 3}.", CS(f"{s}+3"))
def r_back():
    s = R.randint(8, 118)
    return mk('5.A', 3, f"Count backward.  {s}, {s - 1}, {s - 2}, __", s - 3, ws(s - 3, (1, -1, 2, -2, 10), 1, 120), f"Counting backward: {s - 3}.", CS(f"{s}-3"))
def r_miss():
    s = R.randint(8, 115)
    return mk('5.A', 3, f"What number is missing?  {s}, {s + 1}, __, {s + 3}", s + 2, ws(s + 2, (1, -1, 2, -2, 10), 1, 120), f"{s + 2} comes between {s + 1} and {s + 3}.", CS(f"{s}+2"))
rep(3, r_fwd); rep(2, r_back); rep(2, r_miss)

# ---------------------------------------------------------------- 5.B skip count
def k_two():
    k = R.randint(3, 9); th = R.choice(["socks", "shoes", "mittens", "eyes"]); nm = who()
    pairs = {"socks": "pairs of socks", "shoes": "pairs of shoes", "mittens": "pairs of mittens", "eyes": "children"}[th]
    return mk('5.B', 2, f"There are {k} {pairs}. Each pair has 2 {th if th != 'eyes' else 'eyes'}. Count by 2s. How many {th if th != 'eyes' else 'eyes'} are there?", 2 * k, ws(2 * k, (1, -1, 2, -2, 10), 1, 120), f"Count by 2s {k} times: {2 * k}.", CS(f"2*{k}")) if th != "eyes" else mk('5.B', 2, f"There are {k} children. Each child has 2 eyes. Count by 2s. How many eyes are there in all?", 2 * k, ws(2 * k, (1, -1, 2, -2, 10), 1, 120), f"Count by 2s {k} times: {2 * k}.", CS(f"2*{k}"))
def k_five():
    k = R.randint(3, 12)
    return mk('5.B', 2, f"Each hand has 5 fingers. Count by 5s. How many fingers are on {k} hands?", 5 * k, ws(5 * k, (5, -5, 1, 10, -10), 1, 120), f"Count by 5s {k} times: {5 * k}.", CS(f"5*{k}"))
def k_ten():
    k = R.randint(3, 12); nm = who()
    return mk('5.B', 2, f"{nm} has {k} bags with 10 marbles in each bag. Count by 10s. How many marbles does {nm} have?", 10 * k, ws(10 * k, (10, -10, 1, 5, -5), 1, 120), f"Count by 10s {k} times: {10 * k}.", CS(f"10*{k}"))
def k_next():
    by = R.choice([2, 5, 10]); s = by * R.randint(1, 6)
    return mk('5.B', 2, f"Skip count by {by}s.  {s}, {s + by}, {s + 2 * by}, __", s + 3 * by, ws(s + 3 * by, (by, -by, 1, 2 * by), 1, 120), f"Add {by} each time: {s + 3 * by}.", CS(f"{s}+3*{by}"))
rep(2, k_two); rep(2, k_five); rep(2, k_ten); rep(1, k_next)

# ---------------------------------------------------------------- 5.C ten more, ten less
def u_more():
    n = R.randint(1, 109)
    return mk('5.C', 2, f"What is 10 more than {n}?", n + 10, ws(n + 10, (1, -1, 10, -10), 1, 120) + [n + 1], f"{n} + 10 = {n + 10}.", CS(f"{n}+10"))
def u_less():
    n = R.randint(11, 120)
    return mk('5.C', 2, f"What is 10 less than {n}?", n - 10, ws(n - 10, (1, -1, 10, -10), 1, 120) + [n - 1], f"{n} − 10 = {n - 10}.", CS(f"{n}-10"))
rep(4, u_more); rep(4, u_less)

# ---------------------------------------------------------------- 5.D number sentences for word problems
def v_sent():
    nm = who(); th = R.choice(THINGS); add = R.random() < .5
    if add:
        a = R.randint(4, 12); b = R.randint(2, 20 - a)
        return mk('5.D', 3, f"{nm} has {a} {th} and finds {b} more. Which number sentence can be used to find how many {th} {nm} has now?", f"{a} + {b} = {a + b}", [f"{a} − {b} = {max(a - b, 0)}" if a >= b else f"{b} − {a} = {b - a}", f"{a} + {b} = {a + b + 1}", f"{a + b} + {a} = {2 * a + b}"], "Finding more is joining, so add.")
    a = R.randint(8, 20); b = R.randint(2, a - 2)
    return mk('5.D', 3, f"{nm} has {a} {th} and loses {b}. Which number sentence can be used to find how many {th} {nm} has left?", f"{a} − {b} = {a - b}", [f"{a} + {b} = {a + b}", f"{a} − {b} = {a - b + 1}", f"{b} − {a - b} = {b - (a - b)}" if b >= a - b else f"{b} + {a - b} = {a}"], "Losing some is separating, so subtract.")
rep(6, v_sent)

# ---------------------------------------------------------------- 5.E equal sign
def q_missing():
    a, b = R.randint(2, 9), R.randint(2, 9); c = R.randint(1, a + b - 1)
    return mk('5.E', 3, f"What number makes this true?  {a} + {b} = {c} + __", a + b - c, ws(a + b - c, (1, -1, 2), 0, 20) + [a, b], f"{a} + {b} = {a + b}, and {c} + {a + b - c} = {a + b}.", CS(f"{a + b - c}"))
def q_true():
    a, b = R.randint(2, 9), R.randint(2, 9); c, d = R.randint(2, 9), R.randint(2, 9)
    if a + b == c + d: return False
    x = R.randint(2, 9); y = (a + b) - x
    if y < 1 or y == b and x == a: return False
    return mk('5.E', 3, f"Which number sentence is true?", f"{a} + {b} = {x} + {y}", [f"{a} + {b} = {x} + {y + 1}", f"{a} + {b} = {x + 1} + {y + 1}", f"{a} + {b} = {x} + {y - 1}" if y > 1 else f"{a} + {b} = {x + 2} + {y}"], f"Both sides must have the same value: {a} + {b} = {a + b} and {x} + {y} = {a + b}.") if False else False
def q_pair():
    a, b = R.randint(3, 9), R.randint(3, 9); x = R.randint(2, 8)
    s = a + b
    return mk('5.E', 3, f"Which number sentence is true?  Pick the one where both sides have the same value, with {a} + {b} on one side.", f"{a} + {b} = {s - x} + {x}", [f"{a} + {b} = {s - x + 1} + {x}", f"{a} + {b} = {s - x} + {x + 2}", f"{a} + {b} = {s} + {x}"], f"{s - x} + {x} = {s}, the same as {a} + {b}.") if s - x >= 1 and x != b and s - x != b else False
def q_yn():
    a, b = R.randint(2, 9), R.randint(2, 9); c = R.randint(10, 18); d = c - (a + b)
    if d < 1: return False
    return mk('5.E', 3, "Which number sentence is true?", f"{a} + {b} = {c} − {d}", [f"{a} + {b} = {c} − {d + 1}", f"{a} + {b} = {c + 1} − {d}", f"{a} + {b + 1} = {c} − {d}"], f"{a} + {b} = {a + b} and {c} − {d} = {a + b}, so both sides are equal.")
def q_nottrue():
    a, b = R.randint(3, 9), R.randint(3, 9); s_ = a + b; x = R.randint(1, s_ - 1)
    if x == a or x == b: return False
    return mk('5.E', 4, f"Which number sentence is NOT true?  (Both sides must be equal.)", f"{a} + {b} = {s_ - x} + {x + 1}", [f"{a} + {b} = {s_ - x} + {x}", f"{a} + {b} = {b} + {a}", f"{a} + {b} = {s_}"], f"{s_ - x} + {x + 1} = {s_ + 1}, which is not equal to {s_}.")
rep(3, q_missing); rep(2, q_pair); rep(3, q_yn); rep(3, q_nottrue)

# ---------------------------------------------------------------- 5.F unknown in equation
def z_unknown():
    a, b = R.randint(3, 12), R.randint(2, 8); c = a + b; form = R.randint(0, 4)
    if form == 0: q, ans = f"{a} + __ = {c}", b
    elif form == 1: q, ans = f"__ + {b} = {c}", a
    elif form == 2: q, ans = f"{c} − __ = {a}", b
    elif form == 3: q, ans = f"__ − {b} = {a}", c
    else: q, ans = f"{c} = {a} + __", b
    return mk('5.F', 3, f"What number goes in the blank?  {q}", ans, ws(ans, (1, -1, 2, -2), 0, 20) + [a, b, c], f"The missing number is {ans}.", CS(f"{ans}"))
rep(7, z_unknown)

# ---------------------------------------------------------------- 5.G properties
def m_swap():
    a, b = R.randint(3, 9), R.randint(3, 9)
    if a == b: return False
    return mk('5.G', 2, f"If {a} + {b} = {a + b}, what is {b} + {a}?", a + b, ws(a + b, (1, -1, 2, -2), 0, 20) + [abs(a - b)], "You can add in any order and get the same sum.", CS(f"{a}+{b}"))
def m_three():
    a, b = R.randint(2, 8), R.randint(2, 8); c = 10 - a if R.random() < .6 else R.randint(2, 8)
    return mk('5.G', 3, f"What is {a} + {b} + {c}?", a + b + c, ws(a + b + c, (1, -1, 2, -2, 10), 3, 30), f"{a} + {b} + {c} = {a + b + c}.", CS(f"{a}+{b}+{c}"))
def m_fill():
    a, b, c = R.sample(range(2, 10), 3)
    return mk('5.G', 3, f"What number goes in the blank?  {a} + {b} + {c} = {a} + __ + {b}", c, [b, a, c + 1, c - 1], "You can add numbers in any order and get the same total.", CS(f"{c}"))
rep(2, m_swap); rep(2, m_three); rep(2, m_fill)

# ---------------------------------------------------------------- 6 geometry (hand-written)
H('6.A', 2, "Which shape has 3 sides and 3 corners?", "triangle", ["square", "circle", "rectangle"], "A triangle has 3 sides and 3 corners.")
H('6.A', 2, "Which shape has 4 sides that are all the same length and 4 corners like the corner of a book?", "square", ["triangle", "circle", "hexagon"], "A square has 4 equal sides and 4 square corners.")
H('6.A', 3, "Sort these shapes by number of sides. Which shape does NOT have 4 sides?", "triangle", ["square", "rectangle", "rhombus"], "A square, a rectangle, and a rhombus have 4 sides. A triangle has 3.")
H('6.A', 3, "A shape has no corners and no straight sides. Which group does it belong in?", "round shapes", ["shapes with 3 sides", "shapes with 4 sides", "shapes with 6 sides"], "A circle is round with no corners.")
H('6.A', 3, "Which two shapes belong in the same group because they both have 4 sides?", "a square and a rectangle", ["a triangle and a circle", "a circle and a square", "a triangle and a rectangle"], "A square and a rectangle each have 4 sides.")
H('6.A', 3, "Three shapes have 6 sides and one does not. Which one does NOT have 6 sides?", "a square", ["a big hexagon", "a small hexagon", "a tilted hexagon"], "Every hexagon has 6 sides. A square has 4.")
H('6.B', 3, "A triangle is colored red. Is it still a triangle?", "yes, because color does not change the shape", ["no, because it is red", "no, because triangles are blue", "yes, because it has 4 sides"], "The color does not change the number of sides, so it is still a triangle.")
H('6.B', 3, "Which attribute helps tell a triangle from a square?", "the number of sides", ["the color", "the size", "where it is on the page"], "A triangle has 3 sides and a square has 4. That is a defining attribute.")
H('6.B', 3, "Which is NOT a defining attribute of a rectangle?", "its color", ["it has 4 sides", "it has 4 square corners", "it has 2 long sides and 2 short sides"], "A rectangle can be any color. Color does not define the shape.")
H('6.B', 3, "A big square and a small square are both squares. What does this show?", "size does not decide the shape", ["small shapes cannot be squares", "color decides the shape", "squares must have 3 sides"], "Size is not a defining attribute.")
H('6.B', 3, "Which attribute defines a cube?", "6 square faces", ["it is red", "it is small", "it is on a table"], "A cube always has 6 square faces.")
H('6.B', 3, "A ball can be red, blue, big, or small. What always makes it a sphere?", "it is perfectly round", ["its color", "its size", "who owns it"], "A sphere is round all the way around.")
H('6.C', 3, "You join 2 squares along one whole side. What shape can you make?", "rectangle", ["triangle", "circle", "pentagon"], "Two squares joined along a side make a longer rectangle.")
H('6.C', 3, "Which shapes can you use to make a hexagon?", "6 triangles that are the same", ["3 circles", "2 squares", "1 triangle"], "Six same-size triangles can fit together to make a hexagon.")
H('6.C', 3, "You draw a closed shape with 6 straight sides. What shape is it?", "hexagon", ["triangle", "square", "circle"], "A shape with 6 sides is a hexagon.")
H('6.C', 3, "You join 2 triangles that are the same size along a long side. What shape can you make?", "a square or rectangle", ["a circle", "a hexagon", "a cube"], "Two matching right triangles joined along the long side can make a square or a rectangle.")
H('6.C', 2, "How many sides does a rhombus have?", "4", ["3", "5", "6"], "A rhombus has 4 equal sides.")
H('6.D', 2, "How many sides does a hexagon have?", "6", ["4", "5", "8"], "A hexagon has 6 sides.")
H('6.D', 2, "How many vertices does a hexagon have?", "6", ["4", "5", "3"], "A hexagon has 6 vertices (corners).")
H('6.D', 3, "A rhombus has 4 sides that are all the same length. Which of these shapes is also a rhombus?", "square", ["triangle", "circle", "hexagon"], "A square has 4 equal sides, so it is also a rhombus.")
H('6.D', 3, "A square is a special kind of what shape?", "rectangle", ["triangle", "circle", "hexagon"], "A square has 4 sides and 4 square corners, so it is a special rectangle.")
H('6.D', 3, "Which shape has 4 equal sides but its corners are not square?", "rhombus", ["rectangle", "triangle", "hexagon"], "A rhombus has 4 equal sides and slanted corners.")
H('6.D', 3, "A vertex is the point where two sides meet. How many vertices does a triangle have?", "3", ["2", "4", "6"], "A triangle has 3 vertices.")
H('6.D', 2, "Which shape has 6 sides and 6 vertices?", "hexagon", ["triangle", "rectangle", "circle"], "A hexagon has 6 sides and 6 vertices.")
H('6.E', 2, "How many flat faces does a cube have?", "6", ["4", "8", "2"], "A cube has 6 flat faces.")
H('6.E', 3, "Which solid has 1 flat round face and 1 pointed tip?", "cone", ["sphere", "cylinder", "cube"], "A cone has a circle on the bottom and one point at the top.")
H('6.E', 3, "Which solid has 2 flat round faces and 1 curved surface?", "cylinder", ["cone", "sphere", "cube"], "A cylinder has two circles joined by a curved side.")
H('6.E', 3, "Which solid has 6 faces that are all rectangles?", "rectangular prism", ["cone", "sphere", "cylinder"], "A rectangular prism has 6 rectangle faces.")
H('6.E', 3, "Which solid has 2 triangle faces and 3 rectangle faces?", "triangular prism", ["cube", "cone", "cylinder"], "A triangular prism has 2 triangle ends and 3 rectangle sides.")
H('6.E', 3, "A shoe box is shaped like which solid?", "rectangular prism", ["cone", "sphere", "cylinder"], "A shoe box has 6 rectangle faces.")
H('6.E', 3, "Which solid has no flat faces and no edges?", "sphere", ["cube", "cylinder", "cone"], "A sphere is completely round.")
H('6.F', 3, "You put 2 matching trapezoids together. What shape can you make?", "hexagon", ["triangle", "circle", "square"], "Two trapezoid pattern blocks fit together to make a hexagon.")
H('6.F', 3, "Which can you make by joining 4 squares in a 2 by 2 block?", "a bigger square", ["a circle", "a triangle", "a hexagon"], "4 squares in a 2 by 2 block make a bigger square.")
H('6.F', 3, "You join 3 squares in a row, touching side to side. What shape do you make?", "rectangle", ["circle", "triangle", "hexagon"], "A row of squares makes a long rectangle.")
H('6.F', 4, "Which shapes can be put together in more than one way to make a rectangle?", "2 squares or 2 triangles", ["2 circles", "1 circle and 1 triangle", "3 circles"], "Two squares can make a rectangle, and so can two matching right triangles.")
H('6.F', 3, "You put 6 triangles together so they meet in the middle. What shape do you make?", "hexagon", ["square", "circle", "rectangle"], "6 same-size triangles around a center point make a hexagon.")
H('6.F', 3, "Which is a way to make a bigger triangle?", "put 4 small triangles together", ["put 2 circles together", "put 2 squares together", "stack 3 cubes"], "4 small matching triangles can be put together to make a bigger triangle.")
def g_share():
    sh = R.choice(["pizza", "sandwich", "pie", "pancake", "cracker", "banana bread"]); nm = who()
    if R.random() < .5:
        return mk('6.G', 2, f"{nm} cuts a {sh} into 2 equal parts. What is each part called?", "a half", ["a fourth", "a whole", "a third"], "2 equal parts are halves.")
    return mk('6.G', 2, f"{nm} cuts a {sh} into 4 equal parts. What is each part called?", "a fourth (a quarter)", ["a half", "a whole", "a third"], "4 equal parts are fourths, also called quarters.")
rep(3, g_share)
H('6.G', 3, "How many equal parts are there in fourths?", "4", ["2", "3", "8"], "Fourths means 4 equal parts.")
H('6.G', 3, "Max cuts a square into 2 equal parts. How many parts does he have?", "2", ["1", "3", "4"], "Halves are 2 equal parts.")
H('6.G', 3, "A circle is cut into fourths. How many fourths make the whole circle?", "4", ["2", "3", "8"], "4 fourths make 1 whole.")
H('6.G', 3, "How many halves make a whole?", "2", ["1", "3", "4"], "2 halves make 1 whole.")
H('6.H', 2, "A sandwich is cut into 2 parts, but one part is much bigger. Are the parts halves?", "no, because the parts are not equal", ["yes, because there are 2 parts", "yes, because it is a sandwich", "no, because halves are bigger"], "Halves must be equal parts.")
H('6.H', 3, "Which shows an example of fourths?", "a square cut into 4 equal parts", ["a square cut into 4 unequal parts", "a square cut into 2 equal parts", "a circle cut into 3 parts"], "Fourths are 4 equal parts.")
H('6.H', 3, "Which shows a non-example of halves?", "a circle cut into 2 unequal parts", ["a circle cut into 2 equal parts", "a rectangle cut into 2 equal parts", "a square cut into 2 equal parts"], "Halves must be equal. Unequal parts are not halves.")
H('6.H', 3, "A pizza is cut into 4 pieces that are all the same size. What can you say?", "each piece is one fourth", ["each piece is one half", "each piece is the whole pizza", "the pieces are not equal"], "4 equal pieces are fourths.")
H('6.H', 3, "Which is NOT a way to cut a rectangle into fourths?", "cutting it into 4 parts of different sizes", ["cutting it into 4 equal strips", "cutting it into 4 equal squares", "cutting it in half and then in half again"], "Fourths must be 4 equal parts.")
H('6.H', 3, "A circle is cut in half and then each half is cut in half. What are the pieces called?", "fourths", ["halves", "wholes", "eighths"], "2 halves, each cut in half, make 4 equal pieces: fourths.")
H('6.H', 2, "Which word names 2 equal parts of a whole?", "halves", ["fourths", "thirds", "wholes"], "2 equal parts are halves.")

# ---------------------------------------------------------------- 7 measurement
H('7.A', 2, "Which tool measures length?", "a ruler", ["a clock", "a scale", "a measuring cup"], "A ruler measures length.")
def l_ruler():
    nm = who(); obj_ = R.choice(["pencil", "crayon", "eraser", "paper clip", "leaf", "straw"]); n = R.randint(3, 10)
    return mk('7.A', 2, f"{nm} lines up the left end of {'an' if obj_[0] in 'aeiou' else 'a'} {obj_} with the 0 on a ruler marked in inches. The right end lines up with the number {n}. How long is the {obj_}?", f"{n} inches", [f"{x} inches" for x in ws(n, (1, -1, 2, -2), 1, 12)], f"The length is {n} inches.")
rep(5, l_ruler)
def u_cubes():
    nm = who(); th = R.choice(["paper clips", "cubes", "buttons"]); em_ = {"paper clips": "📎", "cubes": "🧊", "buttons": "🔘"}[th]; obj_ = R.choice(["book", "pencil", "desk"]); n = R.randint(4, 12)
    return mk('7.B', 2, f"{nm} measures a {obj_} by putting {th} end to end with no gaps:   {em_ * n}   How many {th} long is the {obj_}?", n, ws(n, (1, -1, 2, -2), 1, 14), f"Count the {th} in the row: {n}.", CS(f"{n}"))
rep(4, u_cubes)
H('7.B', 3, "When you measure with paper clips, how should you place them?", "end to end with no gaps or overlaps", ["with gaps between them", "on top of each other", "in a pile"], "Units go end to end with no gaps and no overlaps.")
H('7.B', 3, "Where should the first unit start when you measure the length of a pencil?", "at one end of the pencil", ["in the middle of the pencil", "past the end of the pencil", "anywhere on the table"], "Start the first unit at one end of the object.")
def u_diff():
    nm, n2 = R.sample(NM, 2); n = R.randint(3, 6); obj_ = R.choice(["table", "rug", "shelf", "hallway"])
    return mk('7.C', 3, f"{nm} measures a {obj_} with long sticks and gets {n}. {n2} measures the same {obj_} with short sticks and gets {2 * n}. Why are the numbers different?", f"{n2} used shorter units", [f"{nm} counted wrong", f"The {obj_} grew", "The numbers should be the same"], f"A shorter unit means you need more of them to cover the same length.")
rep(3, u_diff)
H('7.C', 3, "You measure the same desk with big blocks and with small blocks. Which will give the greater number?", "the small blocks", ["the big blocks", "they will give the same number", "neither one"], "More small blocks fit along the desk, so the number is greater.")
H('7.C', 3, "A hallway is measured with giant steps and with baby steps. Which number is smaller?", "the number of giant steps", ["the number of baby steps", "they are the same", "neither can be counted"], "Giant steps are longer units, so you need fewer of them.")
H('7.C', 3, "The same ribbon is measured with inch cubes and with larger blocks. Why is the number of larger blocks less?", "larger blocks are longer units", ["larger blocks are heavier", "the ribbon got shorter", "inch cubes are bigger"], "Longer units cover more length each, so fewer are needed.")
def n_near():
    a = R.randint(3, 9); close = R.choice([a, a + 1]); nm = who(); obj_ = R.choice(["straw", "crayon", "pencil", "ribbon", "twig"])
    side = f"closer to the {close} mark"
    return mk('7.D', 3, f"A ruler is marked in inches. The end of {nm}'s {obj_} is between the {a} and {a + 1} marks, but {side}. To the nearest inch, how long is it?", f"{close} inches", [f"{x} inches" for x in (a - 1, a + 2, (a + 1 if close == a else a)) if x != close], f"The end is closest to {close}, so the length is about {close} inches.")
rep(6, n_near)
def t_hour():
    h = R.randint(1, 12); half = R.random() < .5
    if half:
        return mk('7.E', 3, f"The hour hand is between the {h} and the {h % 12 + 1}. The minute hand points to the 6. What time is it?", f"{h}:30", [f"{h % 12 + 1}:30", f"{h}:00", f"6:{h:02d}" if h > 0 else "6:01"], f"The minute hand on the 6 means 30 minutes after {h}, so it is {h}:30.")
    return mk('7.E', 2, f"The hour hand points to the {h}. The minute hand points to the 12. What time is it?", f"{h}:00", [f"12:{h:02d}" if h < 12 else "12:12", f"{h}:30", f"{h % 12 + 1}:00"], f"The minute hand on the 12 means o'clock, so it is {h}:00.")
rep(4, t_hour)
def t_digital():
    h = R.randint(1, 12); half = R.random() < .5; t = f"{h}:{'30' if half else '00'}"
    word = f"half past {h}" if half else f"{h} o'clock"
    other = f"{h}:{'00' if half else '30'}"
    return mk('7.E', 2, f"Which time is {word}?", t, [other, f"{h % 12 + 1}:{'30' if half else '00'}", f"{'30' if half else '00'}:{h:02d}"], f"{word[0].upper() + word[1:]} is written {t}.")
rep(3, t_digital)

# ---------------------------------------------------------------- 8 data
def a_tally():
    kinds = R.sample([("dogs", "🐶"), ("cats", "🐱"), ("fish", "🐟"), ("birds", "🐦"), ("frogs", "🐸")], 3); cnt = R.sample(range(2, 10), 3)
    data = "   ".join(f"{k[1]} {c}" for k, c in zip(kinds, cnt)); mx = max(range(3), key=lambda i: cnt[i]); mn = min(range(3), key=lambda i: cnt[i])
    form = R.randint(0, 2)
    if form == 0: return mk('8.A', 2, f"A T-chart of pets:   {data}.   Which kind of pet has the MOST?", kinds[mx][0], [k[0] for i, k in enumerate(kinds) if i != mx], f"{cnt[mx]} is the greatest number.", need=2)
    if form == 1: return mk('8.A', 2, f"A T-chart of pets:   {data}.   Which kind of pet has the FEWEST?", kinds[mn][0], [k[0] for i, k in enumerate(kinds) if i != mn], f"{cnt[mn]} is the least number.", need=2)
    return mk('8.A', 3, f"A T-chart of pets:   {data}.   How many pets are there in all?", sum(cnt), ws(sum(cnt), (1, -1, 2, -2), 3, 30) + [max(cnt)], f"{' + '.join(map(str, cnt))} = {sum(cnt)}.", CS(f"{'+'.join(map(str, cnt))}"))
rep(5, a_tally)
H('8.A', 2, "Ava sorts her toys into 3 groups. What is a good way to keep track of how many are in each group?", "make tally marks or a T-chart", ["guess each number", "count only one group", "throw some away"], "Tally marks and T-charts help organize and count data.")
def b_make():
    nm = who(); kinds = R.sample([("red", "blue", "green"), ("circles", "squares", "triangles")][R.randint(0, 1)], 3); c = R.sample(range(1, 8), 3)
    t = lambda cc: ", ".join(f"{k} {v}" for k, v in zip(kinds, cc))
    sw_ = [c[1], c[0], c[2]]; up = [c[0], c[1], c[2] + 1]; dn = [c[0] + 1, c[1], c[2]]
    return mk('8.B', 3, f"{nm} counts: {t(c)}.  Which bar graph shows this?", f"bars of height {', '.join(map(str, c))}", [f"bars of height {', '.join(map(str, x))}" for x in (sw_, up, dn)], f"Each bar's height matches its count.")
rep(4, b_make)
def b_pic():
    nm = who(); (p, e) = R.choice([("dogs", "🐶"), ("cats", "🐱"), ("frogs", "🐸")]); n = R.randint(2, 8)
    return mk('8.B', 2, f"{nm} makes a picture graph. There are {n} {p}. How many pictures go in the {p} row?", n, ws(n, (1, -1, 2), 1, 10), f"One picture for each: {n}.", CS(f"{n}"))
rep(2, b_pic)
def g_read():
    kinds = R.sample([("apples", "🍎"), ("bananas", "🍌"), ("grapes", "🍇"), ("pears", "🍐")], 2); a, b = R.sample(range(2, 10), 2); big, small = max(a, b), min(a, b)
    gr = f"{kinds[0][0].capitalize()}: {' '.join([kinds[0][1]] * a)}      {kinds[1][0].capitalize()}: {' '.join([kinds[1][1]] * b)}"
    form = R.randint(0, 2)
    if form == 0: return mk('8.C', 3, f"Picture graph:   {gr}   How many more pictures are in the longer row?", big - small, ws(big - small, (1, -1, 2), 1, 10) + [big, small], f"{big} − {small} = {big - small}.", CS(f"{big}-{small}"))
    if form == 1: return mk('8.C', 3, f"Picture graph:   {gr}   How many pictures are in both rows?", a + b, ws(a + b, (1, -1, 2, -2), 3, 20) + [big], f"{a} + {b} = {a + b}.", CS(f"{a}+{b}"))
    win = kinds[0][0] if a > b else kinds[1][0]; lose = kinds[1][0] if a > b else kinds[0][0]
    return mk('8.C', 2, f"Picture graph:   {gr}   Which sentence is true?", f"There are fewer pictures of {lose}.", [f"There are fewer pictures of {win}.", "Both rows have the same number."], f"The row for {lose} is shorter.", need=2)
rep(7, g_read)

# ---------------------------------------------------------------- 9 personal financial literacy
H('9.A', 2, "Money that a person earns by working is called what?", "income", ["a gift", "a toy", "a want"], "Income is money you earn.")
H('9.A', 3, "Ben mows lawns and gets paid. What do we call the money he gets?", "income", ["a present", "a loan", "a need"], "Money earned for work is income.")
H('9.A', 2, "Which is an example of earning income?", "being paid to walk a dog", ["finding a toy", "getting a birthday present", "winning a stuffed animal at a fair"], "You earn income by working.")
H('9.A', 3, "A nurse works at a hospital and gets a paycheck. The paycheck is what?", "income", ["a gift", "a want", "a charity"], "A paycheck from working is income.")
H('9.A', 2, "Which is NOT a way to earn income?", "getting a birthday gift", ["washing cars for pay", "working at a store", "selling lemonade"], "A gift is not earned by working.")
H('9.B', 3, "People use income to buy goods and services. Which is a service?", "a haircut", ["a book", "a toy car", "an apple"], "A service is work someone does for you.")
H('9.B', 3, "People use income to buy goods and services. Which is a good?", "a loaf of bread", ["a haircut", "a bus ride", "a dentist visit"], "A good is something you can hold or own.")
H('9.B', 2, "Which one is a need?", "food", ["a video game", "a toy robot", "a new hat"], "Food is something people need to live.")
H('9.B', 2, "Which one is a want?", "a new toy", ["water", "food", "a place to live"], "A toy is something we want but do not need.")
H('9.B', 3, "Ava has some income. Which should she choose first?", "food for dinner", ["a new toy", "candy", "a video game"], "Needs come before wants.")
H('9.C', 2, "Ben keeps $5 in a jar to use later. What is he doing?", "saving", ["spending", "giving", "earning"], "Keeping money to use later is saving.")
H('9.C', 2, "Ava buys a snack at the store with her money. What is she doing?", "spending", ["saving", "earning", "giving it away for free"], "Using money to buy something is spending.")
H('9.C', 3, "Which is an example of saving?", "putting coins in a piggy bank", ["buying a toy right away", "buying candy", "paying for a movie"], "Saving means keeping money for later.")
H('9.C', 3, "Which is an example of spending?", "paying for a book at a store", ["putting coins in a jar", "keeping a dollar in a drawer", "adding money to a bank account"], "Spending means using money to buy something.")
H('9.C', 3, "Dev wants a $10 game. He has $4. What could he do?", "save a little money each week", ["spend the $4 on candy", "ask for the game for free", "never think about it"], "Saving a little at a time helps reach a goal.")
H('9.D', 2, "A person gives food to families who need it. What is this called?", "charitable giving", ["spending", "earning", "borrowing"], "Giving to help others is charitable giving.")
H('9.D', 3, "Which is an example of charitable giving?", "giving old coats to people who are cold", ["buying a new coat for yourself", "selling a coat", "losing a coat"], "Charitable giving helps other people.")
H('9.D', 3, "Why do people give to charity?", "to help others", ["to get paid back", "to buy candy", "to hide money"], "Charity is about helping other people.")
H('9.D', 3, "Ava gives a dollar to an animal shelter. What is she doing?", "giving to help animals", ["earning money", "buying a toy", "saving for a game"], "Giving a gift to help animals is charitable giving.")
H('9.D', 2, "Which one is a way to help others?", "giving food to a food drive", ["buying a toy for yourself", "keeping all your money", "spending on candy"], "Donating to a food drive helps others.")

n = B.save(os.path.join(os.path.dirname(__file__), '..', 'batches', 'g1_math.jsonl'))
print("wrote", n, "questions")

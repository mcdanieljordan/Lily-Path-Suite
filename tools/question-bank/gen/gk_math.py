#!/usr/bin/env python3
"""Kindergarten Mathematics (TEKS 111.2.b) - original questions. Run: python3 gen/gk_math.py  -> batches/gk_math.jsonl
   Pictures are emoji so a teacher can read the question aloud and the class can count on the screen."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('111.2.b.', 101, no_neg=True, own='gk_math.jsonl')
R, mk, H, rep = B.R, B.mk, B.hand, B.rep
NM = ["Ava", "Ben", "Cara", "Dev", "Eli", "Fay", "Gus", "Hana", "Ivan", "Jo", "Kai", "Lena", "Max", "Nia", "Omar", "Pia", "Raj", "Sam", "Tia", "Zoe"]
OBJ = [("apples", "🍎"), ("stars", "⭐"), ("frogs", "🐸"), ("balls", "⚽"), ("cars", "🚗"), ("dogs", "🐶"), ("flowers", "🌸"), ("cookies", "🍪"), ("birds", "🐦"), ("hearts", "❤️"), ("cats", "🐱"), ("bees", "🐝")]
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()
DIE = "⚀⚁⚂⚃⚄⚅"
def who(): return R.choice(NM)
def obj(): return R.choice(OBJ)
def em(e, n): return ' '.join(e * min(5, n - i) for i in range(0, n, 5))
def ws(r, ds=(1, -1, 2, -2, 3, -3, 10, -10), lo=0, hi=20):
    return [r + d for d in ds if lo <= r + d <= hi and r + d != r]

# ---------------------------------------------------------------- 2.A count forward and backward
def a_next():
    s = R.randint(0, 16)
    return mk('2.A', 2, f"What number comes next?  {s}, {s + 1}, {s + 2}, __", s + 3, ws(s + 3), f"Count forward: {s}, {s + 1}, {s + 2}, {s + 3}.", CS(f"{s}+3"))
def a_back():
    s = R.randint(4, 20)
    return mk('2.A', 2, f"Count backward.  {s}, {s - 1}, {s - 2}, __", s - 3, ws(s - 3), f"Count backward: {s}, {s - 1}, {s - 2}, {s - 3}.", CS(f"{s}-3"))
def a_missing():
    s = R.randint(0, 15)
    return mk('2.A', 3, f"What number is missing?  {s}, {s + 1}, __, {s + 3}, {s + 4}", s + 2, ws(s + 2), f"Counting forward, {s + 2} comes after {s + 1}.", CS(f"{s}+2"))
def a_before():
    n = R.randint(2, 19); after = R.random() < .5
    if after: return mk('2.A', 2, f"What number comes right after {n}?", n + 1, ws(n + 1), f"Counting forward, {n + 1} comes right after {n}.", CS(f"{n}+1"))
    return mk('2.A', 2, f"What number comes right before {n}?", n - 1, ws(n - 1), f"Counting forward, {n - 1} comes right before {n}.", CS(f"{n}-1"))
rep(2, a_next); rep(2, a_back); rep(2, a_missing); rep(2, a_before)

# ---------------------------------------------------------------- 2.B read, write, represent
def b_numeral():
    n = R.randint(3, 20); pn, e = obj(); nm = who()
    return mk('2.B', 2 if n <= 10 else 3, f"{nm} counts the {pn}:  {em(e, n)}   Which numeral shows how many {pn}?", n,
              ws(n) + ([int(str(n)[::-1])] if n > 9 and str(n)[::-1] != str(n) else []), f"Count each one. There are {n}.", CS(f"{n}"))
def b_word():
    n = R.randint(5, 19)
    return mk('2.B', 2, f"Which numeral is the number {ONES[n]}?", n, ws(n) + ([int(str(n)[::-1])] if str(n)[::-1] != str(n) else []), f"{ONES[n]} is written {n}.", CS(f"{n}"))
rep(4, b_numeral); rep(3, b_word)

# ---------------------------------------------------------------- 2.C count a set, last number tells how many
def c_last():
    n = R.randint(4, 12); pn, e = obj(); nm = who()
    return mk('2.C', 2, f"{nm} counts the {pn}:  {em(e, n)}   {nm} points to each one and says {', '.join(str(i) for i in range(1, n + 1))}. How many {pn} are there in all?",
              n, ws(n, (1, -1, 2, -2)), f"The last number said, {n}, tells how many there are.", CS(f"{n}"))
def c_move():
    n = R.randint(4, 15); nm = who(); things = R.choice(["cubes", "buttons", "blocks", "crayons", "marbles"])
    return mk('2.C', 2, f"{nm} counts {n} {things} in a row. Then {nm} puts the same {things} in a pile. How many {things} are in the pile?",
              n, ws(n, (1, -1, 2, -2)), f"Moving them does not change how many there are. There are still {n}.", CS(f"{n}"))
rep(3, c_last); rep(2, c_move)
H('2.C', 3, "When you count a group of objects, what does the LAST number you say tell you?", "how many objects are in the group", ["which object is the biggest", "which object is the first one", "what color the objects are"], "The last number said tells how many there are in all.")

# ---------------------------------------------------------------- 2.D recognize small groups instantly
def d_die():
    n = R.randint(1, 6); nm = who()
    return mk('2.D', 2, f"{nm} rolls a die and gets {DIE[n - 1]}.  How many dots are on the die?", n, [x for x in range(1, 7) if x != n], f"The die shows {pl(n, 'dot')}.", CS(f"{n}"))
def d_quick():
    n = R.randint(2, 5); pn, e = obj(); nm = who()
    a = R.randint(0, n); arr = (e * a + '    ' + e * (n - a)).strip()
    return mk('2.D', 2, f"Quick look!  {nm} sees   {arr}   How many {pn} did {nm} see?", n, [x for x in range(1, 8) if x != n], f"Count the small group: there are {n}.", CS(f"{n}"))
rep(4, d_die); rep(3, d_quick)

# ---------------------------------------------------------------- 2.E generate a set more than, less than, equal
def e_more():
    n = R.randint(3, 16); pn, e = obj(); m = R.randint(n + 1, 20)
    wrong = R.sample([x for x in range(1, n + 1)], min(3, n))
    return mk('2.E', 3, f"Which group has MORE than {n} {pn}?", em(e, m), [em(e, w) for w in wrong], f"{m} is more than {n}.")
def e_less():
    n = R.randint(4, 17); pn, e = obj(); m = R.randint(1, n - 1)
    wrong = R.sample([x for x in range(n, 21)], 3)
    return mk('2.E', 4 if n >= 14 else 3, f"Which group has LESS than {n} {pn}?", em(e, m), [em(e, w) for w in wrong], f"{m} is less than {n}.")
def e_same():
    n = R.randint(4, 14); pn, e = obj(); nm = who()
    return mk('2.E', 3, f"{nm} needs a group with exactly {n} {pn}. Which group has exactly {n}?", em(e, n), [em(e, w) for w in ws(n, (1, -1, 2, -2))], f"{n} is equal to {n}: the same number.")
rep(3, e_more); rep(2, e_less); rep(2, e_same)

# ---------------------------------------------------------------- 2.F one more, one less
def f_more():
    n = R.randint(0, 19)
    return mk('2.F', 2, f"What number is one more than {n}?", n + 1, ws(n + 1, (1, -1, 2, -2, 10)), f"{n} + 1 = {n + 1}.", CS(f"{n}+1"))
def f_less():
    n = R.randint(1, 20)
    return mk('2.F', 2, f"What number is one less than {n}?", n - 1, ws(n - 1, (1, -1, 2, -2, 10)), f"{n} − 1 = {n - 1}.", CS(f"{n}-1"))
def f_story():
    n = R.randint(3, 18); pn, e = obj(); nm = who()
    return mk('2.F', 3, f"{nm} has {n} {pn}. {nm} gets one more. How many {pn} does {nm} have now?", n + 1, ws(n + 1, (1, -1, 2, -2)), f"One more than {n} is {n + 1}.", CS(f"{n}+1"))
rep(3, f_more); rep(3, f_less); rep(1, f_story)

# ---------------------------------------------------------------- 2.G compare sets
def g_cmp():
    a, b = R.sample(NM, 2); (p1, e1), (p2, e2) = R.sample(OBJ, 2)
    x = R.randint(1, 9); y = R.randint(1, 9)
    setx, sety = em(e1, x), em(e2, y)
    base = f"{a} has {setx}  and {b} has {sety}."
    if x == y:
        return mk('2.G', 3, f"{base}  Which statement is true?", "They have the same number.", [f"{a} has more.", f"{b} has more."], f"{x} and {y} are the same number.", need=2)
    word = R.choice(["more", "fewer"]); big = a if x > y else b; small = b if x > y else a
    win = big if word == "more" else small
    lose = small if word == "more" else big
    return mk('2.G', 2 if abs(x - y) > 2 else 3, f"{base}  Who has {word}?", f"{win} has {word}.", [f"{lose} has {word}.", "They have the same number."], f"{max(x, y)} is more than {min(x, y)}, so {big} has more and {small} has fewer.", need=2)
rep(7, g_cmp)

# ---------------------------------------------------------------- 2.H comparative language for numerals
def h_two():
    a, b = R.sample(range(0, 21), 2); w = R.choice(["greater", "less"])
    right = max(a, b) if w == "greater" else min(a, b)
    return mk('2.H', 2, f"Which number is {w}, {a} or {b}?", right, [min(a, b) if w == "greater" else max(a, b)], f"{max(a, b)} is greater than {min(a, b)}.", CS(f"{'max' if w == 'greater' else 'min'}({a},{b})"), need=1)
def h_than():
    n = R.randint(3, 16); w = R.choice(["greater", "less"])
    if w == "greater":
        r = R.randint(n + 1, 20); wr = R.sample(range(0, n + 1), 3)
    else:
        r = R.randint(0, n - 1); wr = R.sample(range(n, 21), 3)
    return mk('2.H', 3, f"Which number is {w} than {n}?", r, wr, f"{r} is {w} than {n}.")
def h_blank():
    a, b = R.sample(range(0, 21), 2)
    right = "less than" if a < b else "greater than"
    return mk('2.H', 4 if abs(a - b) <= 2 else 3, f"Which words make this true?  {a} is ___ {b}.", right, ["greater than" if a < b else "less than", "the same as"], f"{a} is {right} {b}.", need=2)
rep(2, h_two); rep(3, h_than); rep(2, h_blank)

# ---------------------------------------------------------------- 2.I compose and decompose to 10
def i_rest():
    t = R.randint(5, 10); a = R.randint(1, t - 1); pn, e = obj(); nm = who()
    return mk('2.I', 4 if t >= 9 else 3, f"{nm} has {t} {pn}:  {em(e, t)}   {a} of them are in a box and the rest are on a table. How many are on the table?", t - a, ws(t - a, (1, -1, 2, -2), 0, 10) + [t], f"{t} is {a} and {t - a}.", CS(f"{t}-{a}"))
def i_pair():
    t = R.randint(4, 10); a = R.randint(1, t - 1); pair = lambda x, y: f"{x} and {y}"
    wrong = []
    while len(wrong) < 3:
        x = R.randint(1, 9); y = R.randint(1, 9)
        if x + y != t and pair(x, y) not in wrong and pair(y, x) not in wrong and pair(x, y) != pair(a, t - a): wrong.append(pair(x, y))
    return mk('2.I', 3, f"Which two numbers make {t} when you put them together?", pair(a, t - a), wrong, f"{a} + {t - a} = {t}.")
rep(3, i_rest); rep(4, i_pair)

# ---------------------------------------------------------------- 3.A joining and separating
def j_story():
    nm = who(); pn, e = obj()
    if R.random() < .5:
        a = R.randint(1, 8); b = R.randint(1, 10 - a)
        return mk('3.A', 2, f"{nm} has {a} {pn}. {nm} gets {b} more.  Which number sentence shows what happened?", f"{a} + {b} = {a + b}",
                  [f"{a} − {b} = {max(a - b, 0)}" if a >= b else f"{a + b} − {a} = {b}", f"{a} + {b} = {a + b + 1}", f"{a + b} − {a} = {b}" if a >= b else f"{b} + {b} = {2 * b}"], "Getting more is joining. Joining is addition.")
    a = R.randint(3, 10); b = R.randint(1, a - 1)
    return mk('3.A', 2, f"{nm} has {a} {pn}. {b} of them {'goes' if b == 1 else 'go'} away.  Which number sentence shows what happened?", f"{a} − {b} = {a - b}",
              [f"{a} + {b} = {a + b}", f"{a} − {b} = {a - b + 1}", f"{b} + {b} = {2 * b}"], "Going away is separating. Separating is subtraction.")
rep(7, j_story)

# ---------------------------------------------------------------- 3.B word problems within 10
def w_add():
    nm = who(); a = R.randint(1, 8); b = R.randint(1, 10 - a); pn, e = obj()
    return mk('3.B', 2, f"{nm} has {a} {pn}. A friend gives {nm} {b} more. How many {pn} does {nm} have now?", a + b, ws(a + b, (1, -1, 2), 0, 10) + [a, b], f"{a} + {b} = {a + b}.", CS(f"{a}+{b}"))
def w_sub():
    nm = who(); a = R.randint(4, 10); b = R.randint(1, a - 1); pn, e = obj()
    return mk('3.B', 3 if a >= 8 else 2, f"{nm} has {a} {pn}. {nm} gives {b} to a friend. How many {pn} does {nm} have left?", a - b, ws(a - b, (1, -1, 2), 0, 10) + [a, b], f"{a} − {b} = {a - b}.", CS(f"{a}-{b}"))
rep(4, w_add); rep(3, w_sub)

# ---------------------------------------------------------------- 3.C explain strategies
STR = ["counting on", "counting back", "skip counting by 2s", "guessing"]
def s_on():
    nm = who(); a = R.randint(2, 7); b = R.randint(2, 3)
    seq = ', '.join(str(a + i) for i in range(1, b + 1))
    return mk('3.C', 3, f"{nm} wants to solve {a} + {b}. {nm} starts at {a} and says {seq}. Which strategy did {nm} use?", "counting on", [s for s in STR if s != "counting on"], f"Starting at {a} and saying the next numbers is counting on.")
def s_back():
    nm = who(); a = R.randint(5, 10); b = 2
    seq = ', '.join(str(a - i) for i in range(1, b + 1))
    return mk('3.C', 3, f"{nm} wants to solve {a} − {b}. {nm} starts at {a} and says {seq}. Which strategy did {nm} use?", "counting back", [s for s in STR if s != "counting back"], f"Starting at {a} and saying the numbers that come before it is counting back.")
def s_pic():
    nm = who(); a = R.randint(1, 5); b = R.randint(1, 5); (p1, e1), (p2, e2) = R.sample(OBJ, 2)
    return mk('3.C', 4, f"{nm} draws {em(e1, a)}   and   {em(e2, b)}   to show a number story. Which number sentence matches the drawing?", f"{a} + {b} = {a + b}",
              [f"{a} + {b} = {a + b + 1}", f"{a + b} − {b} = {a}" if a != b else f"{a + b} + {a} = {2 * a + b}", f"{a} + {b} = {abs(a - b)}" if a != b else f"{a} + {b} = {a + b - 1}"], f"{a} and {b} joined make {a + b}.")
rep(3, s_on); rep(1, s_back); rep(3, s_pic)

# ---------------------------------------------------------------- 6.A identify 2-D shapes
SH = ["circle", "triangle", "rectangle", "square"]
for desc, sh in [("the face of a clock", "circle"), ("a dinner plate", "circle"), ("a slice of pizza", "triangle"), ("a door", "rectangle"), ("the cover of a book", "rectangle"), ("the lid of a pizza box", "square"), ("a sticky note", "square")]:
    wr = [s for s in ["circle", "triangle", "square", "rectangle"] if s != sh and not (sh == "square" and s == "rectangle")]
    H('6.A', 2, f"What shape is {desc}?", sh, wr, f"{desc[0].upper() + desc[1:]} is shaped like a {sh}.", need=len(wr) if len(wr) < 3 else 3)
H('6.A', 3, "A square is a special kind of which shape?", "rectangle", ["circle", "triangle", "hexagon"], "A square has 4 square corners and 4 sides, so it is a special rectangle.")

# ---------------------------------------------------------------- 6.B identify 3-D solids
SOL = ["sphere", "cylinder", "cone", "cube"]
for desc, sol in [("a basketball", "sphere"), ("a can of soup", "cylinder"), ("a pointed clown hat", "cone"), ("a die from a board game", "cube"), ("a globe of the Earth", "sphere"), ("a drum", "cylinder"), ("a party hat", "cone")]:
    H('6.B', 2, f"Which solid is shaped like {desc}?", sol, [s for s in SOL if s != sol], f"{desc[0].upper() + desc[1:]} is shaped like a {sol}.")

# ---------------------------------------------------------------- 6.C 2-D components of 3-D objects
H('6.C', 2, "What shape is the flat top of a can?", "circle", ["square", "triangle", "rectangle"], "The top and bottom of a cylinder are circles.")
H('6.C', 3, "What shape is each face of a cube?", "square", ["circle", "triangle", "hexagon"], "A cube has 6 faces. Each one is a square.")
H('6.C', 3, "If you trace the bottom of a cone on paper, what shape do you draw?", "circle", ["triangle", "square", "rectangle"], "The flat bottom of a cone is a circle.")
H('6.C', 3, "If you trace one face of a cube, what shape do you draw?", "square", ["circle", "triangle", "rectangle"], "Each face of a cube is a square.")
H('6.C', 3, "A cylinder has two flat faces. What shape are they?", "circles", ["squares", "triangles", "rectangles"], "The two flat faces of a cylinder are circles.")
H('6.C', 3, "How many square faces does a cube have?", "6", ["4", "8", "2"], "A cube has 6 faces and each one is a square.")

# ---------------------------------------------------------------- 6.D attributes of 2-D shapes
for sh, n in [("triangle", 3), ("square", 4), ("rectangle", 4)]:
    mk('6.D', 2, f"How many sides does a {sh} have?", n, [x for x in (2, 3, 4, 5, 6, 8) if x != n], f"A {sh} has {n} sides.", CS(f"{n}"))
    mk('6.D', 2, f"How many corners does a {sh} have?", n, [x for x in (2, 3, 4, 5, 6, 8) if x != n], f"A {sh} has {n} corners (vertices).", CS(f"{n}"))
H('6.D', 3, "A vertex is the point where two sides of a shape meet. What is another word for a vertex?", "corner", ["edge", "face", "side"], "A vertex is a corner.")

# ---------------------------------------------------------------- 6.E classify and sort
H('6.E', 3, "Three of these shapes are triangles and one is not. Which one is NOT a triangle?", "a square", ["a tall triangle", "a tiny triangle", "an upside-down triangle"], "A triangle is a triangle no matter its size or which way it points. A square has 4 sides.")
H('6.E', 3, "We sort shapes by how many sides they have. Which shape does NOT go with the squares and rectangles?", "a triangle", ["a tilted square", "a long rectangle", "a small square"], "Squares and rectangles have 4 sides. A triangle has 3 sides.")
H('6.E', 3, "Three of these things are round and one is not. Which one is NOT round?", "a box", ["a basketball", "a globe", "a marble"], "A box has flat sides and corners. The others are round.")
H('6.E', 3, "Which solid will NOT roll when you push it on a flat table?", "cube", ["sphere", "cylinder"], "A cube has flat faces and corners, so it will not roll.", need=2)
H('6.E', 3, "Which solid has one pointed top?", "cone", ["sphere", "cylinder", "cube"], "A cone comes to a point at the top.")
H('6.E', 3, "Which solid has NO curved surface?", "cube", ["cylinder", "cone", "sphere"], "A cube has only flat faces.")
H('6.E', 3, "Which shape has no straight sides and no corners?", "circle", ["triangle", "square", "rectangle"], "A circle is round all the way around.")

# ---------------------------------------------------------------- 6.F create shapes
H('6.F', 3, "Max joins 3 straight sticks at their ends to make a closed shape. What shape does he make?", "triangle", ["square", "circle", "rectangle"], "3 sides joined make a triangle.")
H('6.F', 3, "Lena makes a closed shape with 4 sticks that are all the same length and have corners like the corner of a sheet of paper. What shape is it?", "square", ["triangle", "circle", "hexagon"], "4 equal sides and 4 square corners make a square.")
H('6.F', 3, "Raj makes a closed shape with 2 long sticks and 2 short sticks that meet at corners like the corner of a sheet of paper. What shape is it?", "rectangle", ["triangle", "circle", "square"], "2 long sides and 2 short sides with square corners make a rectangle.")
H('6.F', 2, "How many sticks do you need to make a triangle?", "3", ["2", "4", "5"], "A triangle has 3 sides.")
H('6.F', 2, "Which could you use to make a circle on the floor?", "a loop of string", ["3 straight sticks", "4 straight sticks", "2 flat rulers"], "A loop of string can be shaped into a round circle.")
H('6.F', 3, "Ava draws a shape with no corners and no straight sides. What shape did she draw?", "circle", ["triangle", "square", "rectangle"], "A circle has no corners and no straight sides.")

# ---------------------------------------------------------------- 7.A measurable attributes
H('7.A', 2, "What does a ruler measure?", "length", ["weight", "capacity", "color"], "A ruler measures how long something is: its length.")
H('7.A', 2, "What does a scale measure?", "weight", ["length", "capacity", "color"], "A scale tells how heavy something is: its weight.")
H('7.A', 3, "What does a measuring cup measure?", "capacity", ["length", "weight", "color"], "A measuring cup shows how much a container can hold: its capacity.")
H('7.A', 2, "Which attribute tells how tall a tree is?", "length", ["weight", "capacity", "color"], "How tall something is, is a length.")
H('7.A', 2, "Which attribute tells how heavy a backpack is?", "weight", ["length", "capacity", "shape"], "How heavy something is, is its weight.")
H('7.A', 3, "Which attribute tells how much water a bucket can hold?", "capacity", ["length", "weight", "shape"], "How much a container can hold is its capacity.")
H('7.A', 3, "Which of these has a length you can measure?", "a pencil", ["a happy song", "the color red", "the number 5"], "A pencil is an object, and you can measure how long it is.")

# ---------------------------------------------------------------- 7.B compare two objects
PAIRS = [("elephant", "mouse", "w"), ("giraffe", "cat", "t"), ("bathtub", "teacup", "c"), ("bus", "bike", "l"), ("rock", "feather", "w"), ("bucket", "spoon", "c"), ("tree", "flower", "t")]
WORD = {"w": ("heavier than", "lighter than", "weigh the same"), "t": ("taller than", "shorter than", "are the same height"), "l": ("longer than", "shorter than", "are the same length"), "c": ("holds more than", "holds less than", "hold the same amount")}
for a, b, k in PAIRS:
    more, less, same = WORD[k]
    sw = lambda x, y, w: f"The {x} is {w} the {y}." if k != 'c' else f"The {x} {w} the {y}."
    same_s = f"The {a} and the {b} {same}."
    H('7.B', 2, f"Think about the {a} and the {b}. Which sentence is true?", sw(a, b, more), [sw(b, a, more), sw(a, b, less), same_s], f"The {a} has more of this attribute than the {b} does.")

# ---------------------------------------------------------------- 8.A collect, sort, organize data
FR = [("apples", "🍎"), ("bananas", "🍌"), ("grapes", "🍇"), ("cats", "🐱"), ("dogs", "🐶"), ("birds", "🐦"), ("frogs", "🐸")]
def t_most():
    kinds = R.sample(FR, 3); cnt = R.sample(range(1, 9), 3)
    most = max(range(3), key=lambda i: cnt[i]); fewest = min(range(3), key=lambda i: cnt[i])
    data = "   ".join(f"{k[1]} {c}" for k, c in zip(kinds, cnt))
    if R.random() < .5:
        return mk('8.A', 2, f"Votes for a class favorite:   {data}.   Which kind got the MOST votes?", kinds[most][0], [k[0] for i, k in enumerate(kinds) if i != most], f"{cnt[most]} is the greatest number.", need=2)
    return mk('8.A', 2, f"Votes for a class favorite:   {data}.   Which kind got the FEWEST votes?", kinds[fewest][0], [k[0] for i, k in enumerate(kinds) if i != fewest], f"{cnt[fewest]} is the least number.", need=2)
rep(6, t_most)
H('8.A', 2, "Ava sorts her toys into piles: cars, blocks, and balls. How many groups did she make?", "3", ["2", "4", "6"], "There are 3 piles: cars, blocks, and balls.")

# ---------------------------------------------------------------- 8.B create picture graphs
def g_make():
    nm = who(); (p1, e1), (p2, e2) = R.sample(FR, 2); a = R.randint(2, 6); b = R.randint(2, 6)
    if a == b: return False
    right = f"{em(e1, a)}  |  {em(e2, b)}"
    wrong = [f"{em(e1, b)}  |  {em(e2, a)}", f"{em(e1, a + 1)}  |  {em(e2, b)}", f"{em(e1, a)}  |  {em(e2, b + 1)}"]
    return mk('8.B', 3, f"{nm} counts {a} {p1} and {b} {p2}. Which picture graph matches?", right, wrong, f"{a} {p1} get {a} pictures and {b} {p2} get {b} pictures.")
rep(4, g_make)
def g_row():
    nm = who(); p, e = R.choice(FR); n = R.randint(2, 8)
    return mk('8.B', 2, f"{nm} makes a picture graph. There are {n} {p}. How many pictures go in the {p} row?", n, ws(n, (1, -1, 2), 1, 10), f"One picture for each one: {n} pictures.", CS(f"{n}"))
rep(2, g_row)

# ---------------------------------------------------------------- 8.C draw conclusions from graphs
def g_read():
    (p1, e1), (p2, e2) = R.sample(FR, 2); a = R.randint(2, 9); b = R.randint(1, 8)
    if a == b: return False
    big, small = max(a, b), min(a, b)
    kind = R.choice(["diff", "total"])
    gr = f"{p1.capitalize()}: {em(e1, a)}     {p2.capitalize()}: {em(e2, b)}"
    if kind == "diff":
        return mk('8.C', 4, f"Picture graph:   {gr}   How many more pictures are in the longer row than in the shorter row?", big - small, ws(big - small, (1, -1, 2, -2), 1, 12) + [big, small], f"{big} − {small} = {big - small}.", CS(f"{big}-{small}"))
    return mk('8.C', 3, f"Picture graph:   {gr}   How many pictures are in both rows together?", a + b, ws(a + b, (1, -1, 2, -2), 1, 20) + [big], f"{a} + {b} = {a + b}.", CS(f"{a}+{b}"))
rep(6, g_read)

# ---------------------------------------------------------------- 9 personal financial literacy
H('9.A', 2, "Which is a way for a person to earn money?", "working at a job", ["sleeping in bed", "watching a movie", "eating lunch"], "People earn money by working.")
H('9.A', 2, "A baker sells bread and gets paid. What is the baker doing?", "earning income", ["getting a gift", "spending money", "losing money"], "Money you get for working is income.")
H('9.A', 3, "Ava rakes leaves and her neighbor pays her. Ava is doing what?", "earning money", ["getting a present", "buying a toy", "saving a penny"], "She works and gets paid, so she earns money.")
H('9.A', 2, "Which person is earning money?", "a farmer selling vegetables", ["a child watching cartoons", "a child sleeping", "a child eating a snack"], "Selling things is a way to earn money.")
H('9.A', 3, "Who earns money by teaching children?", "a teacher", ["a firefighter", "a farmer", "a bus driver"], "A teacher is paid to teach children.")
H('9.A', 2, "Money that a person earns from a job is called what?", "income", ["a gift", "a toy", "a want"], "Income is money you earn.")
H('9.B', 2, "Ben gets $5 from his grandma on his birthday. Which word tells about this money?", "a gift", ["income"], "Money that someone gives you for a special day is a gift.", need=1)
H('9.B', 2, "Ava gets $5 for walking a neighbor's dog. Which word tells about this money?", "income", ["a gift"], "She worked for it, so it is income.", need=1)
H('9.B', 3, "Hana finds a $20 bill in a birthday card from her aunt. Which word tells about this money?", "a gift", ["income"], "Her aunt gave it to her, so it is a gift.", need=1)
H('9.B', 3, "Dev gets paid money each week for working at a store. Which word tells about this money?", "income", ["a gift"], "He gets it for working, so it is income.", need=1)
H('9.B', 2, "Which is a gift of money?", "money from a grandma for a birthday", ["money from a job", "money for mowing lawns", "money for selling lemonade"], "A gift is given to you and you do not work for it.")
H('9.B', 3, "Which is money received as income?", "pay for washing cars", ["a birthday card with money", "a coin a friend gives you", "money from a holiday present"], "Income is money you earn by working.")
for job, skill in [("teacher", "explaining things clearly"), ("bus driver", "driving safely"), ("firefighter", "staying calm and brave"), ("doctor", "caring for sick people"), ("farmer", "growing food"), ("librarian", "helping people find books")]:
    others = [s for _, s in [("teacher", "explaining things clearly"), ("bus driver", "driving safely"), ("firefighter", "staying calm and brave"), ("doctor", "caring for sick people"), ("farmer", "growing food"), ("librarian", "helping people find books")] if s != skill]
    H('9.C', 2, f"Which skill does a {job} need?", skill, R.sample(others, 3), f"A {job} needs the skill of {skill}.")
H('9.D', 2, "Which one do people NEED to live?", "water", ["a video game", "a toy car", "a new bike"], "Water is a need. The others are wants.")
H('9.D', 2, "Which one is a want, not a need?", "a toy robot", ["food", "water", "a place to live"], "People do not need a toy to live, so it is a want.")
H('9.D', 3, "Ava has money from her job. Which one does she NEED to buy?", "food", ["a video game", "candy", "a new toy"], "Food is a need.")
H('9.D', 3, "Ben has money from a job. Which one is something he WANTS but does not need?", "a video game", ["food", "water", "a place to live"], "A video game is a want.")
H('9.D', 3, "People use income to pay for things. Which need can income pay for?", "a place to live", ["a new toy", "a video game", "candy"], "A home is a need, and income can pay for it.")
H('9.D', 2, "Which of these is a want?", "candy", ["water", "food", "shelter"], "Candy is something we want, but we do not need it to live.")

n = B.save(os.path.join(os.path.dirname(__file__), '..', 'batches', 'gk_math.jsonl'))
print("wrote", n, "questions")

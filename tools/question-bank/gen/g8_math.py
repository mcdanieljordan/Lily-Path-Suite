#!/usr/bin/env python3
"""Grade 8 Mathematics (TEKS 111.28.b) - original questions. Run: python3 gen/g8_math.py -> batches/g8_math.jsonl"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from mid import *

B, mk = setup('111.28.b.', 808, 'g8_math.jsonl')
R, H, rep = B.R, B.hand, B.rep
def who(): return R.choice(NM)
SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")
def sup(n): return str(n).translate(SUP)

# ---- 2.A sets of real numbers
H('2.A', 2, "Which set of numbers includes both rational and irrational numbers?", "real numbers", ["integers", "whole numbers", "natural numbers"], "The real numbers are made of the rational and irrational numbers together.")
H('2.A', 3, "Which statement is true?", "Every integer is a rational number.", ["Every rational number is an integer.", "Every real number is rational.", "No integer is a real number."], "An integer n can be written as n/1.")
H('2.A', 3, "Which number is irrational?", "√7", ["√49", "0.75", "−3"], "√7 is a non-terminating, non-repeating decimal; √49 = 7.")
H('2.A', 3, "Which number is rational?", "0.333…", ["π", "√3", "√11"], "A repeating decimal equals 1/3, a ratio of integers.")
H('2.A', 4, "Where does −4 belong in a diagram of the real number system?", "integers, rational numbers and real numbers", ["whole numbers only", "irrational numbers", "natural numbers"], "Negative integers are integers, so they are rational and real, but not whole.")
H('2.A', 4, "A decimal that never ends and never repeats is...", "irrational", ["rational", "an integer", "a whole number"], "Only rational numbers have terminating or repeating decimals.")
H('2.A', 3, "Which set is a subset of the rational numbers?", "the integers", ["the irrational numbers", "numbers like π and √2", "numbers that are not real"], "Every integer is a rational number.")
H('2.A', 4, "Which number is a whole number, an integer, and a rational number?", "12", ["−12", "12.5", "√12"], "12 is not negative or fractional, so it is in all three sets.")

# ---- 2.B approximate irrational numbers
H('2.B', 3, "Between which two integers is √20?", "4 and 5", ["3 and 4", "5 and 6", "10 and 11"], "4² = 16 and 5² = 25, so √20 is between 4 and 5.")
H('2.B', 3, "Between which two integers is √50?", "7 and 8", ["6 and 7", "8 and 9", "25 and 26"], "49 < 50 < 64.")
H('2.B', 3, "Between which two integers is √90?", "9 and 10", ["8 and 9", "10 and 11", "45 and 46"], "81 < 90 < 100.")
H('2.B', 4, "Which is the best estimate of √30 to the nearest tenth?", "5.5", ["5.0", "5.9", "6.0"], "5.5² = 30.25, which is very close to 30.")
H('2.B', 4, "Which is the best estimate of √10 to the nearest tenth?", "3.2", ["3.0", "3.5", "3.9"], "3.2² = 10.24 and 3.1² = 9.61; 3.2 is closer.")
H('2.B', 3, "Which is the closest to the value of π as a fraction?", "22/7", ["7/22", "3/4", "31/10"], "22/7 ≈ 3.1429.")
H('2.B', 4, "Which point on a number line is the best placement for √15?", "just below 4", ["just above 4", "exactly 3", "exactly 4"], "√15 ≈ 3.87 since 3.9² ≈ 15.2.")
H('2.B', 4, "Which is closest to π² ?", "9.9", ["6.3", "3.1", "12.6"], "3.14² ≈ 9.86.")
H('2.B', 3, "Which number is closest to √2?", "1.4", ["1.2", "1.8", "2.0"], "1.4² = 1.96.")
H('2.B', 3, "Which is between 6 and 7?", "√40", ["√30", "√50", "√20"], "36 < 40 < 49.")
H('2.B', 3, "Which is between 2 and 3?", "√7", ["√10", "√3", "√16"], "4 < 7 < 9.")

# ---- 2.C scientific notation
def sci_to_std():
    m = R.choice([1.2, 2.5, 3.4, 4.7, 5.6, 6.1, 7.3, 8.9, 9.2]); e = R.randint(2, 6)
    v = round(m * 10 ** e)
    wrong = [f"{round(m * 10 ** (e + 1)):,}", f"{round(m * 10 ** (e - 1)):,}", f"{round(m * 10 ** e * 10):,}"]
    return mk('2.C', 3, f"Write {m} × 10{sup(e)} in standard form.", f"{v:,}", wrong, f"Move the decimal point {e} places right: {v:,}.")
rep(4, sci_to_std)
def std_to_sci():
    m = R.choice([1.5, 2.4, 3.7, 4.2, 5.8, 6.3, 7.9, 8.6]); e = R.randint(3, 8)
    v = round(m * 10 ** e)
    return mk('2.C', 3, f"Write {v:,} in scientific notation.", f"{m} × 10{sup(e)}", [f"{m} × 10{sup(e + 1)}", f"{m} × 10{sup(e - 1)}", f"{round(m * 10, 1)} × 10{sup(e)}"], f"Place the decimal after the first digit; that is {e} places, so {m} × 10{sup(e)}.")
rep(4, std_to_sci)
def small_to_sci():
    m = R.choice([2.5, 3.6, 4.1, 5.4, 6.8, 7.2, 8.3, 9.1]); e = R.randint(2, 6)
    s = f"{m / 10 ** e:.{e + 1}f}"
    return mk('2.C', 4, f"Write {s} in scientific notation.", f"{m} × 10{sup(-e)}", [f"{m} × 10{sup(e)}", f"{m} × 10{sup(-(e - 1))}", f"{m} × 10{sup(-(e + 1))}"], f"Move the decimal {e} places right to get {m}, so the exponent is −{e}.")
rep(4, small_to_sci)
H('2.C', 3, "Which is 4.5 × 10⁻³ in standard form?", "0.0045", ["4500", "0.045", "0.00045"], "A negative exponent moves the decimal left 3 places.")
H('2.C', 3, "Which number is written in scientific notation?", "3.2 × 10⁵", ["32 × 10⁴", "0.32 × 10⁶", "320 × 10³"], "The first factor must be at least 1 and less than 10.")
H('2.C', 4, "The distance from Earth to the Sun is about 93,000,000 miles. Which shows this in scientific notation?", "9.3 × 10⁷", ["9.3 × 10⁶", "93 × 10⁶", "9.3 × 10⁸"], "Eight digits means 7 places after the first digit.")
H('2.C', 4, "A cell is about 0.000012 meters wide. Which is its width in scientific notation?", "1.2 × 10⁻⁵", ["1.2 × 10⁵", "1.2 × 10⁻⁶", "12 × 10⁻⁶"], "The decimal moves 5 places to the right.")

# ---- 2.D order real numbers
H('2.D', 3, "Which list is in order from least to greatest?", "−2, −0.5, √2, 2", ["−0.5, −2, √2, 2", "2, √2, −0.5, −2", "−2, √2, −0.5, 2"], "√2 ≈ 1.41 is between −0.5 and 2.")
H('2.D', 3, "Which number is greatest?", "√17", ["4", "3.9", "15/4"], "√17 ≈ 4.12.")
H('2.D', 3, "Which number is least?", "−√10", ["−3", "−3.1", "−π"], "−√10 ≈ −3.16, which is farther left than −π ≈ −3.14.")
H('2.D', 3, "Which is between 3 and 4?", "√11", ["√20", "√5", "√16"], "9 < 11 < 16.")
H('2.D', 4, "Which comparison is true?", "√5 < 2.3", ["√5 > 2.3", "√5 = 2.3", "√5 > 3"], "√5 ≈ 2.236.")
H('2.D', 4, "A scientist compares 4.2 × 10³, 3.9 × 10⁴ and 5 × 10². Which is the greatest value in standard form?", "39,000", ["4,200", "500", "3,900"], "3.9 × 10⁴ = 39,000, which is larger than 4,200 and 500.")

H('2.D', 4, "Which list is in order from greatest to least?", "22/7, π, 3.1", ["3.1, π, 22/7", "π, 22/7, 3.1", "3.1, 22/7, π"], "22/7 ≈ 3.1429, π ≈ 3.1416, and 3.1 is smallest.")
H('2.D', 4, "Which is greater, 2/3 or √0.36?", "2/3", ["√0.36", "They are equal", "They cannot be compared"], "√0.36 = 0.6 and 2/3 ≈ 0.667.")

# ---- 3.A similar shapes proportional
H('3.A', 3, "A triangle is dilated by a scale factor of 3. A side of 4 becomes...", "12", ["7", "4/3", "1"], "4 × 3 = 12.")
H('3.A', 3, "Two similar rectangles have sides 2 by 5 and 6 by x. What is x?", "15", ["10", "13", "3"], "The scale factor is 3, so x = 5 × 3.")
H('3.A', 4, "Triangle ABC is similar to triangle DEF. AB = 6, DE = 9 and BC = 8. What is EF?", "12", ["10", "11", "9"], "The scale factor is 9/6 = 1.5, and 8 × 1.5 = 12.")
H('3.A', 3, "In a dilation, corresponding angles are...", "congruent", ["doubled", "halved", "always right angles"], "A dilation changes size, not angle measure.")
H('3.A', 4, "A photo is 4 in. by 6 in. It is enlarged so its short side is 10 in. How long is the long side?", "15 in.", ["12 in.", "14 in.", "16 in."], "The scale factor is 2.5, so 6 × 2.5 = 15.")
H('3.A', 4, "The ratio of corresponding sides of two similar triangles is 2:5. If a side of the small triangle is 8, the matching side of the large triangle is...", "20", ["3.2", "13", "10"], "8 ÷ 2 × 5 = 20.")
H('3.A', 3, "A scale factor of 1/2 produces a figure that is...", "smaller than the original", ["larger than the original", "the same size", "turned upside down"], "A factor less than 1 shrinks the figure.")
H('3.A', 4, "A map uses a scale of 1 cm : 20 km. Two cities are 6 cm apart on the map. What is the real distance?", "120 km", ["26 km", "3.3 km", "12 km"], "6 × 20 = 120.")

# ---- 3.B compare shape and dilation on coordinate plane
H('3.B', 3, "The point (2, 3) is dilated from the origin by a scale factor of 2. What are the new coordinates?", "(4, 6)", ["(4, 3)", "(2, 6)", "(1, 1.5)"], "Multiply both coordinates by 2.")
H('3.B', 3, "The point (6, 9) is dilated from the origin by a scale factor of 1/3. What are the new coordinates?", "(2, 3)", ["(18, 27)", "(3, 6)", "(2, 9)"], "Multiply both coordinates by 1/3.")
H('3.B', 4, "A triangle with vertices (1, 1), (3, 1), (1, 4) is dilated by a factor of 2 from the origin. What is the image of (3, 1)?", "(6, 2)", ["(5, 1)", "(3, 2)", "(6, 1)"], "(3×2, 1×2) = (6, 2).")
H('3.B', 4, "After a dilation from the origin, which attribute of a shape is the same?", "its angle measures", ["its side lengths", "its area", "its perimeter"], "Dilations keep shape (angles) but change size unless the factor is 1.")
H('3.B', 4, "A rectangle has vertices (0, 0), (4, 0), (4, 2), (0, 2). It is dilated by a factor of 3 from the origin. What is the new area?", "72", ["24", "36", "8"], "The new rectangle is 12 by 6, so the area is 72.")
H('3.B', 3, "A dilation with a scale factor greater than 1 is called an...", "enlargement", ["reduction", "reflection", "translation"], "Factors above 1 make the figure larger.")
H('3.B', 4, "How do the side lengths of a figure and its dilation by 3 compare?", "Each side of the image is 3 times as long", ["Each side is 3 units longer", "Each side is 1/3 as long", "They are the same"], "Dilation multiplies lengths by the scale factor.")

# ---- 3.C algebraic representation of dilation
H('3.C', 3, "Which rule describes a dilation by a scale factor of 4 from the origin?", "(x, y) → (4x, 4y)", ["(x, y) → (x + 4, y + 4)", "(x, y) → (x/4, y/4)", "(x, y) → (4x, y)"], "Every coordinate is multiplied by 4.")
H('3.C', 3, "Which rule describes a dilation by a scale factor of 1/2 from the origin?", "(x, y) → (x/2, y/2)", ["(x, y) → (2x, 2y)", "(x, y) → (x − 2, y − 2)", "(x, y) → (x/2, y)"], "Every coordinate is multiplied by 1/2.")
H('3.C', 4, "A point (8, −4) is dilated by (x, y) → (1.5x, 1.5y). What is the image?", "(12, −6)", ["(9.5, −2.5)", "(12, −4)", "(8, −6)"], "1.5 × 8 = 12 and 1.5 × (−4) = −6.")
H('3.C', 4, "The rule (x, y) → (2.5x, 2.5y) is applied. What is the image of (4, 6)?", "(10, 15)", ["(6.5, 8.5)", "(10, 6)", "(1.6, 2.4)"], "2.5 × 4 = 10 and 2.5 × 6 = 15.")
H('3.C', 4, "Which scale factor takes (6, 10) to (3, 5)?", "1/2", ["2", "3", "−1"], "3/6 = 5/10 = 1/2.")
H('3.C', 4, "Which scale factor takes (2, 5) to (6, 15)?", "3", ["1/3", "4", "10"], "6/2 = 15/5 = 3.")
H('3.C', 3, "A scale factor of 1 creates a figure that is...", "congruent to the original", ["smaller", "larger", "reflected"], "Multiplying by 1 changes nothing.")

# ---- 4.A slope from similar triangles
def slope_pts():
    x1 = R.randint(-3, 3); y1 = R.randint(-3, 3); dx = R.randint(1, 4); m = R.choice([-3, -2, -1, 1, 2, 3, F(1, 2), F(3, 2)])
    dy = m * dx
    if dy.denominator != 1 if isinstance(dy, F) else False: return False
    dy = int(dy); x2 = x1 + dx; y2 = y1 + dy
    r = F(dy, dx)
    wrong = [ims(-r), ims(F(dx, dy)) if dy else "0", sg(dx + dy)]
    return mk('4.A', 4, f"What is the slope of the line through ({sg(x1)}, {sg(y1)}) and ({sg(x2)}, {sg(y2)})?", ims(r), wrong, f"Slope = rise ÷ run = {sg(dy)}/{dx}" + ("" if ims(r) == f"{sg(dy)}/{dx}" else f" = {ims(r)}") + ".")
rep(8, slope_pts)
H('4.A', 3, "Slope is the ratio of which two changes?", "the change in y to the change in x", ["the change in x to the change in y", "x added to y", "y minus x"], "Slope = rise over run.")
H('4.A', 3, "A line goes up 6 units for every 3 units to the right. What is its slope?", "2", ["1/2", "3", "18"], "6/3 = 2.")
H('4.A', 4, "A line goes down 4 units for every 8 units to the right. What is its slope?", "−1/2", ["−2", "1/2", "2"], "−4/8 = −1/2.")
H('4.A', 3, "A horizontal line has a slope of...", "0", ["1", "undefined", "−1"], "There is no vertical change.")
H('4.A', 4, "A vertical line has a slope that is...", "undefined", ["0", "1", "positive"], "The run is 0, and you cannot divide by 0.")
H('4.A', 4, "Why can any two points on a line be used to find its slope?", "similar right triangles drawn along the line have the same ratio of rise to run", ["the slope changes between points", "only the first two points work", "the line must go through the origin"], "All the slope triangles are similar, so rise/run is constant.")

# ---- 4.B graph proportional relationships
H('4.B', 3, "A line through the origin passes through (4, 12). What is its unit rate (slope)?", "3", ["1/3", "8", "16"], "12 ÷ 4 = 3.")
H('4.B', 3, "A proportional relationship is graphed as...", "a straight line through the origin", ["a curve", "a line that crosses the y-axis at 5", "a horizontal line at y = 1"], "y = kx passes through (0, 0).")
H('4.B', 4, "A car travels 150 miles in 3 hours at a steady rate. What is the slope of the line of distance versus time?", "50 miles per hour", ["3 miles per hour", "450 miles per hour", "153 miles per hour"], "150 ÷ 3 = 50.")
H('4.B', 4, "A graph of cost versus pounds goes through (0, 0) and (5, 20). What does the slope represent?", "the price of one pound", ["the total cost", "the number of pounds", "the starting fee"], "20 ÷ 5 = 4 dollars per pound.")
H('4.B', 3, "Which equation has a graph that passes through the origin?", "y = 6x", ["y = 6x + 1", "y = x − 6", "y = 6"], "y = kx always contains (0, 0).")
H('4.B', 4, "A graph of y = 2.5x passes through which point?", "(4, 10)", ["(4, 6.5)", "(4, 8)", "(2.5, 4)"], "2.5 × 4 = 10.")

# ---- 4.C rate of change and y-intercept from table or graph
def tbl_line():
    m = R.randint(2, 7); b = R.randint(1, 9); xs = [0, 1, 2, 3]
    ys = [m * x + b for x in xs]
    return mk('4.C', 3, f"A table shows x = 0, 1, 2, 3 and y = {', '.join(map(str, ys))}. What is the y-intercept?", str(b), [str(m), str(ys[-1]), str(m + b)], f"When x = 0, y = {b}.")
rep(4, tbl_line)
def tbl_slope():
    m = R.randint(2, 8); b = R.randint(1, 9); xs = [0, 2, 4, 6]
    ys = [m * x + b for x in xs]
    return mk('4.C', 4, f"A table shows x = 0, 2, 4, 6 and y = {', '.join(map(str, ys))}. What is the rate of change?", str(m), [str(2 * m), str(b), str(m + b)], f"y rises {2 * m} when x rises 2, so the rate is {m}.")
rep(4, tbl_slope)
H('4.C', 4, "A plumber charges a flat fee plus an hourly rate. The graph passes through (0, 40) and (2, 100). What is the hourly rate?", "$30", ["$40", "$60", "$20"], "(100 − 40) ÷ 2 = 30.")
H('4.C', 4, "In the same situation, a graph passes through (0, 40) and (2, 100). What does the y-intercept mean?", "the flat fee of $40", ["the hourly rate", "the total after 2 hours", "the number of hours"], "At 0 hours the cost is just the fee.")
H('4.C', 4, "A water tank has 50 gallons and loses 5 gallons each minute. What is the rate of change?", "−5 gallons per minute", ["5 gallons per minute", "50 gallons per minute", "−50 gallons per minute"], "The amount decreases by 5 each minute.")
H('4.C', 3, "A graph crosses the y-axis at (0, −2). The y-intercept is...", "−2", ["2", "0", "−2 for x"], "The y-intercept is the y-value where x = 0.")

# ---- 5.A y = kx
H('5.A', 3, "Notebooks cost $2 each. Which equation gives the cost y of x notebooks?", "y = 2x", ["y = x + 2", "y = 4x", "y = x/2"], "Each notebook costs $2, so y = 2x.")
H('5.A', 3, "A table shows x = 1, 2, 3 and y = 7, 14, 21. Which equation fits?", "y = 7x", ["y = x + 6", "y = 7 + x", "y = 21x"], "y is always 7 times x.")
H('5.A', 4, "A runner covers 12 miles in 2 hours at a constant rate. Which equation gives distance d in t hours?", "d = 6t", ["d = 12t", "d = t + 10", "d = 2t"], "12 ÷ 2 = 6 miles per hour.")
H('5.A', 4, "The line y = kx passes through (5, 20). What is k?", "4", ["15", "100", "1/4"], "20 ÷ 5 = 4.")
H('5.A', 3, "Which table shows a proportional relationship y = kx?", "x: 1, 2, 3 and y: 5, 10, 15", ["x: 1, 2, 3 and y: 6, 11, 16", "x: 1, 2, 3 and y: 4, 6, 8", "x: 1, 2, 3 and y: 5, 6, 7"], "The ratio y/x is always 5.")
H('5.A', 4, "A recipe uses 3 cups of flour for every 2 batches. Which equation gives flour f for b batches?", "f = 1.5b", ["f = 3b", "f = b + 1", "f = 2b"], "3 ÷ 2 = 1.5 cups per batch.")

# ---- 5.B y = mx + b
H('5.B', 3, "A gym costs $25 to join and $10 per month. Which equation gives the total cost y after x months?", "y = 10x + 25", ["y = 25x + 10", "y = 35x", "y = 10x − 25"], "$10 per month plus a $25 fee.")
H('5.B', 3, "A table shows x = 0, 1, 2 and y = 4, 7, 10. Which equation fits?", "y = 3x + 4", ["y = 4x + 3", "y = 3x", "y = x + 4"], "The slope is 3 and the y-intercept is 4.")
H('5.B', 4, "A line has slope −2 and passes through (0, 6). Which is its equation?", "y = −2x + 6", ["y = 6x − 2", "y = 2x + 6", "y = −2x − 6"], "m = −2 and b = 6.")
H('5.B', 4, "A taxi charges $3 plus $2 per mile. What is the cost of a 7-mile ride?", "$17", ["$14", "$23", "$21"], "y = 2(7) + 3 = 17.")
H('5.B', 4, "A candle is 12 inches tall and burns 1.5 inches per hour. Which equation gives its height h after t hours?", "h = 12 − 1.5t", ["h = 1.5t − 12", "h = 12 + 1.5t", "h = 13.5t"], "Start at 12 and subtract 1.5 each hour.")
H('5.B', 3, "In y = 5x + 8, what is the slope?", "5", ["8", "13", "40"], "The coefficient of x is the slope.")
H('5.B', 3, "In y = −3x + 9, what is the y-intercept?", "9", ["−3", "3", "6"], "The constant term is the y-intercept.")

# ---- 5.C linear vs non-linear association
H('5.C', 3, "A scatterplot's points fall close to a straight line rising from left to right. This suggests...", "a positive linear relationship", ["no relationship", "a negative linear relationship", "a non-linear relationship"], "The points follow a rising line.")
H('5.C', 3, "A scatterplot's points are scattered with no pattern. This suggests...", "no association", ["a linear association", "a strong association", "a perfect line"], "Without a pattern, the variables are not related.")
H('5.C', 4, "A scatterplot's points form a curve like a U. This suggests...", "a non-linear association", ["a linear association", "no association", "a negative linear association"], "The points follow a curve, not a line.")
H('5.C', 3, "Points that fall along a line sloping downward suggest a...", "negative linear association", ["positive linear association", "non-linear association", "constant"], "As x increases, y decreases.")
H('5.C', 4, "As the hours of practice increase, test errors decrease in a straight pattern. This is a...", "negative linear association", ["positive linear association", "non-linear association", "random pattern"], "More practice goes with fewer errors in a linear way.")

# ---- 5.D trend line predictions
H('5.D', 4, "A trend line for a plant's height is y = 2x + 5 (cm, x weeks). What is the predicted height at 10 weeks?", "25 cm", ["20 cm", "12 cm", "30 cm"], "2(10) + 5 = 25.")
H('5.D', 4, "A trend line for sales is y = 3x + 20. Predict y when x = 8.", "44", ["28", "24", "60"], "3(8) + 20 = 44.")
H('5.D', 3, "A trend line is used to...", "predict values that are not in the data", ["prove the data is exact", "remove outliers", "avoid graphing"], "It approximates the pattern for predictions.")
H('5.D', 4, "A trend line y = −4x + 90 models temperature. Predict y when x = 5.", "70", ["110", "20", "86"], "−4(5) + 90 = 70.")
H('5.D', 4, "A scatterplot shows a trend line passing through (2, 11) and (6, 23). Predict y at x = 10.", "35", ["29", "33", "46"], "The slope is 3, so from (6, 23) add 12.")

# ---- 5.E direct variation
H('5.E', 3, "If y varies directly with x and y = 12 when x = 3, what is the constant of variation?", "4", ["9", "36", "1/4"], "12 ÷ 3 = 4.")
H('5.E', 4, "If y varies directly with x and y = 20 when x = 4, find y when x = 7.", "35", ["27", "28", "11"], "k = 5, so y = 5 × 7 = 35.")
H('5.E', 4, "The cost of fabric varies directly with its length. 6 yards cost $27. How much do 10 yards cost?", "$45", ["$37", "$33", "$60"], "k = 4.5, so 10 × 4.5 = 45.")
H('5.E', 3, "Which equation shows direct variation?", "y = 9x", ["y = 9x + 2", "y = 9 − x", "y = x²"], "Direct variation has the form y = kx.")
H('5.E', 4, "y varies directly with x. When x = 2, y = 5. What is y when x = 12?", "30", ["25", "17", "60"], "k = 2.5, and 2.5 × 12 = 30.")

# ---- 5.F proportional vs non-proportional
H('5.F', 3, "Which equation represents a non-proportional relationship?", "y = 2x + 3", ["y = 2x", "y = x/2", "y = 5x"], "A nonzero y-intercept means it is not proportional.")
H('5.F', 3, "Which table is non-proportional?", "x: 1, 2, 3 and y: 3, 5, 7", ["x: 1, 2, 3 and y: 4, 8, 12", "x: 1, 2, 3 and y: 2, 4, 6", "x: 1, 2, 3 and y: 10, 20, 30"], "y/x is 3, 2.5, 2.33, so the ratio changes.")
H('5.F', 4, "A line passes through (0, 0) and (3, 9). This relationship is...", "proportional", ["non-proportional", "not linear", "undefined"], "It passes through the origin and has constant ratio 3.")
H('5.F', 4, "A line passes through (0, 4) and (2, 10). This relationship is...", "non-proportional", ["proportional", "not a function", "undefined"], "The line does not pass through the origin.")
H('5.F', 4, "A video plan costs $5 per month with no fee. A different plan costs $2 to join plus $4 per month. Which is proportional?", "the first plan, y = 5x", ["the second plan, y = 4x + 2", "both plans", "neither plan"], "Only y = 5x has no starting amount.")

# ---- 5.G identify functions
H('5.G', 3, "Which set of ordered pairs is a function?", "{(1, 2), (2, 4), (3, 6)}", ["{(1, 2), (1, 4), (3, 6)}", "{(2, 1), (2, 3), (4, 5)}", "{(0, 0), (0, 1), (2, 2)}"], "Each input has exactly one output.")
H('5.G', 3, "Which set of ordered pairs is NOT a function?", "{(3, 1), (3, 5), (4, 2)}", ["{(1, 1), (2, 1), (3, 1)}", "{(0, 2), (1, 3), (2, 4)}", "{(5, 9), (6, 8), (7, 7)}"], "The input 3 has two outputs.")
H('5.G', 4, "A table shows x = 2, 4, 2 and y = 5, 9, 7. Is this a function?", "No, because x = 2 has two outputs", ["Yes, because y values are different", "Yes, because x increases", "No, because y values differ"], "A function cannot give two outputs for the same input.")
H('5.G', 4, "A graph fails the vertical line test when...", "a vertical line touches it in more than one point", ["a horizontal line touches it once", "it is a straight line through the origin", "it has a y-intercept"], "That means an input has more than one output.")
H('5.G', 3, "A mapping sends 1→3, 2→3 and 3→3. Is it a function?", "Yes, each input has one output", ["No, outputs repeat", "No, inputs repeat", "It cannot be told"], "Repeated outputs are allowed; repeated inputs with different outputs are not.")
H('5.G', 4, "Which relation is a function?", "a student ID number to that student's name", ["a first name to all students with that name", "a birthday to all students born that day", "a grade level to all students in it"], "Each ID matches one name.")

# ---- 5.H proportional / non-proportional in real world
H('5.H', 3, "Which situation is proportional?", "buying apples at $2 per pound", ["a $5 delivery fee plus $2 per pound", "a plant that is 10 cm tall and grows 2 cm per week", "a phone plan with a $20 base fee"], "No starting amount means the cost is proportional to the weight.")
H('5.H', 3, "Which situation is non-proportional?", "a gym with a $30 sign-up fee and $15 per month", ["earning $12 per hour with no bonus", "a car at a steady 60 miles per hour from the start", "buying tickets at $8 each"], "The sign-up fee gives a nonzero starting value.")
H('5.H', 4, "Which is a non-proportional function?", "the cost of a taxi ride with a base fare", ["the cost of identical items sold at one price", "distance at a constant speed from rest", "the pay for hours at a flat hourly rate"], "A base fare gives a nonzero y-intercept.")
H('5.H', 4, "The area of a square, A = s², compared with its side length is...", "non-proportional (and non-linear)", ["proportional", "linear and proportional", "a direct variation"], "Doubling s quadruples A.")
H('5.H', 3, "The perimeter of a square, P = 4s, is...", "proportional to its side length", ["not proportional", "quadratic", "unrelated to s"], "P = 4s has the form y = kx.")

# ---- 5.I write y = mx + b
H('5.I', 4, "A line passes through (0, 3) and (2, 7). Which is its equation?", "y = 2x + 3", ["y = 4x + 3", "y = 2x + 7", "y = 3x + 2"], "Slope 4/2 = 2 and y-intercept 3.")
H('5.I', 4, "A table shows x = 0, 1, 2, 3 and y = 10, 8, 6, 4. Which equation fits?", "y = −2x + 10", ["y = 2x + 10", "y = −2x − 10", "y = 10x − 2"], "y drops by 2 each step starting at 10.")
H('5.I', 4, "A phone plan costs $15 per month plus $0.10 per text. Which equation gives the cost y for x texts?", "y = 0.10x + 15", ["y = 15x + 0.10", "y = 15.10x", "y = 0.10x − 15"], "Per-text rate times texts plus the base.")
H('5.I', 4, "A line with slope 3 passes through (0, −5). Which is its equation?", "y = 3x − 5", ["y = −5x + 3", "y = 3x + 5", "y = −3x − 5"], "m = 3 and b = −5.")
H('5.I', 4, "A pool has 200 gallons and drains 8 gallons per minute. Which equation gives gallons g after m minutes?", "g = 200 − 8m", ["g = 8m − 200", "g = 200 + 8m", "g = 192m"], "Start at 200 and subtract 8 each minute.")
H('5.I', 3, "Which equation has slope 4 and y-intercept 7?", "y = 4x + 7", ["y = 7x + 4", "y = 4x − 7", "y = 11x"], "y = mx + b.")

# ---- 6.A cylinder volume
H('6.A', 3, "The volume formula for a cylinder is V = Bh. What does B represent?", "the area of the base", ["the height", "the radius", "the circumference"], "B is the base area, which for a cylinder is πr².")
H('6.A', 3, "A cylinder has a base area of 50 square centimeters and height 6 centimeters. What is its volume?", "300 cubic centimeters", ["56 cubic centimeters", "150 cubic centimeters", "600 cubic centimeters"], "V = Bh = 50 × 6.")
H('6.A', 4, "Which formula gives the volume of a cylinder with radius r and height h?", "V = πr²h", ["V = 2πrh", "V = πrh", "V = 1/3πr²h"], "Base area πr² times height.")
H('6.A', 4, "A cylinder has radius 3 and height 5. What is its volume in terms of π?", "45π", ["15π", "30π", "75π"], "π(3²)(5) = 45π.")
H('6.A', 4, "Two cylinders have the same base. One is twice as tall. Its volume is...", "twice as large", ["half as large", "four times as large", "the same"], "V = Bh grows with h.")

# ---- 6.B cylinder and cone
H('6.B', 3, "A cone and a cylinder have congruent bases and equal heights. The cone's volume is what fraction of the cylinder's?", "1/3", ["1/2", "2/3", "1/4"], "Three cones fill one cylinder.")
H('6.B', 3, "Which is the volume formula for a cone?", "V = 1/3 πr²h", ["V = πr²h", "V = 4/3 πr³", "V = 2πrh"], "One-third of the cylinder formula.")
H('6.B', 4, "A cylinder holds 90 cubic inches. A cone has the same base and height. How many cubic inches does the cone hold?", "30", ["60", "45", "270"], "90 ÷ 3 = 30.")
H('6.B', 4, "How many full cones of water fill an empty cylinder with the same base and height?", "3", ["2", "4", "6"], "V(cone) = 1/3 V(cylinder).")
H('6.B', 4, "A cone has volume 24π. A cylinder has the same base and height. What is the cylinder's volume?", "72π", ["8π", "48π", "24π"], "24π × 3 = 72π.")

# ---- 6.C explain Pythagorean theorem with models
H('6.C', 3, "In a right triangle with legs a and b and hypotenuse c, which equation is the Pythagorean theorem?", "a² + b² = c²", ["a + b = c", "a² − b² = c²", "a² + b² = c"], "The squares on the legs add to the square on the hypotenuse.")
H('6.C', 3, "The hypotenuse of a right triangle is the...", "longest side, opposite the right angle", ["shortest side", "side next to the right angle", "any side"], "It is opposite the 90° angle.")
H('6.C', 4, "A square built on one leg has area 9 and a square on the other leg has area 16. What is the area of the square on the hypotenuse?", "25", ["7", "12", "5"], "9 + 16 = 25.")
H('6.C', 4, "The squares on the legs of a right triangle have areas 36 and 64. What is the hypotenuse length?", "10", ["14", "100", "28"], "36 + 64 = 100, and √100 = 10.")
H('6.C', 4, "A square on the hypotenuse has area 169 and a square on one leg has area 25. What is the area of the square on the other leg?", "144", ["194", "12", "119"], "169 − 25 = 144.")

# ---- 7.A volume of cylinders, cones, spheres
def cyl_vol():
    r = R.randint(2, 9); h = R.randint(2, 12); v = r * r * h
    return mk('7.A', 4, f"A cylinder has radius {r} cm and height {h} cm. What is its volume in terms of π?", f"{v}π cubic cm", [f"{r * h}π cubic cm", f"{2 * r * h}π cubic cm", f"{v * 3}π cubic cm"], f"V = πr²h = π({r}²)({h}) = {v}π.")
rep(5, cyl_vol)
def cone_vol():
    r = R.randint(2, 9); h = 3 * R.randint(1, 5); v = r * r * h // 3
    return mk('7.A', 4, f"A cone has radius {r} cm and height {h} cm. What is its volume in terms of π?", f"{v}π cubic cm", [f"{r * r * h}π cubic cm", f"{r * h // 3}π cubic cm", f"{v * 2}π cubic cm"], f"V = 1/3 πr²h = 1/3 π({r}²)({h}) = {v}π.")
rep(5, cone_vol)
def sph_vol():
    r = 3 * R.randint(1, 4); v = 4 * r ** 3 // 3
    return mk('7.A', 4, f"A sphere has radius {r} cm. What is its volume in terms of π?", f"{v}π cubic cm", [f"{r ** 3}π cubic cm", f"{4 * r * r}π cubic cm", f"{v * 3}π cubic cm"], f"V = 4/3 πr³ = 4/3 π({r}³) = {v}π.")
rep(5, sph_vol)
H('7.A', 3, "Which formula gives the volume of a sphere with radius r?", "V = 4/3 πr³", ["V = 4πr²", "V = πr²h", "V = 1/3 πr²h"], "Sphere volume is four-thirds pi r cubed.")
H('7.A', 4, "A can is a cylinder with diameter 6 in. and height 10 in. What is its volume in terms of π?", "90π cubic inches", ["360π cubic inches", "60π cubic inches", "30π cubic inches"], "r = 3, so π(9)(10) = 90π.")
H('7.A', 4, "A funnel is a cone with radius 6 cm and height 9 cm. What is its volume in terms of π?", "108π cubic cm", ["324π cubic cm", "54π cubic cm", "36π cubic cm"], "1/3 π(36)(9) = 108π.")
H('7.A', 4, "The radius of a sphere is doubled. The volume is multiplied by...", "8", ["2", "4", "6"], "V depends on r³, and 2³ = 8.")

# ---- 7.B lateral and total surface area
def cyl_lat():
    r = R.randint(2, 8); h = R.randint(3, 10); lat = 2 * r * h
    return mk('7.B', 4, f"A cylinder has radius {r} in. and height {h} in. What is its lateral surface area in terms of π?", f"{lat}π square in.", [f"{r * h}π square in.", f"{lat + 2 * r * r}π square in.", f"{r * r * h}π square in."], f"L = 2πrh = 2π({r})({h}) = {lat}π.")
rep(4, cyl_lat)
def cyl_tot():
    r = R.randint(2, 8); h = R.randint(3, 10); tot = 2 * r * h + 2 * r * r
    return mk('7.B', 4, f"A cylinder has radius {r} cm and height {h} cm. What is its total surface area in terms of π?", f"{tot}π square cm", [f"{2 * r * h}π square cm", f"{tot + r * r}π square cm", f"{r * r * h}π square cm"], f"2πrh + 2πr² = {2 * r * h}π + {2 * r * r}π = {tot}π.")
rep(4, cyl_tot)
H('7.B', 3, "The lateral surface area of a cylinder is the area of...", "the curved side without the bases", ["the two bases only", "all faces including the bases", "the cross-section"], "Lateral means the side surface.")
H('7.B', 4, "Which formula gives the total surface area of a cylinder?", "2πr² + 2πrh", ["πr²h", "2πrh", "πr² + πh"], "Two circular bases plus the lateral area.")
H('7.B', 4, "A rectangular prism is 3 cm by 4 cm by 5 cm. What is its total surface area?", "94 square cm", ["60 square cm", "47 square cm", "120 square cm"], "2(12 + 15 + 20) = 94.")
H('7.B', 4, "A square pyramid has base side 10 and four triangular faces each with base 10 and height 13. What is the lateral surface area?", "260", ["130", "360", "520"], "4 × 1/2 × 10 × 13 = 260.")
H('7.B', 4, "A cone has radius 3 and slant height 5. What is its lateral surface area in terms of π?", "15π", ["30π", "45π", "9π"], "L = πrl = π(3)(5).")

# ---- 7.C Pythagorean theorem problems
def pyth_hyp():
    a, b, c = R.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10), (9, 12, 15), (12, 16, 20), (9, 40, 41), (20, 21, 29)])
    return mk('7.C', 3, f"A right triangle has legs {a} and {b}. What is the length of the hypotenuse?", str(c), [str(a + b), str(c + 1), str(c * c)], f"{a}² + {b}² = {a * a + b * b}, and √{a * a + b * b} = {c}.")
rep(6, pyth_hyp)
def pyth_leg():
    a, b, c = R.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10), (9, 12, 15), (12, 16, 20), (15, 20, 25)])
    return mk('7.C', 4, f"A right triangle has a hypotenuse of {c} and one leg of {a}. What is the other leg?", str(b), [str(c - a), str(c + a), str(b + 1)], f"{c}² − {a}² = {c * c - a * a}, and √{c * c - a * a} = {b}.")
rep(6, pyth_leg)
H('7.C', 3, "A 10-ft ladder leans against a wall with its base 6 ft from the wall. How high up the wall does it reach?", "8 ft", ["4 ft", "12 ft", "16 ft"], "√(100 − 36) = 8.")
H('7.C', 4, "A TV screen is 16 in. wide and 12 in. tall. What is its diagonal?", "20 in.", ["28 in.", "14 in.", "400 in."], "√(256 + 144) = 20.")
H('7.C', 4, "A triangle has sides 7, 24 and 25. Is it a right triangle?", "Yes, because 7² + 24² = 25²", ["No, because 7 + 24 ≠ 25", "No, because 25 is too long", "It cannot be told"], "49 + 576 = 625 = 25².")
H('7.C', 4, "A triangle has sides 5, 6 and 9. Is it a right triangle?", "No, because 5² + 6² ≠ 9²", ["Yes, because 5 + 6 > 9", "Yes, because 9 is longest", "It cannot be told"], "25 + 36 = 61, but 9² = 81.")
H('7.C', 3, "What does the converse of the Pythagorean theorem say?", "If a² + b² = c², the triangle is a right triangle", ["Every triangle has a right angle", "The hypotenuse is the shortest side", "All right triangles are isosceles"], "It lets you test a triangle's sides.")
H('7.C', 4, "A baseball diamond is a square 90 ft on a side. What is the distance from home plate to second base?", "about 127 ft", ["about 180 ft", "about 90 ft", "about 64 ft"], "√(90² + 90²) = 90√2 ≈ 127.")

# ---- 7.D distance on the coordinate plane
def dist_pts():
    a, b, c = R.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)])
    x1 = R.randint(-4, 3); y1 = R.randint(-4, 3); sx = R.choice([-1, 1]); sy = R.choice([-1, 1])
    x2 = x1 + sx * a; y2 = y1 + sy * b
    return mk('7.D', 4, f"What is the distance between ({sg(x1)}, {sg(y1)}) and ({sg(x2)}, {sg(y2)})?", str(c), [str(a + b), str(c + 1), str(abs(a - b))], f"Horizontal change {a}, vertical change {b}: √({a}² + {b}²) = {c}.")
rep(6, dist_pts)
H('7.D', 3, "What is the distance between (0, 0) and (3, 4)?", "5", ["7", "12", "1"], "√(9 + 16) = 5.")
H('7.D', 4, "What is the distance between (−2, 1) and (4, 9)?", "10", ["14", "6", "8"], "Changes are 6 and 8, so the distance is 10.")
H('7.D', 4, "Points A(1, 2) and B(1, 9) are on a vertical line. What is AB?", "7", ["8", "10", "63"], "Subtract the y-values: 9 − 2.")
H('7.D', 3, "To find the distance between two points, you draw a right triangle whose legs are the...", "horizontal and vertical changes", ["slope and intercept", "x-coordinates only", "y-coordinates only"], "The hypotenuse is the distance.")

# ---- 8.A write equations with variables on both sides
H('8.A', 4, "Max has $20 and saves $5 per week. Eli has $50 and spends $1 per week. Which equation finds the week w when they have equal amounts of money?", "20 + 5w = 50 − w", ["20 + 5w = 50 + w", "20 − 5w = 50 + w", "5w = w"], "Max has 20 + 5w and Eli has 50 − w.")
H('8.A', 3, "Plan A charges $10 plus $2 per visit. Plan B charges $4 plus $3 per visit. Which equation finds the visits v where the costs are equal?", "10 + 2v = 4 + 3v", ["10 + 3v = 4 + 2v", "10 + 2v = 3v", "2v = 3v"], "Set the two cost expressions equal.")
H('8.A', 4, "Two candles are 12 cm and 20 cm tall. The first burns 1 cm per hour and the second 3 cm per hour. Which inequality shows when the second candle is shorter than the first?", "20 − 3h < 12 − h", ["20 + 3h < 12 + h", "20 − 3h > 12 − h", "3h < h"], "The second candle's height is less than the first's.")
H('8.A', 4, "Which equation says 'five more than 3 times a number equals 2 times the number plus 11'?", "3n + 5 = 2n + 11", ["3(n + 5) = 2n + 11", "5n + 3 = 2n + 11", "3n + 5 = 2(n + 11)"], "3n + 5 on the left and 2n + 11 on the right.")
H('8.A', 3, "A pool A has 100 gallons and fills at 5 per minute. Pool B has 40 gallons and fills at 8 per minute. Which equation finds the minute m they are equal?", "100 + 5m = 40 + 8m", ["100 + 8m = 40 + 5m", "100 − 5m = 40 − 8m", "5m = 8m"], "Starting amounts plus each rate times m.")

# ---- 8.B write real-world problems from equations
H('8.B', 4, "Which situation matches 4x + 6 = 2x + 18?", "Two plans cost $6 plus $4 per visit and $18 plus $2 per visit; find the visits when costs are equal", ["Four tickets cost $6 and 2 tickets cost $18", "A plan costs $6 total and another $18 total", "A number is 4 more than 6 times 2"], "Each side is a fixed fee plus a per-visit charge.")
H('8.B', 4, "Which situation matches 15 + 2n = 5n?", "A tank with 15 gallons gains 2 per minute; an empty tank gains 5 per minute; find when they are equal", ["A tank with 5 gallons loses 15 per minute", "A number plus 15 is 2", "Two tanks have 15 and 5 gallons"], "One side starts at 15, the other at 0.")
H('8.B', 3, "In 7x − 3 = 4x + 9, what does the left side most likely represent?", "7 items at x dollars each minus a $3 discount", ["a total of 3 items", "9 items", "a $7 coupon"], "7x is the item cost and −3 is a reduction.")
H('8.B', 4, "Which problem matches 3w + 2 = 2w + 5?", "Two jobs: $2 plus $3 per hour and $5 plus $2 per hour; find the hours when pay is equal", ["Three workers earn $2 each", "A worker earns $5 total", "Two workers share $3"], "Both sides are fee plus rate times hours.")

# ---- 8.C solve equations with variables on both sides
def both_sides():
    x = R.randint(-6, 9); c = R.randint(1, 4); a = c + R.randint(1, 5); b = R.randint(-9, 9)
    d = (a - c) * x + b
    return mk('8.C', 4, f"Solve: {a}x {'+' if b >= 0 else '−'} {abs(b)} = {c}x {'+' if d >= 0 else '−'} {abs(d)}", f"x = {sg(x)}", [f"x = {sg(-x)}", f"x = {sg(x + 1)}", f"x = {sg(x - 1)}"], f"Subtract {c}x from both sides: {a - c}x = {sg(d - b)}, so x = {sg(x)}.") if b != 0 and d != 0 and x != 0 else False
rep(10, both_sides)
H('8.C', 3, "Solve: 5x = 3x + 14", "x = 7", ["x = 14", "x = 3", "x = 2"], "Subtract 3x: 2x = 14.")
H('8.C', 4, "Solve: 4(x − 2) = 2x + 6", "x = 7", ["x = 1", "x = 14", "x = 3.5"], "4x − 8 = 2x + 6, so 2x = 14.")
H('8.C', 4, "Solve: x/2 + 3 = x − 1", "x = 8", ["x = 4", "x = −8", "x = 2"], "Subtract x/2: 3 = x/2 − 1, so x/2 = 4.")
H('8.C', 4, "Solve: 2(3x + 1) = 4x + 10", "x = 4", ["x = 2", "x = 8", "x = 12"], "6x + 2 = 4x + 10, so 2x = 8.")
H('8.C', 4, "How many solutions does 3x + 4 = 3x + 9 have?", "none", ["one", "two", "infinitely many"], "Subtracting 3x gives 4 = 9, which is false.")
H('8.C', 4, "How many solutions does 2(x + 3) = 2x + 6 have?", "infinitely many", ["none", "exactly one", "exactly two"], "Both sides simplify to 2x + 6.")
H('8.C', 4, "Solve: 7 − 2x = x + 1", "x = 2", ["x = −2", "x = 3", "x = 6"], "6 = 3x, so x = 2.")

# ---- 8.D angle facts
def tri_ext():
    a = R.randint(30, 70); b = R.randint(30, 70); e = a + b
    return mk('8.D', 3, f"Two interior angles of a triangle are {a}° and {b}°. What is the exterior angle at the third vertex?", f"{e}°", [f"{180 - e}°", f"{180 - a}°", f"{360 - e}°"], f"The exterior angle equals the sum of the other two interior angles: {a} + {b} = {e}.") if e != 90 and 180 - e != e else False
rep(5, tri_ext)
H('8.D', 3, "The interior angles of a triangle add up to...", "180°", ["90°", "270°", "360°"], "This holds for every triangle.")
H('8.D', 3, "Parallel lines are cut by a transversal. Corresponding angles are...", "congruent", ["supplementary only", "complementary", "always 90°"], "Corresponding angles match in position and measure.")
H('8.D', 4, "Parallel lines are cut by a transversal. One angle measures 70°. Its alternate interior angle measures...", "70°", ["110°", "20°", "290°"], "Alternate interior angles are congruent.")
H('8.D', 4, "Parallel lines are cut by a transversal. Two co-interior (same-side interior) angles are...", "supplementary", ["congruent", "complementary", "equal to 90° each"], "They add to 180°.")
H('8.D', 4, "Two triangles have angles 40° and 60° in one and 40° and 60° in the other. The third angles are...", "both 80°, so the triangles are similar", ["different", "both 100°", "impossible to find"], "180 − 100 = 80; AA similarity.")
H('8.D', 4, "A triangle has angles x, 2x and 3x. What is x?", "30°", ["60°", "20°", "45°"], "6x = 180.")
H('8.D', 4, "An exterior angle of a triangle is 125° and one remote interior angle is 50°. What is the other remote interior angle?", "75°", ["55°", "125°", "105°"], "125 − 50 = 75.")

# ---- 10.A properties of transformations
H('10.A', 3, "Which transformation changes only the position of a figure and not its size, shape or orientation?", "a translation", ["a dilation", "a rotation", "a reflection"], "A translation slides a figure.")
H('10.A', 3, "Which transformation flips a figure over a line?", "a reflection", ["a rotation", "a translation", "a dilation"], "A reflection creates a mirror image.")
H('10.A', 3, "Which transformation turns a figure around a point?", "a rotation", ["a reflection", "a translation", "a dilation"], "A rotation turns the figure.")
H('10.A', 4, "Which transformations preserve both size and shape?", "translations, reflections and rotations", ["dilations only", "dilations and reflections", "dilations and rotations"], "These are rigid motions.")
H('10.A', 4, "A reflection changes a figure's...", "orientation", ["side lengths", "angle measures", "area"], "A mirror image faces the opposite way.")
H('10.A', 4, "A translation does NOT change a figure's...", "orientation", ["location", "coordinates", "position"], "A slide keeps the figure facing the same way.")

# ---- 10.B congruence-preserving or not
H('10.B', 3, "Which transformation does NOT preserve congruence?", "a dilation with a scale factor of 2", ["a reflection", "a translation", "a rotation of 90°"], "The image is a different size.")
H('10.B', 3, "A figure and its image after a translation are...", "congruent", ["similar but not congruent", "unrelated", "different in area"], "Translations keep size and shape.")
H('10.B', 4, "A figure and its image after a dilation with scale factor 1 are...", "congruent", ["not congruent", "smaller", "larger"], "A factor of 1 changes nothing.")
H('10.B', 4, "A figure and its image after a dilation with scale factor 1/2 are...", "similar but not congruent", ["congruent", "unrelated", "equal in perimeter"], "The shape stays the same but the size changes.")
H('10.B', 4, "Which sequence produces a congruent image?", "a reflection followed by a translation", ["a dilation by 3 followed by a reflection", "a dilation by 1/2 followed by a rotation", "a dilation by 4 followed by a translation"], "Only rigid motions preserve congruence.")

# ---- 10.C translations, reflections, rotations on coordinate plane
def trans():
    x = R.randint(-5, 5); y = R.randint(-5, 5); dx = R.randint(-4, 4); dy = R.randint(-4, 4)
    if dx == 0 or dy == 0: return False
    return mk('10.C', 3, f"Translate ({sg(x)}, {sg(y)}) by ({sg(dx)}, {sg(dy)}). What is the image?", f"({sg(x + dx)}, {sg(y + dy)})", [f"({sg(x - dx)}, {sg(y - dy)})", f"({sg(x + dx)}, {sg(y - dy)})", f"({sg(x * dx)}, {sg(y * dy)})"], f"Add the changes to each coordinate: ({sg(x + dx)}, {sg(y + dy)}).")
rep(5, trans)
def refl_x():
    x = R.randint(-6, 6); y = R.randint(1, 6) * R.choice([-1, 1])
    if x == 0: return False
    return mk('10.C', 3, f"Reflect ({sg(x)}, {sg(y)}) over the x-axis. What is the image?", f"({sg(x)}, {sg(-y)})", [f"({sg(-x)}, {sg(y)})", f"({sg(-x)}, {sg(-y)})", f"({sg(y)}, {sg(x)})"], "Reflection over the x-axis changes the sign of y.")
rep(4, refl_x)
def refl_y():
    x = R.randint(1, 6) * R.choice([-1, 1]); y = R.randint(-6, 6)
    if y == 0: return False
    return mk('10.C', 3, f"Reflect ({sg(x)}, {sg(y)}) over the y-axis. What is the image?", f"({sg(-x)}, {sg(y)})", [f"({sg(x)}, {sg(-y)})", f"({sg(-x)}, {sg(-y)})", f"({sg(y)}, {sg(x)})"], "Reflection over the y-axis changes the sign of x.")
rep(4, refl_y)
def rot180():
    x = R.randint(-6, 6); y = R.randint(-6, 6)
    if x == 0 or y == 0: return False
    return mk('10.C', 4, f"Rotate ({sg(x)}, {sg(y)}) 180° about the origin. What is the image?", f"({sg(-x)}, {sg(-y)})", [f"({sg(-x)}, {sg(y)})", f"({sg(x)}, {sg(-y)})", f"({sg(y)}, {sg(x)})"], "A 180° rotation changes both signs.")
rep(4, rot180)
def rot90():
    x = R.randint(1, 6) * R.choice([-1, 1]); y = R.randint(1, 6) * R.choice([-1, 1])
    return mk('10.C', 4, f"Rotate ({sg(x)}, {sg(y)}) 90° counterclockwise about the origin. What is the image?", f"({sg(-y)}, {sg(x)})", [f"({sg(y)}, {sg(-x)})", f"({sg(-x)}, {sg(-y)})", f"({sg(y)}, {sg(x)})"], "A 90° counterclockwise rotation maps (x, y) to (−y, x).")
rep(4, rot90)
H('10.C', 4, "Rotate (4, 1) 90° clockwise about the origin. What is the image?", "(1, −4)", ["(−1, 4)", "(−4, −1)", "(1, 4)"], "A 90° clockwise rotation maps (x, y) to (y, −x).")
H('10.C', 4, "Rotating a point 360° about the origin gives...", "the original point", ["its reflection", "a point twice as far away", "the origin"], "A full turn returns every point to its start.")
H('10.C', 4, "Rotate (3, −2) 270° counterclockwise about the origin. What is the image?", "(−2, −3)", ["(2, 3)", "(−3, 2)", "(3, 2)"], "270° counterclockwise equals 90° clockwise, (x, y) → (y, −x).")

# ---- 10.D linear and area effects of dilation
H('10.D', 3, "A square with side 4 is dilated by a scale factor of 3. What is the new side?", "12", ["7", "1.33", "16"], "4 × 3 = 12.")
H('10.D', 4, "A square with side 4 is dilated by a scale factor of 3. What is the new area?", "144", ["48", "16", "36"], "The side is 12, so the area is 144.")
H('10.D', 4, "A scale factor of 5 is applied to a shape. The perimeter is multiplied by...", "5", ["25", "10", "1/5"], "Lengths scale by k.")
H('10.D', 4, "A scale factor of 5 is applied to a shape. The area is multiplied by...", "25", ["5", "10", "125"], "Areas scale by k².")
H('10.D', 4, "A rectangle has area 12. It is dilated by a scale factor of 2. What is the new area?", "48", ["24", "14", "36"], "12 × 2² = 48.")
H('10.D', 4, "A triangle's area is 50. After a dilation, the area is 8. What is the scale factor?", "2/5", ["4/25", "5/2", "1/5"], "8/50 = 4/25, and √(4/25) = 2/5.")

# ---- 11.A scatterplots
H('11.A', 3, "As the temperature rises, ice cream sales also rise. A scatterplot would show...", "a positive association", ["a negative association", "no association", "a non-linear association"], "Both variables increase together.")
H('11.A', 3, "As the number of hours of TV increases, test scores tend to decrease. The scatterplot would show...", "a negative association", ["a positive association", "no association", "an exact line"], "One variable goes up while the other goes down.")
H('11.A', 4, "A scatterplot of shoe size and phone number would most likely show...", "no association", ["a positive association", "a negative association", "a linear association"], "These variables are unrelated.")
H('11.A', 4, "Points on a scatterplot form a clear curve that rises and then falls. This shows a...", "non-linear association", ["linear association", "no association", "constant rate"], "The pattern is curved, not straight.")
H('11.A', 4, "Which question could a scatterplot help answer?", "Is there a relationship between hours studied and test score?", ["How many students are in each grade?", "What is the median score?", "Which color is most popular?"], "Scatterplots show relationships between two numerical variables.")
H('11.A', 3, "A point far from the pattern of the other points is called a(n)...", "outlier", ["median", "mode", "trend"], "It does not fit the overall pattern.")

# ---- 11.B mean absolute deviation
def mad_q():
    n = R.choice([4, 5]); base = R.randint(5, 15)
    while True:
        d = [R.randint(-4, 4) for _ in range(n)]
        if sum(d) == 0 and len(set(d)) > 2: break
    data = [base + x for x in d]
    mean = base
    mad = F(sum(abs(x) for x in d), n)
    return mk('11.B', 4, f"The data are {', '.join(map(str, data))}. The mean is {mean}. What is the mean absolute deviation?", ims(mad) if mad.denominator == 1 else dec(mad), [ims(mad + 1) if mad.denominator == 1 else dec(mad + 1), str(mean), "0"], f"Find each distance from {mean}, add them, and divide by {n}: {sum(abs(x) for x in d)}/{n}.") if mad.denominator in (1, 2, 4, 5) else False
rep(6, mad_q)
H('11.B', 3, "What does mean absolute deviation (MAD) measure?", "the average distance data values are from the mean", ["the middle value", "the most common value", "the range"], "MAD summarizes spread.")
H('11.B', 4, "Data set A has MAD 2 and data set B has MAD 6. Which statement is true?", "Set B is more spread out", ["Set A is more spread out", "They have the same spread", "Set A has the larger mean"], "A larger MAD means values are farther from the mean.")
H('11.B', 4, "The data 4, 6, 8 have a mean of 6. What is the MAD?", "4/3", ["2", "0", "6"], "Distances are 2, 0, 2; sum 4, divided by 3.")
H('11.B', 3, "If every value in a data set equals the mean, the MAD is...", "0", ["1", "the mean", "undefined"], "There is no spread.")

# ---- 11.C random samples
H('11.C', 3, "Why is a random sample useful?", "it tends to represent the population fairly", ["it always matches the population exactly", "it only includes friends", "it is the easiest to bias"], "Randomness reduces bias.")
H('11.C', 4, "A bag has 50 red and 50 blue chips. A random sample of 10 has 6 red. If you draw 100 samples of 10, what would you expect the average number of red chips to be?", "about 5", ["exactly 6", "about 10", "about 0"], "Samples vary but center near the population value.")
H('11.C', 4, "Which sample size is likely to give results closest to the population?", "a large random sample", ["a small random sample", "a sample of one", "a sample of volunteers"], "Larger random samples vary less.")
H('11.C', 3, "A simulation draws many random samples of the same size to see...", "how much sample results vary", ["the exact population size", "which person to survey", "how to remove data"], "It shows the sample-to-sample variation.")
H('11.C', 4, "Why might a survey of only students in the gym about favorite sports be biased?", "it leaves out students who are not in the gym", ["it is too random", "it uses a large sample", "it is anonymous"], "The sample is not representative.")

# ---- 12.A cost of credit
H('12.A', 3, "Which loan costs less in total interest, all else equal?", "a lower interest rate", ["a higher interest rate", "a longer loan with higher interest", "a loan with extra fees"], "Lower rates mean less interest.")
H('12.A', 4, "A $1,000 loan at 10% simple interest for 1 year costs $100. The same loan for 3 years costs...", "$300 in interest", ["$100 in interest", "$30 in interest", "$1,300 in interest"], "I = Prt = 1000 × 0.10 × 3.")
H('12.A', 4, "A $2,000 loan has 5% interest for 2 years or 8% for 2 years. How much more interest does the 8% loan cost (simple interest)?", "$120", ["$60", "$30", "$300"], "2000 × 0.03 × 2 = 120.")
H('12.A', 3, "A longer loan term usually means...", "lower payments but more total interest", ["higher payments and less interest", "no interest", "a lower interest rate always"], "Spreading payments out adds interest.")
H('12.A', 4, "Which choice reduces the total cost of a loan?", "paying it off faster", ["making only minimum payments", "choosing the longest term", "borrowing more"], "Less time means less interest.")

# ---- 12.B total cost of repaying a loan
H('12.B', 4, "A $500 loan with 6% simple annual interest is repaid after 2 years. What is the total repaid?", "$560", ["$530", "$600", "$506"], "Interest = 500 × 0.06 × 2 = 60.")
H('12.B', 4, "A credit card balance of $400 charges 2% interest per month if unpaid. How much interest is added in the first month?", "$8", ["$20", "$2", "$80"], "0.02 × 400 = 8.")
H('12.B', 4, "A loan of $1,200 has payments of $110 per month for 12 months. What is the total repaid?", "$1,320", ["$1,200", "$1,100", "$132"], "110 × 12 = 1,320.")
H('12.B', 4, "Using the loan above, how much interest was paid?", "$120", ["$132", "$110", "$12"], "1,320 − 1,200 = 120.")
H('12.B', 3, "Interest on a loan is calculated on the...", "amount borrowed (principal)", ["the cost of the item only", "the income of the borrower", "the length of the contract only"], "Principal times rate times time.")

# ---- 12.C regular investing
H('12.C', 3, "Why does saving a small amount regularly help over time?", "the savings and the interest it earns keep growing", ["the savings never change", "interest stops after one year", "you pay less tax automatically"], "Regular deposits earn interest.")
H('12.C', 4, "Saving $50 every month for 12 months gives how much before interest?", "$600", ["$50", "$62", "$5,000"], "50 × 12 = 600.")
H('12.C', 4, "Starting to save for retirement earlier usually leads to...", "more money because interest has more time to grow", ["less money", "the same money", "no taxes"], "More time means more compounding.")
H('12.C', 3, "A savings plan for college should be started...", "as early as possible", ["only when the child is 17", "after graduating", "never"], "Time helps savings grow.")
H('12.C', 4, "Two people use the same account for 10 years. One deposits $20 each month and the other deposits twice as much. Who saves more?", "the one who deposits more", ["the one who deposits less", "they save the same", "it cannot be told"], "Larger deposits grow to a larger balance.")

# ---- 12.D simple vs compound
def simple_i():
    p = R.choice([500, 800, 1000, 2000, 2500]); r = R.choice([2, 3, 4, 5, 6]); t = R.randint(2, 6)
    i = p * r * t // 100
    return mk('12.D', 4, f"How much simple interest does ${p:,} earn at {r}% per year for {t} years?", f"${i:,}", [f"${i * 2:,}", f"${i + p:,}", f"${p * r // 100:,}"], f"I = Prt = {p} × {r / 100} × {t} = {i}.")
rep(5, simple_i)
H('12.D', 4, "$1,000 earns 10% compounded yearly. What is the balance after 2 years?", "$1,210", ["$1,200", "$1,100", "$1,020"], "1,000 × 1.1 × 1.1.")
H('12.D', 4, "$500 earns 4% compounded yearly. What is the balance after 2 years?", "$540.80", ["$540", "$520", "$580.80"], "500 × 1.04 × 1.04 = 540.80.")
H('12.D', 3, "Compound interest earns more than simple interest because...", "interest is also earned on previous interest", ["it has a lower rate", "it uses only the principal", "it ends sooner"], "Interest is added to the balance each period.")
H('12.D', 4, "$2,000 earns 5% simple interest for 3 years. How much interest?", "$300", ["$100", "$150", "$315"], "2000 × 0.05 × 3 = 300.")
H('12.D', 4, "After 3 years, which account has more: $1,000 at 5% simple interest, or $1,000 at 5% with interest added to the balance each year?", "the one where interest is added to the balance each year", ["the simple interest account", "they are equal", "it cannot be told"], "Compound gives 1,157.63; simple gives 1,150.")

# ---- 12.E payment methods
H('12.E', 3, "Which payment method takes money directly from a bank account when you buy?", "a debit card", ["a credit card", "a layaway plan", "a store coupon"], "Debit uses your own money immediately.")
H('12.E', 3, "A credit card purchase that is not paid in full by the due date usually...", "adds interest charges", ["is free", "reduces the balance automatically", "is cancelled"], "The unpaid balance accrues interest.")
H('12.E', 4, "An advantage of paying with cash is...", "you can spend only what you have", ["it earns reward points", "it builds a credit history", "it can be disputed"], "Cash limits spending to available money.")
H('12.E', 4, "A disadvantage of using a credit card is...", "you can overspend and pay high interest", ["you must carry cash", "the bank takes money at once", "it cannot be used online"], "Borrowed money costs interest.")
H('12.E', 4, "Which payment method helps build a credit history when used responsibly?", "a credit card", ["cash", "a gift card", "a debit card"], "Credit activity is reported to credit bureaus.")
H('12.E', 3, "A check is a payment method that...", "tells a bank to pay money from your account", ["borrows money", "adds interest", "is accepted everywhere instantly"], "It is an order to pay from your account.")

# ---- 12.F financially responsible decisions
H('12.F', 3, "Which is a financially responsible decision?", "saving part of each paycheck", ["spending all income", "ignoring bills", "borrowing to buy wants"], "Saving prepares for future needs.")
H('12.F', 4, "A person pays only the minimum on a credit card each month. The likely cost is...", "more interest over time", ["no interest", "a lower balance quickly", "a lower interest rate"], "A balance that is not paid off keeps accruing interest.")
H('12.F', 3, "Which shows good budgeting?", "paying needs first, then wants", ["buying wants first", "skipping savings", "borrowing for everyday items"], "Needs come before wants.")
H('12.F', 4, "The benefit of paying bills on time is...", "avoiding late fees and protecting credit", ["higher interest", "more debt", "lower income"], "Late payments cost money and hurt credit.")
H('12.F', 4, "Which decision is least financially responsible?", "taking a high-interest loan for a want you could save for", ["saving for an emergency fund", "comparing prices", "paying off a credit card each month"], "It adds interest cost for something unnecessary.")

# ---- 12.G college costs
H('12.G', 4, "A four-year college costs $20,000 per year. What is the total cost of tuition for four years?", "$80,000", ["$20,000", "$100,000", "$60,000"], "20,000 × 4.")
H('12.G', 4, "A family can contribute $10,000 toward a $40,000 total cost. How much remains?", "$30,000", ["$50,000", "$10,000", "$4,000"], "40,000 − 10,000.")
H('12.G', 4, "To have $12,000 in 10 years, how much must be saved per year (ignoring interest)?", "$1,200", ["$120", "$12,000", "$2,000"], "12,000 ÷ 10.")
H('12.G', 4, "To have $9,000 in 3 years, how much must be saved per month (ignoring interest)?", "$250", ["$300", "$750", "$3,000"], "9,000 ÷ 36 = 250.")
H('12.G', 3, "Which can reduce the cost of college?", "scholarships and grants", ["loans only", "skipping a budget", "paying late fees"], "These do not have to be repaid.")
H('12.G', 4, "Compared with a four-year college, a two-year college usually costs...", "less in total", ["more in total", "the same", "nothing"], "Fewer years of tuition.")

# --- END
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "batches", "g8_math.jsonl"))
print("saved", len(B.out), "questions")

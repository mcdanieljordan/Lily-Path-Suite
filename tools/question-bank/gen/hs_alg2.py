#!/usr/bin/env python3
"""High school Algebra II (TEKS 111.40.c). Original questions, process standards (1.A-G) skipped."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('111.40.c.', 984, own='hs_alg2.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A parent functions
H('2.A', 2, "What is the domain of the square root parent function f(x) = √x?", "x ≥ 0", ["all real numbers", "x > 0", "x ≤ 0"], "A square root of a negative number is not real, so x must be zero or positive.")
H('2.A', 2, "Which parent function has a vertical asymptote along the y-axis?", "f(x) = 1/x", ["f(x) = |x|", "f(x) = x³", "f(x) = ∛x"], "The reciprocal function is undefined at x = 0 and blows up near it.")
H('2.A', 3, "The graph of f(x) = b^x with b > 1 approaches which horizontal asymptote?", "y = 0", ["x = 0", "y = 1", "y = b"], "As x gets very negative, b^x gets closer to 0 but never reaches it.")
H('2.A', 2, "What is the range of the absolute value parent function?", "y ≥ 0", ["all real numbers", "y > 0", "y ≤ 0"], "Absolute value is never negative and equals 0 at x = 0.")
H('2.A', 3, "What is the range of the reciprocal parent function f(x) = 1/x?", "all real numbers except 0", ["all real numbers", "y > 0", "y ≥ 0"], "No x makes 1/x equal 0, but every other value is reached.")

# 2.B inverse
H('2.B', 3, "What is the inverse of f(x) = 2x + 6?", "f⁻¹(x) = (x − 6)/2", ["f⁻¹(x) = (x + 6)/2", "f⁻¹(x) = 1/(2x + 6)", "f⁻¹(x) = −2x − 6"], "Swap x and y: x = 2y + 6, so y = (x − 6)/2.")
H('2.B', 3, "What is the inverse of f(x) = x³ + 1?", "f⁻¹(x) = the cube root of (x minus 1)", ["f⁻¹(x) = the cube root of x, plus 1", "f⁻¹(x) = (x minus 1) cubed", "f⁻¹(x) = the cube root of (x plus 1)"], "x = y³ + 1 gives y³ = x − 1, so y = ∛(x − 1).")
H('2.B', 3, "What is the inverse of f(x) = x/3 − 2?", "f⁻¹(x) = 3x + 6", ["f⁻¹(x) = 3x − 6", "f⁻¹(x) = x/3 + 2", "f⁻¹(x) = 3x + 2"], "x = y/3 − 2 gives y/3 = x + 2, so y = 3x + 6.")
H('2.B', 2, "The graph of an inverse function is the graph of the original function reflected across which line?", "y = x", ["the x-axis", "the y-axis", "y = −x"], "Swapping x and y reflects points across the line y = x.")
H('2.B', 3, "Which function is the inverse of f(x) = 2^x?", "f⁻¹(x) = log₂(x)", ["f⁻¹(x) = x²", "f⁻¹(x) = 1/2^x", "f⁻¹(x) = 2 log(x)"], "Exponential and logarithm with the same base undo each other.")

# 2.C relationship between a function and its inverse
H('2.C', 3, "To give f(x) = x² an inverse function, which domain restriction works?", "x ≥ 0", ["all real numbers", "x ≠ 0", "−1 ≤ x ≤ 1"], "Restricting to one side of the vertex makes the function one-to-one.")
H('2.C', 2, "If f(2) = 7, what must be true of the inverse function?", "f⁻¹(7) = 2", ["f⁻¹(2) = 7", "f⁻¹(7) = 1/2", "f⁻¹(2) = 1/7"], "An inverse swaps inputs and outputs.")
H('2.C', 3, "The domain of f is the same set as which part of f⁻¹?", "the range of f⁻¹", ["the domain of f⁻¹", "the zeros of f⁻¹", "the y-intercept of f⁻¹"], "Inputs and outputs swap, so domain and range trade places.")
H('2.C', 3, "Which function is the inverse of g(x) = √x on its natural domain?", "g⁻¹(x) = x², with x restricted to nonnegative values", ["g⁻¹(x) = 1/√x", "g⁻¹(x) = −√x", "g⁻¹(x) = x², with every real x allowed"], "Squaring undoes the square root, but only the nonnegative side is the mirror image.")

# 2.D composition
H('2.D', 2, "Let f(x) = x + 3 and g(x) = 2x. What is f(g(x))?", "2x + 3", ["2x + 6", "2x²+ 3", "x + 5"], "Put 2x into f: 2x + 3.")
H('2.D', 3, "Let f(x) = 3x and g(x) = x/3. What does g(f(x)) simplify to, and what does that show?", "x, so they are inverses", ["3, so they are equal", "x², so they are opposites", "9x, so they are reciprocals"], "Composing a function with its inverse returns x.")
H('2.D', 4, "Let f(x) = √x and g(x) = x − 4. What is the domain of f(g(x))?", "x ≥ 4", ["x ≥ 0", "x ≥ −4", "all real numbers"], "The inside x − 4 must be at least 0.")
H('2.D', 3, "Let f(x) = x² and g(x) = x + 1. What is the value of f(g(3))?", "16", ["10", "12", "7"], "g(3) = 4, then f(4) = 16.")

# 3.A formulate systems
H('3.A', 3, "A store sells pens (x) at $2, notebooks (y) at $3 and folders (z) at $4. Which equation says that sales totaled $50?", "2x + 3y + 4z = 50", ["4x + 3y + 2z = 50", "x + y + z = 50", "2x + 3y + 4z = x + y + z"], "Price times quantity for each item, added together.")
H('3.A', 3, "A path is modeled by y = −x² + 6x and a wire by y = 2x. Which system finds where they cross?", "y = −x² + 6x and y = 2x", ["y = −x² + 6x and y = 2x²", "y = x² + 6x and y = −2x", "y = −x² + 6x and x = 2"], "Both equations must hold at the same point.")
H('3.A', 4, "How many solutions can a system made of a line and a parabola have?", "0, 1 or 2", ["exactly 1", "exactly 2", "infinitely many only"], "A line can miss, touch or cut a parabola.")

# 3.B solve 3x3
H('3.B', 4, "In the system x + y + z = 6, x − y + z = 2, x + y − z = 0, what is y?", "2", ["1", "3", "0"], "Subtract the second equation from the first: 2y = 4.")
H('3.B', 4, "In the system x + y + z = 6, x − y + z = 2, x + y − z = 0, what is z?", "3", ["1", "2", "6"], "Subtract the third equation from the first: 2z = 6.")
H('3.B', 4, "Solve x + y + z = 2, x − y + z = 4, x + y − z = 0. What is x?", "2", ["−1", "1", "4"], "Subtracting gives y = −1 and z = 1, then x = 2.")
H('3.B', 3, "What is the goal of the row operations in Gaussian elimination?", "to reach a triangular (row-echelon) form", ["to make every entry equal", "to transpose the matrix", "to find only the determinant"], "A triangular form lets you solve from the bottom up.")

# 3.C linear-quadratic algebraically
H('3.C', 4, "Which are the solutions of y = x² − 3 and y = x + 3?", "(3, 6) and (−2, 1)", ["(3, 6) and (2, 5)", "(−3, 0) and (2, 5)", "(3, 0) and (−2, 1)"], "x² − 3 = x + 3 gives x² − x − 6 = 0, so x = 3 or −2.")
H('3.C', 3, "How many solutions do y = x² and y = 2x − 1 have?", "exactly one", ["none", "exactly two", "infinitely many"], "x² − 2x + 1 = 0 is a perfect square with one repeated root.")
H('3.C', 4, "How many real solutions do y = x² + 1 and y = x − 1 have?", "none", ["one", "two", "infinitely many"], "x² − x + 2 = 0 has a negative discriminant.")
H('3.C', 3, "Where does y = x² − 4x meet the line y = 0?", "x = 0 and x = 4", ["x = 4 only", "x = −4 and x = 0", "x = 2 only"], "x(x − 4) = 0.")

# 3.D reasonableness
H('3.D', 3, "A rocket and drone meet at t = −2 or t = 5 seconds after launch. Which is reasonable?", "only the second", ["both", "only the first", "neither"], "Time after launch cannot be negative.")
H('3.D', 3, "A rectangle's width w satisfies (w − 7)(w + 3) = 0. Which width makes sense?", "w = 7", ["w = −3", "both widths", "neither width"], "Lengths must be positive.")
H('3.D', 3, "For a quadratic-linear system that models cars x hours after noon, which solution is reasonable?", "(2, 9) rather than (−1, 3)", ["(−1, 3) rather than (2, 9)", "both of them", "neither of them"], "Hours after noon cannot be negative.")

# 3.E formulate inequality systems
H('3.E', 3, "A club needs at least 10 people in total (j juniors, s seniors) and at most 4 seniors. Which system fits?", "j + s ≥ 10 and s ≤ 4", ["j + s ≤ 10 and s ≥ 4", "j + s ≥ 10 and s ≥ 4", "j + s ≤ 10 and s ≤ 4"], "At least means ≥ and at most means ≤.")
H('3.E', 3, "Which system describes the region above y = 2x and below y = 5?", "y > 2x and y < 5", ["y < 2x and y < 5", "y > 2x and y > 5", "y < 2x and y > 5"], "Above is greater than and below is less than.")
H('3.E', 3, "Which system describes the first-quadrant points with x + y at most 8?", "x ≥ 0, y ≥ 0, x + y ≤ 8", ["x ≤ 0, y ≤ 0, x + y ≤ 8", "x ≥ 0, y ≥ 0, x + y ≥ 8", "x > 8, y > 8"], "The first quadrant requires both coordinates nonnegative.")

# 3.F solve systems of inequalities
H('3.F', 3, "Which point satisfies both y ≥ x and y ≤ 4?", "(1, 3)", ["(3, 1)", "(2, 5)", "(5, 4)"], "For (1, 3): 3 ≥ 1 and 3 ≤ 4.")
H('3.F', 3, "What is the solution set of y > x + 1 and y < x − 1?", "no solution (empty set)", ["the whole plane", "a single line", "the strip between the lines"], "The lines are parallel and the shaded sides point away from each other.")
H('3.F', 3, "The solution of x ≥ 0, y ≥ 0 and x + y ≤ 4 forms which shape?", "a triangle", ["a square", "a line segment", "an unbounded region"], "The region is bounded by the axes and the line x + y = 4.")
H('3.F', 4, "What are the vertices of the region x ≥ 0, y ≥ 0, x + y ≤ 4?", "(0, 0), (4, 0), (0, 4)", ["(0, 0), (4, 4), (0, 4)", "(0, 0), (2, 2), (4, 0)", "(4, 0), (0, 4), (4, 4)"], "The corners are where the boundary lines meet.")

# 3.G possible solutions
H('3.G', 3, "Which point is NOT in the solution set of y < 2x and y > 1?", "(0, 2)", ["(3, 2)", "(4, 5)", "(2, 3)"], "At (0, 2), 2 < 0 is false.")
H('3.G', 3, "Which point is a solution of x + y ≤ 6 and x ≥ 2?", "(3, 2)", ["(1, 1)", "(4, 4)", "(2, 5)"], "3 + 2 = 5 ≤ 6 and 3 ≥ 2.")
H('3.G', 3, "A baker makes c cakes and p pies with c + p ≤ 10 and c ≥ 3. Which production plan is possible?", "5 cakes and 4 pies", ["2 cakes and 3 pies", "6 cakes and 6 pies", "5 cakes and −1 pies"], "It meets both limits and uses nonnegative counts.")

# 4.A quadratic from three points
H('4.A', 4, "Which quadratic passes through (0, 3), (1, 0) and (2, −1)?", "f(x) = x² − 4x + 3", ["f(x) = x² + 4x + 3", "f(x) = −x² + 4x + 3", "f(x) = x² − 3x + 3"], "The y-intercept is 3, and the other two points fix a = 1 and b = −4.")
H('4.A', 4, "Which quadratic passes through (0, −2), (1, −1) and (−1, −1)?", "f(x) = x² − 2", ["f(x) = x² + x − 2", "f(x) = 2x² − 2", "f(x) = −x² − 2"], "c = −2, and symmetry about the y-axis gives b = 0, so a = 1.")
H('4.A', 4, "Which quadratic passes through (0, 0), (1, 3) and (2, 10)?", "f(x) = 2x² + x", ["f(x) = x² + 2x", "f(x) = 3x²", "f(x) = 2x² + 3x"], "c = 0, a + b = 3 and 4a + 2b = 10 give a = 2 and b = 1.")

# 4.B parabola from attributes
H('4.B', 3, "A parabola opens up with vertex (2, 3) and a = 1. What is its equation?", "y = (x − 2)² + 3", ["y = (x + 2)² + 3", "y = (x − 2)² − 3", "y = (x − 3)² + 2"], "Vertex form is y = a(x − h)² + k.")
H('4.B', 4, "A parabola has vertex (0, 0) and focus (0, 2). What is its equation?", "y = x²/8", ["y = x²/2", "y = 8x²", "y = x²/4"], "p = 2, so x² = 4py = 8y.")
H('4.B', 4, "A parabola has vertex (1, −2) and directrix y = −3. What is its equation?", "y = (x − 1)²/4 − 2", ["y = (x − 1)² − 2", "y = (x + 1)²/4 − 2", "y = −(x − 1)²/4 − 2"], "p = 1 and the parabola opens up, so (x − 1)² = 4(y + 2).")
H('4.B', 2, "What is the axis of symmetry of y = (x + 4)² − 1?", "x = −4", ["x = 4", "x = −1", "y = −1"], "The axis passes through the vertex (−4, −1).")

# 4.C transformations of sqrt
H('4.C', 2, "How does the graph of f(x) = √x + 3 compare to √x?", "shifted up 3", ["shifted left 3", "shifted down 3", "shifted right 3"], "Adding outside the root moves the graph up.")
H('4.C', 2, "How does the graph of f(x) = √(x − 5) compare to √x?", "shifted right 5", ["shifted left 5", "shifted up 5", "shifted down 5"], "Subtracting inside moves the graph right.")
H('4.C', 3, "How does the graph of f(x) = √(4x) compare to √x?", "horizontally compressed by a factor of 1/4", ["horizontally stretched by a factor of 4", "shifted left 4", "shifted up 4"], "Multiplying x by 4 squeezes the graph toward the y-axis.")
H('4.C', 3, "How does the graph of f(x) = −√x compare to √x?", "reflected across the x-axis", ["reflected across the y-axis", "shifted down 1", "shifted left 1"], "The negative outside flips y-values.")
H('4.C', 3, "How does the graph of f(x) = √(−x) compare to √x?", "reflected across the y-axis", ["reflected across the x-axis", "shifted down 1", "rotated 90°"], "The negative inside flips the graph left and right.")

# 4.D vertex form
H('4.D', 3, "Write x² − 6x + 5 in the form a(x − h)² + k.", "(x − 3)² − 4", ["(x + 3)² − 4", "(x − 3)² + 4", "(x − 6)² − 31"], "Complete the square: x² − 6x + 9 − 9 + 5.")
H('4.D', 3, "Write x² + 4x + 1 in vertex form.", "(x + 2)² − 3", ["(x − 2)² − 3", "(x + 2)² + 3", "(x + 4)² − 15"], "Add and subtract 4.")
H('4.D', 4, "Write 2x² − 8x + 3 in vertex form.", "2(x − 2)² − 5", ["2(x − 2)² + 3", "2(x + 2)² − 5", "(x − 2)² − 5"], "2(x² − 4x + 4) − 8 + 3.")
H('4.D', 3, "What is the vertex of f(x) = x² − 6x + 5?", "(3, −4)", ["(−3, −4)", "(3, 4)", "(6, 5)"], "x = −b/2a = 3 and f(3) = −4.")
H('4.D', 2, "Which form of a quadratic shows the vertex most directly?", "vertex form", ["standard form", "factored form", "a table of values"], "a(x − h)² + k lists h and k.")

# 4.E formulate from table
H('4.E', 3, "A table shows (0, 1), (1, 2), (2, 5) and (3, 10). Which equation fits?", "y = x² + 1", ["y = 2x + 1", "y = x + 1", "y = 3x²"], "Each y equals x squared plus 1.")
H('4.E', 3, "A table shows (1, 2), (4, 3) and (9, 4). Which equation fits?", "y = √x + 1", ["y = x + 1", "y = √x − 1", "y = x/2 + 1.5"], "The square roots of 1, 4, 9 are 1, 2, 3, and then add 1.")
H('4.E', 3, "A table shows (0, 0), (1, 2), (2, 8) and (3, 18). Which equation fits?", "y = 2x²", ["y = 6x − 4", "y = 4x²", "y = 2x"], "2 times 1, 4 and 9 gives 2, 8 and 18.")

# 4.F solve quadratic and sqrt
H('4.F', 2, "What are the solutions of x² − 5x + 6 = 0?", "x = 2 and x = 3", ["x = −2 and x = −3", "x = 1 and x = 6", "x = −1 and x = 6"], "(x − 2)(x − 3) = 0.")
H('4.F', 2, "What are the solutions of 2x² = 18?", "x = 3 and x = −3", ["x = 9", "x = 3 only", "x = 9 and x = −9"], "x² = 9.")
H('4.F', 3, "Solve √(x + 5) = 3.", "x = 4", ["x = −2", "x = 14", "x = 8"], "Square both sides: x + 5 = 9.")
H('4.F', 4, "What are the solutions of x² + 4x + 1 = 0?", "x = −2 ± √3", ["x = 2 ± √3", "x = −2 ± √5", "x = −4 ± √3"], "The quadratic formula gives (−4 ± √12)/2.")
H('4.F', 3, "Solve √(2x − 1) = 5.", "x = 13", ["x = 3", "x = 26", "x = 12"], "2x − 1 = 25.")

# 4.G extraneous
H('4.G', 4, "Solving √(x + 6) = x leads to candidates 3 and −2. Which one fails when checked?", "−2", ["3", "both", "neither"], "√4 = 2, which does not equal −2.")
H('4.G', 4, "Solving √(3x + 4) = x leads to candidates 4 and −1. Which one is extraneous?", "−1", ["4", "both", "neither"], "√1 = 1, not −1.")
H('4.G', 4, "Solving x − 2 = √x leads to candidates 1 and 4. Which one is extraneous?", "1", ["4", "both", "neither"], "At 1, the left side is −1 but √1 = 1.")

# 4.H quadratic inequalities
H('4.H', 3, "Solve x² − 4 > 0.", "x < −2 or x > 2", ["−2 < x < 2", "x > 2 only", "x < 4"], "The parabola is above the axis outside its zeros.")
H('4.H', 3, "Solve x² − 5x + 6 ≤ 0.", "2 ≤ x ≤ 3", ["x ≤ 2 or x ≥ 3", "x ≤ 2", "x ≥ 3"], "The parabola is on or below the axis between its zeros.")
H('4.H', 3, "Solve x² < 9.", "−3 < x < 3", ["x < 3", "x < −3 or x > 3", "x > 3"], "|x| < 3.")
H('4.H', 4, "Solve x² − x − 6 ≥ 0.", "x ≤ −2 or x ≥ 3", ["−2 ≤ x ≤ 3", "x ≥ 3", "x ≤ −3 or x ≥ 2"], "The zeros are −2 and 3, and the parabola opens up.")

# 5.A exponential and log graphs
H('5.A', 3, "For x > 0, which grows faster, y = 2^x or y = 3^x?", "y = 3^x", ["y = 2^x", "They grow at the same rate", "Neither grows"], "A larger base means faster growth.")
H('5.A', 3, "What is the horizontal asymptote of f(x) = 2^x + 3?", "y = 3", ["y = 0", "x = 3", "y = 2"], "The graph shifts up 3.")
H('5.A', 3, "What is the vertical asymptote of f(x) = log₂(x)?", "x = 0", ["y = 0", "x = 1", "x = 2"], "The log is undefined for x ≤ 0.")
H('5.A', 3, "What is the domain of f(x) = log_b(x)?", "x > 0", ["x ≥ 0", "all real numbers", "x > 1"], "Only positive numbers have a logarithm.")
H('5.A', 4, "What is the vertical asymptote of f(x) = log(x − 4)?", "x = 4", ["x = −4", "x = 0", "y = 4"], "The argument is zero when x = 4.")

# 5.B formulate exponential/log models
H('5.B', 3, "$500 earns 4% interest compounded annually. Which equation gives the balance after t years?", "A = 500(1.04)^t", ["A = 500(0.04)^t", "A = 500 + 0.04t", "A = 500(4)^t"], "Growth of 4% multiplies by 1.04 each year.")
H('5.B', 3, "A population of 1000 falls 5% each year. Which equation models it?", "P = 1000(0.95)^t", ["P = 1000(0.05)^t", "P = 1000(1.05)^t", "P = 1000 − 0.05t"], "A 5% loss multiplies by 0.95.")
H('5.B', 3, "A culture starts at 50 bacteria and doubles every hour. Which equation models it?", "N = 50 · 2^t", ["N = 50 + 2t", "N = 2 · 50^t", "N = 100t"], "Start times growth factor to the power of hours.")
H('5.B', 4, "A substance has a half-life of 10 years and starts at A₀. Which equation gives the amount after t years?", "A = A₀(1/2)^(t/10)", ["A = A₀(1/2)^(10t)", "A = A₀ − t/10", "A = A₀(10)^(t/2)"], "The amount halves once every 10 years.")

# 5.C rewrite exp/log
H('5.C', 2, "Rewrite 2⁵ = 32 as a logarithmic equation.", "log₂(32) = 5", ["log₅(32) = 2", "log₃₂(2) = 5", "log₂(5) = 32"], "The exponent is the logarithm.")
H('5.C', 2, "Rewrite log₃(81) = 4 as an exponential equation.", "3⁴ = 81", ["4³ = 81", "81⁴ = 3", "3⁸¹ = 4"], "Base to the power of the log equals the argument.")
H('5.C', 2, "Rewrite 10³ = 1000 as a logarithmic equation.", "log(1000) = 3", ["log(3) = 1000", "log(10) = 1000", "ln(1000) = 3"], "A log with no base shown is base 10.")
H('5.C', 3, "Rewrite log₅(x) = 2 as an exponential equation.", "5² = x", ["2⁵ = x", "x² = 5", "5x = 2"], "Base 5 to the power 2 equals x.")
H('5.C', 3, "Rewrite e^x = 7 as a logarithmic equation.", "ln(7) = x", ["ln(x) = 7", "log(7) = x", "e·ln(7) = x"], "The natural log undoes base e.")

# 5.D solve exponential
H('5.D', 2, "Solve 2^x = 32.", "x = 5", ["x = 16", "x = 4", "x = 6"], "32 = 2⁵.")
H('5.D', 3, "Solve 3^(x + 1) = 27.", "x = 2", ["x = 3", "x = 8", "x = 1"], "27 = 3³, so x + 1 = 3.")
H('5.D', 3, "Solve 5 · 2^x = 40.", "x = 3", ["x = 8", "x = 35", "x = 4"], "Divide by 5: 2^x = 8.")
H('5.D', 4, "Solve 4^x = 2.", "x = 1/2", ["x = 2", "x = 1/4", "x = 8"], "4^(1/2) = 2.")
H('5.D', 4, "Solve 9^x = 27.", "x = 3/2", ["x = 3", "x = 2/3", "x = 18"], "3^(2x) = 3³.")

# 5.E reasonableness of log solutions
H('5.E', 4, "Solving log₂(x) + log₂(x − 3) = 2 produces two candidates, 4 and −1. Which is reasonable?", "only the positive one", ["both", "only the negative one", "neither"], "A logarithm's argument must be positive.")
H('5.E', 3, "A student gets x = 0 for log₅(x) + 1 = 3. Is that reasonable?", "No, the argument of a log must be positive", ["Yes, because 0 is an integer", "Yes, because log₅(0) = 0", "No, because the base is 5"], "log₅(0) is undefined.")
H('5.E', 3, "log₂(x − 1) = 3 gives x = 9. Is the solution reasonable?", "Yes, it makes the argument positive", ["No, because x is odd", "No, because 9 > 3", "Yes, only if x = 3"], "9 − 1 = 8 > 0 and log₂(8) = 3.")

# 6.A cube / cube root transformations
H('6.A', 3, "How does f(x) = (x − 2)³ compare to x³?", "shifted right 2", ["shifted left 2", "shifted up 2", "shifted down 2"], "Subtracting inside shifts right.")
H('6.A', 2, "How does f(x) = ∛x + 4 compare to ∛x?", "shifted up 4", ["shifted left 4", "shifted right 4", "shifted down 4"], "Adding outside shifts up.")
H('6.A', 3, "How does f(x) = −x³ compare to x³?", "reflected across the x-axis", ["reflected across the line y = x", "shifted down", "unchanged"], "Negating the output flips the graph vertically.")
H('6.A', 3, "How does f(x) = ∛(x + 1) compare to ∛x?", "shifted left 1", ["shifted right 1", "shifted up 1", "reflected"], "Adding inside shifts left.")
H('6.A', 3, "How does f(x) = 2x³ compare to x³?", "vertically stretched by a factor of 2", ["horizontally stretched by 2", "shifted up 2", "shifted right 2"], "The output is doubled.")

# 6.B cube root equations
H('6.B', 2, "Solve ∛x = 3.", "x = 27", ["x = 9", "x = 1", "x = 6"], "Cube both sides.")
H('6.B', 3, "Solve ∛(x − 1) = 2.", "x = 9", ["x = 7", "x = 3", "x = 5"], "x − 1 = 8.")
H('6.B', 3, "Solve ∛(2x) = −2.", "x = −4", ["x = −8", "x = 4", "x = −1"], "2x = −8.")
H('6.B', 4, "Solve ∛(x + 4) = −3.", "x = −31", ["x = −7", "x = 23", "x = −13"], "x + 4 = −27.")

# 6.C absolute value transformations
H('6.C', 2, "How does f(x) = |x − 3| compare to |x|?", "shifted right 3", ["shifted left 3", "shifted up 3", "shifted down 3"], "Subtracting inside shifts right.")
H('6.C', 2, "How does f(x) = −|x| compare to |x|?", "opens downward", ["opens upward and is narrower", "shifted left", "shifted up"], "The negative flips the V upside down.")
H('6.C', 3, "How does f(x) = 2|x| compare to |x|?", "narrower", ["wider", "shifted up 2", "shifted right 2"], "A larger vertical stretch makes the V steeper.")
H('6.C', 3, "What is the vertex of f(x) = |x + 5| − 1?", "(−5, −1)", ["(5, −1)", "(−5, 1)", "(5, 1)"], "Inside +5 moves left, outside −1 moves down.")

# 6.D formulate absolute value equations
H('6.D', 3, "Which equation says that x is exactly 5 units from 2 on the number line?", "|x − 2| = 5", ["|x + 2| = 5", "|x| = 7", "x − 2 = 5 only"], "Distance between x and 2 is |x − 2|.")
H('6.D', 3, "A thermostat is set to 70°F and the actual temperature T differs from it by exactly 3 degrees. Which equation fits?", "|T − 70| = 3", ["|T + 70| = 3", "|T − 3| = 70", "T − 70 = 3 only"], "The difference from 70 has an absolute value of 3.")
H('6.D', 4, "Which equation says x is exactly 4 units from −1?", "|x + 1| = 4", ["|x − 1| = 4", "|x + 4| = 1", "|x| = 3"], "x − (−1) = x + 1.")

# 6.E solve absolute value equations
H('6.E', 2, "Solve |x − 3| = 5.", "x = 8 or x = −2", ["x = 8 only", "x = 2 or x = −8", "x = 5"], "x − 3 = 5 or x − 3 = −5.")
H('6.E', 3, "Solve |2x + 1| = 7.", "x = 3 or x = −4", ["x = 3 only", "x = 4 or x = −3", "x = 3 or x = −3"], "2x + 1 = 7 or 2x + 1 = −7.")
H('6.E', 3, "Solve |x| + 2 = 9.", "x = 7 or x = −7", ["x = 7 only", "x = 11 or x = −11", "no solution"], "|x| = 7.")
H('6.E', 3, "How many solutions does |x − 4| = −2 have?", "none", ["one", "two", "infinitely many"], "An absolute value cannot be negative.")
H('6.E', 4, "Solve 3|x + 1| = 12.", "x = 3 or x = −5", ["x = 3 only", "x = 11 or x = −13", "x = 4 or x = −4"], "|x + 1| = 4.")

# 6.F absolute value inequalities
H('6.F', 3, "Solve |x| < 4.", "−4 < x < 4", ["x < −4 or x > 4", "x < 4 only", "x > −4 only"], "Less than means between.")
H('6.F', 4, "Solve |x − 2| ≥ 3.", "x ≤ −1 or x ≥ 5", ["−1 ≤ x ≤ 5", "x ≥ 5 only", "x ≤ −1 only"], "Greater than means outside the interval.")
H('6.F', 4, "Solve |2x − 1| ≤ 5.", "−2 ≤ x ≤ 3", ["x ≤ −2 or x ≥ 3", "−3 ≤ x ≤ 2", "x ≤ 3"], "−5 ≤ 2x − 1 ≤ 5.")
H('6.F', 4, "Solve |x + 3| > 1.", "x < −4 or x > −2", ["−4 < x < −2", "x > −2 only", "x < 4 or x > 2"], "x + 3 > 1 or x + 3 < −1.")

# 6.G reciprocal transformations
H('6.G', 3, "What is the vertical asymptote of f(x) = 1/(x − 4)?", "x = 4", ["x = −4", "y = 4", "x = 0"], "The denominator is zero at x = 4.")
H('6.G', 3, "What is the horizontal asymptote of f(x) = 1/x + 3?", "y = 3", ["y = 0", "x = 3", "y = −3"], "Adding outside shifts the asymptote up 3.")
H('6.G', 3, "How does f(x) = 2/x compare to 1/x?", "vertically stretched by a factor of 2", ["shifted up 2", "shifted right 2", "reflected across the x-axis"], "All outputs are doubled.")
H('6.G', 4, "What are the asymptotes of f(x) = 1/(x + 2) − 5?", "x = −2 and y = −5", ["x = 2 and y = 5", "x = −2 and y = 5", "x = 5 and y = −2"], "Inside +2 moves left and outside −5 moves down.")

# 6.H formulate rational equations
H('6.H', 4, "Pat paints a room in 4 hours and Lee in 6 hours. Working together takes t hours. Which equation fits?", "t/4 + t/6 = 1", ["t/4 − t/6 = 1", "4t + 6t = 1", "t/(4 + 6) = 1"], "Each person's fraction of the job adds up to one whole job.")
H('6.H', 4, "A boat goes 12 miles upstream and 12 miles back in 5 hours in a 2 mph current, with boat speed b. Which equation fits?", "12/(b − 2) + 12/(b + 2) = 5", ["12/(b + 2) − 12/(b − 2) = 5", "24/b = 5", "12b − 24 = 5"], "Time equals distance over speed for each leg.")
H('6.H', 3, "Fixed costs are $500 and each item costs $10 to make. Which equation gives the average cost per item for n items?", "C = (500 + 10n)/n", ["C = 500 + 10n", "C = 500/n + 10n", "C = (500 + 10)/n"], "Total cost divided by the number of items.")

# 6.I solve rational equations
H('6.I', 3, "Solve 3/x = 6.", "x = 1/2", ["x = 2", "x = 18", "x = 3"], "x = 3/6.")
H('6.I', 3, "Solve 1/x + 1/2 = 1.", "x = 2", ["x = 1/2", "x = 3/2", "x = 1"], "1/x = 1/2.")
H('6.I', 4, "Solve (x + 1)/(x − 2) = 4.", "x = 3", ["x = 9", "x = −3", "x = 2"], "x + 1 = 4x − 8.")
H('6.I', 4, "Solve 2/(x − 1) = 1/(x + 2).", "x = −5", ["x = 5", "x = −1", "x = 3"], "Cross multiply: 2x + 4 = x − 1.")

# 6.J reasonableness of rational solutions
H('6.J', 4, "Solving x²/(x − 2) = 4/(x − 2) gives candidates 2 and −2. Which is valid?", "only the negative one", ["both", "only the positive one", "neither"], "The positive candidate makes the denominator zero.")
H('6.J', 4, "Solving (x² − 9)/(x − 3) = 6 leads to x = 3. Is that valid?", "No, it makes a denominator zero", ["Yes, because it satisfies the numerator", "Yes, because 3 is positive", "No, because 3 is odd"], "The expression is undefined at 3.")
H('6.J', 3, "A work-rate equation gives one negative time and one positive time in hours. Which is reasonable?", "the positive time", ["the negative time", "both times", "neither time"], "Time cannot be negative.")

# 6.K domain / range of rational functions
H('6.K', 3, "What is the domain of f(x) = 1/(x − 5) in interval notation?", "(−∞, 5) ∪ (5, ∞)", ["[5, ∞)", "(−∞, ∞)", "(5, ∞)"], "Every number except 5 is allowed.")
H('6.K', 3, "What is the domain of f(x) = (x + 1)/(x + 4)?", "all real numbers except −4", ["all real numbers except −1", "x > −4", "all real numbers"], "The denominator is zero at −4.")
H('6.K', 4, "What is the domain of f(x) = 2/(x² − 9)?", "all real numbers except 3 and −3", ["all real numbers except 9", "x > 3", "all real numbers except 3"], "x² − 9 = 0 at x = ±3.")
H('6.K', 4, "What is the range of f(x) = 1/x + 2?", "all real numbers except 2", ["all real numbers except 0", "y > 2", "all real numbers"], "The horizontal asymptote y = 2 is never reached.")

# 6.L inverse variation
H('6.L', 3, "y varies inversely with x, and y = 6 when x = 2. What is y when x = 3?", "4", ["9", "2", "6"], "k = 12, so y = 12/3.")
H('6.L', 3, "In an inverse variation, xy = 20 and x = 5. What is y?", "4", ["100", "25", "15"], "y = 20/5.")
H('6.L', 3, "A 120-mile trip takes t hours at r mph. How long does it take at 40 mph?", "3 hours", ["80 hours", "2 hours", "4.8 hours"], "t = 120/r = 120/40.")
H('6.L', 4, "Which table shows an inverse variation?", "x: 2, 3, 4 and y: 12, 8, 6", ["x: 2, 3, 4 and y: 4, 6, 8", "x: 2, 3, 4 and y: 10, 8, 6", "x: 2, 3, 4 and y: 12, 9, 6"], "The products xy are all 24.")

# 7.A complex numbers
H('7.A', 2, "What is (3 + 2i) + (1 − 5i)?", "4 − 3i", ["4 + 7i", "2 + 7i", "4 − 7i"], "Add real parts and imaginary parts.")
H('7.A', 2, "What is (5 + i) − (2 + 4i)?", "3 − 3i", ["3 + 5i", "7 + 5i", "3 + 3i"], "Subtract each part.")
H('7.A', 3, "What is (2 + 3i)(1 − i)?", "5 + i", ["2 − 3i", "−1 + i", "5 − i"], "2 − 2i + 3i − 3i² = 2 + i + 3.")
H('7.A', 3, "What is (3 + i)(3 − i)?", "10", ["8", "9 − i²", "6"], "9 − i² = 9 + 1.")
H('7.A', 3, "What is (1 + 2i)²?", "−3 + 4i", ["5 + 4i", "1 + 4i", "−3 + 2i"], "1 + 4i + 4i² = −3 + 4i.")
H('7.A', 3, "What is i⁷?", "−i", ["i", "1", "−1"], "i⁴ = 1, so i⁷ = i³ = −i.")

# 7.B polynomials
H('7.B', 2, "What is (x² + 3x) + (2x² − x + 4)?", "3x² + 2x + 4", ["3x² + 4x + 4", "2x⁴ + 2x + 4", "3x² + 2x"], "Combine like terms.")
H('7.B', 3, "What is (3x³ + x) − (x³ − 2x² + 5)?", "2x³ + 2x² + x − 5", ["2x³ − 2x² + x − 5", "2x³ + 2x² + x + 5", "4x³ + 2x² + x + 5"], "Distribute the subtraction.")
H('7.B', 3, "What is (x + 2)(x² − x + 3)?", "x³ + x² + x + 6", ["x³ − x² + 6", "x³ + 3x² + 6", "x³ + x² + 5x + 6"], "x³ − x² + 3x + 2x² − 2x + 6.")
H('7.B', 3, "What is (2x − 1)(x + 4)?", "2x² + 7x − 4", ["2x² + 9x − 4", "2x² − 4", "2x² + 7x + 4"], "2x² + 8x − x − 4.")
H('7.B', 3, "What is (x − 3)²?", "x² − 6x + 9", ["x² − 9", "x² + 9", "x² − 6x − 9"], "Square the binomial.")

# 7.C polynomial division
H('7.C', 3, "What is (x³ − x² − 4x + 4) ÷ (x − 1)?", "x² − 4", ["x² − 2x + 2", "x² + 4", "x² − x"], "Synthetic division with 1 gives 1, 0, −4 and remainder 0.")
H('7.C', 3, "What is (x³ + 2x² − 5x − 6) ÷ (x + 1)?", "x² + x − 6", ["x² + 3x − 8", "x² − x − 6", "x² + x + 6"], "Synthetic division with −1 gives 1, 1, −6 and remainder 0.")
H('7.C', 4, "What is the remainder when x³ + 3x² + x + 5 is divided by x + 2?", "7", ["−7", "5", "0"], "f(−2) = −8 + 12 − 2 + 5.")
H('7.C', 4, "What is (x⁴ − 1) ÷ (x² + 1)?", "x² − 1", ["x² + 1", "x⁶ − 1", "x² − 2"], "x⁴ − 1 = (x² + 1)(x² − 1).")
H('7.C', 3, "What is (x³ + 8) ÷ (x + 2)?", "x² − 2x + 4", ["x² + 2x + 4", "x² + 4", "x² − 4"], "Sum of cubes factors as (x + 2)(x² − 2x + 4).")

# 7.D linear factors
H('7.D', 4, "Which is a linear factor of f(x) = x³ − 6x² + 11x − 6?", "x − 1", ["x + 1", "x − 6", "x + 6"], "f(1) = 0.")
H('7.D', 4, "Which is the complete set of zeros of f(x) = x³ − 7x − 6?", "−1, −2 and 3", ["1, 2 and −3", "−1, 2 and 3", "1, −2 and −3"], "f(−1) = f(−2) = f(3) = 0.")
H('7.D', 3, "If f(4) = 0 for a polynomial f, what is a factor of f?", "x − 4", ["x + 4", "x − 1", "4x"], "Factor theorem.")
H('7.D', 4, "Which are linear factors of x⁴ − 16?", "(x − 2) and (x + 2)", ["(x − 4) and (x + 4)", "(x − 2) and (x + 4)", "(x − 8) and (x + 8)"], "x⁴ − 16 = (x² + 4)(x − 2)(x + 2).")

# 7.E linear and quadratic factors
H('7.E', 4, "Factor x³ − 8.", "(x − 2)(x² + 2x + 4)", ["(x − 2)(x² − 2x + 4)", "(x − 2)³", "(x − 2)(x² + 4)"], "Difference of cubes.")
H('7.E', 4, "Factor x³ + 27.", "(x + 3)(x² − 3x + 9)", ["(x + 3)(x² + 3x + 9)", "(x + 3)³", "(x + 3)(x² + 9)"], "Sum of cubes.")
H('7.E', 4, "Factor x⁴ − 5x² + 4 completely.", "(x − 1)(x + 1)(x − 2)(x + 2)", ["(x² − 1)(x² + 4)", "(x − 1)²(x − 4)²", "(x − 4)(x + 1)(x² + 1)"], "(x² − 1)(x² − 4), then factor each difference of squares.")
H('7.E', 4, "Factor x³ + 2x² − x − 2 by grouping.", "(x + 2)(x − 1)(x + 1)", ["(x + 2)(x² + 1)", "(x − 2)(x² − 1)", "(x + 2)²(x − 1)"], "x²(x + 2) − (x + 2) = (x + 2)(x² − 1).")

# 7.F rational expressions
H('7.F', 3, "Simplify x/(x + 1) + 1/(x + 1).", "1", ["x + 1", "(x + 1)/2", "x/(x + 2)"], "The numerators add to x + 1.")
H('7.F', 3, "Simplify 3/x² + 2/x.", "(2x + 3)/x²", ["5/x³", "5/x²", "(2x + 3)/x"], "Use the common denominator x².")
H('7.F', 4, "Simplify (x² − 9)/(x + 1) · (x + 1)/(x − 3).", "x + 3", ["x − 3", "x² − 3", "(x + 3)/(x + 1)"], "Cancel x + 1 and x − 3.")
H('7.F', 4, "Simplify 1/x − 1/(x + 2).", "2/(x(x + 2))", ["1/(x(x + 2))", "−2/(x(x + 2))", "0"], "(x + 2 − x)/(x(x + 2)).")
H('7.F', 4, "Simplify (x² − 1)/x ÷ (x − 1)/x².", "x(x + 1)", ["(x + 1)/x", "x − 1", "x²(x + 1)"], "Multiply by the reciprocal and cancel.")

# 7.G radical expressions
H('7.G', 3, "For x ≥ 0, simplify √(18x²).", "3x√2", ["9x√2", "3x²√2", "2x√3"], "√(9 · 2 · x²).")
H('7.G', 3, "For x ≥ 0, simplify √(x⁵).", "x²√x", ["x⁵", "x√x", "x³√x"], "x⁵ = x⁴ · x.")
H('7.G', 3, "Simplify ∛(8x⁶).", "2x²", ["2x³", "8x²", "4x²"], "∛8 = 2 and ∛(x⁶) = x².")
H('7.G', 4, "For x ≥ 0, simplify √(12x³).", "2x√(3x)", ["4x√(3x)", "2x²√3", "6x√x"], "12x³ = 4x² · 3x.")
H('7.G', 4, "For x > 0, rewrite 3/√x with no radical in the denominator.", "3√x / x", ["3x", "√(3x)", "3/x"], "Multiply top and bottom by √x.")

# 7.H rational exponents
H('7.H', 3, "Solve x^(1/2) = 5.", "x = 25", ["x = 5/2", "x = 10", "x = √5"], "Square both sides.")
H('7.H', 4, "Solve x^(3/2) = 27.", "x = 9", ["x = 3", "x = 81", "x = 18"], "x = 27^(2/3).")
H('7.H', 3, "Solve x^(1/3) = −2.", "x = −8", ["x = −6", "x = 8", "x = −2/3"], "Cube both sides.")
H('7.H', 3, "Solve x^(1/4) = 2.", "x = 16", ["x = 8", "x = 6", "x = 2"], "Raise both sides to the fourth power.")
H('7.H', 4, "Solve (x + 1)^(1/2) = 3.", "x = 8", ["x = 9", "x = 2", "x = 4"], "x + 1 = 9.")

# 7.I domain and range notation
H('7.I', 3, "What is the domain of f(x) = √(x − 2) in interval notation?", "[2, ∞)", ["(2, ∞)", "(−∞, 2]", "(−∞, ∞)"], "x − 2 must be at least 0.")
H('7.I', 3, "What is the range of f(x) = x² + 1 in interval notation?", "[1, ∞)", ["(−∞, 1]", "[0, ∞)", "(1, ∞)"], "The minimum value is 1 at x = 0.")
H('7.I', 3, "What is the domain of f(x) = 1/(x − 1) in interval notation?", "(−∞, 1) ∪ (1, ∞)", ["(1, ∞)", "[1, ∞)", "(−∞, ∞)"], "Only x = 1 is excluded.")
H('7.I', 4, "What is the range of f(x) = −|x| + 3 in interval notation?", "(−∞, 3]", ["[3, ∞)", "(−∞, −3]", "(−∞, ∞)"], "The maximum value is 3.")
H('7.I', 3, "Which set notation describes the domain of f(x) = √(x − 2)?", "{x | x ≥ 2}", ["{x | x > 2}", "{x | x ≤ 2}", "{x | x ≠ 2}"], "The set of all x at least 2.")

# 8.A choose a model
H('8.A', 3, "The data (0, 2), (1, 4), (2, 8), (3, 16) are best modeled by which type of function?", "exponential", ["linear", "quadratic", "square root"], "Each y is double the previous one.")
H('8.A', 3, "The data (1, 2), (2, 5), (3, 10), (4, 17) have constant second differences. Which model fits?", "quadratic", ["linear", "exponential", "logarithmic"], "Differences 3, 5, 7 grow by a constant 2.")
H('8.A', 3, "The data (0, 1), (1, 4), (2, 7), (3, 10) are best modeled by which type of function?", "linear", ["quadratic", "exponential", "cubic"], "Each y increases by the same 3.")
H('8.A', 3, "If equally spaced x-values give a constant ratio between consecutive y-values, which model fits?", "exponential", ["linear", "quadratic", "absolute value"], "A constant ratio is the sign of exponential growth or decay.")

# 8.B regression
H('8.B', 3, "Which regression type best models a thrown ball's height over time?", "quadratic", ["linear", "exponential", "reciprocal"], "Height under gravity is a parabola.")
H('8.B', 3, "Which regression type best models a population that doubles every year?", "exponential", ["linear", "quadratic", "absolute value"], "Repeated doubling is exponential growth.")
H('8.B', 3, "A regression gives y = 2.1x + 3.4. What does it predict for x = 5?", "13.9", ["10.5", "14.5", "5.5"], "2.1(5) + 3.4.")
H('8.B', 4, "A regression gives h = −4.9t² + 20t + 1.5. What height does it predict at t = 2?", "21.9", ["19.6", "40", "−19.6"], "−19.6 + 40 + 1.5.")
H('8.B', 3, "An R² value close to 1 suggests what about a regression model?", "it fits the data closely", ["it is guaranteed to predict well outside the data", "the data are random", "the slope must be 1"], "R² measures how much variation the model explains.")

# 8.C predictions and decisions
H('8.C', 3, "An exponential model is y = 100(1.05)^t. What does it predict at t = 2?", "110.25", ["110", "100.25", "105"], "100 × 1.1025.")
H('8.C', 4, "Profit is modeled by P = −x² + 10x. What is the maximum profit?", "25", ["10", "5", "50"], "The vertex is at x = 5 and P(5) = 25.")
H('8.C', 3, "A linear model for school enrollment predicts a negative number far in the future. What should you conclude?", "the model is not reasonable that far out", ["negative students are possible", "the data are wrong", "the slope must be zero"], "Models have limits outside the data range.")
H('8.C', 3, "A population model is y = 50(2)^t, with t in periods. How large is the population after 3 periods?", "400", ["300", "150", "250"], "50 × 8.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_alg2.jsonl'))

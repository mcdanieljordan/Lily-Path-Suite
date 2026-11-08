#!/usr/bin/env python3
"""High school Algebra I (TEKS 111.39.c). Original questions, process standards (1.A-G) skipped."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('111.39.c.', 982, own='hs_alg1.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A domain and range
H('2.A', 3, "A taxi charges $3 plus $2 per mile. For trips of at most 10 miles, which is a reasonable domain for the cost function?", "0 ≤ x ≤ 10", ["x ≥ 3", "3 ≤ x ≤ 23", "all negative numbers"], "Miles driven range from 0 to 10.")
H('2.A', 2, "What are the domain and range of f(x) = 2x + 1 when x can be any real number?", "both all real numbers", ["domain x ≥ 0, range y ≥ 1", "domain all reals, range y = 1", "domain x ≥ 1, range all reals"], "A non-constant line takes every real input and output.")
H('2.A', 3, "A tank is filled at 5 gallons per minute for 20 minutes. If g(t) = 5t, what is a reasonable range?", "0 ≤ g ≤ 100", ["0 ≤ g ≤ 20", "g ≥ 100", "all real numbers"], "At t = 20, g = 100 gallons.")
# 2.B forms of linear equations
H('2.B', 2, "Which equation has slope 3 and y-intercept -2?", "y = 3x − 2", ["y = −2x + 3", "y = 3x + 2", "y = x − 6"], "Slope-intercept form is y = mx + b.")
H('2.B', 3, "Which is the point-slope form of the line with slope 4 through (2, 5)?", "y − 5 = 4(x − 2)", ["y − 2 = 4(x − 5)", "y + 5 = 4(x + 2)", "y = 4x + 5"], "Point-slope form is y − y₁ = m(x − x₁).")
H('2.B', 3, "Write y = 2x + 3 in standard form Ax + By = C.", "2x − y = −3", ["2x + y = 3", "x − 2y = 3", "−2x − y = 3"], "Subtract y from both sides: 2x − y = −3.")
# 2.C from table, graph, description
H('2.C', 3, "A table shows (0, 4), (1, 7), (2, 10). Which equation fits these points?", "y = 3x + 4", ["y = 4x + 3", "y = 3x + 7", "y = 7x + 4"], "Constant change of 3 and y-intercept 4.")
H('2.C', 3, "A line on a graph passes through (0, −1) and (2, 3). Which equation describes it?", "y = 2x − 1", ["y = 2x + 1", "y = −x + 2", "y = 3x − 1"], "Slope (3 − (−1))/2 = 2; y-intercept −1.")
H('2.C', 3, "A savings account starts with $50 and adds $10 each week. Which equation gives the balance y after x weeks?", "y = 10x + 50", ["y = 50x + 10", "y = 10x − 50", "y = 60x"], "Rate is 10 per week; start is 50.")
# 2.D direct variation
H('2.D', 3, "If y varies directly with x and y = 3 when x = 2, what is the constant of variation k?", "1.5", ["6", "0.67", "5"], "k = y/x = 3/2 = 1.5.")
H('2.D', 3, "y varies directly with x. If y = 20 when x = 4, what is y when x = 7?", "35", ["28", "27", "45"], "k = 5, so y = 5(7) = 35.")
H('2.D', 2, "Which equation represents a direct variation?", "y = 5x", ["y = 5x + 1", "y = x + 5", "y = 5 − x"], "Direct variation has the form y = kx.")
# 2.E parallel
H('2.E', 3, "Which line passes through (1, 5) and is parallel to y = 2x + 1?", "y = 2x + 3", ["y = −½x + 5.5", "y = 2x + 5", "y = x + 4"], "Same slope 2; 5 = 2(1) + b gives b = 3.")
H('2.E', 3, "A line parallel to y = −3x + 4 passes through the origin. Its equation is...", "y = −3x", ["y = 3x", "y = −3x + 4", "y = ⅓x"], "Same slope, b = 0.")
H('2.E', 4, "Which line is parallel to y = ½x − 2 and contains (4, 1)?", "y = ½x − 1", ["y = ½x + 1", "y = −2x + 9", "y = 2x − 7"], "1 = ½(4) + b gives b = −1.")
# 2.F perpendicular
H('2.F', 3, "What is the slope of a line perpendicular to y = 2x + 1?", "−½", ["2", "½", "−2"], "Perpendicular slopes are negative reciprocals.")
H('2.F', 4, "Which line contains (4, 3) and is perpendicular to y = 2x + 1?", "y = −½x + 5", ["y = 2x − 5", "y = −½x + 3", "y = ½x + 1"], "Slope −½; 3 = −2 + b gives b = 5.")
H('2.F', 3, "A line perpendicular to y = −3x passes through the origin. Its equation is...", "y = ⅓x", ["y = 3x", "y = −⅓x", "y = −3x + 1"], "Negative reciprocal of −3 is ⅓.")
# 2.G horizontal/vertical
H('2.G', 2, "Which equation describes the line through (3, 5) and (3, −2)?", "x = 3", ["y = 3", "y = 5", "x = −2"], "Both points have x = 3, so the line is vertical.")
H('2.G', 2, "The line through (−1, 4) that is parallel to the x-axis has the equation...", "y = 4", ["x = −1", "y = x + 5", "x = 4"], "A horizontal line has constant y.")
H('2.G', 3, "What is the slope of the line x = 7?", "undefined", ["0", "7", "1"], "A vertical line has undefined slope.")
# 2.H linear inequalities
H('2.H', 3, "A graph shows a dashed boundary line with slope 2 and y-intercept 1, and the region below the line is shaded. Which inequality is shown?", "y < 2x + 1", ["y > 2x + 1", "y ≤ 2x + 1", "y ≥ 2x + 1"], "Dashed means strict; below means less than.")
H('2.H', 3, "Sam spends no more than $20 on x pencils at $2 each and y notebooks at $4 each. Which inequality models this?", "2x + 4y ≤ 20", ["2x + 4y ≥ 20", "2x + 4y = 20", "4x + 2y ≤ 20"], "Total cost cannot exceed 20.")
H('2.H', 3, "You need at least $12 from x small bags selling at $3 and y large bags at $2. Which inequality works?", "3x + 2y ≥ 12", ["3x + 2y ≤ 12", "2x + 3y ≥ 12", "3x + 2y > 12 only"], "At least means ≥.")
# 2.I systems from description
H('2.I', 3, "Plan A costs $20 plus $5 per month; Plan B costs $5 plus $10 per month. Which system models the costs y after x months?", "y = 5x + 20 and y = 10x + 5", ["y = 20x + 5 and y = 5x + 10", "y = 5x + 5 and y = 10x + 20", "y = 25x and y = 15x"], "Each plan is start fee plus rate times months.")
H('2.I', 4, "A theater sells 100 tickets: adults at $8, children at $5, for $620 total. Which system models x adults and y children?", "x + y = 100 and 8x + 5y = 620", ["x + y = 620 and 8x + 5y = 100", "x + y = 100 and 5x + 8y = 620", "8x + 5y = 100 and x = y"], "One equation counts tickets, one totals money.")
H('2.I', 3, "A graph shows two lines crossing at (2, 4). Line 1 has slope 1 and Line 2 has slope −1. Which system fits?", "y = x + 2 and y = −x + 6", ["y = x + 4 and y = −x + 2", "y = x + 2 and y = x + 6", "y = 2x and y = −2x + 8"], "Each line passes through (2, 4).")
# 3.A slope
H('3.A', 2, "What is the slope of the line through (1, 2) and (3, 8)?", "3", ["2", "6", "1/3"], "(8 − 2)/(3 − 1) = 3.")
H('3.A', 3, "A table shows x: 0, 2, 4 and y: 1, 5, 9. What is the slope?", "2", ["4", "1", "½"], "y increases 4 when x increases 2.")
H('3.A', 3, "What is the slope of the line 4x + 2y = 8?", "−2", ["4", "2", "−4"], "y = −2x + 4.")
# 3.B rate of change
H('3.B', 2, "A car travels 150 miles in 3 hours. What is the rate of change of distance with respect to time?", "50 miles per hour", ["450 miles per hour", "3 miles per hour", "150 miles per hour"], "150 ÷ 3 = 50.")
H('3.B', 3, "For f(x) = −4x + 30 modeling water left in a tank (gallons) after x minutes, the rate of change is...", "−4 gallons per minute", ["30 gallons per minute", "4 gallons per minute", "26 gallons per minute"], "Slope is −4: it drains 4 gallons each minute.")
H('3.B', 3, "A graph passes through (2, 10) and (6, 22). What is its rate of change?", "3", ["12", "4", "5.5"], "(22 − 10)/(6 − 2) = 3.")
# 3.C graph key features
H('3.C', 2, "What is the y-intercept of y = 2x − 6?", "−6", ["3", "6", "2"], "Set x = 0.")
H('3.C', 3, "What are the intercepts of 3x + 4y = 12?", "x-intercept 4, y-intercept 3", ["x-intercept 3, y-intercept 4", "x-intercept 12, y-intercept 12", "x-intercept −4, y-intercept −3"], "Set y = 0, then x = 0.")
H('3.C', 3, "What is the zero of f(x) = x + 5?", "−5", ["5", "0", "1"], "Solve x + 5 = 0.")
# 3.D graph inequalities
H('3.D', 3, "Which point is a solution of y > 3x − 2?", "(1, 2)", ["(1, 1)", "(2, 4)", "(0, −3)"], "2 > 3(1) − 2 = 1 is true.")
H('3.D', 3, "The graph of y ≥ 2x − 1 has what kind of boundary line and shading?", "solid line, shaded above", ["dashed line, shaded above", "solid line, shaded below", "dashed line, shaded below"], "≥ is solid; greater means above.")
H('3.D', 3, "Testing (0, 0) in y < x + 2 gives a true statement. Which region is shaded?", "the side containing the origin", ["the side not containing the origin", "only the line", "no region"], "Shade the side where the test point is a solution.")
# 3.E transformations of f(x)=x
H('3.E', 2, "How does the graph of g(x) = x + 3 compare to f(x) = x?", "shifted up 3 units", ["shifted right 3 units", "steeper", "reflected across the x-axis"], "Adding d shifts vertically.")
H('3.E', 3, "How does g(x) = 2x compare to f(x) = x?", "steeper (vertical stretch by 2)", ["shifted up 2", "flatter", "shifted left 2"], "Multiplying by a > 1 stretches the graph.")
H('3.E', 3, "How does g(x) = −x compare to f(x) = x?", "reflected across the x-axis", ["shifted down 1", "reflected across the line y = x", "stretched by 2"], "Multiplying by −1 flips vertically.")
# 3.F graph systems
H('3.F', 3, "Lines y = x + 1 and y = −x + 3 intersect at which point?", "(1, 2)", ["(2, 1)", "(0, 1)", "(3, 0)"], "x + 1 = −x + 3 gives x = 1, y = 2.")
H('3.F', 3, "Two lines with the same slope and different y-intercepts have how many solutions as a system?", "none", ["one", "two", "infinitely many"], "They are parallel and never meet.")
H('3.F', 3, "The system y = 2x + 1 and 2y = 4x + 2 has how many solutions?", "infinitely many", ["none", "one", "two"], "The equations describe the same line.")
# 3.G estimate graphically
H('3.G', 3, "Plan A costs 10 + 2x and Plan B costs 4x. On a graph the lines cross at x = 5. What does that mean?", "both plans cost the same at 5 uses", ["Plan A is free at 5", "Plan B costs 10 at x = 0", "the plans never match"], "The intersection is where costs are equal.")
H('3.G', 3, "Graphs of two bike rentals cross near (3, 18). What does the point tell you?", "after about 3 hours both cost about $18", ["both cost $3 after 18 hours", "the rentals never cost the same", "one rental is free"], "Coordinates give the shared time and cost.")
H('3.G', 4, "If two cost lines never intersect on the graph for x ≥ 0, what can you conclude?", "one option is always cheaper", ["both options cost the same", "the costs are equal at 0", "the graph is wrong"], "Parallel lines never cross.")
# 3.H systems of inequalities
H('3.H', 3, "For the system y > x and y < 4, which point is in the solution region?", "(1, 3)", ["(3, 1)", "(1, 5)", "(5, 2)"], "Need y > x and y < 4; (1, 3) works.")
H('3.H', 3, "The solution to a system of two inequalities on a graph is...", "the region where the shaded areas overlap", ["only where the lines cross", "the area outside both regions", "just one of the shaded regions"], "Points must satisfy both inequalities.")
H('3.H', 4, "Is (2, 2) a solution of the system y ≥ x and y ≤ 2x?", "yes", ["no, it fails y ≥ x", "no, it fails y ≤ 2x", "only if x is negative"], "2 ≥ 2 and 2 ≤ 4.")
# 4.A correlation
H('4.A', 3, "A correlation coefficient r = 0.95 means the data show...", "a strong positive linear relationship", ["a strong negative relationship", "no relationship", "a perfect causal link"], "Close to +1 means strong positive.")
H('4.A', 3, "Which correlation coefficient shows the strongest linear relationship?", "−0.92", ["0.40", "−0.15", "0.60"], "The magnitude closest to 1 is strongest.")
H('4.A', 3, "A correlation of r = −0.2 suggests the relationship is...", "weak and negative", ["strong and negative", "weak and positive", "perfect"], "Near 0 is weak; the sign is negative.")
# 4.B causation
H('4.B', 3, "Ice cream sales and swimming accidents both rise in summer. This is evidence of...", "association, not necessarily causation", ["causation: ice cream causes accidents", "no relationship", "negative correlation"], "A hidden factor (hot weather) explains both.")
H('4.B', 3, "Which statement describes causation?", "Increasing one variable directly makes the other change", ["Two variables rise at the same time", "Two variables have the same units", "Both variables are positive"], "Causation means one produces the other.")
H('4.B', 3, "Students who sleep more tend to earn higher grades. What can be concluded?", "the variables are associated; more evidence is needed for causation", ["sleep always causes higher grades", "grades cause sleep", "there is no relationship"], "Association alone does not prove cause.")
# 4.C fit linear
H('4.C', 3, "A line of best fit passes through (0, 2) and (10, 22). Which equation is it?", "y = 2x + 2", ["y = 2x + 10", "y = 22x + 2", "y = x + 2"], "Slope 20/10 = 2; intercept 2.")
H('4.C', 3, "Using y = 2x + 2, predict y when x = 7.", "16", ["14", "9", "18"], "2(7) + 2 = 16.")
H('4.C', 4, "A scatterplot shows a rising trend. The line of best fit is used to...", "estimate values and make predictions", ["prove every point lies on the line", "remove outliers automatically", "change the data"], "Models estimate unseen values.")
# 5.A solve linear equations
H('5.A', 2, "Solve 3(x + 2) = 18.", "x = 4", ["x = 6", "x = 5.33", "x = 8"], "x + 2 = 6.")
H('5.A', 3, "Solve 4(x − 1) = 2x + 6.", "x = 5", ["x = 1", "x = 2.5", "x = 7"], "4x − 4 = 2x + 6 gives 2x = 10.")
H('5.A', 3, "Solve 2x − 5 = 11.", "x = 8", ["x = 3", "x = 6", "x = 16"], "2x = 16.")
# 5.B solve inequalities
H('5.B', 3, "Solve 3x − 4 > 11.", "x > 5", ["x > 15", "x < 5", "x > 7/3"], "3x > 15.")
H('5.B', 3, "Solve −2x ≤ 10.", "x ≥ −5", ["x ≤ −5", "x ≥ 5", "x ≤ 5"], "Dividing by a negative flips the sign.")
H('5.B', 3, "Solve 2(x + 1) < 8.", "x < 3", ["x < 4", "x > 3", "x < 7"], "x + 1 < 4.")
# 5.C solve systems
H('5.C', 3, "Solve: x + y = 10 and x − y = 2.", "(6, 4)", ["(4, 6)", "(5, 5)", "(8, 2)"], "Add the equations: 2x = 12.")
H('5.C', 3, "Solve: y = 2x and x + y = 9.", "(3, 6)", ["(6, 3)", "(2, 4)", "(4, 5)"], "Substitute: 3x = 9.")
H('5.C', 3, "Solve: 2x + y = 7 and x − y = 2.", "(3, 1)", ["(1, 3)", "(2, 3)", "(5, −3)"], "Add the equations: 3x = 9.")
# 6.A quadratic domain and range
H('6.A', 3, "What is the range of y = x² + 1?", "y ≥ 1", ["y ≥ 0", "y ≤ 1", "all real numbers"], "The vertex (0, 1) is the minimum.")
H('6.A', 3, "What is the range of y = −x² + 4?", "y ≤ 4", ["y ≥ 4", "y ≤ 0", "all real numbers"], "Opens down; maximum 4.")
H('6.A', 2, "What is the domain of any quadratic function y = ax² + bx + c?", "all real numbers", ["x ≥ 0", "y ≥ 0", "x ≠ 0"], "Any real x can be squared.")
# 6.B vertex form
H('6.B', 4, "A parabola has vertex (2, 3) and passes through (3, 5). Which is its vertex form?", "y = 2(x − 2)² + 3", ["y = (x − 2)² + 3", "y = 2(x + 2)² + 3", "y = 2(x − 3)² + 2"], "5 = a(1)² + 3 gives a = 2.")
H('6.B', 4, "A parabola has vertex (1, −4) and passes through (0, −3). Which equation fits?", "y = (x − 1)² − 4", ["y = −(x − 1)² − 4", "y = (x + 1)² − 4", "y = 2(x − 1)² − 4"], "−3 = a + (−4) gives a = 1.")
H('6.B', 4, "A parabola has vertex (−1, 2) and passes through (0, 0). Which equation fits?", "y = −2(x + 1)² + 2", ["y = 2(x + 1)² + 2", "y = −2(x − 1)² + 2", "y = −(x + 1)² + 2"], "0 = a + 2 gives a = −2.")
# 6.C write from solutions
H('6.C', 3, "A quadratic has solutions x = 2 and x = −3. Which function could it be?", "y = x² + x − 6", ["y = x² − x − 6", "y = x² + 5x + 6", "y = x² − 5x − 6"], "(x − 2)(x + 3) = x² + x − 6.")
H('6.C', 3, "A graph crosses the x-axis at 1 and 5. Which equation fits?", "y = x² − 6x + 5", ["y = x² + 6x + 5", "y = x² − 4x − 5", "y = x² − 5x + 6"], "(x − 1)(x − 5) = x² − 6x + 5.")
H('6.C', 3, "A parabola has zeros at 0 and 4. Which equation fits?", "y = x² − 4x", ["y = x² + 4x", "y = x² − 4", "y = x² + 4"], "x(x − 4).")
# 7.A graph quadratics
H('7.A', 3, "What is the vertex of y = x² − 4x + 3?", "(2, −1)", ["(−2, −1)", "(2, 1)", "(4, 3)"], "x = 4/2 = 2; y = 4 − 8 + 3 = −1.")
H('7.A', 3, "What is the y-intercept of y = x² + 2x − 8?", "−8", ["8", "2", "−4"], "Set x = 0.")
H('7.A', 3, "What is the axis of symmetry of y = x² − 6x + 5?", "x = 3", ["x = −3", "x = 6", "x = 5"], "x = −b/2a = 6/2.")
# 7.B factors and zeros
H('7.B', 3, "What are the zeros of y = (x − 3)(x + 2)?", "3 and −2", ["−3 and 2", "3 and 2", "−3 and −2"], "Set each factor to 0.")
H('7.B', 3, "A quadratic has zeros 4 and −1. Which linear factors does it have?", "(x − 4) and (x + 1)", ["(x + 4) and (x − 1)", "(x − 4) and (x − 1)", "(x + 4) and (x + 1)"], "Zero r gives factor (x − r).")
H('7.B', 3, "The graph of y = x² − 9 crosses the x-axis at...", "x = −3 and x = 3", ["x = 9 only", "x = 0", "x = 3 only"], "(x − 3)(x + 3) = 0.")
# 7.C transformations of x²
H('7.C', 2, "How does y = x² + 3 differ from y = x²?", "shifted up 3 units", ["shifted left 3 units", "narrower", "reflected across the x-axis"], "Adding d moves it vertically.")
H('7.C', 3, "How does y = (x − 2)² differ from y = x²?", "shifted right 2 units", ["shifted left 2 units", "shifted up 2 units", "wider"], "Replacing x with x − h shifts right by h.")
H('7.C', 3, "How does y = 3x² differ from y = x²?", "narrower, vertical stretch by 3", ["wider", "shifted up 3", "opens downward"], "A larger |a| narrows the parabola.")
# 8.A solve quadratics
H('8.A', 3, "Solve x² − 5x + 6 = 0.", "x = 2 or x = 3", ["x = −2 or x = −3", "x = 1 or x = 6", "x = 5 or x = 1"], "(x − 2)(x − 3).")
H('8.A', 2, "Solve x² = 49.", "x = 7 or x = −7", ["x = 7 only", "x = 24.5", "x = −7 only"], "Take both square roots.")
H('8.A', 4, "Use the quadratic formula to solve x² + 4x + 1 = 0.", "x = −2 ± √3", ["x = 2 ± √3", "x = −4 ± √3", "x = −2 ± √5"], "x = (−4 ± √12)/2.")
# 8.B quadratic regression
H('8.B', 4, "A ball's height is modeled by h = −16t² + 64t. What is its maximum height?", "64 feet", ["32 feet", "128 feet", "16 feet"], "Vertex at t = 2: −64 + 128 = 64.")
H('8.B', 3, "For h = −16t² + 64t, when does the ball return to the ground?", "t = 4 seconds", ["t = 2 seconds", "t = 8 seconds", "t = 64 seconds"], "−16t(t − 4) = 0.")
H('8.B', 3, "A quadratic model of a thrown ball gives the same height at two different times. This happens because the parabola is symmetric about its...", "axis of symmetry", ["y-intercept", "horizontal asymptote", "slope"], "Equal heights occur at equal distances from the vertex.")
# 9.A exponential domain/range
H('9.A', 3, "What is the range of f(x) = 3·2ˣ?", "y > 0", ["y ≥ 0", "y ≥ 3", "all real numbers"], "Exponentials with a > 0 are always positive.")
H('9.A', 3, "What is the domain of f(x) = 5·(½)ˣ?", "all real numbers", ["x > 0", "x ≥ 0", "x ≠ 0"], "Any real exponent is allowed.")
H('9.A', 4, "What is the range of f(x) = −2ˣ?", "y < 0", ["y > 0", "y ≤ 0", "y ≥ −2"], "Reflecting gives always negative values.")
# 9.B meaning of a and b
H('9.B', 3, "In f(x) = 500(1.05)ˣ, what does 1.05 represent?", "a growth factor of 5% per period", ["an initial amount", "a decay factor", "the number of periods"], "b = 1 + rate.")
H('9.B', 3, "In f(x) = 80(0.9)ˣ, what does 80 represent?", "the starting amount", ["the decay rate", "the number of years", "the growth factor"], "a is the value at x = 0.")
H('9.B', 3, "In f(x) = 200(0.85)ˣ, the quantity is changing by...", "15% decay each period", ["85% growth each period", "15% growth each period", "200% decay"], "1 − 0.15 = 0.85.")
# 9.C write exponential
H('9.C', 3, "A culture starts with 200 cells and doubles every hour. Which function gives cells after x hours?", "f(x) = 200·2ˣ", ["f(x) = 2·200ˣ", "f(x) = 200 + 2x", "f(x) = 400x"], "Initial amount times 2 to the x.")
H('9.C', 3, "A $1000 value declines by 20% each year. Which function models it?", "f(x) = 1000(0.8)ˣ", ["f(x) = 1000(0.2)ˣ", "f(x) = 1000(1.2)ˣ", "f(x) = 800x"], "Each year keeps 80%.")
H('9.C', 3, "A population of 50 triples each year. Which function models it?", "f(x) = 50·3ˣ", ["f(x) = 3·50ˣ", "f(x) = 50 + 3x", "f(x) = 150x"], "Growth factor 3.")
# 9.D graph exponential
H('9.D', 3, "What is the y-intercept of f(x) = 3·2ˣ?", "3", ["2", "6", "1"], "At x = 0, 3·1 = 3.")
H('9.D', 3, "What is the horizontal asymptote of f(x) = 4·(½)ˣ?", "y = 0", ["y = 4", "y = ½", "x = 0"], "The graph approaches the x-axis.")
H('9.D', 3, "For f(x) = a·bˣ with a > 0, the graph shows growth when...", "b > 1", ["0 < b < 1", "b = 0", "b < 0"], "A factor above 1 increases.")
# 9.E exponential regression
H('9.E', 4, "Data points are (0, 5), (1, 10), (2, 20). Which model fits?", "f(x) = 5·2ˣ", ["f(x) = 5x + 5", "f(x) = 5 + 10x", "f(x) = 2·5ˣ"], "Each step doubles.")
H('9.E', 3, "Using f(x) = 5·2ˣ, predict f(4).", "80", ["40", "20", "160"], "5·16 = 80.")
H('9.E', 4, "Exponential models are best for data in which...", "the output changes by a constant percent", ["the output changes by a constant amount", "the output stays the same", "there are no patterns"], "Constant ratio indicates exponential.")
# 10.A add/subtract polynomials
H('10.A', 3, "Add (3x² + 2x − 1) + (x² − 5x + 4).", "4x² − 3x + 3", ["4x² + 7x + 3", "3x² − 3x + 3", "4x² − 3x − 5"], "Combine like terms.")
H('10.A', 3, "Subtract (5x + 3) − (2x − 7).", "3x + 10", ["3x − 4", "7x − 4", "3x − 10"], "Distribute the negative.")
H('10.A', 4, "Subtract (4x² − x) − (x² + 2x − 3).", "3x² − 3x + 3", ["3x² + x − 3", "3x² + 3x + 3", "5x² − x − 3"], "−(2x) − x = −3x and +3.")
# 10.B multiply
H('10.B', 3, "Multiply (x + 3)(x + 5).", "x² + 8x + 15", ["x² + 15x + 8", "x² + 8x + 8", "x² + 2x + 15"], "FOIL.")
H('10.B', 3, "Multiply (2x − 1)(x + 4).", "2x² + 7x − 4", ["2x² − 4", "2x² + 9x − 4", "2x² + 7x + 4"], "2x² + 8x − x − 4.")
H('10.B', 3, "Expand (x − 6)².", "x² − 12x + 36", ["x² − 36", "x² + 36", "x² − 6x + 36"], "Square of a binomial.")
# 10.C divide
H('10.C', 3, "Divide (x² + 5x + 6) ÷ (x + 2).", "x + 3", ["x + 2", "x + 6", "x² + 3"], "(x + 2)(x + 3).")
H('10.C', 4, "Divide (2x² − x − 6) ÷ (x − 2).", "2x + 3", ["2x − 3", "x + 3", "2x + 6"], "(x − 2)(2x + 3).")
H('10.C', 3, "Divide (x² − 9) ÷ (x + 3).", "x − 3", ["x + 3", "x² − 3", "x − 9"], "Difference of squares.")
# 10.D distributive property
H('10.D', 2, "Rewrite 3(x + 4) using the distributive property.", "3x + 12", ["3x + 4", "x + 12", "3x + 7"], "Multiply each term by 3.")
H('10.D', 3, "Rewrite x(2x − 5).", "2x² − 5x", ["2x − 5x", "2x² − 5", "2x² + 5x"], "x·2x = 2x².")
H('10.D', 3, "Rewrite −2(x² − 3x + 1).", "−2x² + 6x − 2", ["−2x² − 6x − 2", "−2x² + 6x + 1", "2x² − 6x + 2"], "Distribute −2 to each term.")
# 10.E factor trinomials
H('10.E', 3, "Factor x² + 7x + 12.", "(x + 3)(x + 4)", ["(x + 2)(x + 6)", "(x + 1)(x + 12)", "(x − 3)(x − 4)"], "3 and 4 add to 7, multiply to 12.")
H('10.E', 3, "Factor x² − 10x + 25.", "(x − 5)²", ["(x + 5)²", "(x − 5)(x + 5)", "(x − 25)(x − 1)"], "Perfect square trinomial.")
H('10.E', 4, "Factor 2x² + 5x + 3.", "(2x + 3)(x + 1)", ["(2x + 1)(x + 3)", "(2x − 3)(x − 1)", "(x + 5)(2x + 3)"], "2x² + 2x + 3x + 3.")
# 10.F difference of squares
H('10.F', 3, "Factor x² − 49.", "(x − 7)(x + 7)", ["(x − 7)²", "(x + 7)²", "(x − 49)(x + 1)"], "a² − b² = (a − b)(a + b).")
H('10.F', 3, "Factor 4x² − 25.", "(2x − 5)(2x + 5)", ["(4x − 5)(x + 5)", "(2x − 5)²", "(2x + 25)(2x − 1)"], "Both terms are squares.")
H('10.F', 3, "Which binomial cannot be factored over the real numbers as a difference of squares?", "x² + 16", ["x² − 16", "9x² − 1", "25 − x²"], "A sum of squares is not a difference.")
# 11.A radicals
H('11.A', 3, "Simplify √50.", "5√2", ["2√5", "10√5", "25√2"], "√(25·2).")
H('11.A', 3, "Simplify √72.", "6√2", ["8√3", "36√2", "2√18"], "√(36·2).")
H('11.A', 3, "Simplify √12 · √3.", "6", ["√15", "36", "3√2"], "√36 = 6.")
# 11.B exponent laws
H('11.B', 2, "Simplify x³ · x⁴.", "x⁷", ["x¹²", "x", "2x⁷"], "Add exponents.")
H('11.B', 3, "Simplify (2x³)².", "4x⁶", ["2x⁶", "4x⁵", "2x⁹"], "Square the coefficient and multiply exponents.")
H('11.B', 3, "Evaluate 27^(2/3).", "9", ["18", "3", "81"], "(∛27)² = 3² = 9.")
# 12.A function or not
H('12.A', 2, "Which relation is NOT a function?", "{(1, 2), (2, 3), (1, 5)}", ["{(1, 2), (2, 3), (3, 5)}", "{(0, 1), (1, 1), (2, 1)}", "{(5, 0), (6, 1), (7, 2)}"], "Input 1 has two outputs.")
H('12.A', 2, "The vertical line test is used to decide whether a graph...", "represents a function", ["has a slope", "is linear", "has an intercept"], "A vertical line crossing twice means not a function.")
H('12.A', 3, "A table shows x: 1, 2, 2, 3 and y: 4, 5, 6, 7. Is it a function?", "no, because x = 2 has two outputs", ["yes, every y is different", "yes, x is increasing", "no, because 7 is odd"], "Each input needs exactly one output.")
# 12.B evaluate functions
H('12.B', 2, "If f(x) = 2x + 3, what is f(4)?", "11", ["14", "9", "8"], "2(4) + 3.")
H('12.B', 3, "If f(x) = x² − 1, what is f(−3)?", "8", ["−10", "10", "−8"], "9 − 1.")
H('12.B', 2, "If g(x) = 3x − 2, what is g(5)?", "13", ["17", "3", "10"], "3(5) − 2.")
# 12.C terms of sequences
H('12.C', 2, "An arithmetic sequence starts at 5 with common difference 3. What is the 4th term?", "14", ["17", "12", "20"], "5, 8, 11, 14.")
H('12.C', 3, "A geometric sequence starts at 2 with common ratio 3. What is the 4th term?", "54", ["24", "18", "162"], "2, 6, 18, 54.")
H('12.C', 3, "If a₁ = 1 and aₙ = aₙ₋₁ + 4, what is a₅?", "17", ["20", "13", "21"], "1, 5, 9, 13, 17.")
# 12.D nth term
H('12.D', 3, "Which formula gives the nth term of 4, 7, 10, 13, ...?", "aₙ = 3n + 1", ["aₙ = 4n + 3", "aₙ = 3n + 4", "aₙ = n + 3"], "First term 4, difference 3.")
H('12.D', 4, "Which formula gives the nth term of 2, 6, 18, 54, ...?", "aₙ = 2·3ⁿ⁻¹", ["aₙ = 3·2ⁿ⁻¹", "aₙ = 2 + 3n", "aₙ = 2·3ⁿ"], "Ratio 3 starting at 2.")
H('12.D', 3, "Which formula gives the nth term of 20, 15, 10, 5, ...?", "aₙ = −5n + 25", ["aₙ = 5n + 20", "aₙ = −5n + 20", "aₙ = 20 − 5ⁿ"], "20 = −5 + 25.")
# 12.E literal equations
H('12.E', 2, "Solve A = lw for w.", "w = A/l", ["w = Al", "w = l/A", "w = A − l"], "Divide both sides by l.")
H('12.E', 3, "Solve y = mx + b for x.", "x = (y − b)/m", ["x = y − b − m", "x = m(y − b)", "x = (y + b)/m"], "Subtract b, then divide by m.")
H('12.E', 3, "Solve P = 2l + 2w for l.", "l = (P − 2w)/2", ["l = P − 2w", "l = (P + 2w)/2", "l = P/2 + 2w"], "Subtract 2w, divide by 2.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_alg1.jsonl'))

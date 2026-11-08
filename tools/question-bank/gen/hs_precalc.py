#!/usr/bin/env python3
"""High school Precalculus (TEKS 111.42.c). Original questions. Strand 1 (process) skipped."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('111.42.c.', 989, own='hs_precalc.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A composition
H('2.A', 3, "If f(x) = 2x + 1 and g(x) = x², what is f(g(3))?", "19", ["49", "13", "36"], "g(3) = 9, then f(9) = 2(9) + 1 = 19.")
H('2.A', 3, "If f(x) = x + 4 and g(x) = 3x, what is g(f(2))?", "18", ["10", "14", "12"], "f(2) = 6, then g(6) = 18.")
H('2.A', 3, "A store takes 20% off a $50 item and then a $5 coupon is applied. If d(x) = 0.8x and c(x) = x − 5, which expression gives the final price?", "c(d(50))", ["d(c(50))", "d(50) + c(50)", "d(50) · c(50)"], "The discount is applied first, then the coupon.")

# 2.B not commutative
H('2.B', 3, "If f(x) = x + 1 and g(x) = 2x, what is f(g(x))?", "2x + 1", ["2x + 2", "2x", "x + 2"], "f(2x) = 2x + 1.")
H('2.B', 3, "If f(x) = x + 1 and g(x) = 2x, what is g(f(x))?", "2x + 2", ["2x + 1", "2x", "x + 2"], "g(x + 1) = 2(x + 1).")
H('2.B', 3, "Since f(g(x)) = 2x + 1 and g(f(x)) = 2x + 2 for f(x) = x + 1 and g(x) = 2x, what does this show about composition?", "it is not always commutative", ["it is always commutative", "the functions are inverses", "the functions are equal"], "Changing the order changed the result.")

# 2.C decomposition
H('2.C', 3, "Which pair of functions f and g gives h(x) = (x + 3)² when h(x) = f(g(x))?", "g(x) = x + 3 and f(x) = x²", ["g(x) = x² and f(x) = x + 3", "g(x) = 3x and f(x) = x²", "g(x) = x² + 3 and f(x) = x"], "The inner function adds 3, then the outer function squares.")
H('2.C', 4, "Which pair gives h(x) = √(5x − 1) as f(g(x))?", "g(x) = 5x − 1 and f(x) = √x", ["g(x) = √x and f(x) = 5x − 1", "g(x) = 5x and f(x) = √(x − 1)", "g(x) = x − 1 and f(x) = √5x"], "Do the inside first, then take the square root.")
H('2.C', 3, "If h(x) = 1/(x − 2), which choice writes h as a composition f(g(x))?", "g(x) = x − 2 and f(x) = 1/x", ["g(x) = 1/x and f(x) = x − 2", "g(x) = x and f(x) = 1/2", "g(x) = 2x and f(x) = 1/x"], "Subtract 2 first, then take the reciprocal.")

# 2.D even and odd
H('2.D', 2, "The graph of an even function has what kind of symmetry?", "symmetry about the y-axis", ["symmetry about the origin", "symmetry about the x-axis", "no symmetry"], "f(−x) = f(x).")
H('2.D', 2, "The graph of an odd function has what kind of symmetry?", "symmetry about the origin", ["symmetry about the y-axis", "symmetry about the x-axis", "symmetry about y = x"], "f(−x) = −f(x).")
H('2.D', 3, "Which function is odd?", "f(x) = x³", ["f(x) = x²", "f(x) = |x|", "f(x) = x⁴ + 1"], "(−x)³ = −x³.")
H('2.D', 3, "Which function is even?", "f(x) = cos x", ["f(x) = sin x", "f(x) = x³", "f(x) = tan x"], "cos(−x) = cos x.")

# 2.E inverse
H('2.E', 3, "What is the inverse of f(x) = 3x − 6?", "f⁻¹(x) = (x + 6)/3", ["f⁻¹(x) = (x − 6)/3", "f⁻¹(x) = 3x + 6", "f⁻¹(x) = x/3 − 6"], "Swap x and y, then solve for y.")
H('2.E', 3, "A function f has an inverse if and only if it is what?", "one-to-one", ["even", "periodic", "constant"], "Each output must come from exactly one input.")
H('2.E', 4, "To get an inverse for f(x) = x², what restriction on the domain works?", "x ≥ 0", ["all real numbers", "x ≠ 0", "x ≤ 5 and x ≥ −5"], "A one-to-one piece is needed.")
H('2.E', 3, "If f(2) = 7, what is f⁻¹(7)?", "2", ["7", "5", "1/7"], "Inverses swap inputs and outputs.")

# 2.F graph function families
H('2.F', 3, "What is the end behavior of y = 2ˣ as x → −∞?", "y approaches 0", ["y approaches ∞", "y approaches −∞", "y approaches 2"], "The graph has a horizontal asymptote at y = 0.")
H('2.F', 3, "What is the domain of y = log₂(x)?", "x > 0", ["all real numbers", "x ≥ 0", "x < 0"], "Only positive inputs have logarithms.")
H('2.F', 3, "Which function has a graph with a vertical asymptote at x = 3?", "y = 1/(x − 3)", ["y = x − 3", "y = (x − 3)²", "y = 3x"], "The denominator is zero at x = 3.")
H('2.F', 3, "What is the y-intercept of y = 4ˣ?", "(0, 1)", ["(0, 0)", "(0, 4)", "(1, 0)"], "4⁰ = 1.")

# 2.G transformations
H('2.G', 3, "How does the graph of y = (x − 2)² + 3 compare with the graph of y = x²?", "shifted right 2 and up 3", ["shifted left 2 and up 3", "shifted right 3 and up 2", "shifted left 2 and down 3"], "x − 2 shifts right; +3 shifts up.")
H('2.G', 3, "What transformation changes y = f(x) into y = −f(x)?", "a reflection across the x-axis", ["a reflection across the y-axis", "a shift down", "a vertical stretch"], "All outputs change sign.")
H('2.G', 3, "What transformation changes y = f(x) into y = f(2x)?", "a horizontal compression by a factor of 1/2", ["a horizontal stretch by a factor of 2", "a vertical stretch by a factor of 2", "a shift left 2"], "Inputs are doubled, so the graph squeezes horizontally.")
H('2.G', 4, "The graph of y = 3 sin x is the graph of y = sin x after what?", "a vertical stretch by a factor of 3", ["a horizontal stretch by a factor of 3", "a shift up 3", "a shift right 3"], "The amplitude becomes 3.")

# 2.H arcsin arccos
H('2.H', 3, "What is the range of y = arcsin x?", "[−π/2, π/2]", ["[0, π]", "[−1, 1]", "(−∞, ∞)"], "It is restricted to make sine one-to-one.")
H('2.H', 3, "What is the domain of y = arccos x?", "[−1, 1]", ["[0, π]", "(−∞, ∞)", "[−π/2, π/2]"], "Cosine only outputs values from −1 to 1.")
H('2.H', 3, "What is the range of y = arccos x?", "[0, π]", ["[−π/2, π/2]", "[−1, 1]", "(0, ∞)"], "It is restricted to make cosine one-to-one.")

# 2.I key features
H('2.I', 3, "How many x-intercepts can a quadratic function have at most?", "2", ["1", "3", "4"], "A degree-2 polynomial has at most 2 real zeros.")
H('2.I', 3, "What is the period of y = sin x?", "2π", ["π", "π/2", "1"], "The sine graph repeats every 2π.")
H('2.I', 3, "What is the amplitude of y = −4 cos x?", "4", ["−4", "1", "8"], "Amplitude is the absolute value of the coefficient.")
H('2.I', 4, "For y = 2ˣ − 5, what is the horizontal asymptote?", "y = −5", ["y = 0", "y = 5", "y = 2"], "The −5 shifts the asymptote down 5.")

# 2.J end behavior
H('2.J', 3, "What is the end behavior of f(x) = −x³ as x → ∞?", "f(x) → −∞", ["f(x) → ∞", "f(x) → 0", "f(x) → −1"], "The leading term dominates and has a negative coefficient.")
H('2.J', 3, "What is the end behavior of f(x) = x⁴ as x → −∞?", "f(x) → ∞", ["f(x) → −∞", "f(x) → 0", "f(x) → 4"], "An even power with a positive coefficient rises on both ends.")
H('2.J', 4, "As x → ∞, what does f(x) = (3x + 1)/(x − 4) approach?", "3", ["0", "∞", "−4"], "Degrees are equal, so divide the leading coefficients.")

# 2.K rational functions
H('2.K', 3, "What is the vertical asymptote of f(x) = 5/(x + 2)?", "x = −2", ["x = 2", "y = 0", "x = 5"], "The denominator is zero at x = −2.")
H('2.K', 3, "What is the horizontal asymptote of f(x) = 4x/(x² + 1)?", "y = 0", ["y = 4", "y = 1", "x = 0"], "The denominator has a higher degree.")
H('2.K', 4, "As x approaches 1 from the right, what does f(x) = 1/(x − 1) do?", "it approaches ∞", ["it approaches −∞", "it approaches 0", "it approaches 1"], "The denominator is a small positive number.")

# 2.L discontinuities
H('2.L', 3, "What kind of discontinuity does f(x) = (x² − 4)/(x − 2) have at x = 2?", "removable (a hole)", ["a vertical asymptote", "a jump", "none"], "The factor x − 2 cancels.")
H('2.L', 3, "What kind of discontinuity does f(x) = 1/x have at x = 0?", "infinite (a vertical asymptote)", ["removable", "a jump", "none"], "The function grows without bound.")
H('2.L', 3, "A piecewise function jumps from y = 1 to y = 3 at x = 2. What is this discontinuity called?", "a jump discontinuity", ["a removable discontinuity", "an infinite discontinuity", "a continuous point"], "The one-sided limits are different finite numbers.")

# 2.M one-sided behavior
H('2.M', 4, "For f(x) = 1/x, what happens as x approaches 0 from the left?", "f(x) → −∞", ["f(x) → ∞", "f(x) → 0", "f(x) → 1"], "Negative inputs give large negative outputs.")
H('2.M', 4, "For a function with a jump from 1 to 3 at x = 2, what is the right-sided value as x approaches 2?", "3", ["1", "2", "does not exist"], "The right-hand limit is the value approached from larger x.")
H('2.M', 3, "If the left-sided and right-sided behavior at x = a are both approaching the same finite value, the function has what at x = a?", "a limit", ["a vertical asymptote", "a jump", "a corner only"], "The one-sided limits agree.")

# 2.N modeling
H('2.N', 3, "A population doubles every 5 years. Which type of function best models it?", "exponential", ["linear", "quadratic", "logarithmic"], "Constant percent growth means exponential.")
H('2.N', 3, "Sound intensity levels in decibels are measured on a scale based on which function?", "logarithmic", ["linear", "quadratic", "exponential growth only"], "Each 10 dB step means 10 times more intensity.")
H('2.N', 4, "The height of a ball thrown upward over time is best modeled by what type of function?", "quadratic", ["linear", "exponential", "logarithmic"], "Gravity produces a parabola.")

# 2.O sinusoidal
H('2.O', 4, "A Ferris wheel has a radius of 20 m, its center is 22 m above ground, and it completes one turn every 8 minutes. What is the midline of a sinusoidal model of the height?", "22 m", ["20 m", "42 m", "8 m"], "The midline is at the center height.")
H('2.O', 4, "For the same Ferris wheel, what is the amplitude of the height model?", "20 m", ["22 m", "8 m", "40 m"], "The amplitude equals the radius.")
H('2.O', 4, "The tide height is modeled by h = 3 sin(πt/6) + 5, where t is in hours. What is the period?", "12 hours", ["6 hours", "3 hours", "5 hours"], "Period = 2π ÷ (π/6) = 12.")

# 2.P special angles
H('2.P', 2, "What is sin 30°?", "1/2", ["√3/2", "√2/2", "1"], "A special-angle value.")
H('2.P', 3, "What is cos(π/3)?", "1/2", ["√3/2", "√2/2", "0"], "π/3 = 60°, and cos 60° = 1/2.")
H('2.P', 3, "What is tan 45°?", "1", ["0", "√3", "undefined"], "sin 45° = cos 45°.")
H('2.P', 3, "What is sin(π/2)?", "1", ["0", "1/2", "√2/2"], "The point on the unit circle at π/2 is (0, 1).")

# 3.A parametric graphs
H('3.A', 3, "For x = t and y = t² with t from −2 to 2, what shape does the graph trace?", "a parabola", ["a line", "a circle", "a hyperbola"], "Eliminating t gives y = x².")
H('3.A', 3, "For x = 2t and y = 3t, what shape does the graph trace?", "a line", ["a parabola", "a circle", "an ellipse"], "Both coordinates are linear in t.")
H('3.A', 3, "If x = cos t and y = sin t for 0 ≤ t ≤ 2π, what does the graph trace?", "a unit circle", ["a parabola", "a line", "a sine wave"], "x² + y² = 1.")

# 3.B parametric conversion
H('3.B', 3, "Eliminate the parameter from x = t + 1 and y = 2t. Which rectangular equation results?", "y = 2x − 2", ["y = 2x + 2", "y = x − 1", "y = 2x"], "t = x − 1, so y = 2(x − 1).")
H('3.B', 3, "Which pair of parametric equations represents y = x² + 1?", "x = t, y = t² + 1", ["x = t², y = t", "x = t + 1, y = t²", "x = 1, y = t"], "Let x equal the parameter.")
H('3.B', 4, "Which rectangular equation matches x = 3 cos t and y = 3 sin t?", "x² + y² = 9", ["x² + y² = 3", "x + y = 3", "x² − y² = 9"], "cos²t + sin²t = 1.")

# 3.C parametric modeling
H('3.C', 4, "A ball is launched with horizontal speed 10 m/s. Which parametric equation for x(t) gives its horizontal position (ignoring air resistance)?", "x = 10t", ["x = 10t²", "x = t + 10", "x = 10/t"], "Constant horizontal speed gives distance equal to speed times time.")
H('3.C', 4, "Why are parametric equations helpful for modeling projectile motion?", "they let x and y each depend on time", ["they make the path a straight line", "they remove gravity", "they ignore time"], "Position components can be written separately in terms of t.")
H('3.C', 3, "A boat moves so that x = 4t and y = 3t. How far from the start is it after 2 hours?", "10", ["14", "7", "5"], "At t = 2, (8, 6) and the distance is √(64 + 36) = 10.")

# 3.D polar coordinates
H('3.D', 3, "Convert the polar point (2, π/2) to rectangular coordinates.", "(0, 2)", ["(2, 0)", "(0, 0)", "(−2, 0)"], "x = 2 cos(π/2) = 0 and y = 2 sin(π/2) = 2.")
H('3.D', 3, "Convert the rectangular point (3, 3) to polar form with r > 0.", "(3√2, π/4)", ["(3, π/4)", "(6, π/4)", "(3√2, π/2)"], "r = √18 and the angle is 45°.")
H('3.D', 3, "What is r for the rectangular point (−5, 0)?", "5", ["−5", "0", "25"], "r is the distance from the origin.")

# 3.E polar graphs
H('3.E', 3, "What is the graph of r = 4 in polar coordinates?", "a circle of radius 4 centered at the origin", ["a line through the origin", "a spiral", "a parabola"], "Every point is 4 units from the origin.")
H('3.E', 3, "What is the graph of θ = π/4 in polar coordinates?", "a line through the origin", ["a circle", "a spiral", "a parabola"], "All points lie along a fixed angle.")
H('3.E', 4, "How many petals does r = 3 cos(2θ) have?", "4", ["2", "3", "6"], "A rose curve with an even n has 2n petals.")

# 3.F conic sections
H('3.F', 2, "If a plane cuts a double-napped cone perpendicular to its axis, what shape forms?", "a circle", ["a parabola", "an ellipse that is not a circle", "a hyperbola"], "A perpendicular cut gives a circle.")
H('3.F', 3, "If a plane cuts both nappes of a double-napped cone, what shape forms?", "a hyperbola", ["a circle", "an ellipse", "a parabola"], "Both pieces of the cone are cut.")
H('3.F', 3, "If a plane is parallel to the side of the cone, what shape forms?", "a parabola", ["a circle", "an ellipse", "a hyperbola"], "It cuts only one nappe without closing.")

# 3.G locus definitions
H('3.G', 3, "Which conic is the locus of points whose distances to two fixed points add up to a constant?", "an ellipse", ["a parabola", "a hyperbola", "a circle"], "The fixed points are foci.")
H('3.G', 3, "Which conic is the locus of points equally distant from a focus and a line?", "a parabola", ["an ellipse", "a hyperbola", "a circle"], "The line is the directrix.")
H('3.G', 4, "Which conic is the locus of points whose distances to two fixed points differ by a constant?", "a hyperbola", ["an ellipse", "a parabola", "a circle"], "The absolute difference of the distances is constant.")

# 3.H ellipse
H('3.H', 3, "An ellipse has center (1, 2), horizontal semi-axis 5 and vertical semi-axis 3. Which equation matches?", "(x − 1)²/25 + (y − 2)²/9 = 1", ["(x − 1)²/9 + (y − 2)²/25 = 1", "(x + 1)²/25 + (y + 2)²/9 = 1", "(x − 1)²/5 + (y − 2)²/3 = 1"], "The squares of the semi-axes go in the denominators.")
H('3.H', 3, "What are the coordinates of the center of the ellipse (x + 3)²/16 + (y − 4)²/4 = 1?", "(−3, 4)", ["(3, −4)", "(3, 4)", "(−3, −4)"], "Read the signs inside the parentheses and flip them.")
H('3.H', 4, "For (x)²/25 + (y)²/9 = 1, how far from the center are the foci?", "4", ["5", "3", "8"], "c = √(25 − 9) = 4.")

# 3.I hyperbola
H('3.I', 3, "Which equation is a hyperbola?", "x²/9 − y²/4 = 1", ["x²/9 + y²/4 = 1", "x² + y² = 9", "y = x²"], "A minus sign between the squared terms gives a hyperbola.")
H('3.I', 3, "What are the coordinates of the center of the hyperbola (x − 2)²/9 − (y + 1)²/4 = 1?", "(2, −1)", ["(−2, 1)", "(2, 1)", "(−2, −1)"], "Take the opposite signs of the shifts.")
H('3.I', 4, "A hyperbola has a = 3 and b = 4 with a horizontal transverse axis through the origin. What are the slopes of its asymptotes?", "±4/3", ["±3/4", "±1", "±12"], "The slopes are ±b/a.")

# 4.A unit circle
H('4.A', 3, "On the unit circle, what are the coordinates of the point at angle π?", "(−1, 0)", ["(1, 0)", "(0, −1)", "(0, 1)"], "cos π = −1 and sin π = 0.")
H('4.A', 3, "What is the period of the cosine function in radians?", "2π", ["π", "π/2", "4π"], "A full turn around the unit circle.")
H('4.A', 3, "What is cos(3π/2)?", "0", ["1", "−1", "undefined"], "The point is (0, −1).")

# 4.B degrees and radians
H('4.B', 2, "How many radians equal 180°?", "π", ["2π", "π/2", "1"], "A half turn is π radians.")
H('4.B', 3, "Convert 135° to radians.", "3π/4", ["π/4", "5π/4", "2π/3"], "135 × π/180.")
H('4.B', 3, "Convert 5π/6 radians to degrees.", "150°", ["120°", "135°", "165°"], "(5π/6) × (180/π).")

# 4.C coterminal and reference angles
H('4.C', 3, "Which angle is coterminal with 60°?", "420°", ["240°", "120°", "300°"], "Add 360°.")
H('4.C', 3, "What is the reference angle for 210°?", "30°", ["60°", "210°", "150°"], "210° − 180° = 30°.")
H('4.C', 3, "What is the reference angle for 7π/6?", "π/6", ["π/3", "7π/6", "5π/6"], "7π/6 − π = π/6.")

# 4.D rotation modeling
H('4.D', 3, "A wheel turns 3 full revolutions counterclockwise. What is the angle measure in radians?", "6π", ["3π", "3", "12π"], "Each revolution is 2π.")
H('4.D', 3, "A wheel turns 90° clockwise. What is the angle in radians, using the standard convention?", "−π/2", ["π/2", "−π", "π"], "Clockwise rotation is negative.")
H('4.D', 4, "A point on a circle of radius 5 rotates through an angle of 2 radians. What arc length does it travel?", "10", ["2.5", "7", "5"], "s = rθ.")

# 4.E trig ratios
H('4.E', 3, "In a right triangle, the side opposite angle A is 3 and the hypotenuse is 5. What is sin A?", "3/5", ["4/5", "3/4", "5/3"], "sin = opposite ÷ hypotenuse.")
H('4.E', 3, "If sin θ = 3/5 and θ is in the first quadrant, what is cos θ?", "4/5", ["3/4", "5/3", "3/5"], "A 3-4-5 triangle.")
H('4.E', 4, "If tan θ = 1 and 0 < θ < π/2, what is θ?", "π/4", ["π/3", "π/6", "π/2"], "Opposite equals adjacent.")

# 4.F bearings
H('4.F', 3, "A ship sails 10 km on a bearing of 090°. In which direction is it heading?", "due east", ["due north", "due south", "due west"], "Bearings are measured clockwise from north.")
H('4.F', 4, "A plane flies 100 km on a bearing of 030°. About how far north has it traveled?", "86.6 km", ["50 km", "100 km", "173 km"], "100 cos 30°.")
H('4.F', 4, "A hiker walks 5 km north and then 12 km east. How far is the hiker from the start?", "13 km", ["17 km", "7 km", "60 km"], "√(25 + 144) = 13.")

# 4.G Law of Sines
H('4.G', 3, "Which equation expresses the Law of Sines?", "a/sin A = b/sin B", ["a² = b² + c²", "a sin A = b cos B", "a + b = sin A + sin B"], "Sides are proportional to the sines of opposite angles.")
H('4.G', 4, "In triangle ABC, A = 30°, B = 45° and a = 10. What is b?", "10√2", ["5√2", "20", "10"], "b = 10 sin45° ÷ sin30° = 10√2.")
H('4.G', 3, "The Law of Sines is most useful when you know what?", "two angles and a side", ["three sides only", "only one angle", "only the area"], "Such as AAS or ASA.")

# 4.H Law of Cosines
H('4.H', 3, "Which equation is the Law of Cosines?", "c² = a² + b² − 2ab cos C", ["c² = a² + b²", "c = a sin C", "c² = a² − b²"], "It generalizes the Pythagorean theorem.")
H('4.H', 4, "In triangle ABC, a = 3, b = 4 and C = 90°. What is c?", "5", ["7", "1", "12"], "cos 90° = 0, so c² = 9 + 16.")
H('4.H', 3, "Which information lets you start with the Law of Cosines?", "three sides", ["one side and one angle", "only two angles", "only one side"], "SSS or SAS cases.")

# 4.I vectors
H('4.I', 2, "What two things does a vector have?", "magnitude and direction", ["only magnitude", "only direction", "mass and charge"], "A vector is more than a size.")
H('4.I', 3, "What is the magnitude of the vector <3, 4>?", "5", ["7", "1", "12"], "√(9 + 16).")
H('4.I', 3, "What is the magnitude of <−5, 12>?", "13", ["7", "17", "169"], "√(25 + 144).")
H('4.I', 3, "A plane flies at 200 mph heading east. Which vector models its velocity?", "<200, 0>", ["<0, 200>", "<−200, 0>", "<200, 200>"], "East is the positive x direction.")

# 4.J vector operations geometrically/symbolically
H('4.J', 3, "What is <2, 3> + <4, −1>?", "<6, 2>", ["<2, 4>", "<8, 3>", "<6, 4>"], "Add components.")
H('4.J', 3, "What is 3 · <1, −2>?", "<3, −6>", ["<4, 1>", "<3, −2>", "<1, −6>"], "Multiply each component by 3.")
H('4.J', 4, "Geometrically, adding two vectors with the tip-to-tail method gives a vector from where to where?", "from the tail of the first to the tip of the second", ["from the tip of the first to the tail of the second", "from the tail of the first to the tail of the second", "from the tip of the first to the tip of the second"], "The resultant closes the triangle.")

# 4.K vector applications
H('4.K', 4, "A boat heads east at 6 m/s while a current flows north at 8 m/s. What is the boat's speed relative to the ground?", "10 m/s", ["14 m/s", "2 m/s", "48 m/s"], "√(36 + 64).")
H('4.K', 3, "Two forces <3, 0> N and <0, 4> N act on an object. What is the resultant force?", "<3, 4> N", ["<7, 0> N", "<0, 7> N", "<12, 0> N"], "Add the vectors.")
H('4.K', 4, "If a force vector is doubled, what happens to its direction and magnitude?", "the direction stays the same and the magnitude doubles", ["the direction doubles", "the direction reverses", "the magnitude stays the same"], "A positive scalar multiple keeps the direction.")

# 5.A sigma notation and series
H('5.A', 3, "What is Σ (k = 1 to 4) of k?", "10", ["4", "24", "16"], "1 + 2 + 3 + 4.")
H('5.A', 3, "What is Σ (k = 1 to 3) of 2k?", "12", ["6", "9", "18"], "2 + 4 + 6.")
H('5.A', 4, "What is the sum of the infinite geometric series 8 + 4 + 2 + 1 + ...?", "16", ["15", "∞", "12"], "S = a ÷ (1 − r) = 8 ÷ (1/2).")

# 5.B recursive formulas
H('5.B', 3, "Which recursive formula describes the arithmetic sequence 3, 7, 11, 15, ...?", "a₁ = 3, aₙ = aₙ₋₁ + 4", ["a₁ = 3, aₙ = 4aₙ₋₁", "a₁ = 4, aₙ = aₙ₋₁ + 3", "a₁ = 3, aₙ = aₙ₋₁ + 3"], "Each term adds 4.")
H('5.B', 3, "Which recursive formula describes the geometric sequence 2, 6, 18, 54, ...?", "a₁ = 2, aₙ = 3aₙ₋₁", ["a₁ = 2, aₙ = aₙ₋₁ + 3", "a₁ = 3, aₙ = 2aₙ₋₁", "a₁ = 2, aₙ = aₙ₋₁ + 4"], "Each term is 3 times the one before.")
H('5.B', 3, "A sequence has a₁ = 5 and aₙ = aₙ₋₁ − 2. What is a₄?", "−1", ["1", "−3", "3"], "5, 3, 1, −1.")

# 5.C arithmetic series
H('5.C', 3, "What is the 10th term of the arithmetic sequence 2, 5, 8, ...?", "29", ["30", "27", "32"], "aₙ = 2 + 3(9).")
H('5.C', 3, "What is the sum of the first 5 terms of the arithmetic sequence 1, 3, 5, 7, 9?", "25", ["15", "20", "30"], "Sₙ = n(a₁ + aₙ)/2 = 5 × 10/2.")
H('5.C', 4, "What is the sum of the whole numbers from 1 to 100?", "5050", ["5000", "5100", "10100"], "100 × 101 ÷ 2.")

# 5.D sigma notation for series
H('5.D', 3, "Which sigma notation represents 3 + 6 + 9 + 12?", "Σ (k = 1 to 4) of 3k", ["Σ (k = 1 to 3) of 3k", "Σ (k = 1 to 4) of k + 3", "Σ (k = 1 to 12) of 3"], "Each term is 3 times its position.")
H('5.D', 3, "Which sigma notation represents 2 + 4 + 8 + 16?", "Σ (k = 1 to 4) of 2ᵏ", ["Σ (k = 1 to 4) of 2k", "Σ (k = 1 to 4) of k²", "Σ (k = 1 to 4) of k + 2"], "The terms are powers of 2.")
H('5.D', 4, "Which sigma expression gives 1 + 3 + 5 + 7 + 9?", "Σ (k = 1 to 5) of (2k − 1)", ["Σ (k = 1 to 5) of 2k", "Σ (k = 1 to 9) of k", "Σ (k = 1 to 5) of (2k + 1)"], "The kth odd number is 2k − 1.")

# 5.E geometric series
H('5.E', 3, "What is the 5th term of the geometric sequence 3, 6, 12, ...?", "48", ["24", "30", "96"], "3 × 2⁴.")
H('5.E', 3, "What is the sum of the first 4 terms of 1, 2, 4, 8, ...?", "15", ["16", "14", "31"], "1 + 2 + 4 + 8.")
H('5.E', 4, "Under what condition does an infinite geometric series have a finite sum?", "|r| < 1", ["|r| > 1", "r = 1", "r > 2"], "Terms must shrink toward zero.")

# 5.F Binomial Theorem
H('5.F', 3, "What is the coefficient of x² in the expansion of (x + 1)⁴?", "6", ["4", "1", "12"], "C(4, 2) = 6.")
H('5.F', 3, "How many terms are there in the expansion of (a + b)⁵?", "6", ["5", "4", "10"], "There are n + 1 terms.")
H('5.F', 4, "What is the second term in the expansion of (x + 2)³?", "6x²", ["3x²", "12x", "8"], "C(3, 1) · x² · 2 = 6x².")

# 5.G log properties
H('5.G', 3, "Which expression equals log(a) + log(b)?", "log(ab)", ["log(a + b)", "log(a) · log(b)", "log(a/b)"], "The product rule.")
H('5.G', 3, "What is log₂ 8?", "3", ["2", "4", "16"], "2³ = 8.")
H('5.G', 3, "Which expression equals three times the logarithm of x?", "log(x³)", ["log(3x)", "(log x)³", "log(x + 3)"], "The power rule.")
H('5.G', 4, "Simplify log₅ 125 − log₅ 5.", "2", ["1", "3", "25"], "3 − 1 = 2.")

# 5.H log equations
H('5.H', 3, "Solve log₂ x = 5.", "x = 32", ["x = 10", "x = 25", "x = 7"], "2⁵ = 32.")
H('5.H', 4, "Solve log x + log(x − 3) = 1 for x.", "x = 5", ["x = −2", "x = 4", "x = 10"], "x(x − 3) = 10, so x = 5 or −2, and only 5 is valid.")
H('5.H', 3, "Solve ln x = 0.", "x = 1", ["x = 0", "x = e", "no solution"], "e⁰ = 1.")

# 5.I exponential equations
H('5.I', 3, "Solve 2ˣ = 16.", "x = 4", ["x = 8", "x = 3", "x = 2"], "2⁴ = 16.")
H('5.I', 4, "Solve 3^(x+1) = 27.", "x = 2", ["x = 3", "x = 1", "x = 8"], "x + 1 = 3.")
H('5.I', 4, "An investment of $1000 grows by 5% per year. Which equation finds the time t when it reaches $2000?", "1000(1.05)ᵗ = 2000", ["1000 + 0.05t = 2000", "1000(0.05)ᵗ = 2000", "1000t = 2000(1.05)"], "Exponential growth with a ratio of 1.05.")

# 5.J polynomial equations
H('5.J', 3, "Solve x³ − 4x = 0.", "x = 0, 2, −2", ["x = 4 only", "x = 0, 4", "x = 2 only"], "x(x − 2)(x + 2) = 0.")
H('5.J', 4, "What does the Rational Root Theorem suggest as possible rational roots of x³ + 2x² − x − 2 = 0?", "±1, ±2", ["±1, ±3", "±2, ±4", "only 0"], "Factors of −2 divided by factors of 1.")
H('5.J', 4, "How many real roots (counting multiplicity) can a cubic with real coefficients have at most?", "3", ["1", "2", "4"], "A degree-3 polynomial has 3 roots in the complex numbers.")

# 5.K polynomial inequalities
H('5.K', 3, "Solve x² − 4 > 0.", "x < −2 or x > 2", ["−2 < x < 2", "x > 2 only", "x > −2"], "The parabola is above the axis outside the zeros.")
H('5.K', 3, "Solve (x − 1)(x + 3) ≤ 0.", "−3 ≤ x ≤ 1", ["x ≤ −3 or x ≥ 1", "x ≥ 1", "x ≤ −3"], "The product is nonpositive between the roots.")
H('5.K', 4, "Which interval notation shows the solution to x² − 9 ≥ 0?", "(−∞, −3] ∪ [3, ∞)", ["[−3, 3]", "(−3, 3)", "[3, ∞)"], "The inequality includes the endpoints.")

# 5.L rational inequalities
H('5.L', 3, "Which x value makes (x − 1)/(x + 2) undefined?", "−2", ["1", "2", "0"], "The denominator must not be zero.")
H('5.L', 4, "Solve (x − 1)/(x + 2) > 0.", "x < −2 or x > 1", ["−2 < x < 1", "x > 1 only", "x > −2"], "The sign is positive when numerator and denominator agree.")
H('5.L', 4, "Solve 1/x < 1 for x > 0.", "x > 1", ["0 < x < 1", "x < 1", "x > 0"], "Multiplying by positive x gives 1 < x.")

# 5.M trig identities
H('5.M', 2, "What is sin²θ + cos²θ equal to?", "1", ["0", "2", "sin 2θ"], "The Pythagorean identity.")
H('5.M', 3, "Which expression equals tan θ?", "sin θ / cos θ", ["cos θ / sin θ", "1 / sin θ", "sin θ · cos θ"], "The quotient identity.")
H('5.M', 3, "Which expression equals sec θ?", "1 / cos θ", ["1 / sin θ", "cos θ / sin θ", "sin θ / cos θ"], "The reciprocal identity.")
H('5.M', 4, "Simplify 1 − cos²θ.", "sin²θ", ["cos θ", "tan²θ", "1"], "From sin²θ + cos²θ = 1.")

# 5.N trig equations
H('5.N', 3, "Solve sin x = 1/2 for 0 ≤ x < π/2.", "x = π/6", ["x = π/3", "x = π/4", "x = π/2"], "sin 30° = 1/2.")
H('5.N', 4, "How many solutions does cos x = 0 have on [0, 2π]?", "2", ["1", "3", "4"], "x = π/2 and x = 3π/2.")
H('5.N', 4, "Solve 2 sin x − 1 = 0 on [0, 2π].", "x = π/6 and 5π/6", ["x = π/6 only", "x = π/3 and 2π/3", "x = π/4 and 3π/4"], "sin x = 1/2 in quadrants I and II.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_precalc.jsonl'))

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('111.31.d.', 1054, own='ms_madv8.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A domain and range linear
H('2.A',3,"A candle is 12 inches tall and burns down 2 inches each hour until gone. Which is a reasonable domain for its height function?","0 ≤ t ≤ 6 hours",["all real numbers","t ≥ 12 hours","-6 ≤ t ≤ 6 hours"],"The candle burns for 12 ÷ 2 = 6 hours, and time cannot be negative.")
H('2.A',3,"For the linear function f(x) = 3x - 4 with no restrictions, what is the range?","all real numbers",["y ≥ -4","y ≤ 3","only integers"],"A non-constant line reaches every y-value.")
# 2.B forms of a line
H('2.B',3,"Which is the slope-intercept form of 2x + y = 7?","y = -2x + 7",["y = 2x + 7","y = -2x - 7","y = 7x - 2"],"Subtract 2x from both sides.")
H('2.B',3,"Write y - 3 = 4(x - 2) in slope-intercept form.","y = 4x - 5",["y = 4x + 5","y = 4x - 11","y = 4x + 1"],"y = 4x - 8 + 3 = 4x - 5.")
# 2.C write from table graph description
H('2.C',3,"A table gives (0, 5), (1, 8), (2, 11). Which equation fits?","y = 3x + 5",["y = 5x + 3","y = 3x + 8","y = x + 5"],"Slope is 3 and the y-intercept is 5.")
H('2.C',3,"A moving company charges a $60 base fee plus $25 per hour. Which equation gives the cost y for x hours?","y = 25x + 60",["y = 60x + 25","y = 85x","y = 25x - 60"],"Rate is the slope; base fee is the intercept.")
# 2.D direct variation
H('2.D',3,"y varies directly with x, and y = 12 when x = 4. What is y when x = 9?","27",["21","36","13"],"k = 3 so y = 3 × 9.")
H('2.D',3,"Which equation shows direct variation?","y = 0.4x",["y = 0.4x + 1","y = 0.4/x","y = x²"],"Direct variation has the form y = kx.")
# 2.E parallel
H('2.E',4,"What is the equation of the line through (0, 4) parallel to y = 2x - 1?","y = 2x + 4",["y = -x/2 + 4","y = 2x - 1","y = -2x + 4"],"Parallel lines share the slope 2.")
H('2.E',4,"A line through (1, 5) is parallel to y = 3x - 7. What is its equation?","y = 3x + 2",["y = 3x - 7","y = -x/3 + 5","y = 5x + 3"],"Slope 3; 5 = 3(1) + b gives b = 2.")
# 2.F perpendicular
H('2.F',4,"Which slope is perpendicular to a line with slope 4?","-1/4",["4","1/4","-4"],"Perpendicular slopes are negative reciprocals.")
H('2.F',4,"Find the line through (0, 1) perpendicular to y = 2x + 7.","y = -x/2 + 1",["y = 2x + 1","y = -2x + 1","y = x/2 + 1"],"Slope -1/2 and intercept 1.")
# 2.G horizontal vertical lines
H('2.G',2,"What is the equation of the horizontal line through (3, -2)?","y = -2",["x = 3","x = -2","y = 3"],"Horizontal lines have constant y.")
H('2.G',3,"Which line is perpendicular to the x-axis and passes through (5, 7)?","x = 5",["y = 7","x = 7","y = 5"],"A vertical line has constant x.")
# 2.H linear inequality writing
H('2.H',3,"Mia can spend at most $40 on pens at $2 each and notebooks at $5 each. Which inequality fits?","2p + 5n ≤ 40",["2p + 5n ≥ 40","7pn ≤ 40","2p - 5n ≤ 40"],"Total cost may not exceed $40.")
H('2.H',4,"A graph shows a dashed boundary y = x + 1 with shading above it. Which inequality does it show?","y > x + 1",["y < x + 1","y ≥ x + 1","y ≤ x + 1"],"Dashed means strict; shading above means greater.")
# 2.I systems writing
H('2.I',3,"Adult tickets cost $8 and child tickets $5. A group buys 10 tickets for $65. Which system fits?","a + c = 10 and 8a + 5c = 65",["a + c = 65 and 8a + 5c = 10","8a + 5c = 10 and a + c = 65","a - c = 10 and 8a - 5c = 65"],"One equation counts tickets, the other counts dollars.")
H('2.I',3,"A table shows two plans: Plan 1 costs 20 + 3x and Plan 2 costs 8 + 5x. Which system represents them?","y = 3x + 20 and y = 5x + 8",["y = 20x + 3 and y = 8x + 5","y = 3x - 20 and y = 5x - 8","y = 23x and y = 13x"],"Each plan is a line with a rate and starting fee.")
# 3.A similar triangles slope
H('3.A',3,"Similar right triangles drawn under a line show that the ratio rise over run is:","the same for every pair of points on the line",["different for each pair","always 1","always zero"],"Slope is constant for a line.")
H('3.A',3,"A right triangle under a line has rise 6 and run 3. What is the slope of the line?","2",["1/2","18","9"],"6 ÷ 3 = 2.")
# 3.B proportional graph
H('3.B',3,"A graph of a proportional relationship passes through (4, 10). What is the unit rate?","2.5",["0.4","14","6"],"10 ÷ 4 = 2.5.")
H('3.B',3,"In y = 7x, the slope of the graph is:","7",["1/7","0","y"],"The coefficient is the unit rate and slope.")
# 3.C slope
H('3.C',3,"What is the slope of the line through (1, 3) and (5, 11)?","2",["8","1/2","-2"],"(11 - 3) ÷ (5 - 1) = 2.")
H('3.C',3,"What is the slope of 3x + 4y = 12?","-3/4",["3/4","-4/3","3"],"y = -3/4 x + 3.")
# 3.D rate of change
H('3.D',3,"A function has values f(2) = 7 and f(6) = 19. What is its rate of change?","3",["12","4","1/3"],"(19 - 7) ÷ (6 - 2) = 3.")
H('3.D',3,"A tank holds 80 gallons and drains steadily to 20 gallons in 5 minutes. What is the rate of change?","-12 gallons per minute",["12 gallons per minute","-60 gallons per minute","-4 gallons per minute"],"(20 - 80) ÷ 5 = -12.")
# 3.E slope and intercept in context
H('3.E',3,"A table: 0 hours = $30, 2 hours = $50, 4 hours = $70. What does the y-intercept mean in context?","the starting amount of $30",["the pay per hour","the pay after 4 hours","the total hours"],"At x = 0 the value is 30.")
H('3.E',3,"In y = 12x + 45, where x is months and y is dollars saved, what does 12 represent?","dollars saved each month",["dollars at the start","the number of months","total dollars saved"],"The slope is the monthly rate.")
# 3.F graph linear functions
H('3.F',3,"Where does y = 2x - 6 cross the x-axis?","(3, 0)",["(0, 3)","(-6, 0)","(0, -6)"],"Set y = 0: 2x = 6.")
H('3.F',3,"What is the y-intercept of y = -5x + 9?","(0, 9)",["(9, 0)","(0, -5)","(-5, 0)"],"At x = 0, y = 9.")
# 3.G graph linear inequalities
H('3.G',3,"Which point is in the solution set of y ≥ 2x + 1?","(0, 3)",["(0, 0)","(2, 1)","(1, 0)"],"3 ≥ 1 is true.")
H('3.G',3,"The graph of y < 3x - 2 uses what kind of boundary line?","a dashed line",["a solid line","a vertical line","no line"],"Strict inequalities exclude the boundary.")
# 3.H effect of transformations on f(x)=x
H('3.H',3,"How does the graph of f(x) = x + 4 differ from f(x) = x?","It is shifted up 4 units.",["It is shifted right 4 units.","It is steeper.","It is reflected over the y-axis."],"Adding d moves the graph up by d.")
H('3.H',4,"How does the graph of f(x) = 3x compare with f(x) = x?","It is steeper.",["It is shifted up 3 units.","It is flatter.","It is shifted left 3 units."],"Multiplying by a > 1 stretches vertically.")
# 3.I systems graph
H('3.I ',3,"Two lines in a system intersect at (2, 5). What is the solution of the system?","x = 2, y = 5",["x = 5, y = 2","x = 0, y = 0","There is no solution."],"The intersection satisfies both equations.")
H('3.I ',3,"A system of two lines is graphed as parallel lines. How many solutions does it have?","none",["exactly one","exactly two","infinitely many"],"Parallel lines never meet.")
# 3.J estimate graphically
H('3.J ',4,"Two phone plans cost y = 10 + 0.05x and y = 4 + 0.10x. Graphing them, they cross when x is about:","120 minutes",["60 minutes","10 minutes","240 minutes"],"10 + 0.05x = 4 + 0.10x gives x = 120.")
H('3.J ',3,"Two lines cross at about (3.1, 6.9). Which is the best estimate of the solution?","(3, 7)",["(7, 3)","(0, 0)","(31, 69)"],"Round to the nearest whole numbers.")
# 3.K systems of inequalities
H('3.K',4,"The solution set of a system of two inequalities is graphed as the region:","where the shaded regions overlap",["above both lines only","on one line only","outside both shaded regions"],"Both inequalities must be true at once.")
H('3.K',4,"Is (1, 1) a solution of the system y > x - 3 and y < x + 2?","Yes",["No, it fails the first.","No, it fails the second.","No, it fails both."],"1 > -2 and 1 < 3 are both true.")
# 4.A scatterplot
H('4.A',3,"A scatterplot shows study time and test score rising together. The association is:","positive",["negative","none","vertical"],"As x increases y increases.")
H('4.A',3,"A scatterplot of car age and car value slopes downward. The association is:","negative",["positive","constant","unrelated"],"Value falls as age rises.")
# 4.B linear vs nonlinear
H('4.B',3,"Points on a scatterplot form a curve like a U-shape. Which model fits best?","a nonlinear model",["a linear model","no model","a horizontal line"],"The pattern is not a line.")
H('4.B',3,"Which scatterplot suggests a linear relationship?","points clustered tightly along a straight band",["points forming a circle","points spread everywhere","points in a sharp zigzag"],"A straight band indicates a linear trend.")
# 4.C trend line
H('4.C',3,"A trend line is y = 2x + 10 for x hours studied and y score. Predict the score for 8 hours.","26",["16","20","80"],"2(8) + 10 = 26.")
H('4.C',4,"Using the trend line y = -0.5x + 30, predict y when x = 20.","20",["10","-10","40"],"-10 + 30 = 20.")
# 4.D correlation coefficient
H('4.D',3,"A correlation coefficient near 1 indicates a:","strong positive linear relationship",["strong negative linear relationship","no relationship","perfect curve"],"Values near +1 mean strong positive.")
H('4.D',3,"Which correlation coefficient shows the weakest linear relationship?","0.05",["0.9","-0.85","-0.6"],"Values near 0 show little linear association.")
# 4.E association vs causation
H('4.E',3,"Ice cream sales and sunburns rise together in summer. What is the best conclusion?","They are associated but one does not necessarily cause the other.",["Ice cream causes sunburns.","Sunburns cause ice cream sales.","They are unrelated."],"A third factor, hot sunny weather, affects both.")
H('4.E',3,"Which evidence would best show that one variable causes another?","a controlled experiment",["a scatterplot alone","a high correlation alone","a guess"],"Experiments isolate cause.")
# 4.F fit linear functions
H('4.F',3,"A line fits data points (0, 3) and (4, 11). Which function best models it?","f(x) = 2x + 3",["f(x) = 3x + 2","f(x) = 2x + 11","f(x) = 4x + 3"],"Slope 2, intercept 3.")
H('4.F',4,"A linear model f(x) = 1.5x + 20 is used to estimate the value when x = 10.","35",["21.5","30","150"],"1.5(10) + 20 = 35.")
# 5.A solve linear eq
H('5.A',3,"Solve: 3(x - 4) = 2x + 5","x = 17",["x = 1","x = 9","x = 7"],"3x - 12 = 2x + 5 gives x = 17.")
H('5.A',4,"Solve: (x + 1)/2 = (x - 5)/4 + 3","x = 5",["x = -5","x = 11","x = 3"],"2(x + 1) = x - 5 + 12 gives x = 5.")
# 5.B inequalities
H('5.B',3,"Solve: 2(x + 3) < 14","x < 4",["x > 4","x < 8","x < 11"],"2x + 6 < 14 so x < 4.")
H('5.B',4,"Solve: 5 - 2x ≥ 11","x ≤ -3",["x ≥ -3","x ≤ 3","x ≥ 3"],"-2x ≥ 6, dividing by a negative flips the sign.")
# 5.C systems solve
H('5.C',3,"Solve the system: y = 2x and x + y = 12.","(4, 8)",["(6, 12)","(8, 4)","(3, 6)"],"x + 2x = 12 so x = 4.")
H('5.C',4,"Solve the system: 2x + y = 9 and x - y = 3.","(4, 1)",["(3, 3)","(1, 4)","(5, 2)"],"Adding gives 3x = 12.")
# 6.A domain range quadratic
H('6.A',3,"What is the range of f(x) = x² + 3?","y ≥ 3",["y ≤ 3","all real numbers","y ≥ 0"],"The minimum value is 3 at x = 0.")
H('6.A',3,"What is the domain of every quadratic function f(x) = ax² + bx + c?","all real numbers",["x ≥ 0","x > 0","only integers"],"Any real x can be squared.")
# 6.B write from vertex
H('6.B',4,"A parabola has vertex (2, 1) and passes through (3, 3). Which equation fits?","y = 2(x - 2)² + 1",["y = (x - 2)² + 1","y = 2(x + 2)² + 1","y = 2(x - 2)² - 1"],"3 = a(1)² + 1 gives a = 2.")
H('6.B',4,"Write the equation of a parabola with vertex (0, -4) opening up with a = 3.","y = 3x² - 4",["y = 3x² + 4","y = -3x² - 4","y = x² - 12"],"Vertex form with h = 0 and k = -4.")
# 6.C write from solutions
H('6.C',4,"A quadratic has real solutions x = 2 and x = 5. Which function has these zeros?","f(x) = (x - 2)(x - 5)",["f(x) = (x + 2)(x + 5)","f(x) = (x - 2)(x + 5)","f(x) = x² + 7"],"Each zero gives a factor.")
H('6.C',4,"A parabola crosses the x-axis at -1 and 4. Which equation fits?","y = (x + 1)(x - 4)",["y = (x - 1)(x + 4)","y = (x + 1)(x + 4)","y = x² - 4"],"x = -1 gives factor (x + 1).")
# 7.A graph quadratics
H('7.A',3,"Which is the axis of symmetry of y = x² - 6x + 5?","x = 3",["x = -3","x = 5","x = 6"],"-b/(2a) = 6/2 = 3.")
H('7.A',3,"A parabola y = -x² + 4 opens:","downward",["upward","left","right"],"A negative leading coefficient opens down.")
# 7.B factors and zeros
H('7.B',3,"The zeros of y = (x - 3)(x + 7) are:","3 and -7",["-3 and 7","3 and 7","21"],"Set each factor equal to zero.")
H('7.B',3,"If x = 4 is a zero of a quadratic, then which is a factor?","x - 4",["x + 4","4x","x - 16"],"A zero r gives the factor (x - r).")
# 7.C transformations of x²
H('7.C',3,"How does y = x² + 5 compare with y = x²?","It is shifted up 5 units.",["It is shifted right 5 units.","It is narrower.","It opens downward."],"Adding d shifts the graph up.")
H('7.C',4,"How does y = (x - 4)² compare with y = x²?","It is shifted right 4 units.",["It is shifted left 4 units.","It is shifted up 4 units.","It is wider."],"Replacing x with x - h moves right by h.")
# 8.A solve quadratics
H('8.A',3,"Solve x² = 49 by taking square roots.","x = 7 or x = -7",["x = 7 only","x = 24.5","x = 49"],"Both roots satisfy x² = 49.")
H('8.A',4,"Solve by factoring: x² - 5x + 6 = 0","x = 2 or x = 3",["x = -2 or x = -3","x = 1 or x = 6","x = 5 or x = 6"],"(x - 2)(x - 3) = 0.")
H('8.A',4,"Using the quadratic formula, what are the solutions of x² - 4x + 3 = 0?","x = 1 or x = 3",["x = -1 or x = -3","x = 2 or x = 6","x = 4 or x = -3"],"x = (4 ± 2) ÷ 2.")
# 8.B fit quadratic
H('8.B',4,"A quadratic model fits a ball's height data well. What does its vertex represent?","the ball's maximum height",["the ball's starting time","the number of bounces","the ball's mass"],"The vertex is the peak of the parabola.")
H('8.B',3,"Which data pattern is best modeled by a quadratic function?","values that rise then fall in a curve",["values that rise by a constant amount","values that never change","values that double"],"Quadratic data curve like a parabola.")
# 9.A domain range exponential
H('9.A',3,"What is the range of f(x) = 2^x?","y > 0",["y ≥ 0","all real numbers","y < 0"],"Exponentials with positive a are positive.")
H('9.A',3,"What is the domain of f(x) = 5 · 3^x?","all real numbers",["x > 0","x ≥ 0","x ≠ 0"],"Any real exponent can be used.")
# 9.B interpret a and b
H('9.B',3,"In f(x) = 200(1.05)^x, what does 1.05 represent?","the growth factor",["the starting amount","the number of years","the decay factor"],"b > 1 is a growth factor.")
H('9.B',3,"In f(x) = 80(0.5)^x, what does 80 represent?","the initial amount",["the decay rate","the growth factor","the final amount"],"a is the value when x = 0.")
# 9.C write exponential
H('9.C',4,"A population of 500 doubles every year. Which function models it?","f(x) = 500(2)^x",["f(x) = 500 + 2x","f(x) = 2(500)^x","f(x) = 1000x"],"Starting amount times a doubling factor.")
H('9.C',4,"A car worth $20,000 loses 10% of its value each year. Which function gives its value after x years?","f(x) = 20000(0.9)^x",["f(x) = 20000(1.1)^x","f(x) = 20000 - 0.1x","f(x) = 0.9(20000)^x"],"The decay factor is 1 - 0.10.")
# 9.D graph exponential
H('9.D',3,"The y-intercept of f(x) = 6(2)^x is:","(0, 6)",["(0, 2)","(6, 0)","(0, 12)"],"At x = 0, the value is a.")
H('9.D',3,"The graph of an exponential growth function gets closer to which line as x becomes very negative?","y = 0",["x = 0","y = 1","y = x"],"The horizontal asymptote is y = 0.")
# 9.E fit exponential
H('9.E',4,"Data that more than doubles each step is best fit by:","an exponential function",["a linear function","a constant","a quadratic with a negative leading term"],"Constant multiplication suggests exponential growth.")
H('9.E',3,"Using f(x) = 100(1.2)^x, the value at x = 2 is:","144",["120","140","240"],"100 × 1.44.")
# 10.A add subtract polynomials
H('10.A',3,"(3x² + 2x - 1) + (x² - 5x + 4) =","4x² - 3x + 3",["4x² + 7x + 3","3x² - 3x + 3","4x² - 3x - 5"],"Combine like terms.")
H('10.A',3,"(5x + 7) - (2x - 3) =","3x + 10",["3x + 4","7x + 4","3x - 4"],"Distribute the negative.")
# 10.B multiply polynomials
H('10.B',3,"(x + 3)(x + 5) =","x² + 8x + 15",["x² + 15","x² + 8x + 8","x² + 15x + 8"],"FOIL: x² + 5x + 3x + 15.")
H('10.B',4,"(2x - 1)(x + 4) =","2x² + 7x - 4",["2x² - 4","2x² + 9x - 4","2x² + 7x + 4"],"2x² + 8x - x - 4.")
# 10.C divide polynomial
H('10.C',4,"(6x² + 9x) ÷ (3x) =","2x + 3",["2x² + 3","18x² + 27x","3x + 2"],"Divide each term by 3x.")
H('10.C',4,"(x² + 5x + 6) ÷ (x + 2) =","x + 3",["x + 2","x² + 3","x + 6"],"x² + 5x + 6 = (x + 2)(x + 3).")
# 10.D distributive
H('10.D',3,"Rewrite 4(2x - 5) using the distributive property.","8x - 20",["8x - 5","6x - 9","2x - 20"],"Multiply each term by 4.")
H('10.D',3,"Rewrite -3x(x + 2) using the distributive property.","-3x² - 6x",["-3x² + 6x","-3x + 6","3x² - 6x"],"Multiply -3x by each term.")
# 10.E factor trinomials
H('10.E',4,"Factor x² + 7x + 12.","(x + 3)(x + 4)",["(x + 2)(x + 6)","(x + 1)(x + 12)","(x - 3)(x - 4)"],"3 × 4 = 12 and 3 + 4 = 7.")
H('10.E',4,"Factor 2x² + 7x + 3.","(2x + 1)(x + 3)",["(2x + 3)(x + 1)","(x + 1)(x + 3)","(2x + 7)(x + 3)"],"Check the middle term: 6x + x = 7x.")
H('10.E',3,"Which is a perfect square trinomial?","x² + 10x + 25",["x² + 10x + 20","x² + 25","x² - 25"],"It equals (x + 5)².")
# 10.F difference of squares
H('10.F',3,"Factor x² - 49.","(x - 7)(x + 7)",["(x - 7)²","(x + 7)²","(x - 49)(x + 1)"],"a² - b² = (a - b)(a + b).")
H('10.F',3,"Which binomial is NOT a difference of two squares?","x² + 16",["x² - 16","4x² - 9","25 - y²"],"The sum of squares does not factor over the reals.")
# 11.A radicals
H('11.A',3,"Simplify √72.","6√2",["2√6","36√2","8√9"],"72 = 36 × 2.")
H('11.A',3,"Simplify √50 + √8.","7√2",["√58","5√2","13√2"],"5√2 + 2√2.")
# 11.B laws of exponents
H('11.B ',3,"Simplify x⁵ · x³.","x⁸",["x¹⁵","x²","2x⁸"],"Add exponents when multiplying like bases.")
H('11.B ',3,"Simplify (2x³)².","4x⁶",["2x⁶","4x⁵","2x⁵"],"Square 2 and multiply exponents.")
H('11.B ',4,"What is 5⁻² written with a positive exponent?","1/25",["-25","-10","25"],"A negative exponent means reciprocal.")
# 12.A functions ordered pairs
H('12.A',3,"Which set of ordered pairs is a function?","{(1, 2), (2, 4), (3, 6)}",["{(1, 2), (1, 4), (2, 6)}","{(3, 1), (3, 2), (3, 3)}","{(0, 1), (0, 2), (1, 5)}"],"Each input has exactly one output.")
H('12.A',3,"A mapping sends 1 to 5, 2 to 5 and 3 to 7. Is it a function?","Yes, each input has one output.",["No, because 5 repeats.","No, because 3 is odd.","No, because outputs must differ."],"Repeated outputs are allowed.")
# 12.B relations define functions
H('12.B',3,"A graph fails the vertical line test. What does this mean?","It is not a function.",["It is a linear function.","It is a quadratic function.","It is a function with domain zero."],"A vertical line hits it more than once.")
H('12.B',3,"A table lists x: 1, 2, 2 and y: 4, 5, 6. Does it define y as a function of x?","No, x = 2 has two outputs.",["Yes","Yes, since y values differ","No, since x repeats of 1"],"One input gives two outputs.")
# 12.C evaluate
H('12.C',3,"If f(x) = 4x - 3, find f(5).","17",["23","20","12"],"4(5) - 3 = 17.")
H('12.C',3,"If g(x) = x² + 2x, find g(-3).","3",["15","-3","-15"],"9 - 6 = 3.")
# 12.D sequences terms
H('12.D',3,"What is the next term of the arithmetic sequence 7, 11, 15, ...?","19",["23","18","17"],"Common difference is 4.")
H('12.D',3,"What is the next term of the geometric sequence 3, 6, 12, ...?","24",["18","15","36"],"Common ratio is 2.")
# 12.E nth term
H('12.E',4,"Which is the formula for the nth term of 5, 8, 11, 14, ...?","a_n = 3n + 2",["a_n = 3n + 5","a_n = 5n + 3","a_n = n + 5"],"First term 5 plus (n - 1)3.")
H('12.E',4,"Which formula gives the nth term of the geometric sequence 2, 6, 18, ...?","a_n = 2 · 3^(n - 1)",["a_n = 3 · 2^(n - 1)","a_n = 2n + 4","a_n = 6n - 4"],"First term 2 with ratio 3.")
# 12.F literal equations
H('12.F',3,"Solve d = rt for t.","t = d/r",["t = dr","t = r/d","t = d - r"],"Divide both sides by r.")
H('12.F',3,"Solve P = 2l + 2w for w.","w = (P - 2l)/2",["w = P - 2l","w = 2(P - l)","w = P/2 - 2l"],"Subtract 2l, then divide by 2.")
B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'ms_madv8.jsonl'))

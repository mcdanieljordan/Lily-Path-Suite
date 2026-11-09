import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('111.29.c.', 1052, own='ms_madv6.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A sets and subsets
H('2.A',2,"In a Venn diagram of number sets, the set of whole numbers sits entirely inside the set of integers. What does that show?","Whole numbers are a subset of the integers.",["Integers are a subset of whole numbers.","The two sets share no numbers.","Whole numbers and integers are the same set."],"A circle drawn inside another means every member of the inner set belongs to the outer set.")
H('2.A',3,"Which hierarchy lists these sets from smallest to largest: integers, whole numbers, rational numbers?","whole numbers, integers, rational numbers",["integers, whole numbers, rational numbers","rational numbers, integers, whole numbers","whole numbers, rational numbers, integers"],"Whole numbers fit inside integers, and integers fit inside rational numbers.")
# 2.B opposite and absolute value
H('2.B',2,f"What is the opposite of {-37}?","37",["-37","0","-73"],"The opposite of a number is the same distance from 0 on the other side.")
H('2.B',3,"What is the absolute value of -4.6?","4.6",["-4.6","0.46","-5"],"Absolute value is distance from 0, so it is never negative.")
# 2.C benchmark fractions and percents
H('2.C',2,"Which percent equals the fraction 1/4?","25%",["14%","4%","40%"],"1/4 of 100 is 25, so 1/4 = 25%.")
H('2.C',3,"A model has 100 squares and 33 1/3 of them are shaded in a pattern of thirds. About what fraction is shaded?","1/3",["1/33","1/4","3/10"],"33 1/3% is the benchmark percent for one third.")
# 2.D equivalent forms
H('2.D',2,"Which decimal and percent are equal to 3/5?","0.6 and 60%",["0.35 and 35%","0.3 and 30%","6.0 and 600%"],"3/5 = 6/10 = 0.6 = 60%.")
H('2.D',3,"A recipe uses 0.125 of a cup of oil. What fraction of a cup is this?","1/8",["1/125","1/5","12/5"],"0.125 = 125/1000 = 1/8.")
# 2.E equal parts of same whole
H('2.E',3,"Mia ate 7/10 of a pizza and Jay ate 70% of an identical pizza. How do their amounts compare?","They ate equal amounts.",["Mia ate more.","Jay ate more.","They ate different amounts but cannot tell which is more."],"7/10 = 0.7 = 70% of the same size whole.")
H('2.E',3,"Which three values name the same part of a whole?","3/20, 0.15, 15%",["3/20, 0.3, 30%","3/20, 0.015, 1.5%","3/20, 1.5, 15%"],"3/20 = 15/100 = 0.15 = 15%.")
# 2.F locate compare order on a number line
H('2.F',2,"On a horizontal number line, which number is farthest to the left?","-9",["-2","0","5"],"Numbers farther left are less.")
H('2.F',3,"Which statement is true?","-3.5 < -3",["-3.5 > -3","-3 < -3.5","-3.5 = -3"],"On a number line -3.5 is left of -3, so it is less.")
# 2.G order rational numbers
H('2.G',3,"Which list is in order from least to greatest?","-2.5, -1/2, 0.3, 3/4",["-1/2, -2.5, 0.3, 3/4","3/4, 0.3, -1/2, -2.5","-2.5, 0.3, -1/2, 3/4"],"Order by position on a number line, left to right.")
H('2.G',4,"Which list is in order from greatest to least?","7/8, 0.8, 3/4, 0.7",["0.7, 3/4, 0.8, 7/8","3/4, 7/8, 0.8, 0.7","0.8, 7/8, 0.7, 3/4"],"As decimals: 0.875, 0.8, 0.75, 0.7.")
# 2.H coordinate plane
H('2.H',2,"In which quadrant is the point (-4, 6)?","Quadrant II",["Quadrant I","Quadrant III","Quadrant IV"],"Negative x and positive y puts a point in Quadrant II.")
H('2.H',3,"What are the coordinates of the point 5 units right of the origin and 3 units down?","(5, -3)",["(-3, 5)","(-5, 3)","(3, -5)"],"Move right for x and down for negative y.")
# 3.A dividing by rational = multiply by reciprocal
H('2.H' if False else '3.A',3,"Dividing by 3/4 gives the same result as multiplying by:","4/3",["3/4","-3/4","1/3"],"Dividing by a rational number equals multiplying by its reciprocal.")
H('3.A',3,"Which expression has the same value as 6 ÷ 2/5?","6 × 5/2",["6 × 2/5","6 ÷ 5/2","2/5 ÷ 6"],"Change the divisor to its reciprocal and multiply.")
# 3.B increase/decrease with fraction
H('3.B',3,"Without calculating, which product is greater than 40?","40 × 1 1/4",["40 × 3/4","40 × 1/2","40 × 9/10"],"Multiplying by a number greater than 1 increases the quantity.")
H('3.B',3,"Maya multiplies 18 by 5/6. Will the product be less than, equal to or greater than 18?","less than 18",["equal to 18","greater than 18","impossible to tell"],"5/6 is less than 1.")
# 3.C a/b = a ÷ b
H('3.C',2,"The fraction 7/8 represents the same number as which division?","7 ÷ 8",["8 ÷ 7","7 × 8","8 - 7"],"The fraction bar means divide numerator by denominator.")
H('3.C',3,"Five friends share 3 sandwiches equally. How much does each friend get?","3/5 of a sandwich",["5/3 of a sandwich","3 sandwiches","1/5 of a sandwich"],"3 ÷ 5 = 3/5.")
# 3.D integer ops with models
H('3.D',2,"A model shows 5 positive counters and 8 negative counters. What integer does it represent?","-3",["3","13","-13"],"Pair 5 positives with 5 negatives, leaving 3 negatives.")
H('3.D',3,"Which action on a number line models -2 + 6?","Start at -2 and move 6 units right.",["Start at 2 and move 6 units left.","Start at -6 and move 2 units right.","Start at 0 and move 8 units right."],"Adding a positive moves right.")
# 3.E integer fluency
H('3.E',2,f"What is -14 + 9?","-5",["5","-23","23"],"Subtract the absolute values and keep the sign of the larger one.")
H('3.E',3,f"What is {-48 // 6} + ({-7} × {-3})?","13",["-29","29","-13"],"-8 + 21 = 13.")
# 3.F rational ops
H('3.F',3,"What is 2/3 + 3/4?","1 5/12",["5/7","1 1/12","1/12"],"8/12 + 9/12 = 17/12 = 1 5/12.")
H('3.F',4,"What is -1.5 × 0.4?","-0.6",["0.6","-6","-0.06"],"1.5 × 0.4 = 0.6, and a negative times a positive is negative.")
# 3.G order of operations
H('3.G',3,"Which is the value of 4 + 3² × 2?","22",["98","26","49"],"Exponent first: 9; then 9 × 2 = 18; then 4 + 18 = 22.")
H('3.G',4,"The prime factorization of 72 is:","2³ × 3²",["2² × 3³","2 × 6²","8 × 9"],"72 = 8 × 9 = 2³ × 3².")
# 3.H check register
H('3.H',3,"A check register starts at $240. A deposit of $85 is made and a withdrawal of $60 is made. What is the balance?","$265",["$185","$295","$215"],"240 + 85 - 60 = 265.")
H('3.H',3,"A register balance is $120. A transfer of $45 out of the account is recorded. What is the new balance?","$75",["$165","$45","$120"],"A transfer out is subtracted.")
# 3.I net worth
H('3.I',3,"A student has assets of $1,250 and liabilities of $400. What is the net worth?","$850",["$1,650","$400","$1,250"],"Net worth = assets - liabilities.")
H('3.I',3,"Which item is a liability?","a loan balance owed to a lender",["a savings account","a bicycle you own","cash in a wallet"],"Liabilities are amounts you owe.")
# 4.A percent problems
H('4.A',3,"What is 35% of 80?","28",["2.8","45","280"],"0.35 × 80 = 28.")
H('4.A',4,"A jacket sale price is $36 after 40% off the original price. What was the original price?","$60",["$50.40","$14.40","$90"],"Sale price is 60% of the original. 36 ÷ 0.60 = 60.")
# 4.B sales tax and income tax
H('4.B',3,"A game costs $45 and sales tax is 8%. How much is the tax?","$3.60",["$36","$0.36","$4.50"],"0.08 × 45 = 3.60.")
H('4.B',4,"A worker earns $520 in a week and 12% is withheld for income tax. How much is withheld?","$62.40",["$6.24","$457.60","$124.80"],"0.12 × 520 = 62.40.")
# 5.A ratios
H('5.A',2,"A bag has 12 red and 9 blue marbles. Which ratio compares red to blue?","12 to 9",["9 to 12","12 to 21","9 to 21"],"Ratio of red to blue is 12:9.")
H('5.A',3,"The ratio of cats to dogs at a shelter is 5:3. If there are 15 cats, how many dogs are there?","9",["3","25","5"],"15 = 5 × 3, so dogs = 3 × 3 = 9.")
# 5.B rates
H('5.B',2,"Which is a rate?","240 miles in 4 hours",["12 red apples and 12 green apples","3 boys and 3 girls","5 cups and 5 cups"],"A rate compares two quantities with different units.")
H('5.B',3,"A hose fills 30 gallons in 6 minutes. What is the rate per minute?","5 gallons per minute",["0.2 gallons per minute","36 gallons per minute","24 gallons per minute"],"30 ÷ 6 = 5.")
# 5.C represent ratios and percents
H('5.C',3,"A 10-by-10 grid has 45 squares shaded. Which percent does the shading represent?","45%",["4.5%","55%","10%"],"45 out of 100 squares is 45%.")
H('5.C',3,"The ratio 3:4 written as a fraction of the total (3 + 4 parts) shows the first part is:","3/7",["3/4","4/7","3/12"],"First part over total parts is 3/7.")
# 5.D scale factors
H('5.D',3,"A map uses a scale of 1 inch = 15 miles. Two towns are 4 inches apart on the map. How far apart are they?","60 miles",["19 miles","3.75 miles","15 miles"],"4 × 15 = 60.")
H('5.D',3,"A photo is enlarged by a scale factor of 3. A 4-inch side becomes:","12 inches",["7 inches","1.33 inches","3 inches"],"4 × 3 = 12.")
# 6.A reasoning predictions
H('6.A',3,"A recipe uses 3 cups of flour for 24 cookies. About how much flour is needed for 60 cookies?","7.5 cups",["6 cups","9 cups","18 cups"],"60 cookies is 2.5 times 24, so 3 × 2.5 = 7.5.")
H('6.A',3,"Store A sells 4 pens for $3.20 and store B sells 6 pens for $4.50. Which has the better price per pen?","Store B at $0.75",["Store A at $0.80","They are the same","Store B at $0.80"],"Store A is $0.80 per pen and store B is $0.75.")
# 6.B unit rates
H('6.B',3,"A runner covers 9 miles in 1.5 hours. What is the unit rate in miles per hour?","6",["13.5","0.17","7.5"],"9 ÷ 1.5 = 6.")
H('6.B',3,"A 12-ounce box of cereal costs $4.20. What is the unit price per ounce?","$0.35",["$0.28","$3.50","$2.86"],"4.20 ÷ 12 = 0.35.")
# 6.C measurement conversion
H('6.C',2,"How many centimeters are in 3.5 meters?","350",["35","3,500","0.035"],"1 meter = 100 centimeters.")
H('6.C',3,"There are about 2.54 centimeters in 1 inch. About how many centimeters are in 10 inches?","25.4",["3.94","254","12.54"],"10 × 2.54 = 25.4.")
# 7.A expressions vs equations
H('7.A',2,"Which is an equation?","x + 5 = 12",["x + 5","3x - 2","4(x + 1)"],"An equation contains an equals sign.")
H('7.A',2,"Which is an expression and NOT an equation?","7n - 3",["7n - 3 = 4","n = 2","2n = 8"],"An expression has no equals sign.")
# 7.B equivalent expressions
H('7.B',3,"Which expression is equivalent to 2(x + 4)?","2x + 8",["2x + 4","x + 8","2x + 6"],"Distribute the 2 to both terms.")
H('7.B',3,"Which expression is NOT equivalent to 3x + 6?","3(x + 6)",["3(x + 2)","6 + 3x","x + x + x + 6"],"3(x + 6) = 3x + 18.")
# 7.C properties of operations
H('7.C',3,"Which property shows that 4 + (x + 9) = (4 + x) + 9?","associative property",["commutative property","identity property","inverse property"],"Regrouping terms is the associative property.")
H('7.C',3,"Which property is used when 5 × y is rewritten as y × 5?","commutative property",["associative property","distributive property","inverse property"],"Changing order is the commutative property.")
# 8.A write equations/inequalities
H('8.A',3,"A gym charges a $20 sign-up fee plus $15 per month. Which equation gives the total cost C after m months?","C = 15m + 20",["C = 20m + 15","C = 35m","C = 15 + 20 + m"],"Fixed fee plus rate times months.")
H('8.A',3,"You have $50 and can spend at most $8 per ticket. Which inequality shows how many tickets t you can buy?","8t ≤ 50",["8t ≥ 50","t ≤ 8","8 + t ≤ 50"],"Total cost must not exceed $50.")
# 8.B real-world problems from equations
H('8.B',3,"Which situation matches the equation 4n = 36?","4 friends share $36 equally and each pays n.",["You had $4 and spent $36.","A $4 fee is added to a $36 bill.","You buy 36 items for $4 total."],"Four equal parts total 36 gives 4n = 36.")
H('8.B',3,"Which problem matches x + 12 = 30?","A class had x students, 12 joined and now there are 30.",["A class has 12 students and loses x.","30 students are split into 12 groups.","A class has 30 students and loses 12 more."],"Starting amount plus 12 equals 30.")
# 8.C number line solutions
H('8.C',3,"Which graph shows x > 4 on a number line?","an open circle at 4 with an arrow pointing right",["a closed circle at 4 with an arrow pointing left","an open circle at 4 with an arrow pointing left","a closed circle at 4 with an arrow pointing right"],"Open circle: 4 not included. Arrow right: values greater than 4.")
H('8.C',3,"A number line shows a closed circle at 2 with an arrow pointing left. Which inequality does it show?","x ≤ 2",["x < 2","x ≥ 2","x > 2"],"Closed circle includes 2; arrow left means less.")
# 8.D one-step
H('8.D',2,"Solve: x + 9 = 21","12",["30","-12","11"],"Subtract 9 from both sides.")
H('8.D',3,"Solve: 6x = 84","14",["90","78","504"],"Divide both sides by 6.")
# 8.E two-step
H('8.E',3,"Solve: 3x + 5 = 26","7",["10","31/3","21"],"Subtract 5 to get 3x = 21, then divide by 3.")
H('8.E',4,"Solve: 2x - 7 > 9","x > 8",["x > 1","x < 8","x > 16"],"Add 7 to get 2x > 16, then divide by 2.")
# 8.F check solutions
H('8.F',2,"Which value makes 2x + 3 = 15 true?","x = 6",["x = 9","x = 4","x = 12"],"2(6) + 3 = 15.")
H('8.F',3,"Which value makes x - 4 < 3 true?","x = 6",["x = 7","x = 8","x = 10"],"6 - 4 = 2 which is less than 3; 7 - 4 = 3 is not less than 3.")
# 9.A independent/dependent
H('9.A',2,"A table pairs the hours a person works with a paycheck amount. Which quantity is the dependent quantity?","pay earned",["hours worked","the hourly rate","the number of workers"],"Pay depends on hours worked.")
H('9.A',3,"In a graph of distance traveled versus time, which axis usually shows the independent quantity?","the horizontal axis (time)",["the vertical axis (distance)","neither axis","both axes"],"Independent quantity goes on the horizontal axis.")
# 9.B equation from a table
H('9.B',3,"x: 1, 2, 3, 4 and y: 6, 12, 18, 24. Which equation matches?","y = 6x",["y = x + 5","y = 6 + x","y = 12x"],"Each y is 6 times x.")
H('9.B',3,"x: 2, 4, 6, 8 and y: 5, 7, 9, 11. Which equation matches?","y = x + 3",["y = 2x + 1","y = 3x","y = x - 3"],"Each y is 3 more than x.")
# 9.C situations as y = kx or y = x + b
H('9.C',3,"Pencils cost $0.25 each. Which equation shows the cost y of x pencils?","y = 0.25x",["y = x + 0.25","y = 0.25 + x","y = x ÷ 0.25"],"Cost is a constant rate times the number.")
H('9.C',3,"A plant is 8 cm tall and grows 3 cm. Which equation shows the new height y when the original is x?","y = x + 3",["y = 3x","y = x - 3","y = 8x"],"Add the growth to the original height.")
# 9.D compare two rules
H('9.D',3,"Rule A: y = 2x. Rule B: y = x + 2. For which x are the outputs equal?","x = 2",["x = 0","x = 1","x = 3"],"2(2) = 4 and 2 + 2 = 4.")
H('9.D',4,"Compare y = 3x and y = x + 6. When x = 5 which output is greater?","y = 3x",["y = x + 6","They are equal","Cannot be determined"],"3(5) = 15 and 5 + 6 = 11.")
# 11.A model area formulas
H('11.A',3,"A parallelogram can be cut and rearranged into a rectangle with the same base and height. What formula does this model?","A = b × h",["A = 1/2 × b × h","A = b + h","A = 2b + 2h"],"The rectangle has area base times height.")
H('11.A',3,"Two identical triangles form a parallelogram. The area of one triangle is therefore:","1/2 × b × h",["b × h","2 × b × h","b + h"],"Half the parallelogram's area.")
# 11.B equations for area
H('11.B',3,"A triangle has area 30 square units and base 12 units. Which equation finds its height h?","1/2 × 12 × h = 30",["12 × h = 30","1/2 × 12 + h = 30","12 + h = 30"],"Area of a triangle is 1/2 × base × height.")
H('11.B',3,"A rectangle has area 56 and width 7. Which equation finds the length?","7 × l = 56",["7 + l = 56","l ÷ 7 = 56","7 - l = 56"],"Area equals length times width.")
# 12.A triangles
H('12.A',3,"Two angles of a triangle measure 48° and 67°. What is the third angle?","65°",["115°","45°","85°"],"180 - 48 - 67 = 65.")
H('12.A',3,"In a triangle, the largest angle is opposite the:","longest side",["shortest side","middle side","any side"],"The longest side is across from the largest angle.")
# 12.B area problems
H('12.B',3,"A trapezoid has bases 6 and 10 and height 4. What is its area?","32 square units",["24 square units","64 square units","40 square units"],"1/2 × (6 + 10) × 4 = 32.")
H('12.B',3,"A parallelogram has base 9 and height 5. What is its area?","45 square units",["14 square units","90 square units","22.5 square units"],"9 × 5 = 45.")
# 12.C volume
H('12.C',3,"A right rectangular prism is 4 by 3 by 5. What is its volume?","60 cubic units",["12 cubic units","47 cubic units","94 cubic units"],"4 × 3 × 5 = 60.")
H('12.C',4,"A triangular prism has a triangular base with area 14 square units and height 6 units. What is its volume?","84 cubic units",["20 cubic units","42 cubic units","168 cubic units"],"Volume = base area × height = 14 × 6.")
# 12.D equations with geometry
H('12.D',3,"Two angles in a triangle are x and 2x and the third is 60°. Which equation finds x?","x + 2x + 60 = 180",["x + 2x = 60","x + 2x + 60 = 360","2x + 60 = 180"],"Angles of a triangle add to 180°.")
H('12.D',3,"Two angles are supplementary. One is 3x and the other is 40°. Which equation fits?","3x + 40 = 180",["3x + 40 = 90","3x = 40","3x + 40 = 360"],"Supplementary angles add to 180°.")
# 13.A variability
H('13.A',2,"Which question will produce data with variability?","How many minutes did each student spend on homework last night?",["How many days are in a week?","What is 5 + 5?","How many sides does a triangle have?"],"Answers vary from student to student.")
H('13.A',2,"Which question has just one correct answer, so no variability?","How many months are in a year?",["How tall are the students in your class?","How many pets does each classmate have?","How long is each student's commute?"],"A fixed fact has no variability.")
# 13.B represent data
H('13.B',3,"A box plot uses five numbers. Which is NOT one of them?","mean",["minimum","median","maximum"],"A box plot shows min, Q1, median, Q3 and max.")
H('13.B',3,"Which display groups data into intervals using bars with no gaps?","histogram",["dot plot","stem-and-leaf plot","circle graph"],"A histogram shows frequencies in intervals.")
# 14.A center spread shape
H('14.A',3,"A dot plot has most dots on the left and a long tail to the right. The shape is:","skewed right",["skewed left","symmetric","uniform"],"The tail points right.")
H('14.A',3,"In a dot plot, data spread from 2 to 18 describes the:","spread of the distribution",["center","mode only","shape only"],"Spread describes how far data extend.")
# 14.B mean median range IQR
H('14.B',3,"What is the median of 3, 7, 8, 12, 15?","8",["9","7","12"],"The middle value is 8.")
H('14.B',3,"For the data 4, 6, 8, 10, 12, what is the range?","8",["10","6","12"],"12 - 4 = 8.")
# 14.C interpret displays
H('14.C',3,"A stem-and-leaf plot has stem 3 and leaves 2, 5, 5. What data values are shown?","32, 35, 35",["3, 2, 5, 5","23, 53, 53","325"],"Stem is tens digit, leaves are ones digits.")
H('14.C',3,"In a histogram, the tallest bar represents the interval with the:","highest frequency",["highest value","lowest frequency","median value"],"Bar height shows frequency.")
# 14.D graph problems
H('14.D',3,"A circle graph shows 25% of students walk to school. If 200 students were surveyed, how many walk?","50",["25","100","175"],"0.25 × 200 = 50.")
H('14.D',3,"A bar graph shows soccer 18, tennis 12, golf 6. How many more chose soccer than golf?","12",["6","24","36"],"18 - 6 = 12.")
# 14.E compare groups
H('14.E',4,"Two box plots show test scores. One class has a median of 82 and the other has a median of 74. Which class has the higher center?","the class with median 82",["the class with median 74","They are equal","Cannot tell from medians"],"Compare medians for centers.")
H('14.E',4,"Comparing two dot plots, one is tightly clustered and the other is wide. Which comparison does this describe?","spread",["center","mode","range of a single point"],"Cluster width describes spread.")
# 14.F categorical data
H('14.F',2,"Favorite pets in a class: 8 students chose dogs, 6 cats, 6 fish and 4 birds. What does the mode describe here?","the category chosen by 8 students",["the category chosen by 4 students","the total of 24 students","the category chosen by 6 students"],"The mode is the category chosen most often.")
H('14.F',3,"In a survey of 40 students, 10 chose pizza. What percent chose pizza?","25%",["10%","40%","4%"],"10 ÷ 40 = 0.25.")
# 15.A checking account vs debit card
H('15.A',3,"A debit card takes money directly from the:","checking account",["credit line","loan","savings bond"],"A debit card draws on checking account funds.")
H('15.A',3,"When comparing checking accounts, a student should look at monthly fees and:","minimum balance rules",["the bank's logo","the color of the checks","branch decor"],"Fees and rules affect cost.")
# 15.B payment methods
H('15.B',3,"Which payment method lets you pay later and may charge interest?","credit card",["cash","debit card","prepaid gift card"],"Credit is borrowed money.")
H('15.B',3,"Which payment method cannot overdraw beyond the loaded amount?","prepaid card",["credit card","loan","line of credit"],"Prepaid funds limit spending.")
# 15.C credit history
H('15.C',3,"Why is a positive credit history important?","It helps people qualify for loans with better terms.",["It lowers the price of groceries.","It increases a paycheck.","It removes taxes."],"Lenders review credit history.")
H('15.C',3,"Which habit helps build a positive credit history?","paying bills on time",["missing payments","borrowing and never repaying","closing every account"],"On-time payments build trust.")
# 15.D credit report
H('15.D',3,"A credit report lists a person's accounts and:","payment history",["favorite stores","grades","weight"],"Reports list accounts and payment behavior.")
H('15.D',4,"Most negative items on a credit report are kept for about:","seven years",["one month","two days","forty years"],"Many entries remain for around seven years.")
# 15.E credit reports value
H('15.E',3,"Why do lenders check a borrower's credit report?","to judge how likely the borrower is to repay",["to learn his favorite music","to set his height","to choose his hobby"],"Lenders assess risk.")
H('15.E',3,"How does a borrower benefit from checking their own credit report?","They can find and fix errors.",["They can change their address legally","They can lower taxes","They can skip repayments"],"Reviewing reports catches mistakes.")
# 15.F paying for college
H('15.F',2,"Which way to pay for college does NOT have to be repaid?","a scholarship",["a student loan","a credit card balance","a payday loan"],"Scholarships and many grants are gifts.")
H('15.F',3,"A work-study program helps pay for college by:","giving students a part-time job",["canceling tuition","lowering taxes","creating a loan with no interest"],"Work-study provides wages for campus jobs.")
# 15.G salary and education
H('15.G',3,"On average, occupations that require more post-secondary education tend to have:","higher annual salaries",["lower annual salaries","no salary","the same salary always"],"More education generally leads to higher pay.")
H('15.G',3,"A job requiring a vocational certificate usually needs:","specific training after high school",["no training at all","a doctorate","a law degree"],"Certificates are trade-focused training.")
H('2.G',4,"Place these in order from least to greatest: -0.75, -3/4 of 2, 1/3, -1/5.","-3/2, -0.75, -1/5, 1/3",["-0.75, -3/2, -1/5, 1/3","-1/5, -0.75, -3/2, 1/3","1/3, -1/5, -0.75, -3/2"],"-3/4 of 2 is -1.5. Then -1.5 < -0.75 < -0.2 < 0.33.")
H('2.G',3,"A scientist records temperatures -2.4, 0.5, -2.04 and 1/4 degrees. Which is the coldest?","-2.4",["-2.04","0.5","1/4"],"The most negative value is farthest left on the number line.")
H('15.C',3,"A teen makes every payment on a small loan on time for two years. What is the likely effect on the teen's credit history?","It becomes stronger and shows reliable repayment.",["It becomes weaker.","It is erased.","It has no information."],"Consistent on-time payments are recorded as positive history.")
H('15.C',3,"Which item is most likely to hurt a person's credit history?","missing several credit card payments",["paying a utility bill early","keeping a low balance","reviewing a credit report"],"Late and missed payments are reported negatively.")
B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'ms_madv6.jsonl'))

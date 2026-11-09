import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('111.30.', 1053, own='ms_madv7.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A sets and subsets
H('c.2.A',3,"A Venn diagram shows rational numbers as a large circle. Where would the irrational numbers be drawn?","outside the rational circle but inside the real numbers",["inside the integer circle","inside the whole-number circle","overlapping the natural numbers"],"Irrational numbers are real but not rational, so they sit outside the rational set.")
H('c.2.A',3,"Which statement about the real number system is true?","Every integer is also a rational number.",["Every rational number is an integer.","Every irrational number is a whole number.","No decimal is a real number."],"An integer n can be written as n/1.")
# 2.B approximate irrational
H('c.2.B',3,"Between which two consecutive integers does the square root of 38 lie?","6 and 7",["5 and 6","7 and 8","19 and 20"],"36 < 38 < 49, so the root is between 6 and 7.")
H('c.2.B',3,"Which is the best estimate of pi to the nearest hundredth for placing on a number line?","3.14",["3.41","3.00","3.40"],"Pi is about 3.14159.")
H('c.2.B',4,"On a number line, the square root of 20 is closest to which point?","4.5",["4","5","10"],"4.5 squared is 20.25, which is very near 20.")
# 2.C scientific notation
H('c.2.C',3,"Write 4,200,000 in scientific notation.","4.2 × 10⁶",["42 × 10⁵","4.2 × 10⁷","0.42 × 10⁶"],"Move the decimal point six places to get 4.2.")
H('c.2.C',3,"What is 3.7 × 10⁻³ in standard decimal notation?","0.0037",["3,700","0.037","0.00037"],"A negative exponent of 3 moves the decimal three places left.")
# 2.D order real numbers
H('c.2.D',3,"Which list is in order from least to greatest?","-3, √5, 2.5, π",["√5, -3, 2.5, π","-3, 2.5, √5, π","π, 2.5, √5, -3"],"As decimals: -3, 2.24, 2.5, 3.14.")
H('c.2.D',4,"Which value is greatest?","3.2",["√10","3.14","π"],"√10 ≈ 3.16 and π ≈ 3.14, both less than 3.2.")
# 3.A fluency
H('c.3.A',3,"What is -3/4 ÷ 3/8?","-2",["-1/2","-9/32","2"],"Multiply by the reciprocal: -3/4 × 8/3 = -2.")
H('c.3.A',3,"What is -2.5 × (-1.6)?","4",["-4","0.4","-0.4"],"A negative times a negative is positive: 2.5 × 1.6 = 4.")
H('c.3.A',2,"What is -9.4 + 5.7?","-3.7",["3.7","-15.1","15.1"],"The larger absolute value is negative, so the sum is negative.")
# 3.B problems
H('c.3.B',4,"A diver at -18.5 feet rises 6.25 feet and then descends 4 feet. What is the new depth?","-16.25 feet",["-8.25 feet","-28.75 feet","-20.5 feet"],"-18.5 + 6.25 - 4 = -16.25.")
H('c.3.B',3,"Four bottles each hold 1 1/2 cups. A cook pours out 2 3/4 cups in total. How much is left?","3 1/4 cups",["3 3/4 cups","8 3/4 cups","1 1/4 cups"],"4 × 1 1/2 = 6, and 6 - 2 3/4 = 3 1/4.")
# 4.A ratio, rate, percent
H('c.4.A',4,"A tablet costs $250 and its price rises by 20%. A week later the new price drops by 20%. What is the final price?","$240",["$250","$260","$200"],"250 × 1.2 = 300, then 300 × 0.8 = 240.")
H('c.4.A',3,"A town's population grew from 8,000 to 9,200. What is the percent increase?","15%",["12%","13%","1.5%"],"1,200 ÷ 8,000 = 0.15.")
# 4.B simple and compound interest
H('c.4.B',3,"What is the simple interest on $600 at 5% per year for 3 years?","$90",["$30","$93.15","$180"],"I = Prt = 600 × 0.05 × 3 = 90.")
H('c.4.B',4,"$1,000 earns 10% interest compounded annually. How much is it worth after 2 years?","$1,210",["$1,200","$1,100","$1,020"],"1,000 × 1.1 × 1.1 = 1,210.")
# 4.C incentives
H('c.4.C ',3,"A $80 pair of shoes is on sale for 25% off and you also have a $5 coupon taken off the sale price. What do you pay?","$55",["$60","$50","$75"],"25% off gives $60, and the coupon takes it to $55.")
H('c.4.C ',3,"Which describes a rebate?","money returned to you after you buy and submit proof",["a discount taken at the register","a free gift with no purchase","a tax on the item"],"A rebate is paid back after the sale.")
# 4.D interest rate and loan length
H('c.4.D',3,"Two loans are for the same amount at the same rate. One lasts 2 years and the other lasts 5 years. Which usually costs more in total interest?","the 5-year loan",["the 2-year loan","They always cost the same","It cannot be known"],"A longer term accrues interest for more time.")
H('c.4.D',4,"For the same loan length, which rate gives the lowest cost of credit?","4%",["6%","9%","12%"],"Lower rates produce less interest.")
# 4.E total cost of repaying a loan
H('c.4.E',3,"A loan requires $150 a month for 24 months. What is the total repaid?","$3,600",["$174","$2,400","$360"],"150 × 24 = 3,600.")
H('c.4.E',4,"A $2,000 loan is repaid with 12 payments of $185. How much interest was paid?","$220",["$2,220","$185","$12"],"12 × 185 = 2,220, and 2,220 - 2,000 = 220.")
# 4.F invest regularly
H('c.4.F ',3,"Why does saving a small amount every month for many years grow so much?","Earnings are added to the balance and then earn interest too.",["Banks stop charging fees.","Saved money is never taxed or fee-free by law.","Inflation always stops."],"Compounding makes earlier deposits grow the most.")
H('c.4.F ',3,"Who is likely to end up with more at retirement, assuming the same monthly deposit and rate?","the person who starts saving at age 22",["the person who starts at age 42","They always end equal","the person who saves nothing early"],"More time means more compounding.")
# 4.G college cost
H('c.4.G',3,"A four-year college costs $18,000 per year. A family can contribute $20,000 total. How much more is needed in total?","$52,000",["$72,000","$16,000","$38,000"],"4 × 18,000 = 72,000, and 72,000 - 20,000 = 52,000.")
H('c.4.G',3,"A two-year program costs $6,500 per year. Scholarships cover $4,000 in all. How much remains to pay?","$9,000",["$13,000","$2,500","$17,000"],"2 × 6,500 = 13,000, and 13,000 - 4,000 = 9,000.")
# 5.A pi
H('c.5.A',2,"Pi is the ratio of a circle's circumference to its:","diameter",["radius","area","height"],"C ÷ d is pi for every circle.")
H('c.5.A',3,"A circular lid has a diameter of 10 cm and a circumference of about 31.4 cm. What does 31.4 ÷ 10 estimate?","pi",["the radius","the area","the volume"],"Circumference over diameter gives pi.")
# 5.B similarity
H('c.5.B',3,"Which is true of two similar triangles?","Their corresponding angles are equal and corresponding sides are proportional.",["Their side lengths are equal.","Their areas are equal.","They have the same perimeter."],"Similar shapes keep shape but may differ in size.")
H('c.5.B',3,"Triangle P has sides 3, 4, 5. Which triangle is similar to it?","6, 8, 10",["3, 4, 6","4, 5, 6","5, 6, 7"],"6, 8, 10 is each side times 2.")
# 5.C scale drawings
H('c.5.C',3,"A blueprint scale is 1 cm = 2.5 m. A room is 6 cm long on the blueprint. What is its real length?","15 m",["8.5 m","2.4 m","12 m"],"6 × 2.5 = 15.")
H('c.5.C',4,"Two similar rectangles have widths 4 and 10. If the smaller has length 6, what is the larger one's length?","15",["14","24","10"],"The scale factor is 10 ÷ 4 = 2.5, so 6 × 2.5 = 15.")
# 5.D dilations
H('c.5.D',3,"A shape is dilated and its angles stay the same while its sides change. Which statement is true?","The image is similar but not congruent to the original.",["The image is congruent to the original.","The angles must be larger.","The shape reflected."],"Dilation keeps angle measures but changes size.")
H('c.5.D',3,"Which transformation of a figure changes its size?","dilation",["translation","reflection","rotation"],"The other three preserve size.")
# 5.E scale factor algebraic
H('c.5.E',4,"A dilation with scale factor 3 centered at the origin sends (2, 5) to:","(6, 15)",["(5, 8)","(2/3, 5/3)","(6, 5)"],"Multiply each coordinate by 3.")
H('c.5.E',4,"A dilation centered at the origin uses scale factor 1/2. Which point is the image of (8, -4)?","(4, -2)",["(16, -8)","(8, -2)","(4, 2)"],"Halve each coordinate.")
# 6.A sample spaces
H('c.6.A',3,"A spinner has 3 colors and a coin has 2 sides. How many outcomes are in the sample space for spinning once and flipping once?","6",["5","3","2"],"3 × 2 = 6.")
H('c.6.A',3,"Which tool lists every outcome of two independent stages by branching?","tree diagram",["histogram","scatter plot","circle graph"],"Branches show each choice.")
# 6.B simulations
H('c.6.B',3,"Which is a fair way to simulate a 1-in-4 chance event?","draw a card from four equal cards, one marked",["flip a coin once","roll one die and count a 1 or 2","draw from a bag with 3 marked of 4"],"One marked card out of four equal cards has probability 1/4.")
H('c.6.B',3,"To simulate a 50% chance, which tool works?","flipping a fair coin",["rolling a die and counting a 6","spinning a 3-color equal spinner","drawing 1 of 5 equal cards"],"A fair coin has two equally likely results.")
# 6.C experimental data
H('c.6.C',3,"A spinner lands on blue 18 times in 60 spins. What is the experimental probability of blue?","3/10",["18/42","1/6","6/10"],"18 ÷ 60 = 3/10.")
H('c.6.C',3,"Using a result of 12 heads in 40 flips, about how many heads are predicted in 200 flips?","60",["12","40","120"],"12/40 = 0.3, and 0.3 × 200 = 60.")
# 6.D theoretical
H('c.6.D',3,"A fair die is rolled twice. What is the probability of getting a 6 both times?","1/36",["1/6","1/12","2/6"],"1/6 × 1/6 = 1/36.")
H('c.6.D',3,"A bag has 3 red and 5 blue marbles. One marble is drawn. What is the probability it is red?","3/8",["3/5","5/8","1/3"],"3 favorable out of 8 total.")
# 6.E complement
H('c.6.E',3,"The probability of rain is 0.35. What is the probability it does NOT rain?","0.65",["0.35","0.55","1.35"],"The complement is 1 - 0.35.")
H('c.6.E',3,"If an event has probability 2/7, its complement has probability:","5/7",["2/7","7/2","1/7"],"Event and complement sum to 1.")
# 6.F qualitative/quantitative predictions
H('c.6.F',3,"Which event is least likely?","probability 0.05",["probability 0.5","probability 0.75","probability 0.95"],"The smallest probability is least likely.")
H('c.6.F',3,"After 100 trials, event A happened 30 times and event B happened 45 times. Which comparison is supported?","B has the greater experimental probability.",["A has the greater experimental probability.","They are equal.","Neither can be compared."],"45/100 > 30/100.")
# 6.G experimental and theoretical
H('c.6.G',4,"A fair coin is flipped twice. The theoretical probability of two heads is 1/4. In 80 trials, about how many two-head results are expected?","20",["40","10","60"],"1/4 × 80 = 20.")
H('c.6.G',3,"A student's experiment gives 24 two-head outcomes in 80 trials. How does this compare with the theoretical probability?","It is close but slightly higher than 1/4.",["It is exactly 1/4.","It is much lower than 1/4.","It cannot be compared."],"24/80 = 0.30 and 1/4 = 0.25.")
# 7.A graph inequalities
H('c.7.A',3,"Which inequality is graphed with a closed circle at 3 and a ray going right?","x ≥ 3",["x > 3","x ≤ 3","x < 3"],"Closed circle includes 3 and right means greater.")
H('c.7.A',3,"Which number line graph shows 2x + 1 < 9?","an open circle at 4 and a ray going left",["an open circle at 4 and a ray going right","a closed circle at 4 and a ray going left","a closed circle at 5 and a ray going right"],"2x < 8 gives x < 4.")
# 7.B solve two-step inequalities
H('c.7.B',4,"Solve: -3x + 2 > 14","x < -4",["x > -4","x < 4","x > 4"],"-3x > 12; dividing by a negative flips the sign.")
H('c.7.B',3,"Solve: 4x - 5 ≤ 11","x ≤ 4",["x ≤ 1.5","x ≥ 4","x ≤ 24"],"4x ≤ 16 and x ≤ 4.")
# 7.C variables both sides
H('c.7.C',3,"Two gyms: A charges $30 plus $5 per visit and B charges $10 plus $9 per visit. Which equation finds the visits v where cost is equal?","30 + 5v = 10 + 9v",["30 + 9v = 10 + 5v","30 + 10 = 5v + 9v","30v + 5 = 10v + 9"],"Set the two cost expressions equal.")
H('c.7.C',4,"A plant is 4 inches tall and grows 2 inches each week. Another is 10 inches and grows 1 inch each week. Which inequality finds when the first is taller?","4 + 2w > 10 + w",["4 + 2w < 10 + w","4w + 2 > 10w + 1","4 + w > 10 + 2w"],"Compare heights after w weeks.")
# 7.D write a problem
H('c.7.D',4,"Which situation matches 3x + 8 = 5x - 2?","Two plans cost the same: a $8 fee with $3 per use and a $2 credit with $5 per use.",["Three friends buy 8 items and 5 friends buy 2.","A bus carries 8 more than 3 people.","Both amounts are subtracted."],"Each side is a fixed amount plus a rate.")
H('c.7.D',4,"Which real-world problem matches 2x - 6 < x + 4?","A cost of 2 per item minus a 6 discount is less than 1 per item plus a 4 fee.",["Two items cost 6 each.","A person pays x for 4 items.","Half of x is 6."],"Each side is a linear cost.")
# 7.E solve variables both sides
H('c.7.E',3,"Solve: 5x + 3 = 2x + 18","x = 5",["x = 3","x = 7","x = 21/5"],"3x = 15.")
H('c.7.E',4,"Solve: 4(x - 2) = 2x + 6","x = 7",["x = 1","x = 2","x = 14"],"4x - 8 = 2x + 6 gives 2x = 14.")
# 8.A constant of proportionality
H('c.8.A',3,"A table shows (2, 7) and (4, 14). What is the constant of proportionality k = y/x?","3.5",["5","7","0.29"],"7 ÷ 2 = 3.5.")
H('c.8.A',3,"Cheese costs $6 for 4 pounds at a constant rate. What is k, the cost per pound?","1.5",["24","0.67","2"],"6 ÷ 4 = 1.5.")
# 8.B proportional vs not
H('c.8.B',3,"Which equation represents a proportional relationship?","y = 2.5x",["y = 2.5x + 1","y = x²","y = 2 - x"],"Proportional equations have the form y = kx.")
H('c.8.B',3,"A graph is a straight line that does NOT pass through the origin. This relationship is:","non-proportional",["proportional","a constant of 0","undefined"],"Proportional graphs pass through (0, 0).")
# 8.C examples
H('c.8.C',3,"Which situation is proportional?","earning $12 per hour with no starting bonus",["a $20 start fee plus $5 per mile","a pool with 100 gallons that drains at 3 per minute","a ticket costing $8 plus a $3 fee"],"A constant rate from zero is proportional.")
H('c.8.C',3,"Which situation is NOT proportional?","a taxi that charges $4 plus $2 per mile",["a recipe that scales with servings","buying apples at a set price per pound","walking at a constant speed from rest"],"A flat starting fee breaks proportionality.")
# 9 two-variable equation applications
H('c.9',3,"A line has the equation y = 3x + 2. What is the y-value when x = 4?","14",["12","24","11"],"3(4) + 2 = 14.")
H('c.9',3,"A savings plan is y = 50x + 120 where x is weeks. What does 120 represent?","the starting amount",["the savings each week","the number of weeks","the final total"],"The constant term is the amount when x = 0.")
# 10.A circle models
H('c.10.A',3,"Cutting a circle into thin wedges and arranging them in a row forms a shape close to a parallelogram. What formula does this model?","A = πr²",["C = 2πr","A = 2πr","V = πr²h"],"The shape has base half the circumference and height r.")
H('c.10.A',3,"Wrapping a string around a circle and comparing to the diameter models which formula?","C = πd",["A = πd","C = d²","A = r²"],"Circumference is pi times diameter.")
# 10.B surface area
H('c.10.B',3,"A rectangular prism is 5 by 3 by 2. What is its total surface area?","62 square units",["30 square units","31 square units","20 square units"],"2(15 + 10 + 6) = 62.")
H('c.10.B',4,"A square pyramid has a base side of 6 and four triangular faces each with base 6 and slant height 5. What is its lateral area?","60 square units",["30 square units","120 square units","96 square units"],"4 × 1/2 × 6 × 5 = 60.")
# 10.C cylinder volume
H('c.10.C',3,"The volume of a cylinder is found by multiplying the area of the base by:","the height",["the radius","the circumference","the diameter"],"V = Bh.")
H('c.10.C',3,"A cylinder's base area is 12 square cm and its height is 5 cm. What is its volume?","60 cubic cm",["17 cubic cm","30 cubic cm","120 cubic cm"],"12 × 5 = 60.")
# 10.D prism and pyramid
H('c.10.D',3,"A rectangular pyramid and a rectangular prism have congruent bases and equal heights. How do their volumes compare?","The pyramid holds 1/3 as much.",["They are equal.","The pyramid holds twice as much.","The pyramid holds 1/2 as much."],"Three pyramids fill one prism.")
H('c.10.D',3,"How many pyramids with the same base and height fill one rectangular prism?","3",["2","4","6"],"V(pyramid) = 1/3 Bh.")
# 10.E triangular prism and pyramid
H('c.10.E',3,"A triangular pyramid has 1/3 the volume of a triangular prism with congruent bases and equal heights. If the prism volume is 90, the pyramid volume is:","30",["45","60","270"],"90 ÷ 3 = 30.")
H('c.10.E',3,"The volume formula for a triangular pyramid is V =","1/3 Bh",["Bh","1/2 Bh","3Bh"],"B is the area of the triangular base.")
# 10.F cylinder and cone
H('c.10.F',3,"A cone and a cylinder have congruent bases and equal heights. How many cones of water fill the cylinder?","3",["2","4","1"],"A cone is 1/3 of the cylinder.")
H('c.10.F',3,"A cylinder holds 120 cubic cm. A cone with the same base and height holds:","40 cubic cm",["60 cubic cm","240 cubic cm","360 cubic cm"],"120 ÷ 3 = 40.")
# 10.G Pythagorean models
H('c.10.G',3,"Squares are built on the sides of a right triangle. Which statement explains the Pythagorean theorem?","The two smaller squares' areas add to the largest square's area.",["All three squares have the same area.","The largest square is half the smallest.","Only the hypotenuse is squared."],"a² + b² = c².")
H('c.10.G',3,"In a right triangle, the hypotenuse is the side:","opposite the right angle",["adjacent to the right angle","shortest of the three","always equal to a leg"],"It is the longest side across from the 90° angle.")
# 10.H angle facts
H('c.10.H',3,"The exterior angle of a triangle equals the sum of:","the two nonadjacent interior angles",["all three interior angles","the adjacent interior angle","180 degrees"],"An exterior angle equals the remote interior angles added.")
H('c.10.H',3,"Two parallel lines are cut by a transversal. Alternate interior angles are:","congruent",["supplementary","complementary","unrelated"],"Alternate interior angles are equal.")
# 11.A circles
H('c.11.A',3,"A circle has radius 7 cm. Using 22/7 for pi, what is its circumference?","44 cm",["154 cm","22 cm","49 cm"],"2 × 22/7 × 7 = 44.")
H('c.11.A',3,"What is the area of a circle with a radius of 5 in., leaving the answer in terms of pi?","25π square inches",["10π square inches","5π square inches","50π square inches"],"A = πr².")
# 11.B composite
H('c.11.B',3,"A figure is a 6 by 4 rectangle with a triangle of base 6 and height 3 on top. What is the total area?","33 square units",["24 square units","27 square units","42 square units"],"24 + 9 = 33.")
H('c.11.B',4,"A 10 by 8 rectangle has a 4 by 3 rectangle cut out. What is the remaining area?","68 square units",["80 square units","12 square units","92 square units"],"80 - 12 = 68.")
# 11.C lateral and total SA
H('c.11.C',4,"The lateral area of a prism is found by multiplying the base perimeter by:","the height",["the base area","the slant height only","the radius"],"The sides unroll into a rectangle.")
H('c.11.C',4,"A triangular prism has a base perimeter of 12 and a height of 7. What is its lateral area?","84 square units",["19 square units","42 square units","168 square units"],"12 × 7 = 84.")
# 11.D pyramid volume
H('c.11.D',3,"A rectangular pyramid has a 6 by 5 base and a height of 9. What is its volume?","90 cubic units",["270 cubic units","45 cubic units","30 cubic units"],"1/3 × 30 × 9 = 90.")
H('c.11.D',4,"A triangular pyramid has base area 24 and volume 80. What is its height?","10",["20/3","30","3.33"],"80 = 1/3 × 24 × h.")
# 11.E cylinders cones spheres
H('c.11.E',3,"A cylinder has radius 3 and height 10. What is its volume in terms of pi?","90π cubic units",["30π cubic units","60π cubic units","180π cubic units"],"π × 9 × 10.")
H('c.11.E',4,"What is the volume of a sphere with radius 3, in terms of pi?","36π cubic units",["12π cubic units","27π cubic units","108π cubic units"],"4/3 π r³ = 4/3 × 27π.")
H('c.11.E',3,"A cone has radius 6 and height 5. What is its volume in terms of pi?","60π cubic units",["180π cubic units","30π cubic units","90π cubic units"],"1/3 × 36π × 5.")
# 11.F Pythagorean
H('c.11.F',3,"A right triangle has legs 9 and 12. What is the hypotenuse?","15",["21","108","3"],"81 + 144 = 225.")
H('c.11.F',4,"Sides 7, 24 and 25: does this triangle contain a right angle?","Yes, because 49 + 576 = 625.",["No, because 7 + 24 is not 25.","No, because 25 is odd.","Yes, because all sides are positive."],"The converse of the Pythagorean theorem confirms it.")
# 11.G distance
H('c.11.G',4,"What is the distance between (1, 2) and (4, 6)?","5",["7","3","25"],"Legs 3 and 4 give hypotenuse 5.")
H('c.11.G',4,"Points (0, 0) and (5, 12) are plotted. What is the distance between them?","13",["17","7","60"],"25 + 144 = 169.")
# 12.A properties of transformations
H('c.12.A',3,"Which transformation can change the size of a figure?","dilation",["rotation","reflection","translation"],"Only dilations enlarge or shrink.")
H('c.12.A',3,"After a translation, the image and original have:","the same size, shape and orientation",["different sizes","opposite orientation","different shapes"],"A slide preserves everything.")
# 12.B congruence
H('c.12.B',3,"Which transformations always produce a congruent image?","translations, reflections and rotations",["dilations only","dilations and reflections","none of them"],"Rigid motions preserve size and shape.")
H('c.12.B',3,"A figure is dilated by a scale factor of 2. The image is:","similar but not congruent",["congruent","a translation","a reflection"],"Side lengths double.")
# 12.C effect on coordinates
H('c.12.C',3,"Reflect (3, -2) over the x-axis. Where does it land?","(3, 2)",["(-3, -2)","(-3, 2)","(2, 3)"],"Reflecting over the x-axis changes the y sign.")
H('c.12.C',4,"Rotate (4, 1) 90° counterclockwise about the origin. Where does it land?","(-1, 4)",["(1, -4)","(-4, -1)","(1, 4)"],"(x, y) becomes (-y, x).")
# 12.D dilation measurements
H('c.12.D',4,"A square has side 4 and is dilated by scale factor 3. What is the area of the image?","144 square units",["48 square units","36 square units","16 square units"],"New side is 12 and 12² = 144.")
H('c.12.D',3,"A figure is dilated by scale factor 2. Its perimeter becomes:","twice as large",["four times as large","the same","half as large"],"Linear measures multiply by the scale factor.")
# 13.A random sample
H('c.13.A',3,"Which is the best way to choose a random sample of students for a survey?","draw names from a hat containing every student",["ask only your friends","ask only the first ten in line","ask only the athletes"],"Random choice gives each student the same chance.")
H('c.13.A',3,"In a random sample of 50 students, 30 prefer pizza. About what fraction of a population of 500 prefers pizza?","3/5",["3/50","30/500","1/5"],"30/50 = 3/5.")
# 13.B compare populations
H('c.13.B',3,"Sample X has a mean of 82 and sample Y has a mean of 75, with similar spreads. What can be inferred?","Population X tends to score higher than Y.",["Y is certainly higher.","They are identical.","No comparison is possible."],"Compare centers when spreads are alike.")
H('c.13.B',4,"Two samples have the same mean but sample A has much wider spread. Which statement is correct?","Sample B's values are more consistent.",["Sample A's values are more consistent.","Their spreads are equal.","Sample A has no data."],"A narrower spread means less variability.")
# 13.C simulate samples
H('c.13.C',4,"Why generate many random samples of the same size from a known population?","to see how much sample results vary",["to make results equal","to avoid collecting data","to choose a biased sample"],"Repeated sampling shows variability.")
H('c.13.C',3,"As a random sample gets larger, its results usually:","vary less around the population value",["vary more","become biased","stop reflecting the population"],"Larger samples are more consistent.")
# 13.D MAD
H('c.13.D',4,"What is the mean absolute deviation of 2, 4, 6, 8?","2",["4","5","1"],"Mean is 5; deviations are 3, 1, 1, 3 and average 2.")
H('c.13.D',3,"A smaller mean absolute deviation means the data are:","closer to the mean on average",["farther from the mean","all equal","always larger"],"MAD measures average distance from the mean.")
# 14.A budget
H('c.14.A',3,"A budget has income $2,400, savings $300, rent $900 and other expenses $1,000. How much is left unplanned?","$200",["$0","$1,500","$300"],"2,400 - 300 - 900 - 1,000 = 200.")
H('c.14.A',3,"Which is part of a personal budget?","emergency savings",["a favorite color","a vacation photo","a shoe size"],"Budgets include planned savings.")
# 14.B family budget estimator
H('c.14.B',3,"A family budget estimator is used to find the minimum amount a family needs to cover:","basic household costs such as housing, food and transportation",["only luxuries","only entertainment","only taxes"],"It estimates necessary monthly costs.")
H('c.14.B',4,"A family needs $4,800 a month and one adult works 160 hours a month. What hourly wage is needed?","$30",["$48","$20","$160"],"4,800 ÷ 160 = 30.")
# 14.C responsible decisions
H('c.14.C',3,"Which is a financially responsible choice?","saving some money from each paycheck",["spending all income each month","skipping a bill to buy a gadget","taking credit without reading terms"],"Building savings supports future needs.")
H('c.14.C',3,"A person with limited income wants a $1,200 phone. Which is the most responsible plan?","save for several months before buying",["borrow on a high-interest card","skip rent","buy it and hope to pay later"],"Planning avoids costly debt.")
B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'ms_madv7.jsonl'))

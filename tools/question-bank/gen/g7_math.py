#!/usr/bin/env python3
"""Grade 7 Mathematics (TEKS 111.27.b) - original questions. Run: python3 gen/g7_math.py -> batches/g7_math.jsonl"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from mid import *

B, mk = setup('111.27.b.', 707, 'g7_math.jsonl')
R, H, rep = B.R, B.hand, B.rep
def who(): return R.choice(NM)

# ---- 2 sets and subsets of rational numbers
H('2', 2, "Which set of numbers is a subset of the integers?", "whole numbers", ["rational numbers", "fractions between 0 and 1", "decimals only"], "Every whole number is also an integer.")
H('2', 3, "Which statement is true?", "Every integer is a rational number.", ["Every rational number is an integer.", "No whole number is a rational number.", "Every rational number is a whole number."], "An integer n can be written as n/1, so it is rational.")
H('2', 3, "Where would −3/5 be placed in a Venn diagram of whole numbers, integers and rational numbers?", "in the rational numbers only", ["in the integers", "in the whole numbers", "outside every set"], "It is a fraction of integers but is not an integer.")
H('2', 3, "Which number is a rational number but NOT an integer?", "−4.25", ["−4", "0", "12"], "−4.25 = −17/4, which is not a whole amount.")
H('2', 4, "Which set contains ONLY rational numbers that are integers?", "{−6, 0, 9}", ["{−6, 0.5, 9}", "{1/2, 0, 9}", "{−6, 0, 9.1}"], "Integers have no fraction or decimal part.")
H('2', 4, "Why is 0 both a whole number and an integer?", "Whole numbers are part of the integers, and 0 is a whole number", ["Because 0 is negative", "Because 0 is a fraction only", "Because 0 is not a rational number"], "0 belongs to the whole numbers, which are a subset of the integers.")
H('2', 3, "Which number is irrational-looking but actually rational?", "0.25", ["π", "√2", "the non-repeating decimal 0.1010010001…"], "0.25 = 1/4, a ratio of integers.")
H('2', 3, "A terminating decimal like 0.375 is...", "a rational number", ["not a rational number", "an integer", "a whole number"], "0.375 = 375/1000 = 3/8.")

# ---- 3.A add, subtract, multiply, divide rational numbers
def add_rat():
    a = R.randint(-20, 20) / 10; b = R.randint(-20, 20) / 10
    if a == 0 or b == 0: return False
    r = round(a + b, 1)
    return mk('3.A', 3, f"What is {dec(F(str(a)))} + {dec(F(str(b)), 1) if b >= 0 else '(' + dec(F(str(b)), 1) + ')'}?", dec(F(str(r)), 1), [dec(F(str(round(a - b, 1))), 1), dec(F(str(round(-a - b, 1))), 1), dec(F(str(round(r + 1, 1))), 1)], f"Add the decimals carefully with signs: {dec(F(str(r)), 1)}.")
rep(4, add_rat)
def mul_int():
    a = R.randint(2, 12) * R.choice([-1, 1]); b = R.randint(2, 12) * R.choice([-1, 1]); r = a * b
    return mk('3.A', 3, f"What is {sg(a)} × ({sg(b)})?", sg(r), [sg(-r), sg(a + b), sg(a - b)], f"{'Same signs give a positive product' if r > 0 else 'Different signs give a negative product'}: {sg(r)}.", sgc(f"{a}*{b}"))
rep(4, mul_int)
def div_rat():
    d = R.randint(2, 9); q = R.randint(2, 12) * R.choice([-1, 1]); a = d * q * R.choice([-1, 1])
    r = F(a, d)
    if r.denominator != 1: return False
    return mk('3.A', 3, f"What is {sg(a)} ÷ {d}?", sg(int(r)), [sg(-int(r)), sg(int(r) + 1), sg(a - d)], f"{sg(a)} ÷ {d} = {sg(int(r))}.", sgc(f"{a}//{d}"))
rep(3, div_rat)
def frac_add():
    a = F(R.randint(1, 5), R.choice([2, 3, 4, 6, 8])); b = F(R.randint(1, 5), R.choice([2, 3, 4, 6, 8])) * R.choice([-1, 1]); r = a + b
    if r == 0 or a.denominator == 1: return False
    return mk('3.A', 4, f"What is {ims(a)} + ({ims(b)})?" if b < 0 else f"What is {ims(a)} + {ims(b)}?", ims(r), [ims(a - b), ims(a * b), ims(-r)], f"Use a common denominator; the sum is {ims(r)}.")
rep(4, frac_add)
H('3.A', 3, "What is −3/4 + 1/4?", "−1/2", ["−1", "1/2", "−3/16"], "−3/4 + 1/4 = −2/4 = −1/2.")
H('3.A', 3, "What is −2/3 × (−3/4)?", "1/2", ["−1/2", "−9/12", "2"], "Two negatives make a positive: 6/12 = 1/2.")
H('3.A', 4, "What is −5/6 ÷ (−5/12)?", "2", ["−2", "1/2", "25/72"], "−5/6 × (−12/5) = 2.")
H('3.A', 3, "What is −7.5 − (−2.5)?", "−5", ["−10", "5", "10"], "Subtracting a negative is adding: −7.5 + 2.5 = −5.")
H('3.A', 3, "What is 4 − 9?", "−5", ["5", "13", "−13"], "4 − 9 = −5.")

# ---- 3.B apply operations to problems
H('3.B', 3, "At 6 a.m. the temperature was −4°F. By noon it rose 15°F. What was the temperature at noon?", "11°F", ["−19°F", "19°F", "−11°F"], "−4 + 15 = 11.")
H('3.B', 3, "A diver at −30 ft rises 12 ft. What is the diver's new depth?", "−18 ft", ["−42 ft", "18 ft", "−360 ft"], "−30 + 12 = −18.")
H('3.B', 4, "A bank account balance is −$25. A deposit of $60 is made. What is the new balance?", "$35", ["−$85", "$85", "−$35"], "−25 + 60 = 35.")
H('3.B', 4, "A stock changes by −$1.50 each day for 4 days. What is the total change?", "−$6.00", ["−$5.50", "$6.00", "−$0.38"], "4 × (−1.50) = −6.00.")
H('3.B', 4, "A recipe needs 3/4 cup of sugar per batch. How many cups for 2 1/2 batches?", "1 7/8 cups", ["3 1/4 cups", "1 1/4 cups", "3 3/4 cups"], "3/4 × 5/2 = 15/8 = 1 7/8.")
H('3.B', 3, "Eli owes $45 and pays back $18. How would you write his new balance as an integer?", "−$27", ["$27", "−$63", "$63"], "−45 + 18 = −27.")
H('3.B', 4, "The temperature drops 3°F every hour for 5 hours, starting at 2°F. What is the final temperature?", "−13°F", ["−15°F", "13°F", "7°F"], "2 + 5(−3) = −13.")

# ---- 4.A constant rate of change
H('4.A', 3, "A table shows x = 1, 2, 3, 4 and y = 3, 6, 9, 12. What is the constant rate of change?", "3", ["1", "9", "12"], "y increases by 3 each time x increases by 1.")
H('4.A', 3, "A graph is a straight line through (0, 0) and (2, 10). What is the constant rate of change?", "5", ["2", "10", "1/5"], "10 ÷ 2 = 5.")
H('4.A', 4, "A taxi charges $2.50 per mile. Which equation represents the cost c for m miles?", "c = 2.5m", ["c = m + 2.5", "c = m ÷ 2.5", "m = 2.5c"], "Cost is 2.5 times the miles.")
H('4.A', 4, "Which table shows a constant rate of change?", "x: 1, 2, 3 and y: 4, 8, 12", ["x: 1, 2, 3 and y: 4, 5, 7", "x: 1, 2, 3 and y: 2, 5, 11", "x: 1, 2, 3 and y: 9, 4, 1"], "The y-values increase by 4 each time.")
H('4.A', 4, "Which describes a graph of a constant rate of change?", "a straight line", ["a curve that bends", "scattered points", "a vertical jump then flat"], "Constant rate means a straight line.")
H('4.A', 4, "Water drains from a tank at 6 gallons per minute. Which representation matches?", "g = 6m", ["g = m + 6", "g = 6 ÷ m", "g = 6 − m"], "Gallons are 6 times minutes.")

# ---- 4.B unit rates
def unit_rate7():
    r = R.choice([F(3, 2), F(5, 2), F(7, 4), F(9, 4), F(5, 4)]); d = R.choice([2, 4, 8])
    miles = r * d
    return mk('4.B', 3, f"A cyclist rides {ms(miles)} miles in {d} hours. What is the unit rate in miles per hour?", ms(r), [ms(miles * d), ms(d / miles), ms(miles + d)], f"{ms(miles)} ÷ {d} = {ms(r)} miles per hour.")
rep(4, unit_rate7)
H('4.B', 3, "A store sells 4 pounds of grapes for $10. What is the price per pound?", "$2.50", ["$0.40", "$4.00", "$40"], "10 ÷ 4 = 2.5.")
H('4.B', 4, "Brand A: 12 ounces for $3.00. Brand B: 20 ounces for $4.40. Which has the lower unit price?", "Brand B at $0.22 per ounce", ["Brand A at $0.25 per ounce", "Brand A at $0.22 per ounce", "They are equal"], "A is 3.00/12 = 0.25; B is 4.40/20 = 0.22.")
H('4.B', 4, "Mia types 135 words in 3 minutes. What is her rate in words per minute?", "45", ["405", "132", "0.022"], "135 ÷ 3 = 45.")
H('4.B', 3, "A recipe uses 3/4 cup of milk for every 1/2 cup of flour. What is the unit rate of milk per cup of flour?", "1 1/2", ["2/3", "3/8", "1/2"], "3/4 ÷ 1/2 = 3/2.")

# ---- 4.C constant of proportionality
H('4.C', 3, "A table shows x = 2, 4, 6 and y = 10, 20, 30. What is the constant of proportionality k = y/x?", "5", ["2", "10", "30"], "10 ÷ 2 = 5.")
H('4.C', 3, "A proportional relationship has points (3, 12) and (5, 20). What is k?", "4", ["9", "15", "1/4"], "12 ÷ 3 = 4 and 20 ÷ 5 = 4.")
H('4.C', 4, "A recipe uses 6 cups of flour for 4 loaves. What is the constant of proportionality for cups per loaf?", "3/2", ["2/3", "24", "10"], "6 ÷ 4 = 3/2.")
H('4.C', 4, "If y = 7x, what is the constant of proportionality?", "7", ["x", "y", "1/7"], "In y = kx, k = 7.")
H('4.C', 4, "A graph shows a line through (0, 0) and (4, 6). What is k?", "3/2", ["2/3", "10", "24"], "6 ÷ 4 = 1.5.")
H('4.C', 4, "A table has x = 1, 2, 3 and y = 5, 9, 13. Is it proportional?", "No, because y/x is not constant", ["Yes, because y increases", "Yes, because k = 4", "No, because x increases"], "5/1 = 5, 9/2 = 4.5, so the ratio changes.")

# ---- 4.D ratios, rates, percents, percent change
def pct_inc():
    base = R.choice([40, 50, 80, 120, 200]); p = R.choice([10, 20, 25, 50]); new = base + base * p // 100
    if base * p % 100: return False
    return mk('4.D', 4, f"A game price rises from ${base} to ${new}. What is the percent increase?", f"{p}%", [f"{100 - p}%", f"{p * 2}%", f"{new - base}%"], f"Change is {new - base}; {new - base}/{base} = {p}%.", f"'{p}%'")
rep(4, pct_inc)
def pct_dec():
    base = R.choice([40, 50, 80, 100, 200]); p = R.choice([10, 20, 25, 40]); new = base - base * p // 100
    if base * p % 100: return False
    return mk('4.D', 4, f"A jacket price drops from ${base} to ${new}. What is the percent decrease?", f"{p}%", [f"{100 - p}%", f"{p + 10}%", f"{base - new}%"], f"Change is {base - new}; {base - new}/{base} = {p}%.", f"'{p}%'")
rep(4, pct_dec)
def sale_price():
    base = R.choice([20, 40, 60, 80]); p = R.choice([10, 20, 25, 50]); r = base - base * p // 100
    if base * p % 100: return False
    return mk('4.D', 4, f"A ${base} backpack is {p}% off. What is the sale price?", f"${r}", [f"${base * p // 100}", f"${base + base * p // 100}", f"${r + 10}"], f"{p}% of {base} is {base * p // 100}; {base} − {base * p // 100} = {r}.", f"'${r}'")
rep(4, sale_price)
H('4.D', 4, "A price of $50 increases 10% and then decreases 10%. Is the final price $50?", "No, it is $49.50", ["Yes, it is $50", "No, it is $55", "No, it is $45"], "50 × 1.10 = 55, then 55 × 0.90 = 49.50.")
H('4.D', 4, "A population grows from 400 to 500. What is the percent increase?", "25%", ["20%", "100%", "125%"], "100/400 = 25%.")
H('4.D', 3, "What is 15% of 60?", "9", ["15", "4", "90"], "0.15 × 60 = 9.")

# ---- 4.E convert between measurement systems
H('4.E', 3, "About how many centimeters are in 10 inches? (1 inch is about 2.54 centimeters.)", "25.4 cm", ["3.9 cm", "12.54 cm", "254 cm"], "10 × 2.54 = 25.4.")
H('4.E', 3, "About how many pounds are in 5 kilograms? (1 kg ≈ 2.2 lb)", "11 lb", ["2.3 lb", "7.2 lb", "110 lb"], "5 × 2.2 = 11.")
H('4.E', 4, "A race is 5 kilometers. About how many miles is that? (1 mile ≈ 1.6 km)", "about 3.1 miles", ["8 miles", "0.3 miles", "6.6 miles"], "5 ÷ 1.6 ≈ 3.1.")
H('4.E', 4, "About how many liters are in 3 gallons? (1 gallon ≈ 3.8 L)", "11.4 L", ["0.8 L", "6.8 L", "114 L"], "3 × 3.8 = 11.4.")
H('4.E', 4, "Which proportion converts 50 miles to kilometers using 1 mi ≈ 1.6 km?", "1/1.6 = 50/x", ["1/50 = 1.6/x", "1.6/1 = x/50 with x miles", "50/1.6 = x/1 with x pounds"], "One mile is to 1.6 km as 50 miles is to x km: 1/1.6 = 50/x, giving 80 km.")

# ---- 5.A similarity
H('5.A', 3, "Two similar triangles have corresponding sides 3 and 6. The scale factor from the small to the large is...", "2", ["3", "1/2", "9"], "6 ÷ 3 = 2.")
H('5.A', 3, "In similar figures, corresponding angles are...", "congruent", ["supplementary", "always right angles", "unrelated"], "Similar shapes have equal corresponding angles.")
H('5.A', 4, "Triangle ABC ~ triangle DEF. AB = 4, DE = 10. What is the scale factor from ABC to DEF?", "5/2", ["2/5", "40", "6"], "10 ÷ 4 = 5/2.")
H('5.A', 4, "Which is true about similar figures?", "Corresponding sides are proportional", ["All sides are equal", "All areas are equal", "They must be the same size"], "Similar figures have proportional sides.")
H('5.A', 4, "Rectangles with sides 2×3 and 4×6 are...", "similar", ["congruent", "not similar", "equal in area"], "Both ratios 2:3 and 4:6 are equal.")
H('5.A', 4, "Rectangles with sides 2×3 and 4×5 are...", "not similar", ["similar", "congruent", "equal in area"], "2/3 does not equal 4/5.")

# ---- 5.B pi
H('5.B', 2, "π is the ratio of a circle's circumference to its...", "diameter", ["radius", "area", "chord"], "π = C ÷ d.")
H('5.B', 3, "A circle has circumference 31.4 cm and diameter 10 cm. What is 31.4 ÷ 10?", "3.14", ["31.4", "10", "0.314"], "That ratio is about π.")
H('5.B', 3, "Which is the closest approximation of π?", "3.14", ["2.14", "4.13", "1.14"], "π ≈ 3.14.")
H('5.B', 4, "Any circle's circumference divided by its diameter is always...", "the same number, π", ["different for each circle", "the radius", "exactly 3"], "That constant ratio is π.")

# ---- 5.C similar shapes and scale drawings
H('5.C', 3, "A scale drawing uses 1 inch = 5 feet. A room is 4 inches wide in the drawing. How wide is the real room?", "20 feet", ["9 feet", "1.25 feet", "4 feet"], "4 × 5 = 20.")
H('5.C', 3, "On a map, 2 cm represents 10 km. How far apart are two towns that are 7 cm apart on the map?", "35 km", ["14 km", "70 km", "3.5 km"], "Each cm is 5 km: 7 × 5 = 35.")
H('5.C', 4, "A model car is 1/24 the size of a real car. The real car is 192 inches long. How long is the model?", "8 inches", ["216 inches", "4608 inches", "168 inches"], "192 ÷ 24 = 8.")
H('5.C', 4, "A photo 4 in × 6 in is enlarged to be 10 in wide. How tall is the enlargement?", "15 in", ["12 in", "14 in", "16 in"], "Scale factor 10/4 = 2.5; 6 × 2.5 = 15.")
H('5.C', 4, "A 6 ft tall person casts a 4 ft shadow. At the same time a tree casts a 20 ft shadow. How tall is the tree?", "30 ft", ["24 ft", "13 ft", "80 ft"], "6/4 = x/20 gives x = 30.")

# ---- 6.A sample spaces
H('6.A', 3, "A coin is flipped once and a die is rolled once. How many outcomes are in the sample space?", "12", ["8", "7", "6"], "2 × 6 = 12.")
H('6.A', 3, "Two coins are flipped. Which list shows the sample space?", "HH, HT, TH, TT", ["HH, TT", "H, T", "HH, HT, TT"], "There are four equally likely outcomes.")
H('6.A', 4, "A tree diagram has 3 shirts and 2 pants. How many outfits are possible?", "6", ["5", "3", "9"], "3 × 2 = 6.")
H('6.A', 4, "A spinner has colors R, G, B and a coin has H, T. How many outcomes?", "6", ["5", "3", "8"], "3 × 2 = 6.")
H('6.A', 3, "A bag has a red, a blue and a green marble. Two are drawn one at a time without replacement. How many ordered outcomes?", "6", ["3", "9", "4"], "3 × 2 = 6.")

# ---- 6.B simulations
H('6.B', 3, "Which tool could simulate a situation with a 1/6 chance?", "a six-sided die", ["a coin", "a calendar", "a ruler"], "A die has six equally likely faces.")
H('6.B', 4, "Which could simulate a 50% chance event?", "flipping a fair coin", ["rolling a die for a 6", "spinning a spinner with 1/3 section", "drawing 1 of 5 equal cards"], "A fair coin is 50-50.")
H('6.B', 4, "To simulate guessing on a true/false question, you could...", "flip a coin", ["roll a die and count 3", "spin a spinner with 5 sections", "draw from 10 cards"], "True/false has two equal outcomes.")
H('6.B', 3, "Why do we repeat a simulation many times?", "to get results closer to what actually happens in the long run", ["to make the probability 100%", "to change the true probability", "to avoid recording data"], "More trials make results more reliable.")

# ---- 6.C experimental data predictions
H('6.C', 3, "A spinner lands on blue 12 times out of 40 spins. What is the experimental probability of blue?", "3/10", ["12/28", "28/40", "1/12"], "12/40 = 3/10.")
H('6.C', 4, "A basketball player makes 18 of 24 free throws. About how many would you predict out of 40?", "30", ["18", "24", "22"], "18/24 = 3/4; 3/4 × 40 = 30.")
H('6.C', 4, "A coin lands heads 27 times in 50 flips. What is the experimental probability of tails?", "23/50", ["27/50", "1/2", "23/27"], "Tails came up 23 times.")
H('6.C', 4, "In an experiment, an event occurred 15 times in 60 trials. About how many times would you expect it in 200 trials?", "50", ["15", "30", "75"], "15/60 = 1/4; 200 × 1/4 = 50.")

# ---- 6.D theoretical probability
H('6.D', 3, "A bag has 3 red and 5 blue marbles. What is the probability of drawing red?", "3/8", ["3/5", "5/8", "1/3"], "3 red out of 8 marbles.")
H('6.D', 3, "What is the probability of rolling a number greater than 4 on a fair six-sided die?", "1/3", ["1/6", "2/3", "1/2"], "5 and 6 are 2 of 6 outcomes.")
H('6.D', 4, "A fair coin is flipped twice. What is the probability of two heads?", "1/4", ["1/2", "1/3", "2"], "Only HH out of four outcomes.")
H('6.D', 4, "A die is rolled 60 times. About how many times do you expect a 2?", "10", ["6", "12", "30"], "60 × 1/6 = 10.")
H('6.D', 4, "A fair coin is flipped and a fair die is rolled. What is the probability of tails and a 5?", "1/12", ["1/6", "1/2", "1/8"], "1/2 × 1/6 = 1/12.")

# ---- 6.E complement
H('6.E', 3, "The probability of rain is 0.3. What is the probability of no rain?", "0.7", ["0.3", "1.3", "0.03"], "1 − 0.3 = 0.7.")
H('6.E', 3, "P(event) = 2/5. What is P(not event)?", "3/5", ["2/5", "5/2", "1/5"], "1 − 2/5 = 3/5.")
H('6.E', 4, "The probability of picking a vowel from the alphabet is 5/26. What is the probability of a consonant?", "21/26", ["5/21", "1/26", "5/26"], "26 − 5 = 21 consonants.")
H('6.E', 4, "The probabilities of an event and its complement always add up to...", "1", ["0", "2", "100"], "P(A) + P(not A) = 1.")

# ---- 6.F random sample inferences
H('6.F', 3, "A random sample of 50 students shows 20 prefer soccer. About how many of 500 students prefer soccer?", "200", ["20", "100", "250"], "20/50 = 40%; 40% of 500 = 200.")
H('6.F', 4, "Which sample is most likely to represent all students in a school?", "50 students chosen at random from a list of all students", ["the first 50 students in the cafeteria", "50 players from the football team", "50 friends of the survey writer"], "Random samples avoid bias.")
H('6.F', 4, "In a random sample of 40 voters, 24 favor a proposal. Predict how many of 2,000 voters favor it.", "1,200", ["24", "800", "2,400"], "24/40 = 60%; 60% of 2000 = 1200.")
H('6.F', 3, "Why do surveyors use random samples?", "so the sample represents the population fairly", ["to make the survey longer", "to get only one answer", "to avoid analyzing data"], "Random sampling reduces bias.")

# ---- 6.G data in bar graphs, dot plots, circle graphs
H('6.G', 3, "A circle graph shows 25% of students walk to school. If 200 students were surveyed, how many walk?", "50", ["25", "75", "100"], "25% of 200 = 50.")
H('6.G', 3, "A bar graph shows sneakers 12, boots 8, sandals 20. What fraction of the shoes are boots?", "1/5", ["1/3", "2/5", "1/8"], "8/40 = 1/5.")
H('6.G', 4, "A dot plot shows 5 students read 2 books, 3 read 3 books, 2 read 4 books. How many books in all?", "27", ["9", "10", "24"], "10 + 9 + 8 = 27.")
H('6.G', 4, "A circle graph shows red 40%, blue 35%, green 25%. What is the ratio of red to green?", "8:5", ["5:8", "40:35", "3:2"], "40:25 = 8:5.")
H('6.G', 3, "A circle graph's sectors always add up to...", "100%", ["50%", "10%", "1000%"], "They show parts of a whole.")

# ---- 6.H experiments predictions
H('6.H', 3, "Which is more likely to land heads more often: a fair coin flipped 10 times or flipped 1000 times?", "Both are expected to land heads about half the time", ["The 10-flip coin lands heads exactly 5 times", "The 1000-flip coin lands heads exactly 500 times", "The 10-flip coin has a higher chance of heads"], "Results get closer to 1/2 with more trials but are never guaranteed exact.")
H('6.H', 4, "One student flips a coin 10 times and gets 7 heads. Another flips it 100 times and gets 52 heads. Which result is likely closer to the true probability?", "the one from 100 flips", ["the one from 10 flips", "they are equally reliable", "neither is related to the probability"], "More trials give a more reliable estimate.")
H('6.H', 4, "A spinner has 3 equal sections: red, blue, green. After 90 spins, about how many reds do you expect?", "30", ["3", "45", "60"], "90 × 1/3 = 30.")

# ---- 6.I experimental and theoretical probabilities
H('6.I', 4, "Two dice are rolled. How many outcomes have a sum of 7?", "6", ["7", "5", "12"], "(1,6),(2,5),(3,4),(4,3),(5,2),(6,1).")
H('6.I', 4, "Two dice are rolled. What is the probability that the sum is 7?", "1/6", ["1/12", "7/36", "1/7"], "6 out of 36.")
H('6.I', 4, "A student tosses a coin and rolls a die. What is the probability of heads and an even number?", "1/4", ["1/12", "1/2", "1/6"], "1/2 × 1/2 = 1/4.")
H('6.I', 4, "A theoretical probability of 1/4 means that in 100 trials you would expect about...", "25 occurrences", ["4 occurrences", "1 occurrence", "75 occurrences"], "100 × 1/4 = 25.")

# ---- 7 linear relationships
H('7', 3, "A table shows x = 0, 1, 2, 3 and y = 2, 5, 8, 11. Which equation represents it?", "y = 3x + 2", ["y = 2x + 3", "y = x + 2", "y = 5x"], "The slope is 3 and the y-intercept is 2.")
H('7', 3, "In y = 4x + 1, what does the 1 represent?", "the y-value when x = 0", ["the slope", "the x-value when y = 0", "the rate of change"], "It is the starting value.")
H('7', 4, "A plumber charges a $40 fee plus $25 per hour. Which equation gives the cost c for h hours?", "c = 25h + 40", ["c = 40h + 25", "c = 65h", "c = 25h − 40"], "$25 per hour plus the fixed $40.")
H('7', 4, "A graph of y = 2x − 3 crosses the y-axis at...", "(0, −3)", ["(−3, 0)", "(0, 2)", "(2, 0)"], "At x = 0, y = −3.")
H('7', 4, "Which table represents y = 3x − 1?", "x: 0, 1, 2 and y: −1, 2, 5", ["x: 0, 1, 2 and y: 1, 4, 7", "x: 0, 1, 2 and y: −1, 3, 7", "x: 0, 1, 2 and y: 0, 3, 6"], "Substitute each x: 3(0) − 1 = −1, 3(1) − 1 = 2, 3(2) − 1 = 5.")
H('7', 4, "A line has slope 2 and passes through (0, 5). Which equation is correct?", "y = 2x + 5", ["y = 5x + 2", "y = 2x − 5", "y = x + 7"], "Slope-intercept form with m = 2 and b = 5.")
H('7', 3, "Which is a verbal description of y = 5x + 10?", "Start with 10 and add 5 for each x", ["Start with 5 and add 10 for each x", "Multiply x by 15", "Add 5 and 10 to x only once"], "10 is the starting value and 5 is the change per step.")

# ---- 8.A pyramid vs prism volume
H('8.A', 3, "A rectangular pyramid and a rectangular prism have congruent bases and equal heights. The pyramid's volume is what fraction of the prism's volume?", "1/3", ["1/2", "2/3", "1/4"], "Three pyramids fill one prism.")
H('8.A', 3, "A prism holds 90 cubic inches. A pyramid has the same base and height. What is the pyramid's volume?", "30 cubic inches", ["45 cubic inches", "270 cubic inches", "60 cubic inches"], "90 ÷ 3 = 30.")
H('8.A', 4, "How many identical pyramids' worth of water fill a prism with the same base and height?", "3", ["2", "4", "6"], "V(pyramid) = 1/3 V(prism).")
H('8.A', 4, "Which formula gives the volume of a rectangular pyramid?", "V = 1/3 × l × w × h", ["V = l × w × h", "V = 1/2 × l × w × h", "V = 3 × l × w × h"], "One-third of the prism formula.")

# ---- 8.B triangular prism vs pyramid
H('8.B', 3, "A triangular prism and triangular pyramid have congruent bases and equal heights. The pyramid's volume is...", "one-third of the prism's volume", ["one-half of the prism's volume", "equal to the prism's volume", "double the prism's volume"], "V(pyramid) = 1/3 V(prism).")
H('8.B', 4, "A triangular prism has volume 72 cm³. A triangular pyramid has the same base and height. What is its volume?", "24 cm³", ["36 cm³", "216 cm³", "48 cm³"], "72 ÷ 3 = 24.")
H('8.B', 4, "Which formula gives the volume of a triangular pyramid with base area B and height h?", "V = 1/3 Bh", ["V = Bh", "V = 1/2 Bh", "V = 3Bh"], "One-third base area times height.")

# ---- 8.C circles models
H('8.C', 3, "The formula for the circumference of a circle with diameter d is...", "C = πd", ["C = πd²", "C = 2d", "C = d/π"], "Circumference is π times diameter.")
H('8.C', 3, "The formula for the area of a circle with radius r is...", "A = πr²", ["A = 2πr", "A = πd", "A = r²/π"], "Area is π times radius squared.")
H('8.C', 4, "A circle is cut into many thin wedges and rearranged into a rough parallelogram. The base is about half the circumference and the height is the...", "radius", ["diameter", "area", "pi"], "Area ≈ (1/2 × 2πr) × r = πr².")
H('8.C', 4, "The radius of a circle is doubled. What happens to its circumference?", "It doubles", ["It stays the same", "It quadruples", "It is cut in half"], "C = 2πr, so doubling r doubles C.")
H('8.C', 4, "The radius of a circle is doubled. What happens to its area?", "It quadruples", ["It doubles", "It stays the same", "It triples"], "A = πr², and (2r)² = 4r².")

# ---- 9.A volume problems
def prism_vol():
    l = R.randint(3, 12); w = R.randint(2, 9); h = R.randint(2, 10); v = l * w * h
    return mk('9.A', 3, f"A rectangular prism is {l} cm long, {w} cm wide and {h} cm high. What is its volume?", f"{v} cm³", [f"{l * w + h} cm³", f"{2 * (l * w + l * h + w * h)} cm³", f"{l + w + h} cm³"], f"{l} × {w} × {h} = {v}.", f"'{v} cm³'")
rep(4, prism_vol)
def pyr_vol():
    l = R.choice([3, 6, 9]); w = R.randint(2, 8); h = R.randint(3, 9); v = l * w * h // 3
    return mk('9.A', 4, f"A rectangular pyramid has a base {l} in. by {w} in. and height {h} in. What is its volume?", f"{v} in³", [f"{l * w * h} in³", f"{l * w * h // 2 if (l * w * h) % 2 == 0 else l * w * h + 1} in³", f"{l * w + h} in³"], f"1/3 × {l} × {w} × {h} = {v}.", f"'{v} in³'")
rep(4, pyr_vol)
def tri_prism_vol():
    b = R.randint(3, 10); hh = R.choice([2, 4, 6, 8]); L = R.randint(3, 12); v = b * hh // 2 * L
    return mk('9.A', 4, f"A triangular prism has a triangle base of {b} cm and height {hh} cm, and the prism is {L} cm long. What is its volume?", f"{v} cm³", [f"{b * hh * L} cm³", f"{(b + hh) * L} cm³", f"{b * hh // 2 + L} cm³"], f"Base area = 1/2 × {b} × {hh} = {b * hh // 2}; times {L} = {v}.", f"'{v} cm³'")
rep(4, tri_prism_vol)

# ---- 9.B circumference and area
def circ():
    r = R.randint(2, 12); d = 2 * r
    return mk('9.B', 3, f"What is the circumference of a circle with diameter {d} cm? (Use 3.14 for π.)", f"{dec(F(314 * d, 100), 2)} cm", [f"{dec(F(314 * r, 100), 2)} cm", f"{dec(F(314 * d * d, 100), 2)} cm", f"{d + 3.14:.2f} cm"], f"C = πd = 3.14 × {d} = {dec(F(314 * d, 100), 2)}.")
rep(4, circ)
def area_c():
    r = R.randint(2, 10)
    return mk('9.B', 3, f"What is the area of a circle with radius {r} in.? (Use 3.14 for π.)", f"{dec(F(314 * r * r, 100), 2)} in²", [f"{dec(F(314 * 2 * r, 100), 2)} in²", f"{dec(F(314 * r, 100), 2)} in²", f"{dec(F(314 * 4 * r * r, 100), 2)} in²"], f"A = πr² = 3.14 × {r}² = {dec(F(314 * r * r, 100), 2)}.")
rep(4, area_c)
H('9.B', 4, "A circle has circumference 18.84 cm. What is its diameter? (π ≈ 3.14)", "6 cm", ["3 cm", "12 cm", "18 cm"], "18.84 ÷ 3.14 = 6.")

# ---- 9.C composite figures
H('9.C', 4, "A figure is a 6 × 4 rectangle with a right triangle (legs 6 and 3) on one side. What is the total area?", "33", ["24", "27", "42"], "24 + 1/2(6)(3) = 33.")
H('9.C', 4, "A 10 × 6 rectangle has a semicircle with diameter 6 on one end. About what is the area? (π ≈ 3.14)", "74.13", ["60", "88.26", "63.14"], "60 + 1/2 × 3.14 × 3² = 74.13.")
H('9.C', 4, "A square of side 8 has a square of side 3 cut out of a corner. What is the area left?", "55", ["64", "9", "61"], "64 − 9 = 55.")
H('9.C', 4, "To find the area of an L-shaped figure, you can...", "split it into rectangles and add their areas", ["multiply the longest sides only", "add all the sides together", "find the volume"], "Decompose into simple shapes.")

# ---- 9.D surface area
def sa_rect():
    l = R.randint(3, 10); w = R.randint(2, 8); h = R.randint(2, 7); sa = 2 * (l * w + l * h + w * h); lat = 2 * h * (l + w)
    return mk('9.D', 4, f"A rectangular prism is {l} cm by {w} cm by {h} cm. What is its total surface area?", f"{sa} cm²", [f"{lat} cm²", f"{l * w * h} cm²", f"{l * w + l * h + w * h} cm²"], f"2(lw + lh + wh) = {sa}.", f"'{sa} cm²'")
rep(4, sa_rect)
def sa_lat():
    l = R.randint(3, 10); w = R.randint(2, 8); h = R.randint(2, 7); lat = 2 * h * (l + w)
    return mk('9.D', 4, f"A rectangular prism has a {l} cm by {w} cm base and is {h} cm tall. What is its lateral surface area (not including the top and bottom)?", f"{lat} cm²", [f"{2 * (l * w + l * h + w * h)} cm²", f"{l * w * 2} cm²", f"{l * w * h} cm²"], f"Perimeter of base × height = {2 * (l + w)} × {h} = {lat}.", f"'{lat} cm²'")
rep(4, sa_lat)
H('9.D', 4, "A square pyramid has a square base of side 6 and four triangle faces, each with base 6 and height 5. What is the total surface area?", "96", ["66", "36", "150"], "Base 36 + 4 × (1/2 × 6 × 5) = 36 + 60 = 96.")
H('9.D', 4, "A net of a triangular prism contains how many faces?", "5", ["4", "6", "3"], "2 triangles + 3 rectangles.")

# ---- 10 write two-step equations and inequalities
H('10.A', 3, "Ava buys 3 notebooks and a $2 pen for $11 in all. If n is the price of a notebook, which equation fits?", "3n + 2 = 11", ["3n − 2 = 11", "n + 5 = 11", "3(n + 2) = 11"], "3 notebooks plus a $2 pen cost $11.")
H('10.A', 4, "A taxi charges $3 plus $2 per mile. Max has $15. Which inequality shows the miles m he can ride?", "2m + 3 ≤ 15", ["2m + 3 ≥ 15", "3m + 2 ≤ 15", "2m − 3 ≤ 15"], "He cannot spend more than $15.")
H('10.A', 4, "Twice a number decreased by 7 is 19. Which equation represents this?", "2n − 7 = 19", ["2(n − 7) = 19", "2n + 7 = 19", "n − 14 = 19"], "2n then subtract 7.")
H('10.A', 4, "A gym charges $20 to join and $15 per month. Which equation gives the total cost C for m months?", "C = 15m + 20", ["C = 20m + 15", "C = 35m", "C = 15m − 20"], "$20 once plus $15 each month.")
H('10.A', 3, "The sum of 5 and three times a number is greater than 20. Which inequality?", "3n + 5 > 20", ["3n + 5 < 20", "3(n + 5) > 20", "n + 15 > 20"], "Three times n plus 5 is greater than 20.")

# ---- 10.B number lines
H('10.B', 3, "The solution of 2x + 1 = 9 is x = 4. Where is it graphed on a number line?", "a point at 4", ["a point at 9", "an arrow from 4 to the right", "a point at 1"], "An equation has a single solution point.")
H('10.B', 4, "Which graph shows x < 3?", "an open circle at 3 with an arrow to the left", ["a closed circle at 3 with an arrow to the left", "an open circle at 3 with an arrow to the right", "a closed circle at 3 with an arrow to the right"], "Less than excludes 3 and goes left.")
H('10.B', 4, "Which graph shows 2x + 1 ≥ 7?", "a closed circle at 3 with an arrow to the right", ["an open circle at 3 with an arrow to the right", "a closed circle at 3 with an arrow to the left", "an open circle at 4 with an arrow to the right"], "2x ≥ 6, so x ≥ 3.")
H('10.B', 4, "A number line shows an open circle at −2 with an arrow to the right. Which inequality?", "x > −2", ["x ≥ −2", "x < −2", "x ≤ −2"], "Open circle, greater than.")

# ---- 10.C write real-world problem
H('10.C', 4, "Which situation matches 4x + 3 = 27?", "Four friends each buy a ticket costing x dollars plus $3 for parking, and the total is $27", ["Someone buys 3 items for x dollars and pays $27", "Four friends share $3 and $27", "A ticket costs $4 less than $27"], "4 tickets plus a $3 fee make $27.")
H('10.C', 4, "Which situation matches 5n − 6 = 24?", "Five bags each have n marbles; after removing 6 there are 24", ["Five bags have 6 marbles each and 24 are removed", "Someone adds 6 to 24 and divides by 5", "A bag has 5 marbles and 6 more"], "5 groups of n, minus 6, equals 24.")
H('10.C', 4, "Which situation matches 2x + 5 < 21?", "Two tickets at x dollars plus a $5 fee cost less than $21", ["Two tickets cost more than $21", "Five tickets cost $2 each", "A $21 ticket costs $5 less"], "2x + 5 is less than 21.")

# ---- 11.A model and solve two-step
def two_step():
    a = R.randint(2, 9); x = R.randint(2, 15); b = R.randint(1, 12); c = a * x + b
    return mk('11.A', 3, f"What is the solution of {a}x + {b} = {c}?", f"x = {x}", [f"x = {c - b}", f"x = {(c + b) // a if (c + b) % a == 0 else x + 1}", f"x = {c // a if c % a == 0 else x - 1}"], f"Subtract {b}: {a}x = {c - b}; divide by {a}: x = {x}.", f"'x = {x}'")
rep(6, two_step)
def two_step_sub():
    a = R.randint(2, 9); x = R.randint(2, 15); b = R.randint(1, 12); c = a * x - b
    return mk('11.A', 4, f"What is the solution of {a}x − {b} = {c}?", f"x = {x}", [f"x = {x - 1}", f"x = {c - b}", f"x = {c + b}"], f"Add {b}: {a}x = {c + b}; divide by {a}: x = {x}.", f"'x = {x}'")
rep(4, two_step_sub)
def div_step():
    a = R.randint(2, 8); x = R.randint(2, 12) * a; b = R.randint(1, 10); c = x // a + b
    return mk('11.A', 4, f"What is the solution of x/{a} + {b} = {c}?", f"x = {x}", [f"x = {c - b}", f"x = {(c + b) * a}", f"x = {c * a + b}"], f"Subtract {b}: x/{a} = {c - b}; multiply by {a}: x = {x}.", f"'x = {x}'")
rep(4, div_step)
H('11.A', 4, "Which values of x make 3x + 2 > 14 true?", "x > 4", ["x < 4", "x > 12", "x < 12"], "3x > 12 so x > 4.")
H('11.A', 4, "What is the solution to 2x − 5 ≤ 9?", "x ≤ 7", ["x ≥ 7", "x ≤ 2", "x ≤ 14"], "2x ≤ 14 so x ≤ 7.")

# ---- 11.B check
H('11.B', 3, "Is x = 5 a solution of 3x + 4 = 19?", "Yes, because 3(5) + 4 = 19", ["No, because 3(5) + 4 = 20", "No, because 3(5) + 4 = 24", "Yes, because 5 + 4 = 19"], "Substitute 5.")
H('11.B', 3, "Which value of x makes 2x − 1 = 9 true?", "5", ["4", "10", "3"], "2(5) − 1 = 9.")
H('11.B', 4, "Which value of x makes 4x + 1 < 13 true?", "2", ["3", "4", "5"], "4(2) + 1 = 9 < 13, but 4(3) + 1 = 13 is not less than 13.")
H('11.B', 4, "Which values make 2x − 3 ≥ 5 true?", "4 and 6", ["3 and 4", "1 and 2", "2 and 3"], "2(4) − 3 = 5 and 2(6) − 3 = 9.")

# ---- 11.C geometry equations
H('11.C', 3, "Two angles of a triangle measure 50° and 60°. Which equation finds the third angle x?", "x + 50 + 60 = 180", ["x + 50 + 60 = 360", "x = 50 + 60", "x − 50 − 60 = 90"], "Angles in a triangle add to 180°.")
def tri_x():
    a = R.randint(25, 80); b = R.randint(25, 80); x = 180 - a - b
    if x < 15: return False
    return mk('11.C', 3, f"A triangle has angles {a}°, {b}° and x°. What is x?", f"{x}", [f"{a + b}", f"{360 - a - b}", f"{x + 10}"], f"x = 180 − {a} − {b} = {x}.", f"'{x}'")
rep(4, tri_x)
H('11.C', 3, "Two angles form a straight line (supplementary). One is 115°. What is the other?", "65°", ["75°", "245°", "25°"], "180 − 115 = 65.")
H('11.C', 3, "Two angles are complementary. One is 28°. What is the other?", "62°", ["152°", "72°", "28°"], "90 − 28 = 62.")
H('11.C', 4, "Vertical angles are...", "congruent (equal in measure)", ["supplementary", "complementary", "always 90°"], "Opposite angles formed by intersecting lines are equal.")
H('11.C', 4, "Two angles are supplementary. One is 3x° and the other is 60°. What is x?", "40", ["20", "60", "120"], "3x + 60 = 180 gives x = 40.")
H('11.C', 4, "Two angles are complementary. One is (2x + 10)° and the other is 40°. What is x?", "20", ["10", "25", "40"], "2x + 10 + 40 = 90 gives x = 20.")

# ---- 12.A compare two groups
H('12.A', 3, "Two dot plots have the same center but one is more spread out. How do the two groups compare?", "They have the same center but different spreads", ["They are identical", "They have different centers", "One has no data"], "Spread is about how far the values are from the center.")
H('12.A', 3, "Box plot A has a median of 40 and box plot B has a median of 55. Which statement is true?", "Group B has the higher center", ["Group A has the higher center", "The groups have equal centers", "Group A has more data"], "The median is a measure of center.")
H('12.A', 4, "Box plot A has an IQR of 8 and box plot B has an IQR of 20. Which group has more variability in its middle half?", "Group B", ["Group A", "They are equal", "Cannot be told"], "A larger IQR means more spread.")
H('12.A', 4, "On comparative dot plots, group X's data are clustered near 10 and group Y's are clustered near 30. Which comparison is correct?", "Group Y has the greater center", ["Group X has the greater center", "They have the same center", "They have the same shape"], "Y clusters at higher values.")

# ---- 12.B inferences
H('12.B', 3, "A random sample of 100 shoppers shows 35 buy online. About what percent of all shoppers buy online?", "35%", ["100%", "65%", "3.5%"], "35 out of 100.")
H('12.B', 4, "In a random sample of 80 students, 20 walk to school. Of 1,200 students, about how many walk?", "300", ["20", "240", "600"], "20/80 = 25%; 25% of 1200 = 300.")
H('12.B', 4, "Why can a larger random sample give a better estimate?", "It usually represents the population more closely", ["It makes the population smaller", "It removes all variability", "It guarantees an exact answer"], "More data reduce chance variation.")

# ---- 12.C compare two populations
H('12.C', 4, "Random samples of 10 seventh graders and 10 sixth graders show mean sleep of 8.2 and 8.8 hours. What can be said informally?", "Sixth graders in the samples sleep about 0.6 hour more on average", ["Seventh graders sleep more", "They sleep the same", "Nothing can be compared"], "8.8 − 8.2 = 0.6.")
H('12.C', 4, "Two samples have means of 72 and 74 with large variability in both. What is a reasonable conclusion?", "The difference between the groups is small compared with the variability", ["The groups are clearly different", "The first group is always lower", "The second group has no variability"], "A difference smaller than the spread is not strong evidence.")
H('12.C', 4, "Mean battery life of Brand A is 10 h and of Brand B is 14 h, with low variability in both. What might you infer?", "Brand B likely lasts longer", ["Brand A likely lasts longer", "They last the same", "Variability proves nothing"], "The difference is large relative to the spread.")

# ---- 13 personal financial literacy
H('13.A', 3, "A $40 shirt has a sales tax of 8%. What is the tax?", "$3.20", ["$8.00", "$0.32", "$32.00"], "0.08 × 40 = 3.20.")
H('13.A', 3, "A purchase costs $25 before 6% sales tax. What is the total?", "$26.50", ["$25.06", "$31", "$1.50"], "Tax is $1.50 and total is $26.50.")
H('13.A', 4, "Eli earns $400 a week and 10% is withheld for income tax. How much tax is withheld?", "$40", ["$4", "$360", "$10"], "10% of 400 = 40.")
H('13.A', 4, "Raj earns $800 and 12% is withheld for income tax. What is his pay after tax?", "$704", ["$96", "$788", "$896"], "Tax is $96; 800 − 96 = 704.")
H('13.B', 3, "Which is a fixed expense in a personal budget?", "monthly rent", ["entertainment", "restaurant meals", "gifts"], "Fixed expenses stay the same each month.")
H('13.B', 3, "Which is a variable expense?", "groceries", ["rent payment", "car loan payment", "insurance premium"], "Variable expenses change.")
H('13.B', 4, "Which belongs in a personal budget?", "income, savings, taxes, and fixed and variable expenses", ["only income", "only entertainment", "only savings"], "A budget tracks income and spending.")
H('13.B', 4, "Why include savings for emergencies in a budget?", "to cover unexpected costs without borrowing", ["to spend on gifts", "to lower taxes automatically", "to avoid earning income"], "An emergency fund protects against surprises.")
H('13.C', 3, "A net worth statement is calculated as assets minus...", "liabilities", ["income", "taxes", "savings"], "Net worth = assets − liabilities.")
H('13.C', 4, "A person has assets of $12,000 and liabilities of $4,500. What is the net worth?", "$7,500", ["$16,500", "$12,000", "−$7,500"], "12,000 − 4,500 = 7,500.")
H('13.C', 3, "Which is a liability?", "a student loan", ["a savings account", "a bicycle you own", "cash in a wallet"], "A liability is money owed.")
H('13.D', 3, "A family budget estimator can be used to find...", "the minimum budget and wage needed to meet basic needs", ["the winning lottery numbers", "the price of one item", "a loan interest rate only"], "It estimates a household's basic cost of living.")
H('13.D', 4, "A family estimator shows $3,900 needed per month. How much is that per year?", "$46,800", ["$3,900", "$7,800", "$39,000"], "3,900 × 12 = 46,800.")
def simple_int():
    P = R.choice([200, 500, 1000, 2000]); r = R.choice([2, 3, 4, 5]); t = R.choice([2, 3, 4, 5]); I = P * r * t // 100
    return mk('13.E', 4, f"How much simple interest is earned on ${P} at {r}% per year for {t} years?", f"${I}", [f"${P + I}", f"${P * r // 100}", f"${I * 2}"], f"I = Prt = {P} × {r / 100:g} × {t} = {I}.", f"'${I}'")
rep(4, simple_int)
H('13.E', 4, "$1,000 earns 5% compound interest, compounded yearly. What is the balance after 2 years?", "$1,102.50", ["$1,100.00", "$1,050.00", "$1,200.00"], "1000 × 1.05 × 1.05 = 1,102.50.")
H('13.E', 4, "Compared with simple interest, compound interest earns...", "interest on both the principal and earlier interest", ["interest only on the principal", "no interest", "less interest in every case"], "Compounding adds interest on interest.")
H('13.F', 3, "A $50 item has a $10 rebate. What is the final cost after the rebate?", "$40", ["$60", "$10", "$45"], "50 − 10 = 40.")
H('13.F', 4, "A $60 jacket is 25% off. A $50 jacket has a $2 coupon. Which costs less?", "The $60 jacket at $45", ["The $50 jacket at $48", "The $60 jacket at $55", "They cost the same"], "60 × 0.75 = 45 and 50 − 2 = 48, so the first costs less.")
H('13.F', 3, "A sale takes 30% off a $90 pair of shoes. What is the sale price?", "$63", ["$27", "$60", "$87"], "30% of 90 is 27; 90 − 27 = 63.")

# --- END
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "batches", "g7_math.jsonl"))
print("saved", len(B.out), "questions")

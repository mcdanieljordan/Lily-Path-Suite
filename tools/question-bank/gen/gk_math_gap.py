#!/usr/bin/env python3
"""Kindergarten Math gap fill: 111.2.b.4 (coins) and 111.2.b.5 (number word list). Hand written, 7 each."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
B = Bank('111.2.b.', 811, own='gk_math_gap.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 4: identify U.S. coins by name
H('4', 2, "Which coin is called a penny?", "the brown coin worth 1 cent", ["the silver coin worth 5 cents", "the silver coin worth 10 cents", "the silver coin worth 25 cents"], "A penny is brown and worth 1 cent.")
H('4', 2, "Which coin is the smallest silver coin?", "a dime", ["a nickel", "a quarter", "a penny"], "The dime is the smallest silver coin.")
H('4', 2, "What is the name of the biggest coin you can pay with that is worth 25 cents?", "a quarter", ["a dime", "a nickel", "a penny"], "A quarter is worth 25 cents.")
H('4', 2, "Which coin is a nickel?", "the silver coin worth 5 cents", ["the brown coin worth 1 cent", "the smallest silver coin", "the coin worth 25 cents"], "A nickel is worth 5 cents.")
H('4', 2, "Why do people use coins?", "to pay for things", ["to build a house", "to cook food", "to make shadows"], "Coins are money used to buy things.")
H('4', 3, "A girl has a coin that is brown. What is it?", "a penny", ["a dime", "a nickel", "a quarter"], "Only the penny is brown.")
H('4', 3, "Which group has only coins?", "penny, nickel, dime", ["penny, button, dime", "nickel, key, quarter", "dime, shell, penny"], "All three are U.S. coins.")

# 5: recite numbers to 100 by ones and tens
H('5', 2, "What number comes next? 7, 8, 9, __", "10", ["11", "6", "70"], "Counting by ones: after 9 comes 10.")
H('5', 2, "What number comes next? 10, 20, 30, __", "40", ["31", "50", "13"], "Counting by tens adds 10 each time.")
H('5', 2, "Count by tens. What number is missing? 20, 30, __, 50", "40", ["35", "45", "60"], "40 comes between 30 and 50.")
H('5', 3, "Start at 48. What number comes next when counting by ones?", "49", ["50", "58", "47"], "One more than 48 is 49.")
H('5', 3, "What number comes next? 98, 99, __", "100", ["101", "90", "89"], "After 99 comes 100.")
H('5', 3, "Count by tens from 60. What numbers come next?", "70, 80, 90", ["61, 62, 63", "65, 70, 75", "80, 100, 120"], "Adding 10 each time gives 70, 80, 90.")
H('5', 3, "Which group is counting by ones?", "35, 36, 37, 38", ["35, 45, 55, 65", "35, 37, 39, 41", "35, 40, 45, 50"], "Counting by ones goes up one each time.")

B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'gk_math_gap.jsonl'))
print("saved", len(B.out))

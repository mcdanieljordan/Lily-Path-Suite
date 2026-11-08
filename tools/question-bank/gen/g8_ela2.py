#!/usr/bin/env python3
"""Grade 8 ELA supplement: 10.D.i (sentence structure) and 9.D (figurative language) - items dropped as duplicates of earlier grades."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
B = Bank('110.24.b.', 964, own='g8_ela2.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)
H('10.D.i', 3, "Which group of words is a run-on sentence?", "The concert ended we walked to the car.", ["The concert ended, and we walked to the car.", "After the concert ended, we walked to the car.", "The concert ended; we walked to the car."], "Two independent clauses with no punctuation or conjunction.")
H('10.D.i', 4, "Which sentence has correct subject-verb agreement?", "Neither the captain nor the sailors were afraid of the waves.", ["Neither the captain nor the sailors was afraid of the waves.", "Neither the captain nor the sailors is afraid of the waves.", "Neither the captain nor the sailors be afraid of the waves."], "The verb agrees with the nearer subject, sailors.")
H('10.D.i', 3, "Which group of words is a fragment?", "Although the pitcher threw a perfect game.", ["The pitcher threw a perfect game.", "The crowd cheered the pitcher.", "Fans stood and clapped."], "A dependent clause is not a complete sentence.")
H('10.D.i', 4, "Which sentence fixes this comma splice? 'The lights flickered, the room went dark.'", "The lights flickered, and the room went dark.", ["The lights flickered, the room went dark, quickly.", "The lights flickered the room, went dark.", "The lights, flickered the room went dark."], "A comma plus conjunction joins two independent clauses.")
H('9.D', 3, "'The old car coughed and groaned up the hill' is an example of...", "personification", ["simile", "hyperbole", "an idiom"], "A machine is given human actions.")
B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g8_ela2.jsonl'))
print("saved", len(B.out))

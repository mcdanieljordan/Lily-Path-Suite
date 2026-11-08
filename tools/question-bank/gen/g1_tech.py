#!/usr/bin/env python3
"""Grade 1 Technology Applications: TEKS 126.2.c - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('126.', 951, own='g1_tech.jsonl')

load(B, """
2.c.C|3|Making a list of directions that moves a toy robot across a grid is creating a...|sequence of code|game score|story title|snack list|Code is steps in order.
2.c.C|3|A block program tells a character: step, step, turn. If you swap the steps and the turn, the character will...|end up somewhere different|stay the same|disappear|sing|Order changes the result.
2.c.4|3|Phones and video calls help families far away to talk. This shows how technology has impacted...|communities|trees|clouds|rocks|Technology changes how people connect.
2.c.4|3|Computers in libraries help people find books. This is an example of technology helping...|a community|a lake|a mountain|an animal|Technology affects communities.
2.c.6|2|A respectful way to talk to a classmate online is to use...|kind words|mean words|capital letters to yell|silly insults|Respect applies online.
2.c.6|3|If a friend posts something and you disagree, a respectful response is to...|say it politely|make fun of them|ignore all rules|share their secret|Disagree respectfully.
2.c.1.A|2|You need to wash your hands. The first step is to...|turn on the water|dry your hands|put on a coat|leave the room|Break the task into ordered steps.
2.c.1.A|3|Breaking a big problem into small, ordered pieces is called...|decomposing|ignoring|forgetting|guessing|Decompose means break down.
2.c.1.B|2|Every morning you brush teeth after breakfast. The pattern in your routine is...|the same order each day|a different order each day|no order|no steps|Patterns repeat.
2.c.1.B|3|Many recipes start with gathering ingredients. This is a pattern in solving...|everyday tasks|nothing|only math|only art|Patterns appear in tasks.
2.c.1.C|3|Writing numbered directions for tying your shoe is making a simple...|algorithm|animal|apple|anthem|Algorithms are step-by-step instructions.
2.c.1.C|3|A good algorithm for brushing your teeth lists the steps...|in the right order|in a random order|with one step missing|with no steps|Order matters.
2.c.3.A|3|Listening carefully and thinking quickly about new ideas helps you with a...|design process|nap|recess game|lunch|Mental agility supports design.
2.c.3.B|3|Asking questions, brainstorming and drawing a plan are parts of a...|design process|lunch menu|spelling test|bus ride|Design processes solve problems.
2.c.3.B|3|Drawing the order of events for your project before building it is called...|storyboarding|forgetting|hiding|sleeping|Storyboards plan visually.
2.c.5.A|3|Asking classmates their favorite pet and writing the answers is collecting...|data|shoes|toys|trash|Data is collected information.
2.c.5.A|3|Tracking how many students ride the bus each day is collecting data about people's...|daily routines|foods|clothes|shoes|Routines can be counted.
2.c.5.B|3|A keyword you type into a search tool helps the computer to...|find matching information|turn off|draw a picture|play music only|Keywords drive searches.
2.c.7.A|3|Following your school's rules for devices, called the AUP, means you show...|acceptable use|bad habits|no rules|silly play|Follow the AUP.
2.c.7.B|3|A song or picture online belongs to its maker. Asking permission before using it shows respect for the...|owner|ocean|oven|ear|Digital content has owners.
2.c.8.A|2|To keep your account safe, you should never share your...|password|favorite color|shoe size|lunch box|Protect login information.
2.c.8.A|3|Logging off a school computer when you finish keeps your account...|safe|messy|loud|slow|Log off to protect.
2.c.8.B|3|Which is safe to share online?|that you like soccer|your home address|your password|your phone number|Hobbies are safe; identifying info is not.
2.c.8.B|3|Which is unsafe to share online?|where you go to school and live|your favorite animal|your favorite song|your favorite book|Identifying information is unsafe.
2.c.8.C|3|Using the internet to repeatedly say mean things to someone is called...|cyberbullying|sharing|studying|typing|Cyberbullying is online meanness.
2.c.8.C|3|If you see cyberbullying, you should tell...|a trusted adult|nobody|a stranger|the bully|Get help from an adult.
2.c.9.A|3|Using a drawing app to make your own poster is creating an...|original product|copy|mistake|erase|Original work is new.
2.c.9.B|2|A printer that makes paper copies is an...|output device|input device|animal|chair|Output devices give results.
2.c.9.B|3|A keyboard and a mouse are...|input devices|output devices|software|snacks|Input devices send data in.
2.c.9.B|3|The programs that tell a computer what to do are called...|software|hardware|a desk|a screen|Software is a program.
2.c.9.C|3|Putting your finished work in a named folder is file...|management|painting|dancing|jumping|File management keeps work organized.
2.c.9.C|3|Working with a classmate on the same online document is...|collaboration|competition|erasing|hiding|Collaboration means working together.
2.c.9.D|2|When you type, your feet should be...|flat on the floor|up on the desk|crossed over the chair|in the air|Good ergonomics.
2.c.9.D|3|Good keyboarding means keeping your wrists...|straight and relaxed|bent sharply|pressed down hard|raised up high|Posture protects hands.
2.c.9.E|2|The key you hold to make a capital letter is...|shift|space bar|backspace|enter|Shift makes uppercase letters.
2.c.9.E|3|To erase the last letter you typed, press...|backspace|shift|space bar|caps lock|Backspace deletes.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g1_tech.jsonl'))
print("saved", len(B.out), "questions")

#!/usr/bin/env python3
"""Kindergarten Technology Applications: TEKS 126.1.c - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('126.', 950, own='gk_tech.jsonl')

load(B, """
1.c.2|2|You write steps to get a friend to the door: forward, forward, turn, forward. These steps are a...|sequence of directions|poem|song|picture|Code is a list of steps in order.
1.c.2|3|In a maze game, you drag blocks that tell the character to move. What are you making?|code|a drawing|a snack|a song|Drag-and-drop blocks make a program.
1.c.2|3|Which order of steps is right for getting to the door?|Walk forward, then turn, then walk forward|Turn, then sleep, then walk|Sing, then sit, then stop|Jump, then hide, then nap|Steps must be in the right order.
1.c.5|2|You are playing on a tablet and a classmate wants a turn. A responsible thing to do is...|take turns kindly|grab it|hide it|yell|Responsible behavior is kind and fair.
1.c.5|3|In an online class, you should speak to others...|politely|rudely|with mean words|by shouting|Be kind online.
1.c.1.A|2|To make a sandwich, you first break the job into small...|steps|clouds|toys|songs|Decomposing means breaking into smaller pieces.
1.c.1.A|3|Cleaning your room is a big job. Putting books away is one small piece. This is called...|breaking a problem into parts|breaking a toy|making a mess|hiding a job|Decomposing a task.
1.c.1.B|2|Sun, moon, sun, moon, sun, ... What comes next?|the moon|the sun again|a star|a cloud|Patterns repeat.
1.c.1.B|3|Two claps, one stomp, two claps, one stomp, two claps. You predict what comes next is...|a single foot stomp|three claps|a jump|silence|Use the pattern to predict.
1.c.1.C|2|Instructions that tell what to do one step after another are an...|algorithm|apple|animal|album|Algorithms are step-by-step instructions.
1.c.1.C|3|Which words help put steps in order?|first, next, then, last|big, red, soft, fast|cat, dog, fish, bird|up, down, left, right only|Sequence words show order.
1.c.3.A|2|Listening and following directions helps you...|do a project well|forget a project|lose a project|skip a project|Following directions is a design skill.
1.c.3.B|3|Asking questions and drawing a plan before building something is part of a...|design process|nap time|snack time|recess|Design processes include asking and planning.
1.c.3.B|3|Drawing pictures of your idea in order before you make it is called...|storyboarding|erasing|hiding|sleeping|A storyboard plans steps in pictures.
1.c.4.A|2|Facts that are collected about the weather are called...|data|toys|snacks|shoes|Data is information collected.
1.c.4.A|3|Counting how many students picked each fruit gives us...|data|a song|a toy|a shoe|Counting collects information.
1.c.4.B|2|A computer can help you look for information. This is called...|searching|sleeping|painting|dancing|Devices can search for information.
1.c.6.A|2|The rules for using school computers and tablets tell you how to use them...|the right way|any way|never|wrong|Acceptable use policies set the rules.
1.c.6.A|3|Following the acceptable use rules means using school devices...|only for school work and rules|for anything|for games all day|without asking|Use devices as the policy says.
1.c.6.B|3|A picture or song online was made by someone. That means it has an...|owner|ocean|oven|ear|Digital content has owners.
1.c.7.A|2|To keep your account safe, you should not share your...|password|favorite color|pet's name tag|shoes|Never share login information.
1.c.7.A|3|When you finish using a device, you should...|log off|leave it on and walk away|tell a friend your password|break it|Logging off protects your account.
1.c.7.B|3|Which is safe to share online?|a favorite animal|your home address|your password|your phone number|Hobbies and likes are safe; identifying information is not.
1.c.7.B|3|Which is NOT safe to share online?|where you live|a favorite color|a favorite food|a favorite game|Do not share identifying information.
1.c.8.A|2|A tablet, a laptop and a school website are all ways to...|learn and do activities|sleep|swim|bake|Devices and sites can be used to learn.
1.c.8.B|2|A mouse or keyboard that sends information to a computer is an...|input device|output device|sandwich|window|Input devices send information in.
1.c.8.B|3|A screen or a printer that shows information from a computer is an...|output device|input device|snack|bed|Output devices show results.
1.c.8.B|3|The programs on a computer, like a drawing app, are called...|software|hardware|a desk|a chair|Software is a program.
1.c.8.C|2|To use a drawing app, you first...|open the app|close the lid|walk away|turn it upside down|Open the application to use it.
1.c.8.C|3|After you make a picture on the computer, you should...|save it|forget it|throw it|hide the computer|Saving keeps your work.
1.c.8.D|2|Good keyboarding means sitting...|up tall with feet on the floor|slumped over|on the table|upside down|Ergonomics protects the body.
1.c.8.D|3|When you type, your hands should rest...|on the home row keys|on your head|under the desk|behind your back|Good hand position.
1.c.8.E|2|The long key at the bottom that makes a space between words is the...|space bar|backspace|enter|tab|The space bar makes spaces.
1.c.8.E|3|The key that erases the last letter you typed is the...|backspace|space bar|shift|caps lock|Backspace deletes the previous character.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'gk_tech.jsonl'))
print("saved", len(B.out), "questions")

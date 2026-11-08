#!/usr/bin/env python3
"""Social Studies K-5 gap fill: leaf standards with no question yet. Original, hand written.
Codes are full (prefix is empty) so one file can cover several grades."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('113.', 916, own='gap_ss.jsonl')

load(B, """
12.c.16.A|2|A first grader says, "Our class has 12 desks." Which is a fact that can be checked by counting?|There are 12 desks in the room.|Desks are the best furniture.|Everyone loves desks.|Desks are boring.|A fact can be proven with evidence.
12.c.16.C|2|You want to learn what a firefighter does. Which is a good oral source?|asking a firefighter who visits the class|guessing from a cartoon|asking a stranger about cooking|reading a recipe|Talking to a real person who does the job is a valid source.
12.c.17.C|3|After a class trip to a farm, which shows what you learned in a picture?|drawing the animals you saw|drawing nothing|copying a friend's name|erasing the page|You can communicate learning by drawing.
12.c.17.F|2|While a classmate is speaking during circle time, you should...|look at them and wait your turn|talk over them|walk away|make loud noises|Respectful listening follows classroom rules.
13.c.15.A|3|A second grader reads that a town has one library. Which statement is a fact?|The town has one library.|The library is the prettiest building.|Everybody should visit it daily.|It is the best place ever.|Facts can be shown with evidence.
13.c.16.E|3|After studying your neighborhood, which way could you share what you learned in writing?|write a short paragraph about it|hide your notes|only whisper|throw away your paper|Writing is one way to communicate information.
13.c.16.G|2|What is a good rule when a classmate is answering a question?|raise your hand and listen quietly|shout your own answer|leave your seat|interrupt them|Respectful listening is a classroom procedure.
14.c.15.D|3|You studied a map of your town and want to share it. Which way is speaking aloud?|giving a short talk about the map|drawing a second map|erasing the map|folding the map|Oral communication means speaking.
14.c.15.E|3|Which is a picture-based way to show where places are in your school?|draw a map of the school|write a long poem about lunch|clap your hands|count the chairs|Maps are visual material.
15.c.14.B|2|Which is the title of the official state song of Texas?|Texas, Our Texas|Yankee Doodle|America the Beautiful|Jingle Bells|Texas, Our Texas is the state song.
15.c.21.C|3|You researched the Alamo for a project. How can you show your ideas aloud?|give a short oral report|keep your notes secret|only write your name|ask to skip|Oral reports share research aloud.
15.c.21.D|3|Which of these is a written product a student could make after Texas research?|a journal entry written as a settler|a guess without notes|a blank page|a lunch menu|Journal entries and reports are written material.
16.c.10.C|3|Which shows the benefit of free enterprise to a shopper?|several stores compete, so shoppers find lower prices|only one store sets any price|stores are forbidden|goods are never sold|Competition gives customers choice and better prices.
16.c.25.C|3|After research on the Constitution, a student presents findings to the class. This is...|expressing ideas orally|writing a poem|drawing a map|reading silently|Speaking uses oral communication.
16.c.25.D|3|A student makes an outline, a timeline, and a report about the Revolution. These are examples of...|written and visual material|dance moves|math facts|recipes|Outlines and reports are student-created material.
16.c.25.E|4|In a class debate on whether to build a new park, a student disagrees politely and listens to others. This shows...|civil discourse about an issue|an argument that insults others|ignoring all views|refusing to speak|Respectful disagreement is civil discourse.
11.c.13.C|2|A kindergartner wants to learn about community helpers. Which is a good picture source?|looking at photos of firefighters and teachers|looking at photos of random clouds|ignoring the topic|asking a cat|Visuals help gather information.
11.c.14.C|2|After a lesson on neighbors, a kindergartner can share learning by...|drawing a picture and telling about it|hiding the paper|refusing to answer|running away|Drawing and telling communicates ideas.
11.c.14.E|2|When your teacher is giving directions, the best choice is to...|be quiet and listen|talk to a friend|walk around|play with toys|Listening respectfully follows classroom rules.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'gap_ss.jsonl'))
print("saved", len(B.out), "questions")

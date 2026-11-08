#!/usr/bin/env python3
"""Grade 2 Technology Applications: TEKS 126.3.c (and 126.c.6) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('126.', 952, own='g2_tech.jsonl')

load(B, """
3.c.4|3|Online maps help drivers find the fastest way. This shows how technology can impact...|a community|a rock|a cloud|a tree|Technology changes how communities work.
3.c.4|4|A school gets tablets that let students read books in many languages. One impact on the community is...|more students can read and learn|fewer books exist|no one can read|computers disappear|Technology can open access.
c.6|3|A bar graph made in a spreadsheet to show favorite pets is a data...|visualization|story|song|toy|Visualizations show data.
c.6|3|Drawing one picture for each vote, with each picture counting the same, is a...|pictograph|map|poem|menu|Pictographs use pictures.
c.6|3|A tool that helps you build a chart from your class survey is a...|digital tool|paper clip|ruler only|crayon only|Digital tools make graphs.
3.c.7|2|When you chat in a class online space, you should be...|respectful and responsible|rude|silly all the time|silent forever|Responsible interactions.
3.c.7|3|A kind way to answer a classmate's online comment is to...|say something helpful and polite|ignore the topic and be mean|post a secret|repeat it loudly|Be respectful.
3.c.1.A|3|To bake a cake you can break the problem into sequential steps like gather, mix, bake. This is...|decomposing|forgetting|guessing|skipping|Decompose into steps.
3.c.1.B|4|2, 4, 6, 8, ... You predict the next number is...|10|9|7|12|The pattern adds two.
3.c.1.B|4|Square, circle, circle, square, circle, circle, square. Your prediction for what comes next is...|two circles|two squares|a triangle|nothing|A repeating pattern.
3.c.1.C|3|Looking over a plan with an adult to see if every step is listed is...|analyzing a plan|ignoring a plan|losing a plan|tearing a plan|Analyze checks the steps.
3.c.1.D|4|If it is raining, then take an umbrella. This is a...|conditional|loop|variable|bug|If-then statements are conditionals.
3.c.1.D|4|Your robot does not turn at the corner. Finding and fixing the mistake in your steps is...|troubleshooting|decorating|sleeping|erasing|Troubleshoot means fix problems.
3.c.2.A|4|In code, a box that holds a value that can change, like a score, is a...|variable|vowel|vehicle|valley|Variables store changing values.
3.c.2.A|4|A game score goes from 0 to 5 to 10. The score is stored in a...|variable|sentence|noun|loop|Variables change.
3.c.2.B|4|Using one command to repeat a move three times is a...|loop|rest|menu|fact|Loops repeat actions.
3.c.2.B|3|Instead of writing 'step' ten times, a loop lets you write 'repeat ten times: step'. A loop makes code...|shorter|longer|silent|slower|Loops save steps.
3.c.3.A|3|Telling a teammate your idea clearly and listening to theirs is effective...|communication|snacking|napping|jumping|Communication helps design work.
3.c.3.B|3|Trying your invention, seeing what works and then improving it is testing and...|reflecting|forgetting|ignoring|hiding|Testing and reflecting improve designs.
3.c.5.A|3|Which is non-numerical data?|favorite book genres|the number of books|students' ages|inches of rain|Genres are categories, not numbers.
3.c.5.A|3|Keeping a record of whether each day is sunny, cloudy or rainy is collecting non-numerical...|data|shoes|snacks|trash|Weather types are categories.
3.c.5.B|3|You are given the keyword 'volcano' and a safe website list. You search by typing the keyword and checking...|the approved sites|any page|nothing|only ads|Use provided sources.
3.c.8.A|3|Using school devices only for learning tasks, as your AUP says, is...|acceptable use|careless use|rule breaking|free play|Follow the policy.
3.c.8.B|3|Copying a classmate's online drawing and saying it's yours is wrong because digital content has...|owners|ovens|oceans|ears|Respect creators.
3.c.9.A|3|A strong password is...|long and mixes letters and numbers|your name|1234|the word password|Strong passwords are hard to guess.
3.c.9.A|3|When you finish on a shared computer, you should...|log off|leave it open|share your login|turn it off by pulling the plug|Log off.
3.c.9.B|4|Information that anyone can see, like a school mascot, is...|public|private|secret|locked|Public information is open.
3.c.9.B|4|Your home address and password are...|private|public|shareable with strangers|always okay to post|Private information stays protected.
3.c.9.C|3|Sending hurtful messages to someone online again and again is an example of...|cyberbullying|teamwork|research|typing|Cyberbullying is hurtful online behavior.
3.c.10.A|3|Making a slideshow to share with your class is creating and sharing...|content|snacks|shoes|toys|You create content.
3.c.10.B|3|A speaker and a monitor are both...|output devices|input devices|snacks|pencils|They give out sound or pictures.
3.c.10.B|4|A microphone and a scanner bring information in. They are...|input devices|output devices|software|monitors|They send data in.
3.c.10.C|3|Looking over a classmate's digital project and giving kind feedback is...|reviewing digital artifacts|deleting them|printing them upside down|hiding them|Reviewing gives feedback.
3.c.10.D|2|Good keyboarding means your back is...|straight and supported|bent over the desk|lying down|twisted|Good posture.
3.c.10.E|3|The key you press with shift and 2 to type the @ sign is a key with a...|secondary action|primary letter only|silent role|broken role|Keys have secondary actions.
3.c.10.E|3|To type the question mark symbol you usually hold...|shift|space bar|enter|backspace|Shift reaches secondary characters.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g2_tech.jsonl'))
print("saved", len(B.out), "questions")

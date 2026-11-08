#!/usr/bin/env python3
"""Grade 3 Technology Applications: TEKS 126.8.c (and 126.c.2.B) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('126.', 953, own='g3_tech.jsonl')

load(B, """
8.c.4|3|A new kind of technology that is just being developed, like a new type of robot or smart glasses, is an...|emerging technology|old tool|rock|plain pencil|Emerging technologies are new and developing.
8.c.4|4|Which is the best example of an emerging technology?|a newly invented learning robot|a wooden spoon|a paper clip|a rock|Emerging means new.
8.c.6|4|A bar graph shows that more students pick pizza than tacos. You can infer that...|pizza is more popular in this group|tacos are banned|everyone likes pizza|nobody eats lunch|A trend is read from graph data.
8.c.6|4|Looking at a line graph of temperatures that goes up each week shows a...|trend|mistake|border|rest|Trends show direction.
8.c.7|3|Making a slide show of your class survey so other students can learn from it is using a digital tool to...|inform an audience|hide results|lose results|erase results|Publishing results informs others.
8.c.1.A|3|A story problem about sharing 12 cookies among 4 friends can be broken into smaller...|subproblems|songs|stories|snacks|Decompose into smaller parts.
8.c.1.B|4|3, 6, 9, 12 ... In this number pattern, each step adds...|three|two|four|one|The rule is add 3.
8.c.1.C|3|Working with your team to write down each step of a project is developing a...|plan collaboratively|snack|game|joke|Documented plans list steps.
8.c.1.D|4|Your code says: move forward, move forward, turn, but the robot misses the target. Finding and removing the error is...|debugging|decorating|deleting the robot|stopping|Debug means fix errors.
8.c.2.A|4|In a game, 'lives = 3' stores a number that can change. 'Lives' is a...|variable|sentence|noun|rule|Variables store data.
8.c.2.A|4|A program starts the score at 0 and adds 1 every time you win. The score changes, so it is stored in a...|variable|border|loop|picture|Variables hold changing values.
c.2.B|4|A program uses 'repeat 4 times: move forward' to draw a square side. The repeat block is a...|loop|variable|comment|bug|Loops repeat.
c.2.B|4|A program that says 'if the sensor sees a wall, then turn' uses a...|conditional|loop|variable|comment|If-then is a conditional.
8.c.3.A|4|Thinking about how you learn and which strategies work for you is called...|metacognition|metal|metaphor|meter|Metacognition is thinking about thinking.
8.c.3.B|3|Asking classmates and your teacher for feedback on your invention and improving it is part of a...|design process|nap|snack|recess|Design uses feedback.
8.c.5.A|3|Which is numerical data?|the price of a pencil|your favorite color|a story title|a song name|Prices are numbers.
8.c.5.A|3|Recording the temperature each hour is collecting...|numerical data|names|songs|stories|Temperatures are numbers.
8.c.5.B|3|To get better results from a search, you can use specific...|keywords|emojis only|blank spaces|capital letters only|Specific keywords help.
8.c.8.A|3|The trail of information you leave online, like posts and searches, is your digital...|footprint|floor|foot|font|Digital footprints last.
8.c.8.B|3|Being polite and respectful when you communicate online is called digital...|etiquette|equation|estimate|echo|Etiquette means good manners.
8.c.8.C|3|Working on the same online project with classmates is digital...|collaboration|isolation|deletion|competition|Collaboration is shared work online.
8.c.9.A|3|Following the school's acceptable use policy shows positive...|social behavior online|bad habits|silence|secrets|AUPs guide good behavior.
8.c.9.B|4|Copyright law protects the work of...|the creator who made it|nobody|only the library|only the internet|Creators own their work.
8.c.9.B|4|Which is an appropriate use of a picture you found online?|asking permission or using a free-to-use picture and giving credit|copying it and saying you made it|selling it as your own|removing the artist's name|Respect copyright.
8.c.9.C|4|A citation for an online picture should include the creator, the title and the...|website or source|favorite color|weather|lunch|Citations list sources.
8.c.10.A|3|A strong password should be...|long and hard to guess|your name|your birthday|the word 'password'|Strong passwords are unique.
8.c.10.A|3|After using a school computer, you should always...|log out|share your password|leave your account open|turn up the volume|Log out for security.
8.c.10.B|4|Which is a safe practice online?|avoid clicking suspicious links|click every link|open files from strangers|share your passwords|Suspicious links can be harmful.
8.c.10.B|4|Protecting your digital identity means keeping personal details like your address...|secret and protected|public|posted on every site|shared with strangers|Protect identifying info.
8.c.10.C|3|If someone sends you mean messages online, you should...|tell a trusted adult|answer with meaner messages|delete the evidence only|keep it a secret|Report cyberbullying.
8.c.11.A|4|To write a report, the best tool is a...|word processor|spreadsheet|presentation tool|calculator only|Word processors write text.
8.c.11.A|4|To organize and add up your class's savings numbers in rows and columns, use a...|spreadsheet|presentation tool|word processor|paintbrush|Spreadsheets handle numbers.
8.c.11.A|4|To show images and key points to the class, use a...|presentation tool|spreadsheet|word processor only|ruler|Slides present ideas.
8.c.11.B|3|Changing how wide the white space is around the edges of your page changes the...|margins|font|clip|link|Margins are page edges.
8.c.11.B|3|Adding a picture to your document is called...|inserting an image|deleting an image|hiding a page|closing a file|Insert adds content.
8.c.12.A|4|A wireless network that lets devices connect to the internet without cables is a...|Wi-Fi network|paper network|stone network|string network|Wi-Fi is wireless.
8.c.12.A|4|A private network used inside a school is called an...|intranet|internet|outernet|kitchenet|An intranet is internal.
8.c.12.B|3|Naming a file 'Planets-Report' instead of 'Doc1' helps you...|find it later|lose it|hide it|break it|Good file names help you find files.
8.c.12.B|3|Keeping files in organized folders is good file...|management|decoration|dancing|noise|File management organizes.
8.c.12.C|3|Touch keyboarding means typing...|without looking at the keys|only with one finger|with eyes closed only|only with a mouse|Touch typing uses muscle memory.
8.c.12.D|4|The shortcut to copy selected text on many computers is...|Control (or Command) and C|Control and P|Control and Q|Shift and Tab|Copy is Ctrl+C.
8.c.12.D|4|Pressing Control (or Command) and Z does what?|undoes your last action|prints|closes the program|saves forever|Z undoes.
8.c.12.E|4|Your app freezes. A simple first fix to try with help is to...|close it and reopen it|throw the computer|hit the keyboard|pour water|Restarting is a basic fix.
8.c.12.E|3|If your computer will not connect to the internet, a minor problem might be that...|Wi-Fi is turned off|the sky is blue|the desk is brown|the floor is cold|Check Wi-Fi.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g3_tech.jsonl'))
print("saved", len(B.out), "questions")

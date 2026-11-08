#!/usr/bin/env python3
"""Grade 4 Technology Applications: TEKS 126.9.c - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('126.', 954, own='g4_tech.jsonl')

load(B, """
9.c.4|3|A drone that delivers packages or a car that drives itself are examples of...|emerging technologies|old tools|rocks|toys only|Emerging technologies are new.
9.c.4|4|Virtual reality headsets and smart assistants are best described as...|new, developing technologies|fossils|extinct tools|unchanging tools|They are emerging.
9.c.6|4|A spreadsheet can add up a column of numbers. This helps you transform data to answer a...|question|riddle|prize|cost|Digital tools analyze data.
9.c.6|4|You sort survey results from smallest to largest in a spreadsheet and notice most students chose the middle value. This is making an...|inference|error|echo|erase|Inferences come from data.
9.c.7|3|Presenting the results of your science experiment using slides to teach your class is using digital tools to communicate to your...|intended audience|desk|clock|shoe|Match results to the audience.
9.c.1.A|3|Breaking a long word problem into small steps and writing down different ways to solve it is decomposing and...|documenting solutions|ignoring it|guessing|giving up|Decompose and document.
9.c.1.B|4|A bus leaves at 8:00, 8:15, 8:30. You predict the next bus time is...|8:45|9:30|8:20|10:00|The pattern adds 15 minutes.
9.c.1.C|3|Sharing your design with a drawing, a model or a short video gives you more ways to...|communicate your plan|hide your plan|forget your plan|lose your plan|Use multiple options to communicate.
9.c.1.D|4|You test a program and it prints the wrong number. Looking through your steps to find and fix the mistake is...|debugging|decorating|deleting|doubling|Debugging fixes errors.
9.c.2.A|4|A program uses 'points = points + 5' each time a player scores. The program is using a variable to...|modify data|erase the screen|draw a picture|play music only|Variables can change values.
9.c.2.B|4|A program that repeats a step 10 times and also checks 'if score is above 50' uses a loop and a...|conditional|rest|noun|comment|Loops and conditionals control flow.
9.c.2.B|4|A program's blocks that run one after another, top to bottom, form a...|sequence|loop|variable|bug|A sequence is ordered steps.
9.c.3.A|4|Asking good questions, communicating well and thinking about your own learning are personal skills that help you carry out a...|design process|nap|snack|recess|Design needs good habits.
9.c.3.B|4|After your team tests a model and finds a weak part, you improve and refine your product. This is part of a...|design process|nap|snack|recess|Refine and improve.
9.c.5.A|3|A table lists each student's favorite sport. This kind of data is classified as...|non-numerical|numerical|measured|counted|Favorite sports are categories, not numbers.
9.c.5.A|3|You record how many minutes each student reads. Minutes are classified as...|numerical data|non-numerical data|names|categories|Minutes are numbers.
9.c.5.B|4|Searching with two keywords like 'Texas bluebonnet history' in a search engine usually gives...|more focused results|fewer links to read|random pictures only|no results|More keywords narrow a search.
9.c.8.A|3|Things you post or search online can stay stored for a long time, creating a permanent digital...|footprint|footstep|foot|footnote|Digital footprints last.
9.c.8.B|3|In an email to your teacher, appropriate digital etiquette is to use...|a polite greeting and clear message|all capital letters|slang with no greeting|rude jokes|Be respectful.
9.c.8.C|3|During a video conference, a polite behavior is to...|mute yourself when not speaking|talk over others|turn music up|leave the room without a word|Courteous collaboration.
9.c.9.A|3|Following the AUP and using devices responsibly is important because it shows...|ethical technology use|bad choices|no rules|careless play|Responsible use matters.
9.c.9.B|4|A creator who makes a song or picture has rights. Copyright law helps protect those...|rights of the creator|rights of the thief|lunch rights|travel rights|Copyright protects creators.
9.c.9.B|4|You can use a copyrighted picture in a school report most correctly if you...|give credit and follow the usage rules|claim it is yours|remove the artist's name|sell copies|Cite and follow rules.
9.c.9.C|4|A citation for a website should list the author, the title and the...|date and address of the site|favorite color|weather|lunch|Citations track sources.
9.c.10.A|3|A strong password and logging off devices matter because they...|protect your account from strangers|slow the computer|erase your files|waste time|Security protects accounts.
9.c.10.B|4|Small files that websites store on your device to track what you do are called...|cookies|crumbs|candies|coupons|Cookies track activity.
9.c.10.B|4|A pop-up that asks for your personal information may be an attempt to collect...|your private data|a free toy|a lunch|a pencil|Be careful with pop-ups.
9.c.10.B|4|Using an unsecured public Wi-Fi network without protection can put your information at...|risk|rest|ease|speed|Unsecured networks are risky.
9.c.10.C|4|Standing up for a classmate who is being cyberbullied by telling a trusted adult is called...|advocating for others|ignoring problems|joining in|hiding|Advocacy is speaking up.
9.c.10.C|3|If you are cyberbullied, one good response is to save the messages and...|report it to a trusted adult|reply with insults|post them everywhere|delete everything silently|Report it.
9.c.11.A|4|For a task that needs a pie chart from numbers, the most relevant application is a...|spreadsheet|word processor only|calendar only|notepad only|Spreadsheets make charts.
9.c.11.B|3|Creating a list with dots in front of each item is called...|bulleting|footnoting|erasing|rotating|Bullets create lists.
9.c.11.B|4|The 'find and replace' tool in a word processor lets you...|change every instance of a word at once|draw pictures|play videos|mail letters|Find and replace edits quickly.
9.c.12.A|4|A computer-generated 3D world you explore with a headset is...|virtual reality|a paper map|a chalkboard|a book|VR immerses you.
9.c.12.A|4|A tool that puts digital pictures on top of the real world on your tablet's camera is...|augmented reality|a map|a calculator|a pencil|AR overlays.
9.c.12.B|3|Naming a file with a clear name and putting it in the correct folder is good...|file management|noise|dancing|decoration|File management helps you find things.
9.c.12.B|4|Which folder structure is most organized for science work?|Science > Plants > Photosynthesis report|Stuff > Misc > Doc|Folder1 > New|Desktop > Untitled|Clear structures help organization.
9.c.12.C|3|Typing with speed and accuracy while sitting with a straight back and relaxed wrists is proper...|touch keyboarding|doodling|dancing|stretching|Ergonomic typing.
9.c.12.D|4|On many keyboards, pressing Shift and a number key types a...|symbol|number|space|tab|Secondary symbols.
9.c.12.D|4|To paste text you copied, press...|Control (or Command) and V|Control and P|Control and Q|Shift and Tab|Paste is Ctrl+V.
9.c.12.E|4|When a program stops responding, a basic troubleshooting step is to...|restart the program|throw the computer|spill water|ignore it|Restart first.
9.c.12.E|4|If your tablet will not respond to touches, you can try...|rebooting the device|painting it|burying it|shaking it hard|Reboot hardware.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g4_tech.jsonl'))
print("saved", len(B.out), "questions")

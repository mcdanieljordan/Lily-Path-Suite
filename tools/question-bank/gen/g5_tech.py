#!/usr/bin/env python3
"""Grade 5 Technology Applications: TEKS 126.10.c - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('126.', 955, own='g5_tech.jsonl')

load(B, """
10.c.4|4|Predicting that self-driving buses could change how a town gets to school is thinking about how emerging technologies may impact...|communities|rocks|clouds|pencils|Predict technology's effects.
10.c.4|4|Which is the best prediction about robots that help in hospitals?|they may help workers care for more patients|they will make hospitals disappear|they will stop all doctors from working|they will turn into plants|Predictions are reasonable.
10.c.6|4|You use a spreadsheet to average the quiz scores of your class and decide whether the class improved. You are using digital tools to analyze data and make an...|inference|echo|error|escape|Analyze to make inferences.
10.c.6|4|Sorting a spreadsheet from highest to lowest sales is a way to...|transform data|erase data|hide data|lose data|Sorting transforms data.
10.c.7|4|A line graph is the best visualization for showing how something changes over...|time|a lunch|a desk|a door|Line graphs show change over time.
10.c.7|4|To show how a class's favorite fruits compare, which visualization is most appropriate?|a bar graph|a map|a calendar|a timeline|Bar graphs compare categories.
10.c.1.A|4|A graphic organizer that shows a big problem branching into smaller parts is a...|concept map|ruler|calendar|recipe|Concept maps decompose problems.
10.c.1.B|4|Every time your phone battery drops below 20 percent, it warns you at the same point. From this pattern you can predict that it will...|warn you again at 20 percent|never warn again|blow up|change colors|Patterns support predictions.
10.c.1.C|4|An outline that lists the problem, ideas for solutions and a timeline for building the program is a...|collaborative outline|joke|song|menu|Outlines plan projects.
10.c.1.D|4|Two programs both draw a square. One uses 20 blocks and one uses 5 blocks with a loop. The better algorithm is usually the one that is...|shorter and efficient|longer and messier|louder|slower|Compare algorithms for efficiency.
10.c.2.A|4|In a game, a variable called 'timer' starts at 60 and goes down by 1 each second. The variable is being used to store and...|modify data|erase data|play music|draw boxes|Variables store and change values.
10.c.2.B|4|In block-based coding, a block that starts the program when you click the green flag is an...|event|variable|loop|comment|Events trigger actions.
10.c.2.B|4|A block-based program that moves a sprite, repeats the move 5 times and checks if it touches an edge uses sequences, loops and...|conditionals|spelling|dancing|noise|Programs combine blocks.
10.c.2.C|4|Copying part of a working program to use in a new game, after studying how it works, is reusing...|code|chalk|paper|paint|Code can be reused.
10.c.3.A|4|Not giving up when your first design fails is called...|persistence|forgetting|sleeping|hiding|Persistence helps design.
10.c.3.B|4|Brainstorming several different ideas for solving a problem before choosing one is generating multiple...|solutions|errors|erasers|echoes|Design generates options.
10.c.5.A|4|The number of minutes of daily exercise is quantitative data. A student's description of how they feel after exercise is...|qualitative data|quantitative data|numbers only|measurements|Descriptions are qualitative.
10.c.5.B|4|In a search, the word AND between two keywords tells the engine to find pages with...|both words|neither word|only one word|no words|Boolean AND needs both.
10.c.5.B|4|The Boolean word OR in a search finds pages that contain...|either keyword|both keywords only|neither keyword|only pictures|OR broadens a search.
10.c.5.B|4|Choosing to search only for pages updated in the last year is using a...|limiter|loophole|ladder|label|Limiters narrow results.
10.c.8.A|3|Which is part of your digital footprint?|your game history and social media posts|the color of your shirt|your lunch|your height|Online activity creates a footprint.
10.c.8.B|3|When writing to a teacher, a respectful digital approach is to use...|complete sentences and a polite tone|slang only|all capital letters|emojis only|Match tone to audience.
10.c.8.C|4|When collaborating with peers in a shared document, appropriate etiquette is to...|respect others' edits and add comments politely|delete their work|type over them|ignore the plan|Collaborate respectfully.
10.c.9.A|4|Following the school's AUP shows that you understand why responsible and ethical use matters. This is an example of...|ethical technology use|rule avoidance|careless play|ignoring the school|Follow AUP.
10.c.9.B|4|Copyright law exists to protect the creators of original work. Using a song or picture without permission can lead to...|legal and school consequences|free prizes|no results|extra recess|Consequences exist.
10.c.9.C|4|A citation for a picture should include the creator, title and where you found it, such as the...|website address|weather|lunch|shoe size|Citations track sources.
10.c.10.A|4|Using a secured internet connection, like a password-protected network, helps protect your...|digital information|shoes|lunch|desk|Secure connections help.
10.c.10.B|4|Websites that use tracking technology to follow where you click are collecting data about your online...|navigation|lunch|sleep|shoes|Tracking follows navigation.
10.c.10.B|4|A good strategy for protecting privacy online is to...|review and limit the data apps can collect|share everything|use one weak password everywhere|click all pop-ups|Control your privacy settings.
10.c.10.C|4|An online argument can escalate quickly. A good way to stand up to cyberbullying is to...|support the target and report to a trusted adult|join the bullying|share the messages publicly|laugh at it|Advocate for self and others.
10.c.11.A|4|A file ending in .docx or .txt is usually a...|text file|graphic file|video file|sound file|Text file types.
10.c.11.A|4|A file ending in .png or .jpg is usually a...|graphic file|text file|spreadsheet|program|Graphics file types.
10.c.11.A|4|A file ending in .mp4 is usually a...|multimedia file|text file|graphic file only|spreadsheet|Multimedia includes video.
10.c.11.B|3|To change the look of text, such as making it bold or a different size, you use...|formatting tools|the power cord|the volume|the printer ink|Formatting changes appearance.
10.c.12.A|4|Short-range wireless technology such as Bluetooth is used to connect devices that are...|close together|across the ocean|on different planets|underwater only|Bluetooth is short range.
10.c.12.A|4|The software that manages a computer's hardware and runs other programs is the...|operating system|printer|keyboard|screen|The OS manages the computer.
10.c.12.B|4|A folder named '5th Science > Ecosystems > Food Webs' shows an organized folder...|structure|mistake|puzzle|joke|Folders nest.
10.c.12.C|3|Practicing touch keyboarding to type faster with fewer mistakes improves speed and...|accuracy|volume|weight|height|Accuracy matters.
10.c.12.D|4|The keyboard shortcut to undo the last action on many computers is...|Control (or Command) and Z|Control and Q|Shift and Tab|Alt and Space|Ctrl+Z undoes.
10.c.12.D|4|The shortcut Control (or Command) and S usually...|saves your work|prints your work|deletes your work|closes your work|S saves.
10.c.12.E|4|If you do not know how to make a table in a document, a good first step is to use the program's...|help feature or tutorial|nearest trash can|power button|printer|Help sources teach features.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g5_tech.jsonl'))
print("saved", len(B.out), "questions")

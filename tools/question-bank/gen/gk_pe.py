#!/usr/bin/env python3
"""Kindergarten Physical Education (TEKS 116.12.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('116.12.b.', 920, own='gk_pe.jsonl')

load(B, """
1.A|2|Which movement is done by pushing off one foot and landing on the same foot?|hopping|sliding|sitting|rolling|A hop starts and ends on the same foot.
1.A|2|Which movement uses a step and a quick bounce, one foot after the other, like a horse?|galloping|crawling|spinning|floating|A gallop has a step-and-leap rhythm.
1.A|2|To stay balanced while skipping, you should...|keep your eyes up and your arms loose|close your eyes|stare at your feet only|hold your breath|Looking ahead helps balance.
1.B|2|Which is a way to jump in place?|bend your knees and push up with both feet|stand on your hands|lie down|walk backward|Jumping uses bent knees and both feet.
1.B|2|When you jump side to side, you move...|left and right|up and down only|only forward|in a circle only|Side to side means left and right.
1.C|2|Tracking a ball with your eyes means you...|watch it as it moves|look away|close your eyes|turn around|Visual tracking follows moving objects.
1.C|2|Doing two skills in order, like hop then jump, is called...|sequencing|sleeping|resting|sitting|A sequence is skills done in order.
1.D|2|Rolling your body sideways on a mat is called a...|log roll|cartwheel|jump rope|dribble|A log roll is a sideways roll.
1.D|2|Spinning slowly versus quickly changes the...|speed of the turn|color of the mat|size of the room|number of fingers|Speed is how fast you move.
2.A|2|Which body part is a base of support when you stand on one foot?|your foot|your elbow|your ear|your nose|The foot supports your weight.
2.A|2|Which position gives you the widest, steadiest base?|feet apart and knees bent|standing on one toe|standing with feet together on tiptoe|leaning far back|A wide base is steadier.
2.B|2|Curling your body means you...|round your body into a small shape|stretch tall|jump high|run fast|Curling makes a rounded shape.
2.B|2|Stretching your arms up high helps you...|reach and lengthen your body|curl up small|fall down|hide|Stretching lengthens muscles.
3.A|2|Which foot should be forward when you throw underhand?|the foot opposite your throwing hand|the same foot as your throwing hand|neither foot|both feet|Opposite foot forward gives balance.
3.A|3|When tossing a ball to yourself, you should toss it...|gently upward in front of you|behind your back hard|straight at a window|to the ceiling fan|Gentle tosses are easier to catch.
3.B|2|To catch something thrown to you, where should your eyes stay?|on the object coming toward you|on the ceiling|on the floor|on the clock|Watching the object helps you catch it.
3.B|2|When catching, your hands should be...|ready and open in front of your body|behind your back|in your pockets|over your eyes|Open hands are ready to catch.
3.C|2|When dribbling with one hand, you push the ball with...|your fingertips|your elbow|your head|your foot|Fingertips control the ball.
3.D|2|To tap a ball with your foot, you use the...|inside of your foot|toe only, as hard as you can|heel only|top of your head|The inside of the foot gives control.
3.E|2|To kick a ball that is standing still, you should...|step with one foot and kick with the other|jump in the air|pick it up|sit on it|Plant one foot and swing the other.
3.F|2|To volley a light balloon to yourself, you gently...|hit it upward with your hands|throw it down|hold it still|kick it hard|Volleying keeps it in the air.
3.G|2|A good way to strike a lightweight object is to use...|your hand or a short paddle|a heavy bat|your head|a chair|Light objects need light tools.
3.H|2|When you jump rope, you swing the rope over your head and...|jump over it|crawl under it|sit on it|throw it|The rope must pass under your feet.
3.I|2|When two people swing a long rope, they should...|swing it back and forth together|let go|tie it up|jump on it|Partners swing in rhythm.
4.A|2|Your personal space is...|the space around your body|the whole gym|a classmate's space|a closet|Personal space is your own area.
4.A|2|General space is...|the open area where everyone can move|the space inside your pocket|a locker|a tiny box|General space is shared.
4.B|2|A pathway can be...|straight, curvy, or zigzag|loud or quiet|red or blue|hot or cold|Pathways are the lines you travel.
4.B|2|Moving low to the floor is a change in...|level|taste|volume|color|Levels are high, medium or low.
4.C|2|Moving fast then slow shows a change in...|speed|temperature|color|taste|Contrast uses different speeds.
4.C|2|Moving forward then backward changes your...|direction|height|weight|age|Direction is the way you move.
5|2|When you dance to music, you should move with the...|beat|clock|door|window|Rhythm follows the beat.
5|2|A steady beat is like a...|heartbeat that repeats|storm|song with no sound|lost shoe|A beat repeats evenly.
6.A|2|In a chasing game, which skill means moving quickly away from the person chasing you?|fleeing|catching|dribbling|volleying|Fleeing is moving away to avoid being tagged.
6.A|2|Dodging means you...|quickly change direction to avoid being tagged|stand still|jump rope|sit down|Dodge by moving sideways quickly.
6.A|2|While playing a tag game, you should keep your hands to yourself and stay...|in safe space away from others|inches from others|on the walls|under tables|Safe space prevents bumping.
6.B|2|When your teacher shows a skill, you should...|watch and try it the same way|ignore it|do something else|leave|Following directions helps you improve.
6.C|2|Which is a safe practice in class?|follow the rules and listen to directions|run into friends|throw balls at people|take equipment without asking|Safety means following rules.
8.A|2|When you run, your heart beats...|faster|slower|not at all|backward|Exercise speeds the heart.
8.A|2|After you exercise, your breathing is...|faster|slower|stopped|gone|Lungs work harder with exercise.
8.B|2|Why is daily active play important?|it keeps your body healthy and strong|it makes you tired forever|it stops growth|it hurts your heart|Play builds strength.
8.C|2|Which activity helps your fitness?|jumping jacks|watching TV|sleeping all day|sitting in a car|Exercise builds fitness.
9.A|2|Setting a goal means you...|decide something you want to work toward|forget your plan|quit|ignore your coach|A goal is something you aim for.
9.B|2|You can see if you are getting better at hopping by...|counting how many hops you can do|guessing|hiding|sleeping|Counting measures progress.
10.A|2|Why do we eat a variety of foods?|to give our body energy|to make us sleepy|to stop growing|to lose our teeth|Different foods give energy and nutrients.
10.B|2|The best drink to have during exercise is...|water|soda|candy|coffee|Water hydrates your body.
11.A|2|What is the best footwear for playing in P.E.?|sneakers|flip flops|slippers|boots with heels|Sneakers protect feet.
11.A|2|The best clothes for P.E. are...|loose and comfortable|tight and stiff|a winter coat|a costume|Comfortable clothes help movement.
11.B|2|When you cross the street, you should...|look both ways and hold a grown-up's hand|run across|close your eyes|play in the road|Pedestrian safety means looking.
11.B|2|When riding a bike, you should always wear a...|helmet|hat|scarf|mask|Helmets protect your head.
11.B|2|On a sunny day you should protect your skin with...|sunscreen|oil|water|snow|Sunscreen blocks harmful rays.
12.A|2|If you push a friend in line, a consequence could be that...|your friend gets hurt or you lose a turn|you win a prize|nothing ever happens|you get a trophy|Actions have results.
12.B|2|Respecting differences means you...|kindly accept that everyone is different|make fun of others|ignore people|laugh at mistakes|Respect treats others kindly.
12.C|2|If you feel angry, it is good to...|name the feeling and tell a teacher|hit someone|break equipment|run away from class|Naming feelings helps.
13.A|2|Showing respect to a teammate means...|using kind words and taking turns|pushing|calling names|ignoring them|Respect and cooperation help teams.
13.B|2|If you are upset, an appropriate way to tell the teacher is to...|use your words calmly|yell|throw a ball|cry loudly forever|Calm words get help.
14|2|When something is hard, perseverance means you...|keep trying|quit right away|blame others|hide|Perseverance is not giving up.
14|2|If you miss the ball, a good response is to...|try again|throw the ball away|walk off|cry and quit|Trying again shows grit.
15|2|When a friend gives you a tip kindly, you should...|say thank you and try it|argue|ignore it|run away|Accepting feedback helps you learn.
15|2|A kind way to help a classmate improve is to say...|Nice try! Try bending your knees more.|You are bad.|That was awful.|Give up.|Constructive feedback is kind and helpful.
16.A|2|How often should kids be active?|every day|once a year|never|once a month|Daily activity builds health.
16.B|2|Which activity can be fun for exercise?|dancing|sleeping|watching TV|sitting still|Dancing is active and enjoyable.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'gk_pe.jsonl'))
print("saved", len(B.out), "questions")

#!/usr/bin/env python3
"""Grade 3 Physical Education (TEKS 116.15.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('116.15.b.', 923, own='g3_pe.jsonl')

load(B, """
1.A|3|A leap is different from a jump because in a leap you take off from one foot and land on the...|other foot|same two feet|knees|hands|A leap moves from one foot to the other in the air.
1.A|3|Which locomotor skill is a running step where you stretch your legs wide in the air?|leaping|sliding|sitting|crawling|Leaps are long, airborne strides.
1.A|3|In a proper skip, you...|step and hop on one foot, then the other|only walk|only crawl|jump on two feet|Skipping alternates step-hops.
1.B|3|When jumping down from a low platform, you should land with...|soft, bent knees|stiff legs|your hands first|your head first|Absorb force by bending knees.
1.B|3|Landing from a higher height needs a more...|controlled landing|careless landing|loud landing|backward landing|Greater height means more force.
1.C|3|Walking along a low balance beam is an example of...|intermediate balancing with equipment|a race|a rest|a game of tag|Equipment adds challenge to balance.
1.C|3|Skipping with arms swinging in opposition uses...|cross lateral coordination|only one side of the body|no coordination|none of the body|Opposite arm and leg move together.
1.D|3|Spinning with control while holding a scarf means you...|keep your balance and watch the scarf|fall down|close your eyes|let go|Control means steady movement.
2.A|3|Moving in and out of a balanced position with control is useful when you...|change directions in a game|sit still|take a nap|sleep|Dynamic balance helps in sports.
2.B|3|A movement that combines bending and stretching could be...|reaching for a high shelf then crouching|sitting|sleeping|standing still|It uses two actions.
3.A|3|An accurate overhand throw means you...|aim at the target and follow through|look away|throw as hard as you can at anything|swing your arm backward|Accuracy needs aim and follow-through.
3.A|3|Which throw uses a swinging arm from low to high?|underhand|overhand|sidearm only|none|Underhand swings from low.
3.B|3|When catching a soft toss, you reach out and then...|give with the ball by pulling your hands in|snap your arms straight|close your eyes|turn away|"Giving" absorbs the force.
3.C|3|Dribbling while slowly jogging means you...|keep the ball under control as you move|stop dribbling|throw the ball|kick the ball|Control is key.
3.D|3|When dribbling a soccer ball while jogging, you should tap the ball...|lightly so it stays near your feet|with all your force|with your hands|backward|Light touches keep control.
3.E|3|Kicking a rolling ball on the ground means you...|time your kick with the ball's movement|stand far away|close your eyes|run in a circle|Timing is essential.
3.E|3|To kick a ball into the air, you should contact the...|bottom of the ball|top of the ball|side of the ball only|nothing|Kicking low lifts it.
3.F|3|When volleying a ball over a net, you should use your...|hands or forearms|elbows|ears|knees only|Forearms make a flat platform.
3.G|3|To strike a moving ball with a paddle, you should...|watch the ball and swing at it|close your eyes|stand still|throw the paddle|Eye-hand coordination is key.
3.H|3|Which is a basic jump rope skill?|jumping with both feet|dancing without a rope|cutting the rope|climbing the rope|Two-foot jumps are the basic skill.
3.I|3|To enter a turned long rope, you should...|run in when the rope reaches the ground|stand still and wait forever|step in while it is overhead|grab the rope|Enter just as the rope hits the ground.
3.I|3|To exit a long rope, a jumper should...|run out after a jump|stop in the middle|sit down|hold the rope|Exit through the side.
4.A|3|Open space in a gym is...|an area free of people and objects|a closet|a small corner|a locked room|Open space is where you can move freely.
4.B|3|Combining pathways and levels could look like...|a zigzag path then a low roll|standing still|clapping|sleeping|They mix paths and heights.
4.C|3|Combining force with speed could mean...|moving fast with a strong push|moving slowly with a tiny tap|sitting|none|Force and speed combine for different effects.
5|3|Folk dances often use...|steps in a set pattern to music|random movement|no music|no steps|They follow patterns and rhythm.
5|3|A rhythm pattern in dance is usually repeated every...|measure or phrase|week|year|day|Music is organized in phrases.
6.A|3|A game that combines chasing, fleeing, and dodging requires you to...|think quickly and change direction|stand still|sit|nap|Games call for several skills together.
6.B|3|To improve a movement skill, you can...|practice it correctly several times|skip it|ignore it|avoid it|Practice improves skills.
6.C|3|Following game rules makes the game...|fair and safe|longer|boring|dangerous|Rules protect players.
7|3|A skill for an outdoor adventure like orienteering is...|reading a map and compass|baking|painting|dancing|Orienteering uses navigation.
7|3|A good rule for camping safety is to...|stay with the group and tell an adult where you go|wander off|play with fire|leave trash|Camping safety means planning.
8.A|3|One way regular exercise helps manage stress is by...|releasing tension and improving your mood|making you worry|keeping you awake|making you angry|Activity helps your mood.
8.B|3|In endurance activities, intensity means...|how hard you work|how loud you are|how tall you are|how long the class is|Intensity is effort level.
8.B|3|In endurance activities, frequency means...|how often you do the activity|how hard you work|how heavy you are|what you wear|Frequency is how many times a week.
8.C|3|A correct sit-up (curl-up) is done by...|curling your upper body toward your knees|pulling your neck|jumping|swinging your arms|Curl-ups work the abdominal muscles.
8.C|3|Flexibility is the ability to...|move your joints through a full range of motion|run fast|lift heavy things|hold your breath|Stretching builds flexibility.
9.A|3|Setting personal fitness goals helps because they...|give you something to work toward|have no purpose|make you quit|are impossible|Goals provide direction.
9.B|3|One way to track fitness progress is to...|record your scores in a chart|forget your scores|hide your scores|guess|Charts show improvement.
10.A|3|Which food is a healthy source of energy?|whole-grain bread|candy|chips|soda|Whole grains give steady energy.
10.A|3|A food high in sugar gives energy that...|runs out quickly|lasts all day|never ends|builds muscle|Sugar spikes then drops.
10.B|3|Which drink best helps your body during exercise?|water|soda|energy drink|sugary juice|Water hydrates without added sugar.
11.A|3|A pair of proper shoes for P.E. should be...|supportive and tied|untied|slippery|too big|Good shoes prevent falls.
11.A|3|A mouthguard is used in contact sports to protect your...|teeth|toes|eyes|ears|Mouthguards cover teeth.
11.B|3|Scooter safety includes wearing a...|helmet and staying off busy streets|blindfold|swimsuit|scarf|Helmets and safe places keep riders safe.
11.B|3|Water safety rules say you should swim...|only with a lifeguard or adult nearby|alone at night|during a storm|in unknown water|Never swim without supervision.
11.B|3|Sun safety includes...|using sunscreen and seeking shade|staying in the sun all day|wearing a dark blanket|no water|Protect your skin.
12.A|3|When you choose to help a teammate, a consequence for others is that they...|feel supported|feel worse|lose the game|get angry|Actions affect others.
12.B|3|A teammate with a different skill level should be treated with...|respect|jokes|pushing|neglect|Respect applies to everyone.
12.C|3|Counting to ten before reacting is a self-management skill that helps you...|calm down|get angrier|forget the rules|run away|It helps control impulses.
13.A|3|Cooperation in a team game means...|working together toward a common goal|playing only for yourself|ignoring teammates|arguing|Teams succeed through cooperation.
13.B|3|If a classmate looks sad after losing, they may be feeling...|disappointed|excited|proud|silly|Identify feelings by watching others.
14|3|Which shows perseverance during a hard fitness test?|continuing even when tired|stopping early|blaming others|refusing to try|Perseverance is sticking with it.
14|3|Learning a new skill takes time. Perseverance helps you...|keep practicing until you improve|quit|forget|complain|Persistence leads to success.
15|3|Constructive feedback should be...|specific and kind|mean|vague|rude|It should help the person improve.
15|3|When you receive a correction from a coach, you should...|listen carefully and try again|argue|ignore|laugh|Accepting feedback helps improvement.
16.A|3|Moderate activity is the kind that...|makes you breathe a little harder but you can still talk|makes you unable to speak|requires no effort|is sleeping|Moderate effort is comfortable.
16.A|3|Vigorous activity is the kind that...|makes you breathe hard and unable to say more than a few words|lets you chat easily|is resting|is sleeping|Vigorous effort is intense.
16.B|3|Selecting a physical activity you enjoy means you...|choose one that fits your interests|pick the one you dislike|never exercise|only watch|Enjoyment keeps you active.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g3_pe.jsonl'))
print("saved", len(B.out), "questions")

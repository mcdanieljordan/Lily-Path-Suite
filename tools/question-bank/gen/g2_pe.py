#!/usr/bin/env python3
"""Grade 2 Physical Education (TEKS 116.14.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('116.14.b.', 922, own='g2_pe.jsonl')

load(B, """
1.A|2|Which locomotor skill has you move with an uneven step-step-hop pattern, like a quick rhythm on each side?|skipping|standing|sitting|kneeling|Skipping alternates steps and hops.
1.A|3|When running for speed, your arms should bend and swing...|forward and backward|side to side only|in circles|not at all|Arms drive the body forward.
1.A|3|A gallop is different from a skip because a gallop...|keeps the same foot in front|alternates feet|uses no feet|uses hands|In a gallop, one foot leads the whole time.
1.B|3|A correct landing from a jump is on the balls of your feet with your knees...|bent|locked|crossed|turned out|Bent knees cushion the impact.
1.B|3|Jumping consecutively backward means you...|jump again and again toward your back|jump once|stand still|spin in place|Consecutive jumps repeat.
1.C|3|Cross lateralization means using...|opposite sides of the body together|one arm only|one leg only|no limbs|Opposite arm and leg work together.
1.C|3|Which pair is an example of cross lateral movement?|right hand touching left knee|both hands clapping|both feet jumping|a head nod|Crossing the midline uses both sides.
1.D|2|A forward roll is done by tucking your chin and rolling over your...|rounded back|stomach|face|knees only|A tucked, curved back protects the neck.
1.D|3|Spinning at a high level means you spin while...|standing tall or on your toes|lying down|crawling|sitting|High level is up high.
2.A|2|Standing on one foot for eight seconds without wobbling mostly tests your...|ability to stay steady|hearing|running speed|eyesight|Balance holds a steady body position.
2.A|3|Keeping your eyes on a spot that does not move helps your...|balance|hair|temperature|hearing|A focal point steadies balance.
2.B|3|Which action means to move toward your body with force?|pull|push|twist|sway|Pulling draws something toward you.
2.B|3|Pushing is when you...|move something away from your body|bring it closer|turn it|stay still|Pushing moves away.
3.A|3|When throwing overhand, which arm moves toward the target?|your throwing arm after the opposite foot steps|your non-throwing arm only|both feet|your head|Step with the opposite foot, then throw.
3.A|3|A partner underhand throw should be tossed...|gently so the partner can catch it|as hard as possible|at the face|up high out of reach|Throw softly to a partner.
3.B|3|Catching without trapping the ball against your body means you catch with your...|hands and fingers|chest|chin|elbows|Use hands to catch, not the body.
3.C|3|When dribbling with a hand while walking, you push the ball...|out in front and a little to the side|straight behind you|high above your head|down your shirt|Dribble in front, near your side.
3.D|3|Dribbling with both feet means you tap the ball with your...|right foot and left foot|hands|knees|elbows|Use both feet for control.
3.E|3|To kick a rolling ball, you run toward it and...|swing your leg to meet it|stand and hope|catch it|sit|A running approach lines up the kick.
3.F|3|Volleying consecutively means hitting a light object...|again and again without it touching the ground|once only|only to the floor|never|Consecutive means in a row.
3.G|3|To strike a stationary object off a tee, you should...|swing smoothly through the ball|stop before it|close your eyes|let go of the bat early|A level, smooth swing makes contact.
3.H|2|Jumping forward and backward over a self-turned rope means you...|turn the rope the same way and jump over it each time|let the rope go slack|drop it|skip rope with someone|Rope jumping needs rhythm.
3.I|3|When a long rope is turned, a jumper should enter...|at the right time as the rope comes toward them|before the rope starts|when the rope is tangled|never|Timing helps the jumper enter.
4.A|2|A skill that moves you from place to place is called...|a locomotor skill|a non-locomotor skill|a manipulative skill|a rest|Locomotor skills travel.
4.A|3|A skill that is done without traveling, like bending, is...|non-locomotor|locomotor|manipulative|vigorous|Non-locomotor skills stay in place.
4.A|3|Throwing and catching a ball are examples of...|manipulative skills|locomotor skills|non-locomotor skills|rest skills|Manipulatives use objects.
4.B|3|A simple sequence could be...|a low roll, a curved pathway, and a stretch|one jump|a nap|a shout|A sequence has more than one movement.
4.C|3|Combining speed and direction could mean...|moving fast forward then slow sideways|standing still|singing|sitting|Speed and direction combine in a sequence.
5|3|A short dance pattern repeated to the music uses...|rhythm and movement|only speed|only color|only sound|Dance moves follow the rhythm.
5|3|Moving in time with the beats of a song shows good...|rhythm|height|weight|cold|Rhythm matches the beat.
6.A|3|Dodging at a low level means you...|duck down to avoid a tag|stand tall|sit|fly|Levels change how you dodge.
6.A|3|Which game uses chasing, fleeing, and dodging?|a tag game|a puzzle|a spelling test|a jump rope contest|Tag uses all three.
6.B|3|A drill is a practice activity used to...|improve a specific skill|win a prize|skip class|rest|Drills build skills.
6.C|3|Using equipment safely means you...|check it and use it the right way|throw it at others|bend it|hide it|Safe use prevents injury.
7|3|Outdoor and recreational activities you can do with a bike include...|riding on a trail|watching TV|sleeping|baking|Biking is recreation.
7|3|A safe way to hike is to...|stay on the trail and bring water|run off alone|drink from a puddle|leave the group|Hiking safely means planning.
8.A|3|One benefit of regular exercise on your heart is that it...|gets stronger|stops|gets weaker|turns off|Regular activity strengthens the heart.
8.A|3|One benefit of exercise on your lungs is that you can...|take in more air|breathe less|stop breathing|lose them|Lungs work better with exercise.
8.B|3|Frequency in exercise means...|how often you exercise|how heavy you are|how tall you are|what color you wear|Frequency is how many times.
8.B|3|Endurance in exercise means...|how long you can keep going|how fast you can run once|how loud you are|how big you are|Endurance is lasting power.
8.C|3|A correct push-up keeps your body in a...|straight line|curve|hunch|slump|Straight alignment protects your back.
9.A|3|A skill-related goal could be to...|jump rope 20 times in a row|never practice|skip class|ignore feedback|Skill goals improve a skill.
9.B|3|To track progress in a standing jump, you could use a...|tape measure and a chart|spoon|balloon|pillow|Charts track changes.
10.A|3|Which type of food gives your body lasting energy?|whole grains and fruits|frosting|candy|soda|Whole foods supply steady energy.
10.B|3|Why is it important to drink water before, during, and after activity?|it replaces fluid you lose by sweating|it makes you tired|it stops sweating|it makes you thirsty|Water replaces sweat.
11.A|3|How does a helmet keep you safe?|it protects your head from injury|it keeps you cold|it makes you faster|it makes you heavy|Helmets cushion head impacts.
11.A|3|Shin guards are used in soccer to protect your...|lower legs|eyes|hands|ears|Shin guards cover shins.
11.B|3|Skating safety includes wearing...|a helmet, wrist guards, and pads|flip flops|a scarf|nothing|Pads protect joints.
11.B|3|Pedestrian safety means you should cross...|at a crosswalk when the signal says go|between parked cars|anywhere you want|without looking|Crosswalks are safer.
12.A|3|A positive consequence of telling the truth is that people...|trust you|get angry|laugh|forget you|Honesty builds trust.
12.A|3|A negative consequence of not sharing equipment is that...|others may feel left out|everyone is happy|games go faster|teams win|Not sharing hurts feelings.
12.B|3|Showing respect for different abilities means you...|help and cheer for others|laugh at them|complain|ignore them|Respect includes support.
12.C|3|Which is a self-management skill to calm yourself?|taking a deep breath|yelling|throwing things|kicking others|Deep breaths help control impulses.
13.A|3|If two friends want the same ball, a good solution is to...|take turns|fight over it|run away|break it|Taking turns solves the problem.
13.A|3|The cause of a problem is...|what made it happen|how it ends|the color of it|its size|Cause explains why.
13.B|3|Communicating feelings without being reminded means you...|say how you feel on your own|wait for someone to guess|hide your feelings|shout|You can use words by yourself.
14|3|When a skill is hard, perseverance helps you to...|try again with a good attitude|quit|blame others|hide|Perseverance is continued effort.
14|3|Which is an example of perseverance?|practicing a jump rope skill every day until you improve|quitting after one try|ignoring the teacher|giving up|Daily practice shows grit.
15|3|When someone says, "Try bending your knees more," that is...|helpful feedback|a mean comment|a joke|a rule|Feedback gives a tip for improvement.
15|3|After getting feedback, a good response is to...|thank them and try it|get upset|walk away|blame others|Accepting feedback helps growth.
16.A|3|Moderate to vigorous activity should happen...|on a regular basis|once a year|never|only on holidays|Regular activity builds health.
16.B|3|You should choose activities you enjoy because...|you are more likely to keep doing them|they are easier to avoid|they cost less|they are lazier|Enjoyable activities are sustainable.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g2_pe.jsonl'))
print("saved", len(B.out), "questions")

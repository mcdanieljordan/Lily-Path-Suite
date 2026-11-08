#!/usr/bin/env python3
"""Grade 5 Physical Education (TEKS 116.17.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('116.17.b.', 925, own='g5_pe.jsonl')

load(B, """
1.A|3|In a lead-up game, combining a run with a jump and a throw tests your ability to...|link locomotor and manipulative skills|sit still|rest|hide|Combination skills mix movements.
1.A|3|A hop-step-jump sequence is an example of a...|locomotor skill combination|rest period|cool-down|quiz|Combinations link skills.
1.B|4|A strong long jump begins with a swing of the arms and...|a powerful push from both legs|a backward step|a slow walk|closing your eyes|Arms and legs work together.
1.B|4|A full turn jump can be done in...|both directions, left and right|only forward|only up|only down|Practicing both directions builds skill.
1.C|4|Advanced balancing with equipment could be...|walking a balance beam while carrying a ball|sitting on a mat|resting|napping|Added tasks increase difficulty.
1.C|4|Cross lateralization in complex movement means...|coordinating opposite limbs in changing patterns|using one hand only|standing still|using no limbs|Complexity needs coordination.
2.A|3|Transferring body weight with control during a dynamic activity helps prevent...|falls and injuries|fun|speed|fitness|Control keeps you safe.
2.B|3|Performing a series of pushing and pulling movements, such as a tug-of-war, uses...|different muscle groups|only your legs|nothing|only your eyes|Pushing and pulling use many muscles.
3.A|4|The key elements of manipulative skills include eye on target, follow-through, and...|body weight transfer|closing your eyes|dropping the ball|sitting|Weight transfer adds power and accuracy.
3.B|4|Catching while moving means you...|track the object and adjust your steps|stand still|close your eyes|turn away|Moving catches need tracking.
3.C|4|To shield the ball while dribbling, you keep your body between the ball and the player trying to steal it. That player is called a...|defender|goalkeeper|referee|coach|Shielding keeps the ball safe.
3.C|4|When protecting the ball while dribbling, you should keep the ball on the side...|away from the defender|toward the defender|above your head|behind your back always|Use your off-hand away from pressure.
3.D|4|Combining foot dribbling with a pass in a lead-up game means you...|move the ball with your feet then pass to a teammate|only run|only kick hard|stop|Skills link in games.
3.E|4|Punting a ball requires you to drop the ball and then...|kick it before it hits the ground|catch it|roll it|hide it|Punting kicks a dropped ball.
3.E|4|The proper kicking form includes a follow-through that points...|toward your target|backward|at the ground|into the sky|Follow-through directs the ball.
3.F|4|In volleying, you should get under the ball and use your...|fingertips or forearms|elbows|feet|knees|Contact surfaces control the ball.
3.G|4|When striking with a bat, you should keep your eye on the...|ball until contact|crowd|sky|floor|Eyes on the ball improve contact.
3.H|4|An advanced jump rope routine could include...|crossing the rope and double unders|standing still|running away|sitting|Advanced skills raise difficulty.
3.I|4|Entering a turned long rope with an advanced skill could involve...|jumping in with a partner or doing a trick|standing still|holding the rope|hiding|Advanced entries need timing.
4.A|4|Working in small groups, closing space helps your team...|defend and stay connected|spread out|stop|rest|Closing space shrinks the defender's gap.
4.A|4|In a small group game, creating open space helps you...|receive a pass|hide from the ball|stand together|stop moving|Open space invites a pass.
4.B|4|Using varied pathways and levels in a group game helps a team...|confuse defenders|stay in a line|stop playing|rest|Variety creates challenge.
4.C|4|Applying speed, direction, and force with a short-handled implement could be...|hitting a ball with a paddle at different strengths|reading a book|sleeping|walking|Control of force matters.
6.A|4|Game skills often follow this order: preparation, movement, force production, and...|follow-through|resting|quitting|hiding|Follow-through completes the skill.
6.A|4|Preparation in a throw means you...|get set with a balanced stance|run away|close your eyes|sit|Preparation sets up the skill.
6.B|4|Working with a partner or group on a skill means you...|share feedback and practice together|work alone|argue|rest|Team practice builds skills.
6.C|4|Game etiquette without a teacher cue means you...|follow rules and show respect on your own|wait to be told|cheat|argue|Self-direction shows maturity.
7|4|A recreational pursuit that requires a map and compass is...|orienteering|bowling|knitting|painting|Orienteering uses navigation skills.
7|4|Which outdoor skill helps you find direction?|using a compass|baking|painting|dancing|Compasses show direction.
8.A|3|Moderate to vigorous activity reduces the risk of...|heart disease|growing|learning|laughing|Activity protects heart health.
8.A|3|Regular activity improves your sleep and your...|mood and focus|height only|eye color|hair|Exercise supports wellbeing.
8.B|4|The FITT principle stands for frequency, intensity, time, and...|type|trick|test|team|FITT includes type of exercise.
8.B|4|In the FITT principle, time means...|how long each exercise session lasts|what time of day|what time it is in another city|how fast the clock runs|Time is the duration.
8.C|4|Which is a health-related fitness component?|flexibility|reaction time|balance|agility|Flexibility is health-related.
8.C|4|Which is a skill-related fitness component?|reaction time|muscular endurance|body composition|flexibility|Reaction time is skill-related.
9.A|4|When analyzing a fitness goal, you should ask whether it is...|specific, measurable, and realistic|vague|impossible|ignored|Good goals are SMART.
9.B|4|After tracking your push-up scores, if your numbers are not improving, you could...|change your training plan|quit|hide the scores|blame the floor|Data guides change.
10.A|4|Which food helps your body perform during exercise?|oatmeal with fruit|candy|chips|soda|Whole grains and fruit give lasting energy.
10.A|4|A good pre-game snack is...|banana and peanut butter|cake|candy|soda|Balanced snacks fuel activity.
10.B|4|Dehydration can cause...|tiredness and cramps|extra energy|stronger muscles|better focus|Not enough water harms performance.
11.A|4|Choosing proper equipment means you...|select gear that fits the activity and your size|use any gear|skip safety items|share a helmet that doesn't fit|Fit and function matter.
11.B|4|Sun safety includes reapplying sunscreen...|every two hours or after sweating|never|once a week|once a year|Sunscreen wears off.
11.B|4|Water safety means swimming...|with a buddy and where a lifeguard is present|alone|in storms|in strong currents|Buddies and lifeguards increase safety.
12.A|4|Accepting responsibility during a game means you...|own your mistakes and learn from them|blame the referee|deny it|quit|Responsibility builds character.
12.B|4|Showing respect for differences includes...|including players of all abilities|leaving someone out|making jokes|ignoring|Inclusion is respect.
12.C|4|Applying self-control after a bad call means you...|stay calm and keep playing|yell|throw equipment|walk off|Self-management helps teams.
13.A|4|Resolving conflict in a socially acceptable way means you...|talk it out and find a compromise|fight|ignore|yell|Compromise solves conflicts.
13.A|4|Responding to winning with dignity means you...|are humble and respect your opponents|brag|taunt|ignore others|Humility is good sportsmanship.
13.B|4|Effective communication during a disagreement includes...|active listening|interrupting|shouting|name calling|Listening reduces conflict.
13.C|4|Empathy is...|understanding how someone else feels|ignoring feelings|being angry|being bored|Empathy is sharing feelings.
13.C|4|Mutual respect means...|treating each other kindly|only caring about yourself|ignoring each other|making fun of each other|Respect goes both ways.
14|4|Perseverance helps an athlete...|keep practicing after setbacks|quit when it gets tough|ignore coaching|blame others|Persistence builds skill.
14|4|Which statement shows perseverance?|"I didn't get it yet, so I'll practice more."|"I'm done."|"It's not fair."|"I quit."|"Yet" shows a growth mindset.
15|4|Giving constructive feedback means you...|offer a helpful suggestion kindly|criticize harshly|ignore the person|laugh|Feedback should help.
15|4|When receiving constructive feedback, a good response is to...|listen and try the suggestion|argue|quit|ignore|Openness leads to improvement.
16.A|4|Which activity is moderate in intensity?|brisk walking|sprinting|sitting|sleeping|You can talk but not sing.
16.A|4|Which activity is vigorous in intensity?|running laps|slow strolling|resting|sitting|You can only say a few words.
16.B|4|Analyzing your enjoyment of activities helps you...|choose activities you will stick with|avoid exercise|pick the least fun|quit|Enjoyment keeps you active.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g5_pe.jsonl'))
print("saved", len(B.out), "questions")

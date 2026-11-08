#!/usr/bin/env python3
"""Grade 4 Physical Education (TEKS 116.16.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('116.16.b.', 924, own='g4_pe.jsonl')

load(B, """
1.A|3|In a game of basketball, which locomotor skill is used to change direction quickly?|cutting|napping|kneeling|crawling|Cutting is a quick directional change.
1.A|3|Using the correct technique for running means your foot lands under...|your body|your head|your hands|your knees locked|Landing under the hips improves control.
1.B|3|In a long jump, you should swing your arms forward and land with...|both feet and bent knees|stiff legs|your hands|your head|A controlled two-foot landing is safest.
1.B|3|A full turn jump means you jump and rotate...|all the way around in the air|a quarter turn|not at all|backward only|A full turn is 360 degrees.
1.C|3|Cross lateralization during a coordination drill means moving...|opposite arm and leg together|only your arms|only your legs|nothing|Opposite sides work together.
1.C|3|Balancing on a bench while moving is a form of...|intermediate balancing with equipment|a rest|a snack|a cool-down|Equipment raises difficulty.
1.D|3|Rolling with control while holding a ball means you...|keep the ball safe and your movement smooth|let the ball go|stop moving|kick the ball|Control means smooth, steady movement.
2.A|3|Transferring body weight means you shift your weight...|from one body part to another|from one planet to another|from one book to another|from one friend to another|Weight transfers from hands to feet and back.
2.A|3|Moving over a low bench with good control means you...|plan your steps and balance|rush|close your eyes|fall|Control requires planning.
2.B|3|Moving into and out of a combination of twisting and stretching requires...|flexible, controlled movement|stillness|speed only|noise|Combination moves need flexibility.
3.A|3|Which is a key element of throwing?|follow-through|closing your eyes|dropping the ball|hiding|Follow-through improves accuracy.
3.A|3|Transferring your body weight when throwing means you shift weight from your...|back foot to your front foot|head to your foot|hand to your ear|front foot to your elbow|Weight shifts forward for power.
3.B|3|Catching a ball above your waist uses...|thumbs together|pinkies together|elbows together|fingers pointing down|Thumbs together catch high balls.
3.B|3|Catching a ball below your waist uses...|pinkies together and fingers pointing down|thumbs together|palms up high|only one finger|Pinkies together catch low balls.
3.C|3|Dribbling with your non-dominant hand while changing direction helps you...|improve control with both hands|forget the ball|stand still|ignore your team|Practice improves both hands.
3.D|3|When dribbling with a partner and changing speed and direction, you should...|keep the ball close and watch your partner|kick it hard|let it go|run in circles|Awareness helps with control.
3.E|3|A key element of kicking is to...|transfer your weight from your back foot to your front foot|stay in one place|kick with your eyes closed|hop only|Weight transfer adds power.
3.E|3|For a strong kick, your non-kicking foot should be planted...|beside the ball|far behind you|on top of the ball|in the air|A planted foot gives balance.
3.F|3|Overhead volleying means you hit the ball with your...|fingertips above your forehead|knees|feet|elbows|Overhead sets use fingertips.
3.F|3|An underhand volley (bump) uses your...|forearms together|elbows|feet|head|Forearms form a platform.
3.G|3|When striking with a long-handled implement, you should keep your eye on the...|ball|ceiling|floor|crowd|Eyes on the ball improve contact.
3.H|3|An intermediate jump rope skill is...|crossing the rope|stopping|running away|folding the rope|Crosses add complexity.
3.I|3|Entering a turned long rope using an intermediate skill could be...|running in front door while the rope moves toward you|hiding|standing still|sitting|Front door means entering toward the jumper.
4.A|3|Closing space on a defender means you...|move toward the defender|run away|sit down|stand still|Closing space reduces the distance.
4.A|3|Using open space in a game means you...|move to a spot with no defenders|crowd together|stand behind a teammate|hide|Open space helps you receive the ball.
4.B|3|Using different pathways in a lead-up game helps you...|avoid defenders|stay the same|run in a line|stop|Pathways create angles.
4.C|3|Applying force during a throw means you...|use the correct amount of power|use no power|use all your power every time|stop|Force must match the task.
6.A|3|A lead-up game is a game that...|teaches skills used in a full sport|is not fun|has no rules|is only for adults|Lead-up games prepare you for full sports.
6.A|3|A basic strategy in a team game is to...|spread out to create space|stand together|stand still|ignore the ball|Spreading out helps passing.
6.B|3|Practicing a movement skill with a partner helps you...|get feedback and improve|forget|rest|quit|Partners give feedback.
6.C|3|Good sporting behavior means you...|shake hands and respect others|argue with the referee|brag|cheat|Respect is part of sportsmanship.
7|3|Which activity is an outdoor recreational pursuit?|hiking|computer coding|napping|sewing|Hiking is outdoor recreation.
7|3|A skill used in hiking is...|reading a trail map|baking|painting|typing|Trail maps guide the route.
8.A|3|Regular physical activity improves your overall...|health and wellness|boredom|stress|nothing|Activity benefits the whole body.
8.B|3|Frequency in a fitness plan is how often you...|exercise each week|rest|eat|sleep|Frequency is the number of times.
8.B|3|Intensity in endurance activities is...|how hard you work|how long the class is|your shoe size|your height|Intensity is effort.
8.C|3|Which is a health-related fitness component?|muscular strength|bat speed|dance style|ball color|Strength is a health-related component.
8.C|3|Agility is a skill-related component that means you can...|change direction quickly|lift heavy things|stretch far|hold your breath|Agility is quick changes of direction.
8.C|3|Cardiorespiratory endurance is the ability of your heart and lungs to...|supply oxygen during long activity|stop working|sleep|rest|It measures stamina.
9.A|3|A good personal fitness goal is one that is...|specific and measurable|vague|impossible|forgotten|Clear goals are easier to reach.
9.B|3|After tracking your fitness data for a month, you should...|look for patterns and improvements|throw it away|hide it|ignore it|Analyze to see progress.
10.A|3|Eating a balanced meal before a game helps your body by...|giving you energy to perform|making you sleepy|giving you a headache|slowing you down|Good nutrition supports performance.
10.A|3|Which snack helps performance after practice?|fruit and yogurt|candy only|soda|cake|Protein and carbs help recovery.
10.B|3|You should drink water...|before, during, and after activity|only after|never|only before|Stay hydrated all the time.
11.A|3|Choosing proper attire independently means you...|pick the right clothes and gear for the activity|ask for help every time|wear whatever|skip gear|Independent choices show responsibility.
11.B|3|Applying cycling safety means you always...|wear a helmet and obey signals|ride at night without lights|ride with no hands|skip stop signs|Helmets and rules prevent injuries.
11.B|3|When riding a scooter, you should...|wear a helmet and knee pads|ride barefoot|ride in traffic|ride with a friend on your lap|Pads protect against falls.
12.A|3|Taking responsibility for your actions means you...|admit your mistakes|blame others|hide|deny|Responsibility is honesty about actions.
12.B|3|Respecting differences in abilities during a game means you...|encourage others|make fun of them|ignore them|exclude them|Respect includes encouragement.
12.C|3|During a hard game, a self-management skill is to...|take a deep breath and stay calm|yell at the referee|quit|throw the ball|Calming strategies manage emotions.
13.A|3|A socially acceptable way to resolve a conflict is to...|talk it out calmly|fight|yell|ignore|Talking resolves problems.
13.A|3|Responding to a loss with dignity means you...|congratulate the winners|cry and blame others|walk away angry|cheat|Good sportsmanship includes graciousness.
13.B|3|Effective communication in settling a disagreement includes...|listening and using "I" statements|interrupting|shouting|ignoring|Listening helps both sides.
13.C|3|Showing respect for the feelings of others means you...|consider how they feel before you speak|laugh at them|ignore them|tease them|Empathy builds trust.
14|3|When a task is hard, perseverance means you...|keep trying with a plan|quit|complain|blame others|Perseverance is sustained effort.
14|3|A person shows perseverance when they...|practice a challenging skill each day|never practice|give up|avoid challenge|Daily effort builds skill.
15|3|Giving constructive feedback to a classmate should include...|a specific, kind suggestion|an insult|a laugh|silence|It should help them improve.
15|3|A good response to feedback is to...|ask questions and try the suggestion|get angry|quit|ignore it|Accepting feedback helps growth.
16.A|3|Moderate physical activity for a sustained period of time includes...|brisk walking|sitting|sleeping|reading|Brisk walking raises your heart rate.
16.A|3|Vigorous physical activity includes...|running or swimming laps|napping|watching TV|reading|It raises heart rate a lot.
16.B|3|Participating in a variety of community activities, such as joining a youth sports league, helps you...|stay active and make friends|become bored|stay inside|avoid people|Community activities build health and friendships.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g4_pe.jsonl'))
print("saved", len(B.out), "questions")

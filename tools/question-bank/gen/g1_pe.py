#!/usr/bin/env python3
"""Grade 1 Physical Education (TEKS 116.13.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('116.13.b.', 921, own='g1_pe.jsonl')

load(B, """
1.A|2|A first grader slides sideways across the gym. Which foot pattern is this?|step-together moving to the side|jumping on two feet in place|walking backward only|rolling on the floor|Sliding is a side step and close.
1.A|3|Which two skills have a quick "step-hop" rhythm, one foot after the other?|skipping|crawling|sitting|spinning|Skipping is a step and a hop on each foot.
1.A|2|To keep your balance while running, your arms should...|swing naturally by your sides|stay frozen over your head|hold your ears|stay in your pockets|Natural arm swing helps balance.
1.B|2|A quarter turn when jumping means you turn...|one quarter of the way around|all the way around twice|not at all|upside down|A quarter turn is 90 degrees.
1.B|2|When you land from a jump, bend your...|knees|elbows|ears|fingers|Bent knees absorb the landing.
1.C|3|Tracing a shape in the air with your finger while watching it uses...|visual tracking|sleeping|pushing|shouting|Tracking follows what you are drawing.
1.C|3|A sequence of three skills could be...|hop, jump, and spin|hop only|jump only|spin only|A sequence needs three skills in order.
1.D|2|Rolling at a low level means your body is...|close to the floor|up in the air|standing tall|on a chair|Levels describe height.
1.D|3|Spinning faster makes you feel more...|dizzy|calm|asleep|cold|Fast spinning affects balance.
2.A|2|How long should you hold your balance on one foot for this skill?|five seconds|one hour|one minute|one second|The skill asks for about five seconds.
2.A|3|To balance on one foot, the free leg can be...|bent behind you|dragging on the floor|in the air straight up only|tucked under the other|The free leg may be in many positions.
2.B|2|Swaying your body means you...|move gently from side to side|jump up and down|hold very still|run fast|Swaying is a gentle movement.
2.B|2|Twisting your body means you...|turn your middle without moving your feet|jump high|lie down|clap|Twisting rotates the torso.
3.A|3|Where should you aim when you throw underhand to a target?|at the center of the target|at the ceiling|behind you|at the floor far away|Aim at the middle of the target.
3.A|3|For an underhand throw, your arm swings back and then...|forward toward the target|up over your head|across your face|into your pocket|Swing back, then forward.
3.B|3|To catch a large ball softly, you should...|reach out and pull the ball in toward your body|stiffen your arms|turn your head away|swing at it|Soft hands absorb the ball.
3.B|2|The best way to catch a ball that is tossed gently is to use...|both hands|only your foot|only your head|no hands|Two hands help control a large ball.
3.C|2|Dribbling continuously means you...|keep bouncing the ball again and again|bounce once and stop|throw it away|roll it|Continuous dribbling is repeated bounces.
3.C|3|Which hand should you use first for dribbling?|your preferred hand|your elbow|neither hand|both feet|Start with the hand you prefer.
3.D|3|When dribbling with your foot while walking, you should keep the ball...|close to your feet|far ahead of you|in your hands|behind a wall|Close control keeps the ball with you.
3.E|2|Before you kick a ball that is still, you should first...|approach it with a step or two|run away from it|sit down|close your eyes|An approach adds power.
3.F|3|A partner volley means you...|hit a light object back and forth with a partner|throw it far away|hide it|sit on it|Partners keep it in the air.
3.G|3|When you strike an object with a short paddle, you want it to go...|upward|straight down|backward only|into the floor|The skill is to project it upward.
3.H|2|Jumping consecutively with a rope means you...|jump many times in a row|jump once and stop|walk away|sit|Consecutive means one after another.
3.I|2|When turning a long rope, the turners should...|swing it in a steady arc|let it drop|tie it|stand still with it|A steady turn helps the jumper.
4.A|2|Moving to a steady beat means your steps match the...|rhythm|weather|floor|wall|Match your movement to the music.
4.A|2|To stay safe in general space, you should move...|without bumping into others|with your eyes closed|by pushing|by running into walls|Safe movement avoids contact.
4.B|3|Traveling over an object means you...|pass above it|pass beneath it|stop in front of it|move away from it|Over means above.
4.B|3|Traveling under a low bar means you...|stay low and go beneath|jump above|stand tall|run around|Under means beneath.
4.B|2|Moving around a cone means you...|circle past it|go straight through it|sit on it|pick it up|Around goes past the object.
4.C|2|Which describes a strong force when moving?|a powerful push|a tiny tap|a whisper|a sleepy sigh|Strong force uses more power.
4.C|2|Which describes a light force?|a soft, gentle touch|a hard shove|a loud stomp|a big jump|Light force is gentle.
4.C|2|Which pair shows opposite speeds?|fast and slow|red and blue|big and large|loud and noisy|Fast and slow are opposites.
5|2|In a rhythmic activity, you can clap to the...|beat of the music|color of the wall|height of a ball|name of a shoe|Rhythm follows the beat.
5|3|A repeating set of short and long sounds in music is called...|a rhythm pattern|a gym rule|a fitness test|a bike path|Patterns repeat.
6.A|3|In a chasing game, you should avoid pushing and stay...|a safe distance and keep your speed under control|as close as possible|completely still|on the walls|Good spacing keeps everyone safe.
6.B|2|To improve a skill, you can follow your teacher's...|instructions and tips|jokes|snacks|bell|Teacher tips help you get better.
6.C|2|Using equipment appropriately means you...|use it only the way your teacher says|throw it at others|break it|hide it|Appropriate use is safe use.
6.C|2|Respecting personal space means...|keeping your hands and feet to yourself|touching friends often|crowding others|taking their ball|Personal space belongs to each person.
8.A|2|When you jump rope for a while, your heart rate...|goes up|goes to zero|stays asleep|disappears|Exercise raises heart rate.
8.A|3|You can feel your heart beat faster by placing your hand on your...|chest|knee|elbow|ear|You can feel it on your chest.
8.B|2|A warm-up is done before exercise to...|get your body ready|make you tired|skip the game|get you hurt|Warm-ups prepare muscles.
8.B|2|A cool-down after exercise helps your body...|slow down and relax|speed up|freeze|stop breathing|Cool-downs slowly lower heart rate.
8.C|2|Which is an exercise that builds strong muscles?|push-ups or crab walks|napping|watching videos|sitting|Strength exercises build muscle.
9.A|2|A health-related goal could be to...|walk 10 minutes every day|eat only candy|skip school|never sleep|A healthy goal improves health.
9.B|3|You can measure improvement in jumping by...|counting how many jumps you make|guessing|closing your eyes|asking the wall|Counting shows progress.
9.B|3|A measuring tool for how far you jump is a...|tape measure|clock|spoon|cup|Tapes measure distance.
10.A|2|Which food gives you energy before exercise?|a banana|a bag of chips only|a lollipop only|nothing|Fruit is a healthy energy source.
10.A|3|Which snack is a healthy source of energy?|apple slices|candy bars|soda|frosting|Fruit supports activity.
10.B|2|Besides water, a healthy hydration option is...|low-fat milk|energy drinks|soda|candy|Healthy drinks help hydration.
11.A|3|Which gear should you wear for roller skating?|a helmet and pads|sandals|a swimsuit|a scarf|Safety equipment protects you.
11.A|2|What footwear is best for running games?|closed-toe sneakers|high heels|flip flops|socks only|Sneakers support feet.
11.B|2|Water safety means you should swim...|with a grown-up watching|alone|in storms|without a lifeguard|Never swim alone.
11.B|2|Sun safety means you should wear...|sunscreen and a hat|a winter coat|a blindfold|nothing|Sun protection prevents burns.
11.B|3|Cycling safety means you should ride...|with a helmet and follow traffic rules|in the dark without lights|with no hands|in the middle of the road|Helmets and rules keep riders safe.
12.A|3|A positive consequence of practicing is that you...|get better at the skill|get worse|forget it|lose the ball|Practice improves skills.
12.A|3|A negative consequence of breaking a rule might be...|losing a turn|a prize|more time to play|a gold star|Rules have consequences.
12.B|2|Everyone has different abilities. A kind response is to...|encourage others|tease them|ignore them|laugh at them|Encouraging builds respect.
12.C|2|If you feel an impulse to grab, a good idea is to...|stop and think first|grab quickly|run away|yell|Pausing helps control impulses.
12.C|2|Excited, nervous, and proud are all...|feelings|sports|shapes|colors|Emotions are feelings.
13.A|2|On a team, cooperation means you...|work together|work alone|argue|compete against your teammates|Teams cooperate.
13.B|2|If you disagree with a classmate, you can say...|"I see it differently."|"You are wrong."|nothing and hit them|"Go away."|Respectful words resolve conflicts.
14|3|If you fall down during a game, perseverance means you...|get back up and keep trying|quit the game|blame the floor|hide|Perseverance is trying again.
14|2|When you keep practicing a hard skill, you show...|perseverance|laziness|anger|boredom|Sticking with it takes effort.
15|3|Accepting a coach's tip means you...|listen and try to use it|ignore it|argue|walk away|You learn by trying feedback.
15|3|Which is helpful feedback for a teammate?|"Try keeping your eyes on the ball."|"You are terrible."|"I quit."|"Don't try."|Helpful feedback is specific and kind.
16.A|2|Moderate to vigorous activity makes you breathe...|harder|slower|not at all|sleepy|Intense activity raises breathing.
16.A|2|About how much physical activity should kids get on most days?|at least 60 minutes|1 minute|none|5 seconds|Kids need regular daily activity.
16.B|2|A way to be active for fun is to...|play tag with friends|stay in bed|watch TV|sit in a chair|Active play can be fun.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g1_pe.jsonl'))
print("saved", len(B.out), "questions")

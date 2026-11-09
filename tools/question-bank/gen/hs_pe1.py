import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('116.62.', 1012, own='hs_pe1.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',3,"A lifter adds a little more weight to the bar each week so the muscles keep adapting. Which training principle is this?",
  "Progressive overload",["Specificity","Reversibility","Rest and recovery"],"Gradually raising the load is progressive overload.")
H('c.1.A',3,"A swimmer trains only in the pool and finds that her running endurance barely improves. Which principle explains this?",
  "Specificity: the body adapts to the type of training done",["Overload","Variety","Individuality"],"Training effects are specific to the activity.")
H('c.1.B',3,"Using a longer lever, such as a straight arm, makes a throw travel faster at the hand. What biomechanical idea is this?",
  "Longer levers can produce greater speed at the end",["Gravity stops throwing","Friction speeds the ball","Balance is not needed"],"A longer lever moves its tip faster for the same rotation.")
H('c.1.B',3,"A sprinter pushes backward against the track and moves forward. Which law of motion describes this?",
  "Newton's third law: every action has an equal and opposite reaction",["Newton's first law only","The law of gravity only","The law of friction only"],"Pushing back on the ground drives the body forward.")
H('c.2.A',2,"Before a workout on a weight machine, which safety step should you take first?",
  "Check that the pin and seat are set correctly",["Add the heaviest weight","Skip the warm-up","Ignore the instructions"],"Checking equipment prevents injuries.")
H('c.2.A',2,"Why should a spotter be used on a heavy bench press?",
  "To help if the lifter cannot finish a repetition",["To count the weight plates","To make the lift harder","To block other lifters"],"A spotter keeps the lifter safe.")
H('c.2.B',3,"A student practices a jump rope skill ten minutes a day for two weeks and gets smoother. This shows that skills improve with what?",
  "Regular, focused practice",["Luck alone","Avoiding practice","Skipping warm-ups"],"Deliberate practice improves performance.")
H('c.2.B',3,"Which practice habit best improves a skill during fitness activities?",
  "Repeating the movement with correct form and getting feedback",["Rushing through each rep","Practicing only when tired","Changing the skill every minute"],"Correct repetition builds skill.")
H('c.2.C',2,"A student performs a basic squat with feet shoulder-width apart and knees tracking over the toes. This shows competency in what?",
  "Using the proper technique for a basic exercise",["Advanced Olympic lifting","Marathon pacing","Rock climbing"],"Basic competency means correct form on a basic skill.")
H('c.2.C',3,"A competent performer of a basic push-up keeps the body in what position?",
  "A straight line from head to heels",["Hips high in the air","Hips sagging to the floor","Head dropped with a rounded back"],"A straight body line shows correct form.")
H('c.2.D',3,"A coach tells a student to keep her elbows closer to her body during a row. Using the coach's comment to adjust is which type of feedback?",
  "External feedback",["Internal feedback only","No feedback","Random feedback"],"Feedback from another person is external.")
H('c.2.D',3,"You feel your lower back arching on an overhead press and fix your posture. This is an example of what?",
  "Using internal feedback from body sensations",["Ignoring feedback","Relying only on a coach","Copying a stranger"],"Body sensations provide internal feedback.")
H('c.2.E',3,"A workout alternates 30 seconds of hard effort with 30 seconds of rest for several rounds. What method is this?",
  "Interval training",["Static stretching","A cool-down","Continuous easy walking"],"Alternating work and rest periods is interval training.")
H('c.2.E',3,"A routine moves through six stations of different exercises with little rest between them. What method is this?",
  "Circuit training",["Single-set training","A flexibility test","A warm-up walk"],"Circuit training rotates through stations.")
H('c.3.A',2,"Which clothing choice is best for a safe workout?",
  "Supportive athletic shoes and clothing that allows free movement",["Sandals","Jeans that restrict motion","Dress shoes"],"Proper attire reduces injury risk.")
H('c.3.A',2,"Before using free weights, a student should do what with the equipment?",
  "Inspect it and use collars and proper lifting technique",["Throw it to a partner","Leave it on the floor","Overload it right away"],"Safe handling prevents injury.")
H('c.3.B',3,"Which exercise technique is unsafe?",
  "Bouncing hard at the bottom of a deep stretch",["Slow controlled breathing during a lift","Keeping the spine neutral","Warming up before heavy sets"],"Ballistic bouncing can strain muscles and joints.")
H('c.3.B',3,"Holding your breath and locking the knees during a heavy lift can be harmful because it can do what?",
  "Raise blood pressure and strain joints",["Improve circulation","Prevent soreness","Strengthen bones instantly"],"Breath-holding and locked joints are risky.")
H('c.3.C',3,"On a hot, humid afternoon a runner sweats heavily. What is the best way to protect her?",
  "Drink fluids before, during and after exercise",["Avoid water","Wear extra layers","Run harder to finish sooner"],"Hydration offsets fluid lost to sweat.")
H('c.3.C',3,"Which sign suggests a person may be becoming dehydrated during exercise?",
  "Dizziness, dark urine and a dry mouth",["Clear urine","Feeling cool","Steady energy"],"Dehydration produces these signs.")
H('c.3.D',3,"Wellness includes more than the absence of disease. How does physical fitness relate to wellness?",
  "Fitness supports physical, mental and social wellness",["Fitness has no effect","Fitness harms wellness","Wellness only means diet"],"Fitness is one part of overall wellness.")
H('c.3.D',3,"A student who exercises regularly sleeps better and copes with stress more easily. This shows fitness contributes to what?",
  "Overall wellness",["Only muscle size","Only speed","Only flexibility"],"Fitness benefits several areas of wellness.")
H('c.3.E',2,"Which activity develops health-related fitness?",
  "Brisk swimming laps for 20 minutes",["Watching a video","Sitting during class","Eating a snack"],"Sustained swimming builds cardiorespiratory endurance.")
H('c.3.E',2,"Which activity mainly develops muscular strength?",
  "Weight training with progressive resistance",["Slow walking","Stretching only","Standing still"],"Resistance training builds strength.")
H('c.3.F',3,"To improve cardiorespiratory endurance, a person should train using which FITT idea?",
  "Sustained activity at a raised heart rate several days a week",["One slow stretch a month","Only lifting max weights","Resting every day"],"Endurance improves with regular sustained aerobic work.")
H('c.3.F',3,"To build muscular endurance, a good plan uses what?",
  "Lighter loads with higher repetitions",["One max rep a month","No resistance","Only static holds of one second"],"High reps with lighter loads build endurance.")
H('c.3.G',3,"Which pair includes one aerobic and one anaerobic activity?",
  "Distance cycling and heavy weightlifting",["Walking and jogging","Swimming and rowing","Stretching and yoga"],"Cycling is aerobic and heavy lifting is anaerobic.")
H('c.3.G',3,"A 100-meter sprint relies mostly on what kind of energy system?",
  "Anaerobic",["Aerobic only","No energy","Fat only"],"Short bursts of maximum effort are anaerobic.")
H('c.3.H',3,"A student uses a fitness watch to check her heart rate zones while running. What is this technology used for?",
  "Monitoring intensity to improve training",["Replacing exercise","Measuring height","Predicting the weather"],"Heart-rate tracking helps guide intensity.")
H('c.3.H',3,"Which technology tool best helps count steps across a week?",
  "A pedometer or activity tracker",["A stopwatch","A scale","A tape measure"],"Pedometers and trackers count steps.")
H('c.3.I',3,"A personal fitness plan should include which parts?",
  "Goals, activities for each fitness component, and a way to track progress",["Only a favorite song","A single exercise","No schedule"],"A plan sets goals, activities and tracking.")
H('c.3.I',3,"Which is a SMART goal for a fitness program?",
  "Run a mile in under 10 minutes by the end of 8 weeks",["Get fit someday","Be better","Exercise more maybe"],"SMART goals are specific, measurable and time-bound.")
H('c.3.J',3,"Agility, balance, coordination, power, reaction time and speed are examples of what?",
  "Skill-related components of fitness",["Health-related components","Types of food","Types of injury"],"These are the skill-related components.")
H('c.3.J',3,"A shuttle run is commonly used to measure which skill-related component?",
  "Agility",["Flexibility","Body composition","Muscular endurance"],"Shuttle runs test quick changes of direction.")
H('c.3.K',3,"A sit-and-reach test measures which health-related component?",
  "Flexibility",["Cardiorespiratory endurance","Power","Speed"],"Sit-and-reach measures flexibility of the hamstrings and back.")
H('c.3.K',3,"A timed one-mile run is used to evaluate what?",
  "Cardiorespiratory endurance",["Flexibility","Balance","Reaction time"],"Distance runs test aerobic capacity.")
H('c.4.A',3,"Regular physical activity is related to emotional health because it can do what?",
  "Reduce stress and improve mood",["Increase every worry","Remove all sleep","Cause isolation"],"Exercise supports mood and lowers stress.")
H('c.4.A',3,"Playing on a team can improve social health by doing what?",
  "Building cooperation and friendships",["Encouraging isolation","Removing communication","Ending trust"],"Team activity builds social skills.")
H('c.4.B',3,"A student who failed to run a mile in 12 minutes improves to 10 minutes after weeks of training. This shows that what?",
  "Improvement is possible with appropriate practice",["Skill is fixed","Practice is pointless","Only genetics matter"],"Practice produces improvement.")
H('c.4.B',3,"Which statement shows a growth mindset about fitness?",
  "I can get stronger if I keep training consistently",["I was born weak and always will be","I never improve","Training is useless"],"A growth mindset values effort.")
H('c.4.C',3,"A teammate misses the winning shot. Which is the best response?",
  "Encourage him and focus on learning from the play",["Blame him","Mock him","Leave the team"],"Supportive responses handle failure well.")
H('c.4.C',3,"A conflict starts over a rule during a game. Which action resolves it best?",
  "Calmly discuss the rule and agree on a solution",["Yell at the group","Quit","Ignore the rule"],"Calm communication resolves conflict.")
H('c.4.D',3,"A student wins a match and a rival loses. Which behavior shows good sportsmanship?",
  "Shaking hands and acknowledging the opponent's effort",["Bragging loudly","Ignoring the rival","Making excuses"],"Respect is shown in success and defeat.")
H('c.4.D',3,"Accepting a performance limitation, such as a slower time, means doing what?",
  "Working on it respectfully without putting yourself or others down",["Giving up forever","Blaming a teammate","Cheating to hide it"],"Healthy acceptance is paired with effort.")
H('c.4.E',3,"Spending several hours on screens instead of moving can affect social and emotional health by doing what?",
  "Reducing activity and face-to-face connection",["Always improving mood","Replacing sleep needs","Increasing fitness automatically"],"Excess screen time can reduce activity and connection.")
H('c.4.E',3,"Using a fitness app to share goals with friends can have what positive effect?",
  "It can increase motivation and support",["It prevents all injuries","It replaces exercise","It always lowers stress"],"Social features can motivate.")
H('c.5.A',3,"Why is sleep important for an athlete?",
  "It allows the body to recover and supports performance",["It reduces strength","It slows learning","It is unrelated to training"],"Recovery happens during sleep.")
H('c.5.A',3,"A student sleeping five hours a night before a meet will most likely experience what?",
  "Slower reaction time and lower performance",["Better reactions","More energy for all events","Faster recovery"],"Sleep loss hurts performance.")
H('c.5.B',3,"Which statement is a myth about physical activity?",
  "Doing thousands of crunches burns the fat from your stomach only",["Exercise raises heart rate","Muscles need rest","Warm-ups help prevent injury"],"Spot reduction is a myth.")
H('c.5.B',3,"Which is a nutrition myth?",
  "Skipping meals is a healthy way to lose weight fast",["Water supports exercise","Protein helps muscle repair","Whole grains give energy"],"Skipping meals is not a healthy strategy.")
H('c.5.C',3,"Eating a balanced meal with carbohydrates before long exercise helps because it does what?",
  "Provides energy for the workout",["Prevents all fatigue","Replaces warm-up","Removes the need for water"],"Carbohydrates fuel exercise.")
H('c.5.C',3,"After a hard workout, a snack with protein and carbohydrates helps by doing what?",
  "Supporting muscle repair and restoring energy",["Reducing recovery","Causing dehydration","Preventing sleep"],"Protein and carbs aid recovery.")
H('c.5.D',3,"An athlete who trains hard every day with no rest days feels constantly tired and gets injured often. What is the likely cause?",
  "Over training",["Under training","Good recovery","Proper nutrition"],"Too much training without recovery causes problems.")
H('c.5.D',3,"Which is a sign of over training?",
  "Persistent fatigue, declining performance and mood changes",["Steady improvement","Better sleep","Increased energy"],"These are common signs of over training.")
H('c.5.E',3,"An ad promises that a pill will melt away fat without exercise. How should a smart consumer respond?",
  "Be skeptical and check the claim with a reliable source",["Buy immediately","Share it with friends","Trust any celebrity"],"Marketing claims need evidence.")
H('c.5.E',3,"Which source is the most reliable for fitness advice?",
  "A certified trainer or a medical professional",["A random comment","An anonymous ad","A rumor"],"Credentials indicate reliability.")
H('c.5.F',3,"Which combination best improves body composition?",
  "Regular exercise and balanced nutrition",["Crash dieting only","Sitting more","Skipping sleep"],"Both exercise and nutrition affect body composition.")
H('c.5.F',3,"Body composition refers to the proportion of what in the body?",
  "Fat mass compared with lean mass such as muscle and bone",["Height to weight only","Blood types","Hair to skin"],"It compares fat and lean tissue.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_pe1.jsonl'))

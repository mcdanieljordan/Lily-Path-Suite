import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('116.64.', 1014, own='hs_pe3.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',2,"In archery, the target is hit by releasing an arrow toward a bull's-eye. Archery is classified as which type of activity?",
  "A target activity",["A striking and fielding activity","A rhythmic activity","An invasion game"],"Target activities aim an object at a goal.")
H('c.1.A',2,"Disc golf is an example of which kind of activity?",
  "A target activity",["A rhythmic activity","A swimming event","A wrestling event"],"Players throw discs at targets.")
H('c.1.B',2,"Which sport is a striking and fielding activity?",
  "Softball",["Archery","Swimming","Dance"],"Softball involves striking a ball and fielding it.")
H('c.1.B',3,"In a striking activity, a batter keeps the eyes on the ball and shifts weight forward during the swing. This shows what?",
  "Proper technique for contact and power",["A poor stance","A fielding error","An illegal move"],"Watching the ball and weight transfer improve contact.")
H('c.1.C',3,"Which activity promotes cardiorespiratory endurance and muscular strength?",
  "Circuit training",["Standing still","A board game","Sitting stretches only"],"Circuits combine cardio and strength work.")
H('c.1.C',3,"A student who completes a 20-minute continuous workout at a raised heart rate is showing competency in what?",
  "A fitness activity for cardiorespiratory endurance",["A target activity","An officiating skill","A scorekeeping skill"],"Sustained aerobic activity builds endurance.")
H('c.1.D',2,"Square dancing and line dancing are examples of what?",
  "Rhythmic activities",["Target activities","Fielding activities","Weight training"],"Rhythmic activities move to a beat.")
H('c.1.D',3,"In a rhythmic activity, keeping steps in time with the music requires what?",
  "Following the beat and tempo",["Ignoring the music","Moving at random","Standing still"],"Timing to the beat is essential.")
H('c.1.E',3,"Ultimate and pickleball are growing in popularity. Why are they called innovative games?",
  "They are newer activities that mix familiar skills with new rules",["They have no rules","They cannot be played outside","They are ancient games"],"Innovative games blend skills in new ways.")
H('c.1.E',3,"A class invents a new game by combining throwing and running with a new scoring rule. What is this?",
  "An innovative game",["A rhythmic routine","A warm-up only","An officiating signal"],"Creating a new game is innovation.")
H('c.2.A',3,"A player hits the same basic serve correctly seven of ten times and uses it in the match. This shows what?",
  "Performing a skill consistently",["Rarely using the skill","Random luck","Poor strategy"],"Consistency means repeating the skill accurately.")
H('c.2.A',3,"Which strategy is a sound choice in a doubles match?",
  "Covering open space and communicating with your partner",["Standing in the same spot","Ignoring the partner","Hitting every ball the same way"],"Strategy uses space and teamwork.")
H('c.2.B',3,"After missing a free throw short, a player notices the shot felt weak and adds more leg drive on the next try. This is an example of what?",
  "Using internal feedback to adjust",["Ignoring feedback","Copying a rival","Only external feedback"],"The player used body sensation to adjust.")
H('c.2.B',3,"A coach says, \"Follow through toward the target.\" Applying that tip is what type of feedback?",
  "External feedback",["Internal feedback only","No feedback","Random feedback"],"A coach's comment is external feedback.")
H('c.2.C',3,"Which is an appropriate practice procedure to improve a tennis serve?",
  "Practice with focus, repeat the correct form and review results",["Practice only the day before a match","Rush through every serve","Skip warm-ups"],"Focused repetition improves skill.")
H('c.2.C',3,"To improve strategy in a sport, a player should do what?",
  "Study game situations and practice decisions in drills",["Avoid learning the rules","Play without thinking","Never watch games"],"Strategy improves through study and drill.")
H('c.2.D',3,"In a volleyball serve, which is a critical element of success?",
  "Contacting the ball with a firm hand and a smooth follow-through",["Hitting with a loose wrist","Looking away","Closing the eyes"],"Contact and follow-through determine accuracy.")
H('c.2.D',3,"Which critical element helps a bowler or pitcher deliver accurately?",
  "A consistent release point and follow-through",["Changing the release point every time","Looking away","Skipping the stance"],"Consistent mechanics improve accuracy.")
H('c.2.E',3,"An official raises one arm straight overhead to signal a score. This is an example of what?",
  "A hand signal used in officiating",["A foul by the player","A rule change","A warm-up"],"Hand signals communicate calls.")
H('c.2.E',3,"Which is proper officiating technique?",
  "Using clear signals and a firm, calm voice to explain the call",["Shouting at players","Ignoring plays","Making calls without watching"],"Clear communication is key.")
H('c.2.F',3,"A scorekeeper must record points as they happen. Why is accuracy important?",
  "It ensures a fair result and correct standings",["It speeds up the game","It is optional","It changes the rules"],"Accurate scoring keeps the game fair.")
H('c.2.F',3,"In a game where a team scores 3, 2 and 4 points in three innings, the total is how many points?",
  "9",["8","10","7"],"3 + 2 + 4 = 9.")
H('c.3.A',3,"A student wants to improve her cardio for pickleball. Which goal is realistic and challenging?",
  "Play three 30-minute sessions a week for six weeks and track progress",["Never play","Play once next year","Be fit sometime"],"A goal should be specific, measurable and time-bound.")
H('c.3.A',3,"Why should fitness goals be matched to the chosen skill-based activity?",
  "So training improves the fitness parts the activity needs",["So the plan is random","So there is no progress","So the activity is easier to skip"],"Goals should serve the activity.")
H('c.3.B',2,"Before playing a sport, a student should do what to reduce injury?",
  "Warm up and use proper equipment",["Skip stretching","Play barefoot on rough ground","Ignore pain"],"Warm-ups and gear protect players.")
H('c.3.B',3,"Which safety procedure applies when many players share a court or field?",
  "Stay aware of others and follow the rules for boundaries",["Run without looking","Ignore the rules","Throw equipment at others"],"Awareness prevents collisions.")
H('c.3.C',3,"Which health benefit results from regularly playing a skill-based sport like tennis?",
  "Improved cardiorespiratory endurance and coordination",["Lower flexibility only","Weaker bones","Decreased energy"],"Skill-based sports provide fitness benefits.")
H('c.3.C',3,"Playing a lifetime sport with others can also improve what?",
  "Social and emotional health",["Only sleep","Only height","Nothing"],"Participation builds social bonds.")
H('c.4.A',3,"A player congratulates an opponent on a great shot. This shows what?",
  "Good sportsmanship",["Poor sportsmanship","A rule violation","A foul"],"Acknowledging good play is sportsmanship.")
H('c.4.A',3,"Which is an example of acknowledging good play?",
  "Saying \"nice shot\" to the other team",["Making fun of the player","Ignoring the point","Arguing the call"],"Positive remarks show respect.")
H('c.4.B',3,"Why should players accept the roles and decisions of officials?",
  "It keeps the game fair and respectful",["Officials never make calls","So players can break rules","To make the game last longer"],"Officials enforce fair play.")
H('c.4.B',3,"If you disagree with a call, the best response is to do what?",
  "Calmly accept it and keep playing",["Throw the ball","Yell at the official","Leave the game"],"Calm acceptance models sportsmanship.")
H('c.4.C',3,"After losing a match, a player admits the other team played better and plans to practice more. This shows what?",
  "Accepting performance limitations and responding with effort",["Blaming officials","Quitting","Making excuses"],"Healthy acceptance leads to improvement.")
H('c.4.C',3,"Accepting a teammate's mistake with encouragement helps the team because it does what?",
  "Builds trust and morale",["Increases blame","Ends the game","Creates conflict"],"Support builds team spirit.")
H('c.4.D',3,"What does personal responsibility mean for creating a safe, respectful environment in a class?",
  "Following rules and treating others with respect",["Letting others do the work","Ignoring rules","Teasing others"],"Everyone helps maintain a positive environment.")
H('c.4.D',3,"A student sees equipment left on the floor and puts it away. This shows what?",
  "Personal responsibility for safety",["Carelessness","Rule breaking","Disrespect"],"Taking care of the space keeps it safe.")
H('c.4.E',3,"After a tough loss, which response is the healthiest?",
  "Review what went wrong and set a plan to improve",["Blame others","Quit forever","Hide your feelings"],"A constructive response uses the setback to grow.")
H('c.4.E',3,"How should a player respond to a big win?",
  "Celebrate respectfully without taunting opponents",["Mock the other team","Brag loudly","Ignore teammates"],"Respectful celebration is sportsmanship.")
H('c.5.A',2,"Which choice supports lifelong physical activity?",
  "Choosing a skill-based activity you enjoy and can keep doing",["Avoiding all sports","Doing one workout a year","Only watching sports"],"Enjoyable activities are easier to continue.")
H('c.5.A',2,"Why would a student pick one skill-based lifetime activity to participate in regularly?",
  "To build skill, fitness and enjoyment over time",["To avoid activity","To quit quickly","To lower fitness"],"Regular participation builds skill and fitness.")
H('c.5.B',3,"Why is sleep important for athletes in skill-based sports?",
  "It supports recovery, reaction time and learning of skills",["It reduces focus","It lowers skill","It is not important"],"Sleep helps performance and recovery.")
H('c.5.B',3,"A player who sleeps only a few hours before a tournament will likely have what?",
  "Slower reactions and lower performance",["Faster reactions","Better accuracy","More endurance"],"Sleep loss harms performance.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_pe3.jsonl'))

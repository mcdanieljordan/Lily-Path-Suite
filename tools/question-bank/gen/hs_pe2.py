import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('116.63.', 1013, own='hs_pe2.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',2,"A new hiker learns to read a trail map and use a compass. This is an example of building what?",
  "A basic skill for outdoor navigation",["An advanced racing technique","A team sport rule","A swimming stroke"],"Map and compass use is a basic outdoor skill.")
H('c.1.A',2,"Which is a basic skill in recreational paddling?",
  "Using a forward stroke to move a canoe in a straight line",["Throwing a javelin","Spiking a volleyball","Serving a tennis ball"],"A forward stroke is a core paddling skill.")
H('c.1.B',3,"At a disc golf course, a player must throw from behind the tee line and play the disc where it lands. This is an example of what?",
  "Following the rules of the activity",["Breaking an etiquette rule","Skipping the strategy","Using no equipment"],"Rules set how play proceeds.")
H('c.1.B',3,"On a windy day, a golfer chooses a lower, flatter shot to keep the ball from drifting. This is an example of what?",
  "Applying strategy to conditions",["Ignoring the rules","Skipping the warm-up","Avoiding practice"],"Strategy adapts to the environment.")
H('c.1.C',3,"A person training for a weekend backpacking trip builds a plan with hill walks, a loaded pack and leg strength work. What is this?",
  "A conditioning program matched to the activity",["A random list","A rest-only plan","A cooking plan"],"Conditioning is tailored to the demands of the activity.")
H('c.1.C',3,"A kayaker designs a conditioning program. Which fitness area should it most emphasize?",
  "Upper-body and core endurance",["Only leg flexibility","Only reaction time","Only balance on a beam"],"Paddling relies on the upper body and core.")
H('c.2.A',3,"A rock climber sees her foot slipping and moves her weight over it, then adjusts her grip. This shows what?",
  "Modifying movement using internal feedback",["Ignoring feedback","Only external feedback","Random movement"],"Body sensations guide adjustments.")
H('c.2.A',3,"A guide tells a beginner to keep her hands wider on the paddle. Using the tip is which type of feedback?",
  "External feedback",["Internal feedback only","No feedback","Delayed feedback only"],"Information from another person is external.")
H('c.2.B',3,"Which is a critical element of a successful cast in fishing?",
  "Smooth release timing and a controlled follow-through",["Throwing as hard as possible","Closing your eyes","Using no line"],"Timing and follow-through control the cast.")
H('c.2.B',3,"In archery, which critical element helps accuracy?",
  "A consistent stance and steady anchor point",["Changing grip every shot","Ignoring the target","Rushing each shot"],"Consistency improves accuracy.")
H('c.3.A',2,"Which outdoor pursuit provides enjoyment along with health benefits?",
  "Hiking on a trail with friends",["Sitting indoors all day","Skipping activity","Watching a screen"],"Hiking offers enjoyment and activity.")
H('c.3.A',2,"Why do people choose lifetime activities such as cycling or swimming?",
  "They can be enjoyed throughout life for fitness and fun",["They can only be done once","They end at graduation","They require a team of ten"],"Lifetime activities last across ages.")
H('c.3.B',3,"To improve flexibility for hiking and climbing, a person should perform what?",
  "Regular stretching held for 15 to 30 seconds after warming up",["Bouncing stretches while cold","Skipping stretching","Only running"],"Held stretches after a warm-up improve flexibility.")
H('c.3.B',3,"Which training principle states that muscle needs gradually increasing resistance to grow stronger?",
  "Progressive overload",["Detraining","Rest day only","Cooling down only"],"Gradual loading improves strength.")
H('c.3.C',3,"Which fitness goal is realistic and challenging?",
  "Hike 5 miles without stopping within six weeks of regular walks",["Run a marathon tomorrow","Never exercise","Improve someday"],"A good goal is measurable and reachable.")
H('c.3.C',3,"Why should health-related fitness goals be written with a time frame?",
  "So progress can be measured and the plan adjusted",["So the goal is harder to track","To avoid effort","To hide results"],"Time frames make goals measurable.")
H('c.3.D',3,"A hiker uses a GPS watch to track distance and elevation. What is this technology used for?",
  "Monitoring activity to evaluate and improve fitness",["Replacing fitness","Predicting injuries only","Controlling the weather"],"Trackers provide data to evaluate progress.")
H('c.3.D',3,"Which tool can display heart rate while exercising outdoors?",
  "A heart rate monitor",["A thermometer","A compass","A flashlight"],"A heart rate monitor shows intensity.")
H('c.3.E',3,"Regular cycling can improve which fitness area?",
  "Cardiorespiratory endurance and leg strength",["Only hand speed","Only reading skills","Only reaction time"],"Cycling works the heart, lungs and legs.")
H('c.3.E',3,"Which is a health benefit of regular outdoor recreation?",
  "Lower stress and improved fitness",["More stress only","Less sleep always","Lower fitness"],"Outdoor activity benefits body and mind.")
H('c.3.F',3,"A personal fitness program for outdoor pursuits should include what?",
  "Goals, planned activities, progress checks and rest",["Only one workout","No plan","Only snacks"],"A program sets goals and tracks progress.")
H('c.3.F',3,"A student begins a four-week program of walking, bodyweight strength work and stretching. What should come next in the program cycle?",
  "Evaluate results and adjust the plan",["Quit","Stop tracking","Start over with no data"],"Evaluation guides adjustments.")
H('c.4.A',3,"Two hikers share the navigation and decision making on a long trail. This shows what teamwork skill?",
  "Cooperation and shared problem solving",["Competition only","Avoidance","Isolation"],"Teams share tasks and decisions.")
H('c.4.A',3,"A group on a ropes course helps each other through an obstacle. Which skill is demonstrated?",
  "Trust and support",["Selfishness","Silence only","Ignoring teammates"],"Trust and support build teams.")
H('c.4.B',3,"At a campsite, which behavior shows good outdoor etiquette?",
  "Keeping noise low and leaving the site clean",["Playing music loudly all night","Leaving trash","Cutting new trails"],"Etiquette respects others and nature.")
H('c.4.B',3,"A cyclist on a shared trail should do what when approaching a walker from behind?",
  "Announce the pass and slow down",["Speed up silently","Ride on the grass","Ignore the walker"],"Courtesy keeps shared trails safe.")
H('c.4.C',3,"A student replaces hours of screen scrolling with a daily walk and feels calmer. What does this show?",
  "Technology use can affect mood and activity levels",["Screens never matter","Walking is harmful","Mood never changes"],"Habits affect social and emotional health.")
H('c.4.C',3,"Which is a possible positive use of technology for outdoor activity?",
  "Using a map app to find trails and share plans with friends",["Replacing all exercise","Ignoring safety","Hiding from others"],"Technology can support healthy habits.")
H('c.4.D',3,"A student reads an article on how time in nature affects mood and summarizes the main points. This shows which skill?",
  "Analyzing and summarizing critical information",["Guessing","Copying","Ignoring sources"],"Summarizing shows understanding of the research.")
H('c.4.D',3,"Which source would be best for information about the mental health benefits of outdoor activity?",
  "A peer-reviewed study or a health agency",["An anonymous post","A rumor","A product ad"],"Credible sources provide reliable evidence.")
H('c.4.E',3,"A personal wellness plan that includes outdoor pursuits might schedule what?",
  "Weekly time outside for hiking, biking or paddling",["No activity","Only screen time","Only snacks"],"A wellness plan sets regular activity.")
H('c.4.E',3,"Which part of a wellness plan supports emotional health?",
  "Spending time outdoors with supportive people",["Isolation","Ignoring stress","Skipping sleep"],"Social time outdoors supports emotional health.")
H('c.5.A',2,"Which is required safety equipment for riding a bicycle on a trail?",
  "A properly fitted helmet",["Sandals","Headphones turned up loud","A heavy backpack"],"A helmet protects the head.")
H('c.5.A',2,"A person paddling a kayak should wear what?",
  "A personal flotation device",["Heavy boots","A winter coat only","A blindfold"],"A life jacket prevents drowning.")
H('c.5.B',3,"Before a hike a person should file a plan with someone, which means what?",
  "Telling a trusted person the route and expected return time",["Telling no one","Hiding the route","Leaving without water"],"Someone can raise an alarm if you do not return.")
H('c.5.B',3,"If a thunderstorm approaches while hiking in the open, the safest procedure is to do what?",
  "Move to lower ground or shelter and avoid isolated tall objects",["Stand on a hilltop","Stand under the tallest tree","Hold a metal pole up"],"Avoid exposed high spots in lightning.")
H('c.5.C',3,"Which fitness principle applies when a hiker gradually increases trail distance each week?",
  "Progression",["Reversibility","Rest","Specificity"],"Gradual increases are progression.")
H('c.5.C',3,"The FITT principle stands for frequency, intensity, time and what?",
  "Type",["Test","Tempo","Terrain"],"Type is the T that follows time.")
H('c.5.D',3,"After a day of hiking, a person's body needs sleep because sleep does what?",
  "Supports muscle repair and restores energy",["Slows recovery","Reduces strength","Removes fitness"],"Recovery occurs during sleep.")
H('c.5.D',3,"A camper stays up all night and tries a long bike ride in the morning. What is the likely outcome?",
  "Lower performance and higher injury risk",["Better performance","Faster reactions","More energy"],"Sleep loss harms performance and safety.")
H('c.5.E',3,"Which is an advantage of outdoor recreation compared with a gym workout?",
  "Natural scenery and varied terrain",["Guaranteed perfect weather","No cost ever","No travel ever"],"Outdoor activity offers variety.")
H('c.5.E',3,"Which is a disadvantage of some outdoor pursuits?",
  "Weather, travel and equipment costs",["No risks at all","Always free","Always indoors"],"Outdoor pursuits have tradeoffs.")
H('c.5.F',3,"A student records mile times each week for two months and sees them drop. This provides what?",
  "Evidence of improved health-related fitness",["No evidence","Proof of injury","A lower grade"],"Data show progress.")
H('c.5.F',3,"Which is evidence that a person is maintaining fitness?",
  "Consistent test results and regular activity logs",["Skipping workouts","No data","Random guesses"],"Consistent data show maintenance.")
H('c.5.G',3,"A climber designs a safe practice routine by starting on easy routes with a belay partner and moving up gradually. What does this show?",
  "A safe, progressive way to improve skill",["A random approach","Skipping safety","Climbing alone at height"],"Safe progression reduces risk.")
H('c.5.G',3,"Which practice procedure is safest for improving a new skill?",
  "Learn with supervision and increase difficulty gradually",["Try the hardest version first","Skip instruction","Practice alone in danger"],"Gradual, supervised practice is safest.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_pe2.jsonl'))

#!/usr/bin/env python3
"""Grade 4 Health Education (TEKS 115.16.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('115.16.b.', 934, own='g4_health.jsonl')

load(B, """
1|3|Which body system uses hormones to send chemical messages through the blood?|endocrine system|skeletal system|digestive system|urinary system|The endocrine system makes hormones.
1|3|Which two systems work together to deliver oxygen to your muscles?|respiratory and circulatory|digestive and urinary|skeletal and nervous|immune and endocrine|Lungs take in oxygen and blood carries it.
1|4|Which body system includes the skin, which protects against germs and helps control temperature?|integumentary system|digestive system|skeletal system|endocrine system|The integumentary system covers the body.
1|3|Muscles that move your arm are part of the...|muscular system|urinary system|respiratory system|digestive system|Muscles create movement.
2.A|3|Why is health information important?|it helps you make informed choices|it makes decisions for you|it replaces doctors|it is always secret|Information supports good decisions.
2.A|4|Reading the safety instructions on a medicine label is an example of using health information to...|take medicine correctly|choose a color|play a game|cook dinner|Labels help you use medicine safely.
2.B|4|Which external factor can influence health care decisions?|cost of care|the color of a car|the weather in another state|a pet's name|Cost can limit choices.
2.B|4|Access to a clinic near your home can influence...|whether people get checkups|the shape of the moon|the color of the sky|how loud thunder is|Access affects care.
2.C|3|Which strategy helps you keep good personal hygiene?|showering and wearing clean clothes|wearing the same dirty socks|skipping handwashing|sharing combs|Cleanliness prevents illness.
2.C|3|Brushing your tongue and flossing daily help you maintain...|oral health|bone strength|eyesight|hearing|These habits keep your mouth healthy.
2.D|3|A communicable illness is one that...|can spread from person to person|cannot be caught|is caused by a bone injury|is only from food|Communicable means contagious.
2.D|4|Which is a noncommunicable condition?|diabetes|strep throat|chickenpox|the flu|Diabetes is not contagious.
2.D|3|Which illness is communicable?|a cold|asthma|a broken leg|a sprained ankle|Colds are contagious.
2.E|4|If a person with asthma has trouble breathing, they should use...|their inhaler and tell an adult|a heavy blanket|a loud fan|candy|Inhalers relieve symptoms.
2.E|4|If a classmate with diabetes feels shaky and dizzy, you should...|tell a teacher or nurse right away|ignore it|play a game|run away|Low blood sugar needs adult help.
2.E|4|If someone has a seizure from epilepsy, you should...|stay calm, protect their head, and call for help|hold their mouth open|shake them|give them water|Keep them safe and get an adult.
2.F|4|Vector-borne illnesses are spread by...|insects such as ticks and mosquitos|handshakes|hugs|books|Vectors carry germs between hosts.
2.F|4|One way to lower your risk of vector-borne illness is to...|wear insect repellent and check for ticks|swim in swamps at dawn|leave water pooling in buckets|walk in tall grass in shorts|Prevention reduces bites.
3.A|4|How can a thought like "I will fail" affect behavior?|you may avoid trying|you may try harder for sure|you may fly|you may grow taller|Thoughts shape actions.
3.A|3|Feeling proud of your work can lead you to...|keep working hard|give up|hide|run away|Positive emotions encourage effort.
3.B|4|Reframing a thought means...|looking at it in a more helpful way|ignoring it|making it louder|forgetting it|Reframing changes perspective.
3.B|4|Changing "I'm terrible at this" to "I'm still learning" is an example of...|reframing a thought|ignoring a problem|giving up|bragging|The new thought is more helpful.
3.C|4|During childhood, the brain grows and builds stronger...|connections between brain cells|toenails|shoe sizes|bones only|Learning forms connections.
3.C|4|The brain plays a major role in controlling...|thoughts, feelings, and actions|only your fingernails|only your hair|only your toes|The brain directs everything.
3.D|3|A positive characteristic of a social group is...|members support one another|members bully others|members pressure others to break rules|members exclude others unfairly|Support is positive.
3.D|4|A negative characteristic of a social group is...|excluding people for being different|sharing ideas|encouraging teamwork|including newcomers|Exclusion hurts.
3.E|3|A positive role model...|sets a good example for others|breaks rules|teases others|cheats|Role models show good behavior.
3.E|4|Why is being a positive role model important?|younger kids copy what they see|nobody is watching|it makes you taller|it is a secret|Others learn from you.
3.F|4|When talking to someone with a hearing difference, showing consideration could mean...|facing them and speaking clearly|shouting|turning away|whispering|Consideration helps communication.
3.F|4|Being considerate when you speak to a new student who speaks another language means you...|speak slowly and kindly|laugh at them|ignore them|talk very fast|Patience shows respect.
3.G|4|A friend is quiet, looking down, and slumped. These cues suggest they may feel...|sad|excited|proud|silly|Body language shows feelings.
3.G|4|A situational cue that a classmate might be upset is...|they just lost a game|they just got a prize|they are laughing|they are dancing|Context gives clues.
3.H|4|Assertive behavior means you...|state your needs calmly and respectfully|yell and threaten|stay silent always|hit|Assertiveness is respectful.
3.H|4|Aggressive behavior is...|forceful and disrespectful to others|calm and respectful|polite|silent|Aggression harms others.
3.H|4|"I need you to stop, please," said calmly, is an example of...|assertive behavior|aggressive behavior|passive behavior|silent behavior|It is firm but respectful.
4.A|3|A way to help build a friend's self-esteem is to...|give sincere compliments|point out flaws|ignore them|compare them to others|Kind words build confidence.
4.A|4|Building your own self-esteem includes...|noticing your strengths and areas for growth|ignoring all feedback|comparing yourself to everyone|never trying|Balanced thinking builds esteem.
4.B|3|A short-term goal is something you can finish...|soon, like this week|in thirty years|never|only as an adult|Short-term goals take little time.
4.B|4|Setting goals helps you...|focus and measure progress|avoid all work|forget plans|stay confused|Goals give direction.
4.B|4|Which is a long-term goal?|saving money for a bike over several months|finishing homework tonight|brushing teeth|eating lunch|Long-term goals take more time.
4.C|3|Time management means...|planning how to use your time wisely|wasting time|doing nothing|watching clocks only|It helps you reach goals.
4.C|4|A planner or calendar helps you...|keep track of tasks and deadlines|lose homework|waste time|skip goals|Planning supports goals.
5.A|4|A student with a long-term health condition can manage concerns by...|talking to a trusted adult and following a plan|hiding it|skipping treatment|ignoring symptoms|Support and plans reduce worry.
5.A|4|Telling a school nurse about a long-term condition helps...|the school support your needs|nobody|the cafeteria|the bus|Schools can plan care.
5.B|4|Positive stress can help you...|stay motivated for a challenge|feel sick forever|forget your work|avoid people|Positive stress helps performance.
5.B|4|Negative stress is stress that...|feels overwhelming and harms well-being|always helps|is fun|never happens|Negative stress is harmful.
5.C|4|Loss and grief can be sources of...|stress|height|sleep only|hunger only|They cause emotional stress.
5.C|4|Which could be a source of stress?|a big move to a new town|a sunny day|a quiet nap|a snack|Big changes cause stress.
5.D|3|A healthy body image means...|accepting and caring for your body|hating your body|comparing to celebrities only|ignoring health|Body image is how you see your body.
5.D|4|A way to promote a healthy body image is to...|focus on what your body can do|tease others about their size|compare yourself to photos|skip meals|Focus on function and health.
5.E|4|When feeling overwhelmed, a healthy way to express your feelings is to...|talk to a trusted adult or write in a journal|hurt yourself|hurt others|break things|Healthy outlets keep everyone safe.
5.E|4|Which helps you manage anger without harm?|going for a walk|yelling at a friend|throwing a chair|keeping it bottled up forever|Exercise releases tension safely.
6.A|4|Which nutrient is the main source of quick energy?|carbohydrates|vitamins|minerals only|water only|Carbs fuel the body.
6.A|4|The six major nutrients are carbohydrates, proteins, fats, vitamins, minerals, and...|water|candy|salt|spices|Water is the sixth nutrient.
6.A|4|Calcium is a mineral that helps build...|strong bones and teeth|hair color|skin color|eye color|Calcium strengthens bones.
6.B|4|On a food label, serving size tells you...|the amount of food the nutrition facts are based on|the price|the color|the brand|Nutrition facts match the serving size.
6.B|4|On a menu, calorie counts can help you...|choose meals that fit your needs|ignore your body|waste money|speed up cooking|Information supports choices.
6.C|4|When eating out, you can control portions by...|sharing a meal or taking half home|ordering the largest size always|finishing every bite no matter what|adding extra sauce|Sharing reduces portion size.
6.C|4|Fast food portions are often...|larger than a healthy serving|always tiny|exactly right|too small to see|Fast food servings are often big.
6.D|4|Experts recommend limiting...|added sugar|water|vegetables|fruit|Too much added sugar harms health.
6.D|4|Too much added sugar over time can lead to...|tooth decay and weight gain|stronger teeth|taller bones|better vision|Excess sugar harms health.
6.E|4|A healthier fast food choice is to...|order a small size and add a side salad|supersize your meal|order fried food only|add extra cheese and sauce|Smaller portions help.
6.E|4|Substituting water for soda at a restaurant...|cuts sugar and calories|adds sugar|increases calories|raises salt|Water is healthier.
7|4|Aerobic activities like running and swimming strengthen your...|heart and lungs|toenails|hair|eyes|Aerobic exercise builds endurance.
7|4|Which activity builds muscle strength?|push-ups|napping|watching movies|reading|Resistance activities build muscles.
7|3|Stretching before and after activity can improve...|flexibility|eye color|height only|hearing|Stretching keeps muscles flexible.
8.A|3|A food goal such as "eat one vegetable at each dinner" is an example of...|a healthy food goal|a harmful habit|a recipe|an allergy|Specific goals are easier to follow.
8.A|4|Why is goal setting helpful for healthy eating?|it gives you a clear target|it removes all choices|it makes food disappear|it stops hunger|Goals focus effort.
8.B|4|A credible source for nutrition information is...|a registered dietitian or government website|a friend's rumor|a random advertisement|a social media post with no author|Credible sources are reliable.
8.B|4|Which is the most trustworthy source on healthy eating?|a doctor or nurse|a stranger online|a candy commercial|a made-up blog|Medical professionals are credible.
9.A|4|Regular physical activity helps prevent...|heart disease and obesity|growing taller|losing teeth|sleeping|Exercise lowers disease risk.
9.A|4|Physical activity helps lower the risk of...|type 2 diabetes|a sprained wrist from falling|colors|math mistakes|Exercise supports blood sugar control.
9.B|4|An unhealthy eating habit is...|skipping breakfast and eating only snacks|eating balanced meals|drinking water|eating slowly|Skipping meals is unhealthy.
9.B|4|If friends pressure you to eat only junk food, a refusal skill is to say...|"No thanks, I'm eating healthy."|"Sure, give me all of it."|nothing|"Okay."|A clear refusal works.
10|3|Which prevents injuries during sports?|wearing proper safety gear|skipping warm-ups|playing on wet floors|ignoring the rules|Gear protects you.
10|4|To stay safe near water, you should...|swim with a buddy and a lifeguard|swim alone|dive in shallow water|swim during storms|Supervision prevents drowning.
10|3|A good fire-safety step is to...|have a family escape plan|play with matches|block exits|ignore smoke alarms|Plans save lives.
11|4|Healthy relationships involve...|honesty, respect, and trust|control and secrecy|threats|jealousy|Healthy relationships are respectful.
11|4|A strategy for resolving conflict peacefully is to...|listen and look for a compromise|yell until you win|hit|spread rumors|Compromise resolves conflict.
11|4|Mediation is when a neutral person helps...|two people solve a disagreement|two people fight|one person win|nobody speak|Mediators help settle conflicts.
12.A|4|A strategy to avoid gangs is to...|choose friends who make positive choices|join to fit in|carry weapons|hang out in risky places|Good friends keep you safe.
12.A|4|Staying busy with sports and clubs helps you...|avoid violence and gangs|get in trouble|skip school|feel bored|Positive activities protect youth.
12.B|4|A characteristic of gang behavior is...|using intimidation and breaking laws|volunteering|studying together|playing fair|Gangs often use threats.
12.B|4|Gang members may pressure kids to...|break rules or commit crimes|clean parks|read books|learn music|Pressure leads to harm.
12.C|3|A way to promote safety at home is to...|lock doors and have a plan|leave doors open for strangers|hide emergency numbers|ignore smoke alarms|Locks and plans help.
12.C|3|A way to promote safety at school is to...|report unsafe behavior to an adult|ignore threats|bring weapons|spread rumors|Reporting protects others.
12.C|4|A way to promote safety in the community is to...|join neighborhood watch programs|litter|ignore broken lights|stay out late alone|Communities work together.
12.D|3|A personal safety plan should list...|trusted adults and safe places|your favorite show|a game score|your snack list|It guides you in danger.
12.D|4|Part of a safety plan is knowing what to do if you...|feel unsafe at home or away|win a game|get a haircut|buy shoes|Plans prepare for danger.
13.A|4|Which is an appropriate digital message?|a polite question to a classmate about homework|a rude joke about someone|a private picture|a rumor|Be respectful online.
13.A|4|Which is inappropriate online communication?|sending mean messages|thanking a friend|sharing a school event|asking an adult for help|Mean messages hurt.
13.B|4|Which information is safe to share with an online stranger?|none of your private information|your phone number|your home address|your school schedule|Keep personal info private.
13.B|4|Who is appropriate to share your passwords with?|a parent or guardian|any friend|a stranger|everyone|Passwords are private.
13.C|4|A consequence of inappropriate digital behavior can be...|losing device privileges or school discipline|winning a prize|more friends always|extra recess|Misuse has consequences.
13.C|4|Cyberbullying may lead to...|hurt feelings and school consequences|better grades|a new game|longer recess|Cyberbullying has consequences.
14.A|4|Cyberbullying is different from face-to-face bullying because it can...|happen anytime and spread quickly online|only happen at school|never be seen|happen once and vanish|Online posts spread fast.
14.A|4|A distinguishing characteristic of cyberbullying is...|using technology to hurt or embarrass someone|a friendly chat|a school lesson|a class project|It uses digital tools.
14.B|4|Bullying can harm the victim by causing...|anxiety and low self-esteem|stronger friendships|better grades|more energy|Bullying has emotional effects.
14.B|4|Bullying can also have a negative effect on the bully, such as...|trouble with school or the law|lots of trophies|better friends|more trust|Bullies face consequences.
14.C|3|If you see cyberbullying, you should...|tell a trusted adult and save the evidence|forward it|reply with insults|ignore it forever|Adults can stop it.
14.C|4|Why talk to parents about cyberbullying?|they can help you respond safely|they will ignore it|they cannot help|they will take your friends|Parents provide guidance.
14.D|4|Abuse can be physical, emotional, or...|sexual|musical|athletic|artistic|Abuse takes several forms.
14.D|4|If you suspect a friend is being abused, you should...|tell a trusted adult|keep it a secret|confront the abuser|ignore it|Adults can get help.
14.D|4|Neglect is when a child...|does not get basic needs like food or safety|gets too many hugs|gets homework|gets a pet|Neglect means basic needs unmet.
15.A|4|Why do some drugs require a prescription?|they can be harmful without a doctor's guidance|they taste bad|they are free|they are candy|Doctors control risky medicine.
15.A|4|A prescription is written by a...|doctor or other licensed provider|friend|stranger|neighbor|Providers prescribe medicine.
15.B|4|Over-the-counter medicine is...|available without a prescription|always dangerous|illegal|only for adults at night|OTC drugs are sold in stores.
15.B|4|Which is an example of an over-the-counter medicine?|a cough syrup from a pharmacy shelf|an antibiotic from a doctor|a vitamin from a cafeteria|a candy|OTC medicine is sold without a prescription.
16.A|4|A short-term harmful effect of alcohol is...|slowed reaction time|stronger muscles|clearer thinking|better balance|Alcohol impairs the brain.
16.A|4|A long-term harmful effect of tobacco is...|lung disease and cancer|better breathing|stronger bones|higher grades|Tobacco causes disease.
16.A|4|Using other drugs can damage the...|brain and body|nails only|shoes|backpack|Drugs harm health.
16.B|4|It is illegal for minors to...|buy or use tobacco and alcohol|ride bikes|read books|play outside|Underage use is unlawful.
16.B|4|A legal consequence of misusing drugs can be...|fines or being arrested|a certificate|a medal|a promotion|Drug misuse has legal penalties.
17|4|If someone has taken a harmful drug and cannot wake up, you should...|call 911 right away|wait until morning|give them food|shake them for an hour|Emergencies need immediate help.
17|4|Poison Control can be reached at...|1-800-222-1222|a restaurant|a library|a store|The national Poison Help line.
18.A|4|A positive peer influence would be a friend who...|encourages you to stay drug free|dares you to try it|offers a vape|teases you for saying no|Positive peers support healthy choices.
18.A|4|A negative peer influence can lead you to...|make unsafe choices|study harder|exercise more|eat healthier|Negative peers pressure you.
18.B|4|Ways to report unsafe situations involving drugs include telling...|a parent, teacher, or counselor|a stranger|nobody|a pet|Trusted adults can act.
18.B|4|Many schools and communities offer a hotline or tip line to...|report unsafe situations anonymously|order food|play music|sell items|Tip lines allow safe reporting.
19.A|4|An assertive refusal sounds like...|"No, I don't use drugs. I'm leaving."|"Maybe later."|"I guess so."|"Okay, just once."|Assertive refusals are firm.
19.A|4|The word "assertive" means to...|state your position firmly and respectfully|yell|stay silent|give in|Assertive is firm and respectful.
19.B|4|A healthy alternative to drug use is...|joining a sports team or club|hanging out in risky places|ignoring problems|staying isolated|Healthy activities are protective.
19.B|3|Which activity is a drug-free way to have fun?|playing music with friends|trying a vape|sneaking alcohol|breaking rules|Fun can be healthy.
20.A|4|During puberty, the body goes through...|physical and emotional changes|no changes|only hair color changes|only changes in sleep|Puberty brings growth and change.
20.A|4|Puberty usually begins...|between about ages 8 and 14|before birth|at age 40|at age 70|Puberty starts in late childhood or early adolescence.
20.A|4|During puberty, many people experience a growth spurt, which means they...|grow taller quickly|shrink|stay the same height|lose their teeth|Growth spurts are rapid growth.
20.B|4|The menstrual cycle is the monthly process in which the body...|prepares for a possible pregnancy|grows hair|digests food|builds bones|The cycle involves the uterus.
20.B|4|Menstruation is when the body sheds the...|lining of the uterus|stomach lining|bone marrow|skin cells|The lining leaves the body.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g4_health.jsonl'))
print("saved", len(B.out), "questions")

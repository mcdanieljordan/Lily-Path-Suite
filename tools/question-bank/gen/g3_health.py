#!/usr/bin/env python3
"""Grade 3 Health Education (TEKS 115.15.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('115.15.b.', 933, own='g3_health.jsonl')

load(B, """
1|3|Which body system fights germs and helps protect you from sickness?|immune system|skeletal system|digestive system|muscular system|The immune system defends the body.
1|3|Which organ in the nervous system controls thinking and body movement?|brain|stomach|kidney|bone|The brain directs the body.
1|3|In the digestive system, food travels from the mouth through the...|esophagus to the stomach|lungs to the heart|brain to the skin|ears to the nose|The esophagus carries food down.
1|3|Which body system removes waste from the blood and makes urine?|urinary system|respiratory system|skeletal system|muscular system|Kidneys filter blood.
2.A|3|Why is it helpful to talk with a parent or doctor before making a big health choice?|they can give accurate advice|they will decide for you always|they are never right|they dislike questions|Trusted adults share good information.
2.A|3|Seeking help with health decisions is smart because adults and professionals...|know reliable information|always guess|only tell jokes|never listen|Experts help you decide well.
2.B|3|Which source is a reliable way to learn about health?|a school nurse|a rumor from a stranger|a random pop-up ad|a made-up story|Nurses give accurate information.
2.B|3|Which method can help you find health information?|asking a doctor or using a trusted website|guessing|asking a stranger|flipping a coin|Reliable sources give accurate facts.
2.C|3|A benefit of choosing to wash your hands is that you...|are less likely to get sick|get taller|lose a tooth|grow wings|Good choices protect health.
2.C|3|Making good health decisions now can help you...|feel better and stay well|forget your homework|lose friends|get lost|Decisions have lasting benefits.
2.D|3|Taking personal responsibility for your health means you...|do your part to stay healthy|blame others for being sick|never brush your teeth|ignore doctors|Responsibility means acting for yourself.
2.D|3|Which shows personal responsibility for health?|packing a healthy lunch and drinking water|skipping every meal|staying up all night|never washing up|Healthy habits show responsibility.
2.E|3|Washing your hands for about twenty seconds helps remove...|germs|your fingerprints|your freckles|your nails|Washing removes germs.
2.E|3|Which disease can spread from person to person?|the flu|a broken arm|a bruise|sunburn|Flu is a contagious illness.
2.E|4|Vaccines work by helping your body...|build protection before you meet a germ|forget old illnesses|grow bigger muscles|see better|Vaccines train the immune system.
2.F|4|Asthma, diabetes, and epilepsy are diseases that are...|not spread from person to person|spread by sneezing|spread by sharing food|spread by touching|They are not contagious.
2.F|4|Which is true about asthma?|you cannot catch it from a friend|it spreads by coughing|it spreads by handshake|it spreads by food|Asthma is noncommunicable.
2.G|4|A vector is an animal, like a tick or mosquito, that...|carries germs from one host to another|makes music|grows plants|helps you sleep|Vectors carry disease.
2.G|4|To prevent mosquito bites, you can...|use insect repellent and wear long sleeves|stand near standing water|go outside with bare skin at dusk|collect old tires of water|Repellent and covering skin help.
2.G|4|After finding a tick on your skin, you should...|ask an adult to remove it safely|squash it|ignore it|burn it|Adults should remove ticks properly.
3.A|3|Which message communicates an emotion in a healthy way?|"I feel frustrated when my turn is skipped."|"You always cheat!"|"I hate everyone!"|"Nobody cares."|Calm I-statements share feelings.
3.A|3|Telling a friend "I need some space right now" is a healthy way to share...|a need|a joke|a trick|a lie|It communicates a need respectfully.
3.B|4|Before acting on a strong feeling, a good way to check your thoughts is to...|pause and ask whether they are true and helpful|act without thinking|blame others|ignore your body|Thought checking prevents poor choices.
3.B|3|Deep breathing and stretching are examples of...|calming practices|bad habits|tricks|punishments|Calming practices help self-management.
3.C|4|Brain maturation means your brain...|keeps changing and getting more skilled as you grow|stops working|shrinks every year|never learns|The brain develops through childhood.
3.C|4|Learning new skills, sleeping, and eating well help your brain...|develop|shrink|forget|stop|Healthy habits support brain growth.
3.D|3|A healthy influence from a friend would be...|encouraging you to study|daring you to break rules|teasing you|pressuring you to lie|Healthy influence supports good choices.
3.D|3|A harmful influence from others would be...|pressuring you to try something unsafe|helping you clean up|sharing a snack|inviting you to read|Pressure to do unsafe things is harmful.
3.E|3|A healthy friendship includes...|trust and respect|control and fear|jealousy and secrets|name-calling|Healthy friends trust and respect.
3.E|3|An unhealthy friendship may involve a friend who...|bosses you and makes you feel bad|shares fairly|apologizes sincerely|listens to you|Controlling behavior is unhealthy.
3.F|3|Respectful communication helps people...|understand each other|argue more|feel ignored|feel afraid|Respect improves understanding.
3.F|3|Which is a value of respectful communication?|it builds trust|it spreads rumors|it hurts feelings|it ends friendships|Respect builds relationships.
3.G|4|Two students see the same test. One feels excited, the other nervous. This shows that people...|can experience situations differently|always feel the same|have no feelings|never learn|Perspectives differ.
3.G|3|To understand how a classmate feels, you can...|listen to their point of view|decide without asking|laugh at them|ignore them|Listening builds empathy.
3.H|3|A good strategy to resolve a conflict is to...|listen, share your side, and find a compromise|call names|walk away without talking|tell everyone|Compromise resolves conflicts.
3.H|4|Using "I" statements during a disagreement helps you...|explain feelings without blaming|blame the other person|stop listening|walk away|I-statements reduce blame.
4.A|3|Self-esteem is how you...|feel about yourself|look in photos|run a race|spell words|Self-esteem is self-worth.
4.A|4|Self-esteem can grow when you...|practice a skill and improve|compare yourself to everyone|quit when it is hard|put yourself down|Success builds confidence.
4.B|3|Why should you ask a trusted adult for guidance when setting a goal?|they can help you plan realistic steps|they will do it for you|they will say no always|they dislike goals|Adults offer helpful advice.
4.B|3|A trusted adult can help you set a goal by...|helping you break it into small steps|choosing a goal for you every time|telling you to quit|ignoring you|Guidance helps plan.
5.A|4|A person with a long-term health condition such as asthma can manage it by...|following their care plan|ignoring symptoms|skipping medicine|hiding it|Care plans help manage conditions.
5.A|4|Checking blood sugar and following a care plan is a way to manage...|diabetes|a cold|a bruise|a haircut|Daily care helps manage diabetes.
5.B|3|You can support a classmate who learns differently by...|offering help and being patient|laughing|doing it for them without asking|ignoring them|Support means helping kindly.
5.B|3|Using clear directions and extra time can support someone who needs...|a different way to learn|a bigger desk|a louder voice|more homework|Accommodations help learners.
5.C|4|A positive outcome of healthy stress can be...|energy and focus|sickness|hurt feelings|boredom|Short-term stress can motivate.
5.C|4|Feeling a little nervous before a game can give you...|extra energy and focus|fear forever|a stomachache forever|sadness only|Positive stress sharpens focus.
5.D|3|A healthy behavior that reduces stress is...|exercising or listening to music|yelling at others|skipping sleep|skipping meals|Exercise and music relieve stress.
5.D|3|Spending time outdoors or journaling can help reduce...|stress|height|hunger|sleep|Healthy habits lower stress.
5.E|3|Accepting yourself means you...|are okay with who you are while still growing|only see your faults|wish to be someone else|hide|Self-acceptance is healthy.
5.E|3|Accepting others means you...|respect their differences|tease them|ignore them|change them|Acceptance respects differences.
6.A|3|Which nutrient helps build and repair muscle?|protein|water|fiber|salt|Protein supports muscle.
6.A|3|Whole grains, beans, and vegetables are good sources of...|fiber|candy|soda|oil only|Fiber aids digestion.
6.A|4|Foods like oranges and strawberries are known for providing...|vitamin C|only fat|only sugar|only protein|Citrus fruits are rich in vitamin C.
6.B|4|A balanced meal plan from the government guidelines fills half the plate with...|fruits and vegetables|candy|fried food|soda|MyPlate suggests half fruits and vegetables.
6.B|3|A balanced lunch could include...|a sandwich, fruit, and milk|only chips|only candy|only soda|Balance includes several groups.
6.C|4|On a nutrition label, "added sugars" tell you...|sugar put in during processing|sugar that comes naturally from fruit|the amount of salt|the amount of fiber|Added sugars are not natural.
6.C|4|Which food has natural sugar?|an apple|a sugar-filled soda|a candy bar|a frosted cookie|Fruit has natural sugar.
6.D|4|Which fat is considered healthier?|unsaturated fat from olive oil|saturated fat from butter|trans fat in fried food|fat from fast food|Unsaturated fats are healthier.
6.D|4|Foods high in saturated fat include...|fatty meats and butter|apples|carrots|water|These foods have saturated fat.
7|3|Moderate to vigorous activity for about an hour a day helps your...|heart and bones|toys|teacher|shoes|Activity strengthens the body.
7|3|Which pair of habits best supports lifelong health?|balanced eating and regular activity|skipping meals and sitting still|only sweets and sleep|screen time and soda|Balance supports health.
7|3|Why is it important to warm up before exercise?|it helps prevent injury|it makes you tired|it makes you slower|it stops your heart|Warm-ups prepare muscles.
8.A|3|Which is a common food allergen listed on packaging?|peanuts|carrots|rice|apples|Peanuts are a top allergen.
8.A|4|The word "Contains" on a label lists...|common allergens in the food|vitamins in the food|the price|the store|Labels warn about allergens.
8.B|3|Smoking can harm which body system?|respiratory system|skeletal system|muscular system|none|Smoke damages the lungs.
8.B|4|Eating a lot of sugary foods without brushing can harm your...|teeth|toenails|hair|eyes|Sugar causes cavities.
9|3|When biking, you should wear a helmet and...|follow traffic rules|ride in the dark without lights|ride on the wrong side|text while riding|Rules keep riders safe.
9|3|If you smell smoke at home, you should...|get out and tell an adult|hide under the bed|open every window and stay|ignore it|Leave and get help.
9|3|Which helps prevent a house fire?|not playing with matches|leaving candles unattended|overloading outlets|stacking papers on a heater|Matches are dangerous.
10|3|A healthy relationship is one where people...|treat each other with respect|control each other|call names|ignore feelings|Respect defines healthy relationships.
10|4|A good conflict-resolution step is to...|stay calm and listen|yell loudly|hit|spread rumors|Calm listening resolves conflict.
10|3|Which shows kindness during a disagreement?|taking turns talking|interrupting|insulting|ignoring|Taking turns shows respect.
11.A|3|One reason to avoid gangs is that they can...|lead to danger and trouble|give you real friends always|make you healthier|teach you school lessons|Gangs bring risk.
11.A|3|Staying away from violence and weapons helps keep you...|safe|lost|slow|tired|Avoiding violence protects people.
11.B|3|A safe school environment has...|rules and trusted adults|no rules|danger signs|broken stairs|Rules and adults keep school safe.
11.B|3|A safe community has...|well-lit streets and helpful neighbors|dark alleys|lots of trash|no rules|Safe places are cared for.
11.C|3|Mishandling a firearm can cause...|serious injury or death|a better grade|a snack|a nap|Firearms are deadly.
11.C|4|If you find a gun at a friend's house, you should...|leave and tell a trusted adult|play with it|take it|hide it|Do not touch.
11.D|3|A personal safety plan can include...|trusted adults and emergency numbers|a favorite game|a recipe|a spelling list|It tells you who to call.
11.D|4|A good personal safety plan includes...|a safe meeting place|a joke book|a secret|a snack|Meeting places help in emergencies.
12.A|3|Why is it important to be careful online?|strangers may not be who they say|everyone online is a friend|nothing online is real|nothing can go wrong|Online safety protects you.
12.A|3|A safe online habit is to...|keep passwords private|share your password with friends|post your address|click every ad|Passwords keep accounts safe.
12.B|3|Appropriate online communication includes...|kind words and polite messages|insults|rumors|private photos|Be kind online.
12.B|3|An appropriate way to message online is to...|use respectful language|use mean language|tease others|gossip|Respect applies online too.
12.C|4|Who is appropriate to communicate with online?|people you know and trust|any stranger|anyone who asks|anyone who messages you|Limit online contact to trusted people.
12.C|4|Which information is NOT appropriate to share online?|your home address|your favorite color|a joke|a school project title|Private info stays private.
12.D|4|A consequence of cyberbullying can be...|school discipline and hurt feelings|a reward|a new friend|a prize|Cyberbullying has consequences.
12.D|3|Sharing an embarrassing photo of a classmate online can cause...|harm to that person|good grades|a trophy|a snack|It hurts people and breaks rules.
13.A|3|If you see cyberbullying, a good response is to...|not join in and tell a trusted adult|forward it|laugh|comment meanly|Reporting helps.
13.A|3|One way to respond to bullying is to...|stay calm, walk away, and tell an adult|fight back|keep it a secret|join in|Calm action is safer.
13.B|3|Why ask a trusted adult for help with a safety problem?|they can help keep you safe|they will ignore it|they will tease|they will laugh|Adults help with safety.
13.B|3|If you feel unsafe, a good decision is to...|tell a trusted adult right away|wait and see|handle it alone|ignore it|Seek help early.
13.C|4|Abuse is when someone hurts another person's body or feelings on purpose, and neglect is when...|a person's basic needs are not met|a person plays too much|a person reads too much|a person naps|Neglect is failing to provide care.
13.C|4|If someone is being abused, they should tell...|a trusted adult|nobody|a stranger|only a pet|Telling an adult can get help.
14.A|3|Proper use of medicine means taking it...|as directed by a doctor or parent|whenever you want|more than needed|from friends|Follow directions.
14.A|4|Which is a misuse of medicine?|taking someone else's prescription|taking medicine as the label says|asking a doctor|getting medicine from a parent|Misuse can harm.
14.B|3|Smoking and vaping can cause long-term damage to the...|lungs|toes|ears|knees|Lungs suffer harm.
14.B|4|Inhalants such as spray paint fumes can damage the...|brain and organs|toenails|hair color|height|Inhalants are toxic.
15|3|A short-term effect of alcohol is trouble with...|balance and thinking|growing taller|reading only|painting|Alcohol impairs the body.
15|4|A long-term effect of tobacco use is a higher chance of...|heart and lung disease|growing taller|better running|better sleep always|Tobacco raises disease risk.
16|3|If a person takes too much of a harmful drug, you should call...|911|nobody|a friend only|a pet|911 sends emergency help.
16|3|Poison Control can help if someone...|swallowed something harmful|lost a toy|got a haircut|is hungry|Poison Control gives guidance.
17.A|3|A friend can influence your choice about drugs by...|encouraging you to say no or pressuring you to try|knowing your homework|sharing a pencil|sitting next to you|Friends can push either way.
17.A|4|Having friends who avoid drugs makes it easier to...|make healthy choices|forget your name|break rules|stay up late|Positive peers help.
17.B|4|Reporting is telling an adult when someone could be hurt, while tattling is telling...|only to get someone in trouble|because someone is hurt|about an emergency|about a fire|Reporting protects; tattling is petty.
17.B|4|Why report a friend who is in danger from drugs?|an adult can help keep them safe|to get them in trouble|to be mean|to win|Reporting saves lives.
18|3|A refusal skill for an unsafe offer is to say no, give a reason, and...|leave the situation|stay and watch|try it a little|laugh|Leaving is part of refusing.
18|3|Which is a good way to refuse a drug offer?|"No thanks. I don't use that."|"Maybe next time."|"Sure, why not?"|"I'll think about it."|A clear no works best.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g3_health.jsonl'))
print("saved", len(B.out), "questions")

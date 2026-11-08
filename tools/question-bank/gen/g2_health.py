#!/usr/bin/env python3
"""Grade 2 Health Education (TEKS 115.14.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('115.14.b.', 932, own='g2_health.jsonl')

load(B, """
1|2|Which organ is part of the respiratory system and helps you breathe?|lungs|stomach|heart|brain|The lungs move air in and out.
1|3|The brain and nerves make up which body system?|nervous system|digestive system|skeletal system|muscular system|The nervous system sends messages.
1|3|Which two body systems work together when you run?|muscular and skeletal|digestive and nervous only|hair and nails|none of them|Muscles move bones.
1|3|When you exercise, your heart beats faster to deliver more...|blood and oxygen|candy|noise|light|The circulatory system carries oxygen.
2.A|2|A regular checkup with a doctor helps you...|stay healthy and catch problems early|become sick|skip school forever|avoid brushing|Checkups prevent illness.
2.A|3|Seeing a dentist twice a year helps prevent...|cavities|sunburn|homework|hiccups|Dental visits protect teeth.
2.B|2|If your throat hurts and you feel hot, you should tell...|an adult|nobody|a toy|a stranger|Adults can help you feel better.
2.B|3|When you do not feel well, a good action is to...|rest and drink water|run a race|eat only candy|ignore it|Rest helps recovery.
2.C|2|Good hygiene includes...|washing hands and brushing teeth|skipping baths|sharing towels|never washing|Hygiene prevents illness.
2.C|3|Why should you not share your toothbrush?|germs can spread|it wears out|it is too big|it is too pretty|Sharing spreads germs.
2.D|3|Germs can spread through the air when someone...|sneezes|reads silently|sleeps|draws|Droplets carry germs.
2.D|3|Which action helps prevent spreading germs at school?|washing hands before lunch|sharing water bottles|licking pencils|coughing on the desk|Handwashing removes germs.
2.E|3|Asthma is an illness that makes it hard to...|breathe|see|hear|taste|Asthma affects airways.
2.E|4|A person with diabetes must watch their...|blood sugar|shoe size|height|eye color|Diabetes affects blood sugar.
2.E|4|Epilepsy is a condition that can cause...|seizures|a cold|a broken bone|sunburn|Epilepsy involves the brain.
2.F|3|After a tick bite, you should tell an adult if you have...|a fever or a rash|a new backpack|a smile|a loose tooth|Illness signs after bites need care.
2.F|4|A mosquito bite can sometimes cause illness with symptoms like...|fever and body aches|a loud laugh|a new haircut|a good grade|Insect-borne illness causes fever.
3.A|2|A healthy way to say what you need is to...|use words calmly|scream|slam doors|cry without telling|Words communicate needs.
3.A|3|Which sentence shares a feeling in a healthy way?|"I feel sad because I lost my toy."|"You are dumb."|"I'm never talking again."|"Go away."|I-statements are healthy.
3.B|2|Counting backward from five can help you...|calm down|get louder|forget your name|run faster|Counting calms the body.
3.B|3|A self-management strategy is to...|take a break and breathe|yell at a friend|break something|ignore everyone|Breaks help you reset.
3.C|3|Your thoughts can change your...|emotions|eye color|shoe size|height|Thoughts and emotions are linked.
3.C|3|If you think "I can't do this," you might feel...|discouraged|excited|proud|calm|Negative thoughts cause negative feelings.
3.D|3|Peer influence means a person your age can...|change how you think or act|grow your hair|make you taller|give you wings|Peers can affect choices.
3.D|4|A positive peer influence would be a friend who...|encourages you to follow rules|dares you to break rules|teases you|ignores you|Positive influence supports good choices.
3.E|2|One quality of a good friend is...|kindness|selfishness|rudeness|cheating|Good friends are kind.
3.E|3|A good friend will...|listen and keep your trust|spread your secrets|ignore you when you are sad|tease you|Good friends are trustworthy.
3.F|3|A respectful way to talk to a teacher is to...|raise your hand and wait|shout answers|talk over them|roll your eyes|Respect shows in how you speak.
3.F|3|When a family member is speaking, it is respectful to...|listen without interrupting|walk away|laugh at them|yell|Listening shows respect.
3.G|3|A friend crosses their arms and looks away. Their nonverbal cue may mean they feel...|upset|excited|silly|hungry|Body language gives clues.
3.G|3|A classmate's voice shakes and they say "I'm fine." Their verbal and nonverbal cues may not match, so you could...|ask kindly if they are okay|laugh at them|ignore them|tell everyone|Check in with care.
3.H|3|To repair a broken friendship, you can...|apologize and listen|ignore the person forever|spread rumors|break their things|Apologies repair relationships.
3.H|3|To prevent a friendship from breaking, you should...|talk about problems early|keep secrets that hurt|argue loudly|ignore your friend|Early talking prevents big fights.
4.A|3|One way to be kind to yourself is to...|rest when you are tired|put yourself down|skip meals|call yourself names|Self-kindness includes rest.
4.A|2|One way to be kind to others is to...|share and help|tease|push|brag|Kindness helps people.
4.B|3|Personal growth means...|learning and improving over time|staying exactly the same|giving up|forgetting|Growth is getting better.
4.B|3|Which is an area for personal growth?|learning to read more fluently|already knowing everything|never trying|always winning|Growth areas are things to improve.
4.C|3|The first step of setting a goal is to...|decide what you want to do|finish it|give up|celebrate|You must choose a goal first.
4.C|4|Putting these steps in order, which comes after making a plan?|work on the plan|forget the goal|quit|celebrate before starting|After planning you take action.
5.A|3|One strategy for a classmate who needs extra time to learn is to...|be patient and kind|rush them|laugh|ignore them|Patience helps learners.
5.A|3|If you learn best by seeing pictures, a helpful strategy is to...|use drawings and charts|close your eyes|skip class|cover the page|Visual learners use pictures.
5.B|3|A positive stressor might be...|preparing for a spelling bee|losing your pet|a loud fight|getting hurt|Challenges can be positive.
5.B|4|Too much negative stress can make it harder to...|learn and focus|breathe air|have a name|grow tall|Stress affects learning.
6.A|3|Which is a nutrient your body needs to build muscles?|protein|candy|soda|chips|Protein builds and repairs muscle.
6.A|3|Vitamins and minerals help your body...|work properly|shrink|forget|hide|Micronutrients support health.
6.A|4|Carbohydrates give your body...|energy|bones|a voice|hair color|Carbs are fuel.
6.B|3|A healthy portion of cheese is about the size of...|two dice|a soccer ball|a lunchbox|a book|Familiar objects show portions.
6.B|3|A healthy serving of cooked pasta is about the size of...|a tennis ball|a basketball|a suitcase|a pillow|A tennis ball is about one-half cup.
6.C|3|Which is a healthier choice from the grain group?|whole wheat bread|a frosted pastry|a doughnut|a sugary cereal|Whole grains are healthier.
6.C|3|Which is a healthier fruit choice?|fresh strawberries|fruit snacks with added sugar|sugary jelly|fruit candy|Whole fruit is healthier.
6.D|2|Which drink is the best choice for staying hydrated?|water|soda|candy drink|sugary punch|Water is best for hydration.
6.D|3|Milk gives your body...|calcium for strong bones|dirt|salt only|oil|Milk is rich in calcium.
7|3|How many minutes of physical activity do kids need most days?|60 minutes|5 minutes|15 hours|0 minutes|Kids need about an hour of activity.
7|3|Which choice is a healthy habit?|eating a balanced meal and moving every day|eating only dessert|staying inside all day|skipping sleep|Balance supports health.
7|3|Which activity would count toward your daily 60 minutes?|playing tag|watching videos|sitting in a chair|reading in bed|Tag gets you moving.
8.A|3|Hives, itchy skin, and trouble breathing after eating can be signs of...|a food allergy|a haircut|a good mood|bedtime|These are allergy symptoms.
8.A|3|If a classmate has a bad reaction after eating, you should...|tell a teacher right away|laugh|give them more food|wait until tomorrow|Allergic reactions are emergencies.
8.B|3|Healthy habits learned now can last...|a lifetime|one day|one minute|a second|Habits can last a lifetime.
8.B|3|A benefit of regular physical activity is...|a stronger heart|a bigger backpack|louder shoes|a longer nap|Activity strengthens the heart.
9|3|Which action helps prevent an injury at the playground?|using equipment the right way|jumping from the top of slides|pushing others|playing on broken equipment|Proper use prevents falls.
9|3|Wearing a life jacket when boating helps...|keep you afloat|make you faster|keep you dry|keep you warm|Life jackets save lives.
9|3|Before crossing the street you should...|stop and look both ways|close your eyes|run|ignore cars|Looking prevents crashes.
10.A|3|Someone touches you in a way that feels wrong. A good refusal is to say "Stop!" and...|go tell a trusted adult|giggle|stay quiet|go closer|Refuse and report.
10.A|3|A strong voice and a clear "no" are examples of...|refusal skills|dance steps|math tools|art supplies|Refusal skills protect you.
10.B|3|Why should you tell a trusted adult when someone crosses a personal boundary?|so they can help protect you|so you get in trouble|so you lose a friend|so you hide it|Adults protect children.
10.B|3|Private parts of your body are covered by...|your swimsuit|your hat|your gloves|your scarf|Swimsuit areas are private.
11.A|3|Which is an unsafe situation with a stranger?|a stranger asks you to help find a puppy|you play at the playground with your parent|a teacher says hello|your grandma waves|Strangers asking for help can be a trick.
11.A|3|If a stranger offers you candy and asks you to come with them, you should...|run away and tell a trusted adult|take the candy|follow them|say yes|Never go with strangers.
11.B|3|If you find an unsupervised weapon, you should...|stay away and tell a trusted adult|pick it up|show friends|hide it|Weapons are dangerous.
11.B|3|Reporting an unsupervised weapon helps...|keep people safe|get you a prize|make a game|start a fight|Reporting prevents harm.
11.C|3|Mishandling a gun can cause...|serious injury or death|a funny joke|a better grade|a snack|Guns can kill.
11.C|4|Which is the safest thing to do with a gun you find?|do not touch it and tell an adult|point it as a game|unload it yourself|take it home|Do not touch.
11.D|3|A trusted adult outside your immediate family could be...|a neighbor or coach you know well|a stranger|an online friend|someone who texts you secrets|Choose adults you know in real life.
11.D|3|Having two trusted adults and their phone numbers is part of a...|personal safety plan|spelling test|recipe|science fair|It tells you who to call.
12.A|3|You get a message online from someone you do not know asking for your address. You should...|not answer and tell a trusted adult|send it|reply with your school|share your password|Unsafe requests should be reported.
12.A|3|Which is an unsafe online request?|a stranger asks you to meet in person|a teacher assigns a class game|a parent shares a photo|a friend sends a smiley|Meeting strangers is unsafe.
12.B|3|Why should you ask an adult for help with an online problem?|they can help you stay safe|they will take your device forever|they will ignore you|they cannot read|Adults guide safe choices.
12.C|3|One consequence of cyberbullying is that the victim may feel...|hurt and lonely|proud|excited|healthy|Cyberbullying harms feelings.
12.C|4|Posting an unkind comment about a classmate online could lead to...|trouble at school or home|a prize|free time|a new toy|Online actions have consequences.
13.A|3|A consequence for a bully may be...|losing privileges|winning a trophy|extra recess|a new friend|Bullying has consequences.
13.A|3|The impact of bullying on the victim can include...|feeling afraid and sad|always laughing|growing taller|becoming faster|Bullying hurts.
13.B|4|Reporting is when you tell an adult about something that...|is unsafe or harmful|is just annoying|is a small mistake|is a joke|Reporting keeps people safe.
13.B|4|Tattling is when you tell on someone...|just to get them in trouble|because someone is in danger|because someone is hurt|because a rule is broken and harms others|Tattling is for getting someone in trouble.
13.C|3|When bullying happens, a trusted adult can...|help stop it|ignore it|join in|laugh|Adults have authority to help.
13.C|3|Why is it good to tell a parent about bullying?|they can help solve it|they will punish you|they will ignore it|they will tease you|Parents can act.
14.A|3|The purpose of prescription medicine is to...|treat a specific illness as ordered by a doctor|give you candy|make you taller|help you sleep in class|Prescriptions treat illness.
14.A|3|An over-the-counter medicine is often used to treat...|a mild headache or cough|a broken leg|a toothache only|nothing|OTC medicines treat mild issues.
14.B|4|Alcohol harms a young person's...|brain and body|favorite shoes|eyes only|fingernails only|Alcohol harms growing bodies.
14.B|3|Vaping is harmful because it can damage the...|lungs|elbows|hair|toenails|Vaping harms lungs.
14.B|3|Sniffing glue or paint fumes is harmful because it can...|damage the brain|help you think|make you stronger|taste good|Inhalants harm the brain.
15|3|If a friend takes something harmful, you should...|get a trusted adult right away|keep it a secret|wait until tomorrow|take some too|Fast help saves lives.
15|3|Who can help in an emergency involving a harmful substance?|911 and Poison Control|nobody|a stranger on the street|a pet|Call for help.
16.A|3|Which friend request is unsafe?|"Try this vape with me."|"Want to play tag?"|"Let's share crayons."|"Come read with me."|Offers of drugs are unsafe.
16.A|3|A friend dares you to take a pill you do not know. This is an unsafe request about...|drugs|games|math|colors|Unknown pills can harm.
16.B|2|A trusted adult could be a parent, a teacher, or a...|police officer|stranger|pretend friend|toy|Law enforcement officers can help.
16.B|3|You can ask a trusted adult for help when you feel...|pressured to try something unsafe|happy|full|sleepy|Adults help with pressure.
17|3|If someone offers you a drug, a refusal skill is to say no and...|walk away|stay and think|take it|laugh|Leave the situation.
17|3|A strong refusal might sound like...|"No, I won't do that."|"Maybe."|"Okay, just once."|"I guess."|A firm statement works best.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g2_health.jsonl'))
print("saved", len(B.out), "questions")

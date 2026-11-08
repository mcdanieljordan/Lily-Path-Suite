#!/usr/bin/env python3
"""Grade 1 Health Education (TEKS 115.13.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('115.13.b.', 931, own='g1_health.jsonl')

load(B, """
1|2|Which body system includes the stomach and helps you digest food?|digestive system|skeletal system|nervous system|respiratory system|The digestive system breaks down food.
1|3|Which body system uses bones to support your body?|skeletal system|digestive system|circulatory system|respiratory system|Bones form the skeleton.
1|3|Your muscles and bones work together to help you...|move|digest|see colors|hear sounds|Muscles pull bones to make movement.
1|2|The heart and blood vessels belong to which system?|circulatory system|digestive system|skeletal system|muscular system|They move blood through the body.
2.A|2|Which health care professional checks your teeth?|a dentist|a mail carrier|a pilot|a baker|Dentists care for teeth.
2.A|2|Which health care professional gives checkups and shots?|a doctor or nurse|a firefighter|a chef|a bus driver|Doctors and nurses give checkups.
2.A|3|An eye doctor helps you with your...|vision|hearing|stomach|toes|Eye doctors check eyesight.
2.B|2|Taking a bath or shower helps your body stay...|clean|dirty|sticky|muddy|Bathing removes dirt and germs.
2.B|2|How often should you brush your teeth to keep them healthy?|morning and night|once a month|never|only on weekends|Regular brushing prevents cavities.
2.B|3|Flossing helps clean...|between your teeth|your elbows|your shoes|your hair|Floss reaches where a brush cannot.
2.C|2|Which action helps stop germs from spreading to others?|staying home when you are sick|sharing cups with friends|sneezing into the air|touching your face all day|Staying home keeps germs from spreading.
2.C|3|Why do doctors recommend getting immunizations?|they help your body fight certain diseases|they make you taller|they make you sleep|they teach you math|Immunizations build protection against illness.
2.C|2|Using a tissue when you sneeze helps...|stop germs from spreading|make a mess|save money|make germs grow|Tissues catch germs.
2.D|3|Ticks and mosquitos are bugs that can bite and may spread...|illness|music|paint|toys|Some bites can cause sickness.
2.D|3|Which clothing helps protect you from tick bites in tall grass?|long pants and socks|a swimsuit|sandals only|no clothes|Covering your skin lowers bites.
2.D|2|Head lice are often spread when people...|share hats or hairbrushes|share a story|wave|sing|Lice crawl from one head to another.
3.A|2|Excited, scared, and proud are examples of...|emotions|animals|numbers|shapes|Emotions are feelings.
3.A|2|Your stomach feels tight before you go on stage. You may be feeling...|nervous|asleep|cold|hungry for pizza|Nervousness can feel like tight muscles.
3.B|3|When you are very angry, it can be hard to...|think clearly|breathe air|blink|grow|Strong emotions interrupt thinking.
3.B|3|A strong emotion can make it harder to...|make good choices|see colors|hear music|sleep always|Emotions can interrupt self-management.
3.C|2|Which is a calming strategy?|taking slow breaths|slamming a door|yelling louder|kicking a chair|Slow breathing relaxes the body.
3.C|3|Drawing quietly or listening to calm music can help you...|calm down|get angrier|forget how to read|run faster|Quiet activities calm the mind.
3.D|3|Which shows a family working together to build a healthy relationship?|they talk and listen to each other|they ignore each other|they keep secrets that hurt|they yell all day|Healthy relationships need good communication.
3.D|2|A peer is someone who is...|about your age|a pet|your teacher|a stranger on TV|Peers are people your age.
3.E|2|Which action helps keep a friendship strong?|being fair and sharing|being rude|never listening|bragging all the time|Fairness builds trust.
3.E|3|If you hurt a friend's feelings by accident, you can...|say sorry|ignore them|laugh at them|tell a lie|An apology repairs friendships.
3.F|2|Which is a respectful way to talk?|use a calm voice and say please|yell and point|roll your eyes|say mean names|Calm words show respect.
3.F|3|Looking at the speaker shows respect without using any...|words|ears|shoes|paper|Eye contact is nonverbal communication.
3.G|2|A friend is crying at recess. They are probably feeling...|sad|proud|excited|silly|Tears often show sadness.
3.G|3|Someone with clenched fists and a frown may be feeling...|angry|calm|sleepy|joyful|Body language shows emotion.
3.H|3|Two friends both want the swing. A fair way to solve it is to...|take turns|fight|tattle on everyone|break the swing|Turn taking solves conflicts.
3.H|3|When friends disagree, a good first step is to...|talk it out calmly|walk away mad|spread rumors|push|Calm talking solves problems.
4.A|3|Being kind to yourself means you...|talk to yourself with encouragement|call yourself names|give up right away|never rest|Kind self-talk builds confidence.
4.A|3|An area for growth is something you...|want to get better at|already do perfectly|never think about|hide from everyone|Growth areas are skills to improve.
4.B|2|Why is setting a goal helpful?|it gives you something to work toward|it makes homework disappear|it stops time|it gives free candy|Goals guide effort.
4.B|3|Finishing a task you start shows...|responsibility|silliness|laziness|worry|Task completion builds responsibility.
5.A|3|A classmate learns in a different way than you. You should treat them with...|respect|teasing|laughter|anger|Everyone deserves dignity.
5.A|2|Learning needs can be different, but everyone should be treated with...|dignity|rudeness|fear|noise|Dignity means respect.
5.B|3|Which situation can cause positive stress?|getting ready for your first piano show|losing your favorite toy|getting lost|seeing a bad storm|Positive stress comes from exciting challenges.
5.B|3|Winning a game with your team can create a feeling of...|joy|grief|fear|boredom|Success brings positive emotion.
5.C|3|Missing someone who has died or moved far away is called...|grief|joy|pride|hunger|Grief is sadness after a loss.
5.C|3|A sign of negative stress is...|a stomachache from worry|a big smile|a fast race|a loud laugh|Worry can cause body signals.
6.A|3|Fruits and vegetables give your body...|vitamins and minerals|toys|batteries|paint|Vitamins and minerals keep you healthy.
6.A|3|Dairy foods such as milk give your body...|calcium for strong bones|plastic|sugar only|noise|Calcium builds bones.
6.B|3|A serving of meat is about the size of...|a deck of cards|a refrigerator|a basketball|a pillow|Familiar objects help estimate portions.
6.B|3|A cookie portion is about the size of...|a golf ball|a watermelon|a shoebox|a tire|Portion comparisons help control sweets.
6.C|2|An apple belongs to which food group?|fruit|dairy|protein|grain|Apples are fruits.
6.C|2|Which food belongs to the grain group?|bread|carrot|milk|egg|Bread comes from grain.
6.C|3|Which pair belongs to the vegetable group?|broccoli and spinach|cheese and yogurt|chicken and fish|rice and pasta|Broccoli and spinach are vegetables.
6.D|3|Added sugar makes a drink less...|healthy|wet|cold|colorful|Too much sugar is unhealthy.
6.D|3|Which drink has lots of added sugar?|soda|water|plain milk|sparkling water with no sugar|Soda has added sweeteners.
7|3|Moving your body for at least 60 minutes a day helps kids...|stay healthy and strong|forget how to rest|get weaker|grow smaller|Daily activity supports health.
7|3|Which activity counts as physical activity?|riding a bike|watching TV|napping|sitting still|Biking moves your body.
7|3|Eating nutritious food and being active together help your...|whole body|toys|homework|backpack|Nutrition and activity both build health.
8.A|2|Peanut allergies, egg allergies, and milk allergies are all examples of...|food allergies|fun games|bike rules|sleep habits|Common allergens cause reactions.
8.A|3|You should not give food to a classmate with allergies unless...|a trusted adult says it is safe|they ask loudly|it looks tasty|you are hungry|Adults check ingredients.
8.B|2|Getting enough sleep helps your body and mind to...|rest and grow|stay awake all night|shrink|hide|Sleep restores energy.
8.B|3|Eating breakfast helps you...|have energy for school|forget lessons|feel sleepier|lose your voice|Breakfast fuels learning.
9.A|3|Which is a way to keep yourself safe near a street?|hold a grown-up's hand|run ahead|chase a ball into the road|play in traffic|Adults help you cross safely.
9.A|3|If a stranger offers you a ride, you should...|say no and tell a trusted adult|get in|go with them|keep it a secret|Never go with strangers.
9.B|2|What is the purpose of a helmet when you ride a scooter?|protect your head|make you faster|look silly|keep you cool|Helmets protect from head injuries.
9.B|3|A car seat or booster seat is used to...|keep children safe in a car|make the car quiet|store snacks|cool the car|Child seats protect kids in crashes.
10.A|3|Someone you do not know touches your arm and you feel uncomfortable. You can say...|"Stop! Don't touch me."|"Sure."|nothing|"Do it again."|Refusal skills protect personal space.
10.A|3|A strong refusal includes a loud voice and...|walking away to a safe adult|giggling|hiding forever|keeping it secret|Leave and tell someone you trust.
10.B|2|Privacy means...|keeping some things to yourself|sharing every detail with strangers|being loud|forgetting|Privacy protects personal things.
10.B|3|Personal boundaries tell others how...|close they can come or touch you|fast to run|loud to sing|tall to be|Boundaries are your limits.
10.C|2|Why should you memorize a trusted adult's phone number?|so you can call for help|so you can sell it|so you can forget it|so you can lose it|A phone number helps in an emergency.
10.C|3|If you are lost, it helps to know your...|parent's phone number|favorite cartoon|shoe size|lunch menu|Phone numbers let you reach family.
11.A|2|Which place is safest to play?|a fenced backyard with an adult nearby|a busy parking lot|a river bank alone|a roof|Safe places are watched and secure.
11.A|3|An unsafe environment might have...|broken glass or no adults nearby|a grown-up watching|soft grass and a fence|a clear path|Broken glass is hazardous.
11.B|3|If you see a gun, you should...|stay away and tell a trusted adult|pick it up|show friends|point it|Never touch a weapon.
11.B|3|Telling an adult about a dangerous situation helps...|keep people safe|get people in trouble for no reason|make a mess|lose a friend|Reporting prevents harm.
12|3|Being a good digital citizen means you...|are kind online and ask a grown-up before sharing|post private info|share passwords with friends|tease online|Respect and safety matter online.
12|3|Which should you never share with someone you meet online?|your home address|your favorite color|a joke|a drawing|Never share private info with strangers.
12|3|Before downloading a game, you should...|ask a trusted adult|click everything|share your password|ignore warnings|Adults check safety.
13.A|3|One result of bullying for the target is feeling...|sad or afraid|always happy|excited|proud|Bullying hurts feelings.
13.A|3|A bully may face consequences such as...|losing privileges at school|winning a prize|getting free toys|getting more friends|Bullying has consequences.
13.B|3|One way to discourage bullying is to...|stand with the person being bullied|laugh along|stay silent|spread the story|Support discourages bullies.
13.B|2|If you see bullying, you can...|get a trusted adult|record it for fun|join in|ignore it|Adults can stop bullying.
13.C|3|Teasing becomes bullying when it is...|meant to hurt and happens again and again|a one-time friendly joke|a hug|a game with fair rules|Bullying is repeated and hurtful.
13.C|3|Which is playing around rather than bullying?|friends laughing together during a game|someone pushing another on purpose every day|calling someone names to hurt them|leaving a classmate out on purpose|Playing around is fun for everyone.
13.D|3|If someone makes you feel unsafe, a good choice is to...|tell a parent or trusted adult|keep it a secret|try to fix it alone|ignore your feelings|Trusted adults can help.
13.D|3|A trusted adult at school could be...|a teacher or counselor|a stranger|a pet|a character on TV|School staff can help.
14.A|3|A medicine you can buy without a doctor's note is called...|over-the-counter|prescription|pretend|poison|Over-the-counter drugs do not need a prescription.
14.A|3|A prescription drug is medicine that...|a doctor orders for a specific person|anyone can take|is candy|is food|Prescription medicine is ordered by a doctor.
14.B|3|Tobacco use harms the...|lungs and heart|nails|hair color|shoe size|Tobacco harms organs.
14.B|3|Vaping and cigarettes both contain a harmful drug called...|nicotine|vitamin C|calcium|iron|Nicotine is addictive.
14.B|3|Household cleaners are dangerous if they are...|swallowed|stored on a high shelf|kept in the original bottle|used by an adult safely|Swallowing cleaners can poison.
15|3|If someone swallowed something harmful, you should tell a grown-up and call...|Poison Control or 911|a friend|the dog|nobody|Poison Control gives emergency help.
15|3|Calling for help when someone has taken a harmful substance is called getting...|emergency help|a snack|a toy|a haircut|Fast help saves lives.
16|3|A protective factor that helps kids stay away from drugs is...|a caring family|peer pressure to try drugs|boredom|a stranger offering something|Support protects kids.
16|3|A risk factor for drug use is...|friends who pressure you|a supportive coach|a happy home|healthy hobbies|Pressure is a risk.
17|3|If someone offers you a drug, a good refusal is...|"No thanks, I'm leaving."|"Okay."|"Maybe later."|"Let me try."|Clear refusals protect you.
17|3|After you refuse an unsafe offer, you should...|tell a trusted adult|keep it secret|go back|accept it|Reporting keeps you safe.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g1_health.jsonl'))
print("saved", len(B.out), "questions")

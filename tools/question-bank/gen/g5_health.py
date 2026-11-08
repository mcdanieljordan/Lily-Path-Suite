#!/usr/bin/env python3
"""Grade 5 Health Education (TEKS 115.17.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('115.17.b.', 935, own='g5_health.jsonl')

load(B, """
1|3|Which body system breaks down food into nutrients the body can absorb?|digestive system|nervous system|skeletal system|endocrine system|Digestion turns food into usable nutrients.
1|4|Which pair of systems work together to bring oxygen into the body and carry it to cells?|respiratory and circulatory|skeletal and muscular|digestive and urinary|integumentary and endocrine|Lungs breathe in oxygen and blood delivers it.
1|4|Which structure in the nervous system carries messages between the brain and the body?|spinal cord and nerves|stomach|kidneys|liver|The spinal cord and nerves carry signals.
1|4|The immune system helps the body by...|fighting germs that cause illness|digesting food|moving bones|making hormones only|White blood cells attack germs.
2.A|3|A good way to care for a cold at home is to...|rest and drink plenty of fluids|go to a crowded party|skip all fluids|share cups|Rest and fluids help recovery.
2.A|4|To treat a minor skin infection such as a small scrape, you should...|clean it and cover it with a bandage|pick at it|leave it dirty|share towels|Clean wounds heal better.
2.B|4|A health myth is...|a false belief that people repeat as if it were true|a fact proven by science|a doctor's advice|a lab result|Myths are not supported by evidence.
2.B|4|To check whether a health claim is a fact, you should...|look for evidence from credible sources|trust the loudest voice|believe the first ad you see|ask no one|Evidence separates fact from myth.
2.C|4|Which decision-making skill helps a family stay healthy?|weighing choices and their results before deciding|acting without thinking|always guessing|copying friends|Careful decisions protect health.
2.C|4|Choosing to have your family get a flu shot is an example of a decision that promotes...|community health|only fashion|only wealth|only sleep|Vaccination protects the whole community.
2.D|4|A benefit of health maintenance for a household is...|fewer sick days and lower health problems|more homework|louder noise|colder rooms|Prevention keeps families well.
2.D|4|Regular checkups and keeping medicines safely stored are part of...|health maintenance|a game|a sport|a hobby|Maintenance prevents problems.
2.E|4|Covering coughs and washing hands help prevent the spread of...|communicable illnesses|broken bones|sprains|bruises|Hygiene limits germ transmission.
2.E|4|Why does hand sanitizer help when soap and water are not available?|it kills many germs on the skin|it makes germs grow|it adds germs|it dries pencils|Sanitizers reduce germs.
2.F|4|If a tick has bitten you, the safest treatment step is to...|have an adult remove it with tweezers and watch for symptoms|crush it with your fingers|burn it with a match|ignore it|Proper removal reduces illness risk.
2.F|4|Treatment for a mosquito-borne illness is decided by...|a doctor who diagnoses the illness|a friend|an online stranger|a coin flip|Doctors choose the proper treatment.
3.A|4|Feeling jealous after a friend wins a game could lead someone to...|say unkind things unless they manage the feeling|always feel joy|become taller|win more games automatically|Emotions influence behavior.
3.A|4|Thinking "I can handle this" before a test can lead you to...|stay calm and try your best|panic|forget everything|give up|Positive thoughts support calm behavior.
3.B|3|A strategy for self-management when you feel angry is...|taking a time-out and breathing slowly|slamming doors|teasing|giving up|Pausing prevents rash actions.
3.B|4|Progressive muscle relaxation is a calming strategy where you...|tighten and release muscle groups|run a race|shout|ignore your body|It reduces tension.
3.C|4|Maintaining a healthy relationship requires...|honest communication and mutual respect|secrecy and control|ignoring one another|jealousy|Healthy relationships rely on respect.
3.C|4|To resist negative peer influence, you can...|choose friends who respect your values|go along to fit in|keep quiet|pretend you agree|Supportive friends help.
3.D|4|Respectfully communicating disagreement means...|explaining your view calmly and listening to theirs|name-calling|interrupting|walking out and slamming doors|Respect keeps the conversation open.
3.D|4|Identifying someone else's perspective means...|trying to see the situation from their point of view|insisting you are right|ignoring them|guessing without listening|Perspective-taking builds understanding.
3.E|4|Sympathy means...|feeling sorry for someone's situation|feeling exactly what they feel|ignoring someone|laughing|Sympathy is feeling for someone.
3.E|4|Empathy means...|understanding and sharing another person's feelings|only feeling sorry from far away|ignoring them|being jealous|Empathy is feeling with someone.
3.F|4|One way to promote positive interactions during conflict is to...|use calm words and look for a fair solution|insult|shout|blame everyone|Calm problem-solving helps.
3.F|4|A peer mediator can help classmates...|reach an agreement|argue louder|ignore each other|avoid class|Mediators guide agreements.
4.A|4|A way to build a friend's self-esteem is to...|notice and praise their real strengths|compare them to others|point out their mistakes|ignore them|Genuine praise builds confidence.
4.A|4|A strategy to build your own self-esteem is to...|set a small goal and celebrate when you reach it|only focus on failures|avoid every challenge|compare yourself constantly|Small wins grow confidence.
4.B|4|Perseverance means...|continuing to work toward a goal even when it is hard|quitting at the first problem|waiting for luck|avoiding goals|Persistence builds success.
4.B|4|A benefit of setting short-term goals along the way to a long-term goal is that they...|help you track progress|make the goal vanish|slow you down|create confusion|Steps show progress.
4.C|4|When setting a goal, you should make choices based on...|what will help you reach the goal|what is easiest only|what friends say only|chance|Choices should support the goal.
4.C|4|Making a plan with steps and a deadline is part of...|goal setting|daydreaming|guessing|quitting|Planning leads to success.
4.D|4|Identifying an area for personal growth is a first step toward...|setting a goal to improve|giving up|hiding problems|blaming others|Knowing what to improve guides goals.
4.D|4|A realistic personal goal might be...|reading twenty minutes each night|becoming famous by tomorrow|never making mistakes|learning everything in a day|Realistic goals can be reached.
5.A|4|School climate refers to...|how safe and welcoming a school feels|the weather outside|the school's roof color|lunch menu only|Climate affects well-being.
5.A|4|A school safety measure that supports well-being is...|an anti-bullying policy|ignoring problems|broken locks|no adult supervision|Policies protect students.
5.B|4|As the brain develops during childhood, it gets better at...|planning and controlling emotions|nothing at all|forgetting everything|sleeping only|The brain matures with age.
5.B|4|The part of the brain that helps with decision making keeps developing into...|early adulthood|age 6|age 8|age 10|The prefrontal cortex matures slowly.
6.A|4|A healthy way to manage worries about a long-term health condition is to...|talk with a doctor, counselor, or trusted adult|ignore it forever|hide it from everyone|skip treatment|Support helps coping.
6.A|4|An unhealthy way to manage worries is to...|ignore treatment and avoid talking about it|talk to a counselor|journal|exercise|Avoidance makes problems worse.
6.B|4|Which situation shows stress helping someone achieve a goal?|feeling nervous before a recital and practicing more|feeling stress and quitting|ignoring a deadline|avoiding practice|Healthy stress motivates.
6.B|4|Resilience is the ability to...|recover and keep going after a challenge|never feel stress|avoid all problems|quit|Resilient people bounce back.
6.C|4|A way to reduce the impact of loss and grief is to...|talk with supportive people and allow time to heal|hide feelings forever|never talk about it|harm yourself|Support helps recovery.
6.C|4|Trauma can affect a person's...|emotions and body|only their hair|only their shoes|nothing|Trauma has wide effects.
6.D|4|Eating disorders are...|serious mental health concerns that affect eating habits|choices about favorite foods|jokes|fashion trends|Eating disorders need professional help.
6.D|4|If a friend shows signs of an eating disorder, you should...|tell a trusted adult so they can get help|encourage the behavior|tease them|ignore it|Early help matters.
6.E|4|A situation that calls for professional mental health services is when someone...|feels hopeless or unsafe for a long time|has a happy day|loses a pencil|likes a song|Persistent distress needs professional care.
6.E|4|A school counselor can help students with...|stress, worries, and mental health concerns|only sports|only lunch|only art|Counselors provide support.
6.F|4|A healthy alternative to harming yourself or others when angry is to...|talk to a trusted adult or do something active|break things|hurt someone|bottle it up|Healthy outlets keep people safe.
6.F|4|It is important to ask for help when feelings become overwhelming because...|help keeps you and others safe|it is a secret|it never works|it wastes time|Asking for help is a strength.
7.A|4|Which food is a good source of protein?|beans and lean meat|soda|candy|plain sugar|Protein foods build muscle.
7.A|4|Which food is a good source of calcium?|yogurt or milk|candy|soda|fried chips|Dairy provides calcium.
7.A|4|Whole grains, fruits, and vegetables are good sources of...|fiber|lead|sugar only|salt only|Fiber helps digestion.
7.B|4|Food labels list calories and serving size so you can...|compare foods and choose wisely|ignore nutrition|waste money|guess|Labels show nutritional content.
7.B|4|If a label says one serving is 100 calories and you eat two servings, you eat...|200 calories|100 calories|50 calories|300 calories|Multiply calories by servings.
7.C|4|Many sugary drinks contain about how many teaspoons of added sugar in one can?|around 10 teaspoons|none|1 teaspoon|half a teaspoon|Sodas have large amounts of sugar.
7.C|4|Compared with the recommended daily limit, one can of soda can...|use up most or all of a child's added sugar limit|have no sugar|have too little sugar|be unhealthy only for adults|One drink can exceed the limit.
7.D|4|Caffeine is found in...|coffee, tea, and some energy drinks|water|milk|apple juice|Caffeine is a stimulant.
7.D|4|Too much caffeine can cause kids to feel...|jittery and have trouble sleeping|more asleep|taller|calmer|Caffeine is a stimulant.
8|4|Moderate to vigorous physical activity should total about how long each day for kids?|60 minutes|5 minutes|10 hours|0 minutes|Kids need at least an hour.
8|4|Activities that improve flexibility include...|stretching and yoga|reading|napping|writing|Stretching improves flexibility.
8|4|Muscular endurance is the ability of muscles to...|keep working for a long time|lift only once|stay still|shrink|Endurance sustains effort.
9.A|4|A good fitness goal for a fifth grader is to...|walk or play actively for 60 minutes most days|sit all day|never move|quit exercise|Goals should be achievable.
9.A|4|Setting a fitness goal helps you...|stay motivated and track improvement|forget exercise|avoid fun|stay still|Goals guide activity.
9.B|4|When you research a fitness product, you should...|check whether the claims are backed by credible evidence|buy it because of an ad|trust a celebrity only|ignore reviews|Evaluate evidence.
9.B|4|A reliable source for nutrition and activity information is...|a government health website|an anonymous video|an ad for a supplement|a rumor|Credible sources are trustworthy.
10.A|4|Eating a lot of processed foods high in saturated fat over time can raise the risk of...|heart disease|growing taller|better vision|stronger teeth|Diet affects chronic disease risk.
10.A|4|A healthy diet rich in fruits and vegetables can lower the risk of...|obesity and type 2 diabetes|colds only|a broken arm|a sprained ankle|Healthy eating prevents chronic disease.
10.B|4|Which behavior can reduce the chance of developing a chronic disease?|being active and eating well|skipping all exercise|smoking|eating only snacks|Healthy behaviors prevent disease.
10.B|4|A positive attitude toward healthy habits can help a person...|stick with them for life|quit quickly|ignore doctors|avoid food|Attitude supports habits.
11|3|Which is a safe way to use a bike on the road?|ride with traffic and use hand signals|ride against traffic|ride at night with no lights|text while riding|Following rules prevents crashes.
11|4|If you are caught in a severe weather warning, you should...|move to a safe shelter|go outside to watch|swim|ignore alerts|Shelter protects you.
11|4|Which prevents poisoning at home?|storing chemicals out of reach in original containers|mixing cleaners|leaving medicine on the counter|using unlabeled bottles|Safe storage prevents poisoning.
12.A|4|Human trafficking is...|forcing people to work or perform acts against their will|a type of sport|a school project|a travel hobby|Trafficking is exploitation.
12.A|4|A strategy for avoiding violence is to...|walk away and get help from an adult|escalate the argument|carry a weapon|encourage fights|Avoiding conflict prevents harm.
12.B|4|Gangs often recruit young people by...|offering a sense of belonging while pressuring them|offering free education|building libraries|teaching safe driving|Recruiters use false promises.
12.B|4|A warning sign of gang involvement can be...|wearing certain colors or symbols tied to a group and secrecy|joining the chess club|doing homework|baking cookies|Colors and secrecy can be signs.
12.C|4|During a lockdown at school, you should...|follow your teacher's directions and stay quiet|run around|open the door|use your phone loudly|Lockdown procedures protect students.
12.C|4|If a fire alarm sounds at school, you should...|walk calmly to the nearest exit|stay in your seat|hide|ignore it|Evacuation drills save lives.
12.D|4|A personal safety plan includes knowing...|where to go and who to call in an emergency|your favorite song|the weather|a game score|Plans prepare you.
12.D|4|A personal safety plan should be shared with...|a trusted adult|nobody|a stranger|an online friend|Adults can help carry out the plan.
13.A|4|An appropriate digital boundary is...|only sharing photos with permission|sharing friends' private photos|posting your location|giving out passwords|Respect privacy.
13.A|4|An inappropriate digital boundary is...|sending hurtful or private messages|chatting with grandparents|sharing a school project|asking for help|Harmful messages cross boundaries.
13.B|4|Identity protection online means...|keeping your personal information private|posting your home address|sharing your passwords|using one weak password everywhere|Privacy protects identity.
13.B|4|A strong password should be...|long, unique, and kept secret|your name|1234|shared with friends|Strong passwords protect accounts.
13.C|4|A consequence of posting something hurtful online is that it...|can spread quickly and be hard to remove|disappears immediately|never hurts anyone|is always private|Online posts last.
13.C|4|Cyberbullying can lead to serious consequences for the victim such as...|anxiety, depression, or trouble in school|extra friends|better grades|trophies|Cyberbullying harms mental health.
14.A|4|A way to report bullying at school is to...|tell a teacher, counselor, or principal|keep it secret|join in|post about it|Report to staff.
14.A|4|Many schools provide a way to report bullying...|anonymously through a tip line or form|only by shouting|only on weekends|never|Anonymous reports protect students.
14.B|4|To advocate for someone being bullied, you can...|stand up safely and tell an adult|laugh|record it for fun|stay silent|Advocacy helps.
14.B|4|Being an upstander means...|taking safe action to help someone being bullied|watching silently|joining in|ignoring it|Upstanders help.
14.C|4|Abuse and neglect can affect a child's...|physical and emotional health|favorite color|shoe size|speed|They harm well-being.
14.C|4|It is important to report abuse and neglect because...|adults can protect the child and get help|nobody can help|it is a secret|it gets someone a prize|Reporting protects children.
15.A|4|A reason to avoid misusing prescription drugs is that...|they can cause overdose or serious harm|they are free|they taste good|they make you taller|Misuse can be deadly.
15.A|4|Taking more of a medicine than directed can lead to...|poisoning or overdose|better health|stronger bones|faster running|Too much medicine is dangerous.
15.B|4|The expiration date on a medicine label tells you...|when the medicine should no longer be used|when to buy a toy|the weather|a shoe size|Expired medicine may not work or be unsafe.
15.B|4|The dosage instructions on a label tell you...|how much to take and how often|the brand's history|the price|the color|Doses prevent harm.
15.B|4|Active ingredients on an over-the-counter label are...|the components that treat the symptoms|flavors only|the price|decoration|They explain what the medicine does.
15.C|4|Nicotine in vaping products and tobacco can cause...|addiction and a faster heart rate|stronger lungs|better sleep|taller height|Nicotine is addictive.
15.C|4|Alcohol affects the brain by...|slowing communication between brain cells|helping memory|making reflexes faster|improving balance|Alcohol impairs the brain.
15.C|4|Marijuana and other drugs can harm a growing brain by...|affecting memory and learning|improving learning|building bones|making people faster|Drugs interfere with brain development.
16.A|4|A long-term effect of tobacco use is...|lung cancer and heart disease|stronger lungs|better grades|taller height|Tobacco causes chronic diseases.
16.A|4|A short-term effect of vaping can be...|coughing and a faster heartbeat|better breathing|stronger bones|improved sleep|Vapor irritates the lungs.
16.B|4|Selling alcohol or tobacco to minors is...|illegal and can lead to fines or jail|always legal|encouraged|a school activity|Laws protect minors.
16.B|4|Driving after using alcohol or drugs can lead to...|arrest and serious crashes|a license upgrade|a prize|better driving|Impaired driving is dangerous and illegal.
17|4|If you find someone unconscious after drug use, your first step is to...|call 911 and tell an adult|walk away|take a photo|post online|Emergency help saves lives.
17|4|Naloxone is a medicine that...|can reverse an opioid overdose|causes overdoses|is a candy|is a vitamin|Naloxone saves lives when used with 911.
18.A|4|Positive peer influence can help a person decide not to use drugs by...|encouraging healthy activities and supporting refusal|offering drugs|teasing|pressuring|Good friends support healthy choices.
18.A|4|Friends who join a team with you are an example of...|positive peer influence|negative peer influence|peer pressure to quit|a bad habit|Healthy activities are protective.
18.B|4|Reporting unsafe situations about drugs is important because...|it can prevent harm and get help for people|it gets people in trouble for no reason|it is gossip|it wastes time|Reporting protects.
18.B|4|A trusted person you could tell about an unsafe drug situation is a...|school counselor|stranger online|pet|toy|Counselors can help.
19.A|4|Being assertive when refused can help you resist pressure by...|stating your decision clearly and confidently|giving in|staying silent|apologizing for refusing|Assertiveness supports refusal.
19.A|4|Evaluating peer influence means...|thinking about whether a friend's suggestion is safe|accepting every idea|ignoring friends|copying them|Think before you act.
19.B|4|One refusal skill is to give a reason such as...|"I don't want to risk my health."|"Maybe later."|"I guess."|"Okay."|A reason strengthens refusal.
19.B|4|Another refusal skill is to suggest...|a different activity|trying it once|waiting|giving in|Offering alternatives redirects the situation.
19.B|4|A refusal skill using humor or leaving the situation is useful when...|pressure continues after you say no|you want to join|you are happy|you are alone|Leaving can protect you.
19.C|4|A healthy alternative to drug use is...|volunteering in your community|hanging out where drugs are used|skipping school|isolating|Service keeps you busy and fulfilled.
19.C|3|Joining a school club, team, or band is a way to...|build skills and friendships without drugs|avoid people|get in trouble|stay bored|Healthy activities protect.
20|4|A healthy relationship is built on...|trust, respect, and honest communication|control and pressure|secrecy|fear|Healthy relationships are respectful.
20|4|In a healthy friendship, each person...|respects the other's boundaries|pressures the other|keeps secrets that hurt|controls the other|Boundaries matter.
20|4|A sign of an unhealthy relationship is...|one person controlling or threatening the other|sharing laughter|taking turns|helping|Control is a warning sign.
21.A|4|Sexual harassment includes...|unwanted sexual comments or behavior|friendly waves|class discussions|group projects|Harassment is unwelcome behavior.
21.A|4|Sexual abuse is...|any sexual contact or behavior that is forced or not allowed by law|a game|a friendly hug|a handshake|It is never the child's fault.
21.A|4|Sex trafficking is...|forcing a person into sexual acts for money|a vacation|a job fair|a sport|It is a crime.
21.B|4|If someone is touching you in a way that makes you uncomfortable, you should tell...|a trusted adult such as a parent, teacher, or counselor|nobody|a stranger|an online friend|Trusted adults can protect you.
21.B|4|You can report suspected abuse by telling a trusted adult or calling...|a child abuse hotline|a restaurant|a store|a bus driver|Hotlines provide help.
21.C|4|A refusal skill when someone gives unwanted touch is to...|say "No!" loudly and go to a trusted adult|stay silent|laugh|give in|You have the right to say no.
21.C|4|Your body belongs to...|you|whoever asks|everyone|nobody|You decide who touches you.
21.D|4|Setting personal boundaries means deciding...|what you are comfortable with and saying so|to let everyone decide for you|to hide your feelings|to ignore your comfort|Boundaries protect you.
21.D|4|Making decisions about personal boundaries is important to protect your...|safety and well-being|shoe size|hair color|lunch|Boundaries keep you safe.
22.A|4|Puberty can bring physical changes such as...|growth spurts and body hair|losing teeth|shrinking|a new skeleton|Puberty changes bodies.
22.A|4|During puberty, social and emotional changes can include...|stronger moods and new interests|no feelings|only sleeping|no friendships|Emotions can shift.
22.A|4|A changing voice is one change that occurs during puberty for...|males|nobody|only babies|only teachers|Voice deepens in many males.
22.B|4|The menstrual cycle usually repeats about every...|28 days|2 days|2 years|100 days|The average cycle is about 28 days.
22.B|4|During the menstrual cycle, an egg is released from an...|ovary|stomach|lung|kidney|Ovulation occurs in the ovary.
22.C|4|Hormones are chemical messengers that help the body...|grow and develop|forget|shrink|stop moving|Hormones guide development.
22.C|4|Secondary sex characteristics are changes such as...|body hair and breast development|eye color|fingerprints|blood type|These appear during puberty.
22.D|4|Fertilization happens when...|a sperm cell joins an egg cell|two eggs join|a seed grows|a bone heals|Fertilization starts development.
22.D|4|Reproduction is the process of...|making new living things|eating food|sleeping|breathing|Living things reproduce.
22.E|4|After fertilization, the developing baby is first called an embryo and later a...|fetus|seed|bud|sprout|Developmental stage names.
22.E|4|During fetal development, the baby grows inside the mother in the...|uterus|stomach|lung|bone|The uterus protects the baby.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g5_health.jsonl'))
print("saved", len(B.out), "questions")

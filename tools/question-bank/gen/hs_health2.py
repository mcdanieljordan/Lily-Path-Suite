import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('115.39.c.', 1011, own='hs_health2.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('3',3,"A student wrote down three strengths and two skills to improve, then picked one to work on this month. This builds a healthy self-concept through what?",
  "Self-assessment and goal setting",["Comparing to others","Avoiding feedback","Ignoring weaknesses"],"Honest self-evaluation plus a goal builds self-concept.")
H('3',3,"Which decision-making step comes right after listing the possible choices?",
  "Weighing the possible outcomes of each choice",["Acting without thinking","Asking nobody","Choosing at random"],"Decision making means comparing consequences.")
H('4',3,"Chronic bullying is a risk factor for mental health problems because it can lead to what?",
  "Ongoing stress, anxiety or depression",["Better resilience for everyone","No effect","Higher confidence"],"Risk factors increase the chance of mental health problems.")
H('4',3,"Which is a protective factor that helps a student cope with stress?",
  "Having a caring mentor and a regular sleep routine",["Skipping meals","Staying isolated","Avoiding all help"],"Protective factors build resilience.")
H('6',2,"A person eating about 2,000 calories a day who wants to follow MyPlate guidance should fill about half of the plate with what?",
  "Fruits and vegetables",["Candy","Fried food","Soda"],"MyPlate recommends half the plate from fruits and vegetables.")
H('6',3,"Nutrition recommendations for teens suggest limiting what?",
  "Sugary drinks and foods high in saturated fat and sodium",["Water","Vegetables","Whole grains"],"Limit added sugar, saturated fat and sodium.")
H('10',2,"A student who finds a fire alarm sounding in the building should first do what?",
  "Leave by the planned route and report to the meeting spot",["Hide in a restroom","Go back for belongings","Wait at a desk"],"Follow the evacuation plan.")
H('10',2,"CPR for an adult in cardiac arrest involves chest compressions at a depth of about what?",
  "2 inches at a steady rapid rate",["Half an inch","8 inches","No pressing at all"],"Compressions must be deep enough to circulate blood.")
H('15',3,"Long-term heavy alcohol use is associated with damage to which organ?",
  "The liver",["The hair","The toenails","The earlobes"],"Alcohol is processed by the liver.")
H('15',3,"Which short-term effect is associated with marijuana use?",
  "Impaired memory, judgment and coordination",["Improved reaction time","Better focus on driving","Stronger balance"],"It affects thinking and motor skills.")
H('16',3,"Which is a treatment approach for substance use disorders?",
  "Behavioral therapy combined with medical support",["Hiding the problem","Punishing only","Waiting it out"],"Evidence-based treatment combines approaches.")
H('16',3,"A person who is addicted may need treatment because addiction is what?",
  "A medical condition that is treatable",["Only a weakness","A phase","Always harmless"],"Treatment can lead to recovery.")
H('18',3,"Prevention of substance abuse is most effective when it includes what?",
  "Education, strong family involvement and positive peer groups",["Silence","Easy access","Fear alone"],"Prevention programs use many supports.")
H('18',3,"Which message is an example of an effective prevention strategy at school?",
  "Teaching refusal skills and offering alternative activities",["Ignoring drug use","Punishing only","Hiding information"],"Skills and alternatives lower use.")
H('1.A',3,"Which factor most limits a teen's access to health care?",
  "Lack of insurance or transportation",["Having a doctor nearby","Free clinics","Telehealth"],"Cost and access are common barriers.")
H('1.A',3,"A community health clinic often helps people who cannot afford care by doing what?",
  "Charging fees based on income",["Charging the most","Closing early","Refusing all patients"],"Sliding-scale fees increase access.")
H('1.B',3,"One way to overcome a language barrier at a doctor's visit is to use what?",
  "A qualified interpreter",["A guess","Silence","A rumor"],"Interpreters help patients understand.")
H('1.B',3,"A teen with no transportation to a clinic could overcome this barrier by doing what?",
  "Using a telehealth visit or school-based health service",["Ignoring symptoms","Waiting months","Skipping care"],"Alternatives improve access.")
H('1.C',3,"A law requiring immunizations before school enrollment is an example of a policy that does what?",
  "Protects community health",["Lowers school safety","Prevents learning","Raises disease rates"],"Public health laws reduce disease spread.")
H('1.C',3,"Anti-discrimination laws influence health by doing what?",
  "Helping ensure equal access to care",["Limiting treatment","Raising costs","Ending insurance"],"Policies shape access.")
H('2.A',3,"A relationship in which one person isolates the other from friends has what effect?",
  "Negative effects on emotional and social health",["Positive effects only","No effects","Better health"],"Control and isolation are harmful.")
H('2.A',3,"A supportive friendship tends to improve physical health because it does what?",
  "Reduces stress and encourages healthy habits",["Increases risk","Limits sleep","Ends exercise"],"Support helps health.")
H('2.B',3,"Which communication behavior shows consideration for others' differences?",
  "Listening without interrupting and asking respectful questions",["Mocking accents","Ignoring them","Speaking over them"],"Respectful communication values differences.")
H('2.B',3,"Using \"I\" statements helps because they do what?",
  "Express your feelings without blaming",["Attack the listener","End the talk","Hide feelings"],"They reduce defensiveness.")
H('2.C',3,"Two students disagree about a group project. Which technique is most effective for resolving the conflict?",
  "Listening to both sides and finding a compromise",["Walking away angry","Threatening","Ignoring it"],"Compromise resolves conflicts.")
H('2.C',3,"Mediation is effective in conflict resolution because it does what?",
  "Uses a neutral third person to help both sides reach an agreement",["Picks a winner by force","Blames one side","Ends communication"],"A mediator guides the discussion.")
H('5.A',3,"Positive stress, such as preparing for a performance, can build resilience by doing what?",
  "Teaching coping skills and confidence",["Causing harm","Ending motivation","Reducing effort"],"Manageable stress can help growth.")
H('5.A',3,"A challenge that is difficult but manageable is an example of what?",
  "Positive stress",["Toxic stress","No stress","Harmful abuse"],"It builds resilience.")
H('5.B',3,"Which is a healthy way to manage stress?",
  "Exercise, sleep, talking to someone and deep breathing",["Using alcohol","Avoiding all people","Skipping sleep"],"Healthy coping lowers stress.")
H('5.B',3,"Seeking counseling for anxiety is a healthy choice because it does what?",
  "Provides tools and support for managing symptoms",["Worsens it","Hides it","Is a sign of failure"],"Counseling is effective.")
H('5.C',3,"A health-risk behavior associated with eating disorders is what?",
  "Extreme dieting and a distorted view of body image",["Balanced meals","Regular exercise only","Eating with friends"],"Eating disorders are serious illnesses.")
H('5.C',3,"A person showing signs of an eating disorder should be encouraged to do what?",
  "See a doctor or counselor trained in treating eating disorders",["Diet harder","Hide it","Ignore it"],"Professional treatment helps recovery.")
H('5.D',3,"Why is it helpful to know about the 988 Suicide and Crisis Lifeline?",
  "It gives free, confidential help any time to someone in distress",["It is only for adults","It costs money","It replaces family"],"Knowing resources helps people reach support.")
H('5.D',3,"If a friend seems to be in crisis, calling or texting 988 can help by doing what?",
  "Connecting you to trained counselors for guidance and support",["Starting an argument","Delaying help","Hiding the issue"],"Counselors can guide next steps.")
H('5.E',3,"Looking at local, state and national suicide data helps communities by doing what?",
  "Showing where prevention resources are needed",["Increasing risk","Ending prevention","Hiding the issue"],"Data guides prevention planning.")
H('5.E',3,"Which source provides national data on suicide rates?",
  "The Centers for Disease Control and Prevention",["A rumor","A social media post","A guess"],"The CDC publishes national health data.")
H('7.A',3,"Compared with a sedentary lifestyle, an active lifestyle lowers the risk of what?",
  "Heart disease and type 2 diabetes",["Strong bones","Better sleep","Higher energy"],"Activity reduces chronic disease risk.")
H('7.A',3,"Adults and teens are generally advised to get about how much physical activity?",
  "At least 60 minutes a day for teens",["10 minutes a week","None","5 minutes a month"],"Teens need about 60 minutes daily.")
H('7.B',3,"A fitness profile for a teen might include which measure?",
  "Resting heart rate, endurance and flexibility results",["Shoe color","Favorite song","Locker number"],"Profiles track fitness components.")
H('7.B',3,"A wearable device helps a teen build a fitness profile by doing what?",
  "Tracking activity, heart rate and sleep data",["Cooking meals","Writing essays","Painting"],"Technology records measurable data.")
H('8.A',3,"A student's short-term goal is to walk 8,000 steps daily this week, and the long-term goal is to run a 10K in six months. Why track progress?",
  "To see whether the plan is working and adjust it",["To avoid effort","To hide results","To compare to rivals"],"Tracking guides adjustments.")
H('8.A',3,"If a person misses a weekly fitness goal, a good response is to do what?",
  "Analyze the barrier and revise the plan",["Quit","Blame others","Ignore goals"],"Adjust the plan after review.")
H('8.B',3,"An ad for a supplement says \"doctors don't want you to know this secret.\" This is an example of what?",
  "A marketing technique that may mislead",["Medical advice","Peer-reviewed evidence","A public health warning"],"Be skeptical of exaggerated claims.")
H('8.B',3,"Celebrity endorsements in health ads are used to do what?",
  "Persuade buyers by association with a popular person",["Provide data","Prove safety","Replace research"],"Endorsements are persuasion techniques.")
H('9.A',3,"Chronic conditions such as diabetes can have an economic impact on society by doing what?",
  "Increasing health care costs and lost work time",["Reducing costs","Raising productivity","Ending insurance"],"Chronic illness is expensive.")
H('9.A',3,"A social impact of a chronic illness on a family can be what?",
  "Emotional stress and caregiving responsibilities",["Less stress","No change","Free care"],"Illness affects families.")
H('9.B',3,"A plan for accessing community resources for a chronic condition could include what?",
  "Support groups, a primary care provider and reliable online information",["Rumors","No contact","Random ads"],"Resources help manage conditions.")
H('9.B',3,"A digital resource is reliable for a health plan if it is from what?",
  "A medical or government organization",["An anonymous poster","A stranger","A sales page"],"Credible sources matter.")
H('11.A',3,"If a student finds a firearm in an unsafe place, the safest response is to do what?",
  "Do not touch it, leave the area and tell an adult",["Pick it up","Show friends","Take it home"],"Never handle found weapons.")
H('11.A',3,"A person who sees someone with a weapon at school should do what?",
  "Move to safety and report to staff or call 911",["Confront them","Film it","Ignore it"],"Report and get safe.")
H('11.B',3,"A good home safety model for children includes what?",
  "Locking up medications, chemicals and weapons",["Leaving items out","Hiding smoke detectors","Ignoring hazards"],"Safe storage prevents injury.")
H('11.B',3,"An educational safety model for a school might include what?",
  "Clear emergency drills and posted procedures",["No drills","Secret plans","Random rules"],"Practice and clarity improve safety.")
H('12.A',3,"A consequence of posting an inappropriate image online is that it may do what?",
  "Stay online permanently and harm future opportunities",["Disappear immediately","Be private forever","Have no effect"],"The digital footprint lasts.")
H('12.A',3,"Which is a consequence of cyberbullying for the victim?",
  "Anxiety, depression or fear of going to school",["Higher confidence","Better grades","Closer friendships"],"Cyberbullying harms mental health.")
H('12.B',3,"Sharing someone's private images without permission can be what?",
  "A crime with legal penalties",["Always legal","A joke","A harmless prank"],"There are laws against it.")
H('12.B',3,"An ethical use of social media includes doing what?",
  "Respecting others' privacy and getting permission before sharing",["Posting anything","Sharing rumors","Impersonating others"],"Ethics means respect and honesty.")
H('13.A',3,"If a student sees a classmate being cyberbullied, the best response is to do what?",
  "Support the victim and report it",["Share the post","Join in","Laugh"],"Intervention helps the victim.")
H('13.A',3,"A situation requiring adult intervention in bullying is one that involves what?",
  "Threats, repeated harm or risk to safety",["A single polite disagreement","A joke between friends","A normal debate"],"Serious harm needs adults.")
H('13.B',3,"A schoolwide strategy to prevent bullying is what?",
  "Clear rules, reporting systems and kindness campaigns",["Silence","Ignoring reports","Blaming victims"],"Prevention needs structure.")
H('13.B',3,"Bystander training helps reduce bullying because it does what?",
  "Teaches students safe ways to speak up and report",["Encourages watching","Ignores victims","Blames them"],"Bystanders can make a difference.")
H('14.A',3,"Substance misuse can affect a teen's relationships and school performance by doing what?",
  "Increasing conflict and lowering attendance and grades",["Improving both","Having no effect","Raising motivation"],"Misuse disrupts life areas.")
H('14.A',3,"Addiction affects the brain by changing what?",
  "The reward and decision-making systems",["Hair color","Eye color","Height"],"Addiction rewires pathways.")
H('14.B',3,"An alternative to substance use for managing boredom might be what?",
  "Joining a sport, club or creative activity",["Using alcohol","Skipping school","Isolating"],"Healthy outlets protect teens.")
H('14.B',3,"Why do alternative activities help prevent misuse?",
  "They give healthy ways to cope, connect and have fun",["They cause stress","They isolate","They add pressure"],"Positive activities reduce risk.")
H('14.C',3,"A community protective factor against substance use is what?",
  "Youth programs and supportive adults",["Easy access to drugs","Isolation","Neglect"],"Community supports protect.")
H('14.C',3,"An individual protective skill is what?",
  "Refusal skills and stress management",["Impulsiveness","Peer pressure","Secrecy"],"Skills protect individuals.")
H('17.A',3,"Driving after drinking is dangerous because alcohol does what to a driver?",
  "Slows reaction time and impairs judgment",["Improves focus","Speeds reaction","Sharpens vision"],"Impaired driving causes crashes.")
H('17.A',3,"A legal consequence of drinking and driving can be what?",
  "License suspension, fines or jail time",["A reward","A discount","Nothing"],"DWI carries penalties.")
H('17.B',3,"A social influence on prescription drug misuse among teens is what?",
  "Peers sharing pills at a party",["Doctor-prescribed use","Reading labels","Safe storage"],"Peers affect misuse.")
H('17.B',3,"A physical environment risk factor for prescription misuse is what?",
  "Unlocked medicine cabinets at home",["Locked storage","Take-back programs","Safe disposal"],"Easy access increases risk.")
H('17.C',3,"A safe haven information campaign should tell people what?",
  "Where to go for help and how to find support without judgment",["How to hide problems","Where to buy drugs","How to avoid care"],"Safe havens provide help.")
H('17.C',3,"A public health campaign works best when it does what?",
  "Uses clear messages, trusted messengers and accessible channels",["Is vague","Hides contacts","Is confusing"],"Clarity and trust matter.")
H('19.A',3,"Which is an effective way to communicate emotions in a healthy relationship?",
  "Calmly describing how you feel and listening to the other person",["Giving the silent treatment","Yelling","Blaming"],"Healthy communication is open.")
H('19.A',3,"Which method is an ineffective way to communicate emotions?",
  "Name-calling during a disagreement",["Listening","Using I statements","Taking a break to calm down"],"Insults harm relationships.")
H('19.B',3,"A behavior that enhances dignity and respect in a romantic relationship is what?",
  "Accepting a partner's decision when they say no",["Pressuring them","Checking their phone","Controlling plans"],"Respect honors boundaries.")
H('19.B',3,"Which behavior damages dignity in a relationship?",
  "Humiliating a partner in front of others",["Honest talks","Shared decisions","Kindness"],"Humiliation is disrespectful.")
H('19.C',3,"A healthy marriage can support children through what?",
  "Stable routines and cooperative parenting",["Constant conflict","Neglect","Instability"],"Cooperation nurtures children.")
H('19.C',3,"Children raised in a supportive family tend to do better in what area?",
  "Emotional and social development",["Only in sports","Nothing","Only in math"],"Support helps development.")
H('20.A',3,"A community resource for people who have experienced sexual harassment or assault is what?",
  "A rape crisis center or hotline",["A rumor","A bar","A shopping mall"],"Crisis centers provide help.")
H('20.A',3,"Which national hotline supports survivors of sexual assault?",
  "The RAINN National Sexual Assault Hotline",["A food delivery line","A weather line","A sports line"],"RAINN offers confidential support.")
H('20.B',3,"Reporting sexual harassment to a trusted adult is important because it can do what?",
  "Stop the behavior and connect the victim with help",["Create trouble","Encourage it","Delay help"],"Reporting protects people.")
H('20.B',3,"A student who is harassed should report to whom?",
  "A parent, counselor or other trusted adult",["No one","Only a stranger","Social media"],"Trusted adults can act.")
H('20.C',3,"Refusal skills can be used to set limits by doing what?",
  "Saying no clearly and sticking to boundaries",["Saying maybe","Hesitating","Changing the topic only"],"Clear refusals set limits.")
H('20.C',3,"Which refusal strategy is the most effective?",
  "A firm no, a reason or alternative and leaving the situation",["A vague answer","An apology","Staying silent"],"Be clear and direct.")
H('20.D',3,"Substances increase sexual risk because they do what?",
  "Reduce judgment and the ability to set limits",["Improve safety","Prevent mistakes","Improve consent"],"Impairment raises risk.")
H('20.D',3,"A person under the influence of alcohol cannot give valid consent because of what?",
  "Impaired ability to make a clear decision",["Good judgment","Clear thinking","Full control"],"Consent must be clear.")
H('20.E',3,"Which is an influence that may pressure a teen to become sexually active?",
  "Media messages and peer expectations",["Strong values","Parental guidance","Supportive friends"],"Pressures come from many sources.")
H('20.E',3,"It is wrong to violate another person's boundaries because it does what?",
  "Disrespects their right to control their own body",["Is harmless","Is acceptable","Is expected"],"Consent is necessary.")
H('21.A',3,"Which hormone is associated with male puberty?",
  "Testosterone",["Insulin","Adrenaline only","Melatonin"],"Hormones drive pubertal change.")
H('21.A',3,"Emotional changes during adolescence can include what?",
  "Mood swings and stronger feelings of independence",["No emotions","Constant calm","No changes"],"Adolescence brings emotional change.")
H('21.B',3,"Which factor can affect fetal development?",
  "The mother's nutrition and health during pregnancy",["The color of the nursery","The mother's shoe size","The brand of clothing"],"Prenatal health matters.")
H('21.B',3,"Heredity influences fetal development because it does what?",
  "Passes genetic traits and risks from parents",["Changes the weather","Ends growth","Chooses the hospital"],"Genes matter.")
H('21.C',3,"Postpartum depression is what?",
  "A condition of sadness or anxiety after giving birth",["A cold","A diet","An allergy"],"It is treatable.")
H('21.C',3,"Emotional changes that may occur during pregnancy are often caused by what?",
  "Hormonal changes and life stress",["Weather","Color","Sound"],"Hormones affect mood.")
H('22.A',3,"Options for a teenage parent include which of the following?",
  "Parenting, adoption or other legal choices with support from trusted adults",["Ignoring the situation","Hiding it","Doing nothing"],"Support helps with decisions.")
H('22.A',3,"Adoption is the legal process of what?",
  "Transferring parental rights to another family",["Ending school","Changing a name only","Moving homes"],"Adoption is a legal option.")
H('22.B',3,"Untreated chlamydia and gonorrhea can lead to what in the long term?",
  "Infertility and pelvic inflammatory disease",["Better health","Stronger immunity","Faster healing"],"Untreated bacterial STIs cause damage.")
H('22.B',3,"A viral STI that has no cure but can be managed with treatment is what?",
  "HIV",["Strep throat","Chlamydia","Gonorrhea"],"Viral STIs are managed, not cured.")
H('22.C',3,"A minor's right to consent in some circumstances in Texas includes consent for what?",
  "Treatment related to certain health services, under specific laws",["Any surgery","Voting","Driving at 12"],"Laws allow limited consent for some care.")
H('22.C',3,"A community resource for STI testing is what?",
  "A public health department clinic",["A game store","A bakery","A gas station"],"Clinics offer testing.")
H('22.D',3,"Why do typical-use failure rates exceed perfect-use rates for contraceptives?",
  "People do not always use them correctly or consistently",["They are perfect","Because of weather","Because of age only"],"Human behavior affects results.")
H('22.D',3,"Which choice is 100 percent effective at preventing pregnancy and STIs?",
  "Abstinence",["Any barrier alone","Withdrawal","Rhythm method"],"Only abstinence eliminates risk.")
H('22.E',3,"The HPV vaccine is effective at preventing what?",
  "Infection with the types of HPV that cause most cervical cancers",["The flu","Allergies","Colds"],"Vaccination prevents certain cancers.")
H('22.E',3,"Hepatitis B can be prevented by what?",
  "A vaccine series",["Hand sanitizer","A vitamin","A haircut"],"A vaccine is available.")
H('22.F',3,"A benefit of abstinence is that it allows a teen to focus on what?",
  "Personal goals, education and emotional health",["Risky behavior","Only gossip","Only games"],"Abstinence supports future goals.")
H('22.F',3,"Choosing abstinence helps protect against what?",
  "Unintended pregnancy and STIs",["Good grades","Friendships","Exercise"],"It eliminates the risk.")
H('22.G',3,"A teen creating strategies for abstinence might do what?",
  "Plan activities, talk with parents and set clear limits",["Avoid advice","Hide plans","Ignore friends"],"Support makes plans stronger.")
H('22.G',3,"Support from parents and trusted adults helps a teen make healthy decisions because they do what?",
  "Offer guidance, accountability and encouragement",["Give pressure","Add stress","Avoid talking"],"Support strengthens choices.")
H('22.H',3,"Under Texas law, sexual activity with a minor can be what?",
  "A crime, regardless of consent in many cases",["Always legal","A game","A civil matter only"],"The law protects minors.")
H('22.H',3,"The age of consent in Texas is what?",
  "17",["10","13","21"],"Texas sets the age of consent at 17.")
H('22.I',3,"Sexual harassment can be addressed by laws that do what?",
  "Prohibit unwanted sexual behavior and provide penalties",["Allow it","Ignore it","Reward it"],"Laws protect victims.")
H('22.I',3,"Sexting images of a minor can lead to what?",
  "Serious criminal charges",["A prize","A warning only","Nothing"],"Laws on child sexual images are strict.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_health2.jsonl'))

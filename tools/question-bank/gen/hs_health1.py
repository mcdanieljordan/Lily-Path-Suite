import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('115.38.c.', 1010, own='hs_health1.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('3',3,"Maya sets a goal to run a 5K in 12 weeks and tracks her progress each Sunday. Which skill is she mainly using?",
  "Goal setting and self-assessment",["Peer pressure","Avoidance","Impulse buying"],"Tracking progress toward a goal builds a healthy self-concept.")
H('3',3,"After a poor quiz score, a student reviews what went wrong and plans two changes. This shows a healthy self-concept because the student does what?",
  "Evaluates honestly and makes a plan to improve",["Blames others","Gives up","Hides the score"],"Self-evaluation and decision making support a healthy self-concept.")
H('4',3,"Which is a protective factor for teen mental health?",
  "A supportive relationship with a trusted adult",["Social isolation","Untreated stress","Constant bullying"],"Protective factors lower risk and build resilience.")
H('4',3,"Adverse childhood experiences, such as growing up with ongoing family conflict, can raise the risk of what later in life?",
  "Mental and physical health problems",["Better grades automatically","Faster running","Longer sleep always"],"Early stress can affect long-term health.")
H('9',2,"If a classmate has a nosebleed, which first-aid step is correct?",
  "Have the person sit and lean slightly forward while pinching the soft part of the nose",["Tilt the head far back","Lay the person flat","Put ice down the shirt"],"Leaning forward keeps blood from running down the throat.")
H('9',2,"Before giving first aid at an accident scene, you should first do what?",
  "Check that the scene is safe and call for help",["Move the victim at once","Leave the area","Take photos"],"Scene safety protects you and the victim.")
H('14',3,"Long-term use of tobacco products is most strongly linked with an increased risk of which condition?",
  "Lung disease and cancer",["Stronger bones","Better lung capacity","Lower blood pressure"],"Tobacco harms the lungs and raises cancer risk.")
H('14',3,"Nicotine in vaping products is dangerous for teens because it does what?",
  "Can harm the developing brain and cause addiction",["Improves memory","Cures stress","Builds muscle"],"The teen brain is still developing.")
H('20',3,"Fertilization occurs when what happens?",
  "A sperm cell joins with an egg cell",["Two eggs divide","A hormone is released","An embryo implants"],"Fertilization forms a zygote.")
H('20',3,"Which behavior supports healthy fetal development during pregnancy?",
  "Regular prenatal care and avoiding alcohol and tobacco",["Skipping checkups","Using alcohol","Smoking occasionally"],"Prenatal care improves outcomes.")
H('1.A',2,"A student checks the author, date and sponsor of a website before trusting its health advice. This is an example of what?",
  "Evaluating the reliability of health information",["Skimming headlines","Copying a friend's advice","Ignoring labels"],"Reliable sources are current and credible.")
H('1.A',3,"Which source is most reliable for information about vaccines?",
  "The Centers for Disease Control and Prevention",["An anonymous video","A celebrity post","A product ad"],"Government and medical agencies are reliable sources.")
H('1.B',3,"Which strategy helps prevent the spread of a communicable disease such as the flu?",
  "Getting a flu shot and washing hands often",["Sharing drinks","Skipping sleep","Ignoring symptoms"],"Vaccines and hygiene reduce spread.")
H('1.B',3,"Which is a non-communicable disease that can be reduced by regular exercise and a balanced diet?",
  "Type 2 diabetes",["Strep throat","Measles","The common cold"],"Lifestyle affects chronic disease risk.")
H('1.C',3,"Why is early detection of a disease such as skin cancer important?",
  "Treatment is often more effective when problems are found early",["It makes screening unnecessary","It prevents all illness","It delays treatment"],"Early detection improves outcomes.")
H('1.C',3,"A teen notices a mole that is changing in size and color. The best action is to do what?",
  "See a health care provider",["Wait a year","Cut it off","Ignore it"],"Warning signs should prompt a check-up.")
H('2.A',2,"Perspective-taking means doing what?",
  "Trying to understand how a situation looks and feels to someone else",["Winning every argument","Ignoring feelings","Giving orders"],"It builds respect and empathy.")
H('2.A',2,"Which response shows respect for a friend who is upset about not making the team?",
  "Listening and acknowledging how they feel",["Telling them to get over it","Laughing","Changing the subject"],"Respectful responses acknowledge feelings.")
H('2.B',3,"Saying \"I feel upset when plans change at the last minute, and I'd like a heads-up\" is which style of communication?",
  "Assertive",["Passive","Aggressive","Silent"],"Assertive communication is clear and respectful.")
H('2.B',3,"Yelling and name-calling during a disagreement is an example of which communication style?",
  "Aggressive",["Assertive","Passive","Respectful"],"Aggressive communication disregards others.")
H('5.A',3,"A friend says they feel hopeless and talks about not wanting to be here. What is the most important thing to do?",
  "Tell a parent, counselor or other trusted adult right away",["Keep it a secret","Wait to see if it passes","Post about it online"],"Telling a trusted adult is a key protective step.")
H('5.A',3,"Which is a protective factor against suicide identified by public health agencies?",
  "Strong connections to family, friends and community",["Isolation","Access to dangerous items","Substance use"],"Connectedness protects.")
H('5.B',3,"Calling or texting 988, the Suicide and Crisis Lifeline, can help a person who is in crisis by doing what?",
  "Connecting them with trained counselors who can help",["Replacing all other care","Judging them","Ignoring them"],"988 offers free, confidential support.")
H('5.B',3,"Using crisis resources such as a hotline reduces risk because it does what?",
  "Provides support and a path to help when someone feels overwhelmed",["Increases isolation","Delays help","Discourages talking"],"Support lowers the likelihood of harm.")
H('6.A',2,"On a food label, which item tells you the amount of one portion?",
  "Serving size",["Barcode","Brand name","Recycling symbol"],"Everything on the label is based on serving size.")
H('6.A',3,"A snack lists 180 calories per serving and the bag holds 3 servings. How many calories are in the whole bag?",
  "540",["180","360","60"],"180 x 3 = 540.")
H('6.B',3,"Which dietary practice is healthy?",
  "Eating a variety of fruits, vegetables and whole grains",["Skipping breakfast daily","Drinking only soda","Eating only fast food"],"Variety supports health.")
H('6.B',3,"A diet very high in added sugar is linked to what?",
  "Weight gain and tooth decay",["Stronger teeth","Lower risk of diabetes","Better sleep"],"Added sugar harms health.")
H('6.C',3,"Why might a personal dietary plan change over a lifetime?",
  "Needs change with age, activity level and health",["Needs never change","Only the weather matters","Taste is the only factor"],"Calorie and nutrient needs shift.")
H('6.C',3,"An athlete training daily usually needs what compared with an inactive person of the same size?",
  "More energy (calories) and fluids",["Fewer calories","No water","Only sugar"],"Activity raises energy needs.")
H('7.A',3,"Regular physical activity combined with good nutrition improves quality of life by doing what?",
  "Boosting energy, mood and sleep",["Causing fatigue","Lowering mood","Reducing focus"],"Nutrition and activity work together.")
H('7.A',3,"Which pairing best supports bone health?",
  "Calcium-rich foods and weight-bearing exercise",["Soda and no exercise","Skipping meals","Only sitting"],"Both build bone.")
H('7.B',3,"Body composition refers to what?",
  "The proportion of fat, muscle, bone and water in the body",["Only weight","Only height","Shoe size"],"It is more informative than weight alone.")
H('7.B',3,"To balance energy, a person who takes in more calories than they use will most likely do what?",
  "Gain weight over time",["Lose weight","Stay the same always","Lose muscle only"],"Energy balance affects weight.")
H('8.A',3,"Compared with highly processed foods, fresh or minimally processed foods usually have what?",
  "Less added sodium, sugar and unhealthy fat",["More additives","More added salt","Lower nutrition"],"Fresh foods are generally more nutritious.")
H('8.A',3,"Which is the best way to prepare chicken to limit added fat?",
  "Bake or grill it",["Deep fry it","Bread and fry it","Cover it in cheese sauce"],"Baking or grilling uses less added fat.")
H('8.B',3,"Which combination helps prevent heart disease?",
  "Regular activity and a diet low in saturated fat and sodium",["Inactivity and fast food","Smoking and rest","Energy drinks and no sleep"],"Both choices lower risk.")
H('8.B',3,"A diet high in fiber from vegetables and whole grains helps reduce the risk of what?",
  "Type 2 diabetes and heart disease",["Strong immunity loss","Vision gains","Faster aging"],"Fiber supports metabolic and heart health.")
H('10.A',3,"Which strategy best helps a teen avoid gang involvement?",
  "Joining positive activities and staying connected with supportive adults",["Joining a gang for protection","Carrying a weapon","Skipping school"],"Positive connections reduce risk.")
H('10.A',3,"A common tactic used by human traffickers is to do what?",
  "Offer false promises of jobs or relationships to gain trust",["Announce their plans","Offer free tickets honestly","Pay full wages"],"Traffickers use deception.")
H('10.B',3,"Gang recruitment often targets teens by doing what?",
  "Offering a sense of belonging, status or protection",["Offering careers","Offering scholarships","Offering safe schools"],"Recruiters exploit needs for belonging.")
H('10.B',3,"One risk of gang involvement is what?",
  "Higher exposure to violence and legal trouble",["Better safety","Guaranteed jobs","More freedom"],"Gangs expose members to harm.")
H('11.A',3,"A stranger online asks a teen to keep their chat a secret and to send a photo. The teen should do what?",
  "Refuse, stop talking and tell a trusted adult",["Send the photo","Keep it secret","Share their address"],"Secrecy and photo requests are warning signs.")
H('11.A',3,"Which online habit best protects privacy?",
  "Setting accounts to private and not sharing location",["Posting your address","Accepting all requests","Sharing passwords"],"Privacy settings reduce risk.")
H('11.B',3,"If someone sends a threatening message online, a teen should do what?",
  "Save the evidence, not respond, and report it to a trusted adult",["Delete everything","Reply with threats","Ignore forever"],"Evidence helps adults respond.")
H('11.B',3,"Sexting is risky for teens because shared images can do what?",
  "Spread beyond the sender's control and may have legal consequences",["Be deleted forever","Stay private always","Cause no harm"],"Images can be copied and shared.")
H('12.A',3,"Exposure to family violence can lead to cyclical patterns because children may do what?",
  "Learn violent behavior as normal and repeat it unless they get help",["Always avoid conflict","Become immune","Never be affected"],"Cycles can be broken with support.")
H('12.A',3,"Which step can help break a cycle of family violence?",
  "Seeking counseling and support from trusted adults",["Hiding it","Retaliating","Ignoring it"],"Support and counseling help.")
H('12.B',3,"A personal action plan for bullying should include what?",
  "People to tell, places to go for help and how to respond",["Revenge steps","Silence","Staying home forever"],"Plans identify supports.")
H('12.B',3,"A student who sees bullying can help by doing what?",
  "Supporting the target and reporting it to an adult",["Joining in","Filming it for fun","Ignoring it"],"Bystanders can help safely.")
H('12.C',3,"A possible legal consequence of bullying can be what?",
  "Suspension or criminal charges depending on the behavior",["A prize","Nothing ever","Extra recess"],"Serious bullying can bring legal penalties.")
H('12.C',3,"Bullying can harm the person who bullies because it may lead to what?",
  "Discipline and damaged relationships",["Higher trust","More friends","A better record"],"There are consequences for everyone.")
H('13.A',2,"A drug label that lists \"antihistamine\" tells you the drug belongs to which category?",
  "Allergy medication",["Antibiotic","Pain reliever","Vitamin"],"Labels identify drug categories and uses.")
H('13.A',2,"On an over-the-counter label, \"Directions\" tell you what?",
  "How much to take and how often",["The price","The color","Where it was shipped"],"Follow label directions.")
H('13.B',3,"Which is the safest way to store prescription medicine at home?",
  "In a locked cabinet away from children and visitors",["On a counter","In a backpack","Shared with friends"],"Safe storage prevents misuse.")
H('13.B',3,"Unused prescription pills should be disposed of by doing what?",
  "Using a drug take-back site or program",["Sharing them","Flushing at random","Saving for later"],"Take-back programs are safest.")
H('13.C',3,"Misusing a prescription drug includes what?",
  "Taking a drug prescribed for someone else",["Taking as prescribed","Following the label","Asking a doctor"],"Only the prescribed person should take it.")
H('13.C',3,"A warning sign of prescription drug misuse is what?",
  "Taking more than directed or taking it to get high",["Following directions","Finishing a course","Asking a pharmacist"],"Misuse deviates from directions.")
H('15.A',3,"Treatment options for substance use disorder can include what?",
  "Counseling, medication-assisted treatment and support groups",["Ignoring it","Punishment only","Hiding it"],"Treatment is available.")
H('15.A',3,"Addiction is best described as what?",
  "A chronic health condition that affects the brain",["A lack of willpower only","A choice with no help","Harmless"],"Addiction is treatable.")
H('15.B',3,"A teen who suspects a friend is abusing drugs should do what?",
  "Tell a parent, teacher or counselor",["Join in","Ignore it","Post about it"],"Trusted adults can get help.")
H('15.B',3,"Reporting suspected drug abuse to a trusted adult shows what?",
  "Care for the person's safety",["Disloyalty","Gossip","Weakness"],"It can save a life.")
H('16.A',3,"A physical influence on substance use is what?",
  "Easy access to the substance at home",["Being active","Supportive adults","Positive friends"],"Availability increases risk.")
H('16.A',3,"A social influence on substance use is what?",
  "Peer pressure to try alcohol at a party",["Sleeping well","Studying","Joining a club"],"Peers influence behavior.")
H('16.B',3,"A student organizes a school campaign for a substance-free life. This is an example of what?",
  "Health advocacy",["Peer pressure","Avoidance","Isolation"],"Advocacy promotes health.")
H('16.B',3,"A good health advocacy message is one that is what?",
  "Accurate, clear and aimed at a specific audience",["Vague","Misleading","Hidden"],"Messages must be accurate.")
H('16.C',3,"Which is a school-related effort to address health-risk behaviors?",
  "Peer-led programs and awareness weeks",["Ignoring them","Banning all talk","Secret meetings"],"Schools can organize prevention.")
H('16.C',3,"A teen can participate in school health efforts by doing what?",
  "Volunteering for a peer education team",["Skipping events","Spreading rumors","Hiding"],"Participation helps the community.")
H('17.A',3,"A refusal skill for saying no to alcohol is what?",
  "Saying no clearly, suggesting an alternative and leaving",["Making excuses and staying","Saying maybe","Laughing it off"],"Refusal skills lower risk.")
H('17.A',3,"Using refusal skills helps teens avoid substances because they do what?",
  "Give a plan to resist pressure",["Increase pressure","Remove choices","Increase risk"],"A plan makes saying no easier.")
H('17.B',3,"Alcohol and other drugs increase the risk of unsafe situations such as sexual assault because they do what?",
  "Impair judgment and the ability to give or withdraw consent",["Improve judgment","Prevent all harm","Make people safer"],"Impairment affects safety and consent.")
H('17.B',3,"If a person cannot think clearly because of alcohol or drugs, they are able to give consent. True or false?",
  "False; consent requires a clear, voluntary yes",["True","True only at parties","True with a friend"],"Impaired people cannot consent.")
H('18.A',3,"Healthy friendships provide a foundation for healthy dating relationships by building what?",
  "Trust, respect and communication",["Control","Jealousy","Secrecy"],"Friendship skills carry over.")
H('18.A',3,"Which is a quality of a healthy friendship?",
  "Mutual respect and honesty",["Control","Pressure","Isolation"],"Healthy relationships are equal.")
H('18.B',3,"Which character trait promotes a healthy dating relationship?",
  "Respect for the other person's boundaries",["Jealous control","Pressure","Dishonesty"],"Respect is essential.")
H('18.B',3,"Commitment and honest communication are important in marriage because they do what?",
  "Build trust over time",["Create secrecy","Avoid problems","Prevent talking"],"Strong relationships need both.")
H('18.C',3,"A healthy marriage can support children by doing what?",
  "Providing a stable, supportive environment",["Creating instability","Limiting support","Isolating them"],"Stability helps children.")
H('18.C',3,"Which factor in a family helps children develop well?",
  "Consistent care, love and communication",["Neglect","Conflict only","Unpredictability"],"Nurturing homes support growth.")
H('19.A',3,"Grooming in sex trafficking involves what?",
  "Building trust with a person to later exploit them",["Giving honest advice","Teaching a skill","Offering a fair job"],"Traffickers manipulate trust.")
H('19.A',3,"Which is a sign of coercion?",
  "Threats or pressure to make someone do something against their will",["Free choice","Respect","A fair agreement"],"Coercion removes choice.")
H('19.B',3,"A characteristic of a harmful dating relationship is what?",
  "A partner who tries to control who you see and what you do",["Respecting your time","Honest talks","Supporting friends"],"Control can lead to violence.")
H('19.B',3,"Constant jealousy, name-calling and checking your phone may be signs of what?",
  "An unhealthy relationship that can lead to dating violence",["Healthy love","Trust","Respect"],"These are warning signs.")
H('19.C',3,"A strategy for preventing abuse is what?",
  "Knowing safe adults and trusting your instincts when something feels wrong",["Keeping secrets","Staying silent","Ignoring discomfort"],"Awareness and support protect.")
H('19.C',3,"If an adult touches a teen in a way that feels wrong, the teen should do what?",
  "Say no, get away and tell a trusted adult",["Stay quiet","Blame themselves","Keep it secret"],"Abuse is never the victim's fault.")
H('19.D',3,"Making and respecting decisions about personal boundaries means what?",
  "Setting limits for yourself and honoring the limits of others",["Ignoring limits","Pressuring others","Having no limits"],"Boundaries protect everyone.")
H('19.D',3,"A healthy sense of self helps a teen make safer choices because it does what?",
  "Builds confidence to set limits",["Increases doubt","Reduces confidence","Encourages pressure"],"Self-worth supports boundaries.")
H('19.E',3,"Saying \"No, I'm not comfortable with that\" and walking away is an example of what?",
  "An assertive refusal strategy",["A passive response","An aggressive reaction","Giving in"],"Assertive refusals are clear and calm.")
H('19.E',3,"A good refusal strategy for unhealthy behavior is to do what?",
  "Say no firmly, give a reason or alternative and leave if needed",["Hesitate","Apologize and agree","Stay quiet"],"Be clear and direct.")
H('19.F',3,"Alcohol and other substances increase sexual risk because they do what?",
  "Impair judgment and make unsafe choices more likely",["Improve judgment","Prevent risk","Increase safety"],"Impairment raises risk.")
H('19.F',3,"Setting limits before a date helps because it does what?",
  "Gives you a plan so you are less pressured in the moment",["Increases pressure","Avoids all dating","Creates confusion"],"Plans support decisions.")
H('19.G',3,"It is wrong to violate another person's boundaries because everyone has the right to what?",
  "Decide what happens to their own body",["Ignore others","Control others","Pressure others"],"Consent matters.")
H('19.G',3,"Pressure to become sexually active can come from what?",
  "Peers, media or a partner",["Only parents","Only teachers","Nowhere"],"Pressure has many sources.")
H('19.H',3,"A teen who experiences sexual harassment should do what?",
  "Report it to a parent or other trusted adult",["Keep it secret","Retaliate","Ignore it"],"Reporting is important.")
H('19.H',3,"Reporting sexual abuse is important because it can do what?",
  "Protect the victim and others from further harm",["Cause trouble","Create blame","Delay help"],"Reporting leads to help.")
H('21.A',3,"One impact of teen pregnancy on a young parent is what?",
  "Greater financial and educational challenges",["Free tuition","Less responsibility","No costs"],"Parenting affects education and finances.")
H('21.A',3,"Raising a child requires large costs such as what?",
  "Health care, childcare and housing",["Free daycare","No expenses","Free housing"],"Costs add up.")
H('21.B',3,"STDs/STIs can be transmitted through what?",
  "Sexual contact, and some through blood or from mother to baby",["Shaking hands","Sharing a desk","Hugging"],"Modes vary by infection.")
H('21.B',3,"Which is NOT a way STIs are spread?",
  "Using the same classroom",["Sexual contact","Contaminated needles","Mother to baby"],"Casual contact does not spread STIs.")
H('21.C',3,"Statistics from the CDC show that STI rates among young people are what?",
  "Higher than among older adults",["Zero","Not tracked","Lower than adults"],"Young people have high rates.")
H('21.C',3,"A reliable source for STI statistics is what?",
  "The Centers for Disease Control and Prevention",["A rumor","A friend","A random site"],"Use credible sources.")
H('21.D',3,"Some STIs, such as HPV and chlamydia, can have what?",
  "No symptoms at all, so testing is important",["Always visible signs","Immediate pain","Obvious signs"],"Many infections are silent.")
H('21.D',3,"HIV attacks the body's what?",
  "Immune system",["Bones","Skin","Hair"],"HIV weakens immunity.")
H('21.E',3,"Early testing for STIs matters because it does what?",
  "Allows early treatment and prevents spread",["Delays care","Causes infection","Is not helpful"],"Early treatment is effective.")
H('21.E',3,"A sexually active person should be screened for STIs how often?",
  "As recommended by a health care provider",["Never","Once as a child","Only if sick"],"Screening depends on risk.")
H('21.F',3,"Emotional risks of sexual activity for school-age teens can include what?",
  "Stress, anxiety and depression",["Guaranteed happiness","No feelings","Less worry"],"Emotions matter.")
H('21.F',3,"Why might a teen feel regret after becoming sexually active too early?",
  "They may not be emotionally ready for the consequences",["It is always positive","It is risk-free","It is simple"],"Readiness matters.")
H('21.G',3,"Abstinence from sexual activity is the only method that is what?",
  "100 percent effective at preventing pregnancy and STIs",["Partly effective","Not effective","Unreliable"],"Abstinence eliminates the risk.")
H('21.G',3,"A benefit of abstinence for teens is that it protects what?",
  "Emotional and physical health",["Nothing","Only grades","Only sports"],"Abstinence reduces risk.")
H('21.H',3,"A teen can build support for abstinence by doing what?",
  "Talking with parents and surrounding themselves with supportive peers",["Isolating","Hiding choices","Ignoring advice"],"Support helps.")
H('21.H',3,"Peer support for healthy choices can be built by doing what?",
  "Joining groups that share the same values",["Avoiding people","Following pressure","Hiding"],"Peers help.")
H('21.I',3,"Contraceptive failure rates in typical use are often higher than in perfect use because of what?",
  "Human error, such as inconsistent or incorrect use",["Perfect behavior","Rare mistakes","Random luck"],"Typical use includes mistakes.")
H('21.I',3,"Abstinence is different from barrier methods because abstinence is what?",
  "The only method that is fully effective",["Less effective","Less certain","The same as barriers"],"Barriers reduce but do not eliminate risk.")
H('21.J',3,"Legal responsibilities of a teen father include what?",
  "Child support and acknowledging paternity",["No duties","Only visiting","Nothing"],"Fathers have legal duties.")
H('21.J',3,"A legal responsibility of both parents of a child is what?",
  "Providing financial and emotional support",["Avoiding responsibility","Hiding the child","Leaving"],"Both parents must support.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_health1.jsonl'))

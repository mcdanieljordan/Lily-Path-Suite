import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('127.', 1128, own='cte_51.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 294 Practicum (short) ----
H('294.d.1.A',3,"A practicum student must give a supervisor an update on a task. Which approach is clearest?",
  "Give a short spoken summary and follow up with a written note",["Mumble and hope the supervisor understands","Send only an emoji","Wait until the supervisor asks"],
  "Combining clear speaking with a written record communicates effectively.")
H('294.d.1.A',4,"Which written message to a work-site mentor is most professional?",
  "A brief email with a greeting, the request, and a thank-you",["A text of all capital letters","A message with slang and no greeting","A long message with no clear request"],
  "Professional writing is clear, polite, and purposeful.")
H('294.d.2.A',3,"Why should a practicum student review the course requirements before the work experience begins?",
  "To connect on-the-job tasks to what the course expects them to learn",["To avoid doing any assigned tasks","To skip the evaluation","To pick a different course"],
  "Knowing the requirements guides what to practice and document.")
H('294.d.2.A',4,"A student notices a work-site task is unrelated to the course goals. The best next step is to:",
  "Ask the teacher and supervisor how to align the tasks with the course",["Quietly ignore the course goals","Quit the placement","Do only the unrelated task"],
  "Alignment keeps the experience useful for the course.")
H('294.d.2.B',3,"Mastering a hands-on skill to an industry standard means performing it:",
  "Accurately and safely the way professionals in the field do",["Quickly but carelessly","Only once","Differently each time"],
  "Industry standards define accuracy, safety, and quality.")
H('294.d.2.B',4,"Which habit best builds mastery of a technical skill during a practicum?",
  "Repeated supervised practice with feedback",["Watching without trying","Practicing only when convenient","Skipping directions"],
  "Practice plus feedback builds mastery.")
H('294.d.2.C',3,"An industry-recognized credential shows that a student has:",
  "Met a standard set by the industry for a skill",["Finished a school dance","Joined a club","Paid a parking fee"],
  "Credentials document verified skills.")
H('294.d.2.C',4,"A student earning a certification while in a practicum should keep:",
  "Records of tests passed and hours worked",["Only a guess of the date","Nothing, since employers ignore it","Only a nickname"],
  "Documentation proves progress toward the credential.")

# ---- 295 Professional Communications / Career prep ----
H('295.d.1.A',3,"Which step best helps a student assess their own marketability to employers?",
  "List skills, training, and experience and compare them to job postings",["Wait for an offer before reviewing","Copy a friend's list","Guess based on mood"],
  "Comparing strengths to job needs shows marketability.")
H('295.d.1.A',4,"A student finds that postings often ask for a certification the student lacks. The most useful response is to:",
  "Plan how to earn that certification",["Ignore the postings","Lie on the application","Stop job searching"],
  "Closing a skill gap raises marketability.")
H('295.d.1.C',3,"Which outfit and attitude best fit a job interview for an office position?",
  "Clean, neat business attire and a positive attitude",["Wrinkled shirt and a bored look","Beachwear and loud talk","Costume clothes"],
  "Professional dress and attitude create a good first impression.")
H('295.d.1.C',4,"During an interview, which behavior best shows professionalism?",
  "A firm handshake, eye contact, and a prompt arrival",["Checking a phone during questions","Arriving late with an excuse","Interrupting the interviewer"],
  "These behaviors show respect and reliability.")
H('295.d.1.D',3,"At a mock interview, you are asked to describe a strength. Your best answer includes:",
  "A specific strength with a short example",["A joke instead of an answer","Only the word 'nothing'","A complaint about a past boss"],
  "Specific examples make answers credible.")
H('295.d.1.D',4,"After being asked a question you did not expect, an interviewee should:",
  "Pause, think, and give an honest, organized answer",["Freeze and say nothing","Change the subject","Make up facts"],
  "Composed, honest answers show good interview technique.")
H('295.d.1.F',3,"Which skill most helps an employee advance to a higher position?",
  "Taking initiative and continuing to learn",["Avoiding new tasks","Waiting to be told everything","Skipping training"],
  "Initiative and learning support promotion.")
H('295.d.1.F',4,"An employee wants a promotion in a year. The best plan is to:",
  "Set goals, gain needed skills, and ask for feedback",["Hope someone notices","Complain about the manager","Do the minimum"],
  "Planned growth supports advancement.")
H('295.d.1.G',3,"Two job offers pay the same. One adds health insurance. When comparing, you should:",
  "Weigh salary together with benefits",["Look only at the job title","Ignore benefits","Pick by coin flip"],
  "Total compensation includes benefits.")
H('295.d.1.G',4,"Which factor is a benefit rather than a salary item?",
  "Paid vacation days",["Hourly wage","Annual pay rate","Overtime pay"],
  "Paid time off is a benefit.")
H('295.d.1.H',3,"Which of these is an intangible reward of work?",
  "Pride in doing a job well",["A paycheck","A bonus check","A gift card"],
  "Intangible rewards are non-monetary feelings and experiences.")
H('295.d.1.H',4,"A student ranks pay as the most important reward and a friendly team second. These rankings show:",
  "Personal priorities for choosing a job",["The only right answer for all workers","A mistake in thinking","A legal requirement"],
  "Ranking rewards clarifies what matters to you.")
H('295.d.1.I',3,"Which source is a common way to find job openings?",
  "An online job board",["A random phone number","A weather report","A grocery list"],
  "Job boards list current openings.")
H('295.d.1.I',4,"After finding an opening, the next job search procedure is usually to:",
  "Follow the posted instructions to apply by the deadline",["Wait for the company to call","Show up uninvited at night","Send a blank form"],
  "Following instructions and deadlines is essential.")
H('295.d.1.B.i',3,"A letter of application should be addressed to:",
  "The person or department named in the job posting",["Nobody in particular","A random executive","The mailroom only"],
  "Addressing the right contact shows attention to detail.")
H('295.d.1.B.i',4,"The best opening for an application letter is one that:",
  "States the position you are applying for and why you fit",["Tells a long life story","Complains about unemployment","Asks for a raise"],
  "A clear purpose and fit set the tone.")
H('295.d.1.B.ii',3,"A good resume is usually:",
  "Brief, accurate, and free of spelling errors",["Many pages of every hobby","Handwritten on scrap paper","Full of exaggerated claims"],
  "Concise, correct resumes make a strong impression.")
H('295.d.1.B.ii',4,"Which item typically belongs on a resume?",
  "Work experience and relevant skills",["Your favorite color","A list of your complaints","Your lunch order"],
  "A resume highlights qualifications.")
H('295.d.1.B.iii',3,"Networking for a job search means:",
  "Building contacts who may share job leads and advice",["Only posting memes","Avoiding people","Waiting alone"],
  "Networking creates helpful professional connections.")
H('295.d.1.B.iii',4,"Which action is an effective networking technique?",
  "Asking a family friend in the field for an informational chat",["Sending identical spam to strangers","Ignoring everyone you know","Demanding a job at once"],
  "Respectful outreach builds relationships.")
H('295.d.1.B.iv',3,"When completing a job application form, you should:",
  "Fill in every section accurately and neatly",["Leave blanks to save time","Guess the dates","Write in pencil only"],
  "Accurate, complete applications are taken seriously.")
H('295.d.1.B.iv',4,"A job application asks for references. You should:",
  "Ask people for permission before listing them",["List strangers","List celebrities","Make up names"],
  "References should agree to speak for you.")
H('295.d.1.E.i',3,"After an interview, which follow-up shows good etiquette?",
  "A short thank-you note within a day or two",["Silence for months","Calling ten times a day","Complaining on social media"],
  "A prompt thank-you shows courtesy.")
H('295.d.1.E.i',4,"A thank-you letter after an interview should:",
  "Thank the interviewer and restate your interest in the job",["Ask what the company pays","Criticize other candidates","Be left unsigned"],
  "It reinforces enthusiasm and professionalism.")
H('295.d.1.E.ii',3,"If you are offered a job you do not want, the polite response is to:",
  "Write a letter declining the offer with thanks",["Ignore the offer","Insult the employer","Show up anyway"],
  "A courteous decline keeps relationships positive.")
H('295.d.1.E.ii',4,"A letter accepting a job should confirm:",
  "The position, the start date, and your thanks",["Your complaints","Nothing specific","Another job offer"],
  "Acceptance letters confirm key terms politely.")
H('295.d.2.A',3,"Employee handbooks are used to explain:",
  "Workplace policies and procedures",["The weather","Local sports","Vacation destinations"],
  "Handbooks state rules employees must follow.")
H('295.d.2.A',4,"An employee sees a safety policy that seems inconvenient. The best response is to:",
  "Follow it and raise concerns through proper channels",["Ignore it quietly","Tell coworkers to ignore it","Break it when the boss is away"],
  "Policies are followed while concerns go through the right route.")
H('295.d.2.B',3,"Punctuality at work means:",
  "Arriving and returning from breaks on time",["Arriving whenever convenient","Leaving early without notice","Taking long breaks"],
  "Being on time shows reliability.")
H('295.d.2.B',4,"Which statement shows a positive work attitude?",
  "'I'll help with that task.'",["'That's not my job.'","'I don't care.'","'Someone else will do it.'"],
  "Willingness to help shows a positive attitude.")
H('295.d.2.C',3,"An employee finds an extra $20 in the cash drawer that is not recorded. The ethical action is to:",
  "Report it to a supervisor",["Keep it","Split it with a coworker","Hide it"],
  "Honesty requires reporting the difference.")
H('295.d.2.C',4,"A coworker asks you to clock them in when they are not there. Ethical reasoning says you should:",
  "Refuse because it is dishonest",["Do it as a favor","Do it once","Do it if they pay you"],
  "Falsifying time records is dishonest.")
H('295.d.2.D',3,"Producing quality work means:",
  "Checking your work and fixing errors before turning it in",["Rushing to finish first","Leaving it to someone else","Skipping directions"],
  "Quality comes from careful checking.")
H('295.d.2.D',4,"Why do employers value high standards for products and services?",
  "They keep customers satisfied and reduce rework",["They make work slower on purpose","They increase errors","They discourage customers"],
  "Quality reduces waste and builds trust.")
H('295.d.3.A',3,"Which choice shows good grooming and hygiene for work?",
  "Clean clothes and neat hair that follow dress policy",["Strong perfume that bothers others","Stained clothing","Ignoring the dress code"],
  "Grooming reflects professionalism.")
H('295.d.3.A',4,"Why do many workplaces have a dress code?",
  "To present a professional image and meet safety needs",["To limit friendships","To raise stress","To lower pay"],
  "Dress codes support image and safety.")
H('295.d.3.B',3,"An employee gets constructive criticism. The best response is to:",
  "Listen, ask questions, and use the advice",["Argue immediately","Walk away","Blame others"],
  "Accepting feedback supports growth.")
H('295.d.3.B',4,"Which habit shows productive work habits?",
  "Staying on task and finishing assignments",["Texting during shifts","Daydreaming","Waiting to be reminded"],
  "Focus and follow-through are productive habits.")
H('295.d.3.C',3,"Prioritizing work means:",
  "Doing the most important or urgent tasks first",["Doing the easiest tasks only","Doing nothing","Doing tasks in random order"],
  "Priorities guide the order of tasks.")
H('295.d.3.C',4,"You have three tasks: one due today, one due Friday, one with no deadline. Best order:",
  "Today's task, Friday's task, then the open task",["The open task first","Friday's task first","None until asked"],
  "Deadlines set the priority order.")
H('295.d.4.A',3,"Which quality is a professional quality in the workplace?",
  "Loyalty to the organization",["Gossiping","Careless attitude","Taking credit for others' work"],
  "Loyalty and positivity are professional qualities.")
H('295.d.4.A',4,"A professional who is dependable can be counted on to:",
  "Do what they promised, on time",["Make excuses","Forget tasks","Blame others"],
  "Dependability means keeping commitments.")
H('295.d.4.B',3,"Which skill helps keep strong relationships with coworkers?",
  "Listening and showing respect",["Interrupting","Teasing","Ignoring them"],
  "Respect and listening build relationships.")
H('295.d.4.B',4,"A coworker is struggling with a task and you finish yours early. A relationship-building move is to:",
  "Offer help if appropriate",["Say nothing","Mock them","Take their task silently"],
  "Offering help builds trust.")
H('295.d.4.C',3,"Respecting different workplace cultures means:",
  "Treating all people and customs with courtesy",["Making fun of unfamiliar customs","Only talking to similar people","Ignoring differences"],
  "Respect supports a good workplace.")
H('295.d.4.C',4,"A new coworker follows a holiday you do not. A respectful response is to:",
  "Ask politely and learn about it",["Laugh at it","Refuse to work with them","Stay silent forever"],
  "Curiosity and respect help teams.")
H('295.d.4.D',3,"Sexual harassment in the workplace is:",
  "Unwelcome behavior of a sexual nature that employees have the right to report",["Always a joke","Allowed if the boss does it","Not covered by any law"],
  "Employees have rights and employers have duties.")
H('295.d.4.D',4,"An employee who experiences harassment should first:",
  "Report it following the company's procedure",["Quit without telling anyone","Retaliate","Post about it only"],
  "Using the reporting process protects rights.")
H('295.d.4.E',3,"When a manager points out a mistake, a tactful reply is:",
  "'Thank you, I'll fix that.'",["'It wasn't me!'","'You always do this.'","Silence and a glare"],
  "Tact keeps the conversation productive.")
H('295.d.4.E',4,"You are disappointed because you did not get the shift you requested. The best response is to:",
  "Stay calm and ask how to be considered next time",["Yell at the scheduler","Refuse to work","Gossip about it"],
  "Calm requests handle disappointment professionally.")
H('295.d.4.F',3,"Confidentiality at work means:",
  "Not sharing private information about the company or customers",["Telling everyone secrets","Posting client data online","Selling customer lists"],
  "Private information must be protected.")
H('295.d.4.F',4,"Integrity at work is shown by:",
  "Doing the right thing even when no one is watching",["Following rules only when watched","Lying to avoid blame","Cutting corners"],
  "Integrity is consistent honesty.")
H('295.d.4.G',3,"Which action improves customer satisfaction?",
  "Greeting customers politely and solving their problems",["Ignoring complaints","Arguing with customers","Making them wait without explanation"],
  "Courtesy and problem-solving please customers.")
H('295.d.4.G',4,"A customer's order is wrong. The best employee response is to:",
  "Apologize and correct it promptly",["Blame the customer","Tell them to leave","Ignore the error"],
  "A prompt fix keeps customers loyal.")
H('295.d.5.A',3,"Which trait of a leader builds trust?",
  "Honesty",["Secrecy about everything","Favoritism","Blaming the team"],
  "Trust is built on honesty and integrity.")
H('295.d.5.A',4,"A leader who admits a mistake and corrects it shows:",
  "Integrity and accountability",["Weakness only","Carelessness","A lack of interest"],
  "Owning mistakes builds trust.")
H('295.d.5.B',3,"Which behavior shows teamwork?",
  "Sharing information so the group can finish together",["Keeping tools to yourself","Working only on your own","Refusing to listen"],
  "Cooperation helps the whole team.")
H('295.d.5.B',4,"In a team project, one member finishes early. Good teamwork is to:",
  "Ask if anyone needs help",["Leave quietly","Brag","Redo others' work"],
  "Supporting teammates strengthens the group.")
H('295.d.5.C',3,"Consensus in a team means:",
  "The group reaches an agreement everyone can support",["The loudest person decides","A coin flip decides","The boss decides without input"],
  "Consensus is shared agreement.")
H('295.d.5.C',4,"Which activity promotes team building?",
  "A group problem-solving exercise",["A solo test","Silent work in separate rooms","A contest where one wins everything"],
  "Joint challenges strengthen bonds.")
H('295.d.5.D',3,"Taking responsibility for shared work means:",
  "Completing your part and meeting group deadlines",["Letting others do it","Taking credit for all of it","Skipping meetings"],
  "Each member must deliver their part.")
H('295.d.5.D',4,"A group assignment is late because you did not finish your section. You should:",
  "Admit it and work with the group to fix it",["Blame the others","Deny it","Disappear"],
  "Accountability protects the team.")
H('295.d.5.E.i',3,"Showing respect toward coworkers includes:",
  "Using polite language and valuing their ideas",["Interrupting","Name-calling","Ignoring ideas"],
  "Respect builds working relationships.")
H('295.d.5.E.i',4,"Which message shows respect in a disagreement?",
  "'I see it differently; may I explain?'",["'That's a stupid idea.'","'You never listen.'","'Whatever.'"],
  "Respectful phrasing keeps discussion open.")
H('295.d.5.E.ii',3,"Which statement is positive communication?",
  "'Thanks for your help on that.'",["'You messed up again.'","'Not my problem.'","'Figure it out.'"],
  "Positive communication encourages cooperation.")
H('295.d.5.E.ii',4,"A coworker made a small mistake. A positive way to say it is:",
  "'Let's fix this together.'",["'Look what you did!'","'I told you so.'","'You're hopeless.'"],
  "Constructive language focuses on solutions.")
H('295.d.5.E.iii',3,"Negotiating a solution means:",
  "Working out a compromise that satisfies both sides",["Demanding your way","Giving in completely","Refusing to talk"],
  "Negotiation seeks a fair compromise.")
H('295.d.5.E.iii',4,"Two coworkers want the same break time. A fair negotiation might be to:",
  "Trade times and alternate days",["Argue until one quits","Flip tables","Report each other"],
  "Compromise resolves conflicts fairly.")
H('295.d.5.E.iv',3,"Demonstrating dependability includes:",
  "Following through on commitments",["Making excuses","Missing deadlines","Avoiding responsibility"],
  "Dependable people can be counted on.")
H('295.d.5.E.iv',4,"A dependable employee who is going to be absent should:",
  "Notify the supervisor as early as possible",["Not come and say nothing","Send a friend with no message","Call after the shift"],
  "Early notice lets the team plan.")
H('295.d.6.A',3,"When taking a phone message, you should record the caller's name, number, and:",
  "The message and the date and time",["Your opinion of the caller","Nothing else","A joke"],
  "Complete messages are useful and accurate.")
H('295.d.6.A',4,"Why should a recorded message be legible?",
  "So the person receiving it can read it correctly",["To impress the caller","To use more paper","To hide the content"],
  "Legibility prevents errors.")
H('295.d.6.B',3,"A message is for the sales department. You should:",
  "Deliver it to the sales department promptly",["Keep it on your desk","Throw it away","Give it to anyone"],
  "Messages go to the right person quickly.")
H('295.d.6.B',4,"You do not know who should receive a call. The best step is to:",
  "Ask a supervisor or check the directory",["Hang up","Guess and transfer randomly","Tell the caller to call back later"],
  "Finding the right contact helps the caller.")
H('295.d.6.C',3,"Coordinating arrangements for participants in a conference call includes:",
  "Confirming times and sending the dial-in information",["Telling no one","Sending the wrong date","Cancelling without notice"],
  "Participants need correct details.")
H('295.d.6.C',4,"Before a video meeting, a coordinator should:",
  "Test the connection and share an agenda",["Join late","Skip invitations","Mute the speaker"],
  "Preparation helps the meeting run well.")
H('295.d.6.D',3,"Calling procedures usually require you to:",
  "Identify yourself and the company at the start of a call",["Hang up if a call is long","Answer with slang","Give out private passwords"],
  "Standard greetings sound professional.")
H('295.d.6.D',4,"Before joining a conference line, you often need to:",
  "Enter the correct meeting ID or login",["Guess a code","Skip the login","Use someone else's account"],
  "Login steps secure the meeting.")
H('295.d.6.E',3,"If the call audio is not working, the first thing to try is to:",
  "Check the volume, microphone, and connection",["Cancel the meeting","Shout","Throw the phone"],
  "Basic checks fix many problems.")
H('295.d.6.E',4,"A call keeps dropping. A good troubleshooting step is to:",
  "Move to a stronger network or call back",["Ignore it","Blame the caller","Delete the account"],
  "Fix the likely cause first.")
H('295.d.7.A',3,"An acceptable use policy tells employees:",
  "How company technology may and may not be used",["The weather forecast","What to eat","How to dress for sports"],
  "It sets rules for technology.")
H('295.d.7.A',4,"Which action breaks a technology security policy?",
  "Sharing your password with a coworker",["Locking your screen","Updating software","Logging out"],
  "Passwords should never be shared.")
H('295.d.7.B',3,"A good ergonomic habit when using a computer is to:",
  "Sit with your back supported and the screen at eye level",["Slouch for hours","Place the screen on the floor","Type with your wrists bent up"],
  "Ergonomics prevents strain.")
H('295.d.7.B',4,"Taking short breaks from a screen helps prevent:",
  "Eye strain and muscle fatigue",["Spelling errors","Software updates","Internet outages"],
  "Breaks reduce physical strain.")
H('295.d.7.C',3,"Computer crime includes:",
  "Hacking into a system without permission",["Typing a report","Saving a file","Printing a page"],
  "Unauthorized access is a crime.")
H('295.d.7.C',4,"Using someone else's credit card number found online is:",
  "Fraud, which is illegal",["Legal if small","A harmless prank","A way to test security"],
  "Using stolen numbers is fraud.")
H('295.d.7.D',3,"After a power outage, you should restart a computer by:",
  "Following the organization's recovery steps",["Tapping the keys randomly","Unplugging all cords","Opening a hammer"],
  "Recovery steps prevent data loss.")
H('295.d.7.D',4,"If a system crashes while you work, the first thing to check later is:",
  "Whether your most recent work was saved or recovered",["Whether the monitor is blue","The weather","Your lunch"],
  "Recovering unsaved work matters.")
H('295.d.7.E',3,"To protect data integrity, an employee should:",
  "Back up files regularly",["Share one account","Delete the original","Ignore errors"],
  "Backups prevent loss.")
H('295.d.7.E',4,"Which practice helps prevent accidental changes to important records?",
  "Limiting who can edit them",["Letting everyone edit","Leaving files unprotected","Removing the backup"],
  "Access controls protect integrity.")
H('295.d.7.F',3,"Using work computers for personal shopping during work hours usually:",
  "Violates technology use policy",["Is always allowed","Raises productivity","Is required"],
  "Policies limit personal use.")
H('295.d.7.F',4,"Before installing new software on a work computer, you should:",
  "Get approval under company policy",["Install anything you like","Disable security","Ignore the IT team"],
  "Unapproved software can threaten security.")
H('295.d.8.A',3,"For an advanced web search, a good way to narrow results is to:",
  "Use specific keywords and quotation marks for exact phrases",["Type one vague word","Click the first ad","Search only images"],
  "Specific searches yield better results.")
H('295.d.8.A',4,"A source for research is most reliable when it is:",
  "From an established, credible organization",["An anonymous post","A rumor","A joke site"],
  "Credibility matters for research.")
H('295.d.8.C',3,"A presentation slide is easiest to read when it has:",
  "Short bullet points and clear fonts",["Long paragraphs","Tiny text","Clashing colors"],
  "Simple slides communicate better.")
H('295.d.8.C',4,"Which feature of presentation software helps show how data changes over time?",
  "A chart",["A random clip","A blank slide","A border"],
  "Charts display trends.")
H('295.d.8.E',3,"In a database, a record is:",
  "A set of related fields about one item",["A single letter","A password","A printer"],
  "Records group related information.")
H('295.d.8.E',4,"A query in a database is used to:",
  "Find specific information that matches criteria",["Erase everything","Change the screen color","Print blank pages"],
  "Queries retrieve matching data.")
H('295.d.8.G',3,"To enter data without error, a worker should:",
  "Double-check entries against the source",["Type as fast as possible","Skip proofreading","Guess numbers"],
  "Verification prevents mistakes.")
H('295.d.8.G',4,"Transposing two digits in a number is an example of:",
  "A data-entry error",["A formatting choice","A filing system","A software update"],
  "Reversing digits creates errors.")
H('295.d.8.B.i',3,"Customary business letter formats include:",
  "Block style, with all lines starting at the left margin",["Poetry layout","Random alignment","Diagonal text"],
  "Business formats are standard.")
H('295.d.8.B.i',4,"The parts of a standard business letter include the date, inside address, salutation, and:",
  "Closing and signature",["A drawing","A joke","A slogan"],
  "A letter ends with a closing and signature.")
H('295.d.8.B.ii',3,"Keyboarding technique that improves accuracy includes:",
  "Keeping fingers on the home row",["Looking only at the keys","Using one finger","Pounding the keys"],
  "Home row position improves speed and accuracy.")
H('295.d.8.B.ii',4,"Using correct keyboarding technique also helps prevent:",
  "Repetitive strain injuries",["Power outages","Spam","Slow internet"],
  "Good posture and technique reduce strain.")
H('295.d.8.B.iii',3,"Basic writing principles for business documents emphasize being:",
  "Clear, concise, and correct",["Wordy and vague","Funny only","Emotional"],
  "Clarity and brevity serve readers.")
H('295.d.8.B.iii',4,"Which sentence is more concise?",
  "Please send the report by Friday.",["I was wondering if it might be possible for you to maybe send the report at some point around Friday.","Send it whenever you feel like it, if possible, perhaps.","As per the aforementioned, kindly forward it."],
  "Direct writing is concise.")
H('295.d.8.B.iv',3,"Proofreading a document before sending it helps catch:",
  "Grammar and spelling mistakes",["Weather changes","Power failures","Meeting times"],
  "Proofreading improves accuracy.")
H('295.d.8.B.iv',4,"Which sentence uses correct grammar?",
  "The team finished its report on time.",["The team finish it's report on time.","The team finished there report on time.","The team finished its reports on times."],
  "Correct word forms matter in business writing.")
H('295.d.8.B.v',3,"Citing references in a report shows:",
  "Where the information came from",["That you copied","That you were rushed","That you are unsure"],
  "Citations give credit to sources.")
H('295.d.8.B.v',4,"A footnote in a document is used to:",
  "Give a source or extra note at the bottom of the page",["Hide the title","Change the font","Delete text"],
  "Footnotes supply sources and notes.")
H('295.d.8.D.i',3,"In a spreadsheet, labels are:",
  "Text that describes the data",["Only numbers","Formulas","Images"],
  "Labels identify rows and columns.")
H('295.d.8.D.i',4,"The intersection of a row and a column in a spreadsheet is called a:",
  "Cell",["Slide","Folder","Field name"],
  "A cell is where a row meets a column.")
H('295.d.8.D.ii',3,"Formatting numbers as currency in a spreadsheet will:",
  "Show a dollar sign and decimal places",["Delete the numbers","Round to zero","Change them to words"],
  "Currency format displays money values.")
H('295.d.8.D.ii',4,"Adjusting column width helps to:",
  "Make entries fully visible",["Delete data","Add formulas","Sort rows"],
  "Wider columns display all content.")
H('295.d.8.D.iii',3,"A chart made from spreadsheet data helps readers:",
  "See patterns and comparisons quickly",["Ignore the numbers","Guess the formulas","Print slower"],
  "Charts make data easier to interpret.")
H('295.d.8.D.iv',3,"In most spreadsheets, a formula begins with:",
  "An equal sign",["A question mark","A period","A dollar sign only"],
  "Formulas start with =.")
H('295.d.8.D.iv',4,"To add the values in cells A1 through A5, you could enter:",
  "=SUM(A1:A5)",["=ADD(A1 A5)","SUM A1 to A5","=TOTAL OF A"],
  "SUM with a range adds the cells.")
H('295.d.8.D.v',3,"To verify a spreadsheet formula, you can:",
  "Check the result by hand with sample numbers",["Trust it blindly","Delete it","Change the font"],
  "Manual checks confirm accuracy.")
H('295.d.8.D.v',4,"A spreadsheet total looks too high. The first thing to check is:",
  "Whether the formula range includes the right cells",["The computer's color","The printer","The keyboard brand"],
  "Wrong ranges cause incorrect totals.")
H('295.d.8.F.i',3,"Electronic scheduling helps ensure:",
  "On-time, productive meetings",["More confusion","Longer meetings","Fewer reminders"],
  "Scheduling tools coordinate time.")
H('295.d.8.F.i',4,"To schedule a meeting electronically, you should send an invitation with the:",
  "Date, time, and place or link",["Weather","Lunch order","Nickname only"],
  "Invitations contain meeting details.")
H('295.d.8.F.ii',3,"A calendar reminder before an appointment is helpful because it:",
  "Prompts you to be ready on time",["Cancels the meeting","Deletes the entry","Hides the date"],
  "Reminders prevent missed events.")
H('295.d.8.F.ii',4,"If two meetings are booked at the same time, you should:",
  "Reschedule one and notify attendees",["Ignore both","Attend neither without notice","Hope no one notices"],
  "Conflicts must be resolved and communicated.")
H('295.d.8.F.iii',3,"Sharing a calendar with coworkers lets them:",
  "See when you are available",["Edit your passwords","Read private emails","Change your pay"],
  "Shared calendars help planning.")
H('295.d.8.F.iii',4,"Marking an entry as private on a shared calendar will:",
  "Hide its details from others",["Delete it","Move it a day","Send it to your boss"],
  "Privacy settings protect details.")
H('295.d.8.F.iv',3,"A recurring event is one that:",
  "Repeats on a regular schedule",["Happens once","Is deleted","Is private"],
  "Recurring events repeat.")
H('295.d.8.F.iv',4,"A weekly staff meeting is best entered as:",
  "A recurring event",["Fifty separate manual entries","A note in the margin","A sticky note only"],
  "Recurrence saves time.")
H('295.d.8.F.v',3,"Time zones matter when scheduling:",
  "A call with people in different parts of the country",["A meeting in one room","A solo task","A file save"],
  "Different zones shift meeting times.")
H('295.d.8.F.v',4,"A 2 p.m. Central time meeting is what time in Eastern time?",
  "3 p.m.",["1 p.m.","2 p.m.","4 p.m."],
  "Eastern is one hour ahead of Central.")
H('295.d.8.F.vi',3,"An electronic task list helps by:",
  "Tracking what is due and when",["Hiding deadlines","Deleting tasks","Increasing confusion"],
  "Task lists organize deadlines.")
H('295.d.8.F.vi',4,"After completing a task on your electronic list, you should:",
  "Mark it complete",["Leave it open","Delete the whole list","Change the due date"],
  "Updating status keeps the list accurate.")
H('295.d.9.A',3,"A personal budget compares your:",
  "Income and expenses",["Height and weight","Grades and sports","Rent and weather"],
  "A budget plans money in and out.")
H('295.d.9.A',4,"Monthly income is $2,000 and planned spending is $1,700. The amount available for savings is:",
  "$300",["$200","$3,700","$400"],
  "2,000 − 1,700 = 300.")
H('295.d.9.B',3,"On a pay stub, net pay is the amount:",
  "After deductions are taken out",["Before deductions","Of your tax rate","Of your boss's pay"],
  "Net pay is take-home pay.")
H('295.d.9.B',4,"Gross pay is $500 and deductions are $85. Net pay is:",
  "$415",["$585","$425","$385"],
  "500 − 85 = 415.")
H('295.d.9.C',3,"Reconciling a bank statement means:",
  "Comparing it with your own records",["Throwing it away","Closing the account","Adding random deposits"],
  "Reconciliation finds differences.")
H('295.d.9.C',4,"A check you wrote has not yet cleared. On reconciling, it is:",
  "An outstanding check that explains a difference",["A bank error always","A deposit","Fraud automatically"],
  "Outstanding items cause temporary differences.")
H('295.d.9.D',3,"Keeping receipts and statements organized helps you:",
  "Prove expenses and prepare taxes",["Spend more","Avoid saving","Lose records"],
  "Records support taxes and budgeting.")
H('295.d.9.D',4,"How long should important financial records such as tax returns be kept?",
  "Several years, as recommended",["One day","Never","Until the next meal"],
  "Records may be needed later for audits.")
H('295.d.9.E',3,"A wise use of credit is to:",
  "Pay the balance on time and in full when possible",["Pay only the minimum for years","Max out the card","Ignore due dates"],
  "Paying on time avoids interest and fees.")
H('295.d.9.E',4,"Making only minimum payments on a credit card usually causes:",
  "Higher total interest paid",["Lower interest","No interest","A free upgrade"],
  "Balances left unpaid accrue interest.")
H('295.d.9.F',3,"A credit report is used to:",
  "Show a person's borrowing and repayment history",["Show a person's age only","Show favorite stores","Show test scores"],
  "Credit reports record credit behavior.")
H('295.d.9.F',4,"To validate your credit history, you should:",
  "Review your credit report for errors",["Never look at it","Share it online","Ignore errors"],
  "Reviewing reports finds mistakes.")
H('295.d.9.G',3,"Which action helps protect against identity theft?",
  "Shredding documents that contain personal information",["Posting your Social Security number","Sharing passwords","Leaving mail in a pile outside"],
  "Disposing of data safely protects identity.")
H('295.d.9.G',4,"An unexpected email asks for your bank login. You should:",
  "Delete it without responding",["Reply with the login","Click every link","Forward it to friends"],
  "This is a phishing attempt.")
H('295.d.9.H',3,"Income tax forms are generally filed:",
  "Each year by the deadline",["Every hour","Once in a lifetime","Never"],
  "Taxes are filed annually.")
H('295.d.9.H',4,"A W-2 form shows an employee's:",
  "Yearly wages and taxes withheld",["Vacation days","Favorite tasks","School grades"],
  "The W-2 reports earnings and withholding.")
H('295.d.10.A',3,"When determining equipment needed for an office task, you should first:",
  "List the tasks to be done",["Buy random items","Wait for a failure","Ask nobody"],
  "Tasks determine needs.")
H('295.d.10.A',4,"A team will hold video meetings. Which equipment is needed?",
  "A camera and microphone",["A stapler only","A fax machine only","A paper shredder only"],
  "Video meetings require a camera and a microphone.")
H('295.d.10.B',3,"Printer paper and ink are examples of:",
  "Supplies",["Equipment","Furniture","Software"],
  "Consumables are supplies.")
H('295.d.10.B',4,"To avoid running out of supplies, an office should:",
  "Track usage and reorder before stock is gone",["Never reorder","Order only when empty","Hide the supplies"],
  "Tracking prevents shortages.")
H('295.d.10.C',3,"A maintenance system for equipment includes:",
  "A regular inspection and service log",["No records","Random repairs","A single check ever"],
  "Systems track upkeep.")
H('295.d.10.C',4,"Why keep a maintenance log?",
  "To show when equipment was last serviced",["To impress visitors","To waste time","To hide problems"],
  "Logs show service history.")
H('295.d.10.D',3,"Scheduling equipment maintenance helps to:",
  "Prevent unexpected breakdowns",["Cause breakdowns","Raise noise","Remove the equipment"],
  "Planned service reduces failures.")
H('295.d.10.D',4,"The best time to service a busy copier is:",
  "When it is least needed, per a planned schedule",["During the busiest hour","Never","Only after it breaks"],
  "Scheduling avoids disruption.")
H('295.d.10.E',3,"Before cleaning or repairing office equipment, you should:",
  "Follow the manufacturer's instructions",["Guess","Unplug nothing","Use any liquid"],
  "Instructions ensure safe maintenance.")
H('295.d.10.E',4,"If equipment makes an unusual noise, you should:",
  "Report it and follow maintenance procedures",["Ignore it","Hit it","Take it apart secretly"],
  "Reporting helps prevent damage.")
H('295.d.11.A',3,"A creative solution to a problem often starts with:",
  "Listing the parts of the problem and brainstorming",["Giving up","Blaming someone","Waiting for luck"],
  "Analysis and brainstorming produce ideas.")
H('295.d.11.A',4,"Breaking a problem into smaller parts helps because it:",
  "Makes each part easier to analyze and solve",["Hides the problem","Makes it harder","Removes the goal"],
  "Smaller parts are easier to address.")
H('295.d.11.B',3,"Before using information to solve a problem, you should:",
  "Judge whether it is accurate and relevant",["Believe the first thing you read","Use only opinions","Ignore details"],
  "Evaluating information improves decisions.")
H('295.d.11.B',4,"A source that is out of date and unsigned is:",
  "Less valuable for solving the problem",["The best source","Always correct","Official"],
  "Currency and authorship affect value.")
H('295.d.11.C',3,"Comparing alternatives means:",
  "Weighing the pros and cons of each option",["Choosing at random","Ignoring options","Picking the cheapest only"],
  "Comparison supports good decisions.")
H('295.d.11.C',4,"A decision matrix is a tool for:",
  "Scoring options against criteria",["Drawing maps","Painting walls","Typing faster"],
  "It organizes comparisons.")
H('295.d.11.D',3,"Technical research for a decision may involve:",
  "Reading manuals and checking reliable data",["Guessing","Asking only a stranger","Skipping research"],
  "Research supplies facts.")
H('295.d.11.D',4,"Which is the best first step in technical research?",
  "Define the question you need to answer",["Start typing anywhere","Collect any data","Pick a conclusion"],
  "A clear question focuses research.")

# ---- 296 Practicum in Business Management / Administrative ----
H('296.d.1.A',3,"Which format fits a quick question to a coworker down the hall?",
  "A brief, polite spoken question or short message",["A formal 10-page report","A legal contract","A news broadcast"],
  "Match the format to the purpose.")
H('296.d.1.A',4,"A manager needs to show quarterly sales trends. The best communication tool is:",
  "A chart with a short written summary",["A rumor","A long spoken story","A blank page"],
  "Visual plus written summary communicates data well.")
H('296.d.1.B',3,"Active listening includes:",
  "Eye contact and paraphrasing what was said",["Looking at your phone","Interrupting","Planning your reply only"],
  "Active listening confirms understanding.")
H('296.d.1.B',4,"To clarify unclear instructions, a good question is:",
  "'Do you mean I should send it today or tomorrow?'",["'What?'","'That makes no sense.'","'Whatever you say.'"],
  "Specific clarifying questions prevent mistakes.")
H('296.d.1.C',3,"A good formal presentation has:",
  "A clear opening, main points, and a conclusion",["No structure","Only jokes","Reading every word aloud"],
  "Structure helps the audience follow.")
H('296.d.1.C',4,"Compared with a formal presentation, an informal presentation is usually:",
  "Shorter and less structured, such as a quick team update",["Always longer","Delivered in formal dress","Written only"],
  "Informal presentations are quick and relaxed.")
H('296.d.1.D',3,"Interpreting data before sharing it means:",
  "Explaining what the numbers mean",["Hiding the numbers","Changing them","Printing them smaller"],
  "Interpretation adds meaning to data.")
H('296.d.1.D',4,"A report states that sales rose 12 percent. An effective message adds:",
  "Why sales rose and what it means for next quarter",["Nothing more","A guess about the weather","A complaint"],
  "Context makes data useful.")
H('296.d.1.E',3,"Public relations skills help an organization:",
  "Maintain a positive image with customers and the public",["Avoid all customers","Hide mistakes forever","Close offices"],
  "PR builds goodwill.")
H('296.d.1.E',4,"An employee receives a complaint from a customer on social media. The best step is to:",
  "Respond politely and move the issue to the right channel",["Delete the post","Argue publicly","Ignore it"],
  "Courteous responses protect reputation.")
H('296.d.2.A',3,"Critical thinking in a group means:",
  "Questioning assumptions and weighing evidence",["Going along with everyone","Blaming the group","Skipping evidence"],
  "Critical thinkers evaluate ideas.")
H('296.d.2.A',4,"A teammate proposes a plan with no data to support it. A critical thinker asks:",
  "'What evidence shows this will work?'",["'Who cares?'","'Fine, do whatever.'","'You're wrong.'"],
  "Asking for evidence is critical thinking.")
H('296.d.2.B',3,"A strategy for solving a complex problem is to:",
  "Define it, brainstorm options, test one, and review results",["Guess","Avoid it","Pick the loudest idea"],
  "A process guides problem solving.")
H('296.d.2.B',4,"If your first solution does not work, a strong problem solver will:",
  "Learn from it and try another approach",["Quit","Repeat the same failure","Blame others"],
  "Adapting is part of problem solving.")
H('296.d.2.C',3,"Gathering information from manuals and reliable websites is part of:",
  "Technical research",["Daydreaming","Guesswork","Gossip"],
  "Research informs decisions.")
H('296.d.2.C',4,"A manager needs to decide between two software products. A research step is to:",
  "Compare features, costs, and reviews from credible sources",["Pick the one with the nicer logo","Ask no one","Flip a coin"],
  "Facts support the decision.")
H('296.d.2.D',3,"To develop creative solutions, a team can:",
  "Hold a brainstorming session where all ideas are welcome",["Allow one idea only","Criticize every suggestion","Work separately"],
  "Brainstorming generates ideas.")
H('296.d.2.D',4,"An office has long lines at the front desk. An innovative solution might be:",
  "An online check-in system",["Hiring no one","Closing the desk","Removing the chairs"],
  "Technology can solve workflow problems.")
H('296.d.3.A',3,"Workplace safety rules exist to:",
  "Prevent accidents and injuries",["Slow work down","Spend money","Limit breaks"],
  "Safety rules protect workers.")
H('296.d.3.A',4,"You see a cord across a walkway. The best action is to:",
  "Remove or mark the hazard and report it",["Step over it","Ignore it","Tell no one"],
  "Hazards should be corrected or reported.")
H('296.d.3.B',3,"A strong password for a work account should be:",
  "Long and hard to guess",["Your name","The word 'password'","The same as another account"],
  "Strong passwords resist guessing.")
H('296.d.3.B',4,"Leaving your computer unlocked while you walk away risks:",
  "Unauthorized access to company data",["Faster work","Better security","A software update"],
  "Locking screens prevents access.")
H('296.d.3.C',3,"Regularly saving and backing up files prevents:",
  "Data loss",["Spelling mistakes","Long meetings","Email"],
  "Backups protect data.")
H('296.d.4.A',3,"A positive work ethic is shown by:",
  "Completing assigned tasks with effort and on time",["Doing as little as possible","Complaining","Arriving late"],
  "Effort and reliability show work ethic.")
H('296.d.4.A',4,"A supervisor assigns a boring task. A strong work ethic means:",
  "Doing it well anyway",["Skipping it","Doing it poorly","Delaying it forever"],
  "Work ethic does not depend on task appeal.")
H('296.d.4.B',3,"An ethical responsibility at work is to:",
  "Be honest with customers and coworkers",["Lie to avoid trouble","Take supplies home","Misreport hours"],
  "Honesty is an ethical duty.")
H('296.d.4.B',4,"A legal responsibility of an employee includes:",
  "Following laws that apply to the job",["Ignoring regulations","Breaking safety laws","Falsifying records"],
  "Employees must follow laws.")
H('296.d.4.C',3,"Choosing the ethical course of action when making decisions means:",
  "Doing what is honest and fair even if it is harder",["Doing the easiest thing","Doing what benefits only you","Following the crowd blindly"],
  "Integrity guides choices.")
H('296.d.4.C',4,"A customer overpays by mistake. The ethical choice is to:",
  "Return the extra money",["Keep it","Say nothing","Spend it quickly"],
  "Honesty requires correcting the overpayment.")
H('296.d.4.D',3,"Complying with rules and regulations means:",
  "Following them consistently",["Following them sometimes","Ignoring them","Rewriting them"],
  "Consistency is key.")
H('296.d.4.D',4,"A regulation requires records to be kept for seven years. The company should:",
  "Keep them for at least that long",["Shred them after one year","Lose them","Ignore the rule"],
  "Compliance means following the stated period.")
H('296.d.5.A',3,"In a supervised business experience, a student should:",
  "Document the tasks done and evaluate what was learned",["Hide results","Skip logs","Avoid feedback"],
  "Documenting shows learning.")
H('296.d.5.A',4,"A student completes a task and writes a short reflection on what went well and what to improve. This is:",
  "Evaluating a learning activity",["Wasting time","Cheating","Quitting"],
  "Reflection evaluates learning.")
H('296.d.5.B',3,"Advanced technical skills in business management might include:",
  "Using spreadsheets to analyze budgets",["Only filing paper","Only answering phones","Doing nothing"],
  "Technical skills support business tasks.")
H('296.d.5.B',4,"To grow technical knowledge on a practicum, a student should:",
  "Ask for challenging tasks and training",["Avoid new tasks","Repeat one task only","Refuse instruction"],
  "Stretch tasks build skill.")
H('296.d.5.C',3,"Internal office communication is communication:",
  "Among people inside the organization",["With customers","With the media","With the public"],
  "Internal means within the organization.")
H('296.d.5.C',4,"Which is an example of external office communication?",
  "A letter sent to a vendor",["A memo to your team","A staff meeting","A note to a coworker"],
  "External communication goes outside the organization.")
H('296.d.5.D',3,"Information technology tools such as shared drives help managers to:",
  "Organize and share documents",["Lose files","Block access","Increase paper"],
  "Technology supports document management.")
H('296.d.5.D',4,"A team needs to work on one file at the same time. The best tool is:",
  "A cloud-based collaboration document",["Paper copies","One person's thumb drive","A fax"],
  "Cloud tools allow shared editing.")
H('296.d.5.E',3,"A memorandum is used for:",
  "Short internal communication",["Formal letters to the public","Tax forms","Posters"],
  "Memos are brief internal notes.")
H('296.d.5.E',4,"A business letter is usually written to:",
  "Someone outside the organization",["Coworkers only","Yourself","No one"],
  "Letters are typically external.")
H('296.d.5.F',3,"Electronic scheduling tools help to:",
  "Coordinate meetings and avoid conflicts",["Create conflicts","Hide invitations","Delete events"],
  "They coordinate time.")
H('296.d.5.F',4,"When many people must attend, an electronic scheduling tool can:",
  "Show common available times",["Pick a random time","Cancel the meeting","Hide calendars"],
  "Shared availability speeds scheduling.")
H('296.d.5.G',3,"Growth in technical skill competencies is shown by:",
  "Completing tasks with less help over time",["Needing more help each time","Avoiding tasks","Making more errors"],
  "Independence shows growth.")
H('296.d.5.G',4,"A student tracks skill ratings from September to December. This shows:",
  "Progress over time",["Nothing","Random luck","A tax filing"],
  "Tracking shows growth.")
H('296.d.5.H',3,"Evaluating strengths and weaknesses helps a student:",
  "Decide where to improve",["Feel proud only","Hide mistakes","Skip tasks"],
  "Honest evaluation guides growth.")
H('296.d.5.H',4,"A student is strong at data entry but weak at presentations. A smart plan is to:",
  "Practice presentation skills with feedback",["Avoid presenting","Stop data entry","Do nothing"],
  "Targeting weak areas improves overall skill.")
H('296.d.5.I',3,"A work sample in a portfolio is:",
  "An example of the student's actual work",["A picture from a magazine","A random file","A copy of someone else's work"],
  "Samples show real skills.")
H('296.d.5.I',4,"Which is the best work sample for showing business writing skill?",
  "A well-edited memo you wrote",["A grocery list","A game score","A recipe"],
  "Relevant samples demonstrate skills.")

H('295.d.4.D',4,"Which workplace comment is an example of unwelcome conduct that could be reported as harassment?",
  "Repeated unwanted remarks about a coworker's body",["A request to share meeting notes","A compliment on finished work","A question about the schedule"],
  "Repeated unwanted sexual remarks are harassment.")
H('295.d.8.D.iii',4,"To show each department's share of a total budget, a spreadsheet user would most likely create a:",
  "Pie chart",["Blank worksheet","Footer","Macro-free template"],
  "Pie charts show parts of a whole.")
H('295.d.9.C',3,"A bank statement shows a deposit your records do not. You should:",
  "Find the source and update your records",["Ignore the difference","Close the account","Throw out the statement"],
  "Reconcile by explaining differences.")
H('296.d.1.B',4,"A client explains a request and a worker repeats the key points back to confirm understanding. This is:",
  "Paraphrasing as part of active listening",["Interrupting","Daydreaming","Arguing"],
  "Paraphrasing checks understanding.")
H('296.d.3.C',4,"Which step best protects the integrity of shared company data?",
  "Giving editing access only to people who need it",["Sharing one login","Turning off backups","Leaving records open to all"],
  "Limited access prevents accidental or harmful changes.")
H('296.d.5.H',4,"A practicum student scores low on a self-rating of spreadsheet skills. A reasonable response is to:",
  "Set a goal to practice and ask for feedback",["Hide the score","Stop using spreadsheets","Change the rating without evidence"],
  "Evaluation leads to improvement goals.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_51.jsonl'))

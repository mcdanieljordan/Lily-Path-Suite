import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('127.', 1114, own='cte_37.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---------- 224 Animation I ----------
H('224.d.1.A',3,"An animator pitching a short film to a client keeps her emails free of spelling errors and organizes her ideas clearly. She is applying skills from which subject?",
  "English language arts",["Physical education","Chemistry","Geometry only"],"Clear reading, writing, and speaking are English language arts skills used in every workplace.")
H('224.d.1.A',4,"Which habit shows an animation student consistently using English language arts skills on the job?",
  "Proofreading a script before sending it to a client",["Skipping the script and improvising on set","Sending messages in all capital letters","Using slang in every client email"],"Careful reading and writing keep professional communication clear.")
H('224.d.1.B',3,"An animation studio charges $40 per hour. A freelancer works 6 hours on a short clip. What does she put on the invoice?",
  "$240",["$46","$34","$200"],"40 x 6 = 240.")
H('224.d.1.B',4,"A 12-second animation plays at 24 frames per second. How many frames must be drawn or rendered?",
  "288",["36","144","24"],"12 x 24 = 288 frames.")
H('224.d.2.A',3,"An animator explains a storyboard to a group of kindergarten students. Which choice best adapts the language to the audience?",
  "Simple words and short sentences",["Dense industry jargon","A long technical report","Text full of abbreviations"],"Language should match the audience's age and background.")
H('224.d.2.A',4,"A studio writes a casual text to a coworker and a formal proposal to a client. What are they adjusting?",
  "Structure and style for the situation",["The animation frame rate","The file compression","The monitor brightness"],"Style and structure change with purpose and audience.")
H('224.d.2.B',3,"Before a team meeting, an animator puts her notes in order from most to least important. This is an example of:",
  "organizing information",["erasing information","guessing at facts","hiding information"],"Organizing written and oral information makes it easier to share.")
H('224.d.2.B',4,"Which step comes first when formulating a clear oral explanation of an animation concept?",
  "Decide the main point you want to make",["Read your slides aloud word for word","Start talking and see what happens","Add effects to every slide"],"A clear main point guides how information is arranged.")
H('224.d.2.C',3,"A studio tracks how many people watched each episode and shows the results in a bar graph. This is communicating:",
  "data with a visual",["opinions without proof","rumors","only sound"],"Graphs help people interpret and share data.")
H('224.d.2.C',4,"An animator tells the director that view counts rose 20% after a trailer. What makes this effective?",
  "It communicates data in a clear, specific way",["It uses vague words only","It avoids numbers","It repeats the same point"],"Specific, accurate data communicates results clearly.")
H('224.d.2.D',3,"A student pitches a cartoon idea to classmates using slides and a short demo. This is a:",
  "formal presentation",["private diary entry","blank page","random doodle"],"A planned talk with slides is a formal presentation.")
H('224.d.2.D',4,"Which best describes an informal presentation in an animation class?",
  "Showing a rough clip to a partner and chatting about it",["Delivering a scripted keynote in a theater","Mailing a signed contract","Filing a legal report"],"Informal presentations are relaxed and conversational.")
H('224.d.2.E',3,"A client describes a character change. The animator nods, takes notes, and repeats the request back. These are examples of:",
  "active listening",["interrupting","daydreaming","avoiding eye contact"],"Active listening confirms understanding of what was said.")
H('224.d.2.E',4,"After a client gives vague feedback, which response best clarifies the information?",
  "Ask which scene and what change is wanted",["Say nothing and guess","Redo the whole film","Change the subject"],"Clarifying questions prevent mistakes and rework.")
H('224.d.2.F',3,"An animation team has members from many cultures and backgrounds. A good teammate will:",
  "listen respectfully to each person",["talk over quiet coworkers","ignore different opinions","only work with friends"],"Respecting diverse people improves collaboration.")
H('224.d.2.F',4,"A coworker speaks English as a second language and pauses often. What is a respectful response?",
  "Be patient and speak clearly without rushing them",["Finish all of their sentences","Roll your eyes","Switch to another coworker"],"Patience and clear speech show respect for diverse speakers.")
H('224.d.2.G',3,"A studio replies politely and quickly to a customer who is unhappy with a delivery. This shows:",
  "public relations skills",["poor planning","rendering skills","framing skills"],"Courteous responses protect the studio's reputation.")
H('224.d.2.G',4,"An animation company posts friendly updates about new projects and answers viewer comments. They are building:",
  "a positive public image",["a hidden budget","a secret contract","a lower frame rate"],"Public relations builds goodwill with customers.")
H('224.d.3.A',3,"A team gathers viewer ratings, compares them, and decides which short to expand into a series. This uses:",
  "critical-thinking skills",["guesswork","luck","random choice"],"Gathering and interpreting data supports good decisions.")
H('224.d.3.A',4,"Which action best shows critical thinking when an animation keeps stuttering?",
  "Test possible causes one at a time and compare results",["Restart and hope it fixes itself","Blame the teammate","Delete the project"],"Systematic testing identifies the true cause.")
H('224.d.3.B',3,"Four animators disagree about a scene's look. Which approach helps the group decide?",
  "Share ideas, discuss pros and cons, then agree",["Let the loudest person win","Flip a coin every time","Avoid the topic"],"Interpersonal skills help groups solve problems together.")
H('224.d.3.B',4,"A team uses brainstorming and then votes on the best idea. This is an example of:",
  "group decision making",["working alone","delaying work","ignoring ideas"],"Groups combine ideas and then decide together.")
H('224.d.4.A',3,"Which tool is best for sending a quick written update to a teammate who works in another city?",
  "Email",["A paper airplane","A sketchbook","A tripod"],"Email allows quick written communication at a distance.")
H('224.d.4.A',4,"An animator uses a word processor, email, and the Internet. These are all:",
  "technology applications",["lighting kits","paint brushes","storyboard pins"],"They are software tools that support work tasks.")
H('224.d.4.B',3,"Putting animation files into clearly named folders so they are easy to find is called:",
  "file management",["file deletion","file hiding","file wasting"],"Good file management saves time.")
H('224.d.4.B',4,"Which naming habit makes version tracking easiest for an animation project?",
  "Adding a date or version number to each file name",["Naming every file Final","Using random symbols","Saving everything to the desktop"],"Version numbers show which file is newest.")
H('224.d.5.A',3,"Hand-drawn cels were used in early animation. Today most studios mostly use:",
  "computer-based tools",["only paper cels","only clay","no equipment"],"Animation moved from hand-drawn film to digital production.")
H('224.d.5.A',4,"Which statement best summarizes the evolution of animation?",
  "It moved from hand-drawn frames to digital 2-D and 3-D tools",["It began with 3-D computers","It has not changed","It stopped being made"],"Technology expanded the ways animation is produced.")
H('224.d.5.B',3,"Streaming platforms and short social video are trends that:",
  "give animators new ways to reach viewers",["end all animation careers","remove the need for stories","ban color"],"Industry trends shape where and how animation is seen.")
H('224.d.5.B',4,"Studios now use real-time game engines for some animation. This trend lets teams:",
  "preview scenes instantly while working",["avoid planning","skip sound","delete scripts"],"Real-time rendering speeds up review.")
H('224.d.6.A',3,"Before using a heavy light stand, a student checks that it is stable. This is following:",
  "workplace safety rules",["a style guide","a sales quota","a dress code only"],"Safety rules prevent injuries and damage.")
H('224.d.6.A',4,"Which habit is part of consistently following studio safety regulations?",
  "Keeping cables taped down and walkways clear",["Leaving cables across the floor","Plugging many devices into one outlet","Ignoring posted signs"],"Clear walkways prevent trips and falls.")
H('224.d.6.B',3,"A coworker notices a frayed power cord on a computer. What should they do?",
  "Report it and stop using it",["Keep using it","Tape it quickly and ignore it","Hide it behind a desk"],"Frayed cords are shock and fire hazards.")
H('224.d.6.B',4,"Sitting for hours at a drawing tablet can cause strain. Which step helps resolve this concern?",
  "Take regular breaks and adjust the chair",["Work without any breaks","Raise the screen brightness","Use a smaller desk"],"Ergonomic changes reduce strain injuries.")
H('224.d.6.C',3,"A fire alarm sounds in the studio. What should employees do?",
  "Leave by the posted exit route",["Keep working","Hide in a closet","Record the alarm"],"Following emergency procedures keeps people safe.")
H('224.d.6.C',4,"Why are evacuation maps posted near studio doors?",
  "To show the quickest safe route out",["To decorate the wall","To advertise software","To list holidays"],"Maps support fast, safe exits in an emergency.")
H('224.d.7.A',3,"A lead animator sets a goal, assigns tasks, and checks progress. This shows:",
  "leadership skills",["only artistic skill","avoidance","carelessness"],"Leaders set goals and guide the team to reach them.")
H('224.d.7.A',4,"Which action shows leadership when a project falls behind schedule?",
  "Analyze the problem and adjust tasks with the team",["Blame one animator","Cancel the project quietly","Stop communicating"],"Leaders analyze and respond to obstacles.")
H('224.d.7.B',3,"Two teammates disagree about a character's design. A good teammate will:",
  "listen to both sides and look for a compromise",["refuse to talk","complain to clients","quit the team"],"Conflict management supports collective goals.")
H('224.d.7.B',4,"Which phrase supports teamwork during a disagreement?",
  "Let's list what each of us needs",["That idea is dumb","You never listen","Do it my way"],"Respectful wording keeps teams focused on the goal.")
H('224.d.7.C',3,"Giving a coworker helpful feedback and encouragement builds:",
  "good working relationships",["tension","confusion","distance"],"Constructive support builds trust.")
H('224.d.7.C',4,"Which comment is constructive feedback on a rough animation?",
  "The timing is good; try slowing the jump slightly",["This is awful","I could do better","Why bother"],"Specific, kind feedback helps a coworker improve.")
H('224.d.7.D',3,"Before a production meeting, the animator writes down what the team needs to decide. She is:",
  "preparing goals for the meeting",["avoiding the meeting","wasting time","skipping tasks"],"Preparation makes meetings productive.")
H('224.d.7.D',4,"Which item belongs on a meeting agenda?",
  "Topics, time limits, and desired outcomes",["Gossip","Jokes only","Lunch orders only"],"An agenda keeps a meeting on track.")
H('224.d.7.E',3,"During a work meeting, a good participant will:",
  "stay on topic and take notes",["scroll social media","interrupt others","leave without saying why"],"Focused participation helps accomplish work tasks.")
H('224.d.7.E',4,"After a meeting ends, which step helps ensure tasks get done?",
  "Send notes listing who will do what and by when",["Say nothing","Delete the agenda","Wait a month"],"Written follow-up keeps everyone accountable.")
H('224.d.7.F',3,"An experienced animator teaches a new intern how to use the software. This is:",
  "mentoring",["competing","copying","delaying"],"Mentors teach and inspire others.")
H('224.d.7.F',4,"What makes a good mentor?",
  "Patience and willingness to share knowledge",["Keeping secrets","Criticizing harshly","Avoiding questions"],"Good mentors support growth in others.")
H('224.d.8.A',3,"An animator borrows a color palette from a classmate's work. What is the ethical thing to do?",
  "Give credit to the classmate",["Say it was entirely your idea","Hide the source","Remove their name from the file"],"Ethical conduct includes crediting ideas.")
H('224.d.8.A',4,"Which action best shows ethical conduct in a group animation project?",
  "Listing everyone who contributed in the credits",["Taking credit for the group's work","Leaving collaborators off","Copying a rival's file"],"Proper credit respects each person's contribution.")
H('224.d.8.B',3,"Copyright law protects:",
  "original creative works",["only ideas never written down","public weather facts","blank paper"],"Copyright covers original works fixed in a tangible form.")
H('224.d.8.B',4,"A teacher uses a short clip of a film in class to explain a technique. This may fall under:",
  "fair use",["piracy","trademark loss","free ownership"],"Fair use allows limited use for teaching, with conditions.")
H('224.d.8.C',3,"Before morphing a photograph into a new animation, an artist should:",
  "make sure she has permission or rights to use it",["assume anything online is free","remove the photographer's name","sell it immediately"],"Respecting intellectual property includes getting permission.")
H('224.d.8.C',4,"An animator edits and blends someone else's artwork into a new piece. To respect intellectual property, she should:",
  "obtain permission or use properly licensed material",["claim it as completely her own","crop out the signature","post it without a source"],"Changing a work does not remove the creator's rights.")
H('224.d.8.D',3,"A school's acceptable use policy says students may not install unapproved software. A student should:",
  "follow the policy",["install it anyway","hide it","ask a friend to do it"],"Acceptable use policies set rules for technology.")
H('224.d.8.D',4,"Which is proper etiquette when using a shared studio network?",
  "Avoid downloading huge files that slow others down",["Stream movies all day","Share your password","Change other users' files"],"Etiquette includes thoughtful use of shared resources.")
H('224.d.8.E',3,"Cartoons and animated films can influence what viewers think about topics and people. This shows animation's:",
  "impact on society",["lack of effect","only cost","only color"],"Media influences culture and attitudes.")
H('224.d.8.E',4,"The animation industry affects society by providing entertainment, education, and:",
  "jobs and economic activity",["no income","only losses","less communication"],"The industry employs people and informs audiences.")
H('224.d.9.A',3,"A career portfolio can include:",
  "work samples, a resume, and certificates",["only a lunch menu","a grocery list","unrelated photos"],"A portfolio documents skills and experience.")
H('224.d.9.A',4,"Why should an animation student keep their career portfolio updated?",
  "To show new work and skills to future employers",["To hide past work","To save printing costs","To avoid interviews"],"A current portfolio reflects growth.")
H('224.d.9.B',3,"Two job offers pay differently and offer different benefits. A smart job seeker will:",
  "compare pay, benefits, and growth chances",["pick at random","accept the first one without reading","ignore the details"],"Comparing offers supports a good choice.")
H('224.d.9.B',4,"Which factor should be weighed when evaluating an employment opportunity?",
  "Opportunities for advancement",["The color of the building","The manager's favorite song","The weather forecast"],"Growth potential matters for a career.")
H('224.d.9.C',3,"Attending a career fair to meet industry professionals is an example of:",
  "professional networking",["avoiding work","shopping","gaming"],"Networking builds career connections.")
H('224.d.9.C',4,"Which action helps build a professional network?",
  "Follow up with a thank-you message after meeting someone",["Throw away business cards","Never reply to messages","Avoid industry events"],"Follow-up keeps connections active.")
H('224.d.9.D',3,"Starting your own animation business instead of working for a studio is:",
  "entrepreneurship",["retirement","apprenticeship only","unemployment"],"Entrepreneurs create and run their own businesses.")
H('224.d.9.D',4,"One challenge of being a self-employed animator is:",
  "finding your own clients and managing finances",["receiving a guaranteed paycheck","having no work","never needing contracts"],"Entrepreneurs handle sales and money themselves.")
H('224.d.10.A',3,"Breaking a big animation project into smaller tasks with due dates is:",
  "planning and time management",["procrastination","guessing","avoidance"],"Planning helps complete work on time.")
H('224.d.10.A',4,"Which approach best helps a team meet a deadline?",
  "Set milestones and check progress regularly",["Wait until the last day","Skip planning","Work without a schedule"],"Milestones keep work on track.")
H('224.d.10.B',3,"Using a calendar app to remind you about deadlines is using technology to:",
  "enhance productivity",["delay work","hide tasks","lose files"],"Technology can help organize time.")
H('224.d.10.B',4,"A shared task board lets a team see who is doing what. This improves:",
  "coordination",["confusion","secrecy","cost"],"Visible tasks reduce overlap and missed work.")
H('224.d.11.A',3,"At the first meeting, an animator asks a client what the film is for and who will watch it. She is:",
  "identifying client needs",["selling a product","testing hardware","editing audio"],"Questions reveal what the client wants.")
H('224.d.11.A',4,"Which question best helps determine a client's needs for a short animation?",
  "What message and audience do you have in mind?",["What is your favorite color?","What did you eat today?","Do you like Mondays?"],"Purpose and audience guide the project.")
H('224.d.11.B',3,"A production proposal given to a client for approval often includes:",
  "a timeline and a cost estimate",["private diary pages","unrelated news","a personal playlist"],"Proposals state scope, schedule, and cost.")
H('224.d.11.B',4,"Why get client approval of a proposal before starting production?",
  "To confirm both sides agree on the plan",["To delay the project","To raise the price","To skip the contract"],"Approval prevents misunderstandings.")
H('224.d.12.A',3,"Listing the actors, camera operators, and locations needed for a shoot is identifying:",
  "production requirements",["viewer ratings","paint colors","poster sizes"],"Planning requires knowing cast, crew, equipment, and place.")
H('224.d.12.A',4,"A voice-over recording requires which equipment?",
  "A microphone and a quiet space",["A paint roller","A drill","A projector screen only"],"Clean audio needs the right mic and environment.")
H('224.d.12.B',3,"A production budget should consider the cost of:",
  "crew, equipment, and locations",["unrelated gifts","vacations","pet food"],"Budgets account for the main production expenses.")
H('224.d.12.B',4,"If rental equipment costs more than planned, the producer should:",
  "adjust the budget or find lower-cost options",["ignore the overage","hide the invoice","stop paying the crew"],"Good budgeting responds to changing costs.")
H('224.d.12.C',3,"A storyboard shows a project's scenes as:",
  "a sequence of drawn panels",["a list of prices","a paycheck","an audio mix"],"Storyboards plan visuals shot by shot.")
H('224.d.12.C',4,"Why is a script analyzed alongside the storyboard?",
  "To make sure visuals and dialogue match",["To lower the volume","To change fonts","To erase scenes"],"Both documents must support the same story.")
H('224.d.12.D',3,"Choosing who will be the director, animator, and sound designer is:",
  "assigning team roles",["picking lunch","buying software","painting sets"],"Clear roles make production run smoothly.")
H('224.d.12.D',4,"Why define team roles before production starts?",
  "So each person knows their responsibilities",["So no one works","So tasks overlap","So the budget disappears"],"Defined roles reduce confusion.")
H('224.d.13.A',3,"Before production, an animator meets with the client to explain how the work will be done. This is:",
  "presenting production strategies",["avoiding the client","closing the studio","cancelling the job"],"Clients should understand the plan.")
H('224.d.13.A',4,"What should an animator do when a client suggests a change in the middle of production?",
  "Discuss how it affects time and cost",["Ignore the suggestion","Agree with no questions","Stop responding"],"Changes affect schedule and budget.")
H('224.d.13.B',3,"Filming scenes in an order that fits the schedule and then assembling them is a:",
  "sequence of production events",["random pile of clips","blank timeline","single photo"],"Production follows a planned sequence.")
H('224.d.13.B',4,"What does a coherent sequence of production events help prevent?",
  "Delays and rework",["Sound","Color","Storytelling"],"Order and planning save time.")
H('224.d.13.C',3,"Using the correct microphone, lights, and crew produces:",
  "a quality production",["a messy set","lost files","unsafe work"],"Proper equipment and crew improve results.")
H('224.d.13.C',4,"Why is trained crew important during a shoot?",
  "They operate equipment correctly and safely",["They avoid the script","They replace the client","They delete takes"],"Skilled crew improve both quality and safety.")
H('224.d.13.D',3,"A crew member respectfully listens to a teammate who is stressed on set. This shows:",
  "teamwork and sensitivity",["rudeness","competition","avoidance"],"Interpersonal skills keep the crew working well.")
H('224.d.13.D',4,"Which response shows good interpersonal skills when a deadline is close?",
  "Stay calm and ask how you can help",["Snap at coworkers","Leave the set","Blame the intern"],"Calm support helps the team under pressure.")
H('224.d.13.E',3,"Cutting clips together, adding transitions, and fixing audio uses:",
  "an editing system",["a printing press","a saw","a thermostat"],"Editing software assembles footage into a finished piece.")
H('224.d.13.E',4,"Which is an appropriate use of an editing system?",
  "Trimming clips on a timeline",["Cooking dinner","Typing a taxes form only","Charging a phone"],"Editing involves arranging and trimming clips.")
H('224.d.13.F',3,"A director chooses the camera angle, lighting, and sound for a scene. She is making decisions about:",
  "each element of production",["only the budget","her lunch","the weather"],"Each element influences the final product.")
H('224.d.13.F',4,"Why should decisions about lighting and sound be made together?",
  "They both affect how the audience feels about the scene",["They are unrelated","They cost nothing","They only affect the credits"],"Elements work together to create mood.")
H('224.d.14.A',3,"A video will not play on a client's older device. The animator checks the file type and resolution. She is solving a:",
  "compatibility issue",["marketing issue","color issue","scheduling issue"],"Compatibility problems arise when formats are unsupported.")
H('224.d.14.A',4,"Which step helps avoid compatibility problems on different devices?",
  "Export the file in a widely supported format",["Use a rare file type","Skip testing","Rename the file extension"],"Common formats play on most devices.")
H('224.d.14.B',3,"Making a video file smaller so it uploads faster uses:",
  "compression",["more pixels","bigger frames","louder sound"],"Compression reduces file size.")
H('224.d.14.B',4,"H.264 and MPEG are examples of:",
  "compression standards",["fonts","cameras","microphones"],"They are video encoding standards.")
H('224.d.14.C',3,"A cartoon for mobile phones is delivered in a size and format that fit small screens. The animator researched:",
  "delivery formats for the audience",["office furniture","coffee brands","printer ink"],"Delivery format depends on the target audience.")
H('224.d.14.C',4,"A film is shown in a movie theater and also posted online. Why might two formats be needed?",
  "Each platform has different technical needs",["They are identical","Theaters accept no files","Online sites need no files"],"Platforms differ in resolution and file types.")
H('224.d.14.D',3,"A client wants to share an animation on social media and in a school. The animator should:",
  "recommend the best delivery options for each",["pick one at random","say nothing","refuse to help"],"Advising clients is part of professional service.")
H('224.d.14.D',4,"Which detail should an animator consider when advising a client on delivery?",
  "Where and how the audience will watch it",["Which animator likes pizza","The studio's wall color","The client's shoe size"],"Viewing context decides the best format.")
H('224.d.15.A',3,"A freelance animator creates a short demo reel and a website to attract clients. This is:",
  "self-promotion",["time off","budget cutting","a legal filing"],"Freelancers market themselves.")
H('224.d.15.A',4,"Which is a standard self-promotion technique for a freelancer?",
  "Posting a portfolio and sharing it with potential clients",["Hiding all work","Declining all inquiries","Changing careers each week"],"Visible work attracts business.")
H('224.d.15.B',3,"A freelancer sends a client a document listing the work, price, and due date. This is a:",
  "proposal",["lullaby","song lyric","map"],"A proposal outlines the services and costs.")
H('224.d.15.B',4,"If an invoice has not been paid by its due date, a freelancer follows standard:",
  "collection practices",["storytelling","drawing","design"],"Collection practices help get paid on time.")
H('224.d.15.C',3,"Before starting a freelance business, an animator learns about licenses, taxes, and insurance. This is researching:",
  "start-up practices",["retirement homes","movie reviews","paint colors"],"Start-up research reduces surprises.")
H('224.d.15.C',4,"Which resource would help a new freelancer learn about starting a business?",
  "A small business development organization",["A random meme page","A toy store","A cooking show"],"Business organizations give reliable guidance.")
H('224.d.15.D',3,"Invoice software, cloud storage, and project trackers are:",
  "technology applications for freelancers",["art supplies","building tools","gym equipment"],"Freelancers use software to run their business.")
H('224.d.15.D',4,"A freelancer wants clients to review drafts remotely. Which technology fits best?",
  "A cloud file-sharing service",["A paper mailbox","A fax from 1990","A typewriter"],"Cloud tools make review easy.")
H('224.d.16.A',3,"A job seeker researches which studios hire animators and what skills they need. This is identifying:",
  "types and requirements of employers",["lunch places","parking spots","holiday dates"],"Understanding employers helps target applications.")
H('224.d.16.A',4,"Which source would best show the requirements for an animator job?",
  "The job posting",["A weather report","A toy catalog","A sports score"],"Postings list required skills and experience.")
H('224.d.16.B',3,"When arriving for an interview, a professional will:",
  "greet people politely and arrive on time",["arrive an hour late","use a phone during the interview","skip introductions"],"Etiquette makes a good first impression.")
H('224.d.16.B',4,"Which action shows professional protocol after a job interview?",
  "Send a thank-you note",["Send nothing","Argue about the decision","Post complaints online"],"A thank-you note is a polite follow-up.")
H('224.d.16.C',3,"For a professional animation studio interview, the best choice of clothing is:",
  "neat and appropriate attire",["wrinkled clothes","pajamas","costumes"],"Appropriate attire shows respect and readiness.")
H('224.d.16.C',4,"Good grooming for an interview includes:",
  "being clean and tidy",["wearing heavy fragrance","ignoring hygiene","wearing dirty shoes"],"Grooming contributes to a professional image.")
H('224.d.17.A',3,"During an interview, looking at the speaker and nodding shows good:",
  "nonverbal and listening skills",["distraction","impatience","boredom"],"Body language shows engagement.")
H('224.d.17.A',4,"Which behavior signals poor listening in an interview?",
  "Interrupting the interviewer",["Making eye contact","Taking brief notes","Asking a follow-up question"],"Interrupting shows you are not listening.")
H('224.d.17.B',3,"A candidate describes software she knows and projects she finished. She is conveying her:",
  "skill set",["travel plans","music taste","shopping list"],"Clear communication explains your abilities.")
H('224.d.17.B',4,"Which answer best communicates a skill to an interviewer?",
  "I created a two-minute animated short in Blender.",["I'm okay at stuff.","Whatever you need.","I guess I can try."],"Specific examples show proof of skill.")
H('224.d.17.C',3,"Interviewers must not discriminate based on race, religion, or:",
  "national origin",["portfolio quality","work history","training"],"Federal law protects against discrimination.")
H('224.d.17.C',4,"Which question is generally unlawful for an employer to ask in an interview?",
  "Are you planning to have children?",["Can you meet the schedule?","What software do you know?","Do you have references?"],"Questions about family plans can be discriminatory.")
H('224.d.17.D',3,"A candidate interviews with a panel of people from different backgrounds. She should:",
  "treat each person respectfully",["ignore some members","only speak to one person","use rude jokes"],"Respect for diversity is a professional skill.")
H('224.d.17.D',4,"Which approach helps when communicating with a diverse group during an interview?",
  "Avoid assumptions and use clear, inclusive language",["Use stereotypes","Use slang no one knows","Speak only to the youngest person"],"Inclusive language helps everyone understand.")

# ---------- 225 Practicum in Animation ----------
H('225.d.3',3,"Before operating production equipment, a practicum student should first:",
  "learn the safety techniques for the job",["skip the instructions","hurry through setup","let someone else decide"],"Safe techniques protect people and equipment.")
H('225.d.3',4,"A student sees a spilled drink near a power strip on a set. What is the best safety response?",
  "Clean it up and move the power strip away from liquids",["Step over it","Place a cable on it","Leave it for later"],"Liquids and electricity are a dangerous combination.")
H('225.d.1.A',3,"A practicum student explains a scene change to the crew using clear words and steady eye contact. This demonstrates:",
  "verbal and non-verbal communication",["silent work","guesswork","avoidance"],"Communication includes both words and body language.")
H('225.d.1.A',4,"Which choice shows clear verbal communication in a workplace?",
  "Stating the task, the deadline, and who is responsible",["Mumbling instructions","Using unclear hints","Changing the plan without telling anyone"],"Clarity prevents mistakes.")
H('225.d.1.B',3,"A student studies a chart of monthly viewer counts and writes a short summary for the team. She is:",
  "analyzing and communicating data",["ignoring data","guessing results","deleting charts"],"Interpreting information and sharing findings is a key skill.")
H('225.d.1.B',4,"Which summary best communicates data to a client?",
  "Viewership grew from 500 to 750 over two months.",["Numbers went up, I think.","Stuff happened.","It was fine."],"Specific numbers make a message precise.")
H('225.d.1.C',3,"A practicum student demonstrates her work to the class with slides and answers questions. This is a:",
  "formal presentation",["private rehearsal only","locker check","sound test"],"Planned presentations include visuals and Q&A.")
H('225.d.1.C',4,"Which choice makes a presentation more effective?",
  "Practicing beforehand and keeping slides simple",["Reading every word from the slide","Using tiny text","Skipping the introduction"],"Preparation and clear slides help audiences follow.")
H('225.d.1.D',3,"A client crosses her arms and frowns while viewing a draft. The student should recognize this as a possible sign of:",
  "disagreement or discomfort",["pure joy","excitement","sleep"],"Nonverbal cues can reveal how someone feels.")
H('225.d.1.D',4,"A student notices a coworker looks confused during an explanation. The best response is to:",
  "pause and ask if anything needs clarifying",["speed up","walk away","raise your voice"],"Reading cues helps improve communication.")
H('225.d.1.E',3,"Returning a customer's call promptly and politely helps maintain:",
  "good customer relations",["secret contracts","low morale","bad habits"],"Public relations skills keep customers satisfied.")
H('225.d.1.E',4,"A viewer complains publicly about a late release. Which response protects the studio's reputation?",
  "Apologize, explain, and offer a new release date",["Delete the comment angrily","Argue with the viewer","Ignore all messages"],"A calm, helpful reply preserves trust.")
H('225.d.2.A',3,"A student fixes a recurring file error by testing one change at a time without being told. This shows:",
  "independent critical thinking",["dependence on others","carelessness","avoidance"],"Critical thinking includes working independently.")
H('225.d.2.A',4,"Which statement best describes critical thinking in a group?",
  "Weighing evidence before reaching a conclusion",["Accepting the first idea","Ignoring the facts","Voting without discussion"],"Evidence-based reasoning improves decisions.")
H('225.d.2.B',3,"A rendering job keeps failing. The student breaks the problem into software, hardware, and file settings. She is:",
  "analyzing elements of a problem",["ignoring the problem","giving up","blaming others"],"Dividing a problem helps find creative solutions.")
H('225.d.2.B',4,"After finding that a scene is too heavy to render, which is a creative solution?",
  "Simplify the lighting or split the scene into layers",["Delete the scene","Wait for a miracle","Ignore the deadline"],"Innovative fixes keep the project moving.")
H('225.d.2.C',3,"A student uses what she learned about timing in a bouncing ball to animate a falling box. This shows:",
  "transfer of knowledge to a new task",["forgetting lessons","copying a friend","avoiding practice"],"Knowledge can be adapted to new situations.")
H('225.d.2.C',4,"Which example best shows adapting knowledge to create a new product?",
  "Applying lighting lessons from a short film to a game trailer",["Repeating the same project","Starting over from nothing","Skipping lessons"],"Adapting skills builds creativity.")
H('225.d.4.A',3,"A student arrives on time, works through assigned tasks, and helps others. This shows a positive:",
  "work ethic",["delay","excuse","distraction"],"A strong work ethic includes reliability and effort.")
H('225.d.4.A',4,"Which behavior shows a productive work ethic?",
  "Completing tasks on schedule without being reminded",["Waiting to be told twice","Leaving early","Working slowly on purpose"],"Self-directed reliability is valued by employers.")
H('225.d.4.B',3,"A student uses a sound effect from a library that requires credit. She should:",
  "list the creator in the credits",["claim she made it","delete the license","hide the file"],"Ethical conduct includes giving proper credit.")
H('225.d.4.B',4,"Ethical conduct on a team project includes:",
  "keeping promises and giving credit",["taking shortcuts that hurt others","hiding mistakes","copying without permission"],"Honesty and credit build trust.")
H('225.d.4.C',3,"Before blending a stock photograph into a composited scene, a student should check:",
  "its license and usage rights",["its file size only","its color only","its brightness only"],"Respecting intellectual property requires knowing the license.")
H('225.d.4.C',4,"A student wants to morph a celebrity's photo for a school project and post it publicly. What is the proper step?",
  "Get permission or use licensed or original material",["Post it anyway","Remove the watermark","Claim it as personal art"],"Public use of someone's likeness or work requires permission.")
H('225.d.4.D',3,"Which action is safe, legal, and responsible use of technology?",
  "Using licensed software on school computers",["Sharing your password","Installing pirated programs","Opening unknown email attachments"],"Licensed software and good security are responsible practices.")
H('225.d.4.D',4,"A practicum student finds a website offering free paid software. The responsible choice is to:",
  "avoid the illegal download",["download it quickly","share it with classmates","install it on the lab PCs"],"Illegal copies violate copyright law.")
H('225.d.4.E',3,"Following rules, laws, and regulations at a workplace should be done:",
  "consistently",["only when watched","only on Mondays","never"],"Compliance should be a habit.")
H('225.d.4.E',4,"Which is an example of complying with workplace regulations?",
  "Wearing required protective gear",["Ignoring a posted rule","Skipping training","Taking tools home"],"Following regulations protects people and the company.")
H('225.d.5.A',3,"A practicum student works at a studio under a mentor and writes down what she learned each week. She is:",
  "documenting learning activities",["hiding her work","avoiding feedback","skipping tasks"],"Documentation shows progress.")
H('225.d.5.A',4,"Why do practicum students evaluate their learning activities?",
  "To identify what they learned and what to improve",["To avoid the mentor","To hide errors","To skip reflection"],"Evaluation guides growth.")
H('225.d.5.B',3,"A student learns an advanced compositing technique used in her chosen studio specialty. This is developing:",
  "advanced technical knowledge",["basic hobbies","unrelated skills","beginner tasks only"],"Advanced skills prepare students for jobs.")
H('225.d.5.B',4,"Which activity most directly builds advanced technical skills related to an animation career?",
  "Practicing a professional tool on a real project",["Watching unrelated videos","Reading a menu","Napping"],"Hands-on use builds skill.")
H('225.d.5.C',3,"A production team shoots scenes in the order that makes the best use of the set, then edits them into story order. This is:",
  "a coherent sequence of production events",["random filming","skipping the edit","avoiding planning"],"Planning the order saves time.")
H('225.d.5.C',4,"What typically follows shooting in a production sequence?",
  "Editing and finishing",["Brainstorming the title","Casting","Location scouting"],"After capture comes post-production.")
H('225.d.5.D',3,"A practicum student sets up lights, a camera, and audio gear properly for a shoot. She is:",
  "using equipment appropriately",["wasting equipment","ignoring the crew","guessing at settings"],"Proper setup supports quality.")
H('225.d.5.D',4,"Why should crew members be trained before using expensive equipment?",
  "To protect people and prevent costly damage",["To slow production","To increase costs","To avoid planning"],"Training reduces accidents and repairs.")
H('225.d.5.E',3,"Trimming clips and adding transitions in editing software is using an:",
  "editing system",["accounting system","irrigation system","heating system"],"Editing software assembles footage.")
H('225.d.5.E',4,"Which editing task improves a scene's pacing?",
  "Cutting out unnecessary pauses",["Adding more pauses","Deleting the audio","Changing the file name"],"Tighter cuts increase energy.")
H('225.d.5.F',3,"A producer checks whether work is on schedule and under budget. She is:",
  "monitoring the production schedule and costs",["ignoring deadlines","adding random tasks","ending the project"],"Monitoring keeps a project on track.")
H('225.d.5.F',4,"If a task will cost more than estimated, a producer should:",
  "report the change and adjust the plan",["hide the cost","stop paying","pretend it is fine"],"Open communication prevents surprises.")
H('225.d.5.G',3,"A final animation looks different on two screens. The student corrects the settings for each device. She is solving:",
  "compatibility problems",["storage problems","pricing problems","hiring problems"],"Different devices may need different exports.")
H('225.d.5.G',4,"Which factor often causes compatibility issues between devices?",
  "Differences in file format or resolution",["The color of the desk","The brand of pens","The time of day"],"Formats and resolution vary between devices.")
H('225.d.5.H',3,"A client wants an animation for a phone app. The student exports it in the format the app supports. She is:",
  "implementing the appropriate delivery format",["ignoring the audience","rejecting the client","skipping delivery"],"The format must suit the target platform.")
H('225.d.5.H',4,"Which question helps choose a delivery format?",
  "Where will the viewers watch the project?",["What is the studio address?","Who is on lunch break?","How many pencils are there?"],"Viewing platform determines the format.")
H('225.d.5.I',3,"A student compares showing a film online, in theaters, and at festivals to reach the largest audience. She is:",
  "analyzing distribution options",["avoiding the audience","printing posters only","editing audio only"],"Distribution choices affect reach.")
H('225.d.5.I',4,"Which distribution option usually reaches the widest audience with the lowest cost?",
  "Posting online",["Mailing DVDs to every house","Renting a theater for a day","Handing out flyers only"],"Online platforms reach many people cheaply.")
H('225.d.5.J',3,"A student can now finish edits faster than at the start of the year. This is:",
  "growth of technical skill",["no change","a decline in skill","a lost skill"],"Improving speed and accuracy shows growth.")
H('225.d.5.J',4,"Which evidence best demonstrates growth in technical skill?",
  "Comparing early work with later work",["Skipping assignments","Ignoring feedback","Repeating mistakes"],"Side-by-side comparison shows progress.")
H('225.d.5.K',3,"A student lists what she does well and what needs practice. She is evaluating her:",
  "strengths and weaknesses",["salary","hobbies","address"],"Self-evaluation guides improvement.")
H('225.d.5.K',4,"Why should a student identify weaknesses in technical skills?",
  "To plan how to improve them",["To feel bad","To avoid learning","To skip assignments"],"Knowing weaknesses lets you target practice.")
H('225.d.5.L',3,"Saving finished clips, project files, and mentor comments to show later is collecting:",
  "representative work samples",["junk files","unfinished sketches only","private notes only"],"Work samples show real accomplishments.")
H('225.d.5.L',4,"Which item is the best work sample for an animation portfolio?",
  "A polished clip you finished for a project",["A blank page","A grocery list","A damaged file"],"Samples should show skill and completion.")

# ---------- 226 Audio and Video Production I ----------
H('226.d.1.A',3,"A video producer writes a clear email and proofreads her script before recording. She is using skills from:",
  "English language arts",["metalwork","gym class","woodshop"],"Reading and writing skills support every production task.")
H('226.d.1.A',4,"Which habit shows English language arts knowledge in an audio studio?",
  "Reading a narration script aloud to check grammar and flow",["Recording without a script","Writing messages in all capitals","Skipping spell-check"],"Careful language use improves quality.")
H('226.d.1.B',3,"A video editor charges $35 per hour. She works 8 hours. How much will she invoice?",
  "$280",["$43","$240","$270"],"35 x 8 = 280.")
H('226.d.1.B',4,"A podcast episode is 45 minutes long and the editor spends 3 minutes of work for each minute of audio. How many minutes of editing time is needed?",
  "135",["48","90","15"],"45 x 3 = 135 minutes.")
H('226.d.2.A',3,"A video producer explains a shot list to a new intern using simple words. She is adjusting language for her:",
  "audience",["camera","lens","tripod"],"Style and word choice should match the listener.")
H('226.d.2.A',4,"Which statement best fits a formal email to a TV station manager?",
  "Dear Ms. Lopez, I am writing to confirm the schedule.",["Hey, what's up?","yo send me stuff","lol check this out"],"Formal situations call for formal language.")
H('226.d.2.B',3,"An audio engineer organizes notes about microphone placement before telling the crew. This is:",
  "organizing oral and written information",["ignoring information","guessing","erasing"],"Organized information is easier to share.")
H('226.d.2.B',4,"Which step helps organize a spoken explanation of a production plan?",
  "Outline the main points in order",["Speak randomly","Skip the plan","Use long pauses"],"Outlines give structure to a talk.")
H('226.d.2.C',3,"A radio station shows which time slots have the most listeners on a chart. This communicates:",
  "data",["rumors","gossip","fiction"],"Charts communicate numerical information.")
H('226.d.2.C',4,"A producer reports that podcast downloads increased by 30% after a new topic. This is effective because it:",
  "uses specific data",["is vague","has no proof","is only opinion"],"Specific numbers support a message.")
H('226.d.2.D',3,"A student presents her short video to the class and explains her choices. This is a:",
  "presentation",["rehearsal","password","backup"],"Presentations share work with an audience.")
H('226.d.2.D',4,"Which presentation is informal?",
  "Showing a rough cut to a friend for quick feedback",["A scripted talk at a film festival","A boardroom pitch","A formal conference keynote"],"Informal presentations are casual.")
H('226.d.2.E',3,"A client explains the tone she wants for a radio ad. The producer takes notes and asks questions. She is:",
  "listening actively",["interrupting","guessing","daydreaming"],"Active listening gets information accurately.")
H('226.d.2.E',4,"After hearing unclear feedback, the best way to clarify information is to:",
  "restate it and ask if you understood correctly",["ignore it","change everything","blame the client"],"Paraphrasing confirms meaning.")
H('226.d.2.F',3,"A video crew includes members from different backgrounds. A good team member will:",
  "listen to everyone with respect",["ignore some people","mock accents","only talk to friends"],"Respect helps teams work together.")
H('226.d.2.F',4,"Which behavior shows respect for diverse individuals on a set?",
  "Using names correctly and inviting everyone's ideas",["Using nicknames that offend","Interrupting people","Ignoring input"],"Inclusive habits help everyone contribute.")
H('226.d.2.G',3,"A station manager politely answers a viewer who complained about audio quality. This shows:",
  "public relations skills",["editing skills","lighting skills","camera skills"],"Good PR keeps audiences loyal.")
H('226.d.2.G',4,"A video company keeps a friendly social media presence and responds to comments. This builds:",
  "customer goodwill",["private files","secret budgets","lighting"],"Responsive communication builds trust.")
H('226.d.3.A',3,"A producer reviews audience survey results to decide which show to renew. This uses:",
  "critical thinking",["luck","coin flips","guessing"],"Gathering and interpreting data supports decisions.")
H('226.d.3.A',4,"Which action shows critical thinking when audio has a constant hum?",
  "Check cables and connections one at a time",["Ignore the hum","Delete the recording","Add more volume"],"Systematic troubleshooting finds the source.")
H('226.d.3.B',3,"Three crew members disagree on the best location for a shoot. The best approach is to:",
  "discuss each option and agree as a group",["let the oldest decide","avoid talking","guess"],"Groups use communication to decide.")
H('226.d.3.B',4,"Which group technique helps a team solve a production problem?",
  "Brainstorming ideas before choosing one",["Working in silence","Blaming each other","Delaying forever"],"Brainstorming gathers many ideas.")
H('226.d.4.A',3,"A video team uses email and shared online folders to send files. These are:",
  "technology applications",["props","costumes","tripods"],"Software tools support communication.")
H('226.d.4.A',4,"Which technology application is best suited for scheduling a video conference with a client?",
  "A calendar app",["A camera lens","A microphone cable","A light stand"],"Calendars coordinate meeting times.")
H('226.d.4.B',3,"Naming and sorting raw footage in folders so it is easy to find is:",
  "file management",["file hiding","file erasing","file shrinking"],"Organized files save editing time.")
H('226.d.4.B',4,"Which practice is good for backing up important footage?",
  "Keep copies on two different storage devices",["Store only one copy","Delete the original","Keep everything on a flash drive in a pocket"],"Backups protect against loss.")
H('226.d.5.A',3,"Early radio was broadcast live, and television began as black-and-white. Today audio and video are mostly:",
  "digital",["silent","unchanged","hand-cranked"],"The industry moved from analog to digital.")
H('226.d.5.A',4,"Which statement summarizes the evolution of video production?",
  "Film gave way to tape and then to digital file-based production",["Video has never changed","It began with smartphones","Film replaced digital"],"Technology moved from film to digital.")
H('226.d.5.B',3,"Podcasts and streaming video are current trends that:",
  "give creators new ways to reach audiences",["end all media jobs","remove the need for sound","ban cameras"],"Trends shape how content is made and seen.")
H('226.d.5.B',4,"Short vertical videos for phone apps are a current trend. Producers respond by:",
  "creating content designed for mobile viewing",["ignoring the trend","shooting only film","avoiding phones"],"Producers adapt content to platforms.")
H('226.d.6.A',3,"A student secures a tripod and tapes down cables before a shoot. This is following:",
  "safety rules",["style rules","price rules","spelling rules"],"Safety measures prevent accidents.")
H('226.d.6.A',4,"Which action reflects workplace safety in a studio?",
  "Never overloading electrical outlets",["Plugging many devices into one outlet","Leaving cords across walkways","Ignoring sparks"],"Overloaded outlets cause fires.")
H('226.d.6.B',3,"A student notices a heavy light on an unstable stand. The best action is to:",
  "report it and fix or replace the stand",["leave it","push it aside","use it anyway"],"Resolve concerns before someone is hurt.")
H('226.d.6.B',4,"Loud audio at high volume for hours can damage hearing. Which step helps?",
  "Lower the volume and take listening breaks",["Raise the volume","Remove ear protection","Skip breaks"],"Safe levels protect hearing.")
H('226.d.6.C',3,"If a smoke alarm goes off in the studio, staff should:",
  "exit by the posted route",["keep recording","hide","turn off the alarm and stay"],"Follow the emergency plan.")
H('226.d.6.C',4,"Where should a fire extinguisher be located in a studio?",
  "In a clear, visible spot near an exit",["Behind equipment","Locked in a closet","Under a table"],"Emergency tools must be easy to reach.")
H('226.d.7.A',3,"A producer sets goals, assigns tasks, and motivates the crew. She is showing:",
  "leadership",["avoidance","laziness","confusion"],"Leaders guide groups toward goals.")
H('226.d.7.A',4,"When a deadline is at risk, a good leader will:",
  "analyze the problem and reassign tasks",["ignore it","blame an intern","stop the project"],"Leaders respond to obstacles.")
H('226.d.7.B',3,"Two editors disagree about how to cut a scene. They should:",
  "discuss the options and look for a compromise",["argue loudly","refuse to cooperate","quit"],"Teamwork includes conflict management.")
H('226.d.7.B',4,"Which comment supports teamwork when a conflict arises?",
  "Let's figure out what works best for the project",["That's a bad idea","I won't change anything","You're wrong"],"Focus on the shared goal.")
H('226.d.7.C',3,"Encouraging coworkers and giving constructive feedback helps build:",
  "effective working relationships",["tension","distance","distrust"],"Support builds trust.")
H('226.d.7.C',4,"Which feedback is constructive on a rough audio mix?",
  "The voice is clear; try lowering the music a bit",["This is terrible","Anyone could do better","I hate it"],"Specific and kind feedback is helpful.")
H('226.d.7.D',3,"Writing an agenda with goals before a production meeting is:",
  "preparing for the meeting",["avoiding the meeting","wasting time","skipping work"],"Agendas help meetings achieve outcomes.")
H('226.d.7.D',4,"What is a clear goal for a pre-production meeting?",
  "Finalize the shot list and assign roles",["Talk about weekend plans","Argue about lunch","Listen to music"],"Meeting goals should be specific and relevant.")
H('226.d.7.E',3,"During a crew meeting, participants should:",
  "stay on topic and contribute",["scroll their phones","interrupt","leave early without a word"],"Focus accomplishes work tasks.")
H('226.d.7.E',4,"Which action helps a meeting accomplish its purpose?",
  "Assign action items with owners and deadlines",["Skip decisions","End with no plan","Cancel the agenda"],"Action items turn talk into progress.")
H('226.d.7.F',3,"A senior sound engineer shows an apprentice how to set levels. This is:",
  "mentoring",["competing","copying","hiding"],"Mentors teach and inspire.")
H('226.d.7.F',4,"What quality makes someone a good mentor?",
  "Willingness to share knowledge patiently",["Keeping secrets","Criticizing harshly","Avoiding questions"],"Mentors support the growth of others.")
H('226.d.8.A',3,"A student uses a classmate's script idea in her video. Ethical practice means she should:",
  "give the classmate credit",["claim the idea","change the name","remove the credit"],"Proper credit is part of ethical conduct.")
H('226.d.8.A',4,"Which action shows ethical conduct in a video project?",
  "Crediting contributors in the end titles",["Taking all the credit","Copying a competitor's work","Leaving out co-writers"],"End credits recognize contributors.")
H('226.d.8.B',3,"Copyright law protects a song's creator from:",
  "unauthorized copying and use",["being paid","being famous","being recorded"],"Copyright gives creators control over their work.")
H('226.d.8.B',4,"A teacher plays a brief music clip in class to illustrate a lesson. This may be allowed under:",
  "fair use",["piracy","trademark","patent"],"Fair use covers limited educational use.")
H('226.d.8.C',3,"Before sampling a section of a song in a new track, a producer should:",
  "get permission or a license",["assume it is free","remove the title","sell it fast"],"Respecting IP requires authorization.")
H('226.d.8.C',4,"An editor remixes someone else's footage into a new video. To respect intellectual property, she should:",
  "get permission or use licensed material",["claim it as hers","delete the credits","post it without notes"],"Altering a work does not remove the owner's rights.")
H('226.d.8.D',3,"A school's acceptable use policy forbids downloading pirated media. A student should:",
  "follow the policy",["download anyway","ask a friend to download","hide the files"],"Policies set rules for technology use.")
H('226.d.8.D',4,"Which is proper etiquette on a shared studio network?",
  "Avoid saturating bandwidth with big downloads during shoots",["Share your login","Run streaming all day","Delete others' files"],"Be considerate with shared resources.")
H('226.d.8.E',3,"Music, news, and video affect public opinion and culture. This shows the industry's:",
  "impact on society",["lack of effect","only cost","only noise"],"Media shapes attitudes.")
H('226.d.8.E',4,"The audio and video industry affects society by informing, entertaining, and:",
  "creating jobs",["reducing income","stopping communication","raising prices only"],"It provides employment and information.")
H('226.d.9.A',3,"A career portfolio for a video producer can include:",
  "demo reels, a resume, and certificates",["a lunch menu","spare cords","weather logs"],"A portfolio documents skills and experience.")
H('226.d.9.A',4,"Why keep a portfolio updated throughout school?",
  "To show growth and best work to employers",["To hide old work","To avoid interviews","To save paper"],"A current portfolio shows progress.")
H('226.d.9.B',3,"A graduate has two job offers with different pay and benefits. She should:",
  "compare pay, benefits, and growth chances",["choose by coin flip","accept without reading","ignore the details"],"Comparing helps make a good decision.")
H('226.d.9.B',4,"Which factor is important when evaluating a job in radio or video?",
  "Opportunities to learn and advance",["Brand of coffee","Lobby color","Weather"],"Advancement affects a long career.")
H('226.d.9.C',3,"Attending an industry event and meeting working professionals is:",
  "professional networking",["avoiding work","shopping","gaming"],"Networking builds connections.")
H('226.d.9.C',4,"Which action helps maintain a professional network?",
  "Send a thank-you message after meeting someone",["Throw away cards","Never reply","Avoid events"],"Follow-up keeps relationships going.")
H('226.d.9.D',3,"Starting a wedding video business is an example of:",
  "entrepreneurship",["retirement","internship only","unemployment"],"Entrepreneurs run their own businesses.")
H('226.d.9.D',4,"A challenge of running your own video business is:",
  "finding clients and managing money yourself",["having a guaranteed salary","never needing a budget","never needing customers"],"Self-employment requires sales and finance skills.")
H('226.d.10.A',3,"Dividing a video project into tasks with deadlines is:",
  "planning and time management",["procrastination","guessing","delay"],"Planning helps finish on time.")
H('226.d.10.A',4,"Which practice helps a crew complete a project on time?",
  "Set milestones and check progress often",["Work without a schedule","Wait until the last day","Skip planning"],"Milestones keep work on track.")
H('226.d.10.B',3,"Using a task app to track shooting dates is using technology to:",
  "enhance productivity",["lose time","hide tasks","waste battery"],"Apps can organize work.")
H('226.d.10.B',4,"Cloud storage lets editors in different places work on the same project. This improves:",
  "collaboration",["confusion","cost","delay"],"Shared access supports teamwork.")
H('226.d.11.A',3,"A producer asks a client about goals, audience, and budget at the first meeting. She is:",
  "determining client needs",["selling equipment","editing footage","testing gear"],"Questions reveal what the client wants.")
H('226.d.11.A',4,"Which question best helps determine a client's needs for a radio ad?",
  "Who is the audience and what action do you want them to take?",["What did you watch last night?","Do you like rain?","What is your favorite song?"],"Audience and purpose shape the ad.")
H('226.d.11.B',3,"A proposal for client approval often includes:",
  "a schedule and a price",["gossip","unrelated news","personal playlists"],"Proposals describe scope, time, and cost.")
H('226.d.11.B',4,"Why get client approval of the proposal first?",
  "To make sure both sides agree on the plan",["To delay the work","To raise the cost","To skip a contract"],"Approval prevents misunderstandings.")
H('226.d.12.A',3,"Listing the actors, camera operators, microphones, and shooting locations needed is:",
  "identifying production requirements",["booking a vacation","buying snacks","painting walls"],"Planning covers cast, crew, equipment, and place.")
H('226.d.12.A',4,"For an outdoor interview, which equipment is most important to capture clear sound?",
  "A microphone with a windscreen",["A larger screen","A taller tripod only","A bigger monitor"],"Wind noise ruins audio without protection.")
H('226.d.12.B',3,"A production budget should account for:",
  "crew, equipment, and location costs",["unrelated gifts","vacations","pet food"],"Budgets cover the main expenses.")
H('226.d.12.B',4,"Equipment rental will cost more than planned. The producer should:",
  "adjust the budget or find cheaper options",["ignore it","hide the bill","skip paying"],"Plans must respond to changing costs.")
H('226.d.12.C',3,"A script and a storyboard are used to:",
  "plan dialogue and visuals",["pay the crew","order lunch","erase scenes"],"They map out what is heard and seen.")
H('226.d.12.C',4,"Why compare the script with the storyboard?",
  "To make sure words and images match",["To lower the volume","To change fonts","To delete scenes"],"Both documents tell the same story.")
H('226.d.12.D',3,"Choosing who will be director, camera operator, and sound mixer is:",
  "assigning team roles",["picking lunch","buying lights","painting sets"],"Roles define responsibilities.")
H('226.d.12.D',4,"Why define roles before the shoot?",
  "So each person knows their responsibilities",["So no one works","So tasks overlap","So the budget vanishes"],"Clear roles prevent confusion.")
H('226.d.13.A',3,"A producer meets with the client to explain how the project will be made. This is:",
  "presenting production strategies",["avoiding the client","closing the studio","cancelling the job"],"Clients should understand the plan.")
H('226.d.13.A',4,"A client asks for a change mid-production. The producer should:",
  "explain how it affects schedule and cost",["ignore it","agree with no discussion","stop replying"],"Changes have consequences for time and money.")
H('226.d.13.B',3,"Shooting scenes in an order that fits the schedule and then editing them into story order is:",
  "a sequence of production events",["random filming","skipping the edit","avoiding planning"],"Production follows a plan.")
H('226.d.13.B',4,"A coherent sequence of production events helps prevent:",
  "delays and rework",["storytelling","sound","color"],"Order saves time.")
H('226.d.13.C',3,"Correct microphones, lights, and trained crew lead to:",
  "quality productions",["messy sets","lost footage","unsafe work"],"Good equipment and crew produce good results.")
H('226.d.13.C',4,"Why is trained crew important during a shoot?",
  "They operate gear correctly and safely",["They avoid the script","They replace the client","They delete takes"],"Skilled crew improve quality and safety.")
H('226.d.13.D',3,"A crew member kindly helps a stressed coworker during a long shoot. This shows:",
  "teamwork and sensitivity",["rudeness","competition","avoidance"],"Interpersonal skills keep the crew working.")
H('226.d.13.D',4,"Which response shows good interpersonal skills on a tight schedule?",
  "Stay calm and ask how to help",["Snap at coworkers","Walk off set","Blame the intern"],"Calm support helps under pressure.")
H('226.d.13.E',3,"Cutting clips, mixing audio, and adding titles uses:",
  "an editing system",["a printing press","a hammer","a thermostat"],"Editing software assembles media.")
H('226.d.13.E',4,"Which is an appropriate use of editing software?",
  "Balancing audio levels between dialogue and music",["Cooking dinner","Mailing letters","Charging batteries"],"Mixing is part of editing.")
H('226.d.13.F',3,"A director chooses the camera angle, light, and microphone type for a scene. She is:",
  "making decisions about each production element",["only ordering food","only paying invoices","ignoring the script"],"Each element shapes the finished product.")
H('226.d.13.F',4,"Why should lighting and audio choices be made together?",
  "Both affect how the audience feels about the scene",["They are unrelated","They cost nothing","They only affect credits"],"Elements work together to create mood.")
H('226.d.14.A',3,"A video will not play on a client's old TV. The producer converts it to a supported format. She is fixing a:",
  "compatibility issue",["marketing issue","scheduling issue","lighting issue"],"Unsupported formats cause compatibility problems.")
H('226.d.14.A',4,"Which step helps avoid playback problems across devices?",
  "Export in a widely supported format",["Use a rare file type","Skip testing","Rename the extension"],"Common formats play on most devices.")
H('226.d.14.B',3,"Making a video file smaller for faster uploading uses:",
  "compression",["more pixels","bigger frames","louder sound"],"Compression reduces file size.")
H('226.d.14.B',4,"MP3 and MP4 are examples of:",
  "compression standards",["fonts","cameras","cables"],"They are common encoded formats.")
H('226.d.14.C',3,"A radio spot and a web video need different file formats. The producer researches:",
  "delivery formats for the audience",["office furniture","coffee brands","printer ink"],"Delivery depends on audience and platform.")
H('226.d.14.C',4,"Why might one project be delivered in more than one format?",
  "Each platform has different technical needs",["They are identical","Platforms accept no files","Formats never matter"],"Platforms differ in specs.")
H('226.d.14.D',3,"A client wants to show a video at an event and post it online. The producer should:",
  "recommend the best delivery options",["pick one at random","say nothing","refuse to help"],"Advising clients is part of service.")
H('226.d.14.D',4,"Which detail should a producer consider when advising on delivery?",
  "Where and how the audience will watch",["The producer's favorite food","The studio's wall color","The client's shoe size"],"Viewing context decides the best format.")
H('226.d.15.A',3,"A freelance sound designer builds a website and demo reel to attract clients. This is:",
  "self-promotion",["time off","budget cutting","a legal filing"],"Freelancers market themselves.")
H('226.d.15.A',4,"Which technique promotes a freelance video producer?",
  "Sharing a portfolio with potential clients",["Hiding her work","Declining inquiries","Changing careers"],"Visible work attracts business.")
H('226.d.15.B',3,"A freelancer sends a client a document with the job, price, and due date. This is a:",
  "proposal",["lullaby","map","poem"],"A proposal outlines services and cost.")
H('226.d.15.B',4,"If an invoice remains unpaid, the freelancer follows:",
  "standard collection practices",["storytelling steps","drawing rules","design principles"],"Collection practices help ensure payment.")
H('226.d.15.C',3,"Before starting a freelance business, a producer researches licenses, taxes, and insurance. She is researching:",
  "start-up practices",["retirement homes","movie reviews","paint colors"],"Start-up research reduces surprises.")
H('226.d.15.C',4,"Which resource helps a new freelancer learn about starting a business?",
  "A small business development center",["A meme page","A toy store","A cooking show"],"Business centers give reliable guidance.")
H('226.d.15.D',3,"Invoice software, cloud storage, and project trackers are:",
  "technology applications for freelancers",["art supplies","construction tools","gym equipment"],"Freelancers use software to run their business.")
H('226.d.15.D',4,"A freelancer wants clients to review a cut remotely. Which technology fits best?",
  "A private online review link",["A paper mailbox","A fax","A typewriter"],"Online review is fast and convenient.")
H('226.d.16.A',3,"A job seeker researches which stations and studios hire editors and what skills they require. She is:",
  "identifying types and requirements of employers",["picking lunch spots","choosing parking","selecting holidays"],"Understanding employers helps target applications.")
H('226.d.16.A',4,"Which source best shows the requirements for a video editor job?",
  "The job posting",["A toy catalog","A weather report","A sports score"],"Postings list required skills.")
H('226.d.16.B',3,"When arriving for an interview, a professional will:",
  "greet people politely and arrive on time",["arrive an hour late","use a phone during the interview","skip introductions"],"Etiquette makes a good first impression.")
H('226.d.16.B',4,"Which action shows professional protocol after an interview?",
  "Send a thank-you note",["Send nothing","Argue about the decision","Post complaints online"],"A thank-you is a polite follow-up.")
H('226.d.16.C',3,"For an interview at a TV station, the best clothing choice is:",
  "neat and appropriate attire",["wrinkled clothes","pajamas","costumes"],"Appropriate attire shows respect.")
H('226.d.16.C',4,"Good grooming for an interview includes:",
  "being clean and tidy",["wearing heavy fragrance","ignoring hygiene","wearing dirty shoes"],"Grooming contributes to a professional image.")
H('226.d.17.A',3,"During an interview, looking at the speaker and nodding shows good:",
  "nonverbal and listening skills",["distraction","impatience","boredom"],"Body language shows engagement.")
H('226.d.17.A',4,"Which behavior signals poor listening in an interview?",
  "Interrupting the interviewer",["Making eye contact","Taking brief notes","Asking a follow-up question"],"Interrupting shows you are not listening.")
H('226.d.17.B',3,"A candidate describes the editing software she knows and the projects she has finished. She is conveying her:",
  "skill set",["travel plans","music taste","shopping list"],"Clear communication explains your abilities.")
H('226.d.17.B',4,"Which statement best communicates a skill to an interviewer?",
  "I edited a ten-minute documentary in Premiere.",["I'm okay at stuff.","Whatever you need.","I guess I can try."],"Specific examples show proof of skill.")
H('226.d.17.C',3,"Employers may not discriminate based on race, religion, or:",
  "national origin",["portfolio quality","work history","training"],"Federal law protects against discrimination.")
H('226.d.17.C',4,"Which question is generally unlawful for an employer to ask in an interview?",
  "What is your religion?",["Can you work the schedule?","What software do you know?","Do you have references?"],"Questions about protected traits are unlawful.")
H('226.d.17.D',3,"A candidate interviews with a panel of people from different backgrounds. She should:",
  "treat each person respectfully",["ignore some members","speak to only one person","tell rude jokes"],"Respect for diversity is a professional skill.")
H('226.d.17.D',4,"Which approach helps when communicating with a diverse group in an interview?",
  "Avoid assumptions and use clear, inclusive language",["Use stereotypes","Use slang no one knows","Speak only to the youngest person"],"Inclusive language helps everyone understand.")

H('224.d.8.B',5,"A student wants to use a 30-second song snippet as background in an animated short she will post publicly and monetize. Which step most protects her legally?",
  "Securing a license from the rights holder before posting",["Crediting the singer in the description only","Lowering the volume of the song","Renaming the audio file"],"Public, monetized use usually requires a license; credit alone is not permission.")
H('226.d.13.C',5,"A two-person crew is filming an interview in a loud lobby with one camera and no audio gear. What addition most improves the quality of the final product?",
  "A lavalier microphone for the speaker",["A brighter camera screen","A second tripod for decoration","A larger memory card only"],"Clean dialogue requires a microphone close to the speaker.")
H('226.d.15.D',5,"A freelance video editor needs to bill three clients, track hours, and store raw footage safely. Which combination of tools fits these needs?",
  "Invoicing software, time tracking, and cloud backup",["A sketchbook and a ruler","A radio and a lamp","A fax and a stapler"],"Each tool matches one business need.")
H('226.d.16.B',5,"A candidate for a radio producer job arrives 10 minutes early, silences her phone, and shakes hands with the interviewer. Which protocol is she showing?",
  "Punctuality and courteous introductions",["Over-familiarity","Avoidance","Disinterest"],"Arriving early and greeting politely follow interview etiquette.")
H('226.d.16.C',5,"A candidate is invited to a video studio interview and is unsure what to wear. Which choice best balances a creative field with professionalism?",
  "Clean, neat business-casual clothing",["Gym clothes","Formal evening wear","Ripped, stained clothes"],"Attire should be neat and fit the setting.")
H('226.d.17.A',3,"An interviewer explains the studio's schedule. Which response shows strong listening skills?",
  "Paraphrasing the schedule to confirm understanding",["Checking your phone","Looking at the floor","Talking about something else"],"Paraphrasing shows you heard and understood.")
H('226.d.17.A',4,"Which nonverbal behavior helps you appear engaged while a hiring manager is talking?",
  "Sitting upright and keeping eye contact",["Slouching and yawning","Tapping loudly","Looking at the clock"],"Posture and eye contact signal attention.")
H('226.d.17.C',5,"A hiring manager for a TV station asks a candidate about her age, religion, and marital status. How should lawful interview questions be focused instead?",
  "On the skills and availability needed for the job",["On family plans","On religious practice","On marital status"],"Lawful questions concern job-related qualifications.")
H('226.d.17.D',5,"A candidate is interviewed by a team that includes members who speak with different accents. Which approach works best?",
  "Ask for clarification politely when needed",["Mimic their accents","Ignore their questions","Assume you understand everything"],"Polite clarification shows respect and ensures understanding.")
H('226.d.9.D',5,"A graduate with a camera and editing skills wants to earn income without a boss. Which business path fits her plan?",
  "Starting a freelance video production company",["Waiting for a studio to call","Enrolling in another class only","Applying for retirement"],"Freelancing is entrepreneurship.")

H('224.d.14.E',3,"A client asks where her animated short should be released. The animator explains choices such as video sites, festivals, and TV. She is discussing:",
  "distribution options",["cast lists","script fonts","lens choices"],"Distribution choices determine who sees the work.")
H('224.d.14.E',4,"Which option would likely give an animated short the widest reach at the lowest cost?",
  "Posting it on a popular video-sharing site",["Screening it in one classroom","Mailing one disc","Showing it only at the studio"],"Online platforms reach large audiences cheaply.")
H('226.d.14.E',3,"A podcaster compares posting episodes on a streaming app, a website, and local radio. She is weighing:",
  "distribution options",["camera angles","costume colors","lighting kits"],"Different outlets reach different audiences.")
H('226.d.14.E',4,"Why might a producer release a video on several platforms at once?",
  "To reach more viewers",["To lower audio quality","To avoid an audience","To use more cables"],"More platforms means a wider reach.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_37.jsonl'))

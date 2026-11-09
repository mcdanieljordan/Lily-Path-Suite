import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('127.', 1115, own='cte_38.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---------- 227 Practicum in Audio/Video Production ----------
H('227.d.1.A',3,"A practicum student tells the camera operator which shot comes next, using a clear voice and a pointed hand signal. This is:",
  "verbal and non-verbal communication",["silent guessing","a written contract","an edit"],"Words and gestures together make instructions clear.")
H('227.d.1.A',4,"On a noisy set, which approach keeps instructions clear?",
  "Pair short spoken cues with agreed hand signals",["Whisper and hope","Send a long email later","Wait for others to ask"],"Combining voice and signals prevents misunderstanding.")
H('227.d.1.B',3,"A student reads ratings from three test screenings and tells the director which scene viewers liked most. She is:",
  "interpreting and communicating data",["ignoring results","guessing","erasing notes"],"Making sense of data and sharing it is a core skill.")
H('227.d.1.B',4,"Which statement reports screening data most clearly?",
  "Seventy percent of viewers rated the opening scene four or five stars.",["People mostly liked it, probably.","The scene seemed good.","Some viewers said things."],"Specific figures give clear information.")
H('227.d.1.C',3,"At the end of the semester, a student plays her documentary for a panel and explains her production choices. This is a:",
  "formal presentation",["private rehearsal","password reset","tool check"],"A planned showing with explanation is formal.")
H('227.d.1.C',4,"What helps a presentation of a finished video reach an audience effectively?",
  "A brief introduction, a clear structure, and time for questions",["Reading a script word for word at high speed","Skipping the introduction","Hiding the end"],"Structure and interaction keep audiences engaged.")
H('227.d.1.D',3,"A student calls a customer to explain a delay and offers a new delivery date. This builds:",
  "customer trust through public relations",["tension","confusion","mistrust"],"Honest, prompt updates protect relationships.")
H('227.d.1.D',4,"Which action protects a production company's reputation with its community?",
  "Responding politely to questions and complaints",["Ignoring feedback","Deleting all comments","Blaming viewers"],"Courteous replies show professionalism.")
H('227.d.2.A',3,"A student fixes a flickering video clip by checking the cable, the file, and the player one at a time. This shows:",
  "independent critical thinking",["avoidance","carelessness","panic"],"Testing one factor at a time is critical thinking.")
H('227.d.2.A',4,"A group of students must pick the best of three edits. Which approach shows critical thinking?",
  "Compare each edit to the project goals and discuss the evidence",["Choose the longest","Choose the first","Flip a coin"],"Evaluating against goals supports good decisions.")
H('227.d.2.B',3,"A student uses what she learned in a lighting unit to light a new interview set. This shows:",
  "transfer of knowledge",["forgetting","copying exactly","avoiding the task"],"Knowledge from one unit is adapted to a new setting.")
H('227.d.2.B',4,"Which example best shows creating a new product by adapting prior knowledge?",
  "Using editing rhythm lessons from a music video to cut a safety training film",["Repeating the same project","Starting without any plan","Skipping the project"],"Adapting techniques to new content shows transfer.")
H('227.d.3.A',3,"Before a shoot, the crew tapes down cables and checks the light stands. They are following:",
  "workplace safety rules",["fashion rules","menu rules","naming rules"],"Safe setup prevents injuries.")
H('227.d.3.A',4,"Why must everyone know where the fire exits and first-aid kit are?",
  "So help is fast in an emergency",["To decorate","To impress clients","To reduce power use"],"Knowing the locations saves time in an emergency.")
H('227.d.3.B',3,"A student sees a coiled cable across a doorway. What should she do?",
  "Move it or mark it to prevent tripping",["Step over it","Ignore it","Leave it for another shift"],"Resolve hazards right away.")
H('227.d.3.B',4,"A hot light is placed next to a curtain. Which action resolves the safety concern?",
  "Move the light away and keep flammable items clear",["Add another light","Cover the light with cloth","Turn the lights up"],"Heat near fabric can cause a fire.")
H('227.d.4.A',3,"A practicum student arrives early, finishes her tasks, and offers to help others. She shows a strong:",
  "work ethic",["excuse","shortcut","delay"],"Reliability and effort are work ethic.")
H('227.d.4.A',4,"Which behavior shows a productive work ethic during a busy shoot?",
  "Completing assigned duties without needing reminders",["Waiting for orders each time","Taking long breaks","Working slowly"],"Self-direction is valued on crews.")
H('227.d.4.B',3,"A student's documentary uses an interview clip from a classmate. Ethical practice means she:",
  "gives the classmate credit in the credits",["hides the name","changes the voice","keeps quiet"],"Proper credit is ethical conduct.")
H('227.d.4.B',4,"Which action best shows integrity in crediting a team project?",
  "Listing every contributor's role in the credits",["Listing only yourself","Skipping credits","Crediting only friends"],"Accurate credits respect everyone's work.")
H('227.d.4.C',3,"A student wants to blend a clip from a movie into her project. To respect intellectual property, she should:",
  "get permission or use licensed material",["use it without asking","remove the logo","claim it as hers"],"Using others' work requires permission.")
H('227.d.4.C',4,"Reworking a copyrighted photo with filters before using it in a video:",
  "does not remove the owner's rights",["makes it free to use","cancels the copyright","creates a new copyright for you"],"Changes do not erase ownership.")
H('227.d.4.D',3,"Which choice shows safe, legal, and responsible use of technology in a studio?",
  "Using licensed editing software",["Using pirated plug-ins","Sharing passwords","Opening unknown links"],"Licensed tools are legal and safe.")
H('227.d.4.D',4,"A student is asked to download a free copy of a paid editing program. The responsible choice is to:",
  "decline and use the licensed version",["do it quickly","share the file","install it on every computer"],"Illegal copies violate copyright law.")
H('227.d.4.E',3,"Choosing to report a mistake in a client's invoice instead of ignoring it shows:",
  "integrity",["carelessness","greed","laziness"],"Integrity means choosing the ethical course.")
H('227.d.4.E',4,"A student realizes she accidentally recorded over a classmate's clip. The ethical choice is to:",
  "tell the classmate and help recover or recreate it",["hide it","blame someone else","say nothing"],"Honesty is part of integrity.")
H('227.d.4.F',3,"Following all workplace rules, laws, and regulations should be done:",
  "every day, consistently",["only sometimes","only when watched","never"],"Compliance is an everyday habit.")
H('227.d.4.F',4,"Which example shows following regulations in a production job?",
  "Having signed releases from people who appear on camera",["Filming anyone without asking","Using any music","Skipping safety checks"],"Releases protect the production legally.")
H('227.d.5.A',3,"A practicum student works with a professional crew and logs what she learned each week. She is:",
  "documenting learning activities",["hiding work","skipping tasks","avoiding feedback"],"Documentation shows progress.")
H('227.d.5.A',4,"Why does a mentor review a practicum student's work log?",
  "To evaluate learning and guide improvement",["To punish","To waste time","To avoid mentoring"],"Review supports growth.")
H('227.d.5.B',3,"A student learns a color-grading workflow used by her mentoring studio. This is developing:",
  "advanced technical knowledge",["basic hobbies","unrelated skills","beginner chores only"],"Advanced skills prepare students for a career.")
H('227.d.5.B',4,"Which practicum activity best builds advanced technical skill in audio production?",
  "Mixing dialogue, music, and effects for a real project",["Reading a menu","Watching unrelated videos","Moving chairs"],"Real mixing work builds professional skill.")
H('227.d.5.C',3,"A client-based production is a project made for:",
  "a customer who has needs and approvals",["no one","only the student","a game score"],"Client work requires meeting someone else's requirements.")
H('227.d.5.C',4,"What distinguishes client work from a personal project?",
  "The client's goals, approvals, and deadlines guide decisions",["No deadline","No budget","No audience"],"Clients set requirements.")
H('227.d.5.D',3,"Casting, locating equipment, and scheduling the shoot are part of:",
  "pre-production",["post-production","distribution","archiving"],"Planning happens before filming.")
H('227.d.5.D',4,"Which task belongs to pre-production?",
  "Scouting a location and booking the crew",["Color grading","Exporting the final file","Uploading to a site"],"Scouting and booking come before the shoot.")
H('227.d.5.E',3,"Operating the camera and recording sound on the shoot day is part of:",
  "production",["pre-production","marketing","archiving"],"Production is the filming stage.")
H('227.d.5.E',4,"Which is a production-stage task?",
  "Monitoring audio levels while the scene is recorded",["Writing the proposal","Designing the poster","Delivering the file"],"Monitoring audio happens during recording.")
H('227.d.5.F',3,"Editing footage, mixing sound, and exporting for the client is part of:",
  "post-production",["pre-production","casting","scouting"],"Finishing work occurs after filming.")
H('227.d.5.F',4,"The client's player cannot open the file. The student re-exports it in a compatible format. This is a:",
  "post-production adjustment",["casting change","script rewrite","set design"],"Compatibility fixes are made when finishing.")
H('227.d.5.G',3,"A student finishes tasks that used to take her twice as long. This shows:",
  "growth of technical skill",["no change","lost ability","avoidance"],"Increasing speed shows skill growth.")
H('227.d.5.G',4,"Which evidence best shows skill growth over a practicum?",
  "Comparing early projects with recent ones",["Ignoring earlier work","Skipping evaluations","Deleting old files"],"Comparison reveals progress.")
H('227.d.5.H',3,"A student lists the techniques she handles well and those she still needs to practice. She is evaluating her:",
  "strengths and weaknesses",["salary","hobbies","address"],"Self-assessment directs practice.")
H('227.d.5.H',4,"Why identify weaknesses in technical skills?",
  "To plan targeted practice",["To feel discouraged","To avoid feedback","To skip the lab"],"Knowing a weakness helps you improve it.")
H('227.d.5.I',3,"Saving the best finished videos and mentor comments to show employers is collecting:",
  "representative work samples",["junk files","empty folders","unfinished sketches only"],"Samples show real skill.")
H('227.d.5.I',4,"Which sample best represents a student's editing skills?",
  "A polished, finished project with clean cuts and mixed audio",["A blank timeline","A corrupted file","A grocery list"],"Complete, polished work shows ability.")

# ---------- 228 Printing and Imaging Technology I ----------
H('228.d.4',3,"An employee in a print shop uses design software, email, and a job-tracking program to run orders. These are:",
  "advanced technology applications",["hand tools","paper stocks","press plates"],"Software supports modern print production.")
H('228.d.4',4,"A print shop uses a web-to-print portal where customers upload their files. This technology mainly:",
  "speeds up order intake",["lowers paper quality","replaces the press","removes customer files"],"Online portals streamline orders.")
H('228.d.9',3,"Learning to set up a folder, cutter, and press quickly and correctly builds technical skills for:",
  "efficiency",["delay","waste","rework"],"Skilled setup reduces time and errors.")
H('228.d.9',4,"Which habit improves efficiency in a print shop?",
  "Grouping similar jobs to reduce changeovers",["Switching jobs constantly","Skipping setup checks","Printing before proofs"],"Fewer changeovers save time.")
H('228.d.1.A',3,"A print technician carefully proofreads a customer's brochure for spelling errors before printing. She is applying:",
  "English language arts knowledge",["gym skills","music theory","woodworking"],"Language skills prevent costly errors.")
H('228.d.1.A',4,"Which task uses English language arts skills in a print shop?",
  "Writing a clear job ticket with correct instructions",["Calibrating a lens","Sharpening a blade","Mixing ink"],"Clear writing prevents production mistakes.")
H('228.d.1.B',3,"A customer orders 500 flyers at $0.12 each. What is the total cost?",
  "$60",["$6","$600","$50"],"500 x 0.12 = 60.")
H('228.d.1.B',4,"A job needs 1,200 sheets, and 5% extra are added for waste. How many sheets should be pulled?",
  "1,260",["1,205","1,320","1,250"],"1,200 x 1.05 = 1,260.")
H('228.d.2.A',3,"A print shop employee uses simple language to explain paper options to a first-time customer. She is adapting language for the:",
  "audience",["press","ink","cutter"],"Plain words help non-experts.")
H('228.d.2.A',4,"A shop writes a formal quote to a company and a quick text to a regular customer. They are changing:",
  "style for the situation",["paper weight","ink color","press speed"],"Style depends on audience and purpose.")
H('228.d.2.B',3,"Writing job details in order from customer name to due date is:",
  "organizing information",["erasing information","hiding information","guessing"],"Organized details prevent errors.")
H('228.d.2.B',4,"Which job ticket is best organized?",
  "One with customer, quantity, paper, finishing, and due date in clear fields",["A single paragraph of notes","A list in random order","A blank sheet"],"Clear fields speed production.")
H('228.d.2.C',3,"A technician records ink density readings on a sheet and reports them to a supervisor. She is:",
  "communicating observations and data",["ignoring results","guessing","erasing numbers"],"Reporting readings helps quality control.")
H('228.d.2.C',4,"Which report of a quality problem is most useful?",
  "The magenta ink density dropped to 1.1 after 2,000 sheets.",["Colors looked weird.","Something was off.","It's not right."],"Specific observations help fix problems.")
H('228.d.2.D',3,"A student explains each step of the printing process to visiting parents. This is:",
  "presenting information",["avoiding people","hiding steps","ignoring questions"],"Presenting shares knowledge.")
H('228.d.2.D',4,"Which is an informal way to present a printing method?",
  "Showing a coworker how to load the folder at the machine",["Delivering a keynote","Writing a legal brief","Filing taxes"],"Casual demonstration is informal.")
H('228.d.2.E',3,"A customer explains how she wants her wedding invitations folded. The employee writes notes and repeats the details back. This is:",
  "active listening",["interrupting","ignoring","daydreaming"],"Repeating details confirms understanding.")
H('228.d.2.E',4,"What should a press operator do if a job instruction is unclear?",
  "Ask for clarification before starting",["Start anyway","Guess","Wait until the job is wrong"],"Clarify before production.")
H('228.d.2.F',3,"A print shop serves customers from many cultures. A good employee will:",
  "listen with respect to each customer",["rush people","ignore accents","assume needs"],"Respect improves service.")
H('228.d.2.F',4,"A customer who speaks little English wants business cards. A respectful response is to:",
  "speak slowly, use visual samples, and confirm details",["use difficult words","walk away","finish their sentences"],"Visual aids bridge language gaps.")
H('228.d.2.G',3,"Calling a customer promptly to say their order is ready shows:",
  "public relations skills",["poor planning","press skills","folding skills"],"Courtesy builds loyalty.")
H('228.d.2.G',4,"A shop prints an error and quickly reprints it at no charge. This builds:",
  "customer goodwill",["resentment","delay","tension"],"Fixing mistakes protects relationships.")
H('228.d.3.A',3,"A shift team splits a large print run into tasks and works together to finish it. This uses:",
  "critical thinking in a group",["luck","guessing","isolation"],"Groups plan and decide together.")
H('228.d.3.A',4,"Which action shows critical thinking when a press leaves streaks?",
  "Checking the plates, blanket, and ink in turn",["Restarting repeatedly","Ignoring streaks","Adding water at random"],"Testing causes one by one finds the source.")
H('228.d.3.B',3,"Two operators disagree about the best paper for a job. The best step is to:",
  "compare the choices against the customer's needs",["let one yell louder","flip a coin","skip the job"],"Customer needs guide decisions.")
H('228.d.3.B',4,"Which phrase helps a team solve a production problem?",
  "What options do we have to meet the deadline?",["That's not my job.","Not my problem.","You messed it up."],"Solution-focused talk helps.")
H('228.d.5.A',3,"Wearing safety glasses and keeping long hair tied back near a press is following:",
  "workplace safety rules",["style rules","price rules","spelling rules"],"PPE and tied-back hair prevent accidents.")
H('228.d.5.A',4,"Before clearing a jam in a cutter, an operator should first:",
  "shut off and lock out the power",["reach in quickly","wear loose sleeves","keep it running"],"Lockout prevents injury.")
H('228.d.5.B',3,"If there is a chemical spill in the shop, employees should:",
  "follow the posted emergency procedure",["ignore it","mop with paper towels","leave it overnight"],"Procedures limit harm.")
H('228.d.5.B',4,"Where can workers find how to handle a hazardous ink safely?",
  "In the safety data sheet",["On the paper box","On the invoice","On the poster"],"SDS lists hazards and first-aid steps.")
H('228.d.6.A',3,"A shop lead sets daily goals, assigns tasks, and checks progress. She is showing:",
  "leadership skills",["avoidance","laziness","carelessness"],"Leaders guide the team toward goals.")
H('228.d.6.A',4,"When a rush order arrives, a good leader will:",
  "rearrange tasks and inform the team",["ignore the order","blame the customer","stop all work"],"Leaders adapt plans.")
H('228.d.6.B',3,"Two operators argue over who gets the folder first. A teammate suggests a schedule that fits both jobs. This is:",
  "conflict management",["avoidance","competition","blame"],"Compromise solves conflict.")
H('228.d.6.B',4,"Which statement supports teamwork?",
  "Let's schedule both jobs so each is on time.",["It's my turn only.","I'm not sharing.","Figure it out yourself."],"Cooperative language keeps the team working.")
H('228.d.6.C',3,"Thanking a coworker for helping with a rush job helps build:",
  "good working relationships",["tension","distance","resentment"],"Appreciation builds trust.")
H('228.d.6.C',4,"Which is constructive feedback on a trimmed stack?",
  "The cuts are clean; check the guide for the last few sheets.",["That's bad.","You can't cut.","Never mind."],"Specific, kind feedback helps.")
H('228.d.6.D',3,"A supervisor lists topics and time limits before a staff meeting. She is:",
  "preparing goals for the meeting",["skipping the meeting","wasting time","avoiding work"],"An agenda focuses the meeting.")
H('228.d.6.D',4,"Which goal fits a weekly production meeting?",
  "Decide the order of jobs for next week",["Talk about movies","Tell jokes","Argue about parking"],"Meeting goals should be work-related.")
H('228.d.6.E',3,"During a shop meeting, employees should:",
  "stay on topic and share updates",["leave early","use phones","talk over others"],"Focus accomplishes tasks.")
H('228.d.6.E',4,"After a meeting, which step keeps tasks moving?",
  "Sending notes that list who will do what",["Saying nothing","Deleting the agenda","Waiting until next week"],"Written follow-up creates accountability.")
H('228.d.6.F',3,"A veteran press operator shows a new hire how to set up a folder. This is:",
  "mentoring",["competing","avoiding","copying"],"Mentors teach and inspire.")
H('228.d.6.F',4,"A good mentor in a print shop:",
  "explains the why behind each step patiently",["hides tricks","corrects harshly","avoids questions"],"Patient explanation builds skill.")
H('228.d.7.A',3,"A print shop employee keeps customers' artwork and personal data private. This shows:",
  "ethical conduct",["gossip","carelessness","competition"],"Confidentiality is ethical conduct.")
H('228.d.7.A',4,"A customer's unreleased product design is on a proof. The employee should:",
  "keep it confidential",["post it online","show other customers","take a photo for fun"],"Client information is private.")
H('228.d.7.B',3,"Copying a whole book for sale without permission violates:",
  "copyright law",["paper rules","ink rules","safety rules"],"Copyright protects authors.")
H('228.d.7.B',4,"A customer asks a shop to duplicate a published workbook for a class of 30. The shop should first:",
  "verify copyright permission or fair use",["print immediately","remove the title","charge extra"],"Duplication may need permission.")
H('228.d.7.C',3,"Using a photograph in a flyer only after asking the photographer shows:",
  "respect for intellectual property",["disrespect","carelessness","theft"],"Permission respects creators.")
H('228.d.7.C',4,"Which action respects intellectual property when designing a poster?",
  "Using licensed or original images",["Copying any image from a search","Cropping out a watermark","Claiming a stock photo is yours"],"Licensed images are legal to use.")
H('228.d.7.D',3,"A school's acceptable use policy forbids using lab printers for personal business. A student should:",
  "follow the policy",["print anyway","hide it","ask a friend"],"Policies set the rules for equipment use.")
H('228.d.7.D',4,"Which action shows good etiquette with a shared printer?",
  "Collecting only your pages and refilling the paper",["Printing hundreds of pages","Leaving jams","Changing others' settings"],"Courtesy keeps shared equipment ready.")
H('228.d.7.E',3,"A Creative Commons license tells others:",
  "how they may use and share a work",["that no one may see the work","that the work is deleted","how to print it"],"CC licenses specify permitted uses.")
H('228.d.7.E',4,"A designer finds a photo with a Creative Commons license that requires attribution. She must:",
  "credit the creator as the license requires",["remove the license","sell it as her own","change its name"],"Attribution is a common requirement.")
H('228.d.8.A',3,"A print student keeps samples of her best brochures and a resume in a folder. She is maintaining a:",
  "portfolio",["scrapbook of trash","menu","tax form"],"Portfolios show skills.")
H('228.d.8.A',4,"Why update a print portfolio regularly?",
  "To show your newest and best work to employers",["To hide old samples","To avoid interviews","To use more ink"],"Current work shows growth.")
H('228.d.8.B',3,"A graduate compares two job offers by pay, benefits, and training. She is:",
  "evaluating employment opportunities",["ignoring details","picking at random","avoiding work"],"Comparing options supports good choices.")
H('228.d.8.B',4,"Which factor matters most when comparing two print jobs for long-term growth?",
  "Training and advancement chances",["The color of the lobby","The brand of the vending machine","The parking sign"],"Advancement shapes a career.")
H('228.d.8.C',3,"A trained printer opens her own copy and print shop. This is:",
  "entrepreneurship",["retirement","an internship","unemployment"],"Entrepreneurs run their own businesses.")
H('228.d.8.C',4,"A challenge of owning a small print shop is:",
  "managing equipment costs and finding customers",["having no customers needed","a guaranteed salary","no expenses"],"Owners handle sales and costs.")
H('228.d.10.A',3,"Offset lithography, digital printing, and screen printing are different:",
  "printing systems",["paper sizes","ink brands","cutters"],"Each system has its uses.")
H('228.d.10.A',4,"For a short run of 50 full-color flyers, which system is usually most economical?",
  "Digital printing",["Large offset setup","Letterpress","Gravure"],"Digital needs little setup for short runs.")
H('228.d.10.B',3,"Scheduling jobs, checking proofs, and tracking supplies is:",
  "managing the printing process",["only folding","only cutting","only designing"],"Management coordinates all steps.")
H('228.d.10.B',4,"A job is delayed because ink was not ordered. This is a failure in:",
  "managing the printing process",["design talent","paper color","customer choice"],"Supply planning is part of process management.")
H('228.d.10.C',3,"Setting up a customer's file with correct size, bleed, and resolution is:",
  "preparing customer documents",["cutting paper","packaging","binding"],"Prepress readies the file.")
H('228.d.10.C',4,"A customer's file has no bleed. The prepress technician should:",
  "extend the artwork beyond the trim line",["print it as is","shrink it","change the colors"],"Bleed prevents white edges after trimming.")
H('228.d.10.D',3,"Choosing offset for a 10,000-copy run instead of a desktop printer is selecting the:",
  "appropriate printing process",["wrong tool","lowest quality","slowest option"],"Process choice depends on quantity and quality.")
H('228.d.10.D',4,"For printing on plastic bags in high volume, a suitable process is:",
  "flexography or screen printing",["laser desktop printing","pencil","photocopying only"],"Flexo and screen printing handle many surfaces.")
H('228.d.10.E',3,"Cutting, folding, and trimming printed sheets are:",
  "binding or finishing processes",["design steps","ink mixing steps","scanning steps"],"Finishing completes the product.")
H('228.d.10.E',4,"Why is a cutter's safety guard used?",
  "To protect hands from the blade",["To speed up cutting","To hold ink","To dry paper"],"Guards prevent injuries.")
H('228.d.10.F',3,"A stock sheet is 20 by 24 inches. How many 5 by 6 inch pieces fit if cut without waste?",
  "16",["8","20","12"],"(20/5) x (24/6) = 4 x 4 = 16.")
H('228.d.10.F',4,"A job needs 800 pieces and 8 pieces fit on each stock sheet. How many sheets are needed?",
  "100",["80","64","800"],"800 / 8 = 100.")
H('228.d.10.G',3,"A brochure with two parallel folds in the same direction is a:",
  "accordion fold",["letter fold","gate fold","single fold"],"Accordion folds zigzag.")
H('228.d.10.G',4,"A letter fold has how many panels?",
  "Three",["Two","Four","Six"],"A letter fold makes three panels.")
H('228.d.10.H',3,"A booklet held by staples through the folded spine uses:",
  "saddle stitching",["perfect binding","spiral binding","case binding"],"Saddle stitching staples through the fold.")
H('228.d.10.H',4,"A thick paperback with a glued, squared spine is bound by:",
  "perfect binding",["saddle stitching","side stitching","comb binding"],"Perfect binding uses glue on the spine.")
H('228.d.10.I',3,"Gluing the top edge of a stack of sheets to make a notepad is:",
  "padding",["laminating","die cutting","embossing"],"Padding glues sheets into tablets.")
H('228.d.10.I',4,"A padding press compresses the stack while the glue:",
  "dries",["prints","burns","melts away"],"Pressing holds sheets while adhesive sets.")
H('228.d.10.J',3,"Raising a design on a business card so it can be felt is:",
  "embossing",["laminating","foil stamping","folding"],"Embossing raises the surface.")
H('228.d.10.J',4,"Applying a thin plastic film to protect a menu is:",
  "laminating",["die cutting","embossing","stitching"],"Lamination adds protection.")
H('228.d.10.K',3,"Printing sticky labels in rolls is part of printing:",
  "paper labels",["envelopes only","maps only","signs only"],"Labels are a common product.")
H('228.d.10.K',4,"Multi-part carbonless invoices are called:",
  "bulk or business forms",["posters","brochures","calendars"],"Forms use multiple copies.")
H('228.d.10.L',3,"Sending a heavy box of printed books requires checking:",
  "postal regulations",["fashion trends","menu items","film ratings"],"Mail rules set size and weight limits.")
H('228.d.10.L',4,"Why check postal rules before printing mailers?",
  "Size, weight, and layout affect postage and acceptance",["Postage is free","Rules never change","Paper color is irrelevant"],"Meeting rules avoids rejected mailings.")
H('228.d.10.M',3,"Boxing printed catalogs and labeling them correctly for delivery meets the customer's need for:",
  "packaging and shipping",["design","scanning","mixing ink"],"Proper packaging prevents damage.")
H('228.d.10.M',4,"A customer wants materials delivered to three offices. The shop should:",
  "divide, label, and ship to each address",["send everything to one","ask them to pick up","ignore addresses"],"Accurate labeling meets customer needs.")

# ---------- 229 Practicum in Printing and Imaging Technology ----------
H('229.d.2',3,"A press operator keeps getting uneven ink coverage and checks the settings, plate, and paper one at a time. This is:",
  "problem solving",["panic","avoidance","guessing"],"Systematic checking is problem solving.")
H('229.d.2',4,"Which approach best solves a repeated registration problem?",
  "Record the settings, change one variable at a time, and compare results",["Change everything at once","Ignore it","Blame the paper"],"One change at a time identifies the cause.")
H('229.d.3',3,"A practicum student wears safety glasses and also keeps customer files locked on the shop computer. These show proper:",
  "safety and security techniques",["fashion choices","paper sizes","ink colors"],"Safety protects people; security protects data.")
H('229.d.3',4,"Which action protects customer data in a print shop?",
  "Locking the computer and using a strong password",["Sharing logins","Leaving files open","Emailing them to everyone"],"Security protects client information.")
H('229.d.1.A',3,"A student gives clear verbal instructions and uses eye contact when training a new coworker. This is:",
  "verbal and non-verbal communication",["silent work","guesswork","avoidance"],"Words and body language work together.")
H('229.d.1.A',4,"Which shows effective communication at a loud press?",
  "Using agreed hand signals along with short phrases",["Shouting random words","Whispering","Leaving notes under a machine"],"Signals work over noise.")
H('229.d.1.B',3,"A student shows the class how to plan a project, using slides and a short demonstration. This is:",
  "presenting information formally",["hiding information","avoiding questions","ignoring the topic"],"Planned slides and demos are formal.")
H('229.d.1.B',4,"Presenting a quick process tip to a coworker at the machine is:",
  "informal presentation",["formal presentation","legal filing","tax work"],"Casual demonstration is informal.")
H('229.d.1.C',3,"A client explains a design change. The student takes notes, asks questions, and confirms. This is:",
  "active listening",["interrupting","ignoring","daydreaming"],"Confirming shows understanding.")
H('229.d.1.C',4,"Which response clarifies unclear client feedback?",
  "Ask for an example of what they want changed",["Say nothing","Redo everything","Pretend to understand"],"Examples clarify requests.")
H('229.d.1.D',3,"Politely resolving a customer's complaint about a smudged order shows:",
  "public relations skills",["poor service","pressroom skills","bindery skills"],"Good PR retains customers.")
H('229.d.1.D',4,"A shop publishes a thank-you note to repeat customers. This helps maintain:",
  "external customer relations",["internal errors","press speed","stock levels"],"Gratitude builds loyalty.")
H('229.d.4.A',3,"A practicum student arrives on time and completes assigned jobs without reminders. She shows a:",
  "positive work ethic",["bad habit","delay","shortcut"],"Reliability reflects work ethic.")
H('229.d.4.A',4,"Which behavior reflects productive work habits during a rush week?",
  "Staying organized and finishing tasks to standard",["Working carelessly","Taking extra breaks","Leaving a mess"],"Quality and organization matter.")
H('229.d.4.B',3,"A shop employee keeps customers' unreleased product designs private. This is:",
  "maintaining client confidentiality",["gossip","carelessness","competition"],"Confidentiality is an ethical duty.")
H('229.d.4.B',4,"A friend asks to see a client's unpublished catalog proofs. The employee should:",
  "decline politely to protect confidentiality",["share them","post them online","take photos"],"Client files are private.")
H('229.d.4.C',3,"A customer asks a shop to copy an entire textbook. The shop should first check:",
  "copyright and fair use",["paper color","ink density","the folder"],"Reproduction must follow copyright law.")
H('229.d.4.C',4,"Fair use may allow:",
  "limited copying for purposes such as teaching or criticism",["unlimited copying","selling copies","claiming authorship"],"Fair use has limits and factors.")
H('229.d.4.D',3,"A Creative Commons license that says 'share alike' means others may:",
  "share new versions under the same license",["claim ownership","remove credit","charge any price"],"ShareAlike keeps the same terms.")
H('229.d.4.D',4,"A print designer uses a CC image that forbids commercial use in a store's sale flyer. This:",
  "violates the license",["is allowed","is required","is attributed"],"Commercial use breaks a NonCommercial license.")
H('229.d.4.E',3,"Following workplace laws and rules should be:",
  "consistent and ongoing",["occasional","optional","ignored"],"Compliance is continuous.")
H('229.d.4.E',4,"Which is an example of compliance in a print shop?",
  "Storing solvents in approved, labeled containers",["Leaving solvents open","Pouring them down any drain","Mixing chemicals randomly"],"Regulated storage prevents hazards.")
H('229.d.5.A',3,"A practicum student works under a supervisor at a print shop and logs weekly learning. She is:",
  "documenting and evaluating learning",["hiding progress","skipping work","avoiding review"],"Logs show growth.")
H('229.d.5.A',4,"Why does a supervisor sign a student's practicum log?",
  "To verify work and give feedback",["To waste time","To avoid training","To raise prices"],"Verification supports learning.")
H('229.d.5.B',3,"A practicum student runs offset, digital, and wide-format jobs in the shop. She is practicing:",
  "various printing systems",["one tool only","only design","only shipping"],"Experience across systems builds skill.")
H('229.d.5.B',4,"Which task shows practice with a digital printing system?",
  "Preparing a variable-data mailer on a digital press",["Cutting a rubber stamp","Mixing offset ink","Developing film"],"Variable data is a digital strength.")
H('229.d.5.C',3,"Choosing screen printing for T-shirts and offset for brochures shows using the:",
  "appropriate printing process",["wrong method","same method always","least effective method"],"Process matches product.")
H('229.d.5.C',4,"A student now selects processes quickly and accurately, showing increased:",
  "fluency",["confusion","delay","guesswork"],"Fluency is smooth, accurate skill.")
H('229.d.5.D',3,"Setting a cutter's backgauge to trim posters to size is part of:",
  "binding processes",["design","scanning","ink mixing"],"Cutting is a finishing step.")
H('229.d.5.D',4,"Which sequence is typical for finishing a printed flyer?",
  "Cut, fold, and trim",["Fold, then print","Print, then design","Package, then print"],"Finishing follows printing.")
H('229.d.5.E',3,"Adjusting a folder to make a tri-fold brochure on thicker stock is:",
  "adapting equipment for a fold",["avoiding the job","changing the design","skipping the fold"],"Thicker stock needs adjustments.")
H('229.d.5.E',4,"If folds crack on heavy cover stock, a common fix is to:",
  "score the paper before folding",["fold it faster","use more ink","trim the edge"],"Scoring prevents cracking.")
H('229.d.5.F',3,"Applying a glossy film to protect menus is:",
  "laminating",["embossing","folding","stitching"],"Lamination adds protection.")
H('229.d.5.F',4,"A metallic logo pressed onto a cover with heat is called:",
  "foil stamping",["laminating","padding","die cutting"],"Foil stamping applies foil with heat and pressure.")
H('229.d.5.G',3,"Boxing and labeling a customer's order so it arrives safely meets their needs for:",
  "packaging and shipping",["design","scanning","ink mixing"],"Proper shipping protects the order.")
H('229.d.5.G',4,"A customer needs three separate shipments to different cities. The shop:",
  "labels each package with its own address",["sends all to one","asks the customer to ship","skips labels"],"Accurate labels get orders to the right place.")
H('229.d.5.H',3,"Learning to calibrate a color-managed printer is developing:",
  "advanced technical knowledge",["basic hobbies","unrelated skills","beginner chores"],"Calibration is a professional skill.")
H('229.d.5.H',4,"Which practicum task builds advanced printing knowledge?",
  "Profiling a press for accurate color matching",["Sweeping floors only","Reading a magazine","Moving chairs"],"Color management is an advanced skill.")
H('229.d.5.I',3,"A student runs jobs in half the time she did early in the year. This shows:",
  "growth of technical skills",["decline","no change","lost skill"],"Speed with accuracy shows growth.")
H('229.d.5.I',4,"Which evidence best shows growth in print skills?",
  "Quality checks that improved over the semester",["Skipped checks","More waste","Missed deadlines"],"Better quality shows progress.")
H('229.d.5.J',3,"A student lists skills she does well and those needing practice. She is evaluating her:",
  "strengths and weaknesses",["salary","address","hobbies"],"Self-evaluation guides improvement.")
H('229.d.5.J',4,"Why should practicum students evaluate their proficiency?",
  "To set goals for improvement",["To get discouraged","To avoid work","To hide problems"],"Honest evaluation drives growth.")
H('229.d.5.K',3,"Keeping samples of finished jobs and supervisor comments is collecting:",
  "representative work samples",["trash","blank pages","old bills"],"Samples demonstrate ability.")
H('229.d.5.K',4,"Which item is a strong work sample for a print career?",
  "A finished, well-trimmed brochure with clean color",["A crumpled sheet","A blank page","A scrap of waste"],"Polished work shows skill.")

# ---------- 230 Commercial Photography I ----------
H('230.d.4',3,"A photographer organizes client files, answers email, and keeps a calendar on her phone. She is using:",
  "personal information management",["film developing","studio lighting","framing"],"PIM tools organize business tasks.")
H('230.d.4',4,"Which practice helps a photographer manage hundreds of image files?",
  "Using consistent folder and file names",["Saving all to one folder","Renaming randomly","Deleting after export"],"Consistent names make files easy to find.")
H('230.d.5',3,"Cameras, lenses, lights, and editing software are part of a commercial photographer's:",
  "systems",["menu","budget only","address list"],"Commercial photography systems include gear and software.")
H('230.d.5',4,"A commercial photography system includes capturing, editing, and:",
  "delivering images",["only printing recipes","only costume design","only set building"],"The workflow ends with delivery.")
H('230.d.1.A',3,"A photographer writes a clear email to a client confirming the shoot date and location. She is applying:",
  "English language arts knowledge",["gym skills","metal shop skills","music theory"],"Clear writing supports business.")
H('230.d.1.A',4,"Which task uses English language arts skills in photography?",
  "Writing an accurate caption and credit line",["Cleaning a lens","Charging a battery","Setting the white balance"],"Captions require careful writing.")
H('230.d.1.B',3,"A photographer charges $150 per hour and works 4 hours. What is the fee?",
  "$600",["$154","$300","$450"],"150 x 4 = 600.")
H('230.d.1.B',4,"A photographer shoots 480 images and keeps 25%. How many images are kept?",
  "120",["25","240","96"],"480 x 0.25 = 120.")
H('230.d.2.A',3,"A photographer explains lighting to a child using simple words. She is adapting language to her:",
  "audience",["lens","tripod","flash"],"Language should match the listener.")
H('230.d.2.A',4,"A photographer writes casually to a friend and formally to a magazine editor. This is adjusting:",
  "tone for purpose and audience",["shutter speed","aperture","white balance"],"Tone depends on the situation.")
H('230.d.2.B',3,"Listing shots needed for a wedding in order of the day is:",
  "organizing information",["erasing information","ignoring information","guessing"],"Organized plans prevent missed shots.")
H('230.d.2.B',4,"Which shot list is best organized?",
  "One grouped by time and location with names of family groups",["A random list","A blank page","A single sentence"],"Grouping by time and place helps efficiency.")
H('230.d.2.C',3,"A photographer reports that the best-performing images had warm lighting. She is communicating:",
  "observations and data",["fiction","rumors","guesses"],"Sharing findings helps decisions.")
H('230.d.2.C',4,"Which statement communicates an observation clearly?",
  "The portraits shot near the window were sharper at f/4 than at f/8 indoors.",["Some pictures were nicer.","It looked okay.","I think it worked."],"Specific details help others understand.")
H('230.d.2.D',3,"A student shows her portfolio to a class and explains each choice. This is:",
  "presenting information",["hiding work","avoiding questions","ignoring people"],"Presenting shares work and reasoning.")
H('230.d.2.D',4,"Reviewing prints casually with a classmate at the table is:",
  "informal presentation",["a formal keynote","a legal filing","a tax return"],"Casual sharing is informal.")
H('230.d.2.E',3,"A client describes the mood they want. The photographer takes notes and repeats the details. This is:",
  "active listening",["interrupting","ignoring","daydreaming"],"Repeating confirms understanding.")
H('230.d.2.F',3,"A photographer works with clients of many backgrounds. She should:",
  "listen and speak respectfully to each",["use stereotypes","ignore requests","rush people"],"Respect builds trust.")
H('230.d.2.F',4,"A client's family has cultural traditions for portraits. A professional will:",
  "ask about them and respect them",["ignore them","change them","joke about them"],"Cultural respect shows professionalism.")
H('230.d.2.G',3,"A photographer thanks a client, sends a prompt gallery, and follows up. This builds:",
  "customer relations",["tension","distance","mistrust"],"Prompt service builds goodwill.")
H('230.d.2.G',4,"A negative review is posted about late delivery. A good response is to:",
  "apologize, explain, and offer to fix it",["argue publicly","delete the account","ignore it"],"Calm replies protect reputation.")
H('230.d.3.A',3,"A photo team debates which image to submit to a contest. They compare each to the rules. This is:",
  "critical thinking in a group",["luck","guessing","isolation"],"Evidence-based decisions are critical thinking.")
H('230.d.3.A',4,"A photographer notices blurry images in every shot. Critical thinking suggests she:",
  "test shutter speed, focus, and stabilization",["buy a new camera","stop shooting","blame the subject"],"Test variables to find the cause.")
H('230.d.3.B',3,"Two assistants disagree about where to place a light. A good approach is to:",
  "test both and compare the results",["argue louder","ignore one","guess"],"Testing resolves disagreements.")
H('230.d.3.B',4,"Which statement helps a group solve a problem?",
  "Let's try each option and see which works best.",["It's my way.","I won't help.","That's silly."],"Collaborative language helps.")
H('230.d.6.A',3,"In a photo studio, taping down cables and securing light stands is following:",
  "safety rules",["style rules","price rules","spelling rules"],"Secured gear prevents injuries.")
H('230.d.6.A',4,"A strobe light's stand is on a slippery floor. A safe step is to:",
  "add a sandbag and secure the legs",["leave it","tape a note","raise it higher"],"Weight stabilizes stands.")
H('230.d.6.B',3,"If a fire alarm sounds in the studio, the photographer should:",
  "leave by the marked exit",["keep shooting","hide","remove the lights"],"Follow the emergency plan.")
H('230.d.6.B',4,"Why should chemicals in a darkroom be stored properly?",
  "To prevent spills, fumes, and accidents",["To save space","To hide them","To make them stronger"],"Proper storage prevents hazards.")
H('230.d.7.A',3,"A lead photographer sets the schedule, assigns roles, and keeps the team on task. She is showing:",
  "leadership skills",["avoidance","laziness","carelessness"],"Leaders guide the team toward goals.")
H('230.d.7.A',4,"When a shoot is running late, a good leader will:",
  "adjust the schedule and inform the team",["ignore it","blame the client","stop working"],"Leaders adapt plans.")
H('230.d.7.B',3,"Two assistants disagree about the shot order. A teammate suggests a compromise. This is:",
  "conflict management",["avoidance","blame","competition"],"Compromise resolves conflict.")
H('230.d.7.B',4,"Which phrase supports teamwork on a shoot?",
  "How can we get both shots done on time?",["That's your problem.","I won't help.","You're wrong."],"Solution-focused language supports teams.")
H('230.d.7.C',3,"Thanking an assistant for carrying equipment builds:",
  "good working relationships",["tension","distance","resentment"],"Appreciation builds trust.")
H('230.d.7.C',4,"Which feedback is constructive on a portrait?",
  "The expression is great; try lowering the fill light slightly.",["Awful.","Why bother.","Not good."],"Specific, kind feedback helps.")
H('230.d.7.D',3,"Planning the goals and shot list before a team meeting is:",
  "preparing for the meeting",["avoiding work","wasting time","skipping work"],"Preparation makes meetings effective.")
H('230.d.7.D',4,"Which goal suits a pre-shoot meeting?",
  "Confirm roles, equipment, and timing",["Tell jokes","Discuss the weather only","Plan lunch only"],"Meeting goals should support the job.")
H('230.d.7.E',3,"During a team meeting, a good participant will:",
  "stay on topic and contribute ideas",["scroll a phone","interrupt others","leave early"],"Focus helps accomplish tasks.")
H('230.d.7.E',4,"After a meeting, which step ensures follow-through?",
  "Send notes listing action items and deadlines",["Say nothing","Delete notes","Wait a month"],"Written follow-up creates accountability.")
H('230.d.7.F',3,"An experienced photographer teaches a student how to meter light. This is:",
  "mentoring",["competing","copying","hiding"],"Mentors teach and inspire.")
H('230.d.7.F',4,"A good mentor in photography:",
  "gives feedback patiently and shares techniques",["keeps secrets","criticizes harshly","avoids questions"],"Patience builds skill.")
H('230.d.8.A',3,"A photographer gets signed model releases before publishing portraits. This shows:",
  "ethical conduct",["carelessness","greed","gossip"],"Releases respect people's rights.")
H('230.d.8.A',4,"A photographer shoots a stranger's child at a park. The ethical choice is to:",
  "ask the parent for permission before publishing",["post it online","sell it","ignore it"],"Consent matters, especially for minors.")
H('230.d.8.B',3,"A photographer owns the copyright to her photos unless:",
  "she transfers or licenses it in a contract",["a client uses them","she posts them","she prints them"],"Contracts can transfer or license rights.")
H('230.d.8.B',4,"A client wants to print the photos on a billboard though the contract allowed web use only. The photographer should:",
  "discuss a new license and fee",["allow it for free","ignore it","delete the photos"],"Use beyond the license needs a new agreement.")
H('230.d.8.C',3,"Editing and compositing someone else's photograph into a collage requires:",
  "permission or a proper license",["no permission","removing credit","claiming authorship"],"Altering a work does not remove rights.")
H('230.d.8.C',4,"Which respects intellectual property when assembling a composite?",
  "Using only your own images or licensed ones",["Using any image online","Removing watermarks","Claiming stock as yours"],"Licensed or original images are safe.")
H('230.d.8.D',3,"A lab's acceptable use policy forbids installing personal software. A student should:",
  "follow the policy",["install anyway","hide it","ask a friend to do it"],"Policies protect shared systems.")
H('230.d.8.D',4,"Which is good etiquette in a shared photo lab?",
  "Clean up the workstation and save files to your folder",["Leave files on desktops","Use others' accounts","Change settings for everyone"],"Courtesy keeps shared spaces ready.")
H('230.d.9.A',3,"A photography student keeps a printed and online portfolio of her best images. She is:",
  "maintaining a portfolio",["hiding work","wasting paper","avoiding feedback"],"Portfolios show skills to clients.")
H('230.d.9.A',4,"What should a commercial photography portfolio show?",
  "A range of strong work targeted to the type of clients you want",["Every photo you took","Only blurry shots","Only family snapshots"],"Curated work attracts the right clients.")
H('230.d.9.B',3,"A graduate compares job offers by pay, benefits, and growth chances. She is:",
  "evaluating employment opportunities",["ignoring details","picking at random","avoiding work"],"Comparing supports good decisions.")
H('230.d.9.B',4,"Which factor is important when choosing between a studio job and freelance work?",
  "Income stability and benefits",["The color of the camera strap","The studio's lobby plant","The brand of cameras only"],"Stability affects planning.")
H('230.d.10.A',3,"Scheduling shoots, edits, and deliveries so work is finished on time is:",
  "planning and time management",["procrastination","guessing","avoidance"],"Planning ensures deadlines are met.")
H('230.d.10.A',4,"Which approach helps a photographer meet an edit deadline?",
  "Break the work into steps with daily targets",["Wait until the last day","Skip culling","Edit without a plan"],"Daily targets make progress steady.")
H('230.d.10.B',3,"A freelance photographer prices a job by adding time, equipment, and editing costs. She is:",
  "creating a quote",["ignoring costs","guessing","skipping work"],"Quotes include all expenses.")
H('230.d.10.B',4,"Which cost should be included in a freelance photography quote?",
  "Editing time and image delivery",["Only the shoot time","Nothing for editing","Nothing for travel"],"Edit time is part of the work.")
H('230.d.11.A',3,"A photographer creates images of products for a catalog. She is creating photographs for a:",
  "defined purpose",["random purpose","no purpose","hidden purpose"],"Commercial photos have specific goals.")
H('230.d.11.A',4,"A real estate photographer shoots a house to attract buyers. Her purpose is to:",
  "market the property",["teach cooking","sell cars","create a menu"],"The images support a sale.")
H('230.d.11.B',3,"Using line, color, and balance to improve a product photo applies the:",
  "elements and principles of art",["rules of finance","laws of aviation","steps of plumbing"],"Art principles guide composition.")
H('230.d.11.B',4,"Placing a bright product against a muted background uses:",
  "contrast",["noise","lag","grain"],"Contrast makes a subject stand out.")
H('230.d.11.C',3,"Working with models, props, and a set to create a commercial image applies:",
  "principles of commercial photography",["accounting rules","coding rules","carpentry"],"Direction and styling are commercial skills.")
H('230.d.11.C',4,"What is a main job of a stylist on a product shoot?",
  "Arrange props and details so the product looks its best",["Edit the contract","Pay the invoices","Develop film"],"Styling enhances the scene.")
H('230.d.11.D',3,"A long telephoto lens is useful for:",
  "compressing distance and isolating distant subjects",["wide room shots","macro of tiny objects only","shooting underwater only"],"Telephoto lenses magnify far subjects.")
H('230.d.11.D',4,"Which lens is best for photographing a small piece of jewelry in detail?",
  "A macro lens",["A fisheye lens","A super-wide lens","A mirror lens"],"Macro lenses focus close.")
H('230.d.11.E',3,"Placing the subject along the lines of a grid instead of the exact center follows the:",
  "rule of thirds",["rule of halves","rule of zero","rule of ten"],"The rule of thirds improves composition.")
H('230.d.11.E',4,"Leaving open space in the direction a subject is looking:",
  "gives the image balance",["wastes the frame","hides the subject","blurs the photo"],"Lead room balances the composition.")
H('230.d.11.F',3,"Converting a color image to monochrome for dramatic contrast is working in:",
  "digital black and white",["film color","negative only","paper only"],"Black-and-white conversion emphasizes tone.")
H('230.d.11.F',4,"A photographer adjusts white balance to correct a yellow tint. She is working with:",
  "digital color photography",["darkroom chemistry","film loading","paper cutting"],"White balance corrects color casts.")
H('230.d.11.G',3,"Three-point lighting uses a key light, a fill light, and a:",
  "back light",["flashlight","night light","red light"],"The back light separates the subject.")
H('230.d.11.G',4,"The main light in three-point lighting is called the:",
  "key light",["fill light","kicker only","ambient"],"The key light provides the main illumination.")
H('230.d.11.H',3,"Sharp focus, proper exposure, and clean composition make a photograph:",
  "professional quality",["amateur","damaged","blurry"],"Technical and aesthetic quality define professional work.")
H('230.d.11.H',4,"A client rejects images with underexposed faces. To produce professional work next time, the photographer should:",
  "check exposure and use fill light",["shoot faster","ignore the histogram","use auto everything"],"Exposure control prevents dark faces.")
H('230.d.11.I',3,"A glossy surface that reflects light and makes colors look vivid is a:",
  "photographic paper finish",["camera body","lens hood","tripod leg"],"Gloss is a common finish.")
H('230.d.11.I',4,"For a fine art print with a soft, non-reflective look, which paper is a good choice?",
  "Matte paper",["High-gloss paper","Newsprint","Tracing paper"],"Matte reduces glare.")
H('230.d.11.J',3,"A border cut around a photo inside a frame is called a:",
  "mat",["lens","filter","softbox"],"Mats separate the print from the frame.")
H('230.d.11.J',4,"Why use acid-free mat board for archival prints?",
  "It prevents yellowing and damage over time",["It is cheaper","It is heavier","It is brighter"],"Acid-free materials protect prints.")
H('230.d.11.K',3,"Photographers who use current, industry-standard software are using:",
  "appropriate production tools",["outdated tools","random tools","no tools"],"Using standard tools helps collaboration.")
H('230.d.11.K',4,"Which tool is an industry-standard way to edit raw images?",
  "Professional photo-editing software",["A spreadsheet","A calculator","A word processor"],"Photo editors process raw files.")
H('230.d.11.L',3,"A photographer reviews her images against composition, lighting, and client goals. She is:",
  "evaluating photographs",["ignoring results","guessing","erasing files"],"Evaluation uses criteria.")
H('230.d.11.L',4,"Which question helps evaluate a commercial photo?",
  "Does it communicate the product's key benefit clearly?",["Is it big?","Is the file name long?","Is the date recent?"],"Commercial success depends on communicating the message.")
H('230.d.11.M',3,"A web image needs a small file size, while a billboard print needs:",
  "high resolution",["low resolution","no resolution","only a thumbnail"],"Large prints need more pixels.")
H('230.d.11.M',4,"Which file format is best for a high-quality image with layers for further editing?",
  "TIFF or PSD",["Low-quality JPEG only","GIF only","Plain text"],"TIFF and PSD preserve quality and layers.")

# ---------- 231 Practicum in Commercial Photography ----------
H('231.d.2',3,"A photographer's studio lights keep tripping the circuit. She checks wattage, circuits, and extension cords. This is:",
  "problem solving",["panic","giving up","guessing"],"Systematic checks solve problems.")
H('231.d.2',4,"Which approach is best for solving an inconsistent color problem across a set of images?",
  "Check lighting, white balance, and monitor calibration one at a time",["Change everything","Ignore it","Blame the camera"],"Isolating variables finds the cause.")
H('231.d.3',3,"A practicum student unplugs lights before moving them and wears gloves near hot lamps. These are:",
  "safety techniques",["fashion choices","pricing steps","paper sizes"],"Safe handling prevents burns and shocks.")
H('231.d.3',4,"Which safety habit is important in a studio with many cables?",
  "Taping cables and keeping aisles clear",["Draping cables loosely","Overloading outlets","Ignoring spills"],"Clear aisles prevent trips.")
H('231.d.1.A',3,"A student gives a model clear directions using words and hand gestures. This is:",
  "verbal and non-verbal communication",["silent work","avoidance","guessing"],"Gestures and words guide a subject.")
H('231.d.1.A',4,"Which technique keeps a client at ease during a portrait session?",
  "A calm voice and friendly body language",["Silence and frowning","Shouting orders","Checking your phone"],"Tone and posture affect comfort.")
H('231.d.1.B',3,"A student studies website traffic from her gallery and explains the results to a client. She is:",
  "interpreting and communicating data",["ignoring numbers","guessing","hiding results"],"Reporting data informs decisions.")
H('231.d.1.B',4,"Which statement communicates analytics clearly?",
  "Visits increased from 300 to 450 after the new gallery launched.",["More people came maybe.","It seemed busier.","Things changed."],"Specific numbers are clear.")
H('231.d.1.C',3,"A student presents her portfolio to a panel with slides and Q&A. This is:",
  "a formal presentation",["a private note","a lens check","a sound test"],"Planned slides and questions are formal.")
H('231.d.1.C',4,"Which helps a portfolio presentation succeed?",
  "Practicing the order and keeping explanations brief",["Reading every word","Using tiny text","Skipping the best images"],"Preparation and brevity keep interest.")
H('231.d.1.D',3,"Taking notes while a client explains their needs and then repeating them back is:",
  "active listening",["interrupting","daydreaming","ignoring"],"Repeating confirms understanding.")
H('231.d.1.D',4,"A client's feedback is unclear. The photographer should:",
  "ask questions to clarify the request",["guess","redo everything","ignore it"],"Questions clarify requirements.")
H('231.d.1.E',3,"Sending a polite thank-you and a preview gallery within a day builds:",
  "customer relations",["tension","delay","mistrust"],"Prompt, polite service builds loyalty.")
H('231.d.1.E',4,"A client wants a refund because she disliked her photos. A good public-relations response is to:",
  "listen, apologize, and propose a fix",["argue","ignore","post complaints"],"Calm responses can retain clients.")
H('231.d.4.A',3,"A practicum student arrives early, helps carry gear, and finishes edits on time. She shows:",
  "a positive work ethic",["a bad habit","delay","shortcuts"],"Reliability is work ethic.")
H('231.d.4.A',4,"Which behavior shows a productive work ethic during a long event shoot?",
  "Staying focused and keeping equipment organized",["Wandering away","Skipping shots","Leaving gear on the floor"],"Organization and focus matter.")
H('231.d.4.B',3,"A photographer gets permission before using a client's photos in her advertising. This is:",
  "ethical conduct with others",["carelessness","greed","gossip"],"Permission respects the client.")
H('231.d.4.B',4,"A client asks the photographer not to share her family photos. The photographer should:",
  "respect the request",["post them anyway","sell them","mention it publicly"],"Respecting privacy is ethical.")
H('231.d.4.C',3,"Following all shop rules, laws, and regulations should be done:",
  "every day",["occasionally","only when watched","never"],"Compliance is continuous.")
H('231.d.4.C',4,"Which example shows compliance in a studio?",
  "Keeping signed releases on file for each model",["Skipping releases","Posting without consent","Ignoring fire exits"],"Releases are legal protection.")
H('231.d.5.A',3,"A practicum student works with a professional photographer and logs what she learns weekly. She is:",
  "documenting learning",["hiding work","skipping tasks","avoiding feedback"],"Logs show growth.")
H('231.d.5.A',4,"Why does the mentor review the student's log?",
  "To evaluate progress and provide feedback",["To punish","To waste time","To avoid training"],"Review supports learning.")
H('231.d.5.B',3,"Choosing a prime lens for a portrait and a zoom for a fast event shows increased skill in:",
  "using cameras and lenses",["accounting","carpentry","cooking"],"Lens choice affects results.")
H('231.d.5.B',4,"Which lens would best capture a portrait with a soft blurred background?",
  "A fast lens with a wide aperture",["A slow lens at its smallest aperture","A fisheye lens","A pinhole"],"Wide apertures create shallow depth of field.")
H('231.d.5.C',3,"Arranging a product so its lines draw the eye through the frame uses:",
  "composition and layout principles",["tax rules","audio mixing","printing registration"],"Composition guides attention.")
H('231.d.5.C',4,"In a catalog layout, leaving blank space around a product helps:",
  "text and image fit cleanly",["hide the product","distort the image","remove color"],"Space gives room for copy.")
H('231.d.5.D',3,"Lighting a subject with a key light, fill light, and hair light is:",
  "three-point lighting",["flat lighting","no lighting","single-point"],"Three lights shape the subject.")
H('231.d.5.D',4,"A softbox is used to:",
  "soften and diffuse a light source",["harden shadows","block all light","darken the room"],"Softboxes make light gentle.")
H('231.d.5.E',3,"Delivering sharp, well-exposed, properly composed images to a client is producing:",
  "professional-quality photographs",["amateur work","random snapshots","blurry shots"],"Quality meets client standards.")
H('231.d.5.E',4,"Which step helps ensure professional quality before delivery?",
  "Review each image for focus, exposure, and color",["Deliver all raw shots unedited","Skip culling","Skip color check"],"Quality control matters.")
H('231.d.5.F',3,"A photographer prints a fine art series on archival paper chosen for its texture. She is selecting the:",
  "appropriate photographic paper",["wrong tool","cheapest option always","random paper"],"Paper affects the look and longevity.")
H('231.d.5.F',4,"Which paper suits an image with deep, rich blacks and high contrast?",
  "A glossy or luster paper",["Newsprint","Tracing paper","Rough sketch paper"],"Glossy papers support dense blacks.")
H('231.d.5.G',3,"Placing a print inside a frame with a border is:",
  "matting and framing",["scanning","retouching","filtering"],"Mats and frames protect prints.")
H('231.d.5.G',4,"Why choose UV-protective glass for framing a valuable print?",
  "It reduces fading from light",["It adds weight","It reduces cost","It changes colors"],"UV glass protects prints.")
H('231.d.5.H',3,"A photographer follows industry standards when editing and exporting files. She is using:",
  "industry-standard production tools",["outdated methods","no methods","random methods"],"Standards keep work compatible.")
H('231.d.5.H',4,"Which tool is used to batch-process raw images for color and exposure?",
  "A raw editor with presets",["A word processor","A spreadsheet","A calculator"],"Presets speed consistent edits.")
H('231.d.5.I',3,"Exporting a web gallery image at lower resolution but a print file at full resolution shows understanding of:",
  "resolution and file formats",["fashion","budgeting","music"],"Different uses need different settings.")
H('231.d.5.I',4,"Which format is suitable for a web photograph with small file size?",
  "JPEG",["RAW","TIFF only","PSD only"],"JPEG is compressed for web use.")
H('231.d.5.J',3,"A student now meters light faster and with fewer errors than at the start. This shows:",
  "growth of technical skills",["decline","no change","lost skills"],"Speed and accuracy show growth.")
H('231.d.5.J',4,"Which evidence shows growth in a photographer's skills?",
  "Comparing earlier and later images",["Ignoring earlier work","Deleting old files","Skipping reviews"],"Comparison reveals progress.")
H('231.d.5.K',3,"A student lists the techniques she handles well and those she still needs to improve. She is evaluating her:",
  "strengths and weaknesses",["salary","address","hobbies"],"Self-evaluation guides improvement.")
H('231.d.5.K',4,"Why evaluate your own proficiency during a practicum?",
  "To set goals for improvement",["To feel discouraged","To avoid work","To hide problems"],"Honest evaluation drives growth.")
H('231.d.5.L',3,"Saving finished prints, a digital gallery, and mentor comments is collecting:",
  "representative work samples",["trash","blank pages","old bills"],"Samples show ability.")
H('231.d.5.L',4,"Which item is a strong work sample for a commercial photographer?",
  "A finished client-style product shoot with consistent lighting",["A blurry test","A blank file","A random snapshot"],"Polished, purposeful work shows skill.")

H('228.d.7.E',5,"A designer wants to reuse a Creative Commons-licensed illustration on a printed menu she will sell. Which license element must she check before printing?",
  "Whether the license allows commercial use",["The paper weight","The ink brand","The press speed"],"Some licenses prohibit commercial use.")
H('230.d.11.G',5,"A portrait looks flat because only one front light was used. Which lighting change adds depth and separates the subject from the background?",
  "Adding a fill light and a back light to the key light",["Moving the camera closer","Using a wider lens","Turning off all lights"],"Three-point lighting shapes and separates the subject.")
H('230.d.2.E',4,"A client says, 'I want it to feel warm.' What is the best listening response?",
  "Ask what warm means to her, such as colors, mood, or setting",["Assume you know and begin","Say nothing","Change the subject"],"Clarifying questions turn vague feedback into usable direction.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_38.jsonl'))

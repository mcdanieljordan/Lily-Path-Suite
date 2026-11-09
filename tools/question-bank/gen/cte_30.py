import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('127.', 1107, own='cte_30.jsonl')
def H(code, d, q, right, wrong, e):
    return B.hand(code, d, q, right, wrong, e)

# ---------- 127.172 Printing and Imaging Technology I ----------
H('172.d.4',3,"A print shop employee uses design software, email, and a file-transfer site to send proofs to customers. These are:",
  "Technology applications",["Hand tools","Safety signs","Press plates"],"Technology applications.")
H('172.d.4',4,"Uploading a customer's artwork through a secure web portal for a print job shows the use of:",
  "Technology to exchange files",["Ink mixing","Paper cutting","Die stamping"],"Technology applications.")
H('172.d.9',3,"A press operator who learns the shortcuts on the digital press controller is applying technical skills for:",
  "Efficiency",["Delay","Waste","Confusion"],"Technical skills.")
H('172.d.9',4,"Saving job settings as a preset on a digital press helps a shop:",
  "Repeat jobs faster with fewer setup errors",["Print slower","Waste more paper","Skip proofing"],"Technical skills.")
H('172.d.11',3,"Learning about Gutenberg's movable-type press is part of researching the:",
  "History of the printing and imaging field",["Future of weather","History of metals","Rules of sports"],"History of printing.")
H('172.d.11',4,"The invention of offset lithography in the early 1900s changed printing by allowing:",
  "Fast, high-volume printing with consistent quality",["Hand-copied books","Only black ink","Wood-block carving only"],"History of printing.")
H('172.d.1.A',3,"A print shop employee writes a clear job ticket with correct spelling and details. This applies:",
  "English language arts skills",["Mixing skills","Welding skills","Binding skills"],"ELA.")
H('172.d.1.A',4,"Proofreading a customer's flyer before it goes to press mainly prevents:",
  "Costly errors in the finished job",["Faster ink drying","Paper curl","Machine noise"],"ELA in industry.")
H('172.d.1.B',3,"A print job needs 2,500 flyers. They print 4 flyers per sheet. How many sheets are needed?",
  "625",["600","650","10,000"],"2500 / 4 = 625.")
H('172.d.1.B',4,"A press prints 120 sheets per minute. How many sheets does it print in 15 minutes?",
  "1,800",["1,200","1,500","2,100"],"120 x 15 = 1800.")
H('172.d.2.A',3,"A shop worker explains bleed and trim to a first-time customer in plain words. This is adapting language to the:",
  "Audience",["Press","Ink","Cutter"],"Adapt language.")
H('172.d.2.A',4,"A technical email to a prepress department uses industry terms, while a customer email uses plain terms. This reflects different:",
  "Audience and purpose",["Paper sizes","Ink colors","Press speeds"],"Adapt language.")
H('172.d.2.B',3,"Sorting job tickets by due date is:",
  "Organizing information",["Trimming paper","Mixing ink","Plate making"],"Organize information.")
H('172.d.2.B',4,"Preparing a written quote with materials, labor, and delivery listed in order helps customers:",
  "Understand the cost clearly",["Avoid reading it","Get confused","Delay approval"],"Organize.")
H('172.d.2.C',3,"A press operator reports that the density readings are drifting lighter. This is:",
  "Interpreting and communicating data",["Cutting paper","Loading ink","Cleaning rollers"],"Interpret information.")
H('172.d.2.C',4,"A shop foreman reads a waste report and tells the team that makeready sheets are too high. This communicates:",
  "A data-based observation",["A rumor","A joke","A guess"],"Communicate data.")
H('172.d.2.D',3,"Showing a customer a printed sample and explaining the finish options is a:",
  "Formal presentation",["Casual joke","Break","Press check"],"Formal presentation.")
H('172.d.2.D',4,"Giving a quick shift update to coworkers about a press problem is a(n):",
  "Informal presentation",["Awards speech","Keynote","Press release"],"Informal presentation.")
H('172.d.2.E',3,"A prepress worker repeats back a customer's color request to confirm it. This is:",
  "Active listening",["Interrupting","Daydreaming","Ignoring"],"Active listening.")
H('172.d.2.F',3,"A shop supervisor works with employees and customers from many backgrounds, which requires:",
  "Respectful, clear communication",["Stereotypes","Teasing","Silence"],"Diverse groups.")
H('172.d.2.E',4,"Asking a customer to clarify \"make it pop\" before changing a design is a form of:",
  "Active listening",["Guessing","Arguing","Delaying"],"Active listening.")
H('172.d.2.F',4,"A print shop with a multilingual team can better serve:",
  "A wider range of customers",["Fewer customers","Only one market","No one"],"Diverse groups.")
H('172.d.2.G',3,"Thanking a customer and fixing a printing error quickly builds the shop's:",
  "Public relations and reputation",["Waste","Overhead","Ink supply"],"PR skills.")
H('172.d.2.G',4,"A customer complains that the colors look different from the proof. A strong PR response is to:",
  "Listen, explain, and offer a fix",["Argue","Blame them","Ignore it"],"PR skills.")
H('172.d.3.A',3,"A team compares two paper stocks by cost, finish, and durability before choosing. This is:",
  "Critical thinking",["Guessing","Habit","Coin flipping"],"Critical thinking.")
H('172.d.3.A',4,"Testing a sample print on two papers before a large run is an example of using:",
  "Evidence to make a decision",["A hunch","A rumor","Luck"],"Critical thinking.")
H('172.d.3.B',3,"Two workers disagree about the press schedule. A good interpersonal skill is to:",
  "Listen and compromise",["Yell","Quit","Blame"],"Interpersonal skills.")
H('172.d.3.B',4,"When a rush order conflicts with a scheduled job, a team solves it best by:",
  "Discussing priorities and agreeing on a plan",["Ignoring the rush","Hiding the order","Taking sides"],"Group problem solving.")
H('172.d.5.A',3,"Wearing safety glasses and gloves around the paper cutter is:",
  "Following personal safety rules",["Optional","A fashion choice","Slowing work"],"Safety.")
H('172.d.5.A',4,"Before servicing a press, a worker should use a lockout/tagout procedure to:",
  "Prevent the machine from starting unexpectedly",["Save energy","Speed up work","Reduce noise"],"Workplace safety.")
H('172.d.5.B',3,"If a chemical splashes in a coworker's eyes, the first step is to:",
  "Use an eyewash station and get help",["Wait","Ignore it","Wipe with ink rags"],"Emergency procedures.")
H('172.d.5.B',4,"A shop's safety data sheets (SDS) are kept so workers can:",
  "Find hazard and first-aid information for chemicals",["Order lunch","Find ink prices","Learn press speeds"],"Emergency procedures.")
H('172.d.6.A',3,"Telling a coworker clearly when a press needs maintenance is using:",
  "Communication skills",["Guesswork","Silence","Rumors"],"Communication.")
H('172.d.6.A',4,"Writing a shift handoff note for the next press crew helps by:",
  "Passing on important information",["Hiding errors","Wasting time","Confusing the crew"],"Communication.")
H('172.d.6.B',3,"Press, bindery, and prepress staff working together to finish a rush order shows:",
  "Teamwork",["Isolation","Rivalry","Delay"],"Teamwork.")
H('172.d.6.B',4,"A good way to manage a conflict between two crews over equipment is to:",
  "Meet and agree on a shared schedule",["Argue","Hide equipment","Blame management"],"Conflict management.")
H('172.d.6.C',3,"A well-run shop meeting should have an agenda and:",
  "Stay on topic",["Run all day","Skip decisions","Exclude input"],"Meetings.")
H('172.d.6.C',4,"Recording who is responsible for each action item after a meeting keeps the team:",
  "Accountable",["Unclear","Delayed","Isolated"],"Meetings.")
H('172.d.6.D',3,"A veteran press operator teaching a new hire to load paper is:",
  "Mentoring",["Competing","Hiding skills","Delaying"],"Mentoring.")
H('172.d.6.D',4,"Good mentoring skills include:",
  "Patience, clear instructions, and encouragement",["Impatience","Silence","Criticism only"],"Mentoring skills.")
H('172.d.7.A',3,"Telling the truth about a delayed job instead of hiding it is:",
  "Ethical conduct",["A mistake","Unprofessional","Optional"],"Ethical conduct.")
H('172.d.7.A',4,"Keeping a client's unpublished design confidential is:",
  "Ethical professional behavior",["Optional","A technical error","Unfair"],"Ethics.")
H('172.d.7.B',3,"Copying and printing a magazine's photograph for a customer without permission raises:",
  "A copyright issue",["A paper issue","A color issue","A press issue"],"Copyright.")
H('172.d.7.B',4,"Fair use allows limited reproduction of copyrighted work for purposes such as:",
  "Criticism, teaching, or news reporting",["Resale","Any reuse","Mass advertising"],"Fair use.")
H('172.d.7.C',3,"A Creative Commons license lets creators:",
  "Specify how others may use their work",["Remove all rights","Ban all use","Hide their work"],"Creative Commons.")
H('172.d.7.C',4,"A photographer's Creative Commons license that requires attribution means users must:",
  "Credit the photographer",["Pay a fee always","Delete the photo","Change the photo's name"],"Creative Commons licensing.")
H('172.d.8.A',3,"A portfolio of printed samples helps a graduate:",
  "Show skills to employers",["Hide work","Avoid interviews","Skip training"],"Portfolio.")
H('172.d.8.A',4,"Including a variety of print products, such as brochures and business cards, in a portfolio shows:",
  "Range of skills",["Confusion","Limited ability","Lack of focus"],"Portfolio.")
H('172.d.8.B',3,"Comparing pay, benefits, and training from two print shops is:",
  "Evaluating employment opportunities",["Gambling","Guessing","Daydreaming"],"Compare employment.")
H('172.d.8.B',4,"A job that offers apprenticeship training in press operation may be valuable for:",
  "Long-term career growth",["Immediate retirement","Skipping school","Avoiding learning"],"Evaluate opportunities.")
H('172.d.8.C',3,"Opening a small custom screen-printing business is an example of:",
  "Entrepreneurship",["Retirement","Job loss","Unemployment"],"Entrepreneurship.")
H('172.d.8.C',4,"A print entrepreneur needs to plan for expenses such as:",
  "Equipment, supplies, and marketing",["Only fun","Nothing","Only decorations"],"Entrepreneurship.")
H('172.d.10.A',3,"Offset lithography, digital printing, and screen printing are examples of:",
  "Printing systems",["Paper types","Ink colors","Fonts"],"Printing systems.")
H('172.d.10.A',4,"A shop with a short-run, quick-turn job for 50 copies would likely use:",
  "Digital printing",["Letterpress","Gravure","Large offset press"],"Printing systems.")
H('172.d.10.B',3,"The usual stages of producing a printed product are prepress, press, and:",
  "Finishing (postpress)",["Cooking","Marketing only","Recycling only"],"Production processes.")
H('172.d.10.B',4,"Imposition during prepress arranges pages so that:",
  "They print and fold in the correct order",["Ink dries faster","Paper is cut round","Colors change"],"Production processes.")
H('172.d.10.C',3,"The printing industry affects the U.S. economy by providing:",
  "Jobs and printed goods for many other industries",["No jobs","Only paper","Only ink"],"Economic impact.")
H('172.d.10.C',4,"Packaging, labels, and advertising all depend on:",
  "The printing industry",["Only farming","Only mining","Only banking"],"Economic impact.")
H('172.d.10.D',3,"Newer inkjet presses with automated workflows are examples of:",
  "Emerging technology in printing",["Old technology","Hand lettering","Quill pens"],"Emerging technologies.")
H('172.d.10.D',4,"Web-to-print software lets customers:",
  "Order and customize print products online",["Avoid printing","Slow orders","Mix ink"],"Emerging technologies.")
H('172.d.10.E',3,"Managing the printing process includes scheduling jobs and providing:",
  "Customer service",["Weather forecasts","Sports updates","Cooking tips"],"Manage printing process.")
H('172.d.10.E',4,"Tracking each job's status from order to delivery helps a shop:",
  "Meet deadlines and keep customers informed",["Lose orders","Ignore customers","Raise errors"],"Manage printing.")
H('172.d.10.F',3,"Cardstock, coated paper, and vinyl are examples of:",
  "Materials used in printing projects",["Safety rules","Fonts","Software"],"Materials.")
H('172.d.10.F',4,"For a durable outdoor banner, a shop would most likely use:",
  "Vinyl",["Tissue paper","Newsprint","Index card stock"],"Materials.")
H('172.d.10.G',3,"A printer gathers a customer's logo from a file, a sketch, and a web page. This is acquiring information in:",
  "A variety of formats",["One format only","No format","A printed format only"],"Acquire information.")
H('172.d.10.G',4,"Asking a customer for the original vector file of a logo rather than a screenshot helps get:",
  "A cleaner, scalable print",["A blurrier print","A smaller file","A lower resolution"],"Acquire information.")
H('172.d.10.H',3,"Checking whether a customer's artwork is high enough in resolution is evaluating its:",
  "Usability",["Weight","Smell","Taste"],"Evaluate information.")
H('172.d.10.H',4,"Verifying that a company's phone number on a flyer is correct before printing checks information for:",
  "Accuracy",["Speed","Color","Weight"],"Evaluate information.")
H('172.d.10.I',3,"Programs such as Adobe Illustrator and InDesign are compared by their:",
  "Features for digital printing work",["Prices of paper","Colors of ink","Sizes of presses"],"Graphics programs.")
H('172.d.10.I',4,"A designer chooses a vector program rather than a photo editor for a logo because vector graphics:",
  "Scale without losing quality",["Cannot be resized","Always blur","Need more ink"],"Graphics programs.")
H('172.d.10.J',3,"Headlines, body text, images, and white space are:",
  "Design elements in a layout",["Press parts","Ink types","Paper weights"],"Design elements.")
H('172.d.10.J',4,"Using ample white space around a headline mainly helps:",
  "Readability and focus",["Crowd the page","Hide the text","Increase ink use"],"Design elements.")
H('172.d.10.K',3,"Font size and style affect the:",
  "Readability and tone of printed text",["Weight of the press","Speed of the cutter","Color of the paper only"],"Typography.")
H('172.d.10.K',4,"A serif font is typically recognized by the:",
  "Small strokes at the ends of letters",["Absence of strokes","Thick outlines only","Rounded dots"],"Typography.")
H('172.d.10.L',3,"The color wheel shows that red and green are:",
  "Complementary colors",["Analogous colors","Neutral colors","Identical colors"],"Color theory.")
H('172.d.10.L',4,"Printing in full color typically uses the process colors:",
  "Cyan, magenta, yellow, and black",["Red, green, blue only","Orange, purple, brown","Gold and silver only"],"Color theory.")
H('172.d.10.M',3,"Using a strong difference in size or color to make an item stand out is the concept of:",
  "Contrast",["Repetition","Alignment","Proximity"],"Graphic design concepts.")
H('172.d.10.M',4,"Placing related items close together on a page is the design concept of:",
  "Proximity",["Contrast","Repetition","Bleed"],"Graphic design concepts.")
H('172.d.10.N',3,"A press operator reads the equipment manual to learn how to change a blanket. This is:",
  "Referencing technical documentation",["Guessing","Skipping steps","Ignoring instructions"],"Technical documentation.")
H('172.d.10.N',4,"A spec sheet for a paper stock lists weight, brightness, and:",
  "Finish",["Price of ink","Press name","Customer age"],"Technical documentation.")
H('172.d.10.O',3,"Saving a design as a PDF helps ensure it prints the same on different computers. This relates to:",
  "File and cross-platform compatibility",["Paper compatibility","Ink compatibility","Shipping compatibility"],"File compatibility.")
H('172.d.10.O',4,"Fonts missing on a printer's computer can cause problems, so designers often:",
  "Embed or outline fonts in the final file",["Delete fonts","Avoid fonts","Print in black only"],"Cross-platform compatibility.")
H('172.d.10.P',3,"Looking at balance, contrast, and emphasis in a poster to critique it applies:",
  "Principles of design",["Safety rules","Press maintenance","Delivery routes"],"Principles of design.")
H('172.d.10.P',4,"A critique that says, \"The layout is balanced but the headline lacks contrast\" uses:",
  "Design vocabulary to analyze an image",["Slang only","Guesswork","Rumor"],"Critique.")
H('172.d.10.Q',3,"A poster with equal visual weight on both sides shows the principle of:",
  "Balance",["Chaos","Clutter","Noise"],"Principles of design.")
H('172.d.10.Q',4,"A repeated pattern of shapes across a brochure demonstrates:",
  "Rhythm or repetition",["Isolation","Disorder","Subtraction"],"Principles of design in print.")

# ---------- 127.173 Digital Publishing / Printing II ----------
H('173.d.5',3,"A designer uses page-layout software, email, and cloud sharing to complete a project. These are:",
  "Technology applications",["Hand tools","Safety signs","Press plates"],"Technology applications.")
H('173.d.5',4,"Using a project management app to track job status across the print team is using technology to:",
  "Improve coordination",["Lose track of jobs","Slow production","Hide work"],"Technology applications.")
H('173.d.10',3,"A designer who learns keyboard shortcuts in InDesign is applying technical skills to improve:",
  "Efficiency",["Confusion","Delay","Waste"],"Technical skills.")
H('173.d.10',4,"Using master pages in a multi-page document helps a designer:",
  "Apply consistent elements quickly",["Duplicate work","Add errors","Slow layout"],"Technical skills.")
H('173.d.1.A',3,"Attending a workshop on color management for print is:",
  "Participating in training",["Wasting time","Avoiding work","Playing"],"Training and education.")
H('173.d.1.A',4,"A professional certification in a print software suite can show employers:",
  "Verified technical skills",["No ability","Poor effort","Lack of interest"],"Certification.")
H('173.d.1.B',3,"An employee who arrives on time, finishes tasks, and treats customers politely shows:",
  "Positive work behaviors",["Poor habits","Carelessness","Disinterest"],"Work behaviors.")
H('173.d.1.B',4,"Taking initiative to learn a new finishing process shows which personal quality?",
  "Motivation and willingness to learn",["Indifference","Fear of change","Avoidance"],"Personal qualities.")
H('173.d.1.C',3,"Searching job listings at print shops and preparing a resume is:",
  "Seeking and applying for a job",["Retiring","Quitting","Avoiding work"],"Seeking employment.")
H('173.d.1.C',4,"During an interview for a prepress job, an applicant can show skills best by:",
  "Bringing a portfolio of design samples",["Arriving empty-handed","Criticizing others","Skipping questions"],"Applying for jobs.")
H('173.d.2.A',3,"Writing an accurate job order using correct grammar applies:",
  "English language arts skills",["Welding skills","Cooking skills","Plumbing skills"],"ELA.")
H('173.d.2.A',4,"Copy editing a brochure for errors before printing demonstrates:",
  "Attention to language conventions",["Poor planning","Haste","Carelessness"],"ELA.")
H('173.d.2.B',3,"A booklet has 24 pages printed on both sides of each sheet. How many sheets of paper are needed for one copy?",
  "12",["24","6","48"],"24 pages / 2 pages per sheet = 12.")
H('173.d.2.B',4,"A job costs $0.15 per copy for 800 copies. What is the total cost?",
  "$120",["$80","$150","$12"],"0.15 x 800 = 120.")
H('173.d.3.A',3,"Explaining proof approval to a customer in simple terms is adapting language to the:",
  "Audience",["Press","Paper","Software"],"Adapt language.")
H('173.d.3.A',4,"A designer writes a formal estimate for a corporate client and a short note for a coworker, reflecting different:",
  "Purposes and audiences",["Colors","Paper sizes","Resolutions"],"Adapt language.")
H('173.d.3.B',3,"Placing design files in labeled folders by client and date is:",
  "Organizing information",["Deleting data","Hiding data","Printing data"],"Organize.")
H('173.d.3.B',4,"A clear project brief lists purpose, audience, deadline, and:",
  "Specifications",["Gossip","Hobbies","Weather"],"Organize information.")
H('173.d.3.C',3,"A designer reports that a test print shows colors shifting from the screen version. This is:",
  "Interpreting and communicating observations",["Guessing","Hiding errors","Wasting paper"],"Interpret information.")
H('173.d.3.C',4,"Explaining a color-density chart to a press operator helps the operator:",
  "Adjust the ink to match the target",["Ignore color","Change the paper","Stop the press"],"Interpret data.")
H('173.d.3.D',3,"Pitching a brochure concept to a client with samples is a:",
  "Formal presentation",["Casual remark","Break","Rumor"],"Formal presentation.")
H('173.d.3.D',4,"A quick desk-side update on a proof's status is a(n):",
  "Informal presentation",["Keynote address","Formal report","Awards speech"],"Informal presentation.")
H('173.d.3.E',3,"A designer who takes notes and asks follow-up questions during a client call is using:",
  "Active listening",["Distraction","Interrupting","Multitasking"],"Active listening.")
H('173.d.3.E',4,"Summarizing a client's requests at the end of a call helps ensure:",
  "Mutual understanding",["Confusion","Delay","Conflict"],"Active listening.")
H('173.d.3.F',3,"Working respectfully with clients of different cultures is:",
  "Listening to and speaking with diverse individuals",["Avoiding clients","Stereotyping","Ignoring needs"],"Diverse individuals.")
H('173.d.3.F',4,"Designing a flyer for a multilingual community may need:",
  "Translations and culturally aware images",["One language only","No images","Random fonts"],"Diversity.")
H('173.d.3.G',3,"Following up with a customer after delivery to ask about satisfaction shows:",
  "Public relations skills",["Poor service","Neglect","Avoidance"],"PR.")
H('173.d.3.G',4,"A customer says the order arrived late. A good PR response is to:",
  "Apologize and offer a resolution",["Blame the driver","Ignore the call","Deny it"],"PR.")
H('173.d.4.A',3,"A team picks the best layout after testing three versions with sample readers. This uses:",
  "Critical thinking",["Luck","Chance","Habit"],"Critical thinking.")
H('173.d.4.A',4,"Weighing the cost, speed, and quality of different binding options before choosing is:",
  "Critical thinking in a group",["Random choice","Avoidance","Impulse"],"Critical thinking.")
H('173.d.4.B',3,"Two designers disagree on a headline font. A helpful interpersonal skill is:",
  "Listening and testing both options",["Arguing louder","Walking away","Blaming"],"Interpersonal skills.")
H('173.d.4.B',4,"Group problem solving in a shop works best when members:",
  "Share ideas and agree on a plan",["Work alone only","Argue constantly","Avoid input"],"Group problem solving.")
H('173.d.6.A',3,"Using hearing protection near loud finishing equipment is:",
  "Following workplace safety rules",["Optional","Slowing work","Unnecessary"],"Safety.")
H('173.d.6.A',4,"Keeping walkways clear of paper stacks reduces the risk of:",
  "Slips, trips, and falls",["Faster printing","Color shifts","Ink smears"],"Safety regulations.")
H('173.d.6.B',3,"If a fire alarm sounds in the shop, employees should:",
  "Leave using the posted exit route",["Keep printing","Hide","Finish the job"],"Emergency procedures.")
H('173.d.6.B',4,"Knowing the location of fire extinguishers and exits is part of:",
  "Emergency preparedness",["Marketing","Pricing","Design"],"Emergency procedures.")
H('173.d.7.A',3,"Sharing important changes to a job with the whole team shows:",
  "Communication skills",["Secrecy","Neglect","Isolation"],"Communication.")
H('173.d.7.A',4,"Clear written instructions on a job ticket reduce:",
  "Misunderstandings and errors",["Quality","Efficiency","Teamwork"],"Communication.")
H('173.d.7.B',3,"Prepress, press, and bindery coordinating on a tight deadline show:",
  "Teamwork",["Rivalry","Delay","Isolation"],"Teamwork.")
H('173.d.7.B',4,"A good first step to resolve a conflict between two employees is to:",
  "Let each person explain their view",["Ignore it","Take sides","Yell"],"Conflict management.")
H('173.d.7.C',3,"A supervisor conducts a production meeting by:",
  "Following an agenda and keeping time",["Rambling","Skipping decisions","Excluding staff"],"Meetings.")
H('173.d.7.C',4,"Participating well in a meeting includes:",
  "Listening and contributing ideas",["Texting","Talking over others","Arriving late"],"Meetings.")
H('173.d.7.D',3,"A senior designer reviewing a trainee's work and giving advice is:",
  "Mentoring",["Ignoring","Competing","Hiding tips"],"Mentoring.")
H('173.d.7.D',4,"Good mentoring balances guidance with:",
  "Encouraging independence",["Doing the work","Criticism only","Silence"],"Mentoring skills.")
H('173.d.8.A',3,"Giving credit to a photographer for a photo used in a brochure demonstrates:",
  "Ethical conduct",["Carelessness","Weak design","Poor printing"],"Ethical conduct.")
H('173.d.8.A',4,"Charging a customer fairly for the actual materials used is:",
  "Ethical business practice",["Unnecessary","Illegal","Optional"],"Ethics.")
H('173.d.8.B',3,"Duplicating a protected book cover for sale without permission would:",
  "Violate copyright law",["Be allowed","Be encouraged","Save money legally"],"Copyright.")
H('173.d.8.B',4,"Using a small excerpt of a work in a classroom handout may qualify as:",
  "Fair use",["Piracy","Theft always","Public domain"],"Fair use.")
H('173.d.8.C',3,"Using only images that you created or have licensed to use shows:",
  "Respect for intellectual property",["Carelessness","Plagiarism","Disregard"],"IP.")
H('173.d.8.C',4,"Asking permission before reusing another designer's layout is:",
  "Respecting their intellectual property",["Unneeded","Slowing work","Wasteful"],"IP respect.")
H('173.d.8.D',3,"An acceptable use policy at a print company limits employees to using computers for:",
  "Approved work tasks",["Any personal use","Gaming","Unapproved downloads"],"Acceptable use.")
H('173.d.8.D',4,"Good network etiquette includes:",
  "Not using shared bandwidth for large personal downloads",["Sharing passwords","Streaming constantly","Ignoring policies"],"Etiquette.")
H('173.d.8.E',3,"A Creative Commons license tells others:",
  "How they may reuse the creator's work",["Nothing","That the work is deleted","That it is secret"],"Creative Commons.")
H('173.d.8.E',4,"A Creative Commons \"non-commercial\" license means the work may not be used for:",
  "Commercial profit",["Teaching","Personal learning","Class projects"],"Creative Commons licensing.")
H('173.d.9.A',3,"Keeping updated samples of printed work, certificates, and references is maintaining a:",
  "Portfolio",["Press plate","Print queue","Ink log"],"Portfolio.")
H('173.d.9.A',4,"Updating a portfolio with recent projects shows employers:",
  "Current skills and growth",["Old skills","No change","A lack of work"],"Portfolio.")
H('173.d.9.B',3,"Weighing salary, location, and training of two job offers in the printing field is:",
  "Evaluating and comparing employment",["Guessing","Daydreaming","Complaining"],"Compare employment.")
H('173.d.9.B',4,"A job with tuition assistance for certification is valuable because it:",
  "Supports further career development",["Prevents learning","Limits skills","Costs more"],"Evaluate employment.")
H('173.d.9.C',3,"Running your own small design and print business is:",
  "Entrepreneurship",["Retirement","Job loss","Layoff"],"Entrepreneurship.")
H('173.d.9.C',4,"A new print entrepreneur should learn about licenses, taxes, and:",
  "Pricing their services",["Ignoring customers","Hiding costs","Avoiding records"],"Entrepreneurship.")
H('173.d.11.A',3,"Digital presses, offset presses, and large-format printers are:",
  "Printing systems",["Fonts","Colors","Papers"],"Printing systems.")
H('173.d.11.A',4,"A large-format inkjet printer is best suited for making:",
  "Posters and banners",["Business cards only","Newspaper runs of millions","Stamp sheets"],"Printing systems.")
H('173.d.11.B',3,"Taking a job from design, to proof, to press, to finishing is:",
  "Employing the production process",["Skipping steps","Guesswork","Delay"],"Production process.")
H('173.d.11.B',4,"A proof is approved before press to avoid:",
  "Printing errors on the whole run",["Fast delivery","Cheap paper","Color options"],"Production.")
H('173.d.11.C',3,"Print process management includes tracking jobs and providing:",
  "Customer service",["Games","Gossip","Weather"],"Process management.")
H('173.d.11.C',4,"Keeping a customer updated when a delay occurs is an example of:",
  "Good customer service",["Poor planning","Neglect","Avoidance"],"Customer service.")
H('173.d.11.D',3,"Asking what a customer wants a brochure to do and how many they need is:",
  "Evaluating customer needs",["Ignoring them","Guessing","Delaying"],"Customer needs.")
H('173.d.11.D',4,"After learning a customer's budget, a printer may suggest:",
  "A paper or finish that meets the goal and the budget",["The most expensive option","No options","An unrelated service"],"Evaluate materials.")
H('173.d.11.E',3,"A designer collects text from a Word file, photos from a camera, and a logo from a vector file. This is acquiring information in:",
  "A variety of formats",["One format only","No format","A paper format only"],"Acquire information.")
H('173.d.11.E',4,"Converting a customer's old PDF to an editable format may be needed to:",
  "Update text and layout",["Lose data","Slow printing","Reduce paper"],"Information.")
H('173.d.11.F',3,"Checking that all names and prices on a menu proof are correct evaluates information for:",
  "Accuracy",["Speed","Weight","Brightness"],"Evaluate information.")
H('173.d.11.F',4,"Verifying that a source image has enough resolution for print checks its:",
  "Usability",["Taste","Weight","Smell"],"Evaluate information.")
H('173.d.11.G',3,"Creating a flyer using a word processor and a layout program is:",
  "Applying digital publishing techniques",["Hand-copying","Chiseling","Weaving"],"Digital publishing.")
H('173.d.11.G',4,"Placing text in linked frames lets a designer:",
  "Flow text across columns or pages",["Delete text","Hide text","Shrink the file"],"Digital publishing.")
H('173.d.11.H',3,"Choosing a bold headline and plenty of white space applies:",
  "Design elements",["Press settings","Ink recipes","Paper weights"],"Design elements.")
H('173.d.11.H',4,"Left-aligned text with consistent margins produces a layout that is:",
  "Clean and readable",["Cluttered","Unreadable","Random"],"Design elements.")
H('173.d.11.I',3,"A designer uses 10-12 point type for body text because it is:",
  "Comfortable to read in print",["Impossible to read","Too large","Meaningless"],"Typography.")
H('173.d.11.I',4,"Mixing too many fonts in one flyer usually makes it look:",
  "Messy and inconsistent",["More professional","Cleaner","Easier to read"],"Typography.")
H('173.d.11.J',3,"A designer picks colors next to each other on the color wheel for a calm look. These are:",
  "Analogous colors",["Complementary colors","Opposite colors","Neutral colors"],"Color theory.")
H('173.d.11.J',4,"Using a CMYK color mode for a print project instead of RGB helps ensure:",
  "Colors are closer to what the press can produce",["Brighter screen glow","Smaller files always","Darker paper"],"Color theory.")
H('173.d.11.K',3,"Repeating the same logo placement on each page applies the concept of:",
  "Repetition",["Contrast","Distortion","Randomness"],"Graphic design concepts.")
H('173.d.11.K',4,"Lining up text and images along a common edge applies the concept of:",
  "Alignment",["Contrast","Repetition","Gradient"],"Graphic design concepts.")
H('173.d.11.L',3,"Proofing a design and fixing spacing errors is:",
  "Editing and evaluating a product",["Packing it","Shipping it","Selling it"],"Edit and evaluate.")
H('173.d.11.L',4,"Reviewing a proof for typos, color, and layout before approval is:",
  "A quality-control step",["A shipping step","A billing step","A marketing step"],"Evaluate products.")
H('173.d.11.M',3,"A document that lists a job's paper, size, ink colors, and finishing is:",
  "Technical documentation",["A menu","A flyer","A receipt"],"Technical documentation.")
H('173.d.11.M',4,"Writing clear specifications for a repeat job helps the next operator:",
  "Reproduce the job accurately",["Guess","Delay","Skip steps"],"Technical documentation.")
H('173.d.11.N',3,"Knowing how a computer, scanner, and printer work together is knowledge of:",
  "Hardware and software components",["Cooking","Plumbing","Sports"],"Hardware and software.")
H('173.d.11.N',4,"A calibrated monitor helps a designer judge:",
  "Color accuracy before printing",["Paper weight","Press speed","Binding type"],"Hardware.")
H('173.d.11.O',3,"Saving a file as a print-ready PDF helps ensure that it:",
  "Opens the same on different systems",["Changes colors","Loses fonts","Loses images"],"File compatibility.")
H('173.d.11.O',4,"A Mac and a Windows PC can both open a standard PDF, which is an example of:",
  "Cross-platform compatibility",["Incompatibility","A format problem","A hardware fault"],"Cross-platform.")
H('173.d.11.P',3,"A finished design can be delivered as a printed piece, a PDF, or a:",
  "Web graphic",["Cooking recipe","Bus schedule","Ticket stub"],"Deliver in a variety of media.")
H('173.d.11.P',4,"A brochure delivered in both print and email versions is an example of:",
  "Delivering products in a variety of media",["Wasting resources","Single delivery","Poor design"],"Deliver products.")

# ---------- 127.174 Printing and Imaging Technology (advanced) ----------
H('174.d.4',3,"A press operator uses a digital workflow system to track jobs. This is an application of:",
  "Technology",["Hand copying","Chiseling","Weaving"],"Technology applications.")
H('174.d.4',4,"A shop uses RIP software to process files for large-format output. This is a:",
  "Technology application in print production",["Manual process","Hand tool","Safety rule"],"Technology applications.")
H('174.d.9',3,"An operator who learns advanced press controls is building technical skills for:",
  "Efficiency",["Waste","Delay","Error"],"Technical skills.")
H('174.d.9',4,"Using automatic registration features on a press reduces:",
  "Setup time and wasted sheets",["Quality","Speed","Accuracy"],"Technical skills.")
H('174.d.1.A',3,"A production report written with clear sentences and accurate details applies:",
  "English language arts skills",["Plumbing","Carpentry","Cooking"],"ELA.")
H('174.d.1.A',4,"A clear incident report about a press jam should include:",
  "What happened, when, and what was done",["Jokes","Guesses","Blame"],"ELA in industry.")
H('174.d.1.B',3,"A press runs 8,000 sheets per hour. How many sheets does it run in 3 hours?",
  "24,000",["16,000","11,000","32,000"],"8000 x 3 = 24000.")
H('174.d.1.B',4,"A roll of paper is 40 inches wide and is cut into 5 equal-width strips. How wide is each strip?",
  "8 inches",["5 inches","10 inches","35 inches"],"40 / 5 = 8.")
H('174.d.2.A',3,"A press supervisor uses simple language to explain a problem to a new customer and technical language with the press crew. This is adapting language to the:",
  "Audience and situation",["Ink","Paper","Plate"],"Adapt language.")
H('174.d.2.A',4,"Writing a customer-facing estimate differs from writing an internal maintenance note because of:",
  "Purpose and audience",["Paper size","Ink color","Press name"],"Adapt language.")
H('174.d.2.B',3,"Arranging maintenance records by machine and date is:",
  "Organizing information",["Making ink","Cutting paper","Washing rollers"],"Organize.")
H('174.d.2.B',4,"Preparing an outline before giving a safety talk helps the speaker:",
  "Present ideas clearly and in order",["Skip points","Confuse listeners","Run overtime"],"Organize information.")
H('174.d.2.C',3,"A pressman notes that ink density readings are rising and tells the foreman. This is:",
  "Interpreting and communicating data",["Hiding data","Guessing","Ignoring"],"Interpret information.")
H('174.d.2.C',4,"A graph of waste by shift helps managers decide:",
  "Where to improve training or equipment",["Whom to blame","What to ignore","Where to hide errors"],"Interpret data.")
H('174.d.2.D',3,"Training new employees with a slide deck on safety is presenting information:",
  "Formally",["Randomly","Silently","Casually only"],"Present formally and informally.")
H('174.d.2.D',4,"A quick floor huddle to share a change in the job order is presenting:",
  "Informally",["As a keynote","As a press release","As a lecture series"],"Present informally.")
H('174.d.2.E',3,"An operator asks questions to clarify a job ticket before starting the press. This is:",
  "Active listening to obtain information",["Interrupting","Guessing","Avoiding"],"Active listening.")
H('174.d.2.E',4,"Repeating back the customer's requested paper and finish confirms:",
  "That the information is clear",["That it is wrong","That the job is late","That the press is down"],"Clarify information.")
H('174.d.2.F',3,"Working well with customers and coworkers of different backgrounds requires:",
  "Respect and open communication",["Teasing","Stereotypes","Silence"],"Diverse individuals.")
H('174.d.2.F',4,"A shop that welcomes diverse employees can often:",
  "Serve a wider range of customers",["Lose customers","Reduce ideas","Limit growth"],"Diversity.")
H('174.d.2.G',3,"Treating an angry customer politely and solving their issue builds:",
  "Customer satisfaction",["Waste","Complaints","Delays"],"PR skills.")
H('174.d.2.G',4,"Public relations skills used with coworkers improve:",
  "Internal customer satisfaction",["Press speed","Ink density","Paper weight"],"PR skills.")
H('174.d.3.A',3,"A team compares the cost and quality of three finishing options before choosing. This is:",
  "Critical thinking",["Luck","Guessing","Habit"],"Critical thinking.")
H('174.d.3.A',4,"Using press test data to decide on a paper change relies on:",
  "Evidence-based thinking",["A hunch","Convenience","Rumor"],"Critical thinking.")
H('174.d.3.B',3,"Two crew leaders disagree about the job order. A good interpersonal skill is:",
  "Listening and compromising",["Yelling","Quitting","Blaming"],"Interpersonal skills.")
H('174.d.3.B',4,"Group problem solving about a recurring press jam works best when the group:",
  "Shares observations and tests solutions",["Ignores the problem","Blames one person","Waits"],"Group problem solving.")
H('174.d.5.A',3,"Wearing the right protective gear around cutters and presses is:",
  "Implementing safety rules",["Optional","A fashion choice","Slowing work"],"Safety.")
H('174.d.5.A',4,"Machine guards on a press should be:",
  "In place and never bypassed",["Removed for speed","Optional","Disabled"],"Safety regulations.")
H('174.d.5.B',3,"If a coworker's hand is caught in a machine, the first step is to:",
  "Hit the emergency stop and call for help",["Keep running","Walk away","Wait"],"Emergency procedures.")
H('174.d.5.B',4,"Emergency eyewash stations should be:",
  "Easy to reach and tested regularly",["Hidden","Locked","Unmarked"],"Emergency procedures.")
H('174.d.6.A',3,"A press lead who sets daily goals and assigns tasks is employing:",
  "Leadership skills",["Poor skills","Avoidance","Indifference"],"Leadership.")
H('174.d.6.A',4,"A leader analyzes a missed deadline by looking at:",
  "Causes and ways to prevent it next time",["Who to blame","Who to fire","Nothing"],"Leadership.")
H('174.d.6.B',3,"Crews sharing the work to finish a large order show:",
  "Teamwork",["Rivalry","Isolation","Delay"],"Teamwork.")
H('174.d.6.B',4,"Working through disagreements to meet a shared production goal shows:",
  "Conflict-management skills",["Avoidance","Arguing","Giving up"],"Teamwork and conflict management.")
H('174.d.6.C',3,"Good working relationships grow from:",
  "Respect and constructive feedback",["Gossip","Silence","Competition for credit"],"Working relationships.")
H('174.d.6.C',4,"Constructive feedback on a coworker's setup should:",
  "Name what worked and suggest improvements",["Only criticize","Be vague","Be personal"],"Constructive feedback.")
H('174.d.6.D',3,"Before a meeting, a supervisor sets goals and:",
  "Prepares an agenda",["Cancels","Skips notes","Arrives late"],"Prepare for meetings.")
H('174.d.6.D',4,"A meeting objective should be:",
  "Specific and achievable",["Vague","Hidden","Impossible"],"Meeting objectives.")
H('174.d.6.E',3,"Conducting a meeting efficiently means:",
  "Staying on the agenda and recording decisions",["Wandering","Skipping notes","Ignoring input"],"Conduct meetings.")
H('174.d.6.E',4,"Participating productively in a team meeting includes:",
  "Listening and offering ideas",["Dominating","Texting","Staying silent"],"Participate in meetings.")
H('174.d.6.F',3,"An experienced bindery worker teaching a new employee is:",
  "Mentoring",["Competing","Delaying","Hiding"],"Mentoring.")
H('174.d.6.F',4,"Effective mentoring inspires confidence and:",
  "Teaches skills step by step",["Criticizes only","Does the work","Discourages questions"],"Mentoring.")
H('174.d.7.A',3,"Admitting a mistake on a job instead of covering it up is:",
  "Ethical conduct",["Weak","Unprofessional","Optional"],"Ethical conduct.")
H('174.d.7.A',4,"Keeping a customer's private proof information confidential is:",
  "Ethical professional behavior",["Optional","A technical error","Unnecessary"],"Ethics.")
H('174.d.7.B',3,"Copyright law protects the rights of:",
  "Creators of original works",["Printers only","Paper makers","Ink sellers"],"Copyright.")
H('174.d.7.B',4,"Printing copies of a protected comic for resale without permission is:",
  "Copyright infringement",["Fair use","Public domain","Allowed"],"Copyright.")
H('174.d.7.C',3,"A print shop that requires proof of rights for a customer's logo is modeling:",
  "Respect for intellectual property",["Disrespect","Carelessness","Neglect"],"IP respect.")
H('174.d.7.C',4,"Asking whether a customer has permission to reproduce a photograph shows:",
  "Care for intellectual property",["Rudeness","Indifference","Neglect"],"IP respect.")
H('174.d.7.D',3,"An acceptable use policy at work usually allows computers to be used for:",
  "Approved business tasks",["Any website","Gaming","Unapproved downloads"],"Acceptable use.")
H('174.d.7.D',4,"Good etiquette on the shop's shared network includes:",
  "Not sharing passwords",["Sharing passwords","Downloading anything","Ignoring policy"],"Etiquette.")
H('174.d.7.E',3,"A Creative Commons license tells users:",
  "How they may legally reuse a work",["Nothing","That it is deleted","That it is hidden"],"Creative Commons.")
H('174.d.7.E',4,"A \"share-alike\" Creative Commons condition requires that new works:",
  "Use the same license as the original",["Be deleted","Be sold only","Be kept secret"],"Creative Commons licensing.")
H('174.d.7.F',3,"The printing industry affects society by producing materials such as:",
  "Books, packaging, and signs",["Weather","Soil","Tides"],"Industry impact.")
H('174.d.7.F',4,"Printed labels on food and medicine help society by providing:",
  "Safety and ingredient information",["Confusion","Entertainment only","Weather updates"],"Industry impact.")
H('174.d.8.A',3,"A portfolio of printed samples helps a job seeker:",
  "Document skills and experience",["Hide skills","Avoid interviews","Skip training"],"Portfolio.")
H('174.d.8.A',4,"Including references and certifications in a portfolio shows:",
  "Verified qualifications",["Lack of skill","Weak effort","No ability"],"Portfolio.")
H('174.d.8.B',3,"Comparing wages, benefits, and training at different print companies is:",
  "Evaluating employment opportunities",["Guessing","Daydreaming","Complaining"],"Compare employment.")
H('174.d.8.B',4,"A company that offers certification training may be best for someone wanting:",
  "Career advancement",["No growth","Quick retirement","Fewer skills"],"Evaluate employment.")
H('174.d.8.C',3,"Starting a business that prints custom T-shirts is:",
  "Entrepreneurship",["Unemployment","Retirement","Job loss"],"Entrepreneurship.")
H('174.d.8.C',4,"An entrepreneur planning a print business should create a:",
  "Business plan",["Menu","Playlist","Poster only"],"Entrepreneurship.")
H('174.d.10.A',3,"Offset, digital, flexographic, and gravure are examples of:",
  "Printing systems",["Fonts","Folding types","Bindings"],"Printing systems.")
H('174.d.10.A',4,"Flexographic printing is commonly used for:",
  "Packaging and labels",["Fine art posters only","Hand-set type","Newspaper copy desks"],"Printing systems.")
H('174.d.10.B',3,"Managing the printing process includes scheduling and:",
  "Quality control",["Cooking","Gossip","Sports"],"Manage printing.")
H('174.d.10.B',4,"A shop uses job tickets to:",
  "Communicate instructions and track each job",["Hide jobs","Delay jobs","Cancel jobs"],"Manage printing.")
H('174.d.10.C',3,"Preparing customer materials for printing includes checking for bleed, resolution, and:",
  "Color mode",["Weather","Sports","Phone number"],"Prepare customer materials.")
H('174.d.10.C',4,"A preflight check on a file is done to find:",
  "Problems before printing",["Prices","Contacts","Weather"],"Prepare materials.")
H('174.d.10.D',3,"Letterpress, offset, screen, and digital are:",
  "Printing processes",["Paper types","Inks","Software"],"Printing processes.")
H('174.d.10.D',4,"Screen printing is a good choice for printing designs on:",
  "T-shirts and posters",["Microchips","Windows","Roads"],"Printing processes.")
H('174.d.10.E',3,"Oil-based, water-based, and UV-curable are types of:",
  "Ink",["Paper","Plate","Blanket"],"Ink processes.")
H('174.d.10.E',4,"UV-curable inks dry by:",
  "Exposure to ultraviolet light",["Evaporation only","Freezing","Absorption only"],"Ink processes.")
H('174.d.10.F',3,"Paper weight is commonly described in:",
  "Pounds or grams per square meter",["Gallons","Volts","Degrees"],"Paper.")
H('174.d.10.F',4,"A gloss finish on coated paper is chosen when the project needs:",
  "Vibrant color and a shiny look",["Writing surface only","Rough texture","Matte look"],"Paper finishes.")
H('174.d.10.G',3,"Cleaning rollers and blankets on a schedule helps keep a press:",
  "Running reliably with good print quality",["Dirty","Slower","Noisy"],"Cleanup and maintenance.")
H('174.d.10.G',4,"Following a lubrication schedule for a press is:",
  "Preventive maintenance",["Delay","Waste","Sabotage"],"Maintenance.")
H('174.d.10.H',3,"Looking at balance and contrast in a printed ad to critique it applies:",
  "Principles of design",["Press repairs","Safety tags","Shipping rules"],"Principles of design.")
H('174.d.10.H',4,"A critique that notes weak emphasis on the call to action uses:",
  "Design vocabulary to analyze print",["Slang only","Guesswork","Rumor"],"Critique.")
H('174.d.10.I',3,"A brochure with a clear focal point and good spacing demonstrates:",
  "Principles of design",["Poor design","Clutter","Chaos"],"Principles of design.")
H('174.d.10.I',4,"A visual path that leads the reader's eye from headline to image to text shows the principle of:",
  "Movement or flow",["Chaos","Isolation","Clutter"],"Principles of design in print.")

H('173.d.8.D',5,"A designer's company bans installing unlicensed fonts on shop computers. The main reason is to:",
  "Avoid license violations and security risks",["Slow down projects","Save paper","Reduce ink use"],"Acceptable use policy.")
H('174.d.6.C',5,"A pressman and a bindery worker disagree about who caused a defect, but both talk calmly and review the job together. This is an example of:",
  "Maintaining an effective working relationship",["Avoiding feedback","Escalating conflict","Withholding information"],"Working relationships.")
H('174.d.6.D',5,"A supervisor lists the topics, time limit, and desired decisions before a production meeting. This preparation helps:",
  "The meeting reach its goals efficiently",["The meeting run long","The team skip decisions","Attendance drop"],"Prepare for meetings.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_30.jsonl'))

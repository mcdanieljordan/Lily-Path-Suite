import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('127.', 1109, own='cte_32.jsonl')
def H(code, d, q, right, wrong, e):
    return B.hand(code, d, q, right, wrong, e)

# ---------- 127.178 Commercial Photography (recognition level) ----------
H('178.d.4',3,"A yearbook photographer shares proofs through a password-protected website. This is an example of:",
  "Applying technology",["Using a darkroom only","Avoiding clients","Hand sketching"],"Technology applications.")
H('178.d.4',4,"Which technology tool lets a team review the same photo edits from different locations?",
  "A shared cloud folder with comments",["A paper envelope","A bulletin board","A printed list"],"Technology applications.")
H('178.d.5',3,"Cameras, lenses, lighting, and software that work together to produce client images form a:",
  "Commercial photography system",["Weather system","Bus route","Sewing system"],"Photography systems.")
H('178.d.5',4,"If one part of a photography system fails, such as a memory card, what is most likely to happen?",
  "The whole workflow may be delayed",["Nothing changes","Photos improve","The lens repairs itself"],"Photography systems.")
H('178.d.10',3,"A photographer who sets keyboard shortcuts in editing software is working to boost:",
  "Efficiency",["Clutter","Downtime","Errors"],"Technical skills.")
H('178.d.10',4,"Which habit best saves time across many similar real estate shoots?",
  "Reusing a standard camera and edit preset",["Resetting every setting by hand","Skipping backups","Shooting without a plan"],"Technical skills.")
H('178.d.1.A',3,"Using correct grammar in an email quoting a wedding package demonstrates:",
  "English language arts skills",["Welding skills","Gardening skills","Driving skills"],"ELA.")
H('178.d.1.A',4,"A photographer's invoice description is vague. The best revision is to make it:",
  "Specific and error-free",["Longer and confusing","Full of slang","Shorter without details"],"ELA.")
H('178.d.1.B',3,"A sports photographer shoots 150 frames per game for 6 games. How many frames is that?",
  "900",["756","906","600"],"150 x 6 = 900.")
H('178.d.1.B',4,"A studio books 5 sessions at $85 each and gives a $40 loyalty discount on the total. What is the final total?",
  "$385",["$425","$345","$465"],"5 x 85 = 425; 425 - 40 = 385.")
H('178.d.2.A',3,"Describing exposure to a parent client versus to a fellow photographer is adapting language for:",
  "Audience",["Weather","Lens mount","Sensor size"],"Adapt language.")
H('178.d.2.A',4,"A short text to a model on set differs from a signed contract mainly because of the:",
  "Situation and intent",["Font brand","Camera model","Memory size"],"Adapt language.")
H('178.d.2.B',3,"Putting shoot details in order from first to last on a timeline is:",
  "Organizing written information",["Cropping","Printing","Mounting"],"Organize.")
H('178.d.2.B',4,"Which is the best way to organize oral directions for a family group portrait?",
  "Give steps in a clear sequence",["Mumble quickly","Speak randomly","Skip the plan"],"Organize.")
H('178.d.2.C',3,"A photographer says the histogram is shifted far left, so the image is too dark. This is:",
  "Interpreting data",["Guessing","Retouching","Printing"],"Interpret information.")
H('178.d.2.C',4,"After a shoot, the photographer tells the client which shots were best and why. This is:",
  "Communicating observations",["Hiding results","Avoiding feedback","Giving no information"],"Communicate observations.")
H('178.d.2.D',3,"Walking a school board through a photo contract at a scheduled meeting is a:",
  "Formal presentation",["Quick chat in a hallway","Joke","Rumor"],"Formal presentation.")
H('178.d.2.D',4,"A photographer explains the next pose to a toddler's parents on the spot. This is a(n):",
  "Informal presentation",["Keynote address","Board report","Press release"],"Informal presentation.")
H('178.d.2.E',3,"A photographer restates what a client wants for a corporate headshot. This shows:",
  "Active listening",["Interrupting","Daydreaming","Ignoring"],"Active listening.")
H('178.d.2.E',4,"Asking a follow-up question about a client's vision before the shoot helps to:",
  "Clarify information",["Confuse the plan","Delay payment","Lose the client"],"Active listening.")
H('178.d.2.F',3,"Photographing people of different ages and abilities calls for:",
  "Patience and respect",["Impatience","Rudeness","Assumptions"],"Diverse individuals.")
H('178.d.2.F',4,"A photographer preparing for a family with limited English can help communication by:",
  "Using simple words and gestures kindly",["Speaking loudly","Rushing","Avoiding them"],"Diverse individuals.")
H('178.d.2.G',3,"Sending an event client a quick preview within a day builds:",
  "Customer satisfaction",["Equipment wear","Lens dust","Cable length"],"PR skills.")
H('178.d.2.G',4,"A photographer greets the venue staff and thanks them after a shoot. This improves:",
  "Relationships with external contacts",["Camera battery","Print speed","Lens weight"],"PR skills.")
H('178.d.3.A',3,"Weighing two backgrounds for a product catalog and choosing the cleaner one uses:",
  "Critical thinking",["Luck","Haste","Habit only"],"Critical thinking.")
H('178.d.3.A',4,"A group decides which edit best fits the client's brand by checking the brand guide. This is:",
  "Critical thinking in a group",["Random voting","Ignoring data","Copying a rival"],"Critical thinking.")
H('178.d.3.B',3,"Two assistants disagree about reflector placement. A useful interpersonal move is to:",
  "Test both and compare",["Argue loudly","Walk out","Ignore the issue"],"Interpersonal skills.")
H('178.d.3.B',4,"A team solves a shoot-day problem fastest when everyone:",
  "Contributes ideas respectfully",["Waits silently","Blames others","Works alone"],"Group problem solving.")
H('178.d.6.A',3,"Keeping cables off walkways in a photo studio helps prevent:",
  "Trips and falls",["Sharper focus","Better color","Longer batteries"],"Safety.")
H('178.d.6.A',4,"Before changing a bulb in a studio light, a photographer should:",
  "Unplug it and let it cool",["Keep it on","Use a wet cloth","Touch the hot bulb"],"Safety regulations.")
H('178.d.6.B',3,"If someone is injured on set, the first step is to:",
  "Get help and follow emergency procedures",["Keep shooting","Hide it","Wait a day"],"Emergency procedures.")
H('178.d.6.B',4,"A posted evacuation map in a studio is meant to:",
  "Show the safe route out",["Decorate the wall","Show lighting setups","List client names"],"Emergency procedures.")
H('178.d.7.A',3,"A lead photographer sets a goal to deliver an album by Friday and plans the tasks. This is:",
  "Leadership",["Avoidance","Procrastination","Blame"],"Leadership.")
H('178.d.7.A',4,"After a project, a leader reviews what went well and what did not to:",
  "Improve future results",["Assign blame","Skip learning","End the team"],"Leadership.")
H('178.d.7.B',3,"A photographer, editor, and assistant working toward one deadline shows:",
  "Teamwork",["Competition only","Isolation","Neglect"],"Teamwork.")
H('178.d.7.B',4,"Two team members clash over who edits the album. A good first step is to:",
  "Talk it through and agree on roles",["Let it fester","Take sides","Reassign without asking"],"Conflict management.")
H('178.d.7.C',3,"Offering a coworker kind, specific feedback on an edit helps build:",
  "Good working relationships",["Rivalry","Resentment","Isolation"],"Working relationships.")
H('178.d.7.C',4,"Effective feedback on a coworker's composition should be:",
  "Constructive and specific",["Vague and harsh","Personal","Delayed for months"],"Constructive feedback.")
H('178.d.7.D',3,"Writing down meeting goals and who will attend is part of:",
  "Preparing for a meeting",["Leaving early","Skipping planning","Canceling"],"Prepare for meetings.")
H('178.d.7.D',4,"A strong objective for a client planning meeting is one that is:",
  "Clear and measurable",["Hidden","Unrelated","Impossible"],"Meeting objectives.")
H('178.d.7.E',3,"A participant who comes prepared and stays on topic helps the meeting:",
  "Reach its goals",["Run long","Lose focus","Stall"],"Meetings.")
H('178.d.7.E',4,"At the end of a meeting, the leader should summarize:",
  "Decisions and next steps",["Gossip","Complaints","Lunch plans"],"Conduct meetings.")
H('178.d.7.F',3,"An experienced photographer teaching an apprentice to meter light is:",
  "Mentoring",["Competing","Hiding tricks","Avoiding"],"Mentoring.")
H('178.d.7.F',4,"A mentor inspires an apprentice most by:",
  "Showing patience and giving encouragement",["Doing all the work","Criticizing only","Ignoring questions"],"Mentoring.")
H('178.d.8.A',3,"Keeping a client's private photos from being shared without consent is:",
  "Ethical conduct",["Optional","Unneeded","A hassle"],"Ethical conduct.")
H('178.d.8.A',4,"Being honest about a mistake in a delivered gallery shows:",
  "Professional ethics",["Weakness","Carelessness","Poor service"],"Ethics.")
H('178.d.8.B',3,"A photographer's original images are protected by:",
  "Copyright law",["Weather law","Traffic law","Zoning law"],"Copyright.")
H('178.d.8.B',4,"Copying another artist's photo for a client's brochure without permission is generally:",
  "A copyright violation",["Always allowed","A courtesy","Standard practice"],"Copyright and duplication.")
H('178.d.8.C',3,"Before blending a stock photo into a composite, you should confirm you have:",
  "Permission or a proper license",["A free sample","A larger monitor","A faster computer"],"IP respect.")
H('178.d.8.C',4,"Morphing a celebrity's face into an ad without rights raises which concern?",
  "Intellectual property and likeness rights",["Lens quality","Battery drain","Paper weight"],"IP respect.")
H('178.d.8.D',3,"Company acceptable use policies tell staff how to appropriately use:",
  "Work computers and online accounts",["Parking spaces","Break room chairs","Coffee mugs"],"Acceptable use.")
H('178.d.8.D',4,"Using work equipment to download unlicensed software would likely:",
  "Break acceptable use rules",["Be required","Improve security","Be encouraged"],"Acceptable use.")
H('178.d.9.A',3,"Adding a recent magazine shoot and a new certificate to your career file is:",
  "Updating a portfolio",["Wasting space","Filing receipts","Deleting skills"],"Portfolio.")
H('178.d.9.A',4,"A portfolio that includes work experience, awards, and sample images shows an employer:",
  "Your skills and accomplishments",["Your hobbies only","Nothing","Camera prices"],"Portfolio.")
H('178.d.9.B',3,"Comparing two job offers by salary, hours, and growth chances is:",
  "Evaluating employment opportunities",["Guessing","Daydreaming","Complaining"],"Compare employment.")
H('178.d.9.B',4,"Which factor is most useful when comparing two studio job offers?",
  "Pay, benefits, and room to advance",["Color of the lobby","Brand of the coffee","Length of the name"],"Evaluate employment.")
H('178.d.11.A',3,"A product shot for an online store and a magazine ad are examples of:",
  "Commercial photographs",["Family snapshots","Drawings","Paintings"],"Commercial photography.")
H('178.d.11.A',4,"Which image is most clearly a commercial photograph?",
  "A catalog image of shoes",["A selfie shared with friends","A sunset snapshot","A child's drawing"],"Commercial photography.")
H('178.d.11.B',3,"Contrast, balance, and emphasis in a photograph are:",
  "Elements and principles of art",["Camera parts","Paper types","Safety rules"],"Elements and principles of art.")
H('178.d.11.B',4,"A photo where a bright red object stands out against gray shows what principle?",
  "Emphasis through color contrast",["Perfect symmetry","Even pattern","Neutral harmony"],"Principles of art.")
H('178.d.11.C',3,"Meeting with a client to agree on style and a shot list is a principle of:",
  "Commercial photography",["Sculpture","Printmaking","Pottery"],"Commercial photography.")
H('178.d.11.C',4,"A written agreement spelling out price, deadline, and image use protects:",
  "Both photographer and client",["Only the camera","Nobody","Only the lens"],"Commercial photography.")
H('178.d.11.D',3,"A long zoom lens is a good choice for photographing:",
  "Distant sports action",["Tiny jewelry up close","Room interiors","Passport photos"],"Cameras and lenses.")
H('178.d.11.D',4,"For a close-up of a ring, which lens is most appropriate?",
  "A macro lens",["A fisheye lens","A telephoto zoom","A pinhole"],"Cameras and lenses.")
H('178.d.11.E',3,"Placing a subject along a line that splits the frame into thirds helps with:",
  "Composition",["Battery life","File size","Shutter noise"],"Composition and layout.")
H('178.d.11.E',4,"Leaving blank space where a client's ad text will go is part of planning:",
  "Layout",["Printing","Mounting","Packing"],"Composition and layout.")
H('178.d.11.F',3,"Converting a color image to shades of gray produces a:",
  "Black and white photograph",["Panorama","Macro image","Sepia lens"],"Digital black and white and color.")
H('178.d.11.F',4,"A color setting that shows images as they look to the eye on a screen is commonly set in:",
  "RGB mode",["Metric mode","Binary mode","Audio mode"],"Digital color.")
H('178.d.11.G',3,"A key light, fill light, and back light together make up:",
  "Three-point lighting",["Flat lighting only","Natural light only","Candlelight"],"Lighting techniques.")
H('178.d.11.G',4,"Which light is usually placed behind a subject to separate them from the background?",
  "The back light",["The key light","The fill light","The ambient flash"],"Lighting techniques.")
H('178.d.11.H',3,"Sharp focus, correct exposure, and good composition are elements of:",
  "A professional quality photograph",["A blurry shot","An accident","A rough draft"],"Professional quality.")
H('178.d.11.H',4,"Which flaw would a client most likely reject in a final image?",
  "Out-of-focus subject",["Clean background","Accurate color","Even lighting"],"Professional quality.")
H('178.d.11.I',3,"A photographer picks a paper with a shiny coating for vivid color prints. This is:",
  "Glossy paper",["Matte paper","Newsprint","Tissue"],"Photographic paper.")
H('178.d.11.I',4,"A framed print that must avoid glare under bright gallery lights is best printed on:",
  "Matte paper",["Glossy paper","Plastic film","Foil"],"Photographic paper.")
H('178.d.11.J',3,"A border of cardboard placed between a print and its frame is a:",
  "Mat",["Lens","Tripod","Filter"],"Mounting and matting.")
H('178.d.11.J',4,"Gluing a print to a stiff board before display is called:",
  "Mounting",["Scanning","Cropping","Focusing"],"Mounting.")
H('178.d.11.K',3,"Following current methods from capture to final print is using:",
  "Industry-standard production processes",["Random steps","Outdated habits","Guesswork"],"Production processes.")
H('178.d.11.K',4,"A professional workflow usually backs up images:",
  "Right after the shoot",["Never","After a year","After deleting them"],"Production processes.")
H('178.d.11.L',3,"Judging a photograph by its composition, lighting, and message is:",
  "Evaluating a photograph",["Printing it","Mounting it","Shooting it"],"Evaluate photographs.")
H('178.d.11.L',4,"A helpful evaluation of a photo should include:",
  "Specific strengths and ways to improve",["Only insults","Only price","Nothing"],"Evaluate photographs.")
H('178.d.11.M',3,"Pixels per inch describe an image's:",
  "Resolution",["Weight","Color name","Lens type"],"Resolution.")
H('178.d.11.M',4,"A format that keeps all sensor data for editing is:",
  "RAW",["GIF","BMP thumbnail","Text file"],"Digital file formats.")
H('178.d.11.N',3,"Using balance, emphasis, and unity to discuss a photograph applies:",
  "Principles of design",["Safety rules","Printing codes","Billing steps"],"Principles of design.")
H('178.d.11.N',4,"A critique that mentions movement leading the viewer's eye across the frame uses:",
  "Design vocabulary",["Slang","Guesswork","Rumor"],"Critique.")
H('178.d.11.O',3,"Arranging shapes so the viewer's eye moves smoothly through a photo shows knowledge of:",
  "Principles of design",["Camera repair","Paper weight","Shutter speed"],"Principles of design.")
H('178.d.11.O',4,"A photo with balanced weights on both sides, like a mirrored scene, shows:",
  "Symmetrical balance",["Random scatter","Heavy imbalance","Pure noise"],"Principles of design.")

# ---------- 127.179 Commercial Photography Practicum (application level) ----------
H('179.d.5',3,"A freelance photographer uses invoicing software and a booking calendar. These are:",
  "Technology applications",["Hand tools","Safety signs","Light stands"],"Technology applications.")
H('179.d.5',4,"Using automatic file backup software for client work primarily protects against:",
  "Loss of images",["Sharper lenses","Warmer color","Loud noise"],"Technology applications.")
H('179.d.6',3,"Setting up a camera, lights, backdrop, and computer for a product shoot involves:",
  "A commercial photography system",["A weather system","A subway system","A watering system"],"Photography systems.")
H('179.d.6',4,"Tethering a camera to a laptop during a studio shoot lets the team:",
  "Review images at once",["Skip lighting","Print instantly","Avoid editing"],"Photography systems.")
H('179.d.1.A',3,"A student who earns an Adobe or similar software certification is taking part in:",
  "Certification for employment",["A vacation","A game","A chore"],"Training.")
H('179.d.1.A',4,"Attending a lighting workshop mainly helps a photographer to:",
  "Strengthen job skills",["Avoid learning","Skip practice","Hide mistakes"],"Training.")
H('179.d.1.B',3,"Meeting deadlines and keeping a calm attitude with clients are:",
  "Positive work behaviors",["Poor habits","Optional extras","Barriers"],"Work behaviors.")
H('179.d.1.B',4,"A photographer who stays reliable under tight deadlines shows:",
  "Dependability",["Carelessness","Impatience","Avoidance"],"Personal qualities.")
H('179.d.1.C',3,"Writing a cover letter and sending a resume to a studio is:",
  "Applying for a job",["Quitting","Resigning","Retiring"],"Seeking employment.")
H('179.d.1.C',4,"Which action best prepares an applicant for a photography job interview?",
  "Bringing a curated portfolio",["Arriving empty-handed","Skipping research","Showing every shot ever taken"],"Obtaining a job.")
H('179.d.2.A',3,"Writing a polished email proposal for a product shoot uses:",
  "English language arts skills",["Welding skills","Carpentry skills","Cooking skills"],"ELA.")
H('179.d.2.A',4,"Proofreading a quote before sending it to a client helps avoid:",
  "Costly misunderstandings",["Extra work","Lens flare","Sensor dust"],"ELA.")
H('179.d.2.B',3,"A product shoot costs $90 per hour. How much for 5 hours?",
  "$450",["$360","$405","$495"],"90 x 5 = 450.")
H('179.d.2.B',4,"A job pays $600 and expenses are 35 percent of that. What are the expenses?",
  "$210",["$165","$350","$21"],"600 x 0.35 = 210.")
H('179.d.3.A',3,"Using plain language to explain image licensing to a small business owner is adapting to the:",
  "Audience",["Hard drive","Tripod","Lens hood"],"Adapt language.")
H('179.d.3.A',4,"A casual note to a friend and a client contract differ in tone because of:",
  "Purpose and situation",["Camera type","Paper stock","Memory size"],"Adapt language.")
H('179.d.3.B',3,"Arranging a shoot plan so the steps follow a logical order is:",
  "Organizing information",["Retouching","Printing","Exposing"],"Organize.")
H('179.d.3.B',4,"Why keep a written shot list in order of priority?",
  "To make sure key shots are captured first",["To slow the shoot","To confuse the crew","To delay payment"],"Organize.")
H('179.d.3.C',3,"A photographer explains to an assistant that the light meter shows one stop too dark. This is:",
  "Communicating data",["Hiding facts","Guessing","Complaining"],"Interpret and communicate.")
H('179.d.3.C',4,"Showing a client two crops and describing how each affects the message is:",
  "Communicating observations",["Withholding choices","Confusing the client","Skipping feedback"],"Communicate.")
H('179.d.3.D',3,"Pitching a campaign concept to a marketing team on a scheduled call is a:",
  "Formal presentation",["Hallway remark","Break","Rumor"],"Formal presentation.")
H('179.d.3.D',4,"Quickly explaining a lighting tweak to a model between shots is a(n):",
  "Informal presentation",["Board report","Press release","Keynote"],"Informal presentation.")
H('179.d.3.E',3,"A photographer who repeats back the art director's notes before editing demonstrates:",
  "Active listening",["Ignoring","Interrupting","Multitasking"],"Active listening.")
H('179.d.3.E',4,"Asking for an example image from a client when a request is unclear helps to:",
  "Clarify expectations",["Avoid feedback","Create confusion","Lose time"],"Active listening.")
H('179.d.3.F',3,"A photographer who respects people's customs on a shoot is practicing:",
  "Working with diverse individuals",["Stereotyping","Excluding","Teasing"],"Diverse individuals.")
H('179.d.3.F',4,"Learning how to pronounce a client's name correctly is a way to:",
  "Show respect",["Save time","Avoid contact","Win an argument"],"Diversity.")
H('179.d.3.G',3,"Responding quickly and kindly to a client's question builds:",
  "Customer relations",["Dust","Delays","Disorder"],"PR skills.")
H('179.d.3.G',4,"Offering a small print as thanks to a long-time client supports:",
  "Customer loyalty",["Price hikes","Lens upgrades","Poor reviews"],"PR skills.")
H('179.d.4.A',3,"Deciding whether to use natural window light or a strobe by testing both is:",
  "Critical thinking",["Guessing","Panic","Copying"],"Critical thinking.")
H('179.d.4.A',4,"Using client feedback to choose the best edit relies on:",
  "Evidence-based decisions",["Random picks","Habit only","Ignoring input"],"Critical thinking.")
H('179.d.4.B',3,"When a stylist and photographer disagree, a good group approach is to:",
  "Hear both views and test ideas",["Insult each other","Stop working","Pick randomly"],"Interpersonal skills.")
H('179.d.4.B',4,"A team solves a lighting problem best when members:",
  "Share ideas and listen",["Stay silent","Compete","Work apart"],"Group problem solving.")
H('179.d.7.A',3,"Using sandbags on top-heavy light stands follows:",
  "Workplace safety rules",["A style tip","A pricing rule","A color rule"],"Safety.")
H('179.d.7.A',4,"Why should photographers never overload a power strip with strobes?",
  "It can cause fire or shock",["It improves color","It speeds recycling","It sharpens focus"],"Safety regulations.")
H('179.d.7.B',3,"If a strobe smokes, the first thing to do is to:",
  "Power down safely and follow emergency steps",["Keep shooting","Cover it","Ignore it"],"Emergency procedures.")
H('179.d.7.B',4,"Knowing the location of fire extinguishers and exits is part of:",
  "Emergency preparedness",["Marketing","Retouching","Billing"],"Emergency procedures.")
H('179.d.8.A',3,"A lead photographer who sets goals and delegates fairly is showing:",
  "Leadership",["Avoidance","Neglect","Blame"],"Leadership.")
H('179.d.8.A',4,"A leader who evaluates results after each project is working to:",
  "Improve future outcomes",["Hide problems","End the team","Add blame"],"Leadership.")
H('179.d.8.B',3,"A crew sharing tasks to finish a catalog shoot on time shows:",
  "Teamwork",["Isolation","Rivalry only","Delay"],"Teamwork.")
H('179.d.8.B',4,"To settle a disagreement over shot priority, a team should first:",
  "Discuss it respectfully",["Ignore it","Quit","Argue publicly"],"Conflict management.")
H('179.d.8.C',3,"Thanking a coworker and giving useful feedback helps create:",
  "Effective working relationships",["Tension","Silence","Rivalry"],"Working relationships.")
H('179.d.8.C',4,"Feedback is most helpful when it is:",
  "Specific and respectful",["Vague","Harsh","Late"],"Constructive feedback.")
H('179.d.8.D',3,"Setting a clear goal and agenda before a client call is:",
  "Preparing for a meeting",["Wasting time","Delaying work","Avoiding clients"],"Prepare for meetings.")
H('179.d.8.D',4,"A good meeting objective for a pre-shoot call is to:",
  "Confirm the shot list and schedule",["Share gossip","Avoid decisions","Discuss unrelated topics"],"Meeting objectives.")
H('179.d.8.E',3,"A participant who listens and contributes ideas helps a meeting:",
  "Accomplish its goals",["Run long","Stall","Fail"],"Meetings.")
H('179.d.8.E',4,"After a meeting, sending out notes with action items helps the team:",
  "Follow through on decisions",["Forget tasks","Disagree later","Skip work"],"Conduct meetings.")
H('179.d.8.F',3,"A senior photographer who patiently teaches an intern to use a light meter is:",
  "Mentoring",["Competing","Hiding tips","Avoiding"],"Mentoring.")
H('179.d.8.F',4,"An effective mentor builds a trainee's:",
  "Skills and confidence",["Dependence","Doubt","Fear"],"Mentoring.")
H('179.d.9.A',3,"Telling a client the truth about what a package includes is:",
  "Ethical conduct",["Optional","Poor business","Unnecessary"],"Ethical conduct.")
H('179.d.9.A',4,"Keeping a client's shoot schedule private from others is:",
  "Respecting confidentiality",["Hiding profits","Breaking rules","Wasting time"],"Ethics.")
H('179.d.9.B',3,"Using a photo from a website without permission can result in:",
  "A copyright infringement claim",["A free upgrade","A discount","A new camera"],"Copyright.")
H('179.d.9.B',4,"Using a small portion of an image for a classroom review may fall under:",
  "Fair use",["Piracy","Theft","Resale"],"Fair use.")
H('179.d.9.C',3,"Combining your own photo with a licensed icon pack requires:",
  "Following the license terms",["Ignoring them","Removing credits","Reselling the pack"],"IP respect.")
H('179.d.9.C',4,"Editing a model's face in a way not covered by the release is:",
  "A rights and ethics problem",["A safe shortcut","Required","A client request"],"IP respect.")
H('179.d.9.D',3,"Using work devices only for approved purposes follows:",
  "Acceptable use policies",["Weather rules","Dress codes","Parking rules"],"Acceptable use.")
H('179.d.9.D',4,"Polite, professional language in online messages with clients shows good:",
  "Etiquette",["Slang","Rudeness","Haste"],"Etiquette.")
H('179.d.10.A',3,"Collecting your strongest shots and a record of your experience is:",
  "Building a portfolio",["Filing taxes","Cleaning gear","Mounting prints"],"Portfolio.")
H('179.d.10.A',4,"A portfolio is best updated:",
  "When you complete strong new work",["Never","Once a decade","Only when asked"],"Portfolio.")
H('179.d.10.B',3,"Comparing job offers by pay, schedule, and benefits is:",
  "Evaluating employment options",["Guessing","Complaining","Daydreaming"],"Compare employment.")
H('179.d.10.B',4,"Which is most important when comparing a staff job with freelancing?",
  "Income stability and benefits",["Brand of camera","Studio paint color","Office coffee"],"Evaluate employment.")
H('179.d.11.A',3,"Setting milestones for a multi-day shoot and building a calendar is:",
  "Planning and time management",["Printing","Mounting","Retouching"],"Planning.")
H('179.d.11.A',4,"Allowing buffer time between sessions helps a photographer to:",
  "Avoid running behind schedule",["Lose clients","Skip lunch only","Shoot less"],"Time management.")
H('179.d.11.B',3,"Adding up gear rental, editing time, and travel to set a price is:",
  "Creating a quote",["Printing","Mounting","Cropping"],"Quotes and budgets.")
H('179.d.11.B',4,"A freelancer who forgets to include editing hours in a quote may:",
  "Lose money on the job",["Gain profit","Save time","Impress clients"],"Budgeting.")
H('179.d.12.A',3,"Shooting a lifestyle series for a clothing brand's website means creating photographs for:",
  "A defined purpose",["No reason","Random fun","A hidden agenda"],"Create photographs.")
H('179.d.12.A',4,"A photographer first clarifies the intended use of an image because it:",
  "Guides style, size, and framing",["Changes the weather","Changes the lens brand","Changes the date"],"Create photographs.")
H('179.d.12.B',3,"Using a strong diagonal line to add energy to an ad image applies:",
  "Elements of art",["Camera repair","Billing rules","Printing codes"],"Elements and principles of art.")
H('179.d.12.B',4,"Repeating shapes across a product layout to create unity applies:",
  "Principles of art",["Safety rules","Shipping rules","File naming"],"Elements and principles of art.")
H('179.d.12.C',3,"Planning shots with a client and agreeing on a contract demonstrates:",
  "Principles of commercial photography",["Gardening basics","Cooking basics","Sewing basics"],"Commercial photography.")
H('179.d.12.C',4,"A model release is used so a commercial photographer can:",
  "Use a person's image legally",["Sell cameras","Skip lighting","Reduce file size"],"Commercial photography.")
H('179.d.12.D',3,"A photographer selects a wide-angle lens to photograph a cramped room interior. This is:",
  "Using appropriate lenses",["Choosing randomly","Ignoring needs","Wasting gear"],"Cameras and lenses.")
H('179.d.12.D',4,"Which lens best compresses distance for a flattering headshot?",
  "A short telephoto",["A fisheye","An ultra-wide","A pinhole"],"Cameras and lenses.")
H('179.d.12.E',3,"Placing the subject at a third line and leaving room for a headline demonstrates:",
  "Composition and layout principles",["Battery care","Cable wrapping","Memory storage"],"Composition and layout.")
H('179.d.12.E',4,"Framing a product with an empty area for text helps the client by:",
  "Leaving space for the ad copy",["Hiding the product","Confusing the layout","Blocking the logo"],"Composition and layout.")
H('179.d.12.F',3,"Converting a portrait to monochrome in editing software is:",
  "Digital black and white photography",["Color printing","Film processing","Scanning"],"Digital black and white and color.")
H('179.d.12.F',4,"Matching the colors on a monitor to a printed proof requires:",
  "Color calibration",["More noise","A bigger tripod","Louder fans"],"Digital color.")
H('179.d.12.G',3,"Placing a main light at 45 degrees with a softer fill opposite it applies:",
  "Three-point lighting",["Flat lighting only","Noon sunlight","Candle glow"],"Lighting techniques.")
H('179.d.12.G',4,"Adding a hair light from behind a model mainly helps to:",
  "Separate the subject from the background",["Darken the face","Add noise","Block the key light"],"Lighting techniques.")
H('179.d.12.H',3,"Sharp focus, accurate color, and clean framing indicate a:",
  "Professional quality photograph",["Rough draft","Blurry snapshot","Test scribble"],"Professional quality.")
H('179.d.12.H',4,"Before delivery, a photographer should check images for:",
  "Dust spots, color casts, and crop issues",["Brand names of lenses","Studio temperature","Lunch orders"],"Professional quality.")
H('179.d.12.I',3,"A photographer chooses heavy matte stock for a fine art print because it:",
  "Resists glare and feels premium",["Is cheapest","Absorbs no ink","Is transparent"],"Photographic paper.")
H('179.d.12.I',4,"An archival cotton paper is selected when a print should:",
  "Last for decades without fading",["Be disposable","Be free","Dissolve"],"Paper selection.")
H('179.d.12.J',3,"Placing a print behind a window mat inside a frame is a way of:",
  "Mounting and matting",["Scanning","Resizing","Focusing"],"Mounting and matting.")
H('179.d.12.J',4,"A mat that is acid-free protects a print from:",
  "Discoloration over time",["Wi-Fi loss","Lens flare","Noise"],"Matting solutions.")
H('179.d.12.K',3,"Following today's accepted methods from shooting through delivery shows use of:",
  "Industry-standard production processes",["Random steps","Old shortcuts","Guesswork"],"Production processes.")
H('179.d.12.K',4,"Naming and backing up files with a consistent system is part of:",
  "A professional workflow",["Wasted effort","Optional hobby","Printing"],"Production processes.")
H('179.d.12.L',3,"Reviewing a final photo against the creative brief is:",
  "Evaluating the work",["Printing it","Mounting it","Hiding it"],"Evaluate photographs.")
H('179.d.12.L',4,"A useful evaluation of an ad image compares it with:",
  "The client's goals and design principles",["The weather","The photographer's mood","The price of paper"],"Evaluate photographs.")
H('179.d.12.M',3,"A file prepared at 300 pixels per inch is suited for:",
  "Sharp printing",["Tiny icons only","Audio","Video only"],"Resolution.")
H('179.d.12.M',4,"A format with compression that creates small files for web delivery is:",
  "JPEG",["RAW","Tape","Audio file"],"Digital file formats.")

# ---------- 127.180 Fashion / Apparel (Fashion Design / Apparel Services) ----------
H('180.d.4',3,"A designer uses pattern software and a digital sketch app. These are:",
  "Technology applications",["Hand shears only","Fire exits","Pins"],"Technology applications.")
H('180.d.4',4,"Why might an apparel business use inventory software?",
  "To track garments and supplies accurately",["To hide stock","To slow orders","To avoid customers"],"Technology applications.")
H('180.d.6',3,"Keeping cords away from an iron's hot surface is following:",
  "Safety rules",["Style rules","Pricing rules","Color rules"],"Safety.")
H('180.d.6',4,"Which action best prevents needle-stick injuries at a sewing table?",
  "Keeping fingers clear of the needle",["Sewing faster","Removing guards","Working while tired"],"Safety regulations.")
H('180.d.9',3,"A tailor who learns shortcuts on the sewing machine is building technical skills for:",
  "Efficiency",["Delay","Confusion","Waste"],"Technical skills.")
H('180.d.9',4,"Cutting several layers of fabric at once with a pattern is an efficient way to:",
  "Produce many pieces in less time",["Waste fabric","Slow the line","Increase errors"],"Technical skills.")
H('180.d.1.A',3,"Reading a pattern's written directions carefully applies:",
  "English language arts skills",["Welding skills","Plumbing skills","Driving skills"],"ELA.")
H('180.d.1.A',4,"Writing a clear label for a garment's care instructions uses:",
  "Precise, readable wording",["Slang","Vague hints","Long stories"],"ELA.")
H('180.d.1.B',3,"A dress needs 3.5 yards of fabric. How many yards for 4 dresses?",
  "14",["12","10.5","17.5"],"3.5 x 4 = 14.")
H('180.d.1.B',4,"Fabric costs $8.50 per yard. A jacket uses 2 yards and lining costs $6. What is the material total?",
  "$23",["$17","$25","$14.50"],"8.50 x 2 = 17; 17 + 6 = 23.")
H('180.d.2.A',3,"Using fashion terms with a design team but plain words with a shopper is adapting language for:",
  "Audience",["Fabric","Thread","Buttons"],"Adapt language.")
H('180.d.2.A',4,"A message to a buyer about price differs from one to a seamstress about fit because of the:",
  "Purpose and situation",["Zipper","Hem","Button"],"Adapt language.")
H('180.d.2.B',3,"Writing the order of steps to sew a skirt is:",
  "Organizing written information",["Cutting","Pressing","Dyeing"],"Organize.")
H('180.d.2.B',4,"Putting measurement notes in a labeled list helps a designer to:",
  "Find details quickly",["Lose notes","Skip fittings","Hide errors"],"Organize.")
H('180.d.2.C',3,"A designer says the sleeve length measures an inch too long. This is:",
  "Communicating an observation",["Guessing","Hiding errors","Ignoring"],"Interpret and communicate.")
H('180.d.2.C',4,"Reading a sales chart to explain which color sold best is:",
  "Interpreting data",["Dyeing fabric","Sewing seams","Pressing"],"Interpret information.")
H('180.d.2.D',3,"Showing a seasonal collection to buyers at a scheduled event is a:",
  "Formal presentation",["Casual remark","Daydream","Rumor"],"Formal presentation.")
H('180.d.2.D',4,"Quickly explaining a hem change to a coworker at the sewing table is a(n):",
  "Informal presentation",["Fashion show","Keynote","Press release"],"Informal presentation.")
H('180.d.2.E',3,"A tailor who nods, listens, and asks about the client's needs is using:",
  "Active listening",["Interrupting","Ignoring","Texting"],"Active listening.")
H('180.d.2.F',3,"Helping shoppers of many backgrounds find clothing that fits calls for:",
  "Respectful communication",["Stereotyping","Rushing","Ignoring"],"Diverse individuals.")
H('180.d.2.E',4,"Repeating a client's requested alteration back to them ensures:",
  "Shared understanding",["Errors","Delay","Conflict"],"Active listening.")
H('180.d.2.F',4,"A boutique worker who learns about customers' cultural dress traditions is:",
  "Communicating respectfully with diverse people",["Excluding customers","Teasing shoppers","Avoiding questions"],"Diversity.")
H('180.d.2.G',3,"Greeting every customer warmly and following up on special orders shows:",
  "Public relations skills",["Poor service","Disinterest","Rudeness"],"PR skills.")
H('180.d.2.G',4,"A fashion retailer that politely resolves a return problem improves:",
  "Customer loyalty",["Customer complaints","Employee turnover","Shipping costs"],"PR skills.")
H('180.d.3.A',3,"Comparing three fabrics for durability before choosing one is:",
  "Critical thinking",["Guessing","Luck","Habit"],"Critical thinking.")
H('180.d.3.A',4,"A design team picks a final garment style after reviewing sales and costs. This relies on:",
  "Evidence-based thinking",["Random choice","Ignoring data","Copying"],"Critical thinking.")
H('180.d.3.B',3,"Two seamstresses disagree on a pattern change. A good interpersonal step is to:",
  "Test both ideas on a sample",["Argue","Walk away","Blame each other"],"Interpersonal skills.")
H('180.d.3.B',4,"Group problem solving in a workroom goes best when members:",
  "Listen and share ideas",["Interrupt","Work separately","Stay silent"],"Group problem solving.")
H('180.d.5.A',3,"Studying how clothing styles changed from one century to the next is:",
  "Analyzing fashion history",["Sewing a hem","Pressing cloth","Dyeing thread"],"Fashion history.")
H('180.d.5.A',4,"Why do designers study past eras of clothing?",
  "To learn influences on styles and trends",["To avoid new ideas","To copy exactly","To skip creativity"],"Fashion history.")
H('180.d.5.B',3,"Noticing that a current jacket silhouette resembles a vintage style is:",
  "Comparing history with current trends",["Dyeing cloth","Shipping goods","Printing labels"],"Fashion history and trends.")
H('180.d.5.B',4,"Fashion revivals show that styles often:",
  "Return in updated forms",["Never repeat","Disappear forever","Ignore the past"],"Fashion cycles.")
H('180.d.7.A',3,"A workroom lead who sets goals for a collection and guides the team shows:",
  "Leadership",["Avoidance","Neglect","Blame"],"Leadership.")
H('180.d.7.A',4,"A strong leader gives the team:",
  "Clear direction and support",["Confusion","Silence","Blame"],"Leadership.")
H('180.d.7.B',3,"Respect, honesty, and reliability are characteristics of:",
  "Effective working relationships",["Poor teams","Weak plans","Unsafe shops"],"Working relationships.")
H('180.d.7.B',4,"A coworker who shares credit and communicates openly builds:",
  "Trust",["Rivalry","Suspicion","Distance"],"Working relationships.")
H('180.d.7.C',3,"Taking part in a fitting-room team huddle and contributing ideas is:",
  "Participating in groups",["Skipping work","Leaving early","Staying silent"],"Participate in groups.")
H('180.d.7.C',4,"A good group member:",
  "Listens and shares responsibility",["Dominates","Ignores others","Avoids tasks"],"Participate in groups.")
H('180.d.7.D',3,"An experienced pattern maker showing a new hire how to mark darts is:",
  "Mentoring",["Competing","Hiding tricks","Ignoring"],"Mentoring.")
H('180.d.7.D',4,"A good mentor to a new tailor:",
  "Teaches skills and encourages growth",["Takes over every task","Criticizes only","Withholds help"],"Mentoring.")
H('180.d.8.A',3,"Not discussing a client's body measurements with others is:",
  "Maintaining client confidentiality",["Gossiping","Sharing freely","Advertising"],"Ethical conduct.")
H('180.d.8.A',4,"A designer who gives honest prices and delivers what was promised exhibits:",
  "Ethical conduct",["Poor judgment","Weak business","Carelessness"],"Ethics.")
H('180.d.8.B',3,"Copying another designer's original print and selling it as your own would:",
  "Violate copyright law",["Be fair play","Be a courtesy","Be required"],"Copyright.")
H('180.d.8.B',4,"A designer creating an original textile pattern holds copyright on it because it is:",
  "An original creative work",["Common thread","A public sign","A trademark only"],"Copyright.")
H('180.d.8.C',3,"Fashion trends can influence how people feel about:",
  "Identity and belonging",["Weather","Soil","Traffic"],"Fashion and society.")
H('180.d.8.C',4,"Fast fashion's rapid production affects society by contributing to:",
  "Textile waste concerns",["Less clothing","Fewer trends","Higher quality"],"Fashion industry influences.")
H('180.d.10.A',3,"Clothing provides protection, comfort, and a way to express:",
  "Personal identity",["Weather","Hunger","Gravity"],"Value of fashion.")
H('180.d.10.A',4,"Fashion adds economic value by creating:",
  "Jobs and sales",["Rain","Mountains","Rivers"],"Value of fashion.")
H('180.d.10.B',3,"High-end couture, ready-to-wear, and mass-market lines show the:",
  "Spectrum of the fashion industry",["Weather","Soil types","Road types"],"Fashion industry.")
H('180.d.10.B',4,"Garments made to order for one client, usually by hand, are called:",
  "Haute couture",["Fast fashion","Uniforms","Surplus"],"Fashion industry.")
H('180.d.10.C',3,"Magazines such as Vogue and Elle are examples of:",
  "Fashion publications",["Science journals","Auto manuals","Cookbooks"],"Fashion publications.")
H('180.d.10.C',4,"Fashion editors use publications to:",
  "Showcase trends and designers",["Hide trends","Teach plumbing","Sell tires"],"Fashion publications.")
H('180.d.10.D',3,"Styles that rise in popularity, peak, and decline follow the:",
  "Fashion cycle",["Water cycle","Rock cycle","Moon cycle"],"Fashion cycle.")
H('180.d.10.D',4,"In the fashion cycle, a style at its peak is widely:",
  "Accepted and worn",["Unknown","Banned","Forgotten"],"Fashion cycle.")
H('180.d.10.E',3,"Using the terms silhouette, hem, and bias correctly shows use of:",
  "Appropriate terminology",["Slang","Guesswork","Nicknames"],"Fashion terminology.")
H('180.d.10.E',4,"The line where the edge of a skirt is folded and stitched is the:",
  "Hem",["Dart","Pleat","Collar"],"Fashion terminology.")
H('180.d.11.A',3,"A clothing company that makes garments overseas and sells them in the U.S. shows how economies are:",
  "Interrelated",["Separate","Frozen","Unlinked"],"Global economy.")
H('180.d.11.A',4,"A rise in cotton prices abroad can affect:",
  "Garment prices at home",["Nothing","Only shoes","The moon"],"Global economy.")
H('180.d.11.B',3,"Laws about minimum wage and safe working conditions in garment factories are:",
  "Labor laws",["Fashion tips","Pricing tricks","Style rules"],"Labor laws.")
H('180.d.11.B',4,"Labor laws differ among countries, so companies sourcing abroad should:",
  "Check working conditions at suppliers",["Ignore them","Hide them","Raise prices only"],"Labor laws.")
H('180.d.11.C',3,"Recycling fabric scraps and using water-saving dyes help to:",
  "Protect the environment",["Waste resources","Increase landfill","Add pollution"],"Environmental procedures.")
H('180.d.11.C',4,"Choosing organic cotton is one way an apparel company can:",
  "Reduce environmental impact",["Raise pollution","Use more pesticides","Waste more water"],"Environmental procedures.")
H('180.d.11.D',3,"Computerized cutting machines and 3D body scanners are examples of:",
  "Technological advancements",["Hand tools","Old methods","Folk crafts"],"Technology in apparel.")
H('180.d.11.D',4,"Automated cutting improves apparel production by:",
  "Increasing speed and accuracy",["Adding errors","Slowing output","Wasting more cloth"],"Technology in apparel.")
H('180.d.12.A',3,"A person's age, culture, and stage of life affect:",
  "Clothing choices",["Weather","Soil","Traffic"],"Influences on apparel choices.")
H('180.d.12.A',4,"A new parent may choose clothing that is mostly:",
  "Comfortable and easy to care for",["Impractical","Fragile","Hard to wash"],"Life cycle influences.")
H('180.d.12.B',3,"Designers, celebrities, and street style help determine:",
  "Fashion trends",["Soil quality","Rainfall","Tides"],"Fashion trends.")
H('180.d.12.B',4,"Trend forecasters study runway shows and consumer behavior to:",
  "Predict upcoming trends",["Delete data","Avoid forecasting","Create weather"],"Fashion trends.")
H('180.d.12.C',3,"Ads that show a model wearing a jacket in a lifestyle scene can sway shoppers to:",
  "Buy the item",["Skip shopping","Return it","Ignore fashion"],"Advertising influence.")
H('180.d.12.C',4,"Social media influencers affect apparel purchases by:",
  "Shaping what shoppers find desirable",["Reducing options","Lowering interest","Removing brands"],"Advertising influence.")
H('180.d.12.D',3,"Adding adaptive closures like magnets for someone with limited hand mobility is a technique for:",
  "Special needs apparel management",["Mass advertising","Fabric dyeing","Hem measuring"],"Special needs apparel.")
H('180.d.12.D',4,"Clothing for a person who uses a wheelchair is often designed with:",
  "Longer backs and no bulky seams in the seat",["Short backs","Tight waists only","Heavy buckles"],"Special needs apparel.")
H('180.d.13.A',3,"Reading the symbols on a garment tag tells you how to:",
  "Wash and dry it",["Dye it","Sell it","Photograph it"],"Care labels.")
H('180.d.13.A',4,"A tag with a crossed-out triangle means:",
  "Do not bleach",["Bleach freely","Tumble dry high","Iron on high"],"Care labels.")
H('180.d.13.B',3,"Comparing detergents for use on wool is:",
  "Evaluating clothing care products",["Dyeing","Sewing","Cutting"],"Care products.")
H('180.d.13.B',4,"A product best for removing oil stains from cotton is chosen by checking:",
  "The label and fabric compatibility",["The color of the bottle","The price only","The store location"],"Care products.")
H('180.d.13.C',3,"Deciding between home washing and a professional cleaner for a silk dress is:",
  "Choosing care services",["Dyeing","Sketching","Cutting"],"Care and maintenance.")
H('180.d.13.C',4,"A pressing steamer is a good tool for:",
  "Removing wrinkles from delicate fabrics",["Cutting cloth","Dyeing","Measuring"],"Care equipment.")
H('180.d.13.D',3,"Keeping bleach and ammonia-based cleaners apart is:",
  "A care product safety rule",["A fashion rule","A pricing rule","A style rule"],"Safety.")
H('180.d.13.D',4,"When using a hot iron, a safe practice is to:",
  "Turn it off and unplug it when finished",["Leave it on","Tuck the cord under it","Rest it face down"],"Safety.")
H('180.d.13.E',3,"Choosing a dry-clean-only jacket affects ongoing:",
  "Care costs",["Fabric dye","Button size","Hem length"],"Clothing care and selection.")
H('180.d.13.E',4,"A buyer wanting low upkeep might prefer fabrics that are:",
  "Machine washable",["Dry-clean only","Hand wash only","Spot clean only"],"Clothing care and selection.")
H('180.d.14.A',3,"Tagging each customer's order at a dry cleaner helps to:",
  "Identify items correctly",["Lose items","Confuse orders","Increase mistakes"],"Receive and mark.")
H('180.d.14.A',4,"Checking pockets and noting stains before cleaning protects:",
  "Both garment and customer",["Only the store","Nobody","Only the machine"],"Receive and mark.")
H('180.d.14.B',3,"Sorting garments by color and fabric before washing is a:",
  "Laundry procedure",["Sewing step","Sketching step","Pricing step"],"Laundry procedures.")
H('180.d.14.B',4,"Dark colors are washed separately from whites to prevent:",
  "Dye transfer",["Shrinking only","Static","Wrinkles only"],"Laundry procedures.")
H('180.d.14.C',3,"Using chemicals in a dry-cleaning shop calls for:",
  "Proper ventilation and safety gear",["No precautions","Extra heat","Open flames"],"Safety and sanitation.")
H('180.d.14.C',4,"Cleaning lint traps regularly in dryers helps reduce:",
  "Fire risk",["Cost of soap","Color","Wrinkles"],"Safety and sanitation.")
H('180.d.14.D',3,"A solvent-based method used instead of water for delicate clothes is:",
  "Dry cleaning",["Hand sewing","Dyeing","Embroidery"],"Commercial techniques.")
H('180.d.14.D',4,"Commercial laundries use large machines mostly to:",
  "Process many items efficiently",["Save water by hand washing","Cut cloth","Sew buttons"],"Commercial techniques.")
H('180.d.14.E',3,"Using the correct temperature and a pressing cloth on silk shows knowledge of:",
  "Pressing procedures",["Dyeing","Cutting","Printing"],"Pressing.")
H('180.d.14.E',4,"Pressing a seam open before sewing the next piece helps to produce:",
  "A crisp, flat finish",["More wrinkles","Puckers","A frayed edge"],"Pressing.")
H('180.d.15.A',3,"Listing monthly clothing costs and care costs is creating:",
  "A budget",["A pattern","A hem","A trend"],"Apparel budget.")
H('180.d.15.A',4,"A person who sets a clothing budget of $120 and spends $45 on shoes has how much left?",
  "$75",["$85","$165","$65"],"120 - 45 = 75.")
H('180.d.15.B',3,"Comparing prices at a thrift store, a department store, and online is:",
  "Comparing purchase sources",["Sewing","Dyeing","Cutting"],"Apparel purchases.")
H('180.d.15.B',4,"Which source usually offers the lowest price for a barely worn coat?",
  "A resale or thrift shop",["A designer boutique","A luxury brand store","A custom tailor"],"Apparel purchases.")
H('180.d.15.C',3,"Online shopping and virtual try-on tools show how technology affects:",
  "Consumer purchasing options",["Fabric dye","Seam types","Zipper sizes"],"Technology and purchasing.")
H('180.d.15.C',4,"A benefit of online shopping for shoppers is that they can:",
  "Compare many stores quickly",["Touch the fabric first","Try on in person","Avoid shipping"],"Technology and purchasing.")
H('180.d.15.D',3,"Turning old jeans into tote bags is an example of:",
  "Recycling apparel",["Throwing away","Burning","Wasting"],"Recycling apparel.")
H('180.d.15.D',4,"Organizing a clothing swap helps a community to:",
  "Reuse garments and reduce waste",["Increase waste","Raise prices","Lower sharing"],"Recycling apparel.")
H('180.d.16.A',3,"Shapes such as hourglass, rectangle, and pear describe basic:",
  "Body types",["Fabrics","Colors","Needle sizes"],"Body types.")
H('180.d.16.A',4,"A designer studies body types because garments need to:",
  "Fit and flatter different figures",["Be identical","Be uncomfortable","Hide labels"],"Body types.")
H('180.d.16.B',3,"Making sure the top and bottom of an outfit feel evenly weighted shows use of:",
  "Balance",["Chaos","Clutter","Noise"],"Design principles.")
H('180.d.16.B',4,"A bold belt that draws the eye to the waist applies:",
  "Emphasis",["Symmetry only","Disarray","Dullness"],"Design principles.")
H('180.d.16.C',3,"Choosing an A-line shape, a drapey fabric, and a pleated detail are decisions about:",
  "Silhouette, fabric, and design elements",["Weather","Shipping","Hiring"],"Silhouettes and fabrics.")
H('180.d.16.C',4,"A stiff fabric such as denim would suit which silhouette better than a drapey one?",
  "A structured jacket",["A flowing gown","A soft scarf","A silk blouse"],"Silhouettes and fabrics.")
H('180.d.16.D',3,"Using proportion, rhythm, and harmony to create a dress for a person is:",
  "Using design principles for the human form",["Cutting only","Cleaning only","Pricing only"],"Design principles.")
H('180.d.16.D',4,"Repeating a ruffle across the sleeve and hem creates:",
  "Rhythm",["Clash","Randomness","Imbalance"],"Design principles.")
H('180.d.16.E',3,"Drawing a clothing idea on a croquis figure with a pencil is:",
  "Fashion sketching",["Cutting","Pressing","Weighing"],"Fashion drawings.")
H('180.d.16.E',4,"A flat sketch shows a garment's:",
  "Front and back details laid out plainly",["Runway movement","Customer name","Shipping cost"],"Fashion drawings.")
H('180.d.16.F',3,"Using computer-aided design to draw patterns is a:",
  "Technology application in design",["Hand method only","Dye method","Sewing method"],"Technology in design.")
H('180.d.16.F',4,"Digital pattern software can speed up design by letting designers:",
  "Edit and resize patterns quickly",["Cut paper by hand","Redraw from scratch","Avoid revisions"],"Technology in design.")
H('180.d.17.A',3,"The sweep of a curved seam across a bodice is an example of the design element:",
  "Line",["Weather","Price","Season"],"Elements of design.")
H('180.d.17.A',4,"Choosing a bright red for a scarf to make it stand out uses:",
  "Color",["Texture only","Shape only","Form only"],"Elements of design.")
H('180.d.17.B',3,"A designer decides on a tapered silhouette and a stretch fabric for activewear. This is:",
  "Choosing silhouette and fabric",["Dyeing only","Cutting only","Pricing only"],"Silhouettes and fabrics.")
H('180.d.17.B',4,"Moisture-wicking fabric suits sportswear because it:",
  "Pulls sweat away from the skin",["Holds sweat","Blocks air","Stiffens movement"],"Silhouettes and fabrics.")
H('180.d.17.C',3,"Using shape, color, and texture to create a jacket that suits the wearer is applying:",
  "Design elements for the human form",["Thread counts","Shipping plans","Tax rules"],"Design elements.")
H('180.d.17.C',4,"A designer adds a textured trim to give a plain dress:",
  "Visual interest",["Wrinkles","Shrinkage","Stains"],"Design elements.")

H('179.d.7.B',5,"A heat lamp tips over during a client shoot and the cord sparks. After cutting power, the photographer should next:",
  "Keep everyone clear and report the incident",["Restart it to test it","Cover it with fabric","Continue the session"],"Emergency procedures.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_32.jsonl'))

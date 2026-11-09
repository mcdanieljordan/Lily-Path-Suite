import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('127.', 1103, own='cte_26.jsonl')
def H(code, d, q, right, wrong, e):
    return B.hand(code, d, q, right, wrong, e)

# ---------- 127.164 Animation (3D production practicum-style) ----------
H('164.d.4',3,"A student animation team imports sketches, edits sound, and exports video using computer programs. This shows that they:",
  "Apply technology applications to their work",["Avoid all software","Use only paper","Skip production"],"Technology applications in animation.")
H('164.d.4',4,"Which pairing shows correct use of an application for its job?",
  "Using a video editor to trim and join clips",["Using a spreadsheet to sculpt a character","Using a browser to record dialogue","Using a calculator to paint a background"],"Match the tool to the task.")
H('164.d.5',3,"Before opening an unknown email attachment sent to a studio computer, a student should:",
  "Check with the teacher or IT first",["Open it at once","Forward it to everyone","Turn off the antivirus"],"Cyber safety procedure.")
H('164.d.5',4,"Using a different strong password for each animation account mainly protects against:",
  "One breach exposing every account",["Slow renders","Low frame rates","Large file sizes"],"Password safety.")
H('164.d.8',3,"A student saves a rig as a template so it can be reused on new characters. This is an advanced technique for:",
  "Working more efficiently",["Wasting time","Erasing layers","Lowering quality"],"Technical efficiency.")
H('164.d.8',4,"Scripting a repeated task, such as renaming 200 frames, helps an animator by:",
  "Saving hours of manual work",["Creating more frames","Deleting the project","Lowering resolution"],"Advanced efficiency.")
H('164.d.1.A',3,"When a student proofreads a shot list for spelling and clear sentences, which subject skill are they using?",
  "English language arts",["Welding","Cooking","Gardening"],"ELA applied in animation.")
H('164.d.1.A',4,"Writing a short artist statement for an animated project requires:",
  "Clear writing and correct grammar",["Random notes","Only pictures","Only numbers"],"Writing skills.")
H('164.d.1.B',3,"An animated clip runs 8 seconds at 12 drawings per second. How many drawings are needed?",
  "96",["20","64","108"],"8 x 12 = 96.")
H('164.d.1.B',4,"A background is 4800 pixels wide and the screen shows 1200 pixels at a time. How many screens wide is the background?",
  "4",["3","6","40"],"4800 / 1200 = 4.")
H('164.d.2.A',3,"A student explains a storyboard to second graders using simple words and gestures. This is adapting language to the:",
  "Audience",["Hard drive","Frame rate","Render farm"],"Adapt language.")
H('164.d.2.A',4,"Describing a character's motivation to a teacher versus to a friend requires changing the:",
  "Tone and vocabulary for each listener",["Spelling of names","Frame size","Software version"],"Audience and situation.")
H('164.d.2.B',3,"Putting storyboard panels in numbered order before a pitch is a way to:",
  "Organize information",["Hide the story","Shorten the film","Lower the volume"],"Organize information.")
H('164.d.2.B',4,"A pitch that goes problem, characters, solution is organized by:",
  "Logical sequence",["Alphabet","Random order","Color"],"Organization.")
H('164.d.2.C',3,"A team member explains what a critique chart means in plain language. That is:",
  "Interpreting and communicating information",["Rendering a scene","Rigging a model","Capturing audio"],"Interpret information.")
H('164.d.2.C',4,"A graph shows viewers dropping off at the 20-second mark of a short. The team should:",
  "Review what happens at that point",["Ignore the graph","Delete the whole film","Add credits"],"Interpret data.")
H('164.d.2.D',3,"A class screening where students present finished shorts with slides is a:",
  "Formal presentation",["Casual chat","Sound check","Backup"],"Formal presentation.")
H('164.d.2.D',4,"Giving a quick two-minute progress update at your desk to a partner is a(n):",
  "Informal presentation",["Formal keynote","Awards show","Press release"],"Informal presentation.")
H('164.d.2.E',3,"During critique, active listening includes:",
  "Eye contact and taking notes",["Checking messages","Interrupting","Talking over others"],"Active listening.")
H('164.d.2.E',4,"After a peer gives feedback, the best way to show you listened is to:",
  "Restate the main points in your own words",["Change the subject","Argue every point","Walk away"],"Confirming understanding.")
H('164.d.2.F',3,"A classmate who speaks another language joins your animation team. A respectful action is to:",
  "Use clear words and visuals so they can contribute",["Exclude them","Talk faster","Ignore their ideas"],"Diverse individuals.")
H('164.d.2.F',4,"Hearing ideas from students of different backgrounds can improve an animation by:",
  "Adding more varied story and design choices",["Slowing the render","Shrinking the screen","Cutting the soundtrack"],"Value of diversity.")
H('164.d.2.G',3,"Public relations skills in a student studio include:",
  "Presenting the team's work politely to visitors",["Hiding the film","Arguing with guests","Staying silent"],"PR skills.")
H('164.d.2.G',4,"When a visitor asks a tough question about your short, a good PR response is to:",
  "Answer calmly and thank them for asking",["Get defensive","Ignore them","Leave"],"Professional communication.")
H('164.d.3.A',3,"Weighing the pros and cons of two color palettes before choosing one is:",
  "Critical thinking",["Guessing","Copying","Procrastinating"],"Critical thinking.")
H('164.d.3.A',4,"A group tests two camera moves and picks the one viewers understood better. This is decision making based on:",
  "Evidence",["Luck","Volume","Speed only"],"Group critical thinking.")
H('164.d.3.B',3,"Two teammates want different endings. A helpful interpersonal skill is:",
  "Listening and finding a compromise",["Refusing to talk","Insulting","Quitting"],"Interpersonal skills.")
H('164.d.3.B',4,"Using \"I\" statements such as \"I feel the scene drags\" helps a group because it:",
  "Keeps feedback respectful and focused",["Blames people","Ends discussion","Hides the problem"],"Group communication.")
H('164.d.6.A',3,"A team leader who sets a goal, lists steps, and checks progress is:",
  "Employing leadership skills",["Avoiding work","Working alone","Delaying"],"Leadership.")
H('164.d.6.A',4,"To lead a project well, the leader first needs to understand the team's:",
  "Needs, strengths, and resources",["Favorite snacks","Shoe sizes","Birth months"],"Analyzing needs.")
H('164.d.6.B',3,"Teamwork on a short film means each member:",
  "Does their part and helps others",["Works only for credit","Ignores deadlines","Hides mistakes"],"Teamwork.")
H('164.d.6.B',4,"Conflict management after a disagreement over design starts with:",
  "Calmly hearing each side",["Taking sides","Shouting","Ignoring it"],"Conflict management.")
H('164.d.6.C',3,"Effective working relationships are built by giving:",
  "Constructive feedback",["Gossip","Silence","Insults"],"Working relationships.")
H('164.d.6.C',4,"Constructive feedback on a rough animation should be:",
  "Specific and focused on improving the work",["Vague and harsh","Personal","Delayed for weeks"],"Constructive feedback.")
H('164.d.6.D',3,"Before a team meeting, a student prepares by writing:",
  "Goals and an agenda",["A grocery list","A joke book","A new password"],"Meeting preparation.")
H('164.d.6.D',4,"A meeting objective such as \"decide the title font today\" is useful because it is:",
  "Specific and measurable",["Vague","Endless","Hidden"],"Objectives.")
H('164.d.6.E',3,"A good meeting participant:",
  "Stays on topic and takes turns",["Interrupts often","Browses games","Leaves early"],"Meeting conduct.")
H('164.d.6.E',4,"The best way to end a meeting is to:",
  "Review decisions and assign tasks",["End abruptly","Forget notes","Add new topics"],"Meeting outcomes.")
H('164.d.6.F',3,"A student who teaches a younger classmate how to use a drawing tablet is:",
  "Mentoring",["Competing","Copying","Quitting"],"Mentoring.")
H('164.d.6.F',4,"Good mentors inspire others by being:",
  "Patient and encouraging",["Impatient","Critical of everything","Secretive"],"Mentoring.")
H('164.d.7.A',3,"Giving credit to every classmate who helped make a short is:",
  "Ethical conduct",["A mistake","Optional","Unfair"],"Ethical conduct.")
H('164.d.7.A',4,"Claiming a partner's character design as your own is:",
  "Dishonest",["Teamwork","Efficient","Allowed"],"Ethics.")
H('164.d.7.B',3,"Copyright law protects:",
  "Original creative works like drawings and songs",["Only buildings","Only ideas in your head","Nothing"],"Copyright.")
H('164.d.7.B',4,"Using a popular song in a school film shared online without permission may:",
  "Break copyright law",["Be encouraged","Be required","Be free of rules"],"Copyright application.")
H('164.d.7.C',3,"Respecting intellectual property means you:",
  "Ask permission and give credit",["Copy freely","Remove names","Resell others' art"],"Intellectual property.")
H('164.d.7.C',4,"A free image labeled \"for personal use only\" cannot be used in:",
  "A film you sell",["A private sketchbook","A class draft","A home display"],"License terms.")
H('164.d.7.D',3,"An acceptable use policy tells students how to:",
  "Use school technology responsibly",["Build robots","Cook lunch","Park cars"],"AUP.")
H('164.d.7.D',4,"Proper network etiquette includes:",
  "Respectful messages and no unauthorized downloads",["Sharing passwords","Streaming during class","Hiding browsing"],"Etiquette.")
H('164.d.9.A',3,"Using video chat to hold a review with a partner who is home sick shows how to:",
  "Operate a communication system",["Paint a cel","Mix clay","Weave"],"Communication systems.")
H('164.d.9.A',4,"Before a video review, the presenter should test the:",
  "Microphone and screen sharing",["Printer","Lights in the hall","Door lock"],"Preparing communication.")
H('164.d.9.B',3,"Choosing a close-up to show a character's face is a decision about:",
  "Framing",["Printing","Filing","Pricing"],"Production elements.")
H('164.d.9.B',4,"Placing the camera below a character to make them look powerful is a choice of:",
  "Angle",["Spelling","Budget","Storage"],"Camera angle.")
H('164.d.9.C',3,"A drawing that shows only the front, top, and side of an object as separate flat views is:",
  "Orthographic",["Perspective","Isometric","Abstract"],"Orthographic drawing.")
H('164.d.9.C',4,"An isometric drawing shows an object in:",
  "A single 3D-looking view with equal angles",["Three flat views","Two views","No views"],"Isometric drawing.")
H('164.d.9.D',3,"Maya, Blender, and Toon Boom are examples of:",
  "Commercial production applications",["Board games","Web fonts","Printers"],"Commercial applications.")
H('164.d.9.D',4,"Studios prefer software that many artists already know because it:",
  "Makes it easier to share and hand off work",["Costs more","Runs slower","Has fewer features"],"Commercial standards.")
H('164.d.10.A',3,"A ball that squashes on impact and stretches as it rises shows the principle of:",
  "Squash and stretch",["Rendering","Rigging","Mixing"],"Animation principles.")
H('164.d.10.A',4,"Making a jump bigger and more dramatic than real life is the principle of:",
  "Exaggeration",["Compression","Normalization","Dithering"],"Exaggeration.")
H('164.d.10.B',3,"A short loop of a character walking that repeats is a(n):",
  "Cycle",["Mask","Plug-in","Stylus"],"Cycles.")
H('164.d.10.B',4,"Stacking background, character, and effects in separate sheets in the timeline uses:",
  "Layers",["Mirrors","Magnets","Filters"],"Layers.")
H('164.d.11.A',3,"A thick, curved stroke drawn around a cartoon is an example of the design element of:",
  "Line",["Pitch","Tempo","Volume"],"Design elements.")
H('164.d.11.A',4,"A rough, bumpy look on a dragon's skin is created with the element of:",
  "Texture",["Beat","Echo","Tone"],"Texture.")
H('164.d.11.B',3,"Additive color theory is based on mixing:",
  "Colored light",["Paint pigments","Crayons","Inks"],"Additive color.")
H('164.d.11.B',4,"On a screen, equal red, green, and blue light together look:",
  "White",["Black","Brown","Purple"],"Additive mixing.")
H('164.d.11.C',3,"Anime and classic Saturday-morning cartoons differ most in their:",
  "Visual styles",["Hard drives","Plugs","Power cords"],"Compare styles.")
H('164.d.11.C',4,"Stop-motion and 2D digital animation differ in how frames are:",
  "Made",["Priced only","Named only","Hidden"],"Compare techniques.")
H('164.d.12.A',3,"Deciding if a short is for preschoolers or teens begins with analyzing the:",
  "Target audience",["Weather","Hard drive","Mouse"],"Audience analysis.")
H('164.d.12.A',4,"A short meant for young children should most likely have:",
  "Simple plot and bright colors",["Complex jargon","Dark horror","Long speeches"],"Needs and wants.")
H('164.d.12.B',3,"Cutting extra dialogue from a script so the story moves faster is:",
  "Editing",["Rigging","Rendering","Texturing"],"Editing scripts.")
H('164.d.12.B',4,"Dialogue in a script is written to reveal:",
  "Character and move the story",["Software bugs","Camera brands","File names"],"Script writing.")
H('164.d.12.C',3,"A storyboard shows:",
  "The shots planned in sketch form",["The finished soundtrack","The final render","The invoice"],"Storyboards.")
H('164.d.12.C',4,"Arrows drawn on a storyboard panel usually show:",
  "Movement of a character or camera",["Spelling errors","Budget limits","Lighting watts"],"Storyboard notation.")
H('164.d.12.D',3,"A common frame rate for film is:",
  "24 frames per second",["1 frame per second","240 frames per second","0.5 frames per second"],"Frame rate.")
H('164.d.12.D',4,"A short that will play on a widescreen TV and website would likely use an aspect ratio of:",
  "16:9",["1:20","50:1","9:50"],"Aspect ratio.")
H('164.d.13.A',3,"Choosing a warm palette for a cozy kitchen scene is a(n):",
  "Color design decision",["Rigging choice","Sound cue","Budget line"],"Color design.")
H('164.d.13.A',4,"Placing the hero in the left third of the frame uses:",
  "Compositional design",["Audio mixing","Version control","Keyframing"],"Composition.")
H('164.d.13.B',3,"Drawing front, side, and back views of a new character is called a:",
  "Character turnaround",["Render pass","Backup","Master mix"],"Character design.")
H('164.d.13.B',4,"A prop's design should match the story's:",
  "Setting and tone",["Hard drive","Mouse speed","File size"],"Props and environments.")
H('164.d.13.C',3,"Building a 3D character from simple shapes like spheres and cubes is:",
  "Modeling",["Scripting","Auditioning","Mixing"],"Modeling.")
H('164.d.13.C',4,"A model with too many unneeded polygons will most likely:",
  "Slow the computer down",["Render faster","Look flat","Lose its color"],"Modeling efficiency.")
H('164.d.13.D',3,"Placing lights to make a scene look like sunset is:",
  "Lighting a set",["Casting","Scoring","Editing audio"],"Lighting.")
H('164.d.13.D',4,"Animating a light so a lamp slowly dims shows lights can be:",
  "Animated",["Fixed forever","Deleted","Printed"],"Animated lighting.")
H('164.d.13.E',3,"A rig gives animators:",
  "Controls to pose a character",["A soundtrack","A script","A budget"],"Rigging.")
H('164.d.13.E',4,"The skeleton inside a rigged character is made of:",
  "Joints and bones",["Fonts","Cables","Speakers"],"Rig structure.")
H('164.d.13.F',3,"Rain, snow, and fire in an animation are often made with:",
  "Particle systems",["Pencil sketches only","Live actors only","Paper cutouts only"],"Particle systems.")
H('164.d.13.F',4,"A particle system's emitter controls how many particles:",
  "Are created and in which direction",["Are printed","Are sold","Are named"],"Particle controls.")
H('164.d.13.G',3,"Moving a character's pose from one key position to the next over time is:",
  "Animating",["Casting","Scoring","Mastering"],"Animating.")
H('164.d.13.G',4,"Animating a camera so it slowly moves toward a character is called a:",
  "Dolly or push-in",["Mute","Scrub","Backup"],"Camera animation.")
H('164.d.13.H',3,"Footsteps, door creaks, and splashes added to a scene are:",
  "Sound effects",["Storyboards","Rigs","Textures"],"Sound effects.")
H('164.d.13.H',4,"Music in a scene should match its:",
  "Mood",["File size","Monitor","Mouse"],"Music selection.")
H('164.d.13.I',3,"The step that turns a 3D scene into final images is:",
  "Rendering",["Sketching","Casting","Wiring"],"Render.")
H('164.d.13.I',4,"Test-rendering a single frame before rendering the whole scene helps to:",
  "Catch problems early",["Waste time","Hide errors","Erase layers"],"Render testing.")
H('164.d.14.A',3,"Arranging clips in the best order and trimming them is:",
  "Editing",["Modeling","Rigging","Sculpting"],"Editing.")
H('164.d.14.A',4,"A cut that happens on a character's action usually feels:",
  "Smooth",["Jarring","Silent","Frozen"],"Edit flow.")
H('164.d.14.B',3,"A title card and end credits are added during:",
  "Finishing the film",["Brainstorming","Casting","Pitching"],"Titles and credits.")
H('164.d.14.B',4,"Credits should list:",
  "Everyone who contributed",["Only the editor","Only the director","No one"],"Credits.")
H('164.d.14.C',3,"Adding a glow or lens flare after animation is finished is a:",
  "Visual effect",["Script change","Rig control","Storyboard note"],"Visual effects.")
H('164.d.14.C',4,"Color correction makes sure shots:",
  "Match in color and brightness",["Have no sound","Run backward","Are shorter"],"Processing.")
H('164.d.14.D',3,"Adding echo to a voice in a cave scene is an:",
  "Audio effect",["Camera move","Rig control","Storyboard"],"Audio effects.")
H('164.d.14.D',4,"Lowering music volume under dialogue so words are clear is part of:",
  "Audio mixing",["Modeling","Lighting","Casting"],"Audio processing.")
H('164.d.14.E',3,"Exporting the finished film as an MP4 file is part of:",
  "Producing the output",["Writing the script","Modeling props","Casting voices"],"Produce output.")
H('164.d.14.E',4,"Before sharing the final file, a team should:",
  "Watch it all the way through for errors",["Skip checking","Delete the project","Lower the audio to zero"],"Quality control.")

# ---------- 127.165 Audio/Video Production I ----------
H('165.d.1.A',3,"Writing a clear news script with correct grammar and punctuation shows use of:",
  "English language arts skills",["Welding skills","Cooking skills","Gardening skills"],"ELA in A/V.")
H('165.d.1.A',4,"Reading a script aloud smoothly and with correct pronunciation applies:",
  "Language arts and speaking skills",["Only art skills","Only gym skills","Only math skills"],"ELA in A/V.")
H('165.d.1.B',3,"A freelancer charges $40 per hour and works 6 hours. What is the invoice total?",
  "$240",["$46","$200","$264"],"40 x 6 = 240.")
H('165.d.1.B',4,"A video lasts 3 minutes 30 seconds. How many seconds is that?",
  "210",["330","90","180"],"3 x 60 + 30 = 210.")
H('165.d.2.A',3,"A reporter explains a story to young viewers using simple words. This adapts language to the:",
  "Audience",["Camera brand","Cable length","Battery"],"Adapt language.")
H('165.d.2.A',4,"A producer uses technical terms with the crew but plain words with a client. This is adapting to the:",
  "Situation and audience",["Weather","Time zone only","Monitor size"],"Adapt language to context.")
H('165.d.2.B',3,"Arranging a shoot schedule in time order is a way to:",
  "Organize information",["Delete information","Hide information","Print information"],"Organize information.")
H('165.d.2.B',4,"A call sheet lists:",
  "Who, where, and when for a shoot",["Only the lunch menu","Only camera brands","Only fonts"],"Production documents.")
H('165.d.2.C',3,"A crew member reading a light meter and telling the director the result is:",
  "Interpreting and communicating data",["Editing sound","Writing credits","Casting actors"],"Interpret observations.")
H('165.d.2.C',4,"Reporting that audio peaked above the safe level and needs lowering communicates:",
  "A technical observation",["A joke","A rumor","An opinion on food"],"Communicating data.")
H('165.d.2.D',3,"An on-air presentation to a large audience of viewers is a(n):",
  "Formal presentation",["Informal chat","Private note","Rehearsal only"],"Formal presentation.")
H('165.d.2.D',4,"A quick huddle where the director gives the crew a two-minute update is a(n):",
  "Informal presentation",["Formal speech","Awards show","Press release"],"Informal presentation.")
H('165.d.2.E',3,"A boom operator who listens closely to the director's instructions is:",
  "Applying active listening",["Ignoring the director","Texting","Arguing"],"Active listening.")
H('165.d.2.E',4,"Asking a question when you did not understand a cue shows:",
  "Active listening",["Poor behavior","Weakness","Wasted time"],"Active listening.")
H('165.d.2.F',3,"Interviewing someone whose first language is different from yours requires:",
  "Patience and respect",["Talking louder","Interrupting","Ignoring them"],"Diverse individuals.")
H('165.d.2.F',4,"Including voices from many communities in a documentary helps:",
  "Give a fuller picture of the topic",["Narrow the story","Lower the quality","Shorten it"],"Diversity.")
H('165.d.2.G',3,"Public relations in a student TV station includes:",
  "Representing the station professionally",["Spreading rumors","Being rude","Ignoring viewers"],"PR skills.")
H('165.d.2.G',4,"A station posts a polite correction when it airs a mistake. This builds:",
  "Public trust",["Confusion","Debt","Static"],"Public relations.")
H('165.d.3.A',3,"A crew compares two locations for noise and lighting before choosing. This is:",
  "Critical thinking",["Guessing","Luck","Copying"],"Critical thinking.")
H('165.d.3.A',4,"Choosing a microphone after weighing the room, distance, and budget is:",
  "Informed decision making",["Random choice","Tradition only","Impulse"],"Critical thinking.")
H('165.d.3.B',3,"Two producers disagree about a cut. A good interpersonal skill is:",
  "Listening and compromising",["Shouting","Quitting","Blaming"],"Interpersonal skills.")
H('165.d.3.B',4,"Group problem solving works best when everyone:",
  "Shares ideas respectfully",["Stays silent","Argues loudly","Works alone"],"Group problem solving.")
H('165.d.4.A',3,"A producer emails a script, posts a clip, and searches for reference footage. These are:",
  "Technology applications",["Hand tools","Paper maps","Print ads"],"Technology applications.")
H('165.d.4.A',4,"Using a word processor to format a screenplay shows use of:",
  "Writing software",["Audio mixer","Light kit","Boom pole"],"Technology applications.")
H('165.d.4.B',3,"Naming files clearly and keeping them in labeled folders is:",
  "File management",["Lighting","Casting","Mixing"],"File management.")
H('165.d.4.B',4,"Backing up raw footage to a second drive protects against:",
  "Losing the footage if a drive fails",["Slow internet","Long scripts","Bright lights"],"Backup.")
H('165.d.5.A',3,"Early radio and silent film helped form the history of:",
  "Audio and video production",["Auto repair","Farming","Shipbuilding"],"History of A/V.")
H('165.d.5.A',4,"The move from film to digital video made production:",
  "Faster and cheaper for many creators",["Impossible","Slower for everyone","Black and white only"],"Evolution of A/V.")
H('165.d.5.B',3,"Streaming platforms and short-form video are current trends that give creators:",
  "New ways to reach audiences",["No audience","Fewer options","Only film options"],"Current trends.")
H('165.d.5.B',4,"A producer tracks industry trends mainly to:",
  "Make content audiences want to watch",["Ignore viewers","Raise costs","Avoid change"],"Analyze trends.")
H('165.d.6.A',3,"Taping down cables on a set helps prevent:",
  "Trips and falls",["Echo","Glare","Wind"],"Safety rules.")
H('165.d.6.A',4,"Before climbing a ladder to hang a light, a student should make sure:",
  "A partner steadies it and the area is clear",["Nobody is nearby","The light is hot","The ladder is wet"],"Workplace safety.")
H('165.d.6.B',3,"If the studio fire alarm sounds, the crew should:",
  "Leave by the posted exit route",["Keep filming","Hide in a closet","Plug in more lights"],"Emergency procedures.")
H('165.d.6.B',4,"An emergency plan posted in a studio shows:",
  "Exits and meeting spots",["Prices","Schedules only","Fonts"],"Emergency procedures.")
H('165.d.6.C',3,"Long hours sitting at an edit station can lead to problems like:",
  "Eye strain and back pain",["Free time","Better sleep always","Faster computers"],"Safety-related problems.")
H('165.d.6.C',4,"Taking short breaks and adjusting the chair helps reduce:",
  "Repetitive strain and fatigue",["Frame rate","Screen size","File size"],"Ergonomics.")
H('165.d.7.A',3,"A student who steps up to organize a crew and share tasks is showing:",
  "Leadership",["Avoidance","Delay","Isolation"],"Leadership.")
H('165.d.7.A',4,"A strong leader on set makes sure the team has:",
  "Clear goals and support",["No direction","Extra drama","Less time"],"Leadership.")
H('165.d.7.B',3,"A crew works well together when members:",
  "Cooperate and solve disagreements calmly",["Compete","Hide tasks","Blame each other"],"Teamwork.")
H('165.d.7.B',4,"When two crew members disagree about a shot, a good first step is to:",
  "Listen to both views",["Ignore it","Pick randomly","Cancel the shoot"],"Conflict management.")
H('165.d.7.C',3,"At a pre-production meeting, a participant should:",
  "Contribute and listen respectfully",["Interrupt","Nap","Stay on a phone"],"Meetings.")
H('165.d.7.C',4,"Taking meeting notes helps the team remember:",
  "Decisions and assignments",["Jokes","Snacks","Seat choices"],"Meetings.")
H('165.d.7.D',3,"A senior student shows a newcomer how to set up a tripod. That is:",
  "Mentoring",["Competing","Copying","Delaying"],"Mentoring.")
H('165.d.7.D',4,"Being mentored helps a beginner mostly by:",
  "Speeding up learning",["Slowing progress","Hiding mistakes","Lowering goals"],"Mentoring.")
H('165.d.8.A',3,"Getting permission before filming a person's private space is:",
  "Ethical",["Unnecessary","Rude","Wasteful"],"Ethical interaction.")
H('165.d.8.A',4,"Ethical conduct when interviewing a subject includes:",
  "Not twisting their words",["Editing to mislead","Hiding the camera","Skipping consent"],"Ethics.")
H('165.d.8.B',3,"Using a very short clip for a classroom critique may fall under:",
  "Fair use",["Free theft","Public domain","Never allowed"],"Fair use.")
H('165.d.8.B',4,"To use a commercial song in a video you sell, you generally must:",
  "Obtain a license",["Just credit the singer","Remove the title","Add a watermark"],"Acquiring rights.")
H('165.d.8.C',3,"Respecting intellectual property means:",
  "Crediting and licensing others' work",["Copying freely","Cutting credits","Claiming it all"],"Intellectual property.")
H('165.d.8.C',4,"Royalty-free music means:",
  "No repeat royalty payments after the license is obtained",["Always free","Unprotected by law","Public domain"],"Licensing.")
H('165.d.8.D',3,"Misleading edits in news video can harm an industry's:",
  "Credibility",["Battery","Memory","Cables"],"Ethical impact.")
H('165.d.8.D',4,"The A/V industry has an ethical duty to avoid content that:",
  "Spreads false or harmful claims",["Is colorful","Has music","Uses graphics"],"Ethical impact.")
H('165.d.8.E',3,"Checking a video's facts against reliable sources evaluates its:",
  "Accuracy",["Volume","Length","Frame rate"],"Accuracy.")
H('165.d.8.E',4,"A video with a clear source for every claim is more likely to be:",
  "Valid and trustworthy",["Boring","Blurry","Silent"],"Validity.")
H('165.d.9.A',3,"A class that makes a video about local health or the environment is examining:",
  "A real-world issue",["A fairy tale","A game only","A prank"],"Real-world issues.")
H('165.d.9.A',4,"Choosing a topic like school lunch waste lets students connect video work to:",
  "Their community",["Nothing","Only a fantasy","A random list"],"Real-world issues.")
H('165.d.9.B',3,"Making a public service announcement for people outside the classroom creates a product for:",
  "A wider audience",["Only the teacher","Only yourself","Nobody"],"Unique products.")
H('165.d.9.B',4,"Posting a student documentary on a school channel makes it available to:",
  "Audiences beyond the classroom",["Only classmates","Nobody","The camera"],"Audiences.")
H('165.d.10.A',3,"A demo reel and resume together make up part of a:",
  "Career portfolio",["Shopping list","Playlist","Calendar"],"Career portfolio.")
H('165.d.10.A',4,"A strong portfolio piece shows:",
  "Skills and best finished work",["Everything ever made","Blank files","Unfinished drafts only"],"Portfolio.")
H('165.d.10.B',3,"Comparing two internships by pay, hours, and learning opportunities is:",
  "Evaluating employment options",["Guessing","Quitting","Scheduling"],"Compare opportunities.")
H('165.d.10.B',4,"An internship with no pay but strong mentoring could be worthwhile if it:",
  "Builds skills and connections",["Costs money only","Offers no work","Repeats tasks"],"Evaluate opportunities.")
H('165.d.10.C',3,"Meeting working professionals at a career fair is:",
  "Professional networking",["Wasting time","Cheating","Gaming"],"Networking.")
H('165.d.10.C',4,"Following up a networking contact with a thank-you note helps:",
  "Keep the relationship going",["End contact","Create errors","Avoid jobs"],"Networking.")
H('165.d.10.D',3,"A producer who starts their own video business is practicing:",
  "Entrepreneurship",["Retirement","Observation","Hobbyism only"],"Entrepreneurship.")
H('165.d.10.D',4,"An independent video business owner must handle clients and also:",
  "Billing and marketing",["Only editing","Only filming","Only sleeping"],"Business tasks.")
H('165.d.11.A',3,"Making a shooting schedule with deadlines applies:",
  "Planning and time management",["Guessing","Luck","Delay"],"Time management.")
H('165.d.11.A',4,"Working backward from a premiere date to set each task's deadline is:",
  "Backward planning",["Avoidance","Rewinding","Multitasking"],"Planning.")
H('165.d.11.B',3,"Using a shared calendar app for a crew helps:",
  "Everyone see the plan",["Hide the schedule","Lose time","Add stress"],"Productivity technology.")
H('165.d.11.B',4,"Cloud storage lets a crew:",
  "Access project files from anywhere",["Print footage","Mute cameras","Hide scripts"],"Technology for productivity.")
H('165.d.12.A',3,"The audio, video, and film industry includes jobs in:",
  "Radio, television, and movies",["Farming","Mining","Fishing"],"Industry overview.")
H('165.d.12.A',4,"A film's director, editor, and sound mixer are all part of the:",
  "Production team",["Audience","Tax office","Fan club"],"Industry roles.")
H('165.d.12.B',3,"The earliest moving pictures were shown with:",
  "Mechanical projectors and silent film",["Smartphones","Streaming apps","Virtual reality"],"Beginnings of film.")
H('165.d.12.B',4,"Sound was added to commercial films in the:",
  "Late 1920s",["1800s","2000s","1500s"],"Evolution of film.")
H('165.d.12.C',3,"Smartphones with high-quality cameras have changed the industry by letting:",
  "More people create video",["Fewer people record","No one share","Cameras vanish"],"Changing technology.")
H('165.d.12.C',4,"Streaming services changed how audiences:",
  "Watch movies and shows",["Breathe","Sleep","Walk"],"Technology impact.")
H('165.d.12.D',3,"In video, a \"take\" is:",
  "One recorded attempt of a shot",["A type of cable","A script","A lens"],"Terminology.")
H('165.d.12.D',4,"A \"wrap\" call means the crew is:",
  "Finished with filming for the day or project",["Starting over","Setting lights","Casting"],"Terminology.")
H('165.d.12.E',3,"WAV and MP3 are examples of:",
  "Audio file formats",["Camera lenses","Light stands","Cables"],"Audio formats.")
H('165.d.12.E',4,"Tapeless recording stores audio on:",
  "Digital media like memory cards",["Cassette tape","Vinyl","Film"],"Tapeless.")
H('165.d.12.F',3,"An audio script for a radio ad must be written to be:",
  "Heard and understood by ear",["Seen only","Printed only","Silent"],"Audio script.")
H('165.d.12.F',4,"A radio script should avoid:",
  "Long sentences that are hard to say",["Short phrases","Clear timing","Cue notes"],"Audio script.")
H('165.d.12.G',3,"A slow, soft piano piece in a scene tends to create a feeling that is:",
  "Calm or sad",["Excited","Angry","Silly"],"Music and emotion.")
H('165.d.12.G',4,"Fast, loud drums behind a chase scene increase:",
  "Tension and excitement",["Sleepiness","Calm","Silence"],"Music and emotional impact.")
H('165.d.12.H',3,"A microphone with a cardioid pickup pattern picks up sound mostly from the:",
  "Front",["Back only","Sides only","All directions equally"],"Microphones.")
H('165.d.12.H',4,"For recording one speaker in a noisy room, the best choice is a:",
  "Directional microphone close to the speaker",["Distant omnidirectional mic","No microphone","Speaker phone"],"Microphone choice.")
H('165.d.12.I',3,"A video script often includes:",
  "Dialogue and descriptions of action",["Only jokes","Only prices","Only maps"],"Video scripts.")
H('165.d.12.I',4,"A video script's scene heading tells the crew:",
  "Where and when the scene happens",["Who pays","Which camera brand","Lunch time"],"Script elements.")
H('165.d.12.J',3,"Writing a script for a one-minute video requires:",
  "Concise, focused scenes",["Endless scenes","No structure","Only titles"],"Writing a video script.")
H('165.d.12.J',4,"A script for a short ad is built around a:",
  "Clear message for viewers",["Hidden plot","Random jokes","Blank page"],"Script writing.")
H('165.d.12.K',3,"MP4 and MOV are formats for:",
  "Video files",["Audio cables","Microphones","Tripods"],"Video formats.")
H('165.d.12.K',4,"Tapeless video cameras record to:",
  "SD cards or internal drives",["Cassettes","Film reels","Paper"],"Tapeless video.")
H('165.d.12.L',3,"HDMI and SDI are types of:",
  "Video cables and connectors",["Microphones","Lights","Scripts"],"Cables and connectors.")
H('165.d.12.L',4,"An XLR cable is most commonly used to connect:",
  "A professional microphone to a mixer",["A TV to a lamp","A mouse to a laptop","A phone to a charger"],"Connectors.")
H('165.d.12.M',3,"A signal that uses continuous waves of varying voltage is:",
  "Analog",["Digital","Binary","Pixelated"],"Analog vs digital.")
H('165.d.12.M',4,"A format that stores audio and video as ones and zeros is:",
  "Digital",["Analog","Acoustic","Mechanical"],"Analog vs digital.")
H('165.d.12.N',3,"Placing the subject off center along a grid line uses the:",
  "Rule of thirds",["Rule of ones","Rule of zero","Rule of tens"],"Composition.")
H('165.d.12.N',4,"A long shot, medium shot, and close-up are examples of:",
  "Shot sizes",["Cable types","Sound modes","Editing speeds"],"Videography.")
H('165.d.12.O',3,"Premiere, Final Cut, and DaVinci Resolve are:",
  "Video editing platforms",["Cameras","Microphones","Light kits"],"Editing platforms.")
H('165.d.12.O',4,"Moving clips on a timeline to change their order is done in:",
  "Nonlinear editing software",["A calculator","A printer","A thermostat"],"Editing basics.")
H('165.d.12.P',3,"High definition video has:",
  "More pixels than standard definition",["Fewer pixels","No pixels","Only sound"],"Digital platforms.")
H('165.d.12.P',4,"A standard definition image is generally:",
  "Lower resolution than HD",["Higher than HD","Same as 4K","Invisible"],"SD vs HD.")
H('165.d.13.A',3,"Setting a timeline for a project and tracking progress is:",
  "Project management",["Daydreaming","Gaming","Waiting"],"Procedures.")
H('165.d.13.A',4,"Watching audience analytics helps a producer:",
  "Evaluate what content works",["Avoid feedback","Lower quality","Skip planning"],"Evaluate procedures.")
H('165.d.13.B',3,"A student who changes the edit after a teacher's suggestion is:",
  "Responding to advice",["Ignoring feedback","Quitting","Copying"],"Responding to advice.")
H('165.d.13.B',4,"Professionals respond to critique by:",
  "Considering it and improving the work",["Rejecting all notes","Arguing","Hiding the film"],"Feedback.")
H('165.d.13.C',3,"A tech spec sheet for a shoot lists items like:",
  "Frame rate, resolution, and audio format",["Menu items","Parking spots","Trivia"],"Technology specifications.")
H('165.d.13.C',4,"Technology specifications make sure the team:",
  "Uses compatible settings",["Uses random settings","Skips settings","Hides files"],"Specifications.")
H('165.d.13.D',3,"Checking each shot against a quality checklist is:",
  "Monitoring quality",["Ignoring quality","Wasting time","Hiding errors"],"Quality control.")
H('165.d.13.D',4,"Established criteria for a news segment might include:",
  "Clear audio and accurate facts",["Longest length","Most effects","Loudest music"],"Quality criteria.")
H('165.d.13.E',3,"Listing the props, costumes, and locations a script needs identifies:",
  "Resources for production",["Menu items","Shoe sizes","Passwords"],"Resources.")
H('165.d.13.E',4,"A completed script is needed before a crew can:",
  "Plan the shoot",["Retire","Eat","Edit credits"],"Script and resources.")
H('165.d.13.F',3,"A budget for a shoot includes costs for cast, crew, equipment, and:",
  "Locations",["Birthdays","Sports","Holidays"],"Budget.")
H('165.d.13.F',4,"Renting a camera instead of buying one may be a budget choice that:",
  "Saves money on a short project",["Wastes money always","Prevents filming","Raises taxes"],"Budgeting.")
H('165.d.13.G',3,"A storyboard helps a team:",
  "Plan shots before filming",["Replace the script","Delete footage","Change cables"],"Storyboards.")
H('165.d.13.G',4,"Reviewing the script and storyboard together helps catch:",
  "Gaps or confusing scenes",["Weather","Dust","Cables"],"Script and storyboard process.")
H('165.d.13.H',3,"The person who operates the camera is the:",
  "Camera operator",["Editor","Writer","Caterer"],"Team roles.")
H('165.d.13.H',4,"The director's main job is to:",
  "Guide the creative vision and performances",["Sell tickets","Repair trucks","Print scripts"],"Team roles.")
H('165.d.13.I',3,"For a scene with ten extras and two locations, the crew needs to plan:",
  "Cast, crew, and location needs",["Only camera lenses","Only music","Only posters"],"Requirements.")
H('165.d.13.I',4,"Scouting a location ahead of time checks for:",
  "Power outlets, noise, and lighting",["Gift shops","Prices of food","Birthdays"],"Location requirements.")
H('165.d.13.J',3,"An audition is when actors:",
  "Perform to try for a role",["Edit film","Mix audio","Hang lights"],"Casting.")
H('165.d.13.J',4,"A casting director chooses actors who best fit the:",
  "Characters in the script",["Camera model","Parking lot","Budget spreadsheet"],"Casting process.")
H('165.d.14.A',3,"Collecting audience surveys after a screening helps evaluate:",
  "How well the product worked",["The weather","Battery life","Cable length"],"Evaluation.")
H('165.d.14.A',4,"Reviewing a rough cut with a peer using a rubric is a way to:",
  "Evaluate work in progress",["Hide errors","Avoid edits","Delete files"],"Evaluation.")
H('165.d.14.B',3,"Choosing between social media, posters, and a screening to share a film is:",
  "Researching promotion methods",["Filming","Editing audio","Casting"],"Promotion.")
H('165.d.14.B',4,"The best promotion method depends on the product and the:",
  "Target audience",["Camera brand","Cable color","Studio paint"],"Promotion.")
H('164.d.7.B',5,"A student wants to redraw a studio's famous cartoon mascot for a school poster. Copyright law means the student should:",
  "Get permission or create an original character",["Copy it and claim it","Remove the logo only","Post it as theirs"],"Applying copyright.")
H('165.d.8.C',5,"A student films a school event and wants to include a pop song. Respecting the song's owner means:",
  "Getting a license or using music cleared for reuse",["Using it without asking","Hiding the title","Muting the credits"],"Respect for IP.")
H('165.d.11.B',5,"A crew in two cities needs the same raw footage. Which technology use best boosts productivity?",
  "Sharing files through cloud storage",["Mailing hard drives weekly","Retyping the footage","Printing frames"],"Technology to enhance productivity.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_26.jsonl'))

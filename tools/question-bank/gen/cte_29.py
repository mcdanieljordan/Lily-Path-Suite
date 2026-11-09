import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('127.', 1106, own='cte_29.jsonl')
def H(code, d, q, right, wrong, e):
    return B.hand(code, d, q, right, wrong, e)

# ---------- 127.170 Audio Production II ----------
H('170.d.1.A',3,"A podcast producer proofreads show notes before publishing them. This applies:",
  "English language arts skills to audio work",["Plumbing skills","Welding skills","Culinary skills"],"ELA in audio.")
H('170.d.1.A',4,"Writing a clear client email that states the session date, rate, and deliverables shows strong:",
  "Written communication",["Mixing speed","Mic placement","Cable wrapping"],"ELA.")
H('170.d.1.B',3,"An engineer bills $90 per hour for 7 hours of mixing. What is the invoice amount?",
  "$630",["$97","$560","$700"],"90 x 7 = 630.")
H('170.d.1.B',4,"A session runs from 1:15 p.m. to 6:45 p.m. How many hours long is it?",
  "5.5 hours",["4.5 hours","6 hours","5 hours"],"5 hours 30 minutes = 5.5 hours.")
H('170.d.2.A',3,"Describing compression to a new singer without technical terms is adjusting language to the:",
  "Listener's level of experience",["Color of the walls","Brand of the mic","Length of the cable"],"Adapt language.")
H('170.d.2.A',4,"An email to a radio station manager is more formal in structure and style than a text to a bandmate because of the:",
  "Audience and situation",["Font size","Battery life","Screen color"],"Adapt language.")
H('170.d.2.B',3,"Sorting recorded takes into folders for vocals, guitars, and drums is:",
  "Organizing information",["Over-compressing","Panning","Clipping"],"Organize information.")
H('170.d.2.B',4,"Before presenting a mix plan to a client, a producer arranges the points in:",
  "A logical order",["Random order","Reverse alphabetical order only","No order"],"Organize.")
H('170.d.2.C',3,"An engineer reads a spectrum analyzer and tells the artist the vocal has too much low-end rumble. This is:",
  "Interpreting and communicating data",["Booking a tour","Wiring a lamp","Painting a wall"],"Interpret information.")
H('170.d.2.C',4,"A loudness meter reads well above the streaming target. A clear report to the client is:",
  "The mix is louder than the platform target and needs adjusting",["The mix is perfect","The meter is decorative","Loudness does not matter"],"Communicate observations.")
H('170.d.2.D',3,"Walking a label executive through a finished album mix in a scheduled meeting is a:",
  "Formal presentation",["Casual hallway chat","Sound check joke","Break time"],"Formal presentation.")
H('170.d.2.D',4,"Telling the band at the console what changed in the last take is a(n):",
  "Informal presentation",["Keynote address","Awards speech","Press release"],"Informal presentation.")
H('170.d.2.E',3,"An engineer pauses, nods, and asks a follow-up question while a producer describes a vision. This is:",
  "Active listening",["Distracted listening","Ignoring","Interrupting"],"Active listening.")
H('170.d.2.E',4,"Restating a client's notes in your own words before editing helps ensure:",
  "You understood the request",["The client leaves","The notes are ignored","The deadline passes"],"Active listening.")
H('170.d.2.F',3,"Recording a podcast guest who speaks with a strong regional accent calls for:",
  "Patience and respect",["Mockery","Correcting every word","Cutting them off"],"Diverse individuals.")
H('170.d.2.F',4,"A team that includes musicians from many backgrounds is likely to produce:",
  "A wider range of creative ideas",["Fewer ideas","Identical sounds","More conflict only"],"Diversity.")
H('170.d.2.G',3,"Sending a thank-you note and a prompt revised mix to a client builds the studio's:",
  "Public relations and reputation",["Noise floor","Latency","Gain structure"],"PR skills.")
H('170.d.2.G',4,"A studio gets a complaint about a late delivery. A strong public relations response is to:",
  "Apologize, explain, and offer a firm new date",["Blame the client","Ignore the message","Delete the project"],"PR.")
H('170.d.3.A',3,"A producer tests three vocal chains and keeps the one that sounds best in the mix. This is:",
  "Critical thinking",["Guessing","Flipping a coin","Copying a rival"],"Critical thinking.")
H('170.d.3.A',4,"A group evaluating two mastering quotes compares price, turnaround, and past work before deciding. This is:",
  "Critical thinking as a team",["Impulse buying","Random choice","Avoidance"],"Critical thinking in groups.")
H('170.d.3.B',3,"Two engineers disagree on how much reverb a vocal needs. A good group solution is to:",
  "A/B both versions and listen together",["Argue louder","Walk away","Let one person overrule without listening"],"Interpersonal skills.")
H('170.d.3.B',4,"An effective interpersonal approach to a team disagreement about the schedule is to:",
  "Listen, compare needs, and reach a compromise",["Pick sides","Stay silent","Assign blame"],"Group problem solving.")
H('170.d.4.A',3,"Posting a behind-the-scenes clip to social media to promote a studio is:",
  "A technology application for marketing",["A hand tool","A safety rule","A cable"],"Technology applications.")
H('170.d.4.A',4,"Using a word processor to prepare a session contract and email to send it is an example of:",
  "Using writing and communication software",["Soldering","Mixing in analog","Tape editing"],"Technology applications.")
H('170.d.4.B',3,"Naming files with a clear pattern such as project, date, and version is:",
  "File management",["Compression","Mastering","Equalization"],"File management.")
H('170.d.4.B',4,"Keeping client contacts, notes, and deadlines in one secure system is:",
  "Personal information management",["Wasting memory","Hiding data","Duplicating files"],"Information management.")
H('170.d.5.A',3,"Moving from phonograph records to magnetic tape to digital audio workstations shows the:",
  "Evolution of the audio production industry",["End of sound","Birth of silent film","Decline of music"],"History of audio.")
H('170.d.5.A',4,"The introduction of the compact disc in the 1980s moved consumers toward:",
  "Digital music formats",["Wax cylinders","Telegraph signals","Silent media"],"History of audio.")
H('170.d.5.B',3,"The rise of podcasts and streaming playlists is a current trend that:",
  "Creates demand for new audio content",["Eliminates audio jobs","Ends recording","Bans music"],"Current trends.")
H('170.d.5.B',4,"A producer analyzing trends notices more listeners using earbuds on phones. A smart response is to:",
  "Check mixes on small consumer devices",["Ignore small speakers","Mix only for large rooms","Remove all bass"],"Analyze trends.")
H('170.d.6.A',3,"Using a lift technique or a helper to move a heavy speaker cabinet is:",
  "Following workplace safety rules",["Optional","Slowing work down","A style choice"],"Safety rules.")
H('170.d.6.A',4,"Safe studio cable management means:",
  "Routing cords away from walkways",["Stretching cords across doorways","Stacking cords near water","Leaving cables tangled"],"Safety regulations.")
H('170.d.6.B',3,"During a power outage in the studio, the engineer should first:",
  "Move calmly to safety and follow emergency steps",["Keep recording","Open every equipment case","Run toward the stage"],"Emergency procedures.")
H('170.d.6.B',4,"A fire extinguisher in the control room should be:",
  "Clearly marked and easy to reach",["Hidden behind gear","Removed","Locked away"],"Emergency procedures.")
H('170.d.7.A',3,"A senior student who assigns roles for a recording day and keeps the group focused is showing:",
  "Leadership skills",["Disorganization","Avoidance","Indifference"],"Leadership.")
H('170.d.7.A',4,"A strong leader on a project responds to a mistake by:",
  "Taking responsibility and fixing the problem",["Blaming a teammate","Hiding it","Quitting"],"Leadership.")
H('170.d.7.B',3,"Sharing credit for a finished mix with the whole team shows:",
  "Teamwork",["Selfishness","Rivalry","Isolation"],"Teamwork.")
H('170.d.7.B',4,"A good first step to manage a conflict between two crew members is to:",
  "Let each person explain their side",["Ignore it","Take sides","Raise your voice"],"Conflict management.")
H('170.d.7.C',3,"In a planning meeting, a team member helps most by:",
  "Staying on topic and offering ideas",["Texting","Leaving early","Interrupting"],"Meetings.")
H('170.d.7.C',4,"Sending meeting minutes afterward ensures that the team:",
  "Remembers its decisions and next tasks",["Forgets tasks","Doubles work","Misses deadlines"],"Meetings.")
H('170.d.7.D',3,"An alumnus who volunteers to review a student's demo reel is:",
  "Mentoring",["Delaying","Competing","Ignoring"],"Mentoring.")
H('170.d.7.D',4,"Taking part in a mentoring program helps a student by:",
  "Providing guidance on skills and career steps",["Limiting contacts","Blocking feedback","Reducing options"],"Mentoring.")
H('170.d.8.A',3,"Telling a client honestly that a file is corrupted instead of hiding it is:",
  "Ethical conduct",["A technical fault","Poor planning","An accident"],"Ethical conduct.")
H('170.d.8.A',4,"Respecting a talent's privacy by not sharing their unreleased recordings is an example of:",
  "Ethical professional behavior",["Optional courtesy","Poor mixing","Marketing"],"Ethical conduct.")
H('170.d.8.B',3,"Paying for a sample pack license instead of copying a competitor's samples shows:",
  "Respect for intellectual property",["Carelessness","Disregard for creators","Wastefulness"],"IP respect.")
H('170.d.8.B',4,"Crediting a session musician in the liner notes shows respect for their:",
  "Creative contribution",["Pay rate only","Equipment","Travel route"],"IP respect.")
H('170.d.8.C',3,"Audio producers can shape public opinion because the work they release influences:",
  "What people hear and believe",["The weather","Soil quality","Road signs"],"Ethical impact.")
H('170.d.8.C',4,"Using audio editing to make a political figure appear to say something they never said raises:",
  "A serious ethical problem",["No concern","A technical bonus","A style choice"],"Ethical impact.")
H('170.d.8.D',3,"Copyright protects an original recording from being:",
  "Copied or sold without permission",["Heard by anyone","Recorded at all","Talked about"],"Copyright.")
H('170.d.8.D',4,"Using a short audio clip for a classroom lesson that discusses it is the type of use considered under:",
  "Fair use",["Free distribution","Piracy","Resale rights"],"Fair use.")
H('170.d.8.E',3,"Radio stations in the United States follow broadcast rules set by the:",
  "Federal Communications Commission",["Department of Agriculture","National Park Service","Postal Inspection Service"],"Regulations.")
H('170.d.8.E',4,"Broadcasting indecent content at times prohibited by regulators can lead to:",
  "Fines for the station",["Free equipment","Bonus awards","Wider licenses"],"Compliance.")
H('170.d.9.A',3,"A career portfolio for an audio student might include:",
  "Mix samples, a resume, and certifications",["Receipts only","Blank pages","Unrelated photos"],"Career portfolio.")
H('170.d.9.A',4,"Adding a short description of your role on each sample in a portfolio helps employers:",
  "Understand exactly what you contributed",["Skip your work","Guess your skills","Ignore your résumé"],"Portfolio documentation.")
H('170.d.9.B',3,"Attending a local industry meetup to talk with engineers is:",
  "Professional networking",["Wasting time","Avoiding work","Social hiding"],"Networking.")
H('170.d.9.B',4,"A good way to use a career fair to land an audio internship is to:",
  "Introduce yourself and follow up with a thank-you message",["Skip all booths","Take free items only","Avoid conversation"],"Networking.")
H('170.d.9.C',3,"Starting a small business recording voice-overs for local companies is:",
  "Entrepreneurship",["Retirement","Unemployment","Job loss"],"Entrepreneurship.")
H('170.d.9.C',4,"A freelance audio engineer must handle tasks such as:",
  "Finding clients and managing invoices",["Avoiding all paperwork","Never setting prices","Skipping taxes"],"Entrepreneurship.")
H('170.d.10.A',3,"Scheduling setup, tracking, and cleanup times for a session is:",
  "Planning and time management",["Guessing","Procrastinating","Ignoring deadlines"],"Time management.")
H('170.d.10.A',4,"To finish a mix by Friday, an engineer should:",
  "Break the work into smaller daily tasks",["Wait until Thursday night","Skip revisions","Start with no plan"],"Planning.")
H('170.d.10.B',3,"Using a DAW template with pre-routed tracks is technology that:",
  "Speeds up repeated setups",["Slows work","Adds errors","Wastes time"],"Productivity.")
H('170.d.10.B',4,"A cloud calendar that sends reminders for deadlines helps a producer:",
  "Stay on schedule",["Miss meetings","Lose files","Duplicate work"],"Technology productivity.")
H('170.d.11.A',3,"Jobs in the audio industry include:",
  "Live sound engineer, studio engineer, and podcast producer",["Only radio announcer","Only retail clerk","Only teacher"],"Career pathways.")
H('170.d.11.A',4,"Someone who enjoys sound for video games and film might choose a career in:",
  "Sound design",["Plumbing","Accounting","Agriculture"],"Career pathways.")
H('170.d.11.B',3,"The professional who blends final tracks into a balanced stereo mix is the:",
  "Mixing engineer",["Caterer","Security guard","Tour driver"],"Industry professionals.")
H('170.d.11.B',4,"A person who captures dialogue, ambience, and effects on a film set is a:",
  "Production sound mixer",["Gaffer","Colorist","Costume designer"],"Roles.")
H('170.d.11.C',3,"Knowing the history of audio helps a professional anticipate:",
  "Future changes in technology",["Past mistakes only","Nothing","Weather patterns"],"Trends.")
H('170.d.11.C',4,"Streaming has changed how artists earn money from recorded music, which is a:",
  "Current practice and trend in the industry",["Historic myth","Fixed rule","Law of physics"],"Trends.")
H('170.d.11.D',3,"Affordable laptops and interfaces mean more people can now:",
  "Record professional-sounding audio at home",["Avoid sound","Fix every mix","Stop making music"],"Changing technology.")
H('170.d.11.D',4,"Cloud collaboration tools let engineers in different cities:",
  "Work on the same project remotely",["Lose projects","Avoid email","Reduce quality"],"Technology impact.")
H('170.d.11.E',3,"\"Headroom\" in audio is the:",
  "Space between the average level and the maximum before distortion",["Height of the ceiling","Length of the cable","Number of mics"],"Terminology.")
H('170.d.11.E',4,"\"Noise floor\" refers to the:",
  "Level of unwanted background noise in a system",["Studio carpet","Loudest peak","Stage surface"],"Terminology.")
H('170.d.12.A',3,"A ribbon microphone is often chosen for:",
  "Warm, smooth tone on instruments and vocals",["Harsh digital edge","Extreme ruggedness","Wireless use only"],"Microphone types.")
H('170.d.12.A',4,"A shotgun microphone is best for:",
  "Picking up distant dialogue in a narrow direction",["Recording a drum kit overhead","Capturing room echo","Picking up everything equally"],"Microphone applications.")
H('170.d.12.B',3,"An omnidirectional pattern picks up sound:",
  "From all directions",["From the front only","From the back only","From one side only"],"Pickup patterns.")
H('170.d.12.B',4,"A supercardioid pattern is useful for rejecting sound from the:",
  "Sides while focusing on the front",["Top only","Front","Everything"],"Pickup patterns.")
H('170.d.12.C',3,"On a mixing console, the \"pan\" control places a sound:",
  "Between the left and right speakers",["In a different studio","Above the mixer","Behind the wall"],"Audio consoles.")
H('170.d.12.C',4,"A mixer's auxiliary send is commonly used to:",
  "Route part of a signal to effects or monitors",["Turn off the console","Delete tracks","Change room lighting"],"Console routing.")
H('170.d.12.D',3,"A limiter is used to:",
  "Prevent peaks from going above a set level",["Boost every peak","Add reverb","Change pitch"],"Audio processing.")
H('170.d.12.D',4,"A noise gate reduces unwanted sound by:",
  "Muting the signal when it falls below a threshold",["Boosting quiet sounds","Adding echo","Changing tempo"],"Processing equipment.")
H('170.d.12.E',3,"Digital recorders store audio as:",
  "Numeric data files",["Magnetic tape strips","Wax grooves","Paper tapes"],"Digital recorders.")
H('170.d.12.E',4,"One advantage of analog tape that some engineers prefer is its:",
  "Characteristic warm saturation",["Perfect silence","Unlimited tracks","Instant undo"],"Analog vs digital.")
H('170.d.12.F',3,"An XLR connector usually carries:",
  "A balanced audio signal",["A video signal","Wi-Fi","Power only"],"Connectors.")
H('170.d.12.F',4,"A patch bay lets an engineer:",
  "Reroute signals without moving equipment",["Cool the room","Play movies","Charge phones"],"Interconnect.")
H('170.d.12.G',3,"A pop filter placed in front of a vocal mic reduces:",
  "Plosive bursts from \"p\" and \"b\" sounds",["Room temperature","Cable weight","Battery usage"],"Additional hardware.")
H('170.d.12.G',4,"A shock mount holds a microphone to reduce:",
  "Vibrations traveling through the stand",["Room echo","Studio costs","Cable length"],"Additional hardware.")
H('170.d.12.H',3,"Near-field monitors are placed close to the engineer to:",
  "Hear the mix with less room influence",["Make the room louder","Light the studio","Hide sound"],"Speakers.")
H('170.d.12.H',4,"A subwoofer is used to reproduce:",
  "Very low-frequency sound",["Very high pitches","Only speech","Only clicks"],"Speakers.")
H('170.d.13.A',3,"In film audio, the dialogue, music, and effects groups that are mixed separately are called:",
  "Stems",["Sprockets","Slates","Reels"],"Key elements.")
H('170.d.13.A',4,"Keeping stems separate in a mix delivery makes it easier to:",
  "Create alternate versions such as foreign-language mixes",["Hide files","Reduce quality","Lose the session"],"Stems.")
H('170.d.13.B',3,"Fast drums and distorted guitars in an action scene help create:",
  "Energy and tension",["Calm","Sleepiness","Silence"],"Mood.")
H('170.d.13.B',4,"A sudden silence before a loud effect often produces:",
  "A startle or dramatic impact",["Boredom","Comfort","Humor only"],"Sound effects.")
H('170.d.13.C',3,"Stereo panning of a guitar hard to one side leaves space in the center for:",
  "Lead vocals",["Silence","A blank track","Headphones"],"Technical elements.")
H('170.d.13.C',4,"Adding delay to a vocal can create:",
  "An echo effect that adds space and depth",["A quieter mix","A shorter song","A pitch drop"],"Audio effects.")
H('170.d.13.D',3,"A WAV file is commonly used because it is:",
  "Uncompressed and high quality",["Tiny and lossy","Unplayable","Video only"],"Codecs.")
H('170.d.13.D',4,"Lowering the bitrate of an MP3 reduces the file size but also:",
  "Reduces audio quality",["Raises quality","Adds tracks","Increases length"],"Compression.")
H('170.d.14.A',3,"A script for a podcast ad needs the sponsor's message, a call to action, and:",
  "Timing so it fits the slot",["A set diagram","Costume notes","Camera angles"],"Audio scripts.")
H('170.d.14.A',4,"Sound cues written in the margin of a script tell the engineer:",
  "When to play music or effects",["How to cook","What to wear","Where to park"],"Script elements.")
H('170.d.14.B',3,"A scriptwriter reads a draft aloud to check:",
  "That the words sound natural",["Page count only","Font style","Margin size"],"Writing audio scripts.")
H('170.d.14.B',4,"Writing a radio spot in 30 seconds requires:",
  "Concise wording and a clear message",["Long explanations","Unfocused details","Silent pages"],"Script writing.")
H('170.d.14.C',3,"A producer needing a door slam sound can obtain it by recording one, synthesizing one, or:",
  "Using a licensed sound library",["Printing one","Photographing one","Painting one"],"Audio assets.")
H('170.d.14.C',4,"Foley artists create sound effects by:",
  "Performing everyday sounds in sync with picture",["Writing music","Editing video only","Mixing tapes"],"Create audio assets.")
H('170.d.15.A',3,"Setting the input gain before pressing record helps avoid:",
  "Distorted or too-quiet recordings",["Long sessions","Heavy mics","Missing cables"],"Record audio.")
H('170.d.15.A',4,"Importing a loop into a session at the project tempo is helped by:",
  "Matching the sample rate and tempo",["Deleting the loop","Muting the project","Changing the title"],"Import audio.")
H('170.d.15.B',3,"A bus or group track is useful for:",
  "Controlling several tracks together",["Deleting all tracks","Recording video","Printing labels"],"Audio tracks.")
H('170.d.15.B',4,"A MIDI track differs from an audio track because it holds:",
  "Performance data instead of recorded sound",["A photograph","Printed text","Video frames"],"Track types.")
H('170.d.15.C',3,"Splitting a clip at the playhead is called a:",
  "Cut",["Fade-in","Bounce","Mute"],"Editing tools.")
H('170.d.15.C',4,"A fade-out at the end of a song prevents:",
  "An abrupt, jarring stop",["A smooth ending","A longer song","A louder mix"],"Fades.")
H('170.d.15.D',3,"A reverb plug-in simulates:",
  "The sound of a space such as a hall",["A change of key","A faster tempo","A new microphone"],"Plug-ins.")
H('170.d.15.D',4,"A limiter plug-in on the master bus is often used to:",
  "Raise perceived loudness without clipping",["Remove all dynamics","Add silence","Mute the mix"],"Plug-ins.")
H('170.d.15.E',3,"Drawing a volume automation curve that dips during a spoken line is called:",
  "Ducking the music under the voice",["Muting the voice","Adding noise","Deleting the music"],"Automation.")
H('170.d.15.E',4,"Writing automation for a filter sweep on a synth is done to:",
  "Change the sound smoothly over time",["Stop the track","Delete the plug-in","Reduce file size"],"Automation.")
H('170.d.15.F',3,"Audio prepared for a smartphone app is often delivered as a:",
  "Compressed file such as AAC or MP3",["Vinyl record","Paper score","Radio tower"],"Delivery formats.")
H('170.d.15.F',4,"For CD mastering, the standard audio format delivered is:",
  "16-bit, 44.1 kHz",["8-bit, 8 kHz","32-bit, 192 kHz only","24-bit, 11 kHz"],"Delivery formats.")

# ---------- 127.171 Video Game Design ----------
H('171.d.4',3,"Not sharing your password or personal details with strangers in an online game is practicing:",
  "Cyber safety",["Game balance","Level design","Frame rate"],"Cyber safety procedures.")
H('171.d.4',4,"A message in a game chat offers free in-game items if you click an unknown link. The safe response is to:",
  "Ignore it and report the message",["Click it quickly","Send it to friends","Enter your password"],"Cyber safety.")
H('171.d.7',3,"A designer who learns keyboard shortcuts in a game engine is applying technical skills for:",
  "Efficiency",["Confusion","Slowdown","Distraction"],"Technical skills.")
H('171.d.7',4,"Reusing a prefab (a saved object template) across levels helps a developer:",
  "Save time and keep objects consistent",["Add errors","Lose files","Slow loading"],"Efficiency.")
H('171.d.12',3,"A student plays a classmate's game and notes what is fun and what is confusing. This is:",
  "Evaluating a product with critical thinking",["Guessing","Copying","Hiding bugs"],"Evaluate a product.")
H('171.d.12',4,"The best evidence for judging whether a puzzle level is too hard is:",
  "How many testers complete it and where they get stuck",["A random guess","The designer's mood","The file size"],"Evaluate.")
H('171.d.14',3,"A student plans, builds, tests, and shares a simple platformer. This is a:",
  "Video game design project",["Reading assignment","Lunch menu","Hall pass"],"Create video game projects.")
H('171.d.14',4,"Before building a game, a design team often writes a short document describing goals, rules, and characters called a:",
  "Game design document",["Receipt","Menu","Pay stub"],"Design projects.")
H('171.d.16',3,"A game character falls through the floor. The developer first tries to:",
  "Test to find what causes the bug",["Delete the game","Ignore it","Blame the player"],"Problem-solving strategies.")
H('171.d.16',4,"Debugging by changing one thing at a time is useful because it:",
  "Shows which change fixed or caused the problem",["Hides the bug","Adds more bugs","Wastes time"],"Problem solving.")
H('171.d.17',3,"Coding a game with names like playerSpeed instead of x1 makes code:",
  "Easier to read and fix",["Harder to read","Slower to run always","Unusable"],"Expressive coding.")
H('171.d.17',4,"Putting repeated code into a function lets a developer:",
  "Reuse it instead of retyping it",["Type it again each time","Delete the game","Avoid testing"],"Efficient coding.")
H('171.d.18',3,"A tester says, \"The jump feels floaty, but the art looks great.\" This is:",
  "Constructive criticism",["An insult","Spam","A bug"],"Constructive criticism.")
H('171.d.18',4,"A designer responds well to feedback on a prototype by:",
  "Thanking the tester and trying useful suggestions",["Arguing","Ignoring it","Quitting"],"Apply criticism.")
H('171.d.1.A',3,"Writing clear instructions for how to play a game demonstrates:",
  "English language arts skills",["Welding skills","Plumbing skills","Gardening skills"],"ELA.")
H('171.d.1.A',4,"A game's story dialogue is easier to follow when the writer uses correct:",
  "Spelling, punctuation, and grammar",["Random letters","No spaces","All capitals only"],"ELA.")
H('171.d.1.B',3,"A character has 120 health points and takes 15 points of damage per hit. How many hits does it take to reach zero?",
  "8",["6","10","12"],"120 / 15 = 8.")
H('171.d.1.B',4,"A game gives 250 points per level and a 10% bonus for finishing fast. What are the points for a fast finish?",
  "275",["260","300","225"],"250 + 25 = 275.")
H('171.d.2.A',3,"Explaining game rules to a young player in simple words is adapting language to the:",
  "Audience",["Platform","Console","Screen size"],"Adapt language.")
H('171.d.2.A',4,"A pitch to investors uses more business terms than a tutorial for players because of the:",
  "Purpose and audience",["Frame rate","File type","Controller size"],"Adapt language.")
H('171.d.2.B',3,"Writing a clear outline of levels, characters, and items before building is:",
  "Organizing information",["Debugging","Rendering","Compiling"],"Organize information.")
H('171.d.2.B',4,"A designer lists tasks in order from planning to testing so the team knows:",
  "What to do and when",["Nothing","Which game is best","Who is the loudest"],"Organize.")
H('171.d.2.C',3,"A designer reports that 70% of testers quit at level three. This is:",
  "Interpreting and communicating information",["Hiding data","Guessing","Decorating"],"Interpret information.")
H('171.d.2.C',4,"Showing a team a chart of where players fail in a level helps them:",
  "Decide where to adjust difficulty",["Ignore problems","Delete levels","Add random bugs"],"Communicate.")
H('171.d.2.D',3,"A teammate looks at the speaker, avoids interruptions, and asks follow-up questions. This is:",
  "Active listening",["Daydreaming","Ignoring","Multitasking"],"Active listening.")
H('171.d.2.D',4,"Restating a teammate's bug report before fixing it ensures:",
  "You understood the problem",["The bug disappears","The report is wrong","The game is faster"],"Active listening.")
H('171.d.2.E',3,"Working with teammates who have different backgrounds and ideas requires:",
  "Respectful communication",["Teasing","Talking over others","Ignoring ideas"],"Diverse individuals.")
H('171.d.2.E',4,"A game with characters and stories from many cultures is more likely to:",
  "Appeal to a wider audience",["Confuse everyone","Lose players","Reduce creativity"],"Diversity.")
H('171.d.3.A',3,"A team decides which of two enemy designs is more fun by testing both with players. This is:",
  "Critical thinking in a group",["Guessing","Random choice","Copying"],"Critical thinking.")
H('171.d.3.A',4,"Choosing a game engine after comparing cost, features, and platform support relies on:",
  "Evidence-based critical thinking",["A coin flip","The loudest voice","Habit only"],"Critical thinking.")
H('171.d.3.B',3,"Two teammates disagree about a level layout. A good interpersonal approach is to:",
  "Listen to both and build a test version of each",["Insist on one","Walk away","Stay silent"],"Interpersonal skills.")
H('171.d.3.B',4,"Splitting work fairly by strengths on a game team shows:",
  "Group problem solving",["Poor planning","Competition","Avoidance"],"Interpersonal skills.")
H('171.d.5.A',3,"A team member who organizes a testing day and guides others shows:",
  "Leadership",["Avoidance","Delay","Distraction"],"Leadership.")
H('171.d.5.B',3,"Offering ideas and listening during a brainstorming session is:",
  "Participating in a group setting",["Working alone","Skipping class","Ignoring teammates"],"Group participation.")
H('171.d.5.A',4,"A game team lead keeps the team on schedule by:",
  "Setting clear milestones and checking progress",["Never meeting","Ignoring deadlines","Doing every job alone"],"Leadership.")
H('171.d.5.B',4,"A good participant in a game jam team:",
  "Shares tasks and communicates problems early",["Hides problems","Works in secret","Blames others"],"Group participation.")
H('171.d.6.A',3,"Giving credit to the artist who made the character in your game is:",
  "Ethical conduct",["Optional","Wasteful","A bug"],"Ethical conduct.")
H('171.d.6.A',4,"Keeping a friend's unreleased prototype private until they publish it is:",
  "Respecting others' rights and privacy",["Breaking rules","Poor teamwork","A mistake"],"Ethical conduct.")
H('171.d.6.B',3,"Copyright law applies to a game's code, art, and music because these are:",
  "Original creative works",["Public domain by default","Free to copy","Not owned by anyone"],"Copyright.")
H('171.d.6.B',4,"Using a popular song in your game released online without permission can:",
  "Violate copyright law",["Be legal","Improve the song","Be required"],"Copyright.")
H('171.d.6.C',3,"Using assets that carry a free license and following the license terms shows:",
  "Respect for intellectual property",["Piracy","Carelessness","Plagiarism"],"IP respect.")
H('171.d.6.C',4,"Making a game with your own original characters instead of copying a famous brand's is a way to:",
  "Avoid infringing on someone else's work",["Break the law","Lose originality","Reduce quality"],"IP respect.")
H('171.d.6.D',3,"A school's acceptable use policy says students should use computers for:",
  "Approved learning tasks",["Anything online","Downloading games","Hacking"],"Acceptable use policies.")
H('171.d.6.D',4,"Good online etiquette in a team chat includes:",
  "Writing respectfully",["Using all caps to yell","Spamming","Insulting others"],"Etiquette.")
H('171.d.6.E',3,"Video games influence society by affecting:",
  "Entertainment, education, and culture",["Only weather","Only trees","Only roads"],"Industry impact.")
H('171.d.6.E',4,"Educational games can help society by:",
  "Teaching skills in engaging ways",["Hiding facts","Reducing learning","Replacing all schools"],"Industry impact.")
H('171.d.8.A',3,"Knowing how to save, organize, and open files on Windows or macOS is knowledge of:",
  "Computer operating systems",["Weather maps","Cooking","Sports rules"],"Operating systems.")
H('171.d.8.A',4,"A game built for one operating system may need changes to run on another because of:",
  "Differences in system requirements",["Different weather","Different seating","Different clocks"],"Operating systems.")
H('171.d.8.B',3,"A graphics card (GPU) in a gaming computer mainly helps with:",
  "Rendering images",["Printing","Charging","Cooling the room"],"Hardware.")
H('171.d.8.B',4,"Adding more RAM can help a game development computer by:",
  "Running more programs at once",["Printing faster","Lowering the screen size","Increasing the volume"],"Hardware components.")
H('171.d.8.C',3,"Trimming a sound effect and normalizing its volume before adding it to a game is:",
  "Sound editing",["3D modeling","Level scripting","Texture painting"],"Sound editing.")
H('171.d.8.C',4,"Game developers often use short compressed audio files for effects to keep:",
  "The game's file size small",["The bugs","The lag","The cost"],"Sound.")
H('171.d.8.D',3,"A PNG image is commonly used in games because it supports:",
  "Transparency",["Only audio","Only text","Video playback"],"File formats.")
H('171.d.8.D',4,"A game exported for both PC and mobile must consider:",
  "Cross-platform compatibility",["Only color","Only price","Only title"],"Cross-platform compatibility.")
H('171.d.8.E',3,"Sharing a project folder with a teammate through a cloud service is:",
  "Exchanging information through electronic file sharing",["Printing files","Deleting files","Hiding files"],"File sharing.")
H('171.d.8.E',4,"Version control tools help a team by:",
  "Tracking changes and preventing overwrites",["Deleting files","Hiding errors","Breaking builds"],"File sharing.")
H('171.d.8.F',3,"A designer notices a game menu uses balanced layout and consistent colors. This is evaluating visuals by:",
  "Recognizing design principles",["Ignoring visuals","Reading code","Counting pixels only"],"Evaluate visual information.")
H('171.d.8.F',4,"Strong contrast between a character and the background mainly helps the player:",
  "See the character clearly",["Hear music","Save progress","Update the game"],"Principles of design.")
H('171.d.9.A',3,"Placing a character sprite over a background and adding a jump sound is:",
  "Combining graphics, images, and sound",["Compiling only","Deleting assets","Archiving"],"Combine media.")
H('171.d.9.A',4,"Layering a parallax background behind a platformer character adds:",
  "A sense of depth",["More bugs","Less art","Silence"],"Combine media.")
H('171.d.9.B',3,"Using repeated shapes and colors across a game's menus follows the design principle of:",
  "Consistency",["Randomness","Clutter","Confusion"],"Principles of design.")
H('171.d.9.B',4,"Placing the most important button larger and in the center applies the principle of:",
  "Emphasis",["Hiding","Repetition only","Noise"],"Principles of design.")
H('171.d.9.C',3,"A document that lists the controls, features, and required software for a game is:",
  "Technical documentation",["A menu","A receipt","A poster"],"Technical documentation.")
H('171.d.9.C',4,"A developer checks the engine's manual to learn how to use a function. This is:",
  "Referencing technical documentation",["Guessing","Wasting time","Avoiding work"],"Reference documentation.")
H('171.d.9.D',3,"Fixing a misaligned button and replacing a blurry texture in a game is:",
  "Editing the product",["Deleting it","Ignoring it","Selling it"],"Edit products.")
H('171.d.9.D',4,"After testing, a designer removes a confusing step from the tutorial. This is:",
  "Editing to improve the product",["Breaking the game","Adding bugs","Ignoring feedback"],"Edit products.")
H('171.d.10.A',3,"Early arcade games like Pong helped start the:",
  "Video game industry",["Print industry","Film industry","Radio industry"],"History of video game design.")
H('171.d.10.A',4,"The move from arcades to home consoles in the 1980s meant players could:",
  "Play games at home on a television",["Play only at malls","Stop playing","Use only paper"],"History.")
H('171.d.10.B',3,"Faster mobile phones have led to the growth of:",
  "Mobile gaming",["Typewriters","Rotary phones","Film reels"],"Changing technology.")
H('171.d.10.B',4,"Cloud gaming lets players stream games without needing:",
  "A powerful local console or PC",["The internet","A screen","A controller"],"Changing technology.")
H('171.d.10.C',3,"Games often use symbols such as a heart for health because symbols:",
  "Communicate meaning quickly",["Hide meaning","Confuse players","Slow the game"],"Symbols.")
H('171.d.10.C',4,"A symbol that is friendly in one culture can offend in another, so global designers should:",
  "Research cultural meanings",["Ignore them","Copy blindly","Remove all art"],"Symbols and cultures.")
H('171.d.10.D',3,"Compared with 1980s games, modern games typically have:",
  "More detailed graphics and online play",["Fewer colors","Less sound","Smaller worlds only"],"Compare technologies.")
H('171.d.10.D',4,"One difference between old cartridge-based games and modern digital games is that today's games can be:",
  "Updated with downloadable patches",["Never fixed","Played only once","Smaller than a pixel"],"Compare technologies.")
H('171.d.10.E',3,"A side-scrolling platformer and a first-person shooter are different:",
  "Styles or genres of games",["Weather types","Sports teams","Cars"],"Styles.")
H('171.d.10.E',4,"A puzzle game and a racing game differ most in their:",
  "Gameplay mechanics and goals",["Screen brand","Charger type","Box color"],"Compare styles.")
H('171.d.10.F',3,"Virtual reality headsets are an example of:",
  "Emerging game technology",["Old technology","Print media","Phone books"],"Emerging technologies.")
H('171.d.10.F',4,"Using AI to generate game content such as terrain is an example of:",
  "An innovative game design technology",["An outdated tool","A manual-only method","A board game"],"Emerging technologies.")
H('171.d.11.A',3,"Deciding who a game is for and writing a script and storyboard are early steps of:",
  "Game production",["Game deletion","Game selling","Game recycling"],"Production processes.")
H('171.d.11.A',4,"A storyboard for a game cutscene shows:",
  "Planned scenes in order",["Final sales","Code errors","Server logs"],"Storyboarding.")
H('171.d.11.B',3,"Making a character follow a set route across the screen uses:",
  "A motion path",["A password","A save file","A pixel font"],"Motion paths.")
H('171.d.11.B',4,"Scripting a door that opens when the player holds a key adds:",
  "Interactivity",["Silence","A new engine","Lag"],"Scripting and interactivity.")
H('171.d.11.C',3,"Perspective in a game scene helps show:",
  "Depth and distance",["Sound volume","File size","Frame count"],"Lighting and perspective.")
H('171.d.11.C',4,"Placing a bright light behind a character in a scene creates:",
  "A silhouette effect",["A larger file","A faster frame rate","A blank screen"],"Lighting.")
H('171.d.11.D',3,"A game's opening title, ending credits, and special effects are part of:",
  "Production processes",["Marketing only","Legal only","Shipping"],"Production.")
H('171.d.11.D',4,"Credits at the end of a game recognize:",
  "The people who worked on it",["The players only","The weather","The software errors"],"Credits.")
H('171.d.13.A',3,"A game with bright colors, simple controls, and cute characters is likely designed for:",
  "Young children",["Adult investors","Pilots","Engineers only"],"Identify the audience.")
H('171.d.13.A',4,"A game rated for mature audiences likely has content unsuitable for:",
  "Young children",["Adults","Everyone","Nobody"],"Intended audience.")
H('171.d.13.B',3,"The overall look and feel of a game, including art style and color, is its:",
  "Aesthetics",["Credits","Patch notes","Contract"],"Aesthetics.")
H('171.d.13.B',4,"A dark, muted palette with fog suggests aesthetics that are:",
  "Moody or spooky",["Cheerful","Cartoony","Bright"],"Aesthetics.")
H('171.d.13.C',3,"The story of a game, including its characters and plot, is its:",
  "Storyline",["Hardware","Controller","Frame rate"],"Storyline.")
H('171.d.13.C',4,"A good game storyline usually gives the player:",
  "A goal and a reason to care",["No goal","No characters","No setting"],"Storyline.")
H('171.d.13.D',3,"Summarizing a game's subject matter means describing what the game is:",
  "About",["Priced at","Colored","Sold with"],"Subject matter.")
H('171.d.13.D',4,"A game about managing a farm has a subject matter of:",
  "Farming and resource management",["Space combat","Dancing","Cooking only"],"Subject matter.")
H('171.d.13.E',3,"Sound in a game, such as footsteps and background music, helps create:",
  "Atmosphere and feedback for the player",["Silence only","Confusion","Delays"],"Use of sound.")
H('171.d.13.E',4,"A rising musical tone when a player collects a coin gives:",
  "Positive feedback",["No feedback","Negative feedback","Error messages"],"Use of sound.")
H('171.d.15.A',3,"Python, C#, and JavaScript are used in game design and also in fields like:",
  "Science, medicine, and finance",["Only art","Only music","Only sports"],"Programming languages.")
H('171.d.15.A',4,"Learning to code for games can also help a student in careers like:",
  "Data analysis or robotics",["Weather forecasting only","Nothing else","Gardening only"],"Programming in other fields.")
H('171.d.15.B',3,"In programming, a stored value that can change, such as a player's score, is a:",
  "Variable",["Constant sprite","Syntax tree","Server"],"Programming terminology.")
H('171.d.15.B',4,"A set of repeated steps in code, such as spawning enemies each second, is a:",
  "Loop",["Variable","Comment","Sprite"],"Programming concepts.")
H('171.d.19.A',3,"Joining an online forum for game developers to ask questions and share tips is:",
  "Participating in an electronic community",["Hiding","Quitting","Deleting"],"Electronic communities.")
H('171.d.19.A',4,"Contributing a helpful answer in a modding community is participating as a:",
  "Contributor",["Spammer","Observer only","Bot"],"Electronic communities.")
H('171.d.19.B',3,"Taking an online course on level design extends learning:",
  "Beyond the school building",["Inside a closet","Only to class","Nowhere"],"Digital learning.")
H('171.d.19.B',4,"Sharing a finished game build with players in another state through a website is using digital tools to:",
  "Reach audiences outside the school",["Limit sharing","Hide the game","Delete the build"],"Digital sharing.")
H('171.d.19.C',3,"Volunteering to teach younger students a simple game-making tool is:",
  "A meaningful community activity",["A waste","An error","A distraction"],"Community activities.")
H('171.d.19.C',4,"Entering a local game jam to meet other developers is a way to:",
  "Take part in the larger community",["Avoid people","Hide skills","Stop learning"],"Community.")
H('171.d.20.A',3,"A document listing required features and how a game will be judged is a:",
  "Specification and evaluation rubric",["Receipt","Greeting card","Poster"],"Technology specifications.")
H('171.d.20.A',4,"Writing clear specs before coding helps a team:",
  "Agree on what to build",["Skip planning","Avoid testing","Confuse members"],"Specifications.")
H('171.d.20.B',3,"When code throws an error, a developer reads the message and checks the:",
  "Line number mentioned",["Wall color","Mouse brand","Desk size"],"Debugging.")
H('171.d.20.B',4,"A good debugging strategy for a game that crashes at level five is to:",
  "Reproduce the crash and check recent changes",["Delete level five","Ignore it","Blame the player"],"Debug.")
H('171.d.21.A',3,"The part of a game that handles graphics, physics, and input is the:",
  "Game engine",["Game box","Game cover","Game poster"],"Game components.")
H('171.d.21.A',4,"The rules and objectives that define how a player interacts with a game make up its:",
  "Game play",["Packaging","Pricing","Marketing"],"Game components.")
H('171.d.21.B',3,"A dice-roll in a game program uses:",
  "A random number generator",["A fixed constant","A color picker","A font"],"Random numbers.")
H('171.d.21.B',4,"Randomly choosing where an enemy spawns keeps the game:",
  "Less predictable",["More predictable","Unplayable","Static"],"Random numbers.")
H('171.d.21.C',3,"A program that checks \"if health equals zero, show game over\" uses:",
  "A conditional statement",["A loop only","A comment","A sprite"],"Conditional statements.")
H('171.d.21.C',4,"In code, an else branch runs when the:",
  "if condition is false",["Game starts","if condition is true","Program ends"],"Conditionals.")
H('171.d.21.D',3,"A data model for a game inventory defines how items are:",
  "Stored and organized",["Colored","Priced","Advertised"],"Data models.")
H('171.d.21.D',4,"Storing each item with a name, type, and quantity is an example of a:",
  "Data structure",["Sound file","Title screen","Credit roll"],"Data model.")
H('171.d.21.E',3,"In object-oriented programming, a blueprint for creating game objects is a:",
  "Class",["Loop","Pixel","Bug"],"Object-oriented programming.")
H('171.d.21.E',4,"Making an Enemy class inherit common behavior from a Character class shows:",
  "Inheritance",["Compilation","Deletion","Randomization"],"Object-oriented game programming.")
H('171.d.21.F',3,"The main game loop repeatedly updates the game and:",
  "Draws the next frame",["Closes the window","Erases the code","Prints the manual"],"Game programming essentials.")
H('171.d.21.F',4,"Frame rate is measured in:",
  "Frames per second",["Bytes per level","Points per coin","Volts per pixel"],"Game programming.")
H('171.d.21.G',3,"Pressing a key triggers code that makes a character jump. That code responds to a:",
  "Game event",["Cover image","Sale","Review"],"Game events.")
H('171.d.21.G',4,"Animating a character by switching between images quickly is called:",
  "Sprite animation",["Compiling","Debugging","Packaging"],"Animation.")
H('171.d.21.H',3,"Unity and Unreal are examples of:",
  "Game engines",["Web browsers","Word processors","Spreadsheets"],"Role of game engines.")
H('171.d.21.H',4,"A game engine saves developers time by providing built-in tools for:",
  "Physics, rendering, and input",["Cooking","Weather forecasting","Banking"],"Game engines.")
H('171.d.21.I',3,"Arranging a health bar, score, and buttons on a game screen is:",
  "Screen design and layout",["Server setup","Sound editing","Texture compression"],"Game screen design.")
H('171.d.21.I',4,"A well-designed heads-up display (HUD) should:",
  "Show key information without blocking the action",["Cover the whole screen","Hide the score","Flicker constantly"],"Visual controls.")
H('171.d.21.J',3,"A game that supports keyboard, mouse, and gamepad uses game control design for:",
  "Multiple input devices",["Only one device","No input","Voice only"],"Game control.")
H('171.d.21.J',4,"Letting players remap the controls helps with:",
  "Accessibility and comfort",["Slower loading","Higher prices","Fewer players"],"Game control design.")
H('171.d.21.K',3,"Moving a sprite across the screen by changing its x-position each frame is:",
  "Basic game animation",["Compressing audio","Writing credits","Saving a file"],"Game animation.")
H('171.d.21.K',4,"Easing an animation so it starts slowly and speeds up makes movement feel:",
  "More natural",["More robotic","Broken","Frozen"],"Animation.")
H('171.d.21.L',3,"Code that waits for a button press and then reacts uses a:",
  "Listener",["Cover","Poster","Menu"],"Game events.")
H('171.d.21.L',4,"A trigger zone that starts a cutscene when the player enters it is an example of a:",
  "Game event trigger",["Spreadsheet","Soundtrack","Save point"],"Events and triggers.")
H('171.d.21.M',3,"Detecting when a player touches a wall or coin is:",
  "Collision detection",["Sound mixing","Level naming","Texture painting"],"Collision detection.")
H('171.d.21.M',4,"A bounding box around a sprite helps a game:",
  "Quickly check if two objects overlap",["Draw the sky","Play music","Save scores"],"Collision.")
H('171.d.21.N',3,"Earning experience points to reach a higher level is part of:",
  "Player progression",["Sound design","Menu layout","Data loss"],"Player progression.")
H('171.d.21.N',4,"Unlocking new abilities as a player advances keeps players:",
  "Motivated to continue",["Bored","Confused","Locked out for good"],"Progression.")
H('171.d.21.O',3,"An enemy that chooses to attack when the player is near and flee when its health is low shows:",
  "Algorithmic decision making",["Random chance only","No logic","Manual control"],"Algorithmic decision making.")
H('171.d.21.O',4,"A pathfinding algorithm lets a game character:",
  "Find a route around obstacles",["Delete obstacles","Stand still always","Hide the map"],"Algorithmic decisions.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_29.jsonl'))

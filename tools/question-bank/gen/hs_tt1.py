import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.323.', 1036, own='hs_tt1.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',2,"In a stage shop, what is a 'flat'?",
  "A wooden-framed, covered panel used as scenery",["A type of microphone","A costume undergarment","A box office report"],"Flats are basic scenic units.")
H('c.1.A',2,"A 'gel' is a colored sheet placed in front of a ___.",
  "Stage light",["Microphone","Sewing machine","Door lock"],"Gels color light.")
H('c.1.B',2,"Which stage type has the audience seated on three sides of the playing area?",
  "Thrust stage",["Proscenium stage","Black box with seats in one row","Orchestra pit"],"A thrust stage projects into the audience.")
H('c.1.B',2,"The fly system is used to ___.",
  "Raise and lower scenery and equipment above the stage",["Seat audience members","Cook meals","Mix colors for makeup"],"Fly systems move items overhead.")
H('c.1.C',2,"A production calendar is used to ___.",
  "Schedule rehearsals, builds and performance dates",["Choose paint colors only","Sell concessions","Rate audience members"],"Calendars organize deadlines.")
H('c.1.C',2,"What happens at a technical rehearsal?",
  "Cast and crew run cues for lights, sound and scenery changes",["Casting auditions","Costume shopping","Program printing"],"Tech rehearsals integrate technical elements.")
H('c.1.D',2,"Before using a power saw in the shop, a student should ___.",
  "Wear eye protection and get approval from the shop supervisor",["Remove the guard","Work alone at night","Wear loose sleeves"],"Tool safety starts with PPE and supervision.")
H('c.1.D',2,"Why must exit paths backstage stay clear?",
  "So people can leave quickly in a fire or emergency",["To make the room look larger","To store more props","To save electricity"],"Fire safety requires clear exits.")
H('c.1.E',3,"When reading a script for technical needs, a student underlines every mention of sounds, such as a doorbell. She is making a list of ___.",
  "Sound cues",["Costume repairs","Tickets","Rehearsal snacks"],"Scripts reveal technical requirements.")
H('c.1.E',3,"A stage direction says 'Night. Moonlight enters through the window.' This tells the lighting designer about ___.",
  "Time of day and the type of light needed",["The ticket price","The actor's age","The program fonts"],"Directions give lighting clues.")
H('c.2.A',3,"A realistic living-room play and an abstract dance piece would likely use ___ scenery.",
  "Different styles of",["Identical","No","Only digital"],"Style shapes technical choices.")
H('c.2.A',3,"In a fantasy genre production, which technical element often supports the world of the story?",
  "Special lighting, costumes and scenery that suggest a magical setting",["A grocery receipt","A lobby chair","A parking sign"],"Technical elements support genre.")
H('c.2.B',3,"Which order best lists the steps of the design process?",
  "Analysis, research, incubation/selection, implementation, evaluation",["Evaluation, implementation, analysis, research","Selection, evaluation, research, analysis","Research, evaluation, selection, analysis"],"The process begins with analysis and ends with evaluation.")
H('c.2.B',3,"During the 'research' step of design, a student might ___.",
  "Collect images and facts about the play's time and place",["Paint the final set","Strike the show","Sell tickets"],"Research informs design.")
H('c.2.C',2,"Who is in charge of coordinating all aspects of a production and communicating the vision?",
  "The director",["The usher","The caterer","The janitor"],"Directors guide the vision.")
H('c.2.C',2,"Which member of the production team calls cues during a performance?",
  "Stage manager",["Playwright","House painter","Costume buyer"],"Stage managers call cues.")
H('c.2.D',3,"A scenic designer and lighting designer talk before the build so the paint colors and lights work together. This shows ___.",
  "Collaboration",["Competition","Delay","Isolation"],"Teamwork prevents conflicts.")
H('c.2.D',3,"A crew head assigns tasks, checks progress and encourages teammates. She is showing ___.",
  "Leadership",["Hesitation","Mockery","Avoidance"],"Leaders organize and support.")
H('c.2.E',3,"A student chooses a color palette for a costume that shows a character's mood. This is ___ in design.",
  "Creative personal expression",["Plagiarism","A safety violation","Accounting"],"Creativity shapes design choices.")
H('c.2.E',3,"Which choice shows creativity in prop design?",
  "Building an original prop that fits the story",["Leaving the stage empty","Copying a catalog item exactly","Ignoring the script"],"Original solutions show creativity.")
H('c.2.F',3,"A designer gives the director a rendering and a swatch board for the costumes. These are ways to ___.",
  "Communicate design ideas",["Hide the design","Sell tickets","Cancel the show"],"Renderings and swatches communicate ideas.")
H('c.2.F',3,"A prompt book is a ___.",
  "Script with blocking, cues and notes used to run the show",["List of audience members","Menu for the cast party","Poster collection"],"The prompt book guides the performance.")
H('c.2.G',2,"A carpenter measures a board that is 8 feet long and needs two pieces of 3 feet each. How much is left over?",
  "2 feet",["1 foot","3 feet","5 feet"],"8 − (3 + 3) = 2.")
H('c.2.G',2,"Which tool is used to measure a length for a scenery board?",
  "A tape measure",["A voltmeter","A thermostat","A metronome"],"Tape measures give length.")
H('c.3.A',2,"What should you do with a hand saw when you finish a cut?",
  "Put it back in its proper storage place",["Leave it on the stage floor","Hand it to someone blade first","Throw it in a bin"],"Proper storage prevents accidents.")
H('c.3.A',2,"Which item protects a student's eyes while sanding scenery?",
  "Safety glasses",["A hat","A headset","A scarf"],"Eye protection is required.")
H('c.3.B',3,"Which part of the lighting system raises and lowers brightness?",
  "Dimmer",["Gobo","Cable tie","Clamp"],"Dimmers control intensity.")
H('c.3.B',3,"Before hanging a light, a student should ___.",
  "Check the safety cable and clamp and use a safe ladder with a partner",["Skip the cable","Climb without a spotter","Hang it unsupported"],"Rigging safety is essential.")
H('c.3.C',2,"When applying stage makeup, a performer should ___.",
  "Use clean tools and avoid sharing products that touch the eyes or mouth",["Share eye pencils freely","Use craft glue","Skip washing hands"],"Hygiene prevents infection.")
H('c.3.C',2,"Why use a thimble or pincushion when hand-sewing a costume?",
  "To protect fingers and keep pins organized",["To make the thread louder","To dye the cloth","To shrink the fabric"],"Tools prevent injury.")
H('c.3.D',3,"Which action keeps sound equipment safe?",
  "Keep drinks away from the sound board and tape down cables",["Pour water on the board","Pull on cables","Leave cords in doorways"],"Protect equipment and people.")
H('c.3.D',3,"Why should a sound operator keep volume levels in check?",
  "To protect hearing and equipment",["To shorten the play","To save ink","To change the set"],"Loud sound can damage ears and speakers.")
H('c.3.E',2,"The house manager is responsible for ___.",
  "Audience seating, safety and the front-of-house operations",["Painting the set","Calling cues from the booth","Writing the script"],"House management serves the audience.")
H('c.3.E',2,"Which person keeps the rehearsal and performance running smoothly backstage?",
  "Stage manager",["Concessions clerk","Parking attendant","Playbill printer"],"Stage managers coordinate backstage.")
H('c.4.A',3,"A designer researching a 1920s dress studies photos, fashion magazines and museum collections. She is establishing ___.",
  "Historical accuracy",["Silly mistakes","Budget cuts","Marketing"],"Research ensures accuracy.")
H('c.4.A',3,"Why does cultural accuracy matter in theatrical design?",
  "It respects the culture shown and helps the audience believe the world",["It reduces ticket costs","It removes the need for rehearsal","It replaces actors"],"Accuracy builds respect and credibility.")
H('c.4.B',3,"Compared with live theatre, film allows ___.",
  "Close-ups and editing that can change the audience's view instantly",["No sound","No story","A live audience only"],"Film uses camera and editing.")
H('c.4.B',3,"Which statement shows the impact of electronic media on theatre?",
  "Projections and digital sound are now used in many live productions",["Theatre ended","Theatre banned electricity","Theatre removed actors"],"Technology is integrated into live shows.")
H('c.4.C',3,"Greek theatre in ancient Athens used masks and an open-air amphitheater. This is part of the ___ of world theatre.",
  "Cultural heritage",["Parking plan","Ticket policy","Press kit"],"World theatre has a rich heritage.")
H('c.4.C',3,"Which key figure is known for plays performed at the Globe Theatre?",
  "William Shakespeare",["Walt Disney","Thomas Edison","Pablo Picasso"],"Shakespeare wrote for the Globe.")
H('c.4.D',3,"The United States contributed major innovations to stage lighting and design. One example is ___.",
  "Developments in electric stage lighting",["The invention of the mask","The amphitheater","The mystery play"],"American theatre advanced electric lighting.")
H('c.4.D',3,"Broadway is known for contributing which form that mixes music, dance and drama?",
  "The American musical",["Noh drama","Greek chorus","Commedia dell'arte"],"The musical is an American innovation.")
H('c.5.A',2,"A technical theatre portfolio usually includes ___.",
  "Photos, drawings and notes showing a student's design and build work",["Only a grocery list","Only a ticket","Only a program cover"],"Portfolios display work.")
H('c.5.A',2,"A resume for a technical theatre student lists ___.",
  "Experience, skills and productions worked on",["Favorite foods","Hair color","Locker number"],"Resumes summarize experience.")
H('c.5.B',2,"At a live performance, an audience member should ___.",
  "Silence phones and respect the performers and others",["Take flash photos","Talk loudly","Walk on stage"],"Etiquette supports the show.")
H('c.5.B',2,"Behavior at an outdoor theatre festival may differ from a formal theatre because ___.",
  "Different venues have different expectations",["There are no rules","Performers don't matter","Nobody is watching"],"Context affects etiquette.")
H('c.5.C',3,"A student reflects that a well-lit scene made the actors' expressions clear. She is evaluating the design as part of an ___.",
  "Art form",["Accident","Unplanned event","Mistake"],"Technical design is an art.")
H('c.5.C',3,"Self-evaluation after building a set helps a student ___.",
  "Identify what worked and what to improve",["Avoid learning","Blame others","Skip tools"],"Reflection improves skill.")
H('c.5.D',3,"A review that describes how the costumes and lighting supported the mood of the play is ___.",
  "Specific and precise",["Vague","Off-topic","Unrelated"],"Specific details support evaluation.")
H('c.5.D',3,"Which sentence evaluates a live play precisely?",
  "The warm amber lights during the kitchen scene made the family feel close",["It was okay","Nice show","I liked it"],"Precise observations name the element and effect.")
H('c.5.E',3,"A student reviews a film and notes how sound design heightened tension in a chase. She is evaluating ___.",
  "A medium with precise observations",["The ticket price","The theatre carpet","The parking"],"Film review can be as precise as theatre review.")
H('c.5.E',3,"When evaluating a TV drama, which comment is specific?",
  "The color grading made the flashbacks look faded and distant",["I like TV","It was long","The actors were fine"],"Specificity shows analysis.")
H('c.5.F',3,"A student who enjoys building scenery learns that carpenters, designers and technicians work in many careers. She is ___ theatre skills to careers.",
  "Connecting",["Hiding","Ending","Ignoring"],"Skills link to careers.")
H('c.5.F',3,"Which skill from technical theatre helps in many careers?",
  "Planning, teamwork and problem solving",["Avoiding tasks","Skipping safety","Ignoring deadlines"],"Skills transfer.")
H('c.5.G',3,"A student posts photos of her light plot and a short explanation on a class website. She is using ___ to present findings.",
  "Technology",["A hammer","A ladder only","A broom"],"Digital tools present information.")
H('c.5.G',3,"A clear slideshow of a technical project should ___.",
  "Use labeled images and short, organized text",["Include blurry unlabeled images","Be a wall of text","Have no order"],"Clarity helps the audience.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_tt1.jsonl'))

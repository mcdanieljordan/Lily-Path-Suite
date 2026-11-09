import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.324.', 1037, own='hs_tt2.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',2,"A crew member asks for a 'cyc' to be lit blue for a sky effect. The cyc is a ___.",
  "Large smooth backdrop at the back of the stage",["Tool for cutting fabric","Type of wig","Kind of ticket"],"A cyclorama is a stage backdrop.")
H('c.1.A',2,"In makeup vocabulary, 'contouring' means ___.",
  "Using light and dark shades to shape the face",["Removing all makeup","Gluing on a wig","Printing a program"],"Contouring shapes features.")
H('c.1.B',2,"The area of the stage to the audience's left of center is ___ when facing the audience from the actor's view.",
  "Actor's right",["Upstage","Offstage","Downstage"],"Stage left and right are from the actor's view.")
H('c.1.B',2,"The grid is the structure that ___.",
  "Supports the rigging and lines above the stage",["Seats the audience","Holds the costumes","Houses the ticket booth"],"The grid carries overhead loads.")
H('c.1.C',2,"A production meeting is used so that ___.",
  "Designers, directors and managers share progress and solve problems",["Actors audition","Ticket buyers choose seats","Crew members take breaks"],"Meetings coordinate departments.")
H('c.1.C',2,"What is the purpose of 'load-in'?",
  "Bringing scenery, lights and equipment into the theatre to prepare for tech",["Selling snacks","Casting the show","Writing the review"],"Load-in readies the venue.")
H('c.1.D',2,"Which shop practice improves safety?",
  "Keeping the floor clear of sawdust and cords",["Running in the shop","Horseplay with tools","Leaving blades out"],"A tidy shop prevents accidents.")
H('c.1.D',2,"If a fire alarm sounds during rehearsal, what should students do?",
  "Leave by the posted exit route and gather at the meeting place",["Finish the scene","Hide backstage","Go back for belongings"],"Follow evacuation procedures.")
H('c.1.E',3,"A student reads a script and marks every costume change with the page number. She is analyzing ___.",
  "Technical needs for the wardrobe department",["Seat prices","Parking","Press reviews"],"Script analysis identifies requirements.")
H('c.1.E',3,"A stage direction says 'Thunder rumbles.' Which department is most affected?",
  "Sound",["Costumes","Makeup","Properties"],"Thunder is a sound cue.")
H('c.2.A',3,"A realistic kitchen set and a minimalist dance set use technical elements differently. This reflects ___.",
  "Differences in theatrical style",["Seat numbers","Ticket color","Weather"],"Styles shape design choices.")
H('c.2.A',3,"For a comedy with quick entrances, which scenic choice helps?",
  "Doors that open easily and have clear sightlines",["Heavy locked doors","No exits","Windows only"],"Comedy needs practical movement.")
H('c.2.B',3,"When applying the design process, what step follows analysis?",
  "Research",["Strike","Opening night","Curtain call"],"Analysis then research.")
H('c.2.B',3,"What is the last step of the design process?",
  "Evaluation",["Analysis","Research","Incubation"],"Designers review the result at the end.")
H('c.2.C',3,"Which is a principle of design that deals with how heavy or light something looks on stage?",
  "Mass",["Applause","Echo","Tempo"],"Mass describes visual weight.")
H('c.2.C',3,"A diagonal line on stage often suggests ___.",
  "Movement or tension",["Calm rest","Silence","Absence"],"Diagonals add energy.")
H('c.2.D',3,"A designer repeats a color and shape throughout a set to create ___.",
  "Unity",["Chaos","Silence","Contrast only"],"Repetition builds unity.")
H('c.2.D',3,"A design that uses very different textures side by side shows ___.",
  "Contrast",["Harmony","Repetition","Unity"],"Opposites create contrast.")
H('c.2.E',3,"Mixing red and green light on a white wall will give what color of light, in additive color mixing?",
  "Yellow",["Purple","Black","Orange"],"Red + green light = yellow.")
H('c.2.E',3,"Warm colors on stage often suggest ___.",
  "Comfort or energy",["Cold distance","Silence","Absence"],"Warm hues feel inviting.")
H('c.2.F',3,"A director asks for a 'cold, lonely' lighting mood. A lighting designer responds with ___.",
  "Cool blues and low angles",["Warm amber glow","Bright white everywhere","No light at all"],"Designers translate mood into tools.")
H('c.2.F',3,"What is a costume rendering used for?",
  "To show the director the design of a costume",["To measure lumber","To mix sound","To sell tickets"],"Renderings communicate designs.")
H('c.2.G',3,"A scale model uses 1/2 inch to represent 1 foot. A wall 10 feet tall will measure ___ in the model.",
  "5 inches",["10 inches","2 inches","20 inches"],"10 × 1/2 = 5.")
H('c.2.G',3,"A drafter draws a 12-foot platform at a scale of 1/4 inch = 1 foot. How long is the drawing?",
  "3 inches",["12 inches","6 inches","1 inch"],"12 × 1/4 = 3.")
H('c.3.A',2,"Before operating the drill press, a student should ___.",
  "Secure the work piece and wear safety glasses",["Remove the guard","Hold the piece by hand","Work in loose clothing"],"Clamps and PPE prevent injury.")
H('c.3.A',2,"Who may use a table saw in the school shop?",
  "Trained students with permission from the teacher",["Anyone","Visitors","New students on their first day"],"Training and approval are required.")
H('c.3.C',3,"A light plot shows ___.",
  "Where each lighting instrument is hung and aimed",["The cast list","The ticket sales","The menu"],"A plot maps instruments.")
H('c.3.C',3,"A costume plot lists ___.",
  "Which characters wear which costumes in each scene",["Seats","Lighting levels","Sound cues only"],"It tracks costume use.")
H('c.3.B.i',3,"A flat is made from a wooden frame covered with ___.",
  "Muslin or thin plywood",["Water","Metal foil only","Candy wrappers"],"Flats are covered with fabric or plywood.")
H('c.3.B.i',3,"To build stairs for a set, a student must ensure ___.",
  "Rise and run are equal for every step",["Every step is a different height","No supports are used","They are glued with paste only"],"Equal rises prevent tripping.")
H('c.3.B.ii',3,"Before altering a costume, a crew member should ___.",
  "Take measurements and pin the changes while the actor wears it carefully",["Cut without measuring","Skip the fitting","Use scissors on the actor"],"Fittings prevent errors.")
H('c.3.B.ii',3,"A seam allowance is ___.",
  "Extra fabric between the stitch line and the cut edge",["A type of dye","A wig style","A color of thread"],"Seam allowance allows for finishing.")
H('c.3.B.iii',3,"After hanging a light, the next step is to ___.",
  "Focus it by aiming and adjusting the shutters and beam",["Bury it","Paint it","Hide it"],"Focus aims and shapes the light.")
H('c.3.B.iii',3,"A lighting controller is used to ___.",
  "Set and change the levels of the instruments",["Seat audience members","Mix paints","Measure lumber"],"Controllers operate lights.")
H('c.3.B.iv',3,"The unit used to measure electrical current is the ___.",
  "Ampere",["Volt","Ohm","Watt"],"Current is measured in amperes.")
H('c.3.B.iv',3,"What does a circuit breaker do?",
  "Stops current if the circuit is overloaded",["Colors the beam","Makes sound","Counts tickets"],"Breakers protect from overload.")
H('c.3.B.v',3,"A sound designer records a door slam using a microphone. She is ___ a sound effect.",
  "Creating",["Selling","Burying","Cutting a costume for"],"Recording makes effects.")
H('c.3.B.v',3,"Editing a sound effect to make it shorter involves ___.",
  "Trimming the audio file",["Cutting the cable","Adding paint","Moving the stage"],"Editing changes length.")
H('c.3.B.vi',2,"Which is a marketing product for a school play?",
  "Poster or program",["Ladder","Saw","Clamp"],"Posters and programs promote shows.")
H('c.3.B.vi',2,"Why do theatres use social media posts to market a show?",
  "To reach audiences and sell tickets",["To hide the show","To hire actors","To build scenery"],"Marketing attracts audiences.")
H('c.3.B.vii',3,"A promptbook is built by ___.",
  "Collecting script pages with blocking, cues and notes in one place",["Selling tickets","Painting walls","Ordering supplies"],"The promptbook guides the show.")
H('c.3.B.vii',3,"When the stage manager says 'Standby light cue 12,' she is ___.",
  "Warning the operator that the cue is coming",["Starting intermission","Ending the show","Calling a break"],"Standbys prepare for cues.")
H('c.3.B.viii',3,"In scenic painting, 'dry brushing' is used to ___.",
  "Add texture by lightly dragging a brush with little paint",["Soak the flat","Clean a brush with water","Mix colors with a hammer"],"Dry brushing adds texture.")
H('c.3.B.viii',3,"A base coat on a flat is used to ___.",
  "Cover the surface before adding details",["Make it heavier","Make it louder","Hide the script"],"A base coat prepares the surface.")
H('c.3.B.ix',3,"The property master may 'buy, borrow or build' an item. Which is an example of borrowing?",
  "Asking a community member to lend a rocking chair for the run",["Purchasing a new chair","Sewing a chair","Painting a flat"],"Borrowing means loaning.")
H('c.3.B.ix',3,"Why is a props table organized by scene?",
  "So actors and crew can find items quickly",["To hide the props","To confuse the cast","To cut the show"],"Organization speeds changes.")
H('c.4.A',3,"A designer studying Victorian homes adds detailed wallpaper and furniture to the set. She is applying ___.",
  "Historical accuracy from research",["Guesswork","Randomness","Rule breaking"],"Research informs details.")
H('c.4.A',3,"When designing for a play set in a particular culture, what should a designer do first?",
  "Research authentic clothing, architecture and symbols",["Guess","Copy a cartoon","Ignore the setting"],"Authenticity needs research.")
H('c.4.B',3,"A film can show multiple locations through editing. A stage design typically solves location changes with ___.",
  "Scenery, lighting and transitions",["Cuts to different cameras","Sound alone","Printed maps"],"Stages use scenic transitions.")
H('c.4.B',3,"Which statement describes the influence of television on live theatre?",
  "Audiences expect polished visuals and sound",["Theatre disappeared","Audiences dislike stories","Actors stopped speaking"],"Media raised expectations.")
H('c.4.C',3,"Japanese Kabuki and Noh theatre show the ___ of world theatre.",
  "Cultural heritage",["Cost","Weather","Parking"],"They are major traditions.")
H('c.4.C',3,"Which ancient playwright wrote tragedies such as 'Oedipus Rex'?",
  "Sophocles",["Edison","Picasso","Mozart"],"Sophocles is a Greek tragedian.")
H('c.4.D',3,"Which theatre building style was introduced during the Renaissance, featuring a frame around the stage?",
  "Proscenium",["Amphitheater","Arena","Longhouse"],"Proscenium theatres frame the stage.")
H('c.4.D',3,"Greek theatres were built into hillsides in a shape called a(n) ___.",
  "Amphitheater",["Booth","Hangar","Atrium"],"Hillsides provided seating.")
H('c.4.E',3,"Early stage lighting used candles and oil lamps. Later, theatres adopted gas and then ___.",
  "Electric lighting",["Fireworks","Torches only","Mirrors only"],"Technology progressed to electric.")
H('c.4.E',3,"LED instruments have changed theatre because they ___.",
  "Use less energy and can change colors easily",["Burn hotter","Need candles","Are silent"],"LED technology is efficient and flexible.")
H('c.4.F',3,"American theatre has been shaped by many cultures, including African American, Latino and Native American playwrights. This is the ___ heritage of US theatre.",
  "Multicultural",["Single","Imaginary","Foreign only"],"U.S. theatre reflects many cultures.")
H('c.4.F',3,"Which playwright is known for writing 'A Raisin in the Sun'?",
  "Lorraine Hansberry",["Tennessee Williams","Arthur Miller","Neil Simon"],"Hansberry wrote this play.")
H('c.4.G',3,"Which US innovation helped lighting designers control many lights at once?",
  "Computerized dimmer boards",["Candle chandeliers","Hand mirrors","Torch lines"],"Computer boards enabled complex cueing.")
H('c.4.G',3,"The United States is credited with developing which form that combines song, dance and story?",
  "The musical",["Noh","Commedia dell'arte","Greek chorus"],"The musical grew in America.")
H('c.5.A',2,"A resume for technical theatre should include ___.",
  "Productions worked on, roles held and skills learned",["Favorite color","Pet names","Lunch menu"],"Resumes list relevant experience.")
H('c.5.A',2,"A portfolio of technical theatre works may include ___.",
  "Photos of finished sets, drawings and light plots",["Only receipts","Only tickets","Only programs from other schools"],"Portfolios show work.")
H('c.5.B',2,"A crew member on headset during a show should ___.",
  "Speak only when needed and keep chatter off the line",["Chat constantly","Sing along","Turn the volume to loud"],"Quiet headset discipline.")
H('c.5.B',2,"What should a backstage crew member wear during a show?",
  "Dark, quiet clothing and closed-toe shoes",["Bright costumes","Noisy shoes","Flip-flops"],"Backstage attire is quiet and safe.")
H('c.5.C',3,"A student reflects that her sound design added tension to a scene. She is evaluating her work as ___.",
  "Art that affects the audience",["Random noise","Scrap","A rule violation"],"Design is an art form.")
H('c.5.C',3,"Self-evaluation in technical theatre includes ___.",
  "Looking at what worked, what failed and how to improve",["Ignoring results","Praising only","Blaming others"],"Reflection builds skill.")
H('c.5.D',3,"A peer says: 'Your color palette is cohesive, but the platform edges look unfinished.' This is ___.",
  "Constructive criticism",["A rumor","An insult","Spam"],"Specific and helpful.")
H('c.5.D',3,"When someone critiques your design, you should ___.",
  "Listen, ask questions and consider changes",["Interrupt","Ignore","Argue"],"Open reception improves work.")
H('c.5.E',3,"A reviewer writes that a lighting change at the climax focused attention on the actor. This is ___ evaluation.",
  "Specific",["Vague","Unrelated","Silent"],"Specific details support evaluation.")
H('c.5.E',3,"Which describes a precise comment on a play's scenery?",
  "The revolving set shifted smoothly between the home and the office",["Looked fine","It was a set","Pretty"],"Precision names effect.")
H('c.5.F',3,"A student compares the camera work in a film to the staging in a play. She is evaluating ___.",
  "Different media",["The weather","The parking","The ticket color"],"Different media use different tools.")
H('c.5.F',3,"Which is a precise comment on a TV show's costumes?",
  "The muted colors matched the gloomy tone of the story",["Looked nice","They wore clothes","Fine"],"Detailed observation.")
H('c.5.G',3,"A student interested in sound might explore a career as ___.",
  "Audio engineer in theatre or film",["Surveyor","Pilot","Chef"],"Audio careers exist in several media.")
H('c.5.G',3,"Which place hires scenic carpenters besides theatres?",
  "Film studios and theme parks",["Libraries only","Banks only","Weather stations only"],"Industries use scenic skills.")
H('c.5.H',3,"Time management learned in technical theatre helps students in ___.",
  "College and other careers",["Nothing","Only shows","Only drama class"],"Skills transfer.")
H('c.5.H',3,"A student explains that problem solving on a crew will help in engineering school. She is ___ theatre to higher education.",
  "Connecting",["Rejecting","Hiding","Ending"],"She links experience to her future.")
H('c.5.I',3,"A student uses presentation software to explain how she built a staircase. She is using ___ to communicate findings.",
  "Technology",["A hammer","A saw","A drill bit"],"Slides communicate process.")
H('c.5.I',3,"A coherent technical presentation has ___.",
  "Clear structure, labeled visuals and concise explanations",["Random order","Long unlabeled paragraphs","No images"],"Organization helps audiences.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_tt2.jsonl'))

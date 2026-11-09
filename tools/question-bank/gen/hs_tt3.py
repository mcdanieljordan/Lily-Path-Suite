import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.325.', 1038, own='hs_tt3.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',3,"A master electrician tells the crew to 'gang' dimmers on one channel. In lighting vocabulary this means ___.",
  "Grouping several circuits to be controlled together",["Painting a flat","Sewing a hem","Printing a poster"],"Ganging links circuits.")
H('c.1.A',3,"In costume vocabulary, a 'muslin' is a ___.",
  "Inexpensive test garment used to check fit before cutting the final fabric",["Kind of wig","Type of sound cable","Stage floor finish"],"Muslins are fitting prototypes.")
H('c.1.B',3,"A student explains that a 'rake' is a stage floor that ___.",
  "Slopes upward away from the audience",["Rotates","Folds flat","Lifts like an elevator"],"A raked stage tilts.")
H('c.1.B',3,"Counterweight fly systems let a crew member ___.",
  "Move heavy scenery with balanced weights and a rope lock",["Lift scenery by throwing ropes","Hold scenery by hand only","Burn lines to drop it"],"Counterweights balance loads.")
H('c.1.C',3,"A designer builds a production calendar working backward from opening night. This helps to ___.",
  "Set deadlines for design, build and tech",["Choose the cast","Print tickets only","Cancel rehearsals"],"Backward planning meets deadlines.")
H('c.1.C',3,"During a 'cue-to-cue' rehearsal, the team ___.",
  "Skips to each technical cue to test and adjust it",["Reads the whole play aloud","Auditions new actors","Strikes the set"],"Cue-to-cue focuses on technical transitions.")
H('c.1.D',3,"A student models shop safety by wearing hearing protection near a planer and ___.",
  "Tying back long hair and removing loose jewelry",["Wearing open sandals","Leaving the guard off","Working without instruction"],"Personal safety includes clothing choices.")
H('c.1.D',3,"Which action models fire safety in a theatre?",
  "Using flame-retardant materials and keeping extinguishers accessible",["Storing paint rags in a pile","Blocking the fire exit","Disabling the alarm"],"Fire safety requires planning.")
H('c.1.E',3,"A student creates a scene-by-scene breakdown listing each prop, light cue and sound cue. She is ___.",
  "Applying script analysis to technical needs",["Selling tickets","Choosing seats","Writing a review"],"A breakdown organizes requirements.")
H('c.1.E',3,"A script says 'The room slowly fills with fog.' The student marks this for ___.",
  "Special effects and possibly the lighting department",["Box office","Ushers","Programs"],"Fog affects lighting and safety.")
H('c.2.A',3,"For a Greek tragedy performed on a bare stage with masks, which technical element carries much of the style?",
  "Mask and costume design",["Revolving scenery","Heavy fog only","Digital video wall"],"Style determines focus.")
H('c.2.A',3,"For a futuristic science-fiction play, which technical choice supports the genre?",
  "Metallic scenery, cool lighting and electronic sound",["Candles and wood","Plain curtains","Only a spotlight"],"Elements reinforce genre.")
H('c.2.B',3,"At the 'incubation/selection' stage, a designer ___.",
  "Sketches possible ideas and chooses the strongest concept",["Strikes the show","Sells ads","Cleans the shop"],"Ideas are developed and one is chosen.")
H('c.2.B',3,"After implementation, a designer evaluates the design by ___.",
  "Reviewing how well it served the production and noting improvements",["Hiding results","Ignoring feedback","Skipping tech"],"Evaluation closes the loop.")
H('c.2.C',3,"A scenic designer uses vertical lines in a courthouse set to suggest ___.",
  "Height, strength or formality",["Weakness","Chaos","Silliness"],"Vertical lines convey stature.")
H('c.2.C',3,"The principle of 'position' in design refers to ___.",
  "Where an element is placed on stage",["The price of the set","The time of the play","The cast size"],"Placement affects focus.")
H('c.2.D',3,"A designer varies the heights of platforms so the stage picture is interesting. This is ___.",
  "Variation",["Duplication","Monotony","Unity only"],"Variation adds interest.")
H('c.2.D',3,"A symmetrical set with matching panels on each side shows ___.",
  "Formal balance",["Random layout","Chaos","Rhythm only"],"Symmetry gives formal balance.")
H('c.2.E',3,"A lighting designer puts a blue gel on a warm amber light. The result will be ___.",
  "A muted, darker color because the gel absorbs some light",["A brighter white","A pure red","No change"],"Filters subtract wavelengths.")
H('c.2.E',3,"The three primary colors of light are ___.",
  "Red, green and blue",["Red, yellow and blue","Cyan, magenta and yellow","Black, white and gray"],"Additive primaries are RGB.")
H('c.2.F',3,"A technical director coordinates the build schedule, the designers' needs and the crew's skills. He is ___ the team.",
  "Managing",["Dismissing","Ignoring","Confusing"],"Managers coordinate teams.")
H('c.2.F',3,"Which behavior supports effective teamwork in a production team?",
  "Clear communication and respect for deadlines",["Keeping secrets","Missing meetings","Blaming others"],"Communication and reliability.")
H('c.2.G',3,"A student writes that leadership helps a crew stay organized, safe and motivated. She is ___ it.",
  "Defending the importance of",["Rejecting","Hiding","Ignoring"],"Defending means supporting with reasons.")
H('c.2.G',3,"Which is a sign of strong leadership on a crew?",
  "Sharing credit and helping teammates solve problems",["Taking all the credit","Ignoring questions","Avoiding tasks"],"Leaders support teams.")
H('c.2.H',3,"A student paints a surprising texture on a prop that suits the character. She is developing ___.",
  "Creativity and personal expression",["Plagiarism","Imitation only","Neglect"],"Original choices express creativity.")
H('c.2.H',3,"Which approach helps a designer develop creativity?",
  "Experimenting with materials and sketching many ideas",["Copying the first idea","Avoiding research","Refusing feedback"],"Exploration builds creativity.")
H('c.2.I',3,"A director gives the designer a mood board and a copy of the script with notes. The designer is ___ technical theatre documents.",
  "Interpreting",["Burning","Selling","Erasing"],"Interpreting means understanding the intent.")
H('c.2.I',3,"A set designer draws a ground plan showing the stage from above. This document helps the crew ___.",
  "Place walls, doors and platforms correctly",["Cast the play","Choose music","Print programs"],"Ground plans show layout.")
H('c.2.J',3,"A drafter uses a scale of 1/2 inch = 1 foot. A 16-foot-wide set will be ___ on the drawing.",
  "8 inches",["16 inches","4 inches","32 inches"],"16 × 1/2 = 8.")
H('c.2.J',3,"A carpenter needs to cut a board to 5 feet 6 inches. How many total inches is that?",
  "66",["56","72","60"],"5 × 12 + 6 = 66.")
H('c.3.A',3,"Before using a router in the shop, a trained student should ___.",
  "Secure the work piece, set the bit depth and wear eye and ear protection",["Hold the piece loosely","Remove the guard","Wear loose sleeves"],"Specialized tools need setup and PPE.")
H('c.3.A',3,"Which material requires a respirator to use safely?",
  "Spray paint and some adhesives with fumes",["Plain water","Fabric swatches","Paper tickets"],"Fumes require protection.")
H('c.3.C',3,"The master carpenter in a theatre ___.",
  "Leads the construction of scenery",["Calls cues","Sells tickets","Selects music"],"Carpenters build the sets.")
H('c.3.C',3,"A costume shop manager typically ___.",
  "Supervises costume construction, fittings and care",["Mixes sound","Hangs lights","Paints flats"],"Costume managers lead wardrobe work.")
H('c.3.D',3,"A student creates a light plot and a channel hookup. These documents tell the crew ___.",
  "Where instruments hang and how they are patched",["Who is in the cast","How tickets are priced","Where to park"],"Plots and hookups guide the electricians.")
H('c.3.D',3,"A student interprets a costume plot to find ___.",
  "Which costume pieces each character wears in each scene",["Dimmer levels","Gel colors only","Scene shop budget"],"Plots track costume use.")
H('c.3.B.i',3,"A student designing a set for a two-story house must plan for ___.",
  "Structural support and safe access for actors",["No access","No supports","Decorations only"],"Safety and structure matter.")
H('c.3.B.i',3,"What does 'stock' scenery refer to?",
  "Standard pieces such as flats and platforms that can be reused",["Scenery made of paper","Scenery thrown away","Scenery borrowed from space"],"Stock scenery is reusable.")
H('c.3.B.ii',3,"A costume designer picks fabric with 'drape' for a flowing gown because it ___.",
  "Hangs and moves gracefully",["Stands stiff","Never moves","Reflects light like a mirror"],"Drape affects movement.")
H('c.3.B.ii',3,"When pulling a costume from stock, the first step is to ___.",
  "Check it against the actor's measurements and the design",["Cut it","Dye it","Burn it"],"Stock pieces need fitting.")
H('c.3.B.iii',3,"Ohm's law relates voltage, current and ___.",
  "Resistance",["Color","Rhythm","Position"],"V = I × R.")
H('c.3.B.iii',3,"A 1,000-watt instrument on a 120-volt circuit draws about how much current?",
  "8.3 amps",["0.12 amps","120 amps","1,000 amps"],"1000 ÷ 120 ≈ 8.3.")
H('c.3.B.iv',3,"Sound travels as a ___.",
  "Wave of vibrations through a medium such as air",["Beam of light","Stream of heat","Stack of paper"],"Sound is a mechanical wave.")
H('c.3.B.iv',3,"A hard, bare wall in a theatre tends to ___ sound.",
  "Reflect",["Absorb completely","Erase","Heat"],"Hard surfaces reflect sound.")
H('c.3.B.v',3,"A marketing designer picks a bold image, readable type and clear dates for a poster. She is ___ a marketing product.",
  "Designing",["Scrapping","Burning","Hiding"],"Posters need clear design.")
H('c.3.B.v',3,"Which element must appear on a poster for a school play?",
  "Title, date, time and location",["Cast shoe sizes","Lighting hookups","Props list"],"Audiences need the basics.")
H('c.3.B.vi',3,"A stage manager records blocking in the promptbook using ___.",
  "Pencil notations that can be changed",["Permanent marker","Paint","Glue"],"Blocking changes in rehearsal.")
H('c.3.B.vi',3,"When calling cues, the stage manager says 'Go' to ___.",
  "Tell the operator to execute the cue",["Start intermission","Raise house lights","Seat the audience"],"'Go' triggers the cue.")
H('c.3.B.vii',3,"A scenic artist uses a sponge to apply layers of color for a stone effect. This is called ___.",
  "Sponging or stippling",["Embroidery","Welding","Rigging"],"Sponging creates texture.")
H('c.3.B.vii',3,"To refine a painting technique, a scenic artist should ___.",
  "Test it on a sample board and adjust before painting the final piece",["Paint without testing","Skip the base coat","Use only one color"],"Samples reduce errors.")
H('c.3.B.viii',3,"A prop designer creates a lightweight 'foam' sword for a fight scene. The reason is ___.",
  "Safety for performers",["To make noise","To hide the blade","To save paint"],"Safe props protect actors.")
H('c.3.B.viii',3,"A prop that an actor uses on stage is called a ___ prop.",
  "Hand or practical",["Floor only","Costume","Curtain"],"Hand props are used by actors.")
H('c.4.A',3,"A designer researching an African village scene studies architecture, textiles and symbols from that culture. This shows ___.",
  "Working knowledge of cultural accuracy",["Guessing","Mockery","Ignoring the setting"],"Research ensures accuracy.")
H('c.4.A',3,"If a play is set in the 1960s, which research source is most helpful?",
  "Photographs, magazines and museum collections from that time",["Modern cartoons","A fantasy novel","A cookbook"],"Primary sources give accuracy.")
H('c.4.B',3,"A student synthesizes that streaming and film editing have changed expectations of pacing in theatre. She is ___ the impact of media.",
  "Combining information to explain",["Ignoring","Deleting","Copying"],"Synthesis connects ideas.")
H('c.4.B',3,"Which is an effect of electronic media on theatre marketing?",
  "Online trailers and social media promote shows",["Posters were banned","Tickets became free","Audiences disappeared"],"Media expands marketing.")
H('c.4.C',3,"The Chinese Peking Opera uses elaborate makeup and costumes. It is an example of ___.",
  "Cultural heritage in world theatre",["A modern musical","Greek tragedy","A silent film"],"World theatre has many traditions.")
H('c.4.C',3,"Which key figure is associated with Italian commedia dell'arte masks?",
  "Harlequin",["Hamlet","Macbeth","Antigone"],"Harlequin is a commedia character.")
H('c.4.D',3,"The Elizabethan playhouse such as the Globe featured ___.",
  "An open-air thrust stage with galleries",["A proscenium arch with fly loft","An arena with no stage","A film screen"],"The Globe was thrust-style.")
H('c.4.D',3,"The invention of the proscenium arch during the Renaissance allowed designers to use ___.",
  "Painted perspective scenery",["No scenery","Only masks","Only candles"],"Proscenium theatres favored perspective sets.")
H('c.4.E',3,"The progression of lighting from limelight to electric to LED shows how technology has ___ theatre.",
  "Changed",["Ended","Frozen","Reversed"],"Technology evolves.")
H('c.4.E',3,"Which development made stage fog and haze safer and more controllable?",
  "Modern water-based fog machines",["Open flames","Smoke pots","Burning leaves"],"Safer devices reduce risk.")
H('c.4.F',3,"A student analyzes plays by Wilson, Hansberry and Miranda to see how different cultures have shaped American theatre. She is analyzing ___.",
  "The multicultural heritage of US theatre",["A single tradition","A foreign tradition only","A fictional tradition"],"U.S. theatre is multicultural.")
H('c.4.F',3,"August Wilson is known for plays about ___.",
  "African American life across the twentieth century",["Medieval knights","Ancient Rome","Space travel"],"Wilson wrote the Pittsburgh Cycle.")
H('c.4.G',3,"The Group Theatre and the Federal Theatre Project were important in ___.",
  "Developing American theatre in the 1930s",["Ancient Greece","The Renaissance","Roman times"],"They shaped US theatre history.")
H('c.4.G',3,"Which American designer is known for pioneering stage lighting design in the twentieth century?",
  "Jean Rosenthal",["Pablo Picasso","Vincent van Gogh","Claude Monet"],"Rosenthal advanced lighting design.")
H('c.5.A',3,"A resume for a technical theatre applicant should be ___.",
  "Organized, accurate and concise",["Handwritten on napkins","Long and unfocused","Full of jokes"],"Professionals value clarity.")
H('c.5.A',3,"A portfolio should show ___.",
  "A range of design and build work with clear labels",["Only one photo","Unrelated art","Random papers"],"Variety and clarity.")
H('c.5.B',3,"Backstage during a quiet scene, a crew member should ___.",
  "Move silently and follow the stage manager's instructions",["Chat loudly","Run","Use a flashlight carelessly"],"Quiet professionalism.")
H('c.5.B',3,"If a cue is missed, a technician should ___.",
  "Stay calm, tell the stage manager and follow instructions",["Panic","Leave","Hide"],"Calm communication keeps the show safe.")
H('c.5.C',3,"A student applies design elements such as color and line and then judges how well they served the story. She is evaluating herself as a ___.",
  "Creative artist",["Spectator only","Cashier","Visitor"],"Self-evaluation as an artist.")
H('c.5.C',3,"Reviewing photos of a finished set and comparing them to the original sketches helps a designer ___.",
  "Learn what to improve next time",["Avoid learning","Hide the sketch","Discard the photos"],"Comparison guides growth.")
H('c.5.D',3,"After a design presentation, a peer says: 'The color choices are strong; consider a more durable surface for the platform.' This is ___.",
  "Constructive feedback",["Rumor","Insult","Spam"],"Positive and specific.")
H('c.5.D',3,"When giving constructive criticism, you should ___.",
  "Be specific, respectful and offer a suggestion",["Be vague","Be rude","Be silent"],"Helpful feedback has suggestions.")
H('c.5.E',3,"A review that notes how the crew's quick scene changes kept the pace tight is ___.",
  "Specific and precise",["Vague","Unrelated","Silly"],"Details support the claim.")
H('c.5.E',3,"Which sentence evaluates sound design precisely?",
  "The low rumble under the ghost scene increased the tension",["It was noisy","Sound was there","I heard stuff"],"Precise observations name the effect.")
H('c.5.F',3,"A student compares the costume design of a period film to a stage play. She is evaluating ___.",
  "Two media with precise observations",["The weather","The ticket","The parking"],"Cross-media evaluation.")
H('c.5.F',3,"Which comment about a TV show's lighting is most specific?",
  "The flickering blue light suggested a hospital at night",["It was dark","It looked good","I liked it"],"Specific details.")
H('c.5.G',3,"A student articulates that technical theatre skills open careers in film, TV, concerts and theme parks. She is ___ opportunities.",
  "Describing",["Hiding","Closing","Denying"],"Articulating means explaining.")
H('c.5.G',3,"Which is an avocational opportunity in technical theatre?",
  "Volunteering on the crew of a community theatre",["Ignoring theatre","Selling cars only","Quitting"],"Avocational means pursued for enjoyment.")
H('c.5.H',3,"A student explains that the safety habits she learned in the shop will help her in a future engineering or construction career. She is ___ theatre to careers.",
  "Connecting",["Ignoring","Burning","Hiding"],"She links skills to careers.")
H('c.5.H',3,"Which skill from technical theatre helps in many fields?",
  "Meeting deadlines and working in a team",["Skipping steps","Avoiding teamwork","Ignoring plans"],"These skills transfer.")
H('c.5.I',3,"A student creates a short video that explains how her team built a revolving set. She is using ___ to communicate findings.",
  "Technology",["A saw","A hammer","A ladder"],"Video presents work.")
H('c.5.I',3,"A clear digital presentation of a design project has ___.",
  "Labeled drawings, photos and concise explanations",["Blank slides","Unlabeled files","Random order"],"Clarity helps audiences.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_tt3.jsonl'))

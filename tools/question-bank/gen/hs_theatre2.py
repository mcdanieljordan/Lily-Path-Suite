import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.316.', 1029, own='hs_theatre2.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',2,"Before a tough scene, the cast stretches, shakes out tension and runs tongue twisters together. This routine is called a ___.",
  "Warm-up",["Strike","Curtain call","Dress parade"],"Warm-ups prepare body and voice.")
H('c.1.A',2,"Which warm-up best prepares the facial muscles for clear speech?",
  "Exaggerated articulation drills",["Heavy lifting","Painting backdrops","Taking tickets"],"Articulation drills loosen the mouth and tongue.")
H('c.1.B',3,"An actor repeatedly rehearses a gesture that shows grief so it reads clearly from the back row. She is developing what?",
  "Consistent stage movement to express feelings",["Costume repairs","Box office totals","Lighting cues"],"Movement technique must be repeatable.")
H('c.1.B',3,"Why must stage movement be consistent from rehearsal to rehearsal?",
  "So partners and designers can rely on the staging",["To avoid thinking","To confuse the cast","To shorten the script"],"Consistency supports ensemble work.")
H('c.1.C',3,"An actor ends each line with a clear final consonant and projects to the last row. She is demonstrating what?",
  "Effective voice and diction",["Costume design","Set painting","Blocking notation"],"Diction and projection reach the audience.")
H('c.1.C',3,"Which habit helps an actor keep vocal stamina during a long run?",
  "Hydrating and resting the voice between shows",["Shouting offstage","Whispering strain","Skipping warm-ups"],"Vocal care sustains a run.")
H('c.1.D',3,"A play with a rising conflict, a climax and a falling resolution follows which dramatic structure?",
  "Freytag's pyramid",["A rondo","A sonnet","A haiku"],"Freytag describes dramatic arc.")
H('c.1.D',3,"A play meant to make audiences laugh at human foolishness belongs to which genre?",
  "Comedy",["Tragedy","Documentary","Melodrama only"],"Comedy entertains through humor.")
H('c.1.E',3,"A voice-over narrator who speaks directly to the audience is a convention seen in both stage and film. This is an example of a ___.",
  "Theatrical convention",["Camera lens","Costume stitch","Lighting gel"],"Conventions are accepted practices.")
H('c.1.E',3,"The audience accepts that a bare platform can represent a castle. This shows what?",
  "A shared theatrical convention",["A mistake","A set malfunction","A prop error"],"Audiences accept symbolic staging.")
H('c.1.F',3,"A designer notes that her costume colors must work with the lighting palette. This illustrates what about theatre?",
  "Its elements are interdependent",["Each element is isolated","Costumes do not matter","Light is optional"],"Elements affect each other.")
H('c.1.F',3,"If the sound cue is late, the actor's timing and the lighting change are affected. This relates to what?",
  "The interdependence of theatrical elements",["A budget problem","A seating plan","A ticket issue"],"One element depends on others.")
H('c.1.G',2,"Which strategy best helps memorize a long speech?",
  "Break it into beats and rehearse each with its motivation",["Read it once","Ignore it","Memorize only the first line"],"Chunking by beats helps recall.")
H('c.1.G',2,"Why should an actor practice lines aloud rather than silently?",
  "Speaking engages voice and memory together",["It saves time","It avoids rehearsal","It replaces blocking"],"Speaking reinforces memory.")
H('c.2.A',3,"A scene partner is uncomfortable with a physical stage action. What is the best response?",
  "Pause, communicate and adjust the action with the director",["Push forward","Ignore her feelings","Insist on it"],"Safe and respectful practice matters.")
H('c.2.A',3,"Why should actors set boundaries before an emotional scene?",
  "To allow expression while protecting well-being",["To avoid acting","To lengthen rehearsal","To cut the scene"],"Boundaries support safe emotion.")
H('c.2.B',3,"In a devised piece, the ensemble builds ideas from each member's suggestions. This shows creativity as it relates to what?",
  "Self and ensemble",["Only the director","Only the audience","Only the stage manager"],"Creativity can be collective.")
H('c.2.B',3,"Which behavior supports creativity in an ensemble?",
  "Welcoming and building on others' ideas",["Rejecting every idea","Staying silent","Copying a video"],"Openness fuels creativity.")
H('c.2.C',3,"An actor uses a trembling pitch and halting rhythm to show nervousness. She is using what?",
  "Voice and diction to express feelings",["Costume","Props","Sound cue"],"Vocal choices express emotion.")
H('c.2.C',3,"Which vocal choice would best show authority?",
  "A steady pace with a firm, clear tone",["A mumble","A nervous giggle","A whisper only"],"Steady tone reads as confident.")
H('c.2.D',3,"An actor considers a character's job, age and relationships before deciding how she greets others. She is applying what?",
  "Physical, intellectual, emotional and social interactions to portray a believable character",["Random guesses","Lighting design","Scenic painting"],"Character choices reflect all dimensions.")
H('c.2.D',3,"Which choice makes a character more believable?",
  "Actions grounded in the character's wants and circumstances",["Ignoring the script","Acting without a goal","Copying another actor"],"Motivation grounds believability.")
H('c.2.E',3,"An actor communicates a character's secret anxiety only through posture and small gestures. She is developing what?",
  "Non-verbal physical technique",["A voice-over","A set model","A playbill"],"Non-verbal acting conveys inner life.")
H('c.2.E',3,"Which is a non-verbal way to show sadness on stage?",
  "Lowered shoulders and slow movement",["A loud laugh","A fast sprint","A cheerful dance"],"Posture communicates feeling.")
H('c.2.F',3,"A group devises a scene from a news headline, writes dialogue and refines it after peer notes. What are they doing?",
  "Creating, devising and refining an original scene",["Reciting a classic play","Ordering costumes","Counting seats"],"Devising builds new work from ideas.")
H('c.2.F',3,"Which step best refines an original monologue?",
  "Cutting unnecessary lines after a read-through",["Adding random words","Removing the ending","Ignoring feedback"],"Editing clarifies a piece.")
H('c.3.A',2,"Which practice is part of safe stagecraft?",
  "Wearing proper footwear and using tools correctly",["Running with scissors","Leaving cords across walkways","Skipping training"],"Safety habits protect the crew.")
H('c.3.A',2,"A technician coils cords and labels switches so others can find them. She is practicing what?",
  "Effective stagecraft habits",["Acting technique","Singing","Playwriting"],"Organization supports production.")
H('c.3.B',3,"A script set in the 1960s Civil Rights era requires technical designers to research what?",
  "Cultural, social and political context for sets and costumes",["Only lighting color","Ticket prices","Seating charts"],"Context informs design choices.")
H('c.3.B',3,"Why do designers read the script closely before building a set?",
  "To determine technical needs that fit the story",["To skip planning","To avoid collaboration","To shorten rehearsal"],"Script analysis guides design.")
H('c.3.C',3,"A director reads a script to find themes, character relationships and duties for each design role. She is doing what?",
  "Analyzing the script to determine artistic roles and needs",["Selling tickets","Ignoring the text","Painting a floor"],"Analysis assigns responsibilities.")
H('c.3.C',3,"Identifying the central theme of a play helps designers do what?",
  "Make choices that support the message",["Avoid reading","Change the plot","Eliminate scenes"],"Theme guides design.")
H('c.3.D',3,"A student serves as assistant director, running rehearsals and taking notes. She is performing what?",
  "A role in production decisions",["A spectator role","A random task","A ticket booth job"],"Roles shape production.")
H('c.3.D',3,"Which responsibility belongs to a sound designer?",
  "Creating music and sound effects that support the story",["Painting scenery","Writing dialogue","Directing actors"],"Sound design supports the show.")
H('c.3.E',3,"A crew member stays focused during a long tech rehearsal and solves a cue problem calmly. She is showing what?",
  "Responsibility, discipline and creative problem solving",["Carelessness","Distraction","Avoidance"],"Focus and calm solve problems.")
H('c.3.E',3,"A prop breaks right before an entrance. What shows creative problem solving?",
  "Substituting a similar item and informing the stage manager",["Canceling the show","Hiding the problem","Blaming a castmate"],"Quick fixes keep the show running.")
H('c.4.A',3,"The rise of television changed how audiences consumed drama. This is an example of what?",
  "A historical and cultural influence on theatre",["A set malfunction","A casting error","A costume trend only"],"Media shifts shaped theatre.")
H('c.4.A',3,"Analyzing how the Restoration reopened theatres after a ban involves which influence?",
  "Historical and political",["Weather","Geography only","Sports"],"Politics influenced theatre.")
H('c.4.B',3,"Characters in sitcoms often echo stock characters from comedy of earlier eras. This shows how theatre, television and film do what?",
  "Influence our daily lives and each other",["Avoid each other","Never overlap","Rely on silence"],"Forms borrow from each other.")
H('c.4.B',3,"A viral video inspires a school scene. This shows the role of media in what?",
  "Everyday life and artistic creation",["Isolation","Silence","Set storage"],"Media shape creative ideas.")
H('c.4.C',3,"A student compares the experience of seeing a play in person with watching it streamed. She is evaluating what?",
  "The impact of live theatre and electronic media",["Ticket pricing","Parking","Seat cushions"],"Live and recorded experiences differ.")
H('c.4.C',3,"Which factor is unique to live theatre?",
  "Actors and audience share the same space in real time",["Editing after the fact","Multiple takes","Special effects only"],"Live theatre is immediate.")
H('c.4.D',3,"A student researches how Japanese Kabuki and Noh influenced modern theatre. This is research into what?",
  "World drama and its influences",["Costume sizing","Ticket sales","Lighting grids"],"World theatre shapes practice.")
H('c.4.D',3,"Which playwright is a key figure in French comedy?",
  "Molière",["Sophocles","Eugene O'Neill","August Wilson"],"Molière wrote French comedies.")
H('c.4.E',3,"A student studies how African American playwrights shaped U.S. theatre. She is researching what?",
  "The multicultural heritage of U.S. drama",["Ancient Greek theatre","A single genre only","Costume history only"],"U.S. drama draws on many cultures.")
H('c.4.E',3,"Which playwright is known for the Pittsburgh Cycle of plays about African American life?",
  "August Wilson",["Arthur Miller","Neil Simon","Tennessee Williams"],"Wilson wrote the Pittsburgh Cycle.")
H('c.4.F',3,"The development of the Broadway musical is an example of what?",
  "A U.S. innovation in the performing arts",["A European import only","An ancient ritual","A silent film form"],"Musicals are an American innovation.")
H('c.4.F',3,"Which is a U.S. innovation in staging?",
  "The modern American musical's integration of song and story",["Greek chorus","Noh mask","Commedia scenario"],"Integrated musicals are American.")
H('c.5.A',2,"Choosing when to applaud at a formal event and when to stay silent reflects what?",
  "Audience etiquette suited to the performance",["Rude behavior","Random action","No awareness"],"Etiquette varies with context.")
H('c.5.A',2,"Which behavior fits an interactive, family-style theatre performance?",
  "Responding as invited by the performers",["Leaving mid-show","Texting aloud","Staying fully silent no matter what"],"Interactive shows invite participation.")
H('c.5.B',3,"A student analyzes how a play's design supports its message and then reflects on her own growth. She is doing what?",
  "Analyzing theatre as art and evaluating herself as a creative being",["Ignoring design","Skipping reflection","Copying another"],"Analysis and reflection build artistry.")
H('c.5.B',3,"Which question encourages self-evaluation as an artist?",
  "What choices did I make and what would I change?",["What time is lunch?","Who sits where?","How much is the ticket?"],"Reflection improves craft.")
H('c.5.C',3,"A student gives a peer feedback that names what worked, what confused her and one suggestion. This is ___.",
  "Constructive criticism",["Insulting remarks","Silence","Gossip"],"Balanced specific feedback helps.")
H('c.5.C',3,"A director gives notes after a run-through. How should actors respond?",
  "Listen, ask questions and apply the notes",["Argue with each note","Ignore them","Leave early"],"Receptivity improves performance.")
H('c.5.D',3,"A critic evaluates how a revival treats theme and character through staging choices. She is evaluating what?",
  "The treatment of artistic elements in a production",["Ticket revenue","Parking","Lobby design"],"Evaluation covers theme, character and setting.")
H('c.5.D',3,"Which sentence evaluates character treatment?",
  "The lead's slow breathing in act two revealed her inner conflict",["The seats were red","It was long","It was crowded"],"Specific observation about character.")
H('c.5.E',2,"A person who manages a theatre company's finances and marketing has which kind of career?",
  "Arts administration",["Wildlife biology","Plumbing","Mining"],"Administrators run arts organizations.")
H('c.5.E',2,"Teaching drama at a school is an example of what?",
  "Theatre education career",["An avocation only","A film credit","A set job"],"Teachers educate in theatre.")
H('c.5.F',3,"A student compiles scene footage, reviews and a reflective journal into a digital portfolio. She is using what?",
  "Technology to document and present theatre experiences",["A paper map","A coupon","A tuning fork"],"Portfolios present work.")
H('c.5.F',3,"A research project about a historical playwright helps a student do what?",
  "Present informed knowledge about theatre history",["Skip sources","Avoid presenting","Hide findings"],"Research supports presentation.")
H('c.5.G',3,"Skills from theatre like public speaking and teamwork help students in which setting?",
  "College and careers outside theatre",["Nowhere else","Only on stage","Only in shops"],"Theatre skills transfer.")
H('c.5.G',3,"Learning to take direction and meet deadlines in theatre is useful in what?",
  "Many professional workplaces",["Only acting jobs","No jobs","Only dance"],"Professional habits transfer.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_theatre2.jsonl'))

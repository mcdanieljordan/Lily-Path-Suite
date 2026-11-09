import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.315.', 1028, own='hs_theatre1.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',2,"During an ensemble scene, an actor fixes her attention on her partner's words and responds truthfully. Which theatre skill is she using?",
  "Listening and concentration",["Set painting","Ticket sales","Costume sewing"],"Listening and focus drive believable scenes.")
H('c.1.A',2,"Why is cooperation important in a theatre class?",
  "Productions depend on everyone working together",["Each person works alone","Cooperation slows rehearsals","Only the director matters"],"Theatre is collaborative.")
H('c.1.B',2,"Why do actors warm up before rehearsal?",
  "To prepare the body and voice and prevent injury",["To avoid rehearsing","To memorize lines","To skip costumes"],"Warm-ups ready the instrument.")
H('c.1.B',2,"Which activity is a typical vocal warm-up?",
  "Humming and lip trills",["Lifting scenery","Painting flats","Selling tickets"],"Humming and trills prepare the voice.")
H('c.1.C',2,"An actor performs an invisible rope-pulling action without speaking or props. This stage movement technique is ___.",
  "Mime",["Soliloquy","Monologue","Blocking only"],"Mime uses gesture to show objects and actions.")
H('c.1.C',2,"Laban movement analysis helps actors understand what?",
  "Qualities of effort such as weight, time and space",["Lighting cues","Costume fabrics","Set blueprints"],"Laban describes how movement is shaped.")
H('c.1.D',2,"Speaking with crisp consonants so that each word is understood is practicing good ___.",
  "Diction",["Blocking","Stage left","Cueing"],"Diction is clarity of speech.")
H('c.1.D',2,"Which technique helps an actor project without strain?",
  "Breathing from the diaphragm",["Yelling from the throat","Whispering all lines","Holding the breath"],"Support allows safe projection.")
H('c.1.E',3,"A student writes that her character is tall, impatient, clever and fearful of failure. She is describing the character's what?",
  "Physical, intellectual and emotional attributes",["Set pieces","Light cues","Ticket price"],"Character analysis covers traits.")
H('c.1.E',3,"Which is a social attribute of a character?",
  "Being the new student in a school",["Having brown eyes","Walking quickly","Speaking loudly"],"Social attributes relate to relationships and status.")
H('c.1.F',2,"The part of the stage closest to the audience is called ___.",
  "Downstage",["Upstage","Offstage","Backstage"],"Downstage is nearest the audience.")
H('c.1.F',2,"A written plan of actors' movements on stage is known as ___.",
  "Blocking",["Casting","Strike","Tech"],"Blocking sets movement.")
H('c.1.G',3,"If the lighting designer changes the color to blue, the mood of a scene may change. This shows what about theatre elements?",
  "They depend on each other",["They are unrelated","Only acting matters","Light is unimportant"],"Elements are interdependent.")
H('c.1.G',3,"Why must costumes, set and sound agree with the director's concept?",
  "So the production tells one unified story",["To increase budget","To confuse audiences","To shorten rehearsal"],"Unity requires cooperation of all elements.")
H('c.1.H',3,"Which job oversees the artistic vision of a production?",
  "Director",["Usher","Box office manager","Ticket scanner"],"Directors guide the vision.")
H('c.1.H',3,"The stage manager's role is to do what?",
  "Coordinate rehearsals and call cues during performances",["Design costumes","Write the play","Sell concessions"],"Stage managers run the show.")
H('c.1.I',2,"A good way to memorize lines is to do what?",
  "Repeat them aloud with the action in short sections",["Read once","Ignore them","Skip the hard parts"],"Chunking and repetition help.")
H('c.1.I',2,"Why is it helpful to learn cues along with your lines?",
  "It tells you when your line comes in",["It makes lines longer","It removes the need to rehearse","It changes the script"],"Cue lines trigger responses.")
H('c.1.J',2,"A basic rule of improvisation is to accept your partner's idea and add to it. This is often called ___.",
  "Yes, and",["No, but","Stop and think","Wait and see"],"Accepting and building is a core principle.")
H('c.1.J',2,"Which skill is most essential in an improvised scene?",
  "Listening to your scene partner",["Reading the script","Checking costumes","Counting seats"],"Improv depends on responding.")
H('c.1.K',2,"Before climbing a ladder on set, a student should do what?",
  "Check that it is stable and have a spotter",["Climb quickly","Skip checking","Use a broken ladder"],"Safety checks prevent falls.")
H('c.1.K',2,"Why should walkways backstage be kept clear?",
  "To prevent trips and falls in the dark",["To look neat for photos","To fit more props","To sell more tickets"],"Clear paths prevent accidents.")
H('c.2.A',2,"Using the voice safely means doing what?",
  "Using breath support and resting when hoarse",["Shouting all day","Whispering strain","Ignoring pain"],"Voice care prevents injury.")
H('c.2.A',2,"An actor with a sore ankle should do what before a stage fight rehearsal?",
  "Tell the director and avoid risky movement",["Hide it","Run harder","Jump from platforms"],"Honest communication keeps actors safe.")
H('c.2.B',3,"A student invents an original character with a unique walk and voice. She is showing what?",
  "Creativity in personal expression",["Copying","Avoiding choices","Silence"],"Creativity shapes personal choices.")
H('c.2.B',3,"Which statement best defines creativity in theatre?",
  "Making original choices to express ideas",["Repeating others exactly","Avoiding risk","Ignoring the script"],"Creativity means original expression.")
H('c.2.C',3,"An actor changes volume and pace to show fear during a monologue. She is using what?",
  "Voice to express thoughts and feelings",["Lighting","Set design","Ticket stubs"],"Voice conveys emotion.")
H('c.2.C',3,"Which vocal choice helps show an angry character?",
  "A sharper tone and faster pace",["A slow whisper only","No sound","A sleepy drawl"],"Vocal qualities show emotion.")
H('c.2.D',3,"An actor uses what she knows about a character's background and feelings to decide how to stand and speak. She is portraying a ___.",
  "Believable character",["Random role","Prop","Set"],"Awareness builds believability.")
H('c.2.D',3,"Which source helps an actor create a believable character?",
  "Observing real people and considering the character's goals",["Skipping the script","Memorizing a playbill","Painting the set"],"Observation and motivation inform choices.")
H('c.2.E',3,"An actor shows boredom without words by slumping and sighing. She is expressing a feeling through ___.",
  "Non-verbal physical technique",["Dialogue","Lighting","Stage tape"],"Body language conveys emotion.")
H('c.2.E',3,"Which is a non-verbal way to show surprise?",
  "A sudden step back with wide eyes",["A long speech","A costume change","A set strike"],"Physical choices show emotion.")
H('c.2.F',3,"A group writes a short scene about a lost phone, rehearses it and revises the ending after feedback. What are they doing?",
  "Creating and refining an original scene",["Reciting a published play","Painting a flat","Ordering tickets"],"Writing and revising are part of creation.")
H('c.2.F',3,"Which element makes a short monologue effective?",
  "A clear character with a want and a change",["Random words","No conflict","A copied speech"],"Wants and change create interest.")
H('c.3.A',2,"Which is a technical theatre skill?",
  "Operating a lighting board",["Memorizing a monologue","Singing harmony","Acting in a chorus"],"Light operation is technical.")
H('c.3.A',2,"Practicing technical theatre skills includes learning how to do what?",
  "Build and paint a simple set piece",["Memorize lines only","Direct every scene","Play the lead"],"Tech work includes building and painting.")
H('c.3.B',3,"A student wears safety glasses while cutting wood for a flat. She is doing what?",
  "Applying technical skills safely",["Ignoring rules","Taking risks","Skipping the task"],"Safety gear is part of tech skill.")
H('c.3.B',3,"Before operating a power saw in the shop, a student must do what?",
  "Get training and permission",["Guess how it works","Ask a friend to try","Use it without supervision"],"Equipment requires training.")
H('c.3.C',3,"A student is asked to design the sound for a short show, deciding music and effects. Which role is she performing?",
  "Designer",["Usher","Understudy","Critic"],"Designers create elements of the show.")
H('c.3.C',3,"The person who edits a filmed scene is performing what role?",
  "Editor",["Playwright","Dresser","Usher"],"Editors shape recorded work.")
H('c.3.D',3,"A student shows up on time, learns lines and solves a problem when a prop breaks. She is demonstrating what?",
  "Responsibility, discipline and creative problem solving",["Carelessness","Avoidance","Gossip"],"Professional habits support production.")
H('c.3.D',3,"What is a creative solution if a prop cup is missing during a scene?",
  "Use a similar item or adjust the action to continue",["Stop the show","Blame others","Leave the stage"],"Quick solutions keep scenes moving.")
H('c.4.A',3,"A play set in the Great Depression shows what about theatre?",
  "It can reflect life in a particular time and place",["It ignores history","It has no setting","It repeats news only"],"Plays reflect their setting.")
H('c.4.A',3,"Portraying a culture respectfully on stage requires what?",
  "Research and sensitivity",["Stereotypes","Guesswork","Ignoring facts"],"Accurate portrayal requires research.")
H('c.4.B',3,"Greek theatre used masks and a chorus partly because of the huge outdoor spaces. This relates to which influence?",
  "Cultural and historical conditions",["Modern lighting","Television","Cell phones"],"Context shapes theatrical conventions.")
H('c.4.B',3,"The Elizabethan stage influenced Shakespeare's plays. This is an example of what?",
  "Historical influence on theatre",["A modern invention","A film effect","A game rule"],"Playhouses shaped writing.")
H('c.4.C',3,"How did the invention of film change theatre?",
  "It offered new competition and storytelling ideas",["It ended stage plays","It removed actors","It banned costumes"],"Media influenced theatre.")
H('c.4.C',3,"Streaming a live play online allows what?",
  "Audiences far away to watch performances",["No audience","Only local viewing","Fewer actors"],"Electronic media extends reach.")
H('c.4.D',3,"Which ancient culture is credited with developing early drama in Athens?",
  "Greek",["Roman only","Inuit","Aztec"],"Greek drama began in Athens.")
H('c.4.D',3,"Which playwright wrote Hamlet?",
  "William Shakespeare",["Sophocles","Molière","Anton Chekhov"],"Shakespeare wrote Hamlet.")
H('c.4.E',3,"A play by Lorraine Hansberry, A Raisin in the Sun, is part of which tradition?",
  "United States multicultural drama",["Ancient Greek drama","Japanese noh","Commedia dell'arte"],"Hansberry was an African American playwright.")
H('c.4.E',3,"Which American playwright is known for Death of a Salesman?",
  "Arthur Miller",["Neil Simon","August Wilson","Sam Shepard"],"Miller wrote Death of a Salesman.")
H('c.4.F',3,"The American musical grew from various traditions. This is an example of a United States contribution to what?",
  "The performing arts",["Architecture only","Sports only","Cooking only"],"Musical theatre is an American innovation.")
H('c.4.F',3,"Which is a U.S. contribution to the performing arts?",
  "Broadway musical theatre",["Kabuki","Noh","Greek chorus"],"Broadway musicals are American.")
H('c.5.A',2,"During a live performance, audience members should do what?",
  "Silence phones and watch quietly",["Take calls","Talk loudly","Film with flash"],"Etiquette respects performers.")
H('c.5.A',2,"At a formal theatre, applause is appropriate at what moment?",
  "At the end of the show or when the cast takes a bow",["During quiet dialogue","In the middle of a monologue","While actors exit"],"Applause follows conventions.")
H('c.5.B',3,"A student reflects in a journal about what she learned and where she grew creatively. She is doing what?",
  "Evaluating herself as a creative being",["Avoiding reflection","Copying others","Ignoring work"],"Reflection builds artistic identity.")
H('c.5.B',3,"Why is theatre considered an art form?",
  "It expresses ideas through creative performance",["It is a game","It requires no skill","It is only entertainment"],"Art conveys meaning creatively.")
H('c.5.C',3,"A peer gives helpful feedback by naming a strength and a specific suggestion. This is ___.",
  "Constructive criticism",["Rude comments","Silence","Gossip"],"Constructive means specific and kind.")
H('c.5.C',3,"When receiving criticism of your scene, you should do what?",
  "Listen openly and consider how to improve",["Argue","Ignore everything","Leave the room"],"Open listening supports growth.")
H('c.5.D',3,"After seeing a school play, a student writes that the lighting shift in act two sharpened the tension. This is a ___.",
  "Specific observation in a review",["Vague opinion","Gossip","Prop list"],"Precise detail supports evaluation.")
H('c.5.D',3,"Which is the most useful sentence in a theatre review?",
  "The actor's pacing built suspense in the confrontation scene",["It was good","I liked it","It was long"],"Specifics help readers.")
H('c.5.E',3,"A student writes about how a film's camera angles shaped a character's power. She is evaluating what?",
  "Media with precise observations",["A rumor","A ticket","Her lunch"],"Evaluation uses specific detail.")
H('c.5.E',3,"Which detail strengthens an evaluation of a TV drama?",
  "How editing and sound created tension",["The channel number","The time slot only","The commercial breaks"],"Technical details support analysis.")
H('c.5.F',2,"Which job is a career in theatre education?",
  "Drama teacher",["Pilot","Welder","Surveyor"],"Teachers train students in theatre.")
H('c.5.F',2,"A person who manages a theatre's budget and schedules works in what field?",
  "Arts administration",["Plumbing","Forestry","Mining"],"Arts administrators handle operations.")
H('c.5.G',3,"A student builds an online portfolio with photos and a journal of her productions. She is using what?",
  "Technology to document her experiences",["A paper airplane","A coupon","A script alone"],"Portfolios document growth.")
H('c.5.G',3,"Which is a good use of a theatre journal?",
  "Recording rehearsals, goals and reflections",["Hiding scripts","Drawing only","Storing coupons"],"Journals track development.")
H('c.5.H',3,"Public speaking learned in theatre helps a student succeed in which career?",
  "Sales or law",["Never in sales","Only in acting","Only in dance"],"Theatre skills transfer to many careers.")
H('c.5.H',3,"Teamwork learned in theatre helps students in college because it builds what?",
  "Collaboration skills",["Isolation","Avoidance","Distraction"],"Collaboration is valued everywhere.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_theatre1.jsonl'))

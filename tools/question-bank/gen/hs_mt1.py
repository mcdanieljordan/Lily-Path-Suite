import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.319.', 1032, own='hs_mt1.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',2,"Before a musical rehearsal, the cast stretches, hums scales and walks through simple dance steps. This routine prepares what?",
  "Voice, body and dance skills for performing",["The ticket booth","The costume shop","The program order"],"Musical theatre warm-ups cover singing, acting and dance.")
H('c.1.A',2,"Which vocal warm-up is useful before singing in a musical?",
  "Sirens and gentle lip trills",["Shouting over a crowd","Singing at full volume cold","Whispering only"],"Gentle exercises prepare the voice.")
H('c.1.B',2,"A performer uses small, expressive hand gestures to tell a story without speaking. This skill is ___.",
  "Pantomime",["Soliloquy","Aria","Recitative"],"Pantomime tells a story through gesture.")
H('c.1.B',2,"Which dance genre is often featured in a musical's tap number?",
  "Tap",["Square dancing","Folk waltz only","Marching"],"Tap dance is common in musicals.")
H('c.1.C',3,"A performer shifts from speaking a line to singing the next without changing the character's emotional intention. She is using what?",
  "Acting technique across spoken dialogue and song",["Costume design","Lighting design","Box office skills"],"Acting links song and dialogue.")
H('c.1.C',3,"Why should an actor play an objective during a song?",
  "A clear want makes the song feel like part of the story",["It makes the song longer","It avoids singing","It replaces the melody"],"Objectives motivate musical moments.")
H('c.1.D',2,"At a professional audition for a musical, performers are often asked to prepare what?",
  "A song, sometimes a monologue and a dance combination",["A speech about weather","A lighting plot","A set design"],"Auditions often include song, acting and dance.")
H('c.1.D',2,"What should an auditioner bring to a professional musical theatre audition?",
  "A headshot, resume and prepared music",["A ticket stub","Pajamas","A set model"],"Auditions require professional materials.")
H('c.1.E',3,"A student compares how a stage musical builds a story with songs to how a film musical may use editing and camera work. She is comparing what?",
  "Dramatic structure in stage and film musicals",["Seat prices","Parking","Posters"],"Structure differs between media.")
H('c.1.E',3,"Which tool can a film musical use that a stage musical cannot?",
  "Close-up camera shots",["Live orchestra","Live applause","An intermission"],"Film uses camera framing.")
H('c.1.F',2,"The area of the stage nearest the audience is called ___.",
  "Downstage",["Upstage","Wings","Orchestra pit"],"Downstage is closest to the audience.")
H('c.1.F',2,"The group of singers who perform together in large ensemble numbers is called the ___.",
  "Chorus",["Pit","Crew","Cast crew"],"The chorus supports principals in group numbers.")
H('c.1.G',3,"In a musical, the orchestra, lighting, choreography and set must all support the same story. This shows what?",
  "Theatrical elements depend on one another",["Elements work alone","Only singing matters","Design is optional"],"All elements are interdependent.")
H('c.1.G',3,"If a dance number runs long, what else may need to change?",
  "Music, lighting cues and transitions",["Only the program","Only tickets","Nothing"],"Changes ripple through the show.")
H('c.2.A',2,"Which practice protects the voice during a long rehearsal period for a musical?",
  "Hydrating and resting the voice",["Singing through pain","Yelling at the group","Skipping rest days"],"Vocal care prevents injury.")
H('c.2.A',2,"Why wear proper shoes and warm up before a dance number?",
  "To prevent injuries to feet, ankles and legs",["To look taller","To be louder","To avoid memorizing"],"Preparation and footwear prevent injury.")
H('c.2.B',2,"A student adds her own gesture to show a character's excitement in a song. She is expressing what?",
  "Creativity in personal expression",["Copying exactly","Avoiding choices","Ignoring the song"],"Creativity is personal expression.")
H('c.2.B',2,"What does creativity in musical theatre include?",
  "Making original choices in singing, acting and movement",["Repeating others exactly","Avoiding risks","Skipping rehearsal"],"Creative choices personalize performance.")
H('c.2.C',3,"A student notes that the lead in a comic operetta is played with exaggeration, while the lead in a dramatic musical is played with realism. She is recognizing what?",
  "Characterization in musicals of different genres",["A costume error","A staging mistake","A music cue"],"Genre shapes characterization.")
H('c.2.C',3,"Which detail helps an actor understand a character in a musical?",
  "The lyrics and dialogue that reveal wants and feelings",["The playbill ads","The seat numbers","The lobby layout"],"Text reveals character.")
H('c.2.D',3,"A singer opens her mouth wide and directs the sound forward to project a clear tone. She is using proper ___.",
  "Vocal placement and production",["Costume placement","Light placement","Stage placement"],"Placement affects tone.")
H('c.2.D',3,"Breath support in singing comes mainly from where?",
  "The diaphragm and lower ribs",["The shoulders","The jaw","The forehead"],"Support is from the diaphragm.")
H('c.2.E',3,"An actor reads the lyrics aloud as a monologue to understand meaning before singing. She is interpreting lyrics for what?",
  "Characterization and vocalization",["Set painting","Lighting cues","Ticket sales"],"Lyrics reveal character and guide singing.")
H('c.2.E',3,"A choreographer asks the ensemble to show the lyric 'rushing toward the future' with a forward-driving phrase. This is interpreting lyrics in a choreographed ___.",
  "Dance",["Costuming","Marketing","Ticketing"],"Movement can express lyrics.")
H('c.3.A',2,"Which action shows safe use of technical elements in a musical?",
  "Checking that microphones and cables are secured and out of the way",["Leaving cords across the stage","Skipping safety checks","Climbing without a spotter"],"Safe handling prevents accidents.")
H('c.3.A',2,"Why is it important to follow safety rules around moving scenery during a musical?",
  "Fast set changes can cause injuries if mishandled",["Scenery is soft","Safety is optional","There is no risk"],"Scenic movement needs caution.")
H('c.3.B',3,"The person who leads the singers and orchestra, teaching the music to the cast, is the ___.",
  "Musical director",["Choreographer","Stage manager","Costume designer"],"The musical director prepares the music.")
H('c.3.B',3,"The choreographer is responsible for what?",
  "Creating and teaching the dance movement",["Teaching the harmony","Managing tickets","Painting the set"],"Choreographers design dance.")
H('c.3.C',3,"A musical's production plan might include rehearsal schedules, technical designs and blocking. This planning helps do what?",
  "Coordinate all production elements",["Avoid work","Cut the show","Remove actors"],"Plans organize production.")
H('c.3.C',3,"Why is a costume plot useful in a musical production?",
  "It tracks each costume piece and quick change for every performer",["It lists ticket buyers","It plans parking","It selects music"],"Costume plots track costumes.")
H('c.3.D',3,"A cast member sings in the chorus, learns choreography and supports the leads during a scene. She is collaborating to do what?",
  "Tell a story through live musical theatre",["Avoid performing","Work alone","Skip rehearsals"],"Ensembles collaborate to tell a story.")
H('c.3.D',3,"Which action shows collaboration in a musical cast?",
  "Learning harmonies together and giving each other notes",["Ignoring others","Leaving rehearsal early","Refusing blocking"],"Collaboration builds the show.")
H('c.4.A',3,"The popularity of vaudeville and operetta influenced early American musicals. This is an example of what?",
  "Historical and cultural influences on musical theatre",["A stage injury","A casting mistake","A set change"],"Earlier forms shaped musicals.")
H('c.4.A',3,"Jazz and swing influenced the sound of many musicals in the 1920s and 1930s. This is a ___ influence.",
  "Cultural",["Medical","Geographic only","Culinary"],"Popular music styles influence musicals.")
H('c.4.B',3,"Show Boat, premiering in 1927, is often cited as a landmark in American musical theatre because it did what?",
  "Integrated story, music and serious themes",["Removed songs","Removed actors","Used only dance"],"It integrated story and song.")
H('c.4.B',3,"Which describes the musical as a uniquely American art form?",
  "It blended many cultural traditions into a new theatrical form",["It imitated one European form only","It ignored music","It had no story"],"The American musical combined traditions.")
H('c.4.C',3,"The Golden Age of musical theatre in the 1940s and 1950s is known for productions that did what?",
  "Fully integrated songs, dance and drama",["Dropped dance","Avoided story","Had no orchestra"],"Integrated musicals defined that era.")
H('c.4.C',3,"The rock musical emerged in the 1960s as a development in what?",
  "Musical theatre history and culture",["Cooking","Sports","Architecture"],"Rock reflected changing culture.")
H('c.4.D',3,"A British musical that becomes a hit in New York and Tokyo shows musical theatre as an ___.",
  "International art form",["Local custom only","Dead art","Silent film"],"Musicals travel worldwide.")
H('c.4.D',3,"Which London and Broadway hit helped spread musical theatre internationally?",
  "The Phantom of the Opera",["Our Town","A Doll's House","Hamlet"],"Phantom was a global hit.")
H('c.4.E',3,"A musical set in the Depression era shows musical theatre as what?",
  "A reflection of life in a particular time and place",["Unrelated to history","Only fantasy","A news report"],"Musicals can reflect their settings.")
H('c.4.E',3,"Which musical reflects immigrant life in New York's West Side during the 1950s?",
  "West Side Story",["Cats","Oklahoma!","Annie"],"West Side Story is set among urban rival groups.")
H('c.4.F',3,"Film adaptations of stage musicals show the influence of what?",
  "Musical theatre on film and television",["Cooking shows","Sports","Weather reports"],"Forms influence each other.")
H('c.4.F',3,"Live televised musicals show how musical theatre influences what?",
  "Television programming",["Architecture","Agriculture","Surveying"],"Television adapts the musical.")
H('c.5.A',2,"During a musical, an audience member should do what?",
  "Silence phones and applaud at appropriate times",["Sing along loudly","Take flash photos","Talk through songs"],"Etiquette respects performers.")
H('c.5.A',2,"When is applause especially appropriate at a musical?",
  "After a song ends or at the curtain call",["During a quiet monologue","During an orchestral hush","While actors speak"],"Applause fits musical moments.")
H('c.5.B',3,"A student reflects on how singing, acting and dancing together shaped her growth as a performer. She is doing what?",
  "Evaluating herself as a creative being",["Avoiding reflection","Copying others","Ignoring feedback"],"Self-evaluation supports growth.")
H('c.5.B',3,"Why is musical theatre called an art form?",
  "It expresses ideas through combined music, drama and dance",["It is only a hobby","It needs no skill","It has no purpose"],"The combination creates art.")
H('c.5.C',3,"A peer says, 'Your phrasing in the second verse made the lyric clearer; maybe breathe earlier before the high note.' This is ___.",
  "Constructive criticism",["Insult","Silence","Gossip"],"Specific and helpful feedback.")
H('c.5.C',3,"When receiving feedback on your song, you should do what?",
  "Listen openly and try the suggestion",["Argue","Ignore it","Leave"],"Openness improves performance.")
H('c.5.D',3,"A critic writes that the choreography in the finale reinforced the song's joy and the ensemble stayed in tune. This review includes what?",
  "Precise, specific observations",["Vague opinion","Gossip","Prop list"],"Specific details support evaluation.")
H('c.5.D',3,"Which review statement is most specific?",
  "The harmonies in the trio blended well and the staging clarified the plot",["It was good","I liked it","It was long"],"Specific observations help readers.")
H('c.5.E',2,"A person who accompanies rehearsals and plays the music for a musical works as a ___.",
  "Rehearsal pianist or accompanist",["Lighting operator","Ticket seller","Costumer"],"Accompanists support rehearsals.")
H('c.5.E',2,"Which job is available in musical theatre?",
  "Choreographer",["Welder","Pilot","Surveyor"],"Choreographers work in musicals.")
H('c.5.F',3,"Public speaking and teamwork gained in musical theatre help students in which future setting?",
  "College and careers outside theatre",["Nowhere","Only theatres","Only stage"],"Skills transfer.")
H('c.5.F',3,"How might singing in an ensemble help in a business career?",
  "It builds listening, collaboration and confidence",["It prevents learning","It removes teamwork","It avoids deadlines"],"Collaboration skills transfer.")
H('c.5.G',3,"A student makes a slideshow about the history of musical theatre with clear headings and images. She is practicing what?",
  "Presenting information clearly and coherently with technology",["Disorganization","Silence","Copying"],"Clear presentation matters.")
H('c.5.G',3,"Which tool helps a student present research about musicals?",
  "Presentation software",["A hammer","A stopwatch","A thermometer"],"Slideshows aid presentation.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_mt1.jsonl'))

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.311.', 1024, own='hs_music2.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',3,"A student listens to two professional recordings of the same piece, one orchestral and one for band, and notes similarities and differences. What is she doing?",
  "Comparing and contrasting exemplary musical examples",["Tuning an instrument","Selling tickets","Copying a score"],"Comparison uses recordings as models.")
H('c.1.A',3,"Which listening task best compares two live performances?",
  "Noting differences in tone, balance and interpretation",["Counting the audience","Rating the lobby","Naming the printer"],"Compare musical qualities.")
H('c.1.B',3,"A singer reads a melody in solfège, then compares it with the harmony part sung by another section. What is she comparing?",
  "Melodic and harmonic parts",["Costume colors","Ticket sections","Stage doors"],"She contrasts melody with harmony.")
H('c.1.B',3,"Which part usually carries the main tune in a choral piece?",
  "The melody",["The accompaniment only","The silence","The page number"],"The melody is the featured line.")
H('c.1.C',3,"The interval from C up to G is a ___.",
  "Perfect fifth",["Major second","Minor third","Octave"],"C to G spans five letter names.")
H('c.1.C',3,"A minor triad differs from a major triad because its third is what?",
  "Lowered by a half step",["Raised by a whole step","Removed","Doubled"],"Minor chords have a minor third.")
H('c.1.D',3,"Compare 3/4 and 6/8. What is a key difference?",
  "3/4 is simple meter and 6/8 is compound meter",["Both are asymmetrical","3/4 has no beat","6/8 has two sharps"],"Simple meters divide the beat in two; compound in three.")
H('c.1.D',3,"A student counts 1-la-li, 2-la-li in a measure. This is a counting system for which meter?",
  "Compound",["Simple duple","Silent","Free"],"Three subdivisions per beat signal compound meter.")
H('c.1.E',3,"A song that follows A-B-A-C-A form is a ___.",
  "Rondo",["Binary","Ternary","Strophic"],"A rondo returns to the A theme between contrasting sections.")
H('c.1.E',3,"Binary form has how many main sections?",
  "Two",["Four","Five","One"],"Binary is A-B.")
H('c.1.F',3,"Hearing the trumpets cover the clarinets in a band piece is a problem of what?",
  "Balance",["Key signature","Rhythm","Notation"],"Balance is the relative volume of parts.")
H('c.1.F',3,"When all voices in a choir sound as one unified tone, they have achieved good ___.",
  "Blend",["Rests","Tempo","Articulation"],"Blend is unity of tone color.")
H('c.1.G',3,"Comparing a march and a waltz mainly contrasts which element?",
  "Meter and rhythmic feel",["Paper size","Concert dates","Stage lights"],"Marches and waltzes use different meters.")
H('c.1.G',3,"The overall pitch center around which a piece is organized is its what?",
  "Key",["Rest","Seat","Page"],"Key establishes the tonal home.")
H('c.1.H',2,"What helps prevent vocal strain during a long rehearsal?",
  "Drinking water and resting the voice when needed",["Shouting over the group","Whispering constantly","Skipping warm-ups"],"Hydration and rest protect the voice.")
H('c.1.H',2,"A brass player feels tension in her shoulders. Which adjustment is best?",
  "Relax the shoulders and check posture",["Press harder","Hold her breath","Slouch deeply"],"Relaxed body mechanics prevent injury.")
H('c.2.A',3,"A measure in 6/8 time may contain which grouping of eighth notes?",
  "Two groups of three",["Four groups of two","Five groups of one","Seven groups of three"],"6/8 is typically felt in two beats.")
H('c.2.A',3,"A student writes a rhythm using an asymmetrical pattern of 2+2+3. Which meter is it?",
  "7/8",["4/4","2/4","3/4"],"2+2+3 equals seven eighths.")
H('c.2.B',2,"What does allegro tell a performer?",
  "Play at a fast, lively tempo",["Play very softly","Pause","Play slowly"],"Allegro is quick.")
H('c.2.B',2,"A line above a note telling the player to stress and sustain it is called what?",
  "A tenuto marking",["A rest","A clef","A repeat bar"],"Tenuto means held.")
H('c.3.A',3,"A player who keeps her tone full, focused and in style as pieces grow harder is showing what?",
  "Increasingly mature sound",["Weak tone","Careless playing","Silence"],"Tone matures with technique.")
H('c.3.A',3,"What most improves a flutist's tone color?",
  "Steady air support and a stable embouchure",["Shallow breaths","Tight shoulders","Rushing"],"Air and embouchure shape tone.")
H('c.3.B',3,"Which posture best supports a seated clarinetist's breathing?",
  "Sitting tall with feet flat",["Slumping forward","Crossing legs tightly","Leaning back"],"Open posture allows deep breaths.")
H('c.3.B',3,"A choir member refines her breathing so she can finish long phrases. She is refining what?",
  "A psychomotor skill",["A ticket sale","A program note","A seating chart"],"Breath control is physical technique.")
H('c.3.C',3,"A drummer practices with a metronome set slowly and gradually increases the tempo. She is building what?",
  "Rhythmic accuracy",["Dynamics only","A new key","A cadenza"],"The metronome keeps tempo steady.")
H('c.3.C',3,"Which habit causes uneven rhythm?",
  "Rushing short notes",["Counting aloud","Using a metronome","Subdividing"],"Rushing distorts note values.")
H('c.3.D',3,"A piece has three flats in the key signature. Which notes are flatted?",
  "B, E and A",["F, C and G","D and G","None"],"The order of flats is B, E, A, D, G.")
H('c.3.D',3,"When a piece changes from major to minor mode, what usually changes?",
  "Some scale degrees are lowered and the mood darkens",["The tempo vanishes","The clef disappears","The notes stop"],"Mode changes interval patterns.")
H('c.3.E',3,"A trombonist adjusts her slide to match the section's pitch. She is working on what?",
  "Intonation",["Meter","Notation","Seating"],"Matching pitch is intonation.")
H('c.3.E',3,"Where should a singer breathe in a phrase?",
  "At punctuation or musical rests where the sense allows",["Mid-word","Randomly","Never"],"Breaths follow phrase shape.")
H('c.3.F',3,"A student composes a short piece for her own instrument within her technical ability. This reflects what?",
  "Creating music at an appropriate level of difficulty",["Copying a hymn","Buying sheet music","Ignoring range"],"Composition fits the player's level.")
H('c.3.F',3,"Why record an original phrase after writing it?",
  "To hear it and evaluate whether it works",["To avoid revising","To skip notation","To erase it"],"Recording supports revision.")
H('c.4.A',3,"A sight reader keeps a warm, controlled tone even on an unfamiliar piece. This shows what?",
  "Increasingly mature sound while sight reading",["Careless reading","Memorization only","Hesitation"],"Tone remains consistent.")
H('c.4.A',3,"Which step helps maintain tone while sight reading?",
  "Breathing deeply and keeping a relaxed embouchure",["Holding tension","Staring at the floor","Rushing every line"],"Technique supports tone.")
H('c.4.B',3,"A cellist sight reads while keeping her left hand relaxed and bow arm balanced. She is applying what?",
  "Psychomotor and kinesthetic skills",["Program notes","Music history","Concert dress"],"Physical technique supports reading.")
H('c.4.B',3,"Sight reading with tension in the neck will most likely cause what?",
  "Poor tone and fatigue",["Better intonation","Perfect rhythm","Faster tempo only"],"Tension hurts performance.")
H('c.4.C',3,"While sight reading, a student scans for slurs and accents before starting. She is preparing what?",
  "Correct articulation",["Costume choices","Audience seating","Ticket pricing"],"Articulation markings guide performance.")
H('c.4.C',3,"Which method helps count a tricky rhythm in sight reading?",
  "Speaking syllables such as 1 e & a",["Guessing","Skipping the measure","Ignoring the beat"],"Counting syllables clarifies rhythm.")
H('c.4.D',3,"A piece modulates from G major to D major. What should a sight reader watch for?",
  "A new key signature or added accidentals",["A new title","A different composer","Page turns only"],"Key changes alter notes.")
H('c.4.D',3,"When mode changes from major to minor mid-piece, a sight reader should do what?",
  "Adjust to the new accidentals and tonal center",["Ignore the change","Stop playing","Play only rests"],"Mode changes require attention.")
H('c.4.E',3,"Before singing a new melody, a student labels the first notes with numbers 1-3-5. She is using what?",
  "A melodic reading system",["A rhythm chart","A tuner","A bar line"],"Scale-degree numbers aid reading.")
H('c.4.E',3,"Which is a melodic reading system?",
  "Solfège",["Metronome","Dynamics","Tempo"],"Solfège labels pitches by syllable.")
H('c.4.F',3,"A sight reader follows crescendo markings and shapes phrases while reading. She is applying what?",
  "Dynamics and phrasing",["Key changes only","Rests only","Clefs only"],"She interprets expressive markings.")
H('c.4.F',3,"What should a sight reader do at a phrase marking?",
  "Shape the line with direction and a natural release",["Play every note equally","Stop abruptly","Play louder always"],"Phrasing shapes the music.")
H('c.4.G',3,"A singer uses tall, rounded vowels so a chord rings in tune while sight reading. She is working on what?",
  "Accurate intonation",["Meter","Notation","Tempo"],"Vowel shape affects pitch.")
H('c.4.G',3,"Listening to the bass line helps the ensemble tune because the bass provides what?",
  "A foundation for the harmony",["The meter","The lyrics","The tempo only"],"Harmony builds from the bass.")
H('c.5.A',3,"A student contrasts spirituals with Renaissance madrigals. She is comparing music by what?",
  "Genre, culture and historical period",["Instrument price","Concert attendance","Seat numbers"],"Comparison covers context.")
H('c.5.A',3,"Which pair of styles differs mainly in culture of origin?",
  "Gamelan and bluegrass",["Two C majors","Two quarter notes","Two bar lines"],"They come from different cultures.")
H('c.5.B',2,"A marching band performing at a football game shows music used for what?",
  "Community spirit and entertainment",["Weather forecasting","Cooking","Surveying"],"Music unites communities.")
H('c.5.B',2,"National anthems are an example of music used to express what?",
  "Shared identity",["Math facts","Recipes","Rainfall"],"Anthems express national identity.")
H('c.5.C',3,"Studying the physics of vibrating strings connects music with what subject?",
  "Science",["Dance only","Painting only","Gym only"],"Acoustics is science.")
H('c.5.C',3,"Setting a poem to music connects music with what subject?",
  "English language arts",["Chemistry","Woodworking","Geometry only"],"Text setting links to literature.")
H('c.5.D',2,"A person who teaches band at a high school has a music ___.",
  "Vocation",["Avocation","Hobby only","Fine"],"Teaching is a career.")
H('c.5.D',2,"Which is a music-related vocation?",
  "Recording studio producer",["Dishwasher only","Lifeguard only","Painter's helper"],"Production is a music career.")
H('c.5.E',3,"Using software to correct pitch in a recording shows how technology affects what?",
  "How music is produced",["Gravity","Weather","Taxes"],"Technology changes production.")
H('c.5.E',3,"Using someone else's recording in a video without permission raises what concern?",
  "Copyright and ethical use",["Tuning","Rhythm","Meter"],"Using music requires permission.")
H('c.5.F',3,"A student creates a recording and résumé of her musical experience for a scholarship audition. She is using what?",
  "Tools for college and career preparation",["A key signature","A fermata","A rest"],"Portfolios support auditions.")
H('c.5.F',3,"Which is a useful college-prep tool for a musician?",
  "A performance portfolio",["A coupon","A parking pass","A seating chart"],"A portfolio shows skills.")
H('c.6.A',2,"As an audience member at a recital, you should do what?",
  "Silence your phone and stay quiet during the music",["Take calls","Talk to neighbors","Walk across the stage"],"Etiquette respects the performers.")
H('c.6.A',2,"As a performer, what shows concert etiquette?",
  "Bowing or acknowledging applause with courtesy",["Rolling your eyes","Leaving before the end","Texting onstage"],"Courtesy shows professionalism.")
H('c.6.B',3,"A class writes criteria for judging balance, blend and intonation in a choir performance. This is what?",
  "Designing criteria for informed judgments",["Random guessing","Copying a score","Skipping evaluation"],"Criteria guide evaluation.")
H('c.6.B',3,"Which evaluation applies criteria well?",
  "The altos blended nicely but the tempo dragged in the second verse",["It was okay","Boring","I hate it"],"Specific evidence supports judgments.")
H('c.6.C',3,"A student sets monthly goals and checks them against recordings of her playing. She is using what?",
  "A process for self-evaluation",["A ticket log","A costume list","A seating chart"],"Goals and recordings support growth.")
H('c.6.C',3,"Which tool supports personal artistic improvement?",
  "A practice journal",["A coupon book","A bus map","A menu"],"Journals track progress.")
H('c.6.D',3,"A student listens to a professional recording and compares her section's blend to it. She is doing what?",
  "Evaluating performance against an exemplary model",["Ignoring quality","Avoiding listening","Skipping practice"],"Comparison with models guides growth.")
H('c.6.D',3,"After comparing to an exemplary model, what is a good next step?",
  "Set a specific goal and rehearse it",["Quit","Blame others","Ignore the difference"],"Evaluation leads to goals.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_music2.jsonl'))

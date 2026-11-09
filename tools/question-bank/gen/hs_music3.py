import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.312.', 1025, own='hs_music3.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',3,"A student attends a live concert and also streams a professional recording, then judges which performance best shows phrasing and balance. She is doing what?",
  "Evaluating exemplary musical examples",["Printing programs","Selling tickets","Tuning a piano"],"She judges models against criteria.")
H('c.1.A',3,"Which statement is an evaluation of a recording?",
  "The strings shaped the phrase with a clear dynamic arc",["The cover is red","It is track four","It was released on a Friday"],"Evaluation addresses musical qualities.")
H('c.1.B',3,"A single unaccompanied melody with no harmony has which texture?",
  "Monophony",["Polyphony","Homophony","Heterophony only"],"Monophony is one melodic line.")
H('c.1.B',3,"A melody with chordal accompaniment has which texture?",
  "Homophony",["Monophony","Silence","Rhythm only"],"Homophony is melody plus chords.")
H('c.1.C',3,"Compare a major seventh chord with a major triad. What is the difference?",
  "The seventh chord adds a fourth pitch a seventh above the root",["It has fewer notes","It has no root","It lacks a third"],"Seventh chords add a fourth tone.")
H('c.1.C',3,"An augmented fourth interval contains how many half steps?",
  "Six",["Three","Eight","Eleven"],"The tritone spans six half steps.")
H('c.1.D',3,"Compare 5/4 and 4/4. What distinguishes 5/4?",
  "Five beats per measure, often grouped unevenly",["Four beats per measure","Three beats per measure","No pulse at all"],"5/4 is an asymmetrical meter.")
H('c.1.D',3,"Syncopation is best described as what?",
  "Emphasis placed on normally weak beats or off-beats",["Constant silence","Equal accents on every beat","Gradual slowing"],"Syncopation shifts accents.")
H('c.1.E',3,"A movement with exposition, development and recapitulation uses which form?",
  "Sonata-allegro",["Rondo","Binary","Strophic"],"Sonata-allegro has three main sections.")
H('c.1.E',3,"How does ternary form differ from rondo form?",
  "Ternary has three sections, while a rondo returns to its theme several times",["Ternary has no repeats","Rondo has two notes","They are identical"],"A rondo's refrain recurs.")
H('c.1.F',3,"A conductor asks the horns to play softer so the melody in the oboes can be heard. She is adjusting what?",
  "Balance",["Key","Notation","Meter"],"Balance is the relative volume among parts.")
H('c.1.F',3,"Blend is achieved when instruments match what?",
  "Tone color, attack and dynamic level",["Costume colors","Seat height","Page numbers"],"Matching these qualities unifies sound.")
H('c.1.G',3,"A work for solo voices and orchestra with recitatives and arias that tells a staged story is an ___.",
  "Opera",["Motet","Cantata","Rondo"],"Opera combines drama and music.")
H('c.1.G',3,"Zydeco music is associated with which region?",
  "Southwest Louisiana",["Northern Siberia","Southern Argentina","Central Australia"],"Zydeco comes from Creole communities of Louisiana.")
H('c.1.H',3,"Contrasting two pieces' use of imitation among parts compares which element?",
  "Texture",["Seat count","Program length","Hall acoustics only"],"Imitation among voices is a textural feature.")
H('c.1.H',3,"The pitch center and its major or minor scale form a piece's what?",
  "Tonality",["Tempo","Fermata","Bar line"],"Tonality organizes pitch.")
H('c.1.I',2,"Frequent exposure to very loud rehearsals without protection may cause what?",
  "Permanent hearing damage",["Better pitch","Stronger lungs","Improved tone"],"Noise-induced hearing loss is preventable.")
H('c.1.I',2,"Which practice habit supports healthy body mechanics?",
  "Taking short breaks and stretching during long sessions",["Playing without rest","Holding tension","Ignoring pain"],"Rest and stretching prevent strain.")
H('c.2.A',3,"A student transcribes a melody she hears into notation by writing pitch and rhythm. What is she using?",
  "Skills for reading and notating melody and rhythm",["A conductor's baton","A ticket stub","A stage plot"],"Notation records pitch and rhythm.")
H('c.2.A',3,"Which element must a written melody show besides pitch?",
  "Rhythm",["Color","Smell","Weight"],"Melody notation includes durations.")
H('c.2.B',3,"The term cantabile instructs a performer to play how?",
  "In a singing style",["Very fast","Very short","Silently"],"Cantabile means songlike.")
H('c.2.B',3,"What does the marking rit. tell a player to do?",
  "Gradually slow the tempo",["Gradually get louder","Repeat the section","Stop forever"],"Ritardando means slowing.")
H('c.3.A',3,"Which describes a mature tone on a cello?",
  "Rich, even and resonant throughout the range",["Scratchy and uneven","Very thin","Constantly changing"],"Mature tone is controlled and full.")
H('c.3.A',3,"A baritone adjusts vowel shape to match the genre's expected sound. She is demonstrating what?",
  "Characteristic sound appropriate for the genre",["Poor diction","Random tone","Rushing"],"Tone is style-specific.")
H('c.3.B',3,"A percussionist adjusts stick grip to avoid wrist strain. She is refining what?",
  "Psychomotor skills",["Ticket sales","Program notes","Seating plans"],"Efficient technique prevents strain.")
H('c.3.B',3,"Which technique helps a singer sustain a long phrase?",
  "Low, controlled breath support",["Raising the shoulders","Holding the jaw tight","Gasping"],"Support controls airflow.")
H('c.3.C',3,"A student marks subdivisions in a difficult measure and plays with a metronome. She is working on what?",
  "Rhythmic accuracy",["Key signature","Phrase shape","Seating"],"Subdividing refines timing.")
H('c.3.C',3,"Which tempo choice shows good rhythmic control?",
  "A steady pulse maintained through the passage",["Speeding up in easy spots","Dragging at every rest","Changing randomly"],"Steady pulse is the goal.")
H('c.3.D',3,"A piece in E major has how many sharps?",
  "Four",["One","Six","Zero"],"E major has F, C, G and D sharp.")
H('c.3.D',3,"A relative minor shares what with its major key?",
  "The same key signature",["The same tempo only","The same title","The same clef only"],"Relative keys share signatures.")
H('c.3.E',3,"An alto holds a note slightly sharp against the group. What should she do?",
  "Listen and adjust her pitch to match",["Sing louder","Ignore it","Stop singing"],"Active listening corrects intonation.")
H('c.3.E',3,"Phrasing shapes music by doing what?",
  "Grouping notes into musical sentences with direction",["Playing every note equally","Removing dynamics","Forbidding breaths"],"Phrases give direction.")
H('c.3.F',3,"A student arranges a folk tune for her trio at a level they can perform. She is doing what?",
  "Creating music at an appropriate difficulty",["Avoiding the music","Buying instruments","Printing tickets"],"Arranging fits the players.")
H('c.3.F',3,"Which resource helps share an original composition?",
  "A recording or notation file",["A bus pass","A coupon","A parking ticket"],"Recording or notating preserves music.")
H('c.4.A',3,"Maintaining a mature, characteristic sound while sight reading shows what?",
  "Tone control even with unfamiliar notes",["Panic","Memorization","Lack of focus"],"Tone persists under pressure.")
H('c.4.A',3,"How can a sight reader keep consistent tone?",
  "Keep air steady and posture open",["Hold her breath","Tighten the jaw","Rush the tempo"],"Technique supports tone.")
H('c.4.B',3,"A bassoonist adjusts posture and breathing before sight reading a new piece. She is applying what?",
  "Psychomotor and kinesthetic skills",["Concert dress rules","Ticket policy","Stage plots"],"Preparation uses physical technique.")
H('c.4.B',3,"A relaxed hand position during sight reading helps prevent what?",
  "Tension and injury",["Reading","Counting","Hearing"],"Relaxation protects the body.")
H('c.4.C',3,"Before sight reading, a student checks accents and slurs and mentally counts the rhythm. She is preparing what?",
  "Articulation and rhythmic accuracy",["The seating chart","The lobby","The lighting"],"These are key to accurate reading.")
H('c.4.C',3,"Which strategy helps count rhythms while sight reading?",
  "Tapping the beat while counting subdivisions aloud",["Ignoring the meter","Reading only pitches","Skipping rests"],"Counting systems support accuracy.")
H('c.4.D',3,"A sight-reading piece changes from four flats to two sharps. What must the player do?",
  "Adjust quickly to the new key signature",["Ignore it","Stop at the change","Play every note natural"],"Key changes alter pitches.")
H('c.4.D',3,"Changing modality mid-piece, such as from minor to major, requires attention to what?",
  "New accidentals and the shifted tonal center",["The page color","The composer's name","The audience"],"Mode changes alter pitches.")
H('c.4.E',3,"Using letter names while reading melody is an example of what?",
  "A melodic reading system",["A tuning method","A rhythm pattern","A dynamic marking"],"Letter names identify pitches.")
H('c.4.E',3,"Which method labels notes with syllables like do, re and mi?",
  "Solfège",["Metronome clicks","Bowing marks","Time signatures"],"Solfège uses syllables.")
H('c.4.F',3,"A sight reader sees p cresc. to f in four measures. How should she play it?",
  "Begin soft and grow steadily to loud",["Start loud and fade","Stay soft","Skip the measures"],"The marking indicates a gradual increase.")
H('c.4.F',3,"What does shaping a phrase while sight reading require?",
  "Reading ahead for direction and dynamics",["Playing blindly","Stopping often","Ignoring slurs"],"Reading ahead supports phrasing.")
H('c.4.G',3,"Matching vowel shapes in a choir while sight reading improves what?",
  "Intonation",["Meter","Lyrics","Notation"],"Unified vowels help pitch.")
H('c.4.G',3,"Which listening habit improves intonation in an ensemble?",
  "Tuning chords from the bass up",["Playing louder","Ignoring neighbors","Rushing"],"Building from the bass stabilizes pitch.")
H('c.5.A',3,"A student sorts recordings into Baroque, Classical and Romantic categories. She is doing what?",
  "Classifying music by period and style",["Ordering lunch","Counting seats","Mixing colors"],"Classification uses historical context.")
H('c.5.A',3,"Which feature suggests a Baroque work?",
  "Ornamented lines and continuo",["Electronic synthesizers","Hip-hop beats","Auto-tune"],"Basso continuo is typical of Baroque music.")
H('c.5.B',3,"Why do many communities hold music festivals?",
  "To celebrate and share cultural identity",["To avoid art","To raise taxes","To ban dancing"],"Festivals express culture.")
H('c.5.B',3,"Work songs historically helped communities by doing what?",
  "Coordinating labor and building solidarity",["Banning instruments","Preventing speech","Ending trade"],"They set rhythm for group work.")
H('c.5.C',3,"Frequency and wavelength in sound connect music with which discipline?",
  "Physics",["Gym","Cooking","Typing"],"Pitch is tied to frequency.")
H('c.5.C',3,"Studying the history of a composer's era connects music with what subject?",
  "Social studies",["Welding","Chemistry lab","Driver education"],"Music reflects history.")
H('c.5.D',3,"Which career involves designing sound for films and games?",
  "Audio engineer or sound designer",["Surveyor","Plumber","Lifeguard"],"Sound design is a music-related career.")
H('c.5.D',3,"Analyzing a career option in music includes considering what?",
  "Education needed, income potential and job outlook",["Hair color","Favorite food","Shoe size"],"Careers are analyzed by requirements and outlook.")
H('c.5.E',3,"Streaming platforms pay artists small amounts per play. This is an example of what?",
  "An economic factor affecting musicians",["A rhythm pattern","A key signature","A dynamic marking"],"Payment structures impact musicians.")
H('c.5.E',3,"Sampling another artist's work without permission raises what concern?",
  "Ethical and legal questions about ownership",["A tuning concern","A meter concern","A seating concern"],"Sampling raises rights issues.")
H('c.5.F',3,"A student builds an electronic portfolio with recordings and a résumé. She is generating what?",
  "Tools for college and career preparation",["A time signature","A cadence","A rest"],"Portfolios help auditions and applications.")
H('c.5.F',3,"Which belongs in a professional musician's electronic portfolio?",
  "Performance videos and a list of repertoire",["Receipts for lunch","Random photos","Weather notes"],"These showcase abilities.")
H('c.6.A',2,"Which action shows good etiquette at a recorded or live performance?",
  "Remaining quiet and respectful during the music",["Texting aloud","Shouting over performers","Leaving mid-piece"],"Respect supports the experience.")
H('c.6.A',2,"As a performer during a rest in the program, you should do what?",
  "Stay focused and respectful of others onstage",["Chat loudly","Check phone","Walk off"],"Focus shows professionalism.")
H('c.6.B',3,"A class writes criteria for judging a jazz combo versus a chamber choir. Why should criteria be specific to style?",
  "Each style values different qualities",["All music is the same","Style does not matter","Only volume matters"],"Different styles have different standards.")
H('c.6.B',3,"Which is a criterion for evaluating a jazz performance?",
  "Quality of improvised solos and rhythmic feel",["Brightness of the lobby","Ticket price","Parking"],"Jazz values improvisation and swing.")
H('c.6.C',3,"A student offers a peer constructive feedback by naming a strength and a specific suggestion. She is doing what?",
  "Applying criteria for constructive feedback",["Being rude","Avoiding comment","Copying a score"],"Constructive feedback is specific.")
H('c.6.C',3,"Which format can be used to give feedback to a peer?",
  "A written rubric or recorded comments",["A coupon","A bus map","A menu"],"Multiple formats are valid.")
H('c.6.D',3,"A musician records weekly, listens critically and picks a metronome app to track goals. She is developing what?",
  "A process for self-evaluation",["A concert program","A ticket log","A lobby display"],"Tools and routines support growth.")
H('c.6.D',3,"Which tool supports artistic improvement?",
  "A recorded practice log with goals",["A vacation brochure","A coupon","A bus pass"],"Logs record progress.")
H('c.6.E',3,"A student compares her ensemble's performance with an exemplary model and writes recommendations. She is doing what?",
  "Evaluating performance and offering suggestions",["Skipping rehearsal","Avoiding feedback","Hiding the recording"],"Comparison leads to recommendations.")
H('c.6.E',3,"What makes feedback offered after comparing to a model useful?",
  "It is specific and suggests a next step",["It is vague","It is hurtful","It is silent"],"Specific advice helps improvement.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_music3.jsonl'))

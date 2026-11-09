import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.314.', 1027, own='hs_musicstudies.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',2,"In a music studies class, students stream a famous jazz quartet and then attend a live student jam. They are experiencing what?",
  "Exemplary music through technology and live performance",["Ticket scalping","Stage carpentry","Lobby design"],"Both formats supply musical models.")
H('c.1.A',2,"Why do producers study classic recordings?",
  "To learn how skilled artists shape sound and style",["To avoid listening","To memorize prices","To skip practice"],"Classics model good technique.")
H('c.1.B',2,"On a pop track, the lead vocal carries the tune while keyboards and bass fill in chords. The lead vocal is the ___ part.",
  "Melodic",["Percussive","Silent","Meter"],"The lead line is the melody.")
H('c.1.B',2,"Notes played together beneath a melody create what?",
  "Harmony",["Silence","Tempo","Volume only"],"Harmony supports the melody.")
H('c.1.C',2,"The distance in pitch from C to the next higher C is an ___.",
  "Octave",["Second","Third","Fourth"],"An octave spans eight scale degrees.")
H('c.1.C',2,"Which chord contains a root, a third and a fifth?",
  "A triad",["A rest","An accent","A tie"],"A triad stacks thirds.")
H('c.1.D',2,"In a song with four steady beats per measure, which meter is being used?",
  "4/4",["3/4","2/2 only","9/8"],"Four beats per measure indicates 4/4.")
H('c.1.D',2,"Counting a beat aloud as 1 and 2 and 3 and 4 and shows what?",
  "A counting system that includes the subdivision",["A key signature","A chord symbol","A clef"],"Counting syllables mark eighth-note subdivisions.")
H('c.1.E',2,"Which is an element of music?",
  "Melody",["Costume","Lighting grid","Poster"],"Melody is a core element.")
H('c.1.E',2,"A symbol such as mf or ff tells a performer about what?",
  "Dynamics",["Key","Clef","Meter"],"Dynamic markings show volume.")
H('c.1.F',2,"Which habit helps a studio musician protect their ears during long sessions?",
  "Taking listening breaks and keeping monitor volume moderate",["Turning headphones up","Never resting","Wearing no protection near loud amps"],"Moderate volume and breaks prevent hearing damage.")
H('c.1.F',2,"Why should a keyboardist adjust bench height and wrist position?",
  "To reduce strain and avoid injury",["To play softer","To read faster","To change keys"],"Ergonomics prevent overuse injury.")
H('c.2.A',2,"A student reads chord charts in one assignment and manipulates audio loops in another. This shows what?",
  "Reading notation systems or manipulating sounds as the course requires",["Memorizing menus","Selling music","Avoiding sound"],"Music studies includes diverse tools.")
H('c.2.A',2,"Which could be a notation system used in a music studies course?",
  "Lead sheet or tablature",["Weather map","Bus schedule","Recipe card"],"Different notations suit different instruments.")
H('c.2.B',3,"A student notates a rhythm in 6/8 and records it with a drum machine. What is she doing?",
  "Notating and producing a rhythmic pattern",["Printing tickets","Tuning a violin","Painting a mural"],"Notation and recording work together.")
H('c.2.B',3,"Which meter is considered simple?",
  "2/4",["6/8","9/8","12/8"],"Simple meters divide each beat into two.")
H('c.2.C',2,"The marking staccato tells a performer to do what?",
  "Play the notes short and detached",["Hold the notes long","Play louder","Play slower"],"Staccato means detached.")
H('c.2.C',2,"The Italian word adagio indicates what?",
  "A slow tempo",["A fast tempo","A loud dynamic","A repeat"],"Adagio means slow.")
H('c.2.D',3,"A student producing a track in D major notes that two sharps belong in the key signature. Which are they?",
  "F-sharp and C-sharp",["B-flat and E-flat","G-sharp and D-sharp","None"],"D major has F# and C#.")
H('c.2.D',3,"What does knowing a song's mode help a producer decide?",
  "Which scale notes and mood fit the song",["Which seats are open","Which microphones cost less","Which lights to buy"],"Mode defines the scale and feel.")
H('c.2.E',3,"A student uses a digital audio workstation to record a vocal and layer harmonies. This is which skill?",
  "Using technology for recording and production",["Hand-copying scores only","Ignoring sound","Selling merchandise"],"A DAW is a production tool.")
H('c.2.E',3,"Why should a recording be saved in multiple versions?",
  "So earlier takes can be recovered if edits go wrong",["To use up storage","To change the key","To speed up the song"],"Versioning protects work.")
H('c.3.A',3,"A producer chooses a warm tone for a ballad and a bright, punchy tone for a dance track. She is demonstrating what?",
  "Characteristic sounds appropriate for each genre",["Random choices","Poor mixing","No plan"],"Sound choices fit style.")
H('c.3.A',3,"Which tool shapes the tone of a recorded instrument?",
  "Equalization",["A seating chart","A ticket","A poster"],"EQ adjusts frequency balance.")
H('c.3.B',3,"A student prepares a set including a blues, a bossa nova and a pop ballad. She is building what?",
  "A repertoire representing a variety of styles",["A single-style set","A silent concert","A lecture"],"Variety shows range.")
H('c.3.B',3,"Which choice would add variety to a performance repertoire?",
  "Pieces from different cultures and time periods",["Repeating one song","Skipping rehearsals","Playing only the intro"],"Diverse styles broaden skills.")
H('c.3.C',3,"A student lays down a drum track and checks it against a click to make sure the rhythm is steady. She is demonstrating what?",
  "Rhythmic accuracy",["Poor timing","Random pitch","Loud dynamics"],"A click confirms steady timing.")
H('c.3.C',3,"Legato articulation means notes are what?",
  "Smooth and connected",["Very short","Silent","Accented"],"Legato is connected.")
H('c.3.D',3,"A performer builds a gradual crescendo over a verse and a soft ending for contrast. She is demonstrating what?",
  "Dynamics and phrasing",["Wrong notes","A key change","Silence only"],"Dynamics shape the line.")
H('c.3.D',3,"What is a musical phrase?",
  "A group of notes that forms a complete musical idea",["One single note","A page number","A rest only"],"Phrases are musical sentences.")
H('c.3.E',3,"A guitarist tunes each string with a tuner before a recording session. She is attending to what?",
  "Intonation",["Meter","Notation","Tempo"],"Tuning ensures correct pitch.")
H('c.3.E',3,"Singing slightly flat throughout a song is a problem of what?",
  "Intonation",["Rhythm","Form","Rests"],"Pitch accuracy is intonation.")
H('c.3.F',3,"What is a good technique for an informal coffeehouse performance?",
  "Adapting your set and stage presence to a relaxed audience",["Ignoring the crowd","Refusing to speak","Leaving mid-song"],"Informal concerts allow flexibility.")
H('c.3.F',3,"What is one technique for a formal recital?",
  "Dressing professionally and following a prepared program",["Improvising the order every time","Wearing anything","Arriving late"],"Formal concerts follow conventions.")
H('c.4.A',3,"A student creates a four-bar melody from a scale and builds a rhythm for it. She is doing what?",
  "Creating an original musical phrase",["Copying a song","Buying a score","Selling tickets"],"Composition begins with phrases.")
H('c.4.A',3,"Which approach helps create a memorable melody?",
  "Repeating and varying a short motif",["Using random notes","Never repeating","Using no rhythm"],"Repetition with variation builds memorability.")
H('c.4.B',3,"A producer records a new riff on her phone and later writes it in notation. She is doing what?",
  "Recording and notating an original phrase",["Erasing music","Deleting files","Avoiding documentation"],"Both recording and notation preserve ideas.")
H('c.4.B',3,"Which tool lets a composer write music on a staff and hear it played back?",
  "Notation software",["A stopwatch","A ruler","A coupon"],"Software supports notation and playback.")
H('c.5.A',3,"A student compares reggae and country music by rhythm, instruments and cultural roots. She is doing what?",
  "Comparing and contrasting music by genre and culture",["Counting seats","Ordering food","Painting"],"Comparison uses musical and cultural features.")
H('c.5.A',3,"Which pair of terms describes historical periods?",
  "Baroque and Romantic",["Allegro and piano","Treble and bass","Major and minor"],"These are eras in music history.")
H('c.5.B',2,"Which is a vocation in the music business?",
  "Recording engineer",["Plumber","Roofer","Surveyor"],"Engineering is a music career.")
H('c.5.B',2,"Someone who plays guitar for fun with friends has a music ___.",
  "Avocation",["Vocation","License","Degree"],"An avocation is a hobby.")
H('c.5.C',2,"Why do people sing at birthday celebrations?",
  "Music is used to mark and share special occasions",["It avoids joy","It ends traditions","It prevents speech"],"Songs mark celebrations.")
H('c.5.C',2,"A protest song is an example of music used to do what?",
  "Express beliefs and unite people",["Hide ideas","Replace laws","Stop speech"],"Songs can express and unite.")
H('c.5.D',3,"Calculating the length of a song in measures from its tempo connects music to which subject?",
  "Mathematics",["Gym","Cooking","Welding"],"Music uses arithmetic.")
H('c.5.D',3,"Studying how a microphone captures sound connects music to which discipline?",
  "Physics",["Painting only","Geography only","Typing"],"Sound capture involves physics.")
H('c.5.E',3,"Using a sample from another artist's recording without permission can raise what issue?",
  "Copyright and ethical concerns",["A tuning issue","A tempo issue","A seating issue"],"Using music requires permission.")
H('c.5.E',3,"Streaming has changed how artists earn income because listeners now pay what way?",
  "Through subscriptions and small per-play payments",["Only by buying vinyl","By paying nothing ever","Through coupons only"],"Streaming changed the economics.")
H('c.5.F',3,"A student creates a social media page to share performance clips and book gigs. She is using what?",
  "A tool for career preparation",["A time signature","A cadence","A clef"],"Social media promotes artists.")
H('c.5.F',3,"What is a useful tool for a young musician seeking a college program?",
  "A recorded audition portfolio",["A bus map","A menu","A calendar of sales"],"Portfolios show skills.")
H('c.6.A',2,"At a student showcase, good audience behavior is to do what?",
  "Silence phones and applaud politely",["Talk through songs","Record loudly aloud","Leave during sets"],"Etiquette respects performers.")
H('c.6.A',2,"As a performer, good etiquette includes what?",
  "Thanking the audience and supporting other acts",["Ignoring others","Leaving early","Complaining onstage"],"Courtesy supports a positive event.")
H('c.6.B',3,"A class builds a checklist with tone, rhythm, creativity and stage presence to judge a performance. This is what?",
  "Designing criteria for informed judgments",["Guessing","Copying","Skipping evaluation"],"Criteria guide judgments.")
H('c.6.B',3,"Which feedback applies criteria?",
  "The groove stayed steady, but the vocal was sharp in the chorus",["I liked it","Nope","Not sure"],"Specific comments apply criteria.")
H('c.6.C',3,"A student records her sets, watches them back and tracks goals in a notebook. She is developing what?",
  "A process for self-evaluation",["A concert flyer","A seat map","A ticket booth"],"Review and goals drive improvement.")
H('c.6.C',3,"Which tool supports a musician's artistic growth?",
  "A weekly practice log",["A parking pass","A coupon","A menu"],"Logs track progress.")
H('c.6.D',3,"A student compares her cover of a song to the original recording and lists differences in feel and tone. She is doing what?",
  "Evaluating a performance against an exemplary model",["Ignoring the original","Skipping the lesson","Deleting both"],"Comparison with models guides growth.")
H('c.6.D',3,"After comparing to a model, a musician should do what next?",
  "Pick one or two specific areas to practice",["Quit music","Blame equipment","Ignore the model"],"Evaluation should lead to action.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_musicstudies.jsonl'))

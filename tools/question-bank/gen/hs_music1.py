import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.310.', 1023, own='hs_music1.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',2,"A student listens to a recording of a professional wind ensemble and then attends a live school concert to compare. She is exploring what?",
  "Exemplary musical examples through technology and live performance",["Ticket pricing","Stage lighting wiring","Parking rules"],"Both recordings and live concerts provide models.")
H('c.1.A',2,"Why do musicians listen to exemplary recordings?",
  "To hear a model of tone, style and phrasing",["To avoid practicing","To skip rehearsals","To memorize the cover art"],"Models guide musical choices.")
H('c.1.B',2,"While listening to a choir piece, a student hears a tune on top and supporting notes below. The tune is the ___ part.",
  "Melodic",["Rhythmic only","Silent","Percussive only"],"The melody is the main tune; harmony supports it.")
H('c.1.B',2,"Notes sounded together to support a melody form what?",
  "Harmony",["Tempo","Rest","Meter"],"Harmony is simultaneous pitches.")
H('c.1.C',2,"The distance in pitch between two notes is called a(n) what?",
  "Interval",["Measure","Fermata","Cadenza"],"An interval measures pitch distance.")
H('c.1.C',2,"A chord built from a root, a third and a fifth is called a what?",
  "Triad",["Scale","Rest","Tie"],"A triad stacks thirds.")
H('c.1.D',2,"In 4/4 time, how many beats are in each measure?",
  "Four",["Two","Three","Six"],"The top number shows beats per measure.")
H('c.1.D',2,"What does meter organize in music?",
  "Beats into groups with strong and weak pulses",["Pitches into scales","Voices into parts","Notes into chords"],"Meter groups the steady beat.")
H('c.1.E',2,"Which of these is an element of music?",
  "Rhythm",["Brushstroke","Choreography","Set design"],"Rhythm, melody, harmony and form are musical elements.")
H('c.1.E',2,"A sign such as crescendo or ritardando is an example of what?",
  "An expression marking",["A key signature","A time signature","A clef"],"Expression markings shape performance.")
H('c.1.F',2,"Which habit best protects a musician's hearing?",
  "Using hearing protection and limiting time near loud sound",["Turning volume up louder","Ignoring ringing in the ears","Playing at maximum loudness daily"],"Hearing loss from loud sound is preventable.")
H('c.1.F',2,"Good posture while practicing helps a musician avoid what?",
  "Tension and strain injuries",["Reading notes","Counting rhythms","Hearing pitch"],"Healthy body mechanics prevent strain.")
H('c.2.A',3,"Which meter is a compound meter?",
  "6/8",["4/4","2/4","3/8"],"Compound meter divides the beat into three.")
H('c.2.A',3,"Meter that mixes groups of two and three beats, such as 5/8, is called what?",
  "Asymmetrical",["Simple","Silent","Even"],"Asymmetrical meters have uneven groupings.")
H('c.2.B',2,"The Italian term piano tells a performer to play how?",
  "Softly",["Loudly","Fast","Slowly"],"Piano means soft.")
H('c.2.B',2,"A dot placed above or below a note head tells a player to do what?",
  "Play it short and detached",["Hold it long","Play it louder","Skip it"],"A dot indicates staccato.")
H('c.3.A',3,"A mature, characteristic sound on a trumpet should be what?",
  "Full, centered and appropriate to the style",["Thin and airy","Always as loud as possible","Unfocused"],"Tone quality fits the instrument and genre.")
H('c.3.A',3,"What most helps a singer produce a mature choral tone?",
  "Supported breath and tall vowels",["Shallow breaths","A tight throat","Shouting"],"Breath support and vowel shape build tone.")
H('c.3.B',3,"Which is an example of a psychomotor skill in performance?",
  "Using correct posture and hand position",["Reading the program","Choosing a seat","Buying a ticket"],"Physical technique is psychomotor.")
H('c.3.B',3,"Breathing deeply from the diaphragm helps a performer do what?",
  "Sustain phrases with steady air",["Play without notes","Skip counting","Avoid dynamics"],"Air control supports phrasing.")
H('c.3.C',3,"A player who keeps a steady beat with a metronome is demonstrating what?",
  "Rhythmic accuracy at the right tempo",["Poor timing","Random pitch","Loud dynamics"],"Steady pulse shows accuracy.")
H('c.3.C',3,"A student rushes during an easy passage. What should she fix?",
  "Her steadiness of tempo",["The key signature","The program title","The seating"],"Rushing is a tempo-control issue.")
H('c.3.D',3,"A piece has two sharps in its key signature. A player should do what?",
  "Play F-sharp and C-sharp unless marked otherwise",["Ignore the sharps","Play only naturals","Play every note flat"],"Key signature applies to all notes of those names.")
H('c.3.D',3,"The modality of a piece, such as major or minor, affects what?",
  "The scale pattern and mood of the music",["The ticket price","The stage size","The length of rests"],"Mode sets the interval pattern.")
H('c.3.E',3,"A note that sounds slightly flat to the ensemble has a problem with what?",
  "Intonation",["Meter","Rhythm","Articulation"],"Intonation is accuracy of pitch.")
H('c.3.E',3,"Shaping a phrase with a gradual crescendo then decrescendo uses what?",
  "Appropriate dynamics and phrasing",["Wrong notes","A key change","Silence only"],"Dynamics shape musical lines.")
H('c.3.F',3,"A student writes a four-measure melody and records it on her phone. She is doing what?",
  "Creating and recording an original musical phrase",["Copying a score","Tuning an instrument","Buying music"],"Composition can be notated or recorded.")
H('c.3.F',3,"Which tool can notate an original phrase?",
  "Music notation software",["A calculator","A thermometer","A ruler only"],"Notation software records musical ideas.")
H('c.4.A',3,"Sight reading with a mature sound means a player should do what even on a new piece?",
  "Keep tone quality steady while reading unfamiliar music",["Stop and restart repeatedly","Play only loudly","Skip hard measures"],"Tone should not suffer.")
H('c.4.A',3,"Which statement describes good sight-reading tone?",
  "Characteristic of the genre despite unfamiliar notes",["Different in every measure","Always thin","Never supported"],"Tone stays consistent.")
H('c.4.B',3,"While sight reading, a violinist keeps her bow arm relaxed and her posture balanced. She is demonstrating what?",
  "Psychomotor and kinesthetic skills",["Program notes","Music theory only","Audience etiquette"],"Physical technique carries into reading.")
H('c.4.B',3,"A singer sight reading takes a quiet, quick breath at a rest. She is using what?",
  "Planned breathing",["Random sounds","Silence the whole piece","Transposition"],"Breathing is planned at rests.")
H('c.4.C',3,"Before sight reading, a student scans the time signature and counts a measure aloud. Why?",
  "To establish rhythmic accuracy using a counting system",["To find the composer's birthday","To check the page color","To avoid the key"],"Counting systems support accuracy.")
H('c.4.C',3,"What should a sight reader do if she makes a rhythm error?",
  "Keep the beat going and continue",["Stop the whole group","Walk away","Change the tempo wildly"],"Staying in time matters.")
H('c.4.D',3,"A sight-reading player notices one flat in the key signature. Which note is flat?",
  "B",["C","F","G"],"One flat is B-flat.")
H('c.4.D',3,"Why check the key signature before sight reading?",
  "To know which notes are sharped or flatted throughout",["To see the title","To count measures","To choose a seat"],"The key signature affects many notes.")
H('c.4.E',3,"Singing do, re, mi while reading a melody uses what system?",
  "Solfège",["Fingering chart","Chord tab","Time signature"],"Solfège names scale degrees.")
H('c.4.E',3,"Reading a melody by singing numbers like 1, 2, 3 for scale degrees is an example of what?",
  "A melodic reading system",["A rhythm exercise","A tuning method","A rest"],"Numbers can label scale degrees.")
H('c.4.F',3,"A sight reader listens and adjusts her pitch to match the group. She is working on what?",
  "Intonation",["Meter","Tempo","Notation"],"Listening improves pitch matching.")
H('c.4.F',3,"While sight reading, following written dynamics shows what?",
  "Appropriate dynamics",["Poor focus","Missing the rhythm","No phrasing"],"Dynamics are part of the score.")
H('c.5.A',3,"A student compares a Baroque fugue with a modern jazz piece. She is comparing music by what?",
  "Genre, style and historical period",["Instrument color","Ticket cost","Seat location"],"Comparison covers style and era.")
H('c.5.A',3,"Which pair differs mainly by culture?",
  "Mariachi and Irish folk music",["Two identical scales","Two quarter notes","Two measures"],"Regional traditions differ by culture.")
H('c.5.B',2,"Which is a music-related career?",
  "Sound engineer",["Pilot","Plumber","Surveyor"],"Audio engineering is a music career.")
H('c.5.B',2,"A person who plays in a community band on weekends has a music what?",
  "Avocation",["Vocation","Degree","License"],"An avocation is a hobby pursuit.")
H('c.5.C',2,"A lullaby sung to calm a baby shows music used for what?",
  "Comfort and nurturing in a culture",["Selling cars","Math tests","Weather reports"],"Music serves social purposes.")
H('c.5.C',2,"Why is music played at many ceremonies?",
  "It marks and expresses important events",["It solves equations","It replaces speech laws","It cooks food"],"Ceremonies use music to express meaning.")
H('c.5.D',3,"Counting fractions of a beat in rhythm most closely connects music to which subject?",
  "Mathematics",["Cooking","Gym","Typing"],"Rhythm uses fractions.")
H('c.5.D',3,"Studying how sound waves travel connects music to what discipline?",
  "Physics",["History only","Painting only","Geography only"],"Acoustics is physics.")
H('c.5.E',3,"Downloading music without paying the artist raises what issue?",
  "Ethical and economic issues about creators' rights",["A tuning issue","A rhythm issue","A key signature issue"],"Artists deserve compensation.")
H('c.5.E',3,"How have streaming services changed music?",
  "They changed how listeners access music and how artists earn money",["They ended all live music","They removed melody","They made instruments unnecessary"],"Technology reshaped the business.")
H('c.5.F',3,"A student builds a digital portfolio of recordings to apply for a music program. She is using what?",
  "Tools for college and career preparation",["A rest symbol","A time signature","A tuner only"],"Portfolios support applications.")
H('c.5.F',3,"A musician posts performance clips to promote herself. She is using what?",
  "Social media as a career tool",["A conductor's baton","A metronome","A staff"],"Social media can build an audience.")
H('c.6.A',2,"At a formal concert, when should audience members applaud?",
  "At the end of a piece or when the conductor signals",["Between every movement loudly","Whenever they like","During quiet passages"],"Etiquette respects the music.")
H('c.6.A',2,"As a performer, proper concert etiquette includes what?",
  "Entering and leaving the stage calmly and respectfully",["Talking during the piece","Checking a phone onstage","Leaving mid-song"],"Performers show professionalism.")
H('c.6.B',3,"A class creates a rubric listing tone, rhythm, intonation and expression to judge a recording. This is what?",
  "Designing criteria for informed judgments",["Guessing","Copying a score","Ignoring quality"],"Criteria support judgments.")
H('c.6.B',3,"Which judgment is informed?",
  "The balance was good but the tenors were sharp in measure 12",["It was fine","I just liked it","No comment"],"Specific evidence makes judgments useful.")
H('c.6.C',3,"A student records herself weekly and tracks progress on a chart. She is developing what?",
  "A process for self-evaluation",["A concert program","A seating chart","A ticket system"],"Tracking supports improvement.")
H('c.6.C',3,"Which tool helps a musician evaluate her own playing?",
  "A recording with a checklist",["A mirror only","A calendar only","A map"],"Recordings reveal details.")
H('c.6.D',3,"A student compares her ensemble's recording with a professional recording. She is doing what?",
  "Evaluating a performance against an exemplary model",["Avoiding feedback","Skipping the recording","Changing the key"],"Models set standards.")
H('c.6.D',3,"After comparing to a model, what is the best next step?",
  "Choose specific areas to improve and practice them",["Quit practicing","Blame the instrument","Ignore the model"],"Evaluation should lead to action.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_music1.jsonl'))

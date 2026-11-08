#!/usr/bin/env python3
"""Grade 3 Fine Arts: Art 117.111, Music 117.112, Theatre 117.113 (TEKS) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('117.', 943, own='g3_fa.jsonl')

load(B, """
111.b.1.A|2|An artist paints a picture of her family eating dinner. Her idea came from...|life experience|a math test|a weather report|a bus map|Artists draw ideas from their own lives.
111.b.1.A|3|Drawing a dragon that lives in a cloud castle uses your...|imagination|schedule|allowance|locker|Imagination is a source for original art.
111.b.1.B|3|How light or dark a color is, from pale yellow to deep brown, is its...|value|texture|space|motion|Value is lightness or darkness.
111.b.1.B|3|When one part of an artwork is larger or smaller than another, the artist is thinking about...|proportion|silence|volume|bedtime|Proportion compares sizes.
111.b.1.B|4|A design that feels like all of its parts belong together has...|unity|noise|delay|clutter|Unity makes parts work as a whole.
111.b.1.B|3|Using both light and dark shapes in the same picture to make it more interesting adds...|contrast and variety|silence|boredom|blame|Contrast and variety use differences.
111.b.1.C|3|Line, shape, color, texture, form, space and value are called the...|building blocks of art|rules of recess|parts of a sentence|steps of a recipe|The elements are the building blocks.
111.b.1.C|4|Balance, emphasis, pattern and unity help artists organize their work. They are the principles of...|design|weather|grammar|sports|Principles of design organize elements.
111.b.2.A|3|A student paints her walk to school to show a real memory. She is integrating ideas from...|life experiences|spelling rules|sports scores|lunch menus|Original art can come from experience.
111.b.2.B|3|Planning where to put the sun, hills and river on your paper is making a...|composition|calendar|schedule|report|Compositions arrange elements.
111.b.2.C|2|A picture made using pencils or markers on paper is a...|drawing|sculpture|print|ceramic|Drawings use dry media.
111.b.2.C|3|A three-dimensional shape pinched and shaped from clay is a...|sculpture|painting|photograph|poster|Sculptures have form.
111.b.2.C|3|Creating art with a camera or tablet uses...|photographic or digital media|clay|yarn|paint only|Digital art and photos use technology.
111.b.2.C|4|Using paper, cloth and paint together in one artwork is called...|mixed media|single medium|silent art|performance|Mixed media combines materials.
111.b.3.A|3|When you see a picture of people planting a garden long ago, you can tell its main idea is about...|growing food|a test|a race|a storm|Look for what is shown.
111.b.3.B|3|Looking at art by a man from long ago and a woman today helps you compare and contrast...|artists and cultures|bus routes|test scores|menus|Compare artworks across time and cultures.
111.b.3.C|3|An architect designs...|buildings|songs|poems|sandwiches|Architects design buildings.
111.b.3.C|3|An animator makes drawings that...|appear to move|stay silent|stay buried|cook food|Animators create motion.
111.b.3.C|4|A person who designs clothes for a living is a fashion...|designer|farmer|lifeguard|referee|Fashion designers plan clothing.
111.b.3.D|3|Using symmetry in a butterfly drawing connects art to...|math and science|swimming|recess|lunch|Symmetry is a math idea.
111.b.4.A|3|Telling whether a painting has strong emphasis on a bright color is to...|evaluate the artwork|delete the artwork|hide the artwork|toss the artwork|Evaluate means judge using art terms.
111.b.4.B|3|Writing a short note about why you made an artwork is an artist...|statement|menu|receipt|bill|Artist statements explain art.
111.b.4.C|3|Keeping your best drawings in a folder to see how you have grown is for self...|assessment|punishment|hunger|travel|Portfolios help assess growth.
112.b.1.A|2|A child's voice is usually higher than...|an adult man's voice|a flute|a bird|a whistle|Children's voices are higher.
112.b.1.A|3|Sorting a recording by listening to see if the singers are children or adults is to...|categorize voices|paint voices|bake voices|count voices|Categorizing means sorting by type.
112.b.1.B|3|A flute and an oboe are in the...|woodwind family|brass family|string family|percussion family|Woodwinds are blown with reeds or air.
112.b.1.B|3|A violin and a cello are in the...|string family|brass family|woodwind family|percussion family|Strings are bowed or plucked.
112.b.1.B|3|A tuba and a trombone are in the...|brass family|string family|woodwind family|percussion family|Brass are buzzed into metal horns.
112.b.1.B|3|A tambourine and a triangle are in the...|percussion family|brass family|string family|woodwind family|Percussion instruments are struck or shaken.
112.b.1.C|3|The special quality that makes a trumpet sound different from a flute even on the same note is...|timbre|tempo|beat|rest|Timbre is tone color.
112.b.1.C|3|Mezzo forte means...|medium loud|medium soft|very loud|very soft|Mezzo means medium.
112.b.1.C|3|Mezzo piano means...|medium soft|medium loud|very loud|very fast|Mezzo means medium.
112.b.1.C|3|Which word describes how fast or slow the beat moves?|tempo|timbre|texture|tune|Tempo is speed.
112.b.1.D|4|A song has a first section, a different middle section, and then the first section returns. This form is...|ternary or ABA|binary|random|rondo|ABA has a return.
112.b.1.D|4|When a song moves from a first part to a new contrasting part and stops, it has two sections. This is called...|binary form|ternary form|no form|a fugue|Two parts is binary.
112.b.2.A|3|Four sixteenth notes together get the same time as one...|quarter note|half note|whole note|eighth rest|Four sixteenths equal one beat.
112.b.2.A|3|A whole note in 4/4 meter lasts how many beats?|four|one|two|three|A whole note fills a measure of four beats.
112.b.2.A|3|A whole rest in 4/4 means silence for...|a full measure|one beat|half a beat|no time|A whole rest fills the measure.
112.b.2.B|4|The extended pentatonic scale uses notes from the staff. Reading melody on a staff means reading...|pitches on lines and spaces|only words|only numbers|only colors|The staff shows pitch.
112.b.2.C|3|A symbol that tells players to get softer gradually is a...|decrescendo|crescendo|rest|clef|Decrescendo gets softer.
112.b.2.C|3|A symbol that tells players to get louder gradually is a...|crescendo|decrescendo|rest|clef|Crescendo gets louder.
112.b.3.A|3|Singing with accurate intonation means singing...|in tune|too loudly|too late|without breath|Intonation is pitch accuracy.
112.b.3.A|3|Keeping the long and short sounds exactly on time with your group is playing with accurate...|rhythm|clothing|paper|chairs|Rhythm is timing.
112.b.3.B|3|The song Home on the Range is an example of an American...|folk song|science fact|bus rule|menu|Folk songs are shared traditional songs.
112.b.3.C|3|Moving your hands and feet together to a beat is an example of...|integrated movement|silence|standing still|reading|Integrated movement coordinates the body.
112.b.3.C|3|Walking, skipping and jumping across the room are...|locomotor skills|stationary skills|silent skills|written skills|Locomotor means traveling.
112.b.3.D|4|A repeated rhythm played under a melody is a rhythmic...|ostinato|essay|menu|border|Ostinato is a repeated pattern.
112.b.3.D|4|A short repeated melody played under a song is a melodic...|ostinato|solo|silence|scale|Ostinato repeats.
112.b.3.E|3|When a score says mezzo forte, you perform with a...|medium loud sound|whisper|very fast tempo|rest|Mezzo forte is medium loud.
112.b.4.A|3|Making up a new rhythm on the spot is a rhythmic...|improvisation|spelling|recipe|map|Improvisation is made up in the moment.
112.b.4.B|3|Writing down your own short tune to share is a melodic...|composition|recess|lunch|map|Composition is written music.
112.b.4.C|4|Making up a simple part to play with a song is creating an...|accompaniment|argument|appetizer|answer|An accompaniment supports a melody.
112.b.5.A|3|Playing a singing game with your class from a local tradition is performing music from...|local cultures|only machines|nowhere|outer space|Games connect to culture.
112.b.5.B|3|A march, a lullaby and a dance tune are examples of different...|styles of music|colors of paint|types of food|kinds of weather|Different genres and styles exist.
112.b.5.C|3|Counting beats in a song uses ideas from...|math|swimming|gym only|lunch only|Counting beats is math.
112.b.6.A|2|At a concert, a good audience member applauds...|at the end of a piece|during the music|while talking|while walking|Audience etiquette.
112.b.6.B|3|Hearing a rhythm and naming it with the correct music word is recognizing a rhythmic...|element|table|chair|door|Using vocabulary names the pattern.
112.b.6.C|3|When a song suddenly gets louder in the middle, you have identified a change in...|dynamics|pencil|weather|name|Dynamics are volume changes.
112.b.6.C|4|When a song switches from a violin to a trumpet, there is a change in...|timbre|sentence|price|lunch|Timbre is tone color.
112.b.6.D|2|Swaying slowly to calm music is responding through...|movement|a test|a quiz|a map|Movement is a response.
112.b.6.E|3|Telling a friend that a piece was fast, loud and had a steady beat is describing a performance using music...|vocabulary|laundry|sports|weather|Describing uses music words.
113.b.1.A|2|Acting out feeling happy or sad in a make-believe game is reacting to emotional experiences through creative...|play|math|chores|lunch|Creative play expresses feelings.
113.b.1.B|3|Using slow and fast movement to make the space for your scene is creating...|playing space|a bill|a menu|a clock|Movement can define space.
113.b.1.C|3|Moving like leaves when you hear soft music is responding to sounds with...|movement|a pencil|a bill|a book|Responding through movement.
113.b.1.D|3|Standing very still as a statue in a scene is a way to portray...|a character|a menu|a math fact|a weather map|Characters can be shown with body.
113.b.2.A|2|Speaking clearly without yelling and moving without bumping others is safe use of...|movement and voice|clothing|paper|food|Safety in drama.
113.b.2.B|3|Telling a story by acting without speaking is narrative...|pantomime|math|reading|cooking|Pantomime uses no words.
113.b.2.C|3|Using a flashlight to make a character appear on a wall is called shadow...|play|art class|test|map|Shadow play tells stories.
113.b.2.C|3|A sock with button eyes that acts out a story is a...|puppet|ruler|trumpet|calendar|Puppets can act out stories.
113.b.2.D|4|Acting out a book scene using body motions and copying what characters say is using pantomime and imitative...|dialogue|dessert|distance|dinner|Dialogue is spoken words.
113.b.3.A|3|Props, costumes and sound are technical...|theatre elements|chess pieces|lunch items|math tools|They support character and setting.
113.b.3.B|3|Wearing a paper crown to show you are a king is using a simple...|costume|rule|recipe|score|Costumes show character.
113.b.3.B|3|A cardboard tree on stage is a simple...|prop or set piece|score|recipe|ticket|Props and set pieces show environment.
113.b.3.C|3|Deciding who plays each role before a pretend scene is how you...|plan dramatic play|cancel it|forget it|erase it|Planning helps rehearsal.
113.b.3.D|2|Sharing ideas and listening in a group scene is...|cooperation|argument|hiding|bullying|Cooperation helps theatre.
113.b.3.E|3|Watching a play at a theatre or a video of a show is how you...|observe a theatrical performance|bake a cake|test a theory|play a game|Observing is part of learning theatre.
113.b.4.A|3|Acting out a folktale from another culture helps you explore...|cultural influences|nothing|only recess|only math|Stories carry culture.
113.b.4.B|4|In a movie the actors may do special effects, but in real life they cannot. This shows a difference between life and...|film|bread|rocks|dirt|Compare life and media.
113.b.5.A|2|Audience members should do what during a play?|watch and listen quietly|talk and eat loudly|run around|use phones loudly|Respectful audience behavior.
113.b.5.B|3|Saying what worked well in a class skit and what could be better is to...|evaluate a performance|hide a performance|erase a performance|fold a performance|Evaluate means judge fairly.
113.b.5.C|3|Talking about how music, movement and costumes made a scene stronger is discussing...|visual components|only the weather|only the tickets|only the seats|Discuss how arts blend.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g3_fa.jsonl'))
print("saved", len(B.out), "questions")

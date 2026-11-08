#!/usr/bin/env python3
"""Grade 2 Fine Arts: Art 117.108, Music 117.109, Theatre 117.110 (TEKS) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('117.', 942, own='g2_fa.jsonl')

load(B, """
108.b.1.A|2|Two leaves from the same tree are not exactly alike. Finding how they differ uses your...|senses|shoes|lunch|calendar|We compare objects by looking, touching and smelling.
108.b.1.A|3|Telling how a pinecone and a pebble are the same and different is...|comparing and contrasting|subtracting|spelling|singing|Compare means same, contrast means different.
108.b.1.B|2|Lines, shapes, colors, textures, forms and space are the...|elements of art|school rules|food groups|weather types|These are the building blocks of art.
108.b.1.B|3|A repeated stripe design on a quilt shows the principle of...|repetition and pattern|silence|temperature|measurement|Repeating a shape makes a pattern.
108.b.1.B|3|A big red circle in a small blue picture grabs your eye first. This is the principle of...|emphasis|hunger|tempo|spelling|Emphasis makes one part stand out.
108.b.1.B|4|Wavy lines that lead your eye across a painting show...|movement|a recipe|a time zone|a fraction|Lines can lead the eye and give movement.
108.b.2.A|2|Using dark, heavy lines to show a stormy mood is expressing a...|feeling|fraction|noun|weekday|Art can show feelings.
108.b.2.A|3|Choosing soft, round shapes and light colors for a peaceful picture is expressing an...|idea|error|answer|address|Artists use elements to show ideas.
108.b.2.B|3|Planning where to place a tree, a house and a sun on your paper is creating a...|composition|report|tune|play|A composition is how parts are arranged.
108.b.2.B|3|Using both balance and pattern in your drawing shows you can combine elements and...|principles of design|rules of math|parts of speech|steps of a dance|Design uses elements and principles together.
108.b.2.C|2|Rolling clay into a ball and pinching it into an animal makes a modeled...|form|song|verse|verb|Clay can be modeled into a form.
108.b.2.C|3|Pressing an inked leaf onto paper is a skill used in making a...|print|score|script|speech|Printing transfers ink to paper.
108.b.2.C|3|Gluing cardboard pieces together to build a tall tower is making a...|construction|rhythm|chorus|scene|Constructions join materials.
108.b.3.A|3|When you look at a painting and tell what story you think it shows, you are...|interpreting the artwork|erasing the artwork|folding the artwork|wrapping the artwork|Interpret means explain meaning.
108.b.3.B|3|Both women and men have made art long ago and today in many places. Looking at it helps us learn about...|different cultures|only one town|only one season|only one meal|Art connects to cultures.
108.b.3.C|3|A person who plans how a chair or a poster looks has a job in art and...|design|baking|farming|plumbing|Designers use art skills.
108.b.3.C|3|Colorful signs, toys and book covers show how art touches our...|daily lives|dreams only|sleep only|weather|Art affects everyday life.
108.b.3.D|3|Measuring paper for a collage connects art to...|math|gym|lunch|recess|Measuring is a math skill.
108.b.4.A|3|Saying I picked these colors because they make me feel calm is giving a reason for a...|preference|punishment|prize|problem|Support your choices with reasons.
108.b.4.B|3|A building that shows art for people to visit, either real or online, is a...|museum or gallery|garage|bank|kitchen|Collections of art are shown in museums.
108.b.4.B|4|Looking at two artworks and telling how their ideas match and differ is to...|compare and contrast|multiply|rhyme|scramble|Compare and contrast looks for likenesses and differences.
108.b.4.C|3|Collecting your pictures in a folder to look at later and check your progress is making a...|portfolio|menu|ticket|calendar|Portfolios hold collected work.
109.b.1.A|2|When everyone sings the same notes at the same time, it is called...|unison|ensemble|silence|echo|Unison means singing the same part together.
109.b.1.A|3|When a group sings different parts that fit together, it is an...|ensemble|solo|whisper|accident|Ensemble means multiple parts together.
109.b.1.B|2|Hearing a sound and knowing it is a trumpet means you identified the instrument by...|listening|smelling|tasting|counting|Aural means by ear.
109.b.1.B|3|Seeing the long slide on a trombone helps you identify it by...|sight|taste|smell|touch only|Visual means by sight.
109.b.1.C|3|The musical word presto means very...|fast|slow|loud|soft|Presto is a fast tempo.
109.b.1.C|3|The musical word andante means...|a walking pace|very fast|very loud|very soft|Andante is a walking tempo.
109.b.1.C|3|The musical word moderato means...|a medium speed|very fast|very slow|very loud|Moderato is a moderate tempo.
109.b.1.C|3|Fortissimo tells a singer to be...|very loud|very soft|very slow|very fast|Fortissimo is very loud.
109.b.1.C|3|Pianissimo tells a singer to be...|very soft|very loud|very fast|very slow|Pianissimo is very soft.
109.b.1.D|4|A song plays section one twice, then section two, then section one again. Its form is...|aaba|abac|abcd|aabb|The letters match the order of the sections.
109.b.1.D|4|A song plays section one, then section two, then section one again, then a new third section. Its form is...|abac|aaba|abab|abba|The letters match the order of the sections.
109.b.2.A|3|In 2/4 meter, each measure has how many beats?|two|four|five|six|The top number tells beats per measure.
109.b.2.A|4|A half note in 2/4 meter lasts how many beats?|two|one|four|three|A half note fills the whole 2/4 measure.
109.b.2.A|3|A half rest in 2/4 means...|silence for two beats|play for two beats|clap once|sing high|Rests mean silence.
109.b.2.B|4|A pentatonic melody is made from how many different pitches?|five|three|eight|twelve|Penta means five.
109.b.2.B|3|Musicians write melody on a set of lines and spaces called the...|staff|menu|map|page number|The staff holds notes.
109.b.2.C|3|Allegro means...|fast|slow|soft|loud|Allegro is a quick tempo.
109.b.2.C|3|Largo means...|slow|fast|soft|loud|Largo is a slow tempo.
109.b.2.C|3|Forte means...|loud|soft|fast|slow|Forte is loud.
109.b.2.C|3|Piano means...|soft|loud|fast|slow|Piano is soft.
109.b.3.A|2|Singing tunefully means singing...|on pitch|out of tune|with no sound|too late|Tunefully means in tune.
109.b.3.A|3|Playing a rhythm pattern on a drum with your class is performing in a...|group|bathtub|cave|tree|Classes can play together.
109.b.3.B|3|Singing a song from another country helps you learn about its...|culture|bank|weather map|clock|Songs carry culture.
109.b.3.C|3|Hopping, skipping and galloping to music are all...|locomotor movements|stationary rests|silent notes|written notes|Locomotor movement travels through space.
109.b.3.C|3|Swaying or bending while staying in one spot is...|non-locomotor movement|locomotor movement|a skip|a gallop|Non-locomotor stays in place.
109.b.3.D|4|A short rhythm pattern repeated over and over under a song is an...|ostinato|essay|escape|echo only|Ostinato repeats.
109.b.3.D|3|Singing, speaking and chanting are ways of exploring your...|voice|knees|elbows|toes|Vocal exploration uses your voice.
109.b.3.E|3|If a song should be played presto and fortissimo, you play it...|very fast and very loud|very slow and very soft|slow and loud|fast and soft|Presto = very fast, fortissimo = very loud.
109.b.3.E|4|If a song should be played andante and pianissimo, you play it...|at a walking pace and very softly|very fast and loudly|slowly and loudly|fast and very softly|Andante is a walking pace and pianissimo is very soft.
109.b.4.A|3|Putting known quarter notes and half notes in your own order creates a rhythmic...|phrase|recipe|menu|map|Phrases are short musical ideas.
109.b.4.B|3|Using notes you already know to make your own short tune creates a melodic...|phrase|border|bridge|bell|Melodic phrases use pitches.
109.b.4.C|3|Trying out a new idea on a xylophone or with your voice is...|exploring|erasing|ending|resting|Exploration finds new ideas.
109.b.5.A|2|A song sung at a holiday or season is called...|seasonal music|a math fact|a weather map|a menu|Seasonal songs fit holidays or seasons.
109.b.5.B|3|Listening to a short song from long ago and one from today shows music from different...|times in history|grades|buses|jobs|Music changes over time.
109.b.5.C|3|Clapping the number of syllables in a word links music with...|language arts|swimming|painting only|cooking|Syllables connect rhythm and words.
109.b.6.A|2|During a concert, a good audience member...|listens quietly|talks to a friend|walks around|plays a game|Respectful behavior.
109.b.6.B|3|If you hear a short, short, long rhythm and name it, you are recognizing a rhythmic...|element|desk|chair|door|Naming patterns uses music terms.
109.b.6.C|3|Telling that a second note is higher than the first is distinguishing...|pitch|weather|color|shape|Pitch is high or low.
109.b.6.C|3|Telling that a song got louder is distinguishing...|dynamics|pitch|lyrics|names|Dynamics are volume.
109.b.6.D|2|Showing with your body that a song is calm and slow is responding through...|movement|a test|a bill|a stamp|Movement shows musical response.
110.b.1.A|2|Pretending to hide when you hear thunder is reacting to a sound through dramatic...|play|math|spelling|laundry|Dramatic play uses imagination.
110.b.1.B|3|Moving slowly like honey and quickly like rain around a room expands your...|spatial awareness|spelling|lunch time|bus route|Space awareness is knowing where you are.
110.b.1.C|3|Using actions, sounds and talk in pretend play is using actions, sounds and...|dialogue|ink|glue|paint|Dialogue is spoken words.
110.b.1.D|3|Saying a character's lines the way you heard them is to recreate...|dialogue|a table|a coin|a map|Dialogue is what characters say.
110.b.2.A|2|Using your body and voice in drama without hurting yourself is demonstrating...|safe use of movement and voice|danger|noise|hurry|Safety matters in drama.
110.b.2.B|3|Acting out a story using only body and face with no words is narrative...|pantomime|math|reading|baking|Pantomime has no speaking.
110.b.2.C|3|Using a hand puppet to act out a short story with little action is...|puppetry|surgery|farming|banking|Puppets tell stories.
110.b.2.D|3|Acting out the words of a lullaby with a puppet or by moving is to dramatize a...|song|bill|rock|desk|Songs can be dramatized.
110.b.3.A|3|Choosing a beach in summer as the place for your skit is selecting the...|setting|ending|title|price|Setting is where and when.
110.b.3.B|3|Turning two chairs into a car for pretend play is adapting the...|environment|clock|menu|score|Common objects can become set pieces.
110.b.3.C|3|Deciding who will play each part before you start is how you...|plan dramatic play|end dramatic play|forget dramatic play|cancel dramatic play|Planning gets everyone ready.
110.b.3.D|2|Taking turns and listening to your partner in a scene is...|cooperation|arguing|hiding|running away|Cooperation helps scenes work.
110.b.4.A|3|Pretending to be a lunch worker or a bus driver imitates life in your...|school and community|space station|cave|castle|Real roles come from community life.
110.b.4.B|4|A short tale with talking animals and a lesson, used in drama, is a...|fable|weather chart|math fact|bus pass|Fables teach lessons.
110.b.4.B|4|A story about a princess and a magic wish is a...|fairytale|science report|menu|phone book|Fairytales are magical stories.
110.b.5.A|2|Which is appropriate audience behavior at a play?|watching quietly|talking loudly|throwing paper|shouting|Appropriate behavior is respectful.
110.b.5.B|3|After a skit, saying what part you liked is to...|discuss drama|ignore drama|erase drama|fold drama|Reacting shares thoughts.
110.b.5.C|3|Adding music, dance and costumes to a play is integrating music, creative movement and...|visual components|laundry|homework|cooking|A show combines many arts.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g2_fa.jsonl'))
print("saved", len(B.out), "questions")

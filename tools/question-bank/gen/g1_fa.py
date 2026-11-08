#!/usr/bin/env python3
"""Grade 1 Fine Arts: Art 117.105, Music 117.106, Theatre 117.107 (TEKS) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('117.', 941, own='g1_fa.jsonl')

load(B, """
105.b.1.A|2|Two apples in a bowl look almost the same but one is bigger. Noticing this uses your...|senses to compare|ears to count|mouth to sing|nose to read|Artists notice how things are alike and different.
105.b.1.A|3|Describing how a rough tree bark is different from smooth glass uses the sense of...|touch|hearing|taste|smell|Touch tells texture.
105.b.1.B|2|The way a surface feels, like fuzzy or smooth, is its...|texture|beat|voice|tempo|Texture is how something feels.
105.b.1.B|3|A cube or a ball that you can hold is an example of...|form|line|rhythm|tempo|Form is three-dimensional.
105.b.1.B|3|Putting a big shape on one side and a big shape on the other side makes a picture with...|balance|noise|tempo|rhythm|Balance means equal weight.
105.b.2.A|2|Mixing dots, curvy lines, and squares to make a new creature is...|inventing an image|copying a photo|reading a story|counting|Inventing means making something new.
105.b.2.A|3|Choosing red, orange, and yellow to paint a sunset is a choice about...|color|rhythm|tempo|pitch|Colors can be chosen.
105.b.2.B|3|Placing squares in neat rows to make a design is an...|orderly arrangement|random scribble|accident|mistake|Orderly means in an organized way.
105.b.2.C|2|Using scissors carefully to cut paper shapes is building...|manipulative skills|swimming skills|reading speed|dance steps|Small hand movements are manipulative skills.
105.b.2.C|3|Pressing a rubber stamp into ink and onto paper makes a...|print|song|poem|play|Prints are made by pressing.
105.b.3.A|2|A painting of a sunny park shows the idea of...|a happy day outdoors|a storm at sea|nothing|a math problem|Artworks express ideas.
105.b.3.A|3|The same flower can be shown by a drawing, a painting, or a sculpture. These different tools are called...|media|meals|notes|steps|Media are art materials.
105.b.3.B|3|Artists in different countries and long ago made art. This shows art is made by...|people all over the world and through time|only one country|only adults today|only machines|Art is global and historical.
105.b.3.C|2|A decorated plate or a colorful poster shows how art is used in...|everyday life|only museums|only space|nowhere|Art is part of daily life.
105.b.3.D|3|Using a ruler to measure and draw equal squares links art with...|math|swimming|cooking|singing|Measuring is a math skill.
105.b.4.A|2|Telling the class why you chose blue for the sky in your picture is...|explaining your artwork|erasing your picture|hiding your picture|losing your picture|Artists explain choices.
105.b.4.B|3|A building where paintings and sculptures are displayed for visitors is an art...|museum|bakery|garage|post office|Museums collect art.
105.b.4.B|3|Looking at pictures of artworks on a computer from a museum is visiting a...|virtual museum|zoo|bakery|kitchen|Virtual means online.
105.b.4.C|3|Keeping your drawings together in a folder to show later is making a...|portfolio|sandwich|racecourse|map|Portfolios store art.
106.b.1.A|2|The voice used to sound out a song is the...|singing voice|inner voice|whispering voice|calling voice|The singing voice makes melody.
106.b.1.A|3|A child's singing voice is usually...|higher than an adult man's voice|the same as a tuba|silent|lower than a drum|Children sing higher.
106.b.1.B|2|A trumpet and a trombone are in which instrument family?|brass|strings|percussion|woodwinds|Brass instruments are metal horns.
106.b.1.B|3|A flute and a clarinet are in the...|woodwind family|brass family|percussion family|string family|Woodwinds are blown.
106.b.1.B|3|A xylophone and a snare drum are in the...|percussion family|string family|brass family|woodwind family|Percussion are struck.
106.b.1.C|3|The musical word for fast is...|allegro|largo|forte|piano|Allegro means fast.
106.b.1.C|3|The musical word for slow is...|largo|allegro|forte|piano|Largo means slow.
106.b.1.C|3|The musical word for loud is...|forte|piano|largo|allegro|Forte means loud.
106.b.1.C|3|The musical word for soft is...|piano|forte|allegro|largo|Piano means soft.
106.b.1.D|3|A song with a first part that repeats and then a different part uses the pattern...|ab|zz|xy|all the same|ab means two different sections.
106.b.1.D|4|A song plays its first section twice, then a new section, then the first section once more. Its pattern is...|aaba|abcd|bbbb|abba|aaba repeats a then contrasts.
106.b.2.A|3|A quarter note gets how many beats in a simple pattern?|one beat|four beats|none|ten beats|Quarter note is one beat.
106.b.2.A|4|Two paired eighth notes together take the same time as one...|quarter note|whole note|half rest|dotted whole|Two eighths equal one quarter.
106.b.2.B|4|The pentatonic scale has how many different tones?|five|two|ten|twelve|Pentatonic means five tones.
106.b.2.B|4|Writing three tones in order so you can sing them is writing a...|melodic pattern|rhythmic pattern|picture|poem|Melody is about pitch.
106.b.3.A|2|Singing in tune with your class is singing...|tunefully|silently|sadly|slowly only|Tunefully means on pitch.
106.b.3.B|3|Playing a folk song from another country shows music from a different...|culture|season|weather|shape|Songs reflect cultures.
106.b.3.C|3|Moving only your arms while standing still is a...|non-locomotor movement|locomotor movement|march|run|Non-locomotor stays in place.
106.b.3.D|4|A short pattern that keeps repeating under a song is a...|rhythmic ostinato|story|picture|map|An ostinato repeats.
106.b.3.D|3|Tapping the steady beat while a friend taps the words' rhythm is doing...|part work|a mistake|a nap|a puzzle|Part work uses different parts together.
106.b.3.E|3|If the class plays a song softly and slowly, they are using...|piano and largo|forte and allegro|forte and largo|piano and allegro|Soft and slow match piano and largo.
106.b.4.A|3|Making your own pattern with quarter notes and paired eighth notes is creating a...|rhythmic pattern|shape pattern|color pattern|word pattern|Rhythm uses long and short sounds.
106.b.4.B|3|Choosing three notes to make your own short tune is creating a...|melodic pattern|stage set|costume|painting|Melody is made of pitches.
106.b.4.C|3|Trying a new sound on a classroom instrument is...|exploring a new musical idea|ignoring music|erasing music|stopping music|Exploring finds new ideas.
106.b.5.A|2|A song you sing at a flag ceremony is a...|patriotic song|lullaby only|jingle only|cartoon only|Patriotic songs honor the nation.
106.b.5.B|3|Feeling the steady beat in an old folk tune and a new song shows beat is found in music from...|many times and cultures|only one time|only one place|only machines|Beat appears everywhere.
106.b.5.C|3|Counting beats in a song links music with...|math|cooking|swimming|painting only|Counting is math.
106.b.6.A|2|At a school concert, you show good audience behavior by...|listening quietly|calling out|running|talking loudly|Audiences are respectful.
106.b.6.B|3|If you hear a pattern of long-short-short in a song and name it correctly, you are...|recognizing a rhythmic element|painting|dancing|resting|Naming patterns uses music words.
106.b.6.C|3|Hearing two songs that are both loud shows they are the...|same in dynamics|different in dynamics|silent|slow|Both loud means same.
106.b.6.D|3|Showing with arm movements that the music is getting faster is responding...|through movement|with a paintbrush|with a pen|by sleeping|Movement shows response.
107.b.1.A|2|Playing pretend helps you build...|confidence|nothing|fear|noise only|Dramatic play builds confidence.
107.b.1.B|3|Walking in a big circle and keeping space around you uses...|spatial awareness|spelling|counting|painting|Spatial awareness is knowing space.
107.b.1.C|2|Hopping like a bunny and making a hop sound is imitating actions and...|sounds|colors|words only|numbers|Imitating includes sounds.
107.b.1.D|3|Pretending to be a tree swaying in the wind is creating an...|inanimate object|animal|person|machine|Trees are non-living in drama class.
107.b.1.D|3|Acting like a barking dog is imitating an...|animate object|inanimate object|rock|chair|Animals are animate.
107.b.2.A|2|Using your voice safely in a play means...|using a strong voice without hurting your throat|screaming nonstop|whispering all day|never speaking|Safe voice use protects you.
107.b.2.B|3|Acting like a grandmother at a pretend tea party is creating a role through...|imitation|subtraction|division|sleeping|Imitating a person makes a role.
107.b.2.C|3|Acting out The Three Little Pigs with your class is dramatizing a...|simple story|math fact|science lab|map|Dramatizing is acting out.
107.b.2.D|3|Acting out the words of a nursery rhyme is dramatizing a...|poem|map|menu|recipe|Poems can be dramatized.
107.b.3.A|3|When you decide your play happens in a snowy forest, you are discussing the play's...|location and climate|lunch|shoes|homework|Setting includes place and weather.
107.b.3.B|3|Using chairs and tables to build a ship for pretend is adapting the...|environment|calendar|clock|map|Common objects can become sets.
107.b.3.C|3|Practicing the same scene several times before the show is...|rehearsal|recess|recipe|reading|Rehearsal is practice.
107.b.3.D|2|A good cast mate listens and shares the stage. This is...|cooperation|competition|bullying|ignoring|Cooperation helps a play.
107.b.4.A|3|Pretending to be a school bus driver and a crossing guard in a skit is imitating...|school and community life|space travel|ancient times|cartoons only|Skits can show community roles.
107.b.4.B|4|A tale with talking animals that teaches a lesson is a...|fable|weather report|math problem|recipe|Fables teach lessons.
107.b.4.B|4|A very old story that explains why something in nature happens is a...|myth|math fact|map|shopping list|Myths explain the world.
107.b.5.A|2|Which is good audience behavior at a play?|clap at the end|talk during the scene|walk around|use a loud toy|Respectful audiences stay quiet.
107.b.5.B|3|After the skit, saying what part you liked best is...|discussing the drama|erasing the drama|ignoring the drama|hiding the drama|Discussion shares thoughts.
107.b.5.C|3|Adding music and a costume to a play uses sound and visual components to...|make the story clearer|stop the story|hide the actors|hurt the audience|Components enhance stories.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g1_fa.jsonl'))
print("saved", len(B.out), "questions")

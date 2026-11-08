#!/usr/bin/env python3
"""Grade 4 Fine Arts: Art 117.114, Music 117.115, Theatre 117.116 (TEKS) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('117.', 944, own='g4_fa.jsonl')

load(B, """
114.b.1.A|3|A student paints the school playground to share a memory with viewers. The idea came from...|life experiences|a weather chart|a bus rule|a spelling list|Artists communicate ideas from life.
114.b.1.A|3|Painting a creature that is half bird and half fish comes from...|imagination|a map|a textbook|a ruler|Imagination is a source for original art.
114.b.1.B|3|When an artist draws long curved marks that swirl across the paper, she is using the element of art called...|line|rhythm in music|math|speech|Lines are an element of art.
114.b.1.B|4|A work where one side matches the other in weight and size shows...|balance|noise|speed|hunger|Balance is a principle of design.
114.b.1.B|4|Repeating the same shape in a row creates...|pattern|volume|silence|bedtime|Repetition makes pattern.
114.b.1.B|4|The size relationship between a hand and a face in a portrait is...|proportion|temperature|mood|noise|Proportion compares sizes.
114.b.1.C|3|Color, line and shape are called the elements of art. They work like...|building blocks|weather|rules|prizes|Elements are building blocks.
114.b.1.C|4|Principles such as unity and emphasis are used by artists to...|organize the elements|erase the elements|hide the elements|delete the elements|Principles organize.
114.b.2.A|3|A fourth grader makes a clay model of her dog. She is integrating ideas from...|life experience|a test|a game score|a menu|Original art uses life experience.
114.b.2.B|3|Deciding where to place the largest shape and where to add contrast is creating a...|composition|word list|schedule|math quiz|Compositions arrange elements.
114.b.2.C|2|Making a pot from clay and firing it creates...|ceramics|a photo|a song|a poem|Ceramics are made of clay.
114.b.2.C|3|Weaving yarn through a loom creates...|fiber art|a print|a drawing only|a photograph|Fiber art uses fibers.
114.b.2.C|3|Taking a picture with a camera and editing it is...|photographic imagery|ceramics|weaving|printmaking|Photography is an art form.
114.b.2.C|4|Using a tablet to draw a character is...|digital art|ceramics|woodcarving|weaving|Digital art uses technology.
114.b.3.A|3|A painting that records a famous parade is an artwork meant to...|document history|stop time|cook a meal|build a house|Art can document history.
114.b.3.A|4|A portrait with a sad face and dark colors expresses...|emotions|speed|temperature|distance|Art can express feelings.
114.b.3.B|3|Comparing a mask made long ago to one made today shows how art reflects...|different times and cultures|only one town|only clothes|only math|Art shows culture.
114.b.3.C|3|A person who draws characters for books is an...|illustrator|plumber|farmer|referee|Illustrators draw for publication.
114.b.3.C|3|A person who plans the layout and look of a website is a...|web designer|pilot|baker|dentist|Web designers use art skills.
114.b.3.D|3|Measuring angles when designing a bridge model connects art with...|math and engineering|cooking|swimming|recess|Design uses math.
114.b.4.A|3|Looking at a classmate's painting and describing its color choices and what the artist meant is to...|evaluate artwork|erase artwork|hide artwork|toss artwork|Evaluate uses art words.
114.b.4.B|3|Writing a short statement about what feelings you see in a gallery's paintings is a...|written response|math drill|spelling test|bus pass|Written responses identify emotions.
114.b.4.C|3|Keeping your sketches in a sketchbook so you can see your progress is for...|self-assessment|punishment|travel|cleaning|Portfolios help you assess growth.
115.b.1.A|3|Which pair describes two adult singing voices?|soprano and alto|trumpet and tuba|drum and bell|piano and organ|Soprano and alto are high adult voices.
115.b.1.A|2|A child's singing voice is usually...|high and light|low and rumbly|silent|electric|Children's voices are higher.
115.b.1.B|3|A piano is a...|keyboard instrument|woodwind|brass|string only|Keyboards have keys.
115.b.1.B|3|A synthesizer is an...|electronic instrument|woodwind|brass|string|Electronic instruments make sounds with circuits.
115.b.1.B|3|A clarinet is in the...|woodwind family|brass family|percussion family|string family|Clarinets are blown with a reed.
115.b.1.C|4|Getting gradually louder is a...|crescendo|decrescendo|rest|clef|Crescendo means grow louder.
115.b.1.C|4|Getting gradually softer is a...|decrescendo|crescendo|rest|clef|Decrescendo means grow softer.
115.b.1.C|3|Short, detached notes are played...|staccato|legato|piano|slowly|Staccato is short and separated.
115.b.1.C|3|Smooth, connected notes are played...|legato|staccato|loudly|silently|Legato is smooth.
115.b.1.D|4|A rondo form returns to the main theme...|several times between new sections|never|only at the start|once|Rondo repeats the main theme.
115.b.1.D|4|Hearing a first theme, a new contrasting theme, then the first theme again tells you the form is...|ternary or ABA|binary|random|unison|ABA returns to the first theme.
115.b.2.A|3|A dotted half note in 3/4 meter gets how many beats?|three|one|two|four|A dotted half is 3 beats.
115.b.2.A|3|Two separated eighth notes together equal how many beats in 4/4?|one|four|three|two|Two eighths make one beat.
115.b.2.A|4|One eighth note followed by two sixteenth notes takes the same time as...|one quarter note|one whole note|one half note|a dotted half|Eighth plus two sixteenths equals one beat.
115.b.2.B|4|On a staff, higher notes sit...|higher on the staff|lower on the staff|off the page|inside the clef only|Pitch rises as notes move up.
115.b.2.C|3|A symbol under a note that tells players to hold or detach it is an...|articulation mark|name tag|border|scoreboard|Articulation marks tell how to play notes.
115.b.3.A|3|A choir that matches every pitch exactly as written is singing with good...|intonation|laundry|spelling|volume only|Intonation is pitch accuracy.
115.b.3.B|3|The song Home on the Range is an example of...|an American folk song|a math fact|a video game|a rap|Folk songs are traditional.
115.b.3.B|3|Texas folk music is part of...|local culture|space travel|fashion shows|chess|Local cultures share folk songs.
115.b.3.C|3|Moving feet and hands together is...|integrated movement|a still pose|silence|reading|Integrated means combined.
115.b.3.D|3|A play party is a...|singing and dancing game|math test|science lab|lunch line|Play parties are folk games.
115.b.3.E|4|A repeated pattern played under a melody is an...|ostinato|essay|apple|answer|Ostinato repeats.
115.b.3.F|3|If a score shows crescendo, you should play...|gradually louder|suddenly silent|slower|higher|Crescendo means getting louder.
115.b.4.A|3|Making up a rhythm pattern on the spot is rhythmic...|improvisation|reading|laundry|erasing|Improvisation is spontaneous.
115.b.4.B|3|Writing out your own melody is...|composition|recess|lunch|math|Composition is written music.
115.b.4.C|4|A simple part that supports a melody is an...|accompaniment|answer|appetite|accident|Accompaniment supports the melody.
115.b.5.A|3|A historical folk song of Texas is an example of music from...|Texas cultures|the moon|a sports team|a recipe|Folk songs reflect history.
115.b.5.B|3|Which song is Texas's state song?|Texas, Our Texas|Jingle Bells|Row Row Row|Twinkle Twinkle|Texas, Our Texas is the state song.
115.b.5.C|3|Hearing two songs from different countries and telling how their styles differ is describing...|diverse music styles|the weather|a map|a recipe|Describe genres and styles.
115.b.5.D|3|Counting the beats in a measure uses a skill from...|math|swimming|cooking|painting|Counting is math.
115.b.6.A|2|When the orchestra finishes a piece, a good audience member...|applauds politely|talks loudly|leaves noisily|throws things|Audience etiquette.
115.b.6.B|3|Hearing a long-short-short pattern and naming it correctly is recognizing a rhythmic...|element|door|chair|desk|Use vocabulary.
115.b.6.C|3|When the speed suddenly slows in a recording, you have described a change in...|tempo|lunch|name|weather|Tempo is speed.
115.b.6.C|4|When a song changes from smooth to detached, the change is in...|articulation|weather|address|price|Articulation is how notes are connected.
115.b.6.D|2|Showing a slow song with flowing arms is responding through...|movement|a test|a bill|paper|Movement is a response.
115.b.6.E|3|Describing a concert as lively, with fast tempo and loud dynamics, uses specific music...|vocabulary|chores|clothes|transportation|Use music words.
115.b.6.F|3|Saying I like this piece because of its smooth melody and soft dynamics is...|justifying a preference|ignoring the music|stopping the music|erasing the music|Support preferences with music vocabulary.
116.b.1.A|3|Acting out a scene with real feelings after smelling a cake baking links senses and emotions in...|dramatic play|math|science fair|recess time|Dramatic play uses sensory and emotional responses.
116.b.1.B|3|Moving rhythmically across the stage to music builds body awareness and...|spatial perception|bank balances|bus routes|homework|Spatial perception is awareness of space.
116.b.1.C|3|Using voice and movement to respond to a story you heard is...|dramatic play|a test|a bill|a map|Respond through movement and voice.
116.b.1.D|3|Using a slow, sad walk and soft voice to show grief is using...|interpretive movement|stillness|spelling|math|Interpretive movement shows emotion.
116.b.1.E|3|Acting out going to the store using real experiences is to...|imitate life experiences|ignore life|cook a meal|read a map|Drama imitates life.
116.b.1.F|3|Using a broom as a horse to show riding is using common objects to represent...|setting and action|math|recipes|schedules|Objects can stand for things.
116.b.1.G|3|What the characters say to each other is...|dialogue|setting|prop|theme|Dialogue is spoken words.
116.b.1.G|3|A person in a story is a...|character|scene|prop|costume|Characters are people in the story.
116.b.1.G|3|Where and when a story takes place is the...|setting|dialogue|prop|costume|Setting is time and place.
116.b.1.G|3|An object used by an actor, like a lantern or a book, is a...|prop|theme|setting|dialogue|Props are handheld objects.
116.b.1.G|4|The big idea or message of a story, such as kindness wins, is its...|theme|prop|dialogue|costume|Theme is the message.
116.b.2.A|2|Protecting your voice by not yelling for too long is safe use of...|the voice and body|food|clothing|paper|Safe voice use.
116.b.2.B|3|Telling about a character, who she is friends with and where she lives is describing...|character, relationships and surroundings|math facts|spelling rules|bus numbers|Describe characters and settings.
116.b.2.C|3|Making up a short scene right on the spot as a pioneer child uses...|improvisation|spelling|math|laundry|Improvised scenes use imagination.
116.b.2.D|3|Acting out a chapter of a book with partners, keeping the events in order, is dramatizing a...|literary selection|math fact|recipe|score|Dramatize literary selections.
116.b.2.E|3|Making up and acting out a short story together shows how stories can be created...|collaboratively|alone and hidden|silently only|by accident|Collaboration builds stories.
116.b.3.A|3|Choosing a long red cape to show a king is using a costume to define...|character|a recipe|a clock|a map|Costumes help show who someone is.
116.b.3.B|3|Moving chairs to make a stage in the middle of the room is altering space to create...|a performance environment|a lunchroom|a library|a bus|Space can be changed for theatre.
116.b.3.C|3|Agreeing with your group on a short scene before you act it is how you...|plan a dramatization collaboratively|cancel the play|forget the play|erase the play|Plan together.
116.b.3.D|2|Taking turns and listening while you act is...|cooperation|arguing|hiding|running away|Cooperation helps.
116.b.4.A|3|Performing a story from long ago in Texas shows theatre as a reflection of life in...|particular times and places|no place|no time|space|Theatre reflects its culture.
116.b.4.A|4|Stories passed down by telling them aloud are part of the...|oral tradition|written code|scoreboard|map room|Oral traditions are spoken.
116.b.4.B|3|Live plays, movies and television are all part of...|media in American society|a math book|a food group|a map|Media shape society.
116.b.4.C|4|Comparing a director's job to an actor's job is comparing theatre...|artists|animals|buildings|games|Theatre artists have different roles.
116.b.5.A|2|At a school play, the audience should...|watch quietly and clap at the end|talk loudly|walk around|throw things|Audience etiquette.
116.b.5.B|4|A class playmaking activity is informal; a ticketed show on a stage is...|formal theatre|a recess|a bus ride|a lunch|Formal theatre has a performance.
116.b.5.C|3|Adding quiet music to a sad scene helps show the...|emotions in the scene|weather outside|math facts|lunch menu|Music enhances ideas and emotions.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g4_fa.jsonl'))
print("saved", len(B.out), "questions")

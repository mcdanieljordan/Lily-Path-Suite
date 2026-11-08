#!/usr/bin/env python3
"""Grade 5 Fine Arts: Art 117.117, Music 117.118, Theatre 117.119 (TEKS) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('117.', 945, own='g5_fa.jsonl')

load(B, """
117.b.1.A|3|A fifth grader paints a picture of her neighborhood festival to share with the community. The source of her idea is...|life experience|a scoreboard|a calendar|a fire drill|Artists develop ideas from their own lives.
117.b.1.A|3|A student draws a city floating in the clouds. That idea comes from...|imagination|a timetable|a receipt|a ruler|Imagination can be a source of original art.
117.b.1.B|3|How light or dark a hue is, from pale pink to deep maroon, describes its...|value|volume|speed|weight|Value is lightness or darkness.
117.b.1.B|4|Using one bright color in a mostly gray painting so it pops creates...|emphasis|silence|mistakes|delay|Emphasis draws attention.
117.b.1.B|4|Making a design feel like all parts belong to one whole shows...|unity|chaos|boredom|noise|Unity ties parts together.
117.b.1.B|4|Mixing smooth areas with rough areas gives a work contrast and...|variety|silence|boredom|delay|Contrast and variety use differences.
117.b.1.C|3|Line, shape, color and texture are building blocks of art. Balance and unity are used to organize the blocks. The organizers are the principles of...|design|weather|grammar|recess|Principles of design organize the elements.
117.b.2.A|3|Sketching a family trip to the lake for a class mural is integrating ideas from...|life experiences|test scores|bus rules|lunch lines|Original art draws from life.
117.b.2.B|3|Deciding how to use balance and contrast across your whole page is building a...|composition|menu|schedule|spelling list|Compositions combine elements and principles.
117.b.2.C|3|Carving a design into a block, inking it and pressing it onto paper makes a...|print|song|recipe|score|Printmaking transfers ink.
117.b.2.C|3|Coiling clay into a cup shape and firing it makes...|ceramics|photography|weaving|stitching|Ceramics are fired clay.
117.b.2.C|4|Gluing and joining cardboard, wire and wood into a standing structure is a...|construction|poem|duet|menu|Constructions are assembled.
117.b.2.C|3|Editing a photograph on a computer to create a poster is...|digital art|ceramics|weaving|woodcarving|Digital art uses technology.
117.b.3.A|4|A flag, a dove or a heart can stand for an idea. These are...|symbols|rhythms|recipes|chores|Symbols represent ideas.
117.b.3.A|4|Comparing two artworks and deciding which better achieved its purpose is judging its...|effectiveness|weight|price|height|Effectiveness is how well it achieves its purpose.
117.b.3.B|3|Comparing the purpose of a quilt sewn long ago to one sewn today helps you connect art to...|cultures|clouds|prices|sports|Art reflects cultures.
117.b.3.C|3|A person who plans the rooms and furniture of a home is an interior...|designer|farmer|referee|plumber|Interior designers plan spaces.
117.b.3.C|3|A person who makes movies is a...|film maker|dentist|accountant|pilot|Film makers create films.
117.b.3.D|4|Understanding that mixing red and blue makes purple links art with...|science|swimming|recess|lunch|Color mixing uses science.
117.b.3.D|3|Using a grid and ratios to enlarge a drawing connects art with...|mathematics|swimming|recess|spelling|Ratios are math.
117.b.4.A|4|Explaining how the media and techniques in a painting support the artist's intent is to...|evaluate the work|erase the work|paint the wall|tear the page|Evaluate uses art terms.
117.b.4.B|4|Looking across a museum collection and noting that many works show the sea is identifying a...|theme|bill|button|ticket|Themes are repeated ideas.
117.b.4.C|3|Compiling your work in a portfolio so you can review your growth is for self...|assessment|punishment|travel|cooking|Portfolios support assessment.
118.b.1.A|3|Which set lists adult singing voices from highest to lowest?|soprano, alto, tenor, bass|bass, tenor, alto, soprano|alto, bass, soprano, tenor|tenor, soprano, bass, alto|Soprano is highest, bass is lowest.
118.b.1.A|4|A male adult voice that is in the lowest range is a...|bass|soprano|alto|child's voice|Bass is the lowest voice.
118.b.1.B|3|A saxophone is part of which family?|woodwind|brass|string|percussion|Saxophones are reed instruments.
118.b.1.B|3|A french horn is part of which family?|brass|woodwind|string|keyboard|French horns are brass.
118.b.1.B|3|An electric keyboard is an example of an...|electronic keyboard instrument|woodwind|hand drum|violin|Electronic instruments use circuits.
118.b.1.C|4|Gradually speeding up is called...|accelerando|ritardando|fermata|legato|Accelerando means speed up.
118.b.1.C|4|Gradually slowing down is called...|ritardando|accelerando|crescendo|staccato|Ritardando means slow down.
118.b.1.C|4|A meter with beats grouped in threes like 6/8 is a...|compound meter|simple meter|silent meter|broken meter|Compound meter groups beats in threes.
118.b.1.C|3|Meters like 2/4, 3/4 and 4/4 are...|simple meters|compound meters|silent meters|random meters|Simple meters divide beats into two.
118.b.1.D|4|A piece that states a tune and then plays changed versions of it is a theme and...|variations|silence|repeats|rests|Theme and variations changes the same tune.
118.b.1.D|4|A form with a main theme that keeps coming back between different sections is a...|rondo|round|rest|rhythm|Rondo returns to the theme.
118.b.2.A|4|A rhythm that places emphasis on normally weak beats is...|syncopated|steady|silent|spoken|Syncopation shifts accents.
118.b.2.A|3|In 3/4 meter, each measure has how many beats?|three|two|four|six|The top number is beats per measure.
118.b.2.B|4|A diatonic scale has how many different pitches before the octave repeats?|seven|five|three|twelve|Diatonic scales have seven notes.
118.b.2.B|3|Notes are read on the...|staff|menu|graph|tree|The staff is five lines and four spaces.
118.b.2.C|4|A fermata over a note tells you to...|hold the note longer|skip the note|play it softer|play it staccato|Fermata means hold.
118.b.2.C|3|A repeat sign tells players to...|play the section again|stop forever|play louder|skip the song|Repeat signs mean play again.
118.b.3.A|3|A choir that sings every note exactly in tune and in time has good...|intonation and rhythm|spelling|clothing|lighting|Intonation is pitch accuracy.
118.b.3.B|3|The Star-Spangled Banner is an example of...|patriotic music|a lullaby only|a polka|a rap|Patriotic songs honor the nation.
118.b.3.B|3|Singing folk songs from different countries builds knowledge of...|world cultures|baking|weather|math facts only|Songs carry culture.
118.b.3.C|3|Moving your arms while your feet step in time to a beat is...|integrated movement|silence|stillness|reading|Integrated movement coordinates the body.
118.b.3.D|3|A folk dance often tells about...|a culture's traditions|a bank|a recipe|a test|Folk dances come from traditions.
118.b.3.E|4|A song sung by groups starting at different times, over and over, is a...|round|rest|rondo|rap|Rounds overlap.
118.b.3.E|4|Two different songs that fit together are...|partner songs|silent songs|solo songs|slow songs|Partner songs fit together.
118.b.3.E|4|A second melody that plays against the main tune is a...|counter melody|border|menu|map|Counter melodies accompany.
118.b.3.F|4|If a score says accelerando, performers should...|get gradually faster|get louder|stop|get softer|Accelerando means speed up.
118.b.4.A|3|Making up a rhythm pattern in the moment is rhythmic...|improvisation|laundry|cooking|spelling|Improvisation is spontaneous.
118.b.4.B|3|Writing your own tune for a poem is melodic...|composition|recess|math|lunch|Composition creates music.
118.b.4.C|4|Creating a simple harmony part to support a song is making an...|accompaniment|argument|answer|arrow|Accompaniments support melody.
118.b.5.A|3|African American spirituals and European folk songs in America show music of different...|cultures|oceans|cities only|weeks|Many cultures contribute to music.
118.b.5.B|3|Which song is the United States national anthem?|The Star-Spangled Banner|Jingle Bells|Row Row Row|Happy Birthday|It is the national anthem.
118.b.5.C|4|Hearing a march, a waltz and a blues tune and describing how they differ is describing music of different...|genres and styles|colors|countries only|years only|Genres have different styles.
118.b.5.D|3|Explaining how rhythm uses fractions links music to...|math|swimming|cooking|painting|Rhythm uses fractions.
118.b.6.A|2|After a performance, a polite audience member...|applauds appropriately|shouts out|leaves early noisily|talks during pieces|Audience etiquette.
118.b.6.B|3|Hearing an ascending melody and naming it as stepwise is identifying a melodic...|element|chair|door|table|Naming melody types uses vocabulary.
118.b.6.C|4|Hearing a song shift from piano to forte is describing a change in...|dynamics|lunch|weather|price|Dynamics are volume.
118.b.6.C|4|Hearing a flute melody replaced by a trombone melody is describing a change in...|timbre|address|price|clothing|Timbre is tone color.
118.b.6.D|2|Showing the mood of a piece by dancing flowing arm shapes is responding with...|movement|a bill|a test|a map|Respond through movement.
118.b.6.E|4|Judging a performance by checking accuracy of pitch, rhythm and expression uses specific...|criteria|clothes|prices|seats|Evaluate using criteria.
118.b.6.F|3|Saying I like this piece because the strings play a warm, singing tune is...|justifying a preference|ignoring the music|forgetting the music|stopping the music|Justify with vocabulary.
119.b.1.A|3|Remembering how it felt to be nervous and using that feeling to play a character is using sensory and emotional...|recall|reading|math|lunch|Emotional recall builds characters.
119.b.1.B|3|Acting out opening a heavy door with no door on stage is using...|pantomime|math|reading|baking|Pantomime uses gestures only.
119.b.1.C|3|Moving like falling rain when you hear soft piano music is responding to music with...|movement|a bill|a test|a quiz|Respond through movement.
119.b.1.D|4|Using planned gestures, a worried face and a shaky voice to show fear expresses emotions with interpretive...|movement and dialogue|math and spelling|rules and tests|lunch and recess|Interpretive movement conveys feelings.
119.b.1.E|3|Acting out a moment from your own weekend in class is integrating...|life experiences|a recipe|a schedule|a quiz|Dramatic play uses life.
119.b.1.F|3|Showing you are climbing a mountain through your body is portraying an...|action|invoice|recipe|decimal|Portray actions with movement.
119.b.1.G|3|The words characters speak in a play are called...|dialogue|setting|props|scenery|Dialogue is spoken words.
119.b.1.G|3|The people in a play are the...|characters|props|lights|tickets|Characters are the people in the story.
119.b.1.G|4|A section of a play that happens in one place and time is a...|scene|prop|costume|theme|Scenes divide a play.
119.b.1.G|4|A larger idea in a play, like friendship overcomes fear, is its...|theme|prop|scene|setting|Theme is the message.
119.b.2.A|2|Warming up your voice and body before performing is a safe use of...|the voice and body|math|food|paper|Safe warm-ups.
119.b.2.B|4|Writing about a character's age, personality, friends and home in detail is describing characters, their relationships and their...|surroundings|spelling|sandwiches|sports|Describe in detail.
119.b.2.C|4|Using a stooped walk and a raspy voice to be an old fisherman is creating movements and using...|dialogue appropriately|math problems|spelling tests|bus rules|Characters use movement and dialogue.
119.b.2.D|3|Acting out a chapter of a book with a group, keeping events in a logical order, is dramatizing a...|literary selection|math problem|menu|map|Dramatize literature.
119.b.2.E|4|Inventing and acting out a short story together shows collaborative story...|creation|deletion|erasing|avoiding|Collaborate to create.
119.b.3.A|3|Placing a cardboard tree on stage and wearing a crown shows environment and character using props, costumes and visual...|elements|bills|tests|tickets|Visual elements support the story.
119.b.3.B|4|Placing platforms and chairs to form a ship deck is altering space for a...|performance environment|lunchroom|library|bank|Space is adapted.
119.b.3.C|3|Meeting with your group to decide scenes and roles is how you...|plan dramatizations collaboratively|erase dramatizations|cancel dramatizations|forget dramatizations|Planning is collaborative.
119.b.3.D|3|Responding to your partner's lines and taking turns is...|cooperation|arguing|hiding|running|Cooperation helps scenes.
119.b.4.A|4|A play that shows how people lived during the Revolution reflects life in particular...|times and places in American history|no time|no place|space|Theatre reflects history.
119.b.4.A|4|Stories passed down by speaking from generation to generation are part of an...|oral tradition|invoice|bank|scoreboard|Oral traditions are spoken.
119.b.4.B|4|Live theatre, film, television and electronic media have played different roles throughout...|American history|a lunch|a recess|a bus|Media evolve.
119.b.4.C|4|Comparing a playwright's work to a director's work is analyzing theatre...|artists and their contributions|animals|buildings|vehicles|Theatre artists contribute differently.
119.b.5.A|3|At a formal performance, audiences should...|stay quiet and applaud at the end|talk throughout|walk around|use loud noises|Audience behavior.
119.b.5.B|4|Comparing what you see, hear and say in a class skit to what happens in a professional show is comparing informal and formal...|theatre|recess|math|lunch|Compare informal and formal theatre.
119.b.5.C|3|Adding a drumbeat and moving lights during a tense scene shows how music and visual elements enhance...|emotions and ideas|weather|lunch|prices|Music and visuals enhance theatre.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g5_fa.jsonl'))
print("saved", len(B.out), "questions")

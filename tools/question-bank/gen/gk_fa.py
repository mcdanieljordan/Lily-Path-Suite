#!/usr/bin/env python3
"""Kindergarten Fine Arts: Art 117.102, Music 117.103, Theatre 117.104 (TEKS) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('117.', 940, own='gk_fa.jsonl')

load(B, """
102.b.1.A|2|Which sense do you use to see the colors in a painting?|sight|hearing|smell|taste|Your eyes see color.
102.b.1.A|2|Which sense tells you that a clay bowl feels bumpy?|touch|hearing|taste|smell|Your hands feel texture.
102.b.1.B|2|A line that goes straight across the page is...|horizontal|round|bumpy|tiny|Horizontal lines go side to side.
102.b.1.B|2|A circle, a square, and a triangle are all kinds of...|shapes|sounds|smells|songs|Shapes are an element of art.
102.b.1.B|3|When the same pattern of stripes keeps happening again and again, we call it...|repetition|balance|noise|taste|Repetition repeats an element.
102.b.2.A|2|Which tool could you use to make a wavy line?|a crayon|a spoon|a shoe|a cup|Crayons make lines.
102.b.2.A|2|Red, blue, and yellow are examples of...|colors|textures|sounds|lines|Colors are an element of art.
102.b.2.B|2|When you put shapes on paper where they feel right to you, you are arranging them...|your own way|by a rule book|by accident only|by a machine|Arranging intuitively means trusting your eyes.
102.b.2.C|2|Which is a way to make art with paint?|using a brush|using a fork to eat|using a pillow|using a clock|Painting uses brushes.
102.b.2.C|3|Pressing a carved block with ink onto paper is called...|printmaking|baking|gardening|swimming|Printmaking makes prints.
102.b.2.C|2|Building art by joining clay, paper, and boxes is called making a...|sculpture|song|play|recipe|Sculptures are 3-D.
102.b.3.A|2|A picture of a dog shows the subject of the artwork. The subject is the...|dog|paper|frame|paint tube|The subject is what the picture is about.
102.b.3.B|2|Art can show a picture of your...|family|favorite words only|numbers only|nothing|Artists share experiences.
102.b.3.B|3|When a friend draws something different from what you draw, it shows people have...|different ideas|the same ideas|no ideas|no friends|People think differently.
102.b.3.C|2|Which everyday item was designed by an artist?|a poster|a rock|a leaf|a cloud|Posters are designed.
102.b.3.C|2|We use art every day when we see...|pictures on books and signs|only thunder|only dirt|only bugs|Art is all around us.
102.b.3.D|3|Counting the petals in a flower drawing connects art to...|math|swimming|baking|sleeping|Counting links art and math.
102.b.4.A|2|When you tell someone what you made in your drawing, you are sharing your...|ideas|lunch|shoes|backpack|Artists explain their work.
102.b.4.B|3|A place where many artworks are shown for people to see is a...|museum|bakery|garage|bus|Museums display art.
102.b.4.C|3|A folder that keeps your pictures together is called a...|portfolio|playground|puzzle|pillow|A portfolio collects artwork.
103.b.1.A|2|Which voice do you use when you sing a song?|singing voice|whispering voice|calling voice|inner voice|Singing voice makes music.
103.b.1.A|2|The voice you use to talk to a friend is your...|speaking voice|whispering voice|calling voice|singing voice|Speaking voice is for talking.
103.b.1.A|3|The voice you use to call your friend across the playground is your...|calling voice|inner voice|whispering voice|speaking voice|A calling voice carries far.
103.b.1.A|3|The quiet voice you use in your head when you think is your...|inner voice|singing voice|calling voice|speaking voice|Inner voice is silent.
103.b.1.B|2|A child's singing voice usually sounds...|higher than a grown man's voice|lower than a drum|silent|like a trumpet|Children sing higher.
103.b.1.C|2|Which group of instruments includes drums and rattles?|percussion|strings|brass|woodwinds|Percussion instruments are struck or shaken.
103.b.1.C|3|Violins and cellos belong to the...|string family|brass family|percussion family|woodwind family|Strings are plucked or bowed.
103.b.1.D|2|Two sounds where one is high and one is low are...|different|the same|silent|quiet|High and low are different.
103.b.1.D|2|A song where the singers use more and more volume is getting...|louder|softer|slower|shorter|Louder means more volume.
103.b.1.D|2|When the players speed up, the tempo of the music is...|fast|slow|silent|soft|Faster means quick.
103.b.1.E|2|The steady pulse you feel in music is the...|beat|color|shape|story|The beat is steady.
103.b.1.E|3|Clapping the words of a song is clapping the...|rhythm|color|shape|story|Rhythm follows the words.
103.b.2.A|2|Playing a rhythm stick or drum with the class is playing a classroom...|instrument|vegetable|shoe|toy only|Classroom instruments are played together.
103.b.2.B|3|Learning songs from different countries helps you hear music from different...|cultures|weathers|colors|shapes|Music reflects cultures.
103.b.2.C|2|Marching to the beat is a way to...|move to music|sleep|read|paint|Moving shows the beat.
103.b.2.C|3|Walking and hopping are movements that travel across the floor. They are called...|locomotor movements|non-locomotor movements|silent movements|sit-down movements|Locomotor means moving from place to place.
103.b.2.C|3|Swaying while staying in one place is a...|non-locomotor movement|locomotor movement|march|run|Non-locomotor stays in place.
103.b.2.D|3|Tapping the steady beat on your knees while others clap a different rhythm is...|partwork|a mistake|a nap|a picture|Partwork is different parts at once.
103.b.2.E|2|To sing softly, you use a...|quiet voice|loud voice|shout|whistle|Soft means quiet.
103.b.2.E|2|To make the music faster, you...|play quicker|play slower|stop|sleep|Quicker is faster.
103.b.3.A|2|A rhyme that you chant with a game is a type of...|musical game|bike|recipe|map|Rhymes can be musical.
103.b.3.A|3|A song sung only during a holiday season is a...|seasonal song|math problem|storybook|science lab|Seasonal songs match a time of year.
103.b.3.B|3|A song about counting from one to ten connects music with...|math|swimming|painting only|sleeping|Counting songs link math.
103.b.4.A|2|At a concert, a good audience member...|listens quietly and claps at the end|talks loudly|runs around|shouts|Audiences listen politely.
103.b.4.B|2|When you pat your knees in time with the music, you are keeping a steady...|beat|picture|color|story|Beat is steady.
103.b.4.C|3|When two songs have an identical steady pulse, their beat is the...|same|different|silent|lost|Same beat means same pulse.
104.b.1.A|2|Pretending to be a doctor at play helps you learn about...|yourself and others|nothing|only math|only art|Dramatic play builds self-awareness.
104.b.1.B|2|Walking like a big elephant uses expressive...|movement|spelling|counting|painting|Movement shows ideas.
104.b.1.C|2|Meowing like a cat is copying a...|sound|picture|number|color|Imitate means copy.
104.b.1.D|3|Pretending your hands are a bird flying is imitating an...|object or animal|alphabet|number|crayon|Imitating recreates things.
104.b.2.A|2|Using your voice safely in a play means not...|screaming too long|speaking clearly|using a calm voice|taking turns|Safe use protects your voice.
104.b.2.B|2|When you play the role of a fireman in a pretend game, you are...|acting like someone else|reading a book|painting|cooking|Roles are pretend characters.
104.b.2.C|3|Dramatic play uses pretend, imagination, and...|acting|math tests|spelling quizzes|nap time|Dramatic play is pretending.
104.b.2.D|2|Joining your class in a pretend kitchen is taking part in...|dramatic play|a test|a spelling bee|a race|Dramatic play involves pretending.
104.b.3.A|2|You can make a stage for your play using...|tables and chairs|only airplanes|only boats|a bridge|Classroom objects can build a stage.
104.b.3.B|3|A simple costume can be made from...|paper, cardboard, or cloth|metal only|glass only|nothing|Simple materials work.
104.b.3.C|3|Practicing a play before showing it is called...|rehearsing|forgetting|sleeping|losing|Rehearse means practice.
104.b.3.D|2|When classmates work together to put on a play, they...|cooperate|compete|argue|leave|Cooperation helps everyone.
104.b.4.A|3|Acting out a story about your own family's traditions shows your...|culture|weather|shoes|lunch|Plays can share family cultures.
104.b.4.B|3|Acting out the story of the first Thanksgiving is a story from...|American history|a space trip|a cooking show|a sports game|It shows stories of the past.
104.b.5.A|2|Good audience behavior at a play is to...|watch quietly and clap at the end|shout out|walk around|use your phone loudly|Audiences should be respectful.
104.b.5.B|3|After a play, you can talk about...|what you saw and how it made you feel|nothing|only what you ate|only the weather|Discussing builds understanding.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'gk_fa.jsonl'))
print("saved", len(B.out), "questions")

#!/usr/bin/env python3
"""Grade 1 ELA (TEKS 110.3.b) - original questions, hand written. Skips speaking/listening (1), handwriting (2.F), independent reading (5),
fluency, publishing and research (13)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('110.3.b.', 902, own='g1_ela.jsonl')

load(B, """
2.A.i|2|Which word rhymes with "tree"?|bee|tub|hen|log|Tree and bee end with the same sound.
2.A.i|3|Which list has only rhyming words?|mop, hop, top|mop, hop, tub|cap, cup, cop|net, nut, nap|Words that rhyme end the same.
2.A.ii|2|Which two words start with the same sound?|fish, fan|fish, hat|fan, tub|hat, tub|Fish and fan start with /f/.
2.A.ii|3|Which word begins with the same sound as "chair"?|cheese|shoe|cow|jam|Chair and cheese start with /ch/.
2.A.iii|2|Which word has a long vowel sound?|cake|cat|cap|can|Cake has the long a sound.
2.A.iii|3|Which word has a short vowel sound?|bed|bike|cube|boat|Bed has the short e sound.
2.A.iv|3|Say "ship." Change /sh/ to /ch/. What is the new word?|chip|ship|shop|chap|Chip starts with /ch/.
2.A.iv|3|Say "mat." Take away /m/. What sound is left?|at|ma|am|mat|Without /m/, only "at" is left.
2.A.v|3|Blend these sounds: first /s/, next /t/, next /o/, last /p/. What word is it?|stop|step|top|spot|The sounds make stop.
2.A.v|3|Blend these sounds: first /f/, next /l/, next /a/, last /g/. What word is it?|flag|fig|frog|bag|The sounds make flag.
2.A.vi|3|Say "bake." Change /b/ to /c/. What word do you make?|cake|take|bike|cook|Cake has /c/ at the start.
2.A.vi|3|Say "ten." Change /t/ to /h/. What word do you make?|hen|pen|tin|ton|Hen has /h/ at the start.
2.A.vii|3|How many sounds are in the word "fish"?|3|2|4|5|The sounds are /f/ /i/ /sh/.
2.A.vii|3|How many sounds are in the word "stop"?|4|3|5|2|The sounds are /s/ /t/ /o/ /p/.
2.B.i|2|Which word can you sound out as /d/ /o/ /g/?|dog|dig|dug|log|The sounds spell dog.
2.B.i|3|Which word has the sounds /r/ /u/ /n/?|run|ran|rug|rub|Run is /r/ /u/ /n/.
2.B.ii|2|Which word has the blend "st" at the beginning?|star|ring|cup|jam|Star begins with st.
2.B.ii|3|Which word has the digraph "sh"?|shell|smell|spell|sell|Shell begins with sh.
2.B.ii|3|Which word ends with the digraph "ch"?|lunch|lung|link|land|Lunch ends with ch.
2.B.iii|2|Which word has a silent e that makes the vowel say its name?|bike|big|bit|bin|Bike has the VCe pattern.
2.B.iii|3|Which word has a vowel team?|rain|run|rag|ran|Rain has the vowel team ai.
2.B.iii|3|Which word has an r-controlled vowel?|car|cat|cap|can|Car has the vowel ar.
2.B.iv|3|Which word is a compound word?|sunshine|sunny|sunk|sung|Sunshine joins sun and shine.
2.B.iv|3|What two words make up "cannot"?|can and not|ca and nnot|cann and ot|c and annot|Cannot is can plus not.
2.B.iv|3|Which word is a contraction?|isn't|is|not|his|Isn't joins is and not.
2.B.v|2|Add -ed to "jump." What word do you make?|jumped|jumpes|jumping|jumps|Jumped means it already happened.
2.B.v|3|Which word has the ending -es?|boxes|boxer|bike|bats|Boxes adds es.
2.B.vi|2|Which is a word many readers know by sight?|was|zork|plix|vong|Was is a high-frequency word.
2.B.vi|3|Fill in the blank: "The girls like to run. ___ run fast."|They|Them|Then|There|They takes the place of the girls.
2.C.i|3|Which word is spelled correctly?|rain|rane|rayn|raen|Rain uses the ai team.
2.C.i|3|Which word is spelled correctly?|bike|bik|bighk|byke|Bike has a silent e.
2.C.ii|3|Which word is spelled correctly?|shop|sop|chop|shopp|Shop starts with sh.
2.C.ii|3|Which word is spelled correctly?|grass|gras|grasss|gras|Grass has a gr blend.
2.C.iii|3|Which word is spelled correctly?|farm|fram|faam|ferm|Farm has the ar sound.
2.C.iv|3|Which is spelled right?|because|becuz|becaus|becose|Because is a common word.
2.C.iv|3|Which is spelled right?|said|sed|sayd|siad|Said is spelled s-a-i-d.
2.D|2|Where would you look to find the name of the author?|on the cover|in the middle of the last page|on the spine only|inside a picture|The author's name is on the cover.
2.D|3|Which part of a book tells what chapters are inside?|table of contents|back cover only|a drawing|a page number|The table of contents lists chapters.
2.E|2|Which list is in ABC order?|ant, bee, cat|bee, ant, cat|cat, bee, ant|ant, cat, bee|ABC order follows the alphabet.
2.E|3|Which word comes first in ABC order?|apple|dog|cat|bear|A comes before b, c, d.
3.A|2|You want to know what a new word means. What can you use?|a dictionary|a ruler|a lunchbox|a puzzle|A dictionary explains words.
3.B|3|The page shows a girl wearing a coat and a hat in the snow. What does "chilly" probably mean?|cold|hot|loud|sweet|The picture shows a cold day.
3.B|3|A picture shows a puppy running very quickly. The text says it is "speedy." What does speedy mean?|fast|slow|sleepy|small|The picture shows fast.
3.C|2|What does "jumping" tell you?|the jumping is happening now|the jumping happened long ago|the jumping will never happen|the jumping is a thing|The ending -ing means happening now.
3.C|3|What does the ending -ed mean in "walked"?|it already happened|it is happening now|it will happen later|it is a place|-ed shows past.
3.C|3|What does the -s mean in "cats"?|more than one|none|only one|big|-s makes a word plural.
3.D|2|Which word names a direction?|left|happy|red|jump|Left is a direction.
3.D|3|Which word tells a position?|behind|sing|green|lunch|Behind is a position word.
3.D|3|Which word names a category of food?|fruit|chair|truck|cloud|Fruit is a kind of food.
6.A|2|Why would you read a book on how to plant seeds?|to learn how to plant|to hear a joke|to count to ten|to find a pet|The purpose is to learn.
6.B|3|You are about to read a book on whales. Which is a good question?|How big is a whale?|What is my name?|Is it Friday?|Where is the car?|It fits the topic.
6.C|3|The title is "A Rainy Day." What might the story be about?|playing indoors or in puddles|a hot desert|a rocket ship|a snowman|It fits the title.
6.C|3|A boy puts on his swim trunks and grabs a towel. What might happen next?|he goes swimming|he eats dinner in bed|he flies a kite at night|he plows a field|The clues suggest swimming.
6.D|3|"The wind howled through the trees." What do you picture?|loud wind and swaying trees|a quiet room|a sunny beach|a snowman|Words help you see it.
6.E|2|A story is about a dog who gets lost. What can you connect it to?|a time you were lost|a recipe|a math fact|the alphabet|You can connect to experiences.
6.F|3|Mia has red cheeks and is breathing hard after recess. What can you infer?|she ran a lot|she was asleep|she is cold|she is reading|Hard breathing shows running.
6.F|3|The dog wags its tail and runs to the door. How does it feel?|excited|angry|sleepy|sad|Wagging shows excited.
6.G|3|Read: "Tom woke up late. He missed the bus. He had to walk to school." What is the main point?|Tom missed the bus because he woke up late|Tom likes school|Buses are yellow|Walking is slow|It tells the key event.
6.H|3|One page says bees make honey. Another says bees help flowers grow. What do both pages tell you?|bees are helpful|bees are loud|honey is red|flowers are sweet|Combining ideas shows bees help.
6.I|2|You read a sentence that does not make sense. What should you do?|go back and read it again|keep going without thinking|close the book|throw the pencil|Rereading fixes confusion.
7.A|2|A book about a birthday party reminds you of your own party. What did you do?|made a connection|ignored the book|lost the book|ate the book|You linked the book to your life.
7.C|3|Why is Ben sad? "Ben dropped his ice cream." How do you know?|The text says he dropped his ice cream.|The page is blue.|The book is short.|Ben has a hat.|Text evidence gives the reason.
7.D|2|Retell "The Little Red Hen" in a short way.|A hen asks for help, nobody helps, and she eats the bread alone.|A hen flew to the moon.|A hen lost her shoe.|A fox won a race.|A retell keeps the main events.
7.D|3|When you retell a story you should...|keep the important events in order|add new characters|change the ending|skip the beginning|Retell keeps meaning.
8.A|3|A girl finds a lost mitten and returns it to its owner. What is the lesson?|be kind and honest|never share|mittens are red|winter is long|The theme is kindness and honesty.
8.B|2|Why does the boy in the story hide? "He was scared of the loud thunder."|something loud frightened him|he was hungry|he was tired|he was happy|The text gives the reason.
8.B|3|Rosa shares her lunch with a new student. What does this tell you about Rosa?|she is kind|she is mean|she is lazy|she is noisy|Her action shows she is kind.
8.C|2|In a story, what are the main events?|the most important things that happen|the title|the author's name|the page numbers|Main events are the key actions.
8.C|3|The ending of a story where the problem is solved is called the...|resolution|beginning|cover|title|The resolution solves the problem.
8.D|2|"One snowy night in a small village..." What is the setting?|a small village on a snowy night|a girl|a hat|a dog|Setting tells where and when.
9.A|2|A story where a clever fox tricks a crow and a lesson is taught is a...|fable|weather report|recipe|map|Fables teach lessons.
9.A|3|Which kind of text gives facts about real things?|an informational book|a fairy tale|a nursery rhyme|a fable|Informational texts give facts.
9.B|2|Which pair of words rhyme in a poem?|moon and spoon|moon and sun|spoon and fork|star and sky|Rhyming words sound alike.
9.B|3|When a poem repeats the same line, that is called...|repetition|rhyme|setting|cover|Repeating lines is repetition.
9.B|3|Which words show alliteration?|silly snakes slither|big red ball|jump high now|a happy dog|The words begin with the same sound.
9.C|3|In a play, the place where the story happens is the...|setting|title page|stage lights only|picture|The setting is where and when.
9.D.i|3|A text says, "Bees make honey. Bees help plants grow. Bees live in hives." What is the central idea?|facts about bees|a story about a dog|how to bake bread|a poem about snow|All the sentences are about bees.
9.D.ii|2|What does a caption under a photo tell you?|what the photo shows|who wrote the book|the title|the price|A caption explains the picture.
9.D.ii|3|Which text feature shows the topic of a section?|a heading|a page number|an eraser|a glue stick|Headings name sections.
9.D.iii|3|A text tells what happens first, next, and last. It is organized in...|chronological order|alphabetical order|rhyming order|size order|It follows time order.
9.E|3|A poster says, "Recycle! Keep our park clean!" What does the author want you to do?|put trash in the right bin|run|sleep|sing|The poster is persuasive.
9.F|3|Which is a multimodal text, using pictures, words, and sound?|a video with words and music|a plain rock|a blank page|a shoe|It uses more than one mode.
10.A|2|Why did the author write a book of animal facts?|to inform readers|to scare readers|to sell toys|to tell a joke|Fact books inform.
10.A|3|Why do authors write funny stories?|to entertain|to measure things|to warn about storms|to give directions|Funny stories entertain.
10.B|3|A book that shows steps for making a sandwich uses what text structure?|steps in order|rhyme|a mystery|a poem|Steps show a sequence.
10.C|3|Why might an author use bold print for a word?|to show it is important|to hide the word|to make it small|to skip it|Bold shows importance.
10.D|3|Which sentence uses words that help you picture a scene?|The huge orange sun slid behind a purple hill.|The sun went away.|It was there.|Sun is hot.|Descriptive words create pictures.
10.E|3|"I went to the lake with my dad." Who is telling the story?|a person using "I" (first person)|a stranger|a bird|nobody|"I" shows first person.
10.E|3|"Lena went to the lake with her dad." This story is told in...|third person|first person|second person|no person|It uses her name and "her."
11.B.i|3|Which sentence belongs at the start of a story about a lost puppy?|One day, Sam's puppy ran away.|The end.|Then they all went home.|Puppies are soft.|A beginning introduces the problem.
11.B.ii|3|Which sentence adds a good detail about a dog?|The dog has long, soft brown fur.|The dog is a dog.|I like it.|Dogs.|Specific details add meaning.
11.C|3|Ana writes, "I like my cat." How can she add a detail?|I like my fluffy gray cat.|I like cat.|My my cat.|Cat I like.|A describing word adds a detail.
11.D.i|2|Which sentence is correct?|The dogs run.|The dogs runs.|The dog run.|The dog are.|The subject and verb must agree.
11.D.i|3|Which sentence is correct?|She plays outside.|She play outside.|They plays outside.|We plays outside.|Singular subjects use plays.
11.D.ii|2|Which sentence is in the past?|We walked to school.|We walk to school.|We will walk to school.|We walking.|Walked is past tense.
11.D.ii|3|Which sentence is in the present?|The cat jumps on the bed.|The cat jumped on the bed.|The cat will jump.|The cat had jumped.|Jumps is present tense.
11.D.iii|2|Which word is a proper noun?|Texas|state|city|river|Proper nouns name a specific place.
11.D.iii|3|Which is the plural of "box"?|boxes|boxs|boxies|boxen|Add es to words ending in x.
11.D.iv|2|Which word is an adjective?|fluffy|run|and|under|Fluffy describes a noun.
11.D.iv|3|Which sentence uses the article "an" correctly?|I ate an apple.|I ate an banana.|I ate an pear.|I ate an bread.|An comes before a vowel sound.
11.D.v|3|Which word tells WHEN?|yesterday|quickly|loudly|softly|Yesterday tells time.
11.D.v|3|Which sentence has an adverb of time?|We will go soon.|We saw a red car.|The cat is soft.|She has a hat.|Soon tells when.
11.D.vi|3|Which word is a preposition?|beside|happy|sing|apple|Beside shows position.
11.D.vi|3|Which sentence has a preposition?|The book is on the shelf.|The cat is soft.|Sam sings.|We run fast.|On is a preposition.
11.D.vii|2|Which pronoun can replace "Maria and Jose"?|they|he|she|it|They replaces two people.
11.D.vii|3|Choose the right word: "Give the ball to ___."|me|I|my|mine's|Me is the object form.
11.D.viii|2|Which word needs a capital letter? "my friend and i like to play."|my|friend|like|play|The first word of a sentence needs a capital.
11.D.viii|3|Where does a capital letter belong in a sentence like "we ate pizza."?|on the first word|on the last word|on every word|on no word|The first word of a sentence needs a capital.
11.D.ix|2|Which sentence ends correctly as a question?|Where is my hat?|Where is my hat.|Where is my hat!|Where is my hat,|A question ends with a question mark.
11.D.ix|3|Which sentence shows excitement?|We won the game!|We won the game.|We won the game?|We won the game,|An exclamation mark shows strong feeling.
11.D.x|3|Which word is spelled correctly?|train|trane|trayn|trian|Train uses the ai team.
11.D.x|3|Which word is spelled correctly?|night|nite|nigt|niht|Night has igh.
12.A|3|Which is a good start for a personal story?|Last summer, I went to the beach.|Beaches are made of sand.|There are 7 days.|Sand.|A personal narrative tells about your own life.
12.B|3|A how-to text should have steps in...|order|rhyme|a mix|reverse|Steps need an order.
12.C|3|Which is a good end to a thank-you note?|Thank you for the gift! Love, Sam|The end.|Bye bye bye.|Gift gift.|A thank-you note says thanks and signs off.
12.C|3|Which is the greeting of a letter?|Dear Grandma,|Love, Sam|Thank you!|The end.|A letter starts with Dear and a name.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g1_ela.jsonl'))
print("saved", len(B.out), "questions")

#!/usr/bin/env python3
"""Kindergarten ELA (TEKS 110.2.b) - original questions, hand written. Skips standards that cannot be tested with multiple choice
(handwriting 2.E, independent reading time 4, drafting/sharing/research 10.A-B/E, 11, 12)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('110.2.b.', 901, own='gk_ela.jsonl')

load(B, """
1.A|2|Your teacher asks a question. What is a good way to listen?|look at the speaker and stay quiet|talk to a friend|look at the floor|run around|Good listeners look and listen.
1.A|2|After a story, you do not understand a word. What can you do?|ask a question|say nothing|walk away|cover your ears|Asking a question helps you understand.
1.A|3|Which answer uses more than one word?|I like the red ball.|Yes|Ball|Red|A multi-word answer says more than one word.
1.B|2|Your teacher says, "Put on your jacket, then line up." What do you do first?|wear your jacket|stand in line|sit down|sing|Follow the steps in order.
1.B|3|Your teacher says, "Open your book and point to the picture." What do you do second?|touch the picture|open your book|close your book|stand up|The second step is pointing.
1.C|2|When you share an idea, how should you speak?|clearly and loud enough to hear|in a whisper|with your hand over your mouth|very fast|Speak so others can hear you.
1.C|3|Which is a complete idea to share?|I have a brown dog.|brown|dog the|have a|A complete idea has a who and a what.
1.D|2|When a class is talking together, what is a good rule?|take turns|talk at the same time|grab things|yell|Taking turns is a discussion rule.
1.D|2|Two friends both want to talk. What should they do?|one talks and then the other|both talk at once|neither listens|leave|Take turns.
1.E|2|Which is a greeting?|Hello|Goodbye|Stop|Thank you|Hello is a greeting.
1.E|2|You meet a new child. What can you say?|Hi, my name is Sam.|Go away.|Give me that.|Be quiet.|Introduce yourself kindly.
1.E|3|You are thirsty. What can you say to show what you need?|May I have some water, please?|Water is wet.|I like rain.|Look at me.|Say what you need politely.
2.A.i|2|Which word rhymes with cat?|hat|dog|cup|pen|Cat and hat end with -at.
2.A.i|2|Which word rhymes with sun?|run|moon|star|pig|Sun and run end with -un.
2.A.i|3|Which pair of words rhyme?|bed, red|bed, bat|red, rug|top, cup|Bed and red end the same.
2.A.ii|2|Which word starts with the same sound as ball?|bat|cat|dog|fish|Ball and bat both start with /b/.
2.A.ii|3|Which two words begin with the same sound?|sun, sock|sun, hat|sock, pig|hat, pig|Sun and sock both start with /s/.
2.A.iii|2|Listen: "I like pie." How many words do you hear?|3|2|4|1|I, like, pie are three words.
2.A.iii|3|Listen: "The dog ran fast." How many words do you hear?|4|3|5|2|The, dog, ran, fast.
2.A.iv|2|How many syllables (claps) are in the word "table"?|2|1|3|4|ta-ble has two parts.
2.A.iv|2|How many syllables are in "elephant"?|3|2|1|4|el-e-phant has three parts.
2.A.iv|3|Which word has one syllable?|dog|puppy|banana|window|Dog has one beat.
2.A.v|2|Blend these two parts: pen (first part), cil (second part). What word is it?|pencil|pickle|pencel|panel|Pen and cil make pencil.
2.A.v|3|Blend these two parts: bas (first part), ket (second part). What word is it?|basket|bucket|ballet|bracket|Bas-ket is basket.
2.A.vi|2|Break the word "sunset" into two parts.|sun and set|su and nset|suns and et|s and unset|Sunset has sun and set.
2.A.vi|3|Break the word "monkey" into parts.|mon and key|mo and nkey|monk and ey|m and onkey|Monkey is mon-key.
2.A.vii|2|Blend the sounds /c/ and /at/. What word is it?|cat|cap|cut|can|C plus at makes cat.
2.A.vii|3|Blend /m/ and /op/. What word is it?|mop|map|top|hop|M plus op makes mop.
2.A.viii|3|Blend the sounds /s/ /u/ /n/. What word is it?|sun|sit|sin|nut|The sounds make sun.
2.A.viii|3|Blend /p/ /i/ /g/. What word is it?|pig|pin|big|peg|The sounds make pig.
2.A.ix|3|Say "butterfly." Now take away "butter." What is left?|fly|but|ter|butt|Without butter you have fly.
2.A.ix|3|Say "cupcake." Take away "cup." How many parts are left?|one|two|three|none|Without cup you have cake.
2.A.x|3|How many sounds are in the word "cat"?|3|2|4|1|The sounds are /c/ /a/ /t/.
2.A.x|3|How many sounds are in the word "sit"?|3|2|4|5|The sounds are /s/ /i/ /t/.
2.B.i|2|Which letter makes the /m/ sound?|m|n|w|r|The letter m says /m/.
2.B.i|2|Which letter makes the first sound in "sun"?|s|n|u|t|Sun starts with the letter s.
2.B.i|3|Which letter makes the sound at the end of "dog"?|g|d|o|b|Dog ends with /g/.
2.B.ii|2|Read the word: c-a-t. What does it say?|cat|cut|cot|can|The letters spell cat.
2.B.ii|3|Which word can you read with the sounds /h/ /a/ /t/?|hat|hot|hit|hut|The word is hat.
2.B.ii|3|Which word has the sounds /b/ /e/ /d/?|bed|bad|bud|bid|The word is bed.
2.B.iii|3|Change the first letter of "cat" to "b." What new word do you make?|bat|bit|cot|but|Bat is cat with a b.
2.B.iii|3|Change the last letter of "pin" to "g." What new word do you make?|pig|pit|pan|pen|Pin becomes pig.
2.B.iv|2|Which is a word you read often: the, a, I?|the|tuk|xqz|plim|The is a common word.
2.B.iv|2|Which word says "and"?|and|any|out|add|The word and is spelled a-n-d.
2.B.iv|3|Which is a high-frequency word?|said|zebra|giraffe|volcano|Said is a very common word.
2.C.i|3|Which is the correct spelling of the word for a pet that says meow?|cat|kat|catt|cet|Cat is spelled c-a-t.
2.C.i|3|Which spells the animal that barks?|dog|dag|dgo|doog|Dog is spelled d-o-g.
2.C.ii|3|Which word is spelled right?|sun|sunn|son|zun|Sun uses s-u-n.
2.C.iii|3|Which is spelled correctly?|the|thu|teh|tha|The is spelled t-h-e.
2.C.iii|3|Which spells "see"?|see|sea|ce|sse|See is spelled s-e-e.
2.D.i|2|Where do you find the title of a book?|on the front cover|on the back of your hand|on the last page only|in the table|The title is on the front cover.
2.D.i|3|Which part of a book is the very back?|the back cover|the title page|the front cover|the first page|The back cover is the last outside part.
2.D.ii|2|How do you hold a book to read it?|right side up|upside down|sideways|behind you|A book is read right side up.
2.D.ii|3|In which direction do we read a line of words?|left to right|right to left|bottom to top|in a circle|English is read left to right.
2.D.ii|3|When a line of words ends, where do your eyes go?|to the start of the next line|to the cover|up a line|nowhere|This is called a return sweep.
2.D.iii|2|What separates words in a sentence?|spaces|numbers|colors|pictures|Words have spaces between them.
2.D.iii|3|How many words are in "I see a bird"?|4|3|5|1|I, see, a, bird.
2.D.iv|2|Which is a letter?|b|bat|bat sat|big cat|A letter is one symbol.
2.D.iv|3|Which is a printed word?|run|r|u|n|Run is a word; r, u, n are letters.
2.D.v|2|Which is the uppercase form of "d"?|D|b|P|q|D is uppercase d.
2.D.v|2|Which is the lowercase form of "A"?|a|e|o|u|a is lowercase A.
2.D.v|3|Which two letters are the same letter, big and small?|G and g|G and j|B and d|M and n|G and g are the same letter.
3.A|2|You do not know how to spell a word. What can help?|a picture dictionary|a spoon|a rock|a coat|A picture dictionary shows words.
3.A|3|Which tool can help find a new word?|a picture dictionary|a ruler|a pencil box|a clock|Dictionaries list words.
3.B|2|A page says "The kitten is tiny" and shows a kitten that fits in a hand. What does tiny mean?|very small|very loud|very fast|very big|The picture shows small.
3.B|3|The page shows a boy with a big smile. The text says he is "happy." What does happy mean?|glad|sleepy|hungry|cold|The smile shows glad.
3.C|2|Which word names an action?|jump|red|happy|table|Jump is something you do.
3.C|2|Which word tells where something is?|under|green|laugh|apple|Under tells a position.
3.C|3|Which word is a color?|blue|ball|run|round|Blue is a color.
3.C|3|Which word names a shape?|circle|swim|purple|soft|Circle is a shape.
5.A|2|Why might you read a book about frogs?|to learn about frogs|to cook dinner|to play ball|to wash your hands|A purpose is to learn.
5.A|3|You pick a funny story. What is your purpose?|to enjoy it|to learn to drive|to count money|to sleep|You read to enjoy.
5.B|3|Before reading a book about bees, which question could you ask?|What do bees eat?|What color is my shoe?|How tall is the moon?|When is lunch?|It fits the topic.
5.C|3|The cover shows a dog with a leash. What might the book be about?|a walk with a dog|a rocket|a big storm|baking a cake|The cover gives a clue.
5.C|3|You read "Ana packs her bag for the beach." What might happen next?|she goes to the beach|she goes to the moon|she bakes bread|she sleeps all day|It fits the story.
5.D|3|"The sun was a big, warm ball." What picture do you make in your mind?|a round yellow sun|a square box|a cold ice cube|a tiny seed|The words describe the sun.
5.E|2|A story is about a girl who loses her toy. What can you think about?|a time you lost something|what to eat for lunch|how to spell dog|the color red|That connects to your life.
5.F|3|Tom has a wet coat and an umbrella. What can you tell?|it was raining|it was snowy|it was hot|it was night|The clues show rain.
5.F|3|Sam is yawning and rubbing his eyes. How does Sam feel?|sleepy|angry|hungry|loud|Yawning shows sleepy.
5.G|3|A story says a boy is lost, then finds his mom. What is most important?|he found his mom|he wore a hat|it was Monday|there was a tree|Finding mom is the key part.
5.H|3|You read that bees make honey and honey is sweet. What do you learn?|bees make something sweet|bees are red|honey is cold|bees have wheels|Combine the facts.
5.I|2|You are reading and it stops making sense. What can you do?|read it again|close your eyes|throw the book|stop forever|Rereading helps.
5.I|3|You do not know a word. What can help you?|look at the picture|guess a color|skip every page|turn the book over|Pictures give clues.
6.A|2|A story is about a family dinner. What can you share?|a time you ate with family|the date of the moon|how to fix a car|nothing|You can connect.
6.C|3|The story says Max is sad because his toy broke. How do you know Max is sad?|the story says so|the title is long|the page is white|the book is big|Text evidence shows it.
6.C|3|Why did Lily wear boots? "It was raining, so Lily wore boots." The answer is...|because it was raining|because it was hot|because she was happy|because it was night|The text gives the reason.
6.D|2|Which tells the story of "The Three Pigs" in order?|pigs build houses, wolf comes, pigs are safe|wolf wins, pigs build, pigs sing|pigs sleep, wolf sleeps, end|houses fall, pigs build, wolf builds|Retell in order.
6.D|3|Retelling a story means...|telling it again in your own words|changing the whole story|drawing a house|reading the title|Retell keeps the meaning.
7.A|3|In a story, a girl shares her snack and makes a friend. What is the lesson?|sharing is kind|never eat|friends are bad|snacks are red|The theme is sharing.
7.B|2|Who is the main character in "Ben went to the park. Ben played on the swings."?|Ben|the park|the swings|the day|Ben is the one the story is about.
7.B|2|Which tells about a character?|A brave girl named Rosa|The tall green tree|The rainy sky|A red barn|Rosa is a character.
7.C|2|In a story, what is the problem?|what goes wrong|the title|the last word|the cover|The problem is what needs fixing.
7.C|3|A kitten is stuck in a tree. A boy gets it down. What is the resolution?|the boy gets the kitten down|the kitten is stuck|the tree is tall|the kitten meows|The resolution fixes the problem.
7.C|3|Read: "Jack lost his hat. He looked everywhere. He found it under his bed." What happens FIRST?|a hat goes missing|a search begins|the hat is found|a bed is checked|The story begins with the hat lost.
7.D|2|"The story happens in a forest at night." What is the setting?|the woods in the dark|a boy|a dog|a bear|Setting is where and when.
7.D|3|The setting of a story tells...|where and when it happens|who is the hero|the title|the author|Setting is place and time.
8.A|2|Which is a nursery rhyme?|Twinkle, Twinkle, Little Star|a phone book|a recipe|a weather report|It is a short rhyme for children.
8.A|3|A story where animals talk and teach a lesson is called a...|fable|map|menu|sign|A fable has a lesson.
8.A|3|"Once upon a time, a princess..." begins what kind of story?|a fairy tale|a science book|a news report|a map|Fairy tales often start that way.
8.B|2|Which words rhyme in a poem?|cat and hat|cat and dog|hat and sun|dog and bird|Rhyming words sound alike at the end.
8.B|3|A poem has a beat you can clap. What is that called?|rhythm|spelling|title|cover|Rhythm is the beat.
8.C|3|In a play, who talks and acts?|the characters|the cover|the page numbers|the glue|Characters speak in drama.
8.D.i|3|A book about dogs says, "Dogs need food, water, and love." What is it mostly about?|what dogs need|how to bake|space travel|football|The central idea is dogs' needs.
8.D.ii|2|Where can you find what a nonfiction book is called?|the title|the last word|the page number|a picture of a bee|The title names the book.
8.D.iii|3|To brush teeth: first wet the brush, then add paste, then scrub. What comes first?|get the brush wet|add paste|scrub|rinse|Wetting the brush is the first step.
8.E|3|A sign says, "Wash your hands!" What does it want you to do?|clean your hands|run fast|eat lunch|clap|It is trying to persuade you.
8.F|3|Which is a digital text?|a story on a tablet|a rock|a spoon|a shoe|Digital texts are on screens.
9.A|2|Why do authors write books about animals?|to teach or tell about animals|to sell shoes|to fix cars|to cook|Authors write to inform.
9.A|3|A funny story is written mostly to...|entertain|measure|warn about storms|sell food|Funny stories entertain.
9.B|3|A book tells steps in order, first, next, last. What is it teaching?|how to do something|a silly rhyme|a joke|a scary tale|Steps teach a process.
9.C|2|Bold words in a book help you...|see important words|forget words|skip pages|lose the story|Bold stands out.
9.C|3|A picture with a label helps you...|know what the picture shows|hide the picture|turn the page|spell your name|Labels name things.
9.D|3|Which sentence helps you see a picture in your mind?|The shiny red apple rolled down the hill.|It was a thing.|Go.|Yes.|Descriptive words help you visualize.
9.E|3|"I went to the store." Who is telling the story?|I (first person)|he|she|they|I tells it in first person.
9.E|3|"She went to the store." Who is the story about?|another person (third person)|the speaker|the reader|nobody|She is third person.
10.C|3|Ana writes, "I have a dog." How can she add a detail?|I have a big brown dog.|I dog.|Have dog a.|A dog.|Details add describing words.
10.D.i|2|Which is a complete sentence?|The dog runs.|The dog|runs fast|big red|A complete sentence has a who and a what.
10.D.i|3|Which is NOT a complete sentence?|a big cat|The cat sleeps.|I see a bird.|We play.|It is missing an action.
10.D.ii|2|Which word is a verb?|jump|tree|pink|cup|Verbs are actions.
10.D.ii|3|Which word is a verb?|sing|bird|blue|big|Sings is the action.
10.D.iii|2|Which word means more than one?|dogs|dog|cat|bird|Add s for many.
10.D.iii|3|Which is plural?|boxes|box|cat|one|Boxes means more than one.
10.D.iv|2|Which is an adjective, a word that describes?|big|run|go|and|Big describes a noun.
10.D.iv|3|Which word is an article?|the|run|red|fast|The is an article.
10.D.v|3|Which word is a preposition?|on|dog|big|run|On shows where.
10.D.v|3|Which sentence has a word that tells where?|The cat is under the table.|The cat is big.|The cat is happy.|The cat is sleepy.|Under is a preposition.
10.D.vi|2|Which word can take the place of "Sam"?|he|it|they|we|He replaces Sam.
10.D.vi|3|Which is a pronoun?|she|mat|jump|blue|She replaces a girl's name.
10.D.vii|2|Which sentence starts with a capital letter?|The sun is hot.|sun hot is the|a dog barks|my cat|The first word needs a capital.
10.D.vii|3|Look at these words: dog, max, run, big. Which one should start with a capital letter?|max|dog|run|big|Names start with a capital.
10.D.viii|2|What goes at the end of a telling sentence?|a period|a question mark|a comma|a star|A period ends a statement.
10.D.viii|3|Which sentence ends correctly?|I like pizza.|I like pizza|I like pizza?|I like pizza,|A telling sentence ends with a period.
10.D.ix|3|Which is spelled correctly?|and|nad|adn|ann|And is spelled a-n-d.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'gk_ela.jsonl'))
print("saved", len(B.out), "questions")

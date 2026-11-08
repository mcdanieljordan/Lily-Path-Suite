#!/usr/bin/env python3
"""Grade 2 ELA (TEKS 110.4.b) - original questions, hand written. Skips speaking/listening (1), cursive handwriting (2.E), independent reading (4/5),
publishing and research (13)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('110.4.b.', 903, own='g2_ela.jsonl')

load(B, """
2.A.i|2|Which list has only rhyming words?|light, night, right|light, lamp, lift|hill, hall, hull|rain, ran, run|Words that rhyme end with the same sound.
2.A.ii|3|Which word has a long vowel sound?|time|tin|trip|tub|Time has the long i sound.
2.A.ii|3|Which word has a short vowel sound?|plug|plume|plain|pail|Plug has the short u sound.
2.A.iii|3|Say "plate." Change /p/ to /s/. What word do you hear?|slate|plane|plant|spate|Plate with /s/ in place of /p/ is slate.
2.A.iii|3|Say "stamp." Take away /t/. What word is left?|samp|stap|tamp|ampt|Without /t/ you say samp.
2.A.iv|3|Say "block." Change /l/ to /r/. What word do you say?|brock|black|blink|bleak|Replacing l with r gives brock.
2.B.i|3|Which word has a variant vowel sound like "oo" in "moon"?|spoon|spot|sport|spin|Spoon has the oo sound.
2.B.i|3|Which word has a trigraph at the beginning?|three|thin|then|that|Three begins with the three-letter blend thr.
2.B.ii|3|Which word has a silent letter?|knife|kind|kit|king|The k is silent in knife.
2.B.ii|3|Which word has a silent "g"?|gnat|goat|game|gift|The g is silent in gnat.
2.B.iii|3|Which word has a closed syllable?|pocket|motor|paper|tiger|The first syllable in pocket is closed.
2.B.iii|3|Which word has a VCe syllable?|bake|bat|bag|bar|Bake follows the vowel-consonant-e pattern.
2.B.iv|3|Which word is a compound word?|rainbow|rainy|rained|raining|Rainbow joins rain and bow.
2.B.iv|3|The contraction for "do not" is...|don't|dont|do'nt|d'not|Don't uses an apostrophe for the missing o.
2.B.v|3|How can you split the word "rabbit" into syllables?|rab and bit|ra and bbit|r and abbit|rabb and it|Rabbit splits between the two b's.
2.B.vi|3|What does the prefix un- mean in "unlock"?|not or opposite of|again|before|more|Un- means not.
2.B.vi|3|What does the prefix re- mean in "redo"?|again|not|after|under|Re- means again.
2.B.vii|3|Which is a word readers see often?|would|zibble|thrang|plomp|Would is a high-frequency word.
2.C.i|3|Which word is spelled correctly?|float|flote|floot|flowt|Float uses the oa team.
2.C.ii|3|Which word is spelled correctly?|knee|nee|kne|knea|Knee has a silent k.
2.C.iii|3|Which word is spelled correctly?|everywhere|everywear|evrywhere|everwhere|Everywhere is a compound word.
2.C.iii|3|Which contraction is spelled correctly?|can't|cant|ca'nt|can'tt|Can't has the apostrophe after n.
2.C.iv|3|Which is spelled correctly?|beautiful|beutiful|beautifull|butiful|Beautiful has eau and ful.
2.C.v|3|Which word is spelled correctly?|rabbit|rabit|rabbitt|rabbet|Rabbit doubles the b.
2.C.vi|3|Which word is spelled correctly?|unhappy|unnhappy|unhapy|onhappy|Unhappy adds un- to happy.
3.A|2|Which tool tells you how to say a word and what it means?|a dictionary|a ruler|a calendar|a map|A dictionary gives pronunciation and meaning.
3.A|3|A glossary in a book is found...|at the back and lists important words|on the cover|inside a picture|next to the title|A glossary explains key words.
3.B|3|"The huge elephant stomped. It was gigantic." What does gigantic mean?|very big|very small|very quiet|very pretty|The sentence says huge.
3.B|3|"Mia was famished after the long hike, so she ate three sandwiches." What does famished mean?|very hungry|very cold|very sleepy|very happy|The sandwiches show she was hungry.
3.C|2|What does the suffix -ful mean in "careful"?|full of|without|again|not|-ful means full of.
3.C|3|What does the suffix -less mean in "hopeless"?|without|full of|again|more|-less means without.
3.C|3|What does the prefix dis- mean in "disagree"?|not|again|before|more|Dis- means not.
3.D|3|Which word is a synonym for "big"?|large|tiny|slow|quiet|Large means the same as big.
3.D|3|Which word is an antonym of "hot"?|cold|warm|boiling|sunny|Cold is the opposite of hot.
3.D|3|Which pair are homophones?|two, too|two, ten|to, go|too, tub|Two and too sound alike.
3.D|3|"I need to check the bark of the tree." Bark here means...|the rough outside of a tree|a dog sound|a ship|a song|Bark can mean tree covering.
6.A|2|Why might you read a book of animal facts before a zoo trip?|to learn about the animals|to hear a rhyme|to practice jumping|to draw a car|The purpose is to learn.
6.B|3|You are about to read about volcanoes. Which question helps?|What makes a volcano erupt?|What is my shoe size?|Who won the race?|Why is the grass green?|It fits the topic.
6.C|3|The title is "The Snowy Day." The cover shows a boy in boots. What do you predict?|the boy plays in the snow|the boy swims in a pool|the boy bakes in the sun|the boy flies a plane|The cover and title give clues.
6.D|3|"The sky was a deep purple as the sun melted into the hills." What do you picture?|a sunset|a sunrise at noon|a rainstorm|a snowfall|The words describe sunset.
6.E|3|A story about moving to a new school reminds you of your first day. This is...|a connection|a prediction|a rhyme|a glossary|You linked it to your life.
6.F|3|Sam grabs a towel and runs to the lake. What can you infer?|He plans to swim.|He is cooking.|He is sleeping.|He is reading.|The towel and lake suggest swimming.
6.G|3|Read: "Seeds need water, light, and soil to grow." What is the key idea?|what seeds need to grow|how to build a house|what dogs eat|why the sky is blue|The sentence names needs.
6.H|3|One page says frogs lay eggs in water. Another says tadpoles breathe with gills. What can you conclude?|frogs start life in water|frogs live only on land|tadpoles can not swim|frogs never lay eggs|Combining facts shows water is first.
6.I|3|You read a paragraph and are confused. What should you try?|reread it and think about what it says|skip to the end|close the book|guess every word|Rereading helps.
7.A|2|A story about a lost puppy makes you think of your pet. What is this?|a personal connection|a rhyme|a heading|a title|You linked it to your life.
7.B|3|Which is a good brief comment about a book?|I liked how the story showed friendship.|Book.|It has pages.|I read.|A comment gives an idea.
7.C|3|Why did the child cry? "Jo cried because her kite broke." Where is the evidence?|in the sentence about the kite|in the title only|in the picture frame|on the page number|The sentence tells the reason.
7.D|3|Which is the best paraphrase of "The bright sun warmed the whole village"?|The sun made the village warm.|The sun left the village.|The village was dark.|The sun was cold.|A paraphrase keeps the meaning.
7.D|3|When you retell a story, you should include...|the beginning, middle, and end|only the title|only the ending|only the characters' names|A retell has the key parts.
8.A|3|A boy keeps trying to ride a bike and finally succeeds. What is the theme?|never give up|bikes are red|boys are fast|riding is easy|The theme is perseverance.
8.B|3|Lila is nervous but still speaks to the class. What does this show?|she is brave|she is lazy|she is angry|she is bored|Her action shows bravery.
8.C|3|In a story, the problem is solved at the end. This part is the...|resolution|setting|title|character|The resolution solves the problem.
8.D|3|Why is the setting "a dark cave" important to a scary story?|it adds mood and suspense|it makes the story short|it tells the author's name|it shows the page number|Setting affects the feeling.
9.A|3|A story where animals talk and a lesson is taught is a...|fable|biography|recipe|map|Fables have morals.
9.A|3|A story that starts "Once upon a time" and has magic is a...|fairy tale|science book|news article|dictionary|Fairy tales often include magic.
9.B|3|A poem is shaped like a tree on the page. What does this do?|helps show the topic|hides the poem|changes the rhyme|makes it a recipe|Shape poems show the subject.
9.C|3|In a play, the words the characters say are called...|dialogue|setting|plot|prefixes|Dialogue is spoken words.
9.D.i|3|A text says, "Owls hunt at night. They have great eyesight. They hear small sounds." What is the central idea?|how owls hunt|how to bake|a day at school|how cars work|All sentences are about owls hunting.
9.D.ii|3|Where would you look to find where a section on "Habitats" begins?|the table of contents|the glossary only|the cover only|the last word|The table of contents lists sections.
9.D.iii|3|A text explains that because it rained, the grass grew. The text structure is...|cause and effect|compare and contrast|rhyme|dialogue|It shows why something happened.
9.E.i|3|An ad says, "Buy our juice! It is the best!" What does it want you to do?|buy the juice|plant a tree|read a poem|go to sleep|The ad tries to persuade you.
9.E.ii|3|Which sentence is a fact?|A giraffe is the tallest land animal.|Giraffes are the prettiest animals.|Giraffes are boring.|Giraffes should be pets.|A fact can be proven.
9.E.ii|3|Which sentence is an opinion?|Pizza is the yummiest food.|Pizza has cheese.|Pizza is round.|Pizza is baked in an oven.|An opinion tells a feeling.
9.F|3|Which is a digital text?|a web page with a video|a rock|a leaf|a spoon|Digital texts are on screens.
10.A|3|Why did the author write a book called "How to Plant a Garden"?|to teach readers|to tell a joke|to scare readers|to sell toys|The purpose is to inform.
10.B|3|A book lists steps in order. This structure helps the author...|teach how to do something|tell a ghost story|write a poem|trick readers|Steps explain a process.
10.C|3|What does a diagram with labels help the reader do?|understand the parts of something|forget the text|skip pages|guess|Labels name parts.
10.D|3|"The wind whispered through the trees." This uses...|figurative language|a number|a list|a date|Wind does not really whisper.
10.D|3|Which phrase is figurative?|as busy as a bee|a red pencil|ten dogs|a big box|It compares a person to a bee.
10.E|3|"I felt happy when I won." Which point of view is this?|first person|third person|second person|none|It uses I.
10.E|3|"She felt happy when she won." Which point of view is this?|third person|first person|second person|none|It uses she.
10.F|3|The poem says "Run, run, run, as fast as you can." What is repeated?|the word run|the word fast|the word can|the word as|Run appears three times.
11.B.i|3|Which sentence is a good topic sentence for a paragraph about dogs?|Dogs make great pets.|Dogs.|I have shoes.|It is Monday.|A topic sentence tells the main idea.
11.B.ii|3|Which detail best supports "Dogs make great pets"?|They are loyal and friendly.|The sky is blue.|Cats are small.|Pizza has cheese.|Details back up the main idea.
11.C|3|Which revision adds a good detail to "The boy ran."?|The tall boy ran across the muddy field.|The boy.|Ran boy the.|The boy ran ran.|Adding details improves a sentence.
11.D.i|2|Which sentence has the verb that agrees?|The birds sing.|The birds sings.|The bird sing.|The bird are singing.|Plural subjects use sing.
11.D.ii|3|Which sentence uses the future tense?|We will play tomorrow.|We played yesterday.|We play now.|We have played.|Will play is future.
11.D.ii|3|Which word completes the sentence in the past? "Yesterday, I ___ to the store."|walked|walk|will walk|walking|Walked is past tense.
11.D.iii|3|Which word is a common noun?|city|Austin|Texas|Monday|City is a general noun.
11.D.iii|3|Which shows the plural of "child"?|children|childs|childes|childen|Child has an irregular plural.
11.D.iv|3|Which sentence uses an adjective?|The tall tree fell.|The tree fell.|It fell.|Trees fall.|Tall describes the tree.
11.D.v|3|Which word is an adverb that tells where?|outside|slowly|yesterday|happy|Outside tells where.
11.D.v|3|Which word is an adverb that tells when?|tomorrow|quietly|there|softly|Tomorrow tells when.
11.D.vi|3|Which phrase is a prepositional phrase?|under the table|the red car|ran fast|big and loud|A prepositional phrase begins with a preposition.
11.D.vii|3|Choose the right pronoun: "___ is my friend."|She|Her|Hers|Hers's|She is a subject pronoun.
11.D.vii|3|Which is a possessive pronoun?|their|they|them|then|Their shows ownership.
11.D.viii|3|Which sentence uses a coordinating conjunction to join two subjects?|Sam and Ana ran.|Sam ran fast.|Ana ran.|Running is fun.|And joins Sam and Ana.
11.D.viii|3|Which word is a coordinating conjunction?|but|under|tall|slowly|But joins ideas.
11.D.ix|3|Which of these needs a capital letter?|the name of a month|the word "the"|any verb|every adjective|Months and days of the week are capitalized.
11.D.ix|3|Which punctuation mark ends the greeting in a friendly letter?|a comma|a period|a question mark|a colon|A greeting ends with a comma.
11.D.x|3|Which is written correctly?|I can't go.|I cant go.|I ca'nt go.|I can't' go.|Can't uses an apostrophe.
11.D.x|3|Which sentence uses commas in a list correctly?|I like apples, grapes, and pears.|I like apples grapes, and pears.|I like, apples grapes and pears.|I like apples, grapes and, pears.|Commas separate items in a list.
11.D.xi|3|Which word is spelled correctly?|weigh|wey|waigh|whey|Weigh uses eigh.
12.A|3|Which is a good start for a personal narrative?|Last winter, I learned to skate.|Skates are made of metal.|There are four seasons.|Ice is cold.|A personal narrative tells about your own life.
12.B|3|A how-to paragraph about brushing teeth should include...|steps in order|a rhyme|a joke|a list of colors|Procedural texts use sequence.
12.C|3|A thank-you note should include...|a greeting, a thank you, and a closing|a map|a long story only|just the date|These are the parts of a note.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g2_ela.jsonl'))
print("saved", len(B.out), "questions")

#!/usr/bin/env python3
"""Grade 4 ELA (TEKS 110.6.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('110.6.b.', 905, own='g4_ela.jsonl')

load(B, """
2.A.i|3|Which is the plural form of "child"?|children|childs|childes|childen|Child has an irregular plural.
2.A.i|3|Which is the correct plural of "knife"?|knives|knifes|knifs|knifies|Words ending in fe often change to ves.
2.A.ii|3|How many syllables are in the word "fantastic"?|3|1|2|4|Fan-tas-tic has three parts.
2.A.iii|4|Which shows the correct syllable division?|nap-kin|na-pkin|napk-in|n-apkin|Divide between two consonants.
2.A.iv|3|Which word has the prefix "pre-"?|preview|present|pretty|prefer|Preview means to view before.
2.A.v|3|Which word has a base word plus the suffix -ful?|thankful|cheerless|unkind|rewrite|Thank plus -ful.
2.A.vi|2|Which word is a high-frequency word that should be read quickly by sight?|because|xylophone|oxygen|aquarium|Because appears very often in text.
2.B.i|3|Which word is spelled correctly?|basket|baskit|baskett|basckit|Closed syllables bas-ket.
2.B.ii|3|Which word correctly completes the sentence? "We ate our ___ at the picnic."|meat|meet|mete|mete's|Meat is food.
2.B.iii|4|Which word is spelled correctly?|thought|thawt|thoght|thouht|Thought uses the ough pattern.
2.B.v|3|Which word is spelled correctly?|unhappy|unhapy|unhappey|onhappy|Un- plus happy keeps both p letters.
2.B.vi|3|What is the correct spelling when you add -ing to "hop"?|hopping|hoping|hoppeing|hopeing|Double the consonant after a short vowel.
2.B.vi|3|What is the correct spelling when you add -ed to "carry"?|carried|carryed|caried|carryd|Change y to i before -ed.
3.A|3|Which part of a dictionary entry tells how to say a word?|the pronunciation key|the page number|the cover|the date|Pronunciation shows how to say it.
3.B|3|"The scientist was meticulous, checking every measurement twice." What does meticulous mean?|very careful|careless|sleepy|loud|Checking twice shows great care.
3.B|3|Read: "The bat flew out of the cave." and "He swung the bat at the ball." What is the best way to tell which meaning is used?|read the words around it|guess|skip it|look at the cover|Context shows the right meaning.
3.B|4|"After the long hike, the travelers were famished and ate everything at the table." What does famished mean?|very hungry|very tired|very cold|very wet|They ate everything.
3.C|3|The root "graph" means write. What does "autograph" most likely mean?|a person's own signature|a type of car|a long walk|a picture of food|Auto means self.
3.C|3|The suffix -ment means "the act or result of." What does "enjoyment" mean?|the result of enjoying|not enjoying|enjoying again|before enjoying|Add -ment to enjoy.
3.C|4|What does the root "meter" mean in "thermometer"?|measure|hot|write|self|Meter means measure.
3.D|3|Which sentence uses the homophone correctly?|The king began his reign.|The king began his rain.|The king began his rein.|The king began his reen.|Reign means to rule.
6.A|3|Before reading a chapter on volcanoes for homework, what purpose could a student set?|to learn how volcanoes erupt|to count the pages|to copy the title|to find a rhyme|A purpose guides reading.
6.B|3|Which question helps a reader deepen understanding while reading a story about a lost dog?|Why did the dog leave home?|What color is my desk?|Who is next?|How tall is a tree?|It connects to the text.
6.C|3|A mystery's chapter ends with a locked door and a strange sound. Which prediction is best?|someone will open the door|the story is over|the author will change|a clock will talk|Details suggest the next event.
6.D|3|Which sentence helps a reader create a clear mental image?|The dusty barn leaned to one side, its red paint peeling in long strips.|The barn was a barn.|It was old.|There was a thing.|Sensory detail builds images.
6.E|3|A reader connects a story's theme about courage to a news report about a rescue. This is a connection to...|society|spelling|math|punctuation|It links to the world.
6.F|4|Read: "Jada checked her watch again and again as the bus failed to arrive." What can you infer?|she is worried about being late|she loves buses|she lost her watch|she is asleep|Repeated checking shows worry.
6.G|3|Which detail is most important for the key idea of an article about how penguins stay warm?|they huddle together|penguins like fish|some live in zoos|ice is white|Huddling is how they stay warm.
6.H|4|One article says honeybees make honey, and another says bees pollinate crops. What new understanding could a reader build?|bees are useful in two ways|bees are useless|honey grows crops|crops make bees|Combining the facts builds new understanding.
6.I|3|A reader stops understanding a hard paragraph. Which is a good fix-up strategy?|annotate and reread it|skip the book|stop reading forever|guess a random word|Rereading and annotating help.
7.A|3|A student says, "I know how Maya feels because my family moved too." This response is...|a personal connection|a rhyme|a plot summary|an index|It ties to the student's life.
7.B|4|Which response compares and contrasts two sources?|Both texts discuss recycling, but one focuses on cities and the other on farms.|I like recycling.|Texts have words.|Both are books.|It shows similarities and differences.
7.C|3|Which sentence uses text evidence?|The article says that wolves hunt in packs, so they are social animals.|I think wolves are cool.|Wolves are in zoos.|My uncle has a dog.|It cites the article.
7.D|3|Which is the best summary of a story in which a boy loses his kite, searches the park, and finds it with help from a friend?|A boy lost his kite, searched, and found it with a friend's help.|The park is big.|A friend is nice.|Kites fly high.|It keeps events in order.
7.E|3|A student underlines key facts and writes questions in the margin while reading. This is called...|annotating|rhyming|scheduling|skimming a menu|Annotating means marking the text.
7.F|3|A student learns the word "migrate" in science. Which sentence uses it correctly?|Many geese migrate south each fall.|My shoes migrate.|The lunch migrated red.|I migrate a pencil.|Migrate means to move seasonally.
7.G|3|During a discussion, a student says, "The author uses the storm to show the characters' fear." This statement is about...|an idea important to the meaning|a spelling rule|a page number|a font style|It explains the meaning.
8.A|3|A character in a story gives up her seat to a tired stranger, and the story ends with her smiling. Which theme is best supported?|helping others brings joy|buses are crowded|strangers are dangerous|smiling is hard|The ending supports kindness.
8.B|4|At the start, Leo is afraid to speak in class. By the end, he gives a speech. How did Leo change?|He became more confident.|He became shorter.|He became angry.|He moved away.|He grew braver.
8.C|3|Which part of the plot shows the events leading up to the climax?|rising action|resolution|title|falling action|Rising action builds tension.
8.C|3|Which part of the plot comes right after the climax?|falling action|exposition|rising action|setting|Falling action follows the turning point.
8.D|4|A story set during a long drought on a farm in the 1930s shows how settings can...|shape the characters' problems|replace the plot|erase the theme|change the author|Setting influences events.
9.A|3|A tall tale usually includes...|an exaggerated hero|a list of facts|a dictionary|a recipe|Tall tales exaggerate.
9.A|3|A legend is a story that...|is based on a person or event from the past, often with exaggeration|is only a poem|has no characters|is a science report|Legends mix history and fiction.
9.B|3|"The wind whispered through the trees." This is an example of...|personification|a fact|a rhyme|a prefix|Wind is given a human action.
9.B|3|"Her smile was a ray of sunshine." What kind of figurative language is it?|a metaphor|a simile|a definition|a fact|It compares without like or as.
9.C|3|In a script, a character's name followed by a colon is a...|character tag|stage direction|climax|title|It shows who speaks.
9.C|3|A play is divided into major sections called...|acts|chapters|stanzas|glossaries|Plays use acts and scenes.
9.D.i|3|A text about Texas bluebonnets discusses how they grow, when they bloom, and how to protect them. What is the central idea?|bluebonnets are important Texas flowers|flowers are red|spring is warm|seeds are small|Details support the main idea.
9.D.ii|3|Which text feature helps a reader know how to say a hard science word?|pronunciation guide|index|date line|map|Pronunciation guides spell sounds.
9.D.ii|3|A diagram of the water cycle helps the reader...|understand the steps visually|find the author|skip the text|count syllables|Diagrams show processes.
9.D.iii|3|An article tells how frogs and toads are alike and different. The pattern is...|compare and contrast|cause and effect|sequence|description of a place|It shows similarities and differences.
9.E.i|3|A student writes, "Kids have nowhere to play, so we need a new park in town." What is the claim?|The town should build a park.|Kids play.|Parks are green.|Towns are big.|The claim is the argument's main point.
9.E.ii|4|An author argues for a longer school year and cites test scores. How does the author use facts?|to support the argument|to hide the claim|to change the topic|to rhyme|Facts back the claim.
9.E.iii|3|A guide titled "How to Train a Puppy" is meant for...|new dog owners|bakers|astronauts|doctors|The audience is people with puppies.
9.F|3|Which is a characteristic of a digital text?|links that take you to more information|a paper cover|a printed index only|a stapled spine|Hyperlinks are digital.
10.A|3|An author writes a story about a girl who saves a lost kitten. Which is the likely message?|care for animals in need|cats are small|rain is wet|girls run fast|The message is about compassion.
10.B|3|An author puts events in order from first to last. This helps the reader...|follow the sequence|find rhymes|skip pages|count words|Chronological order shows events.
10.C|3|Why might an author use bold type for a vocabulary word?|so the reader notices it|to hide it|to change its meaning|to add rhyme|Bold draws attention.
10.D|3|"The leaves danced in the autumn wind." What does this imagery help the reader see?|leaves moving lightly|a quiet room|a heavy rock|a bowl of soup|Danced gives movement.
10.D|4|"Slippery snakes slid slowly." Which sound device is used?|alliteration|assonance|onomatopoeia|hyperbole|The s sound repeats at the start.
10.E|3|A narrator says "she" and "they" to tell about the characters but is not in the story. This is...|third-person point of view|first-person point of view|second person|a conclusion|Third person uses he, she, they.
10.F|3|Which sentence has a more formal voice?|Please complete the assignment before the deadline.|Just get it done, okay?|Yeah, whatever.|No way, dude.|Formal language avoids slang.
10.G|3|An author begins an article with a short true story about a girl who helped clean a beach. This short story is called a(n)...|anecdote|glossary|index|chapter|An anecdote is a brief story.
11.A|2|Which is a strategy for planning a first draft?|brainstorming ideas|printing the final copy|erasing the page|publishing it|Brainstorming generates ideas.
11.B.i|3|Which word is a transition that shows order?|first|banana|green|tiny|First shows sequence.
11.B.i|3|Which sentence would work best as the conclusion of an essay about why exercise matters?|In conclusion, exercise keeps our bodies healthy and strong.|Next, I got a pizza.|Birds sing.|Here is a list.|A conclusion wraps up the main point.
11.B.ii|3|Which detail best supports the idea that dogs are loyal pets?|Dogs often wait at the door for their owners to come home.|Dogs have four legs.|Cats nap a lot.|Birds fly.|The detail supports the idea.
11.C|3|Which revision fixes a repeated word? "The dog ran fast. The dog ran home."|The dog ran fast and headed home.|The dog dog ran.|Fast dog home.|The ran dog.|Combining removes repeats.
11.C|3|Which sentence has the best word choice for "The cake was good"?|The cake was moist and delicious.|The cake was thing.|The cake was it.|The cake was cake.|Specific words add clarity.
11.D.i|3|Which is a run-on sentence?|I like pizza my brother likes tacos.|I like pizza, and my brother likes tacos.|I like pizza.|My brother likes tacos.|Two sentences are joined without punctuation.
11.D.i|4|Which is a sentence fragment?|Because the bell rang.|The bell rang.|The class left.|We walked home.|It does not express a complete thought.
11.D.ii|3|What is the past tense of the irregular verb "swim"?|swam|swimmed|swum|swimed|Swim becomes swam.
11.D.ii|3|Which sentence uses an irregular past-tense verb correctly?|She wrote a long letter.|She writed a long letter.|She writes a long letter yesterday.|She write a long letter.|Wrote is the past tense of write.
11.D.iii|3|Which word is a plural noun?|mice|mouse|cheese|mouses|Mice is the plural of mouse.
11.D.iii|3|Which is a proper noun?|Texas|state|river|mountain|Texas names a specific place.
11.D.iv|3|Which sentence uses the correct superlative form?|This is the tallest tree in the park.|This is the most tallest tree in the park.|This is the tallest tree than the park.|This is a taller tree in the park.|Tallest compares three or more.
11.D.v|3|Which word is an adverb of frequency?|always|quietly|very|yesterday|Always tells how often.
11.D.v|3|Which word is an adverb of degree?|extremely|often|tomorrow|never|Extremely tells how much.
11.D.vi|3|Which sentence contains a preposition?|The squirrel jumped over the fence.|The squirrel jumped happily.|Squirrels are quick.|The squirrel ate.|Over shows position.
11.D.vii|3|Which sentence uses a reflexive pronoun correctly?|Ana taught herself to swim.|Ana taught hisself to swim.|Ana taught themself.|Ana taught yourselves.|Herself refers back to Ana.
11.D.viii|3|Which sentence has a compound subject?|Ben and Mia are playing chess.|Ben is playing chess.|Mia plays quietly.|They sat down.|Two subjects share one verb.
11.D.ix|3|Which is a historical document whose name needs capital letters?|the Constitution|a letter|my notebook|the shopping list|Historical documents are capitalized.
11.D.ix|3|Which of these is a book title that needs capital letters?|Charlotte's Web|a pencil|my backpack|our desk|Titles of books are capitalized.
11.D.x|4|Which sentence uses a comma correctly in a compound sentence?|I wanted to swim, but the pool was closed.|I wanted to swim but, the pool was closed.|I wanted, to swim but the pool was closed.|I wanted to swim but the pool, was closed.|A comma comes before the conjunction.
11.D.x|3|Which sentence punctuates dialogue correctly?|"Let's go," said Maya.|"Let's go" said, Maya.|Let's go, "said Maya."|"Let's go said Maya."|Commas belong inside the quotes.
11.D.x|3|Which phrase shows plural possession correctly?|the students' books|the student's' books|the studentses books|the students books'|The plural students takes an apostrophe after s.
11.D.xi|3|Which word is spelled correctly?|necessary|neccessary|necesary|necessery|Necessary has one c and two s's.
11.D.xi|3|Which word is spelled correctly?|different|diffrent|diferent|differant|Different has three syllables spelled out.
12.A|3|Which sentence would begin a personal narrative well?|Last summer, I learned to ride a bike at my grandmother's house.|Bicycles have two wheels.|The end.|Here is a chart.|It sets the scene.
12.A|3|A poem can use all of these EXCEPT...|a table of contents|rhyme|imagery|stanzas|A table of contents belongs in a book.
12.B|3|A good informational composition has...|a clear central idea with facts|a made-up story only|no organization|only opinions|Informational writing uses facts.
12.C|3|In an opinion essay, reasons should...|support the writer's claim|change the topic|be copied|be left out|Reasons back the opinion.
12.D|3|A letter that asks a museum for information should include...|a polite request and clear question|a joke only|a recipe|a drawing only|It states what you want to know.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g4_ela.jsonl'))
print("saved", len(B.out), "questions")

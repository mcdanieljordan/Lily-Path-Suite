#!/usr/bin/env python3
"""Grade 3 ELA (TEKS 110.5.b) - original questions, hand written. Skips speaking/listening (1), foundational 2.A-D (gap pass later), independent reading (4/5),
publishing and research (13-15)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('110.5.b.', 904, own='g3_ela.jsonl')

load(B, """
3.A|3|A dictionary entry for "tide" lists two meanings. The sentence is "The tide came in at noon." Which meaning fits?|the rise and fall of the sea|a kind of soap|a large crowd|a short race|The sentence is about water at the shore.
3.A|3|Which tool shows how to divide a word into syllables and say it?|a dictionary entry|a calendar|a map key|a table of contents|Dictionaries show syllables and pronunciation.
3.B|3|"The detective examined the footprints carefully and noticed a pattern." What does examined mean?|looked at closely|threw away|sang about|painted over|Context says carefully and noticed.
3.B|3|"The ice cream was so delicious that I devoured it in seconds." What does devoured mean?|ate quickly|dropped|saved|froze|The clues say in seconds.
3.B|4|"The old bridge was fragile, so the town closed it before it could collapse." What does fragile mean?|easily broken|very long|painted blue|brand new|Closing it before it collapses shows weakness.
3.C|3|What does the prefix mis- mean in "misplace"?|wrongly|again|before|full of|Mis- means wrongly or badly.
3.C|3|What does the suffix -able mean in "washable"?|can be done|without|before|again|-able means able to be.
3.C|3|Which word means "to fill again"?|refill|unfill|misfill|prefill|Re- means again.
3.D|3|Which word is a synonym for "difficult"?|hard|easy|simple|light|Hard means about the same as difficult.
3.D|3|Which pair are antonyms?|brave, fearful|happy, glad|big, large|quick, fast|Brave and fearful are opposites.
3.D|3|Which words are homophones?|knight, night|bear, beer|cat, cap|ship, sheep|Knight and night sound the same.
3.D|4|"The pitcher poured water" and "The pitcher threw the ball" show that pitcher is a...|multiple-meaning word|compound word|contraction|prefix|One word has two meanings.
3.D|4|"It's raining cats and dogs." This phrase is an example of...|an idiom|a prefix|a rhyme|a fact|An idiom does not mean its exact words.
6.A|2|A student reads a recipe book before baking. What is the purpose?|to follow directions|to hear a poem|to learn math facts|to find a pet|A recipe gives directions.
6.B|3|Which question could a student ask before reading an article about glaciers?|How do glaciers form?|What time is lunch?|Where is my shoe?|Who won the game?|It fits the topic.
6.C|3|A story begins with dark clouds and strong wind. What might happen next?|a storm|a parade|a picnic|a nap|The clues point to a storm.
6.D|3|"The classroom buzzed like a hive of bees." What do you picture?|a noisy busy room|a quiet library|an empty hall|a dark cave|The simile shows noisy activity.
6.E|3|A story about a family moving reminds you of a friend who moved. This is a...|connection to your experience|prediction|summary|rhyme|You linked it to your life.
6.F|3|Marco's backpack is soaked and his hair is dripping. What can you infer?|he was caught in the rain|he took a nap|he baked bread|he is cold from ice cream|The clues point to rain.
6.G|3|Read: "Honeybees visit flowers to collect nectar. In doing so, they carry pollen from plant to plant." What is the key idea?|bees help plants make seeds|bees are black and yellow|flowers are pretty|honey is sweet|The key point is pollination.
6.H|3|Text 1 says plants need sunlight. Text 2 says plants need water. What can you conclude?|plants need more than one thing to grow|plants only need soil|plants need no care|sun harms plants|Combine the facts.
6.I|3|You get to the end of a page and cannot explain what happened. What is the best step?|reread the page|go to the next book|close your eyes|erase the page|Rereading helps comprehension.
7.A|3|A student says, "This story reminds me of the book we read about friendship." This is a connection to...|another text|a math problem|a recipe|a weather report|It links to another book.
7.B|3|Which response to a story uses evidence?|I think Rosa is brave because she faced the dog.|I liked it.|It was long.|Rosa is a name.|It gives an opinion with a reason.
7.C|3|Which detail from the text best supports "Ben was nervous"?|His hands shook as he walked to the stage.|Ben wore a blue shirt.|The stage was wooden.|There were chairs.|Shaking hands show nerves.
7.D|3|Which is the best paraphrase of "The dense fog made driving dangerous"?|Thick fog made it risky to drive.|Fog is white.|Cars are fast.|The road was dry.|A paraphrase uses new words with the same meaning.
7.E|3|While reading about volcanoes, a student writes short notes. This is...|notetaking|illustrating a menu|rhyming|a fable|Notes capture key ideas.
7.F|3|A student reads the word "habitat" in science and then uses it in a sentence. Which is correct?|A frog's habitat is a pond.|A frog is a habitat.|Habitat is a color.|Habitat runs fast.|The sentence uses habitat correctly.
8.A|3|A story shows a boy sharing his lunch with a hungry friend. What theme does it teach?|kindness matters|lunch is cold|friends are loud|school is long|The theme is a lesson.
8.A|4|How is a theme different from a topic?|a theme is a message; a topic is what the text is about|they mean the same thing|a topic is a message|a theme is a place|A theme is a lesson; a topic is the subject.
8.B|3|In a story, a main character wants to win a race, but her friend wants to help her train. How are they connected?|the friend supports the main character|the friend is the setting|the friend is the plot|the friend is the title|Characters can help each other.
8.B|4|Which is a minor character?|a store clerk who appears once|the hero of the story|the narrator who tells the whole tale|the character who solves the problem|Minor characters appear briefly.
8.C|3|In a plot, the high point of the action is called the...|climax|setting|moral|title|The climax is the turning point.
8.C|3|What happens in the resolution of a story?|the problem is solved|the characters are introduced|the title is shown|the setting is described|The resolution resolves the problem.
8.D|3|A story takes place in a lonely lighthouse during a storm. How does this setting influence the plot?|it creates danger and suspense|it makes the plot shorter|it removes the characters|it changes the author|The setting affects events.
9.A|3|Which genre often has talking animals and ends with a lesson?|fable|biography|science report|newspaper article|Fables teach morals.
9.A|3|A story about real events in a person's life, written by someone else, is a...|biography|fable|myth|play|A biography tells about a life.
9.A|3|A traditional story that explains how something in nature came to be is a...|myth|map|schedule|recipe|Myths explain natural events.
9.B|3|In the poem lines "The cat sat on the mat / and wore a funny hat," which words rhyme?|mat and hat|cat and funny|sat and wore|on and wore|Mat and hat end alike.
9.B|3|A poem repeats the same beginning sound in "wild waves wash." This sound device is...|alliteration|rhyme|dialogue|setting|Repeating first sounds is alliteration.
9.B|3|The word "buzz" imitates a sound. This is called...|onomatopoeia|metaphor|prefix|summary|Onomatopoeia imitates sounds.
9.C|3|In a play, directions in parentheses that tell actors how to move are called...|stage directions|titles|chapters|glossary|Stage directions guide actors.
9.C|3|In a drama, the lines that characters speak are...|dialogue|setting|plot|rhyme|Dialogue is spoken lines.
9.D.i|3|A passage describes how octopuses use camouflage, ink, and speed to escape predators. What is the central idea?|octopuses have ways to stay safe|octopuses are red|oceans are big|fish swim|The details show safety methods.
9.D.ii|3|Which text feature would show how a river's depth changed each month?|a graph|a glossary|a title page|a cover|Graphs show data.
9.D.ii|3|A bulleted list in an article is used to...|show items clearly|hide information|replace the title|add rhymes|Bullets list items.
9.D.iii|3|"Because the dam broke, the town flooded." This sentence uses which pattern?|cause and effect|compare and contrast|rhyme|dialogue|Because shows a cause.
9.D.iii|3|An article describes a problem with litter and then gives solutions. The structure is...|problem and solution|chronological order|rhyme|poetry|It poses a problem then answers it.
9.E.i|3|An author writes, "Gardens teach students about plants, so every school needs one." What is the claim?|every school needs a garden|gardens have flowers|plants need water|students like recess|The claim is the main opinion.
9.E.ii|3|Which sentence is an opinion?|Soccer is the best sport.|Soccer uses a round ball.|A soccer team has eleven players.|Soccer games last ninety minutes.|Best is a judgment.
9.E.iii|3|A pamphlet about how to ride a bike safely is meant for...|new riders|chefs|astronauts|pilots|The audience is people who ride.
9.F|3|Which is a feature of a multimodal text?|it combines words, images, and sound|it has only words|it has only numbers|it has no pictures|Multimodal means more than one mode.
10.A|3|An author writes an article titled "Why We Should Protect Sea Turtles." What is the author's purpose?|to persuade|to entertain only|to confuse|to measure|The title argues for a cause.
10.A|4|What message might an author share in a story about a girl who keeps practicing until she wins?|hard work pays off|winning is luck|practice is boring|girls run slowly|The message is about perseverance.
10.B|3|An author lists events in the order they happened. Why?|so the reader can follow the sequence|to hide the ending|to add rhyme|to make it short|Time order helps the reader follow.
10.C|3|Why does an author put a word in italics?|to show emphasis|to hide the word|to make it a rhyme|to end the page|Italics show stress.
10.D|3|"The moon was a silver coin in the sky." This is an example of...|a metaphor|a fact|a prefix|a date|It compares the moon to a coin without like or as.
10.D|3|"She runs like the wind." This is an example of...|a simile|a metaphor|a fact|a rhyme|A simile uses like or as.
10.E|3|A story is told by a character using "I" and "my." This is...|first-person point of view|third-person point of view|second person|a summary|First-person uses I.
10.F|3|Which phrase shows the author's voice as playful?|Gigantic garbage-gobbling goats gulped greedily!|The goats ate.|Goats are animals.|They were there.|Playful word choice shows voice.
10.G|3|"I've told you a million times to clean your room!" is an example of...|hyperbole|a fact|a rhyme|a metaphor|Hyperbole exaggerates.
10.G|3|Which sentence uses hyperbole?|I'm so hungry I could eat a horse.|I ate a sandwich.|Lunch is at noon.|I like soup.|It exaggerates hunger.
11.B.i|3|Which is the best introductory sentence for an essay about recycling?|Recycling helps keep our planet clean.|Plastic.|The end.|I ate lunch.|An introduction states the topic.
11.B.ii|3|Which detail supports an idea about exercise being healthy?|Running makes your heart strong.|The sky is blue.|Shoes are comfy.|Bananas are yellow.|It supports the idea.
11.C|3|Which revision combines two short sentences into a better one? "I like soccer. I like tennis."|I like soccer and tennis.|I like I like.|Soccer tennis like.|Like soccer.|And joins the ideas.
11.C|3|Which word is a stronger choice than "said" in "I'm so tired," said Ava?|sighed|went|put|did|Sighed shows how she spoke.
11.D.i|3|Which is a compound sentence?|I wanted pizza, but we ate soup.|I wanted pizza.|Pizza with cheese.|Running quickly home.|A compound sentence joins two complete ideas.
11.D.ii|3|Which sentence is written in the future tense?|The bus will arrive at eight.|The bus arrived at eight.|The bus arrives at eight.|The bus had arrived.|Will arrive is future.
11.D.iii|3|Which sentence has a proper noun?|We visited Lake Travis.|We visited a lake.|We swam in water.|We saw a boat.|Lake Travis names a specific place.
11.D.iv|3|Which word is the superlative form of "tall"?|tallest|taller|more tall|tallish|Superlative compares three or more.
11.D.iv|3|Which is the comparative form of "fast"?|faster|fastest|most fast|fastly|Comparative compares two.
11.D.v|3|Which word is an adverb of manner?|quietly|yesterday|tomorrow|never|Quietly tells how.
11.D.vi|3|Which sentence has a prepositional phrase?|The cat slept on the couch.|The cat slept.|The cat purred.|The sleepy cat yawned.|On the couch is a prepositional phrase.
11.D.vii|3|Which pronoun completes the sentence? "Please give the book to ___."|her|she|hers's|they're|Her is the object pronoun.
11.D.vii|3|Which is a possessive pronoun?|mine|me|I|myself|Mine shows ownership.
11.D.viii|3|Which sentence uses a coordinating conjunction correctly?|I wanted to go, but it rained.|I wanted to go but, it rained.|But I wanted to go it rained.|I wanted but to go.|A comma comes before but in a compound sentence.
11.D.ix|3|Which of these words should always start with a capital letter?|Thanksgiving|turkey|table|dinner|Names of holidays are capitalized.
11.D.ix|3|Which name includes an official title that needs a capital letter?|Governor Ortiz|my teacher|the doctor|a mayor|An official title before a name is capitalized.
11.D.x|3|Which sentence uses an apostrophe correctly?|That is Ana's backpack.|That is Anas' backpack.|That is Ana,s backpack.|That is Anas backpack'.|An apostrophe plus s shows possession.
11.D.x|3|Which sentence uses commas correctly?|On Monday, we went to the zoo.|On Monday we, went to the zoo.|On, Monday we went to the zoo.|On Monday we went, to the zoo.|A comma follows an introductory phrase.
11.D.x|3|Which sentence has quotation marks correct?|"I am ready," said Eli.|"I am ready, said Eli."|I am ready, "said Eli."|"I am ready said Eli."|Quotation marks surround only the spoken words.
11.D.xi|3|Which word is spelled correctly?|neighbor|nieghbor|naybor|neighbour|Neighbor follows the eigh pattern.
11.D.xi|3|Which word is spelled correctly?|friend|freind|frend|friand|I before e in friend.
12.A|3|What belongs in the beginning of a personal narrative?|who, where, and when the story takes place|only the ending|a list of facts|a table|The beginning sets the scene.
12.B|3|A brief informational composition about frogs should begin with...|a sentence that names the topic|a joke|an unrelated story|the last fact|The introduction names the topic.
12.C|3|An opinion essay should include...|a claim and reasons|only a rhyme|only facts without an idea|a recipe|A claim needs reasons.
12.C|3|Which sentence is a strong closing for an opinion essay about recess?|For these reasons, recess is important for students.|The end.|I like cake.|Then it rained.|A conclusion restates the claim.
12.D|3|The closing of a friendly letter might be...|Your friend, Sam|Dear Sam|Hello|Thank you|A closing comes at the end before the name.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g3_ela.jsonl'))
print("saved", len(B.out), "questions")

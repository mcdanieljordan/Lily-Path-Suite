#!/usr/bin/env python3
"""Grade 5 ELA (TEKS 110.7.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('110.7.b.', 906, own='g5_ela.jsonl')

load(B, """
3.A|3|Which part of a dictionary entry shows where a word came from?|the etymology|the page number|the guide words|the cover|Word origin is the etymology.
3.A|3|A dictionary shows "re-cy-cle." What does this tell the reader?|how the word is divided into syllables|what the word rhymes with|who wrote the word|when the word was invented|The hyphens show syllables.
3.B|3|"The comedian's jokes were so hilarious that the audience roared with laughter." What does hilarious mean?|extremely funny|very sad|quite boring|a little scary|The audience roared with laughter.
3.B|4|"Sam's reluctant smile showed he did not really want to go to the dentist." What does reluctant mean?|unwilling|excited|careless|proud|He did not want to go.
3.B|3|In "The river bank was muddy" and "She went to the bank to deposit money," how can a reader tell the meaning of bank?|by the words around it|by its length|by its first letter|by the page number|Context clues show the meaning.
3.C|3|The prefix trans- means across. What does "transatlantic" most likely mean?|across the Atlantic Ocean|under the sea|near the beach|before the ocean|Trans means across.
3.C|3|The prefix super- means above or beyond. What does "superhuman" mean?|beyond what humans normally can do|less than human|like a small human|a pet|Super means beyond.
3.C|3|The suffix -logy means "the study of." What does "geology" mean?|the study of the Earth|the study of stars|the study of animals|the study of words|Geo means Earth.
3.C|4|The root "photo" means light. What does "photosynthesis" involve?|using light to make food|breaking rocks|building a house|making noise|Photo means light.
3.D|3|"A stitch in time saves nine" is an example of...|an adage|a pun|a metaphor|a rhyme scheme|An adage is a short wise saying.
3.D|4|"I used to be a baker, but I couldn't make enough dough." This joke plays on a word with two meanings. It is a...|pun|an adage|a fact|a simile|A pun uses a word with two meanings.
3.D|3|What does the adage "Look before you leap" advise?|think before acting|jump high|run fast|look at the sky|Be careful before you act.
6.A|3|A student sets a purpose before reading a science article on volcanoes. Which is the best purpose?|to learn how volcanoes form|to count the commas|to copy the font|to guess the author's age|A purpose guides reading.
6.B|3|Which question could a reader ask during reading to better understand a biography of an inventor?|What problem was the inventor trying to solve?|What color is the book cover?|How many pages are left?|Where is the library?|It deepens understanding.
6.C|3|A nonfiction article has a section called "How Hurricanes Form." What might the reader predict about it?|it will explain the steps of how hurricanes develop|it will tell a funny story|it will list recipes|it will show a map of a mall|Headings suggest content.
6.D|3|Which sentence is best for creating a mental image of a thunderstorm?|Lightning split the dark sky as thunder rattled the windows.|There was weather.|It was a day.|Storms happen.|Sensory details build images.
6.E|3|A student reads about a flood and thinks of a news story about a rescue. This is a connection to...|society|spelling|punctuation|handwriting|It links to events in the world.
6.F|4|Read: "Dani kept glancing at the clock and tapping her pencil as the teacher passed out the tests." What can you infer?|Dani feels anxious about the test.|Dani loves clocks.|Dani lost her pencil.|Dani is the teacher.|Her actions show nervousness.
6.G|3|Which detail best shows the key idea that bees are important to farming?|They pollinate many crops.|Bees are small.|Bees can sting.|Bees live in hives.|Pollination helps crops grow.
6.H|4|One article explains how plants make food. Another explains how animals eat plants. What new idea can a reader build by combining them?|energy moves from plants to animals|plants eat animals|animals make sunlight|food grows on rocks|Combining sources shows energy flow.
6.I|3|A reader notices their mind wandering while reading a long paragraph. What is a good adjustment?|reread and ask questions about the paragraph|read faster|skip the paragraph|close the book|Rereading and asking questions help.
7.A|3|Which sentence shows a personal connection to a book about moving to a new school?|I felt nervous like that on my first day at my school.|The book has a blue cover.|Schools have doors.|Moving trucks are big.|It links the reader's experience.
7.B|4|Which written response compares two articles about volcanoes?|Both articles describe eruptions, but only one explains how scientists predict them.|Volcanoes are hot.|I read two things.|Articles have titles.|It shows a comparison.
7.C|3|Which sentence uses text evidence to support the idea that Marcus is generous?|Marcus gave half of his lunch to a classmate who had forgotten his.|Marcus likes lunch.|Marcus is in fifth grade.|Marcus has a backpack.|Sharing his lunch shows generosity.
7.D|3|Which is the best summary of a paragraph that explains how rain forms from water vapor rising, cooling, and falling?|Water vapor rises, cools into clouds, and falls as rain.|Clouds are white.|Rain makes puddles.|Water is wet.|It keeps the main events in order.
7.E|3|A student draws a diagram while reading a science chapter to remember the steps. This is an example of...|interacting with the text by illustrating|copying a title|skipping details|changing the author|Illustrating is a way to interact with text.
7.F|3|After learning the word "ecosystem," which sentence uses it correctly?|A pond is an ecosystem with plants, animals, and water.|The ecosystem ate lunch.|I wore an ecosystem on my head.|Ecosystem is a type of sandwich.|It uses the word correctly.
7.G|3|During a class discussion about a story, which comment helps explain an important idea?|The storm shows how nervous the characters feel.|I like the pictures.|The book is long.|My dog barks.|It explains meaning.
8.A|4|A story shows a girl who is honest even when it is hard, and she also learns to forgive her friend. Which pair of themes fits?|honesty and forgiveness|speed and strength|money and fame|winter and summer|Both ideas are shown.
8.B|4|Two brothers argue about who should lead their team. This is a conflict between...|characters|setting and plot|title and author|stanzas|Characters disagree.
8.B|3|A character wants to reach the mountain top, but a storm blocks the trail. This conflict is between the character and...|nature|a friend|a family member|a teacher|The storm is part of nature.
8.C|3|In a story, the most intense moment, when the main problem is faced, is the...|climax|resolution|exposition|title|The climax is the turning point.
8.C|3|The part of a plot where the problem is finally solved is the...|resolution|rising action|introduction|climax|The resolution ends the conflict.
8.D|4|A story is set in the Wild West in the 1800s. How does this historical setting influence the plot?|events like cattle drives and travel by horse shape what happens|it changes the author|it removes characters|it makes the story a poem|The time period affects events.
9.A|3|Which genre often explains why something in nature exists, such as why the sun rises?|myth|science report|map|biography|Myths explain natural events.
9.A|3|A folktale is a story that...|has been passed down by word of mouth|is a modern news article|is a math problem|is a dictionary entry|Folktales are traditional.
9.B|4|In a poem, the speaker is...|the voice that tells the poem|the author's name|the title|the rhyme|The speaker is not always the poet.
9.B|3|"The stars winked at me" is an example of...|personification|a fact|a prefix|a date|Stars are given a human action.
9.B|3|The line "Whispering winds were wailing" uses...|alliteration|rhyme|onomatopoeia|dialogue|Repeated w sounds.
9.C|3|In a play script, the words in parentheses that describe how a character moves or speaks are...|stage directions|dialogue|a theme|rhymes|Stage directions guide actors.
9.C|3|A play is organized into acts and...|scenes|stanzas|chapters|glossaries|Acts are divided into scenes.
9.D.i|3|An article describes how the Amazon rain forest provides oxygen, shelter for animals, and medicines. What is the central idea?|The Amazon rain forest is valuable to many living things.|Rain is wet.|Forests are green.|Animals sleep.|The details support the central idea.
9.D.ii|3|A sidebar in a textbook is used to...|give extra information about the topic|replace the main text|show the table of contents|list page numbers|Sidebars add details.
9.D.ii|3|A timeline in a history article helps the reader...|see events in order|learn spelling|find rhymes|count pages|Timelines show sequence.
9.D.iii|3|An article lists reasons from least important to most important. The pattern is...|order of importance|chronological order|compare and contrast|description of a place|The reasons build up.
9.E.i|3|Read: "Art builds creativity, so our schools should add art classes." What is the claim?|Schools should offer more art classes.|Art is colorful.|Schools are big.|Paint is wet.|The claim is the main argument.
9.E.ii|4|An author argues against littering and cites a study showing that litter harms wildlife. How does the study help the argument?|It gives a fact that supports the claim.|It changes the topic.|It makes the claim weaker.|It adds a rhyme.|Facts strengthen an argument.
9.E.iii|3|An ad says, "Kids, save your allowance for this great new game!" Who is the intended audience?|children|grandparents|pilots|teachers|The ad addresses kids.
9.F|3|A website with a video, a map, and a clickable menu is an example of...|a multimodal text|a poem|a dictionary|a diary|It uses several modes.
10.A|3|A story about a boy who returns a lost wallet suggests the author wants to share a message about...|honesty|speed|weather|fashion|The message is about being honest.
10.B|4|An author explains a problem in the first paragraph and then offers solutions. How does this structure support the author's purpose?|it helps persuade the reader to take action|it hides the problem|it adds rhyme|it makes the text shorter|Problem-solution persuades.
10.C|3|Why does an author include a chart with numbers in an article about population?|to present data clearly|to decorate the page|to hide facts|to add dialogue|Charts organize data.
10.D|4|"The old house groaned in the wind" uses what to create an image?|personification|a fact|a prefix|a date|The house is given a human action.
10.D|3|Which phrase shows imagery?|the sweet smell of warm cinnamon rolls|a list of numbers|the word because|three plus four|Sensory description creates imagery.
10.E|3|A story told by a character who uses the word "I" is written in...|first-person point of view|third-person point of view|second person|a list|The narrator is in the story.
10.F|3|Which sentence shows a strong, excited voice?|What an amazing, unbelievable day this has been!|The day was.|It is okay.|We went.|Strong word choice shows voice.
10.G|3|Why might an author use hyperbole in a funny story?|to exaggerate for humor|to give exact facts|to hide the plot|to define a word|Hyperbole exaggerates.
10.G|4|Which sentence is an example of stereotyping?|All teenagers are lazy.|Some teenagers play soccer.|Maya is a teenager.|The teenager waited.|It makes a broad unfair claim about a group.
10.G|3|Why might an author include an anecdote in an article?|to illustrate a point with a short true story|to confuse the reader|to replace the title|to add stanzas|Anecdotes make points relatable.
11.A|2|Which tool helps a writer organize ideas before drafting?|a graphic organizer|a stapler|a ruler|an eraser|Organizers map ideas.
11.B.i|3|Which word works best as a transition to show a contrast?|however|then|because|first|However signals a contrast.
11.B.i|3|An essay's introduction should...|state the topic and grab the reader's attention|list all the details|repeat the title only|end the story|The introduction opens the piece.
11.B.ii|4|Which sentence adds the most specific detail about a trip to the beach?|We built a three-foot sandcastle with towers made from shells.|We had fun.|It was nice.|We went somewhere.|Specific facts add depth.
11.C|3|Which revision combines these sentences best? "The storm was loud. The storm was long."|The storm was loud and long.|The loud long.|Storm was.|The was loud storm long.|It combines ideas smoothly.
11.C|3|Which word best replaces "big" in "The big elephant crossed the river"?|enormous|good|small|quick|Enormous is a stronger word.
11.D.i|3|Which sentence is a comma splice?|The bus was late, we waited inside.|The bus was late, so we waited inside.|The bus was late.|We waited inside.|Two sentences are joined only by a comma.
11.D.i|3|Which sentence has subject-verb agreement?|The dogs run in the park.|The dogs runs in the park.|The dog run in the park.|The dogs running in the park.|Plural subject takes a plural verb.
11.D.ii|3|Which is the correct past tense of "begin"?|began|begun|beginned|begined|Begin becomes began.
11.D.ii|3|Which sentence uses the correct past tense of "teach"?|My aunt taught me to knit.|My aunt teached me to knit.|My aunt teaches me yesterday.|My aunt tought me to knit.|Taught is the past tense of teach.
11.D.iii|3|Which word is a collective noun?|flock|bird|fly|feather|A flock is a group of birds.
11.D.iii|3|Which sentence uses a collective noun?|The team practices every day.|Mia ran.|The sky is blue.|He ate quickly.|Team names a group.
11.D.iv|3|Which sentence uses the correct comparative form?|This book is more interesting than that one.|This book is more interestinger than that one.|This book is interestinger than that one.|This book is most interesting than that one.|Use more with longer adjectives.
11.D.v|4|Which word is a conjunctive adverb?|however|and|but|so|However connects two ideas.
11.D.v|3|Which sentence uses a conjunctive adverb correctly?|It rained all day; therefore, the game was canceled.|It rained all day therefore the game was canceled.|It rained all day, therefore the game was canceled.|It rained therefore all day; the game was canceled.|A semicolon comes before and a comma after.
11.D.vi|4|Which sentence has subject-verb agreement when a prepositional phrase follows the subject?|The box of crayons is on the table.|The box of crayons are on the table.|The box of crayons were on the table.|The boxes of crayons is on the table.|The subject is box, not crayons.
11.D.vii|3|Which is an indefinite pronoun?|everyone|she|them|myself|Everyone refers to no one specific.
11.D.vii|3|Which sentence uses an indefinite pronoun correctly?|Everyone is ready for the trip.|Everyone are ready for the trip.|Everyone were ready for the trip.|Everyone be ready for the trip.|Everyone takes a singular verb.
11.D.viii|3|Which sentence is a complex sentence?|Because it was raining, we stayed home.|We stayed home.|It was raining.|We stayed home and read.|It has a dependent clause.
11.D.viii|3|Which word is a subordinating conjunction?|although|and|or|but|Although introduces a dependent clause.
11.D.ix|3|Which of these is an acronym written in all capital letters?|NASA|pencil|teacher|library|Acronyms are capitalized.
11.D.ix|3|Which is a correctly written abbreviation for a title?|Dr.|ms|mr|prof|A title abbreviation is capitalized and ends with a period.
11.D.x|3|Which sentence uses a comma correctly in a complex sentence?|After the game ended, we went out for pizza.|After the game ended we went, out for pizza.|After, the game ended we went out for pizza.|After the game, ended we went out for pizza.|A comma follows an introductory clause.
11.D.x|3|How should the title of a book be shown in handwriting or typing?|underlined or in italics|in quotation marks only|all in lowercase|crossed out|Book titles are underlined or italicized.
11.D.x|3|Which sentence uses quotation marks and commas correctly?|"We should leave now," said Dad.|"We should leave now" said, Dad.|"We should leave now said Dad."|We should leave now, "said Dad."|The comma goes inside the closing quotation mark.
11.D.xi|3|Which word is spelled correctly?|embarrass|embarass|embarress|embarras|Embarrass has double r and double s.
11.D.xi|3|Which word is spelled correctly?|separate|seperate|separete|seprate|Separate has the "par" in the middle.
11.D.xi|3|Which word is spelled correctly?|government|goverment|govermment|guvernment|Government includes n before ment.
12.A|3|Which element is important in fiction?|characters facing a problem|a table of contents|a bibliography|a glossary|Fiction has characters and plot.
12.A|3|A personal narrative is told from the writer's...|own experience|imagination about dragons only|science textbook|neighbor's diary|It is about the writer's life.
12.B|3|An informational composition about the planets should include...|facts organized around a central idea|a made-up story|only the writer's opinion|a rhyming poem|Informational writing uses facts.
12.C|3|Which sentence best states an opinion for an opinion essay?|Our school should have a longer recess.|Recess is a word.|The bell rings at noon.|We have a playground.|It states a claim.
12.C|3|Which closing sentence best restates the claim in an opinion essay about recycling?|For all these reasons, everyone should recycle.|The end.|I like cake.|Then it rained.|A conclusion restates the claim.
12.D|3|Which sentence belongs in a letter requesting information from a zoo?|Could you please send me information about your summer camps?|Give me camps now.|I am bored.|Zoos have animals.|It politely asks for information.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g5_ela.jsonl'))
print("saved", len(B.out), "questions")

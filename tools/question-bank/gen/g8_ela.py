#!/usr/bin/env python3
"""Grade 8 ELA (TEKS 110.24.b) - original questions, about 3 per assessable standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('110.24.b.', 963, own='g8_ela.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A
H('2.A', 2, "Which resource shows a word's origin, or etymology?", "an etymological dictionary", ["a road atlas", "a thesaurus of slang", "a cookbook"], "Etymology traces word history.")
H('2.A', 3, "A dictionary entry lists 'con-tract' with a dot between the syllables. What does the dot show?", "where the word divides into syllables", ["the word's origin", "the word's rhyme", "the word's synonym"], "Dots mark syllable breaks.")
H('2.A', 4, "Why might a reader check a digital dictionary's audio feature?", "to hear the correct pronunciation", ["to find the author", "to count words", "to see the publisher"], "Audio models pronunciation.")

# 2.B
H('2.B', 3, "'The ambiguous directions confused us; they could be read two different ways.' What does 'ambiguous' mean?", "open to more than one meaning", ["extremely clear", "very short", "written in code"], "The clause after the semicolon defines it.")
H('2.B', 3, "'Unlike her gregarious sister, Mia preferred quiet evenings alone.' What does 'gregarious' mean?", "sociable", ["shy", "angry", "wealthy"], "'Unlike' signals an opposite.")
H('2.B', 4, "'The mayor's rhetoric, full of grand promises and stirring phrases, inspired the crowd.' What is 'rhetoric' here?", "persuasive speech", ["a medical test", "a building plan", "a financial report"], "Promises and stirring phrases clarify the meaning.")

# 2.C
H('2.C', 3, "The Latin root 'bene' means 'good.' What does 'benefactor' most likely mean?", "someone who does good for others", ["someone who breaks things", "someone who travels", "someone who hides"], "Bene = good.")
H('2.C', 3, "The Greek root 'auto' means 'self.' Which word means 'a person's own life story, written by that person'?", "autobiography", ["telegraph", "geography", "photograph"], "Auto + bio + graphy.")
H('2.C', 4, "The Latin root 'dict' means 'say.' What does 'dictate' mean?", "to say aloud for someone to write down", ["to erase", "to build", "to sail"], "Dict = say.")

# 5.B
H('5.B', 3, "A reader asks, 'Why did the author include this statistic?' This question helps the reader...", "examine the author's reasoning", ["count pages", "choose a font", "find the index"], "Questions deepen analysis.")
H('5.B', 3, "Which is a strong question to ask before reading an article titled 'The Future of Water'?", "What problems might the article say are coming?", ["What is the paper's color?", "How tall is the author?", "Where was it printed?"], "Pre-reading questions focus on content.")
H('5.B', 4, "During reading, a student asks 'How does this paragraph connect to the thesis?' This question supports...", "monitoring how ideas fit together", ["skipping paragraphs", "memorizing page numbers", "ignoring structure"], "It checks coherence.")

# 5.C
H('5.C', 3, "A text opens with 'Once upon a time, in a kingdom of glass...' What genre prediction is most reasonable?", "a fairy tale or fantasy", ["a lab report", "a newspaper obituary", "a bus schedule"], "The opening signals genre.")
H('5.C', 3, "A reader sees headings like 'Problem' and 'Solution.' Which prediction fits the text structure?", "the text will describe an issue and ways to address it", ["the text is a poem", "the text is a play", "the text is a recipe"], "Headings reveal structure.")
H('5.C', 4, "A reader predicted a happy ending, but the narrator warns of 'a price paid later.' What is the best next step?", "revise the prediction", ["keep it unchanged", "stop reading", "skip the warning"], "Readers correct predictions with new evidence.")

# 5.D
H('5.D', 3, "Which detail most helps a reader picture a stormy sea?", "waves crashed over the deck as the mast groaned", ["the sea was there", "it was water", "a boat existed"], "Vivid sensory detail.")
H('5.D', 3, "Why do readers create mental images while reading?", "to deepen understanding of the text", ["to skip words", "to avoid inference", "to shorten the story"], "Visualizing aids comprehension.")
H('5.D', 4, "A reader sketches the layout of a battlefield from an author's description. What does this show?", "careful use of text details to visualize", ["a random drawing", "ignoring the text", "a summary of the title"], "Details guide imagery.")

# 5.E
H('5.E', 3, "A student thinks of her own move to a new school while reading about a character's move. This is a connection to...", "personal experience", ["another text", "the glossary", "the index"], "Text-to-self.")
H('5.E', 3, "An article on child labor reminds a reader of a novel set in a factory. This is a connection to...", "another text", ["the weather", "a recipe", "the page numbers"], "Text-to-text.")
H('5.E', 4, "A poem about protests reminds a reader of recent civic debates. This is a connection to...", "society", ["the cover", "only the reader's lunch", "the typeface"], "Text-to-world.")

# 5.F
H('5.F', 3, "'Dana set the trophy on the shelf, then turned it to face the wall.' What can be inferred?", "Dana feels conflicted about the trophy", ["Dana won easily", "Dana is dusting", "Dana is in a hurry to leave"], "Turning it away suggests mixed feelings.")
H('5.F', 3, "'The coach looked at the scoreboard, sighed, and slowly took off his cap.' What can be inferred?", "the team is losing or has lost", ["the team is far ahead", "it is raining", "the game has not started"], "Body language implies disappointment.")
H('5.F', 4, "'Though the house was spotless, the table was set for two and no one ever sat down.' What inference is best supported?", "someone who used to live there is missed", ["the house is brand new", "guests are late", "the owner dislikes cleaning"], "Details imply loss.")

# 5.G
H('5.G', 3, "To find the key idea of a passage, a reader should...", "evaluate which details matter most", ["count the commas", "read only the title", "ignore the evidence"], "Key ideas come from weighing details.")
H('5.G', 3, "A passage gives three reasons that recycling saves energy. The key idea is that...", "recycling helps conserve energy", ["recycling is expensive", "trucks are loud", "paper is white"], "Details support the key idea.")
H('5.G', 4, "Which detail is least relevant to the key idea of an article on the benefits of bike lanes?", "the mayor's favorite color", ["bike lanes reduce traffic", "bike lanes improve safety", "bike lanes improve health"], "It does not support the key idea.")

# 5.H
H('5.H', 3, "A student reads an article and watches a video on the same topic, then forms a new conclusion from both. This is...", "synthesis", ["copying", "summarizing only one", "guessing"], "Combining sources creates new understanding.")
H('5.H', 4, "Source A says online classes save money. Source B says they can reduce student engagement. Which synthesis is strongest?", "online classes offer savings but may require ways to keep students engaged", ["online classes are perfect", "online classes are worthless", "the sources are the same"], "A balanced new idea.")
H('5.H', 3, "Synthesizing information means...", "combining ideas to form new understanding", ["copying each source", "listing sources only", "ignoring conflicts"], "New insight from multiple sources.")

# 5.I
H('5.I', 3, "A reader realizes she lost the thread of a dense paragraph. What adjustment helps most?", "re-read it more slowly", ["skip it", "start another book", "read faster"], "Re-reading repairs comprehension.")
H('5.I', 3, "Which is a way to monitor comprehension?", "pausing to restate what was just read", ["flipping pages quickly", "ignoring new words", "reading the last line only"], "Restating checks understanding.")
H('5.I', 4, "A reader meets unfamiliar scientific terms. Which adjustment is best?", "use context, a glossary or a reference source", ["skip the page", "guess without checking", "stop reading"], "Resources clarify meaning.")

# 6.C
H('6.C', 3, "A student claims the narrator is lonely. Which is the strongest text evidence?", "He ate every dinner by himself and spoke to no one for weeks.", ["He lived in a house.", "The dinner was warm.", "The narrator wore a coat."], "It shows isolation.")
H('6.C', 4, "Why is a long quotation weaker than a short, targeted one?", "a focused quote ties directly to the claim", ["long quotes are illegal", "short quotes are always wrong", "quotes need no connection"], "Evidence should be precise.")
H('6.C', 3, "Which sentence correctly introduces text evidence?", "The author shows his fear when he writes, 'My hands would not stop shaking.'", ["Shaking.", "Hands are body parts.", "He is shaking, I guess."], "It frames the quote and links it to the claim.")

# 6.D
H('6.D', 3, "A good summary of a long article should...", "include main ideas in logical order without opinions", ["add personal opinions", "copy every sentence", "skip the main idea"], "Summaries are concise and neutral.")
H('6.D', 4, "Which sentence best paraphrases 'The legislation was met with considerable resistance from local business owners'?", "Many local business owners strongly opposed the law.", ["Business owners wrote the law.", "The law passed without comment.", "Resistance is a type of business."], "Maintains meaning in new words.")
H('6.D', 3, "A paraphrase differs from a summary because a paraphrase...", "restates the full idea in different words", ["shortens a whole book to one word", "adds new facts", "changes the meaning"], "Paraphrase keeps detail; summary condenses.")

# 6.G
H('6.G', 3, "'The porch light stayed on all night, though no one had lived there for years.' What is an implicit meaning?", "someone still hopes the house's owner will return", ["the house is new", "electricity is free", "the porch is wide"], "Implied emotion.")
H('6.G', 3, "Which statement is an explicit meaning?", "The text says the bridge opened in 1932.", ["The bridge seems important.", "The reader guesses the bridge is old.", "The bridge symbolizes unity."], "Explicit means directly stated.")
H('6.G', 4, "'She smiled for the camera, but her knuckles were white on the chair arms.' What is the implicit meaning?", "she is more nervous than she appears", ["she is thrilled", "she is cold", "she is bored"], "Body detail contradicts the smile.")

# 6.J
H('6.J', 3, "To challenge an author's claim, a reader should...", "cite relevant text evidence that conflicts with it", ["shout at the page", "ignore the claim", "change the title"], "Challenges rely on evidence.")
H('6.J', 4, "An author claims 'all teens prefer video games.' Which response best challenges the claim?", "The author offers no survey data, and many teens prefer sports or reading.", ["I disagree.", "Games are bad.", "The claim is red."], "Points to unsupported generalization.")
H('6.J', 3, "To defend an author's claim, a reader could...", "point to the study the author cites as support", ["say it feels right", "skip the study", "change the claim"], "Support uses the text's evidence.")

# 7.A
H('7.A', 3, "In a novel, a character repeatedly chooses honesty despite costs, and eventually earns trust. What theme develops?", "integrity brings lasting respect", ["lying is rewarded", "trust is worthless", "costs do not matter"], "Events and choices reveal theme.")
H('7.A', 4, "How do characters and events work together to develop a theme?", "characters' choices and their consequences reveal a message", ["the setting alone decides", "the title alone decides", "page count decides"], "Interaction builds theme.")
H('7.A', 3, "Which is a theme?", "People can overcome fear by helping others.", ["Fear", "A story about a scared boy", "Helping"], "A theme is a full statement.")

# 7.B
H('7.B', 3, "A character's jealousy leads her to sabotage a friend's project, which ruins their friendship. This shows that...", "motivations can drive events and outcomes", ["setting controls plot", "titles control plot", "conflict is unrelated to motivation"], "Behavior shapes resolution.")
H('7.B', 4, "How does a character's determination most likely affect the resolution of a conflict?", "it pushes the character to keep trying until the problem is solved", ["it ends the story at once", "it removes the conflict", "it changes the genre"], "Motivation influences resolution.")
H('7.B', 3, "A hero acts out of fear of failure and avoids challenges. How does this influence the plot?", "it delays or complicates the resolution", ["it solves the conflict", "it adds rhymes", "it changes the narrator"], "Behavior affects events.")

# 7.C
H('7.C', 3, "A narrator describes a childhood summer in the middle of a present-day scene. This is a...", "flashback", ["foreshadowing", "simile", "stanza"], "A scene from the past.")
H('7.C', 4, "A novel alternates between two characters whose stories later intersect. This is a...", "parallel plot", ["flashback only", "rhyme scheme", "glossary"], "Parallel plots run side by side.")
H('7.C', 3, "A side story involving a minor character that adds depth to the main plot is a...", "subplot", ["thesis", "stanza", "caption"], "Subplots enrich the main plot.")

# 7.D
H('7.D', 3, "A character raised in a strict mountain village distrusts outsiders. How does setting shape her beliefs?", "her environment taught her to value caution", ["setting has no effect", "outsiders created the village", "she was born trusting everyone"], "Setting influences values.")
H('7.D', 4, "A story set in a wartime city shows characters valuing shared food and shelter. What does this reveal?", "hardship in the setting shapes what characters value", ["war has no effect", "food is unimportant", "cities have no culture"], "Setting influences beliefs.")
H('7.D', 3, "A novel set in a futuristic society where speech is controlled most likely shapes characters' beliefs about...", "freedom and obedience", ["recipes", "weather vanes", "shoe sizes"], "A controlled setting affects values.")

# 8.A
H('8.A', 3, "A tale of a young pilot facing a perilous journey across an unexplored sea is most likely...", "an adventure story", ["a biography", "an encyclopedia entry", "a user manual"], "Journey and danger define adventure.")
H('8.A', 3, "A story set during the Civil Rights Movement, with invented characters, is...", "historical fiction", ["science fiction", "a myth", "realistic satire"], "Real period, fictional characters.")
H('8.A', 4, "Which genre combines imagined technologies with scientific ideas about the future?", "science fiction", ["historical fiction", "mystery", "memoir"], "Speculative science defines the genre.")

# 8.B
H('8.B', 3, "A poet breaks a line mid-thought so a word stands alone. What effect could this create?", "emphasis on that word", ["a rhyme scheme", "a footnote", "a plot twist"], "Line breaks stress meaning.")
H('8.B', 4, "A poem uses no punctuation at all and long running lines. What effect could this create?", "a flowing, breathless rhythm", ["a formal tone", "a list", "a table of data"], "Absence of punctuation speeds pace.")
H('8.B', 3, "Short lines and abrupt periods in a poem most likely create...", "a halting or tense rhythm", ["a smooth lullaby", "a long narrative", "a hopeful chorus"], "Punctuation affects pace.")

# 8.C
H('8.C', 3, "In a play, what is a scene?", "a section of an act set in one time and place", ["the whole play", "a list of actors", "the program cover"], "Scenes divide acts.")
H('8.C', 4, "How do acts and scenes help develop dramatic action?", "they organize rising action, climax and resolution", ["they remove conflict", "they delete characters", "they replace dialogue"], "Structure shapes action.")
H('8.C', 3, "Which element signals a change in setting within a play?", "a new scene", ["a new adjective", "a new font", "a new title"], "Scenes mark changes.")

# 8.F
H('8.F', 3, "An interactive web page lets readers click a map for videos and quotes. This is a...", "multimodal digital text", ["limerick", "diary entry", "one-act play"], "It mixes modes.")
H('8.F', 4, "Which characteristic distinguishes digital texts from print texts?", "hyperlinks and embedded media", ["page numbers", "paper covers", "bindings"], "Digital texts link and embed media.")
H('8.F', 3, "A reader evaluates a webpage by checking its author, date and links. This helps decide...", "whether the source is reliable", ["the font size", "the number of ads only", "the page color"], "Features signal reliability.")

# 8.D.i
H('8.D.i', 3, "The thesis of an argumentative essay is best described as...", "the controlling idea the essay supports", ["a list of sources", "the final citation", "a quotation"], "Thesis controls the essay.")
H('8.D.i', 3, "Which evidence best supports the thesis 'Public libraries benefit communities'?", "Libraries offer free classes, internet access and books.", ["Libraries have shelves.", "Some libraries are old.", "Books can be heavy."], "Specific benefits support the thesis.")
H('8.D.i', 4, "A body paragraph strays from the thesis. What should the writer do?", "revise or cut it to stay focused on the controlling idea", ["add more unrelated detail", "delete the thesis", "ignore the problem"], "Focus keeps coherence.")

# 8.D.ii
H('8.D.ii', 3, "What is a footnote used for?", "to add a note or source at the bottom of a page", ["to title the essay", "to end a sentence", "to make a list"], "Footnotes appear at page bottom.")
H('8.D.ii', 3, "Endnotes appear...", "at the end of a chapter or document", ["before the title", "inside every sentence", "on the cover"], "Endnotes are collected at the end.")
H('8.D.ii', 4, "Why do authors include citations?", "to credit sources and allow readers to verify claims", ["to lengthen the text", "to hide evidence", "to add rhymes"], "Citations show credibility.")

# 8.D.iii
H('8.D.iii', 3, "An essay uses cause and effect in one section and compare and contrast in another. This shows...", "multiple organizational patterns", ["a single pattern", "poor organization only", "no pattern at all"], "Different patterns develop the thesis.")
H('8.D.iii', 4, "Why might an author use chronological order in one section and problem-solution in another?", "each pattern helps develop a different part of the thesis", ["to confuse readers", "to avoid evidence", "to shorten the text"], "Patterns serve the argument.")
H('8.D.iii', 3, "Words like 'first,' 'next' and 'finally' signal which organizational pattern?", "sequence", ["compare and contrast", "cause and effect", "problem and solution"], "They mark order.")

# 8.E.i
H('8.E.i', 3, "Which statement is an arguable claim?", "Schools should start later in the morning.", ["Schools have buses.", "Mornings come before noon.", "Some schools have gyms."], "A claim takes a debatable position.")
H('8.E.i', 4, "To analyze an argument, a reader should...", "check whether the evidence actually supports the claim", ["count the paragraphs", "read only the conclusion", "ignore the reasoning"], "Analysis tests support.")
H('8.E.i', 3, "In an argument, reasons and evidence are used to...", "support the claim", ["replace the claim", "end the debate", "delete the opposition"], "Support strengthens the claim.")

# 8.E.ii
H('8.E.ii', 3, "A counterargument is...", "an opposing view to the author's claim", ["the author's thesis", "a type of poem", "a citation style"], "It challenges the claim.")
H('8.E.ii', 4, "Why do strong writers address counterarguments?", "to show the claim holds up against opposing views", ["to weaken their claim", "to avoid evidence", "to shorten the essay"], "It builds credibility.")
H('8.E.ii', 3, "'Some argue homework helps learning; however, studies show limited benefits.' What does the writer do?", "acknowledges and responds to an opposing view", ["tells a joke", "defines a word", "ends the essay"], "A counterargument and rebuttal.")

# 8.E.iii
H('8.E.iii', 3, "An article explaining how to choose a first guitar, with beginner terms and photos, targets...", "new musicians", ["professional luthiers", "stock traders", "judges"], "Beginner tone targets novices.")
H('8.E.iii', 3, "A letter that begins 'Dear residents of Maple Street' is written for...", "people who live on that street", ["all adults worldwide", "only students", "tourists"], "The greeting names the audience.")
H('8.E.iii', 4, "How does knowing the audience help an author?", "to choose vocabulary, tone and evidence that will persuade them", ["to avoid evidence", "to skip a thesis", "to lengthen the text"], "Audience shapes choices.")

# 9.A
H('9.A', 3, "A pamphlet urging people to conserve water has the purpose of...", "persuading readers to act", ["telling a joke", "describing a mountain", "teaching a dance"], "It aims to persuade.")
H('9.A', 4, "A narrative about a family weathering a flood ends with neighbors rebuilding together. What message is conveyed?", "communities can recover through cooperation", ["floods are fun", "families should move", "water is useless"], "The ending highlights the message.")
H('9.A', 3, "A science article explaining how vaccines work has the purpose of...", "informing", ["frightening readers", "entertaining with jokes", "selling a product"], "It explains facts.")

# 9.B
H('9.B', 3, "An author uses chronological order to describe an inventor's career. How does this support the purpose?", "it lets readers follow events in order", ["it hides events", "it removes dates", "it reverses causes"], "Structure clarifies narration.")
H('9.B', 4, "A writer uses a compare-and-contrast structure to discuss two energy sources. This helps readers...", "see similarities and differences clearly", ["avoid evidence", "skip details", "read backward"], "Structure matches purpose.")
H('9.B', 3, "Cause-and-effect structure in a history text helps the author...", "explain why events happened", ["list unrelated facts", "add rhymes", "hide results"], "Structure supports explanation.")

# 9.C
H('9.C', 3, "A bold heading in an article helps readers...", "locate main sections quickly", ["forget the topic", "skip all text", "change the genre"], "Headings organize.")
H('9.C', 3, "A caption under a photograph is used to...", "explain what the image shows", ["end the article", "list the sources", "give the author's address"], "Captions explain images.")
H('9.C', 4, "A magazine uses a large infographic about rising sea levels. What purpose does this serve?", "to present data visually for quick understanding", ["to confuse the reader", "to replace the text with a poem", "to hide the evidence"], "Graphics condense data.")

# 9.D
H('9.D', 3, "An extended metaphor is...", "a comparison developed over several lines or paragraphs", ["a one-word rhyme", "a list of facts", "a sound effect"], "Extended = continued.")
H('9.D', 4, "A writer compares life to a long road throughout an entire essay, mentioning detours, signposts and mile markers. This is a(n)...", "extended metaphor", ["onomatopoeia", "alliteration", "oxymoron"], "A comparison sustained across a text.")
H('9.D', 3, "'The wind whispered through the trees' is an example of...", "personification", ["hyperbole", "simile", "idiom"], "Wind is given a human action.")

# 9.E
H('9.E', 3, "A story is told by two characters who see the same event differently. This uses...", "multiple points of view", ["a single narrator", "an index", "a glossary"], "Different perspectives.")
H('9.E', 3, "A fire station that burns down on the day of a fire-safety fair is an example of...", "irony", ["alliteration", "simile", "rhyme"], "Outcome opposite of expectation.")
H('9.E', 4, "A reader knows a character is walking into a trap, but the character does not. This is...", "dramatic irony", ["situational irony only", "verbal irony only", "a flashback"], "The audience knows more than the character.")

# 9.F
H('9.F', 3, "Words like 'gloomy,' 'shadowed' and 'silent' most likely create what mood?", "somber", ["joyful", "silly", "energetic"], "Word choice sets mood.")
H('9.F', 4, "An author's distinctive style, including sentence length and word choice, contributes to the author's...", "voice", ["table of contents", "index", "glossary"], "Voice is the author's personality in writing.")
H('9.F', 3, "A narrator who calls a dull meeting 'a thrilling festival of paperwork' uses what tone?", "sarcastic", ["sincere", "fearful", "formal"], "Words say the opposite of the meaning.")

# 9.G
H('9.G', 3, "An analogy explains something unfamiliar by...", "comparing it to something familiar", ["listing synonyms", "citing a source", "removing detail"], "Analogy compares.")
H('9.G', 4, "'Just as a seed needs sunlight to grow, a student needs encouragement to learn.' This is an example of...", "analogy", ["juxtaposition", "a slippery slope", "a statistic"], "It parallels two relationships.")
H('9.G', 3, "Placing a lavish party next to a scene of hunger to highlight inequality is...", "juxtaposition", ["alliteration", "foreshadowing", "a pun"], "Contrasting items side by side.")

# 10.B.i
H('10.B.i', 3, "Which transition best shows contrast between two paragraphs?", "On the other hand,", ["For example,", "Similarly,", "In addition,"], "'On the other hand' signals contrast.")
H('10.B.i', 4, "A conclusion should...", "restate the thesis in a fresh way and leave a lasting thought", ["introduce a new unrelated topic", "repeat the introduction word for word", "list only sources"], "Conclusions close the argument.")

# 10.B.ii
H('10.B.ii', 3, "Which sentence best develops the idea that cities need green space?", "Parks cool neighborhoods, reduce stress and give families places to gather.", ["Parks are fine.", "Cities exist.", "Some parks have grass."], "Specific details develop depth.")
H('10.B.ii', 4, "Which addition adds depth of thought to 'Reading improves writing'?", "Exposure to varied sentences helps writers learn rhythm, vocabulary and structure.", ["Reading is a verb.", "Books have covers.", "Writing happens at desks."], "Explains why.")

# 10.C
H('10.C', 3, "Which revision improves word choice in 'The movie was good'?", "The movie was gripping and beautifully filmed.", ["The movie was movie-ish.", "The movie was.", "The movie was fine fine."], "Precise adjectives.")
H('10.C', 4, "A paragraph jumps between ideas with no logical order. Which revision step fits?", "reorganize sentences so related ideas are grouped", ["add more adjectives", "fix commas only", "change the title"], "Revising for organization.")
H('10.C', 3, "A writer combines two short choppy sentences into one smooth sentence. This improves...", "sentence variety and flow", ["spelling only", "the title", "the byline"], "Combining sentences adds variety.")

# 10.D.i
H('10.D.i', 3, "Which is a run-on sentence?", "The storm was loud we hid in the basement.", ["The storm was loud, so we hid in the basement.", "We hid in the basement because the storm was loud.", "The storm was loud; we hid in the basement."], "Two clauses fused with no punctuation.")
H('10.D.i', 4, "Which sentence has correct subject-verb agreement?", "Neither the coach nor the players were ready.", ["Neither the coach nor the players was ready.", "Neither the coach nor the players is ready.", "Neither the coach nor the players be ready."], "Verb agrees with the nearer subject (players).")
H('10.D.i', 3, "Which is a sentence fragment?", "Because the bus was late.", ["The bus was late.", "We waited for the bus.", "The bus finally arrived."], "A dependent clause without a main clause.")

# 10.D.ii
H('10.D.ii', 3, "Which sentence is in the passive voice?", "The window was broken by the ball.", ["The ball broke the window.", "The ball hit hard.", "We saw the ball."], "The subject receives the action.")
H('10.D.ii', 3, "Which revision changes 'The cake was eaten by the guests' to active voice?", "The guests ate the cake.", ["The cake was eaten.", "Eaten by the guests was the cake.", "The cake the guests eaten."], "The doer is the subject.")
H('10.D.ii', 4, "Which sentence keeps verb tense consistent?", "She walked to the park and played soccer.", ["She walked to the park and plays soccer.", "She walks to the park and played soccer.", "She will walk to the park and played soccer."], "Both verbs are past tense.")

# 10.D.iii
H('10.D.iii', 3, "In 'The box of pencils is on the shelf,' what is the subject?", "box", ["pencils", "shelf", "is"], "The prepositional phrase does not determine agreement.")
H('10.D.iii', 4, "Choose the correct verb: 'The teacher, along with her students, ____ going on the trip.'", "is", ["are", "were", "have been"], "The subject 'teacher' is singular.")
H('10.D.iii', 3, "Which is a prepositional phrase?", "under the bridge", ["ran quickly", "the tall boy", "and sang"], "Preposition plus object.")

# 10.D.iv
H('10.D.iv', 3, "Choose the correct pronoun: 'Neither of the girls left ____ umbrella.'", "her", ["their", "our", "his or their"], "'Neither' is singular.")
H('10.D.iv', 4, "Which sentence has a vague pronoun reference?", "When Sam met Jack, he was nervous.", ["Sam was nervous when he met Jack.", "Jack was nervous when he met Sam.", "Sam met Jack, and Sam was nervous."], "'He' could refer to either person.")
H('10.D.iv', 3, "Choose the correct pronoun: 'The committee made ____ decision.'", "its", ["their own selves", "they", "his or hers and theirs"], "Collective noun as one unit.")

# 10.D.v
H('10.D.v', 3, "Which word group needs capital letters?", "the Rocky Mountains", ["a tall mountain", "the nearby valley", "a small river"], "Specific place names are capitalized.")
H('10.D.v', 3, "Which small word is usually left lowercase in the middle of a title?", "of", ["Journey", "Center", "Earth"], "Short prepositions stay lowercase.")
H('10.D.v', 2, "Which needs a capital letter?", "monday", ["morning", "week", "today"], "Days of the week are proper nouns.")

# 10.D.vi
H('10.D.vi', 3, "Which sentence uses a colon correctly?", "You will need three things: a pencil, paper and a ruler.", ["You will need: three things a pencil, paper and a ruler.", "You will: need three things a pencil, paper and a ruler.", "You will need three: things a pencil, paper and a ruler."], "A colon follows a complete clause introducing a list.")
H('10.D.vi', 4, "Which sentence correctly uses parentheses?", "The festival (held every June) draws thousands.", ["The festival (held every June draws thousands.", "The festival held) every June (draws thousands.", "The festival ()held every June draws thousands."], "Parentheses enclose extra information.")
H('10.D.vi', 3, "Which sentence correctly punctuates a nonrestrictive clause?", "My brother, who plays tuba, joined the band.", ["My brother who plays tuba, joined the band.", "My brother, who plays tuba joined the band.", "My, brother who plays tuba joined the band."], "Commas set off nonessential clauses.")

# 10.D.vii
H('10.D.vii', 3, "Choose the correct word: 'The dog wagged ____ tail.'", "its", ["it's", "its'", "it is"], "'Its' shows possession.")
H('10.D.vii', 3, "Choose the correct word: 'Put the books over ____.'", "there", ["their", "they're", "theyre"], "'There' indicates place.")
H('10.D.vii', 3, "Choose the correct word: 'The new law will ____ many families.'", "affect", ["effect", "afect", "effects-on"], "Affect is a verb meaning to influence.")

# 12.E
H('12.E', 3, "A photograph taken during a 1963 march is a...", "primary source", ["secondary source", "textbook", "encyclopedia article"], "Created at the time.")
H('12.E', 4, "A magazine article written last year analyzing a 1920s trial is a...", "secondary source", ["primary source", "diary", "court record"], "It analyzes events from later.")
H('12.E', 3, "Which is a primary source?", "an original letter written during a war", ["a documentary made years later", "a history textbook", "a biography written by someone else"], "Firsthand and original.")

# 12.G
H('12.G', 3, "Which is an example of plagiarism?", "using another author's sentences without credit", ["summarizing and citing", "quoting with quotation marks and credit", "paraphrasing and citing"], "Uncredited copying.")
H('12.G', 4, "Which is acceptable paraphrasing?", "restating the idea in your own words and citing the source", ["changing two words and not citing", "copying and pasting", "using the author's exact wording without credit"], "Original wording plus credit.")
H('12.G', 3, "Why is citing sources important?", "it gives credit and shows where information came from", ["it shortens the essay", "it hides the evidence", "it adds rhymes"], "Citations are ethical.")

# 12.H
H('12.H.i', 3, "Which clue suggests a source is less credible?", "no author or date and no listed sources", ["a named expert author", "a recent date", "cited research"], "Missing information reduces credibility.")
H('12.H.i', 4, "A pamphlet from a company reports only positive reviews of its product. This is an example of...", "bias by omission", ["a primary source", "a balanced report", "an unbiased study"], "Negative information is left out.")
H('12.H.i', 3, "A reader checks whether an article's claims match other reliable sources. This evaluates...", "reliability", ["spelling only", "the font", "the page color"], "Corroboration shows reliability.")
H('12.H.ii', 3, "'Everybody is switching to this brand' is an example of...", "a bandwagon appeal", ["a statistic", "a primary source", "a definition"], "It relies on popularity.")
H('12.H.ii', 4, "An ad repeats 'Fast, fast, fast!' in every sentence instead of giving evidence. This faulty reasoning is...", "repetition", ["a citation", "a counterargument", "an analogy"], "Repetition replaces proof.")
H('12.H.ii', 4, "Calling a proposal 'a reckless scheme by selfish politicians' uses...", "loaded language", ["neutral language", "a statistic", "a quotation"], "Emotional words slant the message.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g8_ela.jsonl'))
print("saved", len(B.out), "questions")

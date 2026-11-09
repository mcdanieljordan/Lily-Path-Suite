#!/usr/bin/env python3
"""High school English I (TEKS 110.36.c). Original questions, knowledge/reading skills only."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('110.36.c.', 991, own='hs_eng1.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A reference tools
H('2.A', 2, "Which resource would best help a ninth grader confirm the pronunciation and part of speech of the word 'ephemeral'?", "a dictionary", ["an atlas", "a thesaurus alone", "an almanac"], "Dictionaries list pronunciation, part of speech and meaning.")
H('2.A', 3, "A student needs a word that means almost the same as 'brave' but sounds more formal. Which tool helps most?", "a thesaurus", ["a glossary of a science book", "an atlas", "a style manual"], "A thesaurus lists synonyms.")
H('2.A', 3, "A technical manual includes a section at the back listing specialized terms with definitions. What is it called?", "a glossary", ["an index", "a preface", "an appendix of maps"], "A glossary defines key terms from the text.")

# 2.B denotative/connotative
H('2.B', 3, "Which word has the most positive connotation for describing a person who spends carefully?", "thrifty", ["stingy", "cheap", "miserly"], "All share the denotation of careful spending, but 'thrifty' feels positive.")
H('2.B', 3, "The denotative meaning of a word is what?", "its literal dictionary definition", ["the feelings it suggests", "its sound", "its spelling history only"], "Denotation is the literal meaning.")
H('2.B', 3, "A writer calls a crowd 'a swarm.' How does this word choice affect the tone compared with 'a gathering'?", "it suggests something chaotic and unwelcome", ["it suggests calm and organized", "it has no added feeling", "it suggests silence"], "'Swarm' connotes insects and disorder.")
H('2.B', 4, "Which pair shows the same denotation but different connotations?", "slim and scrawny", ["hot and cold", "dog and cat", "run and sleep"], "Both describe thinness, but one is kinder.")

# 2.C foreign phrases
H('2.C', 3, "The phrase 'bona fide' used in English most nearly means what?", "genuine", ["temporary", "forbidden", "fancy"], "From Latin, 'in good faith.'")
H('2.C', 3, "A writer says a plan has 'carte blanche' approval. What does the phrase suggest?", "complete freedom to act", ["a ban on all action", "a partial approval", "a request to wait"], "From French, 'blank paper.'")
H('2.C', 3, "What does 'status quo' refer to?", "the existing state of affairs", ["a future goal", "a past mistake", "a rare event"], "Latin for 'the state in which.'")
H('2.C', 4, "'Ad hoc committee' means a committee formed for what?", "a specific purpose at hand", ["permanent service", "a yearly review", "no particular reason"], "'Ad hoc' means 'for this.'")

# 4.F inference
H('4.F', 3, "Passage: 'Mara checked the clock a fourth time and drummed her fingers on the desk until the bell finally rang.' What can be inferred about Mara?", "she is impatient or anxious for class to end", ["she is deeply interested in the lesson", "she has fallen asleep", "she is the teacher"], "Her repeated clock-checking signals impatience.")
H('4.F', 3, "Passage: 'The streets were empty, shutters closed, and not a single dog barked.' What is the best inference?", "something has made the town fearful or quiet", ["a festival is under way", "it is midday market time", "everyone is on vacation at the beach"], "The details imply tension or danger.")
H('4.F', 3, "An inference must be supported by what?", "evidence from the text", ["a guess with no basis", "the reader's mood", "the author's biography only"], "Strong inferences use details.")

# 4.G key ideas
H('4.G', 3, "Which detail is most likely to reveal the key idea of an informational article?", "a claim repeated and developed across several paragraphs", ["an aside in one sentence", "the date of publication", "a long quotation of a minor figure"], "Key ideas are developed throughout.")
H('4.G', 3, "After reading, you must separate important details from minor ones. What are you doing?", "evaluating details to find key ideas", ["predicting the plot", "making a personal connection", "creating a mental image"], "This is the evaluation of details.")
H('4.G', 4, "In an editorial, the author lists three examples of lost wetland habitat. The key idea they support is most likely what?", "wetland loss is a serious problem", ["wetlands are easy to rebuild", "habitats do not matter", "the author dislikes birds"], "Examples back up the central claim.")

# 4.H synthesis
H('4.H', 4, "Text A says a river's water quality improved after 2005. Text B says fish counts rose after 2005. What new understanding could a reader synthesize?", "cleaner water may have helped fish populations recover", ["fish cause water to be clean", "nothing connects the two", "the river dried up"], "Combining two sources suggests a link.")
H('4.H', 3, "To synthesize information from two texts, a reader should do what?", "combine ideas from both to form a new understanding", ["copy one text", "summarize only the longer text", "ignore differences"], "Synthesis builds something new.")

# 4.I monitor comprehension
H('4.I', 2, "A reader loses track of the plot halfway through a chapter. Which strategy fits best?", "re-reading the confusing section", ["skipping to the end", "closing the book for good", "memorizing the title"], "Re-reading is a repair strategy.")
H('4.I', 3, "Which is an example of using background knowledge to repair comprehension?", "recalling what you know about the Great Depression while reading a novel set in 1933", ["counting the pages", "changing the font", "reading only the first line"], "Prior knowledge fills gaps.")

# 5.B compare texts
H('5.B', 3, "A student writes a response comparing how two poems treat the theme of loss. Which sentence best shows comparison?", "Both poems explore grief, but the first uses nature imagery while the second uses household objects.", ["The first poem is long.", "I like poems about loss.", "Poems are written in lines."], "Comparison names a shared idea and a difference.")
H('5.B', 3, "Which transition word signals a contrast between two texts?", "however", ["furthermore", "likewise", "similarly"], "'However' marks a difference.")
H('5.B', 4, "Which thesis best sets up a comparison of two short stories?", "Though both stories feature a lonely narrator, one resolves isolation through friendship while the other accepts it.", ["Both stories are about narrators.", "Stories are fun to read.", "The first story came first."], "A strong comparison thesis states a similarity and a difference.")

# 5.C text evidence and commentary
H('5.C', 3, "Which is an example of original commentary after a quotation?", "This line shows how the narrator's guilt grows throughout the scene.", ["The narrator says 'I should have stayed.'", "Page 14 has this line.", "The quote is in quotation marks."], "Commentary explains the significance of evidence.")
H('5.C', 3, "A response includes a quotation but no explanation. What is missing?", "commentary linking the evidence to the claim", ["a title", "a longer quote", "more adjectives"], "Evidence must be explained.")
H('5.C', 3, "Which sentence best introduces a piece of text evidence?", "The author emphasizes her fear when she writes, 'My hands would not stop shaking.'", ["Here is a quote: 'My hands would not stop shaking.'", "'My hands would not stop shaking.'", "Quote."], "A signal phrase connects the evidence to the idea.")

# 5.D paraphrase and summarize
H('5.D', 3, "Which is the best paraphrase of 'The meeting was adjourned because of the absence of a quorum'?", "The meeting ended because not enough members were present.", ["The meeting was fun and short.", "Everyone left angry.", "The quorum cancelled the room."], "A paraphrase keeps meaning in new words.")
H('5.D', 3, "A good summary of a long article should do what?", "include the main ideas in logical order and in your own words", ["copy every sentence", "add your opinions", "include every detail"], "Summaries are brief and faithful.")
H('5.D', 4, "Which summary sentence introduces a new opinion, making it a poor summary?", "The author is clearly wrong about renewable energy.", ["The author argues renewable energy can lower costs.", "The article lists three advantages.", "The author concludes with a call for investment."], "A summary reports; it does not judge.")

# 5.F academic vocabulary
H('5.F', 3, "In a literary response, which word is most precise academic vocabulary for the central message of a story?", "theme", ["thing", "stuff", "idea of the part"], "'Theme' is the standard term.")
H('5.F', 3, "Which sentence uses academic vocabulary appropriately?", "The author uses foreshadowing to hint at the conflict.", ["The author put in some hints to be cool.", "The author did a thing early on.", "The story had stuff."], "Precise terms improve a response.")

# 5.G explicit/implicit meaning
H('5.G', 3, "An explicit meaning in a text is one that is what?", "directly stated", ["only implied", "hidden in symbols", "a reader's guess"], "Explicit means stated plainly.")
H('5.G', 3, "'She slammed the door and did not say goodbye.' What implicit meaning does this carry?", "she is angry", ["she is cheerful", "she is shy", "she is sleepy"], "Actions imply feelings.")
H('5.G', 4, "A narrator describes a once-lively house as 'quiet as a held breath.' What is implied?", "the house feels tense or waiting", ["the house is newly built", "the house is noisy", "the narrator is moving in"], "The simile suggests suspense.")

# 5.J defend or challenge claims
H('5.J', 4, "An author claims 'all teenagers dislike reading,' citing a survey of 12 students in one class. What is the best challenge?", "the evidence is too limited to support such a broad claim", ["the sample was too large", "surveys are never valid", "teenagers never read"], "A hasty generalization from a tiny sample.")
H('5.J', 3, "To defend an author's claim, a writer should use what?", "relevant evidence from the text", ["a personal anecdote only", "a longer essay", "a stronger adjective"], "Evidence-based defense.")
H('5.J', 4, "Which response most effectively challenges an author's claim?", "It identifies a specific weakness and cites text evidence", ["It says the author is boring", "It repeats the author's claim", "It states 'I disagree' with no reason"], "Support needed.")

# 6.A theme via characterization and plot
H('6.A', 3, "A character begins greedy but gives away his fortune after a disaster. Which theme is developed?", "suffering can change what a person values", ["money is the most important thing", "disasters never matter", "greed is permanent"], "His arc shows change.")
H('6.A', 3, "How can a plot's resolution help reveal theme?", "the outcome suggests the author's message about the conflict", ["it makes the story shorter", "it introduces new characters only", "it lists the setting"], "Outcomes carry meaning.")
H('6.A', 4, "A hero succeeds only after admitting she needs help. Which theme is best supported?", "accepting help can be a strength", ["strong people never ask for help", "success is luck", "teamwork is a mistake"], "Her change supports the idea.")

# 6.B complex characters
H('6.B', 3, "Which technique reveals a character's thoughts directly?", "interior monologue", ["setting description", "foreshadowing", "rhyme scheme"], "It shows inner thoughts.")
H('6.B', 3, "A character is generous but also quick-tempered. What term describes this kind of multi-sided character?", "round character", ["flat character", "stock character", "foil"], "Round characters have complexity.")
H('6.B', 4, "A narrator describes a character only through what others say about him. What type of characterization is this?", "indirect characterization", ["direct characterization", "interior monologue", "omniscient narration"], "Traits are shown through others' views.")
H('6.B', 3, "A character who contrasts with another to highlight traits is called what?", "a foil", ["a narrator", "a protagonist", "an epigraph"], "A foil emphasizes differences.")

# 6.C nonlinear plot
H('6.C', 2, "A scene that jumps back to an earlier event is called what?", "a flashback", ["foreshadowing", "a climax", "a resolution"], "It interrupts the timeline.")
H('6.C', 3, "A narrator mentions a loaded gun in act one that is never used until the ending. This is an example of what?", "foreshadowing", ["a flashback", "irony only", "a refrain"], "Early hints suggest later events.")
H('6.C', 3, "A secondary story that runs alongside the main plot is called what?", "a subplot", ["an exposition", "a prologue only", "a motif"], "A subplot adds depth.")
H('6.C', 4, "Two storylines that echo each other's events are known as what?", "parallel plots", ["a frame story only", "a monologue", "an allegory"], "They mirror one another.")

# 6.D setting and theme
H('6.D', 3, "A story set during a long drought explores survival and community. How does the setting influence the theme?", "the harsh conditions make cooperation central to the message", ["it has no connection", "it changes the narrator's name", "it supplies the rhyme"], "Setting shapes meaning.")
H('6.D', 3, "A novel set in a crowded city emphasizes loneliness. What is the effect of the setting?", "it contrasts crowds with isolation to deepen the theme", ["it hides the theme", "it removes conflict", "it sets the rhythm"], "Contrast strengthens meaning.")

# 7.A American, British, world literature
H('7.A', 3, "Which work is a play by William Shakespeare?", "Romeo and Juliet", ["The Great Gatsby", "Pride and Prejudice", "Things Fall Apart"], "Shakespeare wrote Romeo and Juliet.")
H('7.A', 3, "Which novel was written by Chinua Achebe, a Nigerian author?", "Things Fall Apart", ["Jane Eyre", "To Kill a Mockingbird", "The Odyssey"], "A landmark African novel.")
H('7.A', 3, "Which epic poem is attributed to Homer?", "The Odyssey", ["Beowulf", "Paradise Lost", "Don Quixote"], "Homer is credited with it.")
H('7.A', 3, "Which novelist wrote 'To Kill a Mockingbird'?", "Harper Lee", ["Toni Morrison", "John Steinbeck", "Mark Twain"], "An American classic.")

# 7.B poetry structure
H('7.B', 3, "A poem with fourteen lines and a set rhyme scheme is called what?", "a sonnet", ["a haiku", "a limerick", "free verse"], "Sonnets have 14 lines.")
H('7.B', 3, "What is the term for poetry with no regular rhyme or meter?", "free verse", ["blank verse", "a ballad", "an ode"], "No fixed pattern.")
H('7.B', 4, "Unrhymed lines of iambic pentameter are called what?", "blank verse", ["free verse", "a couplet", "a quatrain"], "Common in Shakespeare's plays.")
H('7.B', 3, "How many lines are in a quatrain?", "four", ["two", "six", "eight"], "A quatrain is a four-line stanza.")

# 7.C dramatic conventions
H('7.C', 3, "In a play, a character speaks alone onstage to reveal inner thoughts. What is this called?", "a soliloquy", ["an aside to another actor", "a prologue", "a stage direction"], "A soliloquy is spoken alone.")
H('7.C', 3, "A short remark to the audience unheard by other characters is called what?", "an aside", ["a soliloquy", "an epilogue", "a scene"], "Others onstage do not hear it.")
H('7.C', 4, "The audience knows a character is in danger but the character does not. This is called what?", "dramatic irony", ["verbal irony", "situational irony", "an oxymoron"], "The audience knows more.")

# 7.D.i argumentative/ informational? 7.D.i thesis structure; 7.D.ii patterns
H('7.D.i', 3, "Which of these is the strongest thesis statement for an expository essay?", "Public libraries strengthen communities by offering free access to learning, technology and shared space.", ["Libraries are places.", "I will write about libraries.", "Do you like libraries?"], "A thesis states a clear, supportable claim.")
H('7.D.i', 3, "Where does a conclusion usually restate the thesis?", "at the end of the essay", ["before the introduction", "in the middle", "in the title only"], "Conclusions close with the main idea.")
H('7.D.ii', 3, "An essay explains how a volcano erupts by describing each step in order. What organizational pattern is used?", "chronological order", ["compare and contrast", "problem and solution", "spatial order"], "Steps follow a time sequence.")
H('7.D.ii', 3, "An essay describes a problem of plastic waste and then proposes recycling programs. What pattern is this?", "problem and solution", ["cause and effect", "chronological", "descriptive only"], "It states a problem then solutions.")

# 7.E argumentative texts
H('7.E.i', 3, "A strong argumentative claim is what?", "a statement that can be debated and supported", ["an undeniable fact", "a question", "a quotation"], "Claims must be arguable.")
H('7.E.i', 3, "Which appeal relies on facts and logic?", "logos", ["ethos", "pathos", "kairos only"], "Logos is reason.")
H('7.E.ii', 3, "In an argument, acknowledging an opposing view and then explaining why it is weaker is called what?", "a rebuttal", ["a concession alone", "a summary", "an anecdote"], "A rebuttal answers the counterargument.")
H('7.E.ii', 4, "A writer says, 'Some argue uniforms limit self-expression; that is true for some, but they also reduce distraction.' What is the first half of the sentence?", "a concession", ["a thesis", "a rebuttal", "a hook"], "A concession grants a point.")
H('7.E.iii', 3, "Who is an argument's audience?", "the readers the writer hopes to persuade", ["only the writer", "the printer", "the editor's family"], "Arguments are shaped for readers.")
H('7.E.iii', 3, "Which tone suits an argument aimed at a school board?", "respectful and formal", ["jokey and slangy", "angry and insulting", "silent"], "Audience shapes tone.")

# 7.F multimodal
H('7.F', 3, "Which is a characteristic of a multimodal text?", "it combines words with images, sound or video", ["it uses only words", "it has no author", "it cannot be digital"], "Multiple modes work together.")
H('7.F', 3, "A news website uses an infographic with a video. What does the infographic add?", "a visual summary of data", ["an unrelated advertisement", "a spelling check", "a rhyme"], "Visuals convey information.")
H('7.F', 3, "Which feature helps a reader navigate a website?", "hyperlinks and menus", ["footnotes in a novel", "a stanza break", "a glossary of poems"], "Digital texts use navigation tools.")

# 8.A purpose, audience, message
H('8.A', 3, "A pamphlet lists symptoms and prevention tips for the flu. What is its most likely purpose?", "to inform", ["to entertain", "to mock", "to sell a novel"], "It conveys useful information.")
H('8.A', 3, "A speech urges voters to approve a new park bond. What is the author's purpose?", "to persuade", ["to describe a character", "to entertain with jokes", "to give directions"], "It seeks to change minds.")
H('8.A', 4, "A blog written for beginners uses simple terms and avoids jargon. Who is the intended audience?", "novices", ["experts", "lawyers only", "professors"], "Language reflects audience.")

# 8.B text structure
H('8.B', 3, "An article describes how deforestation leads to soil erosion and flooding. What structure is it?", "cause and effect", ["compare and contrast", "sequence", "description"], "It links cause to results.")
H('8.B', 3, "A text lists similarities and differences between two economic systems. What structure is it?", "compare and contrast", ["problem and solution", "chronological", "cause and effect"], "It weighs likenesses and differences.")
H('8.B', 3, "A history chapter lists events in the order they occurred. What structure is it?", "chronological", ["spatial", "compare and contrast", "order of importance"], "Time order.")

# 8.C print and graphic features
H('8.C', 3, "Why might an author use bold headings in an article?", "to help readers locate and organize sections", ["to make the text harder to read", "to hide the main idea", "to lengthen it"], "Headings guide readers.")
H('8.C', 3, "A bar graph accompanies a paragraph on rising temperatures. What purpose does the graph serve?", "it presents data clearly to support the text", ["it replaces all text", "it is decoration", "it contradicts the text"], "Graphics support claims.")
H('8.C', 3, "Italicized terms followed by definitions in a textbook help readers do what?", "learn key vocabulary", ["skip the chapter", "find the author's name", "count the pages"], "Print features signal terms.")

# 8.D language
H('8.D', 3, "A writer compares a city at night to 'a jewelry box spilled open.' What does this language achieve?", "it creates a vivid, glittering image", ["it states a statistic", "it lists directions", "it avoids imagery"], "Figurative language paints a picture.")
H('8.D', 3, "Why might an author repeat a phrase at the start of successive sentences?", "to emphasize an idea and build rhythm", ["to save space", "to hide meaning", "to confuse readers"], "Repetition builds emphasis.")
H('8.D', 4, "A speaker uses the phrase 'we shall' repeatedly. What effect is likely?", "a powerful, determined rhythm", ["a casual tone", "doubt", "humor"], "Anaphora strengthens resolve.")

# 8.E irony, oxymoron
H('8.E', 3, "A fire station burns down. What kind of irony is this?", "situational irony", ["verbal irony", "dramatic irony", "an oxymoron"], "The outcome contradicts expectations.")
H('8.E', 3, "Which phrase is an oxymoron?", "deafening silence", ["very loud noise", "bright light", "a quiet room"], "It combines opposites.")
H('8.E', 3, "Someone says 'What lovely weather!' during a storm. What is this?", "verbal irony", ["situational irony", "dramatic irony", "alliteration"], "The speaker means the opposite.")
H('8.E', 3, "Which pair is an oxymoron?", "bittersweet", ["sweet and sour candy", "red roses", "sour milk"], "A single term merging opposites.")

# 8.F diction and syntax
H('8.F', 3, "An author uses short, choppy sentences during a chase scene. What effect does the syntax have?", "it creates urgency and tension", ["it creates calm", "it slows the pace", "it adds humor"], "Short sentences speed the pace.")
H('8.F', 3, "Formal diction in a narrator's voice creates what effect?", "a serious, dignified tone", ["a silly tone", "a casual tone", "no tone"], "Word choice shapes tone.")
H('8.F', 4, "Long, flowing sentences with many clauses most often suggest what mood?", "reflective or contemplative", ["panicked", "abrupt", "comedic"], "Syntax slows the reader.")

# 8.G rhetorical devices
H('8.G', 3, "Saying 'It's just a scratch' about a deep wound is an example of what?", "understatement", ["overstatement", "simile", "personification"], "Minimizing seriousness.")
H('8.G', 3, "'I've told you a million times' is an example of what?", "overstatement (hyperbole)", ["understatement", "irony", "an oxymoron"], "Exaggeration for emphasis.")
H('8.G', 4, "Why might a speaker use understatement?", "to create irony or emphasize by contrast", ["to confuse listeners", "to lengthen a speech", "to avoid meaning"], "It can heighten an effect.")

# 9.B.i organizing structure, 9.B.ii depth
H('9.B.i', 3, "Which structure fits an essay on the causes of the Dust Bowl?", "cause and effect", ["alphabetical", "random", "poem form"], "Match structure to purpose.")
H('9.B.i', 3, "What is the role of a topic sentence?", "to state the main idea of a paragraph", ["to end the essay", "to list sources", "to ask for feedback"], "It anchors the paragraph.")
H('9.B.ii', 3, "Which detail best develops the idea that a town is friendly?", "Neighbors waved from porches and brought casseroles to every new family.", ["The town has a street.", "It is a place.", "People live there."], "Specific details show depth.")
H('9.B.ii', 3, "What does adding a concrete example do for an idea?", "makes it clearer and more convincing", ["shortens the essay", "removes the thesis", "adds confusion"], "Examples strengthen development.")

# 9.C revision
H('9.C', 3, "A student combines three short, choppy sentences into one smooth sentence. What aspect of writing is improved?", "sentence variety and flow", ["spelling", "title", "citations"], "Revision improves style.")
H('9.C', 3, "Replacing 'good' with 'dependable' is mainly a revision of what?", "diction (word choice)", ["capitalization", "punctuation", "paragraphing"], "More precise words.")
H('9.C', 3, "Moving a paragraph so ideas follow a logical order improves what?", "organization", ["spelling", "vocabulary", "handwriting"], "Reordering helps clarity.")

# 9.D conventions
H('9.D.i', 3, "Which sentence is a run-on?", "The bus was late we walked to school.", ["The bus was late, so we walked to school.", "The bus was late; we walked to school.", "Because the bus was late, we walked to school."], "Two independent clauses lack punctuation.")
H('9.D.i', 3, "Which sentence contains a comma splice?", "The test was hard, I studied for it.", ["The test was hard; I studied for it.", "The test was hard, but I studied for it.", "I studied for the hard test."], "A comma alone cannot join independent clauses.")
H('9.D.ii', 3, "Which sentence has consistent verb tense?", "She opened the box and found a map.", ["She opened the box and finds a map.", "She opens the box and found a map.", "She open the box and finding a map."], "Both verbs are past tense.")
H('9.D.ii', 3, "Which sentence is in the passive voice?", "The window was broken by the storm.", ["The storm broke the window.", "The storm is strong.", "Storms break windows."], "The subject receives the action.")
H('9.D.iii', 3, "Which sentence has correct pronoun-antecedent agreement?", "Each student must bring his or her notebook.", ["Each student must bring their notebooks and he.", "Each student must bring our notebook.", "Each student must bring they notebook."], "Singular antecedent, singular pronoun.")
H('9.D.iii', 3, "Which pronoun best completes: 'The committee announced ____ decision.'", "its", ["their own and its", "it's", "theirs"], "A committee acts as a single unit.")
H('9.D.iv', 2, "In the sentence 'my aunt lives in houston,' which words need capital letters?", "my and houston", ["aunt and lives", "my and aunt", "lives and in"], "Capitalize the first word and proper nouns.")
H('9.D.iv', 3, "In standard title capitalization, which kind of word is normally left lowercase in the middle of a title?", "short conjunctions and prepositions", ["nouns", "verbs", "adjectives"], "Major words are capitalized.")
H('9.D.v', 3, "Which sentence uses a semicolon correctly?", "I wanted to go; however, it rained.", ["I wanted; to go however it rained.", "I wanted to go; but it rained;.", "I wanted to; go however, it rained."], "A semicolon joins related independent clauses.")
H('9.D.v', 3, "Which sentence uses a colon correctly?", "Bring three things: a pencil, paper and a calculator.", ["Bring: three things a pencil, paper and a calculator.", "Bring three: things, a pencil, paper.", "Bring three things a pencil: paper and a calculator."], "A colon follows a complete clause before a list.")
H('9.D.v', 3, "Which sentence uses dashes correctly to set off a phrase?", "My brother—who loves chess—won the tournament.", ["My brother—who loves chess won—the tournament.", "My—brother who loves chess won the tournament.", "My brother who—loves chess won the—tournament."], "Dashes enclose an interruption.")
H('9.D.vi', 2, "Which word is spelled correctly?", "necessary", ["neccessary", "necesary", "neccesary"], "One c, two s's.")
H('9.D.vi', 3, "Which word is spelled correctly?", "occurrence", ["occurence", "ocurrence", "occurrance"], "Double c and double r.")
H('9.D.vi', 3, "Which sentence uses the correct word?", "The principal gave the principle of fairness as her reason.", ["The principle gave the principal of fairness as her reason.", "The principal gave the principal of fairness.", "The principle gave the principle of fairness."], "Principal is a person; principle is a rule.")

# 10.D correspondence
H('10.D', 3, "Which closing is appropriate for a formal business letter?", "Sincerely,", ["Later!", "Your pal,", "Peace out,"], "Formal letters use formal closings.")
H('10.D', 3, "Which greeting suits a formal letter to an unknown hiring manager?", "Dear Hiring Manager:", ["Hey you,", "Yo,", "What's up,"], "Formal greeting with a colon.")

# 11 research
H('11.E', 3, "Which source is most likely to give reliable information about a historical event?", "a peer-reviewed history journal", ["an anonymous social media post", "a personal blog with no citations", "a satirical website"], "Scholarly sources are vetted.")
H('11.E', 3, "A library database is useful for locating what?", "published articles and reference materials", ["only novels", "only maps", "phone numbers"], "Databases index sources.")
H('11.F', 3, "To synthesize information from several sources, a researcher should do what?", "combine ideas into one coherent understanding with attribution", ["copy one source", "list sources only", "avoid comparing them"], "Synthesis merges and credits ideas.")
H('11.H', 3, "Why do writers cite sources?", "to give credit and let readers find the original", ["to make the paper longer", "to hide the author", "to confuse readers"], "Citations avoid plagiarism.")
H('11.H', 3, "Presenting someone else's wording as your own without credit is called what?", "plagiarism", ["paraphrasing", "summarizing", "annotating"], "It is a serious academic offense.")
H('11.G.i', 3, "Which clue suggests a source may be biased?", "it uses loaded language and omits opposing evidence", ["it cites several experts", "it includes data tables", "it lists a date"], "Omission and slant signal bias.")
H('11.G.i', 3, "Which author is most credible on climate science?", "a climate scientist at a university", ["an anonymous commenter", "a celebrity with no training", "a company selling a product"], "Expertise improves credibility.")
H('11.G.ii', 3, "Saying 'You can't trust his argument because he failed math' is which fallacy?", "ad hominem", ["slippery slope", "bandwagon", "false dilemma"], "It attacks the person, not the argument.")
H('11.G.ii', 3, "'If we allow this rule, soon there will be no rules at all' is an example of what?", "slippery slope", ["ad hominem", "circular reasoning", "appeal to authority"], "It predicts an extreme chain without proof.")
H('11.G.ii', 4, "A headline calls a policy 'a disastrous, reckless scheme' without evidence. Which problem is this?", "loaded language", ["a balanced tone", "a statistic", "a citation"], "Emotional words replace evidence.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_eng1.jsonl'))

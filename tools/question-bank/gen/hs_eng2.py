#!/usr/bin/env python3
"""High school English II (TEKS 110.37.c). Original questions; world-literature focus."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('110.37.c.', 992, own='hs_eng2.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A
H('2.A', 3, "A student reading a chemistry article meets the term 'covalent.' Which resource gives the most reliable technical definition?", "a technical dictionary", ["a movie review", "a travel guide", "a thesaurus of slang"], "Technical dictionaries define specialized vocabulary.")
H('2.A', 3, "Why would a reader check a glossary at the back of a nonfiction book?", "to confirm the book's own definitions of key terms", ["to find the publisher's address", "to see the next chapter", "to count the pages"], "Glossaries clarify specialized terms as used in the text.")
H('2.A', 3, "An online dictionary entry lists an etymology. What does that information explain?", "the origin and history of a word", ["the word's rhyme", "the page where it appears", "the author's opinion of it"], "Etymology traces word origins.")

# 2.B
H('2.B', 3, "A poem says 'the sun is a golden coin.' What kind of meaning is 'coin' here?", "figurative", ["denotative", "literal only", "technical"], "The sun is not literally a coin.")
H('2.B', 3, "Which word carries the strongest negative connotation for a person who speaks a lot?", "blabbermouth", ["talkative", "chatty", "communicative"], "The informal compound sounds insulting.")
H('2.B', 4, "In a novel, a character is called 'a fox.' Using context about clever schemes, what does the word suggest?", "cunning", ["furry", "fast-moving only", "friendly"], "Figurative use draws on a fox's reputation.")

# 2.C
H('2.C', 3, "A critic praises a dancer's 'pas de deux.' What does the phrase refer to?", "a dance for two performers", ["a solo dance", "a costume", "a stage curtain"], "French for 'step of two.'")
H('2.C', 3, "What does the phrase 'savoir faire' suggest about a person?", "skill at handling social situations gracefully", ["lack of training", "great wealth", "a love of travel"], "French for 'to know how to do.'")
H('2.C', 4, "A speech mentions 'quid pro quo.' What is described?", "an exchange of one thing for another", ["a free gift", "a secret code", "a legal appeal"], "Latin for 'something for something.'")

# 4.F
H('4.F', 3, "Passage: 'Kofi folded the letter into smaller and smaller squares, then slipped it, unread, into his coat.' What can be inferred?", "he is nervous or afraid of what the letter says", ["he is eager to read it aloud", "he is bored by mail", "he has forgotten the letter"], "Folding and hiding suggest dread.")
H('4.F', 3, "Passage: 'The market stalls were packed, yet the vendor lowered his voice whenever the soldiers passed.' What is the best inference?", "he feels cautious or threatened around the soldiers", ["he is selling to the soldiers", "the market is closed", "he enjoys the soldiers' company"], "Lowering his voice implies fear.")
H('4.F', 4, "Which statement is the best example of using evidence to support an inference?", "'She seems exhausted, since she yawned through every scene.'", ["'She is a person.'", "'I just feel she is tired.'", "'Many people yawn.'"], "A sound inference cites text details.")

# 4.G
H('4.G', 3, "When deciding on a text's key idea, a reader should do what with the details?", "judge which ones matter most to the central point", ["treat every detail as equally important", "ignore all of them", "count how many there are"], "Key ideas come from weighing details.")
H('4.G', 3, "A paragraph gives three examples of ocean pollution and one aside about a boat race. Which detail is least important to the key idea?", "the aside about the boat race", ["the first pollution example", "the second pollution example", "the third pollution example"], "The aside is off-topic.")
H('4.G', 4, "An article's last paragraph restates its main claim. Why is that detail helpful to a reader?", "it confirms the key idea", ["it hides the key idea", "it introduces a new topic", "it lists sources"], "Conclusions often reinforce main ideas.")

# 4.H
H('4.H', 3, "One article says a river's flow dropped after a dam; another says fish numbers fell downstream. What new understanding could a reader create?", "the dam may have harmed fish by reducing flow", ["rivers never change", "fish prefer dams", "the articles contradict each other entirely"], "Synthesis links ideas across texts.")
H('4.H', 3, "Which action best shows synthesizing two texts?", "combining their ideas into a new conclusion", ["reading only the longer one", "copying the first one", "memorizing both"], "Synthesis creates new understanding.")

# 4.I
H('4.I', 2, "A reader realizes she cannot explain what she just read. What is the best strategy?", "re-read the section slowly and ask questions", ["keep going without thinking", "skip to the last page", "stop reading for good"], "Monitoring comprehension calls for adjustment.")
H('4.I', 3, "Which fix-up strategy uses what the reader already knows?", "using background knowledge to understand a confusing passage", ["ignoring unfamiliar words", "reading faster", "covering the page"], "Prior knowledge aids comprehension.")

# 5.B
H('5.B', 3, "A student writes a response comparing how two poems treat the idea of time. This response shows what?", "understanding across texts", ["a spelling mistake", "a summary of one poem only", "a personal diary entry"], "Comparing texts shows understanding.")
H('5.B', 3, "Which sentence best begins a comparison between two characters?", "'Both characters face betrayal, but they respond in opposite ways.'", ["'I like characters.'", "'Betrayal is a word.'", "'The book has chapters.'"], "A comparison names similarity and difference.")

# 5.C
H('5.C', 3, "In an interpretive response, what combination is strongest?", "a quotation followed by the writer's own commentary", ["a quotation alone", "commentary alone with no text", "a list of plot points"], "Evidence plus commentary supports interpretation.")
H('5.C', 3, "A student quotes a line, then writes, 'This shows the narrator's guilt because...' What is the second part called?", "commentary", ["a citation", "a thesis", "a transition only"], "Commentary explains the evidence.")
H('5.C', 4, "Which is the weakest use of text evidence in an interpretive paragraph?", "dropping a quotation in with no explanation", ["introducing the quotation, then explaining it", "choosing a quotation that fits the claim", "linking the quotation to the thesis"], "Evidence needs explanation.")

# 5.D
H('5.D', 3, "A good paraphrase of a sentence should do what?", "keep the meaning while using different words", ["copy the exact words", "change the meaning", "add the writer's opinion"], "Paraphrase restates in your own words.")
H('5.D', 3, "A summary of a long story should include what?", "the main events in logical order", ["every minor detail", "only the ending", "the reader's feelings only"], "Summaries are concise and ordered.")
H('5.D', 4, "Which sentence is a summary rather than a paraphrase of a whole chapter?", "'The chapter traces the family's journey from drought to a new home.'", ["'The first sentence says it was dry.'", "'I felt sad.'", "'The chapter has thirty pages.'"], "Summaries condense the whole.")

# 5.F
H('5.F', 3, "Which is an academic vocabulary word suited to a formal response?", "demonstrate", ["show off", "whatever", "kinda"], "Formal writing uses academic terms.")
H('5.F', 3, "A student studying the French Revolution should use which term for rule by one all-powerful leader?", "autocracy", ["picnic", "banquet", "festival"], "Content vocabulary helps precision.")

# 5.G
H('5.G', 3, "An explicit meaning in a text is one that is what?", "directly stated", ["only suggested", "hidden in the title", "not present"], "Explicit means stated.")
H('5.G', 3, "An implicit meaning in a text is one that is what?", "suggested but not stated", ["spelled out", "found in the footnotes", "the same as the title"], "Implicit meaning must be inferred.")
H('5.G', 4, "A narrator says, 'The old clock ticked on, though no one in the house listened anymore.' What implicit meaning is likely?", "the house has become lonely or abandoned", ["the clock is broken", "the narrator is a clockmaker", "everyone is asleep happily"], "Details imply emptiness.")

# 5.J
H('5.J', 3, "An author claims that every city needs a public library but offers only the opinion that books are nice. What is the best challenge?", "the evidence is too weak to support the claim", ["the claim uses long words", "the author is too famous", "the essay has a title"], "A claim needs relevant evidence.")
H('5.J', 4, "To defend an author's claim, a reader should do what?", "point to specific supporting evidence in the text", ["state a personal opinion with no proof", "attack the author", "ignore the text"], "Defending requires text evidence.")

# 6.A
H('6.A', 3, "In a story, a proud ruler loses everything because he refuses advice. Which theme is developed through his plot?", "pride can lead to downfall", ["advice is always wrong", "rulers never fail", "loss is meaningless"], "Plot consequences reveal theme.")
H('6.A', 4, "Two stories show characters who sacrifice for family. How can a reader compare their themes?", "by noting how each plot and character shows the value of family", ["by counting pages", "by comparing the titles", "by ignoring the endings"], "Compare how characters and plots develop ideas.")
H('6.A', 3, "A character who starts out selfish becomes generous after a crisis. This change most directly develops what?", "the theme", ["the rhyme scheme", "the setting's name", "the title page"], "Character change builds theme.")

# 6.B
H('6.B', 3, "A wise old mentor who guides the hero is an example of which kind of figure?", "an archetype", ["a footnote", "a stanza", "a glossary entry"], "Archetypes recur across cultures.")
H('6.B', 4, "Which technique makes a character feel believable rather than flat?", "giving the character both strengths and flaws", ["making them perfect", "making them identical to others", "giving them no motives"], "Believable characters are complex.")
H('6.B', 3, "A character born in a poor village in a strict era makes choices shaped by limited options. What shapes the character here?", "historical and cultural context", ["the rhyme scheme", "the page count", "the font"], "Context influences characterization.")

# 6.C
H('6.C', 3, "Why might an author include a brief scene of a character's act of kindness before the climax?", "to build sympathy that raises the stakes", ["to delay the title", "to avoid conflict", "to change the genre"], "Isolated scenes contribute to the whole plot.")
H('6.C', 4, "If a single scene is removed and the rest of the plot no longer makes sense, what does that show?", "the scene is essential to the plot", ["the scene is decoration", "the plot has no theme", "the author made a spelling error"], "Essential scenes carry the plot.")

# 6.D
H('6.D', 3, "A play set in a society that forbids certain marriages creates conflict. How does the cultural setting influence the plot?", "it creates obstacles for the characters", ["it removes conflict", "it ends the story", "it hides the characters"], "Setting shapes conflict.")
H('6.D', 4, "A story from ancient Greece centers on fate. How does the historical culture influence the theme?", "beliefs about fate shape what the characters believe they can change", ["culture has no effect", "fate is never mentioned", "the setting is only a backdrop"], "Cultural beliefs drive theme.")

# 7.A
H('7.A', 3, "Which epic from ancient Mesopotamia follows a king's search for immortality?", "The Epic of Gilgamesh", ["Beowulf", "The Odyssey", "The Aeneid"], "One of the oldest known works of literature.")
H('7.A', 3, "Which author wrote the novel 'Don Quixote'?", "Miguel de Cervantes", ["Leo Tolstoy", "Gabriel García Márquez", "Albert Camus"], "A foundational Spanish novel.")
H('7.A', 3, "Which Russian author wrote 'Crime and Punishment'?", "Fyodor Dostoevsky", ["Anton Chekhov", "Boris Pasternak", "Maxim Gorky"], "A major nineteenth-century novel.")
H('7.A', 4, "Which work by Sophocles features a king who unknowingly fulfills a prophecy?", "Oedipus Rex", ["Antigone", "The Frogs", "Medea"], "A classic tragedy of fate.")
H('7.A', 3, "Which 20th-century French author wrote 'The Stranger'?", "Albert Camus", ["Victor Hugo", "Jules Verne", "Molière"], "A key work of existentialism.")

# 7.B
H('7.B', 3, "Rhyme that occurs within a single line of poetry is called what?", "internal rhyme", ["end rhyme", "slant rhyme", "eye rhyme"], "Internal rhyme sits inside a line.")
H('7.B', 4, "Words that look like they should rhyme but do not, such as 'love' and 'move,' are an example of what?", "eye rhyme", ["end rhyme", "internal rhyme", "perfect rhyme"], "They match in spelling, not sound.")
H('7.B', 4, "Words with similar but not identical sounds, such as 'worm' and 'warm,' form what?", "slant rhyme", ["perfect rhyme", "eye rhyme", "internal rhyme"], "Slant rhyme is near rhyme.")
H('7.B', 3, "The pattern of stressed and unstressed syllables in a line of poetry is its what?", "meter", ["plot", "setting", "tone"], "Meter is the rhythmic pattern.")
H('7.B', 3, "A repeated line or phrase at intervals in a poem is called what?", "a refrain", ["a footnote", "a stage direction", "an index"], "Refrains echo through a poem.")

# 7.C
H('7.C', 3, "A work that uses humor and exaggeration to criticize society is called what?", "satire", ["an elegy", "an epic", "a memoir"], "Satire critiques through wit.")
H('7.C', 3, "A dramatic aside is spoken by a character to do what?", "share a remark with the audience unheard by the others", ["end the scene", "introduce the setting", "address the director"], "Asides reveal private thoughts.")
H('7.C', 4, "The audience knows a character is about to be betrayed; the character does not. This is which convention?", "dramatic irony", ["soliloquy", "foreshadowing only", "a prologue"], "Audience awareness creates tension.")

# 7.D
H('7.D.i', 3, "Which sentence is the clearest thesis for an essay on a novel's theme?", "'In the novel, the author shows that isolation weakens people by tracing the narrator's decline.'", ["'The novel is long.'", "'I read a novel.'", "'Authors write about things.'"], "A thesis states a clear claim.")
H('7.D.i', 3, "What should the conclusion of an expository essay do?", "restate the thesis and leave a final thought", ["introduce a new argument", "list unrelated facts", "repeat the introduction word for word"], "Conclusions close the argument.")
H('7.D.ii', 3, "How does an essay's organizational design relate to its thesis?", "the structure should support and develop the thesis", ["the structure is unrelated", "the thesis follows the structure's length", "design replaces the thesis"], "Structure serves the main claim.")
H('7.D.ii', 4, "A thesis argues that two empires differed in how they governed. Which design fits best?", "compare and contrast", ["alphabetical order", "a timeline of unrelated events", "a list of rhymes"], "Comparison suits a thesis of difference.")

# 7.E
H('7.E.i', 3, "Which is a clear arguable claim?", "'Schools should start later to improve student performance.'", ["'Schools exist.'", "'Students attend school.'", "'Mornings are early.'"], "An arguable claim can be debated.")
H('7.E.i', 3, "An appeal to emotion is called what?", "pathos", ["logos", "ethos", "syntax"], "Pathos moves feelings.")
H('7.E.i', 3, "An appeal that builds the writer's credibility is called what?", "ethos", ["pathos", "logos", "irony"], "Ethos establishes trustworthiness.")
H('7.E.ii', 4, "A writer says, 'Critics argue the plan is costly; however, savings over ten years outweigh the cost.' What is the second half?", "a rebuttal", ["a thesis", "a title", "a concession"], "It answers the objection.")
H('7.E.ii', 3, "Which is a type of strong evidence in an argument?", "statistics from a reliable study", ["a rumor", "an unnamed friend's guess", "a slogan"], "Credible data supports claims.")
H('7.E.iii', 3, "Which choice best shows awareness of an audience of skeptical readers?", "addressing their likely objections", ["using only slang", "ignoring them", "insulting their views"], "Audience awareness shapes the argument.")
H('7.E.iii', 3, "A letter to a mayor asking for a new crosswalk should use what tone?", "polite and persuasive", ["rude", "joking", "careless"], "Tone matches the audience.")

# 7.F
H('7.F', 3, "What is the purpose of captions in a digital article?", "to explain or add context to images", ["to replace the article", "to hide the images", "to list sources only"], "Captions clarify visuals.")
H('7.F', 3, "A podcast with a transcript and episode notes is an example of what?", "a multimodal text", ["a poem", "a footnote", "a single-mode text"], "It combines audio and text.")

# 8.A
H('8.A', 3, "A pamphlet shows a cheerful family and urges readers to get vaccinated. What is the author's purpose?", "to persuade", ["to entertain", "to mock", "to confuse"], "It urges action.")
H('8.A', 4, "An op-ed uses technical economic terms and charts. Who is the likely audience?", "readers familiar with economics", ["young children", "readers who dislike data", "no one"], "Language signals audience.")
H('8.A', 3, "The central message of a fable is usually called what?", "its moral", ["its index", "its footnote", "its glossary"], "Fables convey morals.")

# 8.B
H('8.B', 3, "An essay describes how the printing press changed society step by step over time. What text structure is used?", "chronological sequence", ["compare and contrast", "problem and solution", "spatial order"], "It follows time order.")
H('8.B', 3, "A text presents a shortage of clean water and then lists proposed fixes. What structure is it?", "problem and solution", ["sequence", "description", "classification"], "It poses a problem then answers it.")
H('8.B', 4, "Why might an author choose cause-and-effect structure?", "to show how one event leads to another", ["to list opinions", "to avoid facts", "to describe a place only"], "Structure supports purpose.")

# 8.C
H('8.C', 3, "A sidebar in a textbook mostly serves to do what?", "provide extra related information", ["end the chapter", "replace the index", "hide the main text"], "Sidebars supplement.")
H('8.C', 3, "A timeline graphic in a history article helps readers see what?", "the order and spacing of events", ["rhyming words", "the author's age", "the cost of the book"], "Timelines show sequence.")
H('8.C', 4, "A pie chart is best used to show what?", "parts of a whole", ["change over time", "a map route", "a poem's meter"], "Pie charts show proportions.")

# 8.D
H('8.D', 3, "An author describes a prison as 'a stone mouth that never closed.' How does this language shape perception?", "it makes the prison seem threatening and consuming", ["it makes it seem cozy", "it makes it seem new", "it has no effect"], "Figurative language influences views.")
H('8.D', 4, "A writer repeatedly uses the word 'swarm' for a crowd of protesters. What perception is likely?", "that the crowd is chaotic and menacing", ["that the crowd is orderly", "that the crowd is small", "that the crowd is silent"], "Word choice slants perception.")

# 8.E
H('8.E', 3, "A character who says 'Great job' after a terrible performance is using what?", "sarcasm", ["a refrain", "foreshadowing", "an allegory"], "Sarcasm means the opposite, with a sting.")
H('8.E', 3, "A recurring image of a locked door across a novel is an example of what?", "a motif", ["a plot twist only", "an index", "a stanza"], "Motifs repeat meaningful elements.")
H('8.E', 3, "A bank robber is arrested after calling the police to report a missing wallet. What kind of irony is this?", "situational irony", ["verbal irony", "dramatic irony", "sarcasm"], "The outcome defies expectation.")

# 8.F
H('8.F', 3, "An author uses ornate vocabulary and long sentences in a ceremonial speech. What tone results?", "formal and grand", ["casual", "hurried", "playful"], "Diction and syntax shape tone.")
H('8.F', 4, "A narrator's voice uses slang, fragments and humor. What does this diction create?", "an informal, personal voice", ["a formal lecture", "a legal contract", "a scientific report"], "Voice reflects diction.")
H('8.F', 3, "Which choice of syntax most clearly creates a rushed, anxious mood?", "short, clipped sentences", ["long flowing clauses", "a calm list", "formal address"], "Short sentences quicken pace.")

# 8.G
H('8.G', 3, "'It was the best of ideas, it was the worst of ideas' uses which device?", "antithesis", ["parallelism only", "alliteration", "onomatopoeia"], "Opposites are set against each other.")
H('8.G', 3, "Repeating the same sentence structure to link ideas is called what?", "parallelism", ["antithesis", "irony", "hyperbole"], "Parallel structure creates rhythm.")
H('8.G', 4, "A speaker moves from sorrow to hope midway through a speech. What is this rhetorical shift used to do?", "to mark a change in tone and lift the audience", ["to confuse the audience", "to end the speech", "to repeat the introduction"], "Shifts guide emotion.")

# 9.B
H('9.B.i', 3, "An essay on three causes of an event should be organized in what way?", "one paragraph for each cause with clear transitions", ["one giant paragraph", "random order", "only a list of effects"], "Organization matches purpose.")
H('9.B.ii', 3, "Which detail best supports the idea that a character is brave?", "she ran back into the burning shop to pull out a trapped neighbor", ["she is a person", "she lives nearby", "she owns a coat"], "Specific details show depth.")
H('9.B.ii', 3, "What does a writer's commentary add to an example?", "explanation of why the example matters", ["extra length only", "a new topic", "a citation style"], "Commentary shows thinking.")

# 9.C
H('9.C', 3, "A writer replaces the vague word 'thing' with 'treaty.' What is improved?", "diction", ["capitalization", "page numbers", "margins"], "Precise words improve clarity.")
H('9.C', 3, "Cutting a paragraph that wanders off topic improves what?", "development and focus", ["spelling", "page color", "title font"], "Revision strengthens focus.")
H('9.C', 4, "Combining short sentences with conjunctions and varying their openings improves what?", "sentence effectiveness and style", ["thesis statement", "citation format", "the title"], "Sentence variety improves flow.")

# 9.D
H('9.D.i', 3, "Which is a run-on sentence?", "The storm hit the coast it flooded every street.", ["The storm hit the coast, and it flooded every street.", "The storm hit the coast; it flooded every street.", "The storm hit the coast."], "Two independent clauses are fused without punctuation.")
H('9.D.i', 3, "Which is a sentence fragment?", "Because the bridge had collapsed.", ["The bridge had collapsed.", "Because the bridge had collapsed, we turned back.", "We turned back."], "The dependent clause stands alone.")
H('9.D.ii', 3, "Which sentence uses the active voice?", "The committee approved the plan.", ["The plan was approved by the committee.", "The plan has been approved.", "The plan is being approved."], "The subject performs the action.")
H('9.D.ii', 4, "When is the passive voice most appropriate?", "when the actor is unknown or unimportant", ["always", "never", "in every sentence"], "Passive voice focuses on the receiver.")
H('9.D.iii', 3, "Which sentence has correct pronoun-antecedent agreement?", "Each student must bring his or her own notebook.", ["Each student must bring their own notebooks.", "Each student must bring our notebook.", "Each student must bring its notebooks."], "Singular antecedents take singular pronouns in formal usage.")
H('9.D.iv', 3, "In 'we toured lake victoria and then flew to nairobi in august,' which words need capital letters?", "we, lake, victoria, nairobi and august", ["victoria and nairobi only", "we and august only", "toured, flew and august"], "Capitalize the first word, proper names of places and the names of months.")
H('9.D.v', 3, "Which sentence uses a semicolon correctly?", "The rain stopped; the festival began.", ["The rain; stopped the festival began.", "The rain stopped the; festival began.", "The; rain stopped the festival began."], "Semicolons join related independent clauses.")
H('9.D.v', 3, "Which sentence uses a colon correctly?", "She packed three items: a map, a compass and a flashlight.", ["She packed: three items a map, a compass and a flashlight.", "She packed three: items a map, a compass and a flashlight.", "She: packed three items a map, a compass and a flashlight."], "A colon introduces a list after an independent clause.")
H('9.D.vi', 3, "Which sentence uses the correct word?", "The weather affected the harvest, and the effect was severe.", ["The weather effected the harvest, and the affect was severe.", "The weather effected the harvest, and the effect was severe.", "The weather affected the harvest, and the affect was severe."], "Affect is usually a verb; effect a noun.")

# 10.D
H('10.D', 3, "Which line is the best opening for a professional email asking a teacher for a recommendation letter?", "'Dear Ms. Alvarez, I am writing to ask whether you would be willing to write a recommendation for me.'", ["'Hey, got a minute?'", "'Yo teacher, write me a letter.'", "'Sup.'"], "Professional correspondence is polite and clear.")
H('10.D', 3, "A friendly letter to a pen pal can differ from a business letter by being what?", "more casual in tone", ["written without words", "required to have a thesis", "signed by a lawyer"], "Friendly letters allow casual tone.")

# 11
H('11.E', 3, "Which of these is the best first step for finding reliable sources on a research topic?", "searching a library database or reputable site", ["asking a friend only", "reading comments on a video", "guessing"], "Reliable databases give vetted sources.")
H('11.F', 3, "A researcher combines facts from four sources into one summary and credits each. What is this called?", "synthesis", ["plagiarism", "copying", "outlining only"], "Synthesis blends and credits.")
H('11.H', 3, "Which practice shows ethical use of source material?", "quoting with quotation marks and citing the source", ["pasting without credit", "changing a few words and omitting the source", "claiming the idea as one's own"], "Ethical writers cite sources.")
H('11.G.i', 3, "A website sells a product and publishes only glowing 'studies' that list no authors. What should a researcher conclude?", "the source may be biased and not credible", ["the source is perfectly neutral", "the source is peer reviewed", "the source is a government report"], "Missing authors and selective evidence signal bias.")
H('11.G.i', 4, "What does 'bias by omission' mean?", "leaving out important facts that don't fit the author's view", ["listing too many facts", "citing too many sources", "using long sentences"], "Omission skews the picture.")
H('11.G.ii', 3, "'Either we ban all cars or the planet will be destroyed.' What fallacy is this?", "either-or (false dilemma)", ["hasty generalization", "bandwagon", "ad hominem"], "It ignores middle options.")
H('11.G.ii', 3, "A writer meets two rude waiters and concludes, 'Everyone in the city is rude.' What fallacy is this?", "hasty generalization", ["circular reasoning", "slippery slope", "straw man"], "Two cases cannot represent a city.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_eng2.jsonl'))

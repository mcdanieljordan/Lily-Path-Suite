#!/usr/bin/env python3
"""High school English IV (TEKS 110.39.c). Original questions; British-literature focus."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('110.39.c.', 994, own='hs_eng4.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A
H('2.A', 3, "A senior reading Beowulf in translation wants to know how an Old English word was used centuries ago. Which resource helps most?", "a historical or etymological dictionary", ["a modern pocket speller", "a rhyming guide", "a world atlas"], "Historical dictionaries trace older usage.")
H('2.A', 3, "A student meets the term 'iambic pentameter' in a critical essay. Where is the most reliable place to check its precise meaning?", "a glossary of literary terms", ["a recipe book", "a sports almanac", "a bus schedule"], "Literary glossaries define critical terms.")

# 2.B
H('2.B', 3, "A critic calls a ruler's speech 'regal' while another calls it 'pompous.' What distinguishes the two words?", "their connotations", ["their rhymes", "their lengths only", "their spelling histories only"], "Same subject, different emotional coloring.")
H('2.B', 4, "In a poem, 'the sea swallowed the ship' uses 'swallowed' in what way?", "figuratively", ["literally", "denotatively only", "technically"], "The sea does not literally swallow.")
H('2.B', 3, "Which word has the most positive connotation for a person who refuses to change a view?", "steadfast", ["stubborn", "pigheaded", "obstinate"], "The others imply rigidity.")

# 2.C
H('2.C', 3, "A reviewer calls a performance 'tour de force.' What does the phrase mean?", "a display of great skill", ["a short trip", "a failed effort", "a quiet rehearsal"], "French for 'feat of strength.'")
H('2.C', 3, "What does 'carpe diem' encourage?", "making the most of the present moment", ["avoiding all risk", "waiting patiently", "remembering the past"], "Latin for 'seize the day.'")
H('2.C', 4, "A scholar describes a poet's 'ennui.' What does the French word suggest?", "weary boredom or listlessness", ["fierce anger", "great joy", "sharp curiosity"], "Ennui is deep dissatisfaction.")

# 4.F
H('4.F', 4, "Passage: 'The castle gates stood open, though no smoke rose from a single chimney.' What can a reader infer?", "the castle may be abandoned or in trouble", ["a feast is under way", "the king is arriving", "winter has just ended happily"], "Open gates and no smoke imply emptiness.")
H('4.F', 3, "A narrator says her sister 'rehearsed her smile in the hall mirror before entering the room.' What does this suggest?", "the sister is hiding her real feelings", ["the sister dislikes mirrors", "the room is dark", "the sister is practicing a song"], "Rehearsed expressions imply concealment.")

# 4.G
H('4.G', 3, "When a reader evaluates details to find a key idea, what question helps most?", "which details repeat or build toward the same point", ["which sentence is shortest", "which word is rarest", "which page is first"], "Repetition signals importance.")
H('4.G', 4, "An essay gives a single vivid anecdote followed by four paragraphs of data on the same theme. What is the key idea likely to be?", "the theme the data and anecdote jointly support", ["the anecdote alone", "the title font", "the number of paragraphs"], "Details converge on the main idea.")

# 4.H
H('4.H', 4, "A student reads a parliamentary speech and a newspaper editorial about the same law. What does synthesizing them produce?", "a view of how the law was defended and received", ["a copy of the speech", "a list of spelling errors", "no new understanding"], "Combining sources yields a fuller picture.")
H('4.H', 3, "Which sentence best shows synthesis across texts?", "'Together, the diary and the treaty reveal why the village feared the border.'", ["'The diary is old.'", "'The treaty has articles.'", "'I read both.'"], "Synthesis connects ideas.")

# 4.I
H('4.I', 3, "A reader finds that Shakespearean language blurs her understanding of a scene. Which strategy helps most?", "paraphrasing each speech into modern language", ["reading faster", "skipping the speeches", "reading only stage directions"], "Paraphrasing improves comprehension.")
H('4.I', 3, "Which question helps a reader monitor comprehension while reading a dense critical essay?", "'Can I restate the author's argument in my own words?'", ["'How many words are on a page?'", "'What color is the cover?'", "'Who printed this?'"], "Self-checking guides adjustment.")

# 5.B
H('5.B', 4, "A student compares how two Romantic poets treat nature, one reverent and one fearful. What does the comparison require?", "evidence from both poems about each attitude", ["a quotation from only one poem", "a biography of each poet only", "a rhyme count"], "Cross-text comparison needs evidence.")
H('5.B', 3, "A strong written comparison of two plays should include what?", "specific similarities and differences supported with evidence", ["plot summary only", "a list of actors", "a single adjective"], "Comparisons need evidence.")

# 5.C
H('5.C', 3, "An interpretive paragraph quotes a soliloquy and then argues what it reveals about the speaker's doubt. The argument that follows the quotation is what?", "original commentary", ["a bibliography entry", "a footnote", "a stage direction"], "Commentary interprets the evidence.")
H('5.C', 4, "Which choice is strongest interpretive writing about a quoted line?", "'The repeated word \"darkness\" suggests the speaker's despair is growing.'", ["'The line has a word.'", "'This is a quote.'", "'Page 4.'"], "Interpretation explains meaning.")

# 5.D
H('5.D', 3, "A faithful paraphrase of 'The queen's silence was louder than any decree' would be:", "The queen's refusal to speak carried more force than an official order.", ["The queen shouted a decree.", "The queen was not present.", "The decree was silent."], "A paraphrase preserves meaning.")
H('5.D', 3, "A summary of a complicated argument should do what?", "state the central claim and key supports briefly", ["copy every sentence", "add the summarizer's opinion", "skip the claim"], "Summaries are concise and faithful.")

# 5.F
H('5.F', 3, "Which word is the most precise academic term for 'a main idea running through a literary work'?", "theme", ["noise", "scene", "mood only"], "Themes are central ideas.")
H('5.F', 3, "In an essay on Parliament, which word names a formal vote to approve a law?", "ratification", ["dessert", "rumor", "costume"], "Content-area vocabulary aids precision.")

# 5.G
H('5.G', 4, "'The manor's portraits stared down on a table set for guests who never came.' What implicit meaning is suggested?", "loneliness and the passing of better days", ["a party is about to start", "the portraits are valuable", "the cook is late"], "Details imply a mood of loss.")
H('5.G', 3, "An explicit meaning is found where?", "in what the text directly says", ["only between the lines", "only in the reader's mind", "only in the title page"], "Explicit meaning is stated.")

# 5.J
H('5.J', 4, "A critic says a poem is 'meaningless' but cites no lines. What is the best challenge?", "the claim lacks supporting evidence from the text", ["poems are always meaningless", "critics are always wrong", "the poem is too short"], "A claim needs textual support.")
H('5.J', 3, "A reader wants to defend an author's view that technology isolates people. What should the reader do?", "cite passages that show characters becoming isolated", ["state a personal opinion only", "summarize the cover", "list the author's other books"], "Defend with text evidence.")

# 6.A
H('6.A', 4, "Two British novels portray characters trapped by class expectations. How can their themes be compared?", "by examining how each plot and character shows the limits of class", ["by comparing the number of chapters", "by comparing the covers", "by ignoring the endings"], "Compare how themes develop.")
H('6.A', 3, "A king who cannot rule himself brings his kingdom to ruin. Which theme does this plot develop?", "self-control is needed for leadership", ["kingdoms are safe", "rulers need no discipline", "ruin is accidental"], "Characterization and plot show theme.")

# 6.B
H('6.B', 3, "A tragic hero is often defined by what?", "a flaw that contributes to his downfall", ["perfect virtue", "a lack of conflict", "an unchanging fortune"], "The tragic flaw drives downfall.")
H('6.B', 4, "A character who appears villainous but reveals a painful past becomes believable through what?", "complexity and context", ["flat traits", "silence", "repetition of one trait"], "Complex motives add believability.")

# 6.C
H('6.C', 3, "A short scene in which servants whisper about a coming betrayal contributes what to the plot?", "foreshadowing of conflict", ["a rhyme scheme", "the denouement", "the epigraph"], "Isolated scenes can set up later events.")
H('6.C', 4, "A play's final scene reunites estranged family members. How does it contribute to the whole?", "it resolves central conflicts and reinforces theme", ["it introduces a new conflict", "it is unrelated", "it changes the genre"], "Closing scenes complete the structure.")

# 6.D
H('6.D', 3, "A novel set in Victorian England shows a child laborer in a factory. How does this historical setting influence the story?", "it shapes the character's hardships and the social critique", ["it removes conflict", "it hides the character", "it makes the plot comic"], "Historical context shapes events and theme.")
H('6.D', 4, "A medieval tale in which a knight must prove his honor reflects what about its culture?", "the era's values of chivalry and reputation", ["modern attitudes only", "no cultural values", "a rhyme scheme"], "Cultural setting shapes characters.")

# 7.A
H('7.A', 3, "Who wrote 'The Canterbury Tales'?", "Geoffrey Chaucer", ["John Milton", "Jane Austen", "Charles Dickens"], "A medieval frame story in verse.")
H('7.A', 3, "Which Shakespeare tragedy centers on a Danish prince who seeks to avenge his father?", "Hamlet", ["Macbeth", "Othello", "King Lear"], "Hamlet is the prince of Denmark.")
H('7.A', 3, "Which author wrote the Victorian novel 'Great Expectations'?", "Charles Dickens", ["Thomas Hardy", "George Eliot", "Oscar Wilde"], "A coming-of-age novel.")
H('7.A', 4, "Which poet wrote the epic 'Paradise Lost'?", "John Milton", ["William Blake", "Lord Byron", "Samuel Coleridge"], "A seventeenth-century epic in blank verse.")
H('7.A', 3, "Which novel by Mary Shelley explores the consequences of creating life?", "Frankenstein", ["Dracula", "Wuthering Heights", "Jane Eyre"], "A founding Gothic and science-fiction novel.")

# 7.B
H('7.B', 3, "A Shakespearean sonnet ends with what structure?", "a rhyming couplet", ["a haiku", "a free-verse stanza", "an unrhymed line"], "The final two lines rhyme.")
H('7.B', 4, "Blank verse is written in what form?", "unrhymed iambic pentameter", ["rhymed couplets", "free verse", "haiku"], "Used in many Shakespeare plays.")
H('7.B', 3, "A line of iambic pentameter contains how many metrical feet?", "five", ["three", "seven", "ten"], "Penta means five.")

# 7.C
H('7.C', 3, "A comic character in a tragedy provides momentary relief from tension. This convention is called what?", "comic relief", ["an epigraph", "a soliloquy", "an index"], "Comic relief lightens tone.")
H('7.C', 4, "In a play, a character reveals a secret plan while alone onstage. This is a feature of what?", "a soliloquy", ["a prologue", "an epilogue", "a stage curtain"], "Soliloquies reveal private thoughts.")

# 7.D
H('7.D.i', 3, "Which sentence is the best thesis for an essay on a novel's use of setting?", "'The novel's foggy moors mirror the heroine's confusion and isolation.'", ["'The novel has moors.'", "'Settings are places.'", "'I will discuss setting.'"], "A thesis states a specific, arguable claim.")
H('7.D.i', 4, "A strong concluding paragraph in an analytical essay typically does what?", "synthesizes the argument and explains its significance", ["introduces an unrelated claim", "repeats the introduction exactly", "lists new questions only"], "Conclusions emphasize significance.")
H('7.D.ii', 3, "An essay argues that a play's tone grows darker in each act. Which organization best matches this thesis?", "an act-by-act progression", ["alphabetical order", "random order", "a list of characters"], "Structure mirrors the thesis.")

# 7.E
H('7.E.i', 3, "Which claim is most arguable?", "'Public libraries should be funded before stadiums.'", ["'Libraries have books.'", "'Stadiums are large.'", "'Funding is money.'"], "Arguable claims can be debated.")
H('7.E.i', 3, "An appeal to shared values and beliefs is mostly an appeal to what?", "ethos", ["syntax", "logos only", "meter"], "Ethos builds trust and shared identity.")
H('7.E.ii', 4, "A writer says, 'While some argue the tax burdens small shops, it also funds the roads those shops depend on.' This is an example of what?", "addressing a counterargument", ["an anecdote", "a summary", "a title"], "The writer answers an opposing view.")
H('7.E.ii', 3, "Which type of evidence is a historical example?", "an event from the past used to support a point", ["a rumor", "an opinion with no source", "a slogan"], "Examples illustrate claims.")
H('7.E.iii', 3, "A writer adjusts vocabulary and examples to suit readers with limited background knowledge. This shows awareness of what?", "audience", ["rhyme", "meter", "plot"], "Audience shapes choices.")

# 7.F
H('7.F', 3, "A news website pairs an article with an interactive timeline. What does the interactive element allow?", "readers to explore events at their own pace", ["the article to disappear", "the author to change the facts", "silent reading only"], "Interactive features engage users.")
H('7.F', 3, "A podcast adapts a classic novel. Which feature distinguishes it as a multimodal text?", "sound effects and voice acting", ["margins", "chapter titles only", "page numbers"], "Audio adds a mode.")

# 8.A
H('8.A', 3, "An article reports facts about a historic battle without taking sides. What is the author's purpose?", "to inform", ["to persuade", "to amuse", "to command"], "Neutral reporting informs.")
H('8.A', 4, "A satirical essay proposes an outrageous remedy to expose a social failing. What is the underlying purpose?", "to criticize through irony", ["to give instructions", "to entertain with no point", "to advertise"], "Satire criticizes.")
H('8.A', 3, "A speech delivered to graduating seniors offers advice and encouragement. Who is the intended audience?", "the graduates", ["toddlers", "scientists only", "no one"], "Audience is signaled by occasion.")

# 8.B
H('8.B', 3, "A historical essay describes how rising bread prices led to riots and then to reform. What structure is this?", "cause and effect", ["alphabetical", "spatial", "classification"], "Events link in chains.")
H('8.B', 3, "A text lists categories of poetry and describes each in turn. What structure is this?", "classification", ["chronological", "problem and solution", "compare and contrast"], "Items are grouped by type.")

# 8.C
H('8.C', 3, "Why might a reference book include a footnote?", "to give a source or additional note without interrupting the main text", ["to replace the chapter", "to decorate the page", "to hide the author"], "Footnotes supplement.")
H('8.C', 4, "A line graph in an economics article best shows what?", "trends over time", ["parts of a whole", "a map route", "a poem's meter"], "Line graphs track change.")

# 8.D
H('8.D', 4, "An author calls the king's court 'a glittering cage.' How does this language shape perception?", "it suggests luxury that confines people", ["it suggests the court is shabby", "it suggests freedom", "it has no meaning"], "Metaphor shapes views.")
H('8.D', 3, "An author repeatedly uses 'toil' instead of 'work' to describe labor. What does the choice suggest?", "that the labor is hard and burdensome", ["that the labor is easy", "that the labor is fun", "that the labor is brief"], "Diction affects perception.")

# 8.E
H('8.E', 3, "A character says 'How thoughtful' after being insulted. This is an example of what?", "sarcasm", ["a motif", "foreshadowing", "a flashback"], "The words mean the opposite.")
H('8.E', 4, "A repeated image of blood throughout a tragedy is an example of what?", "a motif", ["a pun", "an epigraph", "a stage direction"], "Motifs recur with meaning.")
H('8.E', 3, "A thief steals a policeman's wallet in front of the police station. What kind of irony is this?", "situational irony", ["verbal irony", "dramatic irony", "sarcasm"], "The outcome is unexpected.")

# 8.F
H('8.F', 3, "Elevated, formal diction in a narrator's account of a coronation creates what effect?", "a solemn, ceremonial tone", ["a playful tone", "a casual tone", "a bitter tone"], "Diction shapes tone.")
H('8.F', 4, "Short, fragmented sentences in a character's panicked monologue create what effect?", "a sense of urgency and distress", ["a calm, measured pace", "a stately pace", "a dreamy mood"], "Syntax shapes mood.")
H('8.F', 3, "A narrator's voice is dry, witty and understated. Which element most contributes to this voice?", "diction and sentence rhythm", ["page numbers", "the font", "the cover"], "Voice emerges from language choices.")

# 8.G
H('8.G', 3, "'To be, or not to be' sets up a contrast that is an example of what?", "antithesis", ["alliteration", "onomatopoeia", "hyperbole"], "Opposites are juxtaposed.")
H('8.G', 3, "A speaker repeats a similar sentence structure across several sentences to build momentum. This is called what?", "parallelism", ["irony", "antithesis", "understatement"], "Parallel structure builds rhythm.")
H('8.G', 4, "A speech moves from criticism of a policy to a proposal for reform. What does this rhetorical shift accomplish?", "it moves the audience from problem to solution", ["it repeats the opening", "it ends the speech abruptly", "it avoids the topic"], "Shifts structure persuasion.")

# 9.B
H('9.B.i', 3, "Which organizational pattern best suits an essay arguing that a policy should change?", "claim, evidence, counterargument, conclusion", ["a list of rhymes", "random order", "alphabetical order"], "Arguments follow a logical structure.")
H('9.B.ii', 3, "Which supports the claim that a character is ambitious?", "he rehearses speeches nightly and courts powerful allies", ["he owns a coat", "he lives in a town", "he eats breakfast"], "Specific details develop ideas.")
H('9.B.ii', 4, "Depth of thought in a body paragraph is shown by what?", "explaining the significance of the evidence", ["adding more quotations without comment", "repeating the topic sentence", "using longer sentences"], "Commentary shows insight.")

# 9.C
H('9.C', 3, "A writer deletes a repeated sentence and tightens wordy phrases. What is being improved?", "clarity and concision", ["spelling only", "typeface", "margins"], "Revision tightens style.")
H('9.C', 3, "Replacing 'big' with 'monumental' improves what?", "diction", ["capitalization", "punctuation", "paragraph breaks"], "More precise words improve style.")

# 9.D
H('9.D', 3, "Which sentence contains a comma splice?", "The play ended, the audience applauded.", ["The play ended, and the audience applauded.", "The play ended; the audience applauded.", "When the play ended, the audience applauded."], "A comma alone cannot join two independent clauses.")
H('9.D', 3, "Which sentence uses a semicolon correctly?", "The fog lifted; the harbor came into view.", ["The fog; lifted the harbor came into view.", "The fog lifted the; harbor came into view.", "The; fog lifted the harbor came into view."], "Semicolons join related independent clauses.")
H('9.D', 3, "Which sentence uses the correct pronoun?", "Each of the actors forgot his or her lines.", ["Each of the actors forgot their lines happily.", "Each of the actors forgot its lines.", "Each of the actors forgot our lines."], "A singular antecedent takes a singular pronoun in formal usage.")
H('9.D', 3, "In 'the thames flows through london,' which words need capital letters?", "the, thames and london", ["flows and through", "thames only", "london only"], "Capitalize the first word and the names of places.")
H('9.D', 3, "Which sentence has a spelling error?", "The queen's reign was marked by prosperity and sucess.", ["The queen's reign was marked by prosperity and success.", "The senate approved the budget.", "The audience applauded loudly."], "'Success' has a double c and double s.")
H('9.D', 3, "Which sentence uses the active voice?", "The sculptor carved the statue.", ["The statue was carved by the sculptor.", "The statue has been carved.", "The statue is being carved."], "The subject performs the action.")

# 10.D
H('10.D', 3, "Which element is needed in a professional cover letter?", "a clear statement of the position sought", ["slang expressions", "emoji", "a joke opening"], "Professional correspondence states its purpose.")
H('10.D', 3, "Which greeting is appropriate when the recipient's name is unknown?", "To Whom It May Concern:", ["Hey there,", "Yo,", "Hi friend,"], "A neutral formal greeting.")

# 11
H('11.E', 3, "A student researching the Industrial Revolution wants a primary source. Which is best?", "a worker's letter written in 1840", ["a modern blog summary", "a textbook paragraph", "a documentary review"], "Primary sources come from the era.")
H('11.F', 3, "When a researcher synthesizes information, the final product should do what?", "blend ideas from sources into a new, organized understanding", ["copy one source", "list sources only", "avoid citing"], "Synthesis builds a coherent whole.")
H('11.H', 3, "Which of the following is plagiarism?", "using another writer's exact paragraph without credit", ["quoting a sentence with a citation", "paraphrasing and citing", "summarizing and citing"], "Uncredited copying is plagiarism.")
H('11.G.i', 3, "An article about a medicine is written by the company that sells it. What should a careful reader consider?", "the possibility of bias", ["that the article is perfectly objective", "that sellers never exaggerate", "that all claims are proven"], "Conflicts of interest can skew content.")
H('11.G.i', 4, "A source describes only one side of a debate and omits all counterevidence. This indicates what?", "possible bias by omission", ["balanced coverage", "peer review", "strong credibility"], "Omission skews perspective.")
H('11.G.ii', 3, "'No one has proven ghosts do not exist, so they must be real' is an example of what?", "faulty reasoning from lack of proof", ["sound deduction", "expert testimony", "statistical evidence"], "Absence of disproof is not proof.")
H('11.G.ii', 3, "'Either you support this bill, or you hate your country' is an example of what?", "an either-or fallacy", ["a balanced argument", "a statistic", "an anecdote"], "It limits options falsely.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_eng4.jsonl'))

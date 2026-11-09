#!/usr/bin/env python3
"""High school English III (TEKS 110.38.c). Original questions; American-literature focus."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('110.38.c.', 993, own='hs_eng3.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A
H('2.A', 3, "A junior needs the legal meaning of 'tort' for a civics paper. Which resource fits best?", "a specialized legal dictionary", ["a rhyming dictionary", "a road atlas", "a cookbook index"], "Specialized dictionaries define field-specific terms.")
H('2.A', 3, "Which resource would a student use to find the history of a word's meaning over centuries?", "an etymological dictionary", ["a phone directory", "a style sheet", "a map legend"], "Etymological dictionaries trace word history.")

# 2.B
H('2.B', 3, "A speaker calls a policy 'a bold experiment' while a critic calls it 'a reckless gamble.' What is the difference?", "their connotations", ["their denotations, which differ completely", "their rhyme", "their length"], "The words describe the same thing with different emotional weight.")
H('2.B', 4, "In 'The mill's smoke was a gray quilt over the town,' what kind of meaning does 'quilt' have?", "figurative", ["literal", "denotative only", "technical"], "Smoke is compared to a quilt.")
H('2.B', 3, "Which word has the most neutral connotation for describing a person who stays home often?", "homebody", ["recluse", "hermit", "shut-in"], "The others suggest isolation.")

# 2.C
H('2.C', 3, "A historian refers to the 'laissez-faire' approach of a government. What does the phrase suggest?", "a hands-off policy toward the economy", ["strict control", "constant war", "heavy taxation"], "French for 'let do.'")
H('2.C', 3, "What does the Latin phrase 'habeas corpus' protect against?", "unlawful imprisonment without a hearing", ["theft of property", "libel", "double taxation"], "It requires a person be brought before a court.")
H('2.C', 4, "A critic describes a novel as a 'magnum opus.' What is being said?", "it is the author's greatest work", ["it is the shortest work", "it was never finished", "it is an early draft"], "Latin for 'great work.'")

# 4.F
H('4.F', 3, "Passage: 'Though the fields were green, Amos stood at the fence and counted the empty seed sacks twice.' What can be inferred?", "he is worried about the coming season", ["he has a large surplus", "he is planning a party", "he is leaving the farm happily"], "Counting empty sacks twice signals worry.")
H('4.F', 4, "A narrator in a 1930s story notes that 'the line outside the bakery wound around the block, and nobody spoke.' What does this imply about the setting?", "times are hard and people are desperate", ["the bakery is giving a party", "the town is on vacation", "the baker is famous for pastries"], "Silent crowds waiting suggest hardship.")

# 4.G
H('4.G', 3, "To evaluate which details support a key idea in a speech, a reader should ask what?", "which details directly connect to the speaker's main point", ["which detail is the longest", "which detail is first", "which detail has the most adjectives"], "Evaluate relevance to the central idea.")
H('4.G', 4, "A writer includes a statistic about city air quality inside an essay on lung disease. How should a reader treat the statistic?", "as a supporting detail for the essay's claim", ["as irrelevant", "as the essay's title", "as a rhyme"], "Statistics back up key ideas.")

# 4.H
H('4.H', 4, "A reader compares a diary entry from a pioneer and a government land record from the same year. What does combining them allow?", "a fuller understanding than either source alone", ["a replacement of both sources", "no new understanding", "proof the diary is false"], "Synthesis builds a richer picture.")
H('4.H', 3, "When two sources disagree on a date, what should a researcher do?", "check additional reliable sources to resolve it", ["pick the one with fewer words", "ignore both", "average the dates"], "Cross-checking resolves conflict.")

# 4.I
H('4.I', 3, "A reader keeps losing track of characters in a dense novel. Which adjustment helps most?", "making a character list while reading", ["skipping every chapter", "reading with the sound off", "ignoring names"], "Notes support comprehension.")
H('4.I', 3, "A reader reaches a sentence with several unfamiliar terms. What is a sound first step?", "use context clues and then consult a reference", ["guess randomly", "stop reading permanently", "skip all sentences like it"], "Monitor and adjust.")

# 5.B
H('5.B', 4, "A student compares how two American poems depict the frontier, one hopeful and one grim. What is being compared?", "the poets' attitudes and techniques", ["the font in each book", "the number of pages", "the publishers"], "Cross-text comparison focuses on ideas and craft.")
H('5.B', 3, "A strong response that compares two texts usually does what?", "identifies similarities and differences with evidence", ["lists only similarities with no evidence", "retells one text only", "avoids quotations"], "Comparison needs evidence.")

# 5.C
H('5.C', 3, "A student writes, 'The narrator's tone shifts from hope to bitterness,' then adds a quotation. What should follow the quotation?", "an explanation of how it shows the shift", ["a new unrelated topic", "another quotation without comment", "the title again"], "Original commentary connects evidence to claim.")
H('5.C', 4, "Which sentence contains original commentary about a quotation?", "'This image of a cold hearth suggests the family's loss of warmth and security.'", ["'The text says \"cold hearth.\"'", "'Page 12.'", "'The author wrote the line.'"], "Commentary interprets the evidence.")

# 5.D
H('5.D', 3, "Which is a faithful paraphrase of 'The orator's words ignited the crowd'?", "The speaker's words stirred the audience to excitement.", ["The crowd burned down the hall.", "The speaker was silent.", "The audience left."], "A paraphrase keeps meaning in new words.")
H('5.D', 3, "A summary of a speech should keep what?", "its main points in the original order", ["the speaker's gestures", "every anecdote", "the reader's opinion only"], "Summaries maintain logical order.")

# 5.F
H('5.F', 3, "In a response about the Constitution, which word is the most precise for 'an official change to the document'?", "amendment", ["suggestion", "doodle", "poster"], "Content vocabulary improves accuracy.")
H('5.F', 3, "Which word is academic vocabulary for 'to explain in detail'?", "elaborate", ["skip", "shrug", "mumble"], "Academic terms suit formal responses.")

# 5.G
H('5.G', 3, "'He never mentioned the war again, though he flinched at every loud noise.' What is implied?", "the war left him with lasting distress", ["he loves loud sounds", "the war was a game", "he wrote a book on it"], "Behavior implies meaning.")
H('5.G', 3, "Which statement describes an explicit meaning?", "a narrator directly states that the farm failed", ["a mood suggested by weather", "an unspoken attitude", "a hint in a character's pause"], "Explicit meaning is stated outright.")

# 5.J
H('5.J', 4, "An editorial claims 'everyone supports the new law' but cites a poll of 20 people from one club. What is a reasonable challenge?", "the sample is too small and unrepresentative", ["the editorial is too short", "the law is new", "polls are never valid"], "A poor sample weakens the claim.")
H('5.J', 3, "A defense of an author's claim is strongest when it includes what?", "relevant evidence cited from the text", ["a loud tone", "a longer title", "a different topic"], "Evidence defends a claim.")

# 6.A
H('6.A', 3, "A pioneer family loses a crop but is rescued by neighbors. Which theme is developed through the plot?", "community can sustain people through hardship", ["neighbors cause trouble", "crops never fail", "hardship is imaginary"], "Rescue resolves conflict and signals theme.")
H('6.A', 4, "How can two American novels about ambition show similar themes?", "through characters whose pursuit of success has costs", ["through identical titles", "through matching page counts", "through the same cover art"], "Compare character and plot development.")

# 6.B
H('6.B', 3, "A character who dreams of a better life and reinvents himself is sometimes called what, in American literature?", "a self-made figure", ["a stock extra", "a glossary entry", "a footnote"], "The self-made figure is a recurring type.")
H('6.B', 4, "An author shows a character's honesty through repeated small acts, such as returning extra change. What method is this?", "indirect characterization", ["direct characterization", "a soliloquy", "an epigraph"], "Actions reveal traits without stating them.")

# 6.C
H('6.C', 3, "A scene in which a mother hides her tears while packing a suitcase mostly contributes what to the plot?", "emotional stakes for the departure", ["the story's rhyme", "the setting's name", "the thesis"], "Isolated scenes add weight to plot.")
H('6.C', 4, "A quiet scene before a trial shows a lawyer rehearsing alone. How does it contribute to the whole?", "it builds tension and reveals his doubts", ["it resolves the conflict", "it introduces a rhyme scheme", "it is unrelated"], "Scenes support the larger structure.")

# 6.D
H('6.D', 3, "A novel set in the Jim Crow South shows characters limited by unjust laws. How does the setting influence the plot?", "the laws create obstacles and shape the conflict", ["the setting has no effect", "the laws are invisible", "the plot is only about weather"], "Historical context shapes events.")
H('6.D', 4, "A story set during the Great Depression emphasizes sharing scarce food. What does the setting help develop?", "a theme about survival and generosity", ["a theme about abundance", "a rhyme scheme", "a comedy of manners"], "Setting influences theme.")

# 7.A
H('7.A', 3, "Who wrote 'The Scarlet Letter'?", "Nathaniel Hawthorne", ["Herman Melville", "Edgar Allan Poe", "Mark Twain"], "A classic of American Romanticism.")
H('7.A', 3, "Which novel by F. Scott Fitzgerald explores the American Dream in the 1920s?", "The Great Gatsby", ["Moby-Dick", "The Grapes of Wrath", "Walden"], "A key novel of the Jazz Age.")
H('7.A', 3, "Which author wrote the Transcendentalist essay 'Self-Reliance'?", "Ralph Waldo Emerson", ["Walt Whitman", "Emily Dickinson", "Robert Frost"], "Emerson championed individualism.")
H('7.A', 3, "Which literary period is associated with Harlem during the 1920s?", "the Harlem Renaissance", ["the Gothic revival", "the Beat era", "Colonial America"], "A flowering of Black arts and letters.")
H('7.A', 4, "Which poet is known for unconventional punctuation and short, slant-rhymed poems such as 'Hope is the thing with feathers'?", "Emily Dickinson", ["Langston Hughes", "Robert Frost", "Carl Sandburg"], "Dickinson used dashes and slant rhyme.")

# 7.B
H('7.B', 3, "Free verse poetry often uses which feature to create rhythm?", "line breaks and repetition rather than regular meter", ["strict iambic pentameter", "fixed rhyme pairs", "a required refrain"], "Free verse lacks fixed meter and rhyme.")
H('7.B', 4, "A poem with alternating end rhymes in a pattern ABAB is made of what?", "a quatrain with an alternating rhyme scheme", ["a couplet", "a haiku", "a limerick"], "ABAB is a common quatrain pattern.")
H('7.B', 3, "Repeating consonant sounds at the beginning of nearby words is called what?", "alliteration", ["assonance", "meter", "refrain"], "Alliteration repeats initial consonants.")

# 7.C
H('7.C', 3, "A play's narrator steps out of the scene to speak to the audience about the story. What dramatic convention is this?", "direct address", ["a footnote", "a stage curtain", "an index"], "Direct address breaks the fourth wall.")
H('7.C', 4, "A playwright mocks politicians by exaggerating their flaws. Which genre convention is used?", "satire", ["elegy", "ode", "epic"], "Satire uses exaggeration for critique.")

# 7.D
H('7.D.i', 3, "Which thesis best fits an analytical essay on a short story?", "'Through the use of a shifting setting, the author shows the narrator's growing fear.'", ["'I will write about a short story.'", "'The story has a setting.'", "'Short stories are fun.'"], "A thesis makes an arguable claim with focus.")
H('7.D.i', 4, "Where in an essay do pertinent examples belong?", "in body paragraphs that support the thesis", ["only in the title", "only in the introduction", "after the conclusion"], "Examples develop each point.")
H('7.D.ii', 3, "If an essay's thesis is about how a hero changes, which organization best supports it?", "following the hero's change in sequence", ["listing rhymes alphabetically", "describing the cover", "random events"], "Structure should serve the thesis.")

# 7.E
H('7.E.i', 3, "Which sentence is an arguable claim?", "'Public parks should receive more city funding than parking lots.'", ["'Parks have grass.'", "'Cities have budgets.'", "'Parking lots are gray.'"], "A claim takes a debatable position.")
H('7.E.i', 3, "Using statistics and logical reasoning to persuade is an appeal to what?", "logos", ["pathos", "ethos", "kairos"], "Logos appeals to reason.")
H('7.E.ii', 4, "A writer says, 'I agree that the fee is burdensome, but waiving it entirely would end the program.' This sentence combines a concession with what?", "a rebuttal", ["a thesis only", "a summary", "an anecdote"], "It grants a point, then counters.")
H('7.E.ii', 3, "Which kind of evidence is an expert's testimony?", "authoritative evidence", ["statistical evidence", "visual evidence", "invented evidence"], "Experts lend authority.")
H('7.E.iii', 3, "A writer addressing busy employees keeps an argument short and focused. What does this show?", "attention to the reader's needs", ["ignoring the reader", "wanting to hide the claim", "a lack of evidence"], "Audience awareness shapes style.")

# 7.F
H('7.F', 3, "Which element of a documentary film is part of its multimodal design?", "narration paired with archival images", ["only printed text", "only silence", "a table of contents"], "Documentaries combine modes.")
H('7.F', 3, "Why do many websites add alt text to images?", "to describe them for readers who cannot see them", ["to slow loading", "to hide captions", "to add rhyme"], "Alt text improves access.")

# 8.A
H('8.A', 3, "A speech given at a veterans' memorial honors the fallen with solemn words. What is the likely purpose?", "to commemorate and inspire respect", ["to sell a product", "to confuse", "to give directions"], "Commemorative speeches honor.")
H('8.A', 3, "A pamphlet from 1917 urges citizens to buy war bonds. What is its purpose?", "to persuade readers to act", ["to entertain", "to teach grammar", "to describe weather"], "Propaganda persuades.")
H('8.A', 4, "A magazine feature uses plain language and many photos to explain tax forms. Who is the intended audience?", "general readers", ["tax lawyers only", "toddlers", "no one"], "Accessible language signals a broad audience.")

# 8.B
H('8.B', 3, "An essay explains the stages of the Dust Bowl in the order they occurred. What structure does it use?", "chronological order", ["compare and contrast", "spatial order", "classification"], "Time order structures events.")
H('8.B', 4, "A text describes the benefits and costs of a policy and weighs them. What structure is dominant?", "compare and contrast", ["chronological", "descriptive", "alphabetical"], "Weighing options compares.")

# 8.C
H('8.C', 3, "A map in a history chapter showing territorial changes helps the reader do what?", "visualize changes across places", ["decode rhymes", "count syllables", "find the author's name"], "Maps show spatial change.")
H('8.C', 3, "Why might an author use a pull quote in a magazine feature?", "to highlight a key line and draw readers in", ["to hide the article", "to list sources", "to replace the title"], "Pull quotes emphasize ideas.")

# 8.D
H('8.D', 4, "An author describes factory workers as 'cogs in an endless machine.' How does this language shape perception?", "it suggests workers are dehumanized", ["it suggests workers are rich", "it suggests workers are lazy", "it has no effect"], "Metaphor affects readers' views.")
H('8.D', 3, "A writer chooses 'pioneer' rather than 'invader' to describe settlers. What does the choice influence?", "the reader's sympathy toward the settlers", ["the length of the sentence", "the page margin", "the rhyme"], "Diction affects perception.")

# 8.E
H('8.E', 3, "A man who sells fire extinguishers has his shop burn down. What kind of irony is this?", "situational irony", ["verbal irony", "dramatic irony", "sarcasm"], "The outcome contradicts expectation.")
H('8.E', 4, "A recurring image of rivers in a novel about change is an example of what?", "a motif", ["a pun", "an oxymoron", "an index"], "Motifs recur with meaning.")
H('8.E', 3, "Saying 'Nice weather we're having' during a hurricane is what?", "sarcasm or verbal irony", ["a motif", "a flashback", "an epigraph"], "The speaker means the opposite.")

# 8.F
H('8.F', 3, "A narrator's plain, everyday vocabulary and regional dialect most contribute to what?", "a distinct voice", ["a rhyme scheme", "a legal tone", "a mathematical tone"], "Diction shapes voice.")
H('8.F', 4, "Long, winding sentences with many clauses in a reflective essay tend to produce which mood?", "meditative", ["frantic", "abrupt", "comic"], "Syntax slows the pace.")
H('8.F', 3, "Terse, blunt sentences in a hard-boiled narrative create what tone?", "stark and unsentimental", ["warm and dreamy", "gently humorous", "ornate"], "Syntax shapes tone.")

# 8.G
H('8.G', 3, "'Ask not what your country can do for you; ask what you can do for your country' is an example of which device?", "antithesis", ["alliteration only", "onomatopoeia", "simile"], "Contrasting ideas in parallel form.")
H('8.G', 3, "Repeating 'I have a dream' at the start of successive sentences is an example of what?", "anaphora", ["antithesis", "irony", "hyperbole"], "Anaphora repeats at the start.")
H('8.G', 4, "A speaker begins with statistics, then shifts to a personal story. What is the likely purpose of the shift?", "to add emotional appeal", ["to avoid the topic", "to end the speech", "to confuse the audience"], "Shifts balance logic and feeling.")

# 9.B
H('9.B.i', 3, "An essay comparing two poets should likely be organized in what way?", "point by point or subject by subject", ["by alphabetical title", "in random order", "as a single sentence"], "Comparison needs a pattern.")
H('9.B.ii', 3, "Which choice best develops the claim that a setting is oppressive?", "describing low ceilings, locked windows and constant noise", ["saying it is a place", "listing the street address only", "naming the author"], "Specific details develop an idea.")
H('9.B.ii', 4, "What distinguishes depth of thought in an essay?", "explaining why evidence matters, not just presenting it", ["using longer words only", "adding more paragraphs", "repeating the thesis"], "Commentary shows thinking.")

# 9.C
H('9.C', 3, "A writer reorders the middle paragraphs so the strongest point comes last. What aspect is improved?", "organization", ["spelling", "typeface", "margins"], "Revision for emphasis and flow.")
H('9.C', 3, "Replacing 'said' with 'insisted' in dialogue improves what?", "diction and precision", ["page count", "spelling", "capitalization"], "A stronger verb conveys tone.")

# 9.D
H('9.D', 3, "Which sentence is correctly punctuated?", "Although the road was closed, we found another route.", ["Although the road was closed we, found another route.", "Although, the road was closed we found another route.", "Although the road was closed we found, another route."], "A comma follows an introductory clause.")
H('9.D', 3, "Which sentence maintains a consistent verb tense?", "He walked to the mill and saw the smoke.", ["He walks to the mill and saw the smoke.", "He walked to the mill and sees the smoke.", "He walk to the mill and seen the smoke."], "Both verbs are past tense.")
H('9.D', 3, "Which sentence has correct pronoun-antecedent agreement?", "When a customer arrives, the clerk greets him or her.", ["When customers arrives, the clerk greets her.", "When a customer arrive, the clerk greets them.", "When a customer arrives, the clerk greets it."], "The singular antecedent takes a singular pronoun.")
H('9.D', 3, "In 'the delegates met in philadelphia in may to write the constitution,' which words need capital letters?", "the, philadelphia, may and constitution", ["delegates and met only", "philadelphia only", "the and write only"], "Capitalize the first word, place names, months and the name of a document like the Constitution.")
H('9.D', 3, "Which sentence uses a dash correctly to set off a phrase?", "The senator—tired but determined—took the stage.", ["The senator tired—but determined took the—stage.", "The—senator tired but determined took the stage.", "The senator tired but—determined took—the stage."], "Dashes enclose the interruption.")
H('9.D', 3, "Which sentence uses parentheses correctly?", "The festival (held every spring) draws thousands.", ["The festival held (every spring draws) thousands.", "The (festival held every spring draws thousands.)", "The festival held every spring draws (thousands)."], "Parentheses enclose added information.")
H('9.D', 3, "Which sentence has no spelling errors?", "The committee will receive the necessary documents.", ["The comittee will recieve the neccessary documents.", "The committee will recieve the necessary documents.", "The committee will receive the neccessary documents."], "Common misspellings are fixed.")

# 10.D
H('10.D', 3, "In a business letter requesting information, where does the writer usually state the purpose?", "in the first paragraph", ["after the signature", "in the postscript only", "in the return address"], "Professional letters get to the point.")
H('10.D', 3, "Which closing is appropriate for a letter to a prospective employer?", "Respectfully yours,", ["See ya,", "Later,", "Cheers, buddy,"], "Formal closings fit professional letters.")

# 11
H('11.E', 3, "A student researching the Dust Bowl needs primary sources. Which is a primary source?", "a farmer's diary from the 1930s", ["a modern textbook chapter", "a movie review", "an encyclopedia entry"], "Primary sources come from the time period.")
H('11.F', 4, "A researcher notices two sources disagree on a number. What should the researcher do when synthesizing?", "explain the discrepancy and favor the better-supported figure", ["hide the conflict", "pick the larger number", "drop both sources"], "Synthesis addresses conflicts honestly.")
H('11.H', 3, "Which is an example of properly quoting a source?", "placing the exact words in quotation marks with a citation", ["using the exact words with no marks", "changing one word and omitting the source", "citing the wrong author"], "Direct quotes need marks and credit.")
H('11.G.i', 3, "Which clue most strongly suggests an article is credible?", "named authors with relevant expertise and cited sources", ["no author listed", "only emotional language", "anonymous claims"], "Credible sources show expertise and evidence.")
H('11.G.i', 4, "An advocacy group's report mentions only data supporting its goal. What is the concern?", "possible bias through omission", ["too much detail", "too many experts", "correct citation format"], "Selective presentation skews conclusions.")
H('11.G.ii', 3, "'Everyone I know likes this candidate, so the candidate will win' is an example of what?", "hasty generalization", ["valid reasoning", "an appeal to experts", "a rhyme"], "A small sample is overgeneralized.")
H('11.G.ii', 3, "'If we don't pass this law, our whole economy will collapse' offers what kind of reasoning when no evidence is given?", "an unsupported either-or claim", ["a balanced analysis", "an expert citation", "a statistical proof"], "It oversimplifies outcomes.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_eng3.jsonl'))

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('128.', 1071, own='sla_6.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# b.1
H('7.b.1.A',3,"A listener's crossed arms and frown are examples of:",
  "non-verbal messages",
  ["written messages","spelling errors","punctuation marks"],
  "Body language is a non-verbal message a listener can interpret.")
H('7.b.1.A',3,"To interpret a speaker's message fully, a listener pays attention to words and also to:",
  "tone of voice and body language",
  ["the clock","the room's paint","the seating chart"],
  "Verbal and non-verbal cues work together.")
H('7.b.1.B',3,"A coach says: stretch, jog two laps, then drink water. Following multiple action steps means:",
  "doing each action in the order given",
  ["doing only the last one","doing them in any order, or none","skipping the water"],
  "Multi-step directions are followed in sequence.")
H('7.b.1.B',3,"To restate multi-step directions accurately, a listener can:",
  "summarize each step in sequence",
  ["ask no questions","repeat only the first word","write nothing and hope"],
  "Restating each step shows understanding.")
H('7.b.1.C',3,"An organized oral presentation has:",
  "a clear opening, body and closing",
  ["random order of ideas","no main point","only questions"],
  "Organization helps listeners follow.")
H('7.b.1.C',3,"Enunciation means:",
  "pronouncing words clearly",
  ["speaking as loudly as possible","speaking as fast as possible","using only whispers"],
  "Enunciation is clear pronunciation.")
H('7.b.1.D',2,"In a group plan with shared responsibilities, each member:",
  "has a role and a task to finish",
  ["waits for others","does nothing","does everything"],
  "Shared plans assign roles.")
H('7.b.1.D',3,"If a teammate misses a deadline in a shared plan, a good response is to:",
  "talk with the teammate and adjust the plan",
  ["ignore it","finish the whole project alone and complain","quit the group"],
  "Collaboration means communicating and adjusting.")

# b.10
H('7.b.10.A',3,"An author writes an article explaining how vaccines work. The author's purpose and message are best described as:",
  "to inform readers about how vaccines protect people",
  ["to entertain with a silly story","to sell a product","to hide the facts"],
  "Explanatory articles inform.")
H('7.b.10.A',3,"The message of a text is:",
  "the main point or lesson the author wants readers to take away",
  ["the number of paragraphs","the title only","the author's address"],
  "A message is the takeaway.")
H('7.b.10.B',3,"An author uses chronological structure for a biography to:",
  "show how events in a life unfolded over time",
  ["compare two unrelated people","list vocabulary","hide the dates"],
  "Text structure supports the author's purpose.")
H('7.b.10.B',3,"A problem-and-solution structure in an editorial helps persuade readers by:",
  "showing why a change is needed",
  ["making the topic confusing","removing all evidence","listing random facts"],
  "Structure supports persuasion.")
H('7.b.10.C',3,"An inset in a magazine article is used to:",
  "highlight a related fact or story",
  ["replace the headline","hide the author","repeat the page number"],
  "Insets add focused extra information.")
H('7.b.10.C',3,"An author's use of boldface for key terms helps readers:",
  "locate important vocabulary",
  ["ignore the text","skip the chapter","count the words"],
  "Print features direct attention to key terms.")
H('7.b.10.D',3,"Which is an example of imagery?",
  "The scent of fresh bread drifted through the warm kitchen.",
  ["The bread was there.","Bread is food.","He ate."],
  "Imagery appeals to the senses.")
H('7.b.10.D',3,"'Time is a thief' is a:",
  "metaphor",
  ["simile","literal statement","fact"],
  "A metaphor says one thing is another.")
H('7.b.10.E',3,"In a story with a first-person narrator, the narrator is:",
  "a character who tells events using I",
  ["an outside voice using he and she","the author's editor","not in the story at all"],
  "First-person narrators take part in the story.")
H('7.b.10.E',3,"A third-person limited narrator tells the story:",
  "from outside, focusing on one character's thoughts",
  ["with the pronoun I","by addressing the reader as you","without any characters"],
  "Limited narrators focus on a single character's view.")
H('7.b.10.F',3,"One author writes a rainstorm scene with short, tense sentences and another with flowing, calm ones. These differences show:",
  "each author's voice",
  ["different spellings","different page numbers","different fonts"],
  "Sentence style helps create voice.")
H('7.b.10.F',3,"A humorous voice often uses:",
  "playful word choice and exaggeration",
  ["only dates and numbers","formal legal terms","no adjectives"],
  "Humor shows in word choice.")
H('7.b.10.G',3,"A stereotype is:",
  "an oversimplified idea about a group of people",
  ["a proven fact about everyone","a type of rhyme","a map symbol"],
  "Stereotypes overgeneralize.")
H('7.b.10.G',3,"An ad calls a pizza 'the best in the universe'. The hyperbole is meant to:",
  "make the claim sound exciting",
  ["provide exact data","teach history","correct a mistake"],
  "Hyperbole exaggerates for effect.")
H('7.b.10.G',3,"Why might a writer open an essay about teamwork with an anecdote?",
  "to make the idea personal and memorable",
  ["to avoid the topic","to replace evidence","to confuse the reader"],
  "Anecdotes draw readers in.")

# b.11
H('7.b.11.A',3,"A writer plans an essay urging the city to build a skate park. The best genre choice is:",
  "an opinion essay for city officials",
  ["a recipe","a limerick about cats","a weather chart"],
  "Genre fits purpose and audience.")
H('7.b.11.A',3,"Prewriting techniques include:",
  "brainstorming, outlining and freewriting",
  ["publishing, binding and printing","copying, pasting and deleting everything","erasing, folding and stapling"],
  "Prewriting plans a draft.")
H('7.b.11.B.i',3,"A strong conclusion does which of the following?",
  "restates the main idea and leaves the reader with a final thought",
  ["introduces a new argument","repeats every sentence","ends mid-idea"],
  "Conclusions wrap up the writing.")
H('7.b.11.B.i',3,"Which transition shows contrast?",
  "however",
  ["for example","in addition","as a result"],
  "However signals a contrast.")
H('7.b.11.B.ii',4,"Depth of thought is shown when a writer:",
  "explains why a fact matters",
  ["lists facts without comment","repeats the thesis","uses longer words only"],
  "Depth means analysis, not just facts.")
H('7.b.11.B.ii',3,"Which detail is the most specific?",
  "The Hubble Telescope has orbited Earth since 1990.",
  ["It is a big telescope.","Space things are cool.","There are things in space."],
  "Specific facts add depth.")
H('7.b.11.C',3,"Replacing a vague verb like 'went' with 'sprinted' improves:",
  "word choice",
  ["margins","pagination","the title"],
  "Precise verbs improve word choice.")
H('7.b.11.C',3,"To avoid choppy writing, a writer can:",
  "combine short sentences into longer ones",
  ["delete every adjective","start every sentence with 'The'","use only simple sentences"],
  "Combining sentences varies sentence structure.")
H('7.b.11.D.i',3,"A comma splice can be fixed by replacing the comma with:",
  "a period or a semicolon",
  ["a question mark","a hyphen","a second comma"],
  "Separate the sentences or join them correctly.")
H('7.b.11.D.i',3,"Which of these is a run-on sentence?",
  "The bell rang everyone left the room",
  ["The bell rang, and everyone left the room.","The bell rang. Everyone left the room.","After the bell rang, everyone left."],
  "Two complete thoughts run together without punctuation.")
H('7.b.11.D.ii',3,"What is the correct past tense of the irregular verb 'to go'?",
  "went",
  ["goed","gone","goes"],
  "Go is irregular; its past tense is went.")
H('7.b.11.D.ii',4,"What is the irregular simple past of 'tener' for yo?",
  "tuve",
  ["tené","tení","tenió"],
  "Tener has an irregular stem in the preterite.")
H('7.b.11.D.iii',3,"Which verb agrees with the collective noun in 'The team ___ ready'?",
  "is",
  ["are","were","be"],
  "A collective noun acting as a unit takes a singular verb.")
H('7.b.11.D.iii',3,"Which is a collective noun?",
  "flock",
  ["run","green","quickly"],
  "A flock is a group of birds.")
H('7.b.11.D.iv',3,"Which adjective indicates origin?",
  "Mexican",
  ["tall","loud","heavy"],
  "Mexican tells where something is from.")
H('7.b.11.D.iv',3,"What is the superlative form of 'good'?",
  "best",
  ["gooder","most good","better"],
  "Good is irregular: good, better, best.")
H('7.b.11.D.ix',3,"Acronyms like NASA are usually written with:",
  "all capital letters",
  ["all lowercase letters","only the first letter capitalized","no vowels"],
  "Acronyms use capital letters.")
H('7.b.11.D.ix',3,"Initials in a name, such as J. R. Wells, are written:",
  "with capital letters followed by periods",
  ["in lowercase with commas","without capitals","in italics only"],
  "Initials are capitalized and punctuated.")
H('7.b.11.D.v',3,"Which is a conjunctive adverb?",
  "therefore",
  ["because","and","although"],
  "Therefore connects ideas between clauses.")
H('7.b.11.D.v',4,"A conjunctive adverb joining two independent clauses is usually preceded by:",
  "a semicolon",
  ["a question mark","a quotation mark","an apostrophe"],
  "Use a semicolon before and a comma after.")
H('7.b.11.D.vi',4,"In 'The box of pencils is on the desk', the verb agrees with:",
  "box, not pencils",
  ["pencils, not box","desk","the preposition of"],
  "The subject is box.")
H('7.b.11.D.vi',4,"A prepositional phrase between a subject and its verb:",
  "does not change which word is the subject",
  ["becomes the subject","removes the verb","always makes the verb plural"],
  "The object of a preposition is never the subject.")
H('7.b.11.D.vii',3,"Which is an indefinite pronoun?",
  "everyone",
  ["she","myself","their"],
  "Indefinite pronouns do not name a specific person.")
H('7.b.11.D.vii',3,"Which pronoun is reflexive?",
  "themselves",
  ["them","their","they"],
  "Reflexive pronouns end in -self or -selves.")
H('7.b.11.D.viii',3,"Words like 'since', 'unless' and 'while' that start a dependent clause are called:",
  "subordinating conjunctions",
  ["coordinating conjunctions","prepositions","interjections"],
  "Subordinating conjunctions introduce dependent clauses.")
H('7.b.11.D.viii',3,"A complex sentence is formed when a subordinating conjunction joins:",
  "a dependent clause to an independent clause",
  ["two titles","two fragments only","two periods"],
  "A complex sentence has one independent and at least one dependent clause.")
H('7.b.10.D',3,"A poet writes that the sun 'waved goodbye' at dusk. This figurative language is:",
  "personification",
  ["a literal fact","a number","a rhyme scheme"],
  "The sun is given a human action.")
H('7.b.11.D.vii',3,"In 'Nobody left early', the word nobody is an:",
  "indefinite pronoun",
  ["reflexive pronoun","possessive pronoun","preposition"],
  "Indefinite pronouns refer to no specific person.")
H('7.b.11.D.x',3,"Titles of books are shown in print with:",
  "italics or underlining",
  ["bold only","all capitals","no marks"],
  "Book titles are italicized or underlined.")
H('7.b.11.D.x',3,"Which sentence correctly punctuates an introductory clause?",
  "After the game ended, we cheered.",
  ["We cheered after, the game ended.","After, the game ended we cheered.","After the game, ended we cheered."],
  "Use a comma after an introductory clause.")
H('7.b.11.D.xi',3,"Which spelling names a person who studies the stars?",
  "astrónomo",
  ["astronomo","astrónomó","ástronomo"],
  "Esdrújula words always carry an accent.")
H('7.b.11.D.xi',3,"Which spelling names a place where students earn degrees?",
  "universidad",
  ["universidat","unibersidad","universidád"],
  "Universidad uses v and ends in d.")
H('7.b.11.E',2,"A student finishes a report and posts it on the class website. This step is:",
  "publishing",
  ["brainstorming","outlining","drafting"],
  "Publishing shares the final copy.")
H('7.b.11.E',3,"Choosing a format for a specific audience, such as a brochure for parents, is part of:",
  "publishing for an appropriate audience",
  ["proofreading only","ignoring the reader","outlining"],
  "Publishing considers the audience.")

# b.12
H('7.b.12.A',3,"A fictional short story must include:",
  "characters, setting and a plot",
  ["a bibliography","a table of data","a citation"],
  "Fiction needs these story elements.")
H('7.b.12.A',3,"A personal narrative differs from fiction because it:",
  "tells about real events from the author's life",
  ["uses invented characters only","has no beginning","has no point of view"],
  "Personal narratives are true accounts.")
H('7.b.12.B',3,"A thesis statement in an informational composition:",
  "states the main idea about the topic",
  ["lists the bibliography","ends the paper","tells a joke"],
  "The thesis controls the composition.")
H('7.b.12.B',3,"Which source detail would strengthen a composition on the Amazon rainforest?",
  "a scientific estimate of how many species live there",
  ["the author's favorite color","a cartoon of a cat","the cost of a ticket"],
  "Relevant, factual details strengthen informational writing.")
H('7.b.12.C',3,"A counterclaim is:",
  "an opposing viewpoint the writer addresses",
  ["the writer's main idea","a type of rhyme","a conclusion"],
  "Strong arguments respond to opposing views.")
H('7.b.12.C',3,"An opinion essay is stronger when the writer:",
  "supports each reason with evidence",
  ["repeats the opinion without reasons","uses only feelings","avoids facts"],
  "Evidence strengthens reasons.")
H('7.b.12.D',3,"A letter requesting information should begin with:",
  "a greeting and a clear statement of purpose",
  ["a joke about the weather","the closing","a list of complaints"],
  "Request letters state the purpose early.")
H('7.b.12.D',2,"In a formal request letter, the closing might be:",
  "Sincerely,",
  ["See ya,","Whatever,","Later,"],
  "Formal letters use a polite closing.")

# b.13
H('7.b.13.A',3,"A researcher clarifies a broad question like 'Tell me about space' by:",
  "narrowing it to a specific focus",
  ["adding more topics","deleting it","making it vaguer"],
  "Clarifying makes a question researchable.")
H('7.b.13.A',3,"Formal inquiry differs from informal inquiry because it:",
  "follows a planned process and uses documented sources",
  ["relies on guessing","has no questions","uses no sources"],
  "Formal inquiry is structured.")
H('7.b.13.B',3,"Following a research plan helps a student:",
  "stay organized and meet deadlines",
  ["avoid sources","skip steps","write without notes"],
  "Plans keep research on track.")
H('7.b.13.B',3,"A research plan made with adult help might include:",
  "a timeline, a source list and check-in dates",
  ["a joke list","a seating chart","a lunch menu"],
  "Plans organize time and sources.")
H('7.b.13.C',3,"A variety of sources for a report might include:",
  "a book, an interview and a reliable website",
  ["three copies of the same page","only social media posts","only the cover of a book"],
  "Different types of sources give a fuller picture.")
H('7.b.13.C',3,"To gather relevant information efficiently, a researcher can use:",
  "keywords and an index",
  ["random page flipping","the cover image","guessing page numbers"],
  "Keywords and indexes lead to relevant information.")
H('7.b.13.D',3,"Which source is most credible for information about a medical topic?",
  "a published article by a doctor at a medical school",
  ["an anonymous blog","a rumor shared online","a friend's opinion"],
  "Credible sources have expert authors.")
H('7.b.13.D',3,"Credibility of a source is higher when the author:",
  "is an expert and cites evidence",
  ["is unknown","gives no sources","only shares opinions"],
  "Expertise and evidence build credibility.")
H('7.b.13.E',3,"Which shows understanding of information gathered?",
  "explaining the main points in a written summary",
  ["copying the first paragraph","listing page numbers","writing only the title"],
  "A summary shows understanding.")
H('7.b.13.E',3,"A graphic organizer can show understanding by:",
  "organizing facts into categories",
  ["hiding the facts","deleting the notes","mixing the topics"],
  "Organizers sort ideas.")
H('7.b.13.F',3,"Which is an example of paraphrasing?",
  "Rewriting an idea in your own words and citing the source",
  ["Copying a sentence without quotation marks","Copying the entire article","Changing only the author's name"],
  "Paraphrasing restates ideas with credit.")
H('7.b.13.F',3,"Plagiarism is a problem because it:",
  "presents someone else's work as your own",
  ["gives credit to the author","makes writing shorter","improves originality"],
  "Plagiarism is dishonest.")
H('7.b.13.G',3,"A bibliography entry usually includes the author, title and:",
  "publication information",
  ["the reader's name","a joke","a drawing"],
  "Publication details help locate the source.")
H('7.b.13.G',3,"Why do researchers include a bibliography?",
  "so readers can find the sources",
  ["to make the paper look longer","to hide sources","to list their friends"],
  "A bibliography credits and locates sources.")
H('7.b.13.H',3,"A student chooses a podcast to deliver research. This is an:",
  "oral mode of delivery",
  ["written mode of delivery","silent mode of delivery","unrelated mode of delivery"],
  "A podcast is spoken.")
H('7.b.13.H',3,"Which delivery combines more than one mode?",
  "a video with narration and text",
  ["a handwritten note","a spoken message only","a printed page only"],
  "Multimodal delivery blends modes.")

# b.2
H('7.b.2.A.i',3,"Which word is aguda?",
  "canción",
  ["mesa","árbol","teléfono"],
  "Canción is stressed on the last syllable.")
H('7.b.2.A.i',4,"In the word cómpraselo, the stress is on the:",
  "syllable before the third-to-last",
  ["last syllable","next-to-last syllable","third-to-last syllable"],
  "Sobresdrújulas are stressed before the antepenultimate syllable.")
H('7.b.2.A.ii',3,"How many syllables does the word sueño have?",
  "2",
  ["1","3","4"],
  "Sue-ño: ue is a diphthong.")
H('7.b.2.A.ii',3,"Two weak vowels together, as in ui in the word cuidado, form:",
  "a diphthong",
  ["a hiatus","a consonant blend","a prefix"],
  "Weak vowels combine into one syllable.")
H('7.b.2.A.iii',3,"Which word with an accent means 'more'?",
  "más",
  ["mas","màs","mâs"],
  "Más with an accent means more.")
H('7.b.2.A.iii',3,"Tú and tu differ because:",
  "tú means you and tu means your",
  ["they have different syllable counts","they are both verbs","the accent changes the sound of t"],
  "A diacritical accent changes meaning.")
H('7.b.2.A.iv',3,"The prefix anti- in the word antibiótico means:",
  "against",
  ["with","before","under"],
  "Anti- means against.")
H('7.b.2.A.iv',3,"The prefix super- in the word supermercado means:",
  "above or very large",
  ["below","without","again"],
  "Super- means over or beyond.")
H('7.b.2.B.i',3,"Which spelling of the word meaning 'now' uses h correctly?",
  "ahora",
  ["aora","ahorra","ahóra"],
  "Ahora begins with a silent h.")
H('7.b.2.B.i',3,"Which word is spelled with v?",
  "nuevo",
  ["nuebo","nueyo","nuevó"],
  "Nuevo uses v.")
H('7.b.2.B.ii',3,"Which spelling of the word for 'also' has the correct accent for a word stressed on the last syllable and ending in n?",
  "también",
  ["tambien","támbien","tambíen"],
  "Aguda words ending in n carry an accent.")
H('7.b.2.B.ii',3,"Which spelling is a grave word ending in a consonant other than n or s?",
  "árbol",
  ["arbol","arból","arbóll"],
  "Graves ending in other consonants take an accent.")
H('7.b.2.B.iii',4,"Which spelling is a correct sobresdrújula?",
  "dígamelo",
  ["digamelo","digámelo","digaméló"],
  "Sobresdrújulas always carry a written accent.")
H('7.b.2.B.iii',3,"Sobresdrújulas always carry:",
  "a written accent",
  ["no accent","two accents","a hyphen"],
  "Stress before the antepenultimate syllable is always marked.")
H('7.b.2.B.iv',3,"Which spelling shows a hiatus in a girl's name?",
  "María",
  ["Maria","Marìa","Mária"],
  "The accent on í separates the vowels.")
H('7.b.2.B.iv',3,"Which spelling shows a diphthong without an accent?",
  "ciudad",
  ["cíudad","ciúdad","ciudád"],
  "Iu forms a diphthong; no accent is needed.")
H('7.b.2.B.v',3,"Which spelling is correct for 'you ate' (tú, comer, simple past)?",
  "comiste",
  ["comíste","comistè","cómiste"],
  "The tú form of the simple past needs no accent here.")
H('7.b.2.B.v',3,"Which spelling is correct for 'I will sing'?",
  "cantaré",
  ["cantare","cántare","cantarê"],
  "Future yo forms carry an accent on the final é.")
H('7.b.2.C',2,"Cursive writing for a long assignment should stay:",
  "consistent and readable",
  ["tiny at the end","messy to save time","different each line"],
  "Legible writing aids communication.")
H('7.b.2.C',2,"Which habit improves cursive legibility?",
  "keeping letters evenly sloped and sized",
  ["pressing as hard as possible","rushing each word","skipping loops"],
  "Consistency improves legibility.")

# b.3
H('7.b.3.A',3,"Which resource would show a word's origin?",
  "a dictionary entry",
  ["a calendar","a ruler","a map"],
  "Dictionaries often include etymology.")
H('7.b.3.A',3,"A thesaurus is used to find:",
  "synonyms",
  ["page numbers","maps","pronunciation only"],
  "A thesaurus lists words with similar meanings.")
H('7.b.3.B',3,"To determine the meaning of an unfamiliar word you can use:",
  "clues in the sentences nearby",
  ["its page number","the font","the book's color"],
  "Context beyond a sentence reveals meaning.")
H('7.b.3.B',3,"The sentence 'Her actions were benevolent; she donated food every week' suggests benevolent means:",
  "kind and generous",
  ["cruel","lazy","confused"],
  "Donating food shows kindness.")
H('7.b.3.C',3,"The prefix trans- in the word transatlántico means:",
  "across",
  ["under","before","not"],
  "Trans- means across or beyond.")
H('7.b.3.C',3,"The prefix semi- in the word semicírculo means:",
  "half",
  ["double","many","none"],
  "Semi- means half.")
H('7.b.3.D',3,"An adage is:",
  "a short saying that expresses a common truth",
  ["a type of rhyme","a long story","a math rule"],
  "Adages are traditional sayings.")
H('7.b.3.D',3,"A pun is:",
  "a joke that plays on word meanings or sounds",
  ["a type of map","a rule of grammar","a list of facts"],
  "Puns use wordplay.")
H('7.b.3.E',3,"Sino and si no are commonly confused because they:",
  "sound alike but have different meanings",
  ["are spelled the same","have the same meaning","are both verbs"],
  "Sound-alike terms need careful spelling.")
H('7.b.3.E',3,"Homographs such as 'live' (to reside) and 'live' (alive) differ in:",
  "pronunciation and meaning",
  ["spelling only","number of letters","nothing"],
  "Homographs share spelling but not meaning or sometimes sound.")

# b.4 b.5
H('7.b.4',2,"Strong readers often improve their writing because:",
  "reading and writing skills build on each other",
  ["they are unrelated","only listening helps","writing hurts reading"],
  "Language skills support each other.")
H('7.b.4',2,"Talking through ideas with a partner before writing uses:",
  "speaking and listening to support writing",
  ["only reading","only spelling","no skills"],
  "Oral language supports writing.")
H('7.b.5',2,"A student interviews a classmate, takes notes and writes a profile. Which skills were integrated?",
  "listening, speaking and writing",
  ["only drawing","only counting","none"],
  "Integrated tasks use several skills.")
H('7.b.5',2,"Reading a text aloud with expression practices:",
  "reading and speaking together",
  ["writing only","drawing only","counting"],
  "Oral reading combines skills.")

# b.6
H('7.b.6.A',3,"Before reading a primary source, a student might set the purpose to:",
  "learn how people experienced an event",
  ["find the longest word","skip the introduction","count the images"],
  "Purpose guides reading.")
H('7.b.6.A',3,"A reader's purpose can change when:",
  "the reader's goal changes",
  ["the font changes","the page turns","the title is underlined"],
  "Purposes are tied to goals.")
H('7.b.6.B',3,"A question that deepens understanding during reading is:",
  "Why did the author include this detail?",
  ["What time is it?","Is the page number odd?","Where is the cover?"],
  "Analytical questions deepen thinking.")
H('7.b.6.B',3,"Asking questions before reading helps a reader:",
  "activate prior knowledge",
  ["skip the text","avoid thinking","forget the topic"],
  "Pre-reading questions prepare the mind.")
H('7.b.6.C',3,"A reader predicts that a mystery's detective will find the culprit. The prediction is based on:",
  "genre characteristics",
  ["the page count","the cover weight","the author's birthday"],
  "Genre patterns guide predictions.")
H('7.b.6.C',3,"If a prediction turns out to be wrong, the reader should:",
  "revise it using new evidence",
  ["ignore the text","restart the book","stop reading"],
  "Predictions are corrected or confirmed with evidence.")
H('7.b.6.D',3,"Visualizing a scene in a poem helps readers to:",
  "deepen understanding of the images",
  ["skip the stanzas","change the rhyme","ignore the title"],
  "Mental images deepen comprehension.")
H('7.b.6.D',3,"Which sensory words help create a mental image?",
  "crackling, golden, smoky",
  ["is, was, be","the, a, an","it, they, we"],
  "Sensory words create images.")
H('7.b.6.E',3,"A student reads about immigration and thinks about a neighbor's family history. This is a:",
  "personal connection",
  ["table of contents","summary","glossary"],
  "Connections relate texts to experience.")
H('7.b.6.E',3,"Connecting a novel to a news event is a connection to:",
  "society",
  ["the page number","the font","the glossary"],
  "Text-to-world connections link to society.")
H('7.b.6.F',3,"From the sentence 'Jo checked her backpack twice and sighed', a reader can infer Jo is:",
  "worried she forgot something",
  ["celebrating","sleeping","laughing"],
  "Actions give clues about feelings.")
H('7.b.6.F',3,"Inferences are strongest when they are supported by:",
  "multiple pieces of evidence",
  ["one guess","a feeling","the cover"],
  "More evidence makes inferences stronger.")
H('7.b.6.G',3,"To decide which details are key, a reader asks:",
  "Which details support the main idea?",
  ["Which are longest?","Which are first?","Which are in color?"],
  "Key details support the main idea.")
H('7.b.6.G',3,"A key idea differs from a minor detail because it:",
  "is central to the meaning of the text",
  ["appears only once","is always a number","is always first"],
  "Key ideas carry the meaning.")
H('7.b.6.H',3,"Which activity shows synthesis?",
  "Combining facts from a graph and an article to form a new conclusion",
  ["Copying a graph","Copying an article","Skipping both"],
  "Synthesis merges sources.")
H('7.b.6.H',3,"Synthesis results in:",
  "a new understanding",
  ["a copy of the text","a list of page numbers","a title"],
  "Synthesis builds new meaning.")
H('7.b.6.I',3,"A reader realizes she cannot explain what she just read. A good adjustment is to:",
  "pause, reread and summarize",
  ["keep reading faster","skip the section","close the book"],
  "Fix-up strategies restore meaning.")
H('7.b.6.I',3,"Monitoring comprehension includes:",
  "checking whether the text makes sense as you read",
  ["counting pages","guessing endings","copying sentences"],
  "Monitoring is checking understanding.")

# b.7
H('7.b.7.A',2,"A self-selected text is one that you:",
  "choose to read yourself",
  ["must read for a test","never read","cannot understand"],
  "Self-selected texts are chosen by the reader.")
H('7.b.7.A',3,"A personal connection response might begin:",
  "This reminds me of a time when I",
  ["The author's address is","The publisher is","Page twelve says"],
  "Personal connections link to experience.")
H('7.b.7.B',3,"A compare-and-contrast response to two poems should discuss:",
  "similarities and differences in theme, style or imagery",
  ["page numbers","the poets' ages only","word counts only"],
  "Comparisons examine meaning and craft.")
H('7.b.7.B',3,"Which response demonstrates understanding?",
  "The story shows how courage can grow from fear, as when Ana speaks at the assembly.",
  ["The story is a story.","I liked it.","It was fine."],
  "A strong response explains with a detail.")
H('7.b.7.C',3,"Text evidence can be shown by:",
  "quoting or paraphrasing a detail and explaining it",
  ["pointing to the cover","guessing","skipping details"],
  "Evidence is a detail plus explanation.")
H('7.b.7.C',3,"Which piece of text evidence best supports 'The wolf is cunning'?",
  "The wolf disguised himself as a sheep to trick the farmer.",
  ["The wolf lives in the forest.","The wolf is gray.","The farmer has sheep."],
  "Actions show character traits.")
H('7.b.7.D',3,"A summary of an article should:",
  "include main ideas in logical order",
  ["include every detail","add your opinions only","start at the end"],
  "Summaries are concise and ordered.")
H('7.b.7.D',3,"To paraphrase a sentence you:",
  "restate it in different words, keeping the meaning",
  ["copy it","reverse its meaning","delete it"],
  "Paraphrase keeps meaning.")
H('7.b.7.E',3,"Notetaking while reading helps because it:",
  "records key ideas for later",
  ["replaces reading","hides the text","always slows thinking"],
  "Notes capture key ideas.")
H('7.b.7.E',3,"Which is an example of interacting with a source?",
  "creating a sketchnote of the main ideas",
  ["closing the book","tearing it","hiding it"],
  "Sketchnotes are a meaningful interaction.")
H('7.b.7.F',3,"Using precise vocabulary learned in class in a response shows:",
  "deeper understanding",
  ["carelessness","copying","avoidance"],
  "Applying vocabulary shows learning.")
H('7.b.7.F',3,"A student writes: 'The explorer's perseverance impressed me.' The student is:",
  "applying a newly learned word",
  ["avoiding vocabulary","skipping the reading","drawing"],
  "Using new words in context shows learning.")
H('7.b.7.G',3,"In a text discussion, an important idea can be supported by:",
  "citing a specific passage",
  ["changing the subject","guessing","staying silent"],
  "Discussion draws on the text.")
H('7.b.7.G',3,"Discussing specific ideas helps a group:",
  "build shared understanding",
  ["avoid the text","end the discussion","forget the meaning"],
  "Discussion deepens meaning.")

# b.8
H('7.b.8.A',3,"A novel about a girl who learns about courage and loyalty has:",
  "multiple themes",
  ["no themes","only one setting","only one word"],
  "Texts can have several themes.")
H('7.b.8.A',3,"To infer multiple themes, a reader should:",
  "find evidence for each idea in the text",
  ["pick one word","ignore events","guess"],
  "Themes need text evidence.")
H('7.b.8.B',3,"Conflict between a character and a storm is called:",
  "character versus nature",
  ["character versus self","character versus society","character versus time"],
  "The storm is a force of nature.")
H('7.b.8.B',3,"A conflict inside a character's mind is:",
  "internal conflict",
  ["external conflict","the setting","the theme"],
  "Internal conflict happens in the character.")
H('7.b.8.C',3,"The rising action of a plot:",
  "builds tension through events and complications",
  ["solves the problem","ends the story","introduces the title"],
  "Rising action leads to the climax.")
H('7.b.8.C',3,"The resolution of a story is when:",
  "the main conflict is settled",
  ["the conflict begins","the setting is described","the title appears"],
  "The resolution ends the conflict.")
H('7.b.8.D',3,"A story set during the Great Depression shapes the plot by:",
  "creating problems tied to poverty and hardship",
  ["removing all problems","making time irrelevant","changing the author"],
  "Historical settings influence events.")
H('7.b.8.D',3,"A cultural setting influences a plot when characters:",
  "make choices based on their community's customs",
  ["ignore all customs","speak no words","have no relationships"],
  "Culture shapes choices.")

# b.9
H('7.b.9.A',3,"A legend is a story that is usually:",
  "based on a historical person or event with exaggeration",
  ["a recipe","a news report","a dictionary entry"],
  "Legends blend history and exaggeration.")
H('7.b.9.A',3,"A moral at the end of a fable is:",
  "the lesson it teaches",
  ["the title","the setting","the author's name"],
  "Fables teach morals.")
H('7.b.9.B',3,"Alliteration is:",
  "repetition of beginning consonant sounds",
  ["repetition of ending vowels","comparison using like","exaggeration"],
  "Alliteration is a sound device.")
H('7.b.9.B',3,"In a poem, the voice that tells the poem, who may not be the poet, is the:",
  "speaker",
  ["editor","publisher","illustrator"],
  "The speaker is distinct from the poet.")
H('7.b.9.C',3,"In a script, parentheses and italics often show:",
  "stage directions",
  ["the author's address","page numbers","spelling errors"],
  "Stage directions guide performance.")
H('7.b.9.C',3,"A scene in a play is:",
  "a section of an act in one setting and time",
  ["a whole play","a prop","a costume"],
  "Acts are divided into scenes.")
H('7.b.9.D.i',3,"Evidence that supports a central idea is best when it is:",
  "relevant and specific",
  ["long and unrelated","vague and general","opinion only"],
  "Evidence should fit the idea.")
H('7.b.9.D.i',3,"To identify the central idea of a science article, a reader looks at:",
  "the title, headings and repeated key ideas",
  ["only the first word","the page numbers","the font"],
  "These clues reveal the main idea.")
H('7.b.9.D.ii',3,"A timeline helps readers:",
  "see the order of events",
  ["compare opinions","count syllables","find rhymes"],
  "Timelines show sequence.")
H('7.b.9.D.ii',3,"A sidebar differs from the main text because it:",
  "gives extra information set apart on the page",
  ["replaces the headline","is the conclusion","is the title"],
  "Sidebars add focused information.")
H('7.b.9.D.iii',3,"Order of importance organizes information from:",
  "most to least important, or the reverse",
  ["oldest to newest only","A to Z always","random order"],
  "Importance determines the order.")
H('7.b.9.D.iii',3,"Logical order arranges ideas:",
  "so each idea follows sensibly from the last",
  ["by length","by color","randomly"],
  "Logical order makes sense step by step.")
H('7.b.9.E.i',3,"A claim in an editorial is:",
  "the writer's position on an issue",
  ["the writer's address","a rhyme","a fact everyone agrees on"],
  "The claim is the stance argued.")
H('7.b.9.E.i',3,"Which sentence is the clearest claim?",
  "Middle schools should start classes after 8:30 a.m.",
  ["Schools have start times.","Many students wake up.","8:30 is a time."],
  "A claim takes a position.")
H('7.b.9.E.ii',3,"An author uses facts against an argument to:",
  "show the opposing claim is weak or incorrect",
  ["agree with it","ignore it","rhyme"],
  "Facts can refute claims.")
H('7.b.9.E.ii',3,"Which fact could be used against the claim 'Homework always improves grades'?",
  "A study found no grade gains for students with heavy nightly homework.",
  ["Homework takes time.","Some teachers assign homework.","Students have backpacks."],
  "Evidence that contradicts the claim works against it.")
H('7.b.9.E.iii',3,"A magazine article with technical terms about engineering is aimed at:",
  "readers interested in engineering",
  ["babies","no one","pets"],
  "Technical language suggests an informed audience.")
H('7.b.9.E.iii',3,"The intended audience of a tween magazine ad is:",
  "young readers around middle-school age",
  ["retirees","toddlers","lawyers"],
  "Tween means ages around ten to twelve.")
H('7.b.9.F',3,"A podcast with a transcript is multimodal because it:",
  "offers both audio and text",
  ["has only text","has no content","has only images"],
  "Multimodal texts use more than one mode.")
H('7.b.9.F',3,"Hyperlinks let readers:",
  "move to related information with a click",
  ["erase the text","change the author","print the page color"],
  "Digital texts use links.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'sla_6.jsonl'))

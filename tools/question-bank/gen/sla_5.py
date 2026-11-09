import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('128.', 1070, own='sla_5.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# b.1
H('6.b.1.A',3,"A pertinent comment builds on what a speaker said. Which one does?",
  "Your example about the river helped me understand the setting.",
  ["My dog is brown.","I forgot my folder.","Is it recess yet?"],
  "Pertinent comments connect to the speaker's ideas.")
H('6.b.1.A',2,"Asking a speaker to explain what a term meant is a way to:",
  "clarify information",
  ["change the topic","end the talk","show you stopped listening"],
  "Relevant questions clarify meaning.")
H('6.b.1.B',3,"A teammate gives you four oral steps for a science lab. To restate them you should:",
  "repeat each step in order using your own words",
  ["repeat only step four","say them backward","skip the steps you forgot"],
  "Restating shows you understood the sequence.")
H('6.b.1.B',2,"Oral instructions with related steps often use words like:",
  "first, then, after that, finally",
  ["maybe, never, always, nobody","blue, green, red, pink","up, down, left, there"],
  "Sequence words keep instructions clear.")
H('6.b.1.C',3,"When expressing an opinion in a talk, you should back it up with:",
  "accurate information",
  ["a louder voice","longer pauses","a guess"],
  "Opinions are stronger with accurate support.")
H('6.b.1.C',3,"Which opinion is supported by accurate information?",
  "Our school needs more bike racks because forty students ride bikes daily.",
  ["Our school needs more bike racks because I said so.","Bike racks are cool, probably.","Everyone wants bike racks, I think."],
  "Facts make an opinion convincing.")
H('6.b.1.D',3,"A shared-responsibility plan for a group project lists:",
  "who will do each task and when",
  ["only the leader's name","the grade you expect","nothing in writing"],
  "Plans divide tasks clearly.")
H('6.b.1.D',2,"Group members develop a plan of shared responsibilities so that:",
  "the work is divided fairly",
  ["one person does everything","no one knows the job","the project never ends"],
  "Shared plans support teamwork.")

# b.10
H('6.b.10.A',3,"A speech urging students to join a recycling club has the purpose to:",
  "persuade",
  ["confuse","rhyme","tease"],
  "Calls to action persuade.")
H('6.b.10.A',3,"After reading a fable about a hare who bragged and lost a race, the author's message is likely:",
  "Bragging can lead to failure.",
  ["Hares are slow.","Races are long.","Prizes are shiny."],
  "A message is the lesson in the text.")
H('6.b.10.B',3,"An author compares two cities side by side. This structure helps the purpose of:",
  "showing similarities and differences",
  ["listing steps","telling a joke","giving a date"],
  "Compare and contrast supports comparison.")
H('6.b.10.B',3,"Putting a text in cause-and-effect order helps the author:",
  "explain why events happened",
  ["hide the main idea","count the sentences","avoid facts"],
  "Cause and effect explains reasons.")
H('6.b.10.C',3,"Why might an author use a sidebar in a magazine article?",
  "to add extra information beside the main text",
  ["to end the article","to hide facts","to repeat the title"],
  "Sidebars give additional details.")
H('6.b.10.C',3,"An author puts a foreign word in italics to:",
  "signal that the word is special",
  ["make it disappear","show a mistake","shorten the line"],
  "Print features direct attention.")
H('6.b.10.D',3,"'The wind whispered through the trees' is an example of:",
  "personification",
  ["hyperbole","a fact","a title"],
  "Wind is given a human action.")
H('6.b.10.D',3,"Which phrase is literal language?",
  "The pool is four feet deep.",
  ["The pool is an ocean.","The pool swallowed me whole.","The pool is a giant bathtub."],
  "Literal language means exactly what it says.")
H('6.b.10.E',3,"In first-person point of view, the reader learns:",
  "only what the narrator knows and feels",
  ["everything about every character","nothing at all","the author's secrets"],
  "First-person narrators share their own view.")
H('6.b.10.E',3,"A narrator outside the story who describes what every character does uses:",
  "third-person point of view",
  ["first-person point of view","second-person point of view","no point of view"],
  "Third-person narrators stand outside the story.")
H('6.b.10.F',3,"Which sentence most helps readers hear a formal voice?",
  "The committee will convene promptly at noon.",
  ["Yo, we start at noon, okay?","Noon! Be there or be square!","We kick off at noon, folks."],
  "Formal word choice creates a formal voice.")
H('6.b.10.F',3,"An author's voice is created by:",
  "word choice, tone and sentence style",
  ["page size","paper color","the printer's name"],
  "Voice comes from how the author uses language.")
H('6.b.10.G',3,"An anecdote is a:",
  "short story used to make a point",
  ["list of facts","type of rhyme","table of data"],
  "Anecdotes illustrate ideas.")
H('6.b.10.G',3,"A speaker begins with a brief story about getting lost to show why maps matter. This is an:",
  "anecdote",
  ["index","hyperbole","glossary"],
  "A short personal story that supports a point is an anecdote.")

# b.11
H('6.b.11.A',3,"Before drafting a letter to the principal, a writer should consider:",
  "the purpose and the audience",
  ["the paper's weight","the pencil brand","the weather"],
  "Planning starts with purpose and audience.")
H('6.b.11.A',3,"Choosing a genre means deciding whether you will write:",
  "a poem, a report or an opinion essay",
  ["in blue ink","with big margins","on Friday"],
  "Genre is the type of text.")
H('6.b.11.B.i',3,"Transition words such as 'however' and 'for example' help writers:",
  "connect ideas smoothly",
  ["shorten words","skip paragraphs","avoid punctuation"],
  "Transitions link ideas.")
H('6.b.11.B.i',3,"A conclusion should:",
  "wrap up the main idea",
  ["introduce a brand-new topic","repeat the title ten times","apologize for writing"],
  "Conclusions bring the writing to a close.")
H('6.b.11.B.ii',3,"An engaging idea is developed with:",
  "relevant details and examples",
  ["random facts","longer words only","extra spacing"],
  "Relevant details support the idea.")
H('6.b.11.B.ii',3,"Which sentence adds a relevant detail to 'The festival was fun'?",
  "Colorful dancers twirled while a band played.",
  ["I own a bicycle.","Math is hard.","It rained last July."],
  "A relevant detail stays on the topic.")
H('6.b.11.C',3,"Deleting a sentence that does not support your main idea is part of:",
  "revising",
  ["publishing","brainstorming","alphabetizing"],
  "Revision includes adding, deleting and combining.")
H('6.b.11.C',3,"Combining 'The dog barked. The dog was loud.' into one sentence improves:",
  "sentence structure",
  ["spelling only","margins","the title"],
  "Combining sentences smooths the writing.")
H('6.b.11.D.i',4,"Which choice fixes the comma splice 'We were tired, we kept walking'?",
  "We were tired, but we kept walking.",
  ["We were tired, we kept walking.","We were tired we kept walking.","We were tired, kept walking, we."],
  "Add a coordinating conjunction after the comma to join two complete thoughts.")
H('6.b.11.D.i',3,"Which verb completes 'The books on the shelf ___ old' with subject-verb agreement?",
  "are",
  ["is","am","be"],
  "A plural subject, books, takes a plural verb.")
H('6.b.10.D',3,"A writer says the moon smiled down on the field. This figurative language is:",
  "personification",
  ["a fact","literal language","a rhyme"],
  "The moon is given a human action.")
H('6.b.11.B.i',3,"A strong introduction might begin with:",
  "an interesting question or fact about the topic",
  ["the last sentence of the essay","a list of page numbers","a goodbye"],
  "Introductions hook the reader and name the topic.")
H('6.b.11.D.vi',3,"A prepositional phrase can tell where something is, such as:",
  "sobre el escritorio",
  ["tengo hambre","corre rápido","es muy alto"],
  "Sobre el escritorio begins with a preposition and shows location.")
H('6.b.13.F',3,"Quotation marks and a citation are used when you:",
  "use an author's exact words",
  ["paraphrase loosely without credit","invent facts","skip the source"],
  "Exact words need quotation marks and credit.")
H('6.b.2.B.i',3,"Which spelling of the place where trains stop is correct?",
  "estación",
  ["estacion","estácion","estaciòn"],
  "Estación is stressed on the last syllable and ends in n.")
H('6.b.6.H',3,"Merging details from a map and a passage to understand a trip is:",
  "synthesizing",
  ["scanning","skipping","alphabetizing"],
  "Synthesis combines sources into new understanding.")
H('6.b.9.F',3,"Which feature is common in a digital text?",
  "hyperlinks that open related pages",
  ["page numbers only","ink smudges","a paper cover"],
  "Digital texts often include links.")
H('6.b.11.D.ii',4,"Which verb phrase uses a past participle?",
  "había terminado",
  ["terminaré","termino","terminando"],
  "Haber plus a participle forms a perfect tense.")
H('6.b.11.D.ii',3,"'Mañana comeremos temprano' is in the:",
  "future tense",
  ["imperfect past","present tense","simple past"],
  "Mañana and the -emos future ending show the future.")
H('6.b.11.D.iii',3,"Which phrase has the correct gender-specific article?",
  "la mano",
  ["el mano","los mano","un mano"],
  "Mano is feminine even though it ends in o.")
H('6.b.11.D.iii',3,"Which is the plural of 'canción'?",
  "canciones",
  ["canciónes","cancións","cancionos"],
  "Nouns ending in -ción form the plural with -ciones.")
H('6.b.11.D.iv',3,"In 'Esta tarea es menos difícil que la otra', the phrase menos difícil is a:",
  "comparative",
  ["superlative","noun","verb"],
  "Menos plus que compares two things.")
H('6.b.11.D.iv',3,"Which phrase is a superlative?",
  "la más rápida del equipo",
  ["más rápida que Ana","rápida","tan rápida como Ana"],
  "A superlative names the highest degree in a group.")
H('6.b.11.D.ix',3,"In Spanish, titles of books usually capitalize:",
  "only the first word and proper nouns",
  ["every word","no words","only the last word"],
  "Spanish title capitalization is limited.")
H('6.b.11.D.ix',3,"Which is the name of a historical document that should be capitalized?",
  "the Declaration of Independence",
  ["the weather report","the lunch menu","the class schedule"],
  "Names of historical documents are capitalized.")
H('6.b.11.D.v',3,"Which adverb tells how often?",
  "siempre",
  ["aquí","despacio","muy"],
  "Siempre means always.")
H('6.b.11.D.v',3,"Which adverb tells degree (how much)?",
  "muy",
  ["nunca","hoy","atrás"],
  "Muy means very.")
H('6.b.11.D.vi',3,"Which phrase is a prepositional phrase?",
  "debajo de la mesa",
  ["corre muy rápido","la niña alta","canta y baila"],
  "It starts with a preposition.")
H('6.b.11.D.vi',3,"Hacia, desde and entre are all:",
  "prepositions",
  ["verbs","adjectives","conjunctions"],
  "These words introduce prepositional phrases.")
H('6.b.11.D.vii',3,"Pronouns that follow prepositions, such as mí, ti and él, are called:",
  "prepositional pronouns",
  ["reflexive pronouns","possessive adjectives","interjections"],
  "They come after a preposition.")
H('6.b.11.D.vii',3,"Which sentence uses a reflexive pronoun?",
  "Ella se peina.",
  ["Ella peina a su hermana.","Ella canta bien.","Ellos comen."],
  "Se shows the subject does the action to itself.")
H('6.b.11.D.viii',3,"A compound predicate has two verbs for one subject. Which fits?",
  "Tomás lee y escribe.",
  ["Tomás y Ana leen.","Tomás lee.","Lee Tomás."],
  "Lee and escribe share the subject Tomás.")
H('6.b.11.D.viii',3,"The conjunction 'o' in 'té o café' joins:",
  "two choices",
  ["two verbs only","two sentences only","two titles"],
  "O joins alternatives.")
H('6.b.11.D.x',4,"In compound sentences, a comma usually comes before:",
  "a coordinating conjunction joining two complete thoughts",
  ["every verb","the last period","every noun"],
  "Use a comma before the conjunction in a compound sentence.")
H('6.b.11.D.x',3,"An em dash in written dialogue is used to:",
  "show that a character is speaking",
  ["end a paragraph","join two numbers","mark a title"],
  "Spanish dialogue often begins with an em dash.")
H('6.b.11.D.xi',3,"Which spelling names the place where you borrow books?",
  "biblioteca",
  ["bibloteca","biblioteka","viblioteca"],
  "Biblioteca uses b and c.")
H('6.b.11.D.xi',3,"Which spelling names water falling from clouds?",
  "lluvia",
  ["yuvia","lluvía","lluvya"],
  "Lluvia starts with ll.")
H('6.b.11.E',2,"To publish a report for the school community you might:",
  "post a final copy in the library",
  ["keep the first draft in your desk","erase the report","skip editing"],
  "Publishing shares final work.")
H('6.b.11.E',3,"Before publishing, a writer should:",
  "edit for spelling and punctuation",
  ["tear up the draft","remove the title","hide the audience"],
  "Final copies are edited.")

# b.12
H('6.b.12.A',3,"A personal narrative uses:",
  "first-person point of view and real events",
  ["third-person facts only","a list of steps","a table of data"],
  "Personal narratives tell about your own experience.")
H('6.b.12.A',3,"A poem might use:",
  "images, rhythm and figurative language",
  ["tables, bullets and sidebars","citations and a bibliography","legal terms"],
  "Poems rely on sound and imagery.")
H('6.b.12.B',3,"A brief composition that conveys information about a topic begins with:",
  "a topic sentence",
  ["a joke","a recipe","a rhyme"],
  "A topic sentence names the subject.")
H('6.b.12.B',3,"Which sentence belongs in an informational composition about volcanoes?",
  "Magma rises through cracks in Earth's crust.",
  ["I want a pet lizard.","Volcanoes are boring.","Once upon a time there was a dragon."],
  "Informational writing presents facts.")
H('6.b.12.C',3,"An opinion essay states a claim and gives:",
  "reasons and evidence",
  ["rhymes and riddles","directions and steps","jokes and songs"],
  "Argumentative writing supports claims.")
H('6.b.12.C',3,"Which is the strongest evidence for 'School lunches should include more fruit'?",
  "A study found students who ate fruit paid better attention.",
  ["Fruit is my favorite.","I like lunch.","Fruit is colorful."],
  "Evidence from a study is convincing.")
H('6.b.12.D',3,"A letter that requests information should include:",
  "a clear question and a polite closing",
  ["a joke only","a long story","no greeting"],
  "Correspondence has a clear purpose.")
H('6.b.12.D',3,"Which opening fits a letter requesting information from a museum?",
  "I am writing to ask about your summer tour times.",
  ["Hey, what's up?","Give me tickets.","I don't like museums."],
  "A request letter states its purpose politely.")

# b.13
H('6.b.13.A',3,"To clarify a research question, a student can:",
  "make it more specific",
  ["make it vaguer","delete it","answer it with a guess"],
  "Clear questions guide research.")
H('6.b.13.A',3,"Which question is narrow enough for a short report?",
  "How do monarch butterflies migrate?",
  ["What is science?","What is everything about animals?","Why is life?"],
  "A focused question is researchable.")
H('6.b.13.B',3,"Developing a research plan with an adult means you:",
  "list steps, sources and deadlines",
  ["choose your favorite color","wait until the last day","avoid asking for help"],
  "Plans organize the work.")
H('6.b.13.B',3,"A deadline in a research plan tells you:",
  "when each step should be done",
  ["who the author is","how long a source is","which font to use"],
  "Deadlines schedule tasks.")
H('6.b.13.C',3,"Which source is likely best for facts about volcanoes?",
  "a science encyclopedia",
  ["a comic strip","a cookbook","a joke book"],
  "Relevant, reliable sources match the topic.")
H('6.b.13.C',3,"A reliable website for research often ends with:",
  ".gov or .edu",
  [".boo",".lol",".wow"],
  "Government and education sites tend to be reliable.")
H('6.b.13.D',3,"An interview with a person who lived through a hurricane is a:",
  "primary source",
  ["secondary source","dictionary","index"],
  "First-hand accounts are primary.")
H('6.b.13.D',3,"An encyclopedia article about a hurricane is a:",
  "secondary source",
  ["primary source","first-hand account","eyewitness"],
  "Secondary sources summarize other information.")
H('6.b.13.E',3,"Which note shows understanding of a source about owls?",
  "Owls hunt at night using sharp hearing.",
  ["Owls.","See page four.","Interesting."],
  "A meaningful note restates an idea.")
H('6.b.13.E',3,"Summarizing a source shows you can:",
  "state the main points briefly",
  ["copy every sentence","hide the topic","list page numbers"],
  "A summary is short and complete.")
H('6.b.13.F',3,"Which is plagiarism?",
  "Copying a paragraph word for word without credit",
  ["Putting an idea in your own words and citing the source","Quoting a sentence with quotation marks and a citation","Summarizing and naming the author"],
  "Plagiarism is taking others' words without credit.")
H('6.b.13.F',3,"A good paraphrase keeps the meaning but changes:",
  "the wording and sentence structure",
  ["the facts","the source's meaning","the topic"],
  "Paraphrase uses your own words.")
H('6.b.13.G',3,"A bibliography is a list of:",
  "sources used in research",
  ["words you misspelled","pages you skipped","jokes"],
  "It credits sources.")
H('6.b.13.G',3,"In a bibliography, entries are usually arranged:",
  "alphabetically by the author's last name",
  ["by page color","by length","randomly"],
  "Alphabetical order helps readers find sources.")
H('6.b.13.H',3,"A student presents research with a slide show and a short speech. The mode is:",
  "multimodal",
  ["silent only","written only","none"],
  "More than one mode is multimodal.")
H('6.b.13.H',2,"Which delivery is a written mode?",
  "a printed report",
  ["a speech","a skit","a song"],
  "Written delivery is on paper or screen text.")

# b.2
H('6.b.2.A.i',4,"Palabras sobresdrújulas are stressed:",
  "before the third-to-last syllable",
  ["on the last syllable","on the next-to-last syllable","on no syllable"],
  "Sobresdrújulas, like cómpramelo, have stress earlier than the antepenultimate syllable.")
H('6.b.2.A.i',3,"Which word is esdrújula?",
  "murciélago",
  ["mesa","jardín","café"],
  "Murciélago is stressed on the third-to-last syllable.")
H('6.b.2.A.ii',3,"How many syllables are in the word ciudad?",
  "2",
  ["1","3","4"],
  "Ciu-dad: iu forms a diphthong.")
H('6.b.2.A.ii',3,"Which word is divided correctly into syllables?",
  "ma-ri-po-sa",
  ["mar-i-po-sa","mari-po-sa","ma-rip-o-sa"],
  "Mariposa has four syllables.")
H('6.b.2.A.iii',3,"Which word means 'tea' and carries a diacritical accent?",
  "té",
  ["te","tè","tê"],
  "Té with an accent is tea; te is a pronoun.")
H('6.b.2.A.iii',3,"Why is dé (give) different from de (of)?",
  "the accent marks a different meaning",
  ["dé is longer","de is plural","dé is a noun only"],
  "A diacritical accent separates words that sound alike.")
H('6.b.2.A.iv',3,"The prefix sub- in the word submarino means:",
  "under",
  ["over","between","again"],
  "Sub- means under.")
H('6.b.2.A.iv',3,"The suffix -oso in the word peligroso means:",
  "full of",
  ["without","before","again"],
  "-oso means full of or characterized by.")
H('6.b.2.B.i',3,"Which spelling of the word for 'lesson' is correct?",
  "lección",
  ["leccion","lección","leción"],
  "Words ending in -ción take an accent on the o.")
H('6.b.2.B.i',3,"Which spelling of the word meaning 'never' ends in an accented á?",
  "jamás",
  ["jamas","jámas","jamâs"],
  "Jamás is stressed on the last syllable and ends in s.")
H('6.b.2.B.ii',3,"Which spelling is correct for the flying mammal stressed on the third-to-last syllable?",
  "murciélago",
  ["murcielago","murcielágo","murcíelago"],
  "Esdrújulas always carry a written accent.")
H('6.b.2.B.ii',3,"Esdrújulas such as plátano are marked with an accent because:",
  "they are stressed on the third-to-last syllable",
  ["they end in a vowel","they have two syllables","they start with p"],
  "All esdrújulas carry a written accent.")
H('6.b.2.B.iii',3,"Which spelling shows a hiatus in the word for 'to laugh'?",
  "reír",
  ["reir","réir","reiír"],
  "The accent on í keeps the vowels in separate syllables.")
H('6.b.2.B.iii',3,"Which spelling shows a diphthong with no accent?",
  "cuento",
  ["cuénto","cuentó","cüento"],
  "Ue is a diphthong and needs no accent here.")
H('6.b.2.B.iv',3,"Which spelling is correct for the first-person simple past of the verb meaning 'to sing'?",
  "canté",
  ["cante","cantè","cantê"],
  "Simple past yo form of -ar verbs takes an accent.")
H('6.b.2.B.iv',4,"Which spelling is correct for 'they were eating' in the imperfect (comer)?",
  "comían",
  ["comian","cómian","comiàn"],
  "The -ía endings carry an accent.")
H('6.b.2.C',2,"Cursive handwriting for assignments should be:",
  "legible, with consistent slant and spacing",
  ["tiny and crooked","printed only","as fast as possible"],
  "Legibility matters for assignments.")
H('6.b.2.C',2,"Writing legibly in cursive means that:",
  "a reader can easily read each letter",
  ["no one can read it","letters are decorated","letters touch the next line"],
  "Clear letters are legible.")

# b.3
H('6.b.3.A',2,"A digital dictionary can show you a word's:",
  "syllable breaks and audio pronunciation",
  ["price","author","weight"],
  "Digital resources give pronunciation and syllabication.")
H('6.b.3.A',2,"Which resource shows how to divide 'universidad' into syllables?",
  "a dictionary entry",
  ["a map","a calendar","a clock"],
  "Dictionaries show syllable breaks.")
H('6.b.3.B',3,"A word has several meanings. How do you choose the relevant meaning?",
  "read the surrounding sentences",
  ["pick the first meaning","skip the word","choose the longest definition"],
  "Context determines meaning.")
H('6.b.3.B',3,"She sat on the bank of the river. 'Bank' here means:",
  "land beside water",
  ["a place for money","a row of seats","to tilt a plane"],
  "Context shows the water-related meaning.")
H('6.b.3.C',3,"The prefix mono- in the word monólogo means:",
  "one",
  ["two","many","none"],
  "Mono- means one.")
H('6.b.3.C',3,"The prefix inter- in the word internacional means:",
  "between",
  ["under","over","after"],
  "Inter- means between or among.")
H('6.b.3.D',3,"Abrazar and abrasar sound alike but have different spellings. These words are:",
  "homophones",
  ["antonyms","synonyms","homographs"],
  "Homophones sound alike.")
H('6.b.3.D',4,"Which idiom means 'to be extremely happy'?",
  "estar en el séptimo cielo",
  ["estar bajo tierra","estar en la cocina","estar en el cuarto"],
  "The idiom means being on cloud nine.")
H('6.b.3.E',3,"The word bat for an animal and bat for baseball are:",
  "homographs",
  ["homophones","antonyms","synonyms"],
  "They are spelled alike with different meanings.")
H('6.b.3.E',3,"Commonly confused terms such as 'a ver' and 'haber' differ because:",
  "they sound alike but have different meanings",
  ["they are the same word","they have no meaning","they are both nouns"],
  "Sound-alike terms need careful spelling.")

# b.4 b.5
H('6.b.4',2,"Listening to a speech and then discussing it uses which skills?",
  "listening and speaking",
  ["writing and drawing","reading and tracing","spelling and counting"],
  "Language skills work together.")
H('6.b.4',2,"Why is it important to develop all four language skills?",
  "each skill strengthens the others",
  ["only one skill matters","they compete","they are unrelated"],
  "Skills grow together.")
H('6.b.5',2,"A student reads a news article, discusses it and writes a response. The student used:",
  "all four language skills",
  ["only reading","only writing","no skills"],
  "Listening, speaking, reading and writing combine.")
H('6.b.5',2,"Which activity combines listening and writing?",
  "taking notes during a talk",
  ["silent drawing","reading alone","singing"],
  "Notetaking links listening and writing.")

# b.6
H('6.b.6.A',2,"Setting a purpose before reading means:",
  "deciding why you are reading",
  ["counting the pages","choosing a pencil","finishing quickly"],
  "A purpose guides reading.")
H('6.b.6.A',2,"A purpose for reading an assigned science chapter might be:",
  "to answer questions about the water cycle",
  ["to find a fun font","to count paragraphs","to avoid vocabulary"],
  "Purposes connect to learning goals.")
H('6.b.6.B',3,"Which is a question to ask during reading?",
  "What does this word mean in this sentence?",
  ["What is for dinner?","Where did I put my shoes?","Who has the biggest desk?"],
  "Questions during reading monitor understanding.")
H('6.b.6.B',3,"Generating questions after reading helps you to:",
  "check and deepen understanding",
  ["forget the text","avoid rereading","skip the ending"],
  "Questions extend thinking.")
H('6.b.6.C',3,"Characteristics of genre can help you predict because:",
  "texts in a genre follow similar patterns",
  ["all genres are identical","genres have no patterns","genres hide the plot"],
  "Genre patterns suggest what comes next.")
H('6.b.6.C',3,"Reading a fairy tale, you predict a happy ending. You used:",
  "characteristics of the genre",
  ["the book's weight","the page count","the author's age"],
  "Fairy tales often end happily.")
H('6.b.6.D',3,"A mental image of a stormy night in a story helps you to:",
  "feel the mood of the scene",
  ["skip the scene","change the plot","forget the setting"],
  "Imagery deepens understanding.")
H('6.b.6.D',3,"Which sentence helps you picture a scene best?",
  "Golden light spilled across the quiet, dusty road.",
  ["It was there.","The road was.","Something happened."],
  "Sensory details create images.")
H('6.b.6.E',3,"A text-to-self connection links a text to:",
  "your own experience",
  ["another book","the news","a map"],
  "Self connections come from your life.")
H('6.b.6.E',3,"A character's courage makes you think of a historical hero you studied. That is a:",
  "text-to-world connection",
  ["text-to-self connection","spelling pattern","glossary entry"],
  "Connections to society and history are text-to-world.")
H('6.b.6.F',3,"A character yawns and rubs his eyes all through class. A good inference is that he:",
  "did not sleep well",
  ["won a prize","is cheerful","just finished lunch"],
  "Clues support the inference of tiredness.")
H('6.b.6.F',3,"To support an inference, a reader should cite:",
  "evidence from the text",
  ["a rumor","a guess","the cover"],
  "Inferences need text evidence.")
H('6.b.6.G',3,"Evaluating details means deciding which details:",
  "best support the key idea",
  ["are longest","are in bold only","come first"],
  "Key ideas are supported by important details.")
H('6.b.6.G',3,"Which is a key idea in an article titled 'Why Bees Matter'?",
  "Bees help plants grow by moving pollen.",
  ["The article has a photo.","Bees are small.","The title is short."],
  "A key idea carries the central point.")
H('6.b.6.H',3,"Synthesizing information means:",
  "combining ideas to build new understanding",
  ["copying the first source","skipping details","memorizing word lists"],
  "Synthesis builds new meaning.")
H('6.b.6.H',3,"After reading three texts about water safety, you write one rule using ideas from all of them. You:",
  "synthesized the information",
  ["ignored the texts","copied one text","guessed"],
  "Combining sources creates new understanding.")
H('6.b.6.I',3,"A reader monitors comprehension by:",
  "noticing when meaning breaks down",
  ["reading faster","ignoring confusion","skipping punctuation"],
  "Monitoring means checking understanding.")
H('6.b.6.I',3,"Which is a fix-up strategy for a hard text?",
  "reread and use background knowledge",
  ["stop at the first problem","guess the ending","skip every hard word forever"],
  "Fix-up strategies restore meaning.")

# b.7
H('6.b.7.A',2,"Describing how a story's setting reminds you of your hometown is:",
  "a personal connection",
  ["a summary","a caption","an index"],
  "Connections link text to life.")
H('6.b.7.A',2,"Personal connections can come from:",
  "self-selected texts you choose to read",
  ["no texts","only assigned tests","blank pages"],
  "Self-selected texts invite connections.")
H('6.b.7.B',3,"A response that compares two texts should tell:",
  "how they are alike and different",
  ["which has more pages","which is heavier","which has a better cover"],
  "Comparing and contrasting examines similarities and differences.")
H('6.b.7.B',3,"Contrasting two characters means showing:",
  "how they are different",
  ["how they are the same","only their names","their ages"],
  "Contrast shows differences.")
H('6.b.7.C',3,"To support a response, use evidence that is:",
  "taken from the text",
  ["invented","unrelated","from a different story"],
  "Evidence comes from the text.")
H('6.b.7.C',3,"Which is the best text evidence for 'Leo is determined'?",
  "Leo tried the puzzle ten times until he solved it.",
  ["Leo lives in Houston.","Leo has a puzzle.","Leo is in fourth grade."],
  "Evidence shows the trait through action.")
H('6.b.7.D',3,"A summary of a text should be:",
  "shorter than the text and keep its main ideas",
  ["longer than the text","full of new facts","unrelated to the text"],
  "Summaries are brief and accurate.")
H('6.b.7.D',3,"Which is a retelling in logical order?",
  "First, the team lost; then they practiced; finally they won.",
  ["Finally they won; first they practiced; the team lost.","They practiced; finally the team lost; first they won.","Won, lost, practiced, never."],
  "Retellings keep logical order.")
H('6.b.7.E',3,"Freewriting after reading is a way to:",
  "explore your thoughts about the text",
  ["avoid the text","edit spelling only","copy a page"],
  "Freewriting is a response strategy.")
H('6.b.7.E',3,"Annotating a text while reading can include:",
  "underlining key ideas and writing notes in the margin",
  ["tearing the page","erasing words","covering the title"],
  "Annotations record thinking.")
H('6.b.7.F',3,"A student learns the word 'determined' and writes: 'The determined girl practiced every day.' This is:",
  "using new vocabulary in a response",
  ["an index entry","a caption","a rhyme"],
  "Using new words shows learning.")
H('6.b.7.F',3,"Responding with newly acquired vocabulary shows:",
  "you can use new words correctly",
  ["you copied a dictionary","you skipped the reading","you disliked the text"],
  "Applying vocabulary shows understanding.")
H('6.b.7.G',3,"In a book talk, an important idea is one that:",
  "helps explain the meaning of the text",
  ["is only in the title","is about the cover","is the shortest sentence"],
  "Important ideas connect to the meaning.")
H('6.b.7.G',3,"To discuss specific ideas, you can:",
  "point to a page and explain it",
  ["talk about lunch","stay quiet","describe the cover only"],
  "Discussion is grounded in the text.")

# b.8
H('6.b.8.A',3,"A basic theme of a story about a boy who returns a lost wallet is:",
  "Honesty is important.",
  ["Wallets are leather.","Boys are tall.","Money is round."],
  "A theme is the message.")
H('6.b.8.A',3,"To infer a theme you use:",
  "text evidence about what characters learn",
  ["the number of pages","the first word","the font"],
  "Theme is supported by evidence.")
H('6.b.8.B',3,"A character begins shy but becomes brave by the end. This shows:",
  "a change the character undergoes",
  ["a change in setting only","a new author","a table of contents"],
  "Characters change through the story.")
H('6.b.8.B',3,"Interactions between characters can show:",
  "how their relationships affect the story",
  ["how long the book is","the price","the page count"],
  "Interactions drive the plot.")
H('6.b.8.C',3,"The highest point of tension in a plot is the:",
  "climax",
  ["exposition","title","resolution"],
  "The climax is the turning point.")
H('6.b.8.C',3,"Events after the climax that lead toward the end are the:",
  "falling action",
  ["rising action","title","exposition"],
  "Falling action follows the climax.")
H('6.b.8.D',3,"A story set in the Old West has a historical setting. This affects the plot because:",
  "characters face problems typical of that time",
  ["all stories take place today","setting never matters","time is not part of setting"],
  "Historical settings shape events.")
H('6.b.8.D',3,"A cultural setting, such as a village festival, influences the plot by:",
  "shaping the characters' traditions and choices",
  ["hiding the characters","removing the conflict","ending the story"],
  "Cultural setting shapes behavior and events.")

# b.9
H('6.b.9.A',3,"A myth is a traditional story that often:",
  "explains nature or beliefs",
  ["lists directions","gives a recipe","presents a timetable"],
  "Myths explain the world.")
H('6.b.9.A',3,"Which is a characteristic of a folktale?",
  "It was passed down by storytellers.",
  ["It has a bibliography.","It contains a graph.","It is a news report."],
  "Folktales come from oral tradition.")
H('6.b.9.B',3,"'The stars danced in the sky' is:",
  "personification",
  ["a simile","an index","a fact"],
  "Stars are given a human action.")
H('6.b.9.B',3,"'Her smile was sunshine' is a:",
  "metaphor",
  ["simile","hyperbole","fact"],
  "A metaphor says one thing is another.")
H('6.b.9.C',3,"In a script, character tags show:",
  "who is speaking",
  ["the setting only","the price","the page count"],
  "Tags label speakers.")
H('6.b.9.C',3,"Scenes and acts in a play:",
  "divide the action into parts",
  ["list the audience","name the director","give the theater address"],
  "Plays are divided into acts and scenes.")
H('6.b.9.D.i',3,"Supporting evidence for a central idea should be:",
  "facts and details from the text",
  ["personal feelings only","unrelated facts","a rhyme"],
  "Evidence supports the main point.")
H('6.b.9.D.i',3,"The central idea of an article on healthy sleep is:",
  "Good sleep helps the body and mind.",
  ["Beds have pillows.","Night is dark.","Clocks tick."],
  "The central idea is the main point.")
H('6.b.9.D.ii',3,"A pronunciation guide in a text helps readers:",
  "say a hard word correctly",
  ["find the author","spell the title","count the pages"],
  "Guides show how to say words.")
H('6.b.9.D.ii',3,"A diagram in an informational text:",
  "shows parts or how something works",
  ["tells a joke","rhymes","lists the author's name"],
  "Diagrams explain visually.")
H('6.b.9.D.iii',3,"A text that shows how two animals are alike and different uses:",
  "compare and contrast",
  ["cause and effect","sequence","description only"],
  "Compare and contrast shows similarities and differences.")
H('6.b.9.D.iii',3,"Words such as 'similarly' and 'in contrast' signal:",
  "compare and contrast",
  ["chronological order","problem and solution","cause and effect"],
  "These words show likeness and difference.")
H('6.b.9.E.i',3,"The claim of an argument is the author's:",
  "position on an issue",
  ["name","address","favorite color"],
  "The claim is the stance argued.")
H('6.b.9.E.i',3,"Which statement is a claim an author could argue?",
  "Every school should have a library.",
  ["The library has books.","Libraries are buildings.","I went to the library."],
  "Claims can be argued.")
H('6.b.9.E.ii',3,"An author uses facts in an argument to:",
  "make the claim more convincing",
  ["confuse readers","change the topic","replace the claim"],
  "Facts support claims.")
H('6.b.9.E.ii',3,"Which fact could support the claim 'Walking to school is healthy'?",
  "Walking helps the heart and builds strong muscles.",
  ["Some schools are big.","Buses are yellow.","Shoes come in sizes."],
  "Relevant facts support the claim.")
H('6.b.9.E.iii',3,"An ad with cartoons and bright colors for a cereal is aimed at:",
  "children",
  ["engineers","judges","pilots"],
  "Design shows the intended audience.")
H('6.b.9.E.iii',3,"To identify the intended audience, look at the author's:",
  "word choice and topic",
  ["page numbers","ink color","book size"],
  "Language and topic reveal the audience.")
H('6.b.9.F',3,"Which is a characteristic of a digital text?",
  "It can include links, audio and video.",
  ["It cannot be changed.","It has no words.","It must be on paper."],
  "Digital texts can be interactive.")
H('6.b.9.F',3,"A multimodal text uses:",
  "more than one way to communicate, such as text and images",
  ["only one font","only audio","only silence"],
  "Multimodal combines modes.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'sla_5.jsonl'))

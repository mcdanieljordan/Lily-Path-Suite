import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('128.', 1069, own='sla_4.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# a.7
H('5.a.7',3,"Why does learning to read in Spanish help a student learn to read in English?",
  "Many literacy skills transfer between the two languages",
  ["The two languages share no skills","Reading in one language erases the other","Only spelling is shared"],
  "Skills such as decoding, comprehension and vocabulary strategies carry over between languages.")
H('5.a.7',3,"Research on second language acquisition says that students learn best when language lessons are:",
  "connected to reading, writing, listening and speaking",
  ["separated from all other skills","limited to memorizing lists","taught only through silent copying"],
  "Language is learned through meaningful use across all four skills.")

# b.1 listening and speaking
H('5.b.1.A',2,"Active listeners ask relevant questions to:",
  "clarify information",
  ["change the subject","interrupt the speaker","tease a classmate"],
  "Relevant questions make the speaker's meaning clearer.")
H('5.b.1.A',3,"Which is a pertinent comment during a class discussion about a story?",
  "I agree with Mia because her example matched the text.",
  ["I like pizza.","Can I get a drink of water?","What time is lunch?"],
  "A pertinent comment connects to the topic and to what others said.")
H('5.b.1.B',2,"To restate directions you were given, you:",
  "say them again in your own words",
  ["ignore the first step","guess what comes next","repeat only the last word"],
  "Restating shows you understood the series of steps.")
H('5.b.1.B',3,"When you give oral instructions with several steps, you should:",
  "say them in order with clear signal words",
  ["mix up the order","skip the hard steps","whisper so no one hears"],
  "Related sequences of instructions need a clear order.")
H('5.b.1.C',3,"Speaking coherently about a topic includes:",
  "staying on topic with a clear voice and eye contact",
  ["looking at the floor and mumbling","talking in a rush","jumping to new topics"],
  "Coherent speakers use eye contact, rate and volume to keep listeners with them.")
H('5.b.1.C',2,"A speaker who looks at the audience is showing that they:",
  "are engaging the listeners",
  ["forgot the topic","are bored","are lost"],
  "Eye contact helps hold the audience's attention.")
H('5.b.1.D',2,"Agreed-upon discussion rules help a group:",
  "work well together",
  ["finish faster by talking over others","avoid every new idea","ignore teammates"],
  "Rules, norms and protocols make teamwork fair and productive.")
H('5.b.1.D',2,"A protocol for sharing ideas in a group could be to:",
  "raise a hand and wait your turn",
  ["shout out answers","leave the group","talk the whole time"],
  "Taking turns follows agreed-upon group norms.")
H('5.b.1.E',2,"Conversing politely in all situations includes:",
  "saying please and thank you",
  ["interrupting often","ignoring greetings","teasing others"],
  "Polite social communication shows respect.")
H('5.b.1.E',3,"When you disagree with a classmate politely, you might say:",
  "I see it differently because of this detail.",
  ["That is a dumb idea.","Be quiet.","You are wrong and I am right."],
  "Polite disagreement gives a reason without insulting anyone.")

# b.10 author's craft
H('5.b.10.A',2,"A news article explains how a new bridge was built. The author's purpose is to:",
  "inform",
  ["scare","tease","sing"],
  "Informational articles are written to give facts.")
H('5.b.10.A',2,"An author writes a funny tale about a clumsy robot. The author's purpose is mainly to:",
  "entertain",
  ["give directions","sell a product","teach a science process"],
  "Humorous stories are written to entertain readers.")
H('5.b.10.B',3,"An author tells events in time order. This text structure helps the reader:",
  "follow what happened first, next and last",
  ["find rhyming words","see opposite meanings","learn spelling rules"],
  "Chronological structure supports understanding of a sequence of events.")
H('5.b.10.B',3,"A text describes a problem and then ways to fix it. The structure helps the author:",
  "show how the problem can be solved",
  ["list opposite words","count syllables","spell names"],
  "Problem and solution structure supports the author's purpose of explaining solutions.")
H('5.b.10.C',2,"A heading in an article helps the reader:",
  "see what a section is about",
  ["count the pages","find rhymes","know who printed it"],
  "Headings are print features that organize information.")
H('5.b.10.C',3,"A photograph with a caption is a graphic feature that:",
  "adds details to the words",
  ["removes the topic","spells hard words","lists the author's pets"],
  "Graphics and captions give extra information.")
H('5.b.10.D',3,"Which sentence has a simile?",
  "The runner was as fast as lightning.",
  ["The runner was fast.","The runner ran home.","Lightning struck."],
  "A simile compares two things using as or like.")
H('5.b.10.D',3,"'The classroom was a zoo' is an example of a:",
  "metaphor",
  ["simile","fact","rhyme"],
  "A metaphor says one thing is another without using like or as.")
H('5.b.10.E',3,"A narrator who says 'I' and 'we' tells the story from:",
  "first-person point of view",
  ["third-person point of view","second-person point of view","no point of view"],
  "First-person narrators use I and we.")
H('5.b.10.E',3,"'She looked out the window while he cooked' is told from:",
  "third-person point of view",
  ["first-person point of view","second-person point of view","a poem's point of view"],
  "Third-person narrators use she, he and they.")
H('5.b.10.F',3,"An author's voice is shown by:",
  "word choice and style that sound unique",
  ["page numbers","paper color","the index"],
  "Voice is the personality in the author's language.")
H('5.b.10.F',3,"Which sentence shows a playful voice?",
  "My brother snores like a grumpy bear in a cave!",
  ["Brother sleeps.","The man slept.","He is asleep."],
  "Humor and vivid comparison create voice.")
H('5.b.10.G',3,"Which sentence uses hyperbole?",
  "I have told you a million times to clean up!",
  ["I told you to clean up.","Please clean up.","You cleaned your room."],
  "Hyperbole exaggerates for effect.")
H('5.b.10.G',3,"Hyperbole is:",
  "extreme exaggeration for effect",
  ["a comparison using like","a repeated sound","a true fact"],
  "Hyperbole is not meant to be taken literally.")

# b.11 writing process
H('5.b.11.A',3,"When planning a first draft, the genre you choose depends on:",
  "your topic, purpose and audience",
  ["the weight of your pencil","the color of your paper","today's date"],
  "Writers choose a genre to fit topic, purpose and audience.")
H('5.b.11.A',2,"A graphic organizer such as a web helps a writer:",
  "plan and group ideas before drafting",
  ["publish the draft","edit spelling at the end only","print the title"],
  "Planning tools organize ideas first.")
H('5.b.11.B.i',3,"Which part of an essay wraps up the main idea at the end?",
  "the conclusion",
  ["the title","the heading","the caption"],
  "A purposeful structure ends with a conclusion.")
H('5.b.11.B.i',3,"An introduction should:",
  "get the reader's attention and name the topic",
  ["end the essay","list every detail","repeat the conclusion"],
  "The introduction opens the piece and states what it is about.")
H('5.b.11.B.ii',3,"Which detail fits a paragraph about why dogs make good pets?",
  "Dogs are loyal and love to play.",
  ["Cats have whiskers.","Fish live in water.","Cars have wheels."],
  "Relevant details support the idea.")
H('5.b.11.B.ii',3,"To make a writing idea engaging, a writer can add:",
  "vivid details that fit the topic",
  ["unrelated facts","extra blank spaces","repeated sentences"],
  "Engaging ideas use relevant, interesting details.")
H('5.b.11.C',3,"Combining two short, choppy sentences into one is a revision for:",
  "sentence structure",
  ["handwriting","margins","the title"],
  "Combining sentences improves how sentences flow.")
H('5.b.11.C',2,"Replacing the word 'nice' with 'friendly' improves:",
  "word choice",
  ["page length","margins","handwriting"],
  "A more precise word improves word choice.")
H('5.b.11.D.i',3,"Which Spanish sentence agrees in number between the subject and the verb?",
  "Los niños juegan afuera.",
  ["Los niños juega afuera.","El niño juegan afuera.","Los niño juega afuera."],
  "A plural subject takes a plural verb.")
H('5.b.11.D.i',3,"A compound sentence joins:",
  "two complete thoughts with a conjunction",
  ["two fragments with no verb","two titles","two periods"],
  "Compound sentences combine independent clauses.")
H('5.b.11.D.ii',4,"Which sentence is in the imperfect past?",
  "Cuando era niña, jugaba en el parque.",
  ["Mañana jugaré en el parque.","Hoy juego en el parque.","Ayer jugué en el parque."],
  "Jugaba shows a repeated or ongoing action in the past.")
H('5.b.11.D.ii',4,"In 'Ella ha comido', the verb phrase ha comido is in the:",
  "present perfect, using a past participle",
  ["future tense","simple present","command form"],
  "Haber plus a past participle forms a perfect tense.")
H('5.b.11.D.iii',3,"Which pair uses the correct gender-specific articles?",
  "la casa, el libro",
  ["el casa, la libro","la casa, la libro","el casa, el libro"],
  "Casa is feminine and libro is masculine.")
H('5.b.11.D.iii',2,"Which noun is plural?",
  "mariposas",
  ["mariposa","libro","ciudad"],
  "Plural nouns commonly end in -s.")
H('5.b.11.D.iv',3,"Which sentence uses a comparative?",
  "Mi perro es más grande que tu perro.",
  ["Mi perro es grande.","Mi perro es el más grande de todos.","Mi perro corre."],
  "Más plus que compares two things.")
H('5.b.11.D.iv',3,"'El más alto de la clase' is a:",
  "superlative",
  ["comparative","verb","preposition"],
  "A superlative names the highest degree in a group.")
H('5.b.11.D.v',3,"Which adverb tells how an action is done (manner)?",
  "rápidamente",
  ["ayer","mañana","hoy"],
  "Adverbs ending in -mente often show manner.")
H('5.b.11.D.v',3,"Which adverb tells when (time)?",
  "después",
  ["despacio","bien","fuerte"],
  "Después means afterward.")
H('5.b.11.D.vi',3,"Which word is a preposition?",
  "sobre",
  ["correr","feliz","rápido"],
  "Sobre means on or about and begins prepositional phrases.")
H('5.b.11.D.vi',3,"A prepositional phrase begins with a preposition and ends with:",
  "a noun or pronoun",
  ["a verb","a period only","an adjective only"],
  "The object of the preposition is a noun or pronoun.")
H('5.b.11.D.vii',3,"Which pronoun fits: Yo ___ lavo las manos?",
  "me",
  ["te","se","le"],
  "Me is the reflexive pronoun that matches yo.")
H('5.b.11.D.vii',3,"Which word shows who owns the book?",
  "mi",
  ["al","por","sin"],
  "Mi is a possessive word meaning my.")
H('5.b.11.D.viii',3,"The word 'pero' in 'Quiero ir, pero llueve' joins:",
  "two complete thoughts into one sentence",
  ["two titles","two numbers","two syllables"],
  "Coordinating conjunctions can form compound sentences.")
H('5.b.11.D.viii',3,"A compound subject is:",
  "two or more subjects sharing one verb",
  ["one subject with two verbs","a verb with no subject","a title with a subject"],
  "Conjunctions can join subjects.")
H('5.b.11.D.ix',2,"Which word should start with a capital letter?",
  "México",
  ["ciudad","país","estado"],
  "Names of countries are proper nouns.")
H('5.b.11.D.ix',3,"Which name of a historical event should be capitalized?",
  "la Revolución Mexicana",
  ["la fiesta","la comida","el recreo"],
  "Historical period and event names are capitalized.")
H('5.b.11.D.x',3,"Which sentence uses commas in a series correctly?",
  "Compré manzanas, peras y uvas.",
  ["Compré, manzanas peras y uvas.","Compré manzanas peras, y uvas.","Compré manzanas, peras, y, uvas."],
  "Commas separate items in a series.")
H('5.b.11.D.x',3,"Which date is punctuated correctly?",
  "Monday, May 5, 2025",
  ["Monday May, 5 2025","Monday, May 5 2025","Monday May 5, 2025,"],
  "Use a comma after the day of the week and between the day and year.")
H('5.b.11.D.xi',3,"Which spelling names the farm animal that gives wool?",
  "oveja",
  ["obeja","ovexa","ovega"],
  "Oveja is spelled with v and j.")
H('5.b.11.D.xi',3,"Which spelling names the number between nine and eleven?",
  "diez",
  ["dies","diés","diéz"],
  "Diez ends in z.")
H('5.b.11.E',2,"Publishing written work means:",
  "sharing a final copy with an audience",
  ["starting a rough draft","erasing your plan","tearing the page"],
  "Publishing presents polished writing to readers.")
H('5.b.11.E',2,"Which is a way to publish a story for classmates?",
  "posting a clean final copy on a bulletin board",
  ["hiding the paper in a desk","tearing it up","leaving it blank"],
  "Posting or reading a final copy shares the work.")

# b.12 composing
H('5.b.12.A',2,"Personal narratives are written from the author's:",
  "own real experience",
  ["recipe","map","dictionary"],
  "A personal narrative tells about the writer's own life.")
H('5.b.12.A',3,"Poetry often uses:",
  "line breaks and sound devices",
  ["tables of data","numbered steps","footnotes only"],
  "Poems use lines, rhythm and sound.")
H('5.b.12.B',3,"A brief informational composition should include:",
  "a main idea supported by facts",
  ["only opinions","only dialogue","only rhymes"],
  "Informational writing explains with facts.")
H('5.b.12.B',3,"Which sentence best begins an informational composition about owls?",
  "Owls are birds that hunt at night.",
  ["I like my pillow.","Once there was a dragon.","Buy owls today!"],
  "A topic sentence states the subject with a fact.")
H('5.b.12.C',3,"An opinion essay should state:",
  "a claim and reasons that support it",
  ["only a list of rhymes","only a title","only a drawing"],
  "Argumentative texts need a claim and reasons.")
H('5.b.12.C',3,"Which reason supports the claim 'Our class should have a garden'?",
  "Plants teach students how living things grow.",
  ["Gardens are green.","I have a shirt.","Today is Monday."],
  "A reason connects directly to the claim.")
H('5.b.12.D',2,"A thank-you note usually includes:",
  "a greeting, the reason for thanks and a closing",
  ["only a title","a recipe","a map"],
  "Correspondence has a greeting, body and closing.")
H('5.b.12.D',2,"Which closing fits a friendly letter?",
  "Your friend, Ana",
  ["The end","Page two","Chapter one"],
  "Letters end with a closing and signature.")

# b.13 research
H('5.b.13.A',2,"Which is a good research question?",
  "How do bees make honey?",
  ["Bees.","Honey is yellow.","Stop."],
  "Research questions ask something that sources can answer.")
H('5.b.13.A',3,"A good inquiry question should be:",
  "open enough to need research to answer",
  ["answerable with one word","already answered","unrelated to the topic"],
  "Good questions lead to investigation.")
H('5.b.13.B',3,"Following a research plan with adult assistance means you:",
  "work through your steps and check them with an adult",
  ["skip the steps","hide the plan","let the adult research alone"],
  "A plan guides steps and adult help keeps you on track.")
H('5.b.13.B',3,"Which belongs in a research plan?",
  "a list of questions, sources and a due date",
  ["a list of favorite colors","a recipe","a cartoon"],
  "Plans list what to ask, where to look and when.")
H('5.b.13.C',3,"A variety of sources includes:",
  "books, websites and interviews",
  ["only one book","only a rumor","only your guess"],
  "Using several kinds of sources makes research stronger.")
H('5.b.13.C',3,"To gather relevant information you should:",
  "choose facts that answer your research question",
  ["copy every page","skip all sources","use facts about other topics"],
  "Relevant facts match the question.")
H('5.b.13.D',3,"A diary written by a soldier during a war is a:",
  "primary source",
  ["secondary source","glossary","index"],
  "A first-hand record from the time is primary.")
H('5.b.13.D',3,"A textbook that summarizes a war years later is a:",
  "secondary source",
  ["primary source","diary entry","photograph from that day"],
  "Secondary sources are written after the event by someone not there.")
H('5.b.13.E',3,"To show understanding of gathered information you can:",
  "explain it in your own words",
  ["copy it exactly","hide it","count the letters"],
  "Restating shows understanding.")
H('5.b.13.E',3,"Which is the best way to show you understood an article?",
  "Write a summary using key facts.",
  ["Copy the title.","Leave it blank.","Count the words."],
  "A summary shows that you grasped the main points.")
H('5.b.13.F',3,"Paraphrasing means:",
  "restating ideas in your own words and naming the source",
  ["copying and saying it is yours","skipping sources","changing one word only"],
  "Paraphrasing is allowed when the source is credited.")
H('5.b.13.F',3,"Copying someone's words without giving credit is:",
  "plagiarism",
  ["paraphrasing","citing","summarizing"],
  "Plagiarism is using others' work as your own.")
H('5.b.13.G',3,"A works cited page lists:",
  "the sources you used",
  ["your favorite books","your grades","unused ideas"],
  "It gives credit to the sources.")
H('5.b.13.G',3,"A works cited entry usually begins with the:",
  "author's name",
  ["page color","your name","today's weather"],
  "Most entries start with the author.")
H('5.b.13.H',2,"Presenting research with a poster and a talk uses:",
  "a multimodal delivery",
  ["no delivery","a silent report only","a hidden draft"],
  "Mixing written and oral modes is multimodal.")
H('5.b.13.H',2,"Which is an oral way to present results?",
  "giving a short speech",
  ["writing a letter","printing a list","drawing a silent map"],
  "Oral delivery is spoken.")

# b.2 decoding and spelling
H('5.b.2.A.i',3,"Which word has a written accent mark (an orthographic accent)?",
  "teléfono",
  ["mesa","libro","casa"],
  "Teléfono is stressed on the third-to-last syllable and carries an accent.")
H('5.b.2.A.i',3,"In the word café, the stress falls on the:",
  "last syllable",
  ["first syllable","no syllable","middle of a letter"],
  "The accent mark is over the last vowel, so it is stressed.")
H('5.b.2.A.ii',3,"Which letter makes the /s/ sound in the word cena?",
  "the letter c",
  ["the letter k","the letter q","the letter h"],
  "C before e or i can sound like s.")
H('5.b.2.A.ii',3,"Which word starts with the /k/ sound?",
  "queso",
  ["cielo","zapato","sopa"],
  "Qu before e makes the /k/ sound.")
H('5.b.2.A.iii',3,"Which word begins with a silent letter?",
  "hermano",
  ["mano","tío","rana"],
  "The letter h is silent in Spanish.")
H('5.b.2.A.iii',3,"In the word guitarra, how is the u treated?",
  "It is silent.",
  ["It sounds like w.","It sounds like b.","It sounds like f."],
  "In gui the u is silent.")
H('5.b.2.A.iv',3,"In which word do two vowels share one syllable?",
  "ciudad",
  ["feo","país","leer"],
  "Ciudad has the diphthong iu in one syllable.")
H('5.b.2.A.iv',3,"A strong vowel next to another strong vowel forms:",
  "a hiatus",
  ["a diphthong","a digraph","a prefix"],
  "Two strong vowels are pronounced in separate syllables.")
H('5.b.2.A.v',3,"Sí, quiero helado means:",
  "Yes, I want ice cream.",
  ["If I want ice cream.","Whether I want ice cream.","No ice cream for me."],
  "Sí with an accent means yes.")
H('5.b.2.A.v',3,"Why are mas and más spelled differently?",
  "The accent shows a different meaning, but versus more.",
  ["They are the same word.","Más is shorter.","Accents are only decoration."],
  "A diacritical accent separates words that sound alike.")
H('5.b.2.A.vi',3,"The prefix des- in deshacer means:",
  "to undo",
  ["again","very","before"],
  "Des- reverses the action.")
H('5.b.2.A.vi',3,"The suffix -mente in rápidamente makes the word an:",
  "adverb",
  ["noun","verb","article"],
  "-mente forms adverbs of manner.")
H('5.b.2.B.i',3,"Which spelling needs a written accent because it ends in n and is stressed on the last syllable?",
  "camión",
  ["camion","cámion","camíon"],
  "Agudas ending in n, s or a vowel take an accent.")
H('5.b.2.B.i',3,"Which word is grave (stress on the next-to-last syllable) and needs no accent because it ends in a vowel?",
  "mesa",
  ["café","sofá","jamás"],
  "Graves ending in a vowel, n or s need no accent.")
H('5.b.2.B.ii',3,"Which spelling is correct for a word stressed on the third-to-last syllable?",
  "pájaro",
  ["pajaro","pajáro","pajarô"],
  "Esdrújulas always carry a written accent.")
H('5.b.2.B.ii',3,"Palabras esdrújulas, like música, are words that:",
  "always carry a written accent",
  ["never carry a written accent","are stressed on the last syllable","end only in n or s"],
  "Stress on the antepenultimate syllable is always marked.")
H('5.b.2.B.iii',3,"Which spelling shows the hiatus in the word for a male relative, uncle?",
  "tío",
  ["tio","tîo","tiyo"],
  "The accent on í breaks the diphthong into a hiatus.")
H('5.b.2.B.iii',3,"In the word cuidado, the vowels ui:",
  "stay together in one syllable",
  ["split into two syllables","need an accent","are silent"],
  "Ui is a diphthong.")
H('5.b.2.B.iv',3,"Which question is written correctly?",
  "¿Dónde vives?",
  ["¿Donde vives?","¿Dónde vives","Dónde vives?"],
  "Question words carry accents and the question uses ¿ and ?.")
H('5.b.2.B.iv',3,"In ¿Cómo te llamas?, the word cómo has an accent because it:",
  "asks a question",
  ["ends the sentence","names a person","is a verb"],
  "Interrogatives carry a written accent.")
H('5.b.2.B.ix',3,"Which word begins with a hard r sound?",
  "rana",
  ["pera","caro","toro"],
  "R at the start of a word is trilled.")
H('5.b.2.B.ix',3,"Between two vowels, the strong trilled sound is spelled with:",
  "a double letter rr",
  ["a single letter r","the letters rh","the letters rl"],
  "Perro uses rr for the strong sound.")
H('5.b.2.B.v',3,"Which spelling means 'I know'?",
  "sé",
  ["se","sè","sê"],
  "Sé with an accent is the verb saber.")
H('5.b.2.B.v',3,"In Spanish, the pronoun meaning 'he' is spelled:",
  "él",
  ["el","èl","ël"],
  "The accent separates él from the article el.")
H('5.b.2.B.vi',3,"Which spelling is correct for 'he ate' (comer, simple past)?",
  "comió",
  ["comio","cómio","comiô"],
  "Simple past forms ending in a stressed vowel take an accent.")
H('5.b.2.B.vi',4,"Which spelling is correct for 'we used to sing' in the imperfect past?",
  "cantábamos",
  ["cantabamos","cantabámos","cántabamos"],
  "Nosotros imperfect forms of -ar verbs take an accent on the á.")
H('5.b.2.B.vii',3,"Which word is spelled correctly with a silent h?",
  "hormiga",
  ["ormiga","jormiga","hormigga"],
  "Hormiga begins with a silent h.")
H('5.b.2.B.vii',3,"Which spelling has the /ge/ sound correctly?",
  "guerra",
  ["gerra","juerra","guerrra"],
  "Gue has a silent u to keep the hard g.")
H('5.b.2.B.viii',3,"Which spelling names a road in a town?",
  "calle",
  ["caye","cayle","calye"],
  "Calle is spelled with ll.")
H('5.b.2.B.viii',3,"Which spelling names the yolk of an egg?",
  "yema",
  ["llema","jema","iema"],
  "Yema begins with y.")
H('5.b.2.B.x',3,"Which spelling of the word for 'also' follows the rule of m before b?",
  "también",
  ["tanbién","tamvién","tanvién"],
  "Use m before b.")
H('5.b.2.B.x',3,"Which spelling of the word for 'winter' follows the rule of n before v?",
  "invierno",
  ["imvierno","inbierno","imbierno"],
  "Use n before v.")
H('5.b.2.B.xi',3,"Which word contains a consonant blend such as tr?",
  "tren",
  ["casa","mesa","luna"],
  "Tren begins with the blend tr.")
H('5.b.2.B.xi',3,"Which spelling of the word for a bound set of pages with a blend is correct?",
  "libro",
  ["lirbo","liro","libbro"],
  "Libro has the blend br.")
H('5.b.2.B.xii',3,"The plural of luz is:",
  "luces",
  ["luzes","luzs","lucez"],
  "Change z to c before adding -es.")
H('5.b.2.B.xii',3,"The plural of lápiz is:",
  "lápices",
  ["lápizes","lápizs","lapices"],
  "Change z to c and add -es.")
H('5.b.2.C',2,"To alphabetize tiza, tigre and tina, which letter position decides the order?",
  "the third letter",
  ["the first letter","the last letter","the word length"],
  "All three share t and i, so compare the third letters.")
H('5.b.2.C',3,"Which list is in alphabetical order to the third letter?",
  "cana, cano, casa",
  ["casa, cana, cano","cano, cana, casa","casa, cano, cana"],
  "N comes before s, and a comes before o.")
H('5.b.2.D',2,"Legible cursive means:",
  "others can read your letters",
  ["letters are as tiny as possible","letters slant in every direction","words touch each other"],
  "Legibility is the goal of handwriting.")
H('5.b.2.D',2,"In cursive writing, the space between words should be:",
  "about the width of one letter",
  ["none at all","as wide as a line","different every time"],
  "Appropriate spacing keeps words separate.")

# b.3 vocabulary
H('5.b.3.A',2,"Which dictionary feature helps you say a word aloud?",
  "the pronunciation guide",
  ["the page number","the word count","the cover title"],
  "Entries show pronunciation and syllable breaks.")
H('5.b.3.A',2,"A dictionary shows syllabication so you can:",
  "divide the word into syllables",
  ["change the meaning","shorten the word","find the author"],
  "Syllable breaks help with decoding and spelling.")
H('5.b.3.B',3,"Reading the sentences before and after a hard word gives you:",
  "clues to its meaning",
  ["its spelling only","the author's age","the page number"],
  "Context beyond the sentence can define a word.")
H('5.b.3.B',3,"The cat is ágil. It jumps over fences quickly. What does ágil most likely mean?",
  "quick and graceful",
  ["slow and sleepy","very hungry","very old"],
  "Context shows the cat moves quickly.")
H('5.b.3.C',3,"The prefix in- in the word incapaz means:",
  "not",
  ["again","before","above"],
  "In- can mean not.")
H('5.b.3.C',3,"The suffix -dad in bondad forms a noun meaning:",
  "the quality of being good",
  ["a person who is good","a place for good things","very good"],
  "-dad makes nouns for qualities.")
H('5.b.3.D',3,"Which pair of words are antonyms?",
  "alto and bajo",
  ["grande and enorme","bonito and lindo","rápido and veloz"],
  "Antonyms have opposite meanings.")
H('5.b.3.D',4,"The idiom 'tomar el pelo' means:",
  "to joke with or tease someone",
  ["to take hair","to wash hair","to cut hair"],
  "An idiom's meaning is not literal.")
H('5.b.3.E',3,"Which pair sounds the same but has different spellings?",
  "tubo and tuvo",
  ["casa and cosa","pato and pata","mesa and masa"],
  "Words that sound alike with different spellings are homophones.")
H('5.b.3.E',3,"A homograph is a word that:",
  "is spelled the same but has different meanings",
  ["sounds the same and means the same","has an opposite meaning","rhymes with other words"],
  "Homographs share spelling but not meaning.")

# b.4 b.5 foundational skills
H('5.b.4',2,"Practicing listening and speaking helps reading and writing because:",
  "the language skills support each other",
  ["they are unrelated","only reading matters","only speaking counts"],
  "Foundational language skills develop together.")
H('5.b.4',2,"A student listens to a story and then writes a summary. Which two skills worked together?",
  "listening and writing",
  ["speaking and drawing","reading and tracing","singing and counting"],
  "Skills are combined in real tasks.")
H('5.b.5',2,"Which activity builds both reading and speaking?",
  "reading a story aloud with a partner and discussing it",
  ["silent coloring","copying a menu","sorting buttons"],
  "Reading aloud and discussion combine skills.")
H('5.b.5',2,"A student can strengthen second-language skills by:",
  "using the language in all four skill areas daily",
  ["avoiding practice","only memorizing lists","only listening for years"],
  "Regular use of listening, speaking, reading and writing builds fluency.")

# b.6 reading comprehension
H('5.b.6.A',2,"A purpose for reading a science article could be:",
  "to learn facts about a topic",
  ["to count the commas","to avoid the title","to find the longest word"],
  "Readers set a purpose before reading.")
H('5.b.6.A',2,"Choosing a book on your own to read for fun makes it a:",
  "self-selected text",
  ["assigned text","restricted text","backward text"],
  "Self-selected texts are chosen by the reader.")
H('5.b.6.B',3,"Which question deepens understanding before reading?",
  "What do I already know about this topic?",
  ["How many pages are left?","Where is my backpack?","Who can read faster?"],
  "Pre-reading questions activate prior knowledge.")
H('5.b.6.B',3,"After reading, a good question to ask is:",
  "How did the main character change?",
  ["What time is it?","Where is the dictionary?","Who is sitting next to me?"],
  "Questions after reading deepen comprehension.")
H('5.b.6.C',3,"Using the title and pictures to guess what a text is about is:",
  "making a prediction",
  ["alphabetizing","summarizing the end","editing"],
  "Predictions use text features.")
H('5.b.6.C',3,"You predicted a happy ending but the story ended sadly. The best move is to:",
  "correct your prediction using the text",
  ["ignore the ending","reread nothing","blame the author"],
  "Readers confirm or correct predictions with evidence.")
H('5.b.6.D',2,"Picturing a story scene in your mind helps you to:",
  "understand details better",
  ["skip words","ignore the plot","read without thinking"],
  "Mental images deepen understanding.")
H('5.b.6.D',2,"Which words help you create a mental image?",
  "sparkling blue waves crashing on the shore",
  ["and then","the of it","it was there"],
  "Descriptive details support imagery.")
H('5.b.6.E',3,"When a story reminds you of another book, you are making a:",
  "text-to-text connection",
  ["text-to-self connection","spelling rule","caption"],
  "Connections can link texts to other texts.")
H('5.b.6.E',3,"A story about recycling reminds you of a news report about trash. That is a:",
  "text-to-world connection",
  ["text-to-self connection","glossary entry","rhyming pattern"],
  "Connections can link texts to society.")
H('5.b.6.F',3,"The text says Mia slammed the door and stomped upstairs. You can infer she is:",
  "angry",
  ["sleepy","thrilled","lost"],
  "Actions give clues about feelings.")
H('5.b.6.F',3,"An inference combines text evidence with:",
  "what you already know",
  ["a random guess","the page number","the book's weight"],
  "Inferences use clues plus background knowledge.")
H('5.b.6.G',3,"Which detail is most important in a paragraph about how bees make honey?",
  "Bees collect nectar and turn it into honey.",
  ["The paragraph has five sentences.","Some bees are yellow.","The page is near the back."],
  "Key ideas are the details that carry the main point.")
H('5.b.6.G',3,"Evaluating details helps you find the:",
  "key idea",
  ["font size","publisher","page count"],
  "Weighing details reveals what matters most.")
H('5.b.6.H',3,"Combining facts from two articles to build a new idea is:",
  "synthesizing",
  ["skimming","decoding","scanning"],
  "Synthesis creates new understanding.")
H('5.b.6.H',3,"After reading about frogs in a book and in a video, you write one new conclusion. You are:",
  "synthesizing information",
  ["copying a page","skipping details","spelling words"],
  "Merging sources into a new conclusion is synthesis.")
H('5.b.6.I',3,"Your comprehension drops in the middle of a chapter. A fix-up strategy is to:",
  "re-read the confusing part",
  ["close the book for good","skip to the last page","read faster"],
  "Monitoring means adjusting when you do not understand.")
H('5.b.6.I',3,"Using what you already know about a topic to understand a hard paragraph is:",
  "using background knowledge",
  ["guessing blindly","skipping the paragraph","memorizing letters"],
  "Background knowledge is a comprehension strategy.")

# b.7 response
H('5.b.7.A',2,"Telling how a character's move reminds you of your own is:",
  "a personal connection",
  ["a rhyme scheme","a glossary term","a table of contents"],
  "Personal connections link texts to your life.")
H('5.b.7.A',2,"Which sentence describes a personal connection?",
  "This reminds me of when I moved to a new school.",
  ["The book has ten chapters.","The author lives in Texas.","The cover is blue."],
  "A personal connection links the text to your experience.")
H('5.b.7.B',3,"A strong written response to a text:",
  "shows you understood the main points",
  ["repeats the title only","lists unrelated facts","has no details"],
  "Responses demonstrate understanding.")
H('5.b.7.B',3,"Which opening for a response shows understanding?",
  "The story is mostly about a girl who learns to be brave.",
  ["The story is long.","I did not read it.","It has pictures."],
  "A response names the main idea.")
H('5.b.7.C',3,"Which detail is text evidence that Ana is generous?",
  "Ana gave half her lunch to a classmate.",
  ["Ana is in third grade.","Ana has a brother.","Ana likes the color green."],
  "Evidence is a detail from the text that supports a claim.")
H('5.b.7.C',3,"Strong text evidence is:",
  "a detail taken from the text",
  ["a guess","a feeling alone","an unrelated fact"],
  "Evidence comes from the text itself.")
H('5.b.7.D',3,"Which sentence paraphrases 'The tiny pup trembled in the cold'?",
  "The small puppy shook because it was chilly.",
  ["The huge dog jumped in the sun.","The pup trembled in the cold.","The cat slept."],
  "A paraphrase keeps the meaning in new words.")
H('5.b.7.D',3,"A retelling that keeps logical order tells the events in:",
  "the beginning, middle and end",
  ["only the last page","the title and nothing else","middle first, then beginning"],
  "Retelling maintains order.")
H('5.b.7.E',2,"Annotating a text means:",
  "marking it and writing notes on it",
  ["erasing it","covering it","tearing the pages"],
  "Annotation is interaction with a source.")
H('5.b.7.E',2,"Which is a way to interact with a source?",
  "taking notes while reading",
  ["closing it unread","hiding it","turning it upside down"],
  "Notetaking is meaningful interaction.")
H('5.b.7.F',3,"The class learned the word 'curious'. Which sentence uses it?",
  "The curious puppy sniffed every corner.",
  ["The curious is a table.","Curious curious curious.","A curious of four."],
  "Use new vocabulary correctly in context.")
H('5.b.7.F',3,"Using newly learned words in your response shows that you:",
  "understand and can apply them",
  ["skipped them","forgot them","dislike reading"],
  "Application shows learning.")
H('5.b.7.G',3,"Which discussion comment points to an important idea?",
  "The author says teamwork helped them win.",
  ["My shoes are new.","I'm hungry.","The bell rings soon."],
  "Important ideas relate to the meaning of the text.")
H('5.b.7.G',3,"When discussing ideas important to the meaning, you should:",
  "point to specific parts of the text",
  ["talk about unrelated things","only repeat the title","stay silent"],
  "Discussion is supported by the text.")

# b.8 literary elements
H('5.b.8.A',3,"A story about a lost dog teaches that honesty matters. 'Honesty matters' is the:",
  "theme",
  ["topic","setting","title"],
  "A theme is a message, not just a subject.")
H('5.b.8.A',4,"The topic of a story is one word, like friendship. Which sentence states a theme?",
  "True friends help each other in hard times.",
  ["Pets","A park","Jumping rope"],
  "A theme is a full-sentence message about life.")
H('5.b.8.B',3,"A major character differs from a minor character because the major character:",
  "is more central to the plot",
  ["appears only once","has no name","never speaks"],
  "Major characters drive the story.")
H('5.b.8.B',3,"A sidekick who helps the hero now and then is usually a:",
  "minor character",
  ["narrator","setting","theme"],
  "Minor characters support the main characters.")
H('5.b.8.C',3,"The order in which events happen in a story is its:",
  "sequence",
  ["glossary","rhyme","caption"],
  "Plot elements include the sequence of events.")
H('5.b.8.C',3,"The part that solves the main problem is the:",
  "resolution",
  ["exposition","setting","dialogue"],
  "The resolution ends the conflict.")
H('5.b.8.D',3,"A story set during a flood makes the characters:",
  "face dangers that shape the plot",
  ["forget the plot","stay unchanged","ignore the weather"],
  "Setting influences events.")
H('5.b.8.D',3,"A snowy mountain setting could cause which plot event?",
  "Characters must find shelter from a storm.",
  ["Characters buy sunscreen at the beach.","Characters swim in a pool.","Characters plant a garden in summer."],
  "The setting influences what can happen.")

# b.9 genres
H('5.b.9.A',3,"A fable is a short story that:",
  "teaches a lesson, often with talking animals",
  ["lists facts in a table","gives step-by-step directions","tells a real person's life"],
  "Fables teach morals.")
H('5.b.9.A',3,"Which is a feature of a fairy tale?",
  "magic and a happily-ever-after ending",
  ["a glossary","a timeline","a recipe"],
  "Fairy tales include magic and set endings.")
H('5.b.9.B',3,"In a poem, lines that end with the same sound have:",
  "rhyme",
  ["dialogue","a glossary","captions"],
  "Rhyme is a sound device.")
H('5.b.9.B',3,"In a poem with rhyme scheme ABAB, lines 1 and 3:",
  "rhyme with each other",
  ["never rhyme","are the same word","are in different stanzas"],
  "Matching letters show matching end sounds.")
H('5.b.9.C',3,"The main divisions of a play are called:",
  "acts",
  ["stanzas","chapters","captions"],
  "Plays are divided into acts.")
H('5.b.9.C',3,"In a play, stage directions tell actors:",
  "how to move or speak",
  ["the page number","the author's age","the price"],
  "Directions guide performance.")
H('5.b.9.D.i',3,"To find the central idea of an informational text, ask:",
  "What is this text mostly about?",
  ["How many words are bold?","Who printed it?","Where is the index?"],
  "The central idea is the main point.")
H('5.b.9.D.i',3,"Which detail supports the central idea 'Recycling helps the planet'?",
  "Recycling paper saves trees.",
  ["Paper is white.","Trees are tall.","Bins are blue."],
  "Supporting evidence connects to the central idea.")
H('5.b.9.D.ii',2,"Bold words in a text usually show:",
  "important terms",
  ["mistakes","jokes","the author's name"],
  "Print features highlight key words.")
H('5.b.9.D.ii',3,"A table in an informational text is used to:",
  "organize facts in rows and columns",
  ["tell a joke","show a rhyme","list the author's pets"],
  "Tables organize data.")
H('5.b.9.D.iii',3,"Which words signal cause and effect?",
  "because, so, as a result",
  ["first, next, then","above, below, beside","however, but, although"],
  "Cause and effect uses signal words like because and as a result.")
H('5.b.9.D.iii',3,"A text explains a problem and then ways to fix it. Its organizational pattern is:",
  "problem and solution",
  ["compare and contrast","description","sequence"],
  "Problem and solution shows a problem and its answers.")
H('5.b.9.E.i',3,"In an argumentative text, the claim is:",
  "the main point the author wants you to accept",
  ["a list of rhymes","a character's name","the page number"],
  "A claim is the position the author argues.")
H('5.b.9.E.i',3,"Which sentence states a claim?",
  "Schools should start later in the morning.",
  ["Schools have classrooms.","Some buses are yellow.","The bell rang at eight."],
  "A claim is an arguable position.")
H('5.b.9.E.ii',3,"Which sentence about the ocean is an opinion?",
  "The ocean is the prettiest place to visit.",
  ["The ocean has salt water.","The ocean covers most of Earth.","Whales live in the ocean."],
  "Opinions state beliefs and cannot be proved.")
H('5.b.9.E.ii',3,"Which statement about the sun is a fact?",
  "The sun is a star.",
  ["The sun is the nicest star.","Sunny days are the best days.","Everyone loves hot weather."],
  "Facts can be proved.")
H('5.b.9.E.iii',3,"A text with simple words and bright pictures about letters is likely meant for:",
  "young children",
  ["scientists","lawyers","pilots"],
  "Intended audience shapes language and design.")
H('5.b.9.E.iii',3,"An author who uses technical terms in a report about engines is writing for:",
  "readers who know the topic",
  ["babies","pets","no one"],
  "Technical language suggests an informed audience.")
H('5.b.9.F',2,"A website with videos, links and sound is a:",
  "digital and multimodal text",
  ["printed poem","handwritten letter","paper map only"],
  "Digital texts can combine modes.")
H('5.b.9.F',3,"A multimodal text combines:",
  "words with images, sound or video",
  ["only words","only numbers","only blank space"],
  "Multimodal means more than one mode.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'sla_4.jsonl'))

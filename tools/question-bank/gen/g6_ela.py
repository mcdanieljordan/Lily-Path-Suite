#!/usr/bin/env python3
"""Grade 6 ELA (TEKS 110.22.b) - original questions, about 3 per assessable standard.
   Skipped: speaking/listening (1), assigned-purpose/drafting/publishing/composing projects (5.A, 10.A, 10.E, 11.A-C), research planning (12.A-D,F,I,J)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('110.22.b.', 961, own='g6_ela.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 2.A dictionary / glossary
H('2.A', 2, "Which part of a dictionary entry shows how to say a word aloud?", "the pronunciation respelling", ["the part-of-speech label only", "the etymology only", "the sample sentence only"], "Respellings in parentheses guide pronunciation.")
H('2.A', 3, "A dictionary entry lists 'rec-og-nize' with a dot or dash between the chunks. What does this show?", "how the word is divided into syllables", ["how the word is spelled in Latin", "what the word rhymes with", "where the word was first used"], "Syllable breaks help with decoding and line breaks.")
H('2.A', 3, "A student wants to know which language a word came from. Which dictionary feature should be checked?", "the word origin note", ["the pronunciation key", "the guide words", "the example sentence"], "Etymology notes give word origins.")
H('2.A', 4, "A dictionary lists 'permit' as both a verb and a noun, with the stress on a different syllable in each. What should a reader do to choose the correct pronunciation?", "use the part of speech from the sentence to pick the matching entry", ["always use the first entry", "ignore the stress marks", "choose the shortest entry"], "Stress and meaning change with part of speech.")

# ---- 2.B context clues
H('2.B', 2, "'The arid desert received almost no rain, so its dry soil cracked.' What does 'arid' mean?", "very dry", ["very cold", "full of animals", "very large"], "The sentence gives 'dry soil' and 'no rain' as clues.")
H('2.B', 3, "'Maya was reluctant to jump, hesitating at the edge of the pool for several minutes.' What does 'reluctant' mean?", "unwilling", ["eager", "angry", "tired"], "Hesitating shows she did not want to jump.")
H('2.B', 3, "'The scientist's hypothesis, or educated guess, was tested in three trials.' What is the 'hypothesis'?", "an educated guess", ["a final result", "a tool", "a trial"], "The phrase set off by commas defines the word.")
H('2.B', 4, "'Unlike her gregarious brother, who loved parties, Tia preferred to stay home alone.' What does 'gregarious' most likely mean?", "sociable", ["shy", "clumsy", "wealthy"], "The word 'unlike' signals an opposite of staying home alone.")

# ---- 2.C Greek and Latin roots
H('2.C', 2, "The Latin root 'port' means 'carry.' Which word means 'able to be carried'?", "portable", ["portal", "portion", "porch"], "Port + able = can be carried.")
H('2.C', 3, "The Greek root 'tele' means 'far.' What does 'telescope' most likely mean?", "an instrument for viewing far-off things", ["a close-up lens", "a type of clock", "a map of stars"], "Tele (far) + scope (view).")
H('2.C', 3, "The Latin root 'dict' means 'say.' Which word fits 'a formal statement ordered by a ruler'?", "edict", ["predict", "contradict", "dictionary"], "An edict is something said or declared with authority.")
H('2.C', 4, "The root 'bio' means 'life' and 'graph' means 'write.' What is a 'biography'?", "a written account of a person's life", ["a study of rocks", "a drawing of an animal", "a list of rules"], "Bio (life) + graph (write).")

# ---- 5.B questions during reading
H('5.B', 3, "A student reads the first paragraph of an article about volcanoes. Which question would best deepen understanding before reading on?", "What causes a volcano to erupt?", ["What color is the cover?", "How many pages are there?", "Who published the magazine?"], "A question about the topic guides reading.")
H('5.B', 4, "Which question would a reader ask AFTER reading to check the main idea of a text about coral reefs?", "What was the most important point about coral reefs?", ["Is the font easy to read?", "Where was the book printed?", "What is the page count?"], "After-reading questions examine key ideas.")
H('5.B', 3, "Asking 'Why did the character make that choice?' while reading is a way to...", "dig deeper into the text", ["skip hard parts", "avoid the plot", "memorize the author's name"], "Questions deepen understanding.")

# ---- 5.C predictions
H('5.C', 3, "A text has the headings 'Causes,' 'Effects,' and 'Solutions.' What can a reader predict about its structure?", "it explains a problem and how to respond to it", ["it is a poem", "it is a diary", "it is a play script"], "Headings reveal organization.")
H('5.C', 3, "A story begins 'Once upon a time, in a kingdom beyond the hills...' What genre is most likely?", "fairy tale", ["biography", "science article", "news report"], "The opening is a fairy-tale convention.")
H('5.C', 4, "A reader predicted that a character would apologize, but the character stormed away. What should the reader do?", "correct the prediction using the new evidence", ["ignore the new text", "stop reading", "change the title"], "Good readers confirm or correct predictions.")

# ---- 5.D mental images
H('5.D', 2, "Which sentence would help a reader create the clearest mental image?", "The red kite dipped and swirled above the snowy field.", ["The kite was there.", "It was nice outside.", "Something happened in the sky."], "Concrete details help readers visualize.")
H('5.D', 3, "A reader pictures a dark, creaking cabin after reading 'The floorboards groaned under each step.' Which technique is this?", "visualizing", ["skimming", "paraphrasing", "citing"], "Creating images from details deepens understanding.")
H('5.D', 3, "Which detail best supports picturing a stormy sea?", "waves hammered the deck while thunder cracked overhead", ["the sailors had lunch", "the boat was painted white", "a flag hung on the mast"], "Active, sensory details show the storm.")

# ---- 5.E connections
H('5.E', 2, "A student reads about a character who moves to a new school and recalls her own first day. This is a connection to...", "personal experience", ["another text", "society", "an author's biography"], "Text-to-self connection.")
H('5.E', 3, "After reading about a fire in a novel, a student thinks about an article on fire safety. This is a connection to...", "another text", ["personal experience", "a map", "a dictionary"], "Text-to-text connection.")
H('5.E', 4, "A reader connects a story about unfair rules to a current debate about school policies. This is a connection to...", "society", ["only the plot", "only the setting", "only the author"], "Text-to-world connection.")

# ---- 5.F inferences
H('5.F', 3, "'Jada stared at the empty chair, then slowly folded the note and slipped it into her pocket.' What can be inferred?", "Jada is sad or upset about someone's absence", ["Jada is eager to start a game", "Jada is angry about dinner", "Jada is going to sleep"], "Her slow, quiet actions imply sadness.")
H('5.F', 3, "'Carlos grabbed his umbrella and pulled on his boots before leaving.' What can be inferred about the weather?", "it is raining or about to rain", ["it is a heat wave", "it is snowing heavily", "it is calm and sunny"], "Umbrella and boots suggest rain.")
H('5.F', 4, "'The dog thumped its tail and pulled the leash toward the door.' Which inference is best supported?", "the dog wants to go outside", ["the dog is afraid", "the dog is asleep", "the dog is angry"], "Tail thumping and pulling show eagerness.")

# ---- 5.G key ideas
H('5.G', 3, "Which detail is MOST important to the key idea of an article about recycling's benefits?", "recycling reduces waste in landfills", ["the article has a blue border", "the author lives in Ohio", "a photo shows a truck"], "Key ideas are central to the message.")
H('5.G', 4, "A passage describes three ways bees help crops and one way bees make honey. The key idea is most likely...", "bees are important to farming", ["bees are hard to find", "honey is expensive", "crops need no care"], "Most details support pollination's importance.")
H('5.G', 3, "To find the key idea in a paragraph, a reader should...", "decide what the details have in common", ["count the words", "check the last letter", "look at the page number"], "Details point to the main message.")

# ---- 5.H synthesize
H('5.H', 3, "A student reads two articles about ocean pollution and combines facts from both to explain solutions. This is...", "synthesizing", ["copying", "skimming", "guessing"], "Combining sources creates new understanding.")
H('5.H', 4, "Article A says plastic harms sea turtles. Article B says plastic breaks into tiny pieces that enter the food chain. Which synthesis is best?", "plastic harms ocean animals directly and spreads through the food chain", ["plastic is a type of toy", "sea turtles never eat", "the articles disagree about turtles"], "Merges both ideas.")
H('5.H', 4, "Which statement shows synthesis rather than summary of one text?", "Combining the interview and the report shows the policy affects both students and teachers.", ["The report is eight pages long.", "The interview starts on page two.", "The report has a title."], "Synthesis builds a new idea from several sources.")

# ---- 5.I monitor comprehension
H('5.I', 2, "A reader no longer understands a paragraph. What is a good fix-up strategy?", "re-read it", ["skip the whole chapter", "close the book forever", "guess the ending"], "Re-reading clarifies meaning.")
H('5.I', 3, "Which strategy helps a reader who meets an unknown word?", "use context clues or look it up", ["skip every sentence with it", "memorize the page", "change the font"], "Fix-up strategies address confusion.")
H('5.I', 4, "A reader keeps losing track of characters. Which adjustment is most useful?", "make a quick list of characters and their roles", ["read faster", "ignore the names", "read only the last page"], "Notetaking aids comprehension.")

# ---- 6.C text evidence
H('6.C', 3, "Claim: 'The narrator is nervous.' Which evidence best supports the claim?", "The narrator's hands shook as she approached the stage.", ["The stage was painted green.", "The audience clapped politely.", "The show started at seven."], "Direct detail shows nervousness.")
H('6.C', 3, "Which is the strongest piece of text evidence for 'The town is poor'?", "Many houses had boarded windows and bare cupboards.", ["The town has a river.", "It rained on Tuesday.", "The mayor wore a hat."], "Concrete details show poverty.")
H('6.C', 4, "A student writes 'The author thinks school lunches should be healthier' but gives no support. What is missing?", "a quotation or detail from the text", ["a longer title", "a bigger font", "a drawing"], "Responses need textual evidence.")

# ---- 6.D paraphrase and summarize
H('6.D', 2, "A good summary of a text should include...", "the main ideas in your own words", ["every detail", "only your opinion", "the first sentence word for word"], "Summaries are short and keep meaning.")
H('6.D', 3, "Which is the best paraphrase of 'The sun dipped below the horizon, painting the sky orange'?", "The sun set and the sky turned orange.", ["The sun rose in the east.", "The sky was empty.", "The horizon vanished."], "Paraphrase keeps the meaning in new words.")
H('6.D', 4, "Which sentence is a summary rather than a paraphrase of one line?", "The article explains how floods form and how towns prepare.", ["Floods form when rivers rise.", "Towns must pay for sandbags.", "The river rose by two feet."], "A summary covers the whole text.")

# ---- 6.G explicit and implicit meanings
H('6.G', 3, "'Dad said he would be home by six. At nine, Elena was still setting the table for two.' What is the implicit meaning?", "Elena is still waiting and hoping he will come", ["Dad arrived early", "Elena dislikes dinner", "Dad is cooking"], "The meaning is implied, not stated.")
H('6.G', 3, "An explicit meaning in a text is one that is...", "directly stated", ["hidden in the title only", "never written", "shown only in pictures"], "Explicit means clearly stated.")
H('6.G', 4, "'The old swing swayed gently in the empty yard.' Which implicit idea is most likely suggested?", "loneliness or something missing", ["a loud celebration", "a busy playground", "a sports game"], "Empty settings suggest absence.")

# ---- 7.A themes
H('7.A', 3, "In a story, a boy refuses help, struggles, then accepts it and succeeds. Which theme is best supported?", "accepting help can lead to success", ["wealth brings happiness", "it is wrong to try", "lying is useful"], "The plot shows the lesson.")
H('7.A', 4, "A theme is best described as...", "a message about life or human nature in a text", ["the order of events", "the place where the story happens", "the author's birthplace"], "Themes are underlying messages.")
H('7.A', 4, "Two stories show characters who lose a contest but learn teamwork. What theme runs across both?", "cooperation matters more than winning", ["winning is everything", "contests are unfair", "teams never work"], "The shared lesson is the theme.")

# ---- 7.B character responses
H('7.B', 3, "A character is embarrassed when she forgets her lines, so she quits the play. Which type of response is quitting?", "an external response", ["an internal response", "a setting", "a theme"], "Actions are external; feelings are internal.")
H('7.B', 3, "Which is an INTERNAL response?", "He felt a wave of jealousy.", ["He slammed the door.", "She ran down the hall.", "They waved goodbye."], "Thoughts and feelings are internal.")
H('7.B', 4, "How does a character's fear of failure most likely develop the plot when she hides her test?", "it creates a problem she must face later", ["it ends the story at once", "it changes the setting", "it removes all conflict"], "Choices create conflict.")

# ---- 7.C plot elements
H('7.C', 2, "The part of a plot where the problem reaches its highest tension is the...", "climax", ["exposition", "resolution", "title"], "The climax is the turning point.")
H('7.C', 3, "A story opens with the ending, then goes back in time to show how events led there. This is a...", "non-linear plot (flashback)", ["linear plot", "rhyme scheme", "stanza"], "Order of events is rearranged.")
H('7.C', 4, "After the main conflict is settled, the events that follow and tie up loose ends are called...", "falling action and resolution", ["rising action", "exposition", "foreshadowing"], "These follow the climax.")

# ---- 7.D setting
H('7.D', 3, "A story is set during a harsh winter in 1850s Texas. How might the setting influence the plot?", "scarce supplies could force characters to make hard choices", ["the setting has no effect", "the characters will be on a beach", "it ensures the story is funny"], "Setting creates challenges.")
H('7.D', 3, "A character raised in a fishing village knows how to read tides. This detail shows how...", "culture and setting shape the character", ["the author's age matters", "the title was chosen", "the climax occurs"], "Cultural setting shapes skills.")
H('7.D', 4, "Why does historical setting matter in a story about a girl denied the vote?", "it explains the rules and attitudes that cause her conflict", ["it changes the font", "it replaces the plot", "it hides the theme"], "Historical context drives conflict.")

# ---- 8.A genres
H('8.A', 2, "A story in which detectives follow clues to solve a crime belongs to which genre?", "mystery", ["biography", "poetry", "encyclopedia entry"], "Mysteries focus on clues and solving crimes.")
H('8.A', 3, "A story set in the past that uses real events and invented characters is...", "historical fiction", ["science article", "autobiography", "fable only"], "It blends real history with fiction.")
H('8.A', 3, "A story with a tense journey, danger and daring escapes is most likely a(n)...", "adventure story", ["recipe", "textbook", "news article"], "Adventure stories feature risk and action.")

# ---- 8.B poetry structure
H('8.B', 3, "A poet breaks a line in the middle of a sentence to make readers pause. This effect comes from...", "a line break", ["a title", "a footnote", "an index"], "Line breaks control pacing.")
H('8.B', 3, "A poem with a regular pattern of stressed and unstressed syllables has a steady...", "meter", ["plot", "setting", "glossary"], "Meter is the rhythm of a poem.")
H('8.B', 4, "A poem has no rhyme or regular meter. It is called...", "free verse", ["a sonnet", "a limerick", "a haiku"], "Free verse lacks fixed patterns.")

# ---- 8.C drama
H('8.C', 3, "In a play, a character's personality is mostly revealed through...", "dialogue and actions", ["footnotes", "glossaries", "indexes"], "Plays rely on speech and staging.")
H('8.C', 3, "Stage directions in a script are used to tell...", "actors and directors how to move, speak, or what the set looks like", ["readers the definition of words", "the author's address", "when the play will end"], "They guide staging.")
H('8.C', 4, "A playwright has a character whisper to a rival while another character looks away. What is the playwright showing?", "tension through staging and speech", ["the climax's resolution", "a flashback", "a footnote"], "Staging and dialogue show relationships.")

# ---- 8.F multimodal
H('8.F', 3, "A webpage includes text, a video and a clickable map. This is an example of a...", "multimodal text", ["limerick", "letter", "myth"], "It uses more than one mode.")
H('8.F', 3, "Which feature is unique to digital texts?", "hyperlinks that lead to more information", ["page numbers", "paragraph indents", "titles"], "Links connect to other content.")
H('8.F', 4, "A reader evaluates a website's infographic. Which question is most useful?", "Does the image clearly show the data being described?", ["Is the background blue?", "How many pixels is it?", "Who made the font?"], "Evaluation looks at effectiveness.")

# ---- 8.D.i controlling idea
H('8.D.i', 3, "The controlling idea of an informational essay is its...", "central idea or thesis", ["last sentence only", "title page", "glossary"], "It ties details together.")
H('8.D.i', 4, "An essay says 'Cities should plant more trees.' Which detail best supports it?", "Trees lower summer temperatures and clean the air.", ["Trees are tall.", "Some trees lose leaves.", "Cities have buildings."], "Evidence supports the thesis.")
H('8.D.i', 3, "Which sentence states a controlling idea?", "Regular exercise improves both health and mood.", ["Exercise is on page three.", "The author is a coach.", "The gym opens at six."], "It makes a claim covering the details.")

# ---- 8.D.ii text features
H('8.D.ii', 3, "Which text feature lists the sources the author used?", "references", ["the preface", "the foreword", "the headline"], "References credit sources.")
H('8.D.ii', 3, "A short note at the start of a book explaining why the author wrote it is a...", "preface", ["glossary", "bibliography", "index"], "Prefaces give background.")
H('8.D.ii', 4, "A reader wants to know who the author thanks for help. Where should the reader look?", "the acknowledgements", ["the index", "the glossary", "the table of contents"], "Acknowledgements thank contributors.")

# ---- 8.D.iii organizational patterns
H('8.D.iii', 3, "A passage describes the benefits and drawbacks of electric cars. Which pattern is used?", "advantage and disadvantage", ["chronological order", "cause and effect only", "poetry"], "It weighs pros and cons.")
H('8.D.iii', 3, "A text sorts animals into groups such as mammals, birds, and reptiles. The pattern is...", "classification", ["sequence", "problem and solution", "definition only"], "It organizes into categories.")
H('8.D.iii', 4, "A paragraph begins with the word 'Photosynthesis is the process by which...' and then explains it. The pattern is...", "definition", ["chronology", "compare and contrast", "persuasion"], "It defines a term.")

# ---- 8.E.i claim
H('8.E.i', 3, "In an argumentative text, the claim is...", "the writer's position on an issue", ["the author's name", "a list of sources", "the title font"], "The claim states the argument.")
H('8.E.i', 3, "Which sentence is a claim?", "Schools should start later in the morning.", ["Schools open at eight.", "Buses are yellow.", "Students carry backpacks."], "It takes a position.")
H('8.E.i', 4, "A writer argues 'Our town needs a skate park.' What is the claim?", "the town needs a skate park", ["skate parks are on streets", "teens skate", "parks cost money"], "The claim is the stated position.")

# ---- 8.E.ii evidence
H('8.E.ii', 3, "Which is an example of statistical evidence?", "Seventy percent of students surveyed prefer later start times.", ["Everyone knows later is better.", "I think it is better.", "It feels right."], "Statistics offer numeric evidence.")
H('8.E.ii', 4, "An author quotes a doctor to support a claim about sleep. This evidence is...", "an expert testimony", ["a personal anecdote only", "a rhyme", "a simile"], "Experts add credibility.")
H('8.E.ii', 3, "A writer shares a short story about a single student to support a claim. This evidence is a(n)...", "anecdote", ["statistic", "definition", "glossary"], "Anecdotes use personal examples.")

# ---- 8.E.iii audience
H('8.E.iii', 3, "A flyer says 'Join the middle school science club! No experience needed!' Who is the intended audience?", "middle school students", ["adult scientists", "toddlers", "retired teachers"], "The wording targets students.")
H('8.E.iii', 4, "An article about retirement savings uses terms like 'portfolio' and 'annuity.' The intended audience is probably...", "adults planning for retirement", ["kindergartners", "pet owners", "movie fans"], "Vocabulary shows the reader.")
H('8.E.iii', 3, "A letter to the school board about bus routes is aimed at...", "school board members", ["students at recess", "sports fans", "bakery customers"], "The addressee is the audience.")

# ---- 9.A author's purpose
H('9.A', 2, "A text that teaches readers how volcanoes form has which main purpose?", "to inform", ["to entertain only", "to persuade only", "to confuse"], "Informational texts explain.")
H('9.A', 3, "An article urges readers to adopt shelter dogs. The author's purpose is to...", "persuade", ["inform with neutral facts", "entertain with a joke", "describe a setting"], "It calls for action.")
H('9.A', 4, "A fable about a tortoise and a hare ends with a moral. What is the author's message?", "slow and steady effort can beat careless speed", ["tortoises are fast", "hares are slow", "races are illegal"], "The moral is the message.")

# ---- 9.B text structure
H('9.B', 3, "An author explains a problem and then describes how it was fixed. This structure helps the author...", "show a problem and solution", ["tell a joke", "describe a rhyme", "avoid details"], "Structure supports purpose.")
H('9.B', 4, "A history article is arranged in order of dates. How does this structure support the author's purpose?", "it helps readers follow events as they happened", ["it hides the causes", "it makes the text a poem", "it removes all facts"], "Chronology clarifies sequence.")
H('9.B', 3, "A compare-and-contrast structure helps an author...", "show similarities and differences", ["list steps", "tell a story", "describe a place"], "That is the structure's function.")

# ---- 9.C print and graphic features
H('9.C', 3, "Why might an author use bold type for key terms?", "to help readers notice important vocabulary", ["to make the text longer", "to hide the details", "to change the genre"], "Bold signals importance.")
H('9.C', 3, "A diagram labeled 'Parts of a Cell' is included in a science article. Its purpose is to...", "show information visually", ["entertain with a rhyme", "tell a story", "give the author's name"], "Graphics clarify content.")
H('9.C', 4, "Why would an author include a map in a text about an expedition?", "to help readers see the route and places", ["to rhyme with the text", "to hide the date", "to replace the title"], "Maps show location and routes.")

# ---- 9.D figurative language
H('9.D', 2, "'The wind whispered through the trees' is an example of...", "personification", ["metaphor", "alliteration", "idiom"], "The wind is given a human action.")
H('9.D', 3, "'Time is a thief' is a...", "metaphor", ["simile", "personification", "hyperbole"], "It compares without 'like' or 'as.'")
H('9.D', 4, "'The classroom was a zoo' helps the author...", "show the room was loud and chaotic", ["describe real animals", "list school rules", "state the date"], "The metaphor conveys noise and disorder.")

# ---- 9.E point of view
H('9.E', 3, "A narrator who knows the thoughts of every character uses which point of view?", "omniscient", ["limited", "second person", "first person"], "Omniscient narrators know everything.")
H('9.E', 3, "A narrator tells only what one character thinks and sees, using 'he' or 'she.' This is...", "third-person limited", ["omniscient", "second-person", "first-person plural"], "It limits knowledge to one character.")
H('9.E', 4, "Why would an author use a limited point of view in a mystery?", "to keep readers from knowing everything the detective doesn't", ["to reveal all secrets at once", "to remove suspense", "to add footnotes"], "Limited view builds suspense.")

# ---- 9.F mood and voice
H('9.F', 3, "'The silent halls were dim and cold' creates which mood?", "eerie or gloomy", ["cheerful", "excited", "silly"], "Word choice sets mood.")
H('9.F', 3, "An author's distinctive way of expressing ideas, shown through word choice and sentence style, is called...", "voice", ["plot", "setting", "theme"], "Voice is the author's personality in writing.")
H('9.F', 4, "Which phrase would most likely create a joyful mood?", "sunlight spilled over the laughing crowd", ["gloom settled over the ruins", "the shadows closed in", "a chill crept along the wall"], "Positive imagery sets a joyful mood.")

# ---- 9.G rhetorical devices vs fallacies
H('9.G', 3, "Which is a logical fallacy?", "Everyone is buying it, so it must be the best.", ["Studies show regular sleep improves focus.", "A doctor recommends daily exercise.", "The data shows a 5% rise."], "Bandwagon appeal is a fallacy.")
H('9.G', 4, "Repeating a key phrase for emphasis in a speech is a(n)...", "rhetorical device", ["logical fallacy", "glossary entry", "plot twist"], "Repetition persuades through style.")
H('9.G', 4, "'Either we ban all cars or the planet is doomed' is a fallacy because it...", "offers only two extreme choices", ["uses a metaphor", "cites an expert", "includes data"], "That is a false dilemma.")

# ---- 10.B.i organization
H('10.B.i', 3, "Which word helps connect two paragraphs by showing contrast?", "however", ["therefore", "similarly", "first"], "However signals a contrast.")
H('10.B.i', 3, "An introduction in an essay should...", "present the topic and the controlling idea", ["list every detail", "repeat the conclusion", "avoid the topic"], "Introductions orient readers.")
H('10.B.i', 4, "Which sentence best works as a transition between a paragraph on benefits and one on drawbacks?", "Despite these advantages, there are some concerns.", ["Pizza is popular.", "The end.", "In conclusion, I like dogs."], "It links the two ideas.")

# ---- 10.C revise
H('10.C', 3, "Which revision adds sentence variety to 'I ran. I jumped. I fell.'?", "I ran, jumped, and then tumbled to the ground.", ["I ran. I ran. I ran.", "Ran jumped fell.", "I ran I jumped I fell."], "Combining sentences adds variety.")
H('10.C', 3, "Which word choice is more precise than 'nice'?", "generous", ["good", "fine", "okay"], "Precise words clarify meaning.")
H('10.C', 4, "A paragraph about pets suddenly mentions a baseball game. In revision, the writer should...", "remove the unrelated sentence", ["add more baseball", "delete the topic sentence", "change all verbs"], "Revision maintains focus.")

# ---- 10.D.i complete sentences
H('10.D.i', 2, "Which is a complete sentence?", "The dog barked at the mail carrier.", ["Barked at the mail.", "Running through the yard.", "Because the dog."], "It has a subject and a predicate.")
H('10.D.i', 3, "Which sentence is a run-on?", "I love music I play guitar every day.", ["I love music, and I play guitar every day.", "I love music; I play guitar every day.", "Because I love music, I play guitar."], "Two independent clauses are joined without punctuation.")
H('10.D.i', 3, "Which sentence has correct subject-verb agreement?", "The books on the shelf are dusty.", ["The books on the shelf is dusty.", "The books on the shelf was dusty.", "The books on the shelf be dusty."], "The subject 'books' is plural.")
H('10.D.i', 4, "Which is a fragment?", "When the bell rang.", ["The bell rang.", "She left.", "We waited."], "A dependent clause cannot stand alone.")

# ---- 10.D.ii verb tenses
H('10.D.ii', 3, "Which sentence uses a consistent verb tense?", "She opened the box and found a note.", ["She opened the box and finds a note.", "She opens the box and found a note.", "She will open the box and found a note."], "Both verbs are in the past tense.")
H('10.D.ii', 3, "Choose the correct verb: 'Yesterday, we ____ to the museum.'", "went", ["go", "will go", "going"], "Yesterday signals the past.")
H('10.D.ii', 4, "Which sentence shifts tense incorrectly?", "He walks to school and waved to his friend.", ["He walked to school and waved to his friend.", "He walks to school and waves to his friend.", "He will walk to school and wave to his friend."], "Walks (present) and waved (past) clash.")

# ---- 10.D.iii conjunctive adverbs
H('10.D.iii', 3, "Which conjunctive adverb best completes: 'It was raining; ____, we stayed inside.'?", "therefore", ["however", "although", "because"], "It shows a result.")
H('10.D.iii', 4, "Choose the correct punctuation: 'I wanted to go ____ however, I was too tired.'", "; (semicolon)", [", (comma)", ". (no pause)", "- (hyphen)"], "A semicolon precedes a conjunctive adverb joining two independent clauses.")
H('10.D.iii', 3, "Which word is a conjunctive adverb?", "moreover", ["because", "and", "but"], "Moreover connects ideas and adds information.")

# ---- 10.D.iv prepositional phrases and agreement
H('10.D.iv', 3, "Which word is the subject in 'The box of pencils is on the desk'?", "box", ["pencils", "desk", "is"], "The prepositional phrase does not contain the subject.")
H('10.D.iv', 4, "Choose the correct verb: 'The group of students ____ waiting.'", "is", ["are", "were", "be"], "The subject 'group' is singular.")
H('10.D.iv', 3, "Which sentence contains a prepositional phrase?", "The cat slept under the porch.", ["The cat slept soundly.", "The cat purred loudly.", "The cat is tired."], "'Under the porch' is a preposition plus its object.")

# ---- 10.D.v pronouns
H('10.D.v', 3, "Which pronoun correctly completes 'The girl ____ won the race is my cousin'?", "who", ["whom", "whose", "which"], "Who is the subject of 'won'.")
H('10.D.v', 3, "Which pronoun is a relative pronoun?", "that", ["she", "they", "we"], "Relative pronouns introduce clauses.")
H('10.D.v', 4, "Which sentence uses a relative pronoun correctly?", "The book that I borrowed is overdue.", ["The book who I borrowed is overdue.", "The book whom I borrowed it is overdue.", "The book whose I borrowed is overdue."], "That refers to a thing and begins the clause 'that I borrowed'.")

# ---- 10.D.vi conjunctions
H('10.D.vi', 3, "Which pair is a correlative conjunction?", "either...or", ["because...so", "and...but", "if...then-ever"], "Either/or are paired.")
H('10.D.vi', 3, "Which subordinating conjunction best completes: '____ the storm ended, we went outside'?", "After", ["Neither", "Or", "Both"], "After introduces a time clause.")
H('10.D.vi', 4, "Which sentence is complex?", "Although it was late, we kept working.", ["We worked and she slept.", "We worked.", "We worked, but she slept."], "It has a dependent and an independent clause.")

# ---- 10.D.vii capitalization
H('10.D.vii', 2, "Which of these words should always be capitalized?", "Texas", ["state", "mountain", "street"], "Names of specific places are proper nouns.")
H('10.D.vii', 3, "Which of these is an acronym that should be written in all capital letters?", "NASA", ["library", "teacher", "pencil"], "Acronyms are formed from initials and written in capitals.")
H('10.D.vii', 3, "Which phrase needs capital letters?", "the Boy Scouts of America", ["a group of friends", "a club at school", "my class"], "Names of specific organizations are capitalized.")

# ---- 10.D.viii punctuation
H('10.D.viii', 3, "Which sentence uses a comma correctly after an introductory element?", "After the rain stopped, we went outside.", ["After the rain stopped we went, outside.", "After, the rain stopped we went outside.", "After the rain, stopped we went outside."], "Use a comma after an introductory clause.")
H('10.D.viii', 3, "Which sentence is punctuated correctly?", "However, the answer was wrong.", ["However the answer, was wrong.", "However the answer was, wrong.", "However the, answer was wrong."], "A comma follows a transition word.")
H('10.D.viii', 4, "Which sentence needs a comma?", "Although she was tired she finished the race.", ["She finished the race.", "She was tired.", "He ran fast."], "A comma follows an introductory dependent clause.")

# ---- 10.D.ix spelling
H('10.D.ix', 2, "Which word correctly completes 'The dog wagged ____ tail'?", "its", ["it's", "its'", "it is"], "'Its' shows possession.")
H('10.D.ix', 3, "Choose the correct word: 'Lack of sleep can ____ your mood.'", "affect", ["effect", "effects", "affects"], "Affect is the verb meaning to influence.")
H('10.D.ix', 3, "Which sentence uses the right word?", "They're going to their house over there.", ["Their going to they're house over there.", "There going to there house over their.", "They're going to there house over they're."], "They're = they are; their = possessive; there = place.")

# ---- 12.E primary vs secondary sources
H('12.E', 3, "Which is a primary source?", "a diary written by a soldier during the war", ["a textbook chapter about the war", "an encyclopedia article", "a documentary made in 2020"], "Primary sources are firsthand.")
H('12.E', 3, "Which is a secondary source?", "a biography of a president written by a historian", ["a letter written by the president", "a photograph taken at the event", "an original speech"], "Secondary sources interpret primary ones.")
H('12.E', 4, "A student needs firsthand accounts of the 1969 moon landing. Which source is best?", "an astronaut's logbook", ["a movie review", "a modern magazine summary", "a website listing trivia"], "A logbook is an original record.")

# ---- 12.G paraphrase vs plagiarism
H('12.G', 3, "Copying a sentence from a website into your report without credit is...", "plagiarism", ["paraphrasing", "summarizing", "synthesizing"], "Using someone's words as your own is plagiarism.")
H('12.G', 3, "Which is a proper paraphrase of 'The Amazon holds half of the world's rainforest' ?", "About half of Earth's rainforest is in the Amazon, according to the source.", ["The Amazon holds half of the world's rainforest.", "Rainforests are nice.", "I invented this fact."], "Rephrase and credit the source.")
H('12.G', 4, "Even when you paraphrase, you should...", "cite the original source", ["hide the source", "keep it secret", "copy it word for word"], "Ideas still belong to the source.")

# ---- 12.H credibility and fallacies
H('12.H.i', 3, "Which source is most credible for information about vaccines?", "a government health agency website", ["an anonymous blog", "a social media post", "a product ad"], "Reliable, expert sources are best.")
H('12.H.i', 4, "A website selling energy drinks says its drink makes you smarter. What should a careful reader consider?", "the site may be biased toward selling the product", ["the website is always right", "bias doesn't matter", "ads are unbiased"], "Sellers have an interest in the claim.")
H('12.H.i', 3, "An author shows bias when he...", "presents only one side with loaded words", ["offers many viewpoints fairly", "cites several experts", "gives balanced evidence"], "Bias favors one view.")
H('12.H.ii', 3, "'This is the worst idea in the history of the world!' is an example of...", "hyperbole", ["a statistic", "a primary source", "a definition"], "Extreme exaggeration is hyperbole.")
H('12.H.ii', 4, "An ad shows a sad puppy to make viewers donate without giving facts about the charity. This is a(n)...", "emotional appeal", ["logical proof", "statistic", "primary source"], "It uses feelings, not evidence.")
H('12.H.ii', 4, "'All teenagers are lazy' is an example of...", "a stereotype", ["a fact", "a statistic", "a definition"], "It overgeneralizes about a group.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g6_ela.jsonl'))
print("saved", len(B.out), "questions")

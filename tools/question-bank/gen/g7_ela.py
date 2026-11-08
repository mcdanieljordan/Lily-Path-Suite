#!/usr/bin/env python3
"""Grade 7 ELA (TEKS 110.23.b) - original questions, about 3 per assessable standard.
   Skipped: speaking/listening (1), purpose-setting/drafting/publishing/composing projects (5.A, 6.A, 6.B, 6.E, 6.F, 6.H, 6.I, 10.A, 10.E, 11.*), research planning (12.A-D,F,I,J)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('110.23.b.', 962, own='g7_ela.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 2.A reference tools
H('2.A', 2, "Which resource would a reader use to find a word's synonyms?", "a thesaurus", ["an atlas", "an almanac", "a phone book"], "A thesaurus lists words with similar meanings.")
H('2.A', 3, "A reader sees the label 'adj.' in a dictionary entry for 'gleaming'. What does the label tell the reader?", "the word's part of speech", ["the word's origin", "the number of syllables", "the pronunciation"], "Adj. stands for adjective.")
H('2.A', 3, "Which dictionary detail helps a reader pronounce an unfamiliar word?", "the phonetic spelling and stress marks", ["the sample sentence only", "the word's part of speech", "the guide words"], "Phonetic respellings show how to say a word.")
H('2.A', 4, "A student looks up 'novel' and finds two entries: one adjective and one noun. How can the student pick the right entry?", "match the word's use in the sentence to the part of speech", ["use the entry with fewer letters", "choose the older entry", "pick the second entry every time"], "Part of speech identifies the meaning.")

# ---- 2.B context contrast / cause-effect
H('2.B', 2, "'Unlike the calm lake, the river was turbulent and wild.' What does 'turbulent' mean?", "rough and unsettled", ["quiet", "frozen", "shallow"], "'Unlike calm' signals an opposite.")
H('2.B', 3, "'Because the road was treacherous, drivers moved slowly and clutched their wheels.' What does 'treacherous' mean?", "dangerous", ["scenic", "wide", "newly built"], "The cause-effect clue is slow, tense driving.")
H('2.B', 3, "'Her frugal habits, such as reusing envelopes, saved the family money.' What is the meaning of 'frugal'?", "careful about spending", ["wasteful", "famous", "noisy"], "Reusing envelopes shows saving.")
H('2.B', 4, "'In contrast to his verbose uncle, Ben answered in a few words.' What does 'verbose' mean?", "using too many words", ["using few words", "speaking softly", "speaking rudely"], "Contrast with 'a few words' signals the opposite.")

# ---- 2.C roots
H('2.C', 2, "The Greek root 'chron' means 'time.' Which word means 'arranged in order of time'?", "chronological", ["geological", "biological", "psychological"], "Chrono + logical = time order.")
H('2.C', 3, "The Latin root 'spect' means 'look.' What does 'spectator' mean?", "a person who watches", ["a person who sings", "a person who builds", "a person who writes"], "Spect = look.")
H('2.C', 3, "The Greek root 'phon' means 'sound.' Which instrument name uses it?", "saxophone", ["telescope", "microscope", "periscope"], "Phon = sound.")
H('2.C', 4, "The Latin root 'scrib/script' means 'write.' What is a 'manuscript'?", "a handwritten or typed document", ["a musical instrument", "a map", "a speech made aloud"], "Manu (hand) + script (write).")

# ---- 5.B questions
H('5.B', 3, "A reader generates the question 'What evidence supports the author's claim?' This is most useful to...", "evaluate the argument", ["count the pages", "find the font", "name the publisher"], "Questions guide analysis.")
H('5.B', 3, "While reading a mystery, which question best helps predict what comes next?", "What clues has the author given so far?", ["What is the weight of the book?", "How many chapters are left?", "Who illustrated the cover?"], "Clue-based questions guide inference.")
H('5.B', 4, "After finishing an article, a reader asks 'What new questions do I have?' This after-reading step helps the reader...", "extend understanding and seek more information", ["forget the text", "stop reading", "avoid analysis"], "Questions can lead to further inquiry.")

# ---- 5.C predictions
H('5.C', 3, "A chapter title is 'The Storm Gathers.' What is the best prediction?", "a dangerous event will build in the plot", ["the characters take a nap", "the setting changes to a snowy mountain only", "the story ends happily"], "The title signals rising tension.")
H('5.C', 3, "Text features such as a map, a timeline and sidebars suggest a text that is...", "informational", ["a poem", "a play", "a fable"], "Features signal genre.")
H('5.C', 4, "A reader predicted a character would win a race. The text says he trips on page 40. What should the reader do?", "revise the prediction with the new evidence", ["keep the same prediction", "stop reading", "ignore the page"], "Predictions are confirmed or corrected.")

# ---- 5.D images
H('5.D', 3, "Which sentence would help a reader form the sharpest mental image?", "Rain hammered the tin roof as lightning split the black sky.", ["It was a bad night.", "The weather was bad.", "There was a storm."], "Specific sensory details create images.")
H('5.D', 3, "A reader sketches a setting from a description in the text. This helps the reader...", "understand and remember details", ["skip passages", "change the plot", "avoid the theme"], "Visualizing deepens comprehension.")
H('5.D', 4, "Which phrase most strongly supports picturing a crowded market?", "voices overlapped as vendors shouted over piles of fruit", ["there were people", "the market existed", "some stalls stood there"], "Sensory and action details create imagery.")

# ---- 5.E connections
H('5.E', 3, "A reader compares a character's fear of speaking in public with her own. This is a connection to...", "personal experience", ["another text", "society", "the glossary"], "Text-to-self.")
H('5.E', 3, "A novel about a plague reminds a student of a documentary about disease. This is a connection to...", "another text", ["personal experience", "the author's hobbies", "a recipe"], "Text-to-text.")
H('5.E', 4, "A story about unfair labor laws makes a student think about today's workplace rules. This is a connection to...", "society", ["only the characters", "only the font", "the author's name"], "Text-to-world.")

# ---- 5.F inferences
H('5.F', 3, "'Marcus kept checking his phone and tapping his foot. When the door opened he jumped to his feet.' What can be inferred?", "Marcus was anxiously waiting for someone", ["Marcus was bored by a lecture", "Marcus was asleep", "Marcus was baking"], "His actions show anticipation.")
H('5.F', 3, "'The small boat bobbed in the harbor, its paint peeling and its ropes frayed.' What can be inferred?", "the boat is old and not well kept", ["the boat is brand new", "the boat is racing", "the boat is full of passengers"], "Peeling paint and frayed ropes show neglect.")
H('5.F', 4, "'Nadia hung her medals in the closet and quietly stopped going to practice.' Which inference is best supported?", "Nadia may have lost interest or confidence in the sport", ["Nadia won a national title", "Nadia is moving to a new house", "Nadia is practicing more"], "Hiding medals and quitting practice suggest withdrawal.")

# ---- 5.G key ideas
H('5.G', 3, "Which detail is least important to the key idea of an article about solar power's benefits?", "the photographer's name", ["solar power lowers electric bills", "solar panels reduce pollution", "sunlight is renewable"], "Details about the photographer don't support the key idea.")
H('5.G', 3, "A key idea is the...", "most important point the author makes", ["longest sentence", "first word", "title's font"], "It captures what matters most.")
H('5.G', 4, "An article gives several examples of animals adapting to deserts. The key idea is probably that...", "living things adapt to survive in harsh environments", ["deserts are cold", "animals are all the same", "adapting is impossible"], "Details illustrate adaptation.")

# ---- 5.H synthesis
H('5.H', 3, "Two sources describe different causes of a city's growth. A student combines the causes into a new explanation. This is...", "synthesis", ["plagiarism", "guessing", "copying"], "Combining info creates new understanding.")
H('5.H', 4, "Source 1 says electric cars cut air pollution. Source 2 says battery production uses scarce minerals. Which synthesis is best?", "electric cars have environmental benefits but also costs to consider", ["electric cars have no effect", "the sources agree exactly", "cars should never be built"], "A balanced new idea.")
H('5.H', 4, "Which sentence is a synthesis of an interview and a chart?", "The interview and chart together show that rising prices have hurt local farmers.", ["The interview was recorded.", "The chart has three colors.", "The farmer wore a hat."], "It draws a conclusion from both sources.")

# ---- 5.I monitoring
H('5.I', 3, "A reader realizes she cannot recall what she just read. Which adjustment is best?", "slow down and re-read the confusing section", ["read the next page faster", "close the book", "skip to the end"], "Re-reading repairs comprehension.")
H('5.I', 3, "Using background knowledge while reading means...", "connecting what you already know to the text", ["ignoring new facts", "reading only the title", "counting paragraphs"], "Prior knowledge aids understanding.")
H('5.I', 4, "A reader stops after each page to summarize it in one sentence. This strategy helps the reader...", "check understanding as she reads", ["avoid the main idea", "memorize the page numbers", "skip hard words"], "Summarizing monitors comprehension.")

# ---- 6.C evidence
H('6.C', 3, "Claim: 'The mayor was well liked.' Which text evidence best supports it?", "Crowds lined the streets to cheer as she passed.", ["The parade started at noon.", "The street was named Main.", "She wore a blue coat."], "Cheering crowds show popularity.")
H('6.C', 4, "A student claims a character is brave but quotes only the character's name. Why is this weak?", "a name does not show bravery", ["names are too long", "quotes must be long", "claims need no evidence"], "Evidence must show the trait.")
H('6.C', 3, "Which choice is a strong example of citing text evidence?", "The text says, 'She stood alone against the crowd,' showing her courage.", ["I like the book.", "The book is long.", "It was a good story."], "Evidence is a specific quotation tied to the claim.")

# ---- 6.D summarize
H('6.D', 3, "Which is the best one-sentence summary of a passage about how bees make honey and pollinate crops?", "Bees produce honey and also help plants reproduce by pollinating them.", ["Bees are insects.", "Honey is sweet.", "Crops grow in fields."], "It covers both main ideas.")
H('6.D', 3, "A summary should keep ideas in a logical order. If events happened first, second and third, the summary should...", "present them in the same order", ["reverse them", "mix them randomly", "leave out the first"], "Logical order maintains meaning.")
H('6.D', 4, "Which sentence is a paraphrase of 'The committee postponed the vote until further data was available'?", "The group delayed the vote while waiting for more information.", ["The committee voted yesterday.", "The data was lost.", "The vote was canceled forever."], "Paraphrase keeps the same meaning.")

# ---- 6.G explicit/implicit
H('6.G', 3, "'Every light in the house went out, and the whole family fell silent.' What is the implicit meaning?", "the family feels fear or surprise", ["the family is celebrating", "the family is cooking", "the family is asleep"], "Silence in the dark suggests tension.")
H('6.G', 3, "Which statement gives an explicit meaning?", "The text says the cave is a mile long.", ["The reader guesses the cave is haunted.", "The reader feels the cave is scary.", "The cave seems sad."], "Explicit meanings are directly stated.")
H('6.G', 4, "'By the end of the week, Ali's lunch table was always empty.' Which implicit meaning is most likely?", "Ali has become isolated from classmates", ["Ali made many friends", "Ali joined the choir", "Ali loves lunch"], "The empty table implies loneliness.")

# ---- 7.A themes
H('7.A', 3, "A character cheats to win, loses his friends, and regrets it. Which theme is supported?", "dishonesty can cost you what you value", ["cheating is clever", "winning is everything", "friends are unimportant"], "The consequences reveal the theme.")
H('7.A', 4, "Two poems both describe a storm clearing and new growth. What theme appears across both?", "renewal follows hardship", ["storms are loud", "gardens need fences", "rain is bad"], "A shared message.")
H('7.A', 4, "Which statement is a theme rather than a topic?", "Courage means acting even when you are afraid.", ["Courage", "A story about a firefighter", "Fire trucks"], "A theme is a complete message.")

# ---- 7.B character qualities
H('7.B', 3, "A stubborn character refuses advice and ends up lost. How does her quality affect the plot?", "it leads to the conflict", ["it ends the conflict", "it changes the setting", "it removes the theme"], "Traits drive events.")
H('7.B', 3, "A generous character shares his only coat, leading a stranger to help him later. This shows that...", "a character's qualities can shape the resolution", ["setting is unimportant", "the conflict is unrelated", "the title is false"], "Kindness results in help.")
H('7.B', 4, "Which character quality is most likely to cause conflict in a team project?", "refusing to listen to others", ["arriving on time", "sharing the work", "asking for ideas"], "Poor listening creates conflict.")

# ---- 7.C foreshadowing and suspense
H('7.C', 3, "A story mentions early on that the bridge looks weak. Later it collapses. This technique is...", "foreshadowing", ["a flashback", "personification", "alliteration"], "Early hints suggest later events.")
H('7.C', 3, "The author slows the pace by describing the creaking door, one step at a time. This builds...", "suspense", ["a rhyme scheme", "a glossary", "resolution"], "Slow detail increases tension.")
H('7.C', 4, "Which sentence best foreshadows trouble?", "Dark clouds gathered, and the dog refused to leave the porch.", ["The sun shone brightly all day.", "Lunch was served at noon.", "The grass was green."], "Ominous hints foreshadow a problem.")

# ---- 7.D setting
H('7.D', 3, "A novel is set in a crowded city during a blackout. How could this setting affect the plot?", "it may create obstacles and danger for characters", ["it ensures nothing happens", "it removes conflict", "it makes the story a poem"], "Setting shapes events.")
H('7.D', 3, "A boy from a farming town struggles in a big city. This shows how setting influences a story's...", "character", ["rhyme", "stanza", "caption"], "Environment shapes behavior.")
H('7.D', 4, "How does a story set on a spaceship with limited oxygen most likely drive the plot?", "limited resources create urgent choices", ["time has no meaning", "the crew has no problems", "the setting is irrelevant"], "Constraints create conflict.")

# ---- 8.A genres
H('8.A', 3, "A story about teenagers handling school pressure and friendship in everyday life is...", "realistic fiction", ["science fiction", "a fable", "a myth"], "Set in a believable world.")
H('8.A', 3, "A story with talking animals that ends in a moral is most likely a...", "fable", ["biography", "news report", "diary"], "Fables use animals to teach lessons.")
H('8.A', 4, "A story set in a future with advanced technology and space travel is...", "science fiction", ["historical fiction", "a biography", "realistic fiction"], "Imagined science and future settings.")

# ---- 8.B poetry
H('8.B', 3, "A poem's stanzas end with the pattern ABAB. This describes its...", "rhyme scheme", ["meter", "setting", "plot"], "The ending-sound pattern is the rhyme scheme.")
H('8.B', 3, "A poet capitalizes a single word to draw attention to it. This is a...", "graphical element for emphasis", ["rhyme", "footnote", "stage direction"], "Formatting can emphasize.")
H('8.B', 4, "A poem uses short, choppy lines and many dashes. What effect could this create?", "a sense of urgency or hesitation", ["a calm lullaby", "a long narrative", "a table of data"], "Punctuation and line length affect rhythm.")

# ---- 8.C drama
H('8.C', 3, "In a script, how can a playwright show a character is nervous?", "through stuttering lines and pacing stage directions", ["through an index", "through a footnote", "through a glossary"], "Dialogue and staging show traits.")
H('8.C', 3, "An aside in a play is a moment when a character...", "speaks to the audience unheard by others", ["leaves the stage forever", "sings the final song", "reads the stage directions"], "Asides reveal private thoughts.")
H('8.C', 4, "A playwright places two rivals at opposite ends of a long table. What does this staging suggest?", "distance and conflict between them", ["friendship", "a flashback", "a rhyme"], "Space reveals relationships.")

# ---- 8.F multimodal
H('8.F', 3, "A news website shows an article, a short video and an interactive graph. This is a...", "multimodal text", ["limerick", "memoir", "folktale"], "It uses text, video and graphics.")
H('8.F', 3, "How can a podcast with a transcript help a reader?", "by offering both audio and written information", ["by avoiding facts", "by removing words", "by blocking pages"], "Multiple modes support access.")
H('8.F', 4, "Which question helps analyze a digital advertisement?", "How do images, color and text work together to persuade?", ["What size is the screen?", "Who made the cursor?", "How many pixels wide is the logo?"], "Analysis examines how elements work together.")

# ---- 8.D.i
H('8.D.i', 3, "Which detail best supports the thesis 'Teens need more sleep'?", "Studies show teens focus better after nine hours of rest.", ["Pillows are soft.", "Some beds are tall.", "The sun rises early."], "Evidence supports the thesis.")
H('8.D.i', 3, "The thesis of an essay usually appears...", "in the introduction", ["only in the index", "on the copyright page", "after the glossary"], "A thesis is stated early.")
H('8.D.i', 4, "A paragraph includes a claim, a statistic and an example. These details are used to...", "support the controlling idea", ["replace the thesis", "avoid evidence", "confuse the reader"], "Evidence supports the main point.")

# ---- 8.D.ii references and acknowledgements
H('8.D.ii', 3, "Where would a reader find the sources an author used?", "the references page", ["the preface only", "the title", "the cover art"], "References list sources.")
H('8.D.ii', 3, "An acknowledgements page is used to...", "thank people who helped the author", ["list definitions", "show maps", "give page numbers"], "Authors thank helpers.")
H('8.D.ii', 4, "Why does an author include references?", "to credit sources and let readers verify information", ["to hide the evidence", "to add rhymes", "to shorten the text"], "References show credibility.")

# ---- 8.D.iii organizational patterns
H('8.D.iii', 3, "A textbook chapter has headings and subheadings that group ideas by category. This pattern helps readers...", "see how topics and subtopics relate", ["skip details", "avoid evidence", "read backward"], "Hierarchy shows organization.")
H('8.D.iii', 3, "A text lists causes of the Dust Bowl and then its effects. The pattern is...", "cause and effect", ["classification only", "poetry", "dialogue"], "It shows why and what happened.")
H('8.D.iii', 4, "A passage describes three types of rocks, then breaks each type into examples. This is an example of...", "categories and subcategories", ["chronological order", "problem and solution", "persuasion"], "It groups and subdivides.")

# ---- 8.E.i claim
H('8.E.i', 3, "Which sentence states a claim a writer could argue?", "Schools should require uniforms.", ["Uniforms are sold in stores.", "Some uniforms are blue.", "Uniforms have buttons."], "A claim is a debatable position.")
H('8.E.i', 3, "A claim is different from a fact because a claim...", "can be argued", ["cannot be questioned", "is always false", "is a quotation"], "Claims are debatable.")
H('8.E.i', 4, "Which statement is a claim about technology?", "Phones should be allowed in class for research.", ["Phones have screens.", "Phones are made of glass.", "Phones were invented before 2020."], "It takes a debatable position.")

# ---- 8.E.ii evidence and alternatives
H('8.E.ii', 3, "An author acknowledges the opposing view and explains why it is weaker. This is called...", "addressing a counterargument", ["telling a joke", "foreshadowing", "personification"], "Considering alternatives strengthens an argument.")
H('8.E.ii', 3, "Which type of evidence is an expert's opinion?", "testimony", ["a statistic", "a rhyme", "a map"], "Experts give testimony.")
H('8.E.ii', 4, "Why does an author include both facts and examples?", "to support the claim in different ways", ["to confuse the reader", "to avoid the topic", "to shorten the argument"], "Variety strengthens evidence.")

# ---- 8.E.iii audience
H('8.E.iii', 3, "A pamphlet explains 'How to Start Saving Your Allowance' with simple words and cartoons. The intended audience is probably...", "young students", ["bank executives", "retirees", "lawyers"], "Simple wording and cartoons target kids.")
H('8.E.iii', 4, "A journal article full of technical terms about medicine is aimed at...", "medical professionals", ["young children", "pet owners", "tourists"], "Specialized vocabulary signals experts.")
H('8.E.iii', 3, "An editorial addressed 'Dear voters of our district' is aimed at...", "citizens who can vote", ["only athletes", "toddlers", "visitors"], "The address names the audience.")

# ---- 9.A purpose
H('9.A', 3, "A text with the headline 'Why You Should Volunteer This Summer' is mainly written to...", "persuade", ["entertain with jokes", "narrate a story", "describe a mountain"], "It tries to convince.")
H('9.A', 3, "A comic story meant to make readers laugh has the purpose of...", "entertaining", ["informing with data", "persuading voters", "warning of danger"], "Humor entertains.")
H('9.A', 4, "A biography of a scientist ends with how her work changed medicine. What message does the author most likely send?", "one person's work can have lasting impact", ["science is unimportant", "medicine never changes", "scientists work alone"], "The ending highlights the significance.")

# ---- 9.B structure
H('9.B', 3, "An author organizes an article as problem, then solutions. How does this support the purpose?", "it helps the reader understand and consider actions", ["it hides the problem", "it removes evidence", "it makes it a poem"], "Structure matches the purpose.")
H('9.B', 4, "A writer uses flashbacks in a mystery. How does this structure help the purpose?", "it reveals important background at key moments", ["it removes suspense", "it makes the plot linear", "it ends the story"], "Flashbacks add information.")
H('9.B', 3, "A text arranged in order of importance helps readers...", "focus on the key points first", ["ignore the main idea", "read backward", "avoid details"], "Structure guides attention.")

# ---- 9.C print features
H('9.C', 3, "A sidebar in a magazine article is used to...", "provide extra related information", ["end the article", "replace the title", "hide the evidence"], "Sidebars add detail.")
H('9.C', 3, "Why might an author use a graph in an article about rising temperatures?", "to show trends clearly", ["to add rhymes", "to tell a joke", "to list rules"], "Graphs show data visually.")
H('9.C', 4, "An author puts a key quote in large type at the edge of a page. This is called a pull quote, and its purpose is to...", "catch the reader's attention and highlight a main idea", ["hide the main idea", "list sources", "end the article"], "Pull quotes emphasize.")

# ---- 9.D figurative
H('9.D', 3, "'The city never sleeps' is an example of...", "personification", ["simile", "alliteration", "onomatopoeia"], "A city is given human action.")
H('9.D', 3, "'Her smile was as bright as the morning sun' is a...", "simile", ["metaphor", "idiom", "hyperbole"], "Uses 'as' to compare.")
H('9.D', 4, "'My backpack weighs a ton' is an example of...", "hyperbole", ["simile", "metaphor", "irony"], "Exaggeration for effect.")

# ---- 9.E point of view
H('9.E', 3, "A text that presents facts without personal feelings uses which kind of point of view?", "objective", ["subjective", "first-person emotional", "persuasive"], "Objective accounts avoid opinion.")
H('9.E', 3, "A narrator who shares personal feelings and opinions about events is using a...", "subjective point of view", ["objective point of view", "scientific method", "table of contents"], "Subjective views reveal feelings.")
H('9.E', 4, "A news report states what happened without opinion words. A blog post says the same event was 'a disaster.' Which uses a subjective point of view?", "the blog post", ["the news report", "both equally", "neither"], "'A disaster' is an opinion.")

# ---- 9.F mood, voice, tone
H('9.F', 3, "An author writes a letter that is formal and respectful. The tone is...", "serious and polite", ["silly", "angry", "sarcastic"], "Word choice reveals tone.")
H('9.F', 3, "Which word choice creates a hopeful tone?", "bright", ["bleak", "gloomy", "dreary"], "Positive words set a hopeful tone.")
H('9.F', 4, "An author uses short sentences and sharp words like 'snapped' and 'slammed.' What tone is created?", "tense or angry", ["relaxed", "dreamy", "playful"], "Sharp diction creates tension.")

# ---- 9.G rhetorical devices
H('9.G', 3, "A speaker says 'You can make a difference today.' This is an example of...", "direct address", ["flashback", "simile", "onomatopoeia"], "The speaker addresses the audience directly.")
H('9.G', 3, "'Who wouldn't want cleaner air?' is a...", "rhetorical question", ["factual question needing an answer", "statistic", "definition"], "It makes a point and needs no reply.")
H('9.G', 4, "'If we allow one exception, soon there will be no rules at all' is an example of...", "a slippery slope fallacy", ["a statistic", "a simile", "a primary source"], "It assumes one step leads to extreme results.")

# ---- 10.B organization and development
H('10.B.i', 3, "Which sentence would best begin the conclusion of an essay?", "In conclusion, regular reading builds vocabulary and focus.", ["Reading is on page two.", "My dog likes treats.", "The first paragraph is below."], "Conclusions restate the main idea.")
H('10.B.i', 4, "A writer jumps from a paragraph about sports to one about cooking with no connection. What is missing?", "a transition and coherence between paragraphs", ["a longer title", "more adjectives", "a different font"], "Transitions link ideas.")
H('10.B.ii', 3, "Which revision adds specific detail to 'The food was good'?", "The tacos were warm, crisp and loaded with fresh salsa.", ["The food was fine.", "The food existed.", "I had food."], "Specifics develop an idea.")
H('10.B.ii', 4, "Which sentence best develops the idea 'Exercise improves health'?", "Daily exercise lowers blood pressure and strengthens the heart.", ["Exercise is a thing people do.", "Some people exercise.", "Exercise has a name."], "Facts and details deepen the point.")

# ---- 10.C revise
H('10.C', 3, "Which revision removes wordiness from 'Due to the fact that it was raining, we stayed home'?", "Because it was raining, we stayed home.", ["Due to the fact that raining, home.", "It was raining and the reason is that we stayed.", "We stayed because of the fact."], "Concise wording keeps meaning.")
H('10.C', 3, "Which word is the most precise replacement for 'walked' in 'He walked across the stage nervously'?", "shuffled", ["went", "moved", "did"], "Precise verbs clarify action.")
H('10.C', 4, "A writer notices that three sentences in a row start with 'The.' Which revision improves style?", "vary the sentence beginnings and structures", ["add more 'The's", "delete all verbs", "remove the title"], "Variety improves flow.")

# ---- 10.D.i
H('10.D.i', 3, "Which is a comma splice?", "I studied hard, I passed the test.", ["I studied hard, so I passed the test.", "I studied hard; I passed the test.", "Because I studied hard, I passed the test."], "Two independent clauses joined only by a comma.")
H('10.D.i', 3, "Which sentence has correct subject-verb agreement?", "Each of the players has a uniform.", ["Each of the players have a uniform.", "Each of the players are a uniform.", "Each of the players were a uniform."], "'Each' is singular.")
H('10.D.i', 4, "Which is a complete complex sentence?", "When the music stopped, the dancers bowed.", ["When the music stopped.", "The dancers bowed, the music stopped.", "Because the dancers."], "It has a dependent and an independent clause.")

# ---- 10.D.ii
H('10.D.ii', 3, "Which sentence uses verb tenses consistently?", "He opens the door and steps outside.", ["He opens the door and stepped outside.", "He opened the door and steps outside.", "He will open the door and stepped outside."], "Both verbs are in the present tense.")
H('10.D.ii', 3, "Which verb tense shows an action that will happen later?", "future", ["past", "present", "past perfect"], "Will + verb is future.")
H('10.D.ii', 4, "Choose the sentence with a correct past perfect tense.", "By noon, she had finished her homework.", ["By noon, she finish her homework.", "By noon, she has finishing her homework.", "By noon, she will had finished."], "Had + past participle.")

# ---- 10.D.iii conjunctive adverbs
H('10.D.iii', 3, "Which word best joins 'He studied for hours' and 'he failed the test' to show contrast?", "nevertheless", ["therefore", "moreover", "similarly"], "Nevertheless shows contrast.")
H('10.D.iii', 4, "Which sentence punctuates a conjunctive adverb correctly?", "The bus was late; however, we made it on time.", ["The bus was late, however we made it on time.", "The bus was late however; we made it on time.", "The bus was late; however we made it, on time."], "Semicolon before and comma after.")
H('10.D.iii', 3, "Which conjunctive adverb adds information?", "furthermore", ["however", "otherwise", "instead"], "Furthermore adds to an idea.")

# ---- 10.D.iv
H('10.D.iv', 3, "Choose the correct verb: 'The list of ingredients ____ long.'", "is", ["are", "were", "be"], "The subject 'list' is singular.")
H('10.D.iv', 4, "Choose the correct verb: 'The students in the back row ____ talking.'", "are", ["is", "was", "be"], "The subject 'students' is plural.")
H('10.D.iv', 3, "Which word group is a prepositional phrase?", "in the green boat", ["rowed quickly", "the boy ran", "and then left"], "Preposition plus object.")

# ---- 10.D.v pronoun-antecedent
H('10.D.v', 3, "Choose the correct pronoun: 'Each student must bring ____ own book.'", "his or her", ["their-selves", "they", "our"], "Singular antecedent needs a singular pronoun.")
H('10.D.v', 3, "What is the antecedent of a pronoun?", "the noun the pronoun refers back to", ["the verb that follows it", "the last word of the sentence", "the punctuation mark before it"], "An antecedent is the word a pronoun replaces.")
H('10.D.v', 4, "Which sentence has correct pronoun-antecedent agreement?", "The team celebrated its victory.", ["The team celebrated their victory loudly together alone.", "The team celebrated they victory.", "The team celebrated his and her victories."], "Collective noun treated as one unit.")

# ---- 10.D.vi
H('10.D.vi', 3, "Which pair completes the sentence: '____ the movie ____ the book was good'?", "Neither / nor", ["Either / and", "Both / or", "Not only / but or"], "Correlative pair neither/nor.")
H('10.D.vi', 3, "Which word is a subordinating conjunction?", "although", ["and", "but", "so"], "Although begins a dependent clause.")
H('10.D.vi', 4, "Which sentence correctly uses a subordinating conjunction?", "Since it was late, we left early.", ["Since it was late we, left early.", "Since, it was late we left early.", "Since it was late, and we left early."], "A comma follows the introductory clause.")

# ---- 10.D.vii capitalization
H('10.D.vii', 3, "Which word group needs capital letters?", "the Pacific Ocean", ["a large lake", "the nearby hills", "an old river"], "Specific geographic names are capitalized.")
H('10.D.vii', 3, "Which of these should be capitalized in a sentence?", "Senator Alvarez", ["a senator", "the senators", "any senator"], "Titles before names are capitalized.")
H('10.D.vii', 2, "Which word is always capitalized?", "I", ["we", "you", "me"], "The pronoun I is always capitalized.")

# ---- 10.D.viii punctuation
H('10.D.viii', 3, "Which sentence uses a semicolon correctly?", "I like hiking; my brother prefers swimming.", ["I like; hiking my brother prefers swimming.", "I like hiking my brother; prefers swimming.", "I like hiking my; brother prefers swimming."], "A semicolon joins related independent clauses.")
H('10.D.viii', 3, "Which sentence correctly sets off a nonessential phrase with commas?", "My cousin, who lives in Dallas, visited us.", ["My cousin who lives in Dallas, visited us.", "My cousin, who lives in Dallas visited us.", "My, cousin who lives in Dallas visited us."], "Commas surround nonessential information.")
H('10.D.viii', 4, "Which list is punctuated correctly?", "We packed tents, flashlights, and sleeping bags.", ["We packed, tents flashlights, and sleeping bags.", "We packed tents flashlights and, sleeping bags.", "We packed tents, flashlights and, sleeping bags."], "Commas separate items in a series.")

# ---- 10.D.ix spelling
H('10.D.ix', 2, "Which sentence uses the correct form?", "It's time to go home.", ["Its time to go home.", "Its' time to go home.", "It time to go home."], "It's means it is.")
H('10.D.ix', 3, "Choose the correct word: 'The ____ of the new rule was positive.'", "effect", ["affect", "affects", "effects-on"], "Effect is a noun meaning result.")
H('10.D.ix', 3, "Which word is spelled correctly?", "necessary", ["neccessary", "necesary", "necessery"], "One c, two s.")

# ---- 12.E / 12.G / 12.H
H('12.E', 3, "A letter written by a soldier in 1944 is a...", "primary source", ["secondary source", "textbook", "encyclopedia"], "Firsthand documents are primary.")
H('12.E', 4, "A student needs a secondary source about the Great Depression. Which fits?", "a history book written in 2015", ["a photograph from 1932", "a diary from 1931", "a newspaper from 1930"], "Secondary sources analyze primary ones.")
H('12.E', 3, "An interview recorded with a witness of an event is a...", "primary source", ["secondary source", "textbook", "dictionary"], "A firsthand account.")
H('12.G', 3, "Rewriting a source's idea in your own words and crediting it is...", "ethical paraphrasing", ["plagiarism", "stealing", "forgery"], "Credit keeps it ethical.")
H('12.G', 3, "Which is plagiarism?", "turning in a classmate's essay as your own", ["quoting with credit", "summarizing with a citation", "paraphrasing and citing"], "Passing off others' work is plagiarism.")
H('12.G', 4, "A student copies a paragraph and changes only three words without citing. This is still...", "plagiarism", ["paraphrasing", "synthesis", "summarizing"], "Minor word changes are not enough.")
H('12.H.i', 3, "Which website is most reliable for scientific data on weather?", "a national weather service", ["an anonymous forum", "a celebrity gossip blog", "an online ad"], "Government science agencies are credible.")
H('12.H.i', 4, "A reader finds an article with no author, no date and no sources. What should the reader conclude?", "the article may not be credible", ["the article is probably perfect", "dates don't matter", "sources are optional"], "Missing details reduce credibility.")
H('12.H.i', 3, "Bias in a source means the source...", "favors one side unfairly", ["is always true", "is written by an expert", "is balanced"], "Biased sources lack balance.")
H('12.H.ii', 3, "'Everyone knows this phone is the best' is an example of...", "an unsupported claim or bandwagon appeal", ["a statistic", "a primary source", "a definition"], "It relies on popularity, not evidence.")
H('12.H.ii', 4, "A commercial shows a happy family to sell cereal but gives no nutrition facts. This is a(n)...", "emotional appeal", ["statistic", "scientific study", "primary source"], "It appeals to feelings.")
H('12.H.ii', 4, "'Those people never follow the rules' about an entire group is an example of...", "a stereotype", ["a fact", "a quotation", "a metaphor"], "A broad unfair generalization.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g7_ela.jsonl'))
print("saved", len(B.out), "questions")

#!/usr/bin/env python3
"""ELA K-5 gap fill (TEKS 110.2-110.7.b): foundational decoding/spelling, alphabetizing, a few comprehension/writing standards that had no question."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('110.', 907, own='gap_ela.jsonl')

load(B, """
# ---- Kindergarten
2.b.10.A|1|Before writing about your pet, what can you do first to get ideas?|talk about it and draw a picture|erase the paper|throw away the pencil|close the book|Ideas come from talking and drawing.
2.b.10.B|1|You draw three pictures to tell a story about a picnic. What should you do next to organize your ideas?|put the pictures in order|cut the paper into bits|hide the pictures|paint the table|Order shows what happens first, next, last.
2.b.10.D.ix|1|Which spelling of the little word that often comes before a noun, like "__ cat," is correct?|the|tha|thu|thee|The is a common word to know by sight.
2.b.10.D.ix|1|Which spelling of the word that tells what someone spoke, like "She __ hello," is correct?|said|sed|sayd|sad|Said is a high-frequency word.
2.b.6.B|1|After you hear a story about a bear, which is a good way to show you understood it?|draw the bear and tell what happened|cover your ears|walk away|sing a different song|A drawing and a retelling show understanding.
2.b.6.E|1|A good way to remember a new story is to...|draw a picture of your favorite part|tear the book|forget the pictures|hide the pages|Illustrating helps you interact with the story.
2.b.6.F|1|Your teacher teaches you the new word "enormous." Which sentence uses it?|The elephant is enormous.|The ant is enormous and tiny.|I enormous the book.|Enormous is a red dog.|It means very big.
2.b.11.A|1|A personal narrative tells about...|something that happened to you|a made-up dragon only|a list of numbers|a recipe card|Personal means about you.
2.b.11.B|1|Which sentence could be in an informational text about frogs?|Frogs lay eggs in water.|Once upon a time, a princess slept.|Hooray for cake!|My sock is lost.|It gives true facts.
# ---- Grade 1
3.b.11.A|2|Which idea could you draw or brainstorm before writing about a trip to the park?|swings, slide, and picnic|math facts|rain boots on a shelf|a spelling test|Ideas that fit the topic.
3.b.2.C.ii|2|Which spelling is right for the word a red sign tells drivers to do?|stop|stap|stope|stopp|Initial consonant blend st.
3.b.2.C.ii|2|Which spelling is right for a small piece of a potato or cookie?|chip|cip|chipp|shipp|The digraph ch is at the start.
3.b.2.C.ii|2|Which spelling is right for what happens when you jump into a puddle?|splash|sblash|splach|spalsh|The trigraph spl begins the word.
3.b.2.C.iii|2|Which spelling is right for water that falls from clouds?|rain|rane|rayn|rainn|The ai vowel team spells long a.
3.b.2.C.iii|2|Which spelling is right for something that floats on a lake?|boat|bote|bowt|boate|The oa vowel team spells long o.
3.b.2.F|2|When you print a sentence, what should you leave between words?|a small space|a big drawing|a number|nothing|Spaces make words easy to read.
3.b.7.B|2|After reading a book about a puppy, which comment is a brief written comment?|I like the puppy because it plays.|Puppies.|Page seven.|The end of the bus.|It states a thought about the book.
3.b.7.E|2|While reading, a child writes one word on a sticky note about each page. This is...|interacting with the text|losing the book|a spelling test|a joke|Writing on notes is interacting.
3.b.7.F|2|You learned the word "gigantic." Which sentence uses it right?|The whale is gigantic.|The mouse is gigantic and small.|I gigantic my lunch.|Gigantic is a color.|It means huge.
3.b.11.D.x|2|Which spelling is right for a person you like and play with?|friend|frend|freind|frind|Friend has ie.
3.b.11.D.x|2|Which spelling is right for the word that asks about a place, like "__ is my hat?"|where|wher|ware|wear|Where asks about a place.
3.b.11.E|2|When you share your finished writing, you...|read it to the class|hide it forever|erase it all|tear the paper|Sharing means showing others.
# ---- Grade 2
4.b.11.A|2|Which strategy is useful before drafting a story about a rainy day?|brainstorm words like puddles, umbrella, and thunder|memorize page numbers|erase the first draft|color the cover|Brainstorming gathers ideas.
4.b.11.D.xi|2|Which spelling is right for the word that starts a reason, like "I smiled __ I was happy"?|because|becuz|becase|becaus|Because is a common word.
4.b.11.D.xi|2|Which spelling is right for the word that means one more time?|again|agen|agin|agane|Again ends with ain.
4.b.11.E|2|Why do writers publish and share their writing?|so others can read it|to hide it|to lose it|to count pages|Publishing shares with readers.
4.b.2.A.i|2|Which word rhymes with "light"?|night|lit|lift|late|Night ends with the same sound.
4.b.2.A.i|2|Which word rhymes with "game"?|name|gum|gem|gain|Name ends with ame.
4.b.2.A.ii|2|Which word has a long i sound, like the word for a two-wheeled ride?|bike|bit|bat|but|Bike has a long i.
4.b.2.A.ii|2|Which word has a short o sound, like where ducks swim?|pond|pole|pane|pine|Pond has a short o.
4.b.2.C.i|2|Which spelling is right for a machine that can move and do jobs?|robot|robbot|rowbot|roabot|Open and closed syllables ro-bot.
4.b.2.C.i|2|Which spelling is right for the body parts you wear shoes on?|feet|fete|feat|fiet|Vowel team ee spells long e here.
4.b.2.C.ii|2|Which word is spelled correctly with a silent letter?|knife|nife|knyfe|nyfe|Knife begins with a silent k.
4.b.2.C.ii|2|Which tiny biting insect word starts with a silent letter?|gnat|gate|goat|get|Gnat starts with a silent g.
4.b.2.C.iv|3|Which spelling is right for the huge gray animal with a trunk?|elephant|elefant|elaphant|elephent|Ph makes the f sound.
4.b.2.C.v|3|Which spelling is right for a hopping pet with long ears?|rabbit|rabit|rabbet|rabbitt|Double the b in the middle.
4.b.2.C.v|3|Which spelling is right for the hottest season of the year?|summer|sumer|sommer|sumner|The middle has double m.
4.b.2.C.vi|2|Which spelling is right for the word that means to open a lock?|unlock|unloc|onlock|unlok|Un- plus lock.
4.b.2.C.vi|2|Which spelling is right for the word that means to play again?|replay|reeplay|riplay|replai|Re- plus play.
4.b.2.C.vi|2|Which is the correct spelling of the plural of "box"?|boxes|boxs|boxies|boxz|Words ending in x add es.
4.b.2.D|2|Which list is in alphabetical order?|cat, dog, fish, hen|dog, cat, fish, hen|hen, fish, dog, cat|fish, cat, hen, dog|C comes before d, f, and h.
4.b.2.D|2|Which word comes first in a dictionary?|apple|banana|cherry|date|A comes before b, c, and d.
4.b.7.E|2|A reader writes a note in the margin that says "Why did she run?" This is...|asking a question while reading|spelling a word|drawing a map|a title|Questions help a reader interact.
4.b.7.F|2|After learning "predict," which sentence uses it correctly?|I predict it will rain tomorrow.|I predict my shoes.|The cat predicted blue.|Predict is a chair.|Predict means to say what will happen.
4.b.9.F|2|A story you read on a tablet that has sound and tap-to-play pictures is...|a digital text|a printed book only|a map|a letter|Digital texts can have sound and links.
# ---- Grade 3
5.b.2.A.i|3|Which word has the vowel pattern eigh?|weigh|week|wig|wait|Weigh uses eigh.
5.b.2.A.i|3|Which word has the ough pattern?|though|thing|thin|them|Though ends with ough.
5.b.2.A.ii|3|Which word has the r-controlled vowel or, like the place where two walls meet?|corner|candle|monkey|window|Corner has or.
5.b.2.A.ii|3|Which word with a vowel team names something that floats and carries people?|boat|bat|bet|bit|Boat has oa.
5.b.2.A.iii|3|Which is a compound word?|sunflower|tractor|garden|window|Sun plus flower.
5.b.2.A.iii|3|What is the contraction for "did not"?|didn't|dint|din't|didnt'|The apostrophe replaces the o.
5.b.2.A.iv|4|Which is the correct way to divide a VCCV word into syllables?|pen-cil|pe-ncil|penc-il|p-encil|VCCV words split between consonants.
5.b.2.A.v|3|Which word has the prefix "dis-"?|disagree|dish|disk|discover|Disagree means not agree.
5.b.2.A.vi|3|Which word has the suffix "-less"?|careless|lesson|lessen|least|Careless means without care.
5.b.2.A.vii|2|Which word is a high-frequency word?|would|xylophone|rhinoceros|archipelago|Would appears very often.
5.b.2.B.i|3|Which spelling is right for the word that means to ask someone to a party?|invite|invit|invight|inveit|VCe syllable in vite.
5.b.2.B.ii|3|Which word correctly completes the sentence? "I can ___ the ocean waves."|hear|here|hair|heer|Hear is about listening.
5.b.2.B.iii|3|Which is the correct spelling of the abbreviation for "Street"?|St.|Sts|Str|S.t|It ends with a period.
5.b.2.B.iii|3|Which contraction means "we will"?|we'll|well|we'l|wel'l|The apostrophe replaces wi.
5.b.2.B.iv|3|Which spelling is right for the word that means what you know?|knowledge|nolege|knowlege|nowledge|Knowledge has a silent k.
5.b.2.B.v|3|Which spelling is right for the word that means to take place?|happen|hapen|hapenn|happin|Double p in happen.
5.b.2.B.vi|3|Which spelling is right for the word that means to read a second time?|reread|reeread|riread|rereed|Re plus read.
5.b.2.B.vii|3|Which is the correct spelling of "make" plus -ing?|making|makeing|makking|makin|Drop the e before -ing.
5.b.2.C|2|Which list is in alphabetical order to the third letter?|bad, bat, bay, bed|bat, bad, bay, bed|bay, bat, bad, bed|bed, bad, bat, bay|Compare the third letters.
5.b.2.D|2|When writing in cursive, you should...|connect the letters in each word|print every letter apart|use only capitals|draw pictures|Cursive letters connect.
5.b.7.G|3|In a discussion, which comment shows an important idea from a story about a lost key?|The key stands for the trust the character lost.|My shoes are red.|It is lunchtime.|I like pizza.|It focuses on meaning.
5.b.9.E.ii|3|Which sentence states a fact?|The Earth orbits the Sun.|Summer is the best season.|Dogs are better than cats.|Math is boring.|A fact can be checked.
5.b.9.E.ii|3|Which sentence states an opinion?|Pizza is the tastiest food.|Pizza has cheese.|Pizza is baked in an oven.|Pizza is cut into slices.|Tastiest is a judgment.
5.b.11.A|3|A writer picks a genre for a letter to a friend, a poem, or a story. This step is called...|planning a first draft|publishing|proofreading|illustrating|Choosing genre is planning.
5.b.11.D.xi|3|Which spelling is right for the word for a reply to a question?|answer|anser|anwser|answir|Answer has a silent w.
5.b.11.D.xi|3|Which spelling is right for the word meaning the one you like best?|favorite|favrite|faverit|favorit|Favorite has four syllables in careful speech.
5.b.11.E|3|Why would a student publish a class newsletter?|to share information with readers|to hide it|to erase it|to lose it|Publishing shares work.
# ---- Grade 4
6.b.11.D.xi|3|Which spelling is right for the place where you borrow books?|library|libary|librery|liberry|Library has two r letters.
6.b.11.D.xi|3|Which spelling is right for the word meaning to think something is true?|believe|beleive|belive|beleeve|I before e after l.
6.b.11.E|3|After a student finishes revising and editing a report, the next step might be...|publish it for the audience|erase it|forget it|plan it|Publishing comes after revising.
6.b.2.B.i|3|Which spelling is right for the colorful insect that starts as a caterpillar?|butterfly|butterfli|buterfly|buttirfly|Closed syllables but-ter-fly.
6.b.2.B.iii|4|Which is the correct spelling of the word that tells how heavy something is?|weight|wate|wayt|waight|The eigh pattern spells long a.
6.b.2.B.iv|4|Which spelling is right for the second month of the year?|February|Febuary|Februery|Febrary|Feb-ru-ar-y keeps both r letters.
6.b.2.B.v|3|Which spelling is right for the word meaning to vanish from sight?|disappear|dissappear|disapear|dissapear|Dis plus appear.
6.b.2.C|2|When you write in cursive, which tip helps keep writing legible?|keep letters the same size and slant|write as tiny as possible|press so hard it tears|skip spaces|Even size and slant help.
# ---- Grade 5
7.b.11.D.xi|3|Which spelling is right for the word meaning without a doubt?|definitely|definately|definitly|defanitely|Definitely has finite in it.
7.b.11.D.xi|3|Which spelling is right for the word meaning to get a gift?|receive|recieve|receeve|receve|I before e except after c.
7.b.11.E|3|Why might a student publish an article for the school website?|so the school community can read it|to hide it|to erase it|to delete the website|Publishing reaches an audience.
7.b.2.A.i|4|In "selection," the t in "select" changes to what sound?|sh|k|z|p|Select becomes selection with a /sh/ sound.
7.b.2.A.ii|3|How many syllables are in the word "unforgettable"?|5|3|4|6|Un-for-get-ta-ble.
7.b.2.A.iii|4|Which is the correct syllable division of the word that means 'having great value or meaning'?|im-por-tant|i-mpor-tant|imp-ort-ant|impo-rtant|Divide after the prefix and between consonants.
7.b.2.A.iv|4|Which word has the prefix un- and the suffix -able?|unbreakable|unlock|breakable|reachable|Un- begins it and -able ends it.
7.b.2.A.v|2|Which word is a high-frequency word?|through|photosynthesis|xenophobia|onomatopoeia|Through is very common.
7.b.2.B.i|3|Which spelling is right for the word meaning to have a party for a special day?|celebrate|celabrate|celebrat|selebrate|VCe syllable in brate.
7.b.2.B.ii|4|Which word is spelled correctly for the action of picking something out?|selection|selecshun|selektion|selecsion|The tion ending spells the /sh/ sound.
7.b.2.B.iii|4|Which spelling is right for how hot or cold something is?|temperature|temprature|temperture|tempurature|Four syllables: tem-per-a-ture.
7.b.2.B.iv|4|Which spelling is right for a talk between two people?|conversation|conversasion|converzation|conversashun|The tion ending.
7.b.2.B.v|3|Which spelling is right for the word meaning to get the meaning wrong?|misunderstand|mizunderstand|misunderstan|misunderstund|Mis plus understand.
7.b.2.B.vi|3|Which word is spelled correctly when you add -ness to "happy"?|happiness|happyness|happines|hapiness|Change y to i before -ness.
7.b.2.C|2|Cursive writing is easiest to read when letters are...|joined smoothly and evenly spaced|jammed together|printed apart|different heights|Neatness helps legibility.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'gap_ela.jsonl'))
print("saved", len(B.out), "questions")

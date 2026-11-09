import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('127.', 1118, own='cte_41.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---------- 244 Business Communications ----------
H('244.d.14',3,"Which sentence uses correct capitalization and punctuation?",
  "Our manager, Ms. Lee, approved the budget on Monday.",["Our manager Ms. lee approved the budget on monday.","our Manager, ms. Lee, approved the Budget on Monday","Our manager ms. Lee. approved the budget, on Monday"],"Proper nouns and sentence starts are capitalized; commas set off appositives.")
H('244.d.14',4,"A handwritten note to a client should be legible mainly because:",
  "the client must be able to read and trust the message",["it shortens the message","it removes the need for a signature","it lowers postage"],"Illegible writing blocks communication.")
H('244.d.15',3,"Which spelling is correct in a business email?",
  "receive",["recieve","receeve","riceive"],"The rule 'i before e except after c' applies.")
H('244.d.15',4,"Which sentence contains a spelling error?",
  "Please acknowledge the shipment by Friday and sign the recipt.",["Please acknowledge the shipment by Friday.","The accountant reviewed the receipt.","Our schedule is separate from theirs."],"'Recipt' should be 'receipt'.")
H('244.d.17',3,"Before giving an oral presentation to a client, a speaker should:",
  "rehearse and organize main points",["memorize every word with no notes","avoid eye contact","start without a plan"],"Preparation improves delivery.")
H('244.d.17',4,"During a sales presentation, which speaking technique best keeps the audience engaged?",
  "varying tone and making eye contact",["speaking in a monotone","reading slides word for word","turning away from the audience"],"Engagement requires eye contact and vocal variety.")
H('244.d.18',3,"Three coworkers are preparing a proposal. The team works best when each member:",
  "has a clear role and shares updates",["works alone and hides progress","waits to be told every step","competes with the others"],"Clear roles and updates support teamwork.")
H('244.d.18',4,"A team member keeps missing deadlines. The most productive first response is to:",
  "talk privately to find the cause and agree on a plan",["publicly criticize the member","redo the work silently","ignore it"],"Direct, private discussion solves problems.")
H('244.d.1.A',3,"A professional who writes clear emails and speaks respectfully to customers is demonstrating:",
  "effective oral and written communication",["avoidance","poor planning","careless habits"],"Both skills build business relationships.")
H('244.d.1.A',4,"A supervisor asks you to explain a delayed order to an upset client. The best approach is to:",
  "state the facts calmly and offer a solution",["blame another department","avoid the client","send a vague message"],"Clarity and solutions build trust.")
H('244.d.1.B',3,"Sharing ideas, listening to others, and dividing tasks among classmates on a project shows:",
  "collaboration skills",["working alone","competition","avoidance"],"Collaboration shares work and ideas.")
H('244.d.1.B',4,"A team disagrees about a report layout. The collaborative response is to:",
  "discuss options and agree on one that fits the purpose",["let the loudest voice win","vote without talking","quit the project"],"Consensus serves the goal.")
H('244.d.1.C',3,"Arriving on time, dressing appropriately, and using courteous language in the workplace show:",
  "professionalism",["carelessness","indifference","rebellion"],"Professional conduct fits the setting.")
H('244.d.1.C',4,"A coworker posts a frustrated message about a client on a public page. A professional would:",
  "keep client concerns private and address them through proper channels",["join in the posting","repost it","ignore company policy"],"Confidentiality is professional.")
H('244.d.1.D',3,"Completing assigned tasks fully and on time without constant reminders shows:",
  "a productive work ethic",["procrastination","avoidance","shortcuts"],"Reliability reflects ethic.")
H('244.d.1.D',4,"An employee finishes her work early. A strong work ethic suggests she should:",
  "ask what else needs to be done",["leave quietly","wait idly","distract others"],"Initiative shows ethic.")
H('244.d.1.E',3,"An employee notices an error that benefits the company on a customer's invoice. Integrity means:",
  "correcting the error",["hiding it","keeping the extra money","blaming the customer"],"Honesty requires fixing mistakes.")
H('244.d.1.E',4,"Complying with company policies and laws regarding customer data is part of:",
  "choosing the ethical course of action",["optional behavior","cutting corners","avoiding rules"],"Compliance is ethical conduct.")
H('244.d.1.F',3,"Ranking tasks by urgency and following a calendar shows:",
  "time-management skills",["poor focus","disorganization","delay"],"Prioritizing manages time.")
H('244.d.1.F',4,"Three tasks are due today: a client call, a report due tomorrow, and a weekly filing. The best first step is to:",
  "make the client call first, then schedule the rest by deadline",["file first","wait until evening","skip the call"],"Urgent, time-sensitive items go first.")
H('244.d.2.A',3,"A good email about a product launch should first state the purpose, then give details in:",
  "logical order",["random order","reverse alphabetical order","no order"],"Logical sequencing aids understanding.")
H('244.d.2.A',4,"Which list of steps for training a new hire is in logical sequence?",
  "Welcome, explain duties, demonstrate tasks, assess performance",["Assess performance, welcome, demonstrate, explain","Demonstrate, assess, welcome, explain","Explain, assess, welcome, demonstrate"],"Steps build in order.")
H('244.d.2.B',3,"To find a company's return policy, a worker should:",
  "locate and read the policy in the handbook or website",["guess","ask a stranger","skip it"],"Reading official information is reliable.")
H('244.d.2.B',4,"A written memo says 'effective Monday.' To interpret it, you should check the memo's:",
  "date to know which Monday",["font","logo","paper color"],"Context determines meaning.")
H('244.d.2.C',3,"The statement 'Our product has the highest sales in the region' is a fact only if it:",
  "can be verified with sales data",["sounds convincing","is repeated often","is said by the boss"],"Facts are verifiable.")
H('244.d.2.C',4,"Words like 'I believe' and 'in my view' usually signal:",
  "an opinion",["a fact","a statistic","a law"],"Key words flag opinion.")
H('244.d.2.D',3,"A bar chart shows that sales rose each quarter. This visual helps a reader:",
  "see trends quickly",["hide data","change numbers","avoid reading"],"Charts show patterns.")
H('244.d.2.D',4,"A map in a delivery report is most useful for showing:",
  "locations and distances",["employee ages","profits","interest rates"],"Maps convey geography.")
H('244.d.2.E',3,"Instead of 'a lot of stuff,' a precise report would state:",
  "'250 units of inventory'",["'many things'","'some items'","'a pile'"],"Precision aids clarity.")
H('244.d.2.E',4,"Which sentence is the most concise and clear?",
  "Please submit the form by Friday.",["It would be very much appreciated if you could possibly submit the form at some point near Friday.","Submit form maybe.","Friday is a day, so form."],"Concise wording communicates clearly.")
H('244.d.2.F',3,"A well-written paragraph begins with a topic sentence and then provides:",
  "supporting details",["unrelated jokes","a new topic","blank space"],"Coherent paragraphs develop one idea.")
H('244.d.2.F',4,"Transition words such as 'first,' 'next,' and 'finally' help writing by:",
  "showing the logical progression of ideas",["adding length","removing meaning","hiding errors"],"Transitions guide readers.")
H('244.d.3.A',3,"A student gathers statistics from a company website and a printed journal for a report. She is using:",
  "printed and electronic resources",["only memory","only opinions","no sources"],"Multiple sources support research.")
H('244.d.3.A',4,"Which source is most reliable for current industry statistics?",
  "a government or industry association report",["an anonymous blog","a social media rumor","a friend's guess"],"Credible sources are trustworthy.")
H('244.d.3.B',3,"Restating an author's idea in your own words while giving credit is:",
  "paraphrasing",["plagiarizing","copying","deleting"],"Paraphrasing still requires a citation.")
H('244.d.3.B',4,"Which is an acceptable paraphrase practice?",
  "Rewriting the idea in your own words and citing the source",["Changing one word","Copying a paragraph","Leaving out the source"],"Original wording plus citation is honest.")
H('244.d.3.C',3,"Listing the author, title, publisher, and date of a source is called:",
  "documenting the source",["editing","hiding","formatting only"],"Documentation gives credit.")
H('244.d.3.C',4,"Failing to document a source in a report can lead to:",
  "plagiarism",["extra credit","a longer report","higher accuracy"],"Uncredited use is plagiarism.")
H('244.d.3.D',3,"A group wants to know which snack customers prefer. A useful first step in a survey is to:",
  "write clear, unbiased questions",["ask only friends","skip planning","use leading questions"],"Good questions yield good data.")
H('244.d.3.D',4,"A survey of 100 customers shows 60 prefer option A. What percent prefer A?",
  "60%",["6%","40%","160%"],"60 / 100 = 60%.")
H('244.d.3.E',3,"Before interviewing a business owner for a class project, you should:",
  "prepare questions and schedule a time",["show up unannounced","skip research","ask rude questions"],"Preparation shows respect.")
H('244.d.3.E',4,"After an interview, a good follow-up action is to:",
  "send a thank-you note",["ignore the person","post their answers publicly without permission","lose your notes"],"Gratitude builds relationships.")
H('244.d.3.F',3,"A student creates a report that includes a chart from a spreadsheet and a table from a web page. This is a project that incorporates:",
  "data imported from several sources",["only handwriting","unsupported claims","hidden files"],"Combining sources builds documents.")
H('244.d.3.F',4,"When importing a chart into a report, you should:",
  "cite the data source and check accuracy",["alter the numbers","hide the source","use it without review"],"Credit and verify.")
H('244.d.4.A',3,"For a quick question to a coworker down the hall, the most appropriate telecommunications method is:",
  "an instant message or phone call",["certified mail","a printed memo","a formal letter"],"Fast needs call for fast channels.")
H('244.d.4.A',4,"A manager needs signed approval from a client overseas by tomorrow. Which method is most appropriate?",
  "email with an electronic signature",["standard mail","a postcard","word of mouth"],"Speed and record are needed.")
H('244.d.4.B',3,"When answering a business call, proper etiquette is to:",
  "identify yourself and the company politely",["answer with 'what?'","stay silent","hang up"],"A polite greeting is professional.")
H('244.d.4.B',4,"Using speakerphone in an open office during a confidential call:",
  "violates good etiquette and ethics",["is courteous","is required","is harmless"],"Confidentiality matters.")
H('244.d.5.A',3,"Learning terms such as 'invoice,' 'revenue,' and 'client' builds:",
  "professional vocabulary",["slang","errors","delays"],"Vocabulary supports clarity.")
H('244.d.5.A',4,"In a business meeting, a more professional word for 'buy' might be:",
  "purchase",["grab","snatch","score"],"Formal vocabulary suits business.")
H('244.d.5.B',3,"An effective oral presentation includes an introduction, body, and:",
  "conclusion",["apology","argument","delay"],"Presentations need structure.")
H('244.d.5.B',4,"A speaker's pace is too fast for the audience. She should:",
  "slow down and pause between key points",["speed up","whisper","read faster"],"Pacing aids understanding.")
H('244.d.5.C',3,"A salesperson explaining a product's benefits to a customer is delivering a:",
  "sales presentation",["tax form","resume","memo"],"Sales talks persuade buyers.")
H('244.d.5.C',4,"A manager reviewing quarterly results with the board is giving a:",
  "report presentation",["sales pitch to consumers","training video","press release"],"Reports inform decision makers.")
H('244.d.5.D',3,"When leaving a voicemail for a client, you should state your name, number, and:",
  "the reason for the call",["a joke","a long story","nothing else"],"Clear messages save time.")
H('244.d.5.D',4,"Which is a good phone technique when you must put a caller on hold?",
  "Ask permission and thank the caller for waiting",["Hang up","Leave them silent without asking","Turn off the phone"],"Courtesy matters.")
H('244.d.5.E',3,"After a guest speaker finishes, writing a short summary of the main points shows the ability to:",
  "listen and retain information",["avoid listening","interrupt","ignore detail"],"Summaries show listening.")
H('244.d.5.E',4,"A good summary of a presentation includes:",
  "the key ideas in brief",["every word spoken","only the speaker's name","unrelated opinions"],"Summaries are concise.")
H('244.d.5.F',3,"Nodding and paraphrasing what a client says is:",
  "active listening",["interrupting","daydreaming","ignoring"],"Feedback shows attention.")
H('244.d.5.F',4,"Which response shows active listening?",
  "'So you need the shipment by Tuesday, correct?'",["'Whatever.'","'I wasn't listening.'","'Talk faster.'"],"Repeating confirms understanding.")
H('244.d.5.G',3,"A supervisor gives step-by-step directions for a new filing system. The best response is to:",
  "take notes and ask questions if unclear",["ignore the steps","guess","wait for a reminder"],"Following directions requires attention.")
H('244.d.5.G',4,"If written directions conflict with oral ones, the best action is to:",
  "ask for clarification",["pick one randomly","ignore both","skip the task"],"Clarification prevents errors.")
H('244.d.5.H',3,"Explaining to a new employee how to send a fax or scan a document is giving:",
  "oral instructions",["a performance review","a sales pitch","a press release"],"Oral instructions guide tasks.")
H('244.d.5.H',4,"Clear oral instructions for a simple task should be given:",
  "in order, one step at a time",["all at once","randomly","very fast"],"Sequencing aids learning.")
H('244.d.5.I',3,"During a job interview, a candidate should answer questions:",
  "honestly and clearly",["with exaggeration","with silence","with slang"],"Honesty and clarity impress.")
H('244.d.5.I',4,"A good question for a candidate to ask at the end of an interview is:",
  "'What are the next steps in the hiring process?'",["'How soon can I leave early?'","'Do I have to work?'","'Can I skip training?'"],"Questions show interest.")
H('244.d.6.A',3,"In the communication process, the person who creates and sends a message is the:",
  "sender",["receiver","channel","feedback"],"Senders encode messages.")
H('244.d.6.A',4,"A receiver's response to a message is called:",
  "feedback",["noise","encoding","filtering"],"Feedback completes the loop.")
H('244.d.6.B',3,"Loud machinery that makes a speaker hard to hear is a barrier called:",
  "noise",["feedback","encoding","a channel"],"Noise blocks understanding.")
H('244.d.6.B',4,"Using unexplained technical jargon with customers is a barrier because:",
  "listeners may not understand the terms",["it shortens meetings","it saves time","it lowers cost"],"Jargon confuses non-experts.")
H('244.d.6.C',3,"A company email that falsely claims a product is safe could create:",
  "legal and ethical problems",["no consequences","extra sales only","stronger trust"],"False claims can be unlawful.")
H('244.d.6.C',4,"Before forwarding a client's confidential email to others, a professional should consider:",
  "the privacy and legal implications",["only speed","only length","only font"],"Privacy matters.")
H('244.d.6.D',3,"For a brief reminder to your team, the best channel is likely:",
  "an email or chat message",["a formal printed report","a legal contract","a billboard"],"Match channel to message.")
H('244.d.6.D',4,"A serious personnel matter should usually be communicated through:",
  "a private conversation or formal letter",["a group chat","social media","a bulletin board"],"Sensitive topics need private channels.")
H('244.d.6.E',3,"A customer crosses her arms and frowns while you explain a policy. This nonverbal message may signal:",
  "disagreement or discomfort",["agreement","excitement","joy"],"Body language conveys feelings.")
H('244.d.6.E',4,"Which nonverbal cue most often shows attention?",
  "eye contact",["looking at a phone","turning away","yawning"],"Eye contact shows engagement.")
H('244.d.6.F',3,"A handshake, tone of voice, and posture make up part of the total:",
  "communication message",["tax form","budget","resume"],"Nonverbal cues add meaning.")
H('244.d.6.F',4,"If a speaker's words are friendly but her tone is sarcastic, listeners will likely:",
  "trust the tone over the words",["trust only the words","ignore both","fall asleep"],"Nonverbal cues can override words.")
H('244.d.6.G',3,"One way to improve communication across a company is to:",
  "hold regular team meetings",["ban email","avoid feedback","use unclear jargon"],"Regular meetings keep staff informed.")
H('244.d.6.G',4,"Which step best improves communication between departments?",
  "set up shared updates and clear contacts",["limit contact","keep tasks secret","delay replies"],"Shared updates reduce confusion.")
H('244.d.6.H',3,"In a multicultural business meeting, a common communication problem could be:",
  "different meanings of gestures",["too much clarity","identical customs","no language"],"Gestures vary by culture.")
H('244.d.6.H',4,"To avoid misunderstandings with international partners, a professional should:",
  "learn basic cultural customs and use clear language",["use slang","assume they share customs","speak louder"],"Cultural awareness helps.")
H('244.d.7.A',3,"Using consistent fonts, margins, and headings in a memo is:",
  "formatting a business document",["deleting content","hiding errors","random styling"],"Consistency looks professional.")
H('244.d.7.A',4,"Which memo format is correct?",
  "TO, FROM, DATE, SUBJECT at the top",["Dear Sir at the top","a signature first","no heading"],"Memos have headings.")
H('244.d.7.B',3,"A basic writing assignment such as a short summary should be:",
  "clear, correct, and complete",["long and confusing","full of errors","off topic"],"Basic writing is accurate.")
H('244.d.7.B',4,"Before submitting a short written task, you should:",
  "proofread it",["skip checking","delete half","change the topic"],"Proofreading catches errors.")
H('244.d.7.C',3,"A letter that announces a price increase is an example of a:",
  "negative message",["positive message","persuasive message only","personal note"],"Unwelcome news is negative.")
H('244.d.7.C',4,"A letter that encourages a customer to renew a subscription is a:",
  "persuasive message",["negative message","routine memo","legal notice"],"Persuasion encourages action.")
H('244.d.7.D',3,"A business letter that begins with the main idea and then gives details follows a:",
  "direct organizational pattern",["random pattern","circular pattern","hidden pattern"],"Direct plans put the point first.")
H('244.d.7.D',4,"For bad news, an indirect pattern usually begins with:",
  "a neutral buffer before the news",["the bad news immediately","an insult","nothing"],"Buffers soften delivery.")
H('244.d.7.E',3,"A report with a table of quarterly sales and a chart is a report containing:",
  "text and graphics",["only text","only pictures","blank pages"],"Graphics support text.")
H('244.d.7.E',4,"The best placement for a chart in a report is:",
  "near the text that refers to it",["on the last page for no reason","upside down","hidden"],"Placement aids comprehension.")
H('244.d.7.F',3,"A company newsletter often includes headlines, short articles, and:",
  "photos or graphics",["tax forms","blank pages","passwords"],"Newsletters are visual.")
H('244.d.7.F',4,"Which feature helps readers scan a newsletter?",
  "headings and columns",["tiny fonts","no spacing","one huge paragraph"],"Structure aids scanning.")
H('244.d.8.B',3,"Showing a prospective employer your electronic portfolio is an example of presenting to a:",
  "stakeholder",["competitor","stranger only","bystander"],"Stakeholders have an interest in the work.")
H('244.d.8.B',4,"When presenting a portfolio to an interviewer, you should:",
  "explain how each item shows your skills",["read it silently","skip items","hide weaknesses by lying"],"Explaining adds value.")
H('244.d.8.A.i',3,"An electronic portfolio often begins with a:",
  "resume and cover letter",["tax return","chat log","photo of lunch"],"Core documents introduce the applicant.")
H('244.d.8.A.i',4,"A portfolio resume should be:",
  "current, accurate, and error free",["long and unedited","handwritten only","full of slang"],"Resumes must be polished.")
H('244.d.8.A.ii',3,"Which item would best show your writing ability in a portfolio?",
  "a polished report you wrote",["a selfie","a game score","a grocery list"],"Work samples demonstrate skills.")
H('244.d.8.A.ii',4,"Work samples in an e-portfolio should be:",
  "your own work, labeled with a brief description",["anyone's work","unlabeled","copied from the web"],"Labeled originals are honest.")
H('244.d.8.A.iii',3,"A letter from a supervisor praising your work belongs in your portfolio as:",
  "a letter of recommendation",["a receipt","a bill","spam"],"Recommendations show credibility.")
H('244.d.8.A.iii',4,"Before listing a person as a reference in your portfolio, you should:",
  "ask for their permission",["guess","list them secretly","use a stranger"],"Permission is polite and required.")
H('244.d.8.A.iv',3,"A certificate showing you completed a software course should be included as:",
  "documentation of skills",["junk","a joke","unneeded paper"],"Certifications prove training.")
H('244.d.8.A.iv',4,"Scanning a certificate for your e-portfolio is best saved as:",
  "a PDF or clear image file",["a blurry photo","an unlabeled file","an unreadable format"],"Readable files impress.")
H('244.d.8.A.v',3,"Listing awards and honors in a portfolio shows:",
  "recognized accomplishments",["bragging only","confusion","laziness"],"Awards show achievement.")
H('244.d.8.A.v',4,"An accomplishment should be described in a portfolio with:",
  "the date, the organization, and the result",["only an emoji","no details","exaggerated claims"],"Details make claims credible.")
H('244.d.8.A.vi',3,"Volunteer work and school activities included in a portfolio demonstrate:",
  "leadership and involvement",["avoidance","idleness","selfishness"],"Activities show character.")
H('244.d.8.A.vi',4,"A club office you held can be shown in a portfolio by listing:",
  "your role and what you accomplished",["only the club name","nothing","a rumor"],"Roles and results matter.")
H('244.d.8.A.vii',3,"A professional e-portfolio should be organized with:",
  "clear sections and navigation",["random files","passwords on every page","no titles"],"Organization aids viewers.")
H('244.d.8.A.vii',4,"Before sharing an e-portfolio publicly, you should remove:",
  "private information such as your home address",["your name","all work","the resume"],"Privacy protection is wise.")
H('244.d.9.A',3,"A report that uses headings and subheadings from general to specific shows a:",
  "hierarchical organization",["random order","reverse order","no structure"],"Hierarchy shows relationships.")
H('244.d.9.A',4,"An organizational chart's top-down layout communicates:",
  "levels of authority",["font choices","budget amounts","office hours"],"Hierarchy shows reporting.")
H('244.d.9.B',3,"Headers and bullet points in a manual help readers by:",
  "making information easy to find",["hiding information","adding noise","lengthening text"],"Structure supports clarity.")
H('244.d.9.B',4,"Which format makes a safety procedure clearest?",
  "numbered steps with a bold header",["a single paragraph","random fonts","no spacing"],"Steps need order.")
H('244.d.9.C',3,"A pie chart is most effective for showing:",
  "parts of a whole",["change over time","raw text","phone numbers"],"Pie charts show proportions.")
H('244.d.9.C',4,"A line graph is best for showing:",
  "trends over time",["parts of a whole","names","addresses"],"Lines show change.")
H('244.d.10.A',3,"An ad that shows only young, active customers reflects a social and cultural:",
  "value or assumption",["law","tax","rule"],"Media reflect values.")
H('244.d.10.A',4,"A company changes its ads to include people of many backgrounds. This shows how media can:",
  "respond to changing cultural values",["ignore society","hide products","lower prices"],"Media evolve with culture.")
H('244.d.10.B',3,"A video ad that combines music, images, and text uses:",
  "multi-layered media techniques",["a single technique","silence only","one color"],"Layers add impact.")
H('244.d.10.B',4,"In a layered ad, the soundtrack and visuals together create:",
  "a stronger emotional effect",["no effect","confusion only","less attention"],"Techniques interact.")
H('244.d.10.C',3,"Comparing how a news story is covered on TV, in print, and online helps you see:",
  "differences in emphasis and bias",["no differences","identical coverage","nothing"],"Comparing media reveals framing.")
H('244.d.10.C',4,"A product recall might be shown as minor in a company statement but serious in a news report, which illustrates:",
  "different representation of the same event",["identical coverage","no coverage","a lack of facts"],"Perspective shapes representation.")
H('244.d.10.D',3,"A text to a friend uses casual tone, but a company announcement uses:",
  "formal tone",["slang","emoji only","no tone"],"Formality varies by audience.")
H('244.d.10.D',4,"A brand's social media post is more casual than its annual report because:",
  "the audience and medium differ",["the brand is careless","the law requires slang","it has no editor"],"Medium shapes tone.")
H('244.d.11.A',3,"Before writing, a communicator chooses the genre: for a quick update, a:",
  "short email",["novel","legal brief","poem"],"Genre fits purpose.")
H('244.d.11.A',4,"To formally propose a new project to executives, the best genre is a:",
  "written proposal",["text message","sticky note","tweet"],"Proposals fit formal requests.")
H('244.d.11.B',3,"Making an outline or notes before writing a persuasive message helps you:",
  "organize arguments",["avoid ideas","write less clearly","delay"],"Planning improves persuasion.")
H('244.d.11.B',4,"A persuasive message is stronger when it:",
  "supports claims with evidence",["uses only opinion","avoids detail","insults the reader"],"Evidence persuades.")
H('244.d.11.C',3,"Revising a draft to fix confusing paragraphs and keep a consistent tone is:",
  "improving clarity and organization",["ignoring errors","ending the draft","copying"],"Revision improves meaning.")
H('244.d.11.C',4,"After rereading a draft, you see that two paragraphs repeat the same point. You should:",
  "combine or cut one of them",["add a third copy","ignore it","change the font"],"Eliminate redundancy.")
H('244.d.11.D',3,"Checking a draft for spelling, grammar, and punctuation is:",
  "editing",["revising only","planning","designing"],"Editing polishes mechanics.")
H('244.d.11.D',4,"Which sentence has been edited correctly?",
  "Their team met its goal.",["There team met it's goal.","Thier team met its goal.","Their team met its' goal."],"Correct homophones and apostrophes.")
H('244.d.11.E',3,"A teacher and a classmate suggest changes to your final draft. A good writer will:",
  "consider the feedback and revise",["ignore it","delete the draft","blame the reader"],"Feedback improves quality.")
H('244.d.11.E',4,"Peer feedback is most useful when it is:",
  "specific and respectful",["vague and harsh","only praise","absent"],"Specific feedback guides revision.")
H('244.d.12.A',3,"An analytical essay should include a thesis supported by:",
  "evidence and reasoning",["unrelated stories","opinions only","filler"],"Analysis requires evidence.")
H('244.d.12.A',4,"Which thesis is most suitable for an analytical essay on workplace email?",
  "Email improves workplace communication when used clearly and responsibly.",["Email exists.","I like email.","Email is a thing."],"A thesis takes a supportable position.")
H('244.d.12.B',3,"A one-page summary of your skills used to apply for a job is a:",
  "resume",["proposal","invoice","manual"],"Resumes summarize qualifications.")
H('244.d.12.B',4,"A document that offers a plan to solve a problem and asks for approval is a:",
  "proposal",["resume","newsletter","invoice"],"Proposals recommend solutions.")
H('244.d.12.C',3,"A class news broadcast combining video, audio, and graphics is a:",
  "multimedia presentation",["tax form","text-only memo","blank page"],"Multimedia combines forms.")
H('244.d.12.C',4,"When producing a documentary, students should credit:",
  "all sources and images used",["no one","only music","nothing"],"Credit protects honesty.")
H('244.d.13.A',3,"In the sentence 'The manager who approved the plan left,' the phrase 'who approved the plan' is a:",
  "clause modifying manager",["noun","verb","pronoun"],"It is an adjective clause.")
H('244.d.13.A',4,"In 'She spoke after the meeting ended,' the clause 'after the meeting ended' functions as an:",
  "adverbial clause",["adjectival clause","noun clause","phrase only"],"It tells when she spoke.")
H('244.d.13.B',3,"Which is a compound sentence?",
  "The team met, and the manager approved the plan.",["The team met.","The team that met approved the plan.","After the team met, the plan was approved."],"Two independent clauses joined by 'and' form a compound.")
H('244.d.13.B',4,"Which is a complex sentence?",
  "Because the client called, the manager rescheduled the meeting.",["The client called.","The client called, and the manager came.","The client called; the manager came."],"A dependent clause plus an independent clause is complex.")
H('244.d.16.A',3,"A student gathers facts from several sources to prepare a speech about customer service trends. She is:",
  "synthesizing research",["copying a source","guessing","summarizing one source only"],"Synthesis combines sources.")
H('244.d.16.A',4,"A strong research presentation:",
  "combines sources into an organized argument",["lists unrelated facts","quotes one blog","has no sources"],"Synthesis organizes information.")
H('244.d.16.B',3,"Explaining why a policy is effective, using examples, develops a personal:",
  "opinion supported by analysis",["rumor","fact only","guess"],"Opinions need support.")
H('244.d.16.B',4,"An analysis supports an opinion best when it:",
  "includes evidence and addresses counterpoints",["avoids facts","uses only emotion","ignores other views"],"Balanced analysis is stronger.")
H('244.d.16.C',3,"A speaker uses a story, statistics, and a call to action to persuade an audience. She is using:",
  "rhetorical strategies",["random speech","filler","silence"],"Strategies persuade.")
H('244.d.16.C',4,"Appealing to logic with data in an argument is called:",
  "logos",["pathos","ethos","kairos"],"Logos appeals to reason.")
H('244.d.16.D',3,"A strong argument acknowledges:",
  "opposing viewpoints and addresses them",["only agreement","no evidence","only opinions"],"Complexity strengthens arguments.")
H('244.d.16.D',4,"When sources disagree, a writer should:",
  "explain the discrepancy and evaluate each source",["ignore one","hide the difference","make up data"],"Evaluate credibility.")
H('244.d.16.E',3,"Using a style manual such as MLA or APA ensures:",
  "consistent citation and formatting",["random citations","no citations","hidden sources"],"Style guides standardize format.")
H('244.d.16.E',4,"An in-text citation shows readers:",
  "where the information came from",["the font size","the author's age","the page color"],"Citations credit sources.")
H('244.d.16.F',3,"A business report long enough to address a complex topic fully should include:",
  "an introduction, supporting sections, and a conclusion",["only a title","one sentence","a blank page"],"Length and structure fit complexity.")
H('244.d.16.F',4,"A report is too short to address a complex issue. The writer should:",
  "add evidence and analysis",["add filler","change fonts","reduce margins"],"Depth, not filler, adds value.")

# ---------- 245 Business Information Management II ----------
H('245.d.13',3,"A worker uses a word processor for letters, a spreadsheet for budgets, and a presentation program for pitches. This shows use of:",
  "a variety of software applications",["only one tool","no software","paper tools"],"Different software serves different tasks.")
H('245.d.13',4,"To track expenses and calculate totals automatically, the best application is a:",
  "spreadsheet",["presentation program","drawing program","browser"],"Spreadsheets calculate.")
H('245.d.1.A',3,"Using information systems to give a company an advantage over competitors illustrates their:",
  "strategic role",["minor role","accidental role","irrelevant role"],"IS can support strategy.")
H('245.d.1.A',4,"A company's online ordering system helps it by:",
  "serving customers faster than competitors",["slowing sales","removing customers","increasing paperwork"],"Technology can provide advantage.")
H('245.d.1.B',3,"Investing in a new inventory system costs money but can reduce waste. This illustrates:",
  "risks and rewards",["no change","guaranteed profit","zero cost"],"Strategy involves tradeoffs.")
H('245.d.1.B',4,"One risk of relying heavily on a single information system is:",
  "a failure can halt operations",["lower price","more customers","fewer reports"],"Dependency creates risk.")
H('245.d.1.C',3,"Aligning the IT plan with the company's goals is:",
  "integrating information systems planning with business planning",["ignoring goals","random buying","duplicating work"],"Plans should align.")
H('245.d.1.C',4,"A company plans to expand to new cities. Its IT plan should:",
  "support the expansion with scalable systems",["ignore expansion","limit users","remove software"],"IT must support business goals.")
H('245.d.2.A',3,"A sales manager needs weekly reports on top-selling products. This is a:",
  "management information requirement",["social event","hardware brand","password"],"Managers need data to decide.")
H('245.d.2.A',4,"Identifying business needs before choosing a system helps ensure the system:",
  "meets real requirements",["costs more","has more features unused","is purchased randomly"],"Needs drive selection.")
H('245.d.2.B',3,"Designing a system for a small shop versus a large corporation differs mainly in:",
  "scale and complexity",["font color","logo","office hours"],"Systems must fit the organization.")
H('245.d.2.B',4,"A key issue when developing a system for different users is:",
  "ease of use and security",["wallpaper","paper color","desk size"],"Usability and safety matter.")
H('245.d.3.A',3,"Before opening a new office, a manager lists computers, printers, and paper needed. This is:",
  "determining equipment and supplies",["ignoring needs","buying randomly","delaying"],"Planning prevents shortages.")
H('245.d.3.A',4,"To decide how many printers an office needs, a manager should consider:",
  "number of users and print volume",["wall color","logo","clock"],"Usage determines needs.")
H('245.d.3.B',3,"A checklist for cleaning screens and replacing toner is part of a:",
  "maintenance system",["marketing plan","tax form","sales pitch"],"Systems keep equipment ready.")
H('245.d.3.B',4,"Tracking when each printer was last serviced is an example of:",
  "an equipment maintenance record",["a sales record","a payroll form","a phone log"],"Records support maintenance.")
H('245.d.3.C',3,"Setting a monthly calendar to back up servers and clean computers is:",
  "scheduling maintenance",["ignoring upkeep","random fixing","delaying forever"],"Regular schedules prevent failures.")
H('245.d.3.C',4,"Preventive maintenance is done:",
  "before problems occur",["only after failure","never","once a decade"],"Prevention saves cost.")
H('245.d.3.D',3,"Following the steps to replace a toner cartridge is using:",
  "maintenance procedures",["guesswork","shortcuts","random actions"],"Procedures prevent damage.")
H('245.d.3.D',4,"Before cleaning computer equipment, you should first:",
  "power it off and unplug it",["spray liquid on it","leave it on","open it with wet hands"],"Safety first.")
H('245.d.3.E',3,"A printer shows an error. A critical thinker first:",
  "checks the error message and basic connections",["throws it away","ignores it","breaks it open"],"Troubleshooting starts simply.")
H('245.d.3.E',4,"A program freezes only when opening large files. The best next step is to:",
  "test with smaller files and check system resources",["reinstall the OS immediately","ignore it","unplug the building"],"Isolate the cause.")
H('245.d.4.A',3,"Dragging a file from one folder to another in the operating system is:",
  "moving a file",["deleting a file","printing a file","encrypting a file"],"Moving changes location.")
H('245.d.4.A',4,"Moving a file differs from copying it because moving:",
  "removes it from the original location",["makes two copies","deletes the system","creates a virus"],"Move relocates.")
H('245.d.4.B',3,"A folder created to organize all invoices is a:",
  "directory",["macro","virus","formula"],"Directories hold files.")
H('245.d.4.B',4,"Placing subfolders inside a main folder helps by:",
  "organizing files hierarchically",["hiding the computer","slowing the network","deleting data"],"Hierarchy aids finding files.")
H('245.d.4.C',3,"A document that must keep its look on any device is best saved as a:",
  "PDF",["plain text","unsaved file","temp file"],"PDFs preserve layout.")
H('245.d.4.C',4,"A file saved as plain text will lose:",
  "formatting such as bold and images",["all words","its name","its size"],"Plain text has no styling.")
H('245.d.5.A',3,"A memo, a letter, and a report are different:",
  "styles of business documents",["tax forms","software programs","computers"],"Each has customary format.")
H('245.d.5.A',4,"Which style is a block letter?",
  "all lines flush with the left margin",["centered everything","all lines indented","right aligned"],"Block style is left aligned.")
H('245.d.5.B',3,"Improving touch-system skills on the keyboard and keypad helps you:",
  "enter data faster and more accurately",["type slower","make more errors","avoid work"],"Practice raises speed.")
H('245.d.5.B',4,"The best way to improve keypad accuracy is to:",
  "practice without looking at the keys",["look at the keys","guess","go faster at once"],"Touch practice builds accuracy.")
H('245.d.5.C',3,"To produce a printed brochure, you need software and:",
  "a printer",["a microwave","a scale","a ruler only"],"Hardware is needed to print.")
H('245.d.5.C',4,"Hardware and software must be chosen to:",
  "fit the type of document being produced",["match the desk","match shoes","match wallpaper"],"Tools should suit the task.")
H('245.d.5.D',3,"Before writing a business proposal, brainstorming and gathering facts is:",
  "generating ideas and collecting information",["finishing early","editing","printing"],"Prewriting prepares drafts.")
H('245.d.5.D',4,"A good place to gather facts for a business document is:",
  "credible company records and reliable sources",["gossip","guesses","rumors"],"Reliable sources matter.")
H('245.d.5.E',3,"A document sent to apply for a job, summarizing your experience, is a:",
  "resume",["memo","invoice","report"],"Resumes summarize experience.")
H('245.d.5.E',4,"Which document typically includes an abstract, body, and references?",
  "a research report",["a thank-you note","a text message","a sticky note"],"Reports have these sections.")
H('245.d.5.F',3,"Reading a letter to correct spelling and grammar errors is:",
  "editing",["printing","filing","deleting"],"Editing refines text.")
H('245.d.5.F',4,"Which tool in a word processor tracks suggested changes for review?",
  "track changes",["print preview","zoom","word art"],"Track changes shows edits.")
H('245.d.5.G',3,"Adding a table to organize product prices in a document is:",
  "inserting an object",["deleting text","printing","saving"],"Tables are objects.")
H('245.d.5.G',4,"A page number placed in the footer on every page uses:",
  "headers and footers",["tables only","hyperlinks only","comments only"],"Footers repeat on each page.")
H('245.d.5.H',3,"Sending a letter to 200 customers with each name filled in uses:",
  "mail merge",["copy and paste each","manual retyping","a calculator"],"Mail merge personalizes.")
H('245.d.5.H',4,"In mail merge, the list of names and addresses is the:",
  "data source",["footnote","header","macro"],"The data source supplies merge fields.")
H('245.d.5.I',3,"Several coworkers edit the same report at the same time in a cloud word processor. This is:",
  "online collaboration",["file loss","printing","offline editing only"],"Cloud tools allow shared editing.")
H('245.d.5.I',4,"A benefit of online word processors is that documents:",
  "can be accessed and shared from any device",["are lost easily","cannot be edited","require paper"],"Cloud access is flexible.")
H('245.d.6.A',3,"Examining sales numbers to find which month performs best is:",
  "data analysis",["data deletion","data loss","random counting"],"Analysis finds patterns.")
H('245.d.6.A',4,"Before analyzing data, you should make sure it is:",
  "accurate and complete",["old","random","hidden"],"Quality data matters.")
H('245.d.6.B',3,"Software that lets you store and search large collections of records is a:",
  "database management system",["word processor","photo editor","browser"],"DBMSs manage data.")
H('245.d.6.B',4,"Which tool is used to ask a database a question?",
  "a query",["a footer","a slide","a margin"],"Queries retrieve data.")
H('245.d.6.C',3,"A company that tracks thousands of customer records should choose:",
  "database software",["a calculator app","a drawing app","a game"],"Databases handle many records.")
H('245.d.6.C',4,"A small team just needs a quick budget with formulas. The better choice is a:",
  "spreadsheet",["large database server","video editor","drawing tool"],"Spreadsheets suit small calculations.")
H('245.d.6.D',3,"In a table, a column storing customer phone numbers is a:",
  "field",["record","report","query"],"Fields hold one data type.")
H('245.d.6.D',4,"The data type best suited for a quantity in stock is:",
  "number",["picture","yes/no","text only"],"Quantities are numeric.")
H('245.d.6.E',3,"Creating tables, naming fields, and choosing data types builds a:",
  "database structure",["presentation","letter","report"],"Structure defines storage.")
H('245.d.6.E',4,"Each table in a database should have a:",
  "primary key to uniquely identify records",["picture","password","footnote"],"Primary keys identify rows.")
H('245.d.6.F',3,"Linking a Customers table to an Orders table using a customer ID is defining a:",
  "relationship",["macro","footer","chart"],"Relationships connect tables.")
H('245.d.6.F',4,"One customer can place many orders. This is a:",
  "one-to-many relationship",["one-to-one relationship","many-to-many only","no relationship"],"One-to-many is common.")
H('245.d.6.G',3,"Interviewing managers to learn what data they need is:",
  "analyzing company data requirements",["ignoring needs","guessing","buying hardware"],"Requirements drive design.")
H('245.d.6.G',4,"A requirements analysis should be done:",
  "before designing the database",["after launch","never","once it breaks"],"Analysis comes first.")
H('245.d.6.H',3,"Sketching tables and relationships to meet business needs is:",
  "designing a database",["printing a report","sending a memo","editing a letter"],"Design plans the structure.")
H('245.d.6.H',4,"A well-designed database avoids:",
  "duplicate data and inconsistencies",["all users","all queries","all forms"],"Good design reduces redundancy.")
H('245.d.7.A',3,"Logging in and opening a table to view records is:",
  "accessing information in the database system",["deleting the system","printing","encrypting"],"Access begins use.")
H('245.d.7.A',4,"Limiting who can access certain data in a database helps maintain:",
  "security",["speed only","color","size"],"Permissions protect data.")
H('245.d.7.B',3,"A data warehouse is used to:",
  "store large amounts of historical data for analysis",["print letters","edit photos","send email"],"Warehouses aggregate data.")
H('245.d.7.B',4,"Data from several sources combined into a warehouse supports:",
  "reporting and decision making",["data loss","slow reports","guessing"],"Warehouses support analytics.")
H('245.d.7.C',3,"Typing a new customer's information into a form that feeds a table is:",
  "entering data",["deleting data","printing data","sorting only"],"Forms enter data.")
H('245.d.7.C',4,"A form with a drop-down list helps data entry by:",
  "reducing typing errors",["adding errors","hiding fields","slowing entry"],"Controlled input improves accuracy.")
H('245.d.7.D',3,"Bringing data from a spreadsheet into a database is:",
  "importing",["exporting","printing","encrypting"],"Importing brings data in.")
H('245.d.7.D',4,"Sending data from a database to a spreadsheet file is:",
  "exporting",["importing","deleting","archiving only"],"Exporting sends data out.")
H('245.d.8.A',3,"A query that shows only customers in Dallas is:",
  "retrieving data with criteria",["deleting data","printing only","encrypting"],"Criteria filter results.")
H('245.d.8.A',4,"Which criteria would show orders over $500?",
  ">500",["<500","=500 only","none"],"Greater than 500.")
H('245.d.8.B',3,"A query that asks for all products with stock below 10 is:",
  "formulating a query",["a report footer","a letter","a chart"],"Queries ask questions.")
H('245.d.8.B',4,"To list orders from two tables, the query must use:",
  "a relationship or join between tables",["a font","a macro only","a footnote"],"Joins connect tables.")
H('245.d.8.C',3,"A formatted printout summarizing monthly sales from a database is a:",
  "report",["form","table","key"],"Reports summarize data.")
H('245.d.8.C',4,"A good database report should be:",
  "clear, labeled, and organized",["cluttered","unlabeled","random"],"Clarity helps decisions.")
H('245.d.9.A',3,"Searching large data sets for hidden patterns is called:",
  "data mining",["data entry","data deletion","data printing"],"Mining discovers patterns.")
H('245.d.9.A',4,"Retailers use data mining to find:",
  "which products customers often buy together",["employee birthdays","paper sizes","font styles"],"Patterns reveal buying behavior.")
H('245.d.9.B',3,"Software that finds trends and clusters in large databases is a:",
  "data mining tool",["word processor","photo editor","clock"],"Mining tools analyze patterns.")
H('245.d.9.B',4,"Which is a data mining technique?",
  "clustering customers by purchase habits",["typing letters","printing","formatting text"],"Clustering groups similar items.")
H('245.d.9.C',3,"Running a basic analysis to see which items sell together is:",
  "demonstrating a data mining technique",["editing a letter","sending email","filing paper"],"Association analysis is a technique.")
H('245.d.9.C',4,"Before mining data, the first step is usually:",
  "cleaning and preparing the data",["publishing","deleting everything","guessing"],"Clean data gives better results.")
H('245.d.9.D',3,"A mining result shows customers who buy bread often buy butter. A store might:",
  "place the items near each other",["remove both","hide them","double prices randomly"],"Insights guide action.")
H('245.d.9.D',4,"A correlation found in mined data means that two variables:",
  "tend to occur together, not necessarily cause each other",["always cause each other","never relate","are identical"],"Correlation is not causation.")
H('245.d.10.A',3,"In a spreadsheet, a 15% tip on a $40 bill is calculated as:",
  "$6",["$15","$4","$0.60"],"40 x 0.15 = 6.")
H('245.d.10.A',4,"A $80 item is discounted by 20%. The sale price is:",
  "$64",["$60","$16","$96"],"80 x 0.80 = 64.")
H('245.d.10.B',3,"Using a spreadsheet to calculate monthly loan payments solves a:",
  "business problem",["personal hobby","game","drawing task"],"Financial functions solve problems.")
H('245.d.10.B',4,"Which function totals a column of numbers?",
  "SUM",["COUNT only","NAME","PRINT"],"SUM adds values.")
H('245.d.10.C',3,"A column chart in a spreadsheet is best for:",
  "comparing values across categories",["writing letters","sending email","drawing logos"],"Column charts compare.")
H('245.d.10.C',4,"An infographic combines data and visuals to:",
  "present information quickly and clearly",["hide data","add noise","confuse readers"],"Infographics simplify.")
H('245.d.10.D',3,"A team updates the same online spreadsheet in real time. This is:",
  "online spreadsheet collaboration",["offline editing","printing","paper filing"],"Cloud sheets allow sharing.")
H('245.d.10.D',4,"A benefit of an online spreadsheet is that changes are:",
  "visible to collaborators instantly",["hidden","lost","delayed for days"],"Real-time syncing helps.")
H('245.d.11.A',3,"A slide with too many fonts and effects is hard to read. A guideline is to:",
  "use few fonts and simple effects",["use many fonts","use tiny text","add random animation"],"Simplicity helps.")
H('245.d.11.A',4,"For readability on a projected slide, the text should be:",
  "large with strong contrast",["small and light","tiny gray","blurry"],"Readability matters.")
H('245.d.11.B',3,"Asking whether a presentation held the audience's attention and met its goal is:",
  "analyzing its effectiveness",["ignoring it","printing it","deleting it"],"Evaluation improves delivery.")
H('245.d.11.B',4,"A good measure of a presentation's effectiveness is whether the audience:",
  "understood and could act on the message",["fell asleep","left early","ignored it"],"Understanding signals success.")
H('245.d.11.C',3,"For a large conference room, the appropriate technology is likely:",
  "a projector or large display",["a tiny phone screen","a paper note","a radio"],"Technology should fit the setting.")
H('245.d.11.C',4,"For a presentation with online participants, the best tool is:",
  "a video conferencing platform with screen sharing",["a printed handout only","a landline only","a fax"],"Remote needs remote tools.")
H('245.d.11.D',3,"Saving a slideshow as a video lets viewers:",
  "watch it without the software",["edit it easily","lose slides","change fonts"],"Video is portable.")
H('245.d.11.D',4,"Saving a presentation as a template allows you to:",
  "reuse its design for future decks",["delete it","lock it forever","print it twice"],"Templates save time.")
H('245.d.11.E',3,"Making eye contact and speaking clearly while presenting slides shows how to:",
  "deliver an effective presentation",["avoid the audience","read silently","hide slides"],"Delivery matters.")
H('245.d.11.E',4,"A presenter reads each slide word for word. A better technique is to:",
  "speak naturally using slides as prompts",["read faster","skip slides","use more text"],"Slides support, not replace, the speaker.")
H('245.d.11.F',3,"Creating a slide deck in a cloud tool and sharing a link is using:",
  "online presentation management technology",["offline slides only","paper","a typewriter"],"Cloud tools allow sharing.")
H('245.d.11.F',4,"A benefit of transmitting a presentation online is that:",
  "audiences anywhere can view it",["only one can view","it cannot be edited","it needs paper"],"Online sharing is accessible.")
H('245.d.12.A',3,"Software used to arrange text and images for newsletters and brochures is:",
  "desktop publishing software",["spreadsheet software","a browser","a calculator"],"DTP lays out pages.")
H('245.d.12.A',4,"Which technology is used in desktop publishing?",
  "a page layout program and a printer",["a thermometer","a calendar only","a stapler only"],"Layout software plus output device.")
H('245.d.12.B',3,"Using consistent columns, fonts, and white space in a newsletter follows:",
  "desktop publishing standards",["random design","bad style","no style"],"Standards create a professional look.")
H('245.d.12.B',4,"A standard desktop publishing practice is to:",
  "align elements to a grid",["use dozens of fonts","center everything randomly","overlap text"],"Grids organize pages.")
H('245.d.12.C',3,"Building a brochure that includes text from a document and a logo from a file is:",
  "importing text and graphics",["deleting objects","printing only","saving only"],"DTP combines content.")
H('245.d.12.C',4,"Before printing a desktop publication, you should:",
  "proofread and check image resolution",["skip checks","shrink to blur","delete graphics"],"Quality checks avoid reprints.")

H('244.d.13.B',5,"Which choice combines two independent clauses correctly in a compound sentence?",
  "Sales increased in March, but profits stayed flat.",["Sales increased in March but.","Although sales increased in March.","Sales, increased in March but profits."],"A coordinating conjunction with a comma joins two independent clauses.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_41.jsonl'))

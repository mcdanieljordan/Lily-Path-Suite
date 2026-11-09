import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('113.48.c.', 1003, own='hs_ssresearch.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('1.A',3,"Which topic is narrow enough for a social science research project?",
  "How did the 1936 Texas Centennial affect tourism in Dallas?",["History","Why do people live in cities?","What happened in the world?"],"A focused topic can be researched in depth.")
H('1.A',3,"A good way to choose a research topic is to do what?",
  "Pick an issue that interests you and has available sources",["Choose the biggest topic possible","Pick one with no evidence","Copy a classmate's topic"],"Interest and available evidence sustain research.")
H('1.B',3,"A research rationale explains what?",
  "Why the topic is worth studying",["Who the author is","The length of the paper","The font style"],"It justifies the project.")
H('1.B',3,"Preliminary ideas for research methods include deciding what?",
  "How you will gather and analyze information",["What color to print in","Which friend to cite","Where to eat lunch"],"Methods are planned early.")
H('1.C',3,"A literature review is a summary of what?",
  "What scholars have already written about the topic",["The student's opinions","A list of survey questions","Future predictions"],"It shows what is known and where the gaps are.")
H('1.C',3,"A literature review helps a researcher by doing what?",
  "Showing a gap that the new study can fill",["Replacing the research","Hiding earlier work","Proving the thesis automatically"],"Reviews place a study in context.")
H('1.D',3,"A research thesis should be what?",
  "An arguable claim that evidence can support or test",["A fact everyone knows","A list of questions","A quote from a source"],"A thesis guides the study.")
H('1.D',3,"Which is the best research thesis?",
  "Rural-to-urban migration after 1940 increased Texas school enrollment in cities more than in counties.",["Texas is large.","Schools exist.","Migration is interesting."],"It is specific and testable.")
H('2.A',3,"Quantitative research methods primarily collect what?",
  "Numerical data that can be measured and analyzed statistically",["Only stories and quotes","Only images","Only opinions without numbers"],"Qualitative research collects descriptive data.")
H('2.A',3,"Qualitative research methods emphasize what?",
  "Meaning, context and descriptions from sources such as interviews",["Only large datasets","Only computation","Only experiments"],"Interviews and observation are common.")
H('2.B',3,"Designing a research project involves choosing what?",
  "A question, a theory and methods that fit the question",["A random paper size","A title only","A random date"],"Design connects question and method.")
H('2.B',3,"Which research question requires a survey method?",
  "What percent of students at a school support a later start time?",["What did a 1950 treaty say?","Who wrote a diary in 1800?","Where is a river located?"],"Surveys measure attitudes in a sample.")
H('2.C',3,"Which technique collects oral information from people?",
  "Interviews",["Census tables","Encyclopedias","Atlas maps"],"Oral sources include interviews and oral histories.")
H('2.C',3,"A researcher who watches behavior in a natural setting without changing it is using what?",
  "Observation",["Survey sampling","Experiments","Literature review"],"Observation records behavior as it occurs.")
H('2.D',3,"Which technology would help a researcher locate scholarly articles?",
  "An academic journal database",["A music streaming app","A shopping website","A video game"],"Databases index peer-reviewed work.")
H('2.D',3,"When searching online, a researcher should prefer which kind of source?",
  "Scholarly and government sites with identifiable authors",["Anonymous posts","Advertisements","Rumor pages"],"Credibility depends on authorship and review.")
H('2.E',3,"Using sources that show multiple perspectives helps a researcher do what?",
  "Avoid a one-sided view of the topic",["Shorten the project","Remove evidence","Avoid analysis"],"Multiple perspectives reduce bias.")
H('2.E',3,"A study of a labor strike that uses only management records is likely to be what?",
  "Incomplete because it omits workers' perspectives",["Perfectly balanced","Fully objective","Quantitative"],"Both sides should be represented.")
H('2.F',3,"A researcher reading a senator's personal journal from 1862 is using what type of source?",
  "A primary source",["A secondary source","A textbook","A tertiary source"],"It was created by a participant at the time.")
H('2.F',3,"A scholarly book that interprets primary documents is what type of source?",
  "A secondary source",["A primary source","An artifact","A raw dataset"],"Secondary sources analyze and interpret.")
H('2.G',3,"Which is a useful criterion for evaluating a source?",
  "Author expertise, evidence quality and timeliness",["Number of images","Length of title","Page color"],"Criteria help judge reliability.")
H('2.G',3,"When evaluating numerical information, a researcher should check what?",
  "How the data were collected and the sample size",["The font","The cover design","The paper weight"],"Method affects trustworthiness.")
H('2.H',3,"Describing the results of research means doing what?",
  "Reporting what the data showed without overstating",["Hiding unexpected results","Changing the numbers","Skipping the findings"],"Results are described objectively.")
H('2.H',3,"A results section should present findings in what form?",
  "Clear text supported by tables or charts",["Rumors","A guess","A long quote only"],"Visuals clarify the findings.")
H('2.I',3,"A logical conclusion should be what?",
  "Drawn directly from the research results",["Based on assumptions only","Unrelated to the data","Formed before research began"],"Conclusions follow evidence.")
H('2.I',3,"If a survey shows 78 percent of respondents favor a policy, which conclusion is logical?",
  "Most respondents in the sample favor the policy",["Everyone in the world favors it","No one opposes it","The policy will pass"],"Conclusions must match the data and sample.")
H('2.J',3,"Justifying a conclusion requires what?",
  "Supporting evidence from the research",["Strong opinion","Repeating the thesis","A long introduction"],"Evidence backs claims.")
H('2.J',3,"Which statement best justifies a conclusion?",
  "Three independent sources and the survey data point to the same result.",["The author feels sure.","A friend agrees.","It seems right."],"Convergent evidence strengthens a conclusion.")
H('2.K',3,"Making a prediction from research means doing what?",
  "Using findings to suggest likely future outcomes",["Guessing without data","Ignoring trends","Changing the data"],"Predictions extend from conclusions.")
H('2.K',3,"If data show enrollment rising steadily for ten years, a reasonable prediction is what?",
  "Enrollment will likely continue to rise if conditions stay similar",["Enrollment will fall tomorrow","Enrollment cannot be predicted","Enrollment is unrelated to time"],"Trend extrapolation has limits.")
H('2.L',3,"MLA and APA are examples of what?",
  "Citation styles for social science writing",["Survey methods","Statistical tests","Types of graphs"],"Style guides format bibliographies.")
H('2.L',3,"A bibliography entry usually includes which information?",
  "Author, title, publisher and date",["Only the date","Only the title","A summary"],"Entries let readers find the source.")
H('3.A',3,"Historiography is the study of what?",
  "How historians have interpreted and written about a topic over time",["Weather records","Biographies only","Future trends"],"Interpretations change with new evidence and views.")
H('3.A',3,"Why do historians interpret the same event differently over time?",
  "New evidence and changing perspectives shape interpretations",["Facts never change","Sources disappear","Historians avoid the topic"],"Historiography reflects shifting viewpoints.")
H('3.B',3,"Causality in social science research refers to what?",
  "The relationship in which one factor produces an effect",["A list of dates","A type of map","A bibliography style"],"Researchers test causal claims carefully.")
H('3.B',3,"Which key concept refers to how things stay the same or alter across time?",
  "Continuity and change",["Rhetoric","Sampling","Citation"],"Time and change are central concepts.")
H('3.C',3,"Analyzing viewpoints within and across cultures requires a researcher to do what?",
  "Consider how culture and context shape beliefs",["Apply only modern values","Ignore other cultures","Judge them all the same"],"Context explains differing viewpoints.")
H('3.C',3,"Two cultures describe the same border dispute differently. A researcher should do what?",
  "Examine sources from both sides and compare their viewpoints",["Reject both accounts","Choose the louder account","Use only one"],"Comparison yields a fuller analysis.")
H('3.D',3,"A recurring dilemma in social science is the conflict between what?",
  "Individual liberty and the common good",["Two colors","Two fonts","Two seasons"],"Such dilemmas recur across eras.")
H('3.D',3,"A persistent issue relevant to many topics is what?",
  "Unequal distribution of resources and power",["The invention of the pencil","The color of the sky","Daily weather"],"Persistent issues connect topics across time.")
H('3.E',3,"Skepticism in research means what?",
  "Questioning claims and requiring evidence",["Rejecting all sources","Believing everything","Avoiding conclusions"],"Healthy doubt improves analysis.")
H('3.E',3,"Historical empathy means doing what?",
  "Trying to understand people of the past within their own context",["Excusing all actions","Ignoring evidence","Judging only by today"],"Empathy helps interpretation without losing critical judgment.")
H('4.A',3,"The first step of the scientific method in a research project is usually what?",
  "Ask a question or identify a problem",["Publish results","Draw a conclusion","Write the bibliography"],"Research begins with a question.")
H('4.A',3,"A hypothesis in the scientific method is what?",
  "A testable prediction about a relationship",["A proven law","A random guess","A bibliography"],"It is tested with data.")
H('4.B',3,"A research methods matrix is used to do what?",
  "Compare which methods suit different research questions",["Hide data","Replace sources","Write a conclusion"],"Matrices organize method choices.")
H('4.B',3,"Which method fits the study of a community's customs by living among its members?",
  "Ethnography",["Survey research","Statistical modeling","Content coding"],"Ethnography uses immersion.")
H('4.C',3,"The most efficient research approach is the one that does what?",
  "Answers the question with the needed evidence at reasonable cost and time",["Uses the most sources","Takes the longest","Avoids data"],"Efficiency weighs time, cost and fit.")
H('4.C',3,"A researcher needing opinions from 500 students quickly should most likely use what?",
  "A survey",["Archival research","Ethnography","A case study"],"Surveys reach many people efficiently.")
H('4.D',3,"Aggregate information refers to what?",
  "Data combined from many individuals or units",["One person's diary","A single interview","A personal letter"],"Statistics summarize aggregate data.")
H('4.D',3,"Which tool helps summarize a large data set?",
  "Statistical measures such as mean and median",["A rhyme scheme","A map legend only","A footnote"],"Basic statistics describe data.")
H('4.E',3,"The mean of 4, 6, 8 and 10 is what?",
  "7",["6","8","28"],"Sum 28 divided by 4 equals 7.")
H('4.E',3,"A positive correlation means that what is true?",
  "As one variable rises, the other tends to rise",["One causes the other","They never move together","As one rises, the other falls"],"Correlation is not causation.")
H('4.F',3,"Which software can be used to compute averages and make charts from survey data?",
  "A spreadsheet program",["A photo editor only","A game console","A calendar only"],"Spreadsheets analyze data.")
H('4.F',3,"Statistical analysis software is helpful because it does what?",
  "Processes large data sets quickly and accurately",["Chooses the thesis","Creates the evidence","Removes bias automatically"],"Tools speed analysis but do not replace judgment.")
H('4.G',3,"Reliability in research refers to what?",
  "Consistency of results when a study is repeated",["Accuracy of the topic choice","Length of the paper","Popularity of findings"],"Reliable measures yield consistent results.")
H('4.G',3,"Validity in research refers to what?",
  "Whether a study measures what it claims to measure",["Consistency alone","The sample's age","The number of pages"],"Valid measures are accurate.")
H('4.H',3,"Cross-cultural understanding is obstructed by what?",
  "Ethnocentric attitudes and stereotypes",["Curiosity","Respect","Open dialogue"],"Biased attitudes block understanding.")
H('4.H',3,"A researcher studying greetings across cultures should expect what?",
  "Behavior patterns to reflect each culture's values",["All greetings to be identical","No cultural influence","Only individual differences"],"Values shape behavior.")
H('4.I',3,"Before surveying human participants, researchers should obtain what?",
  "Informed consent",["A prize","A grade","A refund"],"Participants must know and agree.")
H('4.I',3,"Ethical standards for storing survey data require what?",
  "Protecting participants' privacy and keeping data secure",["Posting names publicly","Selling data","Sharing with anyone"],"Confidentiality is essential.")
H('5.A',3,"Which sentence uses standard written English?",
  "The data support the researcher's conclusion.",["The data supports the researchers conclusion","The datas support the researcher's conclusion.","the data support the researcher's conclusion"],"Usage and mechanics matter in research writing.")
H('5.A',3,"Editing a research draft helps to do what?",
  "Improve clarity, grammar and organization",["Add new sources","Change the topic","Remove the thesis"],"Revision polishes a paper.")
H('5.B',3,"Where does a research paper typically state its thesis?",
  "In the introduction",["Only in the bibliography","On the cover","In the footnote"],"The thesis frames the paper.")
H('5.B',3,"The conclusion of a research paper should do what?",
  "Restate the thesis and summarize the findings",["Introduce unrelated topics","Add new data","Apologize for the study"],"It closes the argument.")
H('5.C',3,"Which term means a systematic way of collecting data from a group?",
  "Survey",["Footnote","Thesis","Map"],"Accurate terminology aids communication.")
H('5.C',3,"Using social science terminology correctly shows what?",
  "Understanding of the field's concepts",["Complexity for its own sake","Disinterest","Disorganization"],"Precision builds credibility.")
H('5.D',3,"Addressing a counter argument shows that a researcher has done what?",
  "Considered opposing evidence and responded to it",["Ignored evidence","Changed the thesis","Hidden the sources"],"It strengthens the argument.")
H('5.D',3,"Which approach best justifies a conclusion while addressing objections?",
  "Presenting evidence and explaining why opposing claims are weaker",["Refusing to discuss opposition","Insulting critics","Repeating the claim"],"Rebuttal with evidence persuades.")
H('5.E',3,"A timeline is best used to show what?",
  "Events in chronological order",["Percentages of a whole","Relationships between two variables","Geographic locations"],"It displays sequence.")
H('5.E',3,"Which visual best shows the parts of a whole such as budget shares?",
  "A pie chart",["A timeline","A scatter plot","A flowchart"],"Pie charts show proportions.")
H('5.F',3,"Presentation software lets a researcher do what?",
  "Combine text, graphics and multimedia to share findings",["Replace research","Collect primary data","Review literature"],"Software aids communication of results.")
H('5.F',3,"A strong slide in a research presentation includes what?",
  "A clear point supported by a simple visual",["A wall of text","No labels","Unrelated clip art"],"Clarity helps the audience.")
H('5.G',3,"Visual images in a presentation should be what?",
  "Relevant to the topic and properly credited",["Random","Uncredited","Distracting"],"Images should enhance the message.")
H('5.G',3,"An archival photograph can enhance a presentation by doing what?",
  "Making historical context more vivid for the audience",["Proving the thesis alone","Replacing the evidence","Removing the need for sources"],"Visual evidence adds depth.")
H('5.H',3,"A works cited list is used for what?",
  "Showing the sources that supplied the paper's ideas and data",["Hiding evidence","Writing the thesis","Making a graph"],"Attribution is a basic research standard.")
H('5.H',3,"Which practice avoids plagiarism?",
  "Citing every source whose ideas or words you use",["Copying and pasting without credit","Changing a few words","Using only one source"],"Credit sources properly.")
H('6.A',3,"For a capstone research project, a student should select what?",
  "A social studies issue that can be studied with available evidence",["The longest topic","An unresearchable topic","A topic with no sources"],"Topic selection starts the project.")
H('6.A',3,"An area of interest becomes a research topic when it is what?",
  "Narrowed into a focused, researchable question",["Left broad","Dropped","Copied"],"Focus makes research manageable.")
H('6.B',3,"A well-designed capstone project examines what?",
  "The theory and methods that fit the research question",["Only the introduction","Only formatting","Only the conclusion"],"Fit between theory and method matters.")
H('6.B',3,"Why include a methods section in a capstone paper?",
  "So readers can see how evidence was collected and evaluate it",["To lengthen the paper","To hide results","To avoid a thesis"],"Transparency allows evaluation.")
H('6.C',3,"Describing results in a capstone project means doing what?",
  "Explaining what the research found, supported by data",["Skipping data","Making predictions only","Listing sources only"],"Results come before interpretation.")
H('6.D',3,"A strong capstone conclusion justifies its claim with evidence and also does what?",
  "Makes reasoned predictions about future outcomes",["Avoids implications","Ignores limits","Repeats the title"],"Predictions extend findings.")
H('6.D',3,"A capstone paper claims a new law will reduce crime. Which evidence best justifies this claim?",
  "Crime data from similar places before and after comparable laws",["The author's hope","A single anecdote","A slogan"],"Comparable data support predictions.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_ssresearch.jsonl'))

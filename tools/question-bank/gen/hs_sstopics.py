import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('113.47.c.', 1002, own='hs_sstopics.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('1.A',3,"A student studying how a town changed after a factory closed wants to explore a social studies question. Which approach fits best?",
  "Gather data such as census figures, interviews and newspaper articles, then analyze them",["Rely on one friend's memory only","Skip research and state an opinion","Copy another student's paper"],"Social studies methods combine varied evidence and analysis.")
H('1.A',3,"Which pair of tools would a researcher combine to study a historical topic from different angles?",
  "Primary documents and statistical data",["A single textbook sentence and a guess","A rumor and a slogan","A cartoon only"],"Mixed methods strengthen conclusions.")
H('1.B',3,"Which is a political condition that could affect a topic such as migration patterns?",
  "Changes in immigration laws",["A change in the weather forecast","The color of a flag","A new music genre"],"Laws shape who can move and where.")
H('1.B',3,"A recession is an example of which type of condition shaping a social studies topic?",
  "Economic",["Geographic","Linguistic","Artistic"],"Economic downturns affect jobs, migration and politics.")
H('1.C',3,"A geographic perspective on a topic considers what?",
  "How physical features and human activity interact in places",["Only dates and names","Only laws","Only wars"],"Geography links place, environment and culture.")
H('1.C',3,"Which is a cultural process that can change a region over time?",
  "Diffusion of ideas and customs through trade and migration",["Plate tectonics","Erosion","A volcanic eruption"],"Cultural processes are human-driven.")
H('1.D',3,"Why should a study of a historic event examine diverse communities?",
  "Different groups often experienced the same event in different ways",["All groups always agree","Only one group matters","It shortens the study"],"Multiple perspectives give a fuller picture.")
H('1.D',3,"Including the voices of women, immigrants and minority groups in a study helps to do what?",
  "Create a more complete account of the past",["Hide conflicting evidence","Remove primary sources","Avoid analysis"],"Inclusion widens the evidence base.")
H('1.E',3,"An ethical issue in studying a topic like the use of human subjects in historic experiments is what?",
  "Whether people were treated fairly and gave informed consent",["How long the report is","What font to use","Which map color to choose"],"Ethics concern rights and fairness.")
H('1.E',3,"Judging past actions by values from different time periods and cultures requires what?",
  "Considering historic, cultural and social context",["Ignoring evidence","Using only modern views","Avoiding the topic"],"Context matters in ethical analysis.")
H('1.F',3,"In a problem-solving process, what comes right after identifying the problem?",
  "Gathering information",["Declaring a winner","Publishing results","Ending the project"],"Facts are needed before choosing a solution.")
H('1.F',3,"After listing possible solutions, a team should next do what?",
  "Consider the advantages and disadvantages of each solution",["Choose the first idea","Abandon the problem","Skip evaluation"],"Weigh options before selecting one.")
H('1.G',3,"A decision-making process begins by doing what?",
  "Identifying a situation that requires a decision",["Implementing the choice","Evaluating the outcome","Ignoring alternatives"],"The need for a decision must be defined first.")
H('1.G',3,"The final step in a decision-making process is typically what?",
  "Evaluating the effectiveness of the decision",["Selecting a problem","Gathering first facts","Listing no options"],"Reflection improves future decisions.")
H('2.A',3,"A researcher locates several sources on a topic. What should be done next?",
  "Analyze, organize and evaluate the information",["Throw out contradictory data","Memorize titles only","Delete the notes"],"Research moves from gathering to evaluating.")
H('2.A',3,"Synthesizing information means doing what?",
  "Combining ideas from several sources into a new understanding",["Copying one source","Ignoring details","Choosing the longest source"],"Synthesis builds a coherent argument.")
H('2.B',3,"Which of these is a primary source?",
  "A soldier's letter written during the war",["A textbook chapter about the war","An encyclopedia entry","A documentary made decades later"],"Primary sources come from the time period studied.")
H('2.B',3,"A secondary source is best described as what?",
  "An account created later by someone who did not witness the event",["An original diary","A photograph taken at the event","A treaty signed at the event"],"Secondary sources interpret primary evidence.")
H('2.C',3,"When reading a narrative text critically, a student should identify what?",
  "The author's point of view and the historical context",["Only the font","Only the page count","Only the title"],"Perspective shapes narrative accounts.")
H('2.C',3,"Two eyewitness accounts of the same event differ. This most likely shows what?",
  "Each writer had a different point of view",["The event never happened","One writer is always lying","Primary sources are useless"],"Perspective affects reporting.")
H('2.D',3,"Putting events in time order is called what?",
  "Sequencing",["Categorizing","Comparing","Contrasting"],"Sequencing shows chronology.")
H('2.D',3,"Identifying how one event led to another is what skill?",
  "Finding cause-and-effect relationships",["Memorizing dates","Copying text","Summarizing a title"],"Causation explains change.")
H('2.E',3,"A political cartoon from 1900 is useful to a researcher because it does what?",
  "Shows opinions and attitudes of the time through images",["Gives exact statistics","Replaces all documents","Proves a fact alone"],"Visual media reveal perspective.")
H('2.E',3,"Which of these is a visual source a student might collect?",
  "A photograph of a protest march",["A tax table","A list of laws","A glossary"],"Images enhance understanding.")
H('2.F',3,"Bias in a source means what?",
  "A tendency that favors one viewpoint unfairly",["A fully neutral report","A list of dates","An index"],"Detecting bias is essential in evaluation.")
H('2.F',3,"Which word choice most likely signals bias in a news article?",
  "Highly charged or emotional language",["Neutral measurements","Dates","Page numbers"],"Loaded language reveals slant.")
H('2.G',3,"Corroboration of a source means what?",
  "Confirming its claims with other independent sources",["Quoting it twice","Printing it","Ignoring other evidence"],"Agreement among sources adds validity.")
H('2.G',3,"Which detail helps judge a source's validity?",
  "The author's credentials and purpose",["The paper color","The number of pages","The size of the font"],"Expertise and purpose affect reliability.")
H('2.H',3,"A student reads a bar graph showing population by decade. Which skill is being used?",
  "Interpreting data with mathematical skills",["Memorizing slogans","Writing a thesis","Citing sources"],"Graphs communicate numerical trends.")
H('2.H',3,"A map scale of 1 inch to 100 miles helps a researcher do what?",
  "Calculate real distances between places",["Judge bias","Date a source","Write a bibliography"],"Scale converts map distance to ground distance.")
H('3.A',3,"Which sentence follows standard written English?",
  "The committee presented its findings to the class.",["The committee presented there findings to the class.","The committee present their findings to the class.","the committee presented its findings too the class."],"Usage and mechanics matter in written work.")
H('3.A',3,"Proofreading a research paper checks for what?",
  "Spelling, grammar and punctuation errors",["New evidence","Better sources","Longer sentences only"],"Mechanics improve clarity.")
H('3.B',3,"Using social studies terminology correctly means doing what?",
  "Applying precise terms such as primary source and cause",["Using slang only","Avoiding all vocabulary","Changing meanings"],"Accurate vocabulary supports clear communication.")
H('3.B',3,"Which term describes a long-term change in the way a society operates?",
  "Social change",["Fad","Rumor","Accident"],"Terms must match concepts.")
H('3.C',3,"Which is an effective oral communication technique?",
  "Speaking clearly and making eye contact with the audience",["Reading in a whisper","Turning away","Rushing through slides"],"Delivery affects understanding.")
H('3.C',3,"During a class discussion, a speaker should do what?",
  "Support claims with evidence and listen to others",["Interrupt often","Avoid facts","Speak off topic"],"Courtesy and evidence improve discussion.")
H('3.D',3,"A thesis statement is best described as what?",
  "A main claim that evidence in the paper supports",["A list of sources","A question with no answer","A paragraph of quotes"],"The thesis guides the argument.")
H('3.D',3,"Which thesis is strongest?",
  "The railroad transformed Texas by linking markets, spurring towns and shifting political power.",["Railroads exist.","Trains are fast.","I like trains."],"A strong thesis makes a specific, arguable claim.")
H('3.E',3,"A counter argument is what?",
  "A claim that opposes your thesis",["A source list","A summary","A title"],"Addressing it strengthens your own case.")
H('3.E',3,"A writer who evaluates counter arguments should do what?",
  "Respond with evidence showing why the thesis still holds",["Ignore them","Hide them","Repeat the thesis only"],"Rebuttal is part of strong argumentation.")
H('3.F',3,"How can photographs help a presentation about a historic culture?",
  "They help the audience understand and appreciate cultural details",["They replace all text","They prove a thesis automatically","They reduce interest"],"Visual media support understanding.")
H('3.F',3,"When using an image in a project, a student should do what?",
  "Credit the source and make sure it supports the point",["Remove the source","Crop out the caption","Use any picture"],"Images should be relevant and attributed.")
H('3.G',3,"A bibliography is used to do what?",
  "List the sources that supplied ideas and information",["Replace the thesis","Summarize the paper","Hide sources"],"Attribution avoids plagiarism.")
H('3.G',3,"Using someone else's words without giving credit is called what?",
  "Plagiarism",["Citation","Paraphrasing with credit","Synthesis"],"Always attribute ideas.")
H('3.H',3,"Which task could a student do with spreadsheet software?",
  "Create a chart from collected survey data",["Interview a witness","Visit an archive","Translate a treaty"],"Software helps display data.")
H('3.H',3,"Presentation software is best used to do what?",
  "Create visual products that communicate findings clearly",["Replace research","Avoid sources","Hide data"],"Technology supports presentation.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_sstopics.jsonl'))

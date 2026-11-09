import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('113.61.c.', 1008, own='hs_econadv.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('1.A',3,"Dana tracks stock prices for fun and likes comparing company reports. Which economics career area connects best to this interest?",
  "Financial analysis",["Plumbing","Landscape design","Commercial fishing"],"Linking interests to a career is the start of an advanced economics project.")
H('1.A',3,"Eli enjoys studying how prices change when a store runs out of an item. Which discipline matches his interest?",
  "Microeconomics",["Astronomy","Anatomy","Metallurgy"],"Supply and prices are core topics in microeconomics.")
H('1.B',3,"For a project on inflation, Rosa reads a Federal Reserve report, an economics journal article and a business news story. Why use varied sources?",
  "To compare data and viewpoints and check claims against each other",["To avoid citing anyone","To find only one number","To lengthen the paper"],"Literature review uses varied sources.")
H('1.B',3,"Which source is the strongest choice for data on national unemployment rates?",
  "A Bureau of Labor Statistics release",["An unsigned forum post","A friend's guess","A product advertisement"],"Government statistical agencies publish reliable data.")
H('1.C',3,"A student sees that three local grocery stores closed in two years, leaving neighbors with little access to fresh food. This helps her do what?",
  "Identify an economic problem to study",["Write a bibliography","Print the poster","Grade the project"],"Projects begin with a real problem.")
H('1.C',3,"Which is a clear problem statement for an economics project?",
  "Rising rents in our town are pushing out workers who earn the median wage",["Money exists","I like economics","Rent is a word"],"Specific statements name the issue and the group affected.")
H('1.D',3,"Why would a student interview a small-business owner before finalizing a project on startup costs?",
  "To learn whether the project is realistic from a professional's view",["To skip research","To copy the owner's books","To avoid a proposal"],"Professional input tests appropriateness.")
H('1.D',3,"A student surveys 50 shoppers about how price changes affect what they buy. This survey is what kind of evidence?",
  "Primary data",["A secondary source","A citation","A final report"],"Surveys produce primary data.")
H('1.E',3,"Which pieces belong in an economics project proposal?",
  "Questions, goals and objectives, rationale and procedures",["Only a title","A list of snacks","The final grade"],"Proposals state what, why and how.")
H('1.E',3,"A proposal says, \"I will compare gas prices at six stations each Monday for five weeks.\" Which part of the proposal is this?",
  "Procedure",["Rationale","Conclusion","Bibliography"],"A procedure lists the steps for gathering data.")
H('2.A',3,"Shadowing a bank loan officer for a morning helps a student do what?",
  "Understand the profession's requirements and practices through observation",["Earn a license","Skip the proposal","Avoid research"],"Observation builds career understanding.")
H('2.A',3,"While observing an accountant, a student notes the certification the job requires. Why record it?",
  "It shows the requirements of the profession",["It ends the project","It replaces interviews","It sets the grade"],"Requirements are part of career knowledge.")
H('2.B',3,"A student builds a simple supply and demand model in a spreadsheet the way an economist would. This is what?",
  "Simulating the methods and technologies of the field",["Memorizing a glossary","Copying another paper","Avoiding technology"],"Simulation lets students practice professional methods.")
H('2.B',3,"Which activity best simulates economic research methods?",
  "Analyzing a data set with graphs and averages",["Guessing a trend","Reading only headlines","Skipping the data"],"Economists analyze data.")
H('2.C',3,"Preliminary research shows the data a student planned to use is no longer published. What should the student do?",
  "Revise the proposal to use an available data source",["Drop the project","Invent numbers","Ignore the problem"],"Proposals are revised after preliminary research.")
H('2.C',3,"Why revise an original proposal after early research?",
  "To reflect changes needed based on what the research shows",["To hide goals","To avoid the audience","To remove all questions"],"Revision keeps the plan realistic.")
H('3.A',3,"A student wants to produce a budget guide for teens. Who should help define the product?",
  "A financial counselor or other appropriate professional",["No one","A stranger online","A classmate who has not studied money"],"Professional collaboration sharpens the product.")
H('3.A',3,"Why collaborate with a professional when defining a product?",
  "To make sure it meets real standards of the field",["To skip the plan","To avoid work","To remove the audience"],"Standards guide quality.")
H('3.B',3,"A plan for completing a report with eight weeks left should list what?",
  "Tasks, deadlines and the resources needed",["Only the topic","Favorite songs","No dates"],"Plans organize time and resources.")
H('3.B',3,"A student divides a 10-week project into data, analysis, writing and review phases. This is what?",
  "Developing a plan for completion",["Peer review only","Plagiarism","A final reflection"],"Phases support planning.")
H('3.C',3,"Why write assessment criteria before finishing a project?",
  "So everyone knows how success will be judged",["To lower standards","To hide goals","To avoid feedback"],"Criteria define success.")
H('3.C',3,"Which is a measurable success criterion for a pricing study?",
  "Prices collected from at least 10 stores over 4 weeks",["Make it good","Try hard","Do something useful"],"Measurable criteria can be checked.")
H('3.D',3,"A product for first-time investors should use what kind of language?",
  "Clear, plain language with defined terms",["Dense jargon","No explanations","Random slang"],"Appropriateness for the audience matters.")
H('3.D',3,"Before presenting to a chamber of commerce, why consider the audience?",
  "To match the content and tone to what the members need",["To avoid evidence","To ignore them","To skip research"],"Audience shapes the product.")
H('3.E',3,"After finishing the plan, a student begins collecting data and drafting charts. This step is called what?",
  "Implementing the plan",["Defining the problem","Choosing a career","Grading"],"Implementation carries out the plan.")
H('3.E',3,"A student's data source is delayed by two weeks. The best step is to do what?",
  "Adjust the schedule and keep the goals",["Abandon the project","Hide the delay","Copy another study"],"Plans can be adjusted.")
H('3.F',3,"A project journal should include what?",
  "Dated notes on each phase and reflections on learning",["Only the final grade","Blank pages","Unrelated drawings"],"The journal documents the process.")
H('3.F',3,"Why write reflections in a journal during a project?",
  "To track decisions and learning across phases",["To avoid data","To replace the product","To skip the plan"],"Reflection builds learning.")
H('4.A',3,"After a practice run, a student trims her presentation from 18 minutes to 10 to fit the limit. This is what?",
  "Reviewing and revising the plan to present findings",["Changing the topic","Ignoring feedback","Plagiarizing"],"Revision improves presentations.")
H('4.A',3,"Which revision best improves a presentation about price trends?",
  "Adding a line graph that shows the trend clearly",["Adding unrelated jokes","Removing all data","Reading every number aloud"],"Visuals clarify findings.")
H('4.B',3,"To present to a community lending board, a student must first do what?",
  "Arrange the date, room and equipment with the audience",["Skip the audience","Delay the project","Delete the slides"],"Logistics make a presentation possible.")
H('4.B',3,"A student confirms the room, the time and the laptop connection. This is what?",
  "Making arrangements for the presentation",["Collecting data","Citing sources","Writing a proposal"],"Preparation avoids problems.")
H('4.C',3,"Presenting like a professional economist includes what?",
  "Explaining methods, results and limits with evidence",["Mumbling","Avoiding evidence","Reading with your back turned"],"Professionals present methods and results.")
H('4.C',3,"Which behavior best simulates a professional analyst's presentation?",
  "Stating a clear finding and supporting it with data",["Telling only a story","Hiding sources","Skipping the findings"],"Evidence supports claims.")
H('4.D',3,"An audience member suggests a clearer axis label on a chart. The best response is to do what?",
  "Consider the feedback and decide how to improve the chart",["Ignore it","Argue","Delete the chart"],"Feedback helps refine work.")
H('4.D',3,"Why consider feedback from professionals who watch a presentation?",
  "It shows strengths and areas to improve",["It ends the project","It is always wrong","It replaces the product"],"Professional feedback improves work.")
H('4.E',3,"A student asks whether her findings on local wages could help a city plan job programs. This is what?",
  "Reflecting on the study's potential impact on the field",["Collecting data","Writing citations","Defining the problem"],"Impact reflection looks beyond the project.")
H('4.E',3,"Which question best explores a study's potential impact on economics?",
  "How could these findings change how businesses or policymakers act?",["What font did I use?","Who sat in front?","How long was the break?"],"Impact looks at influence on the field.")
H('4.F',3,"At the end of a project, a student writes what she learned about her own work habits. This is what?",
  "Reflecting on personal learning experiences",["Collecting data","Making a plan","Defining a problem"],"Personal reflection closes the study.")
H('4.F',3,"Which question best guides a personal reflection after a research project?",
  "What did I learn about the research process and about myself?",["What color was the title?","Who was late?","How long was lunch?"],"Reflection examines learning.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_econadv.jsonl'))

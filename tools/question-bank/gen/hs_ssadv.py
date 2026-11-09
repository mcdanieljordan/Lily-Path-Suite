import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('113.60.c.', 1007, own='hs_ssadv.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('1.A',3,"Maya loves mapping old trade routes and also enjoys writing. Which career fit would she most likely explore for a social studies research project?",
  "Historian or cartographer",["Pastry chef","Electrician","Airline mechanic"],"Linking interests to a discipline is the first step of an advanced studies project.")
H('1.A',3,"A student who enjoys debating laws and public policy is analyzing how that interest connects to a career. Which discipline is the closest match?",
  "Political science or law",["Marine biology","Dental hygiene","Welding"],"Matching interests to a discipline guides project choice.")
H('1.B',3,"Before choosing a topic in economics, Jalen reads a journal article, a government report and a news analysis. Why use varied sources?",
  "To see the topic from several viewpoints and check claims against each other",["To make the paper longer","To avoid citing anyone","To find only one opinion"],"Literature review draws on varied sources.")
H('1.B',3,"Which source is the best choice for a scholarly literature review?",
  "A peer-reviewed journal article",["An anonymous blog post","A social media comment","A product advertisement"],"Peer review adds credibility.")
H('1.C',3,"A student notices that many teens in her town cannot reach a library after school. This observation is most useful for doing what?",
  "Identifying a problem or concern to study",["Writing a conclusion","Citing a source","Printing a poster"],"Projects start from a real problem.")
H('1.C',3,"Which statement is a clear problem statement for a social studies project?",
  "Teens in our county have too little access to public transportation to reach after-school jobs",["Buses are fun","I like history","Transportation exists"],"A problem statement names a specific issue and group.")
H('1.D',3,"Why would a student interview a city planner before finalizing a project on local zoning?",
  "To learn whether the project is realistic and appropriate from a professional's view",["To avoid doing research","To copy the planner's work","To skip the proposal"],"Professional input tests appropriateness.")
H('1.D',3,"A survey of 40 community members gives a student data on a local issue. This is an example of what?",
  "Gathering primary data to judge a project",["Plagiarism","A secondary source","A final presentation"],"Surveys and interviews produce primary data.")
H('1.E',3,"Which item belongs in a project proposal?",
  "Well-defined questions, goals, rationale and procedures",["A list of favorite foods","Only a title","The final grade"],"Proposals state what, why and how.")
H('1.E',3,"A proposal states, \"I will measure how many residents use the new bike lane over four weeks.\" This part of the proposal is a what?",
  "Procedure",["Rationale","Conclusion","Citation"],"Procedures describe the steps taken.")
H('2.A',3,"Shadowing an economist for a day helps a student do what?",
  "Understand the requirements and practices of the profession through observation",["Earn a degree","Skip research","Replace the proposal"],"Observation builds career understanding.")
H('2.A',3,"While observing a county clerk, a student notes the training and licenses needed for the job. Why record these?",
  "They show the requirements of the profession",["They prove the job is easy","They replace the interview","They are a final grade"],"Requirements are part of career knowledge.")
H('2.B',3,"A student uses a spreadsheet and survey software the way a market researcher would. This is an example of what?",
  "Simulating the methods and technologies of a field",["Memorizing a textbook","Avoiding technology","Copying a source"],"Simulation lets students practice professional methods.")
H('2.B',3,"Which activity best simulates historical research methods?",
  "Comparing primary documents from an archive",["Guessing the outcome","Reading only the title","Skipping the sources"],"Historians analyze primary documents.")
H('3.A',3,"A student wants to produce a public history exhibit. Who should help define the product?",
  "A museum curator or other appropriate professional",["A stranger online","No one","Only a classmate who knows nothing"],"Collaboration with professionals sharpens the product.")
H('3.A',3,"Why collaborate with a professional when defining a product?",
  "To make sure it meets real standards in the field",["To avoid work","To skip the plan","To remove the audience"],"Professional standards guide quality.")
H('3.B',3,"A plan for completing a research product with 10 weeks left should include what?",
  "Tasks, deadlines and needed resources",["Only the title","A list of hobbies","No dates"],"Plans organize time and resources.")
H('3.B',3,"A student breaks a 12-week project into four 3-week phases. This is an example of what?",
  "Developing a plan for completion",["Plagiarism","Peer review only","A final reflection"],"Phases support planning.")
H('3.C',3,"Why write assessment criteria before finishing a project?",
  "So everyone knows how success will be judged",["To lower standards","To avoid feedback","To hide the goals"],"Criteria define success in advance.")
H('3.C',3,"Which is a measurable success criterion for a survey project?",
  "At least 100 completed responses from a mix of age groups",["Make it nice","Try hard","Do something good"],"Measurable criteria can be checked.")
H('3.D',3,"A product for middle school students should use what kind of language?",
  "Clear, age-appropriate language and examples",["Dense legal jargon","Random slang","No explanations"],"Appropriateness for the audience matters.")
H('3.D',3,"Before presenting to a city council, why consider the audience?",
  "To match the content and tone to what they need and expect",["To ignore them","To avoid evidence","To shorten the research"],"Audience shapes the product.")
H('3.E',3,"After finishing a plan, a student begins gathering data, drafting and building. This step is called what?",
  "Implementing the plan",["Defining the problem","Choosing a career","Grading the product"],"Implementation carries out the plan.")
H('3.E',3,"A student falls behind schedule in week 6. What is the best step in implementing the plan?",
  "Adjust the timeline and priorities while keeping the goals",["Abandon the project","Hide the delay","Copy another paper"],"Plans can be adjusted during implementation.")
H('3.F',3,"A journal kept during a project should include what?",
  "Dated notes on each phase and reflections on what was learned",["Only the final grade","Blank pages","Unrelated drawings"],"The journal documents the process.")
H('3.F',3,"Why record reflections in a project journal?",
  "To track learning and decisions across phases",["To avoid data","To skip the plan","To replace the presentation"],"Reflection builds learning.")
H('4.A',3,"After a practice run, a student cuts the presentation from 20 minutes to 12 to fit the time limit. This is an example of what?",
  "Reviewing and revising the plan to present findings",["Changing the topic","Ignoring feedback","Plagiarizing"],"Revision improves presentations.")
H('4.A',3,"Which revision best improves a presentation of survey results?",
  "Adding a clear chart that shows the key finding",["Adding unrelated jokes","Removing all data","Reading every response aloud"],"Visuals clarify findings.")
H('4.B',3,"To present findings to a school board, a student must do what first?",
  "Arrange a date, time, space and equipment with the appropriate audience",["Skip the audience","Delay the project","Delete the slides"],"Logistics make a presentation possible.")
H('4.B',3,"A student confirms the projector works and that the room is booked. This is an example of what?",
  "Making arrangements for the presentation",["Collecting data","Citing sources","Writing a proposal"],"Preparation avoids problems.")
H('4.C',3,"Presenting like a professional includes what?",
  "Clear organization, evidence, eye contact and appropriate dress",["Reading with the back turned","Mumbling","Avoiding evidence"],"Professional skills include delivery.")
H('4.C',3,"Which behavior best simulates a professional researcher's presentation?",
  "Explaining methods, results and limitations",["Telling only a story","Skipping methods","Hiding sources"],"Researchers present methods and results.")
H('4.D',3,"After presenting, an audience member suggests clearer labels on a graph. The best response is to do what?",
  "Consider the feedback and decide how to improve",["Ignore it","Argue with the audience","Delete the graph"],"Feedback helps refine work.")
H('4.D',3,"Why consider feedback from an audience of professionals?",
  "It reveals strengths and areas for improvement",["It ends the project","It is always wrong","It replaces the product"],"Professional feedback improves work.")
H('4.F',3,"At the end of a project, a student writes about what she learned and what she would change. This is an example of what?",
  "Reflecting on personal learning experiences",["Collecting data","Making a plan","Defining a problem"],"Reflection closes the study.")
H('4.F',3,"Which question best guides a final reflection on a research project?",
  "What did I learn about the process and about myself?",["What color was the poster?","Who sat nearest?","How long was lunch?"],"Reflection examines learning.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_ssadv.jsonl'))

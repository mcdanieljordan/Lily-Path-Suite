import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('127.', 1098, own='cte_21.jsonl')
def H(code, d, q, right, wrong, e):
    return B.hand(code, d, q, right, wrong, e)

# ---------- 127.145 Construction Management ----------
H('145.d.1.A',3,"A construction manager lists the steps of a remodel before starting. The list is part of:",
  "Project planning",["Site cleanup","Bid opening","Final inspection"],"Planning identifies steps before work begins.")
H('145.d.1.A',4,"Which step should come first in the sequence of a building project?",
  "Define the scope of work",["Hang the drywall","Paint the trim","Close out the permit"],"Scope comes before any task.")
H('145.d.1.B',3,"Before a framing crew starts, the manager must arrange lumber, tools, and:",
  "Workers",["Wedding guests","Movie tickets","Spare furniture"],"Resources include labor, materials, and equipment.")
H('145.d.1.B',4,"A resource list for a deck project most likely includes materials, labor, and:",
  "Equipment",["Vacation days","Tax returns","Floor wax"],"Equipment is the third resource category.")
H('145.d.1.C',3,"A schedule shows when each task starts and:",
  "Finishes",["Is forgotten","Is painted","Is insured"],"Schedules give start and finish dates.")
H('145.d.1.C',4,"A bar chart that shows tasks over time is called a:",
  "Gantt chart",["Pie chart","Scatter plot","Venn diagram"],"Gantt charts display schedules.")
H('145.d.2.A',3,"A manager checks whether a deck needs a permit by looking at:",
  "Local building codes",["Menus","Weather apps","Sports scores"],"Codes say when permits are required.")
H('145.d.2.A',4,"Which area commonly has legal rules that affect a building job?",
  "Zoning and setbacks",["Lunch breaks only","Truck color","Tool brand"],"Zoning limits what and where you can build.")
H('145.d.2.B',3,"To find the electrical code that applies to a job, a manager would consult the:",
  "Adopted code book or city office",["Phone game","Sales flyer","Yearbook"],"Adopted codes are the legal source.")
H('145.d.2.B',4,"Which source tells you which edition of a code your city has adopted?",
  "The local building department",["A tool catalog","A social media post","A radio ad"],"The building department sets the edition.")
H('145.d.2.C',3,"A code says a stair riser may not exceed a set height. Interpreting this means:",
  "Applying the limit to your stair design",["Ignoring it","Painting it","Hiding it"],"Interpretation turns text into design decisions.")
H('145.d.2.C',4,"When two code sections seem to conflict, the manager should:",
  "Ask the building official",["Pick the cheaper one","Skip both","Guess"],"The official has authority to interpret.")
H('145.d.3.A',3,"Weighing the risks and benefits of a new building product is called:",
  "Risk assessment",["Housekeeping","Decorating","Surveying"],"Assessment compares risks and benefits.")
H('145.d.3.A',4,"A new roofing material is cheaper but untested. A careful manager would:",
  "Weigh the savings against the risk of failure",["Buy it without research","Ban all new products","Choose by color"],"Balanced assessment.")
H('145.d.3.B',3,"Construction management affects society by providing:",
  "Homes, schools, and roads",["Only advertising","Only toys","Only music"],"Built environment serves communities.")
H('145.d.3.B',4,"A poorly managed project can harm a community through:",
  "Delays, cost overruns, and unsafe conditions",["Better roads","Lower taxes always","Cleaner air always"],"Bad management has public costs.")
H('145.d.4.A',3,"A problem-solving strategy begins by:",
  "Defining the problem",["Buying materials","Painting","Closing the job"],"Define first, then solve.")
H('145.d.4.A',4,"A crew keeps finding the same measuring error. The best next step is to:",
  "Identify the root cause",["Blame the newest worker","Stop measuring","Ignore it"],"Root causes prevent repeats.")
H('145.d.4.B',3,"Critical thinking means:",
  "Questioning evidence before accepting it",["Accepting every claim","Skipping analysis","Copying others"],"Critical thinking tests claims.")
H('145.d.4.B',4,"Two suppliers quote very different prices for the same lumber grade. A critical thinker would:",
  "Compare quality, delivery, and terms",["Pick the first quote","Pick the highest","Flip a coin"],"Compare the whole offer.")
H('145.d.4.C',3,"A decision matrix helps a manager:",
  "Compare options against criteria",["Paint walls","Order lunch","Sharpen saws"],"Matrices score choices.")
H('145.d.4.C',4,"In a decision matrix, the options are scored against:",
  "Weighted criteria such as cost and durability",["Random numbers","Worker nicknames","Truck mileage"],"Criteria drive the scoring.")
H('145.d.5.A',3,"A budget for a research and development build lists expected:",
  "Costs",["Birthdays","Songs","Photos"],"Budgets list costs.")
H('145.d.5.A',4,"Which item belongs in a prototype budget?",
  "Materials and labor hours",["Lunch menus of visitors","Parking tickets","Weather forecasts"],"Direct costs are budgeted.")
H('145.d.5.B',3,"One way to cut project cost without lowering quality is to reduce:",
  "Wasted material",["Safety training","Inspections","Permits"],"Waste reduction saves money safely.")
H('145.d.5.B',4,"Ordering materials cut to length instead of on-site cutting mainly reduces:",
  "Scrap and labor",["Code compliance","Inspection needs","Permit fees"],"Pre-cut saves waste.")
H('145.d.6.A',3,"A technical report should be written in a style that is:",
  "Clear and factual",["Vague and poetic","Funny only","Secret"],"Technical writing is clear.")
H('145.d.6.A',4,"Which section of a technical report states what was found?",
  "Results",["Cover decoration","Dedication","Table of toppings"],"Results report findings.")
H('145.d.6.B',3,"During a technical presentation, a speaker should:",
  "Use visuals and speak clearly",["Read silently","Face the wall","Mumble"],"Good delivery needs clarity.")
H('145.d.6.B',4,"A slide in a presentation to a client should mainly:",
  "Support the spoken point with a simple visual",["Hold all spoken words","Be unreadable","Be blank"],"Slides support the speaker.")
H('145.d.6.C',3,"A room is 12 feet by 15 feet. Its area is:",
  "180 square feet",["27 square feet","54 square feet","90 square feet"],"12 x 15 = 180.")
H('145.d.6.C',4,"A slab is 20 ft by 10 ft by 0.5 ft thick. About how many cubic feet of concrete are needed?",
  "100",["200","30","10"],"20 x 10 x 0.5 = 100.")
H('145.d.6.D',3,"Concrete gains strength as it:",
  "Cures",["Dries only in sun","Freezes","Boils"],"Curing is a chemical hydration process.")
H('145.d.6.D',4,"Steel expands when heated, which matters in construction because it can:",
  "Change the length of structural members",["Turn to wood","Become lighter","Stop rusting"],"Thermal expansion affects structures.")
H('145.d.7.A',3,"The customer's expectations for a house are best learned by:",
  "Meeting and listening to the customer",["Guessing","Reading old ads","Skipping the meeting"],"Listening reveals expectations.")
H('145.d.7.A',4,"A client says \"modern and low maintenance.\" The manager should:",
  "Ask follow-up questions to define those terms",["Assume a style","Ignore the comment","Choose the cheapest option"],"Clarify vague requests.")
H('145.d.7.B',3,"To check whether a design meets expectations, compare it to the:",
  "Customer's stated requirements",["Weather","Neighbor's car","Stock prices"],"Requirements are the yardstick.")
H('145.d.7.B',4,"A walkthrough with the client before completion is used to:",
  "Confirm the work matches what was promised",["Add secret changes","Avoid questions","Delay payment"],"Walkthroughs verify scope.")
H('145.d.7.C',3,"A customer survey after a job helps a company assess:",
  "Satisfaction",["Weather","Lumber prices","Truck tires"],"Surveys measure satisfaction.")
H('145.d.7.C',4,"A pattern of complaints about late finishes suggests the company should improve its:",
  "Scheduling",["Logo","Parking lot","Uniform color"],"Complaints point to process fixes.")
H('145.d.8.A',3,"A manager who needs to compare costs across many jobs might use:",
  "Spreadsheet software",["A paintbrush","A level","A wheelbarrow"],"Spreadsheets handle data comparisons.")
H('145.d.8.A',4,"A drone used on a large site is an example of technology used to:",
  "Survey progress from above",["Pour concrete","Cut lumber","Lay tile"],"Drones capture site data.")
H('145.d.8.B',3,"After using a new tool on a job, the manager evaluates it by asking whether it:",
  "Improved speed, cost, or quality",["Looked shiny","Was loud","Was heavy"],"Evaluate against outcomes.")
H('145.d.8.B',4,"A software trial saved no time and caused errors. The manager should likely:",
  "Reconsider adopting it",["Buy more licenses","Ignore the results","Hide the trial"],"Evidence guides adoption.")
H('145.d.8.C',3,"Which factor influences whether a small firm uses new technology?",
  "Cost",["Moon phase","Paint color","Coffee brand"],"Cost limits adoption.")
H('145.d.8.C',4,"Worker training time can influence the use of new equipment because it:",
  "Delays productivity at first",["Lowers all costs","Removes safety needs","Replaces all workers"],"Training has costs.")
H('145.d.9.A',3,"An accepted design process begins with identifying:",
  "The need or problem",["The final color","The paint brand","The truck"],"Design starts with a need.")
H('145.d.9.A',4,"After brainstorming several ideas for a shelter design, the next step is to:",
  "Select and refine the best idea",["Build all of them","Quit","Sell the ideas"],"Select, then refine.")
H('145.d.9.B',3,"A scale model of a building is used to:",
  "Visualize the design before building",["Replace the permit","Avoid planning","Cut costs to zero"],"Models show the design.")
H('145.d.9.B',4,"A set of plans includes drawings such as the floor plan and:",
  "Elevations",["Menus","Recipes","Playlists"],"Elevations show sides.")
H('145.d.9.C',3,"A design constraint is a:",
  "Limit the design must work within",["Free choice","Final color","Bonus"],"Constraints limit options.")
H('145.d.9.C',4,"Which is a design criterion for a storage shed?",
  "It must hold 500 pounds of tools",["It is a nice idea","It is someday","It looks old"],"Criteria are measurable requirements.")
H('145.d.10.A',3,"3D printing of houses is an example of an:",
  "Emerging technology in construction",["Outdated method","Hand tool","Surveying chain"],"3D printing is emerging in building.")
H('145.d.10.A',4,"Building information modeling, or BIM, is used to:",
  "Create shared 3D digital models of a project",["Mix mortar","Sharpen saws","Weigh trucks"],"BIM coordinates design data.")
H('145.d.10.B',3,"A new technology is more likely to be adopted if it:",
  "Saves money and time",["Costs more and slows work","Is unsafe","Is untested"],"Benefits drive adoption.")
H('145.d.10.B',4,"A barrier to adopting new building technology is:",
  "Codes that do not yet allow it",["Lower prices","Faster work","Fewer errors"],"Regulation can slow adoption.")
H('145.d.11.A',3,"Quality in construction means the work:",
  "Meets the specified requirements",["Is done fast at any cost","Is cheapest","Is hidden"],"Quality equals conformance.")
H('145.d.11.A',4,"Which statement best defines quality for a client?",
  "Fitness for the intended purpose",["Lowest bid","Fastest crew","Loudest tools"],"Fit for purpose.")
H('145.d.11.B',3,"A manager checks tile work by looking for even spacing and:",
  "Level surfaces",["Loud colors","Free samples","Nice labels"],"Inspection criteria.")
H('145.d.11.B',4,"A punch list records:",
  "Items that need correction before closeout",["Daily lunch orders","Payroll","Tool prices"],"Punch lists track defects.")
H('145.d.11.C',3,"Repeated rework on a task suggests the process needs:",
  "Improvement",["More paint","Nothing","Bigger trucks"],"Rework signals process problems.")
H('145.d.11.C',4,"A checklist used before concrete pours can improve quality by:",
  "Catching problems before they become permanent",["Slowing every job forever","Replacing inspections","Hiding errors"],"Prevention beats repair.")
H('145.d.12.A',3,"Using a pneumatic nail gun instead of a hammer builds framing in a more:",
  "Efficient manner",["Dangerous manner","Quiet manner","Costly manner"],"Power tools speed framing.")
H('145.d.12.A',4,"Prefabricating wall panels in a shop before moving them to the site mainly improves:",
  "Speed and consistency",["Weather","Lunch breaks","Customer names"],"Prefab improves efficiency.")
H('145.d.12.B',3,"A skilled construction manager coordinates trades so that work:",
  "Happens in the right order",["Overlaps without limits","Stops","Is random"],"Sequencing is a core skill.")
H('145.d.12.B',4,"Coordinating plumbers before drywall crews prevents:",
  "Tearing out finished walls",["Early completion","Lower safety","Higher quality"],"Sequence avoids rework.")
H('145.d.13.A',3,"After a near miss with a ladder, a manager recommends improving safety by:",
  "Adding training and inspection steps",["Removing all ladders","Ignoring the event","Hiding the report"],"Improve from incidents.")
H('145.d.13.A',4,"Reviewing near misses helps a company:",
  "Prevent future injuries",["Raise accident counts","Cut training","Avoid reports"],"Learn from near misses.")
H('145.d.13.B',3,"A guardrail on an open floor edge is a:",
  "Safety device",["Decoration","Tool","Fuel"],"Guardrails prevent falls.")
H('145.d.13.B',4,"Which device protects a worker on a roof from falling?",
  "Personal fall arrest system",["Hard hat only","Safety glasses","Ear plugs"],"Fall arrest stops falls.")
H('145.d.14.A',3,"Maintaining tools correctly keeps them:",
  "Safe and in working order",["Dull and rusty","Hidden","Broken"],"Maintenance protects workers.")
H('145.d.14.A',4,"Which task is part of proper tool care?",
  "Cleaning and storing tools after use",["Leaving them in the rain","Using them dull","Lending without checking"],"Care extends tool life.")
H('145.d.14.B',3,"Manufacturer maintenance procedures are found in the:",
  "Owner's manual",["Menu","Newspaper","Yearbook"],"Manuals list maintenance.")
H('145.d.14.B',4,"Why follow the manufacturer's schedule for servicing a saw?",
  "It keeps the saw safe and the warranty valid",["It voids the warranty","It makes the saw louder","It removes the guard"],"Following schedules protects warranty.")
H('145.d.14.C',3,"A skid steer with skipped oil changes will most likely suffer:",
  "Engine damage",["Better mileage","Quieter running","Longer life"],"Neglect damages equipment.")
H('145.d.14.C',4,"A frayed power cord left in use can result in:",
  "Shock or fire",["Faster cutting","Lower costs","Better grip"],"Negligence causes hazards.")
H('145.d.15.A',3,"Which factor raises a project's cost the most?",
  "Material prices and labor",["Choice of pencil","Color of hard hats","Parking signs"],"Materials and labor dominate cost.")
H('145.d.15.A',4,"Which of these is a hidden cost factor on a job?",
  "Delays that extend equipment rental",["Free coffee","Brand of tape","Typeface"],"Delays add costs.")
H('145.d.15.B',3,"Choosing standard-size materials instead of custom sizes usually:",
  "Reduces cost",["Raises cost","Voids codes","Delays inspection"],"Standard sizes are cheaper.")
H('145.d.15.B',4,"Value engineering aims to:",
  "Cut cost while keeping required function",["Cut quality","Add features only","Skip codes"],"Same function, lower cost.")
H('145.d.16.A',3,"A school-based learning activity in construction management should include:",
  "A real planning problem to study in depth",["A coloring page","Only a quiz","Nothing"],"Activities need depth.")
H('145.d.16.A',4,"Which topic fits an in-depth construction management study?",
  "Comparing two scheduling methods for a build",["Favorite snack","Weather trivia","Music playlist"],"Depth requires analysis.")
H('145.d.16.B',3,"An industry mentor helps a student by:",
  "Sharing real-world experience",["Doing the work","Grading papers","Hiding information"],"Mentors guide.")
H('145.d.16.B',4,"A good way to find an industry mentor is to contact:",
  "A local contractor or trade association",["A random stranger","A tourist","A stranger online with no checks"],"Local contacts are safest.")
H('145.d.16.C',3,"Presenting a project in two formats might mean a written report and a:",
  "Live presentation",["Blank page","Closed door","Song only"],"Two formats reach different audiences.")
H('145.d.16.C',4,"A panel of reviewers for a student project often includes:",
  "Teachers and industry professionals",["Strangers only","No one","Family pets"],"Panels give expert feedback.")
H('145.d.16.D',3,"A final product that uses a variety of resources might cite books, interviews, and:",
  "Websites",["Dreams","Guesses","Rumors"],"Varied sources show research.")
H('145.d.16.D',4,"Using only one source for a final product makes the work:",
  "Less reliable",["More reliable","Complete","Perfect"],"Multiple sources improve reliability.")
H('145.d.17.A',3,"An entry-level job in construction management often requires a:",
  "High school diploma plus training",["PhD","Pilot license","Medical degree"],"Entry roles need basic training.")
H('145.d.17.A',4,"Moving up to project manager usually requires:",
  "Experience and often a degree or certification",["A coin flip","Only a fast car","No training"],"Advancement requires both.")
H('145.d.17.B',3,"A growing population generally means the demand for builders will:",
  "Increase",["Disappear","Stay the same always","Hit zero"],"More people need more buildings.")
H('145.d.17.B',4,"Which source gives job outlook data for construction managers?",
  "The Bureau of Labor Statistics",["A sports site","A cookbook","A game forum"],"BLS publishes outlook.")
H('145.d.17.C',3,"Starting your own contracting company is an example of:",
  "Entrepreneurship",["Retirement","Volunteering","Apprenticeship"],"Owning a business is entrepreneurship.")
H('145.d.17.C',4,"An entrepreneur in construction needs to understand:",
  "Licensing, insurance, and bidding",["Only paint colors","Only sports","Only fashion"],"Business basics matter.")
H('145.d.17.D',3,"A person who dislikes travel may prefer a construction job that is:",
  "Based in one local area",["Always overseas","Always offshore","Always remote island"],"Personal priorities affect choices.")
H('145.d.17.D',4,"Family responsibilities can influence a career choice by affecting:",
  "Hours and travel the person can accept",["The weather","The code book","Tool prices"],"Life affects job fit.")
H('145.d.17.E',3,"Compared with a laborer, a project manager usually earns:",
  "More pay but handles more responsibility",["Less pay and less stress","Equal pay and equal duties","No pay"],"Rewards track responsibility.")
H('145.d.17.E',4,"A demand of senior management jobs is often:",
  "Long hours and high accountability",["No deadlines","No people","No decisions"],"Higher roles carry demands.")
H('145.d.17.F',3,"A manager can advance by earning a certification such as:",
  "Certified Construction Manager",["Chef certificate","Pilot license","Barista card"],"Certifications show competence.")
H('145.d.17.F',4,"Continuing education benefits a manager by:",
  "Keeping skills and code knowledge current",["Lowering skills","Replacing experience","Ending licenses"],"Learning continues.")
H('145.d.18.A',3,"An employer's responsibility to workers includes providing:",
  "A safe workplace",["Free cars","A yacht","A private jet"],"Employers must ensure safety.")
H('145.d.18.A',4,"An employee's responsibility includes:",
  "Following safety rules and doing the assigned work",["Skipping rules","Hiding injuries","Ignoring supervisors"],"Employees share duties.")
H('145.d.18.B',3,"Billing a client honestly for hours worked is an example of:",
  "Ethical practice",["Fraud","Laziness","Waste"],"Honest billing is ethical.")
H('145.d.18.B',4,"Accepting a gift from a supplier in exchange for awarding a contract is:",
  "A conflict of interest",["Good practice","Required by law","Standard billing"],"It compromises fair bidding.")
H('145.d.18.C',3,"A contract in construction is a:",
  "Legal agreement about work and payment",["Casual chat","Greeting card","Weather report"],"Contracts are binding.")
H('145.d.18.C',4,"A change order is used to:",
  "Document approved changes to scope and cost",["Cancel the permit","Hire a lawyer","Order lunch"],"Change orders record changes.")
H('145.d.19.A',3,"Applying technology to a community problem could mean designing a:",
  "Low-cost rainwater collection system",["Fashion show","Concert","Trophy"],"Technology solves problems.")
H('145.d.19.A',4,"A town has flooding on a street. A technology solution would be:",
  "Designing better drainage",["Painting the street","Closing the school","Changing the name"],"Practical engineering fix.")
H('145.d.19.B',3,"A factor that affects whether people buy a product is its:",
  "Price",["Smell of the box","Weight of the receipt","Age of the clerk"],"Price influences purchase.")
H('145.d.19.B',4,"People are more likely to buy a building product with a long:",
  "Warranty",["Delay","Wait","Instruction page"],"Warranty adds confidence.")
H('145.d.19.C',3,"Research mainly aims to:",
  "Discover new knowledge",["Sell products","Ship goods","Paint walls"],"Research seeks knowledge.")
H('145.d.19.C',4,"Development takes research findings and turns them into:",
  "Usable products or processes",["Trivia","Rumors","Posters"],"Development applies findings.")
H('145.d.19.D',3,"Making an existing product work in a new setting is called:",
  "Adaptation",["Invention","Imitation","Disposal"],"Adaptation modifies for a new use.")
H('145.d.19.D',4,"Creating something completely new that never existed is:",
  "Invention",["Imitation","Adaptation","Repair"],"Inventions are new.")
H('145.d.20.A',3,"To improve a product to meet a need, the first step is to:",
  "Identify what users need",["Pick a color","Print flyers","Order trucks"],"Needs drive improvement.")
H('145.d.20.A',4,"A hammer handle causing hand fatigue could be improved by:",
  "Adding a shock-absorbing grip",["Making it longer for no reason","Painting it","Renaming it"],"Fix the real issue.")
H('145.d.20.B',3,"Safety can be designed into a product by adding:",
  "Guards and interlocks",["Bright colors only","Louder noise only","More weight only"],"Design for safety.")
H('145.d.20.B',4,"Reliability means a product:",
  "Performs as expected over time",["Looks nice","Costs more","Is heavy"],"Reliability is consistency.")
H('145.d.20.C',3,"Applied research tries to:",
  "Solve a specific practical problem",["Explore without any goal","Avoid results","Skip testing"],"Applied research has a goal.")
H('145.d.20.C',4,"Basic research is mainly driven by:",
  "Curiosity and the search for understanding",["Sales goals","Marketing","Packaging"],"Basic research seeks understanding.")
H('145.d.20.D',3,"A project portfolio documents the work with sketches, data, and:",
  "Photos of progress",["Rumors","Guesses","Jokes"],"Portfolios record evidence.")
H('145.d.20.D',4,"A strong portfolio entry includes:",
  "Dates, descriptions, and results",["A blank page","Only a title","Nothing"],"Complete records matter.")

# ---------- 127.146 Practicum in Construction Management ----------
H('146.d.1.A',3,"On a job site, \"RFI\" stands for:",
  "Request for information",["Rapid fire inspection","Rebar fastening iron","Roof finish index"],"Common construction vocabulary.")
H('146.d.1.A',4,"A \"submittal\" in construction is a:",
  "Document or sample sent for approval",["Lunch order","Parking pass","Safety poster"],"Submittals are reviewed.")
H('146.d.1.B',3,"Clear spoken communication on a job site helps prevent:",
  "Mistakes and accidents",["Profits","Progress","Quality"],"Clarity prevents errors.")
H('146.d.1.B',4,"Which body-language habit shows respect when talking with a client?",
  "Making eye contact",["Looking at the floor","Checking a phone","Turning away"],"Nonverbal respect.")
H('146.d.1.C',3,"A manager shows weekly cost data to a client with a:",
  "Chart or table",["Rumor","Guess","Joke"],"Data is communicated visually.")
H('146.d.1.C',4,"When data shows costs rising, the manager should explain:",
  "Why the change occurred and what is planned",["Nothing","Blame others","Delay the report"],"Interpret and communicate.")
H('146.d.1.D',3,"A client who crosses their arms and frowns during a presentation is probably:",
  "Uncomfortable or disagreeing",["Fully pleased","Asleep","Cheering"],"Cues signal reactions.")
H('146.d.1.D',4,"Noticing a worker avoiding eye contact when asked about a task may signal:",
  "A problem they are hesitant to report",["A raise","Perfect work","Boredom only"],"Cues invite follow-up.")
H('146.d.1.E',3,"Active listening includes:",
  "Paraphrasing what you heard",["Interrupting","Ignoring","Texting"],"Paraphrase to confirm.")
H('146.d.1.E',4,"To clarify an unclear instruction from the owner, you should:",
  "Ask a specific question",["Guess","Skip it","Complain"],"Questions clarify.")
H('146.d.2.A',3,"Independent critical thinking on a site means:",
  "Making reasoned decisions on your own",["Waiting for orders always","Copying others","Guessing"],"Reasoning is independent.")
H('146.d.2.A',4,"Working in a team, critical thinking helps the group:",
  "Evaluate ideas fairly",["Argue forever","Skip planning","Avoid choosing"],"Teams evaluate together.")
H('146.d.2.B',3,"To solve a problem creatively, a manager might first:",
  "List several possible solutions",["Pick one at once","Ignore it","Stop work"],"Generate options.")
H('146.d.2.B',4,"A material shortage delays a task. A creative solution is to:",
  "Reorder the schedule to work on another task",["Idle the crew","Blame suppliers only","Cancel the job"],"Re-sequencing keeps work going.")
H('146.d.3.A',3,"Workplace safety rules on a site are enforced to:",
  "Protect workers from harm",["Slow work","Annoy workers","Raise costs"],"Rules protect people.")
H('146.d.3.A',4,"OSHA is a federal agency that:",
  "Sets and enforces workplace safety standards",["Sells tools","Builds houses","Writes menus"],"OSHA regulates safety.")
H('146.d.3.B',3,"Safe use of a circular saw requires keeping the guard:",
  "In place and working",["Removed","Taped back","Ignored"],"Guards prevent injury.")
H('146.d.3.B',4,"Before using a power tool, a worker should inspect:",
  "The tool and its cord",["The lunch","The parking lot","The clock"],"Inspect before use.")
H('146.d.3.C',3,"A hazard analysis looks for:",
  "Possible dangers in a task",["Free items","Tool brands","Lunch times"],"Find hazards first.")
H('146.d.3.C',4,"In a job hazard analysis, after listing the steps and hazards, the next step is to:",
  "Decide on controls to reduce the risk",["Delete the list","Skip the job","Hide the hazards"],"Controls follow identification.")
H('146.d.3.D',3,"A device that stops a machine when the guard is opened is called an:",
  "Interlock",["Adhesive","Spring clamp","Tool belt"],"Interlocks prevent access.")
H('146.d.3.D',4,"A trench box protects workers from:",
  "Cave-ins",["Rain","Noise","Cold"],"Trench boxes support walls.")
H('146.d.3.E',3,"After an injury on site, the first thing to do is to:",
  "Get help for the injured person",["Finish the job","Hide it","Delete records"],"Care first.")
H('146.d.3.E',4,"An accident report should be filed:",
  "As soon as possible, with accurate details",["Next year","Never","With false details"],"Prompt, honest reporting.")
H('146.d.4.A',3,"A positive work ethic means arriving:",
  "On time and ready to work",["Late","Unprepared","Distracted"],"Reliability matters.")
H('146.d.4.A',4,"Completing tasks without needing constant supervision shows:",
  "Responsibility",["Carelessness","Poor planning","Disrespect"],"Self-direction is valued.")
H('146.d.4.B',3,"Ethical reasoning involves asking whether an action is:",
  "Fair and honest",["Cheap","Easy","Quick"],"Ethics weighs fairness.")
H('146.d.4.B',4,"You notice a coworker using substandard fasteners to save money. Ethical reasoning suggests you:",
  "Report it to a supervisor",["Ignore it","Join in","Hide it"],"Safety outweighs savings.")
H('146.d.4.C',3,"A construction manager who reports unsafe conditions even when it costs time is acting:",
  "Ethically",["Foolishly","Carelessly","Lazily"],"Integrity over convenience.")
H('146.d.4.C',4,"Ethical practice in construction includes:",
  "Following contract terms honestly",["Altering invoices","Hiding defects","Falsifying logs"],"Honesty is core.")
H('146.d.4.D',3,"Complying with local building rules means getting:",
  "Required permits and inspections",["Free materials","A paint chart","A larger truck"],"Compliance is mandatory.")
H('146.d.4.D',4,"Working without a required permit can lead to:",
  "Fines and stop-work orders",["Praise","Bonuses","Faster approval"],"Violations have penalties.")
H('146.d.5.A',3,"In a supervised practicum, a student records learning in a:",
  "Journal or log",["Poster","Playlist","Recipe"],"Document activities.")
H('146.d.5.A',4,"A supervisor evaluates a practicum student mainly using:",
  "Observed performance and documentation",["Guesses","Weather","Luck"],"Evidence-based evaluation.")
H('146.d.5.B',3,"A technical skill in construction management is reading:",
  "Blueprints and schedules",["Poetry","Sheet music","Menus"],"Technical skills apply directly.")
H('146.d.5.B',4,"Advanced estimating skills let a manager predict a project's:",
  "Cost",["Weather","Lunch menu","Parking"],"Estimating predicts cost.")
H('146.d.5.C',3,"To build a shed advanced skills such as layout and framing need:",
  "Accuracy and a plan",["Guessing","Speed only","Luck"],"Skills depend on a plan.")
H('146.d.5.C',4,"A student building a small structure should first check the plan for:",
  "Dimensions and materials",["Song lyrics","Menu items","Hobby lists"],"Plans give dimensions.")
H('146.d.5.D',3,"Improving a product design uses a process that starts by:",
  "Testing the current design",["Painting","Selling","Hiding it"],"Test to find weaknesses.")
H('146.d.5.D',4,"After testing a prototype joint and finding it weak, the designer should:",
  "Modify the design and retest",["Ignore the test","Sell it","Paint over it"],"Iterate.")
H('146.d.5.E',3,"Maintaining tools on a practicum site includes:",
  "Cleaning and sharpening them",["Hiding them","Breaking them","Leaving them outside"],"Care for tools.")
H('146.d.5.E',4,"A dull chisel is more dangerous than a sharp one because it:",
  "Requires more force and may slip",["Cuts easier","Is lighter","Is quieter"],"Dull tools slip.")
H('146.d.5.F',3,"When designing a service such as a maintenance plan, the first step is to:",
  "Define what the customer needs",["Pick a name","Buy trucks","Print signs"],"Needs first.")
H('146.d.5.F',4,"A maintenance plan for a building should schedule tasks by:",
  "Frequency and priority",["Alphabet","Color","Cost only"],"Prioritize and schedule.")
H('146.d.5.G',3,"Growth in technical skill is shown by:",
  "Completing harder tasks with fewer errors",["Avoiding tasks","Skipping practice","Repeating mistakes"],"Growth is measurable.")
H('146.d.5.G',4,"To show growth, a student compares early work with:",
  "Recent work",["Other students' work only","Nothing","Random photos"],"Compare over time.")
H('146.d.5.H',3,"Self-evaluation of skills helps identify:",
  "Strengths and weaknesses",["Winners","Prices","Weather"],"Self-assessment finds gaps.")
H('146.d.5.H',4,"After finding a weakness in estimating, the best response is to:",
  "Practice and seek feedback",["Quit","Hide it","Blame others"],"Improve with practice.")
H('146.d.5.I',3,"Representative work samples show:",
  "Typical quality of a student's work",["Only the worst work","Nothing","Random photos"],"Samples represent ability.")
H('146.d.5.I',4,"A portfolio of work samples is useful when applying for:",
  "A job or apprenticeship",["Weather","Lunch","A park permit"],"Samples support applications.")

# ---------- 127.147 Project Management (construction tech) ----------
H('147.d.1.A',3,"Using project management, the steps of a small building project are first:",
  "Listed in order",["Ignored","Painted","Sold"],"Steps are sequenced.")
H('147.d.1.A',4,"Which of these is a project phase?",
  "Planning",["Sleeping","Shopping","Singing"],"Phases include planning, execution, closeout.")
H('147.d.1.B',3,"To complete a project, the manager must acquire people, materials, and:",
  "Funding",["Songs","Opinions","Trophies"],"Funding is a resource.")
H('147.d.1.B',4,"If the project needs a lift that the company does not own, the manager may:",
  "Rent the equipment",["Cancel the job","Borrow without asking","Skip the work"],"Renting acquires resources.")
H('147.d.1.C',3,"A project schedule lists tasks, durations, and:",
  "Due dates",["Songs","Colors","Prices of lunch"],"Schedules have dates.")
H('147.d.1.C',4,"The critical path is the sequence of tasks that:",
  "Determines the shortest total project time",["Costs least","Is easiest","Is shortest"],"Critical path sets duration.")
H('147.d.2.A',3,"Areas of a school shop project that may need rules include:",
  "Safety and building codes",["Mascots","Lunch menus","Yearbook photos"],"Regulations apply.")
H('147.d.2.A',4,"A project that involves electricity will be subject to an:",
  "Electrical code",["Dress code only","Honor roll","Fitness plan"],"Codes cover electrical work.")
H('147.d.2.B',3,"A student can locate local building rules through the:",
  "City or county website",["Cartoon","Game","Flyer"],"Official sources.")
H('147.d.2.B',4,"Standards for materials are published by organizations like:",
  "ASTM",["NASCAR","NBA","NFL"],"ASTM publishes standards.")
H('147.d.2.C',3,"Complying with a code means that the work:",
  "Meets its requirements",["Ignores them","Is hidden","Is cheaper only"],"Compliance means meeting.")
H('147.d.2.C',4,"A project fails inspection when it:",
  "Does not meet code requirements",["Is clean","Is on time","Is under budget"],"Inspections verify code.")
H('147.d.3.A',3,"Assessing a task's needs includes listing the tools, materials, and:",
  "Skills required",["Songs","Opinions","Rumors"],"Needs assessment.")
H('147.d.3.A',4,"If a task requires welding, the assessment should confirm that someone is:",
  "Qualified to weld",["Fast at typing","Good at drawing","Tall"],"Skills must match.")
H('147.d.3.B',3,"Pouring a footing before building walls is an example of:",
  "Task sequencing",["Random order","Guesswork","Cleanup"],"Order matters.")
H('147.d.3.B',4,"Each task has a required order because some tasks:",
  "Depend on others being finished first",["Are optional","Are decoration","Have no cost"],"Dependencies drive order.")
H('147.d.3.C',3,"Assessing the time frame for a task means estimating its:",
  "Duration",["Color","Weight","Smell"],"Estimate time.")
H('147.d.3.C',4,"A task is estimated at 8 hours per person. With 2 people it should take about:",
  "4 hours",["16 hours","8 hours","2 hours"],"8 / 2 = 4.")
H('147.d.3.D',3,"A flowchart of a finished project shows:",
  "The sequence of steps to the end",["Only the end","Only the start","Nothing"],"Flowcharts show sequence.")
H('147.d.3.D',4,"In a project flowchart, a diamond shape usually represents a:",
  "Decision",["Start","Process","Document"],"Diamonds are decisions.")
H('147.d.4.A',3,"To improve a project plan, the manager follows a strategy that begins with:",
  "Identifying the problem",["Painting","Selling","Hiding"],"Define the issue.")
H('147.d.4.A',4,"A recurring schedule delay is best handled by:",
  "Investigating causes and adjusting the plan",["Ignoring it","Adding more delays","Blaming weather only"],"Fix the plan.")
H('147.d.4.B',3,"Evaluating a plan means checking whether it:",
  "Meets the project goals",["Looks pretty","Is long","Is loud"],"Evaluate against goals.")
H('147.d.4.B',4,"Analyzing a project's data for patterns is an example of:",
  "Critical thinking",["Daydreaming","Copying","Skipping"],"Analysis uses data.")
H('147.d.4.C',3,"Choosing between two technologies, a manager compares:",
  "Costs and benefits",["Colors","Songs","Names"],"Compare tradeoffs.")
H('147.d.4.C',4,"A technology costs more but doubles productivity. The manager decides by weighing:",
  "Payback against the higher price",["Only the price","Only the color","Only the brand"],"Weigh payback.")
H('147.d.5.A',3,"A bill of materials lists:",
  "Every item and quantity needed",["Workers' names","Songs","Photos"],"BOM lists items.")
H('147.d.5.A',4,"A BOM for a 10-foot fence with 2 boards per foot needs how many boards?",
  "20",["10","5","2"],"10 x 2 = 20.")
H('147.d.5.B',3,"A project budget includes a cost list of materials and:",
  "Labor",["Rumors","Songs","Posters"],"Budget covers all costs.")
H('147.d.5.B',4,"Materials cost $400, labor $250, equipment $150. Total project cost is:",
  "$800",["$550","$650","$1,000"],"400 + 250 + 150 = 800.")
H('147.d.5.C',3,"A way to minimize project cost is to buy materials in:",
  "Bulk when appropriate",["Tiny packs always","Random amounts","Wrong sizes"],"Bulk discounts.")
H('147.d.5.C',4,"Reducing rework lowers cost because it saves:",
  "Time and materials",["Safety","Quality","Inspections"],"Rework wastes resources.")
H('147.d.6.A',3,"A technical report for a build should record:",
  "What was done and the results",["Gossip","Songs","Jokes"],"Facts and results.")
H('147.d.6.A',4,"Which feature belongs in a technical report on a built shelter?",
  "Measurements and materials used",["A recipe","A fantasy story","A song"],"Technical details.")
H('147.d.6.B',3,"A technical presentation to the instructor should be:",
  "Organized and accurate",["Random","Unprepared","Silent"],"Preparation counts.")
H('147.d.6.B',4,"When presenting to an instructor, the speaker should explain:",
  "What was built and what was learned",["Nothing","Only the price","Only the color"],"Explain outcomes.")
H('147.d.6.C',3,"The Pythagorean theorem is used on a build to check that a corner is:",
  "Square",["Warm","Painted","Locked"],"3-4-5 triangle.")
H('147.d.6.C',4,"A right triangle has legs of 6 ft and 8 ft. The diagonal is:",
  "10 ft",["14 ft","12 ft","48 ft"],"6^2 + 8^2 = 100.")
H('147.d.6.D',3,"A lever makes work easier by giving a:",
  "Mechanical advantage",["Disadvantage","Delay","Mistake"],"Levers multiply force.")
H('147.d.6.D',4,"A pulley system with more rope segments supporting a load requires:",
  "Less force over a longer pull",["More force","The same force exactly","No force"],"Trade force for distance.")
H('147.d.7.A',3,"To solve a drainage problem on site, a team should use technology that is:",
  "Appropriate for the task",["Fancy","Random","Oldest"],"Fit the tool.")
H('147.d.7.A',4,"A laser level is the right technology for:",
  "Setting a level reference over distance",["Mixing paint","Cutting glass","Measuring weight"],"Match tool to task.")
H('147.d.7.B',3,"Evaluating technology in a situation means asking whether it:",
  "Works well for that use",["Looks cool","Is loud","Is new only"],"Evaluate fit.")
H('147.d.7.B',4,"A GPS surveying tool saves hours on a large site but offers little on a small deck. This shows that:",
  "Value depends on the situation",["It is always best","It is never useful","Size is irrelevant"],"Context matters.")
H('147.d.7.C',3,"A factor that influences technology use in different places is:",
  "Available funding",["Nickname","Haircut","Mood"],"Funding varies.")
H('147.d.7.C',4,"Rural job sites may use fewer high-tech tools because of limited:",
  "Internet access",["Sunshine","Birds","Mailboxes"],"Infrastructure affects use.")

# ---------- 127.148 Practicum in Construction (Project Management) ----------
H('148.d.1.A',3,"A practicum student writing a work order uses vocabulary such as:",
  "Scope of work",["Free time","Favorite color","Playlist"],"Technical terms.")
H('148.d.1.A',4,"The term \"as-built\" refers to drawings that show:",
  "The structure as it was actually constructed",["The first idea","A fantasy","The budget"],"As-builts reflect reality.")
H('148.d.1.B',3,"At a toolbox talk, the speaker should be:",
  "Clear and brief",["Silent","Rude","Vague"],"Short clear talks work.")
H('148.d.1.B',4,"Which nonverbal habit helps in a team meeting?",
  "Nodding to show you understand",["Rolling eyes","Looking away","Yawning"],"Positive cues.")
H('148.d.1.C',3,"Sharing a daily progress report with a supervisor is a way to:",
  "Communicate project information",["Hide work","Avoid work","Waste time"],"Reports inform.")
H('148.d.1.C',4,"A daily log should include weather, work done, and:",
  "Delays or issues",["Rumors","Songs","Jokes"],"Logs record issues.")
H('148.d.1.D',3,"When a supervisor sighs while looking at your work, it may signal:",
  "A concern worth asking about",["Delight","Nothing","Praise"],"Read cues.")
H('148.d.1.D',4,"A coworker's tone is sharp. A good response is to:",
  "Stay calm and ask what is wrong",["Shout back","Walk off","Ignore safety"],"De-escalate.")
H('148.d.1.E',3,"Active listening on site means:",
  "Giving full attention to instructions",["Looking at your phone","Talking over","Walking away"],"Pay attention.")
H('148.d.1.E',4,"After getting directions, a worker confirms understanding by:",
  "Repeating the main points back",["Staying silent","Guessing","Leaving"],"Read-back verifies.")
H('148.d.2.A',3,"Thinking critically at a practicum site means:",
  "Questioning assumptions with evidence",["Following blindly","Quitting","Guessing"],"Evidence matters.")
H('148.d.2.A',4,"A teammate suggests skipping an inspection to save time. A critical thinker would:",
  "Weigh the risk of skipping",["Agree immediately","Hide the issue","Ignore costs"],"Think through consequences.")
H('148.d.2.B',3,"Analyzing a problem into parts helps develop:",
  "Innovative solutions",["Delays","Mistakes","Complaints"],"Break down, then solve.")
H('148.d.2.B',4,"A crew runs short of space to stage materials. An innovative solution is to:",
  "Schedule smaller, more frequent deliveries",["Stack them on a ladder","Stop the job","Hide the materials"],"Just-in-time delivery.")
H('148.d.2.C',3,"To improve a project, a student first:",
  "Finds where the process wastes time",["Paints the tools","Skips steps","Drops tasks"],"Find waste.")
H('148.d.2.C',4,"After a trial of a new layout method, the student should:",
  "Measure results and adjust",["Ignore data","Delete notes","Stop"],"Test and adjust.")
H('148.d.3.A',3,"A practicum student should read and follow the site's:",
  "Safety plan",["Dress catalog","Menu","Yearbook"],"Site safety plan applies.")
H('148.d.3.A',4,"Before climbing a scaffold, a worker should confirm it has been:",
  "Inspected by a competent person",["Painted","Moved","Weighed"],"Inspect first.")
H('148.d.3.B',3,"After a minor cut on site, the worker should:",
  "Report it and get first aid",["Hide it","Ignore it","Delay care"],"Report all injuries.")
H('148.d.3.B',4,"The first aid kit on a site should be:",
  "Stocked and easy to reach",["Locked away","Empty","Hidden"],"Be ready.")
H('148.d.4.A',3,"A good work ethic includes finishing assigned tasks:",
  "Carefully and on time",["Carelessly","Late","Never"],"Reliability.")
H('148.d.4.A',4,"A student who stays busy and asks for more work when done shows:",
  "Initiative",["Laziness","Fear","Anger"],"Initiative is valued.")
H('148.d.4.B',3,"A student is asked to sign off on work they did not do. Ethical reasoning says to:",
  "Decline and explain",["Sign anyway","Sign and hide","Forge it"],"Honesty first.")
H('148.d.4.B',4,"Using ethical reasoning, a student who finds an error in an estimate should:",
  "Report it even if it causes extra work",["Hide it","Blame a coworker","Ignore it"],"Truthfulness.")
H('148.d.4.C',3,"Rules and regulations on a job site apply to:",
  "Everyone working there",["Only the boss","Only visitors","Nobody"],"Rules cover all.")
H('148.d.4.C',4,"Following regulations consistently means doing so even when:",
  "No one is watching",["Inspectors are present","The boss is near","Someone applauds"],"Integrity.")
H('148.d.5.A',3,"In a supervised practicum, learning activities are:",
  "Documented and evaluated",["Secret","Random","Ignored"],"Document learning.")
H('148.d.5.A',4,"A practicum student's supervisor provides:",
  "Guidance and feedback",["Free gifts","Nothing","Distractions"],"Supervision.")
H('148.d.5.B',3,"Advanced technical knowledge for a practicum could include reading:",
  "Structural drawings",["Magazines","Comic strips","Novels"],"Technical reading.")
H('148.d.5.B',4,"Understanding load paths is an example of knowledge in:",
  "Structural design",["Baking","Fashion","Music"],"Loads travel to the foundation.")
H('148.d.5.C',3,"A management plan for a project describes how the project will be:",
  "Organized and controlled",["Forgotten","Hidden","Ended"],"Plans organize.")
H('148.d.5.C',4,"A management plan typically defines roles, schedule, budget, and:",
  "Communication methods",["Weather","Songs","Rumors"],"Plans define communications.")
H('148.d.5.D',3,"Applying codes to a practicum project means checking:",
  "Which rules govern the work",["Which paint is cheapest","Who is tallest","Which tool is newest"],"Verify rules.")
H('148.d.5.D',4,"A student building a ramp must check the code for maximum:",
  "Slope",["Color","Smell","Weight of paint"],"Accessibility codes limit slope.")
H('148.d.5.E',3,"A flowchart for a project helps the team:",
  "See the order of tasks",["Hide tasks","Delete tasks","Ignore tasks"],"Visual order.")
H('148.d.5.E',4,"In a flowchart, an arrow shows:",
  "The direction of flow between steps",["Cost","Weight","Color"],"Arrows connect.")
H('148.d.5.F',3,"Choosing technology for a practicum task means selecting the tool that:",
  "Fits the job best",["Is flashiest","Is loudest","Is newest"],"Right tool.")
H('148.d.5.F',4,"To mark a long straight line on a wall, the best technology is a:",
  "Chalk line or laser line",["Pencil and guess","Saw","Hammer"],"Straight references.")
H('148.d.5.G',3,"Growth in skills can be shown with:",
  "Checklists of completed competencies",["Rumors","Songs","Jokes"],"Document competencies.")
H('148.d.5.G',4,"A skills checklist that shows more tasks mastered over time demonstrates:",
  "Growth",["Decline","Waste","Delay"],"Progress is visible.")
H('148.d.5.H',3,"Evaluating strengths and weaknesses helps a student:",
  "Plan what to improve",["Avoid work","Hide errors","Blame others"],"Self-evaluation.")
H('148.d.5.H',4,"A student strong in measuring but weak in estimating should:",
  "Practice estimating more",["Stop measuring","Quit","Ignore estimating"],"Target weaknesses.")
H('148.d.5.I',3,"Work samples collected in a practicum might include:",
  "Photos, drawings, and reports",["Rumors","Songs","Jokes"],"Samples show work.")
H('148.d.5.I',4,"Why keep work samples?",
  "To show your skills to employers",["To hide work","To lose them","To delay"],"Evidence of skill.")
H('146.d.1.E',5,"A foreman gives a three-step instruction over a noisy saw. The best active-listening move is to:",
  "Move somewhere quieter and repeat the steps back",["Nod and guess the steps","Wait and ask a coworker later","Start work and fix errors afterward"],"Confirm understanding.")
H('147.d.5.A',5,"A deck needs 24 joists. Waste allowance of 10 percent means the bill of materials should list how many joists?",
  "27",["26","25","30"],"24 x 1.1 = 26.4, round up to 27.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_21.jsonl'))

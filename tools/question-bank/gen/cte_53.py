import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('127.', 1130, own='cte_53.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 299 Entrepreneurship ----
H('299.d.1.A',3,"A new juice bar closed after eight months. Which finding is most likely to explain its failure?",
  "Rent and supplies cost more than its sales brought in",["The shop had too many happy customers","The menu was printed in color","The owner posted on social media"],"Failed businesses often run out of cash when costs exceed income.")
H('299.d.1.A',4,"Studying why many start-ups fail helps an entrepreneur to:",
  "Avoid repeating common mistakes such as poor planning",["Guarantee a profit","Skip a business plan","Ignore customers"],"Learning from failures reduces risk.")
H('299.d.1.B',3,"Which is a financial risk faced by an entrepreneur?",
  "Losing personal savings invested in the business",["Having a busy schedule","Choosing a logo","Meeting new people"],"Owners often put their own money at risk.")
H('299.d.1.B',4,"An entrepreneur who borrows heavily to open a store faces the risk of:",
  "Being unable to repay the loan if sales are low",["Receiving free inventory","Paying no interest","Avoiding all competition"],"Debt must be repaid regardless of sales.")
H('299.d.1.C',3,"Before launching a food truck, an entrepreneur weighs possible profit against possible loss. This is comparing:",
  "Risk versus opportunity",["Style versus color","Price versus weather","Hours versus holidays"],"Entrepreneurs evaluate risk and reward.")
H('299.d.1.C',4,"A business with high startup costs but strong demand offers:",
  "Large opportunity along with significant risk",["No risk","No opportunity","Guaranteed success"],"Reward and risk often rise together.")
H('299.d.1.D',3,"Compared with an employee, an entrepreneur usually has:",
  "More control over decisions and more responsibility for results",["No responsibility","A guaranteed paycheck","No decisions to make"],"Owners decide and bear the outcome.")
H('299.d.1.D',4,"Which is a typical difference between owning a business and working for one?",
  "Owners earn income only after expenses are paid",["Employees pay all business bills","Owners always work fewer hours","Employees set company policy alone"],"Owners are paid from profit after expenses.")
H('299.d.1.E',3,"A person with strong self-motivation, creativity, and comfort with risk shows:",
  "Aptitude for entrepreneurship",["A lack of skills","No interest in business","Weak planning"],"These traits fit entrepreneurs.")
H('299.d.1.E',4,"A self-assessment shows a student dislikes uncertainty and prefers steady pay. This suggests the student might:",
  "Be better suited to a stable employee role than owning a start-up",["Be sure to succeed as an owner","Have no skills","Need no income"],"Personality fit matters.")
H('299.d.1.F',3,"An entrepreneur who tracks income and expenses each month is:",
  "Managing the organization's finances",["Wasting time","Avoiding taxes","Ignoring customers"],"Record keeping is basic financial management.")
H('299.d.1.F',4,"Why must an owner manage cash flow carefully?",
  "Bills come due even when customers have not yet paid",["Cash flow does not matter","Bills are optional","Customers pay in advance always"],"Timing of cash determines whether bills can be paid.")
H('299.d.1.G',3,"A calculated risk is one that an entrepreneur takes after:",
  "Researching the possible outcomes",["Flipping a coin","Ignoring information","Copying a rumor"],"Calculated risks are informed risks.")
H('299.d.1.G',4,"Which action shows a sound approach to risk-taking?",
  "Testing a product with a small group before a full launch",["Spending all savings on day one","Skipping research","Copying a competitor without thought"],"Small tests limit risk.")
H('299.d.1.H',3,"A competitive advantage is something that lets a business:",
  "Do better than its competitors in a way customers value",["Charge any price","Avoid taxes","Skip marketing"],"Advantages set a business apart.")
H('299.d.1.H',4,"A shop that offers same-day repair when rivals take a week has a competitive advantage in:",
  "Speed of service",["Price only","Location only","Product color only"],"Faster service is a differentiator.")
H('299.d.1.I',3,"Interviewing a local business owner is useful because the owner can describe:",
  "The real risks and rewards of ownership",["Last night's game","Weather","Gossip"],"First-hand experience informs students.")
H('299.d.1.I',4,"Before an interview with an owner, a student should:",
  "Prepare thoughtful questions",["Show up unprepared","Ask only about gossip","Skip taking notes"],"Preparation shows respect.")
H('299.d.1.J',3,"Psychology helps an entrepreneur understand customers by explaining:",
  "Why people choose or avoid a product",["Weather patterns","Shipping routes","Tax law"],"Motives and feelings drive choices.")
H('299.d.1.J',4,"Sociology helps explain customer behavior by studying how:",
  "Groups, culture, and peers influence buying",["Prices are calculated","Taxes are filed","Machines are fixed"],"Social influences shape demand.")
H('299.d.2.A',3,"Which is a basic type of business formation?",
  "Sole proprietorship",["Weather station","Shipping lane","Union card"],"Sole proprietorship, partnership, and corporation are basic forms.")
H('299.d.2.A',4,"A business owned and run by one person is a:",
  "Sole proprietorship",["Corporation","Cooperative","Franchise chain"],"One-owner businesses are sole proprietorships.")
H('299.d.2.B',3,"A benefit of a sole proprietorship is that it:",
  "Is simple and inexpensive to start",["Protects personal assets from all debts","Has unlimited investors","Pays no taxes"],"Simple setup is an advantage.")
H('299.d.2.B',4,"A drawback of a sole proprietorship is that the owner:",
  "Is personally liable for business debts",["Has no control","Cannot hire staff","Cannot earn profit"],"Unlimited personal liability is a major drawback.")
H('299.d.2.C',3,"If a sole proprietor's business is sued and loses, the owner's personal property may be:",
  "At risk to pay the judgment",["Fully protected","Doubled","Taxed less"],"Owners are personally liable.")
H('299.d.2.C',4,"A limited liability company generally protects owners by:",
  "Limiting personal responsibility for business debts",["Eliminating all taxes","Preventing profit","Requiring no records"],"LLCs separate personal and business liability.")
H('299.d.3.A',3,"A business plan's operations section lists the materials, facilities, and:",
  "Personnel needed to run the business",["Favorite songs","Weather","Hobbies"],"Operations describe resources.")
H('299.d.3.A',4,"A start-up bakery's technology needs might include:",
  "A point-of-sale system",["A telescope","A canoe","A typewriter only"],"Operations include technology.")
H('299.d.3.B',3,"A timeline of tasks for opening a business shows:",
  "What must be done and by when",["Only the profits","Only the staff","Only the logo"],"Timelines sequence tasks.")
H('299.d.3.B',4,"Obtaining a permit before opening day is an example of a task with a:",
  "Deadline that depends on approval time",["Random date","Unlimited timeframe","Cost of zero"],"Approvals affect schedules.")
H('299.d.3.C',3,"Which is a start-up cost an owner must list?",
  "Equipment and initial inventory",["Weather","Hobbies","Opinions"],"Start-up costs include assets.")
H('299.d.3.C',4,"Wages and salaries for employees are part of a business's:",
  "Ongoing operating costs",["Profit","Revenue","Loan interest only"],"Payroll is an operating expense.")
H('299.d.3.D',3,"Rent, utilities, and insurance are examples of:",
  "Costs of operating a business",["Revenue","Profit","Savings"],"Operating costs recur.")
H('299.d.3.D',4,"Analyzing monthly costs helps an owner decide:",
  "Where spending can be reduced",["Who to hire as a friend","Which holiday to take","What color to paint"],"Cost analysis finds savings.")
H('299.d.3.E',3,"Estimating how much money is needed on hand to operate a business helps avoid:",
  "Running out of cash",["Making sales","Hiring staff","Paying taxes"],"Working capital prevents cash shortages.")
H('299.d.3.E',4,"A new store expects $4,000 in monthly costs and no sales for the first two months. Cash needed to cover those months is about:",
  "$8,000",["$2,000","$4,000","$16,000"],"4,000 x 2 = 8,000.")
H('299.d.3.F',3,"Seeking advice from an industry mentor helps an entrepreneur:",
  "Learn from real experience",["Avoid planning","Skip research","Ignore customers"],"Mentors share practical wisdom.")
H('299.d.3.F',4,"Reviewing an actual business case with a mentor can help an owner analyze:",
  "Real decisions and their results",["Fictional stories only","Weather","Music"],"Case review builds judgment.")
H('299.d.3.G',3,"An income statement shows a business's:",
  "Revenue, expenses, and profit over a period",["Weather","Employee birthdays","Store hours"],"It summarizes performance.")
H('299.d.3.G',4,"Comparing financial statements month to month helps an owner:",
  "Spot trends and ways to improve profit",["Hide losses","Avoid planning","Skip taxes"],"Trends guide decisions.")
H('299.d.3.H',3,"Cash burn is the rate at which a business:",
  "Spends its cash reserves",["Earns profit","Hires staff","Collects tax"],"Burn measures cash outflow.")
H('299.d.3.H',4,"A start-up with $60,000 in cash that spends $10,000 more than it earns each month has about how many months before it runs out?",
  "6 months",["3 months","10 months","60 months"],"60,000 / 10,000 = 6.")
H('299.d.4.A',3,"A business contributes to the economic well-being of a community by:",
  "Creating jobs and paying local taxes",["Closing early","Raising unemployment","Avoiding customers"],"Jobs and taxes support communities.")
H('299.d.4.A',4,"A new factory in a small town can help local stores by:",
  "Increasing the number of customers with paychecks",["Lowering wages to zero","Closing roads","Removing jobs"],"Employment boosts spending.")
H('299.d.4.B',3,"A business can ensure economic stability by:",
  "Planning finances and diversifying its customers",["Spending all income at once","Relying on one customer only","Ignoring costs"],"Planning supports stability.")
H('299.d.4.B',4,"Relying on one large customer for most sales is risky because:",
  "Losing that customer could cause a major drop in income",["It guarantees growth","It reduces costs","It removes competition"],"Diversification protects stability.")
H('299.d.4.C',3,"A business owner is responsible for providing:",
  "A safe workplace for employees and customers",["Free products to all","A swimming pool","Unlimited breaks"],"Safety is a legal responsibility.")
H('299.d.4.C',4,"A restaurant must follow health codes to protect:",
  "Customers from foodborne illness",["The menu font","The parking lot","Advertising"],"Health regulations protect the public.")
H('299.d.4.D',3,"A business investing in its community might:",
  "Sponsor a local youth team",["Pollute local streams","Ignore local needs","Avoid hiring locally"],"Community investment builds goodwill.")
H('299.d.4.D',4,"Which action is an example of a business investing in community development?",
  "Funding scholarships for local students",["Raising prices","Closing a store","Cutting wages"],"Scholarships invest in people.")
H('299.d.5.A',3,"A growth strategy in which a business opens more locations is called:",
  "Expansion",["Liquidation","Downsizing","Dissolution"],"Adding locations expands the business.")
H('299.d.5.A',4,"Which growth strategy may be most feasible for a small shop with limited cash?",
  "Selling products online to reach more customers",["Building a factory","Buying a competitor","Opening ten stores at once"],"Online sales grow reach at low cost.")
H('299.d.5.B',3,"One way an owner can get financial support to grow is by:",
  "Applying for a bank loan",["Ignoring costs","Printing money","Quitting"],"Loans provide capital.")
H('299.d.5.B',4,"An investor who gives money in exchange for part ownership is providing:",
  "Equity financing",["Debt financing","Free services","Insurance"],"Equity trades ownership for funds.")
H('299.d.5.C',3,"One way to determine what a business is worth is to look at its:",
  "Assets, earnings, and market conditions",["Logo color","Owner's age","Store smell"],"Valuation uses financial data.")
H('299.d.5.C',4,"A buyer values a business partly by how much profit it earns because:",
  "Profit shows what the business may earn in the future",["Profit hides risk","Profit is random","Profit is illegal"],"Earnings suggest future returns.")
H('299.d.5.D',3,"One path for exiting a business is to:",
  "Sell it to another owner",["Ignore it","Raise debt","Hire a mascot"],"Selling is a common exit.")
H('299.d.5.D',4,"Passing a family business to the next generation is an example of a:",
  "Succession exit",["Bankruptcy","Merger","Franchise"],"Succession transfers ownership within a family.")
H('299.d.5.E',3,"Before preparing to sell a business, an owner should have:",
  "Organized financial records",["No records","Only verbal agreements","Missing receipts"],"Buyers want clear records.")
H('299.d.5.E',4,"A factor that can raise a business's sale value is:",
  "Steady, documented profits",["Unpaid taxes","Unclear ownership","Lost customers"],"Documented earnings add value.")
H('299.d.6.A',3,"To research a problem at a real work site, a student should first:",
  "Observe operations and gather facts",["Guess","Blame workers","Ignore it"],"Observation reveals problems.")
H('299.d.6.A',4,"A student notices long customer waits at a cafe. A good first research step is to:",
  "Track wait times at different hours",["Remove the counter","Cut staff","Ignore it"],"Data clarifies the issue.")
H('299.d.6.B',3,"Researching how to resolve a business problem includes:",
  "Comparing possible solutions",["Choosing the first idea","Ignoring cost","Avoiding experts"],"Compare options before choosing.")
H('299.d.6.B',4,"A report on a business problem should include the problem, evidence, and:",
  "Recommended solutions",["A joke","A rumor","A slogan"],"Reports recommend action.")
H('299.d.6.C',3,"A proposal for future business opportunities should describe:",
  "The opportunity, the cost, and expected benefits",["Weather","Hobbies","Birthdays"],"Proposals justify action.")
H('299.d.6.C',4,"Which detail most strengthens a proposal to a business owner?",
  "Evidence that customers want the new service",["A longer font","A louder voice","Fancy borders only"],"Evidence persuades.")
H('299.d.6.D',3,"An alliance with another business can help by:",
  "Sharing resources and customers",["Cutting all ties","Raising conflict","Hiding information"],"Alliances create mutual benefits.")
H('299.d.6.D',4,"A coffee shop and a bakery cross-promote each other's products. This is an example of:",
  "A business alliance",["A monopoly","A merger","Price fixing"],"Cross-promotion is an alliance.")

# ---- 300 Practicum in Entrepreneurship ----
H('300.d.1.A',3,"A start-up founder explains a new idea to a mentor. Clear communication includes:",
  "Stating the idea simply and backing it with examples",["Using only jargon","Speaking too quietly to hear","Skipping details"],"Clarity helps listeners understand.")
H('300.d.1.A',4,"A founder sends investors a one-page summary with a simple graph. This is an example of using:",
  "Written and visual communication together",["Only silence","Only rumors","Only a phone call"],"Combining media supports understanding.")
H('300.d.1.B',3,"A client explains what they want built. Which action shows active listening?",
  "Taking notes and asking follow-up questions",["Checking your phone","Finishing their sentences","Changing the subject"],"Note-taking and questions clarify needs.")
H('300.d.1.B',4,"A founder repeats back a customer's request to be sure it is right. This technique is called:",
  "Paraphrasing to confirm understanding",["Interrupting","Daydreaming","Ignoring"],"Restating verifies meaning.")
H('300.d.1.C',3,"A pitch to a small group of friends about a new app is best delivered as an:",
  "Informal presentation",["Formal board meeting","Legal hearing","Press conference"],"Casual settings suit informal talks.")
H('300.d.1.C',4,"For a formal investor presentation, a founder should:",
  "Rehearse and organize the talk with clear sections",["Wing it","Read every word aloud","Skip the closing"],"Preparation improves delivery.")
H('300.d.1.D',3,"A founder reviews sales data and tells the team what it means. This is:",
  "Analyzing and communicating information",["Hiding results","Guessing","Ignoring numbers"],"Interpretation turns data into insight.")
H('300.d.1.D',4,"After analyzing survey results, the most useful message to a team is:",
  "The key finding and what action to take",["All raw data without comment","Only the highest score","A joke"],"Messages should lead to action.")
H('300.d.1.E',3,"A positive way to handle a client who is upset about late delivery is to:",
  "Listen, apologize, and offer a solution",["Argue","Hang up","Blame them"],"Respectful service retains clients.")
H('300.d.1.E',4,"Following up with a client after a project to ask for feedback helps:",
  "Maintain a strong relationship",["End the relationship","Avoid improvement","Raise complaints"],"Follow-up shows care.")
H('300.d.2.A',3,"A founder facing a drop in sales studies the data before choosing a response. This is:",
  "Critical thinking",["Panicking","Guessing","Ignoring facts"],"Critical thinking uses evidence.")
H('300.d.2.A',4,"A team debates two product ideas and compares evidence for each. This shows critical thinking in a:",
  "Group setting",["Solo guess","Random vote","Coin flip"],"Groups can weigh evidence together.")
H('300.d.2.B',3,"To gather information for a decision about a supplier, a founder could:",
  "Compare prices, reviews, and delivery times",["Pick randomly","Use the first result","Ask nobody"],"Research informs choices.")
H('300.d.2.B',4,"A founder wants to know whether customers will buy a product. A technical research step is to:",
  "Run a small survey or test sale",["Wait","Assume yes","Copy a rival's ad"],"Testing gives evidence.")
H('300.d.2.C',3,"A start-up's packaging costs too much. A creative solution might be to:",
  "Redesign the package with cheaper recyclable materials",["Hide the product","Raise every price","Stop shipping"],"Innovation can cut costs.")
H('300.d.2.C',4,"Breaking a problem like slow shipping into causes such as packing, carrier, and address errors is:",
  "Analyzing the elements of the problem",["Avoiding the issue","Blaming the carrier only","Ignoring customers"],"Analysis isolates causes.")
H('300.d.3.A',3,"A workshop where a founder sells products should have:",
  "Clear exits and safety rules posted",["Blocked doors","No fire extinguisher","Loose cords everywhere"],"Safety rules protect people.")
H('300.d.3.A',4,"An entrepreneur who trains workers on safe equipment use is:",
  "Following workplace safety rules consistently",["Wasting time","Breaking policy","Avoiding duty"],"Training prevents injury.")
H('300.d.3.B',3,"An online store should protect customer data by:",
  "Using secure passwords and encrypted payment systems",["Posting card numbers","Sharing logins","Using weak passwords"],"Security protects customers.")
H('300.d.3.B',4,"A start-up employee receives an email asking for account passwords. Cybersecurity policy says to:",
  "Report it as suspected phishing",["Reply with the password","Forward it to everyone","Click the link"],"Phishing must be reported.")
H('300.d.4.A',3,"A supplier offers a hidden kickback for placing a large order. An ethical entrepreneur should:",
  "Decline it and keep the deal honest",["Accept it quietly","Ask for more","Share it with friends"],"Kickbacks are unethical.")
H('300.d.4.A',4,"When two choices are legal but one is more honest, an entrepreneur committed to ethics will:",
  "Choose the more honest choice",["Choose the cheaper one","Choose randomly","Choose the secret one"],"Ethics go beyond bare legality.")
H('300.d.4.B',3,"A founder realizes a product has a safety flaw but a recall will cost money. Integrity says to:",
  "Notify customers and fix the problem",["Hide the flaw","Wait for complaints","Blame customers"],"Safety comes before profit.")
H('300.d.4.B',4,"A founder who keeps a promise to a customer even when it costs the company shows:",
  "Integrity",["Carelessness","Weakness","Poor planning"],"Integrity means doing right despite cost.")
H('300.d.4.C',3,"A food business must follow health inspection rules. This is an example of complying with:",
  "Regulations for its industry",["Fashion trends","Sports rules","Music laws"],"Industry regulations apply to specific businesses.")
H('300.d.4.C',4,"An entrepreneur selling online must follow laws about:",
  "Truthful advertising and collecting sales tax",["Weather reports","School grades","Parking only"],"E-commerce has legal duties.")
H('300.d.5.A',3,"A supervised entrepreneurship experience should include:",
  "A record of activities and what was learned",["No records","Only grades","Only photos"],"Documentation shows learning.")
H('300.d.5.A',4,"A student writes a weekly reflection on a pop-up shop experience. This is:",
  "Evaluating a learning activity",["Wasting time","Advertising","Cheating"],"Reflection evaluates learning.")
H('300.d.5.B',3,"Advanced technical skills for an entrepreneur might include:",
  "Building a basic online store or budget model",["Doing no research","Ignoring tools","Copying a template blindly"],"Technical skills support the business.")
H('300.d.5.B',4,"To deepen technical knowledge, a student could:",
  "Shadow an owner during bookkeeping tasks",["Avoid new tasks","Skip training","Refuse feedback"],"Observation builds skill.")
H('300.d.5.C',3,"Information technology tools a small business may use to manage work include:",
  "Accounting and scheduling software",["Carbon paper","A telegraph","A paper map only"],"IT tools improve efficiency.")
H('300.d.5.C',4,"Inventory software helps a shop to:",
  "Track stock levels and reorder on time",["Hide products","Lose sales","Raise prices"],"Systems track inventory.")
H('300.d.5.D',3,"A memorandum differs from a business letter because it is usually:",
  "Sent inside an organization",["Sent to customers","Sent to the press","Handwritten"],"Memos are internal.")
H('300.d.5.D',4,"A professional email to a customer should include:",
  "A clear subject line and polite greeting",["All capital letters","No greeting","Slang"],"Format shows professionalism.")
H('300.d.5.E',3,"Applying entrepreneurship processes to grow a business could include:",
  "Researching a new market for the product",["Stopping all marketing","Reducing quality","Closing the shop"],"Growth requires research.")
H('300.d.5.E',4,"Adding a second product line to reach new customers is a:",
  "Growth strategy",["Failure sign","Tax strategy","Retirement plan"],"New lines grow revenue.")
H('300.d.5.F',3,"Growth in technical skill competencies appears when a student:",
  "Performs tasks more independently and accurately over time",["Needs more help each time","Avoids tasks","Makes more errors"],"Independence shows growth.")
H('300.d.5.F',4,"A student rates skills in September and again in March to see:",
  "Progress over the practicum",["Nothing","Weather changes","Price changes"],"Comparing ratings shows growth.")
H('300.d.5.G',3,"Evaluating strengths and weaknesses helps a student:",
  "Plan improvement",["Hide mistakes","Skip tasks","Avoid feedback"],"Self-assessment guides growth.")
H('300.d.5.G',4,"A student is strong at selling but weak at bookkeeping. A smart step is to:",
  "Seek training in bookkeeping",["Avoid bookkeeping","Stop selling","Hide the weakness"],"Address weak areas.")
H('300.d.5.H',3,"Which item is a good work sample for an entrepreneurship portfolio?",
  "A business plan section you wrote",["A game score","A grocery list","A recipe"],"Samples show relevant skills.")
H('300.d.5.H',4,"A portfolio piece is strongest when it:",
  "Shows real work, accurate and well presented",["Is borrowed","Is unrelated","Is unfinished"],"Quality and relevance matter.")

# ---- 309 Principles of Education and Training ----
H('309.d.1.A',3,"Which is a common sign of stress?",
  "Trouble sleeping and irritability",["Steady energy","Calm focus","Improved appetite"],"Stress often disrupts sleep and mood.")
H('309.d.1.A',4,"A teacher who feels constant worry, racing thoughts, and tense muscles may be experiencing:",
  "Anxiety",["Boredom","Hunger","Excitement only"],"These are common anxiety symptoms.")
H('309.d.1.B',3,"A healthy work-life boundary for a teacher is to:",
  "Set a time to stop grading each evening",["Grade until midnight daily","Answer messages at all hours","Skip meals"],"Boundaries protect rest.")
H('309.d.1.B',4,"Which habit helps a teacher separate work from home life?",
  "Leaving school tasks at school when possible",["Working every weekend","Checking email constantly","Skipping hobbies"],"Boundaries support balance.")
H('309.d.1.C',3,"An education career can affect lifestyle through:",
  "A school-year schedule and time outside the classroom",["Guaranteed daily travel","No planning needs","No paperwork"],"Calendars and workloads shape lifestyle.")
H('309.d.1.C',4,"Teachers often spend evenings and weekends on tasks like:",
  "Planning lessons and grading",["Selling products","Repairing roads","Driving buses only"],"Work extends beyond school hours.")
H('309.d.1.D',3,"Maintaining work-life balance helps educators avoid:",
  "Burnout",["Salary","Training","Planning"],"Balance prevents exhaustion.")
H('309.d.1.D',4,"An educator who schedules exercise and family time into the week is practicing:",
  "Work-life balance",["Overwork","Neglect","Isolation"],"Planned personal time supports balance.")
H('309.d.1.E',3,"A strategy for managing wellness is to:",
  "Get regular sleep, exercise, and healthy meals",["Skip sleep","Eat only snacks","Avoid breaks"],"Basic habits support health.")
H('309.d.1.E',4,"A school counselor suggests short mindfulness breaks for staff. This is a strategy to manage:",
  "Stress and wellness",["Budget","Schedules","Bus routes"],"Mindfulness helps reduce stress.")
H('309.d.2.A',3,"A teacher posting on a school-related social account should:",
  "Keep content professional and protect student privacy",["Share student photos freely","Post grades","Post rumors"],"Professional conduct online matters.")
H('309.d.2.A',4,"Using a class social media page to share learning tips is an appropriate:",
  "Educational use of social media",["Personal gossip","Unsafe sharing","Private messages to students"],"Educational posts serve learning.")
H('309.d.2.B',3,"Which web-based resource could help teach reading?",
  "An interactive reading website approved by the district",["A random video game","An unsafe chat room","An unrelated store"],"Approved resources support instruction.")
H('309.d.2.B',4,"Before using a website in class, a teacher should check that it is:",
  "Accurate, age-appropriate, and approved",["Colorful only","Free of any content","Popular only"],"Evaluate resources first.")
H('309.d.3.A',3,"Which job is in the education and training field?",
  "Elementary school teacher",["Pilot","Plumber","Chef"],"Teachers work in education.")
H('309.d.3.A',4,"A person who helps adults learn workplace skills may work in:",
  "Corporate training",["Aviation","Farming","Mining"],"Training roles exist outside schools.")
H('309.d.3.B',3,"A school counselor is an education professional who mainly:",
  "Supports students' academic, social, and career needs",["Drives buses","Cooks lunch","Cleans buildings"],"Counselors support students.")
H('309.d.3.B',4,"A librarian in a school supports learning by:",
  "Helping students find and use information",["Teaching math only","Coaching football","Fixing computers only"],"Librarians support research and reading.")
H('309.d.3.C',3,"Communication, patience, and organization are skills that:",
  "Transfer across many careers in education and training",["Apply only to teaching math","Are useless","Apply only to coaches"],"Transferable skills apply broadly.")
H('309.d.3.C',4,"A teacher's classroom management skills could also help in a career as a:",
  "Corporate trainer or camp director",["Surgeon","Pilot","Architect"],"Leading groups transfers.")
H('309.d.3.D',3,"Results from a career interest assessment can help a student:",
  "Identify careers that fit their interests",["Choose a favorite color","Guess the weather","Pick lunch"],"Assessments guide exploration.")
H('309.d.3.D',4,"A student whose assessment shows strengths in helping others and explaining ideas might explore:",
  "Teaching or tutoring careers",["Aircraft repair","Deep sea welding","Mining"],"Assessment results suggest fit.")
H('309.d.4.A',3,"Investigating trends in education means looking at:",
  "Changes in how and what students learn over time",["Weather","Sports scores","Fashion"],"Trends shape schooling.")
H('309.d.4.A',4,"The growth of online learning is an example of a:",
  "Trend that influenced education",["Weather event","Sports season","Tax change"],"Technology changed instruction.")
H('309.d.4.B',3,"Pedagogy is the study of how to teach:",
  "Children",["Pilots","Machines","Animals"],"Pedagogy focuses on teaching children.")
H('309.d.4.B',4,"Andragogy is the study of how to teach:",
  "Adults",["Infants","Pets","Teens only"],"Andragogy focuses on adult learners.")
H('309.d.4.C',3,"To predict the job market for teachers, a student could use:",
  "Labor statistics and school enrollment trends",["Horoscopes","Rumors","Guesses"],"Data supports predictions.")
H('309.d.4.C',4,"Growing student enrollment in a region suggests:",
  "Greater demand for teachers",["Less demand","No change","No jobs"],"More students need more teachers.")
H('309.d.4.D',3,"Families and caregivers support education by:",
  "Encouraging learning at home and communicating with teachers",["Avoiding schools","Skipping homework","Ignoring grades"],"Family involvement helps students.")
H('309.d.4.D',4,"A parent-teacher conference helps to:",
  "Share information about a student's progress",["Replace class","Hide grades","Cancel school"],"Conferences connect home and school.")
H('309.d.5.A',3,"A principal's role in a school is to:",
  "Lead the school and support teachers and students",["Teach every class","Drive buses","Cook lunches"],"Principals lead schools.")
H('309.d.5.A',4,"A teaching assistant mainly:",
  "Supports the classroom teacher and students",["Writes state laws","Runs the district","Sets taxes"],"Assistants help instruction.")
H('309.d.5.B',3,"A rural school often differs from an urban school in that it may have:",
  "Fewer students and longer travel distances",["More subways","More skyscrapers","No teachers"],"Rural districts cover large areas.")
H('309.d.5.B',4,"A charter school is a type of:",
  "Public school with its own governing agreement",["Private college","Daycare only","Business"],"Charters are public schools with flexibility.")
H('309.d.5.C',3,"A teacher salary schedule usually pays more for:",
  "More years of experience and additional education",["Fewer hours","Less training","A longer commute only"],"Pay rises with experience and degrees.")
H('309.d.5.C',4,"Two districts post different salary schedules. To compare them fairly, a student should look at:",
  "Starting pay, raises, and benefits",["Logo colors","Mascots","Building age"],"Compare total compensation.")
H('309.d.5.D',3,"Incentives that can attract teachers to high-need areas include:",
  "Stipends and loan forgiveness",["Longer commutes","Less pay","No benefits"],"Incentives encourage service.")
H('309.d.5.D',4,"A stipend is:",
  "An extra payment for specific work or circumstances",["A lesson plan","A discipline report","A class roster"],"Stipends supplement salary.")
H('309.d.5.E',3,"A reliable source for information on teaching careers is:",
  "A state education agency website",["A rumor","An unsigned post","A random ad"],"Official sources are reliable.")
H('309.d.5.E',4,"To learn about teacher certification requirements, a student should consult:",
  "The state's educator certification office",["A friend's guess","A game forum","A coupon site"],"Official offices give accurate rules.")
H('309.d.6.A',3,"Observing a classroom teacher helps a student learn:",
  "The duties and daily routines of an educator",["Nothing","Only tests","Only breaks"],"Observation shows real work.")
H('309.d.6.A',4,"Tutoring a younger student is a way to practice:",
  "Teaching duties in a supervised setting",["Cooking","Driving","Painting"],"Tutoring builds teaching skill.")
H('309.d.6.B',3,"A visual aid in a lesson is meant to:",
  "Help students understand the content",["Distract students","Fill space","Replace the teacher"],"Visuals support learning.")
H('309.d.6.B',4,"When evaluating a handout for students, a future teacher should ask whether it is:",
  "Clear, accurate, and appropriate for the age group",["Long","Colorful only","Written in tiny print"],"Quality materials fit learners.")
H('309.d.6.C',3,"A lesson objective states:",
  "What students should know or be able to do",["The teacher's lunch","The bus schedule","The fire drill"],"Objectives guide instruction.")
H('309.d.6.C',4,"After direct instruction, a lesson often includes:",
  "Guided practice, independent practice, and assessment",["Nothing","Only recess","Only homework"],"Lesson parts follow a sequence.")
H('309.d.6.D',3,"Adapting a lesson for a student who needs more time might include:",
  "Extra time and simplified directions",["Less learning","Ignoring the student","Removing the lesson"],"Adaptations meet needs.")
H('309.d.6.D',4,"A teacher offering both written and oral directions is:",
  "Adapting instruction to meet different needs",["Wasting time","Repeating unnecessarily","Ignoring planning"],"Multiple formats help learners.")
H('309.d.6.E',3,"A personal philosophy of education is a set of beliefs about:",
  "Why and how teaching and learning should happen",["Weather","Lunch menus","Bus routes"],"Philosophy shapes teaching.")
H('309.d.6.E',4,"A future teacher who believes every student can learn will likely:",
  "Set high expectations and offer support",["Give up on struggling students","Teach only the top group","Avoid challenging tasks"],"Beliefs shape practice.")
H('309.d.7.A',3,"Classroom equipment such as a projector is best used to:",
  "Present information clearly to all students",["Distract students","Replace teaching","Store supplies"],"Technology supports delivery.")
H('309.d.7.A',4,"Before class, a teacher should test technology to:",
  "Avoid delays during instruction",["Waste time","Hide problems","Annoy students"],"Preparation prevents downtime.")
H('309.d.7.B',3,"A classroom management tool such as a seating chart helps a teacher:",
  "Organize students and monitor behavior",["Hide students","Avoid planning","Cancel class"],"Seating charts support management.")
H('309.d.7.B',4,"Posted rules and consistent routines help prevent:",
  "Disruptions during class",["Learning","Attendance","Homework"],"Routines reduce disruptions.")
H('309.d.7.C',3,"An effective learning environment is one that is:",
  "Safe, organized, and respectful",["Chaotic","Unsafe","Unwelcoming"],"Effective environments support learning.")
H('309.d.7.C',4,"Which feature supports a positive learning environment?",
  "Clear expectations and encouragement",["Harsh punishment only","Constant noise","Unfair rules"],"Positive climate helps learners.")
H('309.d.7.D',3,"Restorative practices focus on:",
  "Repairing harm and rebuilding relationships",["Punishing only","Ignoring behavior","Removing students"],"Restorative approaches heal relationships.")
H('309.d.7.D',4,"A teacher who has two students talk through a conflict and agree on solutions is using:",
  "A restorative approach",["A punishment","A test","A lecture"],"Dialogue repairs harm.")
H('309.d.7.E',3,"Scaffolding in a lesson means:",
  "Providing temporary supports that are gradually removed",["Giving no help","Removing all steps","Giving the answer immediately"],"Scaffolds help learners progress.")
H('309.d.7.E',4,"A differentiated lesson provides:",
  "Different ways to learn the same objective",["The same task for all","No structure","Only lectures"],"Differentiation meets diverse needs.")
H('309.d.8.A',3,"A degree plan for a teaching career usually includes:",
  "College coursework and student teaching",["No training","Only a test","Only a license fee"],"Teaching requires coursework and practice.")
H('309.d.8.A',4,"Some paths to becoming a teacher include alternative certification for those who:",
  "Already hold a bachelor's degree in another field",["Skip college","Lack any degree","Never study"],"Alternative paths exist.")
H('309.d.8.B',3,"A graduation plan for a student who wants to teach could include:",
  "Courses in education and dual-credit options",["No courses","Only gym","Only art"],"Plans align classes to goals.")
H('309.d.8.B',4,"Taking an education and training course in high school helps a student:",
  "Explore teaching before college",["Avoid college","Skip graduation","Miss opportunities"],"Early exposure helps decisions.")
H('309.d.8.C',3,"Dual enrollment lets high school students:",
  "Earn college credit while in high school",["Skip high school","Pay no tax","Avoid exams"],"Dual enrollment saves time.")
H('309.d.8.C',4,"A student interested in teaching could take a dual-credit course in:",
  "Child development or introduction to education",["Auto repair","Welding","Aviation"],"Related dual credit helps.")
H('309.d.8.D',3,"A scholarship is money for education that:",
  "Does not have to be repaid",["Must be repaid with interest","Is a loan","Is a tax"],"Scholarships are gifts.")
H('309.d.8.D',4,"A grant for college students is usually based on:",
  "Financial need or specific criteria",["Height","Hair color","Favorite song"],"Grants meet need or criteria.")
H('309.d.8.E',3,"A community college program can prepare students for:",
  "An associate degree or transfer to a university",["No career","Only high school","Only retirement"],"Community colleges offer transfer paths.")
H('309.d.8.E',4,"A student compares technical and community college programs by looking at:",
  "Cost, length, and career outcomes",["Mascot","Colors","Cafeteria menus"],"Compare programs by outcomes.")
H('309.d.8.F',3,"When comparing universities for teacher preparation, a student should consider:",
  "Accreditation and certification pass rates",["Parking stripes","Slogans","Architecture only"],"Accreditation matters.")
H('309.d.8.F',4,"A university education program that places students in classrooms early offers:",
  "Valuable hands-on experience",["No benefit","Less learning","Higher risk"],"Early field work builds skills.")
H('309.d.9.A',3,"A basic professional portfolio includes a resume, a cover letter, and:",
  "Letters of recommendation or work samples",["Game scores","Receipts","Photos of pets"],"Portfolios show qualifications.")
H('309.d.9.A',4,"A resume for an education career should highlight:",
  "Relevant experience such as tutoring or volunteering",["Unrelated hobbies only","Gossip","Fashion"],"Relevant experience matters.")
H('309.d.9.B',3,"When presenting a portfolio to a school principal, a student should:",
  "Speak confidently and explain each item",["Read silently","Skip items","Argue"],"Presentation skills matter.")
H('309.d.9.B',4,"After presenting a portfolio, a student should:",
  "Ask for feedback and thank the reviewer",["Leave without a word","Argue about feedback","Ignore comments"],"Feedback helps improvement.")
H('309.d.10.A',3,"Targeted observation means watching a class with:",
  "A specific focus, such as how the teacher gives directions",["No focus","Eyes closed","Just chatting"],"Focus gives purpose.")
H('309.d.10.A',4,"Before observing, a student should read the:",
  "Observation guidelines and objectives",["Lunch menu","Bus schedule","Sports page"],"Preparation improves observation.")
H('309.d.10.B',3,"An objective observation record states:",
  "What was seen or heard without opinion",["Personal judgments","Guesses about motives","Rumors"],"Objective notes record facts.")
H('309.d.10.B',4,"Which note is objective?",
  "'The student raised a hand four times.'",["'The student is lazy.'","'The student hates math.'","'The student is the best.'"],"Facts, not judgments.")
H('309.d.10.C',3,"Classroom observations can shape a future teacher's philosophy by:",
  "Showing which practices help students learn",["Hiding methods","Limiting ideas","Ending interest"],"Observation informs beliefs.")
H('309.d.10.C',4,"After seeing a teacher use positive reinforcement successfully, an observer may:",
  "Adopt it in their own approach",["Reject all methods","Ignore it","Criticize it only"],"Observed success influences practice.")
H('309.d.10.D',3,"A quality of an effective classroom is that students are:",
  "Engaged and respected",["Bored","Ignored","Silent only"],"Engagement and respect mark effectiveness.")
H('309.d.10.D',4,"A teacher circulating, giving feedback, and keeping a clear routine shows:",
  "Effective classroom management",["Poor planning","Disorganization","Neglect"],"Active monitoring helps.")

# ---- 310 Human Growth and Development ----
H('310.d.1.A',3,"Theories help in understanding human development because they:",
  "Organize ideas about how and why people change",["Predict the weather","Set prices","Choose careers"],"Theories explain patterns.")
H('310.d.1.A',4,"A developmental theory is most useful when it is:",
  "Supported by research evidence",["Based on rumor","Untested","Contradictory"],"Evidence supports theories.")
H('310.d.1.B',3,"Heredity and environment are both:",
  "Influences on human development",["Unrelated","Irrelevant","Identical"],"Nature and nurture both matter.")
H('310.d.1.B',4,"The 'nature versus nurture' debate asks how much development is shaped by:",
  "Genes versus experiences",["Money versus time","Age versus height","Food versus clothes"],"Heredity versus environment.")
H('310.d.1.C',3,"Early psychological theories influence modern theories by:",
  "Providing ideas that later researchers test and refine",["Being ignored","Being identical","Ending research"],"Science builds on earlier work.")
H('310.d.1.C',4,"Piaget's stages of cognitive development still guide teachers because they:",
  "Describe how children's thinking changes with age",["Ban homework","Set tuition","Predict adult jobs"],"Stage theories shape teaching.")
H('310.d.1.D',3,"A research method in which scientists watch children at play is:",
  "Observation",["Experiment only","Survey only","Interview only"],"Observation records behavior.")
H('310.d.1.D',4,"A study that follows the same group of people over many years is a:",
  "Longitudinal study",["Cross-section","Survey","Case rumor"],"Longitudinal studies track change.")
H('310.d.1.E',3,"Pedagogy and andragogy differ because pedagogy focuses on teaching:",
  "Children, while andragogy focuses on adults",["Adults, while andragogy focuses on children","Pets and people","Teachers only"],"Pedagogy vs andragogy.")
H('310.d.1.E',4,"Adult learners often prefer learning that is:",
  "Practical and self-directed",["Always memorization","Never relevant","Punishment-based"],"Andragogy emphasizes relevance.")
H('310.d.2.A',3,"A nutrient needed in higher amounts before and during pregnancy to help prevent neural tube defects is:",
  "Folic acid",["Caffeine","Sugar","Sodium"],"Folic acid supports fetal development.")
H('310.d.2.A',4,"A pregnant woman's diet should include extra:",
  "Nutrients such as protein, iron, and calcium",["Empty calories","Alcohol","Tobacco"],"Nutrients support growth.")
H('310.d.2.B',3,"Prenatal checkups are important because they:",
  "Monitor the health of mother and baby",["Replace healthy habits","Cause illness","Are optional for safety"],"Medical care reduces risk.")
H('310.d.2.B',4,"Good prenatal health practices include avoiding:",
  "Alcohol, tobacco, and drugs",["Fruits","Sleep","Walking"],"Substances harm the fetus.")
H('310.d.2.C',3,"The three stages of prenatal development are the germinal, embryonic, and:",
  "Fetal stage",["Infant stage","Toddler stage","Adult stage"],"Prenatal stages end with fetal development.")
H('310.d.2.C',4,"Major organs and body systems begin forming mostly during the:",
  "Embryonic stage",["Fetal stage only","Newborn stage","Toddler stage"],"Organ formation occurs early.")
H('310.d.2.D',3,"Genes are inherited from:",
  "Both biological parents",["Neither parent","Only the doctor","Only the grandparents"],"Each parent contributes.")
H('310.d.2.D',4,"A baby's sex is determined by:",
  "The sex chromosomes inherited from the parents",["Diet","Weather","Birth order"],"Chromosomes determine sex.")
H('310.d.2.E',3,"An environmental factor that can harm a developing fetus is:",
  "Exposure to harmful chemicals or infections",["Gentle music","Healthy food","Rest"],"Teratogens harm development.")
H('310.d.2.E',4,"Harmful agents that can cause birth defects are called:",
  "Teratogens",["Vitamins","Nutrients","Hormones only"],"Teratogens cause defects.")
H('310.d.3.A',3,"A toddler learning to walk shows growth in:",
  "Physical development",["Emotional only","Cognitive only","None"],"Walking is motor development.")
H('310.d.3.A',4,"Separation anxiety in infants is part of their:",
  "Emotional and social development",["Physical only","Language only","Math skills"],"Attachment matters.")
H('310.d.3.B',3,"Erikson's first stage focuses on infants developing:",
  "Trust",["Independence","Initiative","Industry"],"Trust versus mistrust.")
H('310.d.3.B',4,"A theory that emphasizes the bond between infant and caregiver is:",
  "Attachment theory",["Learning theory","Stage theory","Memory theory"],"Attachment theory focuses on bonds.")
H('310.d.3.C',3,"A family can influence an infant's development by providing:",
  "Love, care, and stimulation",["Neglect","Isolation","Danger"],"Family care shapes growth.")
H('310.d.3.C',4,"Cultural practices may influence how families:",
  "Feed, soothe, and teach infants",["Choose weather","Set prices","Drive cars"],"Culture shapes parenting.")
H('310.d.3.D',3,"Talking and reading to a baby helps:",
  "Language and brain development",["Slow growth","Reduce learning","Cause delays"],"Interaction builds language.")
H('310.d.3.D',4,"Providing safe toys that match a toddler's age supports:",
  "Exploration and skill growth",["Danger","Boredom","Isolation"],"Age-appropriate play helps.")
H('310.d.3.E',3,"A safety technique for infants is to place them to sleep:",
  "On their backs in a bare crib",["On their stomachs on a pillow","With loose blankets","On a sofa"],"Back sleeping reduces SIDS risk.")
H('310.d.3.E',4,"Which practice protects a toddler's safety?",
  "Using outlet covers and childproof latches",["Leaving medicine out","Leaving stairs open","Leaving water unattended"],"Childproofing prevents injury.")
H('310.d.3.F',3,"A developmentally appropriate guidance technique for a toddler who grabs toys is to:",
  "Redirect them to another activity",["Spank them","Scream","Ignore safety"],"Redirection works for toddlers.")
H('310.d.3.F',4,"Giving simple choices to a toddler helps them:",
  "Practice independence while staying safe",["Control the household","Avoid rules","Become frightened"],"Choices build autonomy.")
H('310.d.4.A',3,"A preschooler hopping on one foot shows growth in:",
  "Physical development",["Language","Money","Memory"],"Hopping is motor skill.")
H('310.d.4.A',4,"Preschoolers rapidly expand their:",
  "Vocabulary",["Salary","Height charts","Tax records"],"Language grows quickly.")
H('310.d.4.B',3,"Erikson's stage for preschoolers is called initiative versus:",
  "Guilt",["Trust","Shame","Inferiority"],"Initiative vs guilt.")
H('310.d.4.B',4,"Piaget's preoperational stage includes:",
  "Pretend play and symbolic thinking",["Abstract logic","Formal operations","Reflexes only"],"Preschoolers use symbols.")
H('310.d.4.C',3,"Preschoolers learn social skills by:",
  "Playing and interacting with peers and family",["Staying alone","Avoiding adults","Watching nothing"],"Social learning occurs through play.")
H('310.d.4.C',4,"Media exposure affects preschoolers because they:",
  "Imitate what they see and hear",["Ignore it","Forget it","Cannot see it"],"Children model behavior.")
H('310.d.4.D',3,"Strategies to optimize preschool development include:",
  "Reading together and encouraging play",["Isolation","Constant screens","Strict silence"],"Rich experiences help growth.")
H('310.d.4.D',4,"Preschool programs support development by:",
  "Offering structured play and early learning",["Replacing family","Teaching adult skills","Limiting play"],"Programs build readiness.")
H('310.d.4.E',3,"A health practice for preschoolers is:",
  "Regular handwashing and vaccinations",["Skipping check-ups","Sharing toothbrushes","Avoiding sleep"],"Prevention protects health.")
H('310.d.4.E',4,"Car seats for young children are used to:",
  "Reduce injury in crashes",["Slow driving","Save fuel","Replace seat belts for adults"],"Restraints protect children.")
H('310.d.4.F',3,"Positive guidance for a preschooler who hits is to:",
  "Calmly explain the rule and teach a better response",["Hit back","Ignore always","Yell loudly"],"Teach alternatives.")
H('310.d.4.F',4,"A time-in strategy helps a preschooler by:",
  "Staying with them to calm down and talk",["Locking them away","Shaming them","Ignoring them"],"Connection helps regulation.")
H('310.d.5.A',3,"Children in early elementary grades rapidly develop:",
  "Reading, writing, and math skills",["Retirement plans","Tax knowledge","Driving skills"],"School-age cognitive growth.")
H('310.d.5.A',4,"A school-age child making friends and following group rules shows growth in:",
  "Social development",["Prenatal development","Language loss","Memory loss"],"Peers become important.")
H('310.d.5.B',3,"Erikson's stage for school-age children is industry versus:",
  "Inferiority",["Trust","Autonomy","Initiative"],"Industry vs inferiority.")
H('310.d.5.B',4,"Piaget's concrete operational stage is when children begin to:",
  "Think logically about concrete events",["Reason only with symbols","Use only reflexes","Think abstractly"],"Logic about real objects emerges.")
H('310.d.5.C',3,"Teachers influence school-age children by:",
  "Shaping attitudes toward learning",["Having no effect","Replacing parents","Ending curiosity"],"Teachers affect motivation.")
H('310.d.5.C',4,"Peer groups become more important in middle childhood because children:",
  "Seek acceptance and friendship",["Avoid others","Avoid learning","Avoid rules"],"Belonging matters.")
H('310.d.5.D',3,"A strategy to support school-age development is to:",
  "Encourage reading and organized activities",["Remove all play","Discourage questions","Limit friendships"],"Enrichment supports growth.")
H('310.d.5.D',4,"Praising effort rather than only results helps children:",
  "Build persistence and confidence",["Quit easily","Fear tasks","Avoid challenges"],"Effort praise builds resilience.")
H('310.d.5.E',3,"Health habits for school-age children include:",
  "Balanced meals and daily physical activity",["Skipping meals","Constant screens","Less sleep"],"Healthy habits support growth.")
H('310.d.5.E',4,"Bicycle helmets for children help to:",
  "Prevent head injuries",["Increase speed","Replace training","Reduce exercise"],"Helmets protect.")
H('310.d.5.F',3,"Effective guidance for a school-age child includes:",
  "Clear rules and logical consequences",["Random punishment","No limits","Public shaming"],"Logical consequences teach.")
H('310.d.5.F',4,"Allowing a child to fix a spill they caused is a:",
  "Logical consequence",["Reward","Punishment by shame","Ignoring"],"Consequence matches behavior.")
H('310.d.6.A',3,"Puberty is a time of major:",
  "Biological and physical change",["Economic change","Weather change","Language loss"],"Puberty changes bodies.")
H('310.d.6.A',4,"During adolescence, the brain area for planning and judgment:",
  "Is still maturing",["Is finished","Is absent","Is unchanged since birth"],"The prefrontal cortex matures into early adulthood.")
H('310.d.6.B',3,"A key emotional task of adolescence is forming:",
  "A sense of identity",["A new alphabet","Taxes","Language"],"Identity development.")
H('310.d.6.B',4,"Adolescents often rely more on:",
  "Peer relationships",["Imaginary friends","Infant care","Isolation"],"Peers gain importance.")
H('310.d.6.C',3,"Erikson's stage for adolescents is identity versus:",
  "Role confusion",["Trust","Guilt","Doubt"],"Identity vs role confusion.")
H('310.d.6.C',4,"Piaget's formal operational stage allows adolescents to:",
  "Reason abstractly and think hypothetically",["Use only senses","Use only reflexes","Think only concretely"],"Abstract reasoning develops.")
H('310.d.6.D',3,"Family influences adolescents by:",
  "Providing support, values, and guidance",["Having no role","Ignoring needs","Ending contact"],"Family remains important.")
H('310.d.6.D',4,"Social media influences adolescents by:",
  "Shaping self-image and peer interaction",["Having no effect","Ending friendships","Replacing school"],"Online life affects development.")
H('310.d.6.E',3,"Strategies to support adolescent development include:",
  "Open communication and healthy activities",["Strict silence","Isolation","Ignoring concerns"],"Communication supports teens.")
H('310.d.6.E',4,"Encouraging teens to join clubs and sports helps them:",
  "Build skills, belonging, and confidence",["Avoid friends","Reduce learning","Isolate"],"Activities help growth.")
H('310.d.6.F',3,"A health and safety technique for adolescents is:",
  "Avoiding risky behavior such as texting while driving",["Skipping sleep","Ignoring seat belts","Using substances"],"Safe choices reduce harm.")
H('310.d.6.F',4,"Getting enough sleep is especially important for teens because it:",
  "Supports growth, learning, and mood",["Reduces homework","Replaces food","Prevents friends"],"Sleep matters for development.")
H('310.d.6.G',3,"A good guidance technique for a teen who breaks a curfew is to:",
  "Discuss expectations and set fair consequences",["Ignore it","Yell","Ground forever"],"Clear expectations help.")
H('310.d.6.G',4,"Involving a teen in making rules tends to:",
  "Increase cooperation",["Increase rebellion always","Eliminate all conflict","Remove rules"],"Participation builds buy-in.")
H('310.d.7.A',3,"An agency that protects children's rights and welfare is:",
  "Child Protective Services",["A zoo","A bank","A bakery"],"CPS investigates abuse and neglect.")
H('310.d.7.A',4,"Services a child welfare agency may provide include:",
  "Investigating abuse reports and arranging safe placements",["Selling toys","Printing books","Building roads"],"Agencies protect children.")
H('310.d.7.B',3,"A resource for parents needing child-care help is:",
  "A community family support center",["A movie theater","A car lot","A mall"],"Community resources assist families.")
H('310.d.7.B',4,"A hotline for reporting suspected child abuse is a resource for:",
  "Protecting children's safety",["Selling goods","Sports","Entertainment"],"Hotlines protect children.")
H('310.d.7.C',3,"Cultural diversity affects child care because families may have different:",
  "Beliefs and practices about raising children",["Eyesight","Heights","Hairstyles only"],"Culture shapes parenting.")
H('310.d.7.C',4,"Changing demographics, such as more single-parent households, can affect:",
  "The kinds of support children and families need",["Weather","Tax rates only","Transportation only"],"Society changes needs.")
H('310.d.7.D',3,"Neglect is when a caregiver fails to provide a child's:",
  "Basic needs such as food, shelter, and supervision",["Toys","Phone","Gifts"],"Neglect is failure to meet needs.")
H('310.d.7.D',4,"Which is a way to help prevent child abuse?",
  "Parenting education and community support",["Ignoring signs","Isolating families","Blaming children"],"Support lowers risk.")
H('310.d.7.E',3,"Regular check-ups and vaccinations help children by:",
  "Preventing illness and detecting problems early",["Causing illness","Replacing food","Avoiding school"],"Preventive care protects health.")
H('310.d.7.E',4,"Safe storage of household chemicals protects children from:",
  "Accidental poisoning",["Learning","Playing","Reading"],"Safe storage prevents poisoning.")
H('310.d.7.F',3,"Community members help protect children by:",
  "Reporting suspected abuse and supporting families",["Ignoring signs","Spreading rumors","Staying silent"],"Everyone has a role.")
H('310.d.7.F',4,"Laws that require teachers and doctors to report suspected abuse are called:",
  "Mandatory reporting laws",["Zoning laws","Tax laws","Traffic laws"],"Mandated reporters must report.")
H('310.d.8.A',3,"Early adulthood (about 18 to 40) is a time when many people:",
  "Choose careers and form long-term relationships",["Retire","Learn to walk","Start kindergarten"],"Early adults establish independence.")
H('310.d.8.A',4,"Erikson's stage for young adults is intimacy versus:",
  "Isolation",["Trust","Guilt","Despair"],"Intimacy vs isolation.")
H('310.d.8.B',3,"Physical abilities such as strength and endurance typically peak in:",
  "Early adulthood",["Infancy","Late adulthood","Preschool"],"Physical peak is early adult.")
H('310.d.8.B',4,"Cognitive development in early adulthood may include:",
  "Greater practical problem solving and decision making",["Loss of memory entirely","No new learning","Only reflexes"],"Reasoning matures with experience.")
H('310.d.8.C',3,"Society and culture influence early adults through:",
  "Expectations about education, work, and family",["Weather","Sports only","Music only"],"Social norms shape choices.")
H('310.d.8.C',4,"Economic conditions can influence early adults' decisions about:",
  "Education, careers, and housing",["Height","Eye color","Birth order"],"Economy shapes decisions.")
H('310.d.8.D',3,"Family and friends help early adults by providing:",
  "Social support and encouragement",["Isolation","Stress only","Debt only"],"Relationships support well-being.")
H('310.d.8.D',4,"Building healthy relationships in early adulthood supports:",
  "Emotional well-being",["Loneliness","Conflict only","Isolation"],"Connection benefits health.")
H('310.d.9.A',3,"Middle adulthood (about 40 to 65) often includes changes in:",
  "Physical abilities such as vision and metabolism",["Becoming an infant","Learning to crawl","Starting kindergarten"],"Gradual physical changes occur.")
H('310.d.9.A',4,"A common midlife physical change is:",
  "Needing reading glasses",["Growing new teeth","Rapid growth spurts","Loss of all memory"],"Presbyopia is common.")
H('310.d.9.B',3,"Erikson's stage for middle adults is generativity versus:",
  "Stagnation",["Trust","Initiative","Intimacy"],"Generativity vs stagnation.")
H('310.d.9.B',4,"Generativity means:",
  "Contributing to the next generation through work, family, or community",["Withdrawing","Staying idle","Avoiding responsibility"],"Giving back defines this stage.")
H('310.d.9.C',3,"Society and culture may influence middle adults' choices about:",
  "Career changes and caring for family",["Learning to walk","Starting school","Naming newborns"],"Midlife roles are social.")
H('310.d.9.C',4,"Many middle adults are 'sandwiched' between caring for:",
  "Their children and their aging parents",["Pets and plants","Students and teachers","Bosses and clients"],"Sandwich generation.")
H('310.d.9.D',3,"Family and relationships in midlife can provide:",
  "Emotional support and a sense of purpose",["Only stress","Only costs","Isolation"],"Relationships help well-being.")
H('310.d.9.D',4,"Staying socially connected in midlife supports:",
  "Mental and physical health",["Illness","Loneliness","Inactivity"],"Social ties protect health.")
H('310.d.10.A',3,"Late adulthood (about 65 and older) is associated with changes in:",
  "Physical health and energy",["Learning to walk","Birth","Kindergarten"],"Aging brings physical change.")
H('310.d.10.A',4,"Regular exercise in late adulthood can help to:",
  "Maintain strength and balance",["Increase falls","Reduce mobility","Cause illness"],"Activity preserves function.")
H('310.d.10.B',3,"Erikson's final stage focuses on integrity versus:",
  "Despair",["Trust","Industry","Intimacy"],"Integrity vs despair.")
H('310.d.10.B',4,"Reflecting on a life well lived and feeling satisfied is called:",
  "Ego integrity",["Despair","Isolation","Role confusion"],"Integrity means acceptance.")
H('310.d.10.C',3,"Society influences older adults through attitudes about aging and:",
  "Retirement and caregiving expectations",["Starting school","Learning letters","Naming babies"],"Culture shapes aging.")
H('310.d.10.C',4,"Negative stereotypes about aging can:",
  "Harm older adults' well-being and opportunities",["Help them","Increase income","Reduce illness"],"Ageism harms.")
H('310.d.10.D',3,"Family and friends help older adults by:",
  "Providing companionship and care",["Isolating them","Ignoring them","Blaming them"],"Support improves quality of life.")
H('310.d.10.D',4,"Staying socially active in late adulthood is linked to:",
  "Better mental health",["Greater loneliness","More illness","Less activity"],"Social ties help.")
H('310.d.11.A',3,"Assessing interests, aptitudes, and abilities can help a student:",
  "Choose a career in a human development field",["Pick a favorite color","Guess weather","Skip class"],"Self-assessment guides careers.")
H('310.d.11.A',4,"A student who enjoys working with young children and has strong patience may explore:",
  "Early childhood education",["Aviation","Welding","Mining"],"Interests and aptitudes align.")
H('310.d.11.B',3,"A career opportunity in human development is:",
  "Child care worker",["Pilot","Plumber","Chef"],"Child care supports development.")
H('310.d.11.B',4,"Entrepreneurial opportunities in this field include:",
  "Opening a child care center",["Mining","Farming","Shipping"],"Owners can start care centers.")
H('310.d.11.C',3,"A good method for finding an entry-level job is to:",
  "Search job boards and ask contacts for leads",["Wait","Guess","Avoid people"],"Active searching works.")
H('310.d.11.C',4,"Volunteering at a child care center can help a student:",
  "Gain experience and references",["Waste time","Avoid skills","Lose interest"],"Volunteering builds experience.")

H('299.d.2.A',4,"Two friends pool money, share profits, and run a bakery together under a written agreement. Which basic form of business formation fits best?",
  "A partnership",["A sole proprietorship","A nonprofit foundation","A government agency"],"Two or more co-owners sharing profits form a partnership.")
H('300.d.5.G',4,"After a mock sales call, a practicum student lists strong greetings but weak product knowledge. This list is a:",
  "Self-evaluation of strengths and weaknesses",["Sales report","Tax form","Price list"],"Listing strengths and weaknesses is self-evaluation.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_53.jsonl'))

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('127.', 1117, own='cte_40.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---------- 241 Principles of Business, Marketing, and Finance ----------
H('241.d.1.A',3,"When the price of a popular sneaker rises sharply, buyers usually purchase fewer pairs. This reflects the principle of:",
  "demand",["inflation","tariffs","barter"],"As price rises, quantity demanded generally falls.")
H('241.d.1.A',4,"A bakery finds that at $2 per muffin it sells 100, but at $3 it sells 60. If a flood destroys wheat crops and muffin costs rise, suppliers will most likely:",
  "offer fewer muffins unless prices rise",["offer more muffins at lower prices","stop charging customers","ignore costs"],"Higher costs reduce supply at old prices.")
H('241.d.1.B',3,"A haircut and a pair of shoes are examples of which, respectively?",
  "a service and a good",["a good and a service","two services","two goods"],"Services are actions; goods are physical items.")
H('241.d.1.B',4,"Which item below is a service rather than a good?",
  "A plumber repairing a leaking pipe",["A bicycle","A bag of rice","A new laptop"],"A repair is work done for someone.")
H('241.d.1.C',3,"A company that makes cars, a store that sells them, and a bank that finances them represent which kinds of business?",
  "manufacturing, retail, and financial services",["only retail","only agriculture","only government"],"Different businesses perform different functions.")
H('241.d.1.C',4,"A store that buys goods from producers and sells them to consumers is classified as:",
  "retail",["extractive","manufacturing","nonprofit only"],"Retailers sell directly to consumers.")
H('241.d.1.D',3,"The owner of a small shop who keeps all profits and is personally responsible for all debts runs a:",
  "sole proprietorship",["corporation","cooperative","franchise"],"Sole proprietors have unlimited liability.")
H('241.d.1.D',4,"Which form of ownership gives owners limited liability and sells shares of stock?",
  "corporation",["sole proprietorship","general partnership","barter group"],"Corporations are separate legal entities.")
H('241.d.1.E',3,"In a typical company, the human resources department is responsible for:",
  "hiring and supporting employees",["manufacturing goods only","printing money","setting taxes"],"HR handles recruitment and employee matters.")
H('241.d.1.E',4,"A company chart showing who reports to whom is called an:",
  "organizational chart",["income statement","balance sheet","price list"],"Org charts show structure and reporting lines.")
H('241.d.1.F',3,"A report showing a company's revenues and expenses over a period is the:",
  "income statement",["balance sheet","bank statement","pay stub"],"Income statements show profit or loss.")
H('241.d.1.F',4,"A balance sheet is built on which equation?",
  "assets = liabilities + owner's equity",["revenue = profit","assets = cash","expenses = income"],"The accounting equation balances.")
H('241.d.1.G',3,"The pattern of expansion, peak, contraction, and trough in the economy is the:",
  "business cycle",["supply chain","tax cycle","trade route"],"Economies move through phases.")
H('241.d.1.G',4,"During which phase of the business cycle do unemployment and spending typically fall the most?",
  "recession",["expansion","recovery","peak"],"Contraction brings less spending and more layoffs.")
H('241.d.2.A',3,"A manager knowingly hides a defect in a product from customers. This is:",
  "an unethical business practice",["legal in every case","good marketing","required by law"],"Concealing defects is dishonest.")
H('241.d.2.A',4,"Which action is an ethical business practice?",
  "Accurately labeling ingredients on a food product",["Padding the expense report","Copying a competitor's secret recipe","Overstating product claims"],"Honesty in labeling is ethical.")
H('241.d.2.B',3,"A choice can be legal yet still considered unethical. Which describes that case?",
  "A company legally dumps waste but knows it harms a neighborhood",["A company follows all laws and is fair","A company breaks a law","A company is audited"],"Legal does not always mean ethical.")
H('241.d.2.B',4,"Ethical choices are guided by values, legal choices by laws, and moral choices by:",
  "personal beliefs of right and wrong",["tax rates","company slogans","market prices"],"Morals are rooted in personal conviction.")
H('241.d.3.A',3,"An economy where tradition decides what to produce, such as a village that farms the way it always has, is a:",
  "traditional economy",["command economy","market economy","mixed economy"],"Custom guides production.")
H('241.d.3.A',4,"In a command economy, who decides what is produced?",
  "the central government",["consumers only","each family","foreign banks"],"The government plans production.")
H('241.d.3.B',3,"Private ownership, profit motive, competition, and consumer choice describe the:",
  "private enterprise system",["command system","tribal system","barter system"],"Private enterprise relies on markets.")
H('241.d.3.B',4,"In a private enterprise system, businesses succeed mainly by:",
  "meeting consumer needs at a profit",["following government orders","avoiding customers","fixing all prices"],"Profit rewards good service.")
H('241.d.3.C',3,"If a company's expenses are greater than its revenues, it has:",
  "a loss",["a profit","a surplus","a dividend"],"Revenue minus expenses decides the result.")
H('241.d.3.C',4,"Which change would most directly increase a company's profit?",
  "Lowering production costs while keeping sales steady",["Raising rent without raising sales","Hiring more staff with no new sales","Buying unused equipment"],"Lower costs improve profit.")
H('241.d.4.A',3,"A company that sells products in many countries is participating in the:",
  "global economy",["local barter","closed market","home market only"],"Business crosses borders.")
H('241.d.4.A',4,"One way global business affects society is by:",
  "creating jobs and offering more product choices",["ending all trade","removing competition","stopping innovation"],"Global trade expands choices.")
H('241.d.4.B',3,"Trade within a country's borders is:",
  "domestic trade",["world trade","import trade","embargo"],"Domestic means within one nation.")
H('241.d.4.B',4,"Selling goods between two countries is an example of:",
  "world trade",["domestic trade","a local sale","a barter fair"],"International trade crosses borders.")
H('241.d.4.C',3,"Goods that a country sells to other countries are called:",
  "exports",["imports","tariffs","quotas"],"Exports leave the country.")
H('241.d.4.C',4,"If imports exceed exports, a country has a:",
  "trade deficit",["trade surplus","balanced budget","tax cut"],"A deficit means more imports than exports.")
H('241.d.5.A',3,"A government that sets safety rules for food and drugs is acting as a:",
  "regulator",["competitor","customer","supplier"],"Governments regulate for safety.")
H('241.d.5.A',4,"A government agency that buys paper and computers for its offices is acting as a:",
  "consumer",["regulator only","tax collector only","competitor only"],"Governments also buy goods.")
H('241.d.5.B',3,"Collecting taxes and enforcing contracts are activities performed by:",
  "government",["consumers only","labor unions","stock exchanges"],"Governments tax and enforce laws.")
H('241.d.5.B',4,"Which is an activity of government in business?",
  "Issuing licenses and enforcing antitrust laws",["Setting the weather","Writing company mottos","Choosing company colors"],"Governments license and regulate competition.")
H('241.d.5.C',3,"Courts that settle disputes between a business and a customer are part of the:",
  "legal system",["tax system","banking system","trade system"],"Courts resolve legal disputes.")
H('241.d.5.C',4,"A business signs a contract and the other party fails to pay. The business can seek relief through:",
  "the court system",["the weather service","a marketing plan","a trade show"],"Courts enforce contracts.")
H('241.d.5.D',3,"An organization of workers that bargains with employers about wages and conditions is a:",
  "labor union",["corporation","cooperative bank","trade tariff"],"Unions represent workers.")
H('241.d.5.D',4,"Collective bargaining is when:",
  "union representatives negotiate with an employer for all members",["one employee quits","a company sets prices","courts print money"],"Bargaining is group negotiation.")
H('241.d.6.A',3,"Marketing a service like car repair usually relies more on:",
  "reputation and trust",["packaging","shelf displays","coupons only"],"Services are intangible, so trust matters.")
H('241.d.6.A',4,"Which difference is most important when marketing goods versus services?",
  "Goods are tangible and can be displayed; services are intangible",["Goods cannot be priced","Services are always free","Goods have no customers"],"Tangibility changes marketing.")
H('241.d.6.B',3,"A company that takes raw materials like iron ore from the earth is a:",
  "raw-goods producer",["retailer","wholesaler","banker"],"Raw-goods producers extract resources.")
H('241.d.6.B',4,"A business that turns raw materials into finished goods is a:",
  "manufacturer",["retailer","consumer","lender"],"Manufacturers make products from inputs.")
H('241.d.6.C',3,"A supermarket, a department store, and a convenience store are types of:",
  "retailers",["wholesalers","manufacturers","producers"],"Retailers sell to the final consumer.")
H('241.d.6.C',4,"A business that sells only through a website is a:",
  "non-store retailer",["wholesaler","raw-goods producer","franchisor only"],"Online sellers are non-store retailers.")
H('241.d.6.D',3,"Retailers help the private enterprise system by:",
  "making goods available to consumers",["setting taxes","printing money","making laws"],"They link producers and consumers.")
H('241.d.6.D',4,"A retailer competes on price, selection, and service, which supports the principle of:",
  "competition",["monopoly","central planning","tradition"],"Competition benefits consumers.")
H('241.d.6.E',3,"A business that buys large quantities from manufacturers and sells to retailers is a:",
  "wholesaler",["consumer","producer","bank"],"Wholesalers sit between makers and stores.")
H('241.d.6.E',4,"A warehouse club selling bulk goods to store owners is an example of:",
  "a wholesaler",["a raw-goods producer","an extractive business","a government agency"],"Bulk sales to resellers are wholesale.")
H('241.d.6.F',3,"Wholesalers help the economy by:",
  "storing goods and delivering them to retailers",["printing currency","setting tariffs","making laws"],"They provide storage and distribution.")
H('241.d.6.F',4,"Without wholesalers, a small retailer might have to:",
  "buy from many individual manufacturers",["pay no taxes","avoid all customers","stop needing stock"],"Wholesalers simplify purchasing.")
H('241.d.7.A',3,"Producing more output with the same resources is an increase in:",
  "productivity",["inflation","debt","taxation"],"Productivity measures output per input.")
H('241.d.7.A',4,"A factory makes 600 widgets with 10 workers. Output per worker is:",
  "60",["6","600","10"],"600 / 10 = 60.")
H('241.d.7.B',3,"Each worker on an assembly line doing one task is called:",
  "division of labor",["barter","retailing","budgeting"],"Dividing tasks increases efficiency.")
H('241.d.7.B',4,"Specialization usually increases productivity because workers:",
  "become faster and more skilled at one task",["work fewer hours","stop learning","avoid teamwork"],"Practice builds skill.")
H('241.d.7.C',3,"A union that negotiates for better pay is an example of organized labor interacting with:",
  "business",["only schools","only banks","only farms"],"Unions bargain with employers.")
H('241.d.7.C',4,"A strike is:",
  "workers stopping work to press demands",["a tax payment","a merger","a loan"],"Strikes are collective work stoppages.")
H('241.d.8.A',3,"Paying for a purchase with plastic that draws money directly from your checking account is a:",
  "debit card",["credit card","check on credit","loan"],"Debit pulls from your own funds.")
H('241.d.8.A',4,"Using a credit card means you are:",
  "borrowing money to be repaid later",["spending your own cash","receiving a gift","earning interest"],"Credit is a loan.")
H('241.d.8.B',3,"Bills issued by a central bank, such as a $20 note, are:",
  "paper money",["coins","commodities","securities"],"Banknotes are paper currency.")
H('241.d.8.B',4,"Which is a type of currency?",
  "coins",["stocks","coupons","warranties"],"Coins are metal currency.")
H('241.d.8.C',3,"Using dollars to buy groceries shows money acting as a:",
  "medium of exchange",["store of debt","price ceiling","tax"],"Money lets us trade easily.")
H('241.d.8.C',4,"Saving money for a future purchase shows money acting as a:",
  "store of value",["unit of measure","tariff","unit of barter"],"Money holds value over time.")
H('241.d.8.D',3,"Credit allows a family to:",
  "buy now and pay later",["avoid all fees","earn interest on debt","ignore payments"],"Credit extends purchasing power.")
H('241.d.8.D',4,"A good credit history helps a person:",
  "qualify for loans at lower interest rates",["avoid paying taxes","skip payments","receive free items"],"Lenders reward reliability.")
H('241.d.8.E',3,"Writing a check when the account has insufficient funds can lead to:",
  "fees and legal trouble",["a refund","extra interest earned","a bonus"],"Bouncing checks has consequences.")
H('241.d.8.E',4,"A person who signs a credit agreement is legally responsible for:",
  "repaying the amount owed under the terms",["nothing","only the interest","only the first payment"],"Agreements are binding.")
H('241.d.9.A',3,"Providing accurate information on a loan application is important because false information can:",
  "result in legal penalties",["raise interest earned","remove debt","shorten the loan"],"Misrepresentation is illegal.")
H('241.d.9.A',4,"Why must an employee give correct Social Security information on tax forms?",
  "to ensure wages and taxes are recorded properly",["to get a discount","to avoid work","to lower the price of goods"],"Accurate records prevent errors.")
H('241.d.9.B',3,"An employee earns $800 and has $120 withheld. Net pay is:",
  "$680",["$920","$120","$800"],"800 - 120 = 680.")
H('241.d.9.B',4,"A worker earns $15 per hour for 40 hours. Gross pay is:",
  "$600",["$55","$400","$150"],"15 x 40 = 600.")
H('241.d.9.C',3,"A checking account is mainly used for:",
  "paying bills and daily purchases",["long-term growth only","buying stocks","paying taxes only"],"Checking supports frequent transactions.")
H('241.d.9.C',4,"A savings account usually pays more than a checking account because it:",
  "earns interest on stored funds",["has no balance","charges no fees ever","lets you overdraw"],"Savings accounts reward saving.")
H('241.d.9.D',3,"Reconciling a bank statement means:",
  "comparing your records to the bank's",["closing the account","paying taxes","opening a loan"],"Reconciliation finds errors.")
H('241.d.9.D',4,"Your records show $500 but the bank statement shows $450 because a $50 check has not cleared. After reconciling you find:",
  "the balances agree",["a bank error","fraud","a missing deposit"],"Outstanding checks explain the difference.")
H('241.d.9.E',3,"A bank that offers accounts only online usually has lower fees but no:",
  "physical branch",["interest","FDIC protection ever","accounts"],"Online banks lack branches.")
H('241.d.9.E',4,"Which is a disadvantage of online banking?",
  "difficulty depositing cash in person",["24-hour access","lower fees","easy transfers"],"Cash deposits can be harder.")
H('241.d.9.F',3,"Investing $1,000 at 5% simple interest for 2 years earns how much interest?",
  "$100",["$50","$1,050","$10"],"1000 x 0.05 x 2 = 100.")
H('241.d.9.F',4,"The earlier a person starts investing, the more their money can grow through:",
  "compounding",["inflation","withholding","depreciation"],"Interest earns interest over time.")
H('241.d.9.G',3,"The form most employees use to report yearly earnings and calculate tax owed is the:",
  "Form 1040",["W-4 only","bank statement","pay stub"],"Form 1040 is the individual income tax return.")
H('241.d.9.G',4,"An employer gives an employee a W-2 to show:",
  "wages earned and taxes withheld",["bank balances","stock prices","tariff rates"],"W-2 supports tax filing.")
H('241.d.10.A',3,"Creating, communicating, and delivering value to customers describes:",
  "marketing",["accounting","manufacturing only","banking"],"Marketing connects products and customers.")
H('241.d.10.A',4,"Which statement best defines marketing?",
  "The process of identifying and satisfying customer needs",["Setting tax rates","Making products only","Printing invoices"],"Marketing meets needs.")
H('241.d.10.B',3,"Marketing works with finance to decide:",
  "budgets for promotion",["employee holidays","tax law","court dates"],"Marketing needs funding.")
H('241.d.10.B',4,"Marketing depends on production to ensure that:",
  "products meet customer expectations",["taxes are paid","bills are filed","loans are closed"],"Quality affects sales.")
H('241.d.10.C',3,"The belief that a business succeeds by satisfying customer needs is the:",
  "marketing concept",["production concept only","barter idea","tax code"],"Customer focus is central.")
H('241.d.10.C',4,"A company that surveys customers before designing a product is following the:",
  "marketing concept",["sales quota","cost concept","budget concept"],"Research guides design.")
H('241.d.10.D',3,"Pricing, promotion, distribution, and market research are:",
  "marketing functions",["tax forms","bank accounts","union rules"],"These are key marketing activities.")
H('241.d.10.D',4,"Getting products from a factory to stores is the marketing function of:",
  "distribution",["promotion","pricing","selling"],"Distribution moves goods.")
H('241.d.11.A',3,"A market is a group of:",
  "people who want and can buy a product",["only sellers","only producers","only banks"],"Markets consist of buyers.")
H('241.d.11.A',4,"Market identification helps a business:",
  "find who is likely to buy its product",["set taxes","print money","hire staff"],"Knowing the market focuses effort.")
H('241.d.11.B',3,"Dividing buyers by age, income, or location creates:",
  "market segments",["tax brackets","supply chains","business cycles"],"Segments group similar buyers.")
H('241.d.11.B',4,"Which is a segment based on geography?",
  "customers in a particular city",["customers aged 20-30","customers with high income","customers who like sports"],"Location defines geographic segments.")
H('241.d.11.C',3,"Selling one product to everyone without tailoring is:",
  "mass marketing",["segmentation","niche marketing","direct sales"],"Mass marketing targets all.")
H('241.d.11.C',4,"Unlike mass marketing, segmentation:",
  "tailors the message to a specific group",["ignores customers","uses no research","sells to everyone"],"Segmentation focuses on a group.")
H('241.d.11.D',3,"The specific group of customers a business aims to serve is its:",
  "target market",["supply chain","tax base","labor pool"],"Target markets guide strategy.")
H('241.d.11.D',4,"Targeting helps a business because it:",
  "uses limited resources on likely buyers",["avoids profit","stops competition","removes risk entirely"],"Focus improves efficiency.")
H('241.d.11.E',3,"A company sells running shoes to teens who play sports. The target market is chosen using:",
  "market segmentation",["random guess","tax records","court rulings"],"Segmentation identifies the target.")
H('241.d.11.E',4,"A shop selling baby clothes would most likely target:",
  "new parents",["retired travelers","college athletes","office managers"],"The product fits their needs.")
H('241.d.12.A',3,"A plan that explains how a business will reach customers and meet goals is a:",
  "marketing strategy",["tax plan","budget cut","wage scale"],"Strategies guide marketing.")
H('241.d.12.A',4,"A good marketing strategy begins with:",
  "understanding customer needs",["raising prices","hiring more staff","buying equipment"],"Customer insight comes first.")
H('241.d.12.B',3,"Product, price, place, and promotion make up the:",
  "marketing mix",["balance sheet","supply chain","tax code"],"These are the four Ps.")
H('241.d.12.B',4,"In the marketing mix, 'place' refers to:",
  "where and how a product is distributed",["how much it costs","how it is advertised","what it looks like"],"Place concerns distribution.")
H('241.d.12.C',3,"A company offering a quality product at a fair price, available in many stores, and advertised widely has:",
  "an effective marketing mix",["no strategy","a weak mix","only a price"],"All four elements work together.")
H('241.d.12.C',4,"Which example shows a well-matched marketing mix?",
  "A premium watch sold in luxury stores with high-end advertising",["A luxury watch sold at a flea market","A low-cost item in luxury shops","A product with no advertising"],"Elements should fit the target market.")
H('241.d.12.D',3,"A student designs a lemonade stand plan with a flavor, a price, a location, and a sign. She is creating:",
  "a marketing mix",["a balance sheet","a union contract","a tax return"],"She has defined all four Ps.")
H('241.d.12.D',4,"When creating a marketing mix for a teen-focused app, the best promotion is likely:",
  "social media ads",["newspaper classified ads","radio for seniors","printed yellow pages"],"Teens use social media.")
H('241.d.12.E',3,"Customers who give reviews and share posts show the role of:",
  "participation in marketing",["taxation","price fixing","banking"],"Participation builds engagement.")
H('241.d.12.E',4,"A brand that asks customers to vote on new flavors uses participation to:",
  "involve customers in product decisions",["avoid advertising","raise taxes","reduce choices"],"Involvement builds loyalty.")
H('241.d.13.A',3,"Listing what you enjoy doing and what you value helps you analyze your:",
  "goals and interests",["tax rate","credit limit","bank fees"],"Self-analysis guides career choice.")
H('241.d.13.A',4,"A student who loves building things might explore careers in:",
  "construction or engineering",["only banking","only retail","only law"],"Interests suggest careers.")
H('241.d.13.B',3,"Strong communication and math skills are examples of:",
  "talents, abilities, and skills",["tax forms","stock prices","loans"],"Skills inform career fit.")
H('241.d.13.B',4,"Taking an interest or aptitude survey helps determine:",
  "your strengths for different careers",["your tax bracket","your credit score","your bank balance"],"Assessments reveal strengths.")
H('241.d.13.C',3,"A written outline of education, training, and goals for a job is a:",
  "career plan",["tax return","balance sheet","trade policy"],"Career plans map steps.")
H('241.d.13.C',4,"A good career plan includes:",
  "short-term and long-term goals with steps",["only a job title","no deadlines","only wishes"],"Plans need goals and steps.")

# ---------- 242 Business Information Management I ----------
H('242.d.1.A',3,"Writing a clear email to a coworker and speaking politely on the phone show:",
  "effective communication",["poor planning","time wasting","careless typing"],"Oral and written skills matter in business.")
H('242.d.1.A',4,"Which email subject line is clearest?",
  "Meeting moved to Tuesday at 2 p.m.",["Hi","Stuff","Urgent!!!"],"Specific subjects inform readers.")
H('242.d.1.B',3,"Working with classmates to finish a spreadsheet project requires:",
  "teamwork",["competition only","working alone","avoidance"],"Collaboration shares tasks.")
H('242.d.1.B',4,"A team member finishes early. The best collaborative action is to:",
  "offer to help others",["leave","wait idle","criticize"],"Teamwork supports shared goals.")
H('242.d.1.C',3,"Dressing neatly and arriving on time for an office internship shows:",
  "professionalism",["poor attitude","carelessness","laziness"],"Professional conduct fits the setting.")
H('242.d.1.C',4,"An employee is frustrated by a coworker. Professional behavior is to:",
  "address the issue calmly and privately",["gossip","shout","ignore work"],"Calm communication is professional.")
H('242.d.1.D',3,"Completing assigned work accurately without being reminded shows:",
  "a productive work ethic",["procrastination","avoidance","carelessness"],"Reliability is valued.")
H('242.d.1.D',4,"Which behavior best shows a positive work ethic?",
  "Finishing tasks fully and checking for errors",["Doing the minimum","Leaving early","Skipping steps"],"Quality effort shows ethic.")
H('242.d.1.E',3,"Using licensed software and protecting client data are ways to:",
  "comply with laws and regulations",["avoid rules","save money by copying","skip training"],"Compliance is required.")
H('242.d.1.E',4,"Copying a purchased program to share with friends violates:",
  "copyright law",["traffic law","tax law","safety law"],"Software is protected by copyright.")
H('242.d.1.F',3,"Making a to-do list ranked by deadline shows:",
  "time-management skills",["poor planning","avoidance","confusion"],"Prioritizing saves time.")
H('242.d.1.F',4,"With three assignments due on different days, you should first work on the one that is:",
  "due soonest and most important",["least important","due last","easiest only"],"Prioritize by urgency.")
H('242.d.2.A',3,"While keying data, your back should be straight, feet flat on the floor, and wrists:",
  "level and relaxed",["bent upward","resting on the edge","twisted"],"Correct posture prevents strain.")
H('242.d.2.A',4,"A screen positioned at eye level helps prevent:",
  "neck and eye strain",["file loss","virus attacks","paper jams"],"Ergonomics protects health.")
H('242.d.2.B',3,"To care for a keyboard, you should:",
  "keep food and drinks away from it",["pour water on it","pound the keys","leave it in the sun"],"Protect equipment from spills.")
H('242.d.2.B',4,"Before moving a computer, you should first:",
  "shut it down and unplug cables",["pull it by the cord","shake it","leave it running"],"Safe handling prevents damage.")
H('242.d.2.C',3,"In touch-system keyboarding, your fingers rest on the:",
  "home row",["number row","function row","bottom row"],"The home row is ASDF JKL;.")
H('242.d.2.C',4,"Which finger types the letter F?",
  "left index finger",["right index finger","left ring finger","left thumb"],"F is on the left home row, index finger.")
H('242.d.2.D',3,"When keying the number row, you should keep your fingers:",
  "reaching from the home row without looking",["lifting the whole hand","using one finger","staring at the keys"],"Touch reach keeps accuracy.")
H('242.d.2.D',4,"A good habit for numeric keyboarding is to:",
  "return fingers to home position after each reach",["use only one hand","hit keys hard","watch the keyboard"],"Home position increases speed.")
H('242.d.2.E',3,"The ten-key numeric keypad is used mostly for:",
  "entering numbers quickly",["writing essays","drawing","formatting letters"],"Ten-key speeds numeric entry.")
H('242.d.2.E',4,"On the ten-key, the middle finger usually rests on the number:",
  "5",["0","9","1"],"The 5 key is the home key.")
H('242.d.2.F',3,"The Ctrl + C and Ctrl + V shortcuts are used to:",
  "copy and paste",["save and exit","undo and redo","print and close"],"Copy and paste save time.")
H('242.d.2.F',4,"Pressing Ctrl + Z will:",
  "undo the last action",["save the file","print","close the program"],"Ctrl + Z reverses actions.")
H('242.d.3.A',3,"Keying more words per minute with fewer errors shows improvement in:",
  "speed and accuracy",["posture only","printing only","filing only"],"Both matter.")
H('242.d.3.A',4,"A student keys 40 words in 1 minute with 2 errors. Her net speed is:",
  "38 words per minute",["42 words per minute","40 words per minute","2 words per minute"],"40 - 2 = 38.")
H('242.d.3.B',3,"Reading your document carefully to find mistakes is:",
  "proofreading",["formatting","printing","sorting"],"Proofreading catches errors.")
H('242.d.3.B',4,"Which sentence has correct grammar?",
  "Their reports are due on Friday.",["There reports is due on Friday.","Their reports was due on Fridays.","Them reports are due Friday."],"Subject-verb agreement matters.")
H('242.d.3.C',3,"To erase a mistake just typed, you press the:",
  "backspace key",["tab key","caps lock","escape"],"Backspace deletes to the left.")
H('242.d.3.C',4,"Pressing Delete removes the character:",
  "to the right of the cursor",["to the left","above","none"],"Delete removes forward.")
H('242.d.3.D',3,"Writing a memo within a 10-minute time limit practices:",
  "composing under timed conditions",["printing slowly","copying","filing"],"Timed work builds speed.")
H('242.d.3.D',4,"A timed writing task is best approached by:",
  "planning briefly, then composing and proofreading",["writing nothing","skipping the plan","deleting often"],"Plan, draft, check.")
H('242.d.3.E',3,"Producing an accurate letter in less time shows:",
  "speed and accuracy in production",["laziness","errors","delays"],"Efficiency with accuracy is the goal.")
H('242.d.3.E',4,"Which practice improves production speed?",
  "using templates and keyboard shortcuts",["retyping everything","avoiding practice","ignoring errors"],"Tools save time.")
H('242.d.4.A',3,"Typing a report from a handwritten draft is working from:",
  "rough-draft copy",["spoken audio only","memory only","a calendar"],"Rough drafts are source copy.")
H('242.d.4.A',4,"When keying from statistical copy, you must be especially careful with:",
  "numbers and decimal points",["font color","page margins only","clip art"],"Data accuracy is critical.")
H('242.d.4.B',3,"Typing an original email directly from your own ideas is:",
  "composing at the keyboard",["copying text","scanning","printing"],"Composing creates new text.")
H('242.d.4.B',4,"Composing at the keyboard is easier when you:",
  "outline ideas first",["wait to proofread","avoid editing","type quickly without thought"],"Outlines organize thoughts.")
H('242.d.4.C',3,"Using spell check but also reading your work is important because spell check may miss:",
  "correctly spelled wrong words, such as 'their' and 'there'",["all spelling errors","bold text","page numbers"],"Spell check cannot judge meaning.")
H('242.d.4.C',4,"Which error would spell check likely NOT catch?",
  "Using 'form' instead of 'from'",["Misspelling 'recieve'","Misspelling 'adress'","Typing 'tehn'"],"Both are valid words.")
H('242.d.4.D',3,"The line that includes a name and address at the start of a business letter is the:",
  "inside address",["closing","signature","enclosure"],"The inside address names the recipient.")
H('242.d.4.D',4,"The section 'Sincerely,' followed by the writer's name is the:",
  "complimentary close and signature",["salutation","subject line","inside address"],"The close ends the letter.")
H('242.d.4.E',3,"In a standard business letter, the salutation is followed by a:",
  "colon in block style",["period","dash","semicolon"],"Business letters use a colon after the salutation.")
H('242.d.4.E',4,"On a business envelope, the return address goes in the:",
  "upper left corner",["lower right","center","back flap only"],"Return addresses go upper left.")
H('242.d.4.F',3,"A report's title page should include:",
  "title, author, and date",["only a picture","only page numbers","a bank statement"],"Title pages identify the report.")
H('242.d.4.F',4,"A reference page lists:",
  "sources used in the report",["page numbers","all typed errors","a table of fonts"],"References credit sources.")
H('242.d.4.G',3,"In an outline, main topics are usually labeled with:",
  "Roman numerals",["bullets only","stars","dashes"],"I, II, III are main points.")
H('242.d.4.G',4,"In a formal outline, subtopics under a Roman numeral heading are labeled with:",
  "capital letters",["Roman numerals","emoji","lowercase Roman numerals"],"A, B, C label subpoints.")
H('242.d.4.H',3,"A sentence that asks a question ends with a:",
  "question mark",["comma","colon","apostrophe"],"Questions end with a question mark.")
H('242.d.4.H',4,"Which sentence uses a comma correctly?",
  "After the meeting, we reviewed the budget.",["After the meeting we, reviewed the budget.","After, the meeting we reviewed the budget.","After the meeting we reviewed, the budget."],"Commas follow introductory phrases.")
H('242.d.5.A',3,"Reading all instructions before starting a document task helps you:",
  "produce the document correctly",["finish slower","ignore details","skip steps"],"Directions prevent errors.")
H('242.d.5.A',4,"If a supervisor asks for a letter in block style on letterhead, you should:",
  "follow those directions exactly",["use any style","skip the letterhead","guess"],"Follow instructions precisely.")
H('242.d.5.B',3,"Choosing 'accept' instead of 'except' correctly shows skill in:",
  "business English and spelling",["printing","filing","scanning"],"Word choice matters.")
H('242.d.5.B',4,"Which sentence is written in clear business English?",
  "Please send the invoice by Friday.",["send me the thing 2 days","Hey dude gimme invoice","yo need that stuff"],"Business writing is clear and polite.")
H('242.d.5.C',3,"Memos usually include which header lines?",
  "To, From, Date, Subject",["Dear, Sincerely","Name, Age","Title, Chapter"],"Memo headings organize information.")
H('242.d.5.C',4,"Which document is best for a short internal announcement to staff?",
  "memo",["formal contract","invoice","tax return"],"Memos are for internal messages.")
H('242.d.5.D',3,"Opening a template, entering text, and saving the file are:",
  "steps in producing a document",["errors","delays","extras"],"Steps ensure a complete product.")
H('242.d.5.D',4,"The best order for creating a document is:",
  "plan, create, proofread, save, and print or send",["print, save, create","send, plan, save","proofread, delete, plan"],"A logical process prevents errors.")
H('242.d.6.A',3,"Arranging your desk, backing up files, and following a routine are ways to:",
  "refine work habits",["waste time","avoid work","create errors"],"Good habits increase efficiency.")
H('242.d.6.A',4,"A good work habit for a data-entry clerk is to:",
  "double-check entries before submitting",["rush","skip review","ignore mistakes"],"Verification prevents errors.")
H('242.d.6.B',3,"Practicing timed tests regularly helps improve:",
  "techniques, speed, and accuracy",["clutter","delays","mistakes"],"Practice builds skill.")
H('242.d.6.B',4,"To raise accuracy, a keyboarder should first:",
  "slow down slightly and focus on correct keystrokes",["type faster only","ignore errors","stop proofreading"],"Accuracy before speed.")
H('242.d.7.A',3,"When choosing word-processing software, a key criterion is whether it can:",
  "create and format the documents you need",["only play music","only browse","only email"],"Software must meet needs.")
H('242.d.7.A',4,"Which feature would you check when evaluating word-processing software?",
  "spell check, templates, and collaboration tools",["video games","music library","weather widget"],"Features affect productivity.")
H('242.d.7.B',3,"Deciding which document to finish first based on deadlines is analyzing:",
  "priority of completion",["font style","color choice","paper type"],"Prioritization manages workload.")
H('242.d.7.B',4,"A memo is due in an hour; a report is due tomorrow. You should usually complete the:",
  "memo first",["report first","neither","report only"],"Earlier deadline takes priority.")
H('242.d.7.C',3,"A short, informal message to staff about a schedule change is a:",
  "memo",["tax form","contract","press release"],"Memos communicate within a business.")
H('242.d.7.C',4,"A document sent to the media to announce company news is a:",
  "press release",["memo","invoice","order form"],"Press releases go to media.")
H('242.d.7.D',3,"Sending the same letter to many customers with each name filled in uses:",
  "mail merge",["copy paste only","manual retyping","a calculator"],"Mail merge personalizes bulk letters.")
H('242.d.7.D',4,"To use mail merge, you need a main document and a:",
  "data source",["printer only","scanner","calendar"],"The data source holds names and addresses.")
H('242.d.8.A',3,"Combining slides with text, graphics, and a spoken explanation is a:",
  "visual and oral report",["bank statement","tax form","budget"],"Presentations mix media.")
H('242.d.8.A',4,"A good slide contains:",
  "brief text and a relevant graphic",["paragraphs of text","tiny fonts","no content"],"Slides should be simple.")
H('242.d.8.B',3,"Keeping others' personal information confidential relates to the social impact of computers on:",
  "privacy",["font size","printing speed","screen color"],"Privacy is a social concern.")
H('242.d.8.B',4,"Sharing a classmate's password is a violation of:",
  "privacy and security",["font rules","printer rules","margin rules"],"Passwords protect accounts.")
H('242.d.8.C',3,"Printing only what you need and saving files electronically show:",
  "responsible use of computer systems",["waste","carelessness","poor planning"],"Responsible use conserves resources.")
H('242.d.8.C',4,"Responsible computer use includes:",
  "logging out and protecting data",["leaving screens open","sharing passwords","downloading anything"],"Security is part of responsibility.")
H('242.d.8.D',3,"Listening to coworkers' ideas and treating them respectfully builds:",
  "human-relation skills",["conflicts","delays","errors"],"Respect strengthens teams.")
H('242.d.8.D',4,"A teammate disagrees with your idea. A good human-relations response is to:",
  "listen and discuss the pros and cons",["argue","ignore them","leave"],"Respectful discussion helps.")
H('242.d.8.E',3,"Joining a student business organization and running for an office are examples of:",
  "student leadership activities",["errors","delays","penalties"],"Leadership builds skills.")
H('242.d.8.E',4,"Participating in a business competition helps students develop:",
  "leadership and workplace skills",["only trophies","bad habits","no skills"],"Competitions build skills.")

# ---------- 243 Business Law ----------
H('243.d.1.A',3,"A business owner who knowingly sells a defective product while claiming it is perfect is acting:",
  "unethically",["ethically","legally always","wisely"],"Deception is unethical.")
H('243.d.1.A',4,"Which action is an ethical business practice?",
  "Disclosing known safety risks to customers",["Hiding product defects","Fixing prices secretly","Copying a trademark"],"Disclosure is ethical.")
H('243.d.1.B',3,"A decision can be legal but not ethical. Which fits that?",
  "Legally laying off workers without warning and without help",["Breaking a contract","Stealing","Falsifying records"],"Legal but harmful choices raise ethical questions.")
H('243.d.1.B',4,"A decision based on personal beliefs about right and wrong is a:",
  "moral choice",["legal choice","tax choice","market choice"],"Morals come from personal values.")
H('243.d.2.A',3,"A lawsuit between a customer and a store over payment is a:",
  "civil case",["criminal case","military case","traffic ticket"],"Civil law handles private disputes.")
H('243.d.2.A',4,"Which is a criminal matter?",
  "Embezzling funds from an employer",["A dispute over a late payment","A rent disagreement","A contract negotiation"],"Crimes violate public law.")
H('243.d.2.B',3,"A court that hears cases first and decides the facts is a:",
  "trial court",["appellate court only","legislature","agency"],"Trial courts hear evidence.")
H('243.d.2.B',4,"A court that reviews whether a lower court made legal mistakes is an:",
  "appellate court",["trial court","small claims court","grand jury"],"Appeals check errors of law.")
H('243.d.2.C',3,"A civil wrong that causes harm, such as negligence, is a:",
  "tort",["felony","contract","tariff"],"Torts are civil wrongs.")
H('243.d.2.C',4,"Fraud punished by the state as a violation of criminal law is a:",
  "business crime",["tort only","contract","warranty"],"Crimes are prosecuted by the government.")
H('243.d.2.D',3,"Governments regulate businesses mainly to:",
  "protect consumers, workers, and competition",["lower all prices","stop profit","close companies"],"Regulation protects the public.")
H('243.d.2.D',4,"A law requiring safety labels on products exists to:",
  "protect consumers from harm",["raise prices","slow business","limit choice"],"Labels inform users.")
H('243.d.3.A',3,"A contract that is written down is:",
  "an express written contract",["an implied contract","a verbal rumor","a void promise"],"Written contracts are express.")
H('243.d.3.A',4,"A contract formed by actions, like getting a haircut without a written deal, is:",
  "implied",["express","void","illegal"],"Conduct can create contracts.")
H('243.d.3.B',3,"A contract begins when one party makes an offer and the other gives:",
  "acceptance",["a refusal","a counteroffer","a gift"],"Offer plus acceptance forms agreement.")
H('243.d.3.B',4,"If a buyer changes the terms when responding to an offer, this is a:",
  "counteroffer",["acceptance","revocation","consideration"],"A change rejects the original offer.")
H('243.d.3.C',3,"A person who is a minor generally has limited capacity to:",
  "enter binding contracts",["go to school","vote","work at all"],"Minors can usually void contracts.")
H('243.d.3.C',4,"A contract with someone who is legally incompetent is usually:",
  "voidable",["enforceable","automatically valid","a gift"],"Capacity is needed.")
H('243.d.3.D',3,"In a contract, each party gives something of value. This is:",
  "consideration",["capacity","fraud","tort"],"Consideration is the exchange.")
H('243.d.3.D',4,"A promise to give a free gift without anything in return generally lacks:",
  "consideration",["capacity","offer","acceptance"],"Gifts lack an exchange.")
H('243.d.3.E',3,"A contract made because one party lied about an important fact may be a:",
  "defective agreement",["valid agreement","gift","lease"],"Fraud makes agreements defective.")
H('243.d.3.E',4,"Agreement signed under threat is called:",
  "duress",["consideration","acceptance","warranty"],"Duress voids consent.")
H('243.d.3.F',3,"A contract to commit a crime is:",
  "illegal and unenforceable",["valid","a bailment","negotiable"],"Illegal contracts are void.")
H('243.d.3.F',4,"Agreements in restraint of trade, such as price fixing, are:",
  "illegal agreements",["legal sales","valid contracts","warranties"],"They harm competition.")
H('243.d.3.G',3,"To research recent contract cases, a student can use:",
  "online legal databases and court websites",["gossip","guesses","rumors"],"Reliable sources provide cases.")
H('243.d.3.G',4,"Which source is best for finding a court's decision about a contract?",
  "the court's official website or a legal database",["a social media post","a friend","an ad"],"Official sources are reliable.")
H('243.d.4.A',3,"Land and buildings are:",
  "real property",["personal property","bailments","securities"],"Real property includes land and attachments.")
H('243.d.4.A',4,"A laptop and a car are:",
  "personal property",["real property","fixtures","land"],"Movable items are personal property.")
H('243.d.4.B',3,"Tangible personal property is items you can touch, such as furniture, while intangible property includes:",
  "stocks and copyrights",["land","buildings","trees"],"Intangibles lack physical form.")
H('243.d.4.B',4,"A patent is an example of:",
  "intangible personal property",["real property","a bailment","a lease"],"Patents are intellectual property.")
H('243.d.4.C',3,"Leaving your car with a mechanic for repair creates a:",
  "bailment",["sale","mortgage","gift"],"A bailment is temporary possession.")
H('243.d.4.C',4,"In a bailment, the person who takes the property must:",
  "take reasonable care of it",["sell it","keep it forever","ignore it"],"Bailees owe care.")
H('243.d.4.D',3,"To research cases about personal property, you can use:",
  "online legal resources",["guesswork","rumors","ads"],"Online databases provide cases.")
H('243.d.4.D',4,"A student researching a lost-luggage case should look at:",
  "published court opinions",["opinions from friends","memes","coupons"],"Court opinions are authoritative.")
H('243.d.5.A',3,"Items sold in a store such as shoes and computers are:",
  "goods",["services only","real property","intangibles"],"Goods are tangible products.")
H('243.d.5.A',4,"Under sales law, a sale of goods is the transfer of title to goods for:",
  "a price",["free","a favor","no reason"],"A sale requires price.")
H('243.d.5.B',3,"Certain sales contracts must be in writing under the:",
  "statute of frauds",["tort law","tax law","bailment rule"],"Large sales often need writing.")
H('243.d.5.B',4,"A sale of goods above a certain dollar amount generally must be:",
  "in a signed writing",["oral only","hidden","verbal"],"The statute of frauds applies.")
H('243.d.5.C',3,"Ownership of goods moving from seller to buyer is a:",
  "transfer of title",["warranty","lien","tort"],"Title is legal ownership.")
H('243.d.5.C',4,"Risk of loss shifts to the buyer when:",
  "title or delivery terms say so",["the seller sleeps","prices change","the weather changes"],"Contract terms decide risk.")
H('243.d.5.D',3,"A seller's promise that a product will work as stated is a:",
  "warranty",["tariff","lien","deposit"],"Warranties guarantee quality.")
H('243.d.5.D',4,"Which warranty is automatically implied that goods are fit for ordinary use?",
  "implied warranty of merchantability",["express warranty","lifetime warranty","service warranty"],"Merchantability is implied by law.")
H('243.d.5.E',3,"A student researching a sale-of-goods dispute can find cases on:",
  "online legal research sites",["social posts","rumors","ads"],"Online sources provide cases.")
H('243.d.5.E',4,"When citing a sales case, a student should include:",
  "the case name, court, and year",["only a nickname","a photo","a rumor"],"Citations make sources clear.")
H('243.d.6.A',3,"A check, a note, or a draft that can be transferred to another person is a:",
  "negotiable instrument",["warranty","deed","tort"],"Negotiable instruments are transferable.")
H('243.d.6.A',4,"Negotiable instruments are used as a substitute for:",
  "money",["land","stock","goods"],"They stand in for cash.")
H('243.d.6.B',3,"To be negotiable, an instrument must be in writing, signed, and contain an unconditional promise to:",
  "pay a fixed amount of money",["perform a service","deliver goods","sell land"],"Negotiability requires fixed amount.")
H('243.d.6.B',4,"An instrument payable 'to bearer' or 'to order' meets the requirement of:",
  "payable to order or bearer",["a warranty","a deed","a lien"],"Words of negotiability are needed.")
H('243.d.6.C',3,"A written promise by one person to pay another a sum of money is a:",
  "promissory note",["draft","check","warranty"],"A note is a two-party promise.")
H('243.d.6.C',4,"An order by one person telling another to pay a third party is a:",
  "draft",["note","deed","lease"],"Drafts are orders to pay.")
H('243.d.6.D',3,"Transferring a negotiable instrument by signing it over is:",
  "negotiation",["discharge","default","fraud"],"Negotiation transfers rights.")
H('243.d.6.D',4,"When a debt on an instrument is paid and liability ends, this is:",
  "discharge",["negotiation","endorsement","transfer"],"Discharge cancels liability.")
H('243.d.6.E',3,"A person who takes an instrument in good faith and for value is a:",
  "holder in due course",["debtor","cosigner only","drawee"],"HDCs have special protections.")
H('243.d.6.E',4,"A holder in due course generally takes the instrument:",
  "free of most defenses",["subject to all defenses","with no rights","without value"],"HDCs are protected.")
H('243.d.6.F',3,"Forgery and fraud are examples of:",
  "defenses against payment",["warranties","deeds","leases"],"Defenses may block collection.")
H('243.d.6.F',4,"A real defense that works even against a holder in due course is:",
  "forgery",["minor mistake","late fee","slow delivery"],"Real defenses are strong.")
H('243.d.6.G',3,"To research negotiable instrument cases, a student can use:",
  "online legal databases",["opinions","ads","rumors"],"Cases are in databases.")
H('243.d.6.G',4,"A good source for case law on checks is:",
  "official court decisions",["social media","tabloids","coupons"],"Official sources are reliable.")
H('243.d.7.A',3,"A person who is authorized to act for another is an:",
  "agent",["principal","competitor","tenant"],"Agents act on behalf of principals.")
H('243.d.7.A',4,"An agency is usually created by:",
  "agreement between principal and agent",["accident","taxation","inheritance only"],"Agreement forms agency.")
H('243.d.7.B',3,"An agency ends when the agent's task is complete or when:",
  "the principal revokes authority",["it rains","a holiday arrives","the agent sleeps"],"Principals can terminate.")
H('243.d.7.B',4,"An agent who exceeds authority may be:",
  "personally liable",["rewarded","immune","paid extra"],"Acting beyond authority has consequences.")
H('243.d.7.C',3,"The relationship in which one person hires another to work for pay is:",
  "employer-employee",["landlord-tenant","buyer-seller","bailor-bailee"],"Employment is a work relationship.")
H('243.d.7.C',4,"An employer controls how, when, and where the work is done for an:",
  "employee",["independent contractor","partner","shareholder"],"Control signals employment.")
H('243.d.7.D',3,"Laws that protect workers from discrimination and unsafe conditions give employees:",
  "rights",["fees","taxes","liens"],"Employee rights are protected.")
H('243.d.7.D',4,"An employee's right to a safe workplace is protected by:",
  "OSHA",["FDIC","SEC","FTC"],"OSHA sets safety standards.")
H('243.d.7.E',3,"Minimum wage and overtime rules come from:",
  "labor legislation",["bailment law","contract warranty","trust law"],"Labor laws govern wages.")
H('243.d.7.E',4,"The Fair Labor Standards Act sets rules about:",
  "minimum wage and overtime",["land transfers","insurance claims","stock sales"],"FLSA covers wages and hours.")
H('243.d.7.F',3,"To research employment law cases, students can use:",
  "online legal resources",["rumors","memes","ads"],"Databases contain cases.")
H('243.d.7.F',4,"When comparing two employment cases, a student should note:",
  "the facts and the court's ruling",["only the date","the clerk's name","the room"],"Facts and rulings matter.")
H('243.d.8.A',3,"A business owned and run by one person with unlimited personal liability is a:",
  "sole proprietorship",["partnership","corporation","trust"],"One owner, unlimited liability.")
H('243.d.8.A',4,"One advantage of a sole proprietorship is:",
  "easy to start and full control",["limited liability","shared profits","stock sales"],"Simplicity and control.")
H('243.d.8.B',3,"Two or more people who agree to carry on a business together form a:",
  "partnership",["corporation","trust","franchise"],"Partnerships share ownership.")
H('243.d.8.B',4,"A written agreement among partners is called a:",
  "partnership agreement",["warranty","bailment","draft"],"It sets roles and shares.")
H('243.d.8.C',3,"A business that is a separate legal entity from its owners is a:",
  "corporation",["sole proprietorship","partnership","bailment"],"Corporations are separate.")
H('243.d.8.C',4,"A corporation is formed by filing:",
  "articles of incorporation",["a lease","a will","a draft"],"Articles create the corporation.")
H('243.d.8.D',3,"Owners of a corporation hold:",
  "shares of stock",["leases","drafts","warranties"],"Stock represents ownership.")
H('243.d.8.D',4,"Shareholders' liability for corporate debts is generally:",
  "limited to their investment",["unlimited","none","double"],"Limited liability protects owners.")
H('243.d.8.E',3,"A board of directors helps:",
  "manage the corporation",["print money","set taxes","write laws"],"Boards oversee management.")
H('243.d.8.E',4,"When a corporation ends and its assets are sold to pay debts, this is:",
  "dissolution",["formation","merger","incorporation"],"Dissolution winds up a corporation.")
H('243.d.9.A',3,"Insurance works by spreading:",
  "risk among many policyholders",["profits","taxes","debts to one person"],"Pooling risk is the principle.")
H('243.d.9.A',4,"The amount paid regularly for an insurance policy is the:",
  "premium",["deductible","claim","benefit"],"Premiums buy coverage.")
H('243.d.9.B',3,"Insurance that covers damage to your home is:",
  "property insurance",["life insurance","health insurance","auto insurance"],"Property policies cover buildings.")
H('243.d.9.B',4,"Life insurance pays a benefit when the insured:",
  "dies",["moves","changes jobs","sells a car"],"Life policies pay on death.")
H('243.d.9.C',3,"A bond that protects an employer from employee theft is a:",
  "fidelity bond",["mortgage","deed","draft"],"Fidelity bonds cover dishonesty.")
H('243.d.9.C',4,"Stocks and bonds are examples of:",
  "securities",["warranties","bailments","torts"],"Securities are investments.")
H('243.d.9.D',3,"A legal process for people or businesses who cannot pay debts is:",
  "bankruptcy",["incorporation","bailment","sale"],"Bankruptcy resolves debts.")
H('243.d.9.D',4,"Chapter 7 bankruptcy typically involves:",
  "selling assets to pay debts",["a payment plan only","no court","creating a trust"],"Liquidation is Chapter 7.")
H('243.d.9.E',3,"To find recent cases about insurance disputes, students can use:",
  "online legal sources",["rumors","ads","gossip"],"Online sources hold cases.")
H('243.d.9.E',4,"A case study on an insurance claim denial should examine:",
  "the policy terms and the court's reasoning",["the weather","the lawyers' cars","the clerk's lunch"],"Policy terms decide disputes.")
H('243.d.10.A',3,"Land, buildings, and things permanently attached to land are:",
  "real property",["personal property","bailments","drafts"],"Real property includes land and fixtures.")
H('243.d.10.A',4,"Rights to the minerals under land are part of:",
  "real property",["personal property","a bailment","a warranty"],"Mineral rights are real property.")
H('243.d.10.B',3,"The legal document used to transfer ownership of real property is a:",
  "deed",["will","draft","note"],"Deeds transfer title to land.")
H('243.d.10.B',4,"To make a real estate transfer public record, a deed is usually:",
  "recorded with the county",["burned","hidden","mailed to a friend"],"Recording gives notice.")
H('243.d.10.C',3,"A loan secured by real estate is a:",
  "mortgage",["draft","lease","bailment"],"Mortgages are secured by property.")
H('243.d.10.C',4,"A mortgage with an interest rate that stays the same for life is a:",
  "fixed-rate mortgage",["adjustable mortgage","balloon lease","variable warranty"],"Fixed rates do not change.")
H('243.d.10.D',3,"The agreement allowing a tenant to use property for rent is a:",
  "lease",["deed","will","warranty"],"Leases govern tenancy.")
H('243.d.10.D',4,"A landlord must generally keep a rental home:",
  "habitable and safe",["rent-free","empty","locked from tenants"],"Landlords owe habitability.")
H('243.d.10.E',3,"A legal document that states how a person's property is distributed after death is a:",
  "will",["deed","lease","draft"],"Wills direct inheritance.")
H('243.d.10.E',4,"A trust is an arrangement in which a trustee:",
  "manages property for beneficiaries",["destroys property","buys insurance","signs a lease"],"Trustees manage assets.")
H('243.d.10.F',3,"To research real estate cases, a student can use:",
  "online legal databases",["ads","rumors","memes"],"Cases appear online.")
H('243.d.10.F',4,"A case about an eviction would be most relevant to:",
  "landlord-tenant law",["patent law","insurance law","tax law"],"Eviction involves leases.")
H('243.d.11.A',3,"Greeting clients politely and listening during a legal office visit show:",
  "effective interpersonal skills",["poor manners","rudeness","distraction"],"Interpersonal skills matter.")
H('243.d.11.A',4,"During a role-play with an upset client, the best response is to:",
  "listen and acknowledge concerns",["interrupt","laugh","walk away"],"Empathy resolves conflict.")
H('243.d.11.B',3,"Working together on a mock trial team practices:",
  "team-building skills",["competition only","isolation","avoidance"],"Teamwork builds results.")
H('243.d.11.B',4,"A mock trial team shares tasks by:",
  "assigning roles based on strengths",["one person doing all","skipping practice","ignoring rules"],"Roles improve efficiency.")
H('243.d.11.C',3,"Joining a career and technical student organization helps students develop:",
  "leadership and career skills",["bad habits","fees","nothing"],"CTSOs build leaders.")
H('243.d.11.C',4,"Attending a career-development conference helps students:",
  "network and learn about careers",["avoid learning","skip class","lose skills"],"Conferences offer exposure.")

H('241.d.3.A',5,"A nation where prices and output are mostly set by buyers and sellers, with some government regulation, has what type of economy?",
  "mixed economy",["pure command economy","pure traditional economy","barter-only economy"],"Mixed economies blend markets and government roles.")
H('241.d.9.D',5,"A customer's deposit of $200 appears in her records but not yet on the bank statement. What is the best reconciliation step?",
  "Add it to the statement balance as a deposit in transit",["Subtract it from her records","Ignore it","Close the account"],"Deposits in transit are added to the bank balance.")
H('243.d.1.A',5,"A company advertises a recalled toy as safe after learning of choking hazards. This conduct is best described as:",
  "unethical and potentially illegal",["ethical marketing","acceptable puffery","routine promotion"],"Concealing hazards violates ethics and consumer law.")
H('243.d.7.E',5,"A law that bars employers from retaliating against workers who report unsafe conditions is an example of:",
  "labor legislation protecting employees",["a tax rule","a real estate statute","a trust provision"],"Whistleblower protections are labor law.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_40.jsonl'))

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('113.31.d.', 1009, own='hs_econfe.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('1.A ',2,"A town has $2 million to spend and requests totaling $5 million. Which concept does this situation illustrate?",
  "Scarcity forces choices",["Unlimited resources","Zero opportunity cost","Perfect competition"],"Wants exceed resources, so every society must choose.")
H('1.A ',2,"Why is scarcity faced by every society, rich or poor?",
  "Resources are limited while wants are unlimited",["Money is illegal","Wants are limited","Goods are free"],"Limited resources and unlimited wants create scarcity.")
H('1.B',2,"Which question is one of the three basic economic questions every society answers?",
  "What goods and services to produce",["Which team will win","Which movie is best","What time school starts"],"Societies decide what, how and for whom to produce.")
H('1.B',3,"In a command economy, who mainly answers \"what to produce\"?",
  "The central government",["Individual consumers","Competing firms","Foreign banks"],"Central planners make the decisions.")
H('1.C',2,"A bakery's ovens and mixers are an example of which factor of production?",
  "Capital",["Land","Labor","Entrepreneurship"],"Capital is human-made goods used to produce other goods.")
H('1.C',2,"A person who starts a new company and takes on its risk is providing which factor of production?",
  "Entrepreneurship",["Land","Capital","Labor only"],"Entrepreneurs organize resources and take risks.")
H('1.D',3,"On a production-possibilities curve, a point inside the curve shows that the economy is doing what?",
  "Using resources inefficiently or leaving some unused",["Producing at maximum capacity","Producing impossible output","Operating with no scarcity"],"Points inside the curve are attainable but inefficient.")
H('1.D',3,"Moving along a production-possibilities curve to produce more of one good means producing less of another. This trade-off is called what?",
  "Opportunity cost",["Inflation","A subsidy","Comparative advantage"],"The cost is the next best alternative given up.")
H('3.A',3,"Producer A gives up 0.5 radio for each shirt it makes. Producer B gives up 1 radio for each shirt. Which has the comparative advantage in shirts?",
  "The producer with the lower opportunity cost",["The producer with the higher opportunity cost","Neither can trade","Both are identical"],"Comparative advantage goes to the lower opportunity cost, which is Producer A.")
H('3.A',3,"A country has an absolute advantage in a good when it can do what?",
  "Produce it using fewer resources than another country",["Produce it at a lower opportunity cost","Ban its import","Price it at zero"],"Absolute advantage compares resource use.")
H('3.B ',3,"A tariff on imported steel is most likely to do what?",
  "Raise the price of imported steel for domestic buyers",["Lower the price of imports","Increase imports","Eliminate scarcity"],"Tariffs are taxes on imports.")
H('3.B ',3,"Which is a benefit of free trade?",
  "Consumers gain access to a greater variety of goods at lower prices",["Higher prices for all","Fewer choices","No job changes at all"],"Trade expands choices.")
H('3.C',3,"If the U.S. dollar becomes stronger against the euro, U.S. exports to Europe are likely to do what?",
  "Become more expensive for Europeans and fall",["Become cheaper and rise","Stay the same","Disappear entirely"],"A stronger dollar raises foreign prices.")
H('3.C',3,"A weaker dollar tends to cause what to happen to imports?",
  "They become more expensive for Americans",["They become cheaper","They are banned","They stay fixed"],"Imports cost more dollars.")
H('4.A',2,"Which feature is a basic characteristic of the free enterprise system?",
  "Private property rights and the profit incentive",["Government sets all prices","No competition","No ownership"],"Free enterprise relies on private ownership and incentives.")
H('4.A',2,"In an economic system, an incentive is what?",
  "A reward or penalty that influences behavior",["A tax form","A bank","A tariff"],"Incentives drive choices.")
H('4.B',3,"Which economy is best described by central planning and government ownership of nearly all property?",
  "Communism",["Free enterprise","Mixed market","Pure competition"],"Communism features state ownership.")
H('4.B',3,"A system with private business and extensive government social programs is best described as what?",
  "Mixed economy",["Pure command","Barter","Pure market"],"Most economies blend market and government roles.")
H('4.C',3,"Which economist is known for promoting free markets and limited government in works such as \"Capitalism and Freedom\"?",
  "Milton Friedman",["Karl Marx","Vladimir Lenin","Mao Zedong"],"Friedman championed free-market ideas.")
H('4.C',3,"Adam Smith's \"invisible hand\" idea suggests that what happens?",
  "Self-interested actions in markets can benefit society",["Government sets prices","Markets never work","Trade harms nations"],"Smith argued markets guide resources.")
H('5.A',2,"Which is a benefit of the U.S. free enterprise system?",
  "Freedom of consumer choice and the opportunity to start a business",["Fixed jobs for all","No competition","Guaranteed profits"],"Choice and opportunity are hallmarks.")
H('5.A',2,"Competition among sellers typically benefits consumers by doing what?",
  "Encouraging lower prices and better quality",["Raising prices","Reducing choices","Eliminating products"],"Rivals compete for customers.")
H('5.B',3,"Which change shows a shift in the role of government in the U.S. economy since 1900?",
  "Growth of regulation and social programs",["Elimination of taxes","Ending private property","A ban on business"],"Government's role has expanded.")
H('5.B',3,"The Sherman Antitrust Act of 1890 was intended to do what?",
  "Prevent monopolies that restrain trade",["Create the income tax","Set minimum wages","Raise tariffs"],"It targets anticompetitive behavior.")
H('6.A',2,"Before buying a $20,000 used truck, a buyer compares insurance, repairs and resale value. This is an example of weighing what?",
  "Costs and benefits of property use",["Barter","Tariffs","Subsidies"],"Cost-benefit analysis guides decisions.")
H('6.A',2,"A business must dispose of old equipment. Which cost should it consider?",
  "Disposal fees or environmental cleanup costs",["Only the original price","No costs exist","Only taxes"],"Disposal can carry costs.")
H('6.B',3,"Zoning laws that limit a factory near homes are an example of what?",
  "Government restrictions on the use of business property",["A subsidy","A barter","A tariff"],"Government can limit property use.")
H('6.B',3,"Eminent domain allows the government to do what?",
  "Take private property for public use with fair payment",["Take property without payment","Ban ownership","Set all prices"],"The Fifth Amendment requires just compensation.")
H('7.A',3,"In the circular-flow model, households provide what to firms in the factor market?",
  "Land, labor and capital in exchange for income",["Goods for free","Taxes only","Loans only"],"Households own resources.")
H('7.A',3,"In the product market of the circular-flow model, firms provide what?",
  "Goods and services in exchange for consumer spending",["Labor","Land","Wages"],"Firms sell output to households.")
H('7.B',3,"When the government collects taxes and buys goods, how does it affect the circular-flow model?",
  "It adds a flow of money and resources into and out of the system",["It stops the flow","It has no effect","It ends firms"],"Government participates in both markets.")
H('7.B',3,"Increased government spending in the circular-flow model generally does what to demand for firms' products?",
  "Increases it",["Eliminates it","Has no effect","Lowers it to zero"],"More spending raises demand.")
H('8.A',3,"A market with many small sellers offering nearly identical products, such as a wheat farm market, is called what?",
  "Pure competition",["Monopoly","Oligopoly","Command economy"],"Many sellers, identical goods.")
H('8.A',3,"A market with only a few large firms, such as U.S. wireless carriers, is an example of what?",
  "Oligopoly",["Pure competition","Barter","Monopolistic competition"],"A few dominant sellers.")
H('8.B',3,"The Federal Trade Commission regulates market structures mainly by doing what?",
  "Enforcing rules against unfair competition and deceptive practices",["Setting every price","Owning companies","Printing money"],"The FTC promotes fair competition.")
H('8.B',3,"Antitrust law applies most directly to which market structure?",
  "Monopoly",["Pure competition","Barter","Household"],"Antitrust curbs monopoly power.")
H('9.A',2,"The unemployment rate measures what?",
  "The percentage of the labor force that is jobless and looking for work",["The prices of goods","Total output","Interest rates"],"It excludes those not seeking work.")
H('9.A',3,"Gross domestic product (GDP) measures what?",
  "The market value of all final goods and services produced in a country in a year",["Total government debt","Total imports","The money supply"],"GDP is a measure of output.")
H('9.B',3,"During a recession, which indicator typically falls?",
  "Real GDP",["The unemployment rate","Bankruptcies","Layoffs"],"Output declines.")
H('9.B',3,"A business cycle expansion is typically marked by what?",
  "Rising output and falling unemployment",["Falling output","Rising joblessness","Closing factories"],"Expansion is a growth phase.")
H('10.A',3,"Which change increases productivity?",
  "Workers produce more output per hour",["Workers produce less per hour","Output stays constant","Wages fall"],"Productivity is output per input.")
H('10.A',3,"Higher productivity usually leads to what?",
  "Economic growth",["Recession","Scarcity ending","Inflation only"],"Producing more per input grows the economy.")
H('10.B',3,"New technology such as automated assembly lines contributes to economic growth by doing what?",
  "Raising output with the same resources",["Reducing output","Ending trade","Banning work"],"Technology improves efficiency.")
H('10.B',3,"The invention of the Internet affected growth by doing what?",
  "Creating new industries and boosting efficiency",["Ending business","Raising scarcity","Stopping trade"],"Technology spurs growth.")
H('10.C',3,"International trade contributes to growth by doing what?",
  "Expanding markets and allowing specialization",["Ending exports","Reducing choices","Banning imports"],"Trade widens markets.")
H('10.C',3,"A nation that specializes and trades is likely to experience what?",
  "A larger overall output of goods and services",["Shrinking output","Zero growth","Higher scarcity"],"Specialization increases efficiency.")
H('11.A',2,"Money serving as a way to compare the value of a pizza and a bicycle is acting as what?",
  "A unit of account",["A store of value only","A barter good","A loan"],"Money measures value.")
H('11.A',2,"Which is NOT a function of money?",
  "Producing goods",["Medium of exchange","Store of value","Unit of account"],"Money does not produce goods.")
H('11.B',3,"A $20 bill is worth more than the paper it is printed on because the government declares it legal tender. This is called what?",
  "Fiat money",["Commodity money","Representative money","Barter"],"Fiat money has value by decree.")
H('11.B',3,"Gold coins used as money are an example of what?",
  "Commodity money",["Fiat money","A debit card","A check"],"Commodity money has value on its own.")
H('11.C',3,"A drawback of barter compared with currency is what?",
  "It requires a double coincidence of wants",["It uses money","It is always fair","It is fast"],"Both parties must want the other's goods.")
H('11.C',3,"A benefit of a debit card is that it does what?",
  "Spends money directly from a checking account without creating debt",["Charges interest","Creates debt","Ends fees"],"Debit pulls from funds on hand.")
H('12.A',3,"The Federal Reserve System is made up of how many regional Federal Reserve Banks?",
  "12",["5","50","3"],"There are 12 districts.")
H('12.A',3,"Who sets monetary policy in the Federal Reserve System?",
  "The Federal Open Market Committee",["Congress","The Supreme Court","The President alone"],"The FOMC directs open market operations.")
H('12.B',3,"Which is one of the Fed's three basic tools of monetary policy?",
  "Open market operations",["Setting income taxes","Printing stock","Setting wages"],"The others are reserve requirements and the discount rate.")
H('12.B',3,"If the Fed raises the reserve requirement, banks must do what?",
  "Hold more money in reserve and lend less",["Lend more","Hold less","Close"],"Lending capacity falls.")
H('12.C',3,"When the Fed buys government securities on the open market, the money supply typically does what?",
  "Increases",["Decreases","Stays zero","Disappears"],"The Fed injects money into banks.")
H('12.C',3,"Raising the discount rate generally causes what?",
  "Borrowing to become more expensive for banks and the money supply to tighten",["Cheaper loans","More money","No effect"],"Higher rates slow lending.")
H('12.D',3,"The U.S. dollar is widely used in world trade, which is why it is called what?",
  "A major reserve currency",["A barter","A commodity","A tariff"],"Many nations hold dollars.")
H('12.D',3,"A very strong dollar can hurt U.S. exporters because it does what?",
  "Makes their goods more expensive abroad",["Makes them cheaper","Bans exports","Ends trade"],"Prices abroad rise.")
H('13.A',3,"Which is a role of government in the U.S. free enterprise system?",
  "Protecting property rights and enforcing contracts",["Setting all prices","Owning all firms","Banning competition"],"Government provides a legal framework.")
H('13.A',3,"Since the Great Depression, the role of the federal government in the economy has what?",
  "Generally expanded",["Disappeared","Ended","Shrunk to zero"],"The New Deal began broader involvement.")
H('13.B',3,"A cost of environmental regulation to a business can be what?",
  "Higher production costs",["Higher unemployment benefits","Fewer rules","Lower taxes"],"Compliance can be costly.")
H('13.B',3,"A benefit of consumer-protection laws is what?",
  "Safer products and fewer deceptive practices",["Higher fraud","Fewer standards","More risk"],"Rules protect consumers.")
H('14.A',2,"A sales tax is a tax on what?",
  "Purchases of goods and services",["Income","Property","Imports only"],"Sales taxes are collected at the register.")
H('14.A',2,"Which tax is the largest source of federal revenue?",
  "The individual income tax",["Sales tax","Property tax","Tariffs"],"Income taxes lead federal revenue.")
H('14.B',3,"Which is a major category of federal expenditures?",
  "Social Security and Medicare",["Allowances","Lottery winnings","Tariff refunds"],"Mandatory spending is large.")
H('14.B',3,"A federal budget deficit occurs when what happens?",
  "Spending is greater than revenue",["Revenue exceeds spending","Spending equals revenue","Taxes are zero"],"Borrowing covers the gap.")
H('14.C',3,"Cutting taxes to increase consumer spending is an example of what?",
  "Expansionary fiscal policy",["Contractionary monetary policy","A tariff","A subsidy"],"Fiscal policy uses taxes and spending.")
H('14.C',3,"Raising taxes and cutting spending to slow inflation is an example of what?",
  "Contractionary fiscal policy",["Expansionary policy","Barter","Free trade"],"It reduces demand.")
H('15.A',2,"A business owned and run by one person who is personally responsible for its debts is called what?",
  "A sole proprietorship",["A corporation","A partnership of 50","A cooperative"],"The owner has unlimited liability.")
H('15.A',2,"A corporation's owners are called what?",
  "Shareholders",["Partners","Proprietors","Depositors"],"Owners hold shares of stock.")
H('15.B',3,"An advantage of a corporation over a sole proprietorship is what?",
  "Limited liability for owners",["Unlimited liability","Double taxation avoided","Easier setup"],"Owners risk only their investment.")
H('15.B',3,"A disadvantage of a corporation is what?",
  "Profits may be taxed twice",["No liability","No ability to raise capital","No owners"],"Corporate and dividend taxes.")
H('16.A',2,"A bank helps households and businesses by doing what?",
  "Holding deposits and making loans",["Printing money","Setting prices","Owning homes"],"Banks connect savers and borrowers.")
H('16.A',3,"The FDIC insures bank deposits up to what amount per depositor, per bank, in each ownership category?",
  "$250,000",["$25,000","$2,500","$2 million"],"The standard limit is $250,000.")
H('16.B',3,"Savings in an economy become capital formation when they are used to do what?",
  "Fund investment in factories, equipment and new businesses",["Buy imports","Pay taxes","Stay in cash"],"Savings fund investment.")
H('16.B',3,"If a country's savings rate rises, capital for businesses generally does what?",
  "Becomes more available",["Disappears","Is banned","Becomes scarce"],"More loanable funds exist.")
H('16.C',3,"Which investment typically carries the highest risk and potential return?",
  "Stocks",["A savings account","A CD","A government savings bond"],"Stocks vary widely in price.")
H('16.C',3,"Interest rates rise with risk because lenders need what?",
  "Compensation for the chance of loss",["Fewer customers","Lower profit","No security"],"Higher risk calls for higher return.")
H('16.D',3,"A certificate of deposit usually pays a higher rate than a regular savings account because the money is what?",
  "Locked up for a set term",["Free to withdraw anytime","Uninsured","Risky"],"Less liquidity earns more.")
H('16.D',3,"A risk of a money market account compared with a checking account is what?",
  "Limits on transactions",["No interest","No insurance","No access ever"],"Transaction limits can apply.")
H('17.A',3,"A wise investor reduces risk by doing what?",
  "Diversifying across different investments",["Putting all money in one stock","Following rumors","Avoiding research"],"Diversification spreads risk.")
H('17.A',3,"An index fund is useful for beginners because it does what?",
  "Spreads investment across many companies at low cost",["Guarantees returns","Buys one stock","Has no fees ever"],"Funds are diversified.")
H('17.B',2,"A good way to begin a savings program is to do what?",
  "Set a goal and save a fixed amount each paycheck",["Save only leftovers","Spend first","Save nothing"],"Regular saving builds habit.")
H('17.B',2,"An emergency fund should cover about how many months of expenses?",
  "3 to 6 months",["1 day","2 years","10 years"],"A cushion for the unexpected.")
H('17.C',3,"Reconciling a bank statement means doing what?",
  "Comparing your records with the bank's to find errors",["Closing the account","Ignoring fees","Opening a loan"],"Reconciliation catches mistakes.")
H('17.C',3,"An outstanding check is one that has been written but not yet what?",
  "Cleared by the bank",["Signed","Deposited","Counted as income"],"It affects the bank balance until it clears.")
H('17.D',2,"A loan secured by the house being bought is called what?",
  "A mortgage",["A credit card","A payday loan","A scholarship"],"The home is collateral.")
H('17.D',2,"Which type of loan is typically used to finance a car?",
  "An installment auto loan",["A mortgage","A student grant","A bond"],"Cars are financed with installment loans.")
H('17.E',3,"A borrower's responsibility on a loan includes what?",
  "Repaying principal and interest on time",["Ignoring terms","Paying whenever","Skipping payments"],"Loans are legal obligations.")
H('17.E',3,"If a borrower defaults on a secured loan, the lender may do what?",
  "Take the collateral",["Forgive the loan","Pay the borrower","Raise wages"],"Collateral secures the debt.")
H('17.F',3,"Paying bills on time raises your credit score because it does what?",
  "Shows a history of reliability",["Hides debts","Raises interest","Closes accounts"],"Payment history is a major factor.")
H('17.F',3,"Keeping credit card balances well below the limit helps a credit score by doing what?",
  "Lowering credit utilization",["Raising utilization","Raising interest","Hiding payments"],"Low utilization looks responsible.")
H('18.A',2,"The best way to avoid credit card debt is to do what?",
  "Pay the full balance each month",["Pay the minimum","Skip payments","Take cash advances"],"Interest then never applies.")
H('18.A',3,"To pay off several cards faster, a strategy is to do what?",
  "Pay extra on the highest-interest card while paying minimums on the others",["Pay only minimums","Open more cards","Ignore interest"],"Targeting high interest saves money.")
H('18.B',3,"One cost of declaring personal bankruptcy is what?",
  "Damage to credit that can last up to 10 years",["A raise","A tax refund","Lower rates"],"It stays on a credit report for years.")
H('18.B',3,"One benefit of bankruptcy is that it can do what?",
  "Discharge certain debts and stop collection actions",["Increase debts","Raise credit","Guarantee a loan"],"It offers a fresh start.")
H('18.C',3,"Insurance protects against financial loss by doing what?",
  "Spreading risk across many policyholders",["Preventing accidents","Ending taxes","Raising risk"],"Premiums pool risk.")
H('18.C',3,"A higher deductible usually does what to the premium?",
  "Lowers it",["Raises it","Cancels it","Doubles it"],"You take on more risk.")
H('18.D',3,"A benefit of charitable giving is what?",
  "It can support a cause and may reduce taxable income",["It guarantees profit","It ends taxes","It is required by law"],"Donations may be deductible.")
H('18.D',3,"A cost of charitable giving is what?",
  "Less money available for your own spending and saving",["Higher income","Free goods","No cost at all"],"Giving has an opportunity cost.")
H('19.A',3,"A benefit of renting compared with buying is what?",
  "Lower upfront cost and flexibility to move",["Building equity","Tax deductions","Fixed payment forever"],"Renters avoid down payments.")
H('19.A',3,"A benefit of buying a home is that you can do what?",
  "Build equity as the loan is paid down",["Avoid all maintenance","Move freely","Skip taxes"],"Equity grows over time.")
H('19.B',3,"Before moving from renting to owning, a buyer should save for what?",
  "A down payment and closing costs",["A vacation","A new car","A hobby"],"Upfront costs are large.")
H('19.B',3,"Private mortgage insurance is often required when a down payment is less than what percent?",
  "20 percent",["2 percent","50 percent","90 percent"],"PMI protects the lender.")
H('20.A',2,"The FAFSA is used to apply for what?",
  "Federal student financial aid",["A credit card","A mortgage","A passport"],"It determines aid eligibility.")
H('20.A',2,"A student should file the FAFSA each year to do what?",
  "Stay eligible for aid",["Avoid taxes","Open a bank","Get a license"],"It must be renewed annually.")
H('20.B',2,"Scholarships differ from loans because scholarships do what?",
  "Do not have to be repaid",["Must be repaid with interest","Charge fees","Are always federal"],"Scholarships are gifts.")
H('20.B',2,"A good place to research scholarships is what?",
  "A school counselor or a state financial aid office",["A random ad","A stranger","A rumor"],"Trusted sources are best.")
H('20.C',3,"A Pell Grant is awarded based mainly on what?",
  "Financial need",["Athletic skill","Age","Grades alone"],"It is need-based aid that is not repaid.")
H('20.C',3,"Grants are preferred over loans because they do what?",
  "Do not have to be repaid",["Must be repaid","Charge interest","Have fees"],"Grants are free aid.")
H('20.D',3,"A federal student loan generally differs from a private loan because it often has what?",
  "Fixed rates and flexible repayment options",["Higher rates","No terms","No limit"],"Federal loans have borrower protections.")
H('20.D',3,"Subsidized federal loans differ from unsubsidized because the government does what?",
  "Pays the interest while the student is in school",["Charges more","Ends repayment","Sets no limit"],"Interest accrues for unsubsidized loans.")
H('20.E',2,"Federal work-study lets students do what?",
  "Earn money through part-time jobs while enrolled",["Skip classes","Borrow without limit","Avoid taxes"],"It is need-based work.")
H('20.E',2,"A benefit of a work-study job is that it can do what?",
  "Offer flexible hours around class schedules",["Cost money","Require full time","Cancel aid"],"Jobs are arranged with the school.")
H('21.A',3,"Placing the Great Depression, the New Deal and World War II in order uses which skill?",
  "Sequencing",["Categorizing","Generalizing","Mapping"],"Order events by time.")
H('21.A',3,"Explaining how higher interest rates lead to less borrowing shows which skill?",
  "Identifying cause and effect",["Sequencing","Summarizing","Mapping"],"Relate causes to effects.")
H('21.B',3,"A diagram showing flows of money between households, firms and government is called what?",
  "A circular-flow chart",["A supply curve","A bar graph","A map"],"It models the economy.")
H('21.B',3,"A supply and demand graph is an example of what kind of economic model?",
  "A graph of market behavior",["A map","A timeline","A table of laws"],"It shows price and quantity.")
H('21.C',3,"A student arguing whether the minimum wage should rise is doing what?",
  "Explaining a point of view on an economic issue",["Memorizing","Mapping","Counting"],"Positions need reasons.")
H('21.C',3,"A well-supported point of view includes what?",
  "Evidence and reasoning",["Only opinion","Insults","Rumors"],"Support claims.")
H('21.D',3,"A Bureau of Labor Statistics table is a what kind of source?",
  "Primary data source",["A rumor","A satire","A myth"],"It is official data.")
H('21.D',3,"To judge a news story about the economy, a student should check what?",
  "The author's expertise and the data used",["The font","The color","The page number"],"Credibility matters.")
H('21.E',3,"A line graph that rises across five years shows what about unemployment?",
  "Unemployment increased",["Fell","Stayed zero","Did not exist"],"Read the trend.")
H('21.E',3,"A pie chart of the federal budget shows what?",
  "The share of spending in each category",["Time trends","Locations","Names"],"Pie charts show parts of a whole.")
H('21.F',3,"A claim backed by data on rising rents is an example of what?",
  "A claim supported by evidence and reasoning",["An opinion","A rumor","A joke"],"Evidence supports claims.")
H('21.F',3,"A presentation that argues for lower taxes should do what?",
  "Support the claim with data and logic",["Skip evidence","Use insults","Use rumors"],"Use evidence.")
H('22.A',2,"Using the word \"inflation\" correctly means referring to what?",
  "A general rise in prices over time",["A fall in prices","A tax","A loan"],"Terminology must be accurate.")
H('22.A',2,"Which term means the amount of a good that sellers will offer at a price?",
  "Quantity supplied",["Demand","Scarcity","Tariff"],"Use terms correctly.")
H('22.B',3,"A strong oral presentation on trade policy includes what?",
  "A clear thesis, evidence and visuals",["No sources","Rambling","No visuals"],"Organization matters.")
H('22.B',3,"A visual that compares GDP across years is best shown as what?",
  "A bar or line graph",["A poem","A map of oceans","A diagram of a cell"],"Choose fitting visuals.")
H('22.C',3,"Civil discourse in an economics discussion means what?",
  "Listening respectfully and responding with reasons",["Interrupting","Insulting","Ignoring"],"Respect others' views.")
H('22.C',3,"During a debate on tariffs, a speaker should do what?",
  "Support points with evidence and respect opponents",["Shout","Avoid evidence","Name-call"],"Use evidence and courtesy.")
H('23',3,"A group must decide how to spend a $3,000 class budget. What is the best first step?",
  "Define the problem and list the options",["Spend it at once","Ignore needs","Vote with no information"],"Start by defining the problem.")
H('23',3,"After weighing the costs and benefits of each option, a group should do what?",
  "Choose a solution and later evaluate the results",["Stop","Hide the results","Never decide"],"Evaluate decisions.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_econfe.jsonl'))

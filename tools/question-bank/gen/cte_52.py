import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('127.', 1129, own='cte_52.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 297 Principles of Marketing ----
H('297.d.1.A',3,"A local grocery store hires neighborhood teens and donates unsold food to a shelter. Which two contributions to society does this show?",
  "Providing jobs and supporting community needs",["Raising prices and cutting hours","Avoiding taxes and ignoring customers","Reducing choices and closing early"],"Businesses contribute through employment and community support.")
H('297.d.1.A',4,"Which of these is a way a business contributes to the economy rather than only to its owners?",
  "Paying taxes that fund public services",["Keeping profits secret","Charging whatever it wants","Avoiding all hiring"],"Taxes and wages circulate through the economy.")
H('297.d.1.B',3,"A company that sources materials responsibly and treats workers fairly is showing:",
  "Social responsibility",["Price fixing","Monopoly power","Tax avoidance"],"Social responsibility means considering society, not just profit.")
H('297.d.1.B',4,"Why does social responsibility matter to a business' long-term success?",
  "Customers and employees tend to support companies they trust",["It guarantees no competition","It removes the need for marketing","It lowers all costs to zero"],"Trust builds loyalty and reputation.")
H('297.d.1.C',3,"A company that makes furniture from raw lumber is engaged in:",
  "Production",["Retail only","Banking","Insurance"],"Producing goods is a core business activity.")
H('297.d.1.C',4,"Which pair lists two types of business activities?",
  "Manufacturing and service",["Weather and sports","Hobbies and games","Birthdays and holidays"],"Businesses manufacture goods or provide services.")
H('297.d.1.D',3,"An organizational chart that shows departments such as marketing, finance, and operations illustrates a business's:",
  "Organizational design",["Weather forecast","Product slogan","Tax return"],"The chart shows how a business is structured.")
H('297.d.1.D',4,"In a functional organizational design, employees are grouped by:",
  "Job function such as sales or accounting",["Height","Birth month","Favorite color"],"Functional design groups similar jobs.")
H('297.d.1.E',3,"A business that sells products in several countries is operating in the:",
  "Global environment",["Local garage","School cafeteria","Family kitchen"],"Global operations cross national borders.")
H('297.d.1.E',4,"Exchange rates matter to a company that:",
  "Buys or sells products across countries",["Sells only on one street","Never uses money","Has no customers"],"Currency values affect international prices.")
H('297.d.1.F',3,"Which is an outside factor that affects the business environment?",
  "Government regulations",["The owner's mood","The break-room snacks","The color of the logo"],"Laws and regulations are external factors.")
H('297.d.1.F',4,"A new competitor opens next door. A business should respond by:",
  "Adjusting its strategy to the changed environment",["Closing immediately","Ignoring all changes","Lying to customers"],"Businesses adapt to environmental change.")
H('297.d.2.A',3,"The marketing concept says a business should focus on:",
  "Satisfying customer needs while earning a profit",["Selling at any cost","Ignoring customers","Copying competitors only"],"Customer satisfaction drives the marketing concept.")
H('297.d.2.A',4,"A company surveys customers before designing a new product. This applies the:",
  "Marketing concept",["Tax code","Zoning law","Payroll cycle"],"Starting with customer needs applies the concept.")
H('297.d.2.B',3,"Marketing research is a marketing function that involves:",
  "Gathering and analyzing information about customers",["Hiring staff","Paying taxes","Building roads"],"Research supports decision making.")
H('297.d.2.B',4,"Which marketing function includes setting a product's cost to customers?",
  "Pricing",["Distribution","Product development","Market research"],"Pricing establishes what customers pay.")
H('297.d.3.A',3,"The four Ps of the marketing mix are product, price, place, and:",
  "Promotion",["Profit","People","Paper"],"The standard marketing mix is the 4 Ps.")
H('297.d.3.A',4,"A company advertises in a magazine. Which P is this?",
  "Promotion",["Place","Price","Product"],"Advertising is promotion.")
H('297.d.3.B',3,"A strategy that uses all four Ps in a coordinated plan helps a business:",
  "Reach its target market effectively",["Avoid customers","Lower quality","Confuse buyers"],"A coordinated mix supports strategy.")
H('297.d.3.B',4,"A luxury brand uses high prices, premium stores, and elegant ads. This shows the mix:",
  "Working together to support one image",["Contradicting itself","Having no strategy","Ignoring the market"],"Consistency across the mix builds brand image.")
H('297.d.4.A',3,"A target market is:",
  "The group of customers a business most wants to reach",["Every person on Earth","Only the owner's friends","Competitors"],"Targeting focuses marketing effort.")
H('297.d.4.A',4,"Why do businesses choose a target market instead of trying to sell to everyone?",
  "To use limited resources more effectively",["To lose sales","To raise costs","To avoid customers"],"Focus improves efficiency.")
H('297.d.4.B',3,"An advantage of market segmentation is that it:",
  "Lets a business tailor messages to specific groups",["Makes all messages the same","Removes the need for research","Reduces product choices to one"],"Segments allow tailored approaches.")
H('297.d.4.B',4,"A possible disadvantage of segmentation is that it can:",
  "Increase costs because several plans are needed",["Eliminate customers","Remove all risk","Make products identical"],"More segments mean more planning.")
H('297.d.4.C',3,"Dividing customers by age, income, and gender is which kind of segmentation?",
  "Demographic",["Geographic","Psychographic","Behavioral"],"Age, income, and gender are demographics.")
H('297.d.4.C',4,"Dividing customers by climate or region is which kind of segmentation?",
  "Geographic",["Demographic","Psychographic","Behavioral"],"Location-based grouping is geographic.")
H('297.d.4.D',3,"Marketing planning typically begins with:",
  "Analyzing the market and setting objectives",["Printing fliers","Hiring a mascot","Choosing a font"],"Plans start with analysis and goals.")
H('297.d.4.D',4,"A marketing plan usually includes objectives, strategies, a budget, and:",
  "A way to evaluate results",["A joke","A rumor","A secret"],"Evaluation closes the loop.")
H('297.d.5.A',3,"A store sells 4 shirts at $15 each. The total sales are:",
  "$60",["$19","$45","$75"],"4 x 15 = 60.")
H('297.d.5.A',4,"A delivery takes 2.5 hours at 40 miles per hour. Distance traveled is:",
  "100 miles",["80 miles","42.5 miles","16 miles"],"40 x 2.5 = 100.")
H('297.d.5.B',3,"A bar graph shows sales were highest in December. A marketer should consider:",
  "Increasing holiday promotions",["Closing in December","Ignoring the graph","Lowering quality"],"Data informs decisions.")
H('297.d.5.B',4,"A line graph of sales falls for three straight months. A good next step is to:",
  "Investigate causes and adjust the strategy",["Celebrate","Raise all costs","Do nothing"],"Trends call for analysis.")
H('297.d.5.C',3,"Profit equals:",
  "Revenue minus costs",["Revenue plus costs","Costs minus revenue","Revenue times costs"],"Profit = revenue − costs.")
H('297.d.5.C',4,"Fixed costs are $2,000. Each unit sells for $20 and costs $10 to make. Break-even units equal:",
  "200",["100","400","20"],"2,000 / (20 − 10) = 200.")
H('297.d.5.D',3,"What is 15% of $80?",
  "$12",["$15","$8","$20"],"0.15 x 80 = 12.")
H('297.d.5.D',4,"A $50 item is on sale for 30% off. The sale price is:",
  "$35",["$20","$15","$30"],"50 x 0.70 = 35.")
H('297.d.5.E',3,"A store expects about 297 customers and rounds to the nearest hundred. The estimate is:",
  "300",["200","250","290"],"297 rounds to 300.")
H('297.d.5.E',4,"A marketer estimates the cost of 49 items at $9.95 each. A reasonable estimate is:",
  "About $500",["About $50","About $5,000","About $5"],"50 x 10 = 500.")
H('297.d.5.F',3,"A taxi charges $3 plus $2 per mile. Which equation models the cost C for m miles?",
  "C = 3 + 2m",["C = 3m + 2","C = 5m","C = 2 + 3"],"Flat fee plus rate times miles.")
H('297.d.5.F',4,"A subscription costs $10 a month plus a $15 setup fee. Total cost after n months is:",
  "10n + 15",["15n + 10","25n","10 + 15 + n"],"Rate times months plus setup.")
H('297.d.5.G',3,"Sales went from $200 to $260 in one month. The change in sales is:",
  "$60",["$460","$200","$130"],"260 − 200 = 60.")
H('297.d.5.G',4,"Sales rose $90 over 3 months. The average rate of change per month is:",
  "$30",["$270","$93","$3"],"90 / 3 = 30.")
H('297.d.6.A',3,"Good interpersonal skills in a team include:",
  "Listening and sharing responsibility",["Interrupting","Blaming others","Avoiding work"],"Teams need cooperation.")
H('297.d.6.A',4,"A team-building activity helps members to:",
  "Learn to trust and communicate",["Compete harshly","Work alone","Avoid conflict by quitting"],"Trust improves teamwork.")
H('297.d.6.B',3,"A short-term goal is one that you hope to reach:",
  "Within days or weeks",["After decades","Never","After retirement"],"Short-term goals are near.")
H('297.d.6.B',4,"Which is a long-term goal?",
  "Earning a college degree in four years",["Finishing homework tonight","Packing a lunch","Arriving on time tomorrow"],"Long-term goals take years.")
H('297.d.6.C',3,"A time-management principle is to:",
  "Plan ahead and prioritize tasks",["Do tasks randomly","Avoid deadlines","Wait for inspiration"],"Planning improves time use.")
H('297.d.6.C',4,"Breaking a big project into smaller scheduled steps helps with:",
  "Time management",["Memorizing slogans","Painting","Typing speed"],"Chunking supports planning.")
H('297.d.6.D',3,"Participating in a student career organization helps you develop:",
  "Leadership and career skills",["Weather skills","Cooking skills only","Sleeping habits"],"CTSOs build leadership.")
H('297.d.6.D',4,"A student attends a career fair to:",
  "Learn about careers and meet employers",["Avoid work","Win a prize only","Skip class only"],"Career events inform choices.")
H('297.d.7.A',3,"Which is a social media trend in marketing?",
  "Using short videos to reach customers",["Printing phone books","Sending telegrams","Faxing flyers"],"Short video is a current trend.")
H('297.d.7.A',4,"Influencer marketing is when a business:",
  "Partners with popular social media personalities to promote products",["Avoids social media","Prints coupons only","Fires staff"],"Influencers extend reach.")
H('297.d.7.B',3,"Technology impacts business by:",
  "Speeding communication and automating tasks",["Eliminating all customers","Making all jobs identical","Stopping sales"],"Technology changes operations.")
H('297.d.7.B',4,"Online ordering systems mainly help a store to:",
  "Serve customers 24 hours a day",["Reduce internet access","Close its doors","Raise confusion"],"E-commerce extends hours.")
H('297.d.7.C',3,"For a more accurate web search, you should use:",
  "Specific keywords",["One vague word","Only emojis","Random letters"],"Specific terms narrow results.")
H('297.d.7.C',4,"Before trusting a web source for marketing data, check the:",
  "Credibility and date of the source",["Font size","Color scheme","Number of ads"],"Evaluate sources.")
H('297.d.7.D',3,"Word-processing software is best used to create a:",
  "Business letter or report",["Spreadsheet formula","Database query","Photo edit only"],"Word processors handle text documents.")
H('297.d.7.D',4,"A marketer uses a mail merge to:",
  "Send personalized letters to many customers",["Delete files","Block email","Change fonts only"],"Mail merge personalizes bulk mail.")
H('297.d.7.E',3,"A customer database can be used to:",
  "Store and search customer information",["Cook meals","Print posters only","Delete employees"],"Databases organize records.")
H('297.d.7.E',4,"A marketer filters a database to find customers who bought in the last month. This is a:",
  "Query",["Chart","Slogan","Merge"],"Queries select matching records.")
H('297.d.7.F',3,"A spreadsheet can help a marketer to:",
  "Calculate totals and make charts",["Edit videos","Send faxes","Design logos only"],"Spreadsheets calculate and chart.")
H('297.d.7.F',4,"To total sales in cells B2 through B10, a marketer could use:",
  "=SUM(B2:B10)",["=B2+B10 only","SUM B2","=TOTAL B"],"SUM adds a range.")
H('297.d.8.A',3,"A working portfolio might include a resume, cover letter, and:",
  "Work samples",["Birthday cards","Receipts from lunch","Game scores"],"Portfolios show skills.")
H('297.d.8.A',4,"A portfolio should be kept:",
  "Updated and organized",["Hidden","Disorganized","Blank"],"Maintained portfolios are useful.")
H('297.d.8.B',3,"Employers may look at an applicant's public social media to judge:",
  "Professionalism and judgment",["Favorite color","Shoe size","Hair length"],"Online presence reflects character.")
H('297.d.8.B',4,"A student should remove posts that could harm employability, such as those that show:",
  "Offensive or unprofessional behavior",["Volunteer work","Awards","School achievements"],"Clean up unprofessional content.")
H('297.d.8.C',3,"A common interview question is:",
  "'Tell me about yourself.'",["'What is the weather?'","'Can you juggle?'","'Where is my pen?'"],"Interviewers ask about background.")
H('297.d.8.C',4,"Showing interview skills includes arriving early, dressing appropriately, and:",
  "Giving thoughtful answers with eye contact",["Texting during questions","Leaving early","Interrupting"],"Professional behavior matters.")
H('297.d.9.A',3,"A trend affecting marketing today is:",
  "Increased use of mobile devices for shopping",["Less technology","Fewer ads online","No data use"],"Mobile commerce is growing.")
H('297.d.9.A',4,"Customers who expect fast online delivery are driving a trend toward:",
  "Faster, more flexible fulfillment",["Slower shipping","Fewer products","No tracking"],"Customer expectations shape trends.")
H('297.d.9.B',3,"Researching emerging technologies helps marketers to:",
  "Find new ways to reach customers",["Avoid customers","Stop advertising","Delete data"],"New tools create new opportunities.")
H('297.d.9.B',4,"Which is an emerging marketing technology?",
  "Artificial intelligence that personalizes offers",["Typewriters","Phone books","Carbon paper"],"AI personalizes marketing.")
H('297.d.10.A',3,"Diversity affects marketing because customers have different:",
  "Backgrounds, needs, and preferences",["Heights only","Phone brands only","Shoe sizes only"],"Diverse customers want different things.")
H('297.d.10.A',4,"An ad that includes people of many backgrounds is likely to:",
  "Appeal to a wider range of customers",["Offend everyone","Reduce reach","Confuse sales"],"Inclusion broadens appeal.")
H('297.d.10.B',3,"Multiculturalism in marketing means recognizing:",
  "Many cultures among customers",["Only one culture","No cultures","Only tourists"],"Marketers respect cultural differences.")
H('297.d.10.B',4,"Multigenerational marketing considers that:",
  "Different age groups use different media and have different values",["Everyone is the same age","Only youth matter","Age never matters"],"Generations differ.")
H('297.d.11.A',3,"An economic good is something that:",
  "Is tangible and can satisfy a want",["Is only a feeling","Is free of cost always","Cannot be seen or used"],"Goods are physical items.")
H('297.d.11.A',4,"Which is a service rather than a good?",
  "A haircut",["A chair","A phone","A book"],"Services are intangible activities.")
H('297.d.11.B',3,"A need is something that is:",
  "Necessary for survival",["Always a luxury","A fashion trend","A hobby"],"Needs are essential.")
H('297.d.11.B',4,"Which is a want rather than a need?",
  "A designer watch",["Water","Food","Shelter"],"Wants are not essential.")
H('297.d.11.C',3,"Utility is the:",
  "Usefulness or satisfaction a good or service provides",["Price of a product","Tax on a sale","Color of a product"],"Utility measures value to the user.")
H('297.d.11.C',4,"A store open late adds which type of utility?",
  "Time utility",["Form utility","Possession utility","Place utility"],"Convenient hours add time utility.")
H('297.d.11.D',3,"Prices in a market act as:",
  "Signals that guide buyers and sellers",["Decorations","Random numbers","Secrets"],"Prices communicate scarcity and value.")
H('297.d.11.D',4,"A rising price for a scarce item tells producers to:",
  "Consider making more",["Stop selling","Hide stock","Close shops"],"Higher prices encourage supply.")
H('297.d.11.E',3,"When demand rises and supply stays constant, the price usually:",
  "Increases",["Decreases","Stays zero","Disappears"],"More demand pushes prices up.")
H('297.d.11.E',4,"When supply increases and demand stays constant, the price usually:",
  "Decreases",["Increases","Stays the same","Doubles"],"More supply lowers prices.")
H('297.d.12.A',3,"The basic economic questions include what to produce, how to produce it, and:",
  "For whom to produce it",["Where to sleep","When to nap","Why to laugh"],"What, how, for whom.")
H('297.d.12.A',4,"In a market economy, the question of what to produce is mostly decided by:",
  "Consumers and producers through the market",["A central planner only","Tradition only","Luck"],"Markets guide production.")
H('297.d.12.B',3,"Most economies are mixed because they combine:",
  "Private enterprise and government involvement",["No government","No businesses","Only barter"],"Mixed means both.")
H('297.d.12.B',4,"Public roads and private shops operating in the same country show a:",
  "Mixed economy",["Pure command economy","Pure barter economy","Traditional economy"],"Public and private mix.")
H('297.d.12.C',3,"One way government affects business is by:",
  "Setting regulations and collecting taxes",["Choosing company logos","Naming products","Planning lunch menus"],"Regulation and taxation.")
H('297.d.12.C',4,"Government may provide goods like roads that benefit businesses and:",
  "Society as a whole",["No one","Only competitors","Only foreigners"],"Public goods help all.")
H('297.d.13.A',3,"A characteristic of private enterprise is:",
  "Private ownership of businesses",["Government owns everything","No profit","No competition at all"],"Private ownership defines it.")
H('297.d.13.A',4,"In a private enterprise system, businesses decide:",
  "What to sell and how to price it",["Nothing","Only what government says","Nothing about quality"],"Business freedom.")
H('297.d.13.B',3,"An advantage of private enterprise is:",
  "Incentive to innovate and earn profit",["No risk","Guaranteed success","No competition"],"Profit motivates innovation.")
H('297.d.13.B',4,"A disadvantage of private enterprise can be:",
  "Unequal incomes and business failure",["No choices","No profits","No freedom"],"Risk and inequality are drawbacks.")
H('297.d.13.C',3,"Two gas stations lowering prices to attract customers is an example of:",
  "Price competition",["Monopoly","Barter","Taxation"],"Price competition lowers costs for buyers.")
H('297.d.13.C',4,"Competing on quality, service, or features rather than price is:",
  "Nonprice competition",["Price war","Monopoly","Subsidy"],"Nonprice competition emphasizes features.")
H('297.d.14.A',3,"Which is an economic measurement?",
  "Gross domestic product",["Shoe size","Phone color","Pet name"],"GDP measures output.")
H('297.d.14.A',4,"Gross domestic product measures:",
  "The total value of goods and services produced in a country",["Number of schools","Number of cars","Weather"],"GDP is total output.")
H('297.d.14.B',3,"Businesses use economic measures to:",
  "Plan production and investment",["Pick holidays","Name products","Choose colors"],"Measures guide planning.")
H('297.d.14.B',4,"Rising GDP may lead a business to:",
  "Expect higher customer spending",["Expect no sales","Close stores","Cut quality"],"Growth boosts demand.")
H('297.d.14.C',3,"Price stability means that prices:",
  "Do not change drastically over time",["Double each year","Fall to zero","Are unknown"],"Stable prices help planning.")
H('297.d.14.C',4,"Price stability helps businesses because it makes:",
  "Planning and budgeting more predictable",["Sales impossible","Costs random","Customers vanish"],"Predictability helps decisions.")
H('297.d.14.D',3,"Consumer spending is important because it:",
  "Drives a large share of economic activity",["Has no effect","Only affects taxes","Never changes"],"Spending fuels the economy.")
H('297.d.14.D',4,"If consumer spending drops sharply, businesses may:",
  "Reduce production and hiring",["Raise hiring","Expand rapidly","Ignore sales"],"Lower demand reduces activity.")
H('297.d.14.E',3,"A high unemployment rate means:",
  "Many people who want jobs cannot find them",["Everyone is working","Prices are zero","Businesses are booming"],"Unemployment signals weak job markets.")
H('297.d.14.E',4,"High unemployment can reduce business sales because:",
  "Unemployed people have less money to spend",["They buy more","They stop eating","Stores close for free"],"Less income, less spending.")
H('297.d.14.F',3,"Inflation is a:",
  "General rise in prices over time",["General fall in prices","Tax cut","Stock tip"],"Inflation raises price levels.")
H('297.d.14.F',4,"During inflation, a business' costs for materials usually:",
  "Increase",["Fall","Vanish","Stay fixed forever"],"Inflation raises costs.")
H('297.d.15.A',3,"A business cycle is the pattern of:",
  "Expansion and contraction in the economy",["Day and night","Seasons only","Tides"],"Cycles rise and fall.")
H('297.d.15.A',4,"The four phases of the business cycle are expansion, peak, contraction, and:",
  "Trough",["Valley of quiet only","Harvest","Plateau forever"],"The low point is the trough.")
H('297.d.15.B',3,"During an expansion, businesses typically:",
  "Hire more and increase production",["Fire everyone","Close stores","Stop selling"],"Growth encourages hiring.")
H('297.d.15.B',4,"During a contraction, consumers often:",
  "Reduce spending",["Spend wildly","Stop paying taxes","Ignore prices"],"Spending slows in downturns.")
H('297.d.16.A',3,"A channel of distribution moves a product from the:",
  "Producer to the consumer",["Consumer to producer","Mall to mall","Bank to bank"],"Channels connect producer and consumer.")
H('297.d.16.A',4,"A channel with a wholesaler and a retailer between the manufacturer and consumer is:",
  "Longer than a direct channel",["Direct","Nonexistent","Illegal"],"More intermediaries lengthen the channel.")
H('297.d.16.B',3,"Which is a physical distribution activity?",
  "Transportation",["Advertising","Pricing","Selling"],"Moving goods is physical distribution.")
H('297.d.16.B',4,"Storing goods in a warehouse until needed is:",
  "Storage",["Promotion","Pricing","Financing"],"Warehousing is storage.")
H('297.d.16.C',3,"Distribution costs include:",
  "Shipping and warehousing",["Weather","Logo design","Hobbies"],"Moving and storing cost money.")
H('297.d.16.C',4,"Reducing the number of intermediaries can lower:",
  "Distribution costs",["Quality","Customers","Safety"],"Fewer steps can mean lower costs.")
H('297.d.17.A',3,"A bank offering checking accounts and loans is providing:",
  "Financial services",["Weather services","Shipping","Retail goods"],"Banks provide financial services.")
H('297.d.17.A',4,"Which is a financial service?",
  "Insurance",["Window cleaning","Pet grooming","Moving"],"Insurance is a financial service.")
H('297.d.17.B',3,"A credit contract states the:",
  "Terms of borrowing, such as interest and payments",["Weather","Store hours","Name of the pet"],"Credit contracts list terms.")
H('297.d.17.B',4,"Before signing a credit contract, a buyer should:",
  "Read and understand the terms",["Sign without reading","Ignore interest","Skip the fine print"],"Understand obligations first.")
H('297.d.18.A',3,"A goal of pricing might be to:",
  "Maximize profit",["Lose money","Avoid sales","Hide products"],"Profit is a common goal.")
H('297.d.18.A',4,"A pricing goal aimed at gaining customers quickly is to:",
  "Increase market share",["Close the business","Cut quality","Avoid competition"],"Market share goal.")
H('297.d.18.B',3,"A factor that affects pricing is:",
  "Cost of production",["Name of CEO","Font used","Time of day"],"Costs influence price.")
H('297.d.18.B',4,"Competitors' prices affect a business' own prices because:",
  "Customers compare alternatives",["Customers never compare","Prices never change","Competition is illegal"],"Comparison shapes price.")
H('297.d.18.C',3,"A high price may signal to customers that the product has:",
  "High quality or prestige",["Poor quality","No value","No demand"],"Price shapes perception.")
H('297.d.18.C',4,"Pricing a product low means a business may need to rely on:",
  "Higher sales volume",["Fewer customers","Less distribution","No promotion"],"Low margins need volume.")
H('297.d.18.D',3,"A pricing policy where a business charges a high price at first and lowers it later is:",
  "Price skimming",["Penetration pricing","Loss leader","Odd pricing"],"Skimming starts high.")
H('297.d.18.D',4,"Setting a low initial price to attract many customers is:",
  "Penetration pricing",["Price skimming","Prestige pricing","Premium pricing"],"Penetration starts low.")
H('297.d.18.E',3,"A product costs $30 to make and has a 40% markup on cost. The price is:",
  "$42",["$12","$70","$34"],"30 x 1.4 = 42.")
H('297.d.18.E',4,"A store buys an item for $20 and sells it for $35. The markup in dollars is:",
  "$15",["$55","$20","$35"],"35 − 20 = 15.")
H('297.d.18.F',3,"Ethical pricing means:",
  "Being honest and fair with customers",["Hiding fees","Misleading buyers","Price fixing"],"Ethics require honesty.")
H('297.d.18.F',4,"Raising prices unfairly during an emergency is often criticized as:",
  "Price gouging",["Smart marketing","Standard pricing","Free promotion"],"Gouging is unethical and sometimes illegal.")
H('297.d.18.G',3,"Competitors agreeing together to set prices is called:",
  "Price fixing, which is illegal",["Legal","Honest","Common"],"Price fixing violates antitrust law.")
H('297.d.18.G',4,"Advertising a sale price that was never actually charged is:",
  "Deceptive pricing",["Allowed","A discount","A coupon"],"False price claims are deceptive.")
H('297.d.19.A',3,"In communication for promotion, the party who creates and sends a message is the:",
  "Sender",["Receiver","Noise","Feedback"],"Sender originates the message.")
H('297.d.19.A',4,"Customer reactions to an ad, such as buying or ignoring it, are:",
  "Feedback",["Noise","Sender","Medium"],"Feedback completes the process.")
H('297.d.19.B',3,"A coupon given to encourage a purchase is a type of:",
  "Sales promotion",["Personal selling","Packaging","Pricing policy"],"Coupons are sales promotion.")
H('297.d.19.B',4,"A news story about a company, not paid for by it, is:",
  "Publicity",["Advertising","Personal selling","Sales promotion"],"Publicity is unpaid coverage.")
H('297.d.19.C',3,"The promotional mix includes advertising, sales promotion, publicity, and:",
  "Personal selling",["Price","Place","Product"],"Mix elements.")
H('297.d.19.C',4,"A company uses ads, coupons, and sales staff together. This is the:",
  "Promotional mix",["Product mix","Channel","Budget"],"Combining tools is the mix.")
H('297.d.19.D',3,"The main role of promotion is to:",
  "Inform, persuade, and remind customers",["Confuse","Avoid","Hide"],"Promotion communicates.")
H('297.d.19.D',4,"Promotion supports the marketing mix by:",
  "Making customers aware of the product",["Setting the price","Building the factory","Hiring staff"],"Awareness drives demand.")
H('297.d.19.E',3,"An ethical promotion is one that is:",
  "Truthful",["Misleading","Exaggerated","Hidden"],"Truthfulness is ethical.")
H('297.d.19.E',4,"Advertising that makes false claims about a product is:",
  "Unethical and potentially illegal",["Smart","Required","Harmless"],"False advertising is unethical.")
H('297.d.19.F',3,"The Federal Trade Commission helps regulate:",
  "Advertising claims",["School grades","Highway speeds","Weather"],"The FTC polices ads.")
H('297.d.19.F',4,"Promotion regulations are meant to protect:",
  "Consumers from deceptive practices",["Companies from competitors","Ads from truth","Prices from change"],"Regulation protects consumers.")
H('297.d.19.G',3,"A direct marketing channel reaches customers:",
  "Without a retailer in between",["Only through stores","Never","Through wholesalers only"],"Direct means no intermediary.")
H('297.d.19.G',4,"Direct mail and telemarketing are examples of:",
  "Direct marketing channels",["Public relations","Packaging","Pricing"],"They reach customers directly.")
H('297.d.19.H',3,"A sales promotion communication channel might be:",
  "A coupon sent by email",["A tax form","A bank loan","A lease"],"Email coupons promote sales.")
H('297.d.19.H',4,"A 'buy one get one free' offer communicated by in-store signs is:",
  "Sales promotion",["Publicity","Personal selling","Financing"],"Short-term incentives promote sales.")
H('297.d.19.I',3,"Press releases are used in:",
  "Public relations",["Pricing","Distribution","Packaging"],"PR communicates with the media.")
H('297.d.19.I',4,"A company sponsors a community cleanup to build goodwill. This is:",
  "Public relations",["Price fixing","Direct mail","Personal selling"],"Community events support PR.")
H('297.d.20.A',3,"Television, radio, and newspapers are examples of:",
  "Advertising media",["Pricing methods","Product lines","Financial services"],"Media carry ads.")
H('297.d.20.A',4,"Which medium lets an advertiser target by interest and location online?",
  "Digital advertising",["Billboards only","Phone books","Handbills only"],"Digital targets precisely.")
H('297.d.20.B',3,"Product advertising focuses on:",
  "A specific product",["The company's image only","Taxes","Hiring"],"Product ads promote items.")
H('297.d.20.B',4,"An ad promoting a company's reputation rather than one item is:",
  "Institutional advertising",["Product advertising","Coupon","Price ad"],"Institutional builds image.")
H('297.d.20.C',3,"An effective ad often has a headline, a visual, and:",
  "A call to action",["A secret","A rumor","A joke only"],"Call to action prompts response.")
H('297.d.20.C',4,"The part of an ad that tells customers what to do next is the:",
  "Call to action",["Headline","Illustration","Border"],"It directs the response.")
H('297.d.21.A',3,"A risk caused by a fire at a store is a:",
  "Natural or physical risk",["Market risk only","Legal risk only","Social risk only"],"Fires are physical risks.")
H('297.d.21.A',4,"Theft by employees is which category of risk?",
  "Human risk",["Natural risk","Economic risk","Market risk"],"Theft is a human risk.")
H('297.d.21.B',3,"Insurance helps a business to:",
  "Reduce the financial impact of risks",["Avoid customers","Raise prices","Eliminate all risk"],"Insurance transfers risk.")
H('297.d.21.B',4,"A new competitor entering the market is a:",
  "Market risk",["Fire risk","Weather risk","Theft risk"],"Competition is a market risk.")
H('297.d.22.A',3,"Which is a security precaution at a store?",
  "Locking doors and using cameras",["Leaving cash out","Sharing keys freely","Disabling alarms"],"Security prevents theft.")
H('297.d.22.A',4,"Limiting who knows the safe combination is a:",
  "Security precaution",["Marketing tactic","Pricing policy","Promotion"],"Access control protects assets.")
H('297.d.22.B',3,"A workplace safety precaution is to:",
  "Wear required safety equipment",["Ignore signs","Block exits","Run in halls"],"Safety gear prevents injury.")
H('297.d.22.B',4,"A spilled liquid on a store floor should be:",
  "Cleaned up or marked right away",["Left for later","Ignored","Hidden"],"Prevent slips and falls.")
H('297.d.23.A',3,"A feature is a:",
  "Characteristic of a product",["Customer's feeling","Price tag","Slogan"],"Features describe the product.")
H('297.d.23.A',4,"A benefit is:",
  "What the feature does for the customer",["Product weight","Product color only","Product code"],"Benefits meet needs.")
H('297.d.23.B',3,"Organizational buyers purchase goods:",
  "For business use or resale",["For personal use only","For free","For gifts only"],"Organizational buying serves businesses.")
H('297.d.23.B',4,"Compared with consumers, organizational buyers usually buy:",
  "Larger quantities with more formal processes",["Smaller quantities casually","Nothing","Only on impulse"],"Business purchases are formal.")
H('297.d.23.C',3,"A salesperson determines customer needs by:",
  "Asking questions and listening",["Guessing","Talking only","Showing everything"],"Questions reveal needs.")
H('297.d.23.C',4,"A customer says they need a phone with a long battery. The salesperson should:",
  "Show phones that match that need",["Show the cheapest","Show the largest","Ignore the need"],"Match need to product.")
H('297.d.23.D',3,"A buying motive is:",
  "A reason a customer buys",["A store's location","A price tag","A coupon code"],"Motives explain buying.")
H('297.d.23.D',4,"Buying a product because it is the lowest price is a(n):",
  "Rational motive",["Emotional motive","Patronage motive only","Habit motive"],"Price-based motives are rational.")
H('297.d.23.E',3,"The first step in the decision-making process for buyers is to:",
  "Recognize a need or problem",["Buy immediately","Return the item","Complain"],"Need recognition starts the process.")
H('297.d.23.E',4,"After identifying alternatives, a buyer should:",
  "Evaluate them before choosing",["Pick randomly","Skip comparison","Ask no one"],"Evaluate then decide.")
H('297.d.24.A',3,"A salesperson can locate product information in:",
  "Product manuals and catalogs",["Weather reports","Sports pages","Menus"],"Reliable sources.")
H('297.d.24.A',4,"Before talking to a customer about a new product, a salesperson should:",
  "Learn its features and benefits",["Guess","Avoid it","Wait for questions"],"Product knowledge builds trust.")
H('297.d.24.B',3,"A step in the sales process is:",
  "Approaching the customer",["Closing the store","Avoiding the customer","Skipping the greeting"],"The approach starts the sale.")
H('297.d.24.B',4,"After presenting a product, a salesperson asks for the sale. This is the:",
  "Close",["Greeting","Follow-up","Approach"],"Closing asks for the purchase.")
H('297.d.25.A',3,"Positive customer relations help a business to:",
  "Keep customers and earn repeat business",["Lose customers","Raise complaints","Avoid sales"],"Good relations build loyalty.")
H('297.d.25.A',4,"A friendly greeting and quick help shows:",
  "Positive customer relations",["Poor service","Neglect","A pricing error"],"Courtesy builds relations.")
H('297.d.25.B',3,"A customer service mindset means:",
  "Putting the customer's needs first",["Avoiding customers","Being rushed","Ignoring feedback"],"Customer-focused attitude.")
H('297.d.25.B',4,"An employee with a service mindset who sees a lost customer will:",
  "Offer to help",["Look away","Hide","Mind their own business"],"Proactive help.")
H('297.d.25.C',3,"Managers support customer relations by:",
  "Training employees and setting service standards",["Ignoring service","Removing training","Cutting staff"],"Management sets standards.")
H('297.d.25.C',4,"A manager who empowers employees to solve problems at the counter is:",
  "Supporting customer service",["Harming service","Ignoring the customer","Lowering morale"],"Empowerment speeds solutions.")
H('297.d.25.D',3,"A brand promise is:",
  "What a company commits customers can expect",["A random slogan","A tax form","A coupon"],"Promises set expectations.")
H('297.d.25.D',4,"A restaurant that advertises 'ready in 10 minutes' must:",
  "Deliver on that promise",["Ignore it","Change it daily","Hide it"],"Promises must be kept.")
H('297.d.25.E',3,"Employee performance reinforces a company's image when employees:",
  "Act professionally and follow brand standards",["Argue with customers","Ignore policies","Gossip"],"Behavior shapes image.")
H('297.d.25.E',4,"A company with a reputation for friendliness is hurt when an employee is:",
  "Rude to a customer",["Helpful","Smiling","On time"],"Rudeness harms image.")
H('297.d.25.F',3,"Customer relationship management software helps businesses to:",
  "Track customer contacts and preferences",["Print money","Replace employees","Close stores"],"CRM stores customer data.")
H('297.d.25.F',4,"A CRM system can remind a salesperson to:",
  "Follow up with a customer on a set date",["Skip follow-up","Raise price","Fire staff"],"Reminders support service.")
H('297.d.26.A',3,"Trustworthiness is shown by:",
  "Being honest and keeping promises",["Lying","Breaking promises","Hiding errors"],"Trust is earned by honesty.")
H('297.d.26.A',4,"A salesperson who admits a product has a limitation shows:",
  "Honesty and trustworthiness",["Poor sales skill","Carelessness","Disloyalty"],"Honest disclosure builds trust.")
H('297.d.26.B',3,"Business ethics are:",
  "Standards of right and wrong in business",["Tax laws","Price lists","Store hours"],"Ethics are moral standards.")
H('297.d.26.B',4,"A business that advertises truthfully is following:",
  "Business ethics",["Pricing policy","Distribution","Packaging"],"Truthful advertising is ethical.")
H('297.d.26.C',3,"A legal issue affecting a business is:",
  "Contract disputes",["The weather","Music taste","Fashion"],"Contracts raise legal issues.")
H('297.d.26.C',4,"A business that does not follow consumer protection laws may face:",
  "Fines or lawsuits",["Awards","Free advertising","Lower taxes"],"Violations bring penalties.")
H('297.d.26.D',3,"Human resources regulations protect employees from:",
  "Unfair treatment and discrimination",["Fair pay","Good management","Training"],"HR laws protect workers.")
H('297.d.26.D',4,"A law that requires equal treatment in hiring is an example of:",
  "Human resources regulation",["Pricing law","Shipping law","Tax law"],"Anti-discrimination law is HR regulation.")
H('297.d.26.E',3,"The Occupational Safety and Health Administration (OSHA) sets rules for:",
  "Workplace safety",["Product prices","Ad colors","Tax rates"],"OSHA protects workers.")
H('297.d.26.E',4,"An employer that provides safety training and equipment is following:",
  "Workplace regulations",["Pricing rules","Advertising rules","Import rules"],"Safety training is required.")
H('297.d.26.F',3,"An employment relationship is created when:",
  "A worker agrees to work for pay under an employer's direction",["Two friends chat","A customer buys","A supplier delivers"],"Work for pay creates employment.")
H('297.d.26.F',4,"A written agreement stating pay and duties helps clarify the:",
  "Employment relationship",["Product line","Channel","Promotion"],"Agreements clarify expectations.")
H('297.d.26.G',3,"Trade regulations control:",
  "Buying and selling across borders",["Local weather","School lunches","Music"],"Trade laws govern imports and exports.")
H('297.d.26.G',4,"A tariff is a:",
  "Tax on imported goods",["Subsidy","Prize","Coupon"],"Tariffs tax imports.")
H('297.d.26.H',3,"Antitrust laws are meant to:",
  "Promote fair competition",["Create monopolies","Raise prices","Reduce choices"],"Antitrust protects competition.")
H('297.d.26.H',4,"A company that controls an entire market and blocks competitors is a:",
  "Monopoly, which antitrust laws oppose",["Partnership","Cooperative","Franchise"],"Monopolies reduce competition.")
H('297.d.27.A',3,"When evaluating alternatives at work, you should consider your:",
  "Personal ethics and company rules",["Mood","Friends","Weather"],"Ethics guide decisions.")
H('297.d.27.A',4,"A coworker offers you a bribe to approve an order. The best response is to:",
  "Decline and report it",["Accept","Accept half","Say nothing"],"Bribery is unethical.")
H('297.d.27.B',3,"Unethical behavior at work can lead to:",
  "Job loss and damaged reputation",["Promotion","Awards","Raises"],"Consequences can be severe.")
H('297.d.27.B',4,"A long-term consequence of falsifying records may be:",
  "Criminal charges",["A larger bonus","A new office","A vacation"],"Falsification is serious.")
H('297.d.27.C',3,"To investigate how to respond to a workplace dilemma, you should:",
  "Consult policies and ask a supervisor",["Guess","Ignore it","Post online"],"Check policy first.")
H('297.d.27.C',4,"When values and policy seem to conflict, the best step is to:",
  "Seek guidance before acting",["Act in secret","Quit","Blame others"],"Ask for guidance.")
H('297.d.27.D',3,"Responsible behavior at work includes:",
  "Admitting mistakes and fixing them",["Hiding errors","Blaming coworkers","Missing deadlines"],"Responsibility means accountability.")
H('297.d.27.D',4,"A worker who returns extra change to a customer shows:",
  "Honesty and integrity",["Poor math","Weakness","Carelessness"],"Integrity under temptation.")
H('297.d.28.A',3,"To find the training needed for an occupation, you can use:",
  "Career websites and job postings",["Cartoons","Rumors","Menus"],"Postings list requirements.")
H('297.d.28.A',4,"A marketing manager job may require a bachelor's degree and:",
  "Related experience",["Nothing","A pilot's license","A chef's hat"],"Experience supplements education.")
H('297.d.28.B',3,"Participating in an internship helps a student to:",
  "Gain real-world experience",["Avoid learning","Skip school","Lose skills"],"Internships build skills.")
H('297.d.28.B',4,"Taking a dual-credit marketing course can help a student:",
  "Earn college credit while in high school",["Avoid graduation","Skip classes","Lose credits"],"Dual credit saves time.")
H('297.d.29.A',3,"Product planning involves:",
  "Deciding what products to develop and offer",["Collecting taxes","Hiring only","Paying bills"],"Planning guides products.")
H('297.d.29.A',4,"Using customer feedback to improve a product is part of:",
  "Product planning",["Tax planning","Shipping","Payroll"],"Feedback shapes development.")
H('297.d.29.B',3,"A product mix is:",
  "The total group of products a company sells",["One product only","A coupon","A price list"],"Mix means all offerings.")
H('297.d.29.B',4,"Adding a gluten-free item to a bakery's menu to meet customer requests changes the:",
  "Product mix",["Tax rate","Zoning","Loan"],"New items change the mix.")
H('297.d.29.C',3,"The product life cycle stages are introduction, growth, maturity, and:",
  "Decline",["Beginning","Plateau only","Rebirth always"],"Products eventually decline.")
H('297.d.29.C',4,"Sales are rising quickly and profits are growing. The product is in the:",
  "Growth stage",["Introduction stage","Decline stage","Maturity stage"],"Rapid sales indicate growth.")

# ---- 298 Practicum in Marketing ----
H('298.d.1.A',3,"A marketing intern needs to share a report. The best way is to:",
  "Write a clear summary and speak with the manager about key points",["Send a blank file","Leave it on a desk","Wait for a request"],"Written and verbal clarity.")
H('298.d.1.A',4,"A visual aid in a presentation should:",
  "Support the message and be easy to read",["Be crowded","Distract","Be unrelated"],"Visuals clarify.")
H('298.d.1.B',3,"A customer describes a problem. Active listening means you:",
  "Pay attention and ask clarifying questions",["Interrupt","Look away","Talk over them"],"Listening clarifies information.")
H('298.d.1.B',4,"Repeating a customer's request in your own words:",
  "Confirms you understood",["Wastes time","Annoys them","Cancels it"],"Paraphrasing confirms.")
H('298.d.1.C',3,"A well-delivered presentation includes:",
  "Practice, eye contact, and a clear structure",["Mumbling","Reading slides only","No preparation"],"Preparation helps delivery.")
H('298.d.1.C',4,"An informal presentation is most appropriate for:",
  "A quick update to teammates",["A shareholder meeting","A court hearing","A formal award"],"Casual settings suit informal talks.")
H('298.d.1.D',3,"To communicate data to a team, a marketer should:",
  "Explain what the data mean and what to do next",["Hand over raw numbers","Hide trends","Use jargon only"],"Interpretation leads to action.")
H('298.d.1.D',4,"An effective chart for comparing monthly sales is a:",
  "Bar or line graph",["Photograph","Map","Poem"],"Graphs show comparisons.")
H('298.d.1.E',3,"Public relations skills in an internship might include:",
  "Writing a friendly response to a customer comment",["Ignoring comments","Deleting reviews","Arguing online"],"PR protects image.")
H('298.d.1.E',4,"Maintaining good relations with outside partners requires:",
  "Prompt, courteous communication",["Late replies","Rude emails","Silence"],"Courtesy builds relations.")
H('298.d.2.A',3,"Critical thinking when planning a promotion means:",
  "Weighing evidence about what has worked",["Copying competitors blindly","Ignoring data","Guessing"],"Evidence supports plans.")
H('298.d.2.A',4,"A teammate suggests a plan that failed last year. A critical thinker asks:",
  "'What will we change this time?'",["'Do it anyway.'","'Never mind.'","'Who cares?'"],"Learn from results.")
H('298.d.2.B',3,"Technical research for a marketing decision may include:",
  "Studying market reports and competitors",["Guessing","Asking no one","Skipping analysis"],"Research informs strategy.")
H('298.d.2.B',4,"A marketer researching a new product's market size would consult:",
  "Credible industry data",["Rumors","Opinions only","Advertisements only"],"Use credible data.")
H('298.d.2.C',3,"To solve a problem creatively, a marketing team can:",
  "Brainstorm many options before choosing",["Pick the first idea","Avoid ideas","Delay forever"],"Brainstorming expands options.")
H('298.d.2.C',4,"Sales are flat in an online store. A creative solution might be to:",
  "Test a new bundle offer",["Close the website","Remove all products","Raise every price"],"Test creative ideas.")
H('298.d.3.A',3,"A safety rule in a retail stockroom is to:",
  "Lift heavy boxes with proper technique",["Stack boxes unsafely","Block exits","Run with boxes"],"Safe lifting prevents injury.")
H('298.d.3.A',4,"Emergency exits in a store should be:",
  "Kept clear and unlocked from inside",["Blocked with stock","Hidden","Locked from inside"],"Exits must be accessible.")
H('298.d.3.B',3,"Acceptable use policies for computers say you should:",
  "Use company technology only for approved purposes",["Install any game","Share passwords","Browse unsafe sites"],"Follow tech policy.")
H('298.d.3.B',4,"A customer database should be protected by:",
  "Strong passwords and limited access",["Posting it online","Sharing logins","Open access"],"Protect customer data.")
H('298.d.4.A',3,"A positive work ethic during a practicum includes:",
  "Completing tasks on time and with care",["Doing as little as possible","Complaining","Arriving late"],"Effort and reliability.")
H('298.d.4.A',4,"A practicum student who stays busy when work is slow might:",
  "Ask for another task",["Wait quietly","Use the phone","Leave early"],"Initiative shows work ethic.")
H('298.d.4.B',3,"A coworker asks you to share confidential pricing with a friend. You should:",
  "Decline politely and follow company policy",["Share it","Sell it","Post it"],"Confidentiality matters.")
H('298.d.4.B',4,"When two responses to a workplace situation are possible, a good choice is the one that:",
  "Matches ethics and company rules",["Is easiest","Is secret","Helps only you"],"Ethics guide choices.")
H('298.d.4.C',3,"Showing integrity means:",
  "Choosing the ethical action even when it costs you",["Taking shortcuts","Lying","Blaming others"],"Integrity under pressure.")
H('298.d.4.C',4,"You discover you made a pricing error that favors the customer. Integrity says to:",
  "Tell your supervisor",["Hide it","Blame a coworker","Ignore it"],"Report your mistake.")
H('298.d.4.D',3,"Complying with OSHA and other workplace rules means:",
  "Following them every day",["Following them sometimes","Ignoring them","Breaking them quietly"],"Compliance is consistent.")
H('298.d.4.D',4,"Rules and regulations for a marketing job may include:",
  "Truth-in-advertising laws",["Fashion trends","Sports rules","Cooking tips"],"Advertising laws apply.")
H('298.d.5.A',3,"In a supervised marketing experience, students should:",
  "Document tasks and evaluate what they learned",["Hide logs","Skip reflection","Avoid feedback"],"Documentation supports learning.")
H('298.d.5.A',4,"A weekly log of tasks, hours, and lessons learned is part of:",
  "Documenting a learning activity",["Wasting time","Cheating","Advertising"],"Logs show progress.")
H('298.d.5.B',3,"Advanced technical knowledge in marketing could include:",
  "Using analytics to measure ad performance",["Memorizing slogans","Drawing only","Typing only"],"Analytics is a technical skill.")
H('298.d.5.B',4,"To strengthen technical skills during a practicum, a student can:",
  "Ask for training on marketing software",["Refuse training","Avoid tools","Repeat one task"],"Training builds skill.")
H('298.d.5.C',3,"Information technology tools used to manage marketing tasks include:",
  "Project management and scheduling software",["Typewriters","Rolodexes","Paper only"],"IT tools organize work.")
H('298.d.5.C',4,"A shared calendar helps a marketing team to:",
  "Coordinate campaign deadlines",["Hide tasks","Lose files","Create conflicts"],"Calendars coordinate.")
H('298.d.5.D',3,"Communicating information about a product to customers requires:",
  "Accurate, clear, and persuasive messaging",["Vague messages","Misleading claims","No message"],"Quality messaging.")
H('298.d.5.D',4,"Concepts and strategies for communicating product information include knowing the:",
  "Audience and the message goal",["Weather","Moon phase","Birthdays"],"Know the audience.")
H('298.d.5.E',3,"A sales promotion communication channel could be:",
  "A text message with a discount code",["A tax notice","A bank loan","A lease"],"Text promos reach customers.")
H('298.d.5.E',4,"Modeling a communication channel for a promotion means:",
  "Showing how the message reaches customers",["Hiding the message","Skipping delivery","Drawing a map"],"Channels deliver messages.")
H('298.d.5.F',3,"Applying the marketing mix means coordinating:",
  "Product, price, place, and promotion",["Taxes only","Staff only","Rent only"],"Coordinated 4 Ps.")
H('298.d.5.F',4,"Lowering a price and increasing advertising at the same time adjusts which two Ps?",
  "Price and promotion",["Product and place","Place and product","Place only"],"Price and promotion changed.")
H('298.d.5.G',3,"Product planning includes related activities like:",
  "Market research and packaging design",["Payroll only","Parking only","Filing taxes only"],"Planning includes research and design.")
H('298.d.5.G',4,"Before launching a new product, a team should:",
  "Test it with target customers",["Skip testing","Hide it","Delay indefinitely"],"Testing reduces risk.")
H('298.d.5.H',3,"Evaluating an advertisement means looking at its message, visuals, and:",
  "Whether it appeals to the target audience",["The weather","The size of the building","The stock price"],"Evaluate effectiveness.")
H('298.d.5.H',4,"A strong ad headline typically:",
  "Grabs attention and fits the audience",["Confuses","Hides the product","Is too long"],"Headlines attract.")
H('298.d.5.I',3,"Growth in technical skill competencies is shown by:",
  "Completing tasks with less supervision over time",["Needing more help","Avoiding tasks","Making more errors"],"Independence shows growth.")
H('298.d.5.I',4,"A student tracks skills such as data entry and design each month. This shows:",
  "Progress over time",["Nothing","Luck","A tax filing"],"Tracking shows growth.")
H('298.d.5.J',3,"Evaluating strengths and weaknesses helps a student to:",
  "Target areas for improvement",["Hide mistakes","Avoid work","Compare to friends"],"Self-assessment guides growth.")
H('298.d.5.J',4,"A student excels at design but struggles with spreadsheets. A reasonable plan is to:",
  "Practice spreadsheets with a mentor",["Avoid spreadsheets","Quit design","Do nothing"],"Work on weak areas.")
H('298.d.5.K',3,"A work sample for a marketing portfolio could be:",
  "A flyer you designed",["A grocery list","A game score","A recipe"],"Samples show skills.")
H('298.d.5.K',4,"The best work samples are those that:",
  "Show your skills and are accurate and well-presented",["Are messy","Are unrelated","Are copied"],"Quality samples impress.")

H('297.d.3.A',4,"A bakery sells cakes (product), sets $24 each (price), uses a downtown shop (place), and runs a weekend radio spot. Which element does the radio spot represent?",
  "Promotion",["Place","Product","Price"],"Radio advertising is the promotion element of the mix.")
H('297.d.4.A',4,"A sports shoe brand aims its new line at teen athletes instead of all shoppers. This choice defines its:",
  "Target market",["Product life cycle","Break-even point","Distribution channel"],"Choosing a specific customer group defines the target market.")
H('297.d.4.B',4,"A retailer creates separate ads for students, parents, and retirees. A cost of doing this is that:",
  "Each segment needs its own message, which raises planning expense",["Customers are ignored","Only one ad is needed","Data becomes unnecessary"],"Multiple segments multiply planning and production costs.")
H('297.d.6.B',4,"A student plans to finish this week's project by Friday and to open a business within ten years. These are examples of:",
  "A short-term goal and a long-term goal",["Two long-term goals","Two short-term goals","Neither type of goal"],"Time frames distinguish short- and long-term goals.")
H('297.d.14.A',4,"Which statistic would a business analyst use to see how fast a national economy is growing?",
  "Change in gross domestic product",["The mayor's approval rating","Average shoe size","Local rainfall"],"GDP growth measures economic expansion.")
H('297.d.16.C',4,"A manufacturer's fuel and driver wages for trucking goods to stores are part of its:",
  "Distribution costs",["Promotion costs","Product design costs","Tax credits"],"Transportation expenses are distribution costs.")
H('298.d.5.I',4,"A practicum student once needed a coach for each report, but now writes them alone and accurately. This growth shows:",
  "Improved technical skill competency",["A decline in skill","No change","Luck"],"Working independently shows growth.")
H('298.d.5.J',4,"After a mock sales call, a student lists strong greetings but weak product knowledge. This list is a:",
  "Self-evaluation of strengths and weaknesses",["Sales report","Tax form","Price list"],"Listing strengths and weaknesses is self-evaluation.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_52.jsonl'))

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('127.', 1116, own='cte_39.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---------- 232 Fashion Marketing ----------
H('232.d.4',3,"A boutique owner tracks sales in a spreadsheet, takes online orders, and uses social media to show new arrivals. These are:",
  "advanced technology applications",["hand sewing tools","fabric swatches","garment racks"],"Software and online tools support modern retail.")
H('232.d.4',4,"A store uses a point-of-sale system that updates inventory every time an item is sold. This technology mainly helps with:",
  "accurate stock tracking",["fabric dyeing","pattern cutting","hemming"],"POS systems keep inventory counts current.")
H('232.d.5',3,"Knowing the difference between knit and woven fabrics helps a fashion retailer:",
  "describe and sell products accurately",["avoid customers","lower the thread count","stop selling"],"Fashion knowledge supports accurate selling.")
H('232.d.5',4,"A salesperson explains that a cotton-polyester blend resists wrinkles better than pure cotton. This shows knowledge of:",
  "textile properties",["store lighting","shipping routes","tax law"],"Fiber content affects performance.")
H('232.d.6',3,"A stock room worker keeps boxes off the walkway and stacks them safely. This is applying:",
  "safety regulations",["fashion trends","pricing rules","display rules"],"Safe storage prevents falls and injuries.")
H('232.d.6',4,"A customer spills a drink near the fitting rooms. Which action best applies safety practices?",
  "Place a wet-floor sign and clean it up",["Step over it","Wait until closing","Tell the customer to clean it"],"Marking and cleaning prevents slips.")
H('232.d.9',3,"A retail employee learns to fold stock quickly and neatly, which saves time. This builds technical skills for:",
  "efficiency",["delay","waste","clutter"],"Skilled routines speed up work.")
H('232.d.9',4,"Which habit improves efficiency when restocking a clothing store?",
  "Sorting items by size and style before placing them",["Putting items back at random","Stacking everything in one pile","Leaving boxes on the floor"],"Pre-sorting saves time on the floor.")
H('232.d.1.A',3,"A sales associate writes a clear product description and proofreads her email to a vendor. She is applying:",
  "English language arts skills",["welding skills","gym skills","music skills"],"Writing skills support business communication.")
H('232.d.1.A',4,"Which task uses English language arts skills in a fashion store?",
  "Writing an accurate product tag and ad copy",["Steaming a garment","Hanging a display","Counting the register"],"Descriptive writing requires correct language.")
H('232.d.1 B',3,"A shirt costs $24.50 and a scarf costs $13.25. What is the total before tax?",
  "$37.75",["$36.75","$38.25","$37.25"],"24.50 + 13.25 = 37.75.")
H('232.d.1 B',4,"A $60 jacket is 25% off. What is the sale price?",
  "$45",["$15","$35","$50"],"60 x 0.75 = 45.")
H('232.d.2.A',3,"A salesperson talks to a teenager in casual language and to a business client in more formal language. She is adapting:",
  "language for audience and situation",["her price tags","her shoes","her store hours"],"Language should fit the listener.")
H('232.d.2.A',4,"Which message best fits a formal email to a fashion supplier?",
  "Dear Mr. Patel, I would like to confirm our order for the fall line.",["yo send the stuff","hey whats up lol","need clothes asap"],"Formal tone fits business partners.")
H('232.d.2.B',3,"A manager puts today's tasks in order of priority and tells the team. She is:",
  "organizing oral and written information",["hiding tasks","guessing","erasing tasks"],"Organized information helps teams work.")
H('232.d.2.B',4,"Which opening-day checklist is best organized?",
  "Tasks grouped by area with a person assigned to each",["A random list","One sentence","A blank sheet"],"Grouping and assigning makes tasks clear.")
H('232.d.2.C',3,"A buyer notices which colors sold best last month and tells her team. She is:",
  "interpreting and communicating data",["ignoring results","guessing","hiding information"],"Reporting sales data guides decisions.")
H('232.d.2.C',4,"Which statement communicates sales data clearly?",
  "Blue sweaters sold 40 units in June compared with 15 in May.",["Blue sold well, I think.","Things moved.","Some items were fine."],"Specific numbers support decisions.")
H('232.d.2.D',3,"A student shows her classmates a fall fashion line using slides. This is a:",
  "formal presentation",["private diary","password","receipt"],"A planned talk with slides is formal.")
H('232.d.2.D',4,"Explaining a new display idea to a coworker while folding sweaters is:",
  "an informal presentation",["a formal keynote","a legal filing","a shareholder report"],"Casual sharing is informal.")
H('232.d.2.E',3,"A shopper describes the exact style she wants. The associate nods, takes notes, and repeats it back. This is:",
  "active listening",["interrupting","ignoring","daydreaming"],"Repeating confirms understanding.")
H('232.d.2.E',4,"A customer asks for something 'trendy but comfortable.' The best response is to:",
  "ask what styles or fabrics she has liked before",["guess","show everything","end the talk"],"Questions clarify vague requests.")
H('232.d.2.F',3,"A store serves shoppers of many ages and cultures. A good associate will:",
  "communicate respectfully with each person",["use stereotypes","avoid some customers","rush people"],"Respect builds loyalty.")
H('232.d.2.F',4,"A customer who is hard of hearing visits the store. Which approach is helpful?",
  "Face the customer, speak clearly, and offer written details",["Speak louder from far away","Walk away","Ignore the customer"],"Clear, patient communication helps.")
H('232.d.2.G',3,"A store replies politely to a social media complaint and offers to fix the problem. This builds:",
  "customer relations",["tension","mistrust","delay"],"Good PR protects the brand.")
H('232.d.2.G',4,"Thanking employees and keeping customers informed about sales builds both internal and external:",
  "public relations",["delays","errors","clutter"],"PR strengthens relationships.")
H('232.d.3.A',3,"A manager reviews return reasons to find why one dress style keeps coming back. This is:",
  "critical thinking with data",["guessing","luck","ignoring data"],"Analyzing data helps solve problems.")
H('232.d.3.A',4,"A store's sales dropped after moving the display. Critical thinking suggests she should:",
  "compare sales before and after and test other causes",["blame the weather","restore it without checking","stop selling"],"Compare data before concluding.")
H('232.d.3.B',3,"Three employees disagree about how to lay out a sale rack. A good approach is to:",
  "discuss ideas and decide together",["let one dictate","avoid the topic","flip a coin"],"Group problem solving uses communication.")
H('232.d.3.B',4,"Which phrase helps a team solve a staffing problem?",
  "What options do we have to cover the schedule?",["That's your fault.","I won't help.","Not my job."],"Solution-focused language helps.")
H('232.d.7.A',3,"A store lead sets the sales goal, assigns jobs, and cheers on the team. She is showing:",
  "leadership",["avoidance","laziness","carelessness"],"Leaders guide groups toward goals.")
H('232.d.7.A',4,"A busy holiday weekend approaches. A good leader will:",
  "plan schedules and tasks ahead of time",["wait and see","ignore the rush","cut hours for everyone"],"Planning supports collective goals.")
H('232.d.7.B',3,"A manager thanks a stock clerk for staying late and gives helpful feedback. This promotes:",
  "effective working relationships",["tension","distance","resentment"],"Appreciation builds trust.")
H('232.d.7.B',4,"Which is constructive feedback to a new sales associate?",
  "Your greeting is friendly; try asking one more question before suggesting items.",["You're bad at this.","Never mind.","Do better."],"Specific, supportive feedback helps.")
H('232.d.7.C',3,"A student organization opens its meeting by having the president call the group to order. This follows:",
  "parliamentary procedure",["a secret rule","a menu","a price list"],"Parliamentary procedure organizes meetings.")
H('232.d.7.C',4,"In parliamentary procedure, a member who wants the group to consider an idea makes a:",
  "motion",["rumor","guess","complaint"],"A motion brings business before the group.")
H('232.d.7.D',3,"An experienced buyer shows a new employee how to read a sales report. This is:",
  "mentoring",["competing","hiding information","copying"],"Mentors teach and inspire.")
H('232.d.7.D',4,"A good mentor in fashion retail:",
  "shares knowledge patiently and encourages questions",["keeps tricks secret","corrects harshly","avoids teaching"],"Patience builds skill.")
H('232.d.8.A',3,"A salesperson returns extra change a customer was given by mistake. This is:",
  "ethical conduct",["greed","carelessness","gossip"],"Honesty is ethical.")
H('232.d.8.A',4,"A coworker offers to give you credit for a sale you did not make. The ethical choice is to:",
  "decline and give credit to the person who made it",["accept the credit","say nothing","ask for a bonus"],"Honesty includes crediting work correctly.")
H('232.d.8.B',3,"A retailer wants to print a famous brand's logo on its own shirts without permission. This could violate:",
  "copyright and trademark law",["traffic law","safety rules","tax rules"],"Logos are protected intellectual property.")
H('232.d.8.B',4,"A designer uses a pattern created by another artist on her tote bags without a license. This is:",
  "a copyright violation",["fair use","public domain use","ethical practice"],"Using protected art without permission infringes copyright.")
H('232.d.10.A',3,"Selecting styles to purchase, ordering, receiving, and pricing merchandise describes the process of:",
  "retail buying",["window cleaning","sewing","dyeing"],"Retail buying brings merchandise into stores.")
H('232.d.10.A',4,"Which step comes first in the retail buying process?",
  "Determine customer needs and set a buying budget",["Mark down leftover stock","Send thank-you cards","Close the register"],"Planning precedes purchasing.")
H('232.d.10.B',3,"Trade shows, showrooms, and market centers are:",
  "wholesale market resources",["retail checkouts","fitting rooms","coat racks"],"Buyers find wholesale products there.")
H('232.d.10.B',4,"A buyer wants to see many vendors' new lines in one place. A good resource is:",
  "a trade show",["a fashion blog only","a clearance rack","a mailing label"],"Trade shows gather many vendors.")
H('232.d.10.C',3,"Comparing a luxury market with a discount market is comparing:",
  "apparel markets",["fabrics only","hair styles","jewelry designs only"],"Markets differ by price level and customers.")
H('232.d.10.C',4,"A fast-fashion market differs from a couture market mainly in:",
  "speed of production and price level",["the number of buttons","the color of tags","store hours"],"Fast fashion is quick and affordable; couture is custom and costly.")
H('232.d.10.D',3,"A store sells winter coats at full price in October and marks them down in January. This shows how timing affects:",
  "pricing",["sewing","dyeing","hanging"],"Seasonal demand changes price.")
H('232.d.10.D',4,"Why do retailers discount swimwear in late summer?",
  "Demand falls as the season ends",["Swimwear is harder to make","Customers prefer paying more","Stores run out of tags"],"End-of-season demand drops.")
H('232.d.10.E',3,"A store pays $20 for a shirt and sells it for $45. What is the markup amount?",
  "$25",["$20","$65","$45"],"45 - 20 = 25.")
H('232.d.10.E',4,"A scarf costs $12 wholesale and the retailer adds a 100% markup on cost. What is the retail price?",
  "$24",["$12","$36","$20"],"100% of 12 is 12; 12 + 12 = 24.")
H('232.d.10.F',3,"A department store, a boutique, and an online shop are different types of:",
  "retail outlets",["fabrics","patterns","stitches"],"Retail outlets sell to consumers in different ways.")
H('232.d.10.F',4,"Which outlet usually offers the widest range of merchandise under one roof?",
  "A department store",["A single-brand boutique","A pop-up kiosk","A street vendor"],"Department stores carry many categories.")
H('232.d.10.G',3,"Sourcing garments from factories in other countries is called:",
  "offshore sourcing",["local weaving","hand tailoring","window dressing"],"Offshore sourcing buys overseas.")
H('232.d.10.G',4,"One reason retailers use offshore sourcing is to:",
  "lower production costs",["increase shipping time to zero","avoid all trade rules","raise the price of fabric"],"Lower labor costs can reduce prices.")
H('232.d.10.H',3,"A buyer plans how many items to order, what to charge, and how many to sell by month. She is composing a:",
  "scenario plan",["window display","press release","fitting schedule"],"Scenario plans project sales and inventory.")
H('232.d.10.H',4,"If expected sales drop in a scenario plan, the buyer should:",
  "reduce purchases or adjust pricing",["order more stock","ignore the plan","close the store"],"Plans guide purchase adjustments.")
H('232.d.11.A',3,"The idea that a business should meet customers' needs and wants in order to be successful is the:",
  "marketing concept",["tax concept","tailoring concept","shipping concept"],"Marketing focuses on customer needs.")
H('232.d.11.A',4,"A store surveys shoppers before choosing which jeans to carry. This applies the marketing concept by:",
  "putting customer needs first",["ignoring customers","choosing the cheapest","copying a competitor exactly"],"Customer needs guide decisions.")
H('232.d.11.B',3,"Pricing, selling, promoting, and distributing fashion goods are:",
  "marketing functions",["sewing steps","dyeing steps","cutting steps"],"Marketing includes several functions.")
H('232.d.11.B',4,"Setting the price of a new line of sneakers is the marketing function of:",
  "pricing",["distribution","financing","storage"],"Pricing decides what customers pay.")
H('232.d.11.C',3,"Product, price, place, and promotion are the four parts of the:",
  "marketing mix",["sewing kit","supply chain","retail plan"],"The marketing mix combines these elements.")
H('232.d.11.C',4,"Selling a new line only in high-end boutiques is a decision about:",
  "place",["product","price","promotion"],"Place covers where goods are sold.")
H('232.d.11.D',3,"A brand that makes athletic wear for runners has identified a:",
  "target market",["fabric type","store layout","tax rate"],"A target market is the group a business aims to serve.")
H('232.d.11.D',4,"Why is knowing the target market important?",
  "It helps match products, prices, and promotions to buyers",["It lowers taxes","It removes competition","It shortens store hours"],"Targeting improves marketing results.")
H('232.d.11.E',3,"Aiming a product at one specific group is called market segmentation. Aiming at everyone is:",
  "mass marketing",["niche selling","segmenting","targeting"],"Mass marketing treats all customers alike.")
H('232.d.11.E',4,"An advantage of market segmentation is that it:",
  "allows messages tailored to a group's needs",["costs nothing","reaches everyone equally","removes all risk"],"Tailoring improves response.")
H('232.d.11.F',3,"Researching what colors are trending and how shoppers use social media is studying:",
  "trends and emerging technologies",["tax forms","shoe sizes","store keys"],"Trend research guides fashion marketing.")
H('232.d.11.F',4,"A retailer starts using augmented reality so shoppers can see clothes on themselves virtually. This is an:",
  "emerging technology",["old method","manual process","sewing step"],"AR is a new technology for retail.")
H('232.d.11.G',3,"A shop that sells only plus-size vintage dresses is practicing:",
  "niche marketing",["mass marketing","discount selling","random selling"],"A niche focuses on a small specialized market.")
H('232.d.11.G',4,"Which is an example of a niche market in fashion?",
  "Adaptive clothing for people with disabilities",["All clothing for all ages","Any store with many items","A general discount store"],"Adaptive clothing serves a specialized group.")
H('232.d.11.H',3,"Religious holidays, regional customs, and school dress codes are:",
  "cultural and societal influences on fashion",["sewing tools","store rules only","tax rules"],"Culture shapes what people wear.")
H('232.d.11.H',4,"A retailer expecting a cultural festival might stock:",
  "traditional garments customers wear for the event",["unrelated items only","nothing new","only winter coats"],"Understanding culture helps stock the right goods.")
H('232.d.11.I',3,"Selling a U.S. fashion brand to customers in other countries is:",
  "international marketing",["local marketing only","private marketing","garage sales"],"International marketing reaches global buyers.")
H('232.d.11.I',4,"International marketing has affected the fashion industry by:",
  "spreading trends and creating global brands",["ending all trends","stopping trade","closing all stores"],"Global exposure spreads styles.")
H('232.d.12.A',3,"Advertising, visual merchandising, publicity, and personal selling are the parts of the:",
  "promotional mix",["pricing chart","fabric chart","store plan"],"The promotional mix combines promotion tools.")
H('232.d.12.A',4,"A store window display is part of which promotional tool?",
  "Visual merchandising",["Personal selling","Direct mail only","Publicity only"],"Displays attract attention visually.")
H('232.d.12.B',3,"Arranging a mannequin outfit with accessories to attract shoppers is:",
  "visual merchandising",["tailoring","dyeing","shipping"],"Visual merchandising presents products.")
H('232.d.12.B',4,"Placing the best-selling items at eye level near the entrance is a visual merchandising technique that:",
  "draws attention to key products",["hides products","slows customers","confuses customers"],"Placement guides attention.")
H('232.d.12.C',3,"A store compares sales before and after a campaign to see if it worked. This is analyzing the plan's:",
  "effectiveness",["packaging","fabric","color"],"Results show whether a plan succeeded.")
H('232.d.12.C',4,"Which measure would show a promotion's effectiveness?",
  "Change in sales during the promotion",["The number of tags printed","The color of the banner","The number of mannequins"],"Sales change shows impact.")
H('232.d.12.D',3,"Advertising a 'half-price' sale when the price was first raised is:",
  "a deceptive practice",["fair pricing","honest advertising","a courtesy"],"Misleading discounts deceive customers.")
H('232.d.12.D',4,"Claiming a coat is 'genuine leather' when it is plastic is:",
  "false advertising",["fair advertising","accurate labeling","good service"],"Misrepresenting materials is deceptive.")
H('232.d.12.E',3,"A store tells the truth about its sale and discount terms. This is:",
  "ethical promotion",["deception","cheating","hiding"],"Honest ads are ethical.")
H('232.d.12.E',4,"Which advertisement is ethical?",
  "One that shows real prices and accurate product details",["One that hides fees","One that exaggerates features","One that uses fake testimonials"],"Ethical promotion is truthful.")
H('232.d.13.A',3,"Sales, coupons, loyalty programs, and special events are types of:",
  "business promotion strategies",["sewing methods","tailoring tools","tax rules"],"These strategies encourage purchases.")
H('232.d.13.A',4,"A loyalty program that gives points for each purchase encourages:",
  "repeat customers",["theft","returns","closing"],"Rewards bring shoppers back.")
H('232.d.13.B',3,"A shopper who buys the latest style to look current is motivated by:",
  "fashion and social acceptance",["no reason","tax savings","a coupon only"],"Buying motives include status and image.")
H('232.d.13.B',4,"A parent buys durable school clothes because they last, showing a motive of:",
  "value and durability",["status","boredom","curiosity"],"Practical buyers look for value.")
H('232.d.13.C',3,"A press release announcing a store's grand opening is part of:",
  "public relations and publicity",["bookkeeping","cutting fabric","shipping"],"Publicity earns free media attention.")
H('232.d.13.C',4,"Publicity differs from paid advertising because it is usually:",
  "not paid for by the business",["always paid for","private","illegal"],"Publicity is earned media.")
H('232.d.13.D',3,"A boutique runs a trunk show to preview new styles to preferred customers. This is a:",
  "promotional activity",["recall","return policy","tax form"],"Special events promote products.")
H('232.d.13.D',4,"Why might a retailer host a charity fashion event?",
  "To promote the brand while supporting a cause",["To avoid customers","To raise taxes","To lose money"],"Events build goodwill.")
H('232.d.13.E',3,"Choosing the date, venue, budget, and models for a fashion show is:",
  "planning a special event",["sewing a gown","dyeing fabric","hanging a sign"],"Event planning organizes all details.")
H('232.d.13.E',4,"Which should be decided first when planning a retail fashion show?",
  "The goal and the budget",["The color of the napkins","The song title","The model's shoes"],"Goals and budgets guide planning.")
H('232.d.13.F',3,"A show called 'Summer Under the Stars' with matching decor, music, and clothing has a:",
  "theme",["budget","receipt","hang tag"],"A theme unifies the show.")
H('232.d.13.F',4,"A good fashion show theme should:",
  "tie the clothing, music, and decor together",["ignore the products","confuse the audience","distract from the clothes"],"Consistency makes the show effective.")
H('232.d.13.G',3,"A scale drawing of the runway and seating helps planners:",
  "visualize the staging before building it",["avoid planning","print tags","train models"],"Scale drawings show how space is used.")
H('232.d.13.G',4,"On a scale of 1 inch = 4 feet, a 20-foot runway is drawn as:",
  "5 inches",["4 inches","20 inches","10 inches"],"20 / 4 = 5.")
H('232.d.13.H',3,"Assigning someone to dress models, someone to run the music, and someone to greet guests is describing:",
  "fashion show responsibilities",["store hours","tax duties","shipping dates"],"Roles keep the show running.")
H('232.d.13.H',4,"The person who coordinates when models enter and exit the runway is the:",
  "backstage manager",["cashier","accountant","stylist assistant"],"The backstage manager controls timing.")
H('232.d.13.I',3,"A short announcement sent to newspapers about a store's upcoming sale is a:",
  "press release",["tax return","price tag","pattern"],"Press releases publicize events.")
H('232.d.13.I',4,"Which information belongs at the top of a press release?",
  "The key news: what, who, when, and where",["A long story about the founder","A list of prices","Unrelated jokes"],"Lead with the essentials.")
H('232.d.14.A',3,"Mannequins, props, signs, and lighting are components used in developing:",
  "displays",["patterns","hems","orders"],"Displays use many components.")
H('232.d.14.A',4,"Which item is a component of a window display?",
  "A mannequin dressed in the featured outfit",["A cash register","A delivery truck","A shipping label"],"Mannequins show products.")
H('232.d.14.B',3,"Using repeated shapes and a clear focal point in a display applies design elements and:",
  "principles",["mistakes","taxes","labels"],"Elements and principles guide design.")
H('232.d.14.B',4,"Placing the largest, brightest item in the center to attract the eye creates:",
  "emphasis",["confusion","noise","clutter"],"Emphasis directs attention.")
H('232.d.14.C',3,"Window displays face outside shoppers while islands and shelves inside the store are:",
  "interior displays",["exterior displays","private displays","hidden displays"],"Displays can be interior or exterior.")
H('232.d.14.C',4,"An exterior display is mainly used to:",
  "attract passersby into the store",["list store policies","show tax rates","hide products"],"Exterior displays draw traffic.")
H('232.d.14.D',3,"A student arranges mannequins, props, and signs for a spring window. She is:",
  "creating a window display",["writing a tax form","hemming","packing"],"Display creation applies design skills.")
H('232.d.14.D',4,"Before installing a display, a designer should:",
  "plan the layout and check safety of props",["skip planning","use broken props","block the door"],"Planning and safety come first.")
H('232.d.15.A',3,"Greeting customers, answering questions, and handling returns well are factors that promote:",
  "quality customer relations",["poor service","delays","confusion"],"Service quality builds loyalty.")
H('232.d.15.A',4,"Which factor most promotes quality customer relations?",
  "Responding promptly and courteously",["Ignoring complaints","Arguing with customers","Closing early"],"Prompt courtesy builds trust.")
H('232.d.15.B',3,"A store trains staff to respect customs and languages of different customers. This evaluates the impact of:",
  "cultural diversity on customer relations",["fabric prices","store lighting","shelf height"],"Cultural awareness improves service.")
H('232.d.15.B',4,"A customer asks about a garment for a cultural ceremony. A good response is to:",
  "listen and offer appropriate options respectfully",["assume what she wants","change the subject","dismiss the request"],"Respect matters in diverse communities.")
H('232.d.15.C',3,"Smiling, greeting each customer, and offering help shows:",
  "effective customer service skills",["poor habits","avoidance","disinterest"],"These behaviors define good service.")
H('232.d.15.C',4,"Which action shows effective customer service?",
  "Offering to find another size in the stockroom",["Pointing at a rack","Ignoring a shopper","Saying it's not your job"],"Going the extra step pleases customers.")
H('232.d.15.D',3,"A customer receives a shirt with a missing button. A good solution is to:",
  "offer a replacement, repair, or refund",["blame the customer","refuse to help","hide the shirt"],"Solutions solve customer issues.")
H('232.d.15.D',4,"A customer is upset about a late order. Which approach is best?",
  "Apologize, explain, and offer a clear fix",["Argue","Ignore the complaint","Transfer blame"],"Calm solutions keep customers.")
H('232.d.15.E',3,"Helping customers choose clothing and ringing up purchases is part of:",
  "selling fashion products in retail",["manufacturing","dyeing","shipping"],"Retail selling serves customers directly.")
H('232.d.15.E',4,"A salesperson's role in a clothing store is mainly to:",
  "match customers' needs with products",["avoid customers","count only stock","clean windows only"],"Selling means meeting needs.")
H('232.d.16.A',3,"A shopper buys a prom dress for a school event. Her motive is:",
  "a special occasion",["no reason","random boredom","a tax break"],"Occasion drives many purchases.")
H('232.d.16.A',4,"Which is a motive for buying a fashion product?",
  "Wanting to feel confident",["Wanting to avoid shopping","Wanting to waste money","Wanting no style"],"Emotional motives influence buying.")
H('232.d.16.B',3,"A salesperson who is friendly, knowledgeable, and honest has qualities of:",
  "an effective salesperson",["a poor seller","an unprepared worker","a disengaged worker"],"Good sellers combine knowledge and honesty.")
H('232.d.16.B',4,"Which quality makes a salesperson more effective?",
  "Knowing the product line well",["Being unprepared","Rushing customers","Arguing"],"Product knowledge builds credibility.")
H('232.d.16.C',3,"A salesperson explains the difference between a tunic and a blazer using correct terms. She is applying:",
  "fashion vocabulary",["tax language","cooking terms","legal terms"],"Correct terms show expertise.")
H('232.d.16.C',4,"A customer asks what 'selvage' means. The salesperson answers that it is:",
  "the finished edge of a fabric",["a type of button","a shoe style","a hair product"],"Selvage is the self-finished edge.")
H('232.d.16.D',3,"Greeting a customer, finding needs, presenting products, handling objections, and closing the sale are the steps of:",
  "effective sales techniques",["inventory counts","pattern making","window cleaning"],"A sale follows these steps.")
H('232.d.16.D',4,"After a customer says a coat is too expensive, the salesperson should:",
  "highlight its value and offer alternatives",["agree and end the sale","argue","walk away"],"Handling objections can save a sale.")
H('232.d.17.A',3,"Cameras, security tags, and mirrors in a store are used to control:",
  "risk such as theft",["lighting only","hiring","pricing"],"Surveillance reduces losses.")
H('232.d.17.A',4,"A security tag on a jacket helps prevent:",
  "shoplifting",["color fading","shrinking","wrinkling"],"Tags trigger alarms when unpaid items leave.")
H('232.d.17.B',3,"Counting stock and preparing a report on what is on hand uses:",
  "inventory information",["fabric dyes","fashion shows","window props"],"Inventory data helps decisions.")
H('232.d.17.B',4,"Inventory information helps a retailer decide:",
  "what to reorder",["which models to hire","what music to play","where to hang signs"],"Counts guide purchases.")
H('232.d.17.C',3,"Accepting cash, giving change, and swiping a card are:",
  "transaction methods",["sewing steps","display steps","pattern steps"],"Transactions complete the sale.")
H('232.d.17.C',4,"A customer pays $18.40 with a $20 bill. How much change is due?",
  "$1.60",["$2.60","$1.40","$1.40.60"],"20 - 18.40 = 1.60.")
H('232.d.17.D',3,"Using last year's holiday sales to estimate this year's is making a:",
  "forecast",["guess","refund","display"],"Forecasts use past data.")
H('232.d.17.D',4,"Which data helps make an accurate sales forecast?",
  "Past sales, trends, and seasons",["The store's paint color","Employee shoe sizes","The mall's hours"],"Historical data supports predictions.")
H('232.d.17.E',3,"A buyer prepares a purchase order that lists the style, quantity, and price. She is demonstrating the:",
  "fashion buying process",["tailoring process","dyeing process","cleaning process"],"Purchase orders are part of buying.")
H('232.d.17.E',4,"Which document confirms what a store orders from a vendor?",
  "A purchase order",["A pay stub","A press release","A hang tag"],"Purchase orders record orders.")
H('232.d.17.F',3,"Reducing a price to sell slow-moving stock is a:",
  "markdown",["markup","cost","shipment"],"Markdowns lower the price.")
H('232.d.17.F',4,"Cash flow in a store describes:",
  "money coming in and going out",["the number of mannequins","the length of aisles","the age of customers"],"Cash flow tracks money movement.")
H('232.d.17.G',3,"A customer slips and is hurt in the store. An employee should follow:",
  "the accident reporting procedure",["no procedure","a menu","a sales script"],"Accidents must be reported and documented.")
H('232.d.17.G',4,"Why must safety incidents be reported accurately?",
  "To protect people and meet legal requirements",["To hide errors","To avoid training","To raise prices"],"Accurate reports protect everyone.")

# ---------- 233 Practicum in Fashion Marketing ----------
H('233.d.2',3,"A practicum student compares sales by color to find why a style is not selling. She is using:",
  "advanced problem-solving methods",["guessing","luck","avoidance"],"Analyzing data solves problems.")
H('233.d.2',4,"An item sells in stores but not online. Which problem-solving step comes first?",
  "Gather data on website views and returns",["Remove the item","Raise the price","Ignore it"],"Data guides the solution.")
H('233.d.1.A',3,"A practicum student greets customers with eye contact and a clear voice. This is:",
  "verbal and non-verbal communication",["silent work","avoidance","guessing"],"Words and body language work together.")
H('233.d.1.A',4,"Which action shows effective communication at a busy checkout?",
  "A friendly greeting, clear explanation of the total, and a thank-you",["Silence","Mumbling the total","Looking away"],"Clarity and courtesy matter.")
H('233.d.1.B',3,"A student reviews weekly sales numbers and explains the trends to her supervisor. She is:",
  "interpreting and communicating data",["ignoring numbers","guessing","hiding results"],"Reporting data supports decisions.")
H('233.d.1.B',4,"Which statement best communicates results from a promotion?",
  "Sales rose 12% during the weekend event compared with the prior week.",["It went okay.","Some people came.","Things changed."],"Specific figures are clear.")
H('233.d.1.C',3,"A supervisor explains a new return policy. The student asks a question and repeats the steps. This is:",
  "active listening",["interrupting","daydreaming","ignoring"],"Repeating confirms understanding.")
H('233.d.1.C',4,"Which behavior shows active listening?",
  "Taking notes and confirming key points",["Checking a phone","Interrupting","Looking away"],"Notes and confirmation show attention.")
H('233.d.1.D',3,"A customer sighs and looks at her watch during a long line. The associate should recognize she may be:",
  "impatient",["delighted","asleep","finished shopping"],"Nonverbal cues show feelings.")
H('233.d.1.D',4,"An associate sees a shopper frowning at a price tag. A good response is to:",
  "offer help and explain the value",["ignore her","raise the price","walk away"],"Reading cues improves service.")
H('233.d.1.E',3,"A manager sends thank-you notes to repeat customers. This helps maintain:",
  "external customer relations",["internal errors","long lines","stock levels"],"Gratitude builds loyalty.")
H('233.d.1.E',4,"An employee thanks a coworker for covering a shift. This supports:",
  "internal relations",["external advertising","tax filing","shipping"],"Appreciation strengthens teams.")
H('233.d.3.A',3,"A practicum student learns where the fire exits, first-aid kit, and spill cleanup supplies are kept. She is following:",
  "workplace safety rules",["fashion rules","pricing rules","display rules"],"Safety knowledge protects people.")
H('233.d.3.A',4,"Which practice helps prevent falls in a retail store?",
  "Keeping aisles clear and cleaning spills quickly",["Stacking boxes in aisles","Leaving cords out","Ignoring wet floors"],"Clear aisles prevent accidents.")
H('233.d.3.B',3,"A customer faints near the entrance. The employee should:",
  "call for help and follow emergency procedures",["step over her","ignore it","keep selling"],"Emergencies require immediate action.")
H('233.d.3.B',4,"After an incident in the store, the employee should:",
  "complete an accident report",["delete records","blame the customer","avoid the manager"],"Reporting records what happened.")
H('233.d.4.A',3,"A practicum student arrives on time, completes tasks, and offers help. She shows a:",
  "positive work ethic",["bad habit","shortcut","delay"],"Reliability reflects work ethic.")
H('233.d.4.A',4,"Which behavior shows a productive work ethic during sale days?",
  "Staying organized and finishing duties without reminders",["Waiting to be told","Taking long breaks","Leaving a mess"],"Self-direction is valued.")
H('233.d.4.B',3,"A student keeps a customer's personal information private. This is:",
  "ethical conduct",["gossip","carelessness","competition"],"Privacy is an ethical duty.")
H('233.d.4.B',4,"A coworker asks to see a customer's address on file for personal reasons. The student should:",
  "decline politely",["share it","post it","write it down"],"Customer data is confidential.")
H('233.d.4.C',3,"A store advertises only the sale terms that are true. This is:",
  "ethical promotion",["deception","careless writing","hidden fees"],"Honest ads are ethical.")
H('233.d.4.C',4,"A sale sign says 'Up to 50% off' but only one item is half price. The ethical fix is to:",
  "clarify that only select items are 50% off",["leave the sign","raise the price","hide the sign"],"Clarity avoids deception.")
H('233.d.4.D',3,"Following store rules, laws, and policies should be:",
  "consistent",["optional","occasional","ignored"],"Compliance is ongoing.")
H('233.d.4.D',4,"Which is an example of complying with employment laws in a store?",
  "Recording hours worked accurately",["Skipping breaks","Working off the clock secretly","Falsifying time cards"],"Accurate records follow labor laws.")
H('233.d.5.A',3,"A practicum student works in a store and logs what she learns each week. She is:",
  "documenting learning activities",["hiding work","skipping tasks","avoiding feedback"],"Documentation shows progress.")
H('233.d.5.A',4,"Why does the supervisor review a student's practicum log?",
  "To evaluate learning and give feedback",["To punish","To waste time","To avoid training"],"Review supports growth.")
H('233.d.5.B',3,"A student prepares a plan for next season's prices, sales, and inventory. She is composing a:",
  "scenario plan",["receipt","press release","patterns book"],"Scenario plans project outcomes.")
H('233.d.5.B',4,"Why include several scenarios, such as best-case and worst-case sales, in a plan?",
  "To prepare for different outcomes",["To confuse the team","To raise costs","To avoid planning"],"Multiple scenarios support flexible decisions.")
H('233.d.5.C',3,"A practicum student helps plan a trunk show, choosing the date, guest list, and budget. She is:",
  "planning a special event",["sewing a gown","dyeing fabric","closing a store"],"Event planning organizes details.")
H('233.d.5.C',4,"Which step helps ensure a store event is successful?",
  "Setting goals and assigning responsibilities",["Skipping a budget","Waiting until the day before","Not telling customers"],"Goals and roles guide success.")
H('233.d.5.D',3,"A student arranges mannequins using balance, emphasis, and color harmony. She is creating displays using:",
  "the principles of design",["random choices","accounting rules","shipping rules"],"Design principles guide displays.")
H('233.d.5.D',4,"A display looks cluttered. Which design principle should she apply?",
  "Simplicity with a clear focal point",["More items everywhere","Darker lighting only","Smaller signs only"],"Focus and simplicity improve displays.")
H('233.d.5.E',3,"A student writes a buying plan listing the items, quantities, and budget for next month. She is implementing aspects of the:",
  "fashion buying process",["tailoring process","cleaning process","dyeing process"],"A buying plan is part of the process.")
H('233.d.5.E',4,"What should a buying plan consider before choosing quantities?",
  "Past sales and expected demand",["The mannequin's size","The sign's color","The entrance lights"],"Demand drives quantity.")
H('233.d.5.F',3,"A student now processes returns in half the time she used to. This shows:",
  "growth of technical skills",["no change","decline","lost skill"],"Speed and accuracy show growth.")
H('233.d.5.F',4,"Which evidence best shows growth in retail skills?",
  "Fewer register errors over the semester",["More mistakes","Skipped tasks","Late arrivals"],"Fewer errors show progress.")
H('233.d.5.G',3,"A student lists the retail tasks she does well and those she needs to practice. She is evaluating her:",
  "strengths and weaknesses",["salary","address","hobbies"],"Self-evaluation guides improvement.")
H('233.d.5.G',4,"Why evaluate your weaknesses during a practicum?",
  "To plan targeted improvement",["To feel discouraged","To avoid work","To hide problems"],"Knowing weak points helps you improve.")
H('233.d.5.H',3,"Photos of displays she created, her buying plan, and supervisor comments are:",
  "representative work samples",["junk","blank pages","old bills"],"Samples show real skills.")
H('233.d.5.H',4,"Which item is the strongest work sample for a fashion marketing portfolio?",
  "A photo of a finished window display with a short explanation",["A blank poster","A receipt only","A broken prop"],"Finished work with explanation shows skill.")

# ---------- 234 Advanced Graphic Design and Illustration ----------
H('234.d.4',3,"A designer uses vector software, a drawing tablet, and cloud storage for client projects. These are:",
  "advanced technology applications",["hand tools only","paper stocks","plain pencils"],"Digital tools support design.")
H('234.d.4',4,"A designer shares a layout through a cloud folder so a client can comment. This technology mainly supports:",
  "collaboration",["printing ink","fabric dyeing","audio mixing"],"Cloud tools enable review.")
H('234.d.5',3,"Understanding how grids, layers, and color modes work helps a designer:",
  "build and edit designs correctly",["avoid clients","reduce screen size","stop using software"],"System knowledge supports clean work.")
H('234.d.5',4,"A designer works in CMYK for print projects and RGB for screens. This shows understanding of:",
  "design systems",["tax systems","music systems","filing systems"],"Color systems differ by output.")
H('234.d.6',3,"Using strong passwords and not sharing client files publicly are examples of:",
  "cyber safety procedures",["print rules","font rules","grid rules"],"Cyber safety protects data.")
H('234.d.6',4,"A designer receives an email with an unknown attachment. Which action follows cyber safety?",
  "Do not open it and report it",["Open it quickly","Forward it","Click the link"],"Unknown attachments can contain malware.")
H('234.d.9',3,"Breaking a logo project into research, sketches, drafts, and revisions with due dates is:",
  "planning and time management",["procrastination","guessing","avoidance"],"Planning ensures deadlines are met.")
H('234.d.9',4,"Which method best helps a designer meet a client deadline?",
  "Set milestones and check progress each day",["Wait until the final day","Skip planning","Work without a schedule"],"Milestones keep work on track.")
H('234.d.1.A',3,"A designer writes a clear proposal and proofreads the copy on a poster. She is applying:",
  "English language arts skills",["welding","gym skills","cooking"],"Writing skills matter in design.")
H('234.d.1.A',4,"Which task uses English language arts skills in graphic design?",
  "Writing accurate headlines and correcting spelling in a layout",["Choosing a printer","Mixing paint","Cutting paper"],"Text accuracy is part of design.")
H('234.d.1.B',3,"A banner is 4 feet tall and 10 feet wide. What is its area?",
  "40 square feet",["14 square feet","28 square feet","80 square feet"],"4 x 10 = 40.")
H('234.d.1.B',4,"A design is scaled down to 25% of its original width of 20 inches. What is the new width?",
  "5 inches",["25 inches","10 inches","2 inches"],"20 x 0.25 = 5.")
H('234.d.2.A',3,"A designer uses formal language in a client proposal and casual language in a team chat. She is adapting:",
  "style for audience and situation",["her font size","her file names","her canvas size"],"Style matches the audience.")
H('234.d.2.A',4,"Which opening best fits a formal design proposal?",
  "Thank you for the opportunity to propose a brand identity for your company.",["Hey, got a logo idea!","Yo, here's my stuff.","Check it out lol."],"Formal tone fits clients.")
H('234.d.2.B',3,"Writing a creative brief with goals, audience, and deadlines in order is:",
  "organizing information",["erasing details","guessing","hiding details"],"Organized details prevent mistakes.")
H('234.d.2.B',4,"Which creative brief is best organized?",
  "One with goals, audience, tone, deliverables, and deadline in labeled sections",["A single paragraph","A random list","A blank page"],"Labeled sections make briefs clear.")
H('234.d.2.C',3,"A designer reads website analytics and tells the client which banner got more clicks. She is:",
  "interpreting and communicating information",["ignoring results","hiding data","guessing"],"Reporting results informs decisions.")
H('234.d.2.C',4,"Which statement communicates test results clearly?",
  "Version B received 320 clicks compared with 210 for Version A.",["B did better.","People liked it.","It performed fine."],"Specific numbers help.")
H('234.d.2.D',3,"A student presents a logo concept to the class with slides and explains her choices. This is a:",
  "formal presentation",["private diary","password","receipt"],"Planned slides are formal.")
H('234.d.2.D',4,"Showing a sketch to a coworker and asking for quick input is:",
  "an informal presentation",["a formal keynote","a legal brief","a financial report"],"Casual sharing is informal.")
H('234.d.2.E',3,"A client describes the feeling she wants. The designer takes notes and asks follow-up questions. This is:",
  "active listening",["interrupting","daydreaming","ignoring"],"Questions confirm understanding.")
H('234.d.2.E',4,"A client says the logo needs to 'pop.' The designer should:",
  "ask what pop means to her, such as color or contrast",["guess","ignore it","change everything"],"Clarify vague feedback.")
H('234.d.2.F',3,"A design team includes members from many cultures. A good teammate will:",
  "listen to and speak with each person respectfully",["ignore some ideas","use stereotypes","interrupt often"],"Respect improves teamwork.")
H('234.d.2.F',4,"Designing a poster for an international audience should include:",
  "images and symbols that are respectful across cultures",["slang only","symbols that offend","one culture's jokes"],"Cultural awareness avoids mistakes.")
H('234.d.2.G',3,"A studio responds to a client's concern quickly and politely. This builds:",
  "customer relations",["tension","delay","mistrust"],"Prompt courtesy builds trust.")
H('234.d.2.G',4,"A designer posts a portfolio and thanks clients publicly. This supports:",
  "public relations",["errors","delays","clutter"],"PR builds reputation.")
H('234.d.3.A',3,"A designer collects reviews and survey data before choosing a color scheme. This is:",
  "critical thinking with data",["guessing","luck","ignoring data"],"Data gathering supports decisions.")
H('234.d.3.A',4,"A banner is unreadable from far away. Critical thinking suggests she:",
  "test larger text, higher contrast, and simpler layout",["blame the viewer","shrink the text","remove the banner"],"Test variables to solve problems.")
H('234.d.3.B',3,"Three designers disagree about a layout. A good approach is to:",
  "discuss ideas, test options, and decide together",["let one dictate","avoid discussion","flip a coin"],"Group decision making uses communication.")
H('234.d.3.B',4,"Which phrase helps a team solve a design problem?",
  "Let's try each option against the project goal.",["That's silly.","I won't change it.","You're wrong."],"Goal-focused talk helps.")
H('234.d.7.A',3,"A lead designer sets goals, assigns tasks, and tracks progress. She is showing:",
  "leadership",["avoidance","laziness","carelessness"],"Leaders guide teams.")
H('234.d.7.A',4,"When a client changes the direction mid-project, a good leader will:",
  "analyze the impact and revise the plan with the team",["ignore the client","blame the team","stop working"],"Leaders adapt.")
H('234.d.7.B',3,"Two designers disagree on a font. A teammate proposes testing both. This is:",
  "conflict management",["avoidance","blame","competition"],"Testing resolves disagreements.")
H('234.d.7.B',4,"Which statement supports teamwork?",
  "Let's see which option serves the audience best.",["It's my way.","I won't help.","That's your problem."],"Audience-focused language supports teams.")
H('234.d.7.C',3,"Thanking a coworker for staying late builds:",
  "good working relationships",["tension","resentment","distance"],"Appreciation builds trust.")
H('234.d.7.C',4,"Which feedback is constructive on a poster draft?",
  "The color palette is strong; increase the text contrast.",["It's bad.","Never mind.","You can't design."],"Specific, kind feedback helps.")
H('234.d.7.D',3,"A lead sends an agenda with goals before a design review. She is:",
  "preparing for the meeting",["skipping the meeting","wasting time","avoiding work"],"An agenda focuses a meeting.")
H('234.d.7.D',4,"Which goal fits a design review meeting?",
  "Decide which concept moves forward and assign revisions",["Tell jokes","Talk about the weather","Discuss lunch"],"Meeting goals should advance the work.")
H('234.d.7.E',3,"During a design review, a good participant will:",
  "stay on topic and give useful feedback",["scroll a phone","interrupt","leave early"],"Focus improves the outcome.")
H('234.d.7.E',4,"After a review, which step keeps work moving?",
  "Send notes with assigned revisions and dates",["Say nothing","Delete the notes","Wait a month"],"Follow-up creates accountability.")
H('234.d.7.F',3,"A senior illustrator teaches a new designer how to use layers efficiently. This is:",
  "mentoring",["competing","hiding","copying"],"Mentors teach and inspire.")
H('234.d.7.F',4,"A good design mentor:",
  "gives patient, specific guidance",["keeps secrets","criticizes harshly","avoids questions"],"Patience builds skill.")
H('234.d.8.A',3,"A designer keeps a client's unreleased logo private until launch. This shows:",
  "ethical conduct",["carelessness","gossip","greed"],"Confidentiality is ethical.")
H('234.d.8.A',4,"A designer is asked to copy a competitor's logo. The ethical response is to:",
  "decline and propose an original design",["copy it","change one color","hide the source"],"Originality is ethical.")
H('234.d.8.B',3,"A designer wants to use a photograph found online in a client ad. First she must check:",
  "its copyright and license",["its file name","its caption color","its pixel color"],"Licenses decide permitted use.")
H('234.d.8.B',4,"Fair use may allow:",
  "limited use for purposes such as education or commentary",["unlimited commercial use","selling copies","claiming authorship"],"Fair use is limited.")
H('234.d.8.C',3,"A designer morphs a stock image into a new illustration and uses only licensed images. This shows:",
  "respect for intellectual property",["disrespect","carelessness","theft"],"Licensed use respects creators.")
H('234.d.8.C',4,"Tracing someone else's illustration and calling it yours:",
  "violates intellectual property rights",["is allowed","is original work","is fair use"],"Tracing copies another's expression.")
H('234.d.8.D',3,"A school's acceptable use policy forbids installing unlicensed software. A student should:",
  "follow the policy",["install anyway","hide it","ask a friend"],"Policies protect shared systems.")
H('234.d.8.D',4,"Which is good etiquette in a shared design lab?",
  "Save files to your folder and log out when finished",["Leave files on the desktop","Use others' accounts","Change everyone's settings"],"Courtesy keeps the lab ready.")
H('234.d.8.E',3,"Ads that influence what people buy and think show the impact of:",
  "advertising and visual communication on society",["tax law","sewing","cooking"],"Visual media shapes culture.")
H('234.d.8.E',4,"A responsible designer considers how an ad may affect:",
  "audiences and communities",["only profits","only competitors","nothing"],"Ads influence people and society.")
H('234.d.10.A',3,"A designer explains why she chose a blue palette for a bank logo, citing trust and stability. She is:",
  "justifying a design decision",["hiding choices","guessing","copying"],"Rationale supports choices.")
H('234.d.10.A',4,"Evaluating a design decision means judging it against the project's:",
  "goals and audience",["price tag","paper type","file name"],"Goals and audience are the measure.")
H('234.d.10.B',3,"Peers review a poster and write comments on what works and what needs change. This is a:",
  "written critique",["tax form","receipt","press release"],"Critiques give feedback.")
H('234.d.10.B',4,"A useful critique is:",
  "specific and respectful",["vague and harsh","rude","absent"],"Good critiques help improvement.")
H('234.d.10.C',3,"Line, shape, color, texture, balance, and contrast are art:",
  "elements and principles",["taxes","routes","files"],"They are the building blocks of design.")
H('234.d.10.C',4,"Repeating a shape across a poster to unify it applies:",
  "repetition",["noise","delay","clutter"],"Repetition creates unity.")
H('234.d.11.A',3,"Creating a poster for a school concert is designing for a:",
  "defined application",["random use","no use","hidden use"],"Designs serve specific purposes.")
H('234.d.11.A',4,"A designer asks for the poster's size, audience, and message before starting. This helps define:",
  "the application",["the lunch menu","the bus route","the paycheck"],"Requirements define the application.")
H('234.d.11.B',3,"Line, shape, color, and texture are elements of:",
  "design",["accounting","grammar","geography"],"Elements are the visual building blocks.")
H('234.d.11.B',4,"Varying stroke thickness to show emphasis versus detail uses which design element?",
  "line",["texture only","sound","motion"],"Line weight creates hierarchy.")
H('234.d.11.C',3,"Choosing a readable font and balanced layout applies design principles and:",
  "typography",["geometry","chemistry","geography"],"Typography is the art of type.")
H('234.d.11.C',4,"For a long paragraph on a brochure, which font choice is most readable?",
  "A clear serif or sans-serif at a comfortable size",["A decorative script at 8 pt","All capital letters in a thin font","Very condensed type"],"Readable text improves communication.")
H('234.d.11.D',3,"Arranging text and images so the eye moves through the page is:",
  "composition",["compression","corrosion","collection"],"Composition guides viewers.")
H('234.d.11.D',4,"Placing key information near the top left on a Western-language page uses composition that:",
  "follows natural reading patterns",["hides information","confuses readers","avoids hierarchy"],"Layout follows reading flow.")
H('234.d.11.E',3,"Drawing a character with correct body proportions is:",
  "anatomically appropriate figure drawing",["abstract doodling","traffic sign design","logo hunting"],"Anatomy guides realistic figures.")
H('234.d.11.E',4,"In many figure drawings, an adult's height is about how many head-lengths?",
  "Seven to eight",["Two","Fifteen","One"],"Seven to eight heads is a common guideline.")
H('234.d.11.F',3,"Drawing objects smaller as they get farther away uses:",
  "perspective",["texture","contrast","rhythm"],"Perspective creates depth.")
H('234.d.11.F',4,"In one-point perspective, lines that go away from the viewer meet at a:",
  "vanishing point",["pixel","crop mark","gutter"],"Lines converge at the vanishing point.")
H('234.d.11.G',3,"Choosing bright, contrasting hues so a sign is seen from far away is a decision about:",
  "color",["fonts","papers","glues"],"Color affects readability and impact.")
H('234.d.11.G',4,"Black text on a dark navy background will likely have poor:",
  "contrast",["resolution","alignment","bleed"],"Low contrast hurts readability.")
H('234.d.11.H',3,"Designing a poster with bleed, crop marks, and CMYK colors applies:",
  "printing concepts",["video editing","audio mixing","sewing"],"Print production needs special setup.")
H('234.d.11.H',4,"Why include bleed on a print file?",
  "To avoid white edges after trimming",["To add color","To save ink","To shrink the file"],"Bleed extends art past the trim.")

# ---------- 235 Practicum in Graphic Design and Illustration ----------
H('235.d.2',3,"A practicum student whose logo looks muddy when printed small tests simplified shapes and thicker lines. This is:",
  "problem solving",["panic","avoidance","guessing"],"Testing solutions is problem solving.")
H('235.d.2',4,"A design keeps failing client approval. A strong problem-solving step is to:",
  "review the brief and ask the client what is missing",["resubmit unchanged","drop the project","blame the client"],"Understanding the gap leads to a fix.")
H('235.d.3',3,"A practicum student keeps cords tidy and uses ergonomic seating at the computer. These show:",
  "safe work techniques",["style rules","tax steps","menu items"],"Safe habits prevent injuries.")
H('235.d.3',4,"Which action helps prevent eye strain during long design sessions?",
  "Take regular screen breaks and adjust lighting",["Stare without breaks","Dim the room fully","Increase brightness only"],"Breaks protect eyes.")
H('235.d.1.A',3,"A student explains her design to a client with clear words and open body language. This is:",
  "verbal and non-verbal communication",["silent work","avoidance","guessing"],"Words and body language work together.")
H('235.d.1.A',4,"Which action shows effective communication during a client call?",
  "Speaking clearly and confirming the next steps",["Mumbling","Interrupting","Ending the call suddenly"],"Clarity and follow-up help.")
H('235.d.1.B',3,"A student reads survey results about logo options and tells the client what viewers preferred. She is:",
  "interpreting and communicating information",["ignoring results","guessing","hiding results"],"Reporting findings informs choices.")
H('235.d.1.B',4,"Which statement best reports survey results?",
  "Sixty percent of respondents preferred the blue logo.",["It seemed popular.","People liked one.","Some chose something."],"Specific data is clear.")
H('235.d.1.C',3,"A client gives feedback on a layout. The student takes notes and repeats the key requests. This is:",
  "active listening",["interrupting","ignoring","daydreaming"],"Repeating confirms understanding.")
H('235.d.1.C',4,"What should a designer do if feedback is unclear?",
  "Ask for examples or specifics",["Guess","Ignore it","Change everything"],"Specifics prevent misunderstanding.")
H('235.d.1.D',3,"A studio sends a quick, polite follow-up after delivering a project. This builds:",
  "customer relations",["tension","delay","mistrust"],"Follow-up shows care.")
H('235.d.1.D',4,"A client is unhappy with a draft. A good PR response is to:",
  "listen, acknowledge, and offer revisions",["argue","ignore","blame"],"Calm responses retain clients.")
H('235.d.4.A',3,"A practicum student arrives on time and meets deadlines. She shows a:",
  "positive work ethic",["bad habit","shortcut","delay"],"Reliability reflects work ethic.")
H('235.d.4.A',4,"Which behavior shows a productive work ethic during revisions?",
  "Completing changes promptly and checking them for errors",["Waiting for reminders","Rushing without checking","Leaving tasks unfinished"],"Prompt, careful work is valued.")
H('235.d.4.B',3,"Using only licensed fonts and software on client projects shows safe, responsible, and legal use of:",
  "technology",["paper","ink","glue"],"Legal use avoids penalties.")
H('235.d.4.B',4,"A student is offered a cracked copy of design software. The responsible choice is to:",
  "decline and use licensed software",["accept it","share it","install it on every machine"],"Cracked software is illegal.")
H('235.d.4.C',3,"Keeping a client's logo files private until launch is:",
  "ethical conduct",["gossip","carelessness","competition"],"Confidentiality is ethical.")
H('235.d.4.C',4,"A friend asks to see a client's unreleased packaging design. The student should:",
  "politely decline",["show it","post it","send a photo"],"Client work is confidential.")
H('235.d.4.D',3,"A designer buys a stock photograph license before using it in a brochure. She is applying:",
  "copyright law",["traffic law","safety law","tax law"],"Licensing follows copyright.")
H('235.d.4.D',4,"Which action is allowed under fair use?",
  "Quoting a small excerpt with credit for a school critique",["Copying a whole book to sell","Posting a full movie","Claiming someone's art as yours"],"Limited educational use may be fair.")
H('235.d.4.E',3,"A designer creates a collage from her own photos and properly licensed textures. This shows respect for:",
  "intellectual property",["disrespect","theft","carelessness"],"Licensed or original materials are safe.")
H('235.d.4.E',4,"Altering a photograph taken by someone else and publishing it without permission:",
  "still infringes the owner's rights",["is allowed","creates your own copyright","is fair use"],"Altering does not remove ownership.")
H('235.d.4.F',3,"A lab's acceptable use policy forbids personal downloads. A student should:",
  "follow the policy",["download anyway","hide it","ask a friend"],"Policies protect shared systems.")
H('235.d.4.F',4,"Which is good etiquette for a shared plotter or large-format printer?",
  "Clean up scraps and report problems to the instructor",["Leave jams","Print without asking","Hide errors"],"Courtesy keeps equipment working.")
H('235.d.4.G',3,"Following studio rules, laws, and regulations should be:",
  "consistent",["optional","occasional","ignored"],"Compliance is ongoing.")
H('235.d.4.G',4,"Which shows compliance in a design business?",
  "Using signed contracts and invoices with clients",["Working without agreements","Skipping records","Hiding income"],"Contracts and records follow regulations.")
H('235.d.5.A',3,"A practicum student works with a design mentor and logs her weekly learning. She is:",
  "documenting learning activities",["hiding work","skipping tasks","avoiding feedback"],"Logs show growth.")
H('235.d.5.A',4,"Why does the mentor review the student's log?",
  "To evaluate progress and guide improvement",["To punish","To waste time","To avoid training"],"Review supports learning.")
H('235.d.5.B',3,"A student explains why she chose a hand-lettered title for a poster, citing the event's friendly tone. She is:",
  "justifying a design decision",["hiding her choice","guessing","copying"],"Rationale supports choices.")
H('235.d.5.B',4,"Which question helps evaluate a design decision?",
  "Does the choice serve the goal and the audience?",["Is the file large?","Is the date recent?","Is the name long?"],"Goals and audience judge decisions.")
H('235.d.5.C',3,"A student uses contrast, emphasis, and repetition throughout a brochure. She is applying:",
  "art elements and principles",["tax rules","filing rules","shipping rules"],"Principles guide design.")
H('235.d.5.C',4,"Using a larger, bolder headline to guide the reader's eye uses:",
  "hierarchy",["noise","clutter","lag"],"Hierarchy directs reading order.")
H('235.d.5.D',3,"Researching, sketching, drafting, revising, and finalizing a design is a creative:",
  "design process",["tax process","lunch process","filing process"],"The process produces quality work.")
H('235.d.5.D',4,"Which step comes right after sketching rough ideas?",
  "Choosing a concept to develop into a draft",["Printing the final","Billing the client","Archiving"],"Concept selection follows ideation.")
H('235.d.5.E',3,"A student creates a layout in half the time it took her at the start. This shows:",
  "growth of technical skills",["no change","decline","lost skill"],"Speed with quality shows growth.")
H('235.d.5.E',4,"Which evidence best shows skill growth?",
  "Comparing early and recent projects",["Ignoring early work","Skipping reviews","Deleting files"],"Comparison shows progress.")
H('235.d.5.F',3,"A student lists the tools she handles well and those she needs to practice. She is evaluating her:",
  "strengths and weaknesses",["salary","address","hobbies"],"Self-evaluation guides practice.")
H('235.d.5.F',4,"Why evaluate your proficiency?",
  "To set goals for improvement",["To get discouraged","To avoid work","To hide problems"],"Honest evaluation drives growth.")
H('235.d.5.G',3,"Saving finished posters, a brand kit, and mentor comments is collecting:",
  "representative work samples",["junk files","blank pages","old bills"],"Samples demonstrate ability.")
H('235.d.5.G',4,"Which item is a strong work sample for a graphic design portfolio?",
  "A finished brand identity with logo, colors, and mockups",["A blank page","A rough scribble","A damaged file"],"Complete, polished work shows skill.")

H('234.d.7.B',5,"A freelance illustrator and a client disagree on revision limits. Which step best resolves the conflict while preserving the relationship?",
  "Review the signed contract together and negotiate a fair adjustment",["Stop replying to emails","Post complaints online","Deliver nothing further"],"Contracts and calm negotiation settle disputes.")
H('234.d.8.B',5,"A studio wants to use a song clip in a promotional video. Which step is needed before publishing?",
  "Obtain a license or permission from the rights holder",["Shorten the clip to ten seconds","Lower the volume","Credit the band in the caption only"],"Short clips and credits do not replace permission.")
H('234.d.11.B',5,"A designer adds rough paper grain to a flat poster background to make it feel handmade. Which design element is being added?",
  "Texture",["Shape","Space","Value"],"Texture is the surface quality of a design.")
H('235.d.5.A',5,"A mentor asks a practicum student to record each task, the tool used, and what was learned. This record mainly shows:",
  "evidence of learning activities over time",["a list of friends","unrelated chores","the mentor's schedule"],"Detailed logs document learning.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_39.jsonl'))

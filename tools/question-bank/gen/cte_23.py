import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('127.', 1100, own='cte_23.jsonl')
def H(code, d, q, right, wrong, e):
    return B.hand(code, d, q, right, wrong, e)

# ---------- 127.153 Interior Design (housing, furnishings, equipment) ----------
H('153.d.1.A',3,"Color, line, shape, and texture are among the:",
  "Elements of design",["Building codes","Safety rules","Sales tactics"],"Elements are the building blocks of a room.")
H('153.d.1.A',4,"Which is a principle of design rather than an element?",
  "Balance",["Color","Line","Texture"],"Balance, rhythm, emphasis, proportion, and harmony are principles.")
H('153.d.1.B',3,"Using dark, warm colors on all walls of a small room usually makes it feel:",
  "Smaller and cozier",["Much larger","Colder","Outdoors"],"Dark warm colors advance.")
H('153.d.1.B',4,"Tall vertical lines in a room, such as striped drapes, create the effect of:",
  "Greater height",["Greater width","Less light","More noise"],"Vertical lines draw the eye upward.")
H('153.d.1.C',3,"To coordinate furnishings in a living room, a designer repeats a color or pattern to create:",
  "Unity and harmony",["Clutter","Conflict","Randomness"],"Repetition ties a room together.")
H('153.d.1.C',4,"A sofa, chair, and rug all share a blue accent so the room feels connected. This uses the principle of:",
  "Rhythm through repetition",["Contrast through opposites","Isolation","Subtraction"],"Repeating a color creates rhythm.")
H('153.d.1.D',3,"Which factor most directly shapes how a family wants its home designed?",
  "Cultural traditions and lifestyle",["The color of the car","The weather forecast","The brand of a pen"],"Culture influences design preferences.")
H('153.d.1.D',4,"Open floor plans became popular largely because families wanted more:",
  "Casual, shared living space",["Closed formal rooms","Dark hallways","Smaller windows"],"Social trends drive layout.")
H('153.d.2.A',3,"When choosing a sofa fabric for a home with young children, the best quality to compare is:",
  "Durability and stain resistance",["Rarity of the dye","Brand of the loom","Weight of the box"],"Fabric must handle wear.")
H('153.d.2.A',4,"Tight, even stitching and a hardwood frame are signs of good:",
  "Workmanship",["Packaging","Advertising","Shipping"],"Construction quality shows in joinery and stitching.")
H('153.d.2.B',3,"Solid wood, veneer, and laminate are different kinds of:",
  "Furniture surface materials",["Light bulbs","Window shades","Paint rollers"],"Materials vary in cost and durability.")
H('153.d.2.B',4,"A piece with a thin wood layer glued over a core of another material uses:",
  "Veneer",["Solid wood","Laminate plastic only","Metal plating"],"Veneer is a thin real wood layer.")
H('153.d.2.C',3,"Fabric care labels on upholstery use codes like W or S to tell you:",
  "How the fabric should be cleaned",["Where it was shipped","Who sold it","Its price"],"Codes give cleaning method.")
H('153.d.2.C',4,"An upholstery code of S means the fabric should be cleaned with:",
  "A water-free solvent only",["Plain water only","Bleach","Steam only"],"S means solvent only.")
H('153.d.2.D',3,"Before using a new appliance, the owner should read the:",
  "Use and care manual",["Receipt only","Advertisement","Box color"],"Manuals explain safe use and upkeep.")
H('153.d.2.D',4,"A manual's warranty section tells you:",
  "What repairs the maker will cover and for how long",["How to paint the item","Where to hang it","Its popularity"],"Warranties limit coverage.")
H('153.d.2.E',3,"A wood table should be dusted with a soft cloth because rough rags can:",
  "Scratch the finish",["Add color","Warp the legs","Soften the top"],"Finish care.")
H('153.d.2.E',4,"For proper care, a leather chair should be kept away from direct sunlight because sun can:",
  "Fade and dry the leather",["Make it wet","Make it heavier","Add shine"],"Sun damages leather.")
H('153.d.3.A',3,"A room with clean lines, little ornament, and neutral colors is most likely in a:",
  "Contemporary style",["Victorian style","Rococo style","Baroque style"],"Contemporary favors simplicity.")
H('153.d.3.A',4,"Heavy carved wood, rich fabrics, and ornate detail are typical of:",
  "Traditional style",["Minimalist style","Industrial style","Scandinavian style"],"Traditional is ornate.")
H('153.d.3.B',3,"Task lighting, such as a reading lamp, is placed to:",
  "Provide light for a specific activity",["Hide the room","Reduce light","Warm the floor"],"Task lighting supports tasks.")
H('153.d.3.B',4,"A designer adds a mirror across from a window to:",
  "Reflect light and make the room feel larger",["Block daylight","Add noise","Reduce ceiling height"],"Mirrors bounce light.")
H('153.d.3.C',3,"A sustainable interior material is one that:",
  "Is renewable or has low environmental impact",["Is rare and imported","Cannot be recycled","Is made with toxic glue"],"Eco-friendly choices.")
H('153.d.3.C',4,"Bamboo flooring is often promoted as eco-friendly because it:",
  "Grows back quickly",["Takes decades to regrow","Is made of plastic","Cannot be harvested"],"Bamboo is rapidly renewable.")
H('153.d.3.D',3,"For a window that needs privacy but should still let in light, a good choice is:",
  "Sheer curtains or light-filtering shades",["Solid steel shutters","A painted-over pane","Brick"],"Filtering shades balance both.")
H('153.d.3.D',4,"Window treatments hung from a rod close to the ceiling make the window look:",
  "Taller",["Shorter","Narrower","Darker"],"Mounting high lengthens the window.")
H('153.d.3.E',3,"When accessorizing a room on a tight budget, a designer should first set:",
  "A spending limit",["A sale date","A color wheel","A guest list"],"Budget first.")
H('153.d.3.E',4,"A cost-saving way to accessorize is to:",
  "Reuse and rearrange items the client already owns",["Buy the most expensive item","Replace every item","Skip all accessories"],"Reuse saves money.")
H('153.d.3.F',3,"Paint, wallpaper, and paneling are examples of:",
  "Wall treatments",["Floor coverings","Light fixtures","Window hardware"],"Wall treatment types.")
H('153.d.3.F',4,"A semi-gloss paint is often chosen for kitchens and baths because it is:",
  "Easier to clean and moisture resistant",["Rougher","Harder to wipe","Always cheapest"],"Higher sheen washes well.")
H('153.d.3.G',3,"Hardwood, tile, and carpet are types of:",
  "Flooring",["Wall paint","Ceiling fans","Shelving"],"Flooring options.")
H('153.d.3.G',4,"Ceramic tile is a good floor choice for a bathroom because it is:",
  "Water resistant",["Soaks up water","Flammable","Fragile to moisture"],"Tile resists moisture.")
H('153.d.4.A',3,"A sofa, a dining table, and a refrigerator are examples of:",
  "Furniture and equipment",["Accessories only","Wall treatments","Floor plans"],"Furnishings and equipment.")
H('153.d.4.A',4,"Equipment such as a dishwasher differs from furniture because it:",
  "Performs a function using power or plumbing",["Is always decorative","Cannot be moved","Has no cost"],"Equipment is functional.")
H('153.d.4.B',3,"A family with a toddler would most likely choose furniture that is:",
  "Durable with rounded edges",["Fragile with sharp corners","Glass and delicate","Very tall"],"Child safe choices.")
H('153.d.4.B',4,"A retired couple downsizing might prefer furniture that is:",
  "Comfortable, smaller, and easy to move",["Oversized and heavy","Tiny and fragile","Hard to enter"],"Needs change with life stage.")
H('153.d.4.C',3,"An important economic factor in choosing a dining set is:",
  "The total cost compared to the budget",["Its nickname","The store sign","The photo size"],"Cost matters.")
H('153.d.4.C',4,"Buying a quality sofa that lasts ten years can cost less over time than replacing a cheap one every:",
  "Two or three years",["Ten years","Twenty years","Fifty years"],"Cost per year.")
H('153.d.4.D',3,"Before placing furniture, a designer measures the room and draws a:",
  "Floor plan",["Menu","Resume","Logo"],"Floor plans guide layout.")
H('153.d.4.D',4,"To keep a traffic path through a room, a designer leaves about how much clear walkway?",
  "About 3 feet",["About 3 inches","About 30 feet","None"],"Walkways need space.")
H('153.d.4.E',3,"A client who uses a wheelchair needs furniture arranged to allow:",
  "Wide clear paths for turning",["Narrow gaps","Stacked boxes","Low light"],"Accessibility.")
H('153.d.4.E',4,"Adjustable-height desks and chairs accommodate:",
  "People of different heights and needs",["Only children","Only pets","Only one user"],"Flexible furniture.")
H('153.d.4.F',3,"Smart-home devices that dim lights by voice are an example of:",
  "Technology in furnishings",["A hand tool","A sewing pattern","A paint color"],"Tech trends.")
H('153.d.4.F',4,"A good way to research furnishing trends is to read:",
  "Trade magazines and industry reports",["Gossip","Lottery tickets","Weather maps"],"Reliable sources.")
H('153.d.5.A',3,"Using safety rules in a showroom workplace includes keeping aisles:",
  "Clear of boxes and cords",["Blocked","Dark","Wet"],"Safe aisles.")
H('153.d.5.A',4,"Lifting a heavy box of furnishings safely means bending the:",
  "Knees and keeping the back straight",["Back and keeping knees locked","Neck only","Elbows only"],"Safe lifting.")
H('153.d.5.B',3,"A frayed power cord on a floor lamp is a:",
  "Fire and shock hazard",["Design feature","Safety feature","Cleaning tool"],"Identify hazards.")
H('153.d.5.B',4,"A rug with curled edges in a hallway is a potential:",
  "Trip hazard",["Fire exit","Light source","Cooling vent"],"Falls.")
H('153.d.5.C',3,"Preventing accidents in a workshop includes wearing:",
  "Proper protective gear",["Loose scarves","Open sandals","Headphones at high volume"],"Prevention.")
H('153.d.5.C',4,"A good prevention habit is to store heavy items:",
  "On lower shelves",["On the top shelf","In walkways","On chairs"],"Store heavy low.")
H('153.d.5.D',3,"OSHA is a federal agency that sets rules for:",
  "Workplace safety and health",["Fashion trends","Movie ratings","Sports teams"],"OSHA basics.")
H('153.d.5.D',4,"Safety Data Sheets must be kept so workers can find information about:",
  "Hazardous chemicals",["Lunch menus","Paint colors","Sales goals"],"Right to know.")
H('153.d.5.E',3,"If a small fire starts in a stockroom, the first priority is to:",
  "Alert others and get to safety",["Take photos","Finish the sale","Move furniture"],"Emergency response.")
H('153.d.5.E',4,"The PASS method for using a fire extinguisher begins with:",
  "Pull the pin",["Pour water","Push the wall","Pick up the phone"],"PASS: Pull, Aim, Squeeze, Sweep.")
H('153.d.5.F',3,"A business protects the environment by recycling:",
  "Packaging and scrap materials",["Nothing","Only gold","Only food"],"Recycling.")
H('153.d.5.F',4,"Disposing of leftover stain and solvent properly means following:",
  "Local hazardous waste rules",["The cheapest option","Any drain","Burning it"],"Environmental responsibility.")
H('153.d.6.A',3,"A tool used to join furniture pieces with screws is a:",
  "Screwdriver or drill",["Tape measure only","Paint brush","Ruler"],"Construction tools.")
H('153.d.6.A',4,"A staple gun is commonly used to attach:",
  "Upholstery fabric to a frame",["Glass to metal","Pipes","Concrete"],"Upholstery tool.")
H('153.d.6.B',3,"Skillful tool care includes keeping cutting blades:",
  "Sharp and clean",["Dull and rusty","Wet","Bent"],"Tool maintenance.")
H('153.d.6.B',4,"Before using a power saw, a worker should check that the:",
  "Blade guard is in place",["Radio is on","Lunch is ready","Door is locked behind them"],"Safe use.")
H('153.d.6.C',3,"CNC routers that cut furniture parts from digital designs show the impact of:",
  "Automation technology",["Hand carving","Painting","Weaving"],"Technology impact.")
H('153.d.6.C',4,"Computer-aided cutting in furniture making mainly improves:",
  "Accuracy and speed",["Weight","Noise","Smell"],"CNC benefits.")
H('153.d.7.A',3,"Dovetail joints in a drawer are a sign of:",
  "Good workmanship",["Poor design","Cheap staples","Glue only"],"Joinery quality.")
H('153.d.7.A',4,"A drawer that glides smoothly and sits flush shows:",
  "Precise construction",["Careless sanding","Warped boards","Thin paint"],"Quality check.")
H('153.d.7.B',3,"Choosing a chair style that fits the room and is built to last combines design and:",
  "Construction knowledge",["Guessing","Advertising","Luck"],"Apply knowledge.")
H('153.d.7.B',4,"A designer specifies kiln-dried hardwood for a table to prevent:",
  "Warping and cracking",["Fading","Rusting","Echoes"],"Selection affects durability.")
H('153.d.7.C',3,"3D rendering software lets a designer show a client:",
  "A realistic view of a room before it is built",["Only sales figures","Only a paint can","A weather report"],"Technology use.")
H('153.d.7.C',4,"Using digital catalogs and CAD in design work helps by:",
  "Saving time and reducing errors",["Adding mistakes","Increasing cost only","Removing clients"],"Tech benefits.")
H('153.d.8.A',3,"A main goal of business promotion for a furniture store is to:",
  "Attract customers and increase sales",["Close the store","Hide products","Raise prices without notice"],"Promotion objectives.")
H('153.d.8.A',4,"A grand-opening sale is an example of a promotion that aims to:",
  "Draw first-time shoppers",["Reduce stock quality","Confuse buyers","Delay deliveries"],"Objective.")
H('153.d.8.B',3,"A model room set up in a showroom is an example of a:",
  "Display",["Receipt","Warranty","Invoice"],"Displays inspire buyers.")
H('153.d.8.B',4,"Placing a lamp and rug with a sofa in a display helps shoppers:",
  "Picture the pieces in their home",["Forget the price","Avoid buying","Leave quickly"],"Merchandising.")
H('153.d.8.C',3,"Social media posts, email, and websites are forms of:",
  "Advertising media",["Building codes","Safety signs","Floor tiles"],"Technology and media.")
H('153.d.8.C',4,"An advantage of online advertising for a small design firm is that it can:",
  "Reach many local people at low cost",["Never be changed","Require no message","Hide from buyers"],"Cost efficient.")
H('153.d.8.D',3,"A store in a beach community would likely promote:",
  "Outdoor and coastal furnishings",["Snow gear only","Winter coats only","Ski lodges"],"Promotion reflects environment.")
H('153.d.8.D',4,"A furniture ad in a city with many small apartments should highlight:",
  "Space-saving pieces",["Oversized sectionals","Ranch-sized tables","Barn furniture"],"Local needs.")
H('153.d.8.E',3,"A growing number of people working from home influences demand for:",
  "Home office furniture",["Fewer chairs","Fewer lamps","No desks"],"Societal trends.")
H('153.d.8.E',4,"As the population ages, businesses may expect more demand for:",
  "Accessible, comfortable furnishings",["Hard stools","Glass tables","Low ceilings"],"Demographics.")
H('153.d.9.A',3,"Good customer relations help a design business by creating:",
  "Repeat customers and referrals",["More complaints","Fewer sales","Longer lines"],"Customer importance.")
H('153.d.9.A',4,"Customer satisfaction builds trust, which can lead a client to:",
  "Recommend the business to friends",["Avoid the store","Return everything","Stop paying"],"Loyalty.")
H('153.d.9.B',3,"A designer maintains a good client relationship by returning calls:",
  "Promptly",["Never","Months later","Only when angry"],"Responsiveness.")
H('153.d.9.B',4,"Following up after a project is finished shows the client that you:",
  "Care about their satisfaction",["Forgot them","Want to avoid them","Are closing"],"Follow-up.")
H('153.d.9.C',3,"When a customer complains about a late delivery, a good first step is to:",
  "Listen calmly and apologize for the problem",["Argue","Hang up","Blame them"],"Resolve conflicts.")
H('153.d.9.C',4,"After listening to a complaint, the next step is to:",
  "Offer a reasonable solution",["Ignore it","Make excuses","Change the subject"],"Conflict resolution.")
H('153.d.10.A',3,"A professional email to a client should include:",
  "A clear subject and polite tone",["Slang only","All capital letters","No greeting"],"Written communication.")
H('153.d.10.A',4,"Eye contact and an open posture are examples of:",
  "Nonverbal communication",["Written communication","Electronic communication","Silent reading"],"Nonverbal.")
H('153.d.10.B',3,"When quitting a job properly, an employee should give:",
  "Proper notice in writing",["No notice","A rumor","A gift"],"Terminate employment.")
H('153.d.10.B',4,"A document that summarizes your education and experience for job applications is a:",
  "Resume",["Warranty","Receipt","Invoice"],"Secure employment.")
H('153.d.10.C',3,"A positive interpersonal skill at work is:",
  "Respecting coworkers' opinions",["Interrupting","Gossiping","Blaming"],"Interpersonal.")
H('153.d.10.C',4,"Resolving a disagreement with a coworker works best when you:",
  "Discuss the issue calmly and look for a compromise",["Yell","Ignore them forever","Spread rumors"],"Conflict resolution.")
H('153.d.10.D',3,"Good sleep and regular exercise contribute to:",
  "Better job performance",["Poor focus","Absences","Bad moods"],"Health and success.")
H('153.d.10.D',4,"Managing stress well helps a designer meet:",
  "Client deadlines",["No goals","Lunch","Parking spots"],"Mental health.")
H('153.d.10.E',3,"Appropriate workplace appearance in a design showroom means being:",
  "Neat and professional",["Unkempt","Careless","Sloppy"],"Grooming.")
H('153.d.10.E',4,"Clean, pressed clothing at a client meeting shows:",
  "Respect for the client and the business",["Disinterest","Laziness","Rudeness"],"Appearance.")
H('153.d.10.F',3,"Workplace etiquette includes being on time and:",
  "Using polite language",["Interrupting","Texting during meetings","Being loud"],"Etiquette.")
H('153.d.10.F',4,"At a business lunch with a client, good etiquette includes:",
  "Turning your phone off or silent",["Talking with food in your mouth","Arriving late","Ignoring the client"],"Business etiquette.")
H('153.d.10.G',3,"A productive work habit is to:",
  "Prioritize tasks and meet deadlines",["Delay everything","Skip details","Avoid asking questions"],"Productivity.")
H('153.d.10.G',4,"A positive attitude at work includes accepting feedback:",
  "Without becoming defensive",["By arguing","By quitting","By ignoring it"],"Attitude.")
H('153.d.10.H',3,"A project portfolio for interior design includes:",
  "Sketches, floor plans, and photos of completed work",["Receipts only","Recipes","Songs"],"Portfolio content.")
H('153.d.10.H',4,"A designer updates a portfolio by adding:",
  "New completed projects with descriptions",["Old receipts","Blank pages","Nothing"],"Maintain portfolio.")
H('153.d.11.A',3,"Entry-level interior design jobs often call for:",
  "A high school diploma plus training or certificate",["No qualifications","A medical degree","A law degree"],"Preparation.")
H('153.d.11.A',4,"A higher level of employment, such as a licensed designer, usually requires:",
  "A college degree and exam in many states",["No education","A driver's test only","A cooking class"],"Education levels.")
H('153.d.11.B',3,"A source of job outlook data for interior design is the:",
  "Bureau of Labor Statistics",["Weather channel","Sports page","Music chart"],"Outlook.")
H('153.d.11.B',4,"Demand for designers tends to rise when the economy and housing market are:",
  "Strong",["Collapsing","Frozen","Disappearing"],"Employment trends.")
H('153.d.11.C',3,"Starting your own design studio is an example of:",
  "Entrepreneurship",["Retirement","Inheritance","Volunteering"],"Entrepreneur.")
H('153.d.11.C',4,"A new design-studio owner must handle design work and also:",
  "Business tasks such as billing and marketing",["Only drawing","Nothing else","Only cleaning"],"Entrepreneurs run the whole business.")
H('153.d.11.D',3,"A person who enjoys working alone may prefer a career as a:",
  "Freelance designer",["Store greeter","Team manager only","Teacher"],"Personal fit.")
H('153.d.11.D',4,"Family responsibilities can affect a career choice by influencing:",
  "Hours and location a person can work",["Eye color","Shoe size","Birth date"],"Priorities.")
H('153.d.11.E',3,"A reward of being an interior designer is:",
  "Creative work and seeing finished results",["No clients","No deadlines","No decisions"],"Rewards.")
H('153.d.11.E',4,"A demand of the job is often:",
  "Tight deadlines and client changes",["Free time all day","No responsibility","No tasks"],"Demands.")
H('153.d.11.F',3,"Taking a course in new design software is an example of:",
  "Continuing education",["Vacation","Retirement","Shopping"],"Advancement.")
H('153.d.11.F',4,"Professional design associations help members by offering:",
  "Networking and training",["Free furniture","Tax cuts","Parking"],"Education.")
H('153.d.12.A',3,"An employer's right is to expect employees to:",
  "Follow company policies",["Ignore rules","Take supplies","Skip work"],"Rights and responsibilities.")
H('153.d.12.A',4,"An employee's right includes working in a:",
  "Safe environment",["Dangerous space","Unpaid shift","Locked room"],"Employee rights.")
H('153.d.12.B',3,"An ethical designer is honest about:",
  "Costs and materials",["Hiding fees","Fake reviews","False claims"],"Ethics.")
H('153.d.12.B',4,"Recommending a product only because it pays you a hidden commission is:",
  "Unethical",["Smart","Required","Legal advice"],"Conflict of interest.")
H('153.d.12.C',3,"Copyright law protects a designer's original:",
  "Drawings and designs",["Tools","Receipts","Uniform"],"Legal aspects.")
H('153.d.12.C',4,"A written contract between a designer and client helps by clearly stating:",
  "The scope of work and payment terms",["The weather","The designer's age","The client's hobbies"],"Contract.")

# ---------- 127.154 Interior Design practicum ----------
H('154.d.1.A',3,"In an interior design practicum, a student speaking with a client should:",
  "Use clear, consistent language and tone",["Mumble","Use only jargon","Avoid eye contact"],"Communication.")
H('154.d.1.A',4,"Matching your facial expression to your words is an example of consistent:",
  "Verbal and nonverbal communication",["Paperwork","Billing","Shipping"],"Consistency.")
H('154.d.1.B',3,"Active listening with a client includes:",
  "Asking follow-up questions",["Interrupting","Looking away","Checking your phone"],"Clarify information.")
H('154.d.1.B',4,"After a client describes their needs, you can confirm understanding by:",
  "Restating the main points",["Changing the subject","Ending the call","Ignoring details"],"Paraphrase.")
H('154.d.1.C',3,"A formal presentation to a client usually follows a:",
  "Planned structure with visuals",["Random order","Silent slide","Rumor"],"Presentations.")
H('154.d.1.C',4,"An informal presentation might be a quick:",
  "Desk review of a sample board with a coworker",["Board meeting","Public award show","Press conference"],"Informal.")
H('154.d.1.D',3,"Measuring a room and recording dimensions is an example of communicating:",
  "Technical data",["Gossip","Poetry","Slogans"],"Interpret data.")
H('154.d.1.D',4,"A chart comparing costs of three flooring options helps a client:",
  "Make an informed choice",["Avoid choosing","Ignore the price","Delay forever"],"Communicate data.")
H('154.d.1.E',3,"If a client looks confused during a presentation, the designer should:",
  "Pause and ask what is unclear",["Speak faster","Walk away","Ignore it"],"Read cues.")
H('154.d.1.E',4,"A client crossing arms and frowning might be signaling:",
  "Disagreement or discomfort",["Excitement","Agreement","Boredom with lunch"],"Interpret cues.")
H('154.d.2.A',3,"Using critical thinking on a project means:",
  "Analyzing options before deciding",["Guessing","Copying","Hurrying"],"Critical thinking.")
H('154.d.2.A',4,"A team that debates two layout plans using evidence is exercising:",
  "Collaborative critical thinking",["Luck","Avoidance","Delay"],"Team critical thinking.")
H('154.d.2.B',3,"A client's tiny room needs more storage. A creative solution is to:",
  "Use built-in or multi-purpose furniture",["Add more clutter","Remove all furniture","Paint the ceiling"],"Innovative solutions.")
H('154.d.2.B',4,"To break down a design problem, a designer first:",
  "Lists the client's needs and constraints",["Buys furniture","Paints walls","Orders carpet"],"Analyze problem.")
H('154.d.2.C',3,"Technical research for choosing flooring may include:",
  "Manufacturer specification sheets",["Rumors","Mood","Luck"],"Research.")
H('154.d.2.C',4,"To decide whether a fabric is flame-resistant, check the:",
  "Manufacturer's test data and labels",["Color","Price tag","Store sign"],"Reliable data.")
H('154.d.3.A',3,"Safety in an interior design studio includes keeping sample cords and tools:",
  "Organized and out of walkways",["Strewn on the floor","Plugged in always","Hidden in boxes"],"Studio safety.")
H('154.d.3.A',4,"Before handling unfamiliar finishing products, a designer reads the:",
  "Safety data sheet",["Price tag","Brochure","Color chart"],"Follow rules.")
H('154.d.3.B',3,"When moving heavy samples, the safest way is to:",
  "Lift with your legs or ask for help",["Jerk with your back","Throw them","Drag over feet"],"Safe procedures.")
H('154.d.3.B',4,"An emergency exit in a studio must remain:",
  "Unobstructed",["Locked","Blocked by boxes","Hidden"],"Procedures.")
H('154.d.3.C',3,"Skillful tool care includes returning tools to:",
  "Their proper storage places",["The floor","Another room","A friend's car"],"Tool care.")
H('154.d.3.C',4,"A dull utility knife is more dangerous than a sharp one because it:",
  "Requires more force and may slip",["Cuts better","Is lighter","Is safer"],"Skillful use.")
H('154.d.4.A',3,"A positive work ethic means performing assigned tasks:",
  "On time and with care",["Late","Carelessly","Never"],"Work ethic.")
H('154.d.4.A',4,"A student who volunteers to help organize the sample library shows:",
  "Initiative",["Laziness","Apathy","Disrespect"],"Initiative.")
H('154.d.4.B',3,"Ethical reasoning means asking whether a decision is:",
  "Honest and fair to everyone affected",["Easy only","Cheap only","Fast only"],"Ethical decisions.")
H('154.d.4.B',4,"A client asks you to claim an item is solid wood when it is veneer. You should:",
  "Refuse and state the truth",["Lie","Hide the label","Change the price"],"Honesty.")
H('154.d.4.C',3,"Ethical practice in the furnishing industry includes:",
  "Giving accurate product information",["Misleading ads","Hiding defects","Fake discounts"],"Industry ethics.")
H('154.d.4.C',4,"Crediting a manufacturer for its design in a presentation is:",
  "An ethical practice",["Required by paint","Illegal","Pointless"],"Credit.")
H('154.d.4.D',3,"Complying with building and safety codes means:",
  "Following them on every project",["Following them sometimes","Ignoring them","Avoiding inspections"],"Compliance.")
H('154.d.4.D',4,"If a selected sofa does not meet the fire code for a public space, the designer should:",
  "Choose a compliant alternative",["Ignore the code","Hide the label","Change the client's mind"],"Comply.")
H('154.d.5.A',3,"In a supervised internship, a student records:",
  "Tasks, hours, and what was learned",["Jokes","Songs","Gossip"],"Document learning.")
H('154.d.5.A',4,"A supervisor evaluates a practicum student through:",
  "Observation and the student's documentation",["Guessing","Rumors","Weather"],"Evaluate.")
H('154.d.5.B',3,"Advanced technical skills for a designer include:",
  "Space planning and reading construction plans",["Juggling","Singing","Gardening"],"Advanced skills.")
H('154.d.5.B',4,"Using a scale ruler to read a floor plan is part of advanced:",
  "Technical knowledge",["Karaoke","Sports","Cooking"],"Technical.")
H('154.d.5.C',3,"Applying principles of design to a room scheme means arranging elements for:",
  "Balance and harmony",["Clutter","Confusion","Randomness"],"Design application.")
H('154.d.5.C',4,"A room that feels top-heavy might be improved by adding:",
  "Visual weight near the floor",["More ceiling decor","Fewer rugs","Tall bare walls"],"Balance.")
H('154.d.5.D',3,"Evaluating materials and workmanship on a client's chair includes checking the:",
  "Frame, joints, and fabric",["Shipping label","Store logo","Sticker"],"Quality.")
H('154.d.5.D',4,"Wobbly legs and loose joints indicate poor:",
  "Construction quality",["Paint","Fabric","Lighting"],"Workmanship.")
H('154.d.5.E',3,"Advanced care of a natural stone countertop includes using:",
  "A pH-neutral cleaner and a sealer as needed",["Harsh acid","Steel wool","Bleach daily"],"Care procedures.")
H('154.d.5.E',4,"Acidic cleaners can damage marble because they:",
  "Etch the surface",["Add shine","Seal it","Dye it"],"Chemistry of care.")
H('154.d.5.F',3,"Choosing accessories, lighting, and materials with advanced skill means considering:",
  "Function, style, and budget together",["Color only","Cost only","Size only"],"Selection.")
H('154.d.5.F',4,"Layering ambient, task, and accent lighting creates a room that is:",
  "Functional and visually interesting",["Flat and dull","Dark","Glaring"],"Lighting layers.")
H('154.d.5.G',3,"Arranging furniture to fit a floor plan starts with noting:",
  "Doors, windows, and traffic flow",["Wall color only","Brand names","Price tags"],"Space planning.")
H('154.d.5.G',4,"A conversation area works best when seating is arranged:",
  "Facing each other within easy talking distance",["Back to back","Across the room","In a line against walls"],"Furniture placement.")
H('154.d.5.H',3,"Applying knowledge of construction means selecting products that are:",
  "Well built and suited to their use",["Cheapest only","Fragile","Unfinished"],"Application.")
H('154.d.5.H',4,"A durable commercial-grade fabric is chosen for a waiting room because it:",
  "Withstands heavy use",["Is delicate","Fades fast","Stains easily"],"Selection.")
H('154.d.5.I',3,"Evaluating strengths and weaknesses of your skills helps you:",
  "Decide what to improve",["Quit","Hide errors","Blame others"],"Self-evaluation.")
H('154.d.5.I',4,"A student strong at design but slow at measuring should:",
  "Practice measuring and drafting",["Ignore it","Stop designing","Skip plans"],"Targeted practice.")
H('154.d.5.J',3,"Representative work samples may include:",
  "Floor plans, mood boards, and photos",["Receipts","Menus","Gossip"],"Samples.")
H('154.d.5.J',4,"A work sample is best when it shows:",
  "Your skill and a clear design process",["Blank paper","Random scribbles","Nothing"],"Selection.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_23.jsonl'))

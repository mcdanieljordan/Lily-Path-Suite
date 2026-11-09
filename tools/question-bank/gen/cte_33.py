import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('127.', 1110, own='cte_33.jsonl')
def H(code, d, q, right, wrong, e):
    return B.hand(code, d, q, right, wrong, e)

# ---------- 127.181 Textiles and Apparel (construction level) ----------
H('181.d.5',3,"A tailoring shop uses a computerized embroidery machine and design software. These are examples of:",
  "Technology applications",["Hand stitches","Fire drills","Pressing cloths"],"Technology applications.")
H('181.d.5',4,"A cutting room that stores patterns digitally can retrieve a pattern:",
  "Quickly without searching files by hand",["Only by visiting a library","After weeks of waiting","Only on paper"],"Technology applications.")
H('181.d.7',3,"Wearing a thimble or finger guard and keeping pins in a cushion follows:",
  "Sewing room safety practices",["Fashion trends","Pricing plans","Color theory"],"Safety.")
H('181.d.7',4,"Before leaving a pressing station, the safe step is to:",
  "Turn the iron off and stand it upright",["Leave it face down","Cover it with fabric","Plug in another tool"],"Safety regulations.")
H('181.d.10',3,"Learning to thread a serger quickly is building technical skills for:",
  "Efficiency",["Delay","Waste","Rework"],"Technical skills.")
H('181.d.10',4,"Which habit speeds up production without lowering quality in a sewing room?",
  "Organizing tools and notions within reach",["Searching for scissors each time","Skipping pattern checks","Working without a plan"],"Technical skills.")
H('181.d.1.A',3,"A student who joins a sewing technology workshop for credentials is taking part in:",
  "Training for employment",["A day off","A competition only","Free time"],"Training.")
H('181.d.1.A',4,"Earning an industry certificate in garment production most helps with:",
  "Proving skills to employers",["Avoiding work","Skipping school","Losing opportunities"],"Certification.")
H('181.d.1.B',3,"Completing alterations by the promised pickup date shows:",
  "Reliability",["Carelessness","Laziness","Disorder"],"Work behaviors.")
H('181.d.1.B',4,"A seamstress who accepts a fit correction without arguing shows:",
  "Professional openness to feedback",["Stubbornness","Disinterest","Defiance"],"Personal qualities.")
H('181.d.1.C',3,"Preparing a resume that lists sewing skills and applying at an alterations shop is:",
  "Seeking and applying for employment",["Quitting","Retiring","Ignoring work"],"Seeking employment.")
H('181.d.1.C',4,"Which detail belongs on a resume for a tailoring job?",
  "Machines and techniques you can operate",["Your favorite color","Your lunch order","Your commute music"],"Applying for jobs.")
H('181.d.1.D',3,"Keeping photos and notes of garments you sewed in one folder creates a:",
  "Career portfolio",["Laundry list","Shipping label","Fabric swatch book only"],"Portfolio.")
H('181.d.1.D',4,"A portfolio entry for a skirt should show:",
  "Photos, materials used, and skills demonstrated",["Only the price","Only the thread brand","Nothing about the work"],"Portfolio.")
H('181.d.2.A',3,"Reading and following a commercial pattern's printed instructions applies:",
  "English language arts skills",["Welding","Plumbing","Gardening"],"ELA.")
H('181.d.2.A',4,"A clear written note on a work order about a hem change should be:",
  "Accurate, brief, and easy to follow",["Vague","Rambling","Full of slang"],"ELA.")
H('181.d.2.B',3,"A skirt needs 1 3/4 yards of fabric. How many yards are needed for 4 skirts?",
  "7",["6","8","5 3/4"],"1.75 x 4 = 7.")
H('181.d.2.B',4,"Fabric costs $6 per yard, thread costs $3, and a zipper costs $2. What is the total for 3 yards of fabric?",
  "$23",["$20","$18","$29"],"6 x 3 = 18; 18 + 3 + 2 = 23.")
H('181.d.3.A',3,"Explaining fabric terms simply to a new customer instead of using trade jargon is adapting to the:",
  "Audience",["Needle size","Bobbin","Hem"],"Adapt language.")
H('181.d.3.A',4,"A formal email to a mill and a quick note to a coworker differ in tone because of:",
  "Purpose and situation",["Fabric weight","Thread color","Needle point"],"Adapt language.")
H('181.d.3.B',3,"Listing garment construction steps in the correct order is:",
  "Organizing written information",["Dyeing","Pressing","Cutting"],"Organize.")
H('181.d.3.B',4,"Labeling cut pieces by garment and size helps a production team:",
  "Keep parts organized",["Lose pieces","Mix up sizes","Waste time"],"Organize.")
H('181.d.3.C',3,"A worker reports that the stitch tension is too tight and puckering the seam. This is:",
  "Communicating an observation",["Hiding a problem","Guessing","Ignoring"],"Interpret and communicate.")
H('181.d.3.C',4,"Reading a measurement chart and telling a coworker which size to cut is:",
  "Interpreting and communicating data",["Dyeing","Pressing","Printing"],"Interpret information.")
H('181.d.3.D',3,"Showing a garment line to a store buyer at a scheduled meeting is a:",
  "Formal presentation",["Casual remark","Rumor","Daydream"],"Formal presentation.")
H('181.d.3.D',4,"Explaining a stitch change to a coworker at the machine is a(n):",
  "Informal presentation",["Trade show","Press release","Keynote"],"Informal presentation.")
H('181.d.3.E',3,"A tailor who listens carefully to a customer describe a fit problem is using:",
  "Active listening",["Interrupting","Ignoring","Texting"],"Active listening.")
H('181.d.3.E',4,"Writing down a customer's measurements while repeating them back prevents:",
  "Misunderstandings",["Sales","Orders","Alterations"],"Active listening.")
H('181.d.3.F',3,"Serving customers of many ages, sizes, and cultures calls for:",
  "Respectful communication",["Stereotypes","Rudeness","Impatience"],"Diverse individuals.")
H('181.d.3.F',4,"A tailor fitting a customer with a disability should:",
  "Ask about comfort and listen to their needs",["Assume what is needed","Skip the fitting","Rush"],"Diverse individuals.")
H('181.d.3.G',3,"A friendly greeting and prompt pickup service at an alterations shop build:",
  "Customer loyalty",["Dust","Delays","Waste"],"PR skills.")
H('181.d.3.G',4,"Following up with a customer a week after delivery shows:",
  "Care for customer satisfaction",["Pushy sales","Disinterest","Poor service"],"PR skills.")
H('181.d.4.A',3,"Testing two seam types on scrap fabric before choosing is:",
  "Critical thinking",["Guessing","Luck","Habit"],"Critical thinking.")
H('181.d.4.A',4,"A team reviews cost, durability, and look before picking a fabric. This uses:",
  "Evidence-based decision making",["Coin flips","Impulse","Copying"],"Critical thinking.")
H('181.d.4.B',3,"Two sewers disagree on the order of steps. A good interpersonal move is to:",
  "Try both on a sample and compare",["Shout","Walk out","Ignore it"],"Interpersonal skills.")
H('181.d.4.B',4,"Group problem solving in a workroom works best when members:",
  "Share ideas and listen",["Interrupt","Work separately","Blame"],"Group problem solving.")
H('181.d.6.A',3,"Seeing that wide-leg pants today look like a style from decades ago is:",
  "Comparing fashion history with current trends",["Hemming","Dyeing","Pressing"],"Fashion history and trends.")
H('181.d.6.A',4,"Studying older garments helps designers spot:",
  "Styles that may return in new forms",["Fabrics that never exist","Ideas never used","Colors that cannot be made"],"Fashion history.")
H('181.d.6.B',3,"A war that limits fabric supplies can lead to clothing styles that are:",
  "Simpler with less fabric",["Fuller with more fabric","More decorated","Heavier"],"Historical events and fashion.")
H('181.d.6.B',4,"Changing attitudes about women's roles in the 1920s influenced fashion by:",
  "Making hemlines and silhouettes more relaxed",["Making clothing stiffer","Ending fashion","Requiring uniforms"],"Historical attitudes.")
H('181.d.8.A',3,"A shop supervisor who sets goals for the sewing team and guides them shows:",
  "Leadership",["Avoidance","Neglect","Blame"],"Leadership.")
H('181.d.8.A',4,"A strong leader helps a team meet a deadline by:",
  "Planning tasks and offering support",["Doing nothing","Blaming others","Hiding problems"],"Leadership.")
H('181.d.8.B',3,"Honesty, respect, and dependability are characteristics of:",
  "Effective working relationships",["Poor teams","Weak plans","Unsafe shops"],"Working relationships.")
H('181.d.8.B',4,"A coworker who admits a seam error and fixes it builds:",
  "Trust",["Distrust","Rivalry","Distance"],"Working relationships.")
H('181.d.8.C',3,"Contributing ideas in a team huddle about packing orders is:",
  "Participating in a group",["Leaving early","Staying silent","Skipping work"],"Participate in groups.")
H('181.d.8.C',4,"A good group member:",
  "Shares tasks and listens to others",["Dominates","Avoids work","Ignores ideas"],"Participate in groups.")
H('181.d.8.D',3,"An experienced seamstress teaching a new hire how to topstitch is:",
  "Mentoring",["Competing","Hiding tricks","Ignoring"],"Mentoring.")
H('181.d.8.D',4,"A mentor helps a trainee grow by:",
  "Demonstrating, then letting them practice",["Taking over tasks","Criticizing only","Withholding help"],"Mentoring.")
H('181.d.9.A',3,"Keeping a customer's measurements private is an example of:",
  "Client confidentiality",["Gossiping","Advertising","Sharing for fun"],"Ethical conduct.")
H('181.d.9.A',4,"A tailor who tells a customer an honest price and timeline is showing:",
  "Ethical conduct",["Poor business","Weakness","Carelessness"],"Ethics.")
H('181.d.9.B',3,"Sewing and selling copies of a brand's logo-covered bag without permission could violate:",
  "Copyright or trademark law",["Weather rules","Traffic laws","Fire codes"],"Copyright.")
H('181.d.9.B',4,"An original fabric print created by a designer is protected because it is:",
  "An original creative work",["Common thread","A public sign","Thread only"],"Copyright.")
H('181.d.9.C',3,"The popularity of athletic wear in everyday life shows how fashion industries can:",
  "Influence what society wears",["Stop trends","Change the weather","Control gravity"],"Fashion and society.")
H('181.d.9.C',4,"Fast fashion's low prices and rapid turnover can influence society by:",
  "Increasing textile waste",["Reducing waste","Slowing trends","Ending sales"],"Fashion and society.")
H('181.d.11.A',3,"Reading Vogue or WWD to follow runway news is analyzing:",
  "Fashion publications",["Science journals","Auto manuals","Cookbooks"],"Fashion publications.")
H('181.d.11.A',4,"Trade publications are useful to retailers because they report on:",
  "Industry trends and business news",["Weather forecasts","Sports scores","Recipes"],"Fashion publications.")
H('181.d.11.B',3,"A style that is introduced, becomes popular, peaks, and declines is following the:",
  "Fashion cycle",["Water cycle","Rock cycle","Carbon cycle"],"Fashion cycle.")
H('181.d.11.B',4,"A retailer notices a style is in its decline stage. It will likely:",
  "Discount the item to clear stock",["Order far more of it","Raise the price","Hide the inventory"],"Fashion cycle.")
H('181.d.12.A',3,"Cotton, wool, silk, and polyester are examples of:",
  "Fibers used in textiles",["Needle types","Pattern marks","Zipper styles"],"Fibers and textiles.")
H('181.d.12.A',4,"Which of these is a natural fiber?",
  "Wool",["Nylon","Polyester","Acrylic"],"Fibers and textiles.")
H('181.d.12.B',3,"Pouring water on a swatch to see if it beads up tests:",
  "Water resistance",["Colorfastness","Heat sensitivity","Thread count"],"Textile testing.")
H('181.d.12.B',4,"Rubbing a damp white cloth on dyed fabric to see if color transfers tests:",
  "Colorfastness",["Heat sensitivity","Water resistance","Weave type"],"Textile testing.")
H('181.d.12.C',3,"Choosing sturdy denim for workwear shows that textile products must suit their:",
  "Intended apparel use",["Store location","Price tag color","Thread brand"],"Suitability of textiles.")
H('181.d.12.C',4,"A lightweight, breathable fabric is a better fit for:",
  "Summer shirts",["Winter coats","Heavy upholstery","Tents"],"Suitability of textiles.")
H('181.d.12.D',3,"The finished edge of fabric that keeps it from raveling is the:",
  "Selvage",["Bias","Hem allowance","Dart"],"Selvage and grain.")
H('181.d.12.D',4,"The lengthwise grain of a fabric runs:",
  "Parallel to the selvage",["Across the width","At a 45-degree angle","Randomly"],"Grain line.")
H('181.d.13.A',3,"Washing a cotton towel in warm water with regular detergent is an appropriate:",
  "Care procedure for textile products",["Dye method","Cutting method","Printing method"],"Care procedures.")
H('181.d.13.A',4,"Before laundering a new blanket, the first step is to:",
  "Read the care label",["Guess the temperature","Use bleach","Tumble on high"],"Care procedures.")
H('181.d.13.B',3,"Following the tag to wash a wool sweater cold and lay it flat to dry is a:",
  "Care procedure for apparel",["Cutting step","Dyeing step","Pricing step"],"Care procedures.")
H('181.d.13.B',4,"Hand washing delicate garments helps prevent:",
  "Stretching and damage",["Color","Comfort","Style"],"Care procedures.")
H('181.d.14.A',3,"Wearing heat-safe gloves near a steam press follows:",
  "Safety and sanitary procedures",["A fashion trend","Pricing rules","Color rules"],"Safety and sanitation.")
H('181.d.14.A',4,"Separating soiled work clothes from clean laundry follows which kind of rule?",
  "A sanitary procedure",["A style rule","A pricing rule","A fit rule"],"Safety and sanitation.")
H('181.d.14.B',3,"Using a pressing cloth on silk to avoid shine is a:",
  "Pressing procedure",["Cutting procedure","Dyeing procedure","Printing procedure"],"Pressing.")
H('181.d.14.B',4,"Pressing with an up-and-down motion rather than sliding the iron helps avoid:",
  "Stretching the fabric",["Brightening","Wrinkle repair","Saving time"],"Pressing.")
H('181.d.15.A',3,"Sewing machines, sergers, and cutting tables are examples of:",
  "Apparel production equipment",["Dyeing chemicals","Marketing slogans","Delivery trucks"],"Equipment.")
H('181.d.15.A',4,"A tool used to cut many layers of fabric at once is a:",
  "Straight knife cutter",["Pin cushion","Seam ripper","Tape measure"],"Equipment.")
H('181.d.15.B',3,"The process of turning a pattern and fabric into a finished garment is:",
  "Apparel construction",["Marketing","Laundering","Shipping"],"Apparel construction.")
H('181.d.15.B',4,"In garment construction, cutting the fabric comes:",
  "Before sewing the pieces together",["After the garment is finished","After pressing the hem","After shipping"],"Apparel construction.")
H('181.d.16.A',3,"Cotton comes from a plant, while polyester is:",
  "A manufactured fiber",["A plant fiber","An animal fiber","A mineral fiber"],"Fibers.")
H('181.d.16.A',4,"A property of wool is that it is generally:",
  "Warm and absorbent",["Waterproof","Stiff like glass","Plastic-like"],"Fibers.")
H('181.d.16.B',3,"Interlacing lengthwise and crosswise yarns on a loom produces a:",
  "Woven fabric",["Knit fabric","Felt","Nonwoven web"],"Textile production.")
H('181.d.16.B',4,"Looping yarn together with needles produces a:",
  "Knit fabric",["Woven fabric","Plain paper","Film"],"Textile production.")
H('181.d.16.C',3,"Leaving a cotton shirt in strong sunlight for months can cause:",
  "Fading and weakening",["Brighter colors","Stronger fibers","Waterproofing"],"Environmental effects.")
H('181.d.16.C',4,"Mold and mildew grow on stored textiles when the environment is:",
  "Warm and damp",["Cool and dry","Clean and dry","Bright and dry"],"Environmental effects.")
H('181.d.17.A',3,"A flexible tape used to measure around the body is a:",
  "Tape measure",["Seam ripper","Rotary cutter","Pin"],"Measurement tools.")
H('181.d.17.A',4,"A standard pattern seam allowance of 5/8 inch means the stitching line sits what distance from the cut edge?",
  "Five-eighths of an inch",["A quarter of an inch","One full inch","Two inches"],"Measurement units.")
H('181.d.17.B',3,"Cleaning lint out of a sewing machine bobbin area is part of:",
  "Equipment care",["Fabric dyeing","Pattern drafting","Price tagging"],"Tools and equipment care.")
H('181.d.17.B',4,"Using the correct needle size for a fabric weight is part of:",
  "Proper selection of tools",["Wasted effort","Random choice","Skipping steps"],"Equipment selection.")
H('181.d.17.C',3,"Shortening a dress hem while keeping the hem balanced applies:",
  "Design principles when altering apparel",["Advertising","Shipping","Laundering"],"Alterations.")
H('181.d.17.C',4,"Altering a jacket so the sleeve line follows the arm's natural curve shows attention to:",
  "Line and proportion",["Packaging","Pricing","Weather"],"Design elements and principles.")
H('181.d.17.D',3,"Keeping hands away from a moving needle follows:",
  "Machine safety procedures",["Style tips","Pricing rules","Color rules"],"Safety procedures.")
H('181.d.17.D',4,"Before changing a sewing machine needle, you should:",
  "Turn the machine off or unplug it",["Keep it running","Pull the fabric","Speed up"],"Safety procedures.")
H('181.d.17.E',3,"Adding a wide waistband for a person with a wheelchair so pants sit comfortably is:",
  "An alteration for special needs",["A style fad","A pricing trick","A color change"],"Special needs apparel.")
H('181.d.17.E',4,"Replacing buttons with hook-and-loop closures can help someone who:",
  "Has limited hand dexterity",["Likes buttons","Has no sleeves","Dislikes fabric"],"Special needs apparel.")
H('181.d.18.A',3,"Even stitches, matching seams, and clean hems are marks of:",
  "Quality apparel construction",["Poor work","Accidents","Shortcuts"],"Quality construction.")
H('181.d.18.A',4,"Which feature most clearly signals good construction?",
  "Seams that lie flat without puckering",["Loose threads","Uneven hems","Crooked darts"],"Quality construction.")
H('181.d.18.B',3,"Choosing a fabric and silhouette that suit a gown's purpose applies:",
  "Design principles and elements when constructing apparel",["Shipping rules","Tax rules","Cleaning rules"],"Design and construction.")
H('181.d.18.B',4,"A formal evening gown would typically use fabric that is:",
  "Elegant and drapey",["Rough canvas","Plastic mesh","Rubber"],"Design and construction.")
H('181.d.18.C',3,"Pressing a seam open after stitching is an appropriate:",
  "Pressing technique in construction",["Cutting method","Dyeing method","Labeling method"],"Construction and pressing.")
H('181.d.18.C',4,"Clipping curves in a seam allowance helps a curved seam to:",
  "Lie smooth when turned",["Pucker more","Tear apart","Shrink"],"Construction techniques.")
H('181.d.18.D',3,"Notches, grain lines, and dart markings are examples of:",
  "Pattern parts and terminology",["Fabric brands","Sewing needles","Care symbols"],"Pattern terminology.")
H('181.d.18.D',4,"Notches on a pattern are used to:",
  "Match pieces correctly when sewing",["Decorate the pattern","Cut fabric shorter","Count yardage"],"Pattern terminology.")

# ---------- 127.182 Fashion Design I (advanced) ----------
H('182.d.4',3,"Fashion design software and a digital drawing tablet are:",
  "Technology applications",["Hand tools only","Fire exits","Fabric scraps"],"Technology applications.")
H('182.d.4',4,"A designer sharing a tech pack with a factory overseas uses technology to:",
  "Communicate specifications clearly",["Hide details","Delay production","Avoid questions"],"Technology applications.")
H('182.d.5',3,"Studying clothing from ancient Egypt to the present is part of analyzing the:",
  "History of fashion, textiles, and apparel",["Weather","Geography of rivers","History of computers"],"Fashion history.")
H('182.d.5',4,"Historical research helps designers because styles often:",
  "Borrow ideas from earlier eras",["Never change","Ignore the past","Come from nowhere"],"Fashion history.")
H('182.d.6',3,"Safely storing rotary cutter blades covered when not in use follows:",
  "Safety regulations",["Fashion trends","Pricing rules","Color rules"],"Safety.")
H('182.d.6',4,"Which practice reduces fire risk in a fashion studio?",
  "Keeping fabric away from hot irons and lamps",["Piling fabric near the iron","Blocking exits","Leaving irons on"],"Safety regulations.")
H('182.d.9',3,"A designer who masters grading software is building advanced technical skills for:",
  "Efficiency",["Delay","Waste","Confusion"],"Technical skills.")
H('182.d.9',4,"Creating reusable block patterns saves a design team:",
  "Time on repeated style development",["Money on nothing","Samples","Customers"],"Technical skills.")
H('182.d.1.A',3,"Reading a design brief for a line of jackets applies:",
  "English language arts skills",["Welding","Plumbing","Gardening"],"ELA.")
H('182.d.1.A',4,"Writing precise descriptions on a spec sheet prevents:",
  "Production mistakes",["Sales","Samples","Trends"],"ELA.")
H('182.d.1.B',3,"A coat uses 2.25 yards of fabric. How many yards for 8 coats?",
  "18",["16","20","22.5"],"2.25 x 8 = 18.")
H('182.d.1.B',4,"A garment costs $14 to make and sells wholesale at twice the cost. What is the wholesale price?",
  "$28",["$16","$14","$42"],"14 x 2 = 28.")
H('182.d.2.A',3,"Explaining a collection's theme to a buyer in plain language is adapting to the:",
  "Audience",["Needle","Bobbin","Zipper"],"Adapt language.")
H('182.d.2.A',4,"A designer's emails to a mill and to a model differ because of:",
  "Purpose and situation",["Fabric weight","Thread color","Needle point"],"Adapt language.")
H('182.d.2.B',3,"Arranging collection notes by season and garment type is:",
  "Organizing information",["Dyeing","Pressing","Sewing"],"Organize.")
H('182.d.2.B',4,"Presenting a design story in a logical order from concept to finished garment helps buyers:",
  "Follow the idea easily",["Lose interest","Skip the collection","Get confused"],"Organize.")
H('182.d.2.C',3,"Telling a team that a fabric swatch faded after washing is:",
  "Communicating an observation",["Hiding results","Guessing","Ignoring"],"Interpret and communicate.")
H('182.d.2.C',4,"Reading sales data and explaining which silhouette sold best is:",
  "Interpreting data",["Sewing","Pressing","Dyeing"],"Interpret information.")
H('182.d.2.D',3,"Presenting a seasonal line to retail buyers at a scheduled showroom appointment is a:",
  "Formal presentation",["Casual remark","Rumor","Daydream"],"Formal presentation.")
H('182.d.2.D',4,"Quickly explaining a trim idea to a sample maker is a(n):",
  "Informal presentation",["Fashion show","Press release","Keynote"],"Informal presentation.")
H('182.d.2.E',3,"A designer who listens to a client describe a vision and takes notes is using:",
  "Active listening",["Interrupting","Ignoring","Texting"],"Active listening.")
H('182.d.2.E',4,"Asking clarifying questions after a critique helps a designer to:",
  "Understand and apply the feedback",["Ignore advice","Avoid changes","Argue"],"Active listening.")
H('182.d.2.F',3,"Designing for clients of many sizes, ages, and cultures calls for:",
  "Respectful communication",["Stereotypes","Rudeness","Impatience"],"Diverse individuals.")
H('182.d.2.F',4,"A design team that includes members from different backgrounds can:",
  "Produce more varied ideas",["Limit creativity","Avoid collaboration","Reduce options"],"Diversity.")
H('182.d.2.G',3,"Thanking buyers and following up after a showroom visit builds:",
  "Business relationships",["Delays","Clutter","Waste"],"PR skills.")
H('182.d.2.G',4,"A brand responds courteously to a social media complaint. This helps its:",
  "Public image",["Fabric stock","Zipper supply","Needle count"],"PR skills.")
H('182.d.3.A',3,"Comparing three trim options for a coat and choosing the best fit for the line is:",
  "Critical thinking",["Guessing","Luck","Habit"],"Critical thinking.")
H('182.d.3.A',4,"A group chooses a final sample by checking cost, fit, and market feedback. This uses:",
  "Evidence-based decision making",["Coin flips","Impulse","Copying"],"Critical thinking.")
H('182.d.3.B',3,"A designer and a pattern maker disagree about a seam placement. A good move is to:",
  "Test both on a muslin sample",["Shout","Walk out","Ignore it"],"Interpersonal skills.")
H('182.d.3.B',4,"Group problem solving in a studio goes best when members:",
  "Listen and share ideas",["Interrupt","Work separately","Blame"],"Group problem solving.")
H('182.d.7.A',3,"A lead designer who sets goals for a capsule collection and guides assistants shows:",
  "Leadership",["Avoidance","Neglect","Blame"],"Leadership.")
H('182.d.7.A',4,"Strong leaders accomplish collective goals by:",
  "Planning, delegating, and supporting the team",["Working alone","Hiding plans","Blaming"],"Leadership.")
H('182.d.7.B',3,"Respect, honesty, and open communication are practices for:",
  "Effective working relationships",["Poor teams","Weak plans","Unsafe shops"],"Working relationships.")
H('182.d.7.B',4,"A designer who gives credit to sample makers builds:",
  "Trust",["Rivalry","Distance","Suspicion"],"Working relationships.")
H('182.d.7.C',3,"Running a student club meeting using motions and votes follows:",
  "Parliamentary procedure",["Random talk","Free-for-all","Silent rules"],"Meetings.")
H('182.d.7.C',4,"In parliamentary procedure, a proposal for the group to consider is a:",
  "Motion",["Recess","Agenda","Minute"],"Meetings.")
H('182.d.7.D',3,"An experienced designer teaching an intern to drape on a form is:",
  "Mentoring",["Competing","Hiding tricks","Ignoring"],"Mentoring.")
H('182.d.7.D',4,"A mentor inspires others by:",
  "Sharing skills and encouraging growth",["Taking over","Criticizing only","Withholding help"],"Mentoring.")
H('182.d.8.A',3,"Giving credit to the original designer of an idea is:",
  "Ethical conduct in fashion",["Weak practice","Unneeded","Slow"],"Ethical conduct.")
H('182.d.8.A',4,"Fair labor practices in factories are part of:",
  "Ethical standards in the industry",["Optional extras","Style choices","Color choices"],"Ethics.")
H('182.d.8.B',3,"Copying another label's original print and selling it as yours would:",
  "Violate copyright law",["Be fair play","Be a courtesy","Be required"],"Copyright.")
H('182.d.8.B',4,"A designer protects an original fabric pattern by registering it under:",
  "Copyright law",["Zoning law","Traffic law","Weather law"],"Copyright.")
H('182.d.8.C',3,"Using a licensed pattern with the proper permissions shows:",
  "Respect for intellectual property",["Neglect","Carelessness","Disrespect"],"IP respect.")
H('182.d.8.C',4,"Taking inspiration from a trend but not copying a specific design shows:",
  "Respect for intellectual property",["Disregard","Theft","Neglect"],"IP respect.")
H('182.d.8.D',3,"Acceptable use policies for studio computers tell staff how to:",
  "Use equipment and online accounts properly",["Park cars","Order lunch","Pick colors"],"Acceptable use.")
H('182.d.8.D',4,"Installing unlicensed design software on a studio computer would:",
  "Break acceptable use rules",["Be encouraged","Improve security","Be required"],"Acceptable use.")
H('182.d.8.E',3,"An employer's right to direct work and an employee's right to safe conditions are:",
  "Rights and responsibilities in the workplace",["Fashion trends","Color rules","Fit rules"],"Rights and responsibilities.")
H('182.d.8.E',4,"An employee's responsibility includes:",
  "Doing assigned work honestly and on time",["Ignoring rules","Coming late","Hiding mistakes"],"Rights and responsibilities.")
H('182.d.8.F',3,"Labeling garments with fiber content as required by law is a:",
  "Legal aspect of apparel",["Style choice","Color choice","Trend"],"Legal aspects.")
H('182.d.8.F',4,"A company using a false 'Made in USA' label could face:",
  "Legal penalties",["Free publicity","Tax breaks","Awards"],"Legal aspects.")
H('182.d.10.A',3,"Comparing Greek chitons, Victorian corsets, and 1960s mod dresses is evaluating:",
  "Significant historic fashions",["Weather patterns","Computer parts","Map symbols"],"Historic fashions.")
H('182.d.10.A',4,"Corsets in the Victorian era shaped the silhouette to emphasize a:",
  "Small waist",["Wide shoulders","Straight lines","Low neckline only"],"Historic fashions.")
H('182.d.10.B',3,"Changes in women's roles at work have influenced fashion by encouraging:",
  "More practical clothing",["Heavier gowns","Larger hoops","Stiffer corsets"],"Social influences.")
H('182.d.10.B',4,"Youth movements such as punk affected fashion by introducing:",
  "New styles that challenged norms",["Uniform dress","Silence","Plain suits only"],"Social influences.")
H('182.d.10.C',3,"Wearing a certain headdress to show status in an early civilization communicated:",
  "Values and rank",["Weather","Hunger","Time"],"Values through clothing.")
H('182.d.10.C',4,"In many cultures, clothing communicates values such as:",
  "Religion, status, and tradition",["Gravity","Weather","Algebra"],"Values through clothing.")
H('182.d.10.D',3,"A 1970s bell-bottom revival on today's runways shows how history:",
  "Influences current fashion",["Ends fashion","Ignores trends","Stops sales"],"Historic influence.")
H('182.d.10.D',4,"Designers often reinterpret archival designs by:",
  "Updating them with new fabrics and fits",["Copying them exactly","Burning them","Ignoring them"],"Historic influence.")
H('182.d.10.E',3,"Coco Chanel and Christian Dior are known as prominent:",
  "Historical designers",["Weather forecasters","Football coaches","Chefs"],"Historical designers.")
H('182.d.10.E',4,"Dior's 1947 'New Look' is known for emphasizing:",
  "A cinched waist and full skirt",["Straight sacks","Short shorts","Bare shoulders only"],"Historical designers.")
H('182.d.11.A',3,"Making many identical garments quickly using standardized parts is:",
  "Mass production",["Haute couture","Hand embroidery","Custom tailoring"],"Mass production.")
H('182.d.11.A',4,"Mass production lowers the cost of clothing mainly by:",
  "Making many items efficiently",["Making one item","Using only gold thread","Avoiding machines"],"Mass production.")
H('182.d.11.B',3,"Charles Frederick Worth is considered a founder of:",
  "Haute couture",["Fast fashion","Sportswear","Uniforms"],"Haute couture.")
H('182.d.11.B',4,"Haute couture houses make garments that are:",
  "Custom, handcrafted, and expensive",["Machine-made in bulk","Disposable","Cheap and quick"],"Haute couture.")
H('182.d.12.A',3,"Famous designers influence trends when their runway looks are:",
  "Copied or adapted by other brands",["Ignored","Hidden","Banned"],"Leading designers.")
H('182.d.12.A',4,"A designer sets a trend by introducing a look that:",
  "Many consumers and brands adopt",["Nobody sees","Is illegal","Is never shown"],"Leading designers.")
H('182.d.12.B',3,"A global event such as a famous film festival can affect fashion by:",
  "Spreading styles across countries",["Stopping trade","Ending trends","Closing stores"],"International factors.")
H('182.d.12.B',4,"Trade agreements and tariffs can change garment costs by:",
  "Altering the price of imported goods",["Setting colors","Changing grain lines","Altering stitches"],"International factors.")
H('182.d.12.C',3,"3D printing and digital pattern making are examples of technology that:",
  "Speeds design and prototyping",["Slows design","Stops design","Replaces fabric"],"Technology in design.")
H('182.d.12.C',4,"Virtual sampling can reduce waste by:",
  "Letting designers test looks without making physical samples",["Making more samples","Using more fabric","Skipping design"],"Technology in design.")
H('182.d.12.D',3,"Choosing expensive silk instead of cotton raises a garment's:",
  "Production cost",["Weight only","Hem length","Button count"],"Design and cost.")
H('182.d.12.D',4,"Adding hand-sewn beading to every piece of a line will most likely:",
  "Increase labor costs",["Lower the price","Remove labor","Cut material costs"],"Design and cost.")
H('182.d.13.A',3,"Drawing a fashion figure with elongated proportions on a croquis is:",
  "Fashion figure drawing",["Pattern grading","Fabric dyeing","Seam pressing"],"Fashion figure drawing.")
H('182.d.13.A',4,"A fashion figure is often drawn about nine to ten heads tall to:",
  "Create an elegant, stylized look",["Match real people exactly","Save paper","Hide details"],"Fashion figure drawing.")
H('182.d.13.B',3,"Using line, color, and balance to create a fashion drawing applies:",
  "Design elements and principles",["Safety rules","Tax rules","Shipping rules"],"Elements and principles.")
H('182.d.13.B',4,"A drawing that uses a bold color accent to draw the eye shows:",
  "Emphasis",["Symmetry only","Chaos","Dullness"],"Design principles.")
H('182.d.13.C',3,"Hue, value, and intensity are properties of:",
  "Color",["Seams","Grain","Selvage"],"Color properties.")
H('182.d.13.C',4,"A color made lighter by adding white is called a:",
  "Tint",["Shade","Tone","Primary"],"Color properties.")
H('182.d.13.D',3,"Using design software to draw a flat sketch and a color story is a:",
  "Computer-aided technique",["Hand-only technique","Dyeing technique","Pressing technique"],"Computer-aided design.")
H('182.d.13.D',4,"One advantage of computer-aided design is that a designer can:",
  "Change colors and details quickly",["Avoid revisions","Skip planning","Redraw everything by hand"],"Computer-aided design.")
H('182.d.13.E',3,"Picking a drapey knit for a flowy dress shows how to:",
  "Select textiles for a specific design",["Choose at random","Ignore fabric","Skip design"],"Textile selection.")
H('182.d.13.E',4,"A structured blazer typically needs fabric that:",
  "Holds its shape",["Collapses","Stretches endlessly","Is see-through"],"Textile selection.")
H('182.d.13.F',3,"Putting sketches, swatches, and photos into a presentation book is:",
  "Assembling portfolio components",["Disposing of work","Cutting patterns","Dyeing fabric"],"Portfolio.")
H('182.d.13.F',4,"A fashion design portfolio should present designs:",
  "Clearly and in a consistent, professional format",["Messily","Randomly","Without labels"],"Portfolio.")
H('182.d.14.A',3,"Reviewing a client's body shape, coloring, and lifestyle is a technique to analyze:",
  "Fashion image",["Fabric dye","Seam strength","Pattern grain"],"Fashion image analysis.")
H('182.d.14.A',4,"A stylist uses a color analysis to recommend:",
  "Shades that flatter the client",["Random colors","Only black","Only neon"],"Fashion image analysis.")
H('182.d.14.B',3,"Personal style, budget, and occupation are factors in:",
  "Fashion image consulting",["Weaving","Dyeing","Cutting"],"Image consulting.")
H('182.d.14.B',4,"A consultant recommends versatile pieces to a client with a small budget because they:",
  "Mix and match for many outfits",["Cost more","Last one wear","Match nothing"],"Image consulting.")
H('182.d.14.C',3,"Writing recommendations for a client's wardrobe and accessories is developing a:",
  "Personal fashion image evaluation",["Pattern block","Tech pack","Price list"],"Fashion image evaluation.")
H('182.d.14.C',4,"A useful image evaluation should consider the client's:",
  "Goals, body, coloring, and lifestyle",["Shoe size only","Favorite song","Zip code"],"Fashion image evaluation.")

# ---------- 127.183 Fashion Design II (advanced practicum) ----------
H('183.d.5',3,"Using pattern-making software and a digital cutter in a studio shows:",
  "Technology applications",["Hand tools only","Fire exits","Fabric scraps"],"Technology applications.")
H('183.d.5',4,"A digital cutter helps a design studio cut patterns:",
  "Accurately and quickly",["Slowly","Randomly","With more waste"],"Technology applications.")
H('183.d.6',3,"The way fibers, textiles, and apparel are designed, produced, and sold forms:",
  "Fashion, textile, and apparel systems",["A weather system","A water system","A bus system"],"Systems.")
H('183.d.6',4,"A change in fiber cost affects later stages such as pricing because the stages are:",
  "Connected in a system",["Unrelated","Isolated","Random"],"Systems.")
H('183.d.7',3,"Wearing a dust mask when cutting certain fabrics and keeping cutting areas clear follows:",
  "Safety regulations",["Style rules","Pricing rules","Color rules"],"Safety.")
H('183.d.7',4,"A properly maintained cutting table includes:",
  "Clear surfaces and covered blades",["Open blades","Clutter","Loose cords"],"Safety regulations.")
H('183.d.10',3,"A designer who masters pattern-grading shortcuts is building advanced technical skills for:",
  "Efficiency",["Delay","Waste","Confusion"],"Technical skills.")
H('183.d.10',4,"Standardizing seam allowances across a line helps the shop:",
  "Cut and sew consistently and faster",["Slow production","Lose fit","Increase errors"],"Technical skills.")
H('183.d.1.A',3,"Joining a fashion internship for training is:",
  "Participating in education for employment",["A vacation","A game","A chore"],"Training.")
H('183.d.1.A',4,"Earning an apparel industry certification shows employers that you have:",
  "Verified skills",["No skills","Free time","Inexperience"],"Certification.")
H('183.d.1.B',3,"Arriving prepared to a fitting and finishing samples on time shows:",
  "Positive work behaviors",["Poor habits","Delay","Neglect"],"Work behaviors.")
H('183.d.1.B',4,"A designer who stays calm when a sample fails shows:",
  "Professional resilience",["Panic","Blame","Avoidance"],"Personal qualities.")
H('183.d.1.C',3,"Sending a resume and portfolio to a design studio is:",
  "Applying for employment",["Quitting","Retiring","Ignoring work"],"Seeking employment.")
H('183.d.1.C',4,"A designer stands out in an interview by:",
  "Presenting a polished portfolio",["Arriving empty-handed","Skipping research","Criticizing others"],"Applying for jobs.")
H('183.d.1.D',3,"Documenting your finished garments, sketches, and certificates in one place creates a:",
  "Career portfolio",["Laundry list","Shipping log","Pantry list"],"Portfolio.")
H('183.d.1.D',4,"A strong portfolio shows an employer a designer's:",
  "Range of skills and experience",["Hobbies only","Lunch habits","Phone number only"],"Portfolio.")
H('183.d.1.E',3,"Opening a small custom-wear business is an example of:",
  "Entrepreneurship",["Retirement","Job loss","Unemployment"],"Entrepreneurship.")
H('183.d.1.E',4,"Before launching a clothing line, an entrepreneur should research:",
  "Costs, market, and competition",["Nothing","Only colors","Only names"],"Entrepreneurship.")
H('183.d.2.A',3,"Reading a spec sheet and writing a clear production note applies:",
  "English language arts skills",["Welding","Plumbing","Gardening"],"ELA.")
H('183.d.2.A',4,"A designer proofreads a purchase order to prevent:",
  "Costly errors",["Sales","Samples","Trends"],"ELA.")
H('183.d.2.B',3,"A dress needs 2 1/2 yards of fabric. How many yards for 6 dresses?",
  "15",["12","18","13 1/2"],"2.5 x 6 = 15.")
H('183.d.2.B',4,"A garment's materials cost $18 and labor costs $12. If it sells for $70, what is the profit?",
  "$40",["$30","$52","$58"],"18 + 12 = 30; 70 - 30 = 40.")
H('183.d.3.A',3,"Using plain language with a customer and technical terms with a factory is adapting to the:",
  "Audience",["Needle","Bobbin","Zipper"],"Adapt language.")
H('183.d.3.A',4,"A formal vendor email differs from a quick text to a model because of:",
  "Purpose and situation",["Fabric weight","Thread color","Needle point"],"Adapt language.")
H('183.d.3.B',3,"Listing steps for producing a sample in order is:",
  "Organizing information",["Dyeing","Pressing","Sewing"],"Organize.")
H('183.d.3.B',4,"A clear project timeline with milestones helps a team:",
  "Meet deadlines",["Miss deadlines","Lose track","Skip tasks"],"Organize.")
H('183.d.3.C',3,"Explaining that a sample fits too tightly across the hip, with measurements, is:",
  "Communicating observations",["Hiding results","Guessing","Ignoring"],"Interpret and communicate.")
H('183.d.3.C',4,"Reading a cost sheet and telling a team which fabric is cheaper per yard is:",
  "Interpreting data",["Sewing","Pressing","Dyeing"],"Interpret information.")
H('183.d.3.D',3,"Presenting a collection to investors in a scheduled pitch is a:",
  "Formal presentation",["Casual remark","Rumor","Daydream"],"Formal presentation.")
H('183.d.3.D',4,"Quickly explaining a fabric change to the sewing team is a(n):",
  "Informal presentation",["Fashion show","Press release","Keynote"],"Informal presentation.")
H('183.d.3.E',3,"A designer who listens to a client and restates the request is using:",
  "Active listening",["Interrupting","Ignoring","Texting"],"Active listening.")
H('183.d.3.E',4,"Asking clarifying questions in a fitting helps a designer to:",
  "Understand the client's needs",["Ignore the client","Delay work","Confuse the plan"],"Active listening.")
H('183.d.3.F',3,"Designing and communicating with clients of many backgrounds calls for:",
  "Respect and open communication",["Stereotypes","Rudeness","Impatience"],"Diverse individuals.")
H('183.d.3.F',4,"A designer who learns about a client's cultural dress traditions is:",
  "Showing cultural respect",["Ignoring customs","Teasing","Excluding"],"Diversity.")
H('183.d.3.G',3,"Thanking buyers and following up after delivery builds:",
  "Business relationships",["Delays","Clutter","Waste"],"PR skills.")
H('183.d.3.G',4,"Responding calmly to a client's complaint and offering a remedy helps a brand's:",
  "Reputation",["Fabric stock","Zipper supply","Needle count"],"PR skills.")
H('183.d.4.A',3,"Testing three fabrics for a jacket lining and choosing the most durable is:",
  "Critical thinking",["Guessing","Luck","Habit"],"Critical thinking.")
H('183.d.4.A',4,"A design team evaluates cost, fit, and feedback before finalizing a style. This uses:",
  "Evidence-based decision making",["Coin flips","Impulse","Copying"],"Critical thinking.")
H('183.d.4.B',3,"A designer and a seamstress disagree about a closure. A good step is to:",
  "Try both on a sample and compare",["Shout","Walk out","Ignore it"],"Interpersonal skills.")
H('183.d.4.B',4,"A team solves production problems best when members:",
  "Share ideas and listen",["Interrupt","Work separately","Blame"],"Group problem solving.")
H('183.d.8.A',3,"A lead designer who sets goals and analyzes results after each collection shows:",
  "Leadership",["Avoidance","Neglect","Blame"],"Leadership.")
H('183.d.8.A',4,"Analyzing what worked after a season helps a leader to:",
  "Improve future collections",["Assign blame","Hide results","End the line"],"Leadership.")
H('183.d.8.B',3,"Providing constructive feedback to a coworker helps establish:",
  "Effective working relationships",["Tension","Silence","Rivalry"],"Working relationships.")
H('183.d.8.B',4,"Constructive feedback should be:",
  "Specific and respectful",["Vague","Harsh","Late"],"Constructive feedback.")
H('183.d.8.C',3,"A student organization meeting where members make motions and vote follows:",
  "Parliamentary procedure",["Random talk","Free-for-all","Silent rules"],"Meetings.")
H('183.d.8.C',4,"To end a parliamentary meeting, a member usually makes a motion to:",
  "Adjourn",["Amend","Table","Postpone indefinitely"],"Meetings.")
H('183.d.8.D',3,"A senior designer showing a junior how to grade a pattern is:",
  "Mentoring",["Competing","Hiding tricks","Ignoring"],"Mentoring.")
H('183.d.8.D',4,"A good mentor inspires and teaches by:",
  "Modeling skills and encouraging questions",["Taking over","Criticizing only","Withholding help"],"Mentoring.")
H('183.d.9.A',3,"Giving honest quotes and delivering what you promise is:",
  "Ethical conduct",["Weak practice","Slow business","Optional"],"Ethical conduct.")
H('183.d.9.A',4,"A designer who admits a labeling mistake and corrects it shows:",
  "Integrity",["Carelessness","Weakness","Deception"],"Ethics.")
H('183.d.9.B',3,"Copying another label's original print would:",
  "Violate copyright law",["Be fair play","Be a courtesy","Be required"],"Copyright.")
H('183.d.9.B',4,"A designer owns the copyright to an original textile print because it is:",
  "An original creative work",["Common thread","A public sign","A trademark only"],"Copyright.")
H('183.d.9.C',3,"Licensing a pattern before using it in a line shows:",
  "Respect for intellectual property",["Neglect","Carelessness","Disrespect"],"IP respect.")
H('183.d.9.C',4,"Being inspired by a trend but creating your own design shows:",
  "Respect for intellectual property",["Disregard","Theft","Neglect"],"IP respect.")
H('183.d.9.D',3,"Acceptable use policies tell employees how to use:",
  "Company computers and accounts properly",["Parking spaces","Lunchrooms","Color swatches"],"Acceptable use.")
H('183.d.9.D',4,"Using a work computer to download unlicensed software would:",
  "Break acceptable use rules",["Be encouraged","Improve security","Be required"],"Acceptable use.")
H('183.d.9.E',3,"The right of an employee to a safe workplace and the duty to perform assigned tasks are:",
  "Rights and responsibilities in employment",["Fashion trends","Color rules","Fit rules"],"Rights and responsibilities.")
H('183.d.9.E',4,"An employer's responsibility includes:",
  "Paying fairly and providing safe conditions",["Ignoring rules","Hiding hazards","Underpaying staff"],"Rights and responsibilities.")
H('183.d.9.F',3,"An industry code that bans unsafe labor and false advertising reflects:",
  "Ethical practices in fashion and apparel",["Style trends","Color rules","Fit rules"],"Ethical practices.")
H('183.d.9.F',4,"Sourcing fabric from suppliers that treat workers fairly is an example of:",
  "Ethical sourcing",["Poor planning","Cost cutting only","Style choice"],"Ethical practices.")
H('183.d.9.G',3,"Labeling laws require clothing to show items such as:",
  "Fiber content and care instructions",["Store hours","Designer's age","Price of thread"],"Legal aspects.")
H('183.d.9.G',4,"A brand that sells counterfeit goods bearing another company's logo may face:",
  "Legal action",["Free publicity","Tax breaks","Awards"],"Legal aspects.")
H('183.d.11.A',3,"Cutting fabric, sewing seams, and pressing garments are:",
  "Tasks employees may perform",["Hobbies","Clubs","Holidays"],"Employee tasks.")
H('183.d.11.A',4,"A pattern cutter's main task is to:",
  "Cut fabric accurately from patterns",["Sell goods","Clean windows","Deliver mail"],"Employee tasks.")
H('183.d.11.B',3,"Following the steps in a written procedure for steaming garments is:",
  "Following procedures for performing tasks",["Skipping steps","Guessing","Improvising"],"Procedures.")
H('183.d.11.B',4,"Procedures help ensure garments are produced:",
  "Consistently and safely",["Randomly","Unsafely","Slowly"],"Procedures.")
H('183.d.11.C',3,"Using fabric scraps for trims and small items is:",
  "Resource management",["Waste","Disorder","Neglect"],"Resource management.")
H('183.d.11.C',4,"Planning a pattern layout to leave the least scrap fabric is:",
  "Efficient use of resources",["Careless cutting","Overbuying","Wasting cloth"],"Resource management.")
H('183.d.12.A',3,"Comparing dyeing, printing, and finishing is comparing:",
  "Textile coloring and treatment processes",["Sewing stitches","Pressing temperatures","Needle sizes"],"Textile processes.")
H('183.d.12.A',4,"Applying color in a pattern by pressing designs onto fabric is:",
  "Printing",["Weaving","Knitting","Felting"],"Textile processes.")
H('183.d.12.B',3,"A wrinkle-resistant finish changes a fabric's:",
  "Characteristics and performance",["Fiber origin","Selvage position","Grain line"],"Finishes.")
H('183.d.12.B',4,"A water-repellent finish on a jacket makes it better for:",
  "Rainy weather",["Hot weather","Dry weather","Indoor use"],"Finishes.")
H('183.d.12.C',3,"Recommending machine washing in cold water for a polyester blouse is:",
  "Recommending care procedures",["Dyeing","Cutting","Printing"],"Care procedures.")
H('183.d.12.C',4,"A wool sweater is best recommended to be:",
  "Washed gently and dried flat",["Boiled","Tumbled hot","Wrung hard"],"Care procedures.")
H('183.d.13.A',3,"Moving from a concept sketch to a sample to a finished product is the textile:",
  "Design process",["Marketing plan","Cleaning cycle","Shipping route"],"Textile design process.")
H('183.d.13.A',4,"In the textile design process, a sample is usually made:",
  "Before full production",["After shipping","After sales","Never"],"Textile design process.")
H('183.d.13.B',3,"Weaving and knitting are different:",
  "Methods of textile production",["Care labels","Marketing tools","Safety rules"],"Textile production.")
H('183.d.13.B',4,"A stretchy T-shirt fabric is most likely made by:",
  "Knitting",["Weaving","Felting","Casting"],"Textile production.")
H('183.d.13.C',3,"Choosing a dye method that uses less water has implications for the:",
  "Environment",["Grain line","Needle size","Zipper size"],"Dyeing and finishing.")
H('183.d.13.C',4,"Printing a design with heat transfer is a method of:",
  "Coloring or decorating fabric",["Weaving cloth","Knitting yarn","Cutting patterns"],"Dyeing and printing.")
H('183.d.13.D',3,"Garment labels must show fiber content, country of origin, and:",
  "Care information",["Designer's age","Store hours","Thread brand"],"Labeling requirements.")
H('183.d.13.D',4,"The agency that enforces textile labeling laws in the United States is the:",
  "Federal Trade Commission",["National Park Service","Department of Agriculture only","Weather Service"],"Labeling requirements.")
H('183.d.13.E',3,"Fabric type, labor, and shipping all affect a textile product's:",
  "Cost",["Grain","Selvage","Needle point"],"Cost factors.")
H('183.d.13.E',4,"Which change would most likely raise a garment's retail price?",
  "Using imported silk with hand finishing",["Using plain cotton","Using fewer trims","Using simple seams"],"Cost factors.")
H('183.d.14.A',3,"Drawing a stylized fashion figure with a croquis is:",
  "Fashion figure drawing",["Pattern grading","Fabric dyeing","Seam pressing"],"Fashion figure drawing.")
H('183.d.14.A',4,"A fashion figure is drawn with elongated legs to:",
  "Present garments in an elegant way",["Match real proportions","Save paper","Hide details"],"Fashion figure drawing.")
H('183.d.14.B',3,"Using line, color, and balance to create a fashion drawing applies:",
  "Design elements and principles",["Safety rules","Tax rules","Shipping rules"],"Elements and principles.")
H('183.d.14.B',4,"A sketch where the outfit's focal point is a bold collar shows:",
  "Emphasis",["Symmetry only","Chaos","Dullness"],"Design principles.")
H('183.d.14.C',3,"Using design software to create flat sketches and color options is a:",
  "Computer-aided technique",["Hand-only technique","Dyeing technique","Pressing technique"],"Computer-aided design.")
H('183.d.14.C',4,"A benefit of computer-aided design is that designers can:",
  "Revise details quickly",["Avoid revising","Skip planning","Redraw by hand each time"],"Computer-aided design.")
H('183.d.14.D',3,"Choosing stretch jersey for a fitted dress is selecting:",
  "Appropriate textiles for a design",["A random fabric","A mismatched cloth","No cloth"],"Textile selection.")
H('183.d.14.D',4,"A tailored coat usually needs a fabric that:",
  "Holds structure and drapes cleanly",["Collapses","Stretches endlessly","Is see-through"],"Textile selection.")
H('183.d.14.E',3,"Assembling sketches, swatches, and photos into a presentation book is:",
  "Assembling portfolio components",["Disposing of work","Cutting patterns","Dyeing fabric"],"Portfolio.")
H('183.d.14.E',4,"A fashion portfolio should present designs:",
  "Clearly, consistently, and professionally",["Messily","Randomly","Without labels"],"Portfolio.")
H('183.d.15.A',3,"Describing the steps and machines used to draft and produce a pattern is outlining:",
  "General procedures and equipment in apparel design",["A care label","A dye bath","A shipping route"],"Design equipment.")
H('183.d.15.A',4,"A dress form is used in apparel design to:",
  "Drape and fit fabric in three dimensions",["Wash garments","Store thread","Cut fabric"],"Design equipment.")
H('183.d.15.B',3,"Making a one-of-a-kind dress for a specific client using proper tools is constructing a:",
  "Custom-made garment",["Mass-market item","Shipping box","Fabric swatch"],"Custom garments.")
H('183.d.15.B',4,"Custom garments are made to a client's:",
  "Individual measurements",["Average measurements","Random size","No size"],"Custom garments.")
H('183.d.15.C',3,"Pinning a muslin on a client and adjusting seams is a step in developing garments for proper:",
  "Fit",["Weather","Price","Dye"],"Garment fit.")
H('183.d.15.D',3,"Taking body measurements, drafting a pattern, and adjusting for fit are procedures of:",
  "Garment fitting and pattern making",["Shipping","Advertising","Printing"],"Fitting and pattern making.")
H('183.d.15.D',4,"A muslin sample is used to test:",
  "Fit and design before cutting final fabric",["Final color","Care labels","Shipping boxes"],"Fitting and pattern making.")
H('183.d.15.E',3,"Cutting out fabric from a custom pattern and sewing the pieces together is:",
  "Constructing a custom garment",["Laundering","Marketing","Shipping"],"Custom construction.")
H('183.d.15.E',4,"A quality custom garment is finished with:",
  "Clean seams, secure fastenings, and a pressed look",["Loose threads","Uneven hems","Crooked closures"],"Custom construction.")
H('183.d.15.F',3,"Keeping fingers away from the needle and wearing closed shoes is:",
  "A safety practice in garment construction",["A style tip","A price tip","A color tip"],"Safety practices.")
H('183.d.15.F',4,"Cutting a fabric with sharp shears on a stable table helps prevent:",
  "Injuries and uneven cuts",["Good fit","Quality","Speed"],"Safety practices.")
H('183.d.16.A',3,"Reviewing a client's coloring, body shape, and lifestyle is a technique to analyze:",
  "Fashion image",["Fabric dye","Seam strength","Pattern grain"],"Fashion image analysis.")
H('183.d.16.A',4,"A stylist uses color analysis to recommend:",
  "Shades that flatter the client",["Random colors","Only black","Only neon"],"Fashion image analysis.")
H('183.d.16.B',3,"Personal style, budget, and career are factors in:",
  "Fashion image consulting",["Weaving","Dyeing","Cutting"],"Image consulting.")
H('183.d.16.B',4,"A consultant suggests mix-and-match basics to a client with a small budget because they:",
  "Create many outfits from few items",["Cost more","Last one wear","Match nothing"],"Image consulting.")
H('183.d.16.C',3,"Writing a wardrobe plan with recommendations for a client is developing a:",
  "Personal fashion image evaluation",["Pattern block","Tech pack","Price list"],"Fashion image evaluation.")
H('183.d.16.C',4,"A good image evaluation should consider the client's:",
  "Goals, body, coloring, and lifestyle",["Shoe size only","Favorite song","Zip code"],"Fashion image evaluation.")

H('181.d.8.C',5,"In a sewing room huddle, one coworker keeps dominating while two others never speak. A good group member would:",
  "Invite quieter members to share their ideas",["Let the dominant one decide","Leave the meeting","Take over the talking"],"Participate in groups.")
H('182.d.7.D',5,"A designer wants a new assistant to learn draping without feeling dependent. Which mentoring approach fits best?",
  "Demonstrate once, then let the assistant try with feedback",["Do every drape for them","Say nothing at all","Criticize each attempt harshly"],"Mentoring.")
H('182.d.8.E',5,"A new hire is asked to work unpaid overtime with no agreement. Which statement reflects employee rights?",
  "Employees are entitled to lawful pay for time worked",["Employers can ignore wage laws","Workers must stay silent","Overtime never needs pay"],"Rights and responsibilities.")
H('183.d.8.B',5,"A coworker's patternmaking has repeated errors. Which feedback best builds the working relationship?",
  "Point to specific examples and offer help improving them",["Say it is all wrong","Complain to others","Say nothing"],"Constructive feedback.")
H('183.d.9.D',5,"A designer wants to install a free photo editor on a studio computer. What should come first?",
  "Check the company's acceptable use policy and ask IT",["Install it immediately","Share the password","Disable security"],"Acceptable use.")
H('183.d.14.B',5,"A sketch looks cluttered with equal emphasis everywhere. Which change creates a clear focal point?",
  "Make one detail bolder and simplify the rest",["Add more details to each part","Use identical colors","Remove the figure"],"Design principles.")
H('183.d.15.C',4,"A muslin pulls across the back when the client reaches forward. The designer should:",
  "Add ease or adjust the back seam",["Ignore the pull","Cut the final fabric anyway","Remove the lining only"],"Garment fit.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_33.jsonl'))

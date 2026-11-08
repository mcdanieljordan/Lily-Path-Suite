#!/usr/bin/env python3
"""Grade 5 Social Studies (TEKS 113.16.c, United States history) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('113.16.c.', 915, own='g5_ss.jsonl')

load(B, """
1.A|3|Which group of colonists sailed to America mainly seeking religious freedom?|the Pilgrims|the conquistadors|the gold miners|the railroad builders|The Pilgrims came in 1620 to worship freely.
1.A|3|Jamestown, the first lasting English colony, was settled mostly for...|economic gain|religious freedom only|a new school|a new railroad|Settlers hoped for profit in 1607.
1.B|3|Who founded Pennsylvania as a place of religious freedom for Quakers?|William Penn|Roger Williams|John Smith|Sam Adams|Penn offered tolerance in his colony.
1.B|3|Roger Williams is remembered for founding which colony?|Rhode Island|Georgia|Texas|Florida|Williams believed in separating church and government.
2.A|3|Britain taxed the colonies after the French and Indian War to...|pay for war debts|build the Alamo|buy Louisiana|fund railroads|Britain needed money after the war.
2.A|3|The colonists protested taxes with the slogan about having no taxation without...|representation|education|migration|exploration|They had no vote in Parliament.
2.A|3|The Boston Tea Party was a protest against...|British taxes on tea|French ships|railroad prices|a new school|Colonists dumped tea in the harbor.
2.B|3|Who wrote most of the Declaration of Independence?|Thomas Jefferson|George Washington|Abraham Lincoln|Andrew Jackson|Jefferson was the main author.
2.B|3|Who led the Continental Army during the American Revolution?|George Washington|Benjamin Franklin|John Adams|Paul Revere|Washington was commander in chief.
2.B|3|The Sons of Liberty were...|Patriots who protested British rule|British soldiers|Spanish explorers|railroad owners|They organized colonial protests.
2.C|3|One result of the American Revolution was...|the United States became a free nation|Britain gained more land|the colonies stayed British|France took over|The colonies won independence.
3|3|Who is often called the Father of the Constitution for his role in writing it?|James Madison|Paul Revere|Ben Franklin only|Davy Crockett|Madison shaped the document at the Convention.
3|3|Which two leaders helped shape the new government as Founding Fathers?|Alexander Hamilton and James Madison|Pierre L'Enfant and Sam Houston|Stephen Austin and Zachary Taylor|Daniel Boone and Davy Crockett|Both debated the Constitution.
4.A|3|The War of 1812 was caused partly by British...|impressment of American sailors|ban on tea|invasion of Texas|use of railroads|Britain forced U.S. sailors into service.
4.A|3|The war of 1812 increased...|American national pride|British rule in America|slavery's end|the number of colonies|The U.S. survived against Britain.
4.B|3|The Industrial Revolution led the North toward...|factories and cities|plantations only|ranching only|hunting only|Northern cities grew with industry.
4.B|3|The South depended mostly on...|farming and enslaved labor|steel mills|computers|microchips|Plantations relied on cotton.
4.C|3|The Louisiana Purchase doubled the size of the U.S. by buying land from...|France|Spain|Canada|Britain|Jefferson bought it in 1803.
4.C|3|Lewis and Clark explored the...|Louisiana Purchase land and the West|Atlantic Ocean|South Pole|English Channel|Their expedition mapped the new territory.
4.C|3|The idea that the U.S. should stretch across the continent was called...|Manifest Destiny|Reconstruction|Prohibition|Isolationism|Many Americans believed in westward growth.
4.D|3|A key cause of the Civil War was disagreement over the spread of...|slavery|railroads|telephones|radio|Slavery divided the nation.
4.D|3|The Civil War was fought between the...|Union and the Confederacy|Texans and Mexicans|French and British|Pilgrims and Patriots|North fought the South.
4.E|3|The 13th Amendment did what?|ended slavery|gave women the vote|created income tax|ended Prohibition|It abolished slavery.
4.E|3|The 15th Amendment gave voting rights to...|men of all races|only women|children|only landowners|It protected the right to vote regardless of race.
4.E|3|Reconstruction was the period of...|rebuilding the South and bringing it back into the Union|writing the Constitution|exploring the West|the Great Depression|It followed the Civil War.
4.F|3|The Homestead Act gave settlers...|free land in the West|free tea|free ships|free cars|Settlers claimed 160 acres.
4.F|3|Many immigrants arriving at Ellis Island came seeking...|opportunity and a new life|the Pilgrims|Mexico|California gold only|Ellis Island welcomed newcomers.
5.A|3|The Great Depression began after the...|stock market crash of 1929|Civil War|American Revolution|Louisiana Purchase|Banks failed and jobs vanished.
5.A|3|The U.S. entered World War II after the attack on...|Pearl Harbor|the Alamo|Gettysburg|Yorktown|Japan attacked in 1941.
5.A|3|The Civil Rights Movement worked to...|end unfair treatment because of race|build the railroad|start a war|find oil|Leaders sought equal rights.
5.A|3|The Cold War was a conflict between the U.S. and the...|Soviet Union|Confederacy|British colonies|French Empire|The two superpowers competed without direct war.
5.B|3|The September 11 attacks led to the...|War on Terror|Great Depression|Civil War|Industrial Revolution|The U.S. responded with new security actions.
5.B|3|In 2008, which event was historic in U.S. elections?|the election of the first Black president|the end of the Civil War|the first moon landing|the Great Depression|Barack Obama was elected.
5.C|3|Susan B. Anthony worked for...|women's right to vote|railroads|oil drilling|cattle drives|She led the suffrage movement.
5.C|3|Rosa Parks became a symbol of the Civil Rights Movement when she...|refused to give up her bus seat|invented the radio|led the Texas army|discovered oil|Her act sparked the Montgomery bus boycott.
5.C|3|Martin Luther King Jr. believed in...|nonviolent protest|war|silence|isolation|He led peaceful marches.
5.C|3|Cesar Chavez helped...|farm workers get better pay and conditions|build the Alamo|invent the telephone|sail to America|He founded a farm workers union.
6.A|3|An example of a political region in the U.S. is...|a state|a desert|a mountain|an ocean|States are political divisions.
6.A|3|An economic region is based on...|how people earn a living|the weather only|the stars|mountains only|Economy defines these regions.
6.B|3|Which region of the U.S. has the Rocky Mountains?|the West|the Northeast|the Southeast|the Gulf Coast|The Rockies run through the West.
6.B|3|The Great Plains are mostly...|flat grassland|snowy peaks|rain forest|ocean|They are broad, flat prairies.
6.C|3|How many states are in the United States?|50|13|48|52|There are fifty states.
6.C|3|Which city is the largest by population in the U.S.?|New York City|Austin|Seattle|Denver|New York City is the largest.
6.D|3|Which river is the longest and runs through the center of the U.S.?|Mississippi River|Colorado River|Hudson River|Potomac River|It flows from Minnesota to the Gulf.
6.D|3|The Appalachian Mountains are located in the...|eastern U.S.|western U.S.|far north of Canada|Gulf of Mexico|They stretch down the East.
7.A|3|A place with many people, tall buildings, and busy streets is...|urban|rural|wild|desert|Urban means city.
7.A|3|A community outside a big city with houses and shops is...|suburban|urban|rural|polar|Suburbs surround cities.
7.A|3|A community with farms and few people is...|rural|urban|suburban|coastal city|Rural means countryside.
7.B|3|Why do many cities grow near rivers or harbors?|they help with trade and travel|they have no people|they are dry|they ban boats|Water routes helped trade.
7.C|3|Many of the largest U.S. cities are located...|near water or trade routes|in the middle of deserts|on mountain tops|in swamps only|Water access helped them grow.
8.A|3|Building a canal is an example of...|modifying the environment|ignoring the environment|storing sunshine|moving a state|People changed land for travel.
8.B|3|A positive effect of building dams is...|producing electricity and storing water|more floods always|fewer jobs|less water|Dams store water and make power.
8.B|3|A negative effect of cutting forests is...|loss of animal habitat|more cities|less trade|more snow|Animals lose their homes.
9.A|3|Early colonies earned money by...|farming and trading|building computers|making movies|selling cars|They traded crops and goods.
9.B|3|Which was a major colonial industry in New England?|shipbuilding|oil drilling|computer making|satellite launching|Ports needed ships.
9.B|3|Tobacco, rice, and cotton were colonial...|cash crops|schools|forts|ships|They were sold for money.
10.A|3|Free enterprise began in colonial America as people...|owned businesses and traded goods|were told what to make|could not sell|lost all property|Colonists traded freely.
10.B|3|In free enterprise, businesses compete to...|win customers|avoid selling|close down|hide goods|Competition leads to better products.
10.C|3|One benefit of free enterprise is...|more choices for shoppers|fewer jobs|higher taxes only|no stores|Competition gives people choices.
11.A|3|When many people want something that is hard to find, the price...|goes up|goes to zero|stays zero|disappears|High demand raises prices.
11.A|3|When a product is plentiful and few people want it, the price...|goes down|goes up|doubles|is fixed|Low demand lowers price.
11.B|3|Why was the plantation system tied to supply and demand?|demand for cotton and tobacco was high|there was no demand|crops were unwanted|nobody bought cotton|Demand fueled plantation growth.
12.A|3|People in the Midwest are known for earning a living through...|farming|surfing|skiing|diving|The Midwest grows grain and corn.
12.A|3|Many people in the Gulf Coast earn a living through...|oil and shipping|ski resorts|ice fishing|glacier tours|Energy and ports dominate.
12.B|3|Geography affects economic activity. Why are farms placed in places with good soil?|good soil helps crops grow|soil is expensive|soil is rare|soil is purple|Farmers use fertile land.
12.C|3|How did immigration help the U.S. economy grow?|immigrants provided workers and new ideas|they stopped trade|they closed factories|they ended farming|Newcomers filled jobs.
12.D|3|Mass production made goods...|faster and cheaper to make|slower to make|more expensive always|harder to find|Assembly lines sped up production.
12.D|3|Division of labor means...|each worker does one part of a job|everyone does everything|nobody works|one worker does it all|Specialization boosts speed.
13.A|3|A monarchy is a government ruled by...|a king or queen|voters|a city council|a class president|Monarchs inherit power.
13.A|3|A representative government is one where...|people elect leaders to make laws|a king rules alone|no laws exist|a soldier decides|Citizens vote for representatives.
13.B|3|The Mayflower Compact was...|an agreement to make fair laws for the colony|a treaty with France|a new tax|a ship|The Pilgrims agreed to self-government.
13.B|3|The Virginia House of Burgesses was the first...|elected lawmaking body in the colonies|state flag|Supreme Court|army|It began in 1619.
14.A|3|The Declaration of Independence stated that all people have the rights to life, liberty, and...|the pursuit of happiness|free tea|a vacation|a car|It lists these unalienable rights.
14.A|3|The Declaration of Independence explained why the colonies were...|breaking away from Britain|joining France|buying Texas|starting a school|It announced independence in 1776.
14.B|3|The Preamble to the Constitution begins with the words...|We the People|Once upon a time|Four score and seven|In the beginning|The people create the government.
14.B|3|One purpose of the Constitution listed in the Preamble is to...|establish justice|build cars|raise taxes only|stop schools|It aims to form a more perfect union.
14.C|3|Why was the Bill of Rights added?|to protect individual freedoms|to start a war|to end the Union|to build roads|Many feared a strong government.
15.A|3|The three branches of government are legislative, executive, and...|judicial|military|local|federal|Courts form the judicial branch.
15.A|3|Congress belongs to which branch?|legislative|executive|judicial|military|Congress makes laws.
15.A|3|The President leads which branch?|executive|legislative|judicial|local|The President enforces laws.
15.B|3|Checks and balances keep any one branch from...|becoming too powerful|existing|voting|making maps|Branches limit each other.
15.B|3|The President can veto a bill. This is an example of...|checks and balances|a tax|a census|a treaty only|One branch checks another.
15.C|3|Which power belongs to the national government?|printing money and declaring war|setting school start times in one town|picking a town's mayor|fixing city potholes|The federal government handles national matters.
15.C|3|Which power usually belongs to state governments?|running public schools|declaring war|printing national money|making treaties|States run local services.
16.A|3|Uncle Sam is a symbol of...|the United States government|a state|a company|a school|He represents the U.S.
16.A|3|The donkey and the elephant are symbols of...|political parties|states|countries|schools|They represent Democrats and Republicans.
16.A|3|Labor Day honors...|American workers|veterans|the Founding Fathers|presidents|It celebrates workers.
16.B|3|Who wrote the words to The Star-Spangled Banner?|Francis Scott Key|Thomas Jefferson|Betsy Ross|Paul Revere|Key wrote it during the War of 1812.
16.C|3|The Pledge of Allegiance shows loyalty to the...|United States flag and republic|a king|a school|a state only|It pledges allegiance to the flag.
16.D|3|The Statue of Liberty symbolizes...|freedom and welcome to immigrants|war|taxes|railroads|It stands in New York Harbor.
16.D|3|Mount Rushmore shows the faces of...|four presidents|four explorers|four soldiers|four inventors|Washington, Jefferson, Roosevelt and Lincoln.
16.D|3|The White House is...|the home and office of the President|a school|a fort|a bank|It is in Washington, D.C.
17.A|3|A citizen has a duty to take part in civic affairs by...|voting and obeying laws|ignoring laws|avoiding news|skipping elections|Participation keeps government strong.
17.B|3|How can you contact a member of Congress?|write a letter or email|stand quietly|wait for a sign|text a stranger|Leaders accept citizen messages.
17.C|3|A class votes on a field trip. Voting is a method for...|group decision making|ending class|hiding choices|ignoring ideas|Voting settles choices.
18.A|3|Who are the members of Congress?|senators and representatives|governors and mayors|judges and sheriffs|generals and admirals|Congress has two chambers.
18.A|3|How many senators does each state have?|two|one|three|four|Each state has two.
18.B|3|Which is a quality of a good leader?|honesty and courage|dishonesty|fear|laziness|Leaders earn trust.
19|3|The First Amendment protects freedom of...|speech, religion, and the press|taxes|weapons only|travel only|It protects basic freedoms.
19|3|The Fourth Amendment protects people from...|unreasonable searches|free speech|voting|school|It guards privacy.
20.A|3|Which song is associated with the colonial era and the Revolution?|Yankee Doodle|Hound Dog|Happy Birthday|Jingle Bells|It was popular during the war.
20.A|3|The painting American Progress shows...|westward expansion|the moon|a dinosaur|a city street|It shows settlers moving west.
20.B|3|Why do songs and paintings help us learn about the past?|they show how people thought and felt at the time|they are always true|they replace textbooks|they never change|Art reflects its era.
21.A|3|Thanksgiving, Diwali, and Hanukkah are examples of...|customs and traditions|laws|taxes|maps|Groups celebrate holidays.
21.B|3|Immigrants have helped shape the U.S. by...|contributing food, music, and ideas|stopping change|ending trade|hiding history|Many cultures shaped the nation.
22.A|3|Eli Whitney is famous for the...|cotton gin|telephone|airplane|light bulb|It cleaned cotton faster.
22.A|3|John Deere invented a...|steel plow|steamboat|radio|TV|It cut through prairie soil.
22.A|3|Thomas Edison is famous for...|developing a practical light bulb|inventing the telephone|writing the Constitution|flying planes|Edison improved electric lighting.
22.A|3|The Wright brothers are known for...|flying the first powered airplane|inventing the telephone|painting|writing laws|They flew at Kitty Hawk in 1903.
22.B|3|How did the computer industry help the economy?|created new jobs and businesses|ended work|closed stores|stopped trade|Tech industries grew rapidly.
22.C|3|How have medical advances helped people?|people live longer and healthier|people got sicker|hospitals closed|medicine stopped|Vaccines and surgery improved health.
23.A|3|A letter written by a soldier in 1863 is a...|primary source|secondary source|map|legend|It is a firsthand account.
23.A|3|A history book written last year about the Civil War is a...|secondary source|primary source|diary|photograph from the war|It was written long after.
23.B|3|To judge whether a source is credible, you should ask...|who wrote it and why|what color it is|how heavy it is|how long it is|Check the author and purpose.
23.C|3|Which words signal a cause-and-effect relationship?|because and as a result|first and next|above and below|big and small|They show cause and effect.
23.D|3|Which would best show events in order over time?|a timeline|a recipe|a map legend|a scale|Timelines show chronology.
23.E|3|Two newspapers describe the same event differently. This shows different...|points of view|maps|titles|dates|People see events differently.
23.F|3|The historical context of an event is...|the setting and time period in which it happened|its spelling|its length|its color|Context explains conditions.
23.G|3|The central claim is the...|main argument the author makes|title|first word|page count|It is the key point.
23.H|3|When you write a claim, evidence is...|the facts that support it|a joke|a rumor|a map|Evidence backs the claim.
24.A|3|A map scale helps you...|measure real distances|name the mapmaker|choose colors|find the capital|Scales relate map to real distance.
24.A|3|A legend or key explains...|what map symbols mean|how tall a mountain is|the mapmaker's age|today's weather|It decodes symbols.
24.B|3|A map with dots for cities shows...|population distribution|rainfall|sea level|the Pledge|Dots show where people live.
25.A|3|The correct term for a person who moves to a new country to live is...|immigrant|explorer|patriot|colonist|Immigrants relocate permanently.
25.B|3|A strong paragraph should have a main idea and...|supporting details|random facts|jokes|nothing else|Details support the topic.
25.E|3|Civil discourse means...|talking respectfully even when you disagree|shouting|insulting others|ignoring ideas|It is polite debate.
26.A|3|A class votes on a school rule. This simulates...|democratic decision making|a monarchy|a dictatorship|a war|Voting models democracy.
26.B|3|After identifying a problem, the next step is to...|gather information|give up|blame someone|hide it|Research comes next.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g5_ss.jsonl'))
print("saved", len(B.out), "questions")

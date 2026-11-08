#!/usr/bin/env python3
"""Grade 4 Social Studies (TEKS 113.15.c, Texas history) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('113.15.c.', 914, own='g4_ss.jsonl')

load(B, """
1.A|3|Some scientists think the first people in Texas came from Asia by crossing a land bridge. What does that idea explain?|a possible origin of American Indian groups|why Texas has bluebonnets|how oil formed|why rivers flow to the Gulf|It is a theory about where early peoples came from.
1.B|3|Which Texas group lived on the coast and hunted and fished along the Gulf?|Karankawa|Caddo|Jumano|Comanche|The Karankawa lived along the Gulf Coast.
1.B|3|The Caddo of East Texas were known for what way of life?|farming and living in grass houses in villages|following buffalo herds in tipis only|living on boats|mining silver|The Caddo farmed corn, beans and squash.
1.B|3|Which group moved across the plains following buffalo and lived in tipis?|Lipan Apache|Caddo|Alabama-Coushatta|Pueblo|The Lipan Apache hunted buffalo on the plains.
1.C|3|Which of these is a cultural region where American Indians lived in Texas?|Plains|Arctic|Pacific Northwest|Great Lakes|Plains, Gulf, Puebloan and Southeastern are Texas regions.
1.C|3|Which cultural region is known for adobe homes and farming near the Rio Grande?|Puebloan|Gulf|Plains|Southeastern|Puebloan peoples built with adobe.
1.D|3|The Ysleta Del Sur Pueblo is a tribe still found near which Texas city?|El Paso|Houston|Dallas|Amarillo|The Ysleta Del Sur Pueblo is in El Paso.
1.D|3|The Alabama-Coushatta tribe lives on a reservation in which part of Texas?|East Texas piney woods|West Texas desert|the Panhandle|the Rio Grande Valley|Their reservation is near Livingston.
2.A|3|Which was a major reason European countries explored Texas?|to find wealth and claim land|to build amusement parks|to study electricity|to start airlines|Explorers looked for gold and new territory.
2.A|3|Spain and France both wanted Texas land. This is an example of...|competition between countries|a peace treaty|a cattle drive|a school lesson|Countries competed for territory.
2.B|3|Which explorer was shipwrecked and walked across Texas, writing about what he saw?|Cabeza de Vaca|La Salle|Coronado|Stephen F. Austin|Cabeza de Vaca crossed Texas in the 1500s.
2.B|3|Which explorer searched for the legendary Cities of Gold?|Francisco Coronado|Sam Houston|Lizzie Johnson|Anson Jones|Coronado searched for riches that did not exist.
2.B|3|La Salle's French colony in Texas is remembered because it...|gave France a claim that made Spain settle Texas|became the capital|built the Alamo|started the cattle industry|His landing made Spain act to protect its claim.
2.C|3|Why did Spain build missions in Texas?|to spread the Catholic faith and hold the land|to sell cars|to mine coal|to run railroads|Missions taught religion and claimed land.
2.C|3|San Antonio de Valero is better known by what name?|the Alamo|Goliad|San Jacinto|Fort Worth|The mission became the Alamo.
2.D|3|When Mexico fought for independence from Spain, Texas became...|part of the new Mexican nation|part of France|part of Canada|a U.S. state at once|Mexico won independence in 1821.
2.E|3|What was an empresario?|a person who brought settlers to Texas under a contract|a railroad worker|a cattle driver|a mission priest|Empresarios recruited colonists for land grants.
2.E|3|Stephen F. Austin is called the "Father of Texas" because he...|led the first Anglo settlement of Texas colonists|invented the cotton gin|drew the first state flag|found oil at Spindletop|Austin settled the Old Three Hundred.
2.E|3|Martin De Leon founded which colony?|Victoria|Houston|El Paso|Amarillo|De Leon founded a Mexican-led colony at Victoria.
3.A|3|Which Texas Revolution battle took place at a mission in San Antonio in 1836?|the Battle of the Alamo|the Battle of Gettysburg|the Battle of Bunker Hill|the Red River War|Texans defended the Alamo for thirteen days.
3.A|3|What was the Runaway Scrape?|when Texas families fled east from Santa Anna's army|a cattle stampede|a rodeo event|a railroad race|Settlers escaped the advancing army.
3.A|3|Which battle ended the Texas Revolution?|San Jacinto|Goliad|Gonzales|the Alamo|Texans won at San Jacinto in 1836.
3.A|3|The Texas Declaration of Independence said that Texas was...|free from Mexico|part of Spain|a U.S. territory|part of France|It announced independence from Mexico.
3.B|3|Who commanded the Texas army at the Battle of San Jacinto?|Sam Houston|William B. Travis|David Crockett|Mirabeau Lamar|Houston led the victory.
3.B|3|Juan Seguin is remembered for...|serving as a Tejano captain in the Texas Revolution|inventing barbed wire|building the Alamo|writing a constitution alone|Seguin fought and led Tejano soldiers.
3.B|3|Who was a lawyer who wrote a famous letter asking for help from the Alamo?|William B. Travis|Jim Bowie|David Crockett|Santa Anna|Travis wrote his "Victory or Death" letter.
3.C|3|Who was the first president of the Republic of Texas elected in 1836?|Sam Houston|Anson Jones|Stephen F. Austin|Lizzie Johnson|Houston served as the first president.
3.C|3|Who was the last president of the Republic of Texas?|Anson Jones|Mirabeau Lamar|Sam Houston|Jose Navarro|Jones oversaw annexation.
3.C|3|Jose Antonio Navarro is remembered because he...|signed the Texas Declaration of Independence|invented the telephone|ran a railroad|led the Union army|Navarro was a Tejano signer.
3.D|3|A big problem for the Republic of Texas was...|owing a lot of money|having too many cars|too many railroads|too much snow|The Republic struggled with debt.
3.D|3|The Republic of Texas wrote its own...|constitution|flag of a different country|road atlas|cookbook|It created a constitution in 1836.
3.E|3|In 1845 Texas became...|a state of the United States|a colony of Spain|a territory of France|a province of Canada|Annexation made Texas the 28th state.
3.E|3|The war between the U.S. and Mexico (1846-1848) began partly over...|the Texas border|cotton prices only|railroad tickets|the telegraph|Disputed borders led to war.
4.A|3|Which war divided the nation, and Texas joined the Confederacy?|the Civil War|the Revolutionary War|World War I|the Mexican War of Independence|Texas seceded in 1861.
4.A|3|Reconstruction was the time...|after the Civil War when the South was rebuilt|before the Revolution|of the Great Depression|of the Dust Bowl|It followed the war.
4.B|3|Cattle drives in Texas took herds along trails to...|railroads in Kansas|the Pacific Ocean|Mexico City|New York|Cowboys drove cattle north to rail towns.
4.B|3|Charles Goodnight is remembered for...|blazing a famous cattle trail|writing the constitution|building the Alamo|discovering oil|The Goodnight-Loving Trail helped cattle drives.
4.B|3|Which ranch founder started the King Ranch?|Richard King|Sam Houston|Mirabeau Lamar|Audie Murphy|King built a huge South Texas ranch.
4.B|3|Lizzie Johnson was important to the cattle industry as...|a rancher and trail driver|a mission priest|a president|an astronaut|She was a businesswoman who drove her own herds.
4.C|3|How did railroads change life in Texas?|they helped towns grow and moved goods quickly|they stopped trade|they closed towns|they ended farming|Railroads connected markets.
4.D|3|What happened to the buffalo in the 1800s that hurt Plains Indians?|they were nearly all hunted out|they moved to Canada by choice|they became pets|they learned to fly|Loss of buffalo harmed their way of life.
4.D|3|The Red River War ended with...|American Indians being moved to reservations|a new state capital|the end of the railroad|a gold rush|The war ended Plains Indian resistance.
5.A|3|The Dust Bowl was caused by drought and...|poor farming practices that left soil to blow away|too many lakes|too much snow|a volcano|Dry soil blew away in great storms.
5.A|3|The Great Depression was a time when...|many people lost jobs and money|everyone got rich|trains stopped running forever|Texas became a state|Banks failed and unemployment rose.
5.A|3|Audie Murphy, a Texan, is remembered for...|being a World War II hero|inventing the airplane|running a mission|founding Houston|He was the most decorated U.S. soldier of the war.
5.B|3|Spindletop, near Beaumont, was important because...|it was a huge oil gusher that began the Texas oil boom|it was a mission|it was a fort|it was a cattle trail|The 1901 gusher changed the state economy.
5.B|3|Oil and gas helped Texas cities grow by...|creating jobs and drawing workers|closing all stores|stopping trade|ending railroads|Industry drew people to cities.
6.A|3|Which Texas region includes the Panhandle and is flat and dry?|Great Plains|Coastal Plains|Mountains and Basins|North Central Plains|The Great Plains are high and flat.
6.A|3|Which region of Texas has the Guadalupe Mountains?|Mountains and Basins|Coastal Plains|North Central Plains|Great Plains|It lies in far West Texas.
6.A|3|Which Texas region runs along the Gulf of Mexico and has hot, humid weather?|Coastal Plains|Mountains and Basins|Great Plains|North Central Plains|The Coastal Plains border the Gulf.
6.B|3|Compared with the Coastal Plains, the Mountains and Basins region is...|higher and drier|lower and wetter|flatter and wetter|colder and wetter|West Texas has higher, drier land.
7.A|3|Why did many early settlers choose land near rivers?|they needed water and good soil|rivers had no fish|rivers were noisy|they wanted deserts|Water supports farming and travel.
7.B|3|Many large Texas cities grew along...|rivers, coasts, and railroads|only mountain tops|only deserts|only the Panhandle border|Resources and routes shaped city locations.
8.A|3|Which is a way Texans modify the environment?|building dams and reservoirs|growing taller trees by wishing|moving the Gulf|changing the seasons|Dams store water for people.
8.B|3|Farmers drain wetlands in order to...|make more land for crops|stop rain|cool the air|remove oil|Draining creates farmland.
8.C|3|A negative consequence of cutting too many trees can be...|soil erosion|more rain every day|colder summers|more tall buildings|Roots hold soil in place.
9.A|3|How did Plains Indians meet their needs and wants?|by hunting buffalo and trading|by running factories|by selling cars|by flying planes|They used buffalo for food, clothing and shelter.
9.B|3|How did early Texas settlers meet their needs?|by farming and ranching|by building skyscrapers|by driving trucks|by using computers|They grew crops and raised livestock.
10.A|3|In a free enterprise system, prices are affected by...|supply and demand|a king's order|a coin flip|the weather alone|Buyers and sellers shape prices.
10.B|3|One benefit of free enterprise is...|people can choose what to buy and what business to start|the government sets every job|nobody may own a business|there are no choices|Choice and opportunity are key.
10.C|3|Cash crops grown by early colonists, like cotton, helped...|the free enterprise system grow in Texas|stop trade|close ports|end ranching|Cotton was sold for money.
11.A|3|Which type of work is common in the coastal region of Texas?|fishing and shipping|mountain mining only|wheat farming only|skiing|Ports and fishing fit the Gulf.
11.B|3|Why is oil drilled where it is found underground?|natural resources decide where the work happens|oil only exists in cities|oil likes mountains|oil moves by itself|Resources decide location.
11.C|3|Immigrants who came to Texas helped its economy by...|bringing new skills, labor, and businesses|stopping all farming|closing railroads|leaving the state empty|Immigration grew the workforce.
11.D|3|How did the telegraph and telephone change business in Texas?|people could share news and orders quickly|people stopped working|trade ended|farms disappeared|Faster communication helped business.
12.A|3|Caddo leaders ruled their villages by...|a chief and a council|an elected president|a king from Spain|a governor|Caddo government was led by chiefs.
12.B|3|Spanish colonial government in Texas was run by...|a king far away in Spain|Texas voters|American Indian councils|a Mexican general|The Spanish king controlled colonies.
13.A|3|The Texas Constitution is important because it...|sets up how the state government works|names the state bird|marks highways|lists recipes|It is the state's basic law.
13.B|3|Which branch of Texas government makes laws?|the legislature|the court|the governor|the mayor|The legislature writes laws.
13.B|3|Which branch of Texas government carries out laws, led by the governor?|the executive branch|the judicial branch|the legislative branch|the military|The governor leads the executive branch.
13.B|3|Which branch of Texas government decides whether laws are broken or fair?|the judicial branch|the executive branch|the legislative branch|the school board|Courts interpret the law.
13.C|3|The Bill of Rights is...|the first ten amendments to the U.S. Constitution|a Texas cookbook|a map|a river|It protects personal freedoms.
14.A|3|How many flags have flown over Texas?|six|two|ten|three|Spain, France, Mexico, Republic of Texas, Confederacy and U.S.
14.A|3|The San Jacinto Monument honors...|the Texas victory in the Texas Revolution|the railroad|a gold rush|oil workers|It marks the 1836 battle site.
14.C|3|The Pledge to the Texas Flag expresses loyalty to...|the state of Texas|a king|a city|Mexico|Texans pledge to their state.
14.D|3|Texas Independence Day is celebrated on...|March 2|July 4|December 25|June 1|It marks the 1836 declaration.
14.D|3|Juneteenth marks the day...|enslaved people in Texas learned they were free|Texas became a state|oil was found|the Alamo fell|It celebrates June 19, 1865.
15.A|3|Adina De Zavala is remembered for working to...|save the Alamo and Texas history sites|build railroads|drive cattle|find oil|She preserved historic places.
15.A|3|Clara Driscoll helped by...|buying land to save the Alamo|signing the Declaration|inventing a plow|leading an army|She gave money to protect it.
15.B|3|One way a citizen can take part in local government is to...|attend a city council meeting|ignore public issues|break laws|stay silent always|Citizens can speak at meetings.
15.C|3|A citizen has a duty in elections to...|be informed and vote|stay away|spread rumors|avoid news|Informed voting is a responsibility.
15.D|3|Barbara Jordan was a Texan who...|served in Congress and gave powerful speeches|invented the cotton gin|fought at San Jacinto|ran the King Ranch|Jordan was a leader in the U.S. House.
15.E|3|How can you contact your elected leaders?|write a letter or send an email|shout in a field|wait for them to guess|do nothing|Leaders accept messages from citizens.
15.F|3|The class votes on a field trip. Voting is a way to...|make a group decision|end a class|hide an answer|stop learning|Votes decide group choices.
16.A|3|Who is the leader of the Texas state government?|the governor|the mayor|the President|the principal|The governor leads Texas.
16.A|3|Each state has two people in the U.S. Senate called...|senators|governors|mayors|judges|Two senators represent each state.
16.B|3|Which quality is important in a good leader?|honesty|selfishness|laziness|rudeness|Honest leaders earn trust.
17.A|3|Cinco de Mayo is a celebration of...|Mexican heritage and the Battle of Puebla|the Alamo|the Boston Tea Party|the Fourth of July|It honors a Mexican victory in 1862.
17.A|3|Oktoberfest in Texas towns celebrates which heritage?|German|Chinese|Egyptian|Greek|German settlers brought the tradition.
17.B|3|Lydia Mendoza is called the "Lark of the Border" for her work in...|Tejano music|painting|farming|politics|She was a famous Mexican American singer.
18.A|3|Gail Borden is known for...|inventing condensed milk|inventing barbed wire|leading the Texas army|building the Alamo|Borden was a Texas inventor.
18.A|3|Joseph Glidden invented...|barbed wire|the telephone|the airplane|the railroad|Barbed wire helped fence ranches.
18.A|3|Michael DeBakey was a Houston doctor who...|helped develop heart surgery tools|built railroads|led cattle drives|won a war|He advanced heart surgery.
18.A|3|Millie Hughes-Fulford was a Texas scientist who...|flew in space as an astronaut|painted murals|ran for governor|led an army|She was a payload specialist on a shuttle flight.
18.B|3|How has aerospace in Texas helped society?|space research led to new technology|it ended farming|it stopped trade|it closed schools|NASA in Houston advanced science.
19.A|3|A diary written by a settler in 1850 is a...|primary source|secondary source|map legend|chart|It is a firsthand record.
19.A|3|A textbook written today about the Alamo is a...|secondary source|primary source|diary|letter from the battle|It was written long after the event.
19.B|3|Why compare a primary source and a secondary source on the same event?|to see how details and views match or differ|to skip learning|to avoid facts|to guess|Comparing reveals different details.
19.C|3|Putting events in the order they happened is called...|sequencing|ignoring|guessing|coloring|It shows chronology.
19.D|3|Which tool shows events in the order they happened over time?|a timeline|a recipe|a legend|a scale|Timelines show chronology.
19.E|3|Two people read about the same event but disagree about it. This shows different...|points of view|maps|titles|weather|People see events differently.
19.F|3|The central claim of a source is its...|main argument or point|font|page number|author's age|It is the key point.
19.G|3|When you make a claim in a report, you should add...|supporting evidence|jokes|rumors|random facts|Evidence supports the claim.
20.A|3|A map symbol key is called a...|legend|compass|scale|border|It explains the symbols.
20.A|3|The tool on a map that shows directions is the...|compass rose|title|legend|scale|It shows north, south, east and west.
20.B|3|A map that shows where most Texans live is showing...|population distribution|rainfall only|tall buildings|weather today|It shows where people live.
21.A|3|Using the correct word for "a person who brings settlers" means saying...|empresario|mayor|pilot|farmer|Use exact social studies terms.
21.B|3|In a report, supporting ideas should...|back up the main idea|change the topic|be random|be left out|Details support the main point.
21.E|3|Civil discourse means...|talking about ideas respectfully|yelling|insulting others|ignoring views|It is respectful discussion.
22.A|3|A class votes on a school rule. This is a simulation of...|democratic decision making|a monarchy|a dictator's rule|a war|Voting simulates democracy.
22.B|3|When solving a problem, what comes right after identifying it?|gather information|give up|hide it|blame someone|Research comes next.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g4_ss.jsonl'))
print("saved", len(B.out), "questions")

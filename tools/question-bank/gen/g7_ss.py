#!/usr/bin/env python3
"""Grade 7 Social Studies (TEKS 113.19.c) - Texas history. Original questions, 2-3 per assessable standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('113.19.c.', 971, own='g7_ss.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 1 Eras and dates
H('1.A', 3, "Which era in Texas history came right after the Texas Revolution?", "the Republic of Texas", ["the Civil War era", "the Great Depression", "the oil boom"], "Texas was an independent republic from 1836 to 1845.")
H('1.A', 3, "Which era includes the long ranch and trail-drive period after the Civil War?", "the Cattle Kingdom era", ["the Spanish colonial era", "the Space Age", "the New Deal"], "Cattle drives dominated Texas in the late 1800s.")
H('1.B', 3, "What happened in Texas in 1836?", "Texas declared independence and won at San Jacinto", ["Texas joined the Union", "Texas seceded from the Union", "oil was found at Spindletop"], "Independence came in 1836.")
H('1.B', 3, "What happened in 1845?", "Texas was annexed by the United States", ["Texas declared independence", "Texas left the Union", "the Alamo fell"], "Texas became the 28th state.")
H('1.B', 3, "In what year did oil gush from Spindletop?", "1901", ["1836", "1845", "1929"], "Spindletop began the Texas oil boom.")

# 2 Exploration and colonization
H('2.A', 3, "Which group lived on the Plains and followed bison herds before European colonization?", "Comanche", ["Karankawa", "Caddo farmers", "Coahuiltecan"], "Plains peoples were nomadic hunters.")
H('2.A', 3, "Which American Indian groups of East Texas built mounds and farmed corn?", "Caddo", ["Comanche", "Apache", "Karankawa"], "Caddo were farmers.")
H('2.A', 4, "Which group along the Gulf Coast lived by fishing and gathering?", "Karankawa", ["Caddo", "Comanche", "Pueblo"], "Coastal people used the sea.")
H('2.B', 3, "Which Spanish explorer was shipwrecked on the Texas coast and traveled across the region in the 1530s?", "Cabeza de Vaca", ["Stephen F. Austin", "Sam Houston", "Moses Austin"], "He wrote about the peoples of Texas.")
H('2.B', 4, "Which French explorer's failed colony near Matagorda Bay led Spain to settle East Texas?", "La Salle", ["Coronado", "Pineda", "Cortez"], "French presence alarmed Spain.")
H('2.C', 3, "What was the main goal of Spanish missions in Texas?", "to convert American Indians to Christianity and claim land", ["to mine gold", "to train armies", "to build railroads"], "Missions spread religion and Spanish control.")
H('2.C', 3, "San Antonio de Bexar was founded in 1718 as a Spanish...", "presidio and mission settlement", ["railroad stop", "oil field", "cattle market"], "It became the heart of Spanish Texas.")
H('2.D', 3, "In 1821, Mexico became an independent nation after winning independence from...", "Spain", ["France", "England", "the United States"], "The Mexican War of Independence ended Spanish rule.")
H('2.D', 4, "The Mexican Constitution of 1824 created the state of...", "Coahuila y Tejas", ["Tejas Libre", "Nueces Republic", "Lone Star State"], "Texas was joined with Coahuila.")
H('2.E', 3, "Who received the first permission to bring American settlers to Texas, though he died before doing so?", "Moses Austin", ["Sam Houston", "Santa Anna", "Davy Crockett"], "His son carried on the colony.")
H('2.E', 3, "Who is called the 'Father of Texas' for founding the first Anglo colony?", "Stephen F. Austin", ["William Travis", "Anson Jones", "Mirabeau Lamar"], "He led the Old Three Hundred.")
H('2.E', 3, "Which tejano leader supported the Texas cause and served as a leader in the Revolution?", "Jose Antonio Navarro", ["Santa Anna", "Zachary Taylor", "Jefferson Davis"], "Navarro signed the Declaration of Independence.")
H('2.F', 4, "Which best contrasts Spanish and Anglo settlement purposes in Texas?", "Spain wanted to protect borders and spread religion; Anglos mainly wanted land for farming and cotton", ["both wanted gold only", "both wanted to build railroads", "neither wanted land"], "Different motives shaped settlement.")

# 3 Revolution
H('3.A', 3, "Which law in 1830 banned further immigration from the United States into Texas?", "Law of April 6, 1830", ["Homestead Act", "Declaration of Independence", "Treaty of Velasco"], "It angered Anglo settlers.")
H('3.A', 4, "The Fredonian Rebellion of 1826 was an early dispute between settlers and...", "the Mexican government", ["the Spanish crown", "the Comanche", "the United States Army"], "It was an early sign of tension.")
H('3.B', 3, "Who commanded the Texan army and won the Battle of San Jacinto?", "Sam Houston", ["Stephen F. Austin", "William Travis", "Santa Anna"], "Houston led the final victory.")
H('3.B', 3, "Who was the Mexican president and general who led the invasion of Texas in 1836?", "Antonio Lopez de Santa Anna", ["Sam Houston", "Mirabeau Lamar", "James Fannin"], "Santa Anna led the Mexican army.")
H('3.B', 4, "Who commanded the Texan defenders at the Alamo along with James Bowie?", "William B. Travis", ["Sam Houston", "Stephen F. Austin", "Anson Jones"], "Travis wrote the famous letter asking for help.")
H('3.C', 3, "The Battle of Gonzales in 1835 began when Texans refused to hand over a...", "cannon", ["flag", "treaty", "horse"], "'Come and Take It' became the rallying cry.")
H('3.C', 4, "What happened at Goliad in March 1836?", "Texan prisoners under Fannin were executed", ["Texans won a decisive victory", "Santa Anna surrendered", "Texas was annexed"], "The Goliad massacre fueled outrage.")
H('3.C', 3, "The Battle of San Jacinto lasted about...", "eighteen minutes", ["three days", "one week", "two months"], "It was a quick and decisive Texan victory.")

# 4 Republic and statehood
H('4.A', 3, "Who was the first president of the Republic of Texas?", "Sam Houston", ["Mirabeau B. Lamar", "Anson Jones", "Stephen F. Austin"], "Houston served two nonconsecutive terms.")
H('4.A', 4, "President Lamar is known as the 'Father of Texas Education' because he promoted...", "public land set aside for schools and universities", ["a national bank", "oil drilling", "railroad subsidies"], "Lamar championed education.")
H('4.B', 3, "Why did many Texans support annexation to the United States?", "security from Mexico and relief from public debt", ["to end all trade", "to leave North America", "to become a British colony"], "Texas faced debt and threats.")
H('4.C', 3, "The U.S.-Mexican War ended with the Treaty of...", "Guadalupe Hidalgo", ["Velasco", "Paris", "Versailles"], "Mexico recognized the Rio Grande boundary.")
H('4.C', 4, "The Compromise of 1850 settled Texas's boundary dispute with...", "the New Mexico Territory", ["Louisiana", "Oklahoma", "Canada"], "Texas gave up claims for federal debt relief.")

# 5 Civil War and Reconstruction
H('5.A', 3, "What was a central reason for Texas's role in the Civil War?", "the expansion and defense of slavery", ["the invention of the cotton gin", "oil disputes", "railroad subsidies"], "Slavery was central to secession.")
H('5.B', 3, "Which battle in 1863 led Confederate troops to prevent a Union invasion at Sabine Pass?", "Battle of Sabine Pass", ["Battle of Gettysburg", "Battle of the Alamo", "Battle of San Jacinto"], "A small force turned back a larger fleet.")
H('5.B', 4, "The last land battle of the Civil War took place in Texas at...", "Palmito Ranch", ["Gonzales", "Goliad", "Gettysburg"], "It occurred after Lee's surrender.")
H('5.C', 3, "What happened in Texas on June 19, 1865, now celebrated as Juneteenth?", "enslaved people were told they were free", ["Texas joined the Union", "the Alamo fell", "oil was discovered"], "General Granger announced emancipation in Galveston.")
H('5.C', 4, "During Reconstruction in Texas, the Freedmen's Bureau helped formerly enslaved people with...", "education, work contracts and legal aid", ["oil drilling", "railroad construction", "cattle drives"], "The Bureau supported freedpeople.")

# 6 Settlement and economy
H('6.A', 3, "Which law encouraged settlers to move onto Western lands by granting 160 acres?", "the Homestead Act", ["the Compromise of 1850", "the Dawes Act", "the Missouri Compromise"], "It offered free land to farmers.")
H('6.A', 3, "Which famous Comanche leader fought to protect Texas Plains homelands?", "Quanah Parker", ["Sam Houston", "Stephen F. Austin", "Jose Navarro"], "Quanah Parker later worked for peace.")
H('6.B', 3, "Cattle drives moved herds north along which famous route from Texas to Kansas railheads?", "the Chisholm Trail", ["the Camino Real", "the Oregon Trail", "the Santa Fe Trail"], "Longhorn herds reached rail towns.")
H('6.B', 3, "The invention of barbed wire led to the end of the open range because it allowed ranchers to...", "fence their land", ["drive cattle faster", "ship oil", "plant cotton"], "Fencing closed the open range.")
H('6.C', 3, "How did railroads change Texas in the late 1800s?", "they connected towns and moved crops and cattle to markets", ["they ended farming", "they blocked trade", "they removed cities"], "Railroads boosted growth.")
H('6.D', 4, "Sharecropping and tenant farming became common after the Civil War because...", "many farmers lacked money to buy land", ["land was free for all", "cotton was banned", "railroads were closed"], "Many farmers fell into debt.")

# 7 20th century
H('7.A', 3, "How did the oil industry lead to the industrialization of Texas?", "it created refineries, jobs and new towns", ["it ended all manufacturing", "it removed cities", "it banned railroads"], "Oil attracted industry.")
H('7.B', 4, "A 'boom-and-bust' cycle in the oil industry means...", "prosperity followed by downturns as prices change", ["steady prices forever", "no demand", "permanent growth"], "Prices and production rise and fall.")
H('7.C', 3, "The Populist movement in Texas sought help mainly for...", "farmers facing high costs and debt", ["oil companies", "railroad owners", "cattle barons"], "Populists pushed for farm reforms.")
H('7.D', 3, "The League of United Latin American Citizens (LULAC), founded in Texas in 1929, worked for...", "civil rights for Mexican Americans", ["oil leases", "railroad safety", "ranching rights"], "LULAC fought discrimination.")
H('7.D', 4, "Which Texas case led the Supreme Court to end the Democratic white primary in 1944?", "Smith v. Allwright", ["Brown v. Board of Education", "Plessy v. Ferguson", "Marbury v. Madison"], "Texas voting rights were advanced.")
H('7.E', 3, "During World War II, many Texans worked in...", "defense industries such as shipbuilding and aircraft", ["Spanish missions", "cattle drives only", "mining gold"], "The war boosted industry.")
H('7.E', 3, "The Great Depression hit Texas farmers hard because...", "crop prices fell and the Dust Bowl damaged farmland", ["oil was cheap", "railroads closed", "cattle drives resumed"], "Economic collapse hurt farms.")

# 8-9 Geography
H('8.A', 3, "Which Texas region contains the Guadalupe Mountains and Big Bend?", "Mountains and Basins", ["Coastal Plains", "North Central Plains", "Great Plains"], "It is in West Texas.")
H('8.A', 3, "Which region includes the Panhandle and the Llano Estacado?", "Great Plains", ["Coastal Plains", "Mountains and Basins", "Piney Woods"], "It is a high, flat region.")
H('8.A', 3, "Which region borders the Gulf of Mexico and includes Houston?", "Coastal Plains", ["Great Plains", "Mountains and Basins", "North Central Plains"], "It is low, flat and humid.")
H('8.B', 3, "Which Texas city is a major seaport on the Gulf Coast?", "Houston", ["Lubbock", "Amarillo", "Abilene"], "Houston has a large port.")
H('8.C', 4, "How do irrigation and the Ogallala Aquifer affect the High Plains economy?", "they allow farming in a dry region but water supplies are limited", ["they stop farming", "they create oceans", "they end ranching"], "Irrigation supports crops.")
H('9.A', 3, "Building dams and reservoirs in Texas is an example of how Texans have...", "modified the environment", ["avoided the environment", "created climate", "ended droughts permanently"], "Dams store water.")
H('9.B', 3, "The 1900 Galveston Hurricane showed that...", "natural disasters can reshape settlement and the economy", ["storms never matter", "Galveston is inland", "hurricanes cannot hit Texas"], "Galveston's recovery led to a seawall and Houston's growth.")
H('9.B', 3, "The Dust Bowl damaged Texas farmland mainly because of...", "drought and poor farming practices", ["too much rain", "too many forests", "volcano eruptions"], "Soil blew away.")

# 10-12 Population and economy
H('10.A', 3, "German and Czech immigrants who came to Texas in the 1800s mainly settled in...", "Central Texas", ["the Panhandle", "East Texas swamps", "West Texas deserts"], "They built farming communities.")
H('10.A', 4, "Many Mexican immigrants came to Texas in the early 1900s to escape...", "the Mexican Revolution", ["the Civil War", "the Great Depression", "World War II"], "Violence in Mexico pushed migration.")
H('10.B', 3, "How has immigration influenced Texas culture?", "through foods, music, languages and traditions", ["by ending traditions", "by banning languages", "by eliminating cities"], "Immigrants enrich culture.")
H('10.C', 4, "Which demographic concept describes how quickly a population grows?", "growth rate", ["latitude", "elevation", "relative location"], "Growth rate measures change.")
H('10.D', 4, "Rapid population growth in Texas cities creates a need for more...", "schools, roads and water supplies", ["glaciers", "volcanoes", "deserts"], "Growth strains infrastructure.")
H('11.A', 3, "The growth of oil and railroads helped lead to the urbanization of Texas by...", "creating jobs in cities", ["closing towns", "stopping trade", "ending industry"], "Cities grew with industry.")
H('11.B', 3, "Urbanization changed Texas jobs from mostly farming to more...", "manufacturing and service jobs", ["mining only", "fishing only", "hunting only"], "Cities create diverse jobs.")
H('12.A', 3, "A decline in world oil prices would most directly affect Texas by...", "reducing income for oil workers and the state budget", ["raising cotton prices", "ending tourism", "stopping rain"], "Texas is tied to global markets.")
H('12.B', 3, "In a free enterprise system, prices in Texas stores depend on...", "supply and demand", ["a king's decision", "the weather only", "tradition alone"], "Markets set prices.")
H('12.C', 3, "The aerospace industry in Texas is closely tied to...", "NASA's Johnson Space Center in Houston", ["Spindletop", "the Chisholm Trail", "Spanish missions"], "NASA brought high-tech jobs.")

# 13-17 Government and citizenship
H('13.A', 3, "The Texas Constitution reflects limited government by...", "dividing power among branches and limiting officials", ["giving one person all power", "removing courts", "ending elections"], "Limited government protects rights.")
H('13.B', 4, "Compared to the U.S. Constitution, the Texas Constitution is...", "longer and amended more often", ["shorter and never amended", "identical", "unwritten"], "Texas's constitution is long and detailed.")
H('14.A', 3, "Which level of government in Texas manages local issues like city streets and police?", "municipal (city) government", ["federal government only", "the state Supreme Court", "the military"], "Cities handle local services.")
H('14.A', 3, "Texas counties are led by a...", "commissioners court", ["city council only", "state senate", "school board"], "County judge and commissioners govern the county.")
H('14.B', 3, "Which is a major source of revenue for Texas local governments?", "property taxes", ["lottery of land", "gold mines", "tariffs"], "Local governments rely on property taxes.")
H('14.B', 3, "Texas does not collect a state...", "personal income tax", ["sales tax", "property tax", "franchise tax"], "Texas has no personal income tax.")
H('15.A', 3, "Which is a right of Texas citizens?", "voting in elections", ["ignoring laws", "skipping jury duty", "avoiding taxes"], "Voting is a basic right.")
H('15.B', 3, "Which is a civic responsibility of Texas citizens?", "serving on a jury when called", ["littering", "ignoring elections", "disobeying laws"], "Jury duty is a civic duty.")
H('16.A', 4, "Why do political parties and interest groups hold different views on Texas issues?", "they have different values and goals", ["they share identical goals", "they do not vote", "they avoid government"], "Different groups, different priorities.")
H('16.B', 3, "Why is a free press important in a democratic society?", "it informs citizens and holds government accountable", ["it hides news", "it replaces courts", "it removes elections"], "Free press supports democracy.")
H('17.A', 3, "A leadership quality of good elected officials is...", "honesty and responsibility", ["secrecy", "avoiding voters", "ignoring laws"], "Leaders must be trustworthy.")
H('17.B', 3, "Barbara Jordan was a Texas leader known for...", "serving in the U.S. Congress and her powerful speeches", ["founding the Alamo", "leading cattle drives", "discovering oil"], "She was a civil rights leader.")
H('17.B', 3, "John Nance Garner of Uvalde served as...", "Vice President of the United States", ["Governor during the Revolution", "President of Mexico", "President of the Republic of Texas"], "He was FDR's vice president.")

# 18-19 Culture and technology
H('18.A', 3, "Which festival celebrates Texas's Czech heritage?", "Czech Fest in West or Wharton", ["Mardi Gras", "Oktoberfest only", "Cinco de Mayo only"], "Czech communities hold festivals.")
H('18.B', 3, "Many Texans maintain their heritage by celebrating...", "traditional holidays, foods and languages", ["only new holidays", "no traditions", "only government holidays"], "Heritage is kept through customs.")
H('18.C', 3, "Many Texas place names such as San Antonio and El Paso show influence from...", "Spanish", ["Dutch", "Russian", "Chinese"], "Spanish names reflect colonial history.")
H('18.D', 4, "J. Frank Dobie is known as a Texas...", "author who wrote about Texas folklore and history", ["oil baron", "general", "railroad engineer"], "Dobie wrote about Texas heritage.")
H('19.A', 3, "Which comparison shows technological change over time?", "from the telegraph to cell phones", ["from oxen to oxen", "from rain to rain", "from soil to soil"], "Technology evolves.")
H('19.B', 3, "Michael DeBakey of Houston is known for...", "pioneering heart surgery", ["inventing barbed wire", "discovering Spindletop", "leading cattle drives"], "He advanced cardiovascular medicine.")
H('19.C', 4, "Air conditioning helped the growth of Texas cities by...", "making hot summers more comfortable for living and working", ["ending storms", "removing the sun", "creating oil"], "Cooling technology supported growth.")
H('19.D', 4, "The cotton gin changed Texas agriculture by...", "speeding the processing of cotton and increasing demand for it", ["ending cotton farming", "producing oil", "replacing railroads"], "It boosted cotton production.")
H('19.E', 4, "Advances in transportation and communication have made Texas more...", "interdependent with other regions and nations", ["isolated", "independent of trade", "closed to travel"], "Technology links economies.")

# 20-23 Skills
H('20.A', 3, "A diary written by a Texas settler in 1850 is a...", "primary source", ["secondary source", "textbook", "encyclopedia"], "Firsthand account.")
H('20.A', 3, "A Texas history textbook published last year is a...", "secondary source", ["primary source", "diary", "letter from the Alamo"], "Written long after the events.")
H('20.B', 3, "Which timeline order is correct?", "Spindletop (1901), Great Depression (1929), World War II (1941)", ["World War II, Spindletop, Great Depression", "Great Depression, Spindletop, World War II", "Spindletop, World War II, Great Depression"], "Absolute chronology orders events by date.")
H('20.C', 3, "Which visual is best for comparing Texas city populations?", "a bar graph", ["a portrait", "a flag", "a lyric sheet"], "Graphs compare data.")
H('20.D', 4, "A letter written by a Mexican officer about the Alamo may differ from a Texan's account because of different...", "points of view and bias", ["fonts", "time zones", "page lengths"], "Perspective shapes accounts.")
H('20.E', 4, "Which is a claim supported by evidence?", "Railroads helped Texas grow because they connected farms and ranches to distant markets.", ["Railroads were cool.", "Texas exists.", "I like trains."], "A claim with reasoning.")
H('20.F', 3, "To judge a source about Texas history, a student should check the...", "author's credentials and evidence", ["font color", "cover size", "page number"], "Credible sources show evidence.")
H('21.A', 3, "A thematic map of Texas could show...", "annual rainfall across the state", ["only city names", "a poem", "a recipe"], "Thematic maps display data themes.")
H('21.B', 4, "A map showing most Texans living near Dallas, Houston and San Antonio helps analyze...", "population distribution", ["rainfall only", "elevation only", "ocean tides"], "Patterns show where people live.")
H('22.A', 3, "The word 'annexation' means...", "adding territory to a larger country", ["dividing a country", "ending a war", "building a dam"], "Texas was annexed by the U.S.")
H('22.B', 3, "A bibliography in a report is used to...", "list sources that were used", ["hide the author", "add a poem", "lengthen the title"], "It credits sources.")
H('22.D', 3, "Civil discourse in a debate about Texas history means...", "listening and responding respectfully", ["interrupting often", "refusing to listen", "insulting others"], "Respectful discussion.")
H('23.A', 3, "A caucus in a political process is a...", "meeting where members discuss candidates or issues", ["trial", "census", "vote of a king"], "Caucuses are part of political processes.")
H('23.B', 4, "A good decision-making process begins by...", "identifying the problem and gathering information", ["announcing the final choice", "ignoring evidence", "avoiding options"], "Define, research, consider options.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g7_ss.jsonl'))
print("saved", len(B.out), "questions")

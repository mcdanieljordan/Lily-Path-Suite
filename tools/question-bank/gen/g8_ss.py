#!/usr/bin/env python3
"""Grade 8 Social Studies (TEKS 113.20.c) - U.S. history through 1877. Original questions, 2-3 per assessable standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('113.20.c.', 972, own='g8_ss.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 1 Eras and dates
H('1.A', 3, "Which era of U.S. history came first?", "colonization", ["Reconstruction", "the Civil War", "westward expansion"], "Colonies came before independence.")
H('1.A', 3, "Which era followed the American Revolution?", "the early republic and the writing of the Constitution", ["Reconstruction", "colonization", "Manifest Destiny"], "A new government was formed.")
H('1.B', 3, "What happened in 1607?", "Jamestown was founded", ["the Mayflower landed", "the Declaration was signed", "the Civil War began"], "Jamestown was the first permanent English settlement.")
H('1.B', 3, "What happened in 1776?", "the Declaration of Independence was adopted", ["the Constitution was signed", "the Civil War began", "Jamestown was founded"], "Independence was declared.")
H('1.B', 3, "What happened in 1787?", "the Constitution was written in Philadelphia", ["the War of 1812 began", "the Civil War ended", "the Mayflower arrived"], "The Convention met in 1787.")
H('1.B', 3, "In what year did the Civil War begin?", "1861", ["1776", "1812", "1877"], "It began at Fort Sumter.")

# 2 Colonization
H('2.A', 3, "Which was a main reason Spain explored and colonized North America?", "to find gold and spread Catholicism", ["to escape the Industrial Revolution", "to build railroads", "to start factories"], "Spain sought wealth and converts.")
H('2.A', 3, "French colonists in North America were mainly interested in...", "the fur trade", ["cotton plantations", "factories", "railroads"], "Fur trapping drove New France.")
H('2.B', 4, "Which colony was founded mainly for religious freedom by the Pilgrims?", "Plymouth", ["Jamestown", "Georgia", "New Amsterdam"], "Pilgrims sought to practice their faith.")
H('2.B', 3, "Georgia was founded partly as...", "a buffer against Spanish Florida and a haven for debtors", ["a religious refuge for Quakers", "a tobacco colony", "a fur trading post"], "James Oglethorpe led it.")
H('2.B', 3, "The Middle Colonies were known for...", "religious tolerance and grain farming", ["only tobacco", "only fishing", "Catholic missions"], "Diversity and fertile farmland.")

# 3 Representative government
H('3.A', 3, "Which colonial institution gave voters a voice in Virginia's government in 1619?", "the House of Burgesses", ["the Senate", "Parliament", "the Supreme Court"], "It was the first elected assembly in English America.")
H('3.B', 3, "The Mayflower Compact was important because it...", "set up self-government by agreement of the settlers", ["declared independence", "created slavery", "ended taxes"], "Settlers agreed to make laws together.")
H('3.B', 4, "The Fundamental Orders of Connecticut are considered an early...", "written constitution", ["declaration of war", "tax law", "trade treaty"], "They set up a government by the people.")
H('3.C', 3, "How did religion contribute to representative government in the colonies?", "congregations practiced self-rule and valued virtue", ["churches banned voting", "churches were governed by kings", "religion was outlawed"], "Town meetings and church governance taught self-rule.")

# 4 Revolution
H('4.A', 3, "The Proclamation of 1763 angered colonists because it...", "banned settlement west of the Appalachians", ["raised tea taxes", "ended slavery", "created a navy"], "It limited westward expansion.")
H('4.A', 3, "'No taxation without representation' protested taxes imposed by...", "Parliament", ["colonial assemblies", "the Continental Congress", "state governors"], "Colonists had no voice in Parliament.")
H('4.A', 3, "The Stamp Act of 1765 taxed...", "printed materials such as newspapers and legal documents", ["tea only", "land only", "ships only"], "It sparked widespread protest.")
H('4.B', 3, "Who wrote most of the Declaration of Independence?", "Thomas Jefferson", ["George Washington", "Benjamin Franklin", "John Adams"], "Jefferson was the main author.")
H('4.B', 3, "Who commanded the Continental Army?", "George Washington", ["Thomas Paine", "Patrick Henry", "John Hancock"], "Washington led the army.")
H('4.C', 3, "The Battles of Lexington and Concord in 1775 were the...", "first battles of the Revolution", ["last battles of the Revolution", "start of the Civil War", "end of the French war"], "'The shot heard round the world.'")
H('4.C', 4, "Which battle in 1777 convinced France to ally with the Americans?", "Saratoga", ["Bunker Hill", "Lexington", "Gettysburg"], "Saratoga was a turning point.")
H('4.D', 4, "The Great Compromise at the Constitutional Convention created...", "a two-house Congress with equal representation in the Senate and population-based representation in the House", ["a single-house Congress", "a king", "a weak central government"], "It balanced large and small states.")
H('4.D', 4, "The Three-Fifths Compromise counted each enslaved person as...", "three-fifths of a person for representation and taxes", ["a full person", "no person", "half a person"], "It increased the South's representation.")

# 5 New republic
H('5.A', 3, "A major problem for the new republic under the Articles of Confederation was...", "paying war debts and keeping order without strong central power", ["too much federal power", "an overly strong president", "no states"], "The central government was weak.")
H('5.B', 3, "The Fugitive Slave Act of 1793 required that...", "escaped enslaved people be returned to their owners", ["enslaved people be freed", "slavery be banned in the North", "free Blacks be given land"], "It strengthened slaveholders' claims.")
H('5.C', 4, "Alexander Hamilton wanted a national bank and protective tariffs to...", "strengthen the economy and credit of the new nation", ["weaken the government", "end trade", "abolish taxes"], "He promoted manufacturing and finance.")
H('5.D', 3, "The first two political parties were the Federalists and the...", "Democratic-Republicans", ["Whigs", "Republicans", "Know-Nothings"], "Jefferson led the Democratic-Republicans.")
H('5.E', 3, "A major cause of the War of 1812 was...", "British impressment of American sailors and interference with trade", ["the Louisiana Purchase", "the cotton gin", "the Mexican War"], "Britain seized sailors and ships.")
H('5.E', 4, "A major effect of the War of 1812 was...", "a surge of American nationalism and growth in manufacturing", ["the loss of the Midwest", "the end of the Constitution", "British rule restored"], "The war boosted national pride.")
H('5.F', 3, "The Monroe Doctrine warned European nations not to...", "colonize or interfere in the Western Hemisphere", ["trade with America", "visit the U.S.", "fight in Asia"], "It declared a sphere of U.S. influence.")
H('5.G', 3, "Andrew Jackson's election in 1828 reflected the expansion of...", "suffrage to more white men without property", ["the powers of the king", "slavery's end", "voting for women"], "Voting rights widened.")
H('5.H', 4, "The Indian Removal Act led to the forced relocation of the Cherokee on the...", "Trail of Tears", ["Oregon Trail", "Santa Fe Trail", "Chisholm Trail"], "Thousands died on the forced march.")

# 6 Westward growth
H('6.A', 3, "The Northwest Ordinance of 1787 established...", "a process for new territories to become states and banned slavery there", ["a national bank", "a new tax", "a state religion"], "It guided orderly expansion.")
H('6.B', 3, "The Louisiana Purchase of 1803 doubled the size of the U.S. when it was bought from...", "France", ["Spain", "Britain", "Mexico"], "President Jefferson made the deal.")
H('6.B', 3, "Manifest Destiny was the belief that the United States was meant to...", "expand across the continent", ["avoid territory", "stay small", "give up land"], "A popular idea in the 1840s.")
H('6.C', 3, "The U.S.-Mexican War ended with the Treaty of Guadalupe Hidalgo, which gave the U.S....", "California and much of the Southwest", ["Texas only", "Florida", "Alaska"], "The Mexican Cession.")

# 7 Sectionalism
H('7.A', 4, "Northern manufacturers supported high protective tariffs, but Southern planters opposed them because...", "tariffs raised prices of goods they bought and hurt exports", ["they wanted slavery abolished", "they wanted more factories", "they opposed trade"], "Tariffs hurt the agricultural South.")
H('7.B', 4, "Which best compares enslaved people and free Blacks before the Civil War?", "free Blacks had more freedom but still faced discrimination and limited rights", ["both had full citizenship", "enslaved people could vote", "free Blacks owned plantations"], "Freedom was limited by law and custom.")
H('7.C', 3, "The Fugitive Slave Act of 1850 made it a crime to...", "help runaway enslaved people and required citizens to assist capture", ["buy land", "move west", "print newspapers"], "Northerners were forced to cooperate.")
H('7.D', 3, "Slavery was most important to the economy of which section?", "the South", ["the Northeast", "the Midwest", "New England"], "Plantations relied on enslaved labor.")
H('7.E', 3, "The Missouri Compromise of 1820 admitted Missouri as a slave state and...", "Maine as a free state", ["Texas as a slave state", "California as a free state", "Kansas as a slave state"], "It kept the balance in the Senate.")
H('7.E', 4, "The Kansas-Nebraska Act of 1854 allowed settlers to decide on slavery through...", "popular sovereignty", ["a national vote", "a presidential decision", "Supreme Court order"], "It led to 'Bleeding Kansas.'")

# 8 Civil War
H('8.A', 3, "Who was president of the Confederate States?", "Jefferson Davis", ["Abraham Lincoln", "Ulysses S. Grant", "Robert E. Lee"], "Davis led the Confederacy.")
H('8.A', 3, "Who led Union forces to victory and later became president?", "Ulysses S. Grant", ["Robert E. Lee", "Stonewall Jackson", "Jefferson Davis"], "Grant accepted Lee's surrender.")
H('8.B', 3, "What issue was central to causing sectionalism and secession?", "the expansion of slavery", ["fishing rights", "the telegraph", "railroad schedules"], "Disagreement over slavery divided the nation.")
H('8.C', 3, "The Civil War began with the firing on...", "Fort Sumter", ["Gettysburg", "Appomattox", "Harpers Ferry"], "Confederates fired in April 1861.")
H('8.C', 3, "The Battle of Gettysburg is considered a turning point because...", "it ended Lee's invasion of the North and weakened the Confederacy", ["it ended slavery by itself", "it ended the war immediately", "it was a Confederate victory that won independence"], "Union victory in July 1863.")
H('8.C', 4, "Lee surrendered to Grant at...", "Appomattox Court House", ["Fort Sumter", "Vicksburg", "Antietam"], "The war ended in April 1865.")
H('8.D', 4, "In the Gettysburg Address, Lincoln emphasized that the nation was dedicated to...", "liberty and equality and government of the people", ["secession", "kings", "isolation"], "He tied the war to the Declaration.")

# 9 Reconstruction
H('9.A', 3, "The Freedmen's Bureau was created to help...", "formerly enslaved people with education, food and legal aid", ["plantation owners", "railroad builders", "factory owners"], "It aided freedpeople.")
H('9.B', 4, "Hiram Revels was the first...", "African American U.S. senator", ["Confederate general", "president", "Chief Justice"], "He represented Mississippi.")
H('9.C', 4, "What was one problem of Reconstruction in the South?", "violence by groups such as the Ku Klux Klan against Black citizens", ["lack of rain", "too many railroads", "lack of cotton"], "White supremacist violence undermined rights.")
H('9.C', 3, "The Compromise of 1877 ended Reconstruction by...", "removing federal troops from the South", ["freeing the enslaved", "giving land to freedpeople", "abolishing the Senate"], "Federal troops left.")

# 10-11 Geography
H('10.A', 3, "Which river was the western boundary of the U.S. after the Revolution?", "the Mississippi River", ["the Rio Grande", "the Columbia River", "the Colorado River"], "The 1783 treaty set it.")
H('10.B', 3, "The Northeast was known for...", "factories and busy ports", ["cattle ranches", "rice plantations", "mining gold"], "Industry grew there.")
H('10.C', 4, "Why was the Mississippi River so important to the early U.S. economy?", "it provided a route to move goods to market", ["it blocked travel", "it was a desert", "it was too shallow"], "Rivers carried trade.")
H('11.A', 3, "Why did most early colonial towns grow near rivers and harbors?", "water provided transportation and trade", ["rivers blocked trade", "harbors were frozen", "rivers were desert"], "Physical features shaped settlement.")
H('11.B', 4, "A negative consequence of clearing forests for farmland was...", "soil erosion and loss of habitat", ["more rainfall", "fewer farms", "more forests"], "Human modification can harm the environment.")

# 12-14 Economics
H('12.A', 3, "Before the Civil War, the Northeast's economy relied mainly on...", "manufacturing and trade", ["plantation cotton", "ranching", "mining"], "Industry dominated the North.")
H('12.B', 4, "The plantation system in the South developed because of demand for cash crops such as...", "cotton and tobacco", ["wheat and oats", "steel and coal", "fish and furs"], "Cash crops needed large labor.")
H('12.C', 4, "A cause of economic differences among regions was...", "differences in climate, resources and labor systems", ["identical land", "equal factories", "the same crops"], "Geography shaped economies.")
H('13.A', 4, "An economic effect of the War of 1812 was...", "growth in American manufacturing because British goods were scarce", ["a collapse of all industry", "higher tariffs on U.S. goods", "loss of trade forever"], "Americans made more at home.")
H('13.B', 3, "What helped cause rapid industrialization in the U.S.?", "new machines, capital and available workers", ["lack of resources", "no cities", "no inventions"], "Factories needed machines and labor.")
H('14.A', 3, "Which belief helped free enterprise develop in the new nation?", "private property and the right to make a profit", ["government owns all land", "no trade", "fixed prices"], "Individual rights supported markets.")
H('14.B', 3, "A benefit of free enterprise is...", "consumers can choose among competing goods", ["a single seller", "government set prices", "no competition"], "Competition benefits buyers.")

# 15 Documents
H('15.A', 3, "The Magna Carta influenced the Constitution by establishing that...", "even the king must obey the law", ["kings are above law", "taxes cannot exist", "there are no courts"], "It limited power.")
H('15.B', 3, "A weakness of the Articles of Confederation was that Congress could not...", "tax or regulate trade", ["declare independence", "sign treaties", "elect a president"], "Congress was weak.")
H('15.C', 3, "A grievance listed in the Declaration of Independence was that the king...", "imposed taxes without consent", ["gave colonists too much freedom", "banned slavery", "created a Congress"], "Colonists objected to taxation.")
H('15.D', 4, "The separation of powers in the Constitution means...", "power is divided among three branches", ["the president rules alone", "states have no power", "Congress can do anything"], "Legislative, executive and judicial.")
H('15.E', 3, "Montesquieu influenced the Constitution with his idea of...", "separating government powers", ["a divine king", "no laws", "a state church"], "He inspired checks and balances.")

# 16 Amendments
H('16.A', 3, "Amendments to the Constitution are made to...", "change or add to the Constitution as needs change", ["erase it", "end the government", "elect a king"], "Amendments adapt the document.")
H('16.B', 3, "The 13th Amendment...", "abolished slavery", ["gave women the vote", "ended Prohibition", "created income tax"], "It ended slavery in 1865.")
H('16.B', 3, "The 14th Amendment granted...", "citizenship and equal protection to all persons born or naturalized in the U.S.", ["voting to women", "an income tax", "a two-term limit"], "It defined citizenship.")
H('16.B', 3, "The 15th Amendment protected the right to vote regardless of...", "race", ["wealth", "age", "religion"], "It targeted racial barriers to voting.")

# 17 Federalism
H('17.A', 3, "Federalists such as Alexander Hamilton supported...", "a strong national government and ratifying the Constitution", ["no constitution", "abolishing the states", "a monarchy"], "They supported ratification.")
H('17.A', 3, "Anti-Federalists feared the Constitution would...", "give too much power to the national government without a bill of rights", ["limit trade", "end elections", "eliminate states"], "They demanded a Bill of Rights.")
H('17.B', 4, "The nullification idea claimed that states could...", "reject federal laws they believed unconstitutional", ["make federal laws", "declare war on Canada", "elect the president"], "John C. Calhoun promoted it.")

# 18 Courts
H('18.A', 3, "Judicial review is the power of courts to...", "decide whether laws are constitutional", ["write laws", "veto bills", "elect judges"], "It was established in Marbury v. Madison.")
H('18.B', 4, "McCulloch v. Maryland (1819) upheld the power of...", "the federal government over the states", ["state governments over federal law", "the king", "the states to tax the bank"], "It affirmed implied powers.")
H('18.C', 4, "Dred Scott v. Sandford (1857) ruled that...", "enslaved people were not citizens and Congress could not ban slavery in the territories", ["slavery was abolished", "free Blacks were citizens", "Missouri was free"], "It inflamed sectional tensions.")

# 19-21 Citizenship
H('19.A', 3, "Unalienable rights are rights...", "that cannot be taken away", ["given by a king", "that can be bought", "that depend on wealth"], "Life, liberty and the pursuit of happiness.")
H('19.B', 3, "The First Amendment guarantees freedom of...", "religion, speech, press, assembly and petition", ["only travel", "only taxes", "only the draft"], "It protects expression.")
H('19.C', 3, "Which is an example of responsible citizenship?", "obeying laws and staying informed", ["ignoring elections", "breaking rules", "avoiding the news"], "Citizens should participate.")
H('20.A', 4, "The Founding Fathers are often called models of civic virtue because they...", "put the common good ahead of self-interest", ["only sought wealth", "avoided public service", "ignored laws"], "They sacrificed for the nation.")
H('20.B', 4, "Henry David Thoreau's civil disobedience meant...", "peacefully refusing to obey a law believed to be unjust", ["violent revolt", "obeying all laws", "fleeing the country"], "He went to jail rather than pay a tax.")
H('21.A', 3, "Why did Federalists and Democratic-Republicans disagree?", "they had different views on the role of the national government", ["they wanted the same things", "they never debated", "they supported kings"], "Parties form around beliefs.")
H('21.B', 3, "A free press in a constitutional republic helps citizens...", "get information and hold leaders accountable", ["avoid news", "elect kings", "avoid laws"], "Free press protects democracy.")
H('21.C', 3, "The Missouri Compromise is an example of a...", "compromise that resolved a conflict", ["war", "treaty with France", "tax law"], "Congress balanced slave and free states.")

# 22 Leaders
H('22.A', 3, "Abraham Lincoln showed leadership during the Civil War by...", "preserving the Union and issuing the Emancipation Proclamation", ["surrendering to the Confederacy", "ending the Constitution", "dissolving Congress"], "He led the Union.")
H('22.B', 3, "Harriet Tubman is remembered for...", "leading enslaved people to freedom on the Underground Railroad", ["inventing the telegraph", "leading the Confederate army", "drafting the Constitution"], "She conducted many rescues.")
H('22.B', 3, "Frederick Douglass was a former slave who became a leading...", "abolitionist writer and speaker", ["Confederate general", "plantation owner", "king's governor"], "He fought for abolition.")

# 23 Groups and conflicts
H('23.A', 3, "Many Irish immigrants came to the U.S. in the 1840s to escape...", "the potato famine", ["the Civil War", "the Cold War", "the Dust Bowl"], "Crop failure drove migration.")
H('23.B', 4, "Rapid urbanization led to conflict in cities partly because of...", "competition for jobs and religious and cultural differences", ["lack of people", "no immigrants", "no factories"], "Cities were crowded.")
H('23.C', 3, "Which helped immigrants adapt to life in a new country?", "community organizations and shared languages", ["isolation", "banning newspapers", "closing schools"], "Support networks helped.")
H('23.D', 3, "German immigrants contributed to American life by...", "farming, brewing and founding schools and newspapers", ["building pyramids", "inventing the telegraph", "ending slavery alone"], "They enriched American culture.")
H('23.E', 3, "Which woman was a leader of the women's suffrage movement and helped organize the Seneca Falls Convention?", "Elizabeth Cady Stanton", ["Dolley Madison", "Betsy Ross", "Sacagawea"], "Seneca Falls took place in 1848.")

# 24 Reform
H('24.A', 3, "William Lloyd Garrison published an antislavery newspaper called...", "The Liberator", ["The Gazette", "The Tribune", "The Federalist"], "He called for immediate abolition.")
H('24.B', 3, "Horace Mann is known for promoting...", "public education reform", ["railroad building", "cotton farming", "the telegraph"], "He championed common schools.")
H('24.B', 4, "The temperance movement sought to...", "reduce or ban the use of alcohol", ["end slavery", "build railroads", "expand voting"], "Reformers viewed alcohol as harmful.")

# 25 Religion
H('25.A', 3, "The First Amendment protects religious freedom by...", "barring Congress from establishing a state religion", ["requiring one church", "banning all religion", "taxing churches"], "Religion is free from government control.")
H('25.B', 4, "The Second Great Awakening encouraged many people to join...", "reform movements such as abolition and temperance", ["the military only", "the Confederacy only", "the king's court"], "Religious revival fueled reform.")
H('25.C', 3, "Religious freedom in America attracted immigrants such as...", "Quakers and Jews seeking to worship without persecution", ["people who wanted a king", "people who banned worship", "only soldiers"], "Freedom drew many groups.")

# 26 Arts
H('26.A', 3, "The Hudson River School painters celebrated...", "the beauty of the American landscape", ["industrial machines", "foreign kings", "wartime battles"], "A group of 19th-century landscape painters.")
H('26.A', 4, "Which writer wrote 'Uncle Tom's Cabin,' influencing attitudes about slavery?", "Harriet Beecher Stowe", ["Louisa May Alcott", "Emily Dickinson", "Edgar Allan Poe"], "The novel stirred antislavery feeling.")
H('26.B', 4, "Spirituals sung by enslaved people reflect...", "faith, hope and coded messages about freedom", ["only factory work", "wealth", "royal court life"], "Music expressed resilience.")

# 27-28 Technology
H('27.A', 3, "The steamboat changed transportation by...", "making river travel faster and upstream trade possible", ["slowing travel", "ending trade", "closing rivers"], "Robert Fulton's steamboat improved shipping.")
H('27.A', 3, "The cotton gin increased the demand for enslaved labor because it...", "made growing cotton far more profitable", ["abolished cotton", "ended plantations", "freed workers"], "Eli Whitney's invention boosted cotton.")
H('27.B', 4, "The use of interchangeable parts changed manufacturing by...", "allowing goods to be made faster and cheaper", ["stopping factories", "ending jobs", "making hand tools required"], "Mass production grew.")
H('27.C', 4, "The railroad helped economic growth by...", "linking markets and speeding the movement of goods", ["slowing trade", "stopping towns", "ending farming"], "Rail networks connected regions.")
H('28.A', 3, "The telegraph changed communication by...", "sending messages quickly over long distances", ["slowing mail", "ending newspapers", "banning letters"], "Samuel Morse's invention sped news.")
H('28.B', 3, "Industrialization changed life in the United States by...", "moving many people from farms to factory jobs in cities", ["ending trade", "stopping immigration", "ending cities"], "Workers moved to cities.")

# 29-31 Skills
H('29.A', 3, "A letter written by a Civil War soldier is a...", "primary source", ["secondary source", "textbook", "encyclopedia"], "Firsthand account.")
H('29.A', 3, "A modern biography of Abraham Lincoln is a...", "secondary source", ["primary source", "diary", "speech he gave"], "Written long after.")
H('29.B', 3, "Which events are in the correct order?", "Declaration of Independence, Constitution, Civil War", ["Civil War, Constitution, Declaration of Independence", "Constitution, Civil War, Declaration of Independence", "Civil War, Declaration of Independence, Constitution"], "Chronological order.")
H('29.C', 3, "Which visual best shows the number of free and slave states over time?", "a line graph or chart", ["a poem", "a portrait", "a recipe"], "Charts show change over time.")
H('29.D', 4, "A newspaper from the South and a newspaper from the North describe the same election differently. This shows...", "different points of view", ["different alphabets", "identical biases", "no opinion"], "Perspective shapes reporting.")
H('29.E', 4, "Which is a claim supported by evidence?", "The cotton gin increased slavery because it made cotton far more profitable.", ["Cotton was nice.", "The gin exists.", "I like cotton."], "A claim with reasoning.")
H('29.F', 3, "To evaluate a historical source, a student should consider the...", "author's purpose and perspective", ["font size", "cover color", "page length"], "Evaluate credibility and bias.")
H('29.G', 3, "A thematic map of the U.S. in 1860 could show...", "which states allowed slavery", ["only rivers", "only deserts", "only stars"], "Maps display themes.")
H('29.H', 3, "A population map of the 1850 U.S. shows most people living in...", "the East", ["the Pacific Coast", "the Great Plains", "the Rocky Mountains"], "Settlement began along the Atlantic.")
H('30.A', 3, "The term 'abolition' means...", "ending slavery", ["starting a war", "raising taxes", "building railroads"], "Abolitionists wanted to end slavery.")
H('30.B', 3, "A footnote in a report is used to...", "credit a source or add a note", ["hide the author", "lengthen the title", "add a poem"], "Footnotes cite sources.")
H('30.D', 3, "Civil discourse in a debate means...", "respectfully listening and responding", ["interrupting", "insulting", "refusing to speak"], "Civil conversation is respectful.")
H('31.A', 3, "A caucus is a meeting where...", "party members choose candidates", ["judges decide cases", "soldiers train", "citizens pay taxes"], "Caucuses are part of the political process.")
H('31.B', 4, "Which step comes first when solving a problem?", "identify the problem", ["announce a decision", "ignore information", "stop researching"], "Define the problem first.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g8_ss.jsonl'))
print("saved", len(B.out), "questions")

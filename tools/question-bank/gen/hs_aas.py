import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('113.51.c.', 1006, own='hs_aas.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('1.A',3,"The Kingdom of Kush, which built pyramids at Meroë, was located in what region?",
  "Along the Nile River south of Egypt",["The Arctic","The Andes Mountains","Western Europe"],"Kush was a major African civilization that rivaled Egypt.")
H('1.A',3,"Mansa Musa of the Mali Empire became famous in the 1300s for doing what?",
  "Making a pilgrimage to Mecca with enormous amounts of gold",["Leading the Spanish conquest","Founding Jamestown","Inventing the printing press"],"His wealth made Mali known across the world.")
H('1.B',3,"Which pre-colonial African institution was a center of learning in the city of Timbuktu?",
  "The University of Sankore",["Harvard","The Library of Congress","The Hull House"],"Timbuktu was a center of scholarship.")
H('1.B',3,"The trans-Saharan trade linked West Africa to North Africa mainly through the exchange of what?",
  "Gold and salt",["Cotton and tobacco","Silk and tea","Oil and steel"],"Caravans crossed the desert carrying goods.")
H('1.C',3,"Enslaved Africans were treated as property rather than people. This is an example of what?",
  "Dehumanization",["Emancipation","Assimilation","Migration"],"Slavery denied the humanity of enslaved people.")
H('1.C',3,"Roughly how many Africans were forcibly carried across the Atlantic during the slave trade?",
  "More than 12 million",["About 12,000","About 120,000","About 1 million"],"Millions were taken over four centuries.")
H('2.A',3,"The African diaspora refers to what?",
  "The dispersal of African peoples and their descendants around the world",["A West African empire","A type of music","An ancient language"],"The slave trade created much of the diaspora.")
H('2.A',3,"European slave traders often obtained captives by doing what?",
  "Trading goods for captives at coastal ports and forts",["Planting crops in Africa","Building universities","Signing peace treaties"],"Some African rulers and merchants took part in the trade.")
H('2.B',3,"Large sugar plantations in the Caribbean depended heavily on what?",
  "The labor of enslaved Africans",["Machines only","Free workers only","Paid European tenants only"],"Sugar was extremely profitable and labor intensive.")
H('2.B',3,"Maroon communities in the Americas were formed by whom?",
  "Escaped enslaved people, sometimes allied with Native Americans",["European kings","Spanish priests","Mexican generals"],"They were settlements of freedom.")
H('2.C',3,"The Middle Passage was what?",
  "The forced voyage across the Atlantic for captive Africans",["A trade route in Asia","A railroad","A mountain pass"],"It was brutal and deadly.")
H('2.C',3,"The shared suffering of the Middle Passage led captives of different groups to do what?",
  "Create new common cultural forms and bonds",["Return home","Forget all traditions","Speak a single African language only"],"New African American culture emerged.")
H('2.D',3,"Which factor encouraged the growth of slavery in the Southern colonies?",
  "Labor-intensive cash crops such as tobacco, rice and indigo",["Large factories","A lack of land","Cheap machines"],"Plantations needed a large labor force.")
H('2.D',3,"The first documented Africans in English North America arrived at Jamestown in which year?",
  "1619",["1492","1776","1865"],"They arrived in Virginia.")
H('3.A',3,"Which was an economic argument used to defend slavery after independence?",
  "That the cotton economy depended on enslaved labor",["That slavery was cheap for the North only","That slavery would end soon","That slaves paid taxes"],"Economic interests were central to the defense of slavery.")
H('3.A',3,"Some slaveholders used religion to defend slavery by doing what?",
  "Selectively citing scripture to justify the system",["Rejecting all religion","Freeing the enslaved","Funding abolition"],"This was one of several rationalizations.")
H('3.B',3,"The Three-Fifths Compromise counted each enslaved person as what?",
  "Three-fifths of a person for representation and taxation",["A full citizen","Zero persons","Two-thirds of a person"],"It increased Southern political power.")
H('3.B',3,"The Fugitive Slave Act of 1850 required what?",
  "That people in free states help return escaped enslaved people",["That slavery end","That fugitives be paid","That Congress meet monthly"],"It angered many Northerners.")
H('3.C ',3,"Disputes over slavery in new territories increased sectionalism because what?",
  "The North and South disagreed about expanding slavery",["Everyone agreed","Slavery was banned","The territories were too small"],"The Missouri Compromise of 1820 tried to balance the sections.")
H('3.C ',3,"Which best describes sectionalism?",
  "Loyalty to one region's interests over those of the nation",["Loyalty to a political party","Hatred of travel","Support for tariffs only"],"Slavery deepened the divide between North and South.")
H('3.D',3,"Which event was a major armed rebellion by enslaved people in Virginia in 1831?",
  "Nat Turner's Rebellion",["The Whiskey Rebellion","Shays' Rebellion","The Boston Massacre"],"It led to harsher slave codes.")
H('3.D',3,"The Underground Railroad helped enslaved people by doing what?",
  "Providing secret routes and safe houses to reach freedom",["Building trains","Selling land","Printing money"],"Conductors such as Harriet Tubman guided many.")
H('3.E',3,"David Walker's Appeal (1829) called on Black Americans to do what?",
  "Resist slavery and demand freedom",["Stay silent","Move to Europe","Support slavery"],"It was a powerful abolitionist pamphlet.")
H('3.E',3,"Sojourner Truth is known as a speaker who did what?",
  "Advocated for abolition and women's rights",["Led the Confederate army","Invented the cotton gin","Signed the Constitution"],"She was formerly enslaved.")
H('3.F',3,"Great Britain abolished slavery throughout most of its empire in which year?",
  "1833",["1607","1776","1900"],"The Slavery Abolition Act passed in 1833.")
H('3.F',3,"The U.S. ban on importing enslaved Africans took effect in which year?",
  "1808",["1776","1861","1920"],"The Constitution allowed Congress to end the trade after 1808.")
H('4.A',3,"The 54th Massachusetts Infantry was significant because it was what?",
  "One of the first Black regiments to fight in the Civil War",["A Confederate unit","A Spanish colonial unit","A World War I unit"],"Its attack on Fort Wagner showed Black soldiers' courage.")
H('4.A',3,"Harriet Tubman served the Union during the Civil War as what?",
  "A scout, nurse and spy",["A Confederate general","A senator","A newspaper owner"],"She guided the Combahee River Raid.")
H('4.B',3,"A success of Reconstruction was what?",
  "The passage of the 13th, 14th and 15th Amendments",["The end of racism","Land for all freedpeople","Equal wages"],"The amendments extended rights.")
H('4.B',3,"A failure of Reconstruction was that it did what?",
  "Ended in 1877 with federal troops withdrawn and rights eroded",["Gave land to all","Banned the KKK permanently","Created integrated schools nationwide"],"Southern governments rolled back gains.")
H('4.C ',3,"Booker T. Washington's Atlanta Compromise speech urged Black Americans to do what?",
  "Focus on vocational training and economic progress",["Demand immediate full equality","Return to Africa","Reject education"],"Du Bois disagreed with this approach.")
H('4.C ',3,"Ida B. Wells became known for doing what?",
  "Investigating and writing against lynching",["Founding Tuskegee","Leading troops","Writing the 14th Amendment"],"She was a journalist and activist.")
H('4.D',3,"The Colfax Massacre of 1873 occurred in which state?",
  "Louisiana",["Maine","Oregon","Ohio"],"Dozens of Black men were killed in a political dispute.")
H('4.D',3,"The Camp Logan Mutiny of 1917 took place in which Texas city?",
  "Houston",["Dallas","El Paso","Austin"],"Black soldiers clashed after police abuse.")
H('4.E',3,"The convict leasing system allowed states to do what?",
  "Lease prisoners to private businesses for labor",["Pay prisoners high wages","Free prisoners","Close prisons"],"It often replaced slavery's labor in practice.")
H('4.E',3,"In 2018, remains found in Sugar Land, Texas, were identified as those of whom?",
  "Black convict laborers known as the Sugar Land 95",["Spanish settlers","Civil War soldiers","Railroad workers"],"They were leased convicts who died in the 1800s.")
H('4.F',3,"Jim Crow laws required what?",
  "Separation of Black and white people in public life",["Equal schools for all","Voting rights for all","Integrated housing"],"They enforced segregation.")
H('4.F',3,"Literacy tests and poll taxes were used to do what?",
  "Keep Black citizens from voting",["Raise school funds","Register all voters","Reduce taxes"],"They were tools of disfranchisement.")
H('4.G',3,"Plessy v. Ferguson (1896) upheld what doctrine?",
  "Separate but equal",["One person, one vote","Equal protection for all","Freedom of the press"],"It allowed legal segregation.")
H('4.G',3,"Plessy v. Ferguson was later overturned in public education by what case?",
  "Brown v. Board of Education",["Marbury v. Madison","Dred Scott v. Sandford","Gideon v. Wainwright"],"Brown was decided in 1954.")
H('4.H',3,"Which organization, founded in 1909, fought segregation through the courts?",
  "The NAACP",["The Ku Klux Klan","The Confederate Army","The Federal Reserve"],"W. E. B. Du Bois helped found it.")
H('4.H',3,"The Great Migration was a response to Jim Crow because many Black Southerners chose to do what?",
  "Move to Northern and Western cities for jobs and safety",["Stay on farms","Move to Mexico","Join the army"],"They sought opportunity.")
H('4.I',3,"The 369th Infantry, known as the Harlem Hellfighters, did what in World War I?",
  "Fought with French forces and earned honors",["Refused to fight","Served only in the U.S.","Guarded prisoners only"],"They were praised for bravery.")
H('4.I',3,"After World War I, many Black veterans returned to what?",
  "Continued discrimination and violence at home",["Full equality","A hero's welcome everywhere","Free land"],"The Red Summer of 1919 saw racial violence.")
H('4.J',3,"The Buffalo Soldiers were what?",
  "Black regiments of the U.S. Army that served after the Civil War",["Confederate spies","A baseball team","A farm union"],"They served on the western frontier.")
H('4.J',3,"Which units were Buffalo Soldier cavalry regiments?",
  "The 9th and 10th Cavalry",["The 54th and 55th Infantry","The 1st and 2nd Marines","The 761st Tank Battalion"],"They also included the 24th and 25th Infantry.")
H('5.A',3,"A negative effect of the Great Depression on African Americans was that they often what?",
  "Faced higher unemployment than white workers",["Gained wealth","Left the country","Lost no jobs"],"They were often the last hired and first fired.")
H('5.A',3,"A positive effect of the New Deal on many African Americans was what?",
  "Jobs through programs such as the WPA and CCC",["The end of segregation","Guaranteed equal pay","Free land"],"Yet many programs discriminated.")
H('5.B',3,"Sweatt v. Painter (1950) concerned what?",
  "A Black applicant denied admission to the University of Texas Law School",["Voting rights","A bus boycott","Fair housing"],"The Court found the separate school unequal.")
H('5.B',3,"Brown v. Board of Education (1954) ruled that what was unconstitutional?",
  "Segregation in public schools",["School prayer","Voting by mail","Taxes"],"The Court said separate was inherently unequal.")
H('5.C',3,"Rosa Parks' refusal to give up her bus seat in 1955 helped start what?",
  "The Montgomery Bus Boycott",["The March on Washington","The Civil War","The Great Migration"],"The boycott lasted over a year.")
H('5.C',3,"The Little Rock Nine were students who did what?",
  "Integrated Central High School in Arkansas in 1957",["Founded the NAACP","Led a bus boycott","Founded Tuskegee"],"Daisy Bates mentored them.")
H('5.D',3,"Leaders of the U.S. civil rights movement drew inspiration from independence movements in what?",
  "Africa and India",["Antarctica","Greenland","Australia"],"Examples include Ghana and Gandhi's nonviolence.")
H('5.D',3,"Pan-Africanism emphasized what?",
  "Unity among people of African descent worldwide",["Colonial rule","Isolation","Segregation"],"It connected diaspora struggles.")
H('5.E',3,"During World War II, the U.S. armed forces were what?",
  "Segregated by race",["Fully integrated","Reserved for whites only by law","Closed to women"],"Black soldiers often served in separate units.")
H('5.E',3,"The \"Double V\" campaign called for victory over what?",
  "Fascism abroad and racism at home",["Two football teams","Two political parties","Two nations"],"It was promoted by the Pittsburgh Courier.")
H('5.F',3,"Doris \"Dorie\" Miller received the Navy Cross for his actions at what event?",
  "Pearl Harbor",["The Battle of Gettysburg","D-Day","Iwo Jima"],"He manned an anti-aircraft gun.")
H('5.F',3,"The Tuskegee Airmen were the first what?",
  "Black military pilots in the U.S. Army Air Forces",["Navy admirals","Marines","Astronauts"],"They trained in Alabama.")
H('5.G ',3,"Executive Order 9981 (1948) did what?",
  "Ordered the desegregation of the U.S. armed forces",["Banned poll taxes","Created Medicare","Ended school segregation"],"President Truman signed it.")
H('5.G ',3,"A. Philip Randolph is known for threatening what in 1941?",
  "A march on Washington to protest discrimination in defense jobs",["A general strike by soldiers","A boycott of baseball","A tax revolt"],"President Roosevelt issued an order banning discrimination in defense industries.")
H('5.H',3,"Sit-ins at lunch counters, beginning in Greensboro in 1960, were what?",
  "Nonviolent protests against segregated service",["Military operations","Court cases","Tax strikes"],"They spread across the South.")
H('5.H',3,"The Voting Rights Act of 1965 was a success because it did what?",
  "Outlawed practices that kept Black citizens from voting",["Ended school segregation","Created Social Security","Banned unions"],"Black voter registration rose sharply.")
H('5.I',3,"One way the Civil Rights Movement transformed American politics was by doing what?",
  "Increasing Black voting and the number of Black elected officials",["Ending all inequality","Abolishing political parties","Eliminating elections"],"Gains were significant but incomplete.")
H('5.I',3,"A limit on the Civil Rights Movement's success is that what remained?",
  "Disparities in wealth, housing and education",["Segregation laws everywhere","No Black voters","No Black elected officials"],"Evaluating success includes ongoing gaps.")
H('6.A',3,"Which is an issue in the continuing effort to achieve equality?",
  "Unequal access to housing, health care and education",["Equal wealth","A lack of jobs for everyone","Perfect equality"],"Gaps persist.")
H('6.A',3,"Voting rights remain an issue because of debates over what?",
  "Voter identification and access to polling places",["Whether voting exists","Tax rates","School lunches"],"Policies affect participation.")
H('6.B',3,"Shirley Chisholm is known as the first Black woman to do what?",
  "Be elected to the U.S. Congress",["Command a ship","Win a Nobel Prize","Fly a plane"],"She also ran for president in 1972.")
H('6.B',3,"Fannie Lou Hamer is remembered for doing what?",
  "Fighting for voting rights in Mississippi",["Founding Ebony","Flying planes","Winning boxing titles"],"She co-founded the Mississippi Freedom Democratic Party.")
H('6.C',3,"Since 1970, a notable change in the African American community has been what?",
  "Growth in college attendance and Black elected officials",["Elimination of all inequality","A halt in migration","A ban on voting"],"Progress coexists with challenges.")
H('6.C',3,"A continuing challenge since 1970 is the gap in what?",
  "Household wealth between Black and white families",["Eye color","Shoe size","Hair length"],"The racial wealth gap persists.")
H('7.A',3,"Which is an example of forced migration in African American history?",
  "The Atlantic slave trade",["The Great Migration","The move to college","Retirement"],"The Great Migration was voluntary.")
H('7.A',3,"Which is an example of voluntary migration?",
  "The Great Migration to Northern cities",["The Middle Passage","Slave auctions","Convict leasing"],"People chose to move for opportunity.")
H('7.B',3,"Which geographic factor helped the plantation system grow in the South?",
  "A warm climate and fertile soil for cotton, tobacco and rice",["Arctic cold","Desert","Mountains"],"Geography shaped the economy.")
H('7.B',3,"Northern textile mills depended on the South because they did what?",
  "Processed cotton grown by enslaved labor",["Sold machines to Africa","Grew rice","Mined coal only"],"The regions' economies were interdependent.")
H('7.C',3,"The Exodusters were African Americans who moved to which state in the late 1870s?",
  "Kansas",["Maine","Hawaii","Florida"],"They sought land and freedom.")
H('7.C',3,"The Great Migration changed Northern cities by doing what?",
  "Increasing Black populations and political influence",["Emptying them","Ending industry","Reducing diversity"],"Cities such as Chicago grew.")
H('7.D',3,"Urban renewal and highway construction often affected Black neighborhoods by doing what?",
  "Displacing residents and dividing communities",["Increasing property values for all","Building schools","Ending segregation"],"Many Black neighborhoods were cut apart.")
H('7.D',3,"The 1927 Mississippi River flood contributed to Black migration because it did what?",
  "Destroyed farms and pushed families north",["Created new farms","Ended sharecropping","Raised wages"],"It displaced many tenant farmers.")
H('8.A',3,"The cotton gin (1793) increased demand for enslaved labor because it did what?",
  "Made cotton much more profitable to grow",["Replaced all workers","Made cotton worthless","Ended plantations"],"Eli Whitney invented it.")
H('8.A',3,"\"King Cotton\" refers to what?",
  "The central role of cotton in the economy of the South and the world",["A British monarch","A card game","A sports team"],"Cotton was the top export.")
H('8.B',3,"Sharecropping trapped many Black farmers in what?",
  "A cycle of debt to landowners",["Wealth","Free land","Higher wages"],"Crop shares barely covered costs.")
H('8.B',3,"Redlining limited economic opportunity by doing what?",
  "Denying loans and insurance to residents of Black neighborhoods",["Increasing home values","Raising wages","Building schools"],"It blocked homeownership and wealth building.")
H('8.C',3,"Which factors contributed to the Great Migration?",
  "Poor wages, racist violence and jobs in Northern factories",["High Southern wages","Equal rights in the South","Free land in Africa"],"Push and pull factors drove movement.")
H('8.C',3,"The boll weevil contributed to migration by doing what?",
  "Destroying cotton crops and farm income",["Raising cotton prices","Creating jobs","Ending segregation"],"It devastated Southern agriculture.")
H('8.D',3,"The Brotherhood of Sleeping Car Porters, led by A. Philip Randolph, was significant because it did what?",
  "Became the first Black-led union to win a contract with a major company",["Ended Jim Crow","Created Social Security","Founded the NAACP"],"It organized Pullman porters.")
H('8.D',3,"Many unions in the early 1900s hurt Black workers by doing what?",
  "Excluding them from membership",["Hiring them first","Paying them more","Teaching them for free"],"Exclusion limited access to skilled jobs.")
H('8.E',3,"Which factor can influence economic mobility?",
  "Family wealth and educational opportunity",["Birthday month","Shoe size","Favorite color"],"These affect opportunities.")
H('8.E',3,"Colorism refers to what?",
  "Discrimination based on skin tone within and across groups",["A type of paint","A farming method","A music style"],"Skin tone has affected opportunity.")
H('8.F',3,"Buy Black campaigns and boycotts are examples of what?",
  "Economic approaches to address inequality",["Military tactics","Voting methods","School subjects"],"They use spending power.")
H('8.F',3,"Black-owned banks and insurance companies helped communities by doing what?",
  "Providing credit and services when others refused",["Closing neighborhoods","Raising taxes","Printing newspapers"],"They filled gaps left by discrimination.")
H('8.G',3,"Madam C. J. Walker built a business empire in what industry?",
  "Hair care and beauty products",["Railroads","Steel","Oil"],"She became one of the first self-made female millionaires.")
H('8.G',3,"Johnson Publishing Company, founded by John H. Johnson, produced which magazines?",
  "Ebony and Jet",["Time and Life","Vogue and Elle","Wired and Mad"],"They celebrated Black life.")
H('8.H',3,"Black Wall Street was the nickname for a thriving business district in what city?",
  "Tulsa, Oklahoma",["Houston, Texas","Boston, Massachusetts","Denver, Colorado"],"The Greenwood district was destroyed in 1921.")
H('8.H',3,"Garrett Morgan is known for inventing what?",
  "An early traffic signal and a safety hood",["The telephone","The light bulb","The airplane"],"His inventions improved safety.")
H('9.A',3,"Free Black people in the late 1700s petitioned for freedom by citing what?",
  "The Declaration of Independence's claim that all men are created equal",["The Articles of Confederation","The Bill of Rights","The Monroe Doctrine"],"They used its ideals to challenge slavery.")
H('9.A',3,"Benjamin Banneker wrote to Thomas Jefferson to do what?",
  "Urge him to see Black people as equals and end slavery",["Ask for money","Offer him land","Request a government job"],"He challenged Jefferson's views.")
H('9.B',3,"Before 1877, which region generally gave Black men more voting rights?",
  "Some Northern states",["The Deep South","The Confederacy","Texas"],"Rights varied widely by region.")
H('9.B',3,"The Seneca Falls Convention of 1848 addressed the rights of whom?",
  "Women",["Immigrants only","Soldiers only","Farmers only"],"Black abolitionists such as Frederick Douglass attended.")
H('9.C',3,"The 13th Amendment did what?",
  "Abolished slavery except as punishment for a crime",["Granted women the vote","Created citizenship","Banned alcohol"],"The exception led to convict leasing.")
H('9.C',3,"The 15th Amendment prohibited denial of the vote based on what?",
  "Race, color or previous servitude",["Age","Gender","Property"],"It was ratified in 1870.")
H('9.D',3,"Smith v. Allwright (1944), a Texas case, ended what practice?",
  "The all-white Democratic primary",["School segregation","Poll taxes","Convict leasing"],"The Court ruled it unconstitutional.")
H('9.D',3,"During the 1920s-1950s, anti-lynching bills in Congress were what?",
  "Repeatedly blocked by Southern senators",["Quickly passed","Never proposed","Signed in 1925"],"Federal law did not pass until much later.")
H('9.E',3,"The Fair Housing Act of 1968 prohibited what?",
  "Discrimination in the sale and rental of housing",["School prayer","Poll taxes","Segregated buses"],"It was passed after King's assassination.")
H('9.E',3,"Affirmative action policies aimed to do what?",
  "Increase opportunities for underrepresented groups in education and employment",["Remove all admissions","End voting","Ban hiring"],"They remain debated.")
H('9.F',3,"In Shelby County v. Holder (2013), the Supreme Court did what?",
  "Struck down a key formula in the Voting Rights Act",["Ended segregation","Created the NAACP","Legalized slavery"],"It limited preclearance requirements.")
H('9.F',3,"Changes in the political environment affect civil rights because they do what?",
  "Influence which laws are passed, enforced or struck down",["Make laws permanent","Stop elections","End court cases"],"Policy shifts matter.")
H('10.A',3,"The Freedom Riders of 1961 did what?",
  "Rode interstate buses to challenge segregation in the South",["Founded the NAACP","Led a farm strike","Flew planes"],"Black and white riders traveled together.")
H('10.A',3,"The 1968 Memphis sanitation workers' strike connected civil rights and what?",
  "Labor rights and economic justice",["Space exploration","Sports","Foreign trade"],"Dr. King was there when he was assassinated.")
H('10.B',3,"Martin Luther King Jr. promoted which philosophy?",
  "Nonviolent resistance",["Armed rebellion","Isolation","Secession"],"He was influenced by Gandhi.")
H('10.B',3,"Black Power in the late 1960s emphasized what?",
  "Racial pride, self-determination and community control",["Assimilation only","Separation by law","Colonial rule"],"It energized a new generation.")
H('10.C',3,"Hiram Revels was the first African American to do what?",
  "Serve in the U.S. Senate",["Be elected President","Win a Nobel Prize","Command an army"],"He represented Mississippi in 1870.")
H('10.C',3,"Barbara Jordan was a Texan who was elected to what?",
  "The U.S. House of Representatives",["The Supreme Court","The Presidency","The Senate of Texas only"],"She was a powerful speaker during the Watergate hearings.")
H('11.A',3,"The Dred Scott decision (1857) held that what?",
  "Black people were not U.S. citizens and had no rights the government must respect",["Slavery was illegal","Black people were citizens","Slaves could vote"],"It was later overturned by the 14th Amendment.")
H('11.A',3,"The 14th Amendment changed the status of African Americans by doing what?",
  "Granting citizenship and equal protection",["Ending the Civil War","Giving land","Abolishing taxes"],"It overturned Dred Scott.")
H('11.B',3,"Regional differences shaped political perspectives because Black communities in the North and South did what?",
  "Faced different laws, opportunities and risks",["Had identical experiences","Never communicated","Lived in the same conditions"],"Context shaped strategies.")
H('11.B',3,"Rural Southern communities and Northern urban communities often differed in what?",
  "Access to voting, jobs and organizations",["Time zones","Language","Weather"],"These differences influenced politics.")
H('11.C',3,"The term \"Negro\" was widely used until which period?",
  "The 1960s",["The 1700s","The 1500s","The 2020s"],"\"Black\" gained popularity with the Black Power movement.")
H('11.C',3,"The term \"African American\" gained popularity in the 1980s, in part through whom?",
  "Civil rights leader Jesse Jackson",["Booker T. Washington","W. E. B. Du Bois","Harriet Tubman"],"It emphasized heritage.")
H('11.D',3,"A contemporary issue that has led to diverse viewpoints in public discourse is what?",
  "Policing and criminal justice reform",["Gravity","Photosynthesis","Plate tectonics"],"People discuss it with different perspectives.")
H('11.D',3,"Activism today often uses which tools?",
  "Social media, protests and voting drives",["Only telegrams","Only newspapers","Only pamphlets"],"Technology has changed activism.")
H('11.E',3,"Afro-Latinos are people who do what?",
  "Have African ancestry and Latin American heritage",["Come only from Europe","Come only from Asia","Have no ancestry"],"Examples include Afro-Cubans and Afro-Brazilians.")
H('11.E',3,"The African American community also includes what group?",
  "Recent immigrants from Africa and the Caribbean",["Only Southerners","Only descendants of enslaved people","Only city residents"],"Black America is diverse.")
H('12.A',3,"De facto segregation is segregation that occurs because of what?",
  "Social customs and housing patterns, not law",["Court orders","Constitutional rules","Treaties"],"De jure segregation was created by law.")
H('12.A',3,"Stereotypes harm African Americans by doing what?",
  "Limiting opportunities based on false generalizations",["Creating wealth","Ending bias","Improving schools"],"They shape discrimination.")
H('12.B',3,"African Americans retained cultural identity while adapting by doing what?",
  "Blending African heritage with American traditions in music, food and religion",["Abandoning all traditions","Isolating from society","Forbidding change"],"Gullah Geechee culture is an example.")
H('12.B',3,"Gullah Geechee communities of the Southeast preserved what?",
  "African-influenced language, crafts and food traditions",["Spanish law","Viking runes","Roman customs"],"They live along the coast and Sea Islands.")
H('12.C',3,"Juneteenth commemorates what?",
  "The announcement of freedom to enslaved people in Texas in 1865",["The Declaration of Independence","The Civil War start","The 15th Amendment"],"It is celebrated June 19.")
H('12.C',3,"HBCU traditions such as homecoming and marching bands contribute to what?",
  "A strong shared cultural identity",["Isolation","Disunity","Segregation law"],"They carry community pride.")
H('13.A',3,"The griot in West African tradition was what?",
  "A storyteller and keeper of history",["A soldier","A farmer","A merchant"],"Oral traditions preserved history.")
H('13.A',3,"Call-and-response in African and African American music means what?",
  "A leader sings or speaks and the group answers",["A solo only","A silent prayer","A written score"],"It appears in spirituals and gospel.")
H('13.B',3,"Spirituals sung by enslaved people often did what?",
  "Expressed faith and sometimes carried coded messages about freedom",["Praised slavery","Were written by planters","Were forbidden everywhere"],"They shaped later music.")
H('13.B',3,"Which folktales preserved African storytelling traditions among the enslaved?",
  "Trickster stories such as Brer Rabbit",["Greek myths only","Norse sagas","Roman fables"],"Stories carried wisdom and resistance.")
H('13.D',3,"Blues music developed in which region in the late 1800s?",
  "The Mississippi Delta",["The Pacific Northwest","New England","The Rocky Mountains"],"It grew from work songs and spirituals.")
H('13.D',3,"Hip hop began in the 1970s in which borough?",
  "The Bronx in New York City",["Houston","Seattle","Miami"],"DJ Kool Herc is credited with early development.")
H('13.E',3,"The Fisk Jubilee Singers raised money for their school by doing what?",
  "Touring and performing spirituals for national and international audiences",["Selling land","Running a bank","Building railroads"],"They helped save Fisk University.")
H('13.E',3,"The Fisk Jubilee Singers' tours helped do what?",
  "Introduce spirituals to a worldwide audience",["End the Civil War","Create jazz","Win suffrage"],"They sang for Queen Victoria.")
H('14.A',3,"Scott Joplin is best known for composing what style?",
  "Ragtime, including the Maple Leaf Rag",["Hip hop","Country","Opera only"],"He was the King of Ragtime.")
H('14.A',3,"James Reese Europe was a bandleader who did what?",
  "Directed the 369th Infantry band and helped bring jazz to Europe",["Invented the piano","Founded Motown","Wrote hip hop"],"He influenced early jazz.")
H('14.B',3,"Katherine Dunham was a pioneer who did what?",
  "Combined dance and anthropology to bring African and Caribbean dance to the stage",["Invented ballet","Won an Oscar","Led an army"],"She founded a major dance company.")
H('14.B',3,"The Dance Theatre of Harlem, founded in 1969, was created by whom?",
  "Arthur Mitchell",["Alvin Ailey","Duke Ellington","Langston Hughes"],"He was the first Black principal dancer with New York City Ballet.")
H('14.C ',3,"The Harlem Renaissance was a flowering of what in the 1920s?",
  "Black art, literature and music centered in Harlem",["A military campaign","A political party","A trade union"],"It celebrated Black identity.")
H('14.C ',3,"Langston Hughes was a leading figure of the Harlem Renaissance as a what?",
  "Poet",["General","Senator","Inventor"],"His poetry captured Black life.")
H('14.D ',3,"W. E. B. Du Bois's The Souls of Black Folk introduced the idea of what?",
  "Double consciousness",["Manifest destiny","Separate but equal","Laissez-faire"],"It described seeing oneself through others' eyes.")
H('14.D ',3,"Toni Morrison won the 1988 Pulitzer Prize for which novel?",
  "Beloved",["Native Son","Invisible Man","Roots"],"It explores the legacy of slavery.")
H('14.E ',3,"Oscar Micheaux was a pioneer who did what?",
  "Produced and directed early films by and about Black Americans",["Invented television","Wrote the Constitution","Led a union"],"He made dozens of films.")
H('14.E ',3,"Lorraine Hansberry's A Raisin in the Sun was the first play by a Black woman to do what?",
  "Be produced on Broadway",["Win a Nobel Prize","Be filmed in 1900","Be banned in 1959"],"It premiered in 1959.")
H('14.F',3,"Jacob Lawrence's Migration Series is a work of what?",
  "Visual art depicting the Great Migration",["A treaty","A symphony","A court case"],"It used paintings to tell history.")
H('14.F',3,"Gospel music grew from what tradition?",
  "African American church music and spirituals",["Classical opera","Polka","Disco"],"It influenced soul and R&B.")
H('14.G',3,"Minstrel shows in the 1800s harmed African Americans by doing what?",
  "Spreading demeaning stereotypes",["Honoring them","Ending prejudice","Raising wages"],"They were a form of popular entertainment.")
H('14.G',3,"Motown Records, founded in 1959, helped Black artists do what?",
  "Reach mainstream audiences across racial lines",["Avoid radio","Leave the country","Stop recording"],"Artists included the Supremes and Stevie Wonder.")
H('15.A ',3,"Anti-literacy laws in many Southern states did what?",
  "Made it illegal to teach enslaved people to read and write",["Required schooling","Funded schools","Ended slavery"],"They tried to keep the enslaved from learning.")
H('15.A ',3,"Frederick Douglass described learning to read as what?",
  "A path toward freedom",["A punishment","Unimportant","Easy to get"],"He learned in secret.")
H('15.B',3,"Rosenwald Schools were built through a partnership of whom?",
  "Julius Rosenwald and Booker T. Washington's Tuskegee Institute",["Thomas Jefferson","Abraham Lincoln","John D. Rockefeller"],"They built thousands of rural schools for Black children.")
H('15.B',3,"The Second Morrill Act (1890) helped create what?",
  "Land-grant colleges for Black students",["Public libraries","Interstate highways","Medicare"],"Many HBCUs were established or funded.")
H('15.C',3,"The school-to-prison pipeline refers to what?",
  "Policies that push students out of school and toward the justice system",["A school bus route","A career program","A sports league"],"It disproportionately affects Black students.")
H('15.C',3,"An opportunity gap in education means what?",
  "Unequal access to resources that affect student achievement",["Differences in height","Different school colors","Different mascots"],"It differs from an achievement gap.")
H('16.A ',3,"African civilizations contributed to science and technology through what?",
  "Advances in astronomy, mathematics and architecture",["Only farming","Only trade","Only warfare"],"Examples include Egyptian pyramids and Timbuktu manuscripts.")
H('16.A ',3,"Great Zimbabwe is notable for what?",
  "Massive stone architecture built by an African civilization",["Wooden forts","Glass skyscrapers","Underground tunnels"],"It reflects advanced engineering.")
H('16.B',3,"Jan Matzeliger's shoe-lasting machine helped industrialization by doing what?",
  "Speeding up shoe manufacturing",["Slowing production","Ending factories","Increasing prices only"],"It transformed shoemaking.")
H('16.B',3,"Elijah McCoy invented a device that did what?",
  "Automatically lubricated engines",["Cleaned carpets","Made ice","Cooked food"],"It reduced downtime for machines.")
H('16.C',3,"George Washington Carver promoted what agricultural practice?",
  "Crop rotation and peanuts to restore soil",["Slash and burn","Cotton monoculture","Overgrazing"],"He worked at Tuskegee.")
H('16.C',3,"Katherine Johnson's calculations helped NASA do what?",
  "Plan orbital flights, including John Glenn's",["Build ships","Write laws","Dig tunnels"],"She was a mathematician.")
H('17.A',3,"Which of these is a primary source for studying the Civil Rights Movement?",
  "Dr. King's \"I Have a Dream\" speech",["A modern textbook","An encyclopedia","A later documentary"],"Primary sources are from the time.")
H('17.A',3,"A migration map showing movement from Mississippi to Chicago helps a student do what?",
  "See patterns of the Great Migration",["Measure temperature","Find a river's depth","Learn a language"],"Maps reveal geographic patterns.")
H('17.B',3,"Placing the Emancipation Proclamation, the 13th Amendment and Plessy v. Ferguson in order is what skill?",
  "Applying chronology through sequencing",["Making a generalization","Finding bias","Reading a legend"],"They occurred in 1863, 1865 and 1896.")
H('17.B',3,"Explaining how cotton demand led to more enslaved labor shows what skill?",
  "Identifying cause and effect",["Mapping","Memorizing","Paraphrasing"],"Cause and effect connect events.")
H('17.C',3,"Historical inquiry begins when a student does what?",
  "Poses a question and gathers multiple sources",["States a conclusion","Copies a text","Skips research"],"Evidence guides interpretation.")
H('17.C',3,"A student studying the Great Migration should use which kinds of evidence?",
  "Census data, letters and newspaper articles",["Only one letter","Only rumors","Only opinions"],"Multiple sources give a fuller picture.")
H('17.D',3,"Two sources agreeing about the date of the Tulsa Race Massacre is an example of what?",
  "Corroboration",["Bias","Plagiarism","Sequencing"],"Agreement supports validity.")
H('17.D',3,"A newspaper account written by a participant in a protest may be limited by what?",
  "The author's point of view and frame of reference",["Its page count","Its font size","Its price"],"Evaluate author's perspective.")
H('17.E',3,"A pro-segregation editorial from 1900 would likely show what?",
  "Bias supporting the writer's point of view",["Neutral facts","A modern view","A scientific proof"],"Identify bias and support with evidence.")
H('17.E',3,"A historian identifies bias in a source by looking for what?",
  "Loaded language and one-sided claims",["Page numbers","Footnotes","Photographs"],"Language reveals perspective.")
H('18.A',3,"A researcher quotes a speech from 1963 in a paper. What must be done?",
  "Provide a citation to the source",["Remove the quote","Change the words","Claim it as original"],"Citing avoids plagiarism.")
H('18.A',3,"A good oral presentation on the Harlem Renaissance includes what?",
  "Clear organization, evidence and visuals",["Only opinions","No sources","Reading without looking up"],"Communication skills matter.")
H('18.B ',3,"Using the term \"suffrage\" correctly means referring to what?",
  "The right to vote",["The right to travel","A type of tax","A kind of law"],"Accurate terminology is key.")
H('18.B ',3,"Which term means the separation of groups by race?",
  "Segregation",["Integration","Assimilation","Migration"],"Terms must match concepts.")
H('19.A',3,"A thematic map of the Great Migration would best show what?",
  "The routes and destinations of migrants",["Climate zones","Mountain heights","Population density only"],"Maps display patterns.")
H('19.A',3,"A line graph of Black voter registration in Mississippi from 1960 to 1970 would show what?",
  "A change in registration over time",["Rainfall","Temperature","Religion"],"Graphs show trends.")
H('19.B',3,"A map shows that most Black Southerners moved to Chicago, Detroit and New York. What question could a student pose?",
  "Why did these cities attract so many migrants?",["What is the capital of Texas?","What color is the map?","How tall are the cities?"],"Questions guide analysis of patterns.")
H('19.B',3,"A student reads a chart of HBCU enrollment. Which question is best?",
  "How has enrollment changed since 1970 and why?",["What is the font?","Who drew the chart?","What is its color?"],"Ask analytical questions.")
H('20',3,"A school community faces a gap in resources between two campuses. What is the first step in a problem-solving process?",
  "Identify and define the problem",["Announce a decision","Evaluate the final result","Skip to funding"],"Define the problem first.")
H('20',3,"After gathering information about the resource gap, a group should do what?",
  "List and consider possible solutions",["Ignore the facts","Stop the project","Delete the data"],"Consider options before deciding.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_aas.jsonl'))

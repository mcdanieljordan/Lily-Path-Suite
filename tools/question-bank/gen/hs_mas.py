import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('113.50.c.', 1005, own='hs_mas.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('1',3,"A student places the Spanish conquest of the Aztecs (1521), the Grito de Dolores (1810) and the Treaty of Guadalupe Hidalgo (1848) in order. What skill is being used?",
  "Applying chronology by sequencing events",["Comparing primary sources","Reading a map scale","Calculating a median"],"Sequencing places events in order of time.")
H('1',3,"Which list places events in correct chronological order?",
  "Mexican independence (1821), Texas independence (1836), Mexican-American War (1846)",["Mexican-American War, Texas independence, Mexican independence","Texas independence, Mexican independence, Mexican-American War","Mexican independence, Mexican-American War, Texas independence"],"Relative chronology compares which came first.")
H('2.A',3,"The Spanish conquest of the Aztec Empire is generally dated to the fall of Tenochtitlan in which year?",
  "1521",["1492","1610","1810"],"Cortés and his allies took Tenochtitlan in 1521.")
H('2.A',3,"The New Laws of 1542 were significant because they did what?",
  "Aimed to limit the enslavement and abuse of Indigenous people in Spanish colonies",["Granted Mexico independence","Ended Spanish rule","Created the Border Patrol"],"They responded to reformers such as Las Casas.")
H('2.B',3,"Bartolomé de las Casas is remembered for doing what?",
  "Defending the rights of Indigenous people against abuse by colonists",["Leading the Aztec army","Founding the Mexican Republic","Writing the Texas constitution"],"He was a priest who spoke out against colonial violence.")
H('2.B',3,"Sor Juana Inés de la Cruz was a Spanish colonial-era figure known as what?",
  "A nun, poet and scholar who defended women's right to education",["A conquistador","An Aztec emperor","A Revolution general"],"She is one of the great writers of colonial Mexico.")
H('3.A',3,"The Grito de Dolores in 1810 was significant because it did what?",
  "Began Mexico's war for independence from Spain",["Ended the Mexican Revolution","Created the Border Patrol","Sold land to the United States"],"Father Miguel Hidalgo called for revolt.")
H('3.A',3,"The Treaty of Guadalupe Hidalgo (1848) did what?",
  "Ended the Mexican-American War and transferred much of present-day Southwest to the United States",["Began the Mexican Revolution","Created the Bracero Program","Declared Texas independent"],"Mexicans living there could become U.S. citizens.")
H('3.B',3,"Emiliano Zapata is best known for doing what during the Mexican Revolution?",
  "Leading peasants in a fight for land reform",["Serving as Spain's viceroy","Writing the Texas Declaration","Founding LULAC"],"His slogan was land and liberty.")
H('3.B',3,"Francisco I. Madero became important in the Mexican Revolution because he did what?",
  "Challenged Porfirio Díaz and was elected president in 1911",["Led the Spanish army","Signed the New Laws","Founded the UFW"],"His call for revolt began the Revolution.")
H('4.A',3,"The Bracero Program, begun in 1942, was a program that did what?",
  "Brought Mexican workers to the United States for temporary agricultural labor",["Gave land to farmers","Ended segregation","Created La Raza Unida"],"It addressed wartime labor shortages.")
H('4.A',3,"In Hernández v. Texas (1954), the Supreme Court ruled that what?",
  "Mexican Americans were protected by the Fourteenth Amendment and could not be excluded from juries",["Segregated schools were legal","Texas could ban Spanish","Braceros could not work"],"The Court recognized discrimination against a class other than Black and white.")
H('4.B',3,"César Chávez and Dolores Huerta are known for doing what?",
  "Organizing farmworkers through the United Farm Workers",["Founding the Border Patrol","Leading the Mexican Revolution","Writing the New Laws"],"They led strikes and boycotts for better wages.")
H('4.B',3,"Héctor P. García is remembered for doing what?",
  "Founding the American G.I. Forum to fight discrimination against Mexican American veterans",["Leading the Aztec Empire","Winning the Nobel Prize in Chemistry","Serving as mayor of San Antonio"],"The Longoria Affair brought the Forum national attention.")
H('5.A',3,"The Immigration Reform and Control Act of 1986 did what?",
  "Offered legal status to some undocumented immigrants while penalizing employers who hired unauthorized workers",["Ended all immigration","Created the Bracero Program","Abolished the Border Patrol"],"It combined amnesty with enforcement.")
H('5.A',3,"H.R. 4437, passed by the House in 2006, led to what?",
  "Large nationwide protests against proposed harsher immigration penalties",["A national holiday","The end of the Border Patrol","The New Laws"],"It would have increased penalties for unlawful presence.")
H('5.B ',3,"Willie Velásquez is known for founding what?",
  "The Southwest Voter Registration Education Project",["The United Farm Workers","The Border Patrol","The Aztec calendar"],"His group registered many Latino voters.")
H('5.B ',3,"Henry Cisneros served as which of the following?",
  "Mayor of San Antonio and a U.S. Secretary of Housing and Urban Development",["Governor of Texas","President of Mexico","A Revolution general"],"He was among the first Mexican American mayors of a major city.")
H('6.A',3,"The U.S.-Mexico border region is historically significant to Mexican American history because it does what?",
  "Is where cultures, families, trade and migration have long overlapped",["Has never been crossed","Is uninhabited","Was created in 2006"],"The border was drawn after the Mexican-American War.")
H('6.A',3,"Tenochtitlan, site of present-day Mexico City, was the capital of which civilization?",
  "The Aztec Empire",["The Spanish Empire","The Republic of Texas","The Comanche"],"It was built on an island in Lake Texcoco.")
H('6.B',3,"Which physical feature supported large settlements in the Valley of Mexico?",
  "Lakes and fertile land that supported agriculture",["Polar ice","Open ocean only","Desert sand dunes only"],"Chinampas farms used lake shallows.")
H('6.B',3,"Why did many American Indian societies settle near rivers?",
  "Rivers provided water, transportation and fertile soil for farming",["Rivers were mountains","Rivers blocked trade","Rivers had no use"],"Physical geography shaped settlement patterns.")
H('6.C',3,"Land use issues during the Mexican Revolution included conflicts over what?",
  "Control of large estates held by a few wealthy landowners",["The color of flags","The color of maps","The cost of tickets"],"Peasants demanded land reform.")
H('6.C',3,"Land grants from Spain and Mexico became central to disputes after the Mexican-American War because what?",
  "Many Mexican landowners had to defend their ownership under U.S. law",["Land became free","Titles were erased by treaty","Everyone returned to Mexico"],"The treaty promised property protection that was often ignored.")
H('6.D',3,"Which factor pushed many Mexicans to migrate north between the 1910s and 1930s?",
  "The Mexican Revolution and economic hardship",["Nationwide peace","Cheap airfare","A new highway to Canada"],"The Revolution displaced people.")
H('6.D',3,"Railroads in the early 1900s helped Mexican migration by doing what?",
  "Connecting Mexican towns with jobs in the U.S. Southwest",["Blocking travel","Ending trade","Closing the border"],"Railroad work attracted laborers.")
H('6.E',3,"During the Bracero Program, many Mexican workers were employed in what?",
  "Agricultural fields in the Southwest and beyond",["Space programs","Banking","Video game design"],"Farms needed workers during the war.")
H('6.E',3,"The Bracero Program ran from 1942 to which approximate year?",
  "1964",["1942","1930","1990"],"It lasted over two decades.")
H('6.F',3,"Mexican American migration within the United States today includes movement to what?",
  "Growing metropolitan areas in states such as Texas, Georgia and the Midwest",["Only rural Mexico","Only Alaska","Only one state"],"Migration patterns have diversified.")
H('6.F',3,"A factor in contemporary Mexican migration is what?",
  "Economic opportunity and family connections",["Free tickets","A ban on travel","A lack of borders"],"Push and pull factors continue to shape migration.")
H('8.A',3,"Mexican Americans have participated in government by doing what?",
  "Voting, running for office and organizing for change",["Avoiding politics","Being barred from all offices","Having no voice"],"Civic participation includes elections and advocacy.")
H('8.A',3,"Which action is an example of civic participation?",
  "Registering voters in a community",["Ignoring local issues","Staying uninformed","Avoiding elections"],"Voter registration expands participation.")
H('8.B',3,"Delgado v. Bastrop ISD (1948) held that what was unlawful?",
  "Separating Mexican American students into segregated schools",["Teaching in Spanish","Paying teachers","Building schools"],"It was part of the legal challenges to school segregation.")
H('8.B',3,"The biracial paradigm refers to a view that society is divided into what two groups?",
  "Black and white",["Rich and poor","Rural and urban","Young and old"],"These cases showed that Mexican Americans were also affected by segregation.")
H('8.D',3,"A success of the Mexican American civil rights movement was what?",
  "Greater political representation and legal protections",["The end of all discrimination","Open borders for all","Abolition of the Constitution"],"Gains were real but incomplete.")
H('8.D',3,"A continuing challenge the movement faced was what?",
  "Unequal school funding and economic disparities",["Too many voters","Too many schools","Equal pay"],"Not all goals were achieved.")
H('8.E',3,"Plyler v. Doe (1982) ruled that states may not do what?",
  "Deny free public education to children because they are undocumented",["Require school attendance","Fund schools","Build classrooms"],"The Court cited the Equal Protection Clause.")
H('8.E',3,"Miranda v. Arizona (1966) required police to do what?",
  "Inform suspects of their rights before questioning",["Arrest without cause","Close courts","Skip trials"],"Ernesto Miranda, a Mexican American, was the defendant.")
H('8.F',3,"LULAC, founded in 1929, works to do what?",
  "Advance the civil rights and educational opportunities of Latinos",["Run the military","Govern Texas","Sell farm equipment"],"It is one of the oldest Latino civil rights groups.")
H('8.F',3,"MALDEF is an organization that does what?",
  "Uses the legal system to protect Latino civil rights",["Builds highways","Regulates banks","Trains pilots"],"It was founded in 1968.")
H('9.A',3,"Which is a responsibility of a U.S. citizen?",
  "Serving on a jury when called",["Avoiding taxes","Ignoring laws","Skipping all elections by law"],"Citizens vote, pay taxes and serve on juries.")
H('9.A',3,"Immigrants living in the United States have which basic protection?",
  "Due process under the law",["Immunity from the law","The right to vote in all elections","No obligations"],"Constitutional protections extend to persons within U.S. jurisdiction.")
H('9.B',3,"Cultural citizenship refers to what?",
  "Belonging to a community through culture and participation, not only legal status",["A passport","A birth certificate","A tax form"],"Formal citizenship is legal membership.")
H('9.B',3,"Formal citizenship is defined by what?",
  "Legal membership in a nation, such as by birth or naturalization",["Language only","Food preferences","Music taste"],"It is a legal status.")
H('9.C',3,"Individuals contribute to national identity when they do what?",
  "Share their cultural traditions, work and civic participation",["Hide their heritage","Avoid community","Reject all change"],"Diversity shapes the nation.")
H('9.C',3,"The United States is sometimes described as a nation of what?",
  "Many cultures contributing to a shared identity",["One culture only","No cultures","Only recent arrivals"],"Identity is shaped by many groups.")
H('9.D',3,"The term \"Chicano\" became widely used during the civil rights era to express what?",
  "Pride in Mexican American identity and political activism",["A government label only","A type of food","An old tax"],"Many activists adopted it in the 1960s.")
H('9.D',3,"The term \"Hispanic\" is associated with what history?",
  "A broad label popularized for people with Spanish-speaking heritage, including in U.S. government use",["A Revolution slogan","An Aztec title","A Spanish law"],"People use different terms for different reasons.")
H('10.A',3,"Mexican American history and issues have been reflected in art through what?",
  "Murals, music, film and literature",["Only statistics","Only maps","Only laws"],"Artists respond to social issues.")
H('10.A',3,"Corridos are folk ballads that often do what?",
  "Tell stories about heroes, events and struggles",["List recipes","Give weather reports","Announce prices"],"They are part of Mexican musical tradition.")
H('10.B',3,"\"I am Joaquín\" (1967) by Rodolfo \"Corky\" Gonzales is significant because it does what?",
  "Expresses Mexican American identity and pride in an epic poem",["Describes a recipe","Lists census numbers","Explains tax law"],"It became a landmark of the Chicano movement.")
H('10.B',3,"Luis Valdez wrote \"Pensamiento Serpentino\" in 1971. He is also known for founding what?",
  "El Teatro Campesino",["The Border Patrol","MALDEF","The G.I. Forum"],"His theater supported farmworkers.")
H('10.C',3,"El Teatro Campesino used short plays to do what?",
  "Inform and rally farmworkers during the strike",["Sell tickets for profit only","Teach calculus","Entertain royalty"],"Actos made political points through performance.")
H('10.C',3,"Why is artistic expression effective in social movements?",
  "It can inspire emotions and unite people around a cause",["It hides messages","It replaces law","It prevents action"],"Art mobilizes communities.")
H('10.D',3,"Sandra Cisneros is a Mexican American author known for what work?",
  "The House on Mango Street",["The Declaration of Independence","The Texas Constitution","I am Joaquín"],"Her stories explore identity and community.")
H('10.D',3,"Norma Alarcón is a Chicana writer and editor who is known for what?",
  "Founding a press that publishes Chicana and Latina feminist writing",["Directing NASA","Leading the UFW","Founding LULAC"],"She edited Third Woman Press.")
H('10.E ',3,"Tejano music, a Texas Mexican American tradition, blends what?",
  "Mexican folk music with polka and other regional styles",["Only opera","Only jazz","Only drums"],"Selena became a star in the genre.")
H('10.E ',3,"Mexican American popular culture has influenced the world in areas such as what?",
  "Food, music and film",["Only tax law","Only geology","Only mathematics"],"Tacos and mariachi are global.")
H('11.A',3,"The Maya are known for developing which mathematical idea?",
  "The concept of zero",["Calculus","The metric system","Logarithms"],"They used a base-20 system.")
H('11.A',3,"The Aztec capital Tenochtitlan showed advanced engineering through what?",
  "Causeways, canals and aqueducts",["Skyscrapers","Interstate highways","Railroads"],"These supported a large city on a lake.")
H('11.B',3,"Mario Molina earned a Nobel Prize in Chemistry for research on what?",
  "The ozone layer and chemicals that damage it",["Gold mining","Rocket fuel","Plant breeding"],"He shared the 1995 prize.")
H('11.B',3,"Ellen Ochoa was the first Hispanic woman to do what?",
  "Travel into space",["Win a Nobel Prize","Become President","Climb Everest"],"She flew on a Space Shuttle in 1993.")
H('12.A',3,"Using the term \"naturalization\" correctly means referring to what?",
  "The legal process of becoming a citizen",["A type of farming","A kind of tax","A map projection"],"Terminology must be used precisely.")
H('12.A',3,"Which term describes a person who moves permanently to another country?",
  "Immigrant",["Voter","Delegate","Juror"],"Accurate terms avoid confusion.")
H('12.B',3,"To analyze diverse points of view on a contemporary issue, a student should do what?",
  "Read perspectives from people with different experiences",["Use one source","Rely on rumors","Skip evidence"],"Multiple perspectives give a fuller picture.")
H('12.B',3,"Two groups disagree about immigration policy. This shows what?",
  "Different values and experiences can lead to different viewpoints",["One group is always lying","Facts do not matter","Policy never changes"],"Analyze reasons behind positions.")
H('12.C ',3,"A strong presentation on a contemporary issue includes what?",
  "A clear thesis supported by credible sources",["Only opinions","No sources","Rumors"],"Critical inquiry strengthens the product.")
H('12.C ',3,"Critical methods of inquiry begin with what?",
  "A focused question and reliable evidence",["A guess","A slogan","A rumor"],"Research is question driven.")
H('12.D ',3,"Identifying how the Mexican Revolution led to increased migration north is what skill?",
  "Finding cause-and-effect relationships",["Memorizing dates","Copying text","Reading a legend"],"It connects events and outcomes.")
H('12.D ',3,"Drawing a conclusion from a set of census data is what skill?",
  "Making inferences and conclusions from evidence",["Guessing","Ignoring data","Rewriting facts"],"Conclusions must follow the data.")
H('7.A',3,"Mexican repatriation in the 1930s resulted in what?",
  "Hundreds of thousands of people of Mexican descent, including U.S. citizens, leaving the United States",["Higher wages for all","A new treaty","The creation of the Bracero Program"],"It occurred during the Great Depression.")
H('7.A',3,"Repatriation affected the economy by doing what?",
  "Removing workers and consumers from communities and businesses",["Creating more jobs for everyone","Raising wages for farmworkers","Ending the Depression"],"Communities lost labor and customers.")
H('7.B',3,"The Bracero Program helped the war effort by doing what?",
  "Supplying agricultural labor while many U.S. workers served in the military",["Building ships","Writing laws","Creating schools"],"Farm output supported the nation.")
H('7.B',3,"Braceros often faced which problem?",
  "Low wages and poor working and living conditions",["Free housing in every case","High salaries","No work at all"],"Abuses led to criticism of the program.")
H('7.C',3,"The farmworkers union struggle sought to win what?",
  "Better wages, safer conditions and the right to organize",["Lower taxes","New roads","Larger farms"],"The UFW used strikes and boycotts.")
H('7.C',3,"The Delano grape strike of 1965 was significant because it did what?",
  "Drew national attention to farmworker conditions",["Ended the Bracero Program","Created the Border Patrol","Started the Revolution"],"Filipino and Mexican American workers joined together.")
H('7.D',3,"Mexican American workers contribute to the U.S. economy in sectors such as what?",
  "Agriculture, construction, services and professional fields",["Only mining","Only fishing","Only the military"],"They work across the economy.")
H('7.D',3,"Small businesses owned by Mexican Americans contribute to the economy by doing what?",
  "Creating jobs and generating tax revenue",["Eliminating competition","Reducing wages for all","Ending trade"],"Entrepreneurship grows communities.")
H('7.E',3,"Purchasing power refers to what?",
  "The amount of goods and services a group can buy with its income",["The number of banks","The size of a house","A tax rate"],"It influences consumer markets and GDP.")
H('7.E',3,"The growing Mexican American population affects GDP by doing what?",
  "Increasing consumer spending on goods and services",["Reducing demand","Ending trade","Removing taxes"],"Consumption is a main part of GDP.")
H('7.F ',3,"Which is a current issue related to the Mexican American labor force?",
  "Wage fairness and immigration policy",["Space travel","Ancient trade","Typewriters"],"Policy debates affect workers.")
H('7.F ',3,"Workers' access to fair pay and safe conditions is affected by what?",
  "Labor laws and their enforcement",["The weather","Time zones","Sports schedules"],"Enforcement matters for protection.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_mas.jsonl'))

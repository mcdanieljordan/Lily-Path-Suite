#!/usr/bin/env python3
"""High school US History Since 1877 (TEKS 113.41.d). Original questions."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('113.41.d.', 995, own='hs_ushist.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 1 founding principles
H('1.A', 3, "Which document states that governments get their power from the consent of the governed?", "the Declaration of Independence", ["the Mayflower Compact", "the Articles of Confederation", "the Emancipation Proclamation"], "The Declaration of Independence asserts consent of the governed.")
H('1.A', 3, "Which principle in the U.S. Constitution divides power among the legislative, executive and judicial branches?", "separation of powers", ["divine right", "nullification", "manifest destiny"], "Separation of powers prevents concentration of authority.")
H('1.B', 4, "The Fourteenth Amendment's guarantee of equal protection was later used in cases such as Brown v. Board of Education. Which founding principle is applied?", "equality under the law", ["rule by hereditary leaders", "state religion", "unlimited executive power"], "Founding ideals were applied to later struggles for rights.")
H('1.C', 2, "The national motto 'E Pluribus Unum' is usually translated as what?", "out of many, one", ["in God we trust", "liberty and justice", "freedom for all"], "It expresses unity from diversity.")

# 2 eras
H('2.A', 3, "Which era of U.S. history is associated with industrialization, big business and immigration after Reconstruction?", "the Gilded Age", ["the Era of Good Feelings", "the Colonial period", "the Jazz Age"], "Industrial growth and inequality defined the Gilded Age.")
H('2.B', 3, "Which year marks the start of the Spanish-American War?", "1898", ["1877", "1914", "1941"], "The war began in 1898.")
H('2.B', 3, "Which event is the turning point of December 7, 1941?", "the attack on Pearl Harbor", ["the sinking of the Maine", "the stock market crash", "the Cuban Missile Crisis"], "It brought the United States into World War II.")

# 3 Gilded Age
H('3.A', 3, "What was the main purpose of the Pendleton Civil Service Act of 1883?", "to base federal hiring on merit rather than political favors", ["to ban immigration", "to create a national bank", "to regulate railroads"], "It reformed the spoils system.")
H('3.A', 4, "Political machines like Tammany Hall gained power in cities by doing what?", "trading services and jobs for votes", ["banning elections", "outlawing parties", "ending patronage"], "Machines relied on patronage and immigrant votes.")
H('3.A', 3, "The Dawes Act of 1887 sought to change American Indian life by doing what?", "dividing tribal lands into individual allotments", ["granting each tribe full sovereignty", "creating new reservations on the coast", "ending all federal involvement"], "It aimed to assimilate Indians through private land ownership.")
H('3.B', 3, "Which law, passed in 1890, was designed to limit monopolies and trusts?", "the Sherman Antitrust Act", ["the Homestead Act", "the Pendleton Act", "the Dawes Act"], "It targeted anti-competitive combinations.")
H('3.B', 3, "Which labor organization, led by Samuel Gompers, focused on skilled workers and workplace bargaining?", "the American Federation of Labor", ["the Knights of Labor", "the Grange", "the Populist Party"], "The AFL organized craft unions.")
H('3.B', 3, "Farmers in the late 1800s formed the Grange to do what?", "address problems with railroad rates and prices", ["ban machines", "increase tariffs on imports", "support industrial monopolies"], "Farmers sought relief from high costs and low crop prices.")
H('3.C', 3, "What was a major cause of rapid urban growth in the late 1800s?", "industrial jobs and immigration", ["decline of factories", "a ban on migration", "the end of railroads"], "Cities grew as workers arrived.")
H('3.C', 4, "Settlement houses such as Hull House aimed to do what?", "help immigrants and the urban poor adjust to city life", ["train soldiers", "regulate banks", "build railroads"], "Jane Addams founded Hull House in Chicago.")

# 4 imperialism and WWI
H('4.A', 3, "Which event is often cited as a spark for the Spanish-American War?", "the explosion of the USS Maine", ["the Zimmermann Telegram", "the attack at Pearl Harbor", "the Boston Massacre"], "The Maine's destruction in Havana inflamed public opinion.")
H('4.B', 3, "As a result of the Spanish-American War, the United States gained which territory?", "the Philippines", ["Texas", "Alaska", "Louisiana"], "The Treaty of Paris transferred Spain's Pacific territories.")
H('4.B', 4, "What was the Open Door Policy toward China intended to ensure?", "equal trading access for all nations", ["U.S. control of China", "Chinese isolation", "a ban on trade"], "It aimed to prevent exclusive spheres of influence.")
H('4.C', 3, "Which German action in 1917 helped push the United States into World War I?", "unrestricted submarine warfare", ["the bombing of Pearl Harbor", "the invasion of Poland", "the Berlin Airlift"], "U-boat attacks on shipping provoked the U.S.")
H('4.C', 3, "The Zimmermann Telegram proposed what?", "a German alliance with Mexico against the United States", ["a U.S. treaty with France", "a peace plan", "an arms agreement with Britain"], "It alarmed Americans and contributed to the declaration of war.")
H('4.D', 3, "Who commanded the American Expeditionary Forces in World War I?", "John J. Pershing", ["Dwight Eisenhower", "Douglas MacArthur", "George Patton"], "Pershing led U.S. forces in Europe.")
H('4.E', 3, "Which new weapon of World War I spread poison gas across trenches and caused terrible suffering?", "chemical warfare", ["atomic bombs", "stealth aircraft", "nuclear submarines"], "Gas attacks were a new horror.")
H('4.E', 3, "Trench warfare on the Western Front led to what?", "long stalemates and heavy casualties", ["swift victories", "an early peace", "few deaths"], "Machine guns made advances deadly.")
H('4.F', 4, "Woodrow Wilson's Fourteen Points included a proposal to create what?", "a League of Nations", ["a U.N. Security Council", "NATO", "the Marshall Plan"], "Wilson sought an international body to preserve peace.")
H('4.F', 3, "Why did the U.S. Senate refuse to ratify the Treaty of Versailles?", "many senators feared it would draw the U.S. into foreign entanglements", ["it ended the war too early", "it gave the U.S. too little power", "it banned all trade"], "Isolationist sentiment blocked ratification.")

# 5 Progressives
H('5.A', 3, "Which Progressive Era reform lets voters propose laws directly?", "the initiative", ["the veto", "the filibuster", "the impeachment"], "Initiative, referendum and recall expanded direct democracy.")
H('5.A', 3, "The Seventeenth Amendment changed U.S. Senate elections by doing what?", "providing for direct election of senators by voters", ["ending term limits", "giving states two more senators", "creating a Senate veto"], "It replaced election by state legislatures.")
H('5.B', 3, "Upton Sinclair's novel 'The Jungle' led to reforms in what industry?", "meatpacking", ["railroads", "banking", "textiles"], "It exposed unsanitary conditions and prompted food safety laws.")
H('5.B', 3, "Which muckraker investigated the Standard Oil Company in a series of magazine articles?", "Ida Tarbell", ["Jacob Riis", "Margaret Sanger", "Booker T. Washington"], "Tarbell exposed Standard Oil's business practices.")
H('5.C', 3, "The Populist Party of the 1890s mainly represented which group?", "farmers", ["bankers", "factory owners", "railroad executives"], "Populists pushed for farm relief and monetary change.")
H('5.C', 4, "Theodore Roosevelt ran in 1912 under which third party?", "the Progressive (Bull Moose) Party", ["the Populist Party", "the Socialist Party", "the Whig Party"], "His candidacy split the Republican vote.")

# 6 1920s
H('6.A', 3, "The Scopes Trial of 1925 centered on a conflict over what?", "teaching evolution in public schools", ["Prohibition", "immigration quotas", "women's suffrage"], "It reflected tension between traditional and modern views.")
H('6.A', 3, "Which constitutional amendment established Prohibition in 1920?", "the Eighteenth Amendment", ["the Nineteenth Amendment", "the Sixteenth Amendment", "the Twenty-First Amendment"], "It banned the manufacture and sale of alcohol.")
H('6.A', 3, "The Red Scare of 1919-1920 was fueled by fear of what?", "communism and radicalism", ["foreign trade", "railroad strikes only", "inflation"], "Post-war anxiety targeted suspected radicals.")
H('6.B', 3, "Henry Ford's assembly line helped make cars more affordable by doing what?", "lowering production costs", ["raising prices", "limiting production", "banning mass manufacturing"], "Efficiency made the Model T widely available.")
H('6.B', 3, "Charles Lindbergh became a national hero in 1927 for what achievement?", "flying solo nonstop across the Atlantic", ["inventing the airplane", "winning an election", "founding a union"], "He flew from New York to Paris.")

# 7 WWII
H('7.A', 3, "Which event directly brought the United States into World War II?", "Japan's attack on Pearl Harbor", ["the sinking of the Lusitania", "the invasion of Poland", "the fall of Paris"], "The U.S. declared war the day after.")
H('7.A', 3, "Which leaders headed the Axis powers' aggression in Europe and Asia?", "Hitler, Mussolini and Tojo", ["Stalin, Churchill and Roosevelt", "De Gaulle, Franco and Truman", "Lenin, Wilson and Chiang"], "Germany, Italy and Japan were the Axis.")
H('7.B', 3, "Franklin D. Roosevelt's domestic leadership during the war included which action?", "mobilizing the economy for wartime production", ["ending the draft", "disbanding the army", "cutting factory output"], "The home front shifted to war industry.")
H('7.B', 4, "Harry Truman's decision in 1945 to use atomic weapons was intended to do what?", "bring Japan's surrender and end the war", ["start the Cold War", "prolong the conflict", "support Germany"], "Truman aimed to end the war without a costly invasion.")
H('7.C', 3, "Executive Order 9066 led to what policy during World War II?", "the internment of Japanese Americans", ["rationing of gasoline", "the Marshall Plan", "the draft of women"], "Thousands were relocated to camps.")
H('7.C', 3, "The systematic murder of six million Jews by Nazi Germany is known as what?", "the Holocaust", ["the Blitz", "the Anschluss", "the Kristallnacht boycott"], "A genocide carried out by the Nazi regime.")
H('7.D', 3, "The D-Day invasion of June 6, 1944 took place in which region?", "Normandy, France", ["Sicily, Italy", "Guadalcanal", "Iwo Jima"], "Allied forces landed on the beaches of Normandy.")
H('7.D', 4, "The Battle of Midway was significant because it did what?", "turned the tide of the war in the Pacific", ["ended the war in Europe", "began the Cold War", "led to the atomic bomb"], "U.S. carriers sank four Japanese carriers.")
H('7.E', 3, "Which general served as Supreme Allied Commander in Europe?", "Dwight Eisenhower", ["Douglas MacArthur", "George Marshall", "Chester Nimitz"], "Eisenhower led the D-Day invasion.")
H('7.E', 3, "Which general famously pledged 'I shall return' about the Philippines?", "Douglas MacArthur", ["Omar Bradley", "Mark Clark", "George Patton"], "MacArthur led the Pacific campaign.")
H('7.F', 2, "Victory Gardens during World War II were planted to do what?", "supplement food supplies for the war effort", ["advertise war bonds", "recruit soldiers", "teach geography"], "Home gardens eased food shortages.")
H('7.F', 3, "War bonds sold on the home front helped the government do what?", "finance the war", ["end rationing", "pay off the Depression", "reduce taxes"], "Citizens lent money to the government.")
H('7.G', 3, "The Tuskegee Airmen are remembered for what?", "serving as Black military pilots in a segregated army", ["inventing radar", "leading D-Day", "working at Los Alamos"], "They proved their skill and courage.")

# 8 Cold War
H('8.A', 3, "The Truman Doctrine pledged U.S. support for which kind of nations?", "those resisting communist takeover", ["colonial powers", "non-aligned neutral states only", "Soviet allies"], "It underlay the policy of containment.")
H('8.A', 3, "The Marshall Plan provided what to Western Europe?", "economic aid for rebuilding after the war", ["military conscripts", "a currency union", "nuclear weapons"], "It aimed to stabilize economies.")
H('8.A', 3, "The Berlin Airlift (1948-1949) was a response to what?", "a Soviet blockade of West Berlin", ["the Korean War", "the Cuban Missile Crisis", "the Suez Crisis"], "Allies supplied the city by air.")
H('8.B', 3, "Senator Joseph McCarthy became known for doing what?", "making sweeping accusations of communism in the government", ["negotiating the Camp David Accords", "leading the Berlin Airlift", "writing the Marshall Plan"], "McCarthyism spread fear and suspicion.")
H('8.C', 3, "The United States entered the Korean War in 1950 mainly to do what?", "defend South Korea against a communist invasion", ["support North Korea", "reclaim Japan", "fight Vietnam"], "It reflected containment policy.")
H('8.D', 4, "The domino theory held that if one country fell to communism, what would follow?", "neighboring countries would also fall", ["Soviet collapse", "a global treaty", "a U.S. withdrawal"], "It justified intervention in Southeast Asia.")
H('8.D', 3, "The Cuban Missile Crisis of 1962 involved what?", "Soviet nuclear missiles placed in Cuba", ["a Soviet attack on Berlin", "a U.S. invasion of Korea", "a coup in Chile"], "Kennedy imposed a naval quarantine.")
H('8.E', 3, "The 1968 Tet Offensive shook American confidence because it did what?", "showed the enemy could launch large attacks despite official optimism", ["ended the war immediately", "captured Washington", "ended the draft"], "It contradicted claims of progress.")
H('8.E', 3, "What was President Nixon's policy of 'Vietnamization'?", "turning ground fighting over to South Vietnamese forces", ["escalating troops", "invading Cambodia permanently", "ending all aid"], "It aimed to reduce U.S. combat roles.")
H('8.F', 3, "The Twenty-sixth Amendment, ratified in 1971, did what?", "lowered the voting age to 18", ["gave women the vote", "banned poll taxes", "limited presidents to two terms"], "It was spurred by the argument that those old enough to fight could vote.")
H('8.F', 3, "Television coverage of the Vietnam War affected public opinion by doing what?", "bringing images of combat into American homes", ["hiding events", "boosting enlistment sharply", "ending the draft"], "Media coverage shaped views of the war.")

# 9 civil rights
H('9.A', 3, "Which 1896 Supreme Court decision upheld 'separate but equal'?", "Plessy v. Ferguson", ["Brown v. Board of Education", "Marbury v. Madison", "Gideon v. Wainwright"], "It legalized segregation.")
H('9.B', 3, "Jim Crow laws in the South did what?", "enforced racial segregation", ["ended segregation", "expanded voting rights", "banned lynching"], "They separated people by race.")
H('9.C', 3, "Which organization, founded in 1909, worked to end racial discrimination through legal action?", "the NAACP", ["the KKK", "SNCC", "the AFL"], "The NAACP pursued litigation and advocacy.")
H('9.C', 3, "Cesar Chavez organized which group of workers?", "farm workers", ["steelworkers", "miners", "railroad engineers"], "He cofounded the United Farm Workers.")
H('9.D', 3, "Which leader promoted nonviolent protest, citing Gandhi's influence?", "Martin Luther King Jr.", ["Malcolm X", "Stokely Carmichael", "Marcus Garvey"], "King led marches and boycotts.")
H('9.D', 3, "Who refused to give up her seat on a Montgomery bus in 1955?", "Rosa Parks", ["Ruby Bridges", "Harriet Tubman", "Fannie Lou Hamer"], "It sparked the Montgomery bus boycott.")
H('9.E', 4, "How did the Black Panthers' approach differ from Dr. King's?", "it emphasized self-defense and community empowerment rather than strict nonviolence", ["it rejected all protest", "it supported segregation", "it relied only on the courts"], "The groups differed in tactics.")
H('9.F', 3, "Dr. King's 'Letter from Birmingham Jail' responded to criticism of what?", "his nonviolent direct-action protests", ["his service in the army", "his book sales", "his campaign for governor"], "He defended civil disobedience against unjust laws.")
H('9.G', 3, "The Civil Rights Act of 1964 outlawed what?", "discrimination in public places and employment", ["poll taxes only", "literacy tests only", "school desegregation only"], "It banned many forms of discrimination.")
H('9.G', 3, "The Voting Rights Act of 1965 aimed to do what?", "protect the right of Black citizens to vote", ["end the draft", "create Medicare", "ban all segregation in housing"], "It targeted discriminatory voting practices.")
H('9.H', 4, "Governor Orval Faubus of Arkansas resisted integration in 1957 by doing what?", "calling out the National Guard to block Black students from Central High", ["supporting integration", "closing the state", "resigning"], "Eisenhower sent federal troops.")
H('9.I', 3, "Which change resulted from the civil rights movement?", "increased political participation by African Americans", ["a return of segregation", "the end of the Constitution", "a ban on protest"], "Voting and officeholding expanded.")
H('9.J', 3, "Brown v. Board of Education (1954) declared what?", "segregated public schools unconstitutional", ["segregated trains legal", "poll taxes legal", "the draft illegal"], "It overturned 'separate but equal' in schools.")
H('9.J', 4, "Sweatt v. Painter (1950) helped lay the groundwork for Brown by showing what?", "separate law schools could not be truly equal", ["segregation was equal", "integration was optional", "states controlled all schooling"], "It undermined the separate-but-equal doctrine.")

# 10 1970s-80s
H('10.A', 3, "Nixon's 1972 visit to China was important because it did what?", "began normalizing relations between the two countries", ["started the Korean War", "ended the Cold War", "created NATO"], "It shifted Cold War diplomacy.")
H('10.A', 3, "Détente refers to what?", "a relaxation of tensions between the superpowers", ["a military alliance", "a trade embargo", "a space program"], "Détente reduced Cold War tension in the 1970s.")
H('10.B', 3, "Reagan's economic program, sometimes called supply-side economics, emphasized what?", "tax cuts and reduced regulation", ["higher taxes", "price controls", "nationalizing industry"], "It aimed to spur growth.")
H('10.B', 3, "President Reagan's Strategic Defense Initiative proposed what?", "a missile defense system", ["a trade treaty", "a space station", "a new draft"], "Nicknamed 'Star Wars' by critics.")
H('10.C', 3, "The Camp David Accords of 1978 involved which two countries?", "Egypt and Israel", ["Iran and Iraq", "Syria and Jordan", "Saudi Arabia and Turkey"], "Carter brokered a peace framework.")
H('10.C', 3, "The Iran hostage crisis began in 1979 when militants did what?", "seized the U.S. embassy in Tehran", ["bombed Pearl Harbor", "invaded Kuwait", "sank a warship"], "Americans were held for 444 days.")
H('10.D', 4, "The Heritage Foundation and the Moral Majority are associated with which trend of the 1980s?", "the conservative resurgence", ["the New Deal", "the Progressive movement", "the Populist revolt"], "Conservative groups gained influence.")
H('10.E', 3, "The War on Drugs of the 1980s aimed to do what?", "reduce drug trafficking and use through tougher enforcement", ["legalize narcotics", "end all prisons", "ban pharmacies"], "It increased penalties and enforcement.")

# 11 post Cold War
H('11.A', 3, "The Cold War is generally considered to have ended with what event?", "the collapse of the Soviet Union", ["the Cuban Missile Crisis", "the Korean War", "Pearl Harbor"], "The USSR dissolved in 1991.")
H('11.A', 3, "The Persian Gulf War (1991) began when Iraq did what?", "invaded Kuwait", ["attacked Israel", "bombed Saudi Arabia", "seized Iran"], "A U.S.-led coalition liberated Kuwait.")
H('11.A', 3, "The terrorist attacks of September 11, 2001 led to which U.S. response?", "the war in Afghanistan and the creation of the Department of Homeland Security", ["a return to isolationism", "the end of NATO", "a new draft only"], "The attacks reshaped U.S. foreign and domestic policy.")
H('11.C', 4, "Third-party candidate Ross Perot in 1992 mattered because he did what?", "drew a significant share of the popular vote", ["won the presidency", "won the House", "withdrew before the election"], "He won about 19 percent.")
H('11.C', 3, "In the 2000 election, Ralph Nader's third-party campaign is often cited for its impact in which state?", "Florida", ["Texas", "California", "Alaska"], "The close Florida margin was decisive.")

# 13 demographics
H('13.A', 3, "The Great Migration refers to the movement of African Americans from where to where?", "the rural South to Northern and Midwestern cities", ["the Midwest to the Pacific", "the North to the South", "Mexico to the East"], "Millions left for jobs and opportunity.")
H('13.A', 3, "Which postwar trend led many Americans to move toward the Sun Belt?", "air conditioning and job growth", ["colder weather", "ending of highways", "decline of defense jobs"], "The South and West grew.")
H('13.B', 3, "Immigration to the U.S. increased after 1965 because the Immigration and Nationality Act did what?", "ended national-origins quotas", ["banned all immigration", "reduced visas to zero", "limited entry to Europeans"], "It opened immigration from Asia and Latin America.")
H('13.B', 3, "Ellis Island served as what?", "an immigration station in New York Harbor", ["a prison", "a military fort", "a trading post"], "Millions entered the U.S. there.")

# 14 environment
H('14.B', 3, "The Environmental Protection Agency was created in 1970 to do what?", "enforce federal environmental regulations", ["build highways", "regulate banks", "manage the postal service"], "Established under Nixon.")
H('14.B', 3, "The Dust Bowl was worsened by what practice?", "plowing up grasslands without soil conservation", ["planting trees", "building canals", "rotating crops"], "Drought plus poor practices caused massive erosion.")
H('14.A', 3, "Rapid population growth in cities often leads to which environmental effect?", "increased air and water pollution", ["cleaner rivers", "more forests", "lower traffic"], "Growth strains the environment.")

# 15 economics
H('15.A', 3, "The Homestead Act of 1862 encouraged settlement of the West by doing what?", "offering land to settlers who farmed it", ["banning farming", "taxing land", "giving land to railroads only"], "It spurred migration to the Plains.")
H('15.A', 3, "The Transcontinental Railroad was completed in what year?", "1869", ["1849", "1889", "1909"], "The tracks joined at Promontory Summit.")
H('15.B', 3, "Interstate Commerce Act of 1887 aimed to do what?", "regulate railroad rates", ["ban labor unions", "limit immigration", "create the Federal Reserve"], "It created the first federal regulatory commission.")
H('15.C', 3, "The Chinese Exclusion Act of 1882 did what?", "barred Chinese laborers from entering the country", ["welcomed Chinese immigrants", "ended the railroad", "created Angel Island"], "It was the first major law restricting immigration by nationality.")
H('15.D', 3, "How did World War I affect the U.S. economy?", "it boosted industrial production and made the U.S. a creditor nation", ["it caused a depression", "it ended manufacturing", "it eliminated debt"], "Wartime demand increased output.")
H('16.A', 3, "A major cause of 1920s prosperity was what?", "growth in consumer goods and the automobile industry", ["a decline in production", "a ban on credit", "high unemployment"], "Mass production fueled growth.")
H('16.A', 3, "Calvin Coolidge's approach to the economy in the 1920s was characterized by what?", "limited government and low taxes", ["heavy regulation", "public works spending", "nationalization"], "Business-friendly policies defined the era.")
H('16.B', 3, "Which event is commonly associated with the start of the Great Depression?", "the stock market crash of 1929", ["the Spanish-American War", "the Dust Bowl", "the Marshall Plan"], "The crash exposed fragile financial conditions.")
H('16.B', 4, "Buying stocks on margin contributed to the crash because it did what?", "let investors borrow to buy stocks, magnifying losses when prices fell", ["required full cash payment", "made stocks safer", "banned speculation"], "Debt-financed speculation increased risk.")
H('16.C', 3, "Unemployment during the Great Depression reached about what level?", "one in four workers", ["one in fifty", "one in ten thousand", "none"], "About 25 percent were unemployed at the worst.")
H('16.D', 3, "The New Deal programs aimed to bring what?", "relief, recovery and reform", ["higher tariffs only", "isolation only", "ending government"], "The three Rs summarize the New Deal.")
H('16.E', 3, "The Federal Deposit Insurance Corporation (FDIC) was created to do what?", "insure bank deposits", ["build dams", "plant trees", "hire artists"], "It restored faith in banks.")
H('16.E', 3, "The Social Security Act of 1935 created a system for what?", "retirement and unemployment support", ["school desegregation", "interstate highways", "food rationing"], "It established old-age pensions.")
H('16.E', 3, "The Tennessee Valley Authority (TVA) brought what to the rural South?", "electricity and flood control", ["new state governments", "telephone monopolies", "free schooling"], "It built dams and power plants.")
H('17.A', 3, "World War II helped end the Great Depression by doing what?", "boosting production and creating jobs", ["raising unemployment", "cutting factories", "ending trade"], "War mobilization restored full employment.")
H('17.B', 3, "The GI Bill after World War II helped veterans by doing what?", "providing education and home-loan benefits", ["banning unions", "ending the draft", "taxing wages"], "It helped fuel postwar prosperity.")
H('17.B', 3, "The Baby Boom contributed to 1950s prosperity by doing what?", "increasing demand for homes and goods", ["lowering consumption", "ending suburbs", "reducing school needs"], "More families meant more consumption.")
H('17.C', 4, "President Eisenhower warned in 1961 about the influence of what?", "the military-industrial complex", ["the free press", "labor unions", "the Federal Reserve"], "His farewell address cautioned about defense spending.")
H('17.E', 3, "NAFTA, enacted in the 1990s, was designed to do what?", "reduce trade barriers among the U.S., Canada and Mexico", ["ban trade with Mexico", "tax imports", "create a currency union"], "It expanded North American trade.")

# 18 government
H('18.A', 3, "President Franklin Roosevelt's 'court-packing' plan in 1937 was an attempt to do what?", "add justices to the Supreme Court to gain support for New Deal laws", ["remove the Court", "end judicial review", "create a new branch"], "It was widely criticized and failed.")
H('18.B', 3, "Executive Order 9066 raised constitutional questions about what?", "civil liberties during wartime", ["the electoral college", "the census", "the right to bear arms"], "Internment tested due process rights.")
H('18.C', 3, "The Watergate scandal led to what?", "the resignation of President Nixon", ["a presidential impeachment trial of Reagan", "a second term for Nixon", "a Supreme Court vacancy"], "Nixon resigned in 1974.")
H('18.C', 3, "The Teapot Dome scandal involved what?", "bribery over oil reserves under Harding", ["a stock crash", "a war declaration", "Prohibition"], "Government officials took bribes for leases.")
H('18.D', 3, "The Americans with Disabilities Act (1990) prohibits what?", "discrimination against people with disabilities", ["immigration", "labor strikes", "taxation"], "It guarantees access and equal opportunity.")
H('19.A', 4, "The Gulf of Tonkin Resolution of 1964 gave the president authority to do what?", "use military force in Vietnam without a formal declaration of war", ["declare war on China", "end the draft", "withdraw troops"], "It later prompted debate about war powers.")
H('19.A', 4, "The War Powers Act of 1973 requires the president to do what?", "notify Congress soon after committing troops abroad", ["get approval from the Court", "obtain a UN vote", "end all deployments"], "Congress sought to check presidential war-making.")
H('19.B', 3, "Marbury v. Madison established which principle?", "judicial review", ["executive privilege", "states' rights", "implied powers"], "Courts can strike down unconstitutional laws.")
H('20.A', 3, "In Miranda v. Arizona (1966) the Court ruled that police must do what?", "inform suspects of their rights before questioning", ["stop all interrogations", "release all suspects", "keep records secret"], "The 'Miranda warning' stems from this case.")
H('20.A', 3, "Gideon v. Wainwright guaranteed what for defendants?", "the right to an attorney in felony cases", ["the right to remain silent only", "the right to a jury of peers only", "free speech"], "States must provide counsel for the poor.")
H('20.A', 3, "In Roe v. Wade (1973) the Court recognized what?", "a constitutional right to privacy covering abortion decisions", ["a ban on abortion", "school prayer", "campaign finance"], "The decision was later overturned in Dobbs v. Jackson (2022).")
H('20.B', 3, "The Sixteenth Amendment gave Congress the power to do what?", "levy an income tax", ["ban alcohol", "abolish slavery", "grant women the vote"], "It was ratified in 1913.")
H('20.B', 3, "The Nineteenth Amendment guaranteed what?", "women's suffrage", ["a federal income tax", "direct election of senators", "the end of Prohibition"], "Ratified in 1920.")

# 21 values
H('21.A', 3, "Which value is central to a constitutional republic?", "the rule of law", ["rule by one person", "inherited rank", "censorship"], "Laws bind both citizens and leaders.")
H('21.B', 3, "American values like individualism and free enterprise contrast with societies that emphasize what?", "strict state control of the economy", ["voting rights", "free speech", "private property"], "The U.S. system differs from command economies.")

# 22 participation
H('22.A', 3, "Lobbying is an effort to do what?", "influence lawmakers on a particular issue", ["count votes", "write a constitution", "draft recruits"], "Groups petition officials.")
H('22.B', 3, "The Twenty-fourth Amendment banned what?", "poll taxes in federal elections", ["literacy tests", "primary elections", "the electoral college"], "It removed a barrier used to suppress votes.")
H('22.D', 3, "Which step is required to become a naturalized citizen?", "passing a civics and English test", ["buying property", "serving in office", "paying a bond"], "Applicants must show knowledge of civics and English.")

# 23 leaders
H('23.A', 3, "Andrew Carnegie is associated with which industry?", "steel", ["oil", "railroads", "banking"], "He founded Carnegie Steel.")
H('23.A', 3, "John D. Rockefeller built a fortune in which industry?", "oil", ["steel", "textiles", "automobiles"], "He founded Standard Oil.")
H('23.B', 3, "The Congressional Medal of Honor recognizes what?", "extraordinary bravery in combat", ["political donations", "scientific discoveries", "athletic achievement"], "It is the nation's highest military decoration.")

# 24 culture
H('24.B', 3, "The Harlem Renaissance was a flowering of what?", "African American art, music and literature", ["factory production", "colonial settlement", "labor unions"], "It centered in New York in the 1920s.")
H('24.B', 3, "Which music genre emerged from African American communities in New Orleans in the early 1900s?", "jazz", ["country", "disco", "punk"], "Jazz shaped American culture.")
H('24.C', 3, "Hollywood movies and American music helped do what?", "spread American culture around the world", ["limit trade", "end radio", "isolate the U.S."], "Media spread U.S. culture globally.")

# 25 contributions
H('25.A', 3, "The women's suffrage movement worked to expand what?", "voting rights for women", ["property taxes", "military draft", "tariffs"], "Activists won the vote in 1920.")
H('25.B', 3, "American Indian boarding schools of the late 1800s were designed to do what?", "assimilate Native children into mainstream culture", ["preserve tribal languages", "teach tribal law", "prepare for statehood"], "Americanization efforts sought to erase tribal identity.")
H('25.D', 3, "Sonia Sotomayor became the first Latina to serve on what?", "the U.S. Supreme Court", ["the U.S. Senate", "the Cabinet", "the Federal Reserve"], "She was appointed in 2009.")

# 26-27 technology
H('26.A', 3, "Thomas Edison's work contributed to the spread of what?", "electric lighting and power", ["the telephone", "the steam engine", "the radio"], "He developed practical electric lighting systems.")
H('26.A', 3, "Alexander Graham Bell is credited with inventing what?", "the telephone", ["the telegraph", "the radio", "the television"], "Patented in 1876.")
H('26.C', 3, "Assembly line manufacturing changed the workplace by doing what?", "dividing tasks to speed production", ["ending factories", "ending wages", "banning machinery"], "Workers repeated specialized tasks.")
H('27.A', 3, "The Space Race between the U.S. and the Soviet Union began after the Soviets launched what?", "Sputnik", ["Apollo 11", "Skylab", "Vostok 5"], "The 1957 satellite startled Americans.")
H('27.A', 3, "Which mission first landed humans on the Moon?", "Apollo 11", ["Gemini 3", "Apollo 1", "Mercury 7"], "Neil Armstrong and Buzz Aldrin landed in 1969.")
H('27.B', 3, "The free enterprise system drives innovation by doing what?", "rewarding profitable new ideas", ["banning competition", "setting prices by law", "taxing all profit"], "Competition and profit motivate invention.")

# 28 skills
H('28.A', 3, "A political cartoon from 1900 shows a giant octopus labeled 'Standard Oil.' What is it most likely criticizing?", "the power of monopolies", ["the weather", "foreign tariffs", "farm prices"], "The octopus symbolizes grasping control.")
H('28.B', 3, "Placing the Civil Rights Act of 1964 before the Voting Rights Act of 1965 on a timeline is an example of what?", "sequencing events chronologically", ["averaging dates", "ignoring order", "mapping boundaries"], "Chronology orders events by time.")
H('28.D', 3, "A diary written during the Dust Bowl by a farmer is what kind of source?", "a primary source", ["a secondary source", "a textbook", "an encyclopedia entry"], "It was created at the time.")
H('28.D', 3, "A textbook chapter about the New Deal is what kind of source?", "a secondary source", ["a primary source", "an oral history", "a diary"], "It interprets events after the fact.")
H('28.E', 4, "A newspaper from 1917 describes German soldiers only in cruel terms. What should a historian consider?", "that wartime propaganda may shape the portrayal", ["that all details are neutral", "that bias cannot exist", "that the paper is a legal document"], "Wartime coverage can be biased.")
H('28.F', 3, "A strong historical claim should include what?", "supporting evidence and reasoning", ["only opinion", "only dates", "only a quotation"], "Claims need evidence.")
H('29.B', 3, "Using the term 'filibuster' correctly means referring to what?", "a tactic to delay a vote in the Senate", ["a type of tax", "a voting machine", "a campaign poster"], "Use social studies terminology accurately.")
H('30.A', 3, "Which visual would best show how the percentage of immigrants changed over time?", "a line graph", ["a pie chart of a single year", "a portrait", "a recipe"], "Line graphs show change over time.")
H('30.B', 3, "A map shows the highest population density along the coasts. Which question helps a student analyze this pattern?", "'Why do people tend to settle near coasts and rivers?'", ["'What color is the map?'", "'Who printed the map?'", "'How wide is the page?'"], "Questions about distribution build analysis.")
H('31.A', 3, "A mock election in class helps students understand what?", "voting and democratic processes", ["tax law", "military strategy", "currency exchange"], "Simulations model civic processes.")
H('31.B', 3, "In a decision-making process, what step comes right after identifying a problem?", "gathering information", ["announcing a decision", "ignoring options", "writing a conclusion"], "Gather information before considering options.")
H('12', 3, "How did the geography of the Great Plains contribute to the Dust Bowl?", "flat, dry land with little tree cover was vulnerable to wind erosion", ["heavy rainfall", "mountain barriers", "ocean winds"], "Geographic conditions amplified the disaster.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_ushist.jsonl'))

#!/usr/bin/env python3
"""High school World History Studies (TEKS 113.42.d). Original questions."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('113.42.d.', 996, own='hs_worldhist.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 1 turning points
H('1.A', 3, "The fall of the Western Roman Empire is traditionally dated to what year?", "476 CE", ["27 BCE", "1066 CE", "1453 CE"], "Odoacer deposed the last Western emperor in 476.")
H('1.A', 3, "The Byzantine Empire survived until its capital fell in what year?", "1453", ["476", "1066", "1648"], "The Ottomans captured Constantinople.")
H('1.B', 3, "Which event began the Protestant Reformation in 1517?", "Martin Luther posting his Ninety-five Theses", ["the signing of the Magna Carta", "the fall of Constantinople", "the Council of Nicaea"], "Luther challenged church practices such as the sale of indulgences.")
H('1.C', 3, "Which event ended the Thirty Years' War in 1648?", "the Peace of Westphalia", ["the Congress of Vienna", "the Treaty of Versailles", "the Edict of Nantes"], "It established principles of state sovereignty.")
H('1.D', 3, "In what year did the French Revolution begin?", "1789", ["1776", "1815", "1848"], "It began with the storming of the Bastille.")
H('1.E', 3, "The assassination of Archduke Franz Ferdinand in 1914 triggered which conflict?", "World War I", ["World War II", "the Crimean War", "the Cold War"], "It set off the alliance system.")
H('1.F', 3, "Which event is considered the end of the Cold War in Europe?", "the fall of the Berlin Wall in 1989", ["the Cuban Missile Crisis", "the Korean War", "the Berlin Airlift"], "It led to German reunification and the Soviet collapse.")

# 2 early civilizations
H('2.A', 3, "The Neolithic Revolution was the shift from what to what?", "hunting and gathering to farming", ["farming to factory work", "trade to barter", "city life to nomadism"], "Agriculture enabled settlements.")
H('2.B', 3, "Which is a characteristic of a civilization?", "organized government and social classes", ["no cities", "no writing", "no trade"], "Civilizations have cities, government, specialization, writing and religion.")
H('2.C', 3, "Which river valley civilization developed cuneiform writing?", "Mesopotamia", ["Egypt", "the Indus Valley", "Shang China"], "Sumerians wrote cuneiform on clay tablets.")
H('2.C', 3, "Egyptian civilization depended on which river?", "the Nile", ["the Tigris", "the Yellow", "the Ganges"], "Annual floods enriched farmland.")
H('2.C', 3, "Hammurabi is known for what?", "creating a written law code", ["building the pyramids", "founding Rome", "inventing the alphabet"], "The Code of Hammurabi set standards of justice.")

# 3 classical
H('3.A', 3, "The Persian Empire was known for what policy?", "religious tolerance and an efficient network of provinces", ["forced conversion", "isolation", "banning trade"], "Persian rulers like Cyrus allowed local customs.")
H('3.A', 3, "Athens is known as the birthplace of what form of government?", "direct democracy", ["absolute monarchy", "theocracy", "fascism"], "Citizens voted directly in the assembly.")
H('3.A', 3, "Which Greek philosopher was the teacher of Alexander the Great?", "Aristotle", ["Plato", "Socrates", "Homer"], "Aristotle tutored the young Alexander.")
H('3.A', 4, "Roman law influenced later legal systems through the idea that what?", "all citizens are subject to written law", ["rulers are above the law", "laws should be secret", "law is only custom"], "The Twelve Tables and later codes shaped Western law.")
H('3.B', 3, "The fall of Rome in the West led to what in Europe?", "the rise of feudalism and a decline in centralized government", ["a stronger empire", "democracy", "industrialization"], "Local lords gained power.")
H('3.C', 4, "Which problem contributed to the collapse of both Rome and Han China?", "weak central government and external invasions", ["too much trade", "lack of cities", "lack of religion"], "Both faced internal decay and nomadic pressure.")

# 4 postclassical
H('4.A', 3, "The Great Schism of 1054 divided Christianity into what two branches?", "Roman Catholic and Eastern Orthodox", ["Protestant and Catholic", "Sunni and Shia", "Buddhist and Hindu"], "East and West split over authority and doctrine.")
H('4.B', 3, "Feudalism in medieval Europe was a system in which what?", "lords granted land to vassals in exchange for service", ["peasants owned the land", "kings held no power", "cities ruled the countryside"], "Land and loyalty bound society.")
H('4.C', 3, "Islam spread rapidly after the death of Muhammad in 632 through what?", "conquest and trade", ["only missions", "isolation", "a single treaty"], "Arab armies and merchants spread the religion.")
H('4.D', 4, "In medieval Spain, a period of relative cooperation among Muslims, Christians and Jews is often called what?", "convivencia", ["the Reconquista", "the Crusades", "the Inquisition"], "Cultural exchange flourished in al-Andalus.")
H('4.E', 3, "Which Muslim dynasty ruled much of northern India beginning in the 1500s?", "the Mughal Empire", ["the Ottoman Empire", "the Safavid Empire", "the Gupta Empire"], "The Mughals blended Islamic and Hindu traditions.")
H('4.F', 3, "The Black Death reduced Europe's population and led to what?", "labor shortages and weakening of feudalism", ["population booms", "a stronger manor system", "the end of trade"], "Fewer workers meant higher wages.")
H('4.F', 3, "The Crusades increased European contact with what?", "Eastern trade goods and ideas", ["the Americas", "Australia", "Antarctica"], "They opened trade routes to the East.")
H('4.G', 3, "The Song Dynasty of China is known for which innovations?", "gunpowder, the compass and movable-type printing", ["steam engines", "telegraphs", "airplanes"], "The Song era saw major technological progress.")
H('4.H', 3, "The trans-Saharan slave trade carried enslaved Africans to where?", "North Africa and the Middle East", ["Australia", "Iceland", "Siberia"], "It predated the Atlantic slave trade.")
H('4.I', 3, "The Silk Road connected China with what regions?", "Central Asia, the Middle East and Europe", ["North America", "Australia", "Antarctica"], "It carried goods, religions and ideas.")
H('4.I', 3, "In West Africa, gold was traded for what valuable commodity from the Sahara?", "salt", ["silk", "tea", "spices"], "Salt was scarce in the forest zone.")
H('4.J', 3, "The Mongol Empire promoted trade across Eurasia through what?", "the Pax Mongolica", ["the Silk Embargo", "the Hanseatic League", "the Council of Trent"], "The Mongols secured trade routes.")
H('4.J', 4, "Which Mongol ruler founded the Yuan Dynasty in China?", "Kublai Khan", ["Genghis Khan", "Tamerlane", "Attila"], "Kublai Khan was Genghis Khan's grandson.")

# 5 renaissance/reformation
H('5.A', 3, "The Renaissance began in which region of Europe?", "Italy", ["Scandinavia", "Spain", "Poland"], "City-states like Florence led the revival.")
H('5.A', 3, "Which Renaissance artist painted the Mona Lisa and designed flying machines?", "Leonardo da Vinci", ["Michelangelo", "Raphael", "Donatello"], "Leonardo was a painter, scientist and inventor.")
H('5.A', 3, "Humanism emphasized what?", "the value of individual potential and classical learning", ["rejecting all learning", "obedience only", "isolation"], "Renaissance thinkers revived Greek and Roman texts.")
H('5.B', 3, "The Reformation led to the creation of which new Christian groups?", "Protestant churches", ["the Eastern Orthodox Church", "Islam", "Buddhism"], "Lutherans, Calvinists and Anglicans emerged.")
H('5.B', 3, "King Henry VIII founded the Church of England largely because he did what?", "wanted an annulment the pope refused", ["admired Luther's doctrine", "wanted to convert to Islam", "was ordered by Parliament"], "He broke from Rome in the 1530s.")

# 6 Americas
H('6.A', 3, "The Maya are known for what achievement?", "a sophisticated writing system and calendar", ["steam power", "gunpowder", "the printing press"], "They developed glyphs and astronomy.")
H('6.A', 3, "The Aztec capital Tenochtitlan stood on the site of present-day what?", "Mexico City", ["Lima", "Bogotá", "Havana"], "It was built on an island in Lake Texcoco.")
H('6.A', 3, "The Inca Empire built an extensive system of what?", "roads across the Andes", ["canals across the Amazon", "railroads", "seaports in Europe"], "The road network united the empire.")
H('6.B', 3, "Which Spanish conquistador conquered the Aztec Empire?", "Hernán Cortés", ["Francisco Pizarro", "Vasco da Gama", "Ferdinand Magellan"], "Cortés allied with local peoples and used disease and force.")
H('6.B', 3, "Which conquistador overthrew the Inca Empire?", "Francisco Pizarro", ["Hernán Cortés", "Christopher Columbus", "Juan Ponce de León"], "Pizarro captured Atahualpa in 1532.")
H('6.B', 3, "A major reason for the collapse of the Aztec and Inca empires was what?", "European diseases such as smallpox", ["lack of food", "volcanic eruptions", "civil wars alone"], "Epidemics devastated the populations.")

# 7 exploration
H('7.A', 3, "Which motives drove European exploration after 1450?", "gold, God and glory", ["isolation and secrecy", "a ban on trade", "religious withdrawal"], "Wealth, religion and prestige motivated explorers.")
H('7.A', 4, "The fall of Constantinople in 1453 encouraged Europeans to seek new routes to Asia because it did what?", "disrupted traditional overland trade routes", ["opened the Silk Road", "ended trade", "ended Ottoman power"], "Ottoman control raised costs.")
H('7.B', 3, "The Columbian Exchange refers to what?", "the transfer of plants, animals, diseases and people between the hemispheres", ["a type of bank", "a trade treaty", "a war"], "It transformed both worlds.")
H('7.B', 3, "Which crop from the Americas became a staple in Europe?", "the potato", ["wheat", "rice", "olives"], "It boosted European population.")
H('7.C', 3, "The Atlantic slave trade had what effect on West Africa?", "loss of population and disruption of societies", ["growth of cities", "peace", "increased literacy"], "Millions were forcibly removed.")
H('7.C', 3, "The 'Middle Passage' refers to what?", "the voyage that carried enslaved Africans across the Atlantic", ["a canal in Panama", "a trade route in Asia", "a mountain pass in the Alps"], "Conditions were brutal.")
H('7.D', 3, "The Ottoman Empire controlled which key city after 1453?", "Constantinople (Istanbul)", ["Rome", "Vienna", "Moscow"], "Mehmed II conquered it.")
H('7.E', 3, "Ming China's treasure voyages under Zheng He demonstrated what?", "China's naval power and reach in the Indian Ocean", ["isolationism", "military conquest of Europe", "the discovery of America"], "Fleets visited Southeast Asia, India and East Africa.")
H('7.F', 3, "Mercantilism held that a nation's strength depends on what?", "exporting more than it imports and accumulating precious metals", ["abolishing trade", "free markets only", "tariff-free borders"], "Colonies provided raw materials.")
H('7.F', 3, "Joint-stock companies helped finance exploration by doing what?", "pooling investors' money to share risk", ["banning investment", "creating monarchies", "ending trade"], "The Dutch East India Company was one example.")

# 8 Industrial revolution and imperialism
H('8.A', 3, "The Industrial Revolution began in which country?", "Great Britain", ["France", "Germany", "Russia"], "Textiles, coal and iron drove early industrialization.")
H('8.A', 3, "A social effect of industrialization was what?", "rapid growth of cities", ["decline of cities", "end of factories", "return to farming"], "Workers moved to industrial centers.")
H('8.B', 4, "Which motive was NOT a major driver of European imperialism?", "a desire to preserve local traditions", ["access to raw materials", "new markets", "national prestige"], "Imperialism sought resources, markets and power.")
H('8.C', 3, "The Berlin Conference of 1884-1885 was held to do what?", "divide Africa among European powers", ["end slavery in the U.S.", "unify Germany", "form NATO"], "No African leaders were present.")
H('8.C', 3, "Sepoys in the Indian Rebellion of 1857 were what?", "Indian soldiers in the British East India Company's army", ["Mongol raiders", "Ottoman officials", "Japanese samurai"], "Their revolt challenged British rule.")
H('8.D', 3, "Free enterprise fueled the Industrial Revolution by doing what?", "rewarding investment and innovation", ["banning private property", "setting all prices by law", "preventing competition"], "Capital and competition drove growth.")

# 9 revolutions
H('9.A', 4, "Both the American and French Revolutions were influenced by what ideas?", "Enlightenment ideas of natural rights and popular sovereignty", ["divine right of kings", "mercantilism", "feudal loyalty"], "Thinkers like Locke and Rousseau inspired both.")
H('9.B', 3, "Napoleon Bonaparte's Napoleonic Code did what?", "reformed laws and spread legal equality across Europe", ["restored feudalism", "banned education", "ended property rights"], "It influenced legal systems worldwide.")
H('9.B', 3, "Napoleon's army was crippled by his invasion of which country in 1812?", "Russia", ["Spain", "Egypt", "Italy"], "Winter and scorched earth destroyed his army.")
H('9.C', 3, "Which leader helped free much of South America from Spanish rule?", "Simón Bolívar", ["Napoleon", "Garibaldi", "Peter the Great"], "He led campaigns in Venezuela, Colombia and beyond.")
H('9.C', 3, "The Haitian Revolution was led by which formerly enslaved leader?", "Toussaint Louverture", ["Simón Bolívar", "José de San Martín", "Miguel Hidalgo"], "It created the first independent Black republic in the Americas.")
H('9.D', 3, "Montesquieu's idea of separation of powers influenced which document?", "the U.S. Constitution", ["the Magna Carta", "the Domesday Book", "the Code of Hammurabi"], "The Framers divided government into branches.")

# 10 WWI
H('10.A', 3, "Which four factors are commonly cited as long-term causes of World War I?", "militarism, alliances, imperialism and nationalism", ["isolationism, pacifism, democracy and trade", "feudalism, mercantilism, fascism and communism", "socialism, capitalism, humanism and monarchy"], "The acronym MAIN summarizes them.")
H('10.B', 3, "The idea of 'total war' in World War I meant what?", "the economy and society were mobilized for war", ["only soldiers fought", "wars were short", "wars were fought only at sea"], "Entire nations supported the war effort.")
H('10.C', 3, "A key provision of the Treaty of Versailles was that Germany had to do what?", "accept blame and pay reparations", ["receive new territory", "join the League as a leader", "rearm"], "The 'war guilt clause' angered Germans.")
H('10.D', 3, "The October Revolution of 1917 in Russia brought which group to power?", "the Bolsheviks led by Lenin", ["the Mensheviks", "the tsar's army", "the Duma liberals"], "It created the first communist state.")
H('10.D', 3, "A cause of the February Revolution in Russia was what?", "food shortages and war weariness", ["a rise in prosperity", "peace with Germany", "a rich harvest"], "Workers and soldiers revolted against Tsar Nicholas II.")

# 11 Depression
H('11.A', 3, "Which factor contributed to the global depression of the 1930s?", "collapse of world trade and bank failures", ["overproduction of luxury goods only", "excess gold", "agricultural booms"], "Protective tariffs and failing banks spread the crisis.")
H('11.B', 3, "In Germany, economic hardship during the depression helped which party gain support?", "the Nazi Party", ["the Social Democrats", "the Monarchists", "the Zionists"], "Desperation fueled extremist movements.")

# 12 totalitarianism, WWII
H('12.A', 3, "Which characteristic is typical of totalitarian states?", "total government control of public and private life", ["free elections", "independent courts", "a free press"], "Propaganda and secret police enforce control.")
H('12.B', 3, "Which leader established Fascism in Italy?", "Benito Mussolini", ["Adolf Hitler", "Joseph Stalin", "Francisco Franco"], "He became Prime Minister in 1922.")
H('12.B', 3, "Joseph Stalin ruled the Soviet Union through what?", "a command economy and brutal repression", ["a free market", "a constitutional monarchy", "direct democracy"], "Collectivization and purges marked his rule.")
H('12.C', 3, "World War II in Europe began when Germany invaded which country?", "Poland", ["France", "Austria", "Belgium"], "Britain and France declared war in September 1939.")
H('12.C', 4, "The policy of appeasement at the Munich Conference gave Hitler control of what?", "the Sudetenland in Czechoslovakia", ["Poland", "Austria", "Denmark"], "The agreement of 1938 failed to prevent war.")
H('12.C', 3, "The Battle of Stalingrad was a turning point on which front?", "the Eastern Front", ["the Pacific", "North Africa", "the Western Front"], "The German army was defeated by the Soviets.")

# 13 Cold War, post 1945
H('13.A', 3, "The Cold War was a rivalry primarily between which two superpowers?", "the United States and the Soviet Union", ["Britain and France", "China and Japan", "Germany and Italy"], "They competed ideologically and strategically.")
H('13.B', 3, "Mao Zedong established the People's Republic of China in what year?", "1949", ["1919", "1989", "1936"], "Communists won the civil war.")
H('13.C', 3, "The Berlin Wall, built in 1961, was meant to do what?", "stop East Germans from fleeing to the West", ["unite Germany", "separate France from Germany", "protect Poland"], "It divided Berlin until 1989.")
H('13.D', 3, "Mikhail Gorbachev's policies of glasnost and perestroika meant what?", "openness and economic restructuring", ["war and expansion", "isolation and censorship", "monarchy and religion"], "They helped end the Cold War.")
H('13.E', 3, "Mohandas Gandhi led India's independence movement using what method?", "nonviolent civil disobedience", ["guerrilla warfare", "terrorism", "armed conquest"], "The Salt March was a famous example.")
H('13.E', 3, "India gained independence from Britain in what year?", "1947", ["1857", "1919", "1965"], "Partition created India and Pakistan.")
H('13.E', 3, "Which African leader led Ghana to independence in 1957?", "Kwame Nkrumah", ["Nelson Mandela", "Jomo Kenyatta", "Patrice Lumumba"], "Ghana was the first sub-Saharan colony to gain independence.")
H('13.F', 3, "In 1948 the state of Israel was founded following which event?", "the end of the British mandate and a UN partition plan", ["the Cuban Missile Crisis", "the Suez Crisis", "the Six-Day War"], "Neighboring Arab states rejected the partition.")

# 14 terrorism
H('14.A', 4, "The Soviet invasion of Afghanistan in 1979 contributed to what?", "the rise of militant groups that later included al-Qaeda", ["a stable democracy", "an end to conflict", "U.S. troop withdrawal"], "Foreign fighters and weapons flowed in.")
H('14.B', 3, "The September 11, 2001 attacks were carried out by which terrorist organization?", "al-Qaeda", ["Hamas", "the Taliban", "Hezbollah"], "Osama bin Laden's group planned the attacks.")
H('14.C', 3, "The U.S. response to September 11 included the war in what country?", "Afghanistan", ["Vietnam", "Korea", "Cuba"], "The Taliban government sheltered al-Qaeda.")

# 15 geography
H('15.A', 3, "The Fertile Crescent lies in which region?", "the Middle East", ["South America", "Scandinavia", "Southern Africa"], "Early agriculture developed there.")
H('15.B', 3, "Which physical feature most influenced the isolation of early China?", "mountains, deserts and seas surrounding it", ["frozen lakes only", "dense forests only", "a shared border with Europe"], "Geography shaped its cultural development.")
H('15.B', 3, "Why did ancient Egypt grow along the Nile?", "annual floods deposited fertile silt", ["constant rainfall", "volcanic soil", "glaciers"], "Geography shaped the economy.")
H('15.C', 3, "A map showing trade routes between Asia and Europe helps explain what?", "how goods and ideas spread", ["the number of presidents", "the length of rivers only", "the size of armies"], "Maps reveal historical connections.")

# 16 economics
H('16.A', 3, "Which change did the Neolithic Revolution bring to human life?", "permanent settlements and food surpluses", ["constant migration", "the end of tools", "smaller populations"], "Farming allowed specialization.")
H('16.C', 3, "Globalization has resulted in what?", "increased trade and interconnection among nations", ["decreased trade", "fewer ports", "isolated economies"], "Goods, capital and ideas cross borders faster.")

# 17 economic systems
H('17.A', 3, "Adam Smith argued that free markets work best when what is allowed?", "individuals pursue self-interest in competition", ["government sets all prices", "monopolies control trade", "trade is banned"], "He called it the invisible hand.")
H('17.B', 3, "Karl Marx predicted that capitalism would be replaced by what?", "a classless communist society", ["a feudal order", "a monarchy", "fascism"], "He wrote The Communist Manifesto with Friedrich Engels.")
H('17.C', 3, "Socialism generally advocates what?", "public or collective ownership of key industries", ["no government", "absolute monarchy", "unregulated markets"], "It seeks to reduce inequality.")
H('17.D', 3, "Fascism is characterized by what?", "extreme nationalism and dictatorial power", ["direct democracy", "classless society", "free-market anarchy"], "Fascist states suppress opposition.")
H('17.E', 4, "Why did communist command economies often collapse in competition with market economies?", "lack of incentives and inefficient central planning", ["too much competition", "too much trade", "lack of government"], "Central planners struggled to meet demand.")

# 18-19 government
H('18.A', 3, "In an absolute monarchy, the ruler does what?", "holds nearly unlimited power", ["shares power with an elected body", "is chosen by lottery", "serves a fixed term"], "Louis XIV is an example.")
H('18.B', 3, "A theocracy is a government in which what?", "religious leaders rule in the name of a deity", ["generals rule", "citizens vote on all laws", "kings share power with Parliament"], "Iran today has theocratic elements.")
H('19.A', 3, "The idea of democratic-republican government began in which ancient societies?", "Greece and Rome", ["Egypt and Persia", "China and India", "the Aztecs and Incas"], "Athens had democracy; Rome had a republic.")
H('19.B', 3, "The Magna Carta (1215) established the principle that what?", "even the king must obey the law", ["kings were divinely appointed", "nobles had no rights", "Parliament was abolished"], "It limited royal power.")
H('19.B', 3, "The English Bill of Rights (1689) limited the power of whom?", "the monarchy", ["Parliament", "the courts only", "the church only"], "It affirmed parliamentary supremacy.")
H('19.C', 3, "Which philosopher argued that people have natural rights to life, liberty and property?", "John Locke", ["Thomas Hobbes", "Niccolò Machiavelli", "Karl Marx"], "His ideas influenced the Declaration of Independence.")
H('19.C', 4, "Thomas Hobbes argued that people need a strong government because what?", "without it, life would be 'nasty, brutish and short'", ["people are naturally good", "government is unnecessary", "rulers should be elected weekly"], "Hobbes feared the state of nature.")
H('19.D', 3, "The United Nations was created after World War II to do what?", "maintain international peace and cooperation", ["rebuild Germany", "control trade", "end colonialism overnight"], "It replaced the League of Nations.")
H('19.D', 3, "A reason the League of Nations failed was that what?", "the United States never joined and it lacked enforcement power", ["it was too powerful", "it conquered nations", "it ended the war early"], "It could not stop aggression in the 1930s.")

# 20-21 citizenship and rights
H('20.A', 3, "Which is an example of people supporting or changing their government?", "voting in elections", ["ignoring laws", "avoiding taxes", "hiding records"], "Participation includes voting and protest.")
H('20.C', 3, "Nelson Mandela is remembered for leading resistance to what?", "apartheid in South Africa", ["Soviet rule", "British rule in India", "Nazi occupation"], "He became South Africa's first Black president.")
H('21.A', 3, "The rule of law means that what?", "everyone, including leaders, must obey the law", ["rulers are above the law", "laws apply only to the poor", "laws change daily"], "It is a foundation of just government.")
H('21.B', 3, "The idea of trial by a jury of peers is rooted in which document?", "the Magna Carta", ["the Domesday Book", "the Ninety-five Theses", "the Code of Hammurabi"], "It promised judgment by one's equals.")
H('21.C', 3, "The Khmer Rouge regime in Cambodia is associated with what?", "mass killings in the 1970s", ["a trade boom", "democratic reform", "a space program"], "Under Pol Pot, about two million died.")
H('21.D', 3, "The Armenian Genocide took place during which conflict?", "World War I", ["World War II", "the Cold War", "the Crimean War"], "Ottoman authorities killed about 1.5 million Armenians.")
H('21.E', 3, "Aung San Suu Kyi is associated with resistance to military rule in what country?", "Myanmar (Burma)", ["Thailand", "Vietnam", "Laos"], "She won the Nobel Peace Prize in 1991.")

# 22 religion
H('22.A', 3, "Which three religions are monotheistic and trace roots to Abraham?", "Judaism, Christianity and Islam", ["Hinduism, Buddhism and Shinto", "Confucianism, Daoism and Jainism", "Zoroastrianism, Sikhism and Shinto"], "They worship one God.")
H('22.B', 3, "Buddhism began in India with the teachings of whom?", "Siddhartha Gautama", ["Confucius", "Muhammad", "Zoroaster"], "He became known as the Buddha.")
H('22.B', 3, "Which religion teaches the cycle of reincarnation and the concept of karma?", "Hinduism", ["Islam", "Judaism", "Confucianism"], "Hindu beliefs include dharma and moksha.")
H('22.C', 3, "The Crusades are an example of what?", "religion influencing political and military events", ["economics ending religion", "science ending war", "trade replacing faith"], "Popes called Christians to retake the Holy Land.")

# 23 women
H('23.A', 3, "During the Industrial Revolution many women and children did what?", "worked in factories", ["abandoned work", "owned most mills", "led governments"], "Low-wage labor was common.")
H('23.B', 3, "Queen Elizabeth I is associated with which era?", "the English Renaissance and the defeat of the Spanish Armada", ["the Industrial Revolution", "the Cold War", "the Crusades"], "She ruled from 1558 to 1603.")
H('23.B', 3, "Catherine the Great expanded the territory of what country?", "Russia", ["France", "Spain", "Austria"], "She ruled from 1762 to 1796.")

# 24 east/west
H('24.A', 3, "Confucianism emphasizes what?", "respect for family and social harmony", ["conquest", "isolation", "monotheism"], "It guided Chinese government and society.")
H('24.B', 3, "Which Western civilization contributed the concept of democracy?", "ancient Greece", ["ancient Persia", "ancient Egypt", "ancient China"], "Athens developed direct democracy.")
H('24.C', 4, "Renaissance humanism led to a conflict with traditional church authority by doing what?", "emphasizing individual reasoning alongside faith", ["rejecting all religion", "banning books", "ending education"], "Humanists revived classical learning.")

# 25 culture
H('25.A', 3, "The Gothic cathedral reflected the medieval culture by doing what?", "expressing religious devotion through towering architecture", ["celebrating science", "promoting democracy", "replacing churches"], "Its height pointed toward heaven.")
H('25.B', 3, "Which composer's music has transcended the culture in which it was written?", "Ludwig van Beethoven", ["Napoleon Bonaparte", "Isaac Newton", "Karl Marx"], "His symphonies are performed worldwide.")

# 26 science/tech
H('26.A', 3, "Which number system, developed in India, spread through the Islamic world to Europe?", "Hindu-Arabic numerals", ["Roman numerals", "Mayan numerals", "Babylonian numerals"], "It includes the concept of zero.")
H('26.C', 3, "Johannes Gutenberg's printing press helped spread what?", "ideas of the Renaissance and Reformation", ["feudalism", "illiteracy", "divine right"], "It lowered the cost of books.")
H('26.D', 3, "The Scientific Revolution emphasized what?", "observation, experiment and reason", ["tradition only", "magic", "divine revelation only"], "It transformed views of nature.")
H('26.E', 3, "Which scientist proposed that Earth orbits the sun?", "Nicolaus Copernicus", ["Ptolemy", "Aristotle", "Galen"], "He challenged the geocentric model.")
H('26.E', 3, "Isaac Newton is best known for formulating what?", "the laws of motion and universal gravitation", ["the theory of evolution", "the periodic table", "germ theory"], "His Principia appeared in 1687.")

# 27 technology
H('27.A', 3, "James Watt improved which invention, powering factories and trains?", "the steam engine", ["the telegraph", "the printing press", "the cotton gin"], "Steam power drove the Industrial Revolution.")
H('27.B', 3, "The Bessemer process made which material cheaper and stronger?", "steel", ["glass", "paper", "cement"], "It supported railroads and buildings.")
H('27.C', 3, "A major new weapon in World War I was what?", "the machine gun", ["the crossbow", "the catapult", "the musket"], "It made frontal assaults deadly.")
H('27.C', 3, "World War II ended in the Pacific after the use of what?", "atomic bombs", ["trench warfare", "chemical gas", "longbows"], "Hiroshima and Nagasaki were bombed in August 1945.")
H('27.D', 3, "The internet has contributed to globalization by doing what?", "speeding communication and trade across borders", ["limiting information", "ending trade", "isolating nations"], "Digital networks connect the world.")
H('27.E', 3, "Marie Curie is known for her research on what?", "radioactivity", ["gravity", "electromagnetism", "evolution"], "She won Nobel Prizes in physics and chemistry.")

# 28 skills
H('28.A', 3, "Which scientist studies artifacts and ancient remains to learn about the past?", "an archaeologist", ["a meteorologist", "an economist", "a botanist"], "Archaeologists excavate sites.")
H('28.B', 3, "When historians consider a source's frame of reference, they ask what?", "who created it and what viewpoint shaped it", ["how long it is", "what color it is", "where it was stored"], "Perspective shapes accounts.")
H('28.C', 3, "A letter from a soldier in World War I is what kind of source?", "a primary source", ["a secondary source", "a textbook", "a documentary"], "It was written at the time.")
H('28.D', 3, "Which clue helps evaluate a source's credibility?", "the author's expertise and use of evidence", ["its length", "its font", "its price"], "Credible sources are reliable and evidence-based.")
H('28.E', 3, "Sorting events into political, economic and social categories is an example of what?", "categorizing information", ["averaging data", "ignoring causes", "mapping rivers"], "Categorizing organizes evidence.")
H('28.F', 3, "A good historical argument links a claim to what?", "evidence and reasoning", ["opinion only", "dates only", "pictures only"], "Evidence supports claims.")
H('29.A', 3, "A thematic map of colonial empires in 1914 shows what?", "which powers controlled which territories", ["the length of rivers", "the sizes of armies", "the elevation of mountains"], "Thematic maps show specific data.")
H('29.B', 3, "Comparing two maps of Europe from 1914 and 1919 helps show what?", "changes in political boundaries after World War I", ["changes in climate", "changes in rainfall", "changes in tides"], "Boundary shifts followed the treaties.")
H('30.A', 3, "Which term means a government controlled by a single leader with unlimited power?", "dictatorship", ["republic", "democracy", "federation"], "Using precise terms matters.")
H('30.B', 3, "To avoid plagiarism, a student should do what?", "cite sources and paraphrase in their own words", ["copy and paste without credit", "change a few words only", "omit references"], "Credit others' ideas.")
H('30.D', 3, "Civil discourse about a controversial topic means doing what?", "listening respectfully and supporting claims with evidence", ["interrupting", "insulting others", "ignoring facts"], "Respect and evidence guide discussion.")
H('31.A', 3, "A caucus is a meeting in which what happens?", "party members gather to select candidates or delegates", ["a trial is held", "taxes are collected", "laws are written"], "Caucuses are a form of party selection.")
H('31.B', 3, "After listing possible solutions to a problem, what is the next step in decision making?", "evaluating the choices and selecting one", ["ignoring the options", "starting a new problem", "repeating research"], "Weigh options before choosing.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_worldhist.jsonl'))

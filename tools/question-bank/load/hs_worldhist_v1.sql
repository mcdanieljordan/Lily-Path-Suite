insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_worldhist_v1'
from (values
('113.42.d.1.A',3,'The fall of the Western Roman Empire is traditionally dated to what year?','["476 CE", "1453 CE", "27 BCE", "1066 CE"]'::jsonb,0,'Odoacer deposed the last Western emperor in 476.','original'),
('113.42.d.1.A',3,'The Byzantine Empire survived until its capital fell in what year?','["476", "1453", "1648", "1066"]'::jsonb,1,'The Ottomans captured Constantinople.','original'),
('113.42.d.1.B',3,'Which event began the Protestant Reformation in 1517?','["the signing of the Magna Carta", "the fall of Constantinople", "Martin Luther posting his Ninety-five Theses", "the Council of Nicaea"]'::jsonb,2,'Luther challenged church practices such as the sale of indulgences.','original'),
('113.42.d.1.C',3,'Which event ended the Thirty Years'' War in 1648?','["the Treaty of Versailles", "the Congress of Vienna", "the Edict of Nantes", "the Peace of Westphalia"]'::jsonb,3,'It established principles of state sovereignty.','original'),
('113.42.d.1.D',3,'In what year did the French Revolution begin?','["1789", "1776", "1815", "1848"]'::jsonb,0,'It began with the storming of the Bastille.','original'),
('113.42.d.1.E',3,'The assassination of Archduke Franz Ferdinand in 1914 triggered which conflict?','["the Cold War", "World War I", "World War II", "the Crimean War"]'::jsonb,1,'It set off the alliance system.','original'),
('113.42.d.1.F',3,'Which event is considered the end of the Cold War in Europe?','["the Berlin Airlift", "the Cuban Missile Crisis", "the fall of the Berlin Wall in 1989", "the Korean War"]'::jsonb,2,'It led to German reunification and the Soviet collapse.','original'),
('113.42.d.2.A',3,'The Neolithic Revolution was the shift from what to what?','["farming to factory work", "city life to nomadism", "trade to barter", "hunting and gathering to farming"]'::jsonb,3,'Agriculture enabled settlements.','original'),
('113.42.d.2.B',3,'Which is a characteristic of a civilization?','["organized government and social classes", "no cities", "no writing", "no trade"]'::jsonb,0,'Civilizations have cities, government, specialization, writing and religion.','original'),
('113.42.d.2.C',3,'Which river valley civilization developed cuneiform writing?','["Egypt", "Mesopotamia", "the Indus Valley", "Shang China"]'::jsonb,1,'Sumerians wrote cuneiform on clay tablets.','original'),
('113.42.d.2.C',3,'Egyptian civilization depended on which river?','["the Tigris", "the Yellow", "the Nile", "the Ganges"]'::jsonb,2,'Annual floods enriched farmland.','original'),
('113.42.d.2.C',3,'Hammurabi is known for what?','["inventing the alphabet", "building the pyramids", "founding Rome", "creating a written law code"]'::jsonb,3,'The Code of Hammurabi set standards of justice.','original'),
('113.42.d.3.A',3,'The Persian Empire was known for what policy?','["religious tolerance and an efficient network of provinces", "isolation", "forced conversion", "banning trade"]'::jsonb,0,'Persian rulers like Cyrus allowed local customs.','original'),
('113.42.d.3.A',3,'Athens is known as the birthplace of what form of government?','["absolute monarchy", "direct democracy", "theocracy", "fascism"]'::jsonb,1,'Citizens voted directly in the assembly.','original'),
('113.42.d.3.A',3,'Which Greek philosopher was the teacher of Alexander the Great?','["Plato", "Homer", "Aristotle", "Socrates"]'::jsonb,2,'Aristotle tutored the young Alexander.','original'),
('113.42.d.3.A',4,'Roman law influenced later legal systems through the idea that what?','["rulers are above the law", "laws should be secret", "law is only custom", "all citizens are subject to written law"]'::jsonb,3,'The Twelve Tables and later codes shaped Western law.','original'),
('113.42.d.3.B',3,'The fall of Rome in the West led to what in Europe?','["the rise of feudalism and a decline in centralized government", "a stronger empire", "industrialization", "democracy"]'::jsonb,0,'Local lords gained power.','original'),
('113.42.d.3.C',4,'Which problem contributed to the collapse of both Rome and Han China?','["lack of cities", "weak central government and external invasions", "lack of religion", "too much trade"]'::jsonb,1,'Both faced internal decay and nomadic pressure.','original'),
('113.42.d.4.A',3,'The Great Schism of 1054 divided Christianity into what two branches?','["Protestant and Catholic", "Sunni and Shia", "Roman Catholic and Eastern Orthodox", "Buddhist and Hindu"]'::jsonb,2,'East and West split over authority and doctrine.','original'),
('113.42.d.4.B',3,'Feudalism in medieval Europe was a system in which what?','["kings held no power", "cities ruled the countryside", "peasants owned the land", "lords granted land to vassals in exchange for service"]'::jsonb,3,'Land and loyalty bound society.','original'),
('113.42.d.4.C',3,'Islam spread rapidly after the death of Muhammad in 632 through what?','["conquest and trade", "only missions", "a single treaty", "isolation"]'::jsonb,0,'Arab armies and merchants spread the religion.','original'),
('113.42.d.4.D',4,'In medieval Spain, a period of relative cooperation among Muslims, Christians and Jews is often called what?','["the Crusades", "convivencia", "the Inquisition", "the Reconquista"]'::jsonb,1,'Cultural exchange flourished in al-Andalus.','original'),
('113.42.d.4.E',3,'Which Muslim dynasty ruled much of northern India beginning in the 1500s?','["the Ottoman Empire", "the Safavid Empire", "the Mughal Empire", "the Gupta Empire"]'::jsonb,2,'The Mughals blended Islamic and Hindu traditions.','original'),
('113.42.d.4.F',3,'The Black Death reduced Europe''s population and led to what?','["population booms", "the end of trade", "a stronger manor system", "labor shortages and weakening of feudalism"]'::jsonb,3,'Fewer workers meant higher wages.','original'),
('113.42.d.4.F',3,'The Crusades increased European contact with what?','["Eastern trade goods and ideas", "Antarctica", "the Americas", "Australia"]'::jsonb,0,'They opened trade routes to the East.','original'),
('113.42.d.4.G',3,'The Song Dynasty of China is known for which innovations?','["steam engines", "gunpowder, the compass and movable-type printing", "airplanes", "telegraphs"]'::jsonb,1,'The Song era saw major technological progress.','original'),
('113.42.d.4.H',3,'The trans-Saharan slave trade carried enslaved Africans to where?','["Siberia", "Iceland", "North Africa and the Middle East", "Australia"]'::jsonb,2,'It predated the Atlantic slave trade.','original'),
('113.42.d.4.I',3,'The Silk Road connected China with what regions?','["Australia", "North America", "Antarctica", "Central Asia, the Middle East and Europe"]'::jsonb,3,'It carried goods, religions and ideas.','original'),
('113.42.d.4.I',3,'In West Africa, gold was traded for what valuable commodity from the Sahara?','["salt", "silk", "spices", "tea"]'::jsonb,0,'Salt was scarce in the forest zone.','original'),
('113.42.d.4.J',3,'The Mongol Empire promoted trade across Eurasia through what?','["the Silk Embargo", "the Pax Mongolica", "the Council of Trent", "the Hanseatic League"]'::jsonb,1,'The Mongols secured trade routes.','original'),
('113.42.d.4.J',4,'Which Mongol ruler founded the Yuan Dynasty in China?','["Genghis Khan", "Tamerlane", "Kublai Khan", "Attila"]'::jsonb,2,'Kublai Khan was Genghis Khan''s grandson.','original'),
('113.42.d.5.A',3,'The Renaissance began in which region of Europe?','["Spain", "Scandinavia", "Poland", "Italy"]'::jsonb,3,'City-states like Florence led the revival.','original'),
('113.42.d.5.A',3,'Which Renaissance artist painted the Mona Lisa and designed flying machines?','["Leonardo da Vinci", "Michelangelo", "Donatello", "Raphael"]'::jsonb,0,'Leonardo was a painter, scientist and inventor.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_worldhist_v1'
from (values
('113.42.d.5.A',3,'Humanism emphasized what?','["rejecting all learning", "the value of individual potential and classical learning", "isolation", "obedience only"]'::jsonb,1,'Renaissance thinkers revived Greek and Roman texts.','original'),
('113.42.d.5.B',3,'The Reformation led to the creation of which new Christian groups?','["Islam", "the Eastern Orthodox Church", "Protestant churches", "Buddhism"]'::jsonb,2,'Lutherans, Calvinists and Anglicans emerged.','original'),
('113.42.d.5.B',3,'King Henry VIII founded the Church of England largely because he did what?','["admired Luther''s doctrine", "wanted to convert to Islam", "was ordered by Parliament", "wanted an annulment the pope refused"]'::jsonb,3,'He broke from Rome in the 1530s.','original'),
('113.42.d.6.A',3,'The Maya are known for what achievement?','["a sophisticated writing system and calendar", "gunpowder", "steam power", "the printing press"]'::jsonb,0,'They developed glyphs and astronomy.','original'),
('113.42.d.6.A',3,'The Aztec capital Tenochtitlan stood on the site of present-day what?','["Havana", "Mexico City", "Bogotá", "Lima"]'::jsonb,1,'It was built on an island in Lake Texcoco.','original'),
('113.42.d.6.A',3,'The Inca Empire built an extensive system of what?','["seaports in Europe", "railroads", "roads across the Andes", "canals across the Amazon"]'::jsonb,2,'The road network united the empire.','original'),
('113.42.d.6.B',3,'Which Spanish conquistador conquered the Aztec Empire?','["Francisco Pizarro", "Ferdinand Magellan", "Vasco da Gama", "Hernán Cortés"]'::jsonb,3,'Cortés allied with local peoples and used disease and force.','original'),
('113.42.d.6.B',3,'Which conquistador overthrew the Inca Empire?','["Francisco Pizarro", "Juan Ponce de León", "Hernán Cortés", "Christopher Columbus"]'::jsonb,0,'Pizarro captured Atahualpa in 1532.','original'),
('113.42.d.6.B',3,'A major reason for the collapse of the Aztec and Inca empires was what?','["volcanic eruptions", "European diseases such as smallpox", "civil wars alone", "lack of food"]'::jsonb,1,'Epidemics devastated the populations.','original'),
('113.42.d.7.A',3,'Which motives drove European exploration after 1450?','["religious withdrawal", "a ban on trade", "gold, God and glory", "isolation and secrecy"]'::jsonb,2,'Wealth, religion and prestige motivated explorers.','original'),
('113.42.d.7.A',4,'The fall of Constantinople in 1453 encouraged Europeans to seek new routes to Asia because it did what?','["ended trade", "opened the Silk Road", "ended Ottoman power", "disrupted traditional overland trade routes"]'::jsonb,3,'Ottoman control raised costs.','original'),
('113.42.d.7.B',3,'The Columbian Exchange refers to what?','["the transfer of plants, animals, diseases and people between the hemispheres", "a war", "a trade treaty", "a type of bank"]'::jsonb,0,'It transformed both worlds.','original'),
('113.42.d.7.B',3,'Which crop from the Americas became a staple in Europe?','["wheat", "the potato", "olives", "rice"]'::jsonb,1,'It boosted European population.','original'),
('113.42.d.7.C',3,'The Atlantic slave trade had what effect on West Africa?','["increased literacy", "peace", "loss of population and disruption of societies", "growth of cities"]'::jsonb,2,'Millions were forcibly removed.','original'),
('113.42.d.7.C',3,'The ''Middle Passage'' refers to what?','["a trade route in Asia", "a mountain pass in the Alps", "a canal in Panama", "the voyage that carried enslaved Africans across the Atlantic"]'::jsonb,3,'Conditions were brutal.','original'),
('113.42.d.7.D',3,'The Ottoman Empire controlled which key city after 1453?','["Constantinople (Istanbul)", "Vienna", "Moscow", "Rome"]'::jsonb,0,'Mehmed II conquered it.','original'),
('113.42.d.7.E',3,'Ming China''s treasure voyages under Zheng He demonstrated what?','["isolationism", "China''s naval power and reach in the Indian Ocean", "the discovery of America", "military conquest of Europe"]'::jsonb,1,'Fleets visited Southeast Asia, India and East Africa.','original'),
('113.42.d.7.F',3,'Mercantilism held that a nation''s strength depends on what?','["abolishing trade", "free markets only", "exporting more than it imports and accumulating precious metals", "tariff-free borders"]'::jsonb,2,'Colonies provided raw materials.','original'),
('113.42.d.7.F',3,'Joint-stock companies helped finance exploration by doing what?','["creating monarchies", "ending trade", "banning investment", "pooling investors'' money to share risk"]'::jsonb,3,'The Dutch East India Company was one example.','original'),
('113.42.d.8.A',3,'The Industrial Revolution began in which country?','["Great Britain", "Germany", "Russia", "France"]'::jsonb,0,'Textiles, coal and iron drove early industrialization.','original'),
('113.42.d.8.A',3,'A social effect of industrialization was what?','["end of factories", "rapid growth of cities", "return to farming", "decline of cities"]'::jsonb,1,'Workers moved to industrial centers.','original'),
('113.42.d.8.B',4,'Which motive was NOT a major driver of European imperialism?','["access to raw materials", "national prestige", "a desire to preserve local traditions", "new markets"]'::jsonb,2,'Imperialism sought resources, markets and power.','original'),
('113.42.d.8.C',3,'The Berlin Conference of 1884-1885 was held to do what?','["end slavery in the U.S.", "form NATO", "unify Germany", "divide Africa among European powers"]'::jsonb,3,'No African leaders were present.','original'),
('113.42.d.8.C',3,'Sepoys in the Indian Rebellion of 1857 were what?','["Indian soldiers in the British East India Company''s army", "Japanese samurai", "Mongol raiders", "Ottoman officials"]'::jsonb,0,'Their revolt challenged British rule.','original'),
('113.42.d.8.D',3,'Free enterprise fueled the Industrial Revolution by doing what?','["setting all prices by law", "rewarding investment and innovation", "preventing competition", "banning private property"]'::jsonb,1,'Capital and competition drove growth.','original'),
('113.42.d.9.A',4,'Both the American and French Revolutions were influenced by what ideas?','["mercantilism", "feudal loyalty", "Enlightenment ideas of natural rights and popular sovereignty", "divine right of kings"]'::jsonb,2,'Thinkers like Locke and Rousseau inspired both.','original'),
('113.42.d.9.B',3,'Napoleon Bonaparte''s Napoleonic Code did what?','["ended property rights", "restored feudalism", "banned education", "reformed laws and spread legal equality across Europe"]'::jsonb,3,'It influenced legal systems worldwide.','original'),
('113.42.d.9.B',3,'Napoleon''s army was crippled by his invasion of which country in 1812?','["Russia", "Spain", "Egypt", "Italy"]'::jsonb,0,'Winter and scorched earth destroyed his army.','original'),
('113.42.d.9.C',3,'Which leader helped free much of South America from Spanish rule?','["Napoleon", "Simón Bolívar", "Garibaldi", "Peter the Great"]'::jsonb,1,'He led campaigns in Venezuela, Colombia and beyond.','original'),
('113.42.d.9.C',3,'The Haitian Revolution was led by which formerly enslaved leader?','["Miguel Hidalgo", "Simón Bolívar", "Toussaint Louverture", "José de San Martín"]'::jsonb,2,'It created the first independent Black republic in the Americas.','original'),
('113.42.d.9.D',3,'Montesquieu''s idea of separation of powers influenced which document?','["the Code of Hammurabi", "the Magna Carta", "the Domesday Book", "the U.S. Constitution"]'::jsonb,3,'The Framers divided government into branches.','original'),
('113.42.d.10.A',3,'Which four factors are commonly cited as long-term causes of World War I?','["militarism, alliances, imperialism and nationalism", "socialism, capitalism, humanism and monarchy", "feudalism, mercantilism, fascism and communism", "isolationism, pacifism, democracy and trade"]'::jsonb,0,'The acronym MAIN summarizes them.','original'),
('113.42.d.10.B',3,'The idea of ''total war'' in World War I meant what?','["wars were fought only at sea", "the economy and society were mobilized for war", "only soldiers fought", "wars were short"]'::jsonb,1,'Entire nations supported the war effort.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_worldhist_v1'
from (values
('113.42.d.10.C',3,'A key provision of the Treaty of Versailles was that Germany had to do what?','["rearm", "receive new territory", "accept blame and pay reparations", "join the League as a leader"]'::jsonb,2,'The ''war guilt clause'' angered Germans.','original'),
('113.42.d.10.D',3,'The October Revolution of 1917 in Russia brought which group to power?','["the Duma liberals", "the tsar''s army", "the Mensheviks", "the Bolsheviks led by Lenin"]'::jsonb,3,'It created the first communist state.','original'),
('113.42.d.10.D',3,'A cause of the February Revolution in Russia was what?','["food shortages and war weariness", "peace with Germany", "a rich harvest", "a rise in prosperity"]'::jsonb,0,'Workers and soldiers revolted against Tsar Nicholas II.','original'),
('113.42.d.11.A',3,'Which factor contributed to the global depression of the 1930s?','["excess gold", "collapse of world trade and bank failures", "agricultural booms", "overproduction of luxury goods only"]'::jsonb,1,'Protective tariffs and failing banks spread the crisis.','original'),
('113.42.d.11.B',3,'In Germany, economic hardship during the depression helped which party gain support?','["the Social Democrats", "the Monarchists", "the Nazi Party", "the Zionists"]'::jsonb,2,'Desperation fueled extremist movements.','original'),
('113.42.d.12.A',3,'Which characteristic is typical of totalitarian states?','["free elections", "independent courts", "a free press", "total government control of public and private life"]'::jsonb,3,'Propaganda and secret police enforce control.','original'),
('113.42.d.12.B',3,'Which leader established Fascism in Italy?','["Benito Mussolini", "Adolf Hitler", "Joseph Stalin", "Francisco Franco"]'::jsonb,0,'He became Prime Minister in 1922.','original'),
('113.42.d.12.B',3,'Joseph Stalin ruled the Soviet Union through what?','["a free market", "a command economy and brutal repression", "direct democracy", "a constitutional monarchy"]'::jsonb,1,'Collectivization and purges marked his rule.','original'),
('113.42.d.12.C',3,'World War II in Europe began when Germany invaded which country?','["Belgium", "Austria", "Poland", "France"]'::jsonb,2,'Britain and France declared war in September 1939.','original'),
('113.42.d.12.C',4,'The policy of appeasement at the Munich Conference gave Hitler control of what?','["Austria", "Poland", "Denmark", "the Sudetenland in Czechoslovakia"]'::jsonb,3,'The agreement of 1938 failed to prevent war.','original'),
('113.42.d.12.C',3,'The Battle of Stalingrad was a turning point on which front?','["the Eastern Front", "North Africa", "the Western Front", "the Pacific"]'::jsonb,0,'The German army was defeated by the Soviets.','original'),
('113.42.d.13.A',3,'The Cold War was a rivalry primarily between which two superpowers?','["Germany and Italy", "the United States and the Soviet Union", "China and Japan", "Britain and France"]'::jsonb,1,'They competed ideologically and strategically.','original'),
('113.42.d.13.B',3,'Mao Zedong established the People''s Republic of China in what year?','["1989", "1919", "1949", "1936"]'::jsonb,2,'Communists won the civil war.','original'),
('113.42.d.13.C',3,'The Berlin Wall, built in 1961, was meant to do what?','["separate France from Germany", "unite Germany", "protect Poland", "stop East Germans from fleeing to the West"]'::jsonb,3,'It divided Berlin until 1989.','original'),
('113.42.d.13.D',3,'Mikhail Gorbachev''s policies of glasnost and perestroika meant what?','["openness and economic restructuring", "monarchy and religion", "isolation and censorship", "war and expansion"]'::jsonb,0,'They helped end the Cold War.','original'),
('113.42.d.13.E',3,'Mohandas Gandhi led India''s independence movement using what method?','["armed conquest", "nonviolent civil disobedience", "terrorism", "guerrilla warfare"]'::jsonb,1,'The Salt March was a famous example.','original'),
('113.42.d.13.E',3,'India gained independence from Britain in what year?','["1965", "1919", "1947", "1857"]'::jsonb,2,'Partition created India and Pakistan.','original'),
('113.42.d.13.E',3,'Which African leader led Ghana to independence in 1957?','["Jomo Kenyatta", "Nelson Mandela", "Patrice Lumumba", "Kwame Nkrumah"]'::jsonb,3,'Ghana was the first sub-Saharan colony to gain independence.','original'),
('113.42.d.13.F',3,'In 1948 the state of Israel was founded following which event?','["the end of the British mandate and a UN partition plan", "the Six-Day War", "the Cuban Missile Crisis", "the Suez Crisis"]'::jsonb,0,'Neighboring Arab states rejected the partition.','original'),
('113.42.d.14.A',4,'The Soviet invasion of Afghanistan in 1979 contributed to what?','["a stable democracy", "the rise of militant groups that later included al-Qaeda", "U.S. troop withdrawal", "an end to conflict"]'::jsonb,1,'Foreign fighters and weapons flowed in.','original'),
('113.42.d.14.B',3,'The September 11, 2001 attacks were carried out by which terrorist organization?','["Hezbollah", "the Taliban", "al-Qaeda", "Hamas"]'::jsonb,2,'Osama bin Laden''s group planned the attacks.','original'),
('113.42.d.14.C',3,'The U.S. response to September 11 included the war in what country?','["Korea", "Vietnam", "Cuba", "Afghanistan"]'::jsonb,3,'The Taliban government sheltered al-Qaeda.','original'),
('113.42.d.15.A',3,'The Fertile Crescent lies in which region?','["the Middle East", "Southern Africa", "Scandinavia", "South America"]'::jsonb,0,'Early agriculture developed there.','original'),
('113.42.d.15.B',3,'Which physical feature most influenced the isolation of early China?','["dense forests only", "mountains, deserts and seas surrounding it", "frozen lakes only", "a shared border with Europe"]'::jsonb,1,'Geography shaped its cultural development.','original'),
('113.42.d.15.B',3,'Why did ancient Egypt grow along the Nile?','["volcanic soil", "glaciers", "annual floods deposited fertile silt", "constant rainfall"]'::jsonb,2,'Geography shaped the economy.','original'),
('113.42.d.15.C',3,'A map showing trade routes between Asia and Europe helps explain what?','["the length of rivers only", "the size of armies", "the number of presidents", "how goods and ideas spread"]'::jsonb,3,'Maps reveal historical connections.','original'),
('113.42.d.16.A',3,'Which change did the Neolithic Revolution bring to human life?','["permanent settlements and food surpluses", "smaller populations", "constant migration", "the end of tools"]'::jsonb,0,'Farming allowed specialization.','original'),
('113.42.d.16.C',3,'Globalization has resulted in what?','["fewer ports", "increased trade and interconnection among nations", "decreased trade", "isolated economies"]'::jsonb,1,'Goods, capital and ideas cross borders faster.','original'),
('113.42.d.17.A',3,'Adam Smith argued that free markets work best when what is allowed?','["monopolies control trade", "trade is banned", "individuals pursue self-interest in competition", "government sets all prices"]'::jsonb,2,'He called it the invisible hand.','original'),
('113.42.d.17.B',3,'Karl Marx predicted that capitalism would be replaced by what?','["a feudal order", "fascism", "a monarchy", "a classless communist society"]'::jsonb,3,'He wrote The Communist Manifesto with Friedrich Engels.','original'),
('113.42.d.17.C',3,'Socialism generally advocates what?','["public or collective ownership of key industries", "unregulated markets", "no government", "absolute monarchy"]'::jsonb,0,'It seeks to reduce inequality.','original'),
('113.42.d.17.D',3,'Fascism is characterized by what?','["free-market anarchy", "extreme nationalism and dictatorial power", "direct democracy", "classless society"]'::jsonb,1,'Fascist states suppress opposition.','original'),
('113.42.d.17.E',4,'Why did communist command economies often collapse in competition with market economies?','["too much competition", "lack of government", "lack of incentives and inefficient central planning", "too much trade"]'::jsonb,2,'Central planners struggled to meet demand.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_worldhist_v1'
from (values
('113.42.d.18.A',3,'In an absolute monarchy, the ruler does what?','["serves a fixed term", "shares power with an elected body", "is chosen by lottery", "holds nearly unlimited power"]'::jsonb,3,'Louis XIV is an example.','original'),
('113.42.d.18.B',3,'A theocracy is a government in which what?','["religious leaders rule in the name of a deity", "citizens vote on all laws", "generals rule", "kings share power with Parliament"]'::jsonb,0,'Iran today has theocratic elements.','original'),
('113.42.d.19.A',3,'The idea of democratic-republican government began in which ancient societies?','["China and India", "Greece and Rome", "Egypt and Persia", "the Aztecs and Incas"]'::jsonb,1,'Athens had democracy; Rome had a republic.','original'),
('113.42.d.19.B',3,'The Magna Carta (1215) established the principle that what?','["Parliament was abolished", "nobles had no rights", "even the king must obey the law", "kings were divinely appointed"]'::jsonb,2,'It limited royal power.','original'),
('113.42.d.19.B',3,'The English Bill of Rights (1689) limited the power of whom?','["the courts only", "Parliament", "the church only", "the monarchy"]'::jsonb,3,'It affirmed parliamentary supremacy.','original'),
('113.42.d.19.C',3,'Which philosopher argued that people have natural rights to life, liberty and property?','["John Locke", "Thomas Hobbes", "Karl Marx", "Niccolò Machiavelli"]'::jsonb,0,'His ideas influenced the Declaration of Independence.','original'),
('113.42.d.19.C',4,'Thomas Hobbes argued that people need a strong government because what?','["government is unnecessary", "without it, life would be ''nasty, brutish and short''", "rulers should be elected weekly", "people are naturally good"]'::jsonb,1,'Hobbes feared the state of nature.','original'),
('113.42.d.19.D',3,'The United Nations was created after World War II to do what?','["rebuild Germany", "end colonialism overnight", "maintain international peace and cooperation", "control trade"]'::jsonb,2,'It replaced the League of Nations.','original'),
('113.42.d.19.D',3,'A reason the League of Nations failed was that what?','["it conquered nations", "it was too powerful", "it ended the war early", "the United States never joined and it lacked enforcement power"]'::jsonb,3,'It could not stop aggression in the 1930s.','original'),
('113.42.d.20.A',3,'Which is an example of people supporting or changing their government?','["voting in elections", "avoiding taxes", "hiding records", "ignoring laws"]'::jsonb,0,'Participation includes voting and protest.','original'),
('113.42.d.20.C',3,'Nelson Mandela is remembered for leading resistance to what?','["Soviet rule", "apartheid in South Africa", "Nazi occupation", "British rule in India"]'::jsonb,1,'He became South Africa''s first Black president.','original'),
('113.42.d.21.A',3,'The rule of law means that what?','["laws change daily", "rulers are above the law", "everyone, including leaders, must obey the law", "laws apply only to the poor"]'::jsonb,2,'It is a foundation of just government.','original'),
('113.42.d.21.B',3,'The idea of trial by a jury of peers is rooted in which document?','["the Code of Hammurabi", "the Domesday Book", "the Ninety-five Theses", "the Magna Carta"]'::jsonb,3,'It promised judgment by one''s equals.','original'),
('113.42.d.21.C',3,'The Khmer Rouge regime in Cambodia is associated with what?','["mass killings in the 1970s", "democratic reform", "a trade boom", "a space program"]'::jsonb,0,'Under Pol Pot, about two million died.','original'),
('113.42.d.21.D',3,'The Armenian Genocide took place during which conflict?','["World War II", "World War I", "the Cold War", "the Crimean War"]'::jsonb,1,'Ottoman authorities killed about 1.5 million Armenians.','original'),
('113.42.d.21.E',3,'Aung San Suu Kyi is associated with resistance to military rule in what country?','["Thailand", "Vietnam", "Myanmar (Burma)", "Laos"]'::jsonb,2,'She won the Nobel Peace Prize in 1991.','original'),
('113.42.d.22.A',3,'Which three religions are monotheistic and trace roots to Abraham?','["Confucianism, Daoism and Jainism", "Zoroastrianism, Sikhism and Shinto", "Hinduism, Buddhism and Shinto", "Judaism, Christianity and Islam"]'::jsonb,3,'They worship one God.','original'),
('113.42.d.22.B',3,'Buddhism began in India with the teachings of whom?','["Siddhartha Gautama", "Confucius", "Zoroaster", "Muhammad"]'::jsonb,0,'He became known as the Buddha.','original'),
('113.42.d.22.B',3,'Which religion teaches the cycle of reincarnation and the concept of karma?','["Confucianism", "Hinduism", "Judaism", "Islam"]'::jsonb,1,'Hindu beliefs include dharma and moksha.','original'),
('113.42.d.22.C',3,'The Crusades are an example of what?','["science ending war", "economics ending religion", "religion influencing political and military events", "trade replacing faith"]'::jsonb,2,'Popes called Christians to retake the Holy Land.','original'),
('113.42.d.23.A',3,'During the Industrial Revolution many women and children did what?','["led governments", "abandoned work", "owned most mills", "worked in factories"]'::jsonb,3,'Low-wage labor was common.','original'),
('113.42.d.23.B',3,'Queen Elizabeth I is associated with which era?','["the English Renaissance and the defeat of the Spanish Armada", "the Cold War", "the Industrial Revolution", "the Crusades"]'::jsonb,0,'She ruled from 1558 to 1603.','original'),
('113.42.d.23.B',3,'Catherine the Great expanded the territory of what country?','["Austria", "Russia", "Spain", "France"]'::jsonb,1,'She ruled from 1762 to 1796.','original'),
('113.42.d.24.A',3,'Confucianism emphasizes what?','["monotheism", "conquest", "respect for family and social harmony", "isolation"]'::jsonb,2,'It guided Chinese government and society.','original'),
('113.42.d.24.B',3,'Which Western civilization contributed the concept of democracy?','["ancient Persia", "ancient China", "ancient Egypt", "ancient Greece"]'::jsonb,3,'Athens developed direct democracy.','original'),
('113.42.d.24.C',4,'Renaissance humanism led to a conflict with traditional church authority by doing what?','["emphasizing individual reasoning alongside faith", "rejecting all religion", "ending education", "banning books"]'::jsonb,0,'Humanists revived classical learning.','original'),
('113.42.d.25.A',3,'The Gothic cathedral reflected the medieval culture by doing what?','["replacing churches", "expressing religious devotion through towering architecture", "celebrating science", "promoting democracy"]'::jsonb,1,'Its height pointed toward heaven.','original'),
('113.42.d.25.B',3,'Which composer''s music has transcended the culture in which it was written?','["Karl Marx", "Isaac Newton", "Ludwig van Beethoven", "Napoleon Bonaparte"]'::jsonb,2,'His symphonies are performed worldwide.','original'),
('113.42.d.26.A',3,'Which number system, developed in India, spread through the Islamic world to Europe?','["Roman numerals", "Babylonian numerals", "Mayan numerals", "Hindu-Arabic numerals"]'::jsonb,3,'It includes the concept of zero.','original'),
('113.42.d.26.C',3,'Johannes Gutenberg''s printing press helped spread what?','["ideas of the Renaissance and Reformation", "feudalism", "divine right", "illiteracy"]'::jsonb,0,'It lowered the cost of books.','original'),
('113.42.d.26.D',3,'The Scientific Revolution emphasized what?','["tradition only", "observation, experiment and reason", "divine revelation only", "magic"]'::jsonb,1,'It transformed views of nature.','original'),
('113.42.d.26.E',3,'Which scientist proposed that Earth orbits the sun?','["Ptolemy", "Galen", "Nicolaus Copernicus", "Aristotle"]'::jsonb,2,'He challenged the geocentric model.','original'),
('113.42.d.26.E',3,'Isaac Newton is best known for formulating what?','["the periodic table", "germ theory", "the theory of evolution", "the laws of motion and universal gravitation"]'::jsonb,3,'His Principia appeared in 1687.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_worldhist_v1'
from (values
('113.42.d.27.A',3,'James Watt improved which invention, powering factories and trains?','["the steam engine", "the printing press", "the cotton gin", "the telegraph"]'::jsonb,0,'Steam power drove the Industrial Revolution.','original'),
('113.42.d.27.B',3,'The Bessemer process made which material cheaper and stronger?','["paper", "steel", "cement", "glass"]'::jsonb,1,'It supported railroads and buildings.','original'),
('113.42.d.27.C',3,'A major new weapon in World War I was what?','["the musket", "the crossbow", "the machine gun", "the catapult"]'::jsonb,2,'It made frontal assaults deadly.','original'),
('113.42.d.27.C',3,'World War II ended in the Pacific after the use of what?','["chemical gas", "trench warfare", "longbows", "atomic bombs"]'::jsonb,3,'Hiroshima and Nagasaki were bombed in August 1945.','original'),
('113.42.d.27.D',3,'The internet has contributed to globalization by doing what?','["speeding communication and trade across borders", "isolating nations", "limiting information", "ending trade"]'::jsonb,0,'Digital networks connect the world.','original'),
('113.42.d.27.E',3,'Marie Curie is known for her research on what?','["evolution", "radioactivity", "electromagnetism", "gravity"]'::jsonb,1,'She won Nobel Prizes in physics and chemistry.','original'),
('113.42.d.28.A',3,'Which scientist studies artifacts and ancient remains to learn about the past?','["a meteorologist", "an economist", "an archaeologist", "a botanist"]'::jsonb,2,'Archaeologists excavate sites.','original'),
('113.42.d.28.B',3,'When historians consider a source''s frame of reference, they ask what?','["where it was stored", "how long it is", "what color it is", "who created it and what viewpoint shaped it"]'::jsonb,3,'Perspective shapes accounts.','original'),
('113.42.d.28.C',3,'A letter from a soldier in World War I is what kind of source?','["a primary source", "a documentary", "a textbook", "a secondary source"]'::jsonb,0,'It was written at the time.','original'),
('113.42.d.28.D',3,'Which clue helps evaluate a source''s credibility?','["its font", "the author''s expertise and use of evidence", "its price", "its length"]'::jsonb,1,'Credible sources are reliable and evidence-based.','original'),
('113.42.d.28.E',3,'Sorting events into political, economic and social categories is an example of what?','["averaging data", "mapping rivers", "categorizing information", "ignoring causes"]'::jsonb,2,'Categorizing organizes evidence.','original'),
('113.42.d.28.F',3,'A good historical argument links a claim to what?','["dates only", "pictures only", "opinion only", "evidence and reasoning"]'::jsonb,3,'Evidence supports claims.','original'),
('113.42.d.29.A',3,'A thematic map of colonial empires in 1914 shows what?','["which powers controlled which territories", "the length of rivers", "the sizes of armies", "the elevation of mountains"]'::jsonb,0,'Thematic maps show specific data.','original'),
('113.42.d.29.B',3,'Comparing two maps of Europe from 1914 and 1919 helps show what?','["changes in climate", "changes in political boundaries after World War I", "changes in rainfall", "changes in tides"]'::jsonb,1,'Boundary shifts followed the treaties.','original'),
('113.42.d.30.A',3,'Which term means a government controlled by a single leader with unlimited power?','["democracy", "republic", "dictatorship", "federation"]'::jsonb,2,'Using precise terms matters.','original'),
('113.42.d.30.B',3,'To avoid plagiarism, a student should do what?','["omit references", "copy and paste without credit", "change a few words only", "cite sources and paraphrase in their own words"]'::jsonb,3,'Credit others'' ideas.','original'),
('113.42.d.30.D',3,'Civil discourse about a controversial topic means doing what?','["listening respectfully and supporting claims with evidence", "insulting others", "ignoring facts", "interrupting"]'::jsonb,0,'Respect and evidence guide discussion.','original'),
('113.42.d.31.A',3,'A caucus is a meeting in which what happens?','["taxes are collected", "party members gather to select candidates or delegates", "laws are written", "a trial is held"]'::jsonb,1,'Caucuses are a form of party selection.','original'),
('113.42.d.31.B',3,'After listing possible solutions to a problem, what is the next step in decision making?','["starting a new problem", "ignoring the options", "evaluating the choices and selecting one", "repeating research"]'::jsonb,2,'Weigh options before choosing.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;

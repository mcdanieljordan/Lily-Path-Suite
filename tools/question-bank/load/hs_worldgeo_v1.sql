insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_worldgeo_v1'
from (values
('113.43.d.1.A',3,'Why did the Nile River valley become the center of ancient Egyptian civilization?','["its yearly floods left fertile soil in a desert region", "it was covered in thick forest", "it was free of flooding", "it had the highest mountains in Africa"]'::jsonb,0,'Physical features shape where people settle.','original'),
('113.43.d.1.A',3,'Which physical feature helped protect medieval Japan from invasion?','["a long river", "surrounding seas", "dense jungle", "wide deserts"]'::jsonb,1,'Island location limited outside attacks.','original'),
('113.43.d.1.B',3,'The Columbian Exchange is an example of what geographic process?','["erosion of coastlines", "volcanic activity", "spatial diffusion of plants, animals and diseases between hemispheres", "a shift in wind patterns"]'::jsonb,2,'Diffusion is the spread of things across space.','original'),
('113.43.d.1.B',4,'The spread of a new idea from a single place outward to surrounding areas is called what?','["migration", "convergence", "erosion", "diffusion"]'::jsonb,3,'Geographers trace how ideas and goods move through space.','original'),
('113.43.d.2.A',3,'Comparing a map of the Silk Road in 1200 to one of today shows changes in what?','["human features such as trade routes and cities", "the length of a day", "the size of the oceans", "the position of the equator"]'::jsonb,0,'Human characteristics change over time.','original'),
('113.43.d.2.B',3,'Which change would most likely cause a region''s cities to grow quickly?','["a loss of all jobs", "new industry that draws workers from rural areas", "a decline in all trade", "a ban on travel"]'::jsonb,1,'Technology and jobs shift population.','original'),
('113.43.d.3.A',3,'The Northern Hemisphere has its longest day around what date?','["March 1", "December 21", "June 21 (summer solstice)", "September 30"]'::jsonb,2,'The North Pole tilts toward the sun in June.','original'),
('113.43.d.3.B',3,'Weathering and erosion are physical processes that do what?','["increase the sun''s heat", "create new oceans", "stop rivers from flowing", "break down and move rock and soil, changing landforms"]'::jsonb,3,'Water, wind and ice reshape Earth''s surface.','original'),
('113.43.d.3.B',3,'A glacier shapes land by doing what?','["carving valleys as it slowly moves", "raising the water table to flood plains", "making deserts", "building volcanoes"]'::jsonb,0,'Glaciers erode and deposit rock.','original'),
('113.43.d.3.C',3,'Which hazard is common along the ''Ring of Fire'' around the Pacific Ocean?','["sandstorms", "earthquakes and volcanoes", "droughts", "blizzards"]'::jsonb,1,'Plate boundaries are active there.','original'),
('113.43.d.3.C',3,'El Niño is a warming of surface water in which ocean?','["the Arctic", "the Indian", "the Pacific", "the Southern"]'::jsonb,2,'It changes weather around the world.','original'),
('113.43.d.4.A',3,'Cities at higher elevation are usually what compared with nearby low-lying areas?','["closer to sea level", "warmer", "more humid", "cooler"]'::jsonb,3,'Temperature drops as altitude increases.','original'),
('113.43.d.4.A',3,'The Gulf Stream keeps western Europe warmer than other places at the same latitude. What is it?','["a warm ocean current", "a desert", "a mountain chain", "a cold wind"]'::jsonb,0,'Ocean currents carry heat.','original'),
('113.43.d.4.A',4,'Why is the interior of a large continent often drier than its coasts?','["it has more oceans", "it is far from moisture-carrying ocean air", "it has no sunlight", "it is closer to the equator"]'::jsonb,1,'Distance from water affects rainfall.','original'),
('113.43.d.4.B',3,'Which landform is a large area of flat or gently rolling land?','["a plateau", "a volcano", "a plain", "a canyon"]'::jsonb,2,'Plains are good for farming.','original'),
('113.43.d.4.B',3,'A chain of islands is called what?','["a delta", "an isthmus", "a peninsula", "an archipelago"]'::jsonb,3,'Japan and the Philippines are archipelagos.','original'),
('113.43.d.4.B',3,'A river delta forms where what happens?','["a river deposits sediment as it enters a larger body of water", "wind blows sand", "a glacier melts", "two mountains meet"]'::jsonb,0,'Deltas are rich farmland.','original'),
('113.43.d.4.C',3,'A biome with very little rainfall and sparse vegetation is a what?','["tropical rainforest", "desert", "taiga", "temperate forest"]'::jsonb,1,'Climate determines biome.','original'),
('113.43.d.4.C',3,'Which biome is found near the equator and receives heavy rain year-round?','["tundra", "grassland", "tropical rainforest", "desert"]'::jsonb,2,'Warm, wet conditions support dense vegetation.','original'),
('113.43.d.5.A',3,'The ''character'' of a place is shaped by what?','["the number of roads", "its distance from the equator only", "its name only", "its physical, cultural, economic and political features"]'::jsonb,3,'Place combines many factors.','original'),
('113.43.d.5.B',3,'Gross domestic product (GDP) measures what?','["the total value of goods and services a country produces", "the length of a country''s coastline", "the number of people in a country", "the size of a country"]'::jsonb,0,'GDP is an economic indicator.','original'),
('113.43.d.5.B',3,'A high literacy rate and long life expectancy usually indicate what?','["a low standard of living", "a higher level of development", "a smaller economy", "a lack of schools"]'::jsonb,1,'Development indicators reflect well-being.','original'),
('113.43.d.6.A',3,'Many large cities were founded near rivers because rivers provided what?','["more mountains", "protection from rain", "water, transportation and fertile land", "colder weather"]'::jsonb,2,'Physical features influence settlement.','original'),
('113.43.d.6.A',3,'A site that is a natural harbor is likely to develop into what?','["an isolated village", "a mining town only", "a desert oasis", "a major port city"]'::jsonb,3,'Ports connect trade.','original'),
('113.43.d.6.B',3,'Urbanization means what?','["the growth of cities as people move from rural areas", "a shrinking population", "the decline of towns", "moving to farms"]'::jsonb,0,'Urban areas expand through migration.','original'),
('113.43.d.6.B',3,'Suburbanization is the movement of people to where?','["the center of a city", "areas on the edges of cities", "deserts", "mountain tops"]'::jsonb,1,'Cars and highways made it possible.','original'),
('113.43.d.7.A',3,'A population pyramid with a wide base and narrow top shows what?','["no births", "a stable older population", "a young population with high birth rates", "an aging population"]'::jsonb,2,'The shape reveals age structure.','original'),
('113.43.d.7.A',3,'A population pyramid that looks like a column or is narrow at the bottom shows what?','["a very young country", "a country with no deaths", "rapid growth", "slow growth or an aging population"]'::jsonb,3,'Low birth rates reduce the base.','original'),
('113.43.d.7.B',3,'A ''push'' factor in migration is something that does what?','["drives people away from their home, such as war or poverty", "keeps them at home", "attracts people to a new place", "prevents travel"]'::jsonb,0,'Push and pull forces influence migration.','original'),
('113.43.d.7.B',3,'A ''pull'' factor in migration is something that does what?','["stops migration", "attracts people to a new place, such as jobs or safety", "causes floods", "forces people to leave"]'::jsonb,1,'Opportunity pulls migrants.','original'),
('113.43.d.7.C',3,'World population has been growing fastest in recent decades in which kind of countries?','["the smallest countries only", "Arctic regions", "developing countries", "all high-income countries"]'::jsonb,2,'Growth rates are higher where birth rates remain high.','original'),
('113.43.d.7.D',3,'How does globalization affect the spread of pandemics?','["it slows all travel", "it ends disease", "it makes disease stop at borders", "faster travel and trade can spread disease more quickly"]'::jsonb,3,'Connectivity has risks and benefits.','original'),
('113.43.d.7.D',3,'A possible negative effect of globalization on cultures is what?','["loss of traditional languages and customs", "less communication", "more traditional crafts", "fewer products"]'::jsonb,0,'Global culture can overshadow local culture.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_worldgeo_v1'
from (values
('113.43.d.8.A',3,'Terracing hillsides for farming is an example of how people do what?','["ignore climate", "modify the environment to meet their needs", "destroy farmland", "avoid the environment"]'::jsonb,1,'Humans adapt and modify landscapes.','original'),
('113.43.d.8.A',3,'Building homes on stilts in flood-prone areas is an example of what?','["depending on deserts", "modifying the climate", "adapting to the environment", "ignoring risks"]'::jsonb,2,'People adapt to hazards.','original'),
('113.43.d.8.B',3,'A major consequence of a severe drought is what?','["colder temperatures", "increased harvests", "more rainfall", "food shortages and migration"]'::jsonb,3,'Drought harms crops and water supplies.','original'),
('113.43.d.8.C',3,'Deforestation can lead to what environmental problem?','["soil erosion and loss of habitat", "more fertile soil", "cleaner water always", "larger forests"]'::jsonb,0,'Removing trees exposes soil.','original'),
('113.43.d.8.C',3,'The draining of the Aral Sea resulted from what?','["rising ocean levels", "diversion of rivers for irrigation", "a volcanic eruption", "glacier growth"]'::jsonb,1,'Water diversion shrank the lake.','original'),
('113.43.d.9.A',3,'A shared language, religion or history can help define a what?','["climate zone", "time zone", "cultural region", "tectonic plate"]'::jsonb,2,'Regions are defined by shared traits.','original'),
('113.43.d.9.B',3,'A formal region is defined by what?','["people''s feelings about a place", "a flow of goods and people around a hub", "a changing tide", "a common characteristic such as an official boundary or a shared language"]'::jsonb,3,'Examples include countries and states.','original'),
('113.43.d.9.B',3,'A functional region is organized around what?','["a central point such as a city and its connected area", "a shared climate only", "a single mountain", "people''s opinions only"]'::jsonb,0,'A newspaper''s delivery area is an example.','original'),
('113.43.d.9.B',3,'A perceptual region reflects what?','["scientific measurements", "people''s feelings or ideas about an area, such as ''the Midwest''", "exact borders", "a transportation hub"]'::jsonb,1,'Perceptual regions are based on opinions.','original'),
('113.43.d.10.A',3,'In a market economy, prices are set mostly by what?','["tradition only", "a ruler''s decree", "supply and demand", "the government"]'::jsonb,2,'Buyers and sellers decide.','original'),
('113.43.d.10.A',3,'In a traditional economy, decisions are based mainly on what?','["stock markets", "competition", "government planning", "custom and habit passed down"]'::jsonb,3,'Roles follow past practice.','original'),
('113.43.d.10.A',3,'In a command economy, who decides what is produced?','["the government", "individual consumers", "competing firms", "local traditions"]'::jsonb,0,'Central planning guides production.','original'),
('113.43.d.10.B',3,'Which economic system allows private ownership and competition with limited government involvement?','["communism", "free enterprise (capitalism)", "a traditional economy", "a command economy"]'::jsonb,1,'Capitalism relies on markets.','original'),
('113.43.d.10.B',3,'Which system has the government own most resources and factories?','["free enterprise", "market capitalism", "communism", "a mixed economy"]'::jsonb,2,'Communist states plan the economy.','original'),
('113.43.d.10.C',3,'A subsistence farmer mainly grows food for what purpose?','["to export to other nations", "to sell to factories", "to supply supermarkets", "to feed their own family"]'::jsonb,3,'Subsistence farming is not for large-scale sale.','original'),
('113.43.d.10.D',3,'Global trade patterns have changed over time because of what?','["advances in transportation and communication", "the end of ports", "lower demand for goods", "a ban on shipping"]'::jsonb,0,'Technology lowers costs of trade.','original'),
('113.43.d.11.A',3,'Farming, fishing and mining are examples of which type of economic activity?','["quaternary", "primary", "secondary", "tertiary"]'::jsonb,1,'Primary activities extract raw materials.','original'),
('113.43.d.11.A',3,'Turning raw cotton into clothing is what kind of economic activity?','["primary", "tertiary", "secondary", "quaternary"]'::jsonb,2,'Manufacturing is secondary.','original'),
('113.43.d.11.A',3,'Teaching, banking and retail are examples of what?','["secondary activities", "subsistence farming", "primary activities", "tertiary (service) activities"]'::jsonb,3,'Services are tertiary.','original'),
('113.43.d.11.B',3,'A factory is often placed near a port or railroad because of what?','["access to transportation for raw materials and finished goods", "lack of workers", "fewer customers", "colder climate"]'::jsonb,0,'Location reduces cost.','original'),
('113.43.d.11.C',3,'A new highway could change a region''s economy by doing what?','["ending trade", "making it easier to move goods and workers", "raising mountains", "isolating towns"]'::jsonb,1,'Infrastructure supports growth.','original'),
('113.43.d.12.A',3,'Oil is a non-renewable resource because it does what?','["regrows each year", "falls as rain", "takes millions of years to form and cannot be replaced quickly", "is unlimited"]'::jsonb,2,'Fossil fuels are finite.','original'),
('113.43.d.12.A',3,'Which is a renewable energy source?','["coal", "oil", "natural gas", "wind"]'::jsonb,3,'Wind and sun are naturally replenished.','original'),
('113.43.d.12.B',4,'A country with large oil reserves may have what advantage and risk?','["income from exports but dependence on one resource", "less trade", "no risk", "no advantage"]'::jsonb,0,'Resource economies can be unstable.','original'),
('113.43.d.12.B',3,'Conservation policies aim to do what?','["ban trade", "protect resources for future use", "use up resources faster", "end all development"]'::jsonb,1,'Sustainable policy balances use and protection.','original'),
('113.43.d.13.A',3,'A boundary that follows a river or mountain range is what kind?','["a time boundary", "a geometric boundary", "a natural boundary", "a cultural boundary"]'::jsonb,2,'Physical features can mark borders.','original'),
('113.43.d.13.A',3,'A straight-line border such as the 49th parallel is what kind?','["a natural boundary", "a religious boundary", "a coastline", "a geometric boundary"]'::jsonb,3,'It follows lines of latitude.','original'),
('113.43.d.13.B',3,'Comparing voting maps with political boundaries helps show what?','["how voting patterns relate to regions", "the age of rocks", "average rainfall", "tectonic movement"]'::jsonb,0,'Maps reveal political geography.','original'),
('113.43.d.14.A',3,'The breakup of Yugoslavia in the 1990s is an example of what?','["unification of countries", "ethnic and political divisions forming new states", "a trade agreement", "a natural disaster"]'::jsonb,1,'Political conflict redrew borders.','original'),
('113.43.d.14.B',3,'In a democracy, who ultimately holds political power?','["the military", "religious leaders only", "the people", "a single ruler"]'::jsonb,2,'Citizens elect leaders.','original'),
('113.43.d.14.B',3,'In a monarchy, power is passed down through what?','["the courts", "elections", "military coups", "a royal family"]'::jsonb,3,'Rulers inherit the throne.','original'),
('113.43.d.14.B',3,'A dictatorship is a government in which what?','["one person or a small group holds absolute power", "religious leaders vote", "citizens vote on all laws", "kings share power with a legislature"]'::jsonb,0,'Dictators limit freedoms.','original'),
('113.43.d.14.C',4,'Why are mountain passes and rivers often contested?','["they have no value", "they control movement of people and resources", "they are always empty", "they are never used for trade"]'::jsonb,1,'Control of key places brings power.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_worldgeo_v1'
from (values
('113.43.d.15.A',3,'Why might two countries have different views about a shared river?','["rivers are not shared", "all countries agree", "each depends on the water for its own needs", "rivers have no value"]'::jsonb,2,'Competing interests cause conflict.','original'),
('113.43.d.15.B',3,'How can public opinion shape policy about a nearby natural area?','["only judges decide", "only the military decides", "it cannot", "through voting, petitions and public meetings"]'::jsonb,3,'Citizens influence decisions.','original'),
('113.43.d.16.A',3,'Terraced rice fields are a distinctive cultural landscape of what region?','["Southeast Asia", "northern Europe", "the Sahara", "Antarctica"]'::jsonb,0,'Farming practices shape the land.','original'),
('113.43.d.16.B',3,'Which is an element of culture?','["tides", "language", "latitude", "weather"]'::jsonb,1,'Culture includes language, religion, beliefs and institutions.','original'),
('113.43.d.16.B',3,'A tradition passed down through generations, such as a festival, is part of what?','["its climate", "its time zone", "a culture''s heritage", "its biome"]'::jsonb,2,'Customs preserve cultural identity.','original'),
('113.43.d.16.C',3,'Which is more common in rural areas than in cities?','["large airports", "subway systems", "skyscrapers", "farming as the main occupation"]'::jsonb,3,'Land use differs between urban and rural.','original'),
('113.43.d.17.A',3,'Arabic is the dominant language of which region?','["North Africa and the Middle East", "South America", "Southeast Asia", "Scandinavia"]'::jsonb,0,'Language patterns reflect history.','original'),
('113.43.d.17.B',3,'Which religion has the largest number of followers in India?','["Judaism", "Hinduism", "Christianity", "Buddhism"]'::jsonb,1,'Hinduism began in the Indian subcontinent.','original'),
('113.43.d.17.B',3,'Mecca, the holiest city of Islam, is in what country?','["Turkey", "Iran", "Saudi Arabia", "Egypt"]'::jsonb,2,'Muslims pilgrimage there.','original'),
('113.43.d.17.B',3,'Buddhism began in which part of the world?','["Australia", "Western Europe", "North America", "South Asia (India and Nepal)"]'::jsonb,3,'Siddhartha Gautama taught there.','original'),
('113.43.d.17.C',3,'In many societies, women''s access to education and jobs depends on what?','["cultural traditions and laws", "latitude", "time zones", "climate only"]'::jsonb,0,'Opportunity differs among cultures.','original'),
('113.43.d.17.D',3,'A multicultural society is one in which what exists?','["only one culture", "many cultural groups live together", "no traditions", "no languages"]'::jsonb,1,'The United States is an example.','original'),
('113.43.d.18.A',3,'Which of these can cause cultural change?','["volcanoes only", "the position of the sun only", "migration, trade or war", "tides only"]'::jsonb,2,'Contact spreads ideas.','original'),
('113.43.d.18.B',3,'The Rwandan genocide of 1994 was a conflict between which groups?','["Greeks and Turks", "Sunni and Shia", "Serbs and Croats", "Hutu and Tutsi"]'::jsonb,3,'It killed around 800,000 people.','original'),
('113.43.d.18.C',3,'Some groups, such as certain Indigenous peoples, maintain traditional ways by doing what?','["preserving language and subsistence practices", "banning outsiders from all contact", "abandoning all customs", "moving to cities only"]'::jsonb,0,'Traditions can survive modernization.','original'),
('113.43.d.18.D',3,'Cultural convergence means what?','["cultures disappearing", "cultures becoming more alike", "cultures becoming more different", "cultures separating"]'::jsonb,1,'Globalization promotes convergence.','original'),
('113.43.d.18.D',3,'Cultural divergence means what?','["languages spreading", "cities growing", "cultures becoming more different over time", "cultures merging"]'::jsonb,2,'Isolation or resistance can cause divergence.','original'),
('113.43.d.19.A',3,'The Panama Canal changed transportation by doing what?','["ending world trade", "creating a new ocean", "blocking ship travel", "shortening ship routes between the Atlantic and Pacific"]'::jsonb,3,'It cut thousands of miles from voyages.','original'),
('113.43.d.19.A',3,'The invention of the jet engine most changed what?','["long-distance travel", "ocean currents", "farming methods", "the length of days"]'::jsonb,0,'Air travel connects the world.','original'),
('113.43.d.19.B',3,'Air conditioning has allowed more people to live where?','["only in cities", "in hot regions such as the U.S. Sun Belt", "only on islands", "only in cold regions"]'::jsonb,1,'Technology changes settlement.','original'),
('113.43.d.19.B',3,'Desalination makes it possible to do what?','["raise sea level", "turn rain into salt", "turn seawater into drinking water", "freeze lakes"]'::jsonb,2,'It helps dry coastal areas.','original'),
('113.43.d.19.C',3,'The Green Revolution increased food production through what?','["banning machines", "less water", "fewer farms", "high-yield crops, fertilizer and irrigation"]'::jsonb,3,'It reduced hunger in many regions.','original'),
('113.43.d.20.A',3,'GPS (Global Positioning System) allows users to do what?','["determine exact locations on Earth using satellites", "change climates", "predict earthquakes", "stop storms"]'::jsonb,0,'Satellites send location data.','original'),
('113.43.d.20.A',3,'GIS (Geographic Information Systems) are used to do what?','["build bridges", "layer and analyze map data on a computer", "sort mail by hand", "print books"]'::jsonb,1,'GIS helps planners make decisions.','original'),
('113.43.d.20.B',3,'Medical advances such as vaccines have affected populations by doing what?','["reducing food", "increasing disease", "increasing life expectancy", "ending travel"]'::jsonb,2,'Health technology changes demographics.','original'),
('113.43.d.21.A',3,'A satellite image is what kind of geographic source?','["an opinion", "a legend", "a poem", "a primary-source type of data showing Earth''s surface"]'::jsonb,3,'Remote sensing provides evidence.','original'),
('113.43.d.21.B',3,'On a world map, which sea lies between Europe and Africa?','["the Mediterranean Sea", "the Baltic Sea", "the Red Sea", "the Caspian Sea"]'::jsonb,0,'It borders southern Europe and northern Africa.','original'),
('113.43.d.21.B',3,'The Strait of Hormuz is important because it does what?','["connects the Atlantic and Pacific", "controls the shipping of oil from the Persian Gulf", "borders Mexico", "crosses Russia"]'::jsonb,1,'A large share of the world''s oil passes through it.','original'),
('113.43.d.21.B',3,'Which continent is home to the Amazon rainforest?','["Australia", "Asia", "South America", "Africa"]'::jsonb,2,'It is the world''s largest rainforest.','original'),
('113.43.d.21.C',3,'A thematic map is designed to show what?','["only latitude", "only political borders", "only roads", "a specific topic such as population density or rainfall"]'::jsonb,3,'Thematic maps show patterns.','original'),
('113.43.d.21.C',3,'A map scale helps you to do what?','["measure real distances", "name the country", "tell the date", "find the compass rose"]'::jsonb,0,'Scale links map distance to real distance.','original'),
('113.43.d.21.C',3,'Lines of latitude measure distance in which direction?','["up from sea level", "north and south of the equator", "around the poles only", "east and west of the prime meridian"]'::jsonb,1,'Latitude lines run east-west.','original'),
('113.43.d.21.C',3,'Lines of longitude measure distance in which direction?','["below sea level", "north and south of the equator", "east and west of the prime meridian", "above the Earth"]'::jsonb,2,'Longitude lines run north-south.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_worldgeo_v1'
from (values
('113.43.d.21.D',3,'Identifying why a famine occurred requires what skill?','["memorizing a map", "ignoring evidence", "guessing", "analyzing cause and effect"]'::jsonb,3,'Geographers examine causes and consequences.','original'),
('113.43.d.21.E',3,'Different points of view on an issue result from what?','["people''s different experiences, values and interests", "geography alone", "identical backgrounds", "a lack of opinions"]'::jsonb,0,'Perspectives vary.','original'),
('113.43.d.21.F',3,'A strong geographic claim is supported by what?','["guesses", "evidence such as maps and data", "opinion only", "rumors"]'::jsonb,1,'Claims need evidence.','original'),
('113.43.d.22.A',3,'A bar graph is best used to do what?','["show elevation", "show borders", "compare amounts across categories", "show time zones"]'::jsonb,2,'Graphs communicate data.','original'),
('113.43.d.22.A',3,'A climograph shows what?','["types of rock", "population by age", "routes of explorers", "monthly temperature and precipitation for a place"]'::jsonb,3,'It combines two data sets.','original'),
('113.43.d.22.B',3,'A thesis statement is what?','["a clear claim that a paper will support with evidence", "a graph title", "a map legend", "a list of sources"]'::jsonb,0,'It states the main argument.','original'),
('113.43.d.22.C ',3,'Which term describes the average weather conditions in a place over many years?','["season", "climate", "forecast", "weather"]'::jsonb,1,'Weather is short term; climate is long term.','original'),
('113.43.d.22.C ',3,'The study of human populations and their characteristics is called what?','["cartography", "meteorology", "demography", "topography"]'::jsonb,2,'Demography studies size, growth and distribution.','original'),
('113.43.d.22.D',3,'When writing a research paper, a student should do what?','["invent evidence", "use no sources", "copy text without credit", "cite sources properly"]'::jsonb,3,'Citations give credit to others.','original'),
('113.43.d.22.E',3,'Civil discourse in a class discussion means what?','["respectful disagreement supported by evidence", "ignoring facts", "personal attacks", "shouting"]'::jsonb,0,'Respect and evidence guide discussion.','original'),
('113.43.d.23.A',3,'The process of voting is an example of what?','["a landform", "a way citizens take part in government", "a natural process", "a trade route"]'::jsonb,1,'Voting is a core democratic process.','original'),
('113.43.d.23.A',3,'A caucus is used to do what?','["collect taxes", "measure rainfall", "select political party candidates in some states", "draw maps"]'::jsonb,2,'Caucuses are party meetings.','original'),
('113.43.d.23.B',3,'The first step of a geographic research project is usually what?','["citing sources", "writing the conclusion", "making a poster", "asking a geographic question"]'::jsonb,3,'Research starts with questions.','original'),
('113.43.d.23.C',3,'A case study of a single city helps geographers do what?','["understand a larger issue through a specific example", "end research", "avoid data", "ignore other places"]'::jsonb,0,'Examples reveal patterns.','original'),
('113.43.d.23.D',3,'After identifying a problem and gathering information, what is the next step in decision making?','["ignoring the evidence", "listing and evaluating options", "repeating the problem", "ending the project"]'::jsonb,1,'Weigh options before choosing.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;

#!/usr/bin/env python3
"""High school World Geography Studies (TEKS 113.43.d). Original questions."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('113.43.d.', 997, own='hs_worldgeo.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 1 physical features and history
H('1.A', 3, "Why did the Nile River valley become the center of ancient Egyptian civilization?", "its yearly floods left fertile soil in a desert region", ["it had the highest mountains in Africa", "it was free of flooding", "it was covered in thick forest"], "Physical features shape where people settle.")
H('1.A', 3, "Which physical feature helped protect medieval Japan from invasion?", "surrounding seas", ["wide deserts", "dense jungle", "a long river"], "Island location limited outside attacks.")
H('1.B', 3, "The Columbian Exchange is an example of what geographic process?", "spatial diffusion of plants, animals and diseases between hemispheres", ["erosion of coastlines", "a shift in wind patterns", "volcanic activity"], "Diffusion is the spread of things across space.")
H('1.B', 4, "The spread of a new idea from a single place outward to surrounding areas is called what?", "diffusion", ["erosion", "migration", "convergence"], "Geographers trace how ideas and goods move through space.")

# 2 regions over time
H('2.A', 3, "Comparing a map of the Silk Road in 1200 to one of today shows changes in what?", "human features such as trade routes and cities", ["the position of the equator", "the length of a day", "the size of the oceans"], "Human characteristics change over time.")
H('2.B', 3, "Which change would most likely cause a region's cities to grow quickly?", "new industry that draws workers from rural areas", ["a loss of all jobs", "a ban on travel", "a decline in all trade"], "Technology and jobs shift population.")

# 3 weather and climate
H('3.A', 3, "What causes the seasons on Earth?", "the tilt of Earth's axis as it orbits the sun", ["Earth's distance from the sun changing a lot", "the moon's gravity", "the speed of ocean currents"], "Tilt changes the angle and length of sunlight.")
H('3.A', 3, "The Northern Hemisphere has its longest day around what date?", "June 21 (summer solstice)", ["December 21", "March 1", "September 30"], "The North Pole tilts toward the sun in June.")
H('3.B', 3, "Weathering and erosion are physical processes that do what?", "break down and move rock and soil, changing landforms", ["create new oceans", "stop rivers from flowing", "increase the sun's heat"], "Water, wind and ice reshape Earth's surface.")
H('3.B', 3, "A glacier shapes land by doing what?", "carving valleys as it slowly moves", ["raising the water table to flood plains", "building volcanoes", "making deserts"], "Glaciers erode and deposit rock.")
H('3.C', 3, "Which hazard is common along the 'Ring of Fire' around the Pacific Ocean?", "earthquakes and volcanoes", ["blizzards", "droughts", "sandstorms"], "Plate boundaries are active there.")
H('3.C', 3, "El Niño is a warming of surface water in which ocean?", "the Pacific", ["the Arctic", "the Indian", "the Southern"], "It changes weather around the world.")

# 4 climate/landforms/biomes
H('4.A', 3, "Cities at higher elevation are usually what compared with nearby low-lying areas?", "cooler", ["warmer", "more humid", "closer to sea level"], "Temperature drops as altitude increases.")
H('4.A', 3, "The Gulf Stream keeps western Europe warmer than other places at the same latitude. What is it?", "a warm ocean current", ["a cold wind", "a mountain chain", "a desert"], "Ocean currents carry heat.")
H('4.A', 4, "Why is the interior of a large continent often drier than its coasts?", "it is far from moisture-carrying ocean air", ["it has no sunlight", "it is closer to the equator", "it has more oceans"], "Distance from water affects rainfall.")
H('4.B', 3, "Which landform is a large area of flat or gently rolling land?", "a plain", ["a plateau", "a canyon", "a volcano"], "Plains are good for farming.")
H('4.B', 3, "A chain of islands is called what?", "an archipelago", ["a peninsula", "a delta", "an isthmus"], "Japan and the Philippines are archipelagos.")
H('4.B', 3, "A river delta forms where what happens?", "a river deposits sediment as it enters a larger body of water", ["a glacier melts", "two mountains meet", "wind blows sand"], "Deltas are rich farmland.")
H('4.C', 3, "A biome with very little rainfall and sparse vegetation is a what?", "desert", ["tropical rainforest", "taiga", "temperate forest"], "Climate determines biome.")
H('4.C', 3, "Which biome is found near the equator and receives heavy rain year-round?", "tropical rainforest", ["tundra", "grassland", "desert"], "Warm, wet conditions support dense vegetation.")

# 5 places
H('5.A', 3, "The 'character' of a place is shaped by what?", "its physical, cultural, economic and political features", ["its name only", "the number of roads", "its distance from the equator only"], "Place combines many factors.")
H('5.B', 3, "Gross domestic product (GDP) measures what?", "the total value of goods and services a country produces", ["the number of people in a country", "the size of a country", "the length of a country's coastline"], "GDP is an economic indicator.")
H('5.B', 3, "A high literacy rate and long life expectancy usually indicate what?", "a higher level of development", ["a lack of schools", "a low standard of living", "a smaller economy"], "Development indicators reflect well-being.")

# 6 settlement
H('6.A', 3, "Many large cities were founded near rivers because rivers provided what?", "water, transportation and fertile land", ["protection from rain", "more mountains", "colder weather"], "Physical features influence settlement.")
H('6.A', 3, "A site that is a natural harbor is likely to develop into what?", "a major port city", ["a mining town only", "an isolated village", "a desert oasis"], "Ports connect trade.")
H('6.B', 3, "Urbanization means what?", "the growth of cities as people move from rural areas", ["moving to farms", "the decline of towns", "a shrinking population"], "Urban areas expand through migration.")
H('6.B', 3, "Suburbanization is the movement of people to where?", "areas on the edges of cities", ["the center of a city", "deserts", "mountain tops"], "Cars and highways made it possible.")

# 7 population
H('7.A', 3, "A population pyramid with a wide base and narrow top shows what?", "a young population with high birth rates", ["an aging population", "no births", "a stable older population"], "The shape reveals age structure.")
H('7.A', 3, "A population pyramid that looks like a column or is narrow at the bottom shows what?", "slow growth or an aging population", ["rapid growth", "a very young country", "a country with no deaths"], "Low birth rates reduce the base.")
H('7.B', 3, "A 'push' factor in migration is something that does what?", "drives people away from their home, such as war or poverty", ["attracts people to a new place", "keeps them at home", "prevents travel"], "Push and pull forces influence migration.")
H('7.B', 3, "A 'pull' factor in migration is something that does what?", "attracts people to a new place, such as jobs or safety", ["forces people to leave", "stops migration", "causes floods"], "Opportunity pulls migrants.")
H('7.C', 3, "World population has been growing fastest in recent decades in which kind of countries?", "developing countries", ["the smallest countries only", "Arctic regions", "all high-income countries"], "Growth rates are higher where birth rates remain high.")
H('7.D', 3, "How does globalization affect the spread of pandemics?", "faster travel and trade can spread disease more quickly", ["it makes disease stop at borders", "it ends disease", "it slows all travel"], "Connectivity has risks and benefits.")
H('7.D', 3, "A possible negative effect of globalization on cultures is what?", "loss of traditional languages and customs", ["more traditional crafts", "fewer products", "less communication"], "Global culture can overshadow local culture.")

# 8 human-environment
H('8.A', 3, "Terracing hillsides for farming is an example of how people do what?", "modify the environment to meet their needs", ["avoid the environment", "ignore climate", "destroy farmland"], "Humans adapt and modify landscapes.")
H('8.A', 3, "Building homes on stilts in flood-prone areas is an example of what?", "adapting to the environment", ["modifying the climate", "ignoring risks", "depending on deserts"], "People adapt to hazards.")
H('8.B', 3, "A major consequence of a severe drought is what?", "food shortages and migration", ["more rainfall", "increased harvests", "colder temperatures"], "Drought harms crops and water supplies.")
H('8.C', 3, "Deforestation can lead to what environmental problem?", "soil erosion and loss of habitat", ["more fertile soil", "larger forests", "cleaner water always"], "Removing trees exposes soil.")
H('8.C', 3, "The draining of the Aral Sea resulted from what?", "diversion of rivers for irrigation", ["a volcanic eruption", "glacier growth", "rising ocean levels"], "Water diversion shrank the lake.")

# 9 regions
H('9.A', 3, "A shared language, religion or history can help define a what?", "cultural region", ["time zone", "tectonic plate", "climate zone"], "Regions are defined by shared traits.")
H('9.B', 3, "A formal region is defined by what?", "a common characteristic such as an official boundary or a shared language", ["a flow of goods and people around a hub", "people's feelings about a place", "a changing tide"], "Examples include countries and states.")
H('9.B', 3, "A functional region is organized around what?", "a central point such as a city and its connected area", ["a shared climate only", "a single mountain", "people's opinions only"], "A newspaper's delivery area is an example.")
H('9.B', 3, "A perceptual region reflects what?", "people's feelings or ideas about an area, such as 'the Midwest'", ["exact borders", "a transportation hub", "scientific measurements"], "Perceptual regions are based on opinions.")

# 10 economic systems
H('10.A', 3, "In a market economy, prices are set mostly by what?", "supply and demand", ["tradition only", "the government", "a ruler's decree"], "Buyers and sellers decide.")
H('10.A', 3, "In a traditional economy, decisions are based mainly on what?", "custom and habit passed down", ["government planning", "competition", "stock markets"], "Roles follow past practice.")
H('10.A', 3, "In a command economy, who decides what is produced?", "the government", ["individual consumers", "competing firms", "local traditions"], "Central planning guides production.")
H('10.B', 3, "Which economic system allows private ownership and competition with limited government involvement?", "free enterprise (capitalism)", ["communism", "a traditional economy", "a command economy"], "Capitalism relies on markets.")
H('10.B', 3, "Which system has the government own most resources and factories?", "communism", ["free enterprise", "a mixed economy", "market capitalism"], "Communist states plan the economy.")
H('10.C', 3, "A subsistence farmer mainly grows food for what purpose?", "to feed their own family", ["to export to other nations", "to supply supermarkets", "to sell to factories"], "Subsistence farming is not for large-scale sale.")
H('10.D', 3, "Global trade patterns have changed over time because of what?", "advances in transportation and communication", ["a ban on shipping", "the end of ports", "lower demand for goods"], "Technology lowers costs of trade.")

# 11 economic activities
H('11.A', 3, "Farming, fishing and mining are examples of which type of economic activity?", "primary", ["secondary", "tertiary", "quaternary"], "Primary activities extract raw materials.")
H('11.A', 3, "Turning raw cotton into clothing is what kind of economic activity?", "secondary", ["primary", "tertiary", "quaternary"], "Manufacturing is secondary.")
H('11.A', 3, "Teaching, banking and retail are examples of what?", "tertiary (service) activities", ["primary activities", "secondary activities", "subsistence farming"], "Services are tertiary.")
H('11.B', 3, "A factory is often placed near a port or railroad because of what?", "access to transportation for raw materials and finished goods", ["fewer customers", "lack of workers", "colder climate"], "Location reduces cost.")
H('11.C', 3, "A new highway could change a region's economy by doing what?", "making it easier to move goods and workers", ["isolating towns", "ending trade", "raising mountains"], "Infrastructure supports growth.")

# 12 resources
H('12.A', 3, "Oil is a non-renewable resource because it does what?", "takes millions of years to form and cannot be replaced quickly", ["regrows each year", "is unlimited", "falls as rain"], "Fossil fuels are finite.")
H('12.A', 3, "Which is a renewable energy source?", "wind", ["coal", "natural gas", "oil"], "Wind and sun are naturally replenished.")
H('12.B', 4, "A country with large oil reserves may have what advantage and risk?", "income from exports but dependence on one resource", ["no advantage", "less trade", "no risk"], "Resource economies can be unstable.")
H('12.B', 3, "Conservation policies aim to do what?", "protect resources for future use", ["use up resources faster", "end all development", "ban trade"], "Sustainable policy balances use and protection.")

# 13 political boundaries
H('13.A', 3, "A boundary that follows a river or mountain range is what kind?", "a natural boundary", ["a geometric boundary", "a cultural boundary", "a time boundary"], "Physical features can mark borders.")
H('13.A', 3, "A straight-line border such as the 49th parallel is what kind?", "a geometric boundary", ["a natural boundary", "a religious boundary", "a coastline"], "It follows lines of latitude.")
H('13.B', 3, "Comparing voting maps with political boundaries helps show what?", "how voting patterns relate to regions", ["the age of rocks", "average rainfall", "tectonic movement"], "Maps reveal political geography.")

# 14 political systems and control
H('14.A', 3, "The breakup of Yugoslavia in the 1990s is an example of what?", "ethnic and political divisions forming new states", ["a natural disaster", "unification of countries", "a trade agreement"], "Political conflict redrew borders.")
H('14.B', 3, "In a democracy, who ultimately holds political power?", "the people", ["a single ruler", "religious leaders only", "the military"], "Citizens elect leaders.")
H('14.B', 3, "In a monarchy, power is passed down through what?", "a royal family", ["elections", "military coups", "the courts"], "Rulers inherit the throne.")
H('14.B', 3, "A dictatorship is a government in which what?", "one person or a small group holds absolute power", ["citizens vote on all laws", "religious leaders vote", "kings share power with a legislature"], "Dictators limit freedoms.")
H('14.C', 4, "Why are mountain passes and rivers often contested?", "they control movement of people and resources", ["they are always empty", "they have no value", "they are never used for trade"], "Control of key places brings power.")

# 15 viewpoints
H('15.A', 3, "Why might two countries have different views about a shared river?", "each depends on the water for its own needs", ["rivers have no value", "rivers are not shared", "all countries agree"], "Competing interests cause conflict.")
H('15.B', 3, "How can public opinion shape policy about a nearby natural area?", "through voting, petitions and public meetings", ["it cannot", "only the military decides", "only judges decide"], "Citizens influence decisions.")

# 16 culture
H('16.A', 3, "Terraced rice fields are a distinctive cultural landscape of what region?", "Southeast Asia", ["northern Europe", "the Sahara", "Antarctica"], "Farming practices shape the land.")
H('16.B', 3, "Which is an element of culture?", "language", ["latitude", "tides", "weather"], "Culture includes language, religion, beliefs and institutions.")
H('16.B', 3, "A tradition passed down through generations, such as a festival, is part of what?", "a culture's heritage", ["its climate", "its time zone", "its biome"], "Customs preserve cultural identity.")
H('16.C', 3, "Which is more common in rural areas than in cities?", "farming as the main occupation", ["skyscrapers", "subway systems", "large airports"], "Land use differs between urban and rural.")

# 17 religions and cultures
H('17.A', 3, "Arabic is the dominant language of which region?", "North Africa and the Middle East", ["South America", "Scandinavia", "Southeast Asia"], "Language patterns reflect history.")
H('17.B', 3, "Which religion has the largest number of followers in India?", "Hinduism", ["Christianity", "Buddhism", "Judaism"], "Hinduism began in the Indian subcontinent.")
H('17.B', 3, "Mecca, the holiest city of Islam, is in what country?", "Saudi Arabia", ["Egypt", "Iran", "Turkey"], "Muslims pilgrimage there.")
H('17.B', 3, "Buddhism began in which part of the world?", "South Asia (India and Nepal)", ["Western Europe", "North America", "Australia"], "Siddhartha Gautama taught there.")
H('17.C', 3, "In many societies, women's access to education and jobs depends on what?", "cultural traditions and laws", ["climate only", "latitude", "time zones"], "Opportunity differs among cultures.")
H('17.D', 3, "A multicultural society is one in which what exists?", "many cultural groups live together", ["only one culture", "no traditions", "no languages"], "The United States is an example.")

# 18 cultural change
H('18.A', 3, "Which of these can cause cultural change?", "migration, trade or war", ["the position of the sun only", "tides only", "volcanoes only"], "Contact spreads ideas.")
H('18.B', 3, "The Rwandan genocide of 1994 was a conflict between which groups?", "Hutu and Tutsi", ["Serbs and Croats", "Sunni and Shia", "Greeks and Turks"], "It killed around 800,000 people.")
H('18.C', 3, "Some groups, such as certain Indigenous peoples, maintain traditional ways by doing what?", "preserving language and subsistence practices", ["abandoning all customs", "moving to cities only", "banning outsiders from all contact"], "Traditions can survive modernization.")
H('18.D', 3, "Cultural convergence means what?", "cultures becoming more alike", ["cultures becoming more different", "cultures disappearing", "cultures separating"], "Globalization promotes convergence.")
H('18.D', 3, "Cultural divergence means what?", "cultures becoming more different over time", ["cultures merging", "languages spreading", "cities growing"], "Isolation or resistance can cause divergence.")

# 19 technology
H('19.A', 3, "The Panama Canal changed transportation by doing what?", "shortening ship routes between the Atlantic and Pacific", ["blocking ship travel", "creating a new ocean", "ending world trade"], "It cut thousands of miles from voyages.")
H('19.A', 3, "The invention of the jet engine most changed what?", "long-distance travel", ["farming methods", "the length of days", "ocean currents"], "Air travel connects the world.")
H('19.B', 3, "Air conditioning has allowed more people to live where?", "in hot regions such as the U.S. Sun Belt", ["only in cold regions", "only in cities", "only on islands"], "Technology changes settlement.")
H('19.B', 3, "Desalination makes it possible to do what?", "turn seawater into drinking water", ["turn rain into salt", "raise sea level", "freeze lakes"], "It helps dry coastal areas.")
H('19.C', 3, "The Green Revolution increased food production through what?", "high-yield crops, fertilizer and irrigation", ["fewer farms", "banning machines", "less water"], "It reduced hunger in many regions.")

# 20 information technology
H('20.A', 3, "GPS (Global Positioning System) allows users to do what?", "determine exact locations on Earth using satellites", ["predict earthquakes", "change climates", "stop storms"], "Satellites send location data.")
H('20.A', 3, "GIS (Geographic Information Systems) are used to do what?", "layer and analyze map data on a computer", ["print books", "sort mail by hand", "build bridges"], "GIS helps planners make decisions.")
H('20.B', 3, "Medical advances such as vaccines have affected populations by doing what?", "increasing life expectancy", ["increasing disease", "reducing food", "ending travel"], "Health technology changes demographics.")

# 21 skills
H('21.A', 3, "A satellite image is what kind of geographic source?", "a primary-source type of data showing Earth's surface", ["a poem", "a legend", "an opinion"], "Remote sensing provides evidence.")
H('21.B', 3, "On a world map, which sea lies between Europe and Africa?", "the Mediterranean Sea", ["the Caspian Sea", "the Baltic Sea", "the Red Sea"], "It borders southern Europe and northern Africa.")
H('21.B', 3, "The Strait of Hormuz is important because it does what?", "controls the shipping of oil from the Persian Gulf", ["connects the Atlantic and Pacific", "borders Mexico", "crosses Russia"], "A large share of the world's oil passes through it.")
H('21.B', 3, "Which continent is home to the Amazon rainforest?", "South America", ["Africa", "Asia", "Australia"], "It is the world's largest rainforest.")
H('21.C', 3, "A thematic map is designed to show what?", "a specific topic such as population density or rainfall", ["only political borders", "only roads", "only latitude"], "Thematic maps show patterns.")
H('21.C', 3, "A map scale helps you to do what?", "measure real distances", ["find the compass rose", "name the country", "tell the date"], "Scale links map distance to real distance.")
H('21.C', 3, "Lines of latitude measure distance in which direction?", "north and south of the equator", ["east and west of the prime meridian", "up from sea level", "around the poles only"], "Latitude lines run east-west.")
H('21.C', 3, "Lines of longitude measure distance in which direction?", "east and west of the prime meridian", ["north and south of the equator", "above the Earth", "below sea level"], "Longitude lines run north-south.")
H('21.D', 3, "Identifying why a famine occurred requires what skill?", "analyzing cause and effect", ["memorizing a map", "ignoring evidence", "guessing"], "Geographers examine causes and consequences.")
H('21.E', 3, "Different points of view on an issue result from what?", "people's different experiences, values and interests", ["identical backgrounds", "a lack of opinions", "geography alone"], "Perspectives vary.")
H('21.F', 3, "A strong geographic claim is supported by what?", "evidence such as maps and data", ["opinion only", "rumors", "guesses"], "Claims need evidence.")

# 22 communication
H('22.A', 3, "A bar graph is best used to do what?", "compare amounts across categories", ["show elevation", "show borders", "show time zones"], "Graphs communicate data.")
H('22.A', 3, "A climograph shows what?", "monthly temperature and precipitation for a place", ["population by age", "types of rock", "routes of explorers"], "It combines two data sets.")
H('22.B', 3, "A thesis statement is what?", "a clear claim that a paper will support with evidence", ["a list of sources", "a map legend", "a graph title"], "It states the main argument.")
H('22.C ', 3, "Which term describes the average weather conditions in a place over many years?", "climate", ["weather", "season", "forecast"], "Weather is short term; climate is long term.")
H('22.C ', 3, "The study of human populations and their characteristics is called what?", "demography", ["topography", "meteorology", "cartography"], "Demography studies size, growth and distribution.")
H('22.D', 3, "When writing a research paper, a student should do what?", "cite sources properly", ["copy text without credit", "invent evidence", "use no sources"], "Citations give credit to others.")
H('22.E', 3, "Civil discourse in a class discussion means what?", "respectful disagreement supported by evidence", ["shouting", "ignoring facts", "personal attacks"], "Respect and evidence guide discussion.")

# 23 research and participation
H('23.A', 3, "The process of voting is an example of what?", "a way citizens take part in government", ["a natural process", "a trade route", "a landform"], "Voting is a core democratic process.")
H('23.A', 3, "A caucus is used to do what?", "select political party candidates in some states", ["measure rainfall", "collect taxes", "draw maps"], "Caucuses are party meetings.")
H('23.B', 3, "The first step of a geographic research project is usually what?", "asking a geographic question", ["writing the conclusion", "citing sources", "making a poster"], "Research starts with questions.")
H('23.C', 3, "A case study of a single city helps geographers do what?", "understand a larger issue through a specific example", ["avoid data", "ignore other places", "end research"], "Examples reveal patterns.")
H('23.D', 3, "After identifying a problem and gathering information, what is the next step in decision making?", "listing and evaluating options", ["ignoring the evidence", "repeating the problem", "ending the project"], "Weigh options before choosing.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_worldgeo.jsonl'))

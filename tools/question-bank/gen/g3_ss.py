#!/usr/bin/env python3
"""Grade 3 Social Studies (TEKS 113.14.c) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('113.14.c.', 913, own='g3_ss.jsonl')

load(B, """
1.A|3|How can a new bridge change a community?|it can make travel faster and bring new businesses|it makes the town disappear|it stops all travel|it removes the river|New roads and bridges change how people live.
1.B|3|Who designed the layout of streets for Washington, D.C.?|Pierre-Charles L'Enfant|Daniel Boone|Clara Barton|Henry Ford|L'Enfant planned the capital city.
1.B|3|Benjamin Banneker helped shape communities by...|helping survey the land for the nation's capital|inventing the airplane|painting murals|building the first car|Banneker was a surveyor and scientist.
1.B|3|Benjamin Franklin helped his community by...|starting a library and a fire company|building a spaceship|creating video games|fighting in the Civil War|Franklin founded community institutions.
1.C|3|Daniel Boone helped expand American settlement by...|leading settlers through the Cumberland Gap|inventing the telephone|designing airplanes|building the Panama Canal|Boone blazed the Wilderness Road.
1.C|4|The Founding Fathers contributed to a new community by...|helping create a new nation|building the Great Wall|flying to the moon|discovering gold in Alaska|They created the United States government.
2.A|3|Why did many people form communities?|for safety and shared laws|to avoid each other|to stop trade|to hide from friends|Communities offer security.
2.A|3|Some people came to America seeking...|religious freedom|a longer school year|new video games|faster phones|Many sought freedom of worship.
2.B|3|How do communities meet their need for communication?|phones, mail, and the internet|only drums|only carrier pigeons today|they do not communicate|Communication tools connect people.
2.B|3|Which is a way communities meet the need for transportation?|buses and roads|ovens|bookshelves|chalk|Buses and roads move people.
3.A|3|Which is a landform?|plateau|climate|rainfall|breeze|A plateau is a high flat area.
3.A|3|Which is a natural hazard?|hurricane|library|bridge|school bell|Hurricanes are dangerous natural events.
3.A|3|Which describes climate?|the typical weather over many years|today's weather only|a single storm|one windy hour|Climate is long-term weather.
3.B|3|How might people in a desert adapt to the heat?|wear light clothing and build thick-walled homes|build igloos|wear heavy coats|plant rice in snow|Adapting helps people survive.
3.B|4|People may modify the land by...|building dams to hold water|rearranging the stars|stopping the wind|erasing mountains by wishing|Dams change the land.
3.C|3|What is one effect of pollution?|it can harm water and animals|it makes the air cleaner|it grows more forests|it brightens the sky|Pollution damages the environment.
3.C|3|Which action is conservation?|recycling paper|dumping trash in a river|leaving lights on|wasting water|Recycling protects resources.
4.A|3|Which direction is between north and east?|northeast|southwest|northwest|southeast|Northeast is between north and east.
4.A|3|Which direction is halfway between south and west?|southwest|northeast|southeast|northwest|Southwest is halfway.
4.B|3|A map scale says 1 inch = 10 miles. Two towns are 3 inches apart. About how many miles apart are they?|30 miles|13 miles|3 miles|300 miles|3 times 10 equals 30.
4.B|3|Why is a map scale useful?|it shows real distances|it tells the weather|it shows jokes|it names birds|A scale converts map to real distance.
4.C|3|Which map element helps find places using letters and numbers?|grid system|compass rose|title|scale|A grid helps locate positions.
4.C|3|The legend of a map shows...|what symbols stand for|the mapmaker's lunch|today's date|a recipe|A legend explains symbols.
5.A|3|Which is a way to earn money?|doing a job|finding a rainbow|wishing for it|watching TV|Work earns income.
5.A|3|Which is a way to donate money?|give it to a charity|burn it|bury it forever|trade it for air|Donating helps others.
5.B|3|A student earns $10 and decides to spend $6 and save the rest. How much is saved?|$4|$6|$10|$16|10 minus 6 is 4.
5.B|3|Why make a budget?|to plan spending and saving|to lose money|to hide coins|to buy everything|A budget organizes money.
6.A|3|If many people want a toy but few are made, the price will likely...|go up|go down|stay at zero|disappear|High demand and low supply raise price.
6.A|3|If a store has too many apples and few buyers, the price will likely...|go down|go up|double|stay the same|Low demand lowers price.
6.B|3|Scarcity means...|there is not enough of something for everyone's wants|there is too much of everything|nothing is wanted|everything is free|Scarcity is limited resources.
6.C|3|A bakery spends $2 to make a cupcake and sells it for $5. What is the profit?|$3|$7|$2|$5|5 minus 2 is 3.
6.D|3|Which person started the Ford Motor Company?|Henry Ford|Sam Walton|Clara Barton|Ruby Bridges|Henry Ford founded Ford.
6.D|3|Sam Walton started the store chain called...|Walmart|Target|Macy's|Sears|Walton founded Walmart.
7.A|3|Which level of government makes laws for a whole state?|state government|local government|a family|a school club|States have their own governments.
7.A|3|Which is the national government?|the federal government|a city council|a school board|a neighborhood club|Federal means national.
7.B|3|How is a mayor usually chosen?|elected by voters|picked by a coin toss|inherited from a relative|chosen by a raffle|Mayors are elected in most cities.
7.B|3|Who leads the United States?|the President|the mayor|the governor|the principal|The President is head of the executive branch.
7.C|2|Which is a service provided by local government?|trash pickup|private jets|toy making|movie making|Cities collect trash.
7.C|3|Which service is provided by the national government?|national defense|your lunch|your neighbor's lawn|a bakery|The military protects the country.
8.A|3|What did the Declaration of Independence say?|the colonies were free from British rule|the colonies would stay under Britain|there would be no laws|schools should close|It declared independence.
8.A|3|The first ten amendments to the Constitution are called...|the Bill of Rights|the Declaration|the Pledge|the Anthem|They protect individual rights.
8.B|4|The idea that government gets its power from the people is called...|consent of the governed|rule by one|power of a king|trade by barter|The people give their consent.
9.A|2|Which shows good citizenship?|obeying laws|breaking rules|cheating|being unkind|Citizens follow laws.
9.B|3|Helen Keller is remembered for...|working to help people with disabilities|piloting jets|inventing the radio|painting the Mona Lisa|Keller was an author and advocate.
9.B|3|Clara Barton is remembered for starting the...|American Red Cross|Boy Scouts|National Zoo|U.S. Mint|Barton founded the Red Cross.
9.B|3|Ruby Bridges is remembered for being...|the first Black child to attend an all-white school in her city|a famous pilot|a basketball star|an inventor of the telephone|She helped integrate schools.
9.C|3|Serving on a jury is an example of...|civic responsibility|a hobby|a holiday|a sport|Jury duty is a civic duty.
9.D|3|The Red Cross is a(n)...|nonprofit organization that helps people in need|private candy company|sports team|bank|Nonprofits serve the common good.
9.E|2|A class votes on a field trip. What does a majority mean?|more than half of the votes|less than half|exactly zero|no one decides|A majority is more than half.
10.A|3|Why are cultural celebrations important to communities?|they honor shared traditions|they remove history|they stop people from meeting|they end laws|Celebrations preserve heritage.
10.B|3|Both Cinco de Mayo and Juneteenth celebrate parts of history. What can you compare?|their meanings and customs|their weather only|their prices|their spelling|You compare significance and customs.
11.A|3|Hector P. Garcia is remembered for...|founding a group that fought for Mexican American civil rights|inventing a robot|flying around the world|painting the Alamo|He founded the American G.I. Forum.
11.A|4|James A. Lovell is remembered as...|an astronaut of Apollo 13|a Civil War general|an early mayor|a pop singer|Lovell commanded Apollo 13.
11.B|3|Harriet Tubman is remembered for...|guiding people to freedom on the Underground Railroad|inventing the telephone|writing the Constitution|building skyscrapers|She helped many escape slavery.
12|3|How do writers and artists help preserve a community's culture?|they tell its stories and show its traditions|they remove history|they hide traditions|they stop celebrations|Their works record culture.
13.A|3|Who developed a polio vaccine?|Jonas Salk|Cyrus McCormick|Bill Gates|Henry Ford|Salk developed the vaccine.
13.A|3|Cyrus McCormick invented a machine called the...|mechanical reaper|telephone|steam train|radio|The reaper helped farmers harvest.
13.A|3|Louis Pasteur is known for discovering...|pasteurization|electric lights|the telephone|airplanes|Pasteur's method kills germs in milk.
13.B|3|How did pasteurization help communities?|made milk and food safer|made roads longer|made houses taller|made lakes bigger|It reduced illness.
13.B|3|How have computers affected communities?|they speed up work and sharing information|they stopped communication|they removed all jobs|they ended schools|Computers help share data quickly.
14.A|3|Which is a good resource for learning about your community's past?|a local museum|a random guess|a rumor|a cartoon|Museums keep records.
14.B|3|What is a secondary source?|a book written later about an event|a diary from the time|a photo from the event|a letter from a soldier|A secondary source is created after the event.
14.B|3|What is a primary source?|a firsthand account from someone who was there|a rumor|a textbook summary|an opinion column|Primary sources are firsthand.
14.C|3|Which sentence is an opinion?|The park is the best place in town.|The park has a pond.|The park is open from 7 to 7.|The park has twenty trees.|Best is a personal judgment.
14.C|3|What is a cause of a flood after heavy rain?|rivers overflow|trees grow taller|clouds appear|the sun rises|Too much water overflows.
14.D|3|A bar graph shows how many books each grade read. What can you tell from it?|which grade read the most|what the weather is|who the principal is|the lunch menu|Bar graphs compare amounts.
14.D|3|A timeline helps you see...|events in order|only the weather|what to eat|which team won|Timelines show sequence.
14.E|3|A pamphlet says, "Our town needs more bike lanes to keep riders safe." What is the central claim?|more bike lanes are needed|bike lanes are red|riders eat lunch|the town is old|The claim is the main point.
14.F|3|What should you include when you share a claim?|supporting evidence|a joke|a random picture|a rumor|Claims need evidence.
15|2|What does the term "community" mean?|a group of people who live or work together|a kind of weather|a type of food|a mountain|Communities share places and goals.
15.B|3|Which timeline label would come first?|1776|1850|1950|2000|The earliest year comes first.
15.C|3|How many years are in a decade?|10|100|1,000|5|A decade is ten years.
15.C|3|How many years are in a century?|100|10|1,000|50|A century is 100 years.
15.F|3|Which is a respectful way to disagree in class?|explain your view politely|shout|interrupt|insult others|Civil discourse is respectful.
16.A|3|A class votes for a new school mascot. This simulates...|democratic decision making|choosing by coin toss|a monarchy|a mystery|Voting is democratic.
16.B|3|What is the first step in solving a community problem?|identify the problem|ignore it|blame others|hide it|You must define the problem first.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g3_ss.jsonl'))
print("saved", len(B.out), "questions")

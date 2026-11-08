#!/usr/bin/env python3
"""Grade 2 Social Studies (TEKS 113.13.c) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('113.13.c.', 912, own='g2_ss.jsonl')

load(B, """
1.A|2|On which holiday do Americans remember people who died while serving in the military?|Memorial Day|Groundhog Day|Labor Day|Flag Day|Memorial Day honors those who died serving.
1.A|2|Which holiday celebrates a harvest feast shared by the Pilgrims and Native Americans?|Thanksgiving|Presidents' Day|Arbor Day|Constitution Day|Thanksgiving is a day of gratitude.
1.B|3|Which kind of place is a monument?|a structure built to honor a person or event|a grocery store|a toy shop|a movie theater|Monuments honor history.
1.B|3|Which is a government building where a state's laws are made?|the state capitol|a bakery|a gym|a zoo|The capitol houses the legislature.
2.A|3|Who was the first African American Justice on the Supreme Court?|Thurgood Marshall|Irma Rangel|Theodore Roosevelt|Sam Houston|Thurgood Marshall served on the Supreme Court.
2.A|3|Who was the first Mexican American woman elected to the Texas House?|Irma Rangel|Eleanor Roosevelt|Harriet Tubman|Betsy Ross|Irma Rangel served in the Texas legislature.
2.A|3|Which President helped protect national parks and forests?|Theodore Roosevelt|James Buchanan|John Tyler|Franklin Pierce|Roosevelt was a conservationist.
2.B|3|Why do people study local history?|to learn how the community changed|to forget old stories|to avoid maps|to stop growing|Local history explains change.
3.A|2|Which part of a map explains what the symbols mean?|legend|title|compass|scale of years|A legend (key) explains symbols.
3.A|2|Which part of a map tells what the map shows?|title|legend|border|stamp|The title names the topic.
3.A|2|Which tool on a map shows north, south, east, and west?|compass rose|clock|ruler|weather vane|A compass rose shows directions.
3.B|3|A student draws a map of the classroom. What should be on it?|desks, door, and window in the right places|a recipe|a song|a joke|Maps show real locations.
4.A|2|How many continents are there?|7|5|3|12|There are seven continents.
4.A|2|Which is the largest ocean on Earth?|Pacific Ocean|Atlantic Ocean|Arctic Ocean|Indian Ocean|The Pacific is the largest.
4.A|2|Which continent do we live on in Texas?|North America|Asia|Africa|Europe|Texas is in North America.
4.B|3|What is the capital of Texas?|Austin|Dallas|Houston|El Paso|Austin is the capital.
4.B|3|What is the capital of the United States?|Washington, D.C.|New York City|Los Angeles|Chicago|The capital is Washington, D.C.
4.B|3|Which two countries border the United States?|Canada and Mexico|Brazil and Peru|France and Spain|Japan and China|Canada is north and Mexico is south.
5.A|3|Which action is a way people change the land?|building a road|watching clouds|counting stars|breathing air|Roads change the land.
5.A|3|Clearing land for farming is an example of...|changing the environment|a new continent|a holiday|a map legend|Farming alters the land.
5.B|3|What can happen if people cut down too many trees?|animals may lose homes|more clouds appear|the sea disappears|the moon shrinks|Habitat loss is a consequence.
5.C|2|Which action helps conserve resources?|turning off lights when not needed|leaving the water running|littering|wasting paper|Saving energy conserves.
5.C|2|Which is a way to replenish a resource?|planting new trees|burning more coal|throwing trash|digging up all the soil|Replanting replaces trees.
6.A|2|Where does a family get money to buy goods and services?|from work|from picking leaves|from drawing pictures only|from wishing|Work provides income.
6.B|3|A child gets five dollars. Which choice is saving?|putting some away for later|spending it all today|giving it away secretly|burning it|Saving means keeping for later.
6.B|3|Spending all your money on a toy means you may not have it for...|something else you want later|today's weather|your last name|breathing|Spending uses money up.
7.A|2|A farmer grows apples. What is the farmer?|a producer|a consumer|a customer|a tourist|Producers make goods.
7.A|2|A person buys apples to eat. What is the person?|a consumer|a producer|a farmer|a miner|Consumers use goods.
7.B|3|A baker sells bread and also buys flour. What does this show?|people can be producers and consumers|bakers do nothing|only farmers are producers|only kids are consumers|People play both roles.
7.C|3|Which shows the correct steps for making a wooden chair?|tree, lumber, chair|chair, lumber, tree|lumber, chair, tree|tree, chair, lumber|A chair starts as a tree.
7.C|3|A plant grown in a field becomes thread and then a T-shirt. Which one is the natural resource?|the plant from the field|thread|fabric|the T-shirt|The plant is the raw material.
8.A|3|What is one job of government?|keeping people safe|baking cakes|painting pictures|singing songs|Governments keep order and security.
8.A|3|Which function of government helps settle disagreements?|managing conflict|building toys|making jokes|growing flowers|Courts and laws manage conflict.
8.B|2|Which is a service from the government?|fire protection|toy store|pizza shop|video game|Fire departments are public services.
8.B|2|Which place do taxes help pay for so everyone can use it?|library|private yacht|candy store|private spa|Libraries are public.
9.A|2|What is the title of the leader of a city?|mayor|governor|president|judge|Mayors lead cities.
9.A|2|Who leads a state in the United States?|governor|mayor|principal|coach|Governors lead states.
9.B|3|How is a governor's role different from a mayor's?|a governor leads a state; a mayor leads a city|they are the same|a mayor leads a country|a governor leads a school|Their areas differ.
9.C|3|Which is one way a public official gets a job?|election|a coin toss|a spelling bee|buying a ticket|Voters elect officials.
9.D|3|Which is a way citizens take part in government?|vote when they are old enough|ignore the news|never speak|break rules|Voting is participation.
10.A|2|Which shows truthfulness?|telling what really happened|making up stories|hiding mistakes|blaming others|Truthful people are honest.
10.A|2|Which shows respect?|listening while others talk|calling names|grabbing toys|ignoring people|Respect includes listening.
10.B|3|Paul Revere is remembered for...|riding to warn colonists|inventing the telephone|flying a plane|building skyscrapers|He warned people during the American Revolution.
10.B|3|The Navajo Code Talkers helped the United States by...|sending secret messages in their language|building bridges|farming cotton|teaching art|They used their language as an unbreakable code.
10.C|2|Which is community service?|picking up trash in a park|breaking a window|skipping chores|yelling at neighbors|Service helps others.
11.A|2|Which do we say to show respect to the Texas flag?|the Pledge to the Texas Flag|a bedtime lullaby|a lunch order|a song about snacks|Texans recite the Texas pledge.
11.B|2|Which song starts with "O say can you see"?|The Star-Spangled Banner|America the Beautiful|Row Row Row|Jingle Bells|It is the national anthem.
11.B|2|Which patriotic song mentions "spacious skies"?|America the Beautiful|Old MacDonald|Twinkle Twinkle|Happy Birthday|It describes the American landscape.
11.C|2|A class votes on a snack. Which snack wins?|the one with the most votes|the one with the fewest votes|the one the teacher dislikes|a random shoe|Majority wins.
11.D|3|Which is the state bird of Texas?|mockingbird|robin|eagle|penguin|Texas's state bird is the mockingbird.
11.D|3|Which is the state flower of Texas?|bluebonnet|rose|tulip|sunflower|Bluebonnets are Texas's flower.
11.D|3|Who is Uncle Sam?|a symbol of the United States|a real cousin|a pirate|a dinosaur|Uncle Sam symbolizes America.
11.E|3|Fireworks on Independence Day reflect a love of...|freedom|rainy weather|sleeping late|homework|Fireworks celebrate liberty.
12.A|3|Why do many communities hold cultural celebrations?|to share traditions and heritage|to cancel school|to avoid friends|to hide stories|Celebrations honor heritage.
12.B|3|One celebration has a parade with drums. Another has dances with fans. What can you compare?|how they celebrate|their spelling|their weather forecasts|their dinner menus only|You compare customs.
13.A|2|How has technology changed communication?|people can talk or text from far away|people can no longer talk|letters appeared for the first time|nobody can listen|Phones and computers connect people.
13.A|2|How has technology changed travel?|planes move people across the country quickly|people no longer travel|people only ride horses|roads disappeared|Planes and cars are faster.
13.B|3|How do refrigerators help families meet needs?|keep food from spoiling|grow clothes|build houses|play music only|They store food safely.
14|3|Which person is known for inventing a telephone?|Alexander Graham Bell|Betsy Ross|Clara Barton|Paul Revere|Bell is credited with the telephone.
14|3|Which person is known for the airplane first flown at Kitty Hawk?|the Wright brothers|Neil Armstrong|Amelia Earhart|Henry Ford|The Wrights flew in 1903.
15.A|2|Which is a fact?|Texas is a state.|Texas is the best.|Texas is boring.|Everyone loves Texas.|A fact can be proven.
15.B|3|A letter written by a soldier long ago is a...|primary source|cartoon|rumor|riddle|It was written by someone who was there.
15.C|2|Which is a good way to learn about the past?|interview an elder|ignore old stories|guess|stop asking questions|Interviews gather first-hand information.
15.D|3|You read a story and say, "This is mostly about a family's move." What did you do?|identified the main idea|made a map|planted a tree|sang a song|The main idea is the big point.
16.A|2|Which time period includes dinosaurs and knights?|historical times|present time|tomorrow|next year|Historical means long ago.
16.B|2|Which word means something that has not happened yet?|future|past|present|history|Future is later.
16.C|3|On a timeline, which event came first?|the earliest date|the latest date|today|tomorrow|Earlier dates are to the left.
16.D|2|What does the word "citizen" mean?|a member of a community or country|a kind of animal|a type of weather|a food|Citizens belong to a community.
16.F|3|Which tool helps organize ideas before writing about a topic?|graphic organizer|calculator|stapler|ruler|Organizers arrange ideas.
17.A|2|A group wants to pick a class name. A fair way to decide is...|vote|argue|shout|walk out|Voting is democratic.
17.B|3|After listing choices and thinking about good and bad points, what is the next step?|choose and carry out a solution|forget the problem|blame a classmate|erase the list|Pick and use a solution.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g2_ss.jsonl'))
print("saved", len(B.out), "questions")

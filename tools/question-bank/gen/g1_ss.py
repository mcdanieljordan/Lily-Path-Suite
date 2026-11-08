#!/usr/bin/env python3
"""Grade 1 Social Studies (TEKS 113.12.c) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('113.12.c.', 911, own='g1_ss.jsonl')

load(B, """
1.A|2|Which holiday celebrates the signing of the Declaration of Independence?|Independence Day|Memorial Day|Labor Day|Arbor Day|Independence Day is July 4.
1.A|2|On Veterans Day, people honor...|those who served in the military|famous chefs|inventors of toys|sports stars|Veterans Day honors military service.
1.B|3|Two families celebrate a holiday. One has a picnic, and the other has a parade. What does this show?|people observe holidays in different ways|holidays are not real|nobody celebrates|only one way is allowed|Customs can differ.
2.A|2|Which leader helped Texas become a republic and later a state?|Sam Houston|Mickey Mouse|Robin Hood|Tom Sawyer|Sam Houston was a leader of Texas.
2.A|2|Which leader led the nation during the Civil War and signed the Emancipation Proclamation?|Abraham Lincoln|Daniel Boone|Paul Revere|Johnny Appleseed|Lincoln led the nation.
2.A|2|Which leader worked to end unfair treatment of Black Americans with peaceful marches and speeches?|Martin Luther King Jr.|Benjamin Banneker|Sam Houston|George Washington|He led the civil rights movement.
2.B|3|How are George Washington and Abraham Lincoln alike?|both were Presidents of the United States|both lived in Texas|both were astronauts|both were inventors of the telephone|Both led the nation.
3.A|2|You stand at the front of the class. Your friend is behind you. Where is your friend?|in back of you|in front of you|above you|inside you|Behind means in back of.
3.A|2|The pencil box is next to the book. What does next to mean?|beside it|very far away|under the world|across the sea|Next to means beside.
3.B|2|On a map, which direction is usually at the top?|north|south|east|west|North is usually up.
3.B|3|If you walk toward the setting sun, which direction are you going?|west|east|north|south|The sun sets in the west.
3.B|3|Which direction is opposite of south?|north|west|east|down|North is opposite south.
4.A|2|What does a simple map of a classroom show?|where furniture is|what is for lunch|who is the teacher|the weather today|A classroom map shows locations.
4.A|2|A map of your school shows the library near the gym. What does this help you do?|find your way|choose a lunch|learn a song|spell a word|Maps help you find places.
4.B|2|Which tool shows the whole Earth as a ball?|globe|calendar|ruler|clock|A globe is a model of Earth.
4.B|3|Which state is shown on a map of the United States where we live?|Texas|Antarctica|Mars|Atlantis|Texas is one of the 50 states.
5.A|2|Which is a landform?|hill|lake|rain|wind|A hill is land.
5.A|2|Which is a body of water?|ocean|desert|valley|plain|An ocean is water.
5.A|3|Which is a natural resource?|water|plastic toy|computer|brick wall|Water comes from nature.
5.A|2|Which is weather?|snowy|plateau|river|canyon|Snow is weather.
5.B|3|Why do people in hot places often wear light clothes?|to stay cool|to stay warm in snow|to hide from rain|to float|Light clothes keep people cool.
5.B|3|Why might people near the ocean eat a lot of fish?|fish live in the ocean nearby|there are no stores|there are no people|fish are in deserts|Location influences food.
6.A|2|Which way can a family meet the need for food?|grow or buy it|ignore it|ask the moon|avoid eating|Families grow or buy food.
6.A|2|Which is a way a family can get shelter?|build or rent a home|float in the sky|dig only to China|wait for a cloud|Shelter is a home.
6.B|3|One family grows vegetables. Another buys vegetables at a store. How are they alike?|both meet the need for food|both live in the same house|both grow tomatoes|both are far away|Both meet a need.
7.A|2|Which is a good, not a service?|a toy|a haircut|a bus ride|a doctor visit|A good is an item you can hold.
7.A|2|Which is a service?|a haircut|a shoe|a book|a toy|A service is work done for someone.
7.B|3|How can people exchange goods?|trade or buy|steal|break|hide|People trade goods for money or other goods.
7.C|3|Where can you buy groceries?|a market|a library book return|a zoo cage|a school bus|Markets sell goods.
8.A|2|Mia wants a new bike, a game, and a kite but only has money for one. What is this?|wanting more than she can have|having everything|being lost|getting free toys|Limited money.
8.B|3|Because people cannot have everything they want, they must...|make choices|stop eating|stop working|get everything|Scarcity requires choices.
8.C|3|A family must choose between a new couch and a vacation. This is an example of...|a family making a choice|a family getting everything|a family doing nothing|a free gift|They must pick one.
9.A|2|Which tool does a carpenter use?|hammer|stethoscope|paintbrush|whistle|Carpenters build with hammers.
9.A|2|A job well done is...|careful and finished|sloppy and late|ignored|broken|Good work is careful.
9.B|3|How does a farmer help make goods?|grows food|builds roads|teaches music|flies planes|Farmers produce food.
9.B|3|Which job helps make a service?|bus driver|candle maker|brick maker|toy builder|Drivers provide a service.
10.A|2|Why do rules and laws help a community?|they keep people safe and fair|they cause trouble|they make people sad|they stop everyone talking|Rules protect people.
10.A|2|Which is a classroom rule?|Raise your hand to speak.|Shout anytime.|Leave without asking.|Break pencils.|Rules guide behavior.
10.B|3|A law says drivers must stop at red lights. What does this law provide?|safety|nothing|noise|candy|Laws keep people safe.
10.B|3|When two students argue over a toy, a rule can help...|manage the conflict|start a fight|break the toy|ignore the problem|Rules help settle disagreements.
11.A|2|Which person makes sure students are safe at school?|principal|clown|pilot|bus mechanic|The principal oversees safety.
11.A|2|Who is responsible for keeping a child safe at home?|a parent or caregiver|a crossing sign|a stuffed toy|the mailbox|Parents care for children.
11.B|3|Who is the leader of our state of Texas?|governor|principal|coach|librarian|The governor leads the state.
11.B|3|Who is the leader of our whole country?|President|mayor|teacher|police chief|The President leads the nation.
11.B|3|Who is the leader of a city or town?|mayor|governor|President|principal|Mayors lead cities.
12.A|2|Which is a trait of a good citizen?|being honest|telling lies|breaking things|being unkind|Honesty is a good trait.
12.A|3|A good citizen shows respect by...|listening to others|interrupting|teasing|taking turns away|Respect includes listening.
12.A|3|Which is an example of responsibility?|cleaning up your toys|leaving trash|ignoring chores|hiding homework|Responsibility means doing your part.
12.B|3|Benjamin Franklin is remembered as a good citizen because he...|helped his community with ideas and inventions|only played games|never helped anyone|stayed alone|Franklin helped his community.
12.B|3|Eleanor Roosevelt is remembered for...|helping people and speaking up for fairness|selling candy|building roller coasters|making pizza|She worked for human rights.
13.A|2|Which landmark is a symbol of freedom in New York?|Statue of Liberty|the Eiffel Tower|the Great Wall|the Pyramids|The Statue of Liberty welcomed immigrants.
13.A|2|Which bell is a symbol of American independence?|Liberty Bell|school bell|doorbell|jingle bell|The Liberty Bell is a patriotic symbol.
13.A|2|What is the Alamo a symbol of in Texas?|bravery and the fight for freedom|a shopping mall|a swimming pool|a zoo|The Alamo is a Texas symbol.
13.B|2|What do you say to show respect to the United States flag?|the Pledge of Allegiance|a happy birthday song|a lunch order|a bedtime story|The pledge honors the flag.
13.C|3|Which song is the national anthem of the United States?|The Star-Spangled Banner|Jingle Bells|Happy Birthday|Twinkle Twinkle|It is the national anthem.
13.C|3|What is the motto printed on U.S. money?|In God We Trust|Go Team Go|Fun for All|Texas Forever|It is the national motto.
13.D|2|The class votes for a field trip. How is the winner chosen?|the choice with the most votes|the choice with the fewest votes|the teacher flips a coin|nobody decides|The most votes win.
13.E|3|Patriotic celebrations like parades show...|pride in freedom|fear of change|boredom|silence|They celebrate American values.
14.A|2|Which tradition might a family share on a special holiday?|a special meal|a nap in the grocery store|a lost sock|a missed bus|Traditions are repeated customs.
14.A|3|Why are family traditions important?|they help people share beliefs and bond|they cause arguments only|they stop people from talking|they make people forget|Traditions keep culture.
14.B|3|What do folktales often teach?|a lesson about beliefs|math homework only|how to fix a car|the weather forecast|Folktales pass on values.
15.A|2|How has technology changed the way families live?|washing machines save time|it makes houses disappear|it stops all work|it removes electricity|Machines help families.
15.B|3|Which invention helps people send messages to someone far away?|telephone|spoon|pillow|comb|Telephones connect distant people.
15.B|3|How is traveling today different from long ago?|cars and planes are faster than horses|there are no vehicles|everyone walks only|no one travels|Technology speeds travel.
15.C|3|Who invented a practical telephone?|Alexander Graham Bell|Garrett Morgan|Thomas Edison|Benjamin Franklin|Bell is credited with the telephone.
15.C|3|Thomas Edison is famous for improving the...|light bulb|airplane|telescope|stove|Edison improved the light bulb.
15.C|3|Garrett Morgan invented an early...|traffic signal|television|laptop|calculator|Morgan invented a traffic signal.
16.A|2|Which is a fact?|The Statue of Liberty is in New York.|The Statue of Liberty is boring.|Everyone should love statues.|Statues are scary.|A fact can be proved.
16.B|3|Which is a primary source from long ago?|an old diary|a cartoon about the past|a toy robot|a snack bar|A diary was written by someone who lived then.
16.B|3|A museum shows old tools and clothes. These objects are called...|artifacts|stories|songs|riddles|Artifacts are old objects.
16.D|2|You sort pictures into animals and plants. This is...|categorizing|hiding|erasing|guessing|Sorting into groups is categorizing.
17.A|2|On a timeline, which word tells about something that already happened?|past|present|future|never|Past is before now.
17.A|2|On a timeline, what do we call right now?|present|past|future|history|Present is now.
17.B|2|How many days are in a week?|7|5|10|12|A week has seven days.
17.B|2|How many months are in a year?|12|7|30|52|A year has twelve months.
17.D|3|A picture graph shows how many students like each fruit. What does it help you see?|which fruit is liked most|the weather|the time|a story ending|Graphs compare data.
17.E|2|Which word means something that happened a long time ago?|history|future|tomorrow|soon|History is about the past.
18.A|2|A class wants to choose a game. A fair way to decide is to...|vote|argue|walk away|hide|Voting is democratic.
18.B|3|What is the first step in solving a problem?|identify the problem|ignore it|blame someone|hide it|You must know the problem first.
18.B|3|After you gather information about a problem, you should...|list options|forget it|quit|panic|List possible solutions.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g1_ss.jsonl'))
print("saved", len(B.out), "questions")

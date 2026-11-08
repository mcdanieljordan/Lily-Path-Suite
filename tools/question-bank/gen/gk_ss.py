#!/usr/bin/env python3
"""Kindergarten Social Studies (TEKS 113.11.c) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('113.11.c.', 910, own='gk_ss.jsonl')

load(B, """
1.A|2|Which day do we remember soldiers who served our country?|Veterans Day|Halloween|Groundhog Day|Valentine's Day|Veterans Day honors people who served in the military.
1.A|2|On which holiday do we celebrate the birthday of our country?|Independence Day|Earth Day|April Fools' Day|Pi Day|Independence Day is on July 4.
1.A|3|Which day honors our presidents?|Presidents' Day|Pajama Day|Pizza Day|Leap Day|Presidents' Day honors leaders of our nation.
1.B|2|Which is something people may see on Independence Day?|fireworks|snowmen|Easter eggs|pumpkins|Fireworks are a July 4 custom.
1.B|2|What do many towns hold on Independence Day?|a parade|a snow day|a pumpkin patch|a bake-off for turkeys|Parades are a national holiday custom.
2|3|Who was the first President of the United States?|George Washington|Taylor Swift|Mickey Mouse|Santa Claus|George Washington led the new nation.
2|2|Who is known for helping lead Texas, as a hero at the Alamo?|Davy Crockett|Superman|Cinderella|Paul Bunyan|Davy Crockett was at the Alamo.
2|2|Which person helped enslaved people find freedom and is honored in American history?|Harriet Tubman|Pinocchio|Snow White|Peter Pan|Harriet Tubman helped many reach freedom.
3.A|3|A cat is hiding below the chair. Which word tells where the cat is?|under|over|near|far|Under means below.
3.A|2|Which word tells that something is close by?|near|far|under|over|Near means close.
3.A|2|A bird is high above your head. Which word fits?|over|under|inside|beneath|Over means above.
3.A|3|You write with your right hand. Which word names your other hand?|left|up|down|far|The other hand is the left.
3.B|2|Which place on a school campus is where you borrow books?|library|gym|cafeteria|nurse's office|The library has books.
3.B|2|Where do students usually eat lunch at school?|cafeteria|library|office|playground|The cafeteria serves lunch.
3.B|3|The playground is near the gym. Which is true?|they are close to each other|they are in different states|they are far away|one is underwater|Near means close.
3.C|2|Which tool is a round model of the Earth?|globe|clock|ruler|calendar|A globe shows the whole Earth.
3.C|2|Which tool shows where places are on flat paper?|map|spoon|brush|button|Maps show locations.
4.A|3|Which is a body of water?|lake|mountain|hill|desert|A lake is water.
4.A|2|Which is a landform?|mountain|ocean|rain|river|A mountain is land.
4.A|2|Which is a kind of weather?|rainy|hill|lake|valley|Rain is weather.
4.B|3|People in very cold places often wear...|warm coats|swim shorts|sandals|sun hats|Weather affects clothing.
4.B|2|People who live where it snows a lot need what kind of shelter?|a warm, sturdy house|an open field|a paper boat|a sandcastle|Shelter protects from weather.
5.A|2|Which is a basic human need?|food|a toy|a video game|a new bike|People need food to live.
5.A|3|Which is something every person needs to stay safe and warm?|shelter|a skateboard|a sticker|a balloon|Shelter protects people.
5.A|2|Which is a basic need for the body when it is cold outside?|clothing|a trophy|a book of jokes|a stuffed animal|Clothes keep people warm.
5.B|2|Which is a want, not a need?|a toy|water|food|a place to sleep|A toy is nice to have but not needed to live.
5.B|3|Which is a need, not a want?|water|candy|a game|a sticker|People need water.
5.C|2|How can a family get food?|buy it at a store|find it in a closet of toys|wait for it to fall from the moon|ask the clouds|Families get food by buying or growing it.
5.C|2|How can a person meet the need for clothing?|buy or wear clothes|plant a clock|eat a book|paint a rock|Clothes can be bought or made.
6.A|3|Which person has a job in the community and puts out fires?|firefighter|clown|painter of birthday signs|toy maker|Firefighters fight fires.
6.A|2|Which job is done at school?|teacher|pilot|astronaut|lifeguard|Teachers work at schools.
6.A|2|Which is a job a person might do at home?|cooking dinner|flying a plane|driving a bus|running a store|Cooking is a job at home.
6.B|3|Why do people have jobs?|to earn money for what they need|to avoid all food|to get lost|to forget school|Jobs earn money for needs.
6.B|2|A person works as a baker. What do they help others do?|get bread and treats|travel to space|build bridges|plant forests|A baker makes food.
7.A|2|Why do we have rules?|to keep us safe and fair|to make everyone sad|to make people lost|to hide toys|Rules help us stay safe.
7.A|3|Which is a good reason for a rule about walking in the hall?|to keep everyone safe|to make hallways loud|to knock things over|to run races|Walking keeps people from getting hurt.
7.B|2|Which rule keeps you safe at home?|Look both ways before crossing the street.|Throw toys on the stairs.|Put your hand in the fire.|Run in the kitchen.|Looking both ways is a safety rule.
7.B|2|Which rule helps order in the classroom?|Raise your hand to speak.|Shout across the room.|Take things without asking.|Leave trash on the floor.|Raising a hand gives everyone a turn.
8.A|3|Who is an authority figure at school?|principal|a cartoon dog|a baby doll|a pet fish|The principal is in charge at school.
8.A|2|Who is an authority figure in the community who helps keep people safe?|police officer|toy store clown|balloon seller|puppet|Police officers help keep order.
8.A|2|Who is an authority figure at home?|a parent|a teddy bear|a toy car|a pillow|Parents guide children at home.
8.B|3|How does a crossing guard help enforce rules?|helps people cross when it is safe|makes everyone go anywhere|breaks the rules|plays tag|Crossing guards keep people safe.
8.B|2|If a student breaks a classroom rule, what might the teacher do?|remind them of the rule|give them a rocket|buy them a pony|move the school|Teachers remind and guide.
9.A|2|Which flag has stars and stripes?|United States flag|Texas flag|a flag with a lone star only|a pirate flag|The U.S. flag has 50 stars and 13 stripes.
9.A|3|Which flag has one big star?|Texas flag|United States flag|a flag with 50 stars|a flag with no colors|The Texas flag has one star.
9.B|2|What do we say each day to show respect for our country's flag?|the Pledge of Allegiance|a bedtime lullaby|a happy birthday song|a lunch order|The pledge honors the flag.
9.B|2|When we say the Pledge of Allegiance, we usually...|stand and face the flag|do a cartwheel|hide under the desk|run outside|We show respect by standing.
9.C|3|Your class cannot decide between two games. What is a fair way to choose?|vote|yell|fight|leave|Voting lets everyone have a say.
9.C|2|When the class votes, which choice wins?|the one with the most votes|the one with the fewest votes|the one the teacher dislikes|the one no one picked|The most votes win.
10|2|Which is a way people can be different?|their favorite foods|they are all the same|they all have the same name|they all think the same thoughts|Likes can differ.
10|3|Which is a way people can be alike?|they all need food|they all have the same fingerprints|they all wear identical socks|they all speak every language|All people need food.
11.A|2|Which is a family tradition?|baking a special cake each birthday|forgetting a holiday|losing a shoe|sleeping in a car|Traditions are repeated customs.
11.A|2|Why are family traditions important?|they bring family together|they cause trouble|they stop people from talking|they make people sick|Traditions create bonds.
11.B|3|One family eats tamales at holidays. Another eats pie. This shows...|traditions can be different|everyone has the same tradition|no one has traditions|food is not needed|Families have different customs.
12.A|2|Which is technology used at school?|computer|pinecone|rock|leaf|Computers are technology.
12.A|2|Which is technology used at home?|telephone|tree|cloud|bird|A phone is a tool people made.
12.B|3|How does a phone help people?|they can talk to someone far away|it helps them grow tall|it makes them invisible|it teaches them to fly|Phones connect people.
12.B|2|How does a washing machine help families?|it cleans clothes|it cooks dinner|it plants flowers|it paints the wall|Machines save work.
12.C|2|Without electric lights, how might your evenings be different?|it would be darker|it would be brighter|it would be hotter|it would be louder|Lights make dark places bright.
13.A|3|Which is a fact?|The sun gives us light.|The sun is angry.|The sun is the best color.|The sun likes cake.|A fact can be shown to be true.
13.B|2|Which is a historical source that shows how people lived long ago?|an old photograph|a new cartoon|a cookie|a toy shop|Photos show the past.
13.B|2|A very old tool found in the ground is called a(n)...|artifact|cartoon|joke|lunchbox|Artifacts are objects from the past.
13.D|3|You put pictures of fruits in one group and pictures of animals in another. This is...|categorizing|erasing|hiding|spilling|Categorizing sorts things.
13.D|2|Which shows putting events in order?|first, next, last|blue, green, red|apple, shoe, cloud|up, down, left|Sequence shows order.
14.A|2|Which order is right for a plant growing?|seed, sprout, plant|plant, seed, sprout|sprout, plant, seed|plant, sprout, seed|A seed grows into a sprout and then a plant.
14.B|3|Which word tells what happens after today?|tomorrow|yesterday|before|first|Tomorrow is the next day.
14.B|2|Which word tells what happened the day before today?|yesterday|tomorrow|next|last|Yesterday is the day before.
14.B|2|Which word names the event that comes at the very start of a sequence?|first|last|next|after|First begins the list.
14.D|3|What does a map picture show?|where places are|what you ate|what you hear|how you feel|Maps show locations.
14.D|2|A picture of your classroom shows your desk next to the window. What does it tell you?|where things are|what time it is|what you will eat|who won a game|Pictures show places.
15.A|2|The class wants to pick a new classroom pet. How can they choose fairly?|take a vote|let one person decide without asking|toss the pets out|flip over the desk|Voting is democratic.
15.B|3|A student loses a library book. What is the first step in solving a problem?|find out what the problem is|ignore it|blame a friend|throw out all books|First, identify the problem.
15.B|2|After you list choices to fix a problem, what should you do next?|think about the good and bad of each|forget them|pick the choice with no thought|hide the list|Compare advantages and disadvantages.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'gk_ss.jsonl'))
print("saved", len(B.out), "questions")

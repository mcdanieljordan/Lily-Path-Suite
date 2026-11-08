#!/usr/bin/env python3
"""Grade 1 Science (TEKS 112.3.b) - original questions, content strands 6-13 (strands 1-5 are practices/themes, skipped).
   Run: python3 gen/g1_science.py  -> batches/g1_science.jsonl   Written by hand, 7 per standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.3.b.', 301, own='g1_science.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 6.A classify objects by shape, color, texture, larger/smaller, heavier/lighter
H('6.A', 2, "A student sorts buttons into a big group and a small group. What property is used?", "size", ["color", "texture", "smell"], "Big and small tell the size of the buttons.")
H('6.A', 2, "Which object is HEAVIER than a feather?", "a rock", ["a leaf", "a cotton ball", "a piece of paper"], "A rock has more weight than a feather.")
H('6.A', 3, "Objects are sorted into two groups: SMOOTH and BUMPY. Which property is used?", "texture", ["color", "shape", "size"], "Smooth and bumpy tell how objects feel.")
H('6.A', 2, "Which object is the LIGHTEST?", "a feather", ["a brick", "a book", "an apple"], "A feather weighs the least of these objects.")
H('6.A', 3, "Which group has objects that all have the same SHAPE?", "a ball, a globe, an orange", ["a ball, a box, a cone", "a book, a can, a ball", "a drum, a die, a marble"], "A ball, a globe, and an orange are all round like spheres.")
H('6.A', 3, "A student puts a red crayon, a red apple, and a red hat in one group. How were they sorted?", "by color", ["by shape", "by texture", "by weight"], "All three objects are red.")
H('6.A', 4, "Which object is LARGER than a marble but SMALLER than a basketball?", "a baseball", ["a grain of rice", "a beach ball", "a pea"], "A baseball is bigger than a marble and smaller than a basketball.")

# ---- 6.B changes caused by heating and cooling
H('6.B', 1, "What happens to an ice cube left in a warm room?", "it melts into water", ["it gets bigger and harder", "it turns into a rock", "it turns into sand"], "Heat makes ice melt into water.")
H('6.B', 2, "What happens to water placed in a freezer?", "it freezes into ice", ["it boils", "it turns into sand", "it gets warmer"], "Cooling makes water freeze into ice.")
H('6.B', 3, "A chocolate bar sits in a hot car. What will happen?", "it will melt", ["it will freeze", "it will grow", "it will turn into a rock"], "Heat makes chocolate melt.")
H('6.B', 3, "A puddle of water is left in the cold on a winter night. What may happen?", "it may freeze", ["it may boil", "it may burn", "it may turn into soil"], "Cold air can freeze water.")
H('6.B', 2, "What happens to butter in a hot pan?", "it melts", ["it freezes", "it turns blue", "it grows bigger"], "Heat makes butter melt.")
H('6.B', 3, "A popsicle drips on a sunny day. What caused the drips?", "heat from the Sun", ["cold from the Sun", "wind only", "the stick"], "Heat from the Sun melts the popsicle.")
H('6.B', 4, "Which object will stay a solid in a hot room for a long time?", "a metal spoon", ["an ice cube", "a chocolate chip", "a bar of butter"], "A metal spoon does not melt in an ordinary hot room.")

# ---- 6.C a whole object is a system made of organized parts
H('6.C', 2, "A toy car has wheels, a body, and an axle. What are these?", "parts of the toy", ["different toys", "tools for cooking", "kinds of weather"], "The wheels, body, and axle are parts that make up the toy.")
H('6.C', 3, "A student takes a toy apart and puts it back together. What does this show?", "an object is made of parts", ["toys cannot be fixed", "toys have no parts", "all toys are the same"], "A whole object is made of organized parts.")
H('6.C', 3, "A bicycle needs wheels, pedals, and a frame to work. What is a bicycle?", "a system of parts working together", ["a single piece", "a living thing", "a kind of weather"], "A bike works because its parts work together as a system.")
H('6.C', 2, "A flashlight has a case, a bulb, and batteries. What happens if the batteries are missing?", "the flashlight will not work", ["it will work better", "it will turn into a lamp", "it will float"], "Each part is needed for the whole flashlight to work.")
H('6.C', 3, "Which is a part of a chair?", "a leg", ["a petal", "a wing", "a fin"], "A chair has legs, a seat, and a back.")
H('6.C', 3, "A puzzle is made of many pieces. What happens if one piece is lost?", "the whole puzzle is not complete", ["the puzzle gets bigger", "nothing is different", "the pieces change color"], "A whole system needs all of its parts.")
H('6.C', 4, "A wagon has a handle, a body, and wheels. Which part helps it roll?", "the wheels", ["the handle", "the paint", "the sticker"], "Wheels let the wagon roll.")

# ---- 7.A pushes and pulls start, stop, or change speed/direction
H('7.A', 1, "A student kicks a ball. What force starts the ball moving?", "a push", ["a pull", "a shadow", "a sound"], "A kick pushes the ball so it starts to move.")
H('7.A', 2, "A student opens a drawer by taking the handle and bringing it toward them. What force is this?", "a pull", ["a push", "heat", "light"], "Moving the handle toward you is a pull.")
H('7.A', 3, "A goalie catches a rolling ball. What did the goalie do to the ball?", "stopped it", ["started it", "made it faster", "turned it into a toy"], "The goalie's hands stopped the ball's motion.")
H('7.A', 3, "A student hits a rolling ball with a bat and it moves the other way. What changed?", "the direction of the ball", ["the color of the ball", "the size of the ball", "the weight of the ball"], "The hit made the ball go a different direction.")
H('7.A', 2, "Which makes a swing go higher?", "a bigger push", ["a smaller push", "no push", "a shadow"], "A bigger push makes the swing move faster and higher.")
H('7.A', 3, "A cart is pushed gently, then pushed harder. What happens to the cart?", "it moves faster", ["it moves slower", "it stops", "it floats"], "A harder push makes the cart move faster.")
H('7.A', 4, "A student pulls a wagon forward. Which tells how the wagon's motion changed?", "it started moving", ["it got heavier", "it changed color", "it got louder"], "A pull started the wagon moving.")

# ---- 7.B investigation: predict how pushes and pulls change motion
H('7.B', 2, "A student predicts a ball will roll farther when pushed harder. What does the student need to test?", "push the ball softly and then hard", ["paint the ball", "weigh the ball", "hide the ball"], "To test the prediction, change only the strength of the push.")
H('7.B', 3, "A toy car rolls down a steep ramp and a low ramp. Which ramp makes the car go faster?", "the steep ramp", ["the low ramp", "they are the same", "neither ramp"], "A steeper ramp makes the car go faster.")
H('7.B', 3, "A student wants to see if a heavier ball needs a bigger push. What should the student compare?", "a light ball and a heavy ball", ["two blue balls", "two balls of the same weight", "a ball and a shadow"], "Comparing a light ball with a heavy ball tests the idea.")
H('7.B', 3, "A student pushes a toy car on a rug and on a smooth floor. On which does the car most likely go farther?", "the smooth floor", ["the rug", "they are the same", "neither one"], "A smooth floor lets objects roll farther than a rug.")
H('7.B', 2, "Before pushing a box, a student says, 'I think it will slide.' What is this?", "a prediction", ["a measurement", "a result", "a drawing"], "A prediction tells what you think will happen.")
H('7.B', 3, "A student records how far a car rolls after a soft push and a hard push. What is being measured?", "how far the car moves", ["the color of the car", "the sound of the car", "the age of the car"], "The distance traveled shows the effect of the push.")
H('7.B', 4, "A student pushes the same car with two different pushes. Which should stay the SAME to keep the test fair?", "the car and the floor", ["the strength of the push", "the distance the car goes", "the speed of the car"], "Only the push should change. The car and the floor stay the same.")

# ---- 8.A applications of heat in everyday life
H('8.A', 2, "Which uses heat?", "cooking soup on a stove", ["reading a book", "kicking a ball", "singing a song"], "A stove gives heat to cook food.")
H('8.A', 2, "A clothes dryer uses heat to do what?", "dry wet clothes", ["make clothes wet", "make clothes bigger", "change clothes' color"], "Heat in a dryer removes water from clothes.")
H('8.A', 3, "Which tool gives heat to a home in winter?", "a heater", ["a fan", "a refrigerator", "a freezer"], "A heater warms the air in a home.")
H('8.A', 3, "A toaster turns bread into toast. What does a toaster give to the bread?", "heat", ["cold", "water", "wind"], "A toaster heats the bread.")
H('8.A', 2, "Which is a source of heat for cooking?", "an oven", ["a refrigerator", "a freezer", "an ice maker"], "An oven makes heat that cooks food.")
H('8.A', 3, "Which job uses heat from the Sun?", "drying clothes on a line", ["making ice cubes", "chilling juice", "freezing a popsicle"], "The Sun's heat dries wet clothes on a line.")
H('8.A', 4, "A student wraps up in a blanket. How does the blanket help?", "it keeps body heat close", ["it makes the body colder", "it makes light", "it makes sound"], "A blanket holds in the heat from the body.")

# ---- 8.B reversible vs irreversible changes caused by heat
H('8.B', 2, "Which change can be turned back to what it was?", "ice melting into water", ["an egg being cooked", "a cake being baked", "bread becoming toast"], "Water can be frozen again to make ice.")
H('8.B', 2, "Which change can NOT be turned back?", "baking a cake", ["melting butter", "melting an ice cube", "melting a crayon"], "Once a cake is baked, it cannot be turned back into batter.")
H('8.B', 3, "Melted butter is placed in the refrigerator. What happens?", "it becomes solid again", ["it boils", "it disappears", "it turns into an egg"], "Cooling melted butter makes it solid again.")
H('8.B', 3, "A student cooks an egg. Can the egg be changed back to a raw egg?", "no, cooking changes it for good", ["yes, with ice", "yes, with water", "yes, with a magnet"], "Cooking an egg is a change that cannot be reversed.")
H('8.B', 3, "Which is a change that CAN be reversed?", "melting chocolate and letting it cool", ["burning a piece of paper", "toasting a marshmallow until black", "baking cookie dough"], "Melted chocolate becomes solid when it cools.")
H('8.B', 2, "A wax crayon melts in the sun. What can a student do to make it hard again?", "cool it", ["heat it more", "add water", "paint it"], "Cooling makes melted wax harden again.")
H('8.B', 4, "Which two changes both CANNOT be reversed?", "baking bread and cooking an egg", ["melting ice and melting butter", "freezing water and melting ice", "melting chocolate and freezing juice"], "Baking and cooking make new materials that cannot be changed back.")

# ---- 9 patterns of the seasons
H('9', 1, "How many seasons are in a year?", "four", ["two", "three", "six"], "The four seasons are spring, summer, fall, and winter.")
H('9', 2, "Which season comes after winter?", "spring", ["summer", "fall", "winter again"], "The order is spring, summer, fall, then winter.")
H('9', 2, "Which season comes after summer?", "fall", ["winter", "spring", "summer again"], "Fall comes after summer.")
H('9', 3, "Flowers bloom and baby animals are born. Which season is it?", "spring", ["fall", "winter", "summer"], "Many plants and animals begin growing in spring.")
H('9', 3, "Which list shows the seasons in order, starting with spring?", "spring, summer, fall, winter", ["spring, fall, summer, winter", "summer, spring, winter, fall", "winter, summer, spring, fall"], "The seasons repeat in the same order each year.")
H('9', 3, "Many trees lose their leaves. What happens to the days soon after?", "they get colder", ["they get hotter", "they stop", "they have no sun"], "After fall comes winter, when days are colder.")
H('9', 4, "It is winter now. What will the next season be?", "spring", ["fall", "summer", "winter"], "After winter, spring comes.")

# ---- 10.A soils: topsoil, clay, sand (particle size, shape, texture, color)
H('10.A', 2, "Which soil has tiny, loose grains that feel gritty?", "sand", ["clay", "topsoil", "mud"], "Sand has gritty grains that do not stick together.")
H('10.A', 3, "Which soil feels sticky when wet and can be shaped?", "clay", ["sand", "gravel", "pebbles"], "Clay feels sticky when wet and holds a shape.")
H('10.A', 3, "Which soil is dark and has bits of dead plants?", "topsoil", ["sand", "clay", "gravel"], "Topsoil is dark and has bits of dead plants that help plants grow.")
H('10.A', 2, "A student looks at soil with a hand lens. What can the student observe?", "tiny particles of different sizes", ["the whole Moon", "the wind", "a sound"], "A hand lens helps show small particles in soil.")
H('10.A', 3, "Which soil is best for growing most plants?", "topsoil", ["sand", "clay", "gravel"], "Topsoil has nutrients that plants need.")
H('10.A', 3, "A student rubs two soils between her fingers. One feels gritty and one feels smooth and sticky. Which has the larger particles?", "the gritty soil", ["the smooth, sticky soil", "they are the same", "neither has particles"], "Sand is gritty and has larger particles than clay.")
H('10.A', 4, "A student sorts soil into groups by color and texture. What is the student doing?", "classifying", ["measuring heat", "growing plants", "making wind"], "Sorting by properties is classifying.")

# ---- 10.B water moves rock and soil particles
H('10.B', 2, "What can rain do to loose soil on a hill?", "wash it away", ["make it grow", "turn it into rock", "turn it to ice"], "Moving water can wash soil downhill.")
H('10.B', 3, "A stream carries sand and pebbles downstream. What is the water doing?", "moving the particles", ["making the particles", "freezing the particles", "burning the particles"], "Flowing water moves particles from one place to another.")
H('10.B', 3, "After a heavy rain, muddy water runs down a slope. What does the mud show?", "water carried soil", ["wind made soil", "the Sun made soil", "rocks made water"], "Muddy water has soil moved by the rain.")
H('10.B', 3, "Where do rocks and sand end up when a river slows down?", "they are dropped on the bottom", ["they fly away", "they melt", "they turn into water"], "A slow river drops what it carries.")
H('10.B', 2, "Pouring water on a pile of sand makes the sand do what?", "move downhill", ["stay exactly the same", "turn red", "catch fire"], "Water moves sand from where it was.")
H('10.B', 3, "How could a student show that water moves soil?", "pour water on a pile of soil on a tray", ["blow on the soil", "look at the soil", "weigh the soil"], "Pouring water on soil shows how water moves particles.")
H('10.B', 4, "Which change is MOST likely after a flood?", "soil and rocks are moved to new places", ["rocks turn into plants", "soil turns into sand", "sand disappears forever"], "Floodwater carries soil and rocks to new places.")

# ---- 10.C compare bodies of water
H('10.C', 1, "Which body of water is the biggest?", "an ocean", ["a puddle", "a pond", "a stream"], "Oceans cover most of Earth and are the biggest.")
H('10.C', 2, "Which body of water is usually saltwater?", "an ocean", ["a pond", "a stream", "a puddle"], "Ocean water is salty.")
H('10.C', 3, "Which is a small, shallow pool of water left after it rains?", "a puddle", ["a lake", "an ocean", "a river"], "A puddle is a small pool after rain.")
H('10.C', 2, "Which body of water flows in a long line to a larger body of water?", "a river", ["a pond", "a puddle", "a lake"], "A river flows across land toward another body of water.")
H('10.C', 3, "Which is larger?", "a lake", ["a puddle", "a pond", "a stream"], "A lake is larger than a puddle, a pond, or a stream.")
H('10.C', 3, "A student finds water that is freshwater and very small, with plants growing in it. Which is it most likely?", "a pond", ["an ocean", "a puddle", "a river"], "A pond is a small body of freshwater.")
H('10.C', 4, "Which two bodies of water are both freshwater?", "a lake and a stream", ["an ocean and a lake", "an ocean and a stream", "an ocean and a puddle"], "Lakes and streams are usually freshwater. Oceans are saltwater.")

# ---- 10.D weather characteristics and daily choices
H('10.D', 2, "What can you wear on a rainy day?", "a raincoat", ["sunglasses only", "a swimsuit", "sandals"], "A raincoat keeps you dry.")
H('10.D', 2, "Which weather word means the sky has many clouds?", "cloudy", ["clear", "calm", "hot"], "Cloudy means many clouds cover the sky.")
H('10.D', 3, "A student sees a flag flapping hard. What does this show about the weather?", "it is windy", ["it is calm", "it is icy", "it is foggy"], "A flapping flag shows strong wind.")
H('10.D', 3, "The ground is icy. Which choice is best?", "walk carefully in boots", ["run fast in sandals", "wear a swimsuit", "skate on the sidewalk"], "Icy ground is slippery, so boots and careful steps help.")
H('10.D', 2, "Which weather is hot?", "a summer afternoon in the sun", ["a snowy morning", "an icy night", "a cold winter day"], "Hot weather happens on a sunny summer afternoon.")
H('10.D', 3, "Which tool tells how hot or cold it is?", "a thermometer", ["a ruler", "a scale", "a magnet"], "A thermometer measures temperature.")
H('10.D', 4, "A student plans a picnic. The weather report says rain all day. What is the best choice?", "have the picnic another day", ["go anyway with no coat", "wear sandals", "bring a kite"], "Weather affects what people decide to do.")

# ---- 11.A how plants, animals, humans use rocks, soil, water
H('11.A', 2, "How do plants use water?", "they take it in through their roots", ["they drink it with a straw", "they ride on it", "they turn it to ice"], "Plants take in water through their roots.")
H('11.A', 2, "How do many animals use soil?", "they dig homes in it", ["they eat the Sun", "they make shadows", "they paint with it only"], "Some animals dig burrows in soil.")
H('11.A', 3, "How do people use rocks?", "to build houses and roads", ["to make wind", "to make rain", "to grow wings"], "People use rocks and stone for building.")
H('11.A', 3, "How do animals use water?", "to drink", ["to fly", "to make light", "to build roads"], "Animals need to drink water.")
H('11.A', 2, "A bird drinks from a stream. What does the bird use?", "water", ["rock", "soil", "sand"], "The bird gets a drink from the water.")
H('11.A', 3, "Ants live under the ground. What do they use for their homes?", "soil", ["water", "clouds", "wind"], "Ants dig tunnels in soil.")
H('11.A', 4, "Which uses rock, soil, and water together?", "a garden with a stone path", ["a pencil", "a book", "a spoon"], "A garden uses soil and water, and a stone path uses rock.")

# ---- 11.B why water conservation is important
H('11.B', 2, "Why is it important to save water?", "there is only so much fresh water", ["water is a toy", "water never gets used", "water makes shadows"], "Fresh water is limited, so we should use it carefully.")
H('11.B', 3, "What happens if people waste water?", "there may not be enough later", ["there will be more", "water will turn to soil", "nothing ever changes"], "Wasting water can leave less for later.")
H('11.B', 2, "Who needs clean water?", "plants, animals, and people", ["only people", "only plants", "only fish"], "All living things need water.")
H('11.B', 3, "Which shows a good reason to conserve water?", "so there is enough for everyone", ["so puddles are bigger", "so rocks are wet", "so clouds are gray"], "Saving water helps make sure everyone has enough.")
H('11.B', 3, "A city has a dry summer. Why should people use less water?", "water in lakes and rivers may run low", ["water turns to sand", "clouds make more rain", "water gets heavier"], "A dry summer can lower water supplies.")
H("11.B", 4, "Which sentence about clean water is true?", "clean water is needed to stay healthy", ["clean water is never needed", "only fish use water", "water is endless everywhere"], "People need clean water to drink and stay healthy.")
H('11.B', 2, "What does conserve mean?", "to save and use carefully", ["to throw away", "to spill", "to make louder"], "To conserve means to save and use carefully.")

# ---- 11.C ways to conserve and protect water
H('11.C', 1, "Which action saves water?", "turn off the faucet while brushing your teeth", ["leave the faucet running", "fill the sink and let it overflow", "play in the sprinkler all day"], "Turning off the faucet stops water from being wasted.")
H('11.C', 2, "Which action keeps a pond clean?", "put trash in a trash can", ["throw trash in the pond", "pour paint in the pond", "dump oil in the pond"], "Keeping trash out of water protects it.")
H('11.C', 3, "Which is a way to use less water?", "take a short shower", ["leave the shower on", "wash a car for hours", "let a hose run all day"], "A short shower uses less water.")
H('11.C', 3, "A faucet is dripping. What should be done?", "tell a grown-up so it can be fixed", ["leave it", "turn it on more", "collect the drips and spill them out"], "A dripping faucet wastes water until it is fixed.")
H('11.C', 2, "What should you do with litter near a stream?", "pick it up and throw it in a trash can", ["throw it in the stream", "bury it in the water", "leave it near the water"], "Litter near a stream can wash in, so it should be put in a trash can.")
H('11.C', 3, "Which is the best way to water a garden without wasting water?", "water early in the morning", ["water at noon in the heat", "water the sidewalk", "leave the hose on all night"], "Watering in the morning means less water dries up.")
H('11.C', 4, "Which action protects lakes and rivers?", "keeping chemicals and trash out of the water", ["pouring soap in the water", "leaving litter by the shore", "dumping oil down a drain"], "Clean water stays clean when pollution is kept out.")

# ---- 12.A classify living and nonliving
H('12.A', 1, "Which is a living thing?", "a tree", ["a rock", "a chair", "a ball"], "A tree needs water and food, grows, and makes new trees.")
H('12.A', 2, "Which is nonliving?", "a rock", ["a bird", "a fish", "a flower"], "A rock does not eat, grow, or have young.")
H('12.A', 3, "Which needs food, water, and air to live?", "a puppy", ["a toy car", "a pencil", "a stone"], "A puppy is a living thing that has basic needs.")
H('12.A', 3, "A butterfly lays eggs. What does this show?", "it is living", ["it is nonliving", "it is a rock", "it is a toy"], "Living things make young.")
H('12.A', 2, "Which does NOT grow or make young?", "a toy robot", ["a plant", "a dog", "a fish"], "A toy robot is nonliving.")
H('12.A', 3, "Which list has only living things?", "a frog, a tree, a bird", ["a frog, a rock, a bird", "a tree, a book, a bird", "a rock, a ball, a tree"], "A frog, a tree, and a bird are all living.")
H('12.A', 4, "A student sees a seed. Is it living?", "yes, it can grow into a plant", ["no, it is a rock", "no, it is a toy", "no, it can never grow"], "A seed is alive and can grow into a plant.")

# ---- 12.B terrariums and aquariums: living and nonliving interactions
H('12.B', 2, "A terrarium has plants, soil, and a lid. Which is nonliving?", "the soil", ["the plant", "a worm", "a bean sprout"], "Soil is a nonliving part of a terrarium.")
H('12.B', 3, "In an aquarium, fish need water. What does this show?", "living things depend on nonliving things", ["fish do not need anything", "water is alive", "water is a fish"], "Fish depend on water, which is nonliving.")
H('12.B', 3, "A plant in a terrarium gets light through the glass. What does the plant need the light for?", "to make food", ["to make shadows only", "to make sound", "to dig"], "Plants use light to make food.")
H('12.B', 2, "Which is a living thing in an aquarium?", "a snail", ["gravel", "water", "a plastic castle"], "A snail is alive. Gravel, water, and a plastic castle are not.")
H('12.B', 3, "A student sprays a terrarium with water. Why?", "the plants need water", ["to make it smell", "to make it cold", "to make it loud"], "Plants need water to live.")
H('12.B', 3, "In a classroom aquarium, what happens if the water gets very dirty?", "the fish can get sick", ["the fish grow faster", "the fish turn into plants", "nothing happens"], "Living things need clean water.")
H('12.B', 4, "Which pair shows a living thing depending on a nonliving thing?", "a fish and water", ["a fish and a frog", "a plant and a worm", "a snail and a fish"], "The fish needs water, a nonliving thing.")

# ---- 12.C food chains
H('12.C', 2, "What do most plants use to make their own food?", "sunlight", ["fish", "rocks", "metal"], "Plants use light from the Sun to make food.")
H('12.C', 3, "A rabbit eats grass. What does the rabbit get from the grass?", "food energy", ["a shadow", "a magnet", "rain"], "The rabbit gets energy from eating the grass.")
H('12.C', 3, "A hawk eats a mouse and a mouse eats seeds. Which shows the food chain in order?", "seed, mouse, hawk", ["hawk, mouse, seed", "mouse, hawk, seed", "seed, hawk, mouse"], "The arrows point to what eats the food: seed to mouse to hawk.")
H('12.C', 3, "Which animal eats other animals?", "a hawk", ["a rabbit", "a cow", "a deer"], "A hawk eats mice and other small animals.")
H('12.C', 2, "Which is the first link in most food chains?", "a plant", ["a hawk", "a frog", "a snake"], "Plants make food, so most food chains start with a plant.")
H('12.C', 3, "A frog eats a fly. What would happen to the frog if there were no flies?", "it would have less food", ["it would have more food", "it would grow wings", "nothing would change"], "Animals depend on what they eat.")
H('12.C', 4, "A cricket eats plants. A bird eats the cricket. Which does the bird depend on for food?", "the small insect", ["the rain only", "the soil only", "the wind"], "The bird gets its food from the cricket, which is a small insect.")

# ---- 13.A external structures of animals
H('13.A', 2, "A bird has wings. What can wings help many birds do?", "fly", ["swim like a fish", "dig tunnels", "climb walls"], "Wings help most birds fly.")
H('13.A', 3, "A fish has fins and gills. What do fins help it do?", "swim", ["fly", "run", "dig"], "Fins help fish move in water.")
H('13.A', 2, "Which animal has fur that keeps it warm?", "a bear", ["a fish", "a frog", "a snake"], "Fur keeps a bear warm.")
H('13.A', 3, "A duck has webbed feet. What do they help it do?", "swim", ["fly high", "climb trees", "dig holes"], "Webbed feet push water to help a duck swim.")
H('13.A', 3, "A turtle has a hard shell. What does the shell help it do?", "stay safe", ["fly", "swim fast", "see in the dark"], "A shell protects a turtle.")
H('13.A', 2, "Which animal has a long neck that helps it reach leaves in tall trees?", "a giraffe", ["a rabbit", "a mouse", "a frog"], "A giraffe's long neck helps it reach high leaves.")
H('13.A', 4, "Why does a woodpecker have a strong, pointed beak?", "to peck into trees for food", ["to swim", "to run fast", "to make a nest of mud"], "A woodpecker's beak is used to peck wood for insects.")

# ---- 13.B life cycles: bird, mammal, fish
H('13.B', 2, "A bird starts its life inside what?", "an egg", ["a seed", "a cocoon", "a pod"], "Birds hatch from eggs.")
H('13.B', 3, "Which order shows a bird's life cycle?", "egg, chick, adult bird", ["adult bird, egg, chick", "chick, egg, adult bird", "egg, adult bird, chick"], "A bird hatches from an egg as a chick, then grows into an adult.")
H('13.B', 2, "Which is a mammal?", "a dog", ["a fish", "a frog", "a bird"], "A dog is a mammal.")
H('13.B', 3, "How do baby mammals get their first food?", "they drink milk from their mother", ["they catch fish", "they eat seeds", "they dig for roots"], "Mammal mothers feed their babies milk.")
H('13.B', 3, "A fish starts as an egg and hatches into a tiny fish. What comes next?", "it grows into an adult fish", ["it turns into a bird", "it becomes an egg again", "it grows legs and walks"], "A young fish grows into an adult fish.")
H('13.B', 2, "A puppy grows up to be what?", "a dog", ["a cat", "a bird", "a fish"], "A puppy grows into an adult dog.")
H('13.B', 4, "Which animal does NOT start life inside an egg?", "a horse", ["a robin", "a trout", "a duck"], "A horse is a mammal and the baby grows inside the mother.")

# ---- 13.C young animals resemble their parents
H('13.C', 2, "A kitten looks most like which animal?", "a grown cat", ["a grown dog", "a grown fish", "a grown frog"], "Young animals look like their parents.")
H('13.C', 2, "A baby duck has feathers, a beak, and webbed feet like its parents. What does this show?", "young animals look like their parents", ["all animals look the same", "ducks do not grow", "ducks are plants"], "Young animals resemble their parents.")
H('13.C', 3, "A calf is a young cow. What does the calf have like its parents?", "four legs and a tail", ["wings and feathers", "fins and gills", "a shell"], "A calf looks like a small cow.")
H('13.C', 3, "A puppy has ears and a tail like its mother. Which is the same?", "the body parts", ["the age", "the size", "the weight"], "The puppy has the same kinds of body parts as its mother.")
H('13.C', 3, "A chick looks small. How is it like its parents?", "it has feathers and a beak", ["it has fins", "it has fur", "it has a shell"], "A chick has feathers and a beak like adult chickens.")
H('13.C', 2, "A baby giraffe looks like which animal?", "an adult giraffe", ["an elephant", "a zebra", "a lion"], "A baby giraffe looks like an adult giraffe.")
H('13.C', 4, "A student finds a baby animal with spots. The mother also has spots. What can the student say?", "young animals can look like their parents", ["spots are rocks", "all animals have spots", "young animals never look like parents"], "The baby and mother share the same pattern.")

B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g1_science.jsonl'))
print("saved", len(B.out), "questions")

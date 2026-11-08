#!/usr/bin/env python3
"""Grade 2 Science (TEKS 112.4.b) - original questions, content strands 6-13 (strands 1-5 are practices/themes, skipped).
   Run: python3 gen/g2_science.py  -> batches/g2_science.jsonl   Written by hand, 7 per standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.4.b.', 401, own='g2_science.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 6.A classify matter: texture, flexibility, relative temperature, solid or liquid
H('6.A', 2, "Which of these is a LIQUID?", "orange juice", ["a brick", "a pencil", "a wooden block"], "Juice flows and takes the shape of its container, so it is a liquid.")
H('6.A', 2, "Which of these is a SOLID?", "a rubber ball", ["milk", "rain", "soda"], "A ball keeps its own shape, so it is a solid.")
H('6.A', 3, "A rubber band can bend and stretch without breaking. What property does it have?", "flexible", ["rigid", "gritty", "frozen"], "Flexible means it can bend easily.")
H('6.A', 3, "Which object is NOT flexible?", "a glass jar", ["a rubber band", "a wet noodle", "a piece of yarn"], "A glass jar is stiff and does not bend.")
H('6.A', 2, "A cup of hot cocoa and a glass of ice water are compared. What property is different?", "temperature", ["texture", "shape of the cup", "color of the cup"], "Hot and cold tell the temperature of each drink.")
H('6.A', 3, "Which group has only liquids?", "water, milk, juice", ["water, rock, juice", "milk, wood, juice", "juice, ice cube, sand"], "Water, milk, and juice all flow.")
H('6.A', 4, "A student sorts materials into groups called ROUGH and SMOOTH. Which property is used?", "texture", ["flexibility", "temperature", "state of matter"], "Rough and smooth describe how a surface feels.")

# ---- 6.B physical properties changed by cutting, folding, sanding, melting, freezing
H('6.B', 2, "A student folds a flat sheet of paper into a boat. What property changed?", "its shape", ["its material", "its temperature", "its weight a lot"], "Folding changes the shape but the paper is still paper.")
H('6.B', 2, "A student cuts a sheet of paper into small pieces. What stayed the same?", "the material", ["the shape", "the size", "the number of pieces"], "The pieces are still paper.")
H('6.B', 3, "A student sands a rough block of wood. How does the block feel after?", "smoother", ["rougher", "colder", "wetter"], "Sanding makes a surface smoother.")
H('6.B', 3, "Juice is poured into a mold and placed in a freezer. What does it become?", "a solid", ["a gas", "a different liquid", "a new kind of juice that is hotter"], "Freezing makes a liquid turn into a solid.")
H('6.B', 3, "A crayon is held near a flame and gets soft and runny. Which process caused this?", "melting", ["freezing", "cutting", "folding"], "Heat makes wax melt.")
H('6.B', 2, "A student wants to make a piece of clay flat. What can the student do?", "press it", ["freeze it", "paint it", "weigh it"], "Pressing changes the clay's shape.")
H('6.B', 4, "A student tears a paper, folds it, then cuts it. Which is still true about the pieces?", "they are still paper", ["they are now cloth", "they are now metal", "they are now liquid"], "Cutting, folding, and tearing change shape or size, not the material.")

# ---- 6.C small units combined to form new objects; choose materials by properties
H('6.C', 2, "Building blocks can be put together to make what?", "many different objects", ["only one object", "a kind of weather", "a living thing"], "Small units can be combined in many ways to make new objects.")
H('6.C', 3, "A student takes apart a block tower and builds a bridge with the same blocks. What does this show?", "blocks can be reassembled", ["blocks are alive", "blocks melt", "blocks cannot change"], "Small units can be reassembled into new objects.")
H('6.C', 3, "Which material is best for building a bridge that holds weight?", "strong wood", ["tissue paper", "cotton balls", "soft sponge"], "A bridge needs a strong, stiff material.")
H('6.C', 3, "Why is a raincoat made of waterproof plastic?", "water cannot pass through it", ["it is very heavy", "it tastes good", "it makes noise"], "The material is chosen because water does not go through it.")
H('6.C', 2, "Which material is best for a soft pillow?", "fluffy cotton", ["metal", "stone", "glass"], "Cotton is soft and comfortable.")
H('6.C', 3, "A toy boat needs to float. Which material is best?", "foam", ["a stone", "a metal bolt", "a heavy brick"], "Foam is light and floats on water.")
H('6.C', 4, "A student builds a tall tower with blocks. Which choice would help make it stronger?", "use a wide base of blocks", ["use a tiny base", "use only one block at the bottom", "make it lean to one side"], "A wide base makes a tower more stable.")

# ---- 7.A objects push on each other and may change shape when they touch or collide
H('7.A', 2, "A ball hits a wall. What does the wall do to the ball?", "pushes back on it", ["pulls it closer", "turns it to ice", "makes it lighter"], "When objects touch, they push on each other.")
H('7.A', 3, "A student presses a sponge with a hand. What happens to the sponge?", "it changes shape", ["it changes color", "it turns into water", "it floats away"], "A push can change an object's shape.")
H('7.A', 3, "Two bumper cars hit each other. What happens?", "they push on each other and move", ["they melt", "they disappear", "they become one car"], "Colliding objects push on each other.")
H('7.A', 2, "A soft clay ball is dropped on the floor. What may happen to the ball?", "it may flatten", ["it may glow", "it may melt", "it may float"], "The push from the floor can change the clay's shape.")
H('7.A', 3, "A hammer hits a nail. Which describes the push?", "the hammer pushes the nail and the nail pushes back", ["only the nail pushes", "nothing pushes", "the hammer pulls the nail"], "When objects touch, each pushes on the other.")
H('7.A', 3, "A student squeezes a rubber ball. What happens when the student lets go?", "it goes back to its shape", ["it stays flat forever", "it turns to metal", "it becomes lighter"], "A rubber ball can spring back after being squeezed.")
H('7.A', 4, "Which collision is most likely to change an object's shape?", "a truck crashing into a soft sandcastle", ["a feather landing on a rock", "a leaf landing on a pillow", "a bubble touching a wall"], "A strong collision with a soft object changes its shape.")

# ---- 7.B strength of a push or pull changes motion
H('7.B', 2, "A stronger push on a toy car makes the car move how?", "faster", ["slower", "not at all", "backward"], "A stronger push makes the car move faster.")
H('7.B', 3, "A student pushes a ball gently and then pushes it hard. How does the motion change?", "the hard push makes it go farther", ["the gentle push makes it go farther", "both go the same", "neither moves"], "A harder push makes it travel farther.")
H('7.B', 3, "A student pulls a wagon with a weak pull and a strong pull. Which makes the wagon speed up more?", "the strong pull", ["the weak pull", "they are the same", "neither"], "A stronger pull changes the motion more.")
H('7.B', 3, "A student wants to test how push strength affects a car. What should change in the test?", "how hard the car is pushed", ["the color of the car", "the name of the car", "the time of day"], "To test the push, only the strength of the push should change.")
H('7.B', 2, "A student measures how far a ball rolls after a soft push. What tool measures the distance?", "a ruler or measuring tape", ["a thermometer", "a clock", "a scale"], "A measuring tape measures length.")
H('7.B', 3, "A swing is pushed lightly and then pushed hard. Which swing goes higher?", "the one pushed hard", ["the one pushed lightly", "both go the same", "neither swing moves"], "A harder push makes a swing go higher.")
H('7.B', 4, "A student records: soft push = 20 cm, medium push = 45 cm, hard push = 80 cm. What does the data show?", "a stronger push makes the object travel farther", ["a softer push goes farther", "all pushes go the same", "the object never moves"], "As the push gets stronger, the distance gets longer.")

# ---- 8.A sound is made by vibrations
H('8.A', 2, "What makes sound?", "vibrating matter", ["still air only", "darkness", "bright light"], "Sound is made when matter vibrates, or moves back and forth quickly.")
H('8.A', 2, "A student plucks a rubber band and it moves quickly back and forth. What does the student hear?", "a sound", ["nothing at all", "a smell", "a color"], "The vibrating rubber band makes sound.")
H('8.A', 3, "A drum is hit and rice on top of the drum jumps. What does the rice show?", "the drum is vibrating", ["the drum is cold", "the drum is melting", "the drum is quiet"], "The jumping rice shows the drum skin vibrates.")
H('8.A', 3, "A student puts a hand on their throat while humming. What does the hand feel?", "vibrations", ["heat only", "wind", "a magnet"], "The vocal cords vibrate when a person hums.")
H('8.A', 2, "When a tuning fork stops vibrating, what happens to its sound?", "the sound stops", ["the sound gets louder", "the sound turns to light", "the sound turns to heat"], "No vibration means no sound.")
H('8.A', 3, "Which can cause vibrations that make sound?", "hitting, plucking, or blowing", ["staying very still", "being in the dark", "being frozen only"], "Many actions cause vibrations.")
H('8.A', 4, "A loud sound can make a window rattle. What does this show?", "sound can cause other things to vibrate", ["sound is a liquid", "sound is a color", "sound is always quiet"], "Vibrations from sound can make other objects vibrate.")

# ---- 8.B levels of sound used in everyday life
H('8.B', 2, "Which sound is the QUIETEST?", "a whisper", ["a fire alarm", "a siren", "a drum"], "A whisper is a very soft sound.")
H('8.B', 2, "Why does a fire alarm make a very loud sound?", "to warn people quickly", ["to put people to sleep", "to play music", "to be heard by no one"], "A loud alarm gets people's attention.")
H('8.B', 3, "A teacher uses a soft voice in the library. Why?", "so others can read quietly", ["to be louder", "to scare people", "to make music"], "Soft sounds help keep a place quiet.")
H('8.B', 3, "Which place needs a quiet sound level?", "a library", ["a football game", "a parade", "a concert"], "A library is a place for quiet reading.")
H('8.B', 2, "Which sound is LOUD?", "a thunderclap", ["a mouse squeak", "a soft whisper", "a falling feather"], "Thunder is a very loud sound.")
H('8.B', 3, "A bus driver honks a horn to warn a car. Why is the horn loud?", "so the other driver can hear it", ["so the bus runs faster", "so the road is clean", "so the car turns red"], "A loud horn is meant to be heard quickly.")
H('8.B', 4, "Which is the BEST sound level for a doctor speaking to a patient in a quiet room?", "a soft, clear voice", ["a screaming voice", "a siren", "a drum"], "A calm, soft voice is best for talking in a quiet room.")

# ---- 8.C device that uses sound to communicate over a distance
H('8.C', 2, "Two cups and a string can be used to make a simple device. What can it help people do?", "talk over a short distance", ["see in the dark", "stay warm", "grow plants"], "A string telephone carries vibrations from one cup to the other.")
H('8.C', 3, "In a cup-and-string phone, what carries the sound from one cup to the other?", "vibrations along the string", ["light along the string", "heat along the string", "water in the string"], "The string vibrates and carries the sound.")
H('8.C', 3, "For a cup-and-string phone to work well, the string should be what?", "tight", ["loose and slack", "tied in knots", "cut in half"], "A tight string carries vibrations better.")
H('8.C', 2, "Which tool helps a person call to others across a field?", "a megaphone", ["a lamp", "a compass", "a thermometer"], "A megaphone makes a voice louder so it travels farther.")
H('8.C', 3, "A student builds a sound device and it is too quiet. What can be changed?", "make the string tighter", ["paint the cups", "use a heavier box", "put it in a freezer"], "A tighter string helps vibrations travel.")
H('8.C', 3, "Which problem can a sound device help solve?", "talking to a friend across a playground", ["lighting a dark room", "staying cool", "growing a plant"], "Sound devices help people communicate over a distance.")
H('8.C', 4, "A student's cup-and-string phone does not work. The string is touching a pole. What is the likely problem?", "the string is not able to vibrate freely", ["the cups are too clean", "the string is too short to hear", "the room is too bright"], "A string touching something cannot vibrate well.")

# ---- 9.A Sun is a star; Moon reflects the Sun's light
H('9.A', 2, "The Sun is what kind of object?", "a star", ["a planet", "a moon", "a cloud"], "The Sun is a star that gives off light and heat.")
H('9.A', 2, "What does the Sun give to Earth?", "light and heat", ["only sound", "only wind", "only rain"], "The Sun provides light and heat.")
H('9.A', 3, "Why can we see the Moon at night?", "it reflects light from the Sun", ["it makes its own light", "it is a lamp", "it is a star"], "The Moon reflects the Sun's light.")
H('9.A', 3, "Which sky object produces its own light?", "the Sun", ["the Moon", "a planet", "a mirror"], "The Sun is a star that makes its own light.")
H('9.A', 2, "Which is closest to Earth?", "the Moon", ["the Sun", "a faraway star", "all are the same distance"], "The Moon is much closer to Earth than the Sun or other stars.")
H('9.A', 3, "A mirror reflects a flashlight's light onto a wall. Which sky object works like the mirror?", "the Moon", ["the Sun", "a star", "a cloud of smoke"], "The Moon reflects sunlight like a mirror.")
H('9.A', 4, "The Sun looks much bigger than other stars at night. Why?", "it is much closer to Earth", ["it is the only star", "it is a planet", "it is a cloud"], "The Sun is a star that is very close compared to other stars.")

# ---- 9.B observing sky objects with tools
H('9.B', 2, "Which tool helps you see faraway objects in the sky?", "a telescope", ["a ruler", "a thermometer", "a scale"], "A telescope makes faraway things look closer.")
H('9.B', 3, "Compared with eyes alone, a telescope makes the Moon look how?", "bigger and with more detail", ["smaller", "darker", "the same"], "A telescope shows more detail.")
H('9.B', 3, "Why do stars look like tiny dots without a tool?", "they are very far away", ["they are very small and close", "they are made of ice", "they are inside clouds"], "Stars are so far away that they look like tiny points.")
H('9.B', 3, "A student sees craters on the Moon using a tool. Which tool was used?", "a telescope", ["a thermometer", "a compass", "a flashlight"], "Craters are easy to see with a telescope.")
H('9.B', 2, "Which should you NEVER look at directly, even with a tool, unless you have special protection?", "the Sun", ["the Moon", "a cloud", "the grass"], "Looking at the Sun can hurt your eyes.")
H('9.B', 3, "Binoculars help you see the night sky how?", "objects look closer and brighter", ["objects look farther away", "objects disappear", "objects change color to blue"], "Binoculars gather light and magnify.")
H('9.B', 4, "A student draws the Moon as seen by eyes alone and by telescope. What would be different?", "the telescope drawing has more detail", ["the eye drawing has more detail", "the drawings are the same", "the telescope drawing shows no Moon"], "A telescope reveals more details.")

# ---- 10.A wind and water move soil and rock particles
H('10.A', 2, "What can wind do to sand on a beach?", "blow it into dunes", ["freeze it", "turn it to rock", "make it glow"], "Wind can pile up sand into dunes.")
H('10.A', 2, "What can a river do to rocks?", "carry them downstream", ["turn them into soil", "melt them", "make them float up"], "Moving water carries rocks and sand.")
H('10.A', 3, "After a storm, a pile of dirt at the bottom of a hill is bigger. What most likely moved the dirt?", "rain water", ["a magnet", "sunlight", "a shadow"], "Water can wash soil downhill.")
H('10.A', 3, "Which landform can be made by wind blowing sand?", "a dune", ["a river", "a lake", "an ocean"], "Wind blowing sand can build dunes.")
H('10.A', 3, "Strong wind in a dry place can move what?", "dust and sand", ["large mountains", "whole forests in a day", "ocean water into the sky"], "Wind can carry small, light particles.")
H('10.A', 2, "A fast river carries more rocks than a slow river. Why?", "faster water has more force", ["slow water is heavier", "fast water is colder", "slow water is deeper"], "Faster water can move larger and more particles.")
H('10.A', 4, "Which two things move soil and rock from one place to another?", "wind and water", ["light and heat", "sound and shadows", "magnets and ice"], "Wind and water both carry particles to new places.")

# ---- 10.B measure, record, graph weather information
H('10.B', 2, "Which tool measures temperature?", "a thermometer", ["a rain gauge", "a windsock", "a ruler"], "A thermometer measures how hot or cold the air is.")
H('10.B', 2, "Which tool measures how much rain falls?", "a rain gauge", ["a thermometer", "a compass", "a scale"], "A rain gauge collects and measures rainfall.")
H('10.B', 3, "A bar graph shows rain each day: Mon 2 cm, Tue 0 cm, Wed 5 cm. Which day was the rainiest?", "Wednesday", ["Monday", "Tuesday", "they were the same"], "Wednesday had the tallest bar, 5 cm.")
H('10.B', 3, "A student records the temperature every day at noon for a week. Why?", "to find patterns in the weather", ["to hide the weather", "to stop the rain", "to make the Sun brighter"], "Recording data over time shows patterns.")
H('10.B', 3, "A thermometer shows 90°F. What kind of day is it?", "a hot day", ["a freezing day", "a snowy day", "a very cold day"], "90°F is hot weather.")
H('10.B', 3, "Precipitation includes which of these?", "rain and snow", ["wind and clouds", "heat and cold", "day and night"], "Rain, snow, sleet, and hail are precipitation.")
H('10.B', 4, "Temperatures for four days are 70, 72, 75, 78. What pattern do you see?", "it is getting warmer", ["it is getting colder", "it stays the same", "it goes up and down"], "Each day is a little warmer.")

# ---- 10.C severe weather events
H('10.C', 2, "Which severe weather event has a spinning funnel of wind?", "a tornado", ["a flood", "a drought", "a snowfall"], "A tornado is a spinning funnel of strong wind.")
H('10.C', 3, "A hurricane forms over what?", "warm ocean water", ["cold mountain tops", "dry deserts", "frozen lakes"], "Hurricanes form over warm ocean water.")
H('10.C', 2, "What is a flood?", "too much water covering dry land", ["too little rain", "a very strong wind only", "a layer of snow"], "A flood happens when water covers land that is usually dry.")
H('10.C', 3, "Which place is MORE likely to have hurricanes?", "a coast near a warm ocean", ["the middle of a desert", "a high mountaintop", "an inland dry field"], "Hurricanes happen near warm ocean coasts.")
H('10.C', 3, "A severe storm warning is announced. What should people do?", "go to a safe place", ["go outside to watch", "play near a river", "ignore it"], "Staying safe during severe weather is the best choice.")
H('10.C', 3, "Which severe weather is MORE likely in a very cold place?", "a blizzard", ["a hurricane", "a heat wave", "a tropical storm"], "Blizzards happen where it is very cold and snowy.")
H('10.C', 4, "Some severe weather happens more in some places than others. Why?", "different places have different climates", ["the weather picks a place at random", "all places are the same", "clouds choose where to go"], "Climate and geography affect the kinds of storms in a region.")

# ---- 11.A natural vs manmade resources
H('11.A', 2, "Which is a natural resource?", "water", ["a plastic toy", "a brick wall", "a metal car"], "Water comes from nature.")
H('11.A', 2, "Which is MANMADE?", "a plastic bottle", ["a tree", "a river", "a rock"], "People make plastic bottles.")
H('11.A', 3, "A wooden table is made from what natural resource?", "trees", ["metal", "plastic", "glass"], "Wood comes from trees.")
H('11.A', 3, "Which group has only natural resources?", "air, water, sunlight", ["air, plastic, glass", "water, steel, paper", "soil, nails, toys"], "Air, water, and sunlight come from nature.")
H('11.A', 3, "Paper is made from what?", "trees", ["rocks", "sand", "water only"], "Paper comes from wood pulp from trees.")
H('11.A', 2, "Which is a manmade object?", "a bicycle", ["a feather", "a pinecone", "a seashell"], "A bicycle is made by people.")
H('11.A', 4, "Glass is made by melting a natural material found on beaches. Which natural resource is it?", "sand", ["plastic", "steel", "paper"], "Sand comes from nature, and people melt it to make glass.")

# ---- 11.B limit human impact: reduce, reuse, recycle, dispose properly
H('11.B', 1, "Which is a way to REUSE something?", "use an old jar to hold pencils", ["throw the jar in a stream", "break the jar", "bury the jar"], "Reusing means using something again.")
H('11.B', 2, "Which is a way to RECYCLE?", "put a plastic bottle in a recycling bin", ["throw it on the ground", "burn it", "leave it in a stream"], "Recycling means turning used materials into new things.")
H('11.B', 3, "Which choice helps REDUCE trash?", "bring a reusable water bottle", ["buy a new plastic bottle every day", "throw away full bottles", "use many paper cups"], "Using a reusable bottle makes less trash.")
H('11.B', 3, "Where should a used soda can go?", "in a recycling bin", ["on the street", "in a stream", "under a bush"], "Metal cans can be recycled.")
H('11.B', 3, "Why is it good to recycle paper?", "it saves trees", ["it makes more trash", "it hurts animals", "it wastes water"], "Recycling paper means fewer trees are cut down.")
H('11.B', 2, "A student uses both sides of a piece of paper. What is this?", "reducing waste", ["littering", "burning paper", "wasting paper"], "Using both sides uses less paper.")
H('11.B', 4, "Which action BEST limits harm to the environment?", "reduce, reuse, and recycle", ["throw all trash in one bin", "leave litter outdoors", "use new items every time"], "Reduce, reuse, and recycle lower the harm people cause.")

# ---- 12.A physical characteristics of environments (rainfall) support plants and animals
H('12.A', 2, "A desert gets very little rain. Which plant can live there?", "a cactus", ["a water lily", "a rice plant", "a rainforest fern"], "A cactus stores water and needs little rain.")
H('12.A', 3, "A rainforest gets a lot of rain. What does this help grow?", "many tall, leafy plants", ["only cactus plants", "no plants", "only sand"], "A lot of rain supports many kinds of plants.")
H('12.A', 3, "Why do fewer animals live in a very dry desert?", "there is little water and food", ["there is too much water", "there are too many trees", "it is always cold"], "Animals need water and food.")
H('12.A', 3, "A pond dries up in summer. What happens to the frogs that live there?", "they must find new water", ["they grow gills", "they turn to rock", "they fly away like birds"], "Animals need water to survive.")
H('12.A', 2, "Which environment has the most rainfall?", "a rainforest", ["a desert", "a dry plain", "a rocky hill"], "Rainforests get a lot of rain each year.")
H('12.A', 3, "Polar bears live where it is very cold. What helps them live there?", "thick fur and fat", ["thin skin", "gills", "wings"], "Thick fur and fat keep polar bears warm.")
H('12.A', 4, "A camel lives in a desert. Which fact helps it live there?", "it can go a long time without water", ["it needs a pond every day", "it eats only fish", "it hides in snow"], "Camels are adapted for a dry place.")

# ---- 12.B food chains: producers and consumers
H('12.B', 2, "What is a PRODUCER in a food chain?", "a living thing that makes its own food", ["an animal that eats other animals", "a rock", "the Moon"], "Plants are producers that make their own food.")
H('12.B', 2, "What is a CONSUMER?", "a living thing that eats other living things", ["a plant that makes food from sunlight", "a rock", "a cloud"], "Consumers cannot make their own food, so they eat other living things.")
H('12.B', 3, "In the food chain grass → rabbit → fox, which kind of living thing is the producer?", "a plant", ["an animal that eats meat", "an animal that eats plants", "a rock"], "Grass is a plant, and plants make their own food from sunlight.")
H('12.B', 3, "Algae are tiny plant-like living things in water. A small fish eats the algae. What does the small fish get from eating them?", "energy", ["shells", "sand", "bubbles"], "Animals get energy from the food they eat.")
H('12.B', 3, "A caterpillar eats leaves. A bird eats the caterpillar. Which is a consumer?", "the caterpillar and the bird", ["only the leaves", "the leaves and the bird", "none of them"], "Both animals are consumers.")
H('12.B', 2, "Which animal eats ONLY plants?", "a rabbit", ["a hawk", "a lion", "a shark"], "A rabbit eats plants only.")
H('12.B', 4, "If all the grass in a field died, what would happen to the rabbits?", "they would have less food", ["they would have more food", "nothing would change", "they would eat rocks"], "Rabbits depend on grass for food.")

# ---- 12.C plants depend on living things, wind, water for pollination and seed dispersal
H('12.C', 2, "A bee flies from flower to flower. What is the bee helping the flowers do?", "make seeds", ["melt", "freeze", "shrink"], "Bees carry pollen, which helps flowers make seeds.")
H('12.C', 3, "Dandelion seeds float away on the wind. What does the wind do?", "spreads the seeds", ["stops the seeds", "freezes the seeds", "eats the seeds"], "Wind moves seeds to new places.")
H('12.C', 3, "A squirrel buries acorns and forgets some. What may happen?", "new oak trees may grow", ["the acorns turn to rock", "the squirrel grows acorns", "nothing can grow"], "Forgotten seeds can grow into new trees.")
H('12.C', 3, "Some seeds have hooks that stick to fur. How does this help the plant?", "an animal carries the seeds away", ["the seeds melt", "the seeds stay in one place", "the plant makes less seeds"], "Hooks catch on animals and travel to new places.")
H('12.C', 2, "A coconut falls into the ocean and floats to another island. What moved the seed?", "water", ["wind only", "sunlight", "a magnet"], "Water can carry seeds to new places.")
H('12.C', 3, "A hummingbird drinks nectar from a flower. What does it help the flower do?", "move pollen", ["grow roots", "lose petals", "make rocks"], "Hummingbirds carry pollen between flowers.")
H('12.C', 4, "Why do plants need to spread their seeds far from the parent plant?", "to have enough space, water, and light", ["to get colder", "to make more shadows", "to hide from the Sun"], "Seeds that grow too close compete for resources.")

# ---- 13.A plant structures and how they help survival
H('13.A', 2, "What do roots do for a plant?", "take in water and hold it in the soil", ["make flowers", "carry seeds through the air", "make the plant glow"], "Roots anchor a plant and take in water.")
H('13.A', 2, "What do leaves do for a plant?", "make food using sunlight", ["hold the plant in the ground", "carry water from the ground only", "make the soil"], "Leaves use sunlight to make food.")
H('13.A', 3, "Which plant part helps a plant stand up and carries water to the leaves?", "stem", ["flower", "seed", "fruit"], "The stem holds the plant up and moves water.")
H('13.A', 3, "Which plant part makes seeds?", "flower", ["root", "stem", "leaf"], "Flowers make the seeds.")
H('13.A', 3, "A cactus has thick stems. How does this help it?", "it stores water", ["it hides the Sun", "it makes rain", "it grows in water"], "A thick stem holds water for dry times.")
H('13.A', 2, "A fruit protects what part of a plant?", "the seeds", ["the roots", "the leaves", "the stem"], "Fruit covers the seeds.")
H('13.A', 4, "A water lily has leaves that float. How does this help it?", "it can get sunlight at the water's surface", ["it can stay underwater", "it can grow roots in the air", "it can hide from fish"], "Floating leaves get sunlight.")

# ---- 13.B animal structures and behaviors help find food, water, air
H('13.B', 2, "A woodpecker has a sharp beak. How does it use it?", "to find insects in wood", ["to swim", "to dig a burrow in sand", "to climb a rock"], "A woodpecker pecks wood to find insects.")
H('13.B', 3, "A whale comes to the surface. Why?", "to breathe air", ["to eat grass", "to find a shell", "to sleep on land"], "Whales breathe air through lungs.")
H('13.B', 3, "A fish takes in oxygen with what body part?", "gills", ["lungs", "wings", "claws"], "Gills take oxygen from water.")
H('13.B', 3, "A bird with a long, thin beak is most likely to eat what?", "nectar from flowers", ["large fish", "tough seeds", "big insects"], "A long thin beak fits into a flower.")
H('13.B', 3, "An elephant uses its trunk to do what?", "get water and food", ["fly", "swim underwater only", "dig a pond"], "An elephant uses its trunk to drink and pick up food.")
H('13.B', 3, "Camels store fat in a hump. How does this help them?", "they can go a long time without food", ["they can fly", "they can swim fast", "they can breathe underwater"], "The fat gives energy when food is hard to find.")
H('13.B', 4, "An owl hunts at night and has big eyes. How do big eyes help?", "it can see in dim light", ["it can fly faster in the day", "it can swim", "it can dig"], "Big eyes gather more light.")

# ---- 13.C being part of a group helps animals
H('13.C', 2, "Wolves hunt in a pack. How does this help them?", "they can catch larger animals", ["they get lost", "they become slower", "they eat less"], "Working together helps them catch food.")
H('13.C', 3, "A herd of zebras stays together. How does this help them?", "there are more eyes to watch for danger", ["they get less food", "they cannot run", "they hide from each other"], "A group watches for danger together.")
H('13.C', 3, "Penguins huddle close together in cold weather. Why?", "to stay warm", ["to get cooler", "to catch fish", "to sing"], "Huddling shares body heat.")
H('13.C', 2, "A group of fish swimming together is called a what?", "school", ["pack", "herd", "hive"], "Fish that swim together are called a school.")
H('13.C', 3, "Ants work together to carry food to the nest. What does this show?", "groups can do big jobs", ["ants work alone", "ants cannot carry things", "ants do not need food"], "Working as a group helps them get food.")
H('13.C', 3, "Bees live in a hive. How does the hive help the bees?", "they share work and stay safe", ["they live alone", "they cannot make honey", "they never leave"], "Bees share jobs in the hive.")
H('13.C', 4, "When winter comes, a group of geese flies south together. What is this called?", "migration", ["hibernation", "camouflage", "pollination"], "Migration is moving to another place for the season.")

# ---- 13.D life cycles where young do not resemble parents (butterfly, frog)
H('13.D', 2, "A caterpillar changes into a butterfly. What is the change called?", "metamorphosis", ["pollination", "migration", "hibernation"], "Metamorphosis is a big change in body form.")
H('13.D', 3, "Which shows a butterfly life cycle in order?", "egg, caterpillar, chrysalis, butterfly", ["egg, butterfly, caterpillar, chrysalis", "caterpillar, egg, butterfly, chrysalis", "chrysalis, egg, caterpillar, butterfly"], "A butterfly goes from egg to caterpillar to chrysalis to adult.")
H('13.D', 3, "A tadpole lives in water and has a tail. What will it become?", "a frog", ["a fish", "a snake", "a turtle"], "A tadpole grows into a frog.")
H('13.D', 3, "How is a tadpole different from an adult frog?", "a tadpole has gills and a tail", ["a tadpole can hop", "a tadpole has four legs from birth", "a tadpole lives only on land"], "Tadpoles live in water with gills and a tail.")
H('13.D', 2, "Does a caterpillar look like its parent butterfly?", "no, it looks very different", ["yes, they look the same", "yes, they both have wings", "yes, both can fly"], "A caterpillar looks very different from a butterfly.")
H('13.D', 3, "A butterfly lays an egg on a leaf. What hatches from the egg?", "a caterpillar", ["a frog", "a chick", "a seed"], "A caterpillar hatches from a butterfly egg.")
H('13.D', 4, "Which animal has young that do NOT look like their parents?", "a frog", ["a dog", "a cat", "a horse"], "A tadpole does not look like an adult frog.")

B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g2_science.jsonl'))
print("saved", len(B.out), "questions")

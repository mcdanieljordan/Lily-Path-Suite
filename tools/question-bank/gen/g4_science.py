#!/usr/bin/env python3
"""Grade 4 Science (TEKS 112.6.b) - original questions, content strands 6-13 (strands 1-5 are practices/themes, skipped).
   Run: python3 gen/g4_science.py  -> batches/g4_science.jsonl   Written by hand, 7 per standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.6.b.', 601, own='g4_science.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 6.A classify matter: temperature, mass, magnetism, relative density, state
H('6.A', 2, "A student drops a small metal bolt, a cork, and a marble into water. The cork floats and the others sink. What property did the student test?", "relative density", ["magnetism", "temperature", "texture"], "Relative density is the ability to sink or float in water.")
H('6.A', 3, "Which tool measures the mass of a small object?", "a balance", ["a thermometer", "a graduated cylinder", "a hand lens"], "A balance measures mass.")
H('6.A', 3, "A student groups objects as 'attracted to a magnet' and 'not attracted to a magnet.' Which property is used?", "magnetism", ["density", "temperature", "state of matter"], "The property being sorted is how the objects respond to a magnet.")
H('6.A', 3, "Which sample is a gas at room temperature?", "oxygen", ["salt", "juice", "iron"], "Oxygen is a gas at room temperature.")
H('6.A', 3, "A student measures the temperature of three cups of water: 15°C, 40°C, and 25°C. Which is the warmest?", "the 40°C cup", ["the 15°C cup", "the 25°C cup", "all are the same"], "A higher temperature means warmer.")
H('6.A', 4, "A block floats in water but sinks in vegetable oil. What can the student conclude?", "the block is denser than the oil but less dense than the water", ["the block is less dense than the oil", "the block is denser than the water", "the block has no mass"], "It floats in water, so it is less dense than water. It sinks in oil, so it is denser than the oil.")
H('6.A', 3, "Which list is in order from SOLID, to LIQUID, to GAS?", "a rock, water, steam", ["steam, water, a rock", "water, a rock, steam", "a rock, steam, water"], "A rock is a solid, water is a liquid, and steam is a gas.")

# ---- 6.B mixtures and solutions
H('6.B', 2, "Sugar is stirred into water and seems to disappear. What is the mixture called?", "a solution", ["a solid", "an element", "a gas"], "A solution is a mixture where one substance spreads evenly through another.")
H('6.B', 3, "Which is a mixture where you can still see the separate parts?", "a bowl of trail mix", ["sugar in water", "salt in water", "a glass of clear tea"], "In trail mix, each part is still visible.")
H('6.B', 3, "Which is a solution of a solid in a liquid?", "salt dissolved in water", ["sand in water", "oil on water", "pebbles in a jar"], "Salt dissolves and is spread evenly in water.")
H('6.B', 3, "Oil and water are poured into a jar and shaken. What happens after a while?", "they separate into layers", ["they turn into one liquid", "they become a solid", "they disappear"], "Oil and water do not dissolve in each other.")
H('6.B', 3, "A student stirs soil into water. What is this mixture?", "a mixture of a solid in a liquid", ["a solution of two gases", "a single substance", "an element"], "Soil and water mix, but the soil can settle out.")
H('6.B', 4, "Which can be separated by pouring through a filter?", "sand mixed in water", ["sugar dissolved in water", "salt dissolved in water", "juice mixed with water"], "Sand pieces are large enough to stay in the filter.")
H('6.B', 3, "Lemonade is made by stirring lemon juice and sugar into water. Why is it a solution?", "the parts are mixed evenly", ["the parts stay in layers", "the parts are all solids", "the parts burn"], "A solution is evenly mixed.")

# ---- 6.C matter is conserved when mixtures form
H('6.C', 3, "A student mixes 100 g of soil with 200 g of water. What is the total mass of the mixture?", "300 g", ["100 g", "200 g", "250 g"], "Mass is conserved, so 100 g plus 200 g equals 300 g.")
H('6.C', 3, "A student pours 50 g of salt into 150 g of water and stirs. What is the mass of the salt water?", "200 g", ["150 g", "100 g", "50 g"], "Matter is conserved when a solution forms, so the masses add.")
H('6.C', 3, "A student weighs sugar and water separately: 40 g and 160 g. After stirring, what will the mixture's mass be?", "200 g", ["120 g", "160 g", "40 g"], "40 g plus 160 g equals 200 g.")
H('6.C', 3, "A sugar cube dissolves in water and disappears. What happened to the sugar?", "it is still there, spread through the water", ["it was destroyed", "it turned into water", "it became a gas only"], "Matter is not destroyed when it dissolves.")
H('6.C', 4, "A student mixes oil and water in a jar with a lid. The total mass before and after shaking stays the same. What does this show?", "matter is conserved", ["matter was created", "matter was destroyed", "mass doesn't matter"], "The mass stayed the same.")
H('6.C', 3, "100 g of sand and 100 g of water are mixed. How much mass does the mixture have?", "200 g", ["100 g", "50 g", "150 g"], "Mass is conserved in a mixture.")
H('6.C', 4, "A cup with soil weighs 80 g. The student adds 120 g of water. What is the combined mass of the cup, soil, and water, if the empty cup weighs 20 g and the soil is 60 g?", "200 g", ["140 g", "180 g", "220 g"], "20 g + 60 g + 120 g = 200 g.")

# ---- 7 patterns of forces: gravity, friction, magnetism
H('7', 2, "What force pulls a falling apple toward the ground?", "gravity", ["friction", "magnetism", "wind"], "Gravity pulls objects toward Earth.")
H('7', 3, "A block slides slower on carpet than on smooth tile. What force is greater on the carpet?", "friction", ["gravity", "magnetism", "light"], "Rough surfaces create more friction.")
H('7', 3, "A student rubs hands together and they get warm. What force causes the warmth?", "friction", ["magnetism", "gravity", "wind"], "Friction between surfaces makes heat.")
H('7', 3, "A magnet pulls on a steel nail across a small gap. What does this show?", "magnetic force can act without touching", ["gravity can act only by touching", "friction stops the nail", "magnets only push"], "Magnetic force acts at a distance.")
H('7', 3, "A student rolls a ball on grass and on a wood floor. On which does the ball slow down faster?", "the grass", ["the wood floor", "they are the same", "neither one"], "Grass has more friction than wood.")
H('7', 3, "Which force keeps a skydiver falling toward Earth?", "gravity", ["magnetism", "friction only", "light"], "Gravity pulls the skydiver down.")
H('7', 4, "A student rolls a toy car on three surfaces. Trial 1: 20 cm. Trial 2: 50 cm. Trial 3: 120 cm. Which surface has the least friction?", "the surface in Trial 3", ["the surface in Trial 1", "the surface in Trial 2", "they are the same"], "The car travels farthest on the surface with the least friction.")

# ---- 8.A transfer of energy by objects in motion, waves in water, sound
H('8.A', 2, "A moving bowling ball hits pins. What happens to the pins?", "they get energy and move", ["they stay still", "they melt", "they turn to light"], "Energy is transferred from the ball to the pins.")
H('8.A', 3, "A pebble is dropped in a pond. What do you see?", "waves moving outward", ["the pond freezing", "the pond going dry", "the water turning colors"], "The pebble's energy makes water waves.")
H('8.A', 3, "A drum is hit and a bell beside it begins to vibrate. What is traveling from the drum to the bell?", "sound energy", ["light energy", "heat only", "nothing"], "Sound waves carry energy.")
H('8.A', 3, "A moving billiard ball hits a still ball and the still ball starts moving. What happened?", "energy was transferred", ["energy was destroyed", "the balls changed color", "gravity stopped"], "The moving ball passed energy to the still one.")
H('8.A', 3, "Waves in the ocean can move a boat up and down. What does this show?", "water waves carry energy", ["waves carry matter far away", "boats make waves only", "the boat creates energy"], "Waves transfer energy.")
H('8.A', 3, "Which shows energy transfer by sound?", "a window rattling from a loud boom", ["a shadow on the wall", "a plant growing", "ice melting"], "A loud sound can make objects vibrate.")
H('8.A', 4, "A student drops a rock into a bucket and sees ripples spread across the water. What causes the ripples?", "energy from the rock moving into the water", ["energy from the water entering the rock", "the bucket creating energy", "gravity pushing sideways"], "The rock's energy transfers to the water as waves.")

# ---- 8.B conductors and insulators of thermal and electrical energy
H('8.B', 2, "Which material is a good conductor of electricity?", "copper", ["rubber", "wood", "plastic"], "Metals like copper conduct electricity.")
H('8.B', 2, "Which material is a good insulator?", "rubber", ["copper", "iron", "aluminum foil"], "Rubber does not let electricity pass easily.")
H('8.B', 3, "Why is the handle of a pot made of plastic or wood?", "they do not conduct heat well", ["they conduct heat well", "they are magnetic", "they melt easily"], "Insulators keep the handle cooler.")
H('8.B', 3, "Why are electrical wires coated with plastic?", "to keep electricity from reaching people", ["to make the wire heavier", "to make the wire shine", "to make the wire a magnet"], "Plastic insulates and protects people.")
H('8.B', 3, "A metal spoon left in hot soup gets hot quickly. What does this show?", "metal conducts heat well", ["metal insulates heat", "soup cannot heat metal", "spoons make heat"], "Metals conduct thermal energy.")
H('8.B', 3, "Which is a good thermal insulator?", "foam", ["silver", "copper", "aluminum"], "Foam resists the flow of heat.")
H('8.B', 4, "A student tests a bulb circuit with a coin, a pencil eraser, and a metal key. The bulb lights with the coin and the key but not the eraser. What does the eraser do?", "it insulates", ["it conducts", "it makes light", "it makes heat"], "The eraser blocks the flow of electricity.")

# ---- 8.C electrical energy in a closed path (circuit) producing light and heat
H('8.C', 2, "What is a closed circuit?", "a complete path for electricity", ["a broken path", "a path with no battery", "a path that stops at a gap"], "A closed circuit has no gaps.")
H('8.C', 3, "A bulb will not light in a circuit. A wire is not touching the battery. What is the problem?", "the circuit is open", ["the circuit is closed", "the bulb is too bright", "the battery is too big"], "A gap stops the flow of electricity.")
H('8.C', 3, "Which parts are needed to make a bulb light?", "a battery, wires, and a bulb", ["a magnet and a rock", "paper and tape only", "a spoon and a cup"], "The battery supplies energy, the wires carry it, and the bulb uses it.")
H('8.C', 3, "A switch is turned on and the light turns on. What did the switch do?", "closed the circuit", ["opened the circuit", "removed the battery", "cooled the wire"], "A closed switch completes the path.")
H('8.C', 3, "A lit bulb gives off light and what else?", "heat", ["sound only", "gravity", "water"], "Bulbs give off thermal energy too.")
H('8.C', 3, "Electrical energy changes into which two forms in a toaster?", "heat and light", ["sound and wind", "cold and dark", "water and soil"], "A toaster glows and gets hot.")
H('8.C', 4, "A student draws a loop with a battery, a bulb, and wires with no gaps. What will happen?", "the bulb will light", ["the bulb will stay off", "the battery will freeze", "the wire will turn to water"], "A closed loop lets the current flow.")

# ---- 9.A patterns of seasons: temperature, length of daylight
H('9.A', 2, "Which season has the longest daylight hours in Texas?", "summer", ["winter", "fall", "spring"], "Summer days are longest.")
H('9.A', 3, "A student records daylight length each month. Daylight gets longer from December to June. What season change does this show?", "winter turning to summer", ["summer turning to winter", "fall turning to winter", "no change"], "Longer days come as winter turns to summer.")
H('9.A', 3, "Which shows the correct season order?", "spring, summer, fall, winter", ["spring, fall, summer, winter", "summer, spring, winter, fall", "winter, fall, spring, summer"], "The seasons repeat in the same order.")
H('9.A', 3, "A data table shows average highs: Jan 55°F, Apr 75°F, Jul 95°F, Oct 78°F. Which month is probably the hottest?", "July", ["January", "April", "October"], "95°F is the highest.")
H('9.A', 3, "Temperatures are 80°F, 70°F, 60°F, 50°F in four months in order. Which season change is likely?", "summer turning to winter", ["winter turning to summer", "spring turning to summer", "no change"], "Cooling temps show a change toward winter.")
H('9.A', 3, "In which season is daylight SHORTEST?", "winter", ["summer", "spring", "fall"], "Winter has the shortest days.")
H('9.A', 4, "A student predicts that days will get shorter in September through December. What season pattern supports the prediction?", "fall moving to winter", ["spring moving to summer", "summer staying summer", "winter moving to spring"], "Daylight shortens in fall and winter.")

# ---- 9.B Moon phases
H('9.B', 2, "About how long does it take the Moon to go through all of its phases?", "about one month", ["one day", "one year", "one week"], "The lunar cycle is about 29.5 days.")
H('9.B', 3, "Which is a Moon phase?", "full moon", ["full star", "half planet", "new cloud"], "A full moon is a phase.")
H('9.B', 3, "The Moon looks like a thin curve. Which phase is this?", "crescent", ["full", "gibbous", "new"], "A thin curve is a crescent.")
H('9.B', 3, "A student sees a new moon. How much of the Moon's lit side faces Earth?", "almost none", ["all of it", "half of it", "most of it"], "A new moon looks dark from Earth.")
H('9.B', 3, "What is the next phase after a waxing crescent?", "first quarter", ["new moon", "full moon", "last quarter"], "The Moon grows from crescent to first quarter to gibbous to full.")
H('9.B', 3, "Why do we see different phases of the Moon?", "we see different amounts of its sunlit half", ["the Moon changes shape", "Earth's shadow always covers it", "the Moon makes less light"], "The part of the Moon lit by the Sun that faces Earth changes.")
H('9.B', 4, "A student records the Moon's shape every night for a month. What pattern will the student see?", "the same cycle of phases repeats", ["a random shape each night", "no change", "the Moon stays full"], "The phases repeat every month.")

# ---- 10.A water cycle
H('10.A', 2, "What is the main source of energy for the water cycle?", "the Sun", ["the Moon", "wind", "ice"], "The Sun's heat drives evaporation.")
H('10.A', 3, "Water from a lake becomes water vapor and rises. What is this called?", "evaporation", ["condensation", "precipitation", "runoff"], "Liquid water turning to vapor is evaporation.")
H('10.A', 3, "Water vapor cools and forms clouds. What is this called?", "condensation", ["evaporation", "precipitation", "melting"], "Vapor turning to liquid is condensation.")
H('10.A', 3, "Rain, snow, sleet, and hail are all examples of what?", "precipitation", ["evaporation", "condensation", "erosion"], "They fall from clouds to Earth.")
H('10.A', 3, "Which order shows the water cycle?", "evaporation, condensation, precipitation", ["precipitation, evaporation, condensation", "condensation, precipitation, evaporation", "precipitation, condensation, evaporation"], "Water evaporates, condenses to form clouds, and falls as precipitation.")
H('10.A', 3, "Rain runs into a stream that flows to the ocean. What is the rain doing?", "moving across Earth's surface", ["leaving Earth", "turning to ice", "turning to rock"], "Runoff carries water over land.")
H('10.A', 4, "On a hot, sunny day, a puddle disappears. Where did the water go?", "into the air as water vapor", ["into the Sun", "into the ground as rock", "into outer space only"], "Heat evaporates the water into the air.")

# ---- 10.B slow changes: weathering, erosion, deposition
H('10.B', 2, "What is weathering?", "the breaking down of rock into smaller pieces", ["the moving of sand by wind", "the dropping of sand in a new place", "the growing of mountains"], "Weathering breaks rock apart.")
H('10.B', 2, "What is erosion?", "the moving of rock and soil from one place to another", ["the breaking of rock by ice", "the forming of a volcano", "the freezing of water"], "Erosion carries sediment away.")
H('10.B', 3, "A river drops sand at its mouth where it meets the ocean. What is this called?", "deposition", ["erosion", "weathering", "evaporation"], "Deposition is dropping sediment in a new place.")
H('10.B', 3, "Wind blows sand to form a dune. Which two processes happened?", "erosion and deposition", ["weathering only", "condensation and precipitation", "melting and freezing"], "Wind moved sand and dropped it in a new place.")
H('10.B', 3, "Water freezes in a rock crack and the rock splits. What process is this?", "weathering", ["deposition", "erosion", "evaporation"], "Ice wedging breaks rock.")
H('10.B', 3, "A glacier slowly carries rocks across the land. What process is this?", "erosion by ice", ["deposition by wind", "weathering by wind", "evaporation by ice"], "Glaciers move rock and sediment.")
H('10.B', 4, "A canyon forms as a river flows over rock for millions of years. Which words describe the changes?", "slow and caused by water", ["fast and caused by wind only", "rapid and caused by volcanoes", "slow and caused by magnets"], "Rivers slowly erode rock.")

# ---- 10.C weather vs climate
H('10.C', 2, "Which describes WEATHER?", "a rainy afternoon in Houston", ["a desert's average rainfall over 30 years", "how hot the tropics usually are", "the long-term pattern of a place"], "Weather is the condition at a certain time and place.")
H('10.C', 3, "Which describes CLIMATE?", "the average temperature of a city over many years", ["today's high temperature", "a storm tomorrow", "this morning's fog"], "Climate is the long-term average.")
H('10.C', 3, "It is cloudy and cool today. Which is this?", "weather", ["climate", "season", "water cycle"], "It describes the conditions on a single day.")
H('10.C', 3, "A rainforest gets heavy rain most of the year. This describes its what?", "climate", ["weather on one day", "a storm", "a season"], "Long-term patterns describe climate.")
H('10.C', 3, "Which is the BEST tool for tracking short-term weather?", "a thermometer and rain gauge", ["a telescope", "a balance", "a magnet"], "These measure daily conditions.")
H('10.C', 3, "Which statement is about climate?", "Deserts are dry most of the year.", ["It rained last night.", "Tomorrow will be windy.", "The sky is clear now."], "It describes a long-term pattern.")
H('10.C', 4, "A student says, 'It was hot today, so Texas has a hot climate.' What is wrong?", "one day of weather does not show climate", ["hot days never happen", "climate is only about wind", "weather lasts years"], "Climate is a long-term pattern.")

# ---- 11.A advantages and disadvantages of renewable and nonrenewable resources
H('11.A', 2, "Which is a renewable resource?", "wind", ["coal", "oil", "natural gas"], "Wind is renewable.")
H('11.A', 2, "Which is a nonrenewable resource?", "coal", ["sunlight", "wind", "water"], "Coal takes millions of years to form.")
H('11.A', 3, "What is an advantage of solar energy?", "it comes from a source that will not run out", ["it only works at night", "it makes a lot of smoke", "it is made from coal"], "Sunlight is renewable.")
H('11.A', 3, "What is a disadvantage of burning coal?", "it can cause air pollution", ["it never produces energy", "it is endless", "it makes the air cleaner"], "Burning coal releases pollutants.")
H('11.A', 3, "What is a disadvantage of wind power?", "it only works when the wind blows", ["it causes smog", "it runs out", "it needs coal"], "Wind turbines need wind.")
H('11.A', 3, "What is an advantage of oil?", "it stores a lot of energy for fuel", ["it is renewable", "it never pollutes", "it is free"], "Oil is energy-dense, although it is nonrenewable and can pollute.")
H('11.A', 4, "A town must choose between a wind farm and a coal plant. Which is a reason to choose the wind farm?", "wind will not run out", ["coal is renewable", "coal makes no pollution", "wind needs fuel to be dug up"], "Wind is renewable.")

# ---- 11.B role of energy; conservation, disposal, recycling impact on environment
H('11.B', 2, "Why is energy important to modern life?", "it powers homes, cars, and factories", ["it makes seasons", "it makes rocks", "it makes oceans"], "Energy is used everywhere.")
H('11.B', 3, "Which action saves electricity?", "turning off lights when you leave", ["leaving the TV on", "leaving all lights on", "opening the fridge for a long time"], "Turning off lights uses less energy.")
H('11.B', 3, "How does recycling aluminum cans help the environment?", "it saves natural resources and energy", ["it makes more waste", "it uses more mines", "it pollutes water"], "Recycling reduces the need for new mining.")
H('11.B', 3, "What can happen when trash is dumped into a river?", "it can harm animals and plants", ["it cleans the river", "it makes water safer", "it feeds the Sun"], "Pollution harms living things.")
H('11.B', 3, "Why should batteries be disposed of properly?", "they contain chemicals that can pollute", ["they are made of food", "they explode when cold", "they cannot be recycled"], "Batteries can leak harmful chemicals.")
H('11.B', 3, "Which is a way to conserve natural resources?", "reuse a glass jar", ["throw it away", "break it", "bury it"], "Reusing saves new materials.")
H('11.B', 4, "A city adds a recycling program. What is a likely result?", "less trash goes to landfills", ["more trash goes to landfills", "more mining is needed", "more forests are cut"], "Recycling reduces landfill waste.")

# ---- 11.C physical properties of rocks that allow resources to be stored
H('11.C', 3, "A rock with many small holes can hold water and oil. What is this property?", "porosity", ["magnetism", "hardness only", "color"], "Porous rocks have spaces that store fluids.")
H('11.C', 3, "Sandstone is porous. What could it store?", "water or oil", ["only air", "only sound", "only light"], "Spaces between grains hold fluids.")
H('11.C', 3, "A layer of rock does NOT let water pass through. What is it called?", "impermeable", ["porous", "permeable", "soft"], "Impermeable rock blocks fluids.")
H('11.C', 3, "Why is oil often found under a layer of hard, tight rock?", "the tight rock traps the oil", ["the rock makes oil", "the rock melts the oil", "the rock gives off oil"], "A caprock holds oil in the rock below.")
H('11.C', 3, "A sponge-like rock can hold water. Which property allows this?", "many connected pore spaces", ["a very smooth surface", "a bright color", "a heavy weight only"], "Pores store water.")
H('11.C', 3, "Which rock is most likely to store groundwater?", "porous sandstone", ["solid granite", "dense shale", "a solid glass-like rock"], "Sandstone has spaces for water.")
H('11.C', 4, "A student pours water on three rocks. One soaks water in quickly, one keeps water on top, and one soaks it in slowly. Which rock is best for storing water?", "the rock with the most pore space", ["the rock that keeps water on top", "the rock with no spaces at all", "none of them"], "Water soaking in quickly shows many pores.")

# ---- 12.A producers make food using sunlight, water, and carbon dioxide
H('12.A', 2, "What do plants take in from the air to make food?", "carbon dioxide", ["oxygen only", "nitrogen only", "smoke"], "Plants use carbon dioxide in photosynthesis.")
H('12.A', 3, "What three things do producers use to make food?", "sunlight, water, and carbon dioxide", ["soil, rocks, and wind", "oxygen, sugar, and ice", "heat, sound, and magnets"], "These are the inputs of photosynthesis.")
H('12.A', 3, "What gas do plants give off when they make food?", "oxygen", ["carbon dioxide", "smoke", "nitrogen"], "Plants release oxygen.")
H('12.A', 3, "Which plant part takes in most of the sunlight?", "leaves", ["roots", "seeds", "bark"], "Leaves capture sunlight.")
H('12.A', 3, "A plant is kept in a dark closet for two weeks. What will probably happen?", "it will not make enough food and will weaken", ["it will make more food", "it will grow faster", "it will turn into an animal"], "Without light, a plant cannot make food well.")
H('12.A', 3, "Which of these is a producer?", "a tree", ["a rabbit", "a hawk", "a snake"], "A tree makes its own food.")
H('12.A', 4, "Which statement describes the cycling of matter in a plant?", "plants use carbon dioxide and water to make sugar", ["plants make carbon dioxide from sugar only", "plants create matter from nothing", "plants destroy matter"], "Matter is cycled and rearranged.")

# ---- 12.B food webs: Sun, producers, consumers, decomposers
H('12.B', 2, "What do decomposers do?", "break down dead plants and animals", ["make food from sunlight", "eat only living animals", "give off light"], "Decomposers recycle matter.")
H('12.B', 3, "Which is a decomposer?", "a mushroom", ["a rabbit", "a grass plant", "an owl"], "Fungi decompose dead things.")
H('12.B', 3, "In a food web, what is the source of energy for producers?", "the Sun", ["the soil", "the decomposers", "the consumers"], "Producers use sunlight.")
H('12.B', 3, "A hawk eats a snake that ate a mouse. The hawk is what?", "a consumer", ["a producer", "a decomposer", "a source of energy"], "A hawk eats other animals.")
H('12.B', 3, "Why are decomposers important?", "they return nutrients to the soil", ["they make sunlight", "they eat producers only", "they stop energy flow"], "They recycle nutrients.")
H('12.B', 3, "Which arrow correctly shows energy flow?", "grass → rabbit", ["rabbit → grass", "rabbit → Sun", "owl → grass"], "Arrows point to the organism that gets the energy.")
H('12.B', 4, "If all decomposers disappeared, what would happen?", "dead material would pile up and nutrients wouldn't be recycled", ["more plants would grow quickly", "the Sun would stop shining", "producers would turn into consumers"], "Decomposers recycle matter.")

# ---- 12.C past environments from fossils; Texas fossils
H('12.C', 2, "What can fossils tell scientists?", "what living things and environments existed long ago", ["tomorrow's weather", "the age of a student", "the temperature now"], "Fossils are evidence of the past.")
H('12.C', 3, "Marine fossils such as shells are found on a hilltop in Texas. What does this suggest?", "the area was once under the sea", ["the hill was always dry", "shells grow on hills", "the shells fell from the sky"], "The fossils show an ancient ocean.")
H('12.C', 3, "Dinosaur tracks found in Texas show that what once lived there?", "dinosaurs", ["whales only", "humans", "dragons"], "Texas has dinosaur trackways.")
H('12.C', 3, "A fossil fern is found in a dry region. What can be concluded?", "the area was once wetter", ["the area was always dry", "ferns need no water", "ferns are animals"], "Ferns need moist places.")
H('12.C', 3, "In which kind of rock are fossils MOST often found?", "sedimentary rock", ["igneous rock", "metamorphic rock", "lava"], "Layers of sediment preserve remains.")
H('12.C', 3, "A fossil of a warm-water coral is found in a cold place today. What does this suggest?", "the place was once warmer", ["the place was always cold", "corals like ice", "the coral moved by itself"], "Corals live in warm water.")
H('12.C', 4, "Why can fossils of sea animals be found far from the ocean today?", "oceans covered the land long ago", ["sea animals walked there", "the ocean is closer than before", "wind carried shells from the sea"], "Land that was once underwater became dry.")

# ---- 13.A plant structures/functions help survival
H('13.A', 2, "A cactus has waxy skin. How does this help it survive?", "it keeps water from escaping", ["it attracts rain", "it makes the cactus taller", "it makes the cactus magnetic"], "The wax holds water in.")
H('13.A', 3, "Mesquite trees in Texas have very deep roots. How does this help them?", "they reach water far underground", ["they float on water", "they climb rocks", "they make seeds faster"], "Deep roots reach water.")
H('13.A', 3, "A water lily has wide, flat leaves that float. What is the function?", "to catch sunlight at the water's surface", ["to hold water inside", "to dig into the mud", "to hide from fish"], "Leaves float to get light.")
H('13.A', 3, "A cactus has spines instead of broad leaves. How does this help it?", "it loses less water and is protected from animals", ["it gets more sunlight", "it needs more water", "it hides underground"], "Spines reduce water loss and defend the plant.")
H('13.A', 3, "A pine tree has thin needle-shaped leaves. How do they help in cold, dry places?", "they lose less water", ["they absorb more snow", "they fall off quickly", "they make the tree grow faster"], "Needles reduce water loss.")
H('13.A', 3, "A plant in a rainforest has leaves with pointed tips. How does this help it?", "water drips off easily", ["water collects on the leaf", "it traps insects", "it blocks light"], "Drip tips shed rainwater.")
H('13.A', 4, "A desert wildflower blooms right after a rain and then makes seeds quickly. How does this help it?", "it can finish its life before the dry time returns", ["it uses sunlight at night", "it grows deeper roots than trees", "it avoids soil completely"], "A quick life cycle fits short wet periods.")

# ---- 13.B inherited vs acquired traits
H('13.B', 2, "Which is an INHERITED trait?", "eye color", ["a scar on the knee", "knowing how to ride a bike", "a haircut"], "Eye color is passed from parents.")
H('13.B', 2, "Which is an ACQUIRED trait?", "a scar from a fall", ["flower color", "fur color in a dog", "the number of legs a spider has"], "Scars are gained during life.")
H('13.B', 3, "A dog learns to sit on command. What kind of trait is this?", "acquired", ["inherited", "both always", "neither"], "Learned behaviors are acquired.")
H('13.B', 3, "A tiger has stripes because its parents did. What kind of trait is this?", "inherited", ["acquired", "learned", "temporary"], "Stripes are passed from parent to offspring.")
H('13.B', 3, "A person learns to play the piano. What kind of trait is this?", "acquired", ["inherited", "genetic", "passed by eye color"], "Skills are learned.")
H('13.B', 3, "Which is NOT inherited?", "a broken arm", ["blood type", "eye color", "hair texture"], "Injuries are acquired.")
H('13.B', 4, "A seedling is bent by wind and grows crooked. Its seeds grow into straight plants. What does this show?", "the bend was acquired and not inherited", ["the bend was inherited", "seeds always bend", "wind changes seeds"], "Acquired traits are not passed on.")

B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g4_science.jsonl'))
print("saved", len(B.out), "questions")

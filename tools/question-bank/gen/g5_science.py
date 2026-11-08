#!/usr/bin/env python3
"""Grade 5 Science (TEKS 112.7.b) - original questions, content strands 6-13 (strands 1-5 are practices/themes, skipped).
   Run: python3 gen/g5_science.py  -> batches/g5_science.jsonl   Written by hand, 7 per standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.7.b.', 701, own='g5_science.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 6.A compare matter by physical properties
H('6.A', 2, "A student wants to find out which of three objects has the most mass. Which tool should the student use?", "a balance", ["a thermometer", "a magnet", "a hand lens"], "A balance compares mass.")
H('6.A', 3, "A steel paper clip is pulled toward a magnet, but a plastic button is not. Which property is being compared?", "magnetism", ["solubility", "volume", "physical state"], "The objects are sorted by how they react to a magnet.")
H('6.A', 3, "A student pours 50 mL of water into a graduated cylinder. What property is the student measuring?", "volume", ["mass", "density", "magnetism"], "A graduated cylinder measures the volume of a liquid.")
H('6.A', 3, "Salt dissolves in water, but sand does not. Which property is being compared?", "solubility in water", ["magnetism", "mass", "physical state"], "Solubility is the ability to dissolve in a liquid.")
H('6.A', 3, "A wooden spoon and a metal spoon are placed in hot soup. After a minute the metal handle is much hotter. What does this show?", "metal conducts thermal energy better than wood", ["wood conducts thermal energy better than metal", "metal has less mass than wood", "wood is magnetic"], "Metal is a better thermal conductor.")
H('6.A', 4, "A student places four objects in water. Object W sinks, Object X floats, Object Y floats, and Object Z sinks. Which two objects are probably LESS dense than water?", "X and Y", ["W and Z", "W and X", "Y and Z"], "Objects that float are less dense than water.")
H('6.A', 3, "Which substance is a liquid at room temperature?", "milk", ["wood", "helium", "copper"], "Milk is a liquid; copper and wood are solids, and helium is a gas.")

# ---- 6.B mixtures keep properties of their substances
H('6.B', 2, "A mixture contains iron filings and sand. Which tool could separate the iron filings?", "a magnet", ["a thermometer", "a ruler", "a balance"], "Iron is attracted to a magnet and sand is not.")
H('6.B', 3, "When iron filings and sand are mixed, what happens to the properties of each substance?", "each keeps its own properties", ["both change into a new substance", "both lose their mass", "the iron stops being magnetic"], "In a mixture the substances keep their properties.")
H('6.B', 3, "Sand is stirred into water. How could the sand be separated again?", "pour the mixture through a filter", ["freeze the mixture", "add more sand", "shine a light on it"], "A filter traps the sand pieces.")
H('6.B', 3, "A bag holds small beads and large marbles. What could be used to separate them?", "a strainer with holes between the sizes", ["a thermometer", "a magnet", "a candle"], "A strainer lets small pieces through and holds the large ones.")
H('6.B', 3, "A student mixes salt and pepper in a bowl. Which statement is true?", "both substances are still in the bowl and keep their properties", ["a new substance was made", "the salt turned into pepper", "the mass of both disappeared"], "A mixture does not form a new substance.")
H('6.B', 4, "A mixture of iron filings, sand, and water is poured through a filter, and then a magnet is held over the sand left on the filter. What will the magnet pick up?", "the iron filings", ["the sand", "the water", "nothing"], "Only the iron is attracted to a magnet.")
H('6.B', 3, "Which is a mixture whose parts can easily be seen?", "a salad", ["pure water", "a gold bar", "an aluminum can"], "The ingredients of a salad can each be seen.")

# ---- 6.C solutions; matter conserved
H('6.C', 3, "A student stirs 30 g of sugar into 170 g of water until it dissolves. What is the mass of the solution?", "200 g", ["140 g", "170 g", "30 g"], "Matter is conserved, so 30 g plus 170 g is 200 g.")
H('6.C', 3, "After salt dissolves in water, how can a student show the salt is still in the solution?", "let the water evaporate and look for the salt", ["look for the salt with a magnet", "freeze the solution", "weigh only the cup"], "When the water evaporates, the salt is left behind.")
H('6.C', 3, "Drink powder is stirred into water. Which properties of the water change?", "its color and taste", ["its mass is destroyed", "it becomes a solid", "it stops being a liquid"], "The solution can look and taste different.")
H('6.C', 3, "A student weighs a cup of water and a spoonful of salt separately, then dissolves the salt in the water. What should the total mass do?", "stay the same", ["go up", "go down", "become zero"], "Mass is conserved when a solution forms.")
H('6.C', 4, "A student has a 150 g solution after dissolving 25 g of sugar in water. How much water did the student start with?", "125 g", ["175 g", "150 g", "25 g"], "150 g minus 25 g leaves 125 g.")
H('6.C', 3, "Which is a solution?", "salt completely dissolved in water", ["sand stirred into water", "oil floating on water", "pebbles in a bucket"], "A solution is evenly mixed, with the substance dissolved.")
H('6.C', 4, "Which statement about dissolving is true?", "the dissolved matter is still there even though it can not be seen", ["the dissolved matter is gone", "dissolving creates new matter", "dissolving removes mass from the water"], "Matter is conserved when it dissolves.")

# ---- 6.D matter made of tiny particles
H('6.D', 2, "What is matter made of?", "particles too small to see", ["only large grains", "empty space only", "light"], "All matter is made of tiny particles.")
H('6.D', 3, "A balloon fills up with air and gets bigger. What does this show?", "air is made of particles that take up space", ["air has no mass at all", "air is not matter", "air is made of liquid"], "Air particles take up space and push on the balloon.")
H('6.D', 3, "A smell from baking cookies spreads across a house. What does this suggest?", "tiny particles are moving through the air", ["the cookies left the oven", "air is empty", "smells are solid"], "The particles of scent spread through the air.")
H('6.D', 3, "A drop of food coloring slowly spreads through a glass of water. Why?", "the particles of dye and water move and mix", ["the water becomes a solid", "the dye is destroyed", "the glass pulls the dye"], "Moving particles mix together.")
H('6.D', 3, "Which can NOT be seen but is still matter?", "the air inside a balloon", ["a rock", "a pencil", "a wooden chair"], "Air is matter, but its particles are too small to see.")
H('6.D', 3, "A model uses small beads to show the particles in a solid, liquid, and gas. In which state would the beads be the farthest apart?", "gas", ["solid", "liquid", "they are all the same"], "Gas particles are spread out the most.")
H('6.D', 4, "A student squeezes air in a closed syringe. The plunger moves in a little. What does this show?", "there is space between the particles of air", ["air particles are destroyed", "air has no particles", "the syringe makes the air a solid"], "The particles can be pushed closer together.")

# ---- 7.A equal and unequal forces
H('7.A', 2, "Two students push on opposite sides of a box with the same force. What happens to the box?", "it does not move", ["it speeds up", "it moves toward one student", "it flies up"], "Equal forces in opposite directions balance.")
H('7.A', 3, "A student pushes a cart with a force of 10 N and another student pushes the other way with 4 N. What happens?", "the cart moves in the direction of the larger force", ["the cart stays still", "the cart moves toward the smaller force", "the cart disappears"], "Unequal forces cause motion in the direction of the greater force.")
H('7.A', 3, "A soccer ball is kicked and rolls across the grass. Eventually it stops. Which force slows it?", "friction", ["magnetism", "gravity pushing it sideways", "light"], "Friction acts against the motion.")
H('7.A', 3, "A moving cart hits a stationary cart and the stationary cart begins to move. What happened to the energy?", "some energy transferred to the second cart", ["energy was destroyed", "energy stayed only in the first cart", "energy turned into matter"], "Energy transfers during a collision.")
H('7.A', 3, "A tug-of-war is tied, with neither team moving. What does this tell you about the forces?", "the forces on each side are equal", ["one side is much stronger", "there are no forces", "gravity is missing"], "Balanced forces produce no change in motion.")
H('7.A', 3, "Which change would make a toy car roll faster down a ramp?", "making the ramp steeper", ["making the ramp rougher", "adding sand to the ramp", "making the ramp flatter"], "A steeper ramp lets gravity speed the car up more.")
H('7.A', 4, "A student pushes a box with 20 N. The floor pushes back with 20 N of friction. What is the motion of the box?", "it moves at a steady speed or stays still", ["it speeds up quickly", "it moves backward", "it floats"], "Equal opposite forces are balanced.")

# ---- 7.B design a simple investigation of force
H('7.B', 3, "A student tests how ramp height affects how far a toy car rolls. Which should be the ONE thing the student changes?", "the height of the ramp", ["the size of the car", "the floor surface", "the person who releases the car"], "Only one variable should be changed.")
H('7.B', 3, "In a balloon rocket investigation, which is a good variable to keep the same?", "the length of the string", ["the amount of air in each trial", "the balloon size for every trial", "the time of day"], "Keeping other conditions equal makes the test fair.")
H('7.B', 3, "A student wants to test whether a heavier cart travels farther down a ramp. What should the student measure?", "the distance the cart travels", ["the color of the cart", "the age of the cart", "the sound the cart makes"], "Distance traveled is the outcome being measured.")
H('7.B', 3, "Why should a student do several trials in a force experiment?", "to make sure the results are reliable", ["to waste time", "to change the question", "to avoid recording data"], "Repeated trials improve reliability.")
H('7.B', 3, "A student releases a cart from the top of a ramp each time. What is the benefit?", "the starting point stays the same", ["the cart will never stop", "the ramp stops moving", "the data become unnecessary"], "A constant starting point keeps the test fair.")
H('7.B', 4, "A student records the distance a balloon rocket travels with different amounts of air. Which table heading is MOST useful?", "amount of air and distance traveled", ["color of balloon and shape of room", "name of student and date", "time of day and weather"], "A data table should show the changed variable and the measured result.")
H('7.B', 4, "Which question can be tested with a car on a ramp?", "Does a steeper ramp make the car go farther?", ["Which color car is prettiest?", "Which ramp do students like?", "Why was the car made?"], "A testable question can be answered with measurements.")

# ---- 8.A transformation of energy
H('8.A', 2, "A flashlight battery stores what kind of energy?", "chemical energy", ["sound energy", "thermal energy only", "magnetic energy"], "Batteries store chemical energy.")
H('8.A', 3, "In a flashlight, which energy change happens?", "chemical to electrical to light", ["light to chemical to sound", "sound to light to heat", "heat to chemical to sound"], "The battery's chemical energy becomes electrical, then light.")
H('8.A', 3, "A toaster gets hot when it is plugged in. Which energy change is happening?", "electrical energy to thermal energy", ["thermal energy to electrical energy", "light energy to sound energy", "sound energy to chemical energy"], "Electric current heats the wires.")
H('8.A', 3, "A solar-powered calculator uses what energy to work?", "light energy changed to electrical energy", ["sound changed to light", "heat changed to sound", "wind changed to chemical"], "Solar cells change light to electricity.")
H('8.A', 3, "A radio plays music. Which energy change occurs?", "electrical energy to sound energy", ["sound energy to electrical energy", "chemical energy to magnetic energy", "light energy to heat energy"], "The radio changes electrical energy to sound.")
H('8.A', 3, "When a person rubs their hands together, which energy change occurs?", "motion to thermal energy", ["thermal to motion", "light to motion", "sound to light"], "Friction changes motion into heat.")
H('8.A', 4, "Wind turns a turbine to light a bulb. Which order shows the energy changes?", "motion, electrical, light", ["light, motion, electrical", "electrical, light, motion", "light, electrical, motion"], "Motion turns the generator, making electricity that lights the bulb.")

# ---- 8.B complete circuits
H('8.B', 2, "What does a circuit need to work?", "a complete path, an energy source, and a load", ["only a switch", "a magnet and a spring", "only wires"], "A working circuit needs a source, a path, and something that uses the energy.")
H('8.B', 3, "Which makes a complete circuit?", "a battery connected by wires to a bulb in a closed loop", ["a battery and bulb with a gap in the wire", "a bulb alone", "a battery in a drawer"], "The loop must be unbroken.")
H('8.B', 3, "A fan, a bulb, and a buzzer are connected to batteries. Which energy form does the buzzer produce?", "sound", ["motion", "light", "magnetism"], "A buzzer changes electrical energy into sound.")
H('8.B', 3, "An electric motor in a circuit spins. Into which form is electrical energy changed?", "motion", ["sound only", "cold", "matter"], "A motor turns electrical energy into motion.")
H('8.B', 3, "A student opens the switch in a working circuit. What happens to the bulb?", "it goes out", ["it gets brighter", "it stays lit", "it turns blue"], "An open switch breaks the circuit.")
H('8.B', 3, "A bulb will NOT light in a circuit. Which could be the cause?", "a wire is disconnected from the battery", ["the room is too bright", "the wire is too clean", "the bulb is too round"], "A break stops the flow of electricity.")
H('8.B', 4, "A circuit has a battery, wires, and a lit bulb. The bulb gives off light and what other form?", "thermal energy", ["magnetic energy", "chemical energy only", "no other form"], "Lit bulbs also give off heat.")

# ---- 8.C light travels in straight lines; reflected, refracted, absorbed
H('8.C', 2, "How does light travel in empty space or air?", "in a straight line", ["in a circle", "in a zigzag", "it does not travel"], "Light travels in straight lines.")
H('8.C', 3, "A mirror bounces light off its surface. What is this called?", "reflection", ["refraction", "absorption", "evaporation"], "Reflection is light bouncing off a surface.")
H('8.C', 3, "A pencil in a glass of water looks bent. What is happening to the light?", "it is refracted as it passes into water", ["it is absorbed completely", "it is reflected by the pencil", "it turns into sound"], "Light bends when it passes between materials.")
H('8.C', 3, "A black shirt feels hotter than a white shirt in sunlight. Why?", "dark colors absorb more light", ["dark colors reflect more light", "white absorbs more light", "shirts make light"], "Absorbed light turns into thermal energy.")
H('8.C', 3, "A shadow forms when an object blocks the path of light. Why does the shadow have the same shape as the object?", "light travels in straight lines", ["light travels in curves", "light is slow", "shadows are made of light"], "Straight-line light gives a matching shadow.")
H('8.C', 3, "Which material lets the MOST light pass through?", "clear glass", ["a wooden board", "a metal sheet", "a thick cardboard box"], "Clear glass is transparent.")
H('8.C', 4, "A flashlight beam hits a mirror at an angle. What happens to the beam?", "it bounces off at a matching angle", ["it stops", "it passes straight through", "it turns into heat only"], "A reflected beam leaves at the same angle it arrived.")

# ---- 9 Earth rotation, day/night, Sun's apparent motion, shadows
H('9', 2, "About how long does it take Earth to rotate once on its axis?", "24 hours", ["1 hour", "one week", "one year"], "One rotation takes about a day.")
H('9', 3, "What causes the day/night cycle on Earth?", "Earth spinning on its axis", ["Earth orbiting the Moon", "the Sun circling Earth", "clouds blocking the Sun"], "Spinning turns places toward and away from the Sun.")
H('9', 3, "The Sun appears to move across the sky each day. What is really happening?", "Earth is rotating", ["the Sun is orbiting Earth daily", "the sky is moving", "the Moon pulls the Sun"], "Earth's rotation makes the Sun seem to move.")
H('9', 3, "A student measures a flagpole's shadow several times during the day. When is the shadow shortest?", "when the Sun is highest in the sky", ["when the Sun is just rising", "when the Sun is just setting", "at midnight"], "The Sun is highest around midday, so shadows are shortest.")
H('9', 3, "It is daytime in Texas. What is it in places on the opposite side of Earth?", "nighttime", ["daytime", "dusk only", "winter always"], "Half of Earth faces the Sun at a time.")
H('9', 3, "In the morning, a tree's shadow points west. Where is the Sun?", "in the east", ["in the west", "directly overhead", "below the horizon in the west"], "Shadows point away from the light source.")
H('9', 4, "Which describes the Sun's apparent path across the sky in the northern hemisphere?", "it rises in the east, moves through the south, and sets in the west", ["it rises in the west and sets in the east", "it stays still", "it rises in the north and sets in the south"], "That is the apparent daily path.")

# ---- 10.A Sun and ocean interact in water cycle and affect weather
H('10.A', 2, "What heats ocean water so it can evaporate?", "the Sun", ["the Moon", "the wind", "ice"], "Sunlight warms the water.")
H('10.A', 3, "Where does most evaporation on Earth happen?", "the ocean", ["a desert", "a cloud", "a mountain top"], "Oceans cover most of Earth.")
H('10.A', 3, "Warm, moist air from an ocean rises, cools, and forms clouds. What can happen next?", "rain or storms", ["a clear sky for weeks", "the ocean freezing", "the Sun going out"], "Condensation can lead to precipitation.")
H('10.A', 3, "A hurricane is powered by what?", "warm ocean water", ["cold air", "ice", "mountains"], "Warm water supplies energy and moisture.")
H('10.A', 3, "Why are coastal areas often milder than inland areas?", "the ocean warms and cools slowly", ["the Sun stops shining there", "ocean water is hot all year", "the wind never blows"], "Water changes temperature slowly.")
H('10.A', 3, "Which sequence shows the water cycle driven by the Sun and ocean?", "evaporation, condensation, precipitation", ["precipitation, condensation, evaporation", "condensation, evaporation, precipitation", "precipitation, evaporation, condensation"], "Ocean water evaporates, forms clouds, and falls as rain.")
H('10.A', 4, "A weather map shows a warm ocean current off the coast. What is MOST likely to happen to humidity near the coast?", "it increases", ["it drops to zero", "it stays frozen", "it has no change ever"], "Warm water increases evaporation.")

# ---- 10.B formation of sedimentary rocks and fossil fuels
H('10.B', 2, "Which kind of rock forms from layers of sediment that are pressed and cemented together?", "sedimentary rock", ["igneous rock", "metamorphic rock", "magma"], "Sedimentary rocks form from compacted sediment.")
H('10.B', 3, "Which is an example of a sedimentary rock?", "sandstone", ["granite", "obsidian", "basalt"], "Sandstone forms from sand.")
H('10.B', 3, "What is the first step in forming sedimentary rock?", "weathering and erosion produce sediment", ["lava cools quickly", "heat melts the rock", "volcanoes erupt"], "Rock is broken into sediment first.")
H('10.B', 3, "Coal formed from what?", "plants that were buried long ago", ["melted metal", "ocean salt", "volcanic ash only"], "Coal comes from buried plant material.")
H('10.B', 3, "Oil and natural gas formed from what?", "tiny sea organisms that died and were buried", ["volcanic glass", "desert sand", "frozen water"], "Heat and pressure changed the remains into fossil fuels.")
H('10.B', 3, "Why are fossil fuels called nonrenewable?", "they take millions of years to form", ["they form in a day", "they can be made in a lab quickly", "they are made from sunlight in minutes"], "Fossil fuels form very slowly.")
H('10.B', 4, "A student models sedimentary rock by pressing layers of wet sand and clay. Which natural force does the pressing represent?", "the weight of layers on top", ["wind blowing across the layers", "the Moon's pull", "ocean tides alone"], "Pressure from overlying layers compacts sediment.")

# ---- 10.C landforms: deltas, canyons, sand dunes
H('10.C', 2, "A canyon is carved mostly by what?", "flowing water", ["falling snow", "the Moon", "a magnet"], "Rivers erode rock over long times.")
H('10.C', 3, "A delta forms where a river meets a larger body of water. What is a delta made of?", "sediment dropped by the river", ["melted ice", "volcanic rock", "wind-blown sand"], "Slowing water deposits sediment.")
H('10.C', 3, "Which landform is created by wind piling sand?", "a sand dune", ["a canyon", "a delta", "a glacier valley"], "Wind deposits sand into dunes.")
H('10.C', 3, "A model uses a tray of sand and a stream of water. What landform can be shown?", "a canyon or delta", ["a volcano only", "a sand dune only", "an island of ice"], "Flowing water erodes and deposits sediment.")
H('10.C', 3, "A glacier moves slowly across land. What does it do to the surface?", "it wears away rock and carries it", ["it makes the surface melt immediately", "it plants trees", "it makes sand dunes"], "Moving ice erodes land.")
H('10.C', 3, "Which landform results from deposition by water?", "a delta", ["a canyon", "a sinkhole", "a mountain peak"], "A delta is built from deposited sediment.")
H('10.C', 4, "A river carries sand and silt. As the river slows at its mouth, what happens to the sediment?", "it settles out and builds up", ["it floats into the sky", "it turns to rock instantly", "it disappears"], "Slow water can not carry as much sediment.")

# ---- 11 natural resources: conservation, recycling, proper disposal
H('11', 2, "Which action helps conserve water?", "turning off the faucet while brushing teeth", ["leaving a hose running", "taking longer showers", "watering the sidewalk"], "Less water use conserves the resource.")
H('11', 3, "A school wants to reduce trash. Which solution would help most?", "set up recycling bins for paper and cans", ["use more disposable plates", "throw all trash in one bin", "burn trash behind the school"], "Recycling reuses materials.")
H('11', 3, "Why is it important to dispose of used motor oil properly?", "oil can pollute soil and water", ["oil is edible", "oil cleans rivers", "oil is renewable"], "Improper disposal contaminates the environment.")
H('11', 3, "Which solution reduces the use of fossil fuels?", "riding a bus instead of driving alone", ["leaving lights on", "idling a car for long times", "driving short trips alone"], "Sharing rides uses less fuel.")
H('11', 3, "How does composting food scraps help the environment?", "it reduces trash and returns nutrients to soil", ["it makes more landfill waste", "it makes plastic", "it removes oxygen from air"], "Food scraps decay into compost.")
H('11', 3, "Which choice reduces waste the MOST?", "using a refillable water bottle", ["buying a new plastic bottle daily", "throwing bottles in a lake", "burning plastic"], "Reusing reduces waste.")
H('11', 4, "A town plans a program to cut landfill use. Which pair of actions would work together best?", "reuse items and recycle paper, glass, and metal", ["burn all trash and bury ash", "ban recycling and reuse", "increase packaging use"], "Reusing and recycling keep materials out of landfills.")

# ---- 12.A organisms interact with biotic and abiotic factors
H('12.A', 2, "Which is an abiotic factor in an ecosystem?", "sunlight", ["a frog", "a tree", "a mushroom"], "Abiotic factors are nonliving.")
H('12.A', 2, "Which is a biotic factor in an ecosystem?", "a bird", ["rain", "soil", "temperature"], "Biotic factors are living things.")
H('12.A', 3, "A cactus needs little water. Which abiotic factor is most important in its desert home?", "limited rainfall", ["abundant clouds", "tall trees", "deep snow"], "A desert has very little rain.")
H('12.A', 3, "A rabbit eats grass and hides from a fox in a bush. Which are biotic factors in this ecosystem?", "the rabbit, grass, fox, and bush", ["the sun and rain only", "the soil and rocks only", "the temperature only"], "Living things are biotic.")
H('12.A', 3, "Fish need dissolved oxygen in a pond. Which is an abiotic factor for the fish?", "oxygen in the water", ["other fish", "pond plants", "snails"], "Oxygen is nonliving.")
H('12.A', 3, "Bees get nectar from flowers, and flowers get pollinated. What kind of interaction is this?", "a helpful relationship between two living things", ["a rock and water relationship", "a sun-and-wind relationship", "an interaction with no living things"], "Both organisms benefit.")
H('12.A', 4, "A pond dries up for several months. Which organism is MOST likely to struggle to survive?", "a fish that lives only in water", ["a cactus nearby", "a desert lizard", "a seed in the soil"], "Fish depend on pond water.")

# ---- 12.B predict ecosystem changes in cycling of matter and flow of energy
H('12.B', 3, "In a food web, snakes eat mice and hawks eat snakes. What will likely happen to the mice if the snakes disappear?", "their number will increase", ["their number will disappear", "they will turn into snakes", "they will stop eating"], "Fewer predators means more prey.")
H('12.B', 3, "A disease kills most of the grass in a field. What is likely to happen to the rabbits?", "their number will decrease", ["their number will rise quickly", "they will become producers", "nothing will change"], "Less food means fewer rabbits.")
H('12.B', 3, "What would happen to the energy in a food web if all the producers died?", "consumers would lose their energy source", ["consumers would gain energy", "decomposers would make sunlight", "nothing would change"], "Producers supply the food energy.")
H('12.B', 3, "Where does the energy in a food web start?", "the Sun", ["the decomposers", "the herbivores", "the carnivores"], "Producers capture sunlight.")
H('12.B', 3, "If decomposers are removed from a forest, what happens to cycling of matter?", "nutrients are not returned to the soil", ["more nutrients return", "matter is created", "energy flows backward"], "Decomposers recycle nutrients.")
H('12.B', 3, "In a food web, owls eat mice and mice eat seeds. If owls are removed, what may happen to the seeds?", "fewer seeds because more mice eat them", ["more seeds because owls eat them", "no change", "the seeds turn into mice"], "More mice would eat more seeds.")
H('12.B', 4, "A drought reduces the number of insects in a food web. Which organism is MOST directly affected?", "a bird that eats mainly insects", ["a tree that makes its own food", "a mushroom", "a rock"], "Insect-eating birds lose food.")

# ---- 12.C healthy ecosystem; human activities
H('12.C', 2, "Which describes a healthy ecosystem?", "it has a variety of organisms and balanced resources", ["it has only one kind of organism", "it has no water", "it has no producers"], "Healthy ecosystems are balanced and varied.")
H('12.C', 3, "Which human activity can help an ecosystem?", "planting native trees", ["dumping trash in a river", "burning forests", "draining all wetlands"], "Native plants support wildlife.")
H('12.C', 3, "Which human activity can harm an ecosystem?", "polluting a stream", ["restoring a wetland", "building a bird feeder", "planting a garden"], "Pollution harms organisms.")
H('12.C', 3, "A town builds a park with native plants and a pond. How might this benefit the ecosystem?", "it provides food and homes for wildlife", ["it removes all animals", "it adds toxic chemicals", "it dries up water sources"], "Habitat supports wildlife.")
H('12.C', 3, "Cutting down a large forest for farmland can lead to what?", "loss of habitat for animals", ["more homes for forest animals", "cleaner air from fewer trees", "more shade"], "Habitat loss harms species.")
H('12.C', 3, "Which action helps keep a river ecosystem healthy?", "keeping chemicals and trash out of the water", ["dumping oil in the river", "building walls of trash", "draining the river"], "Clean water supports organisms.")
H('12.C', 4, "A wildlife group removes an invasive plant that crowds out native plants. How does this help the ecosystem?", "native plants have room to grow, supporting native animals", ["it removes all plants", "it ends the food web", "it adds more invasive species"], "Restoring native plants restores the food web.")

# ---- 13.A structures and functions of different species in the same environment
H('13.A', 3, "Two birds live in the same marsh. One has a long, thin beak and the other has a short, thick beak. Why might both survive there?", "they eat different foods", ["they eat the same food", "their beaks do not matter", "they never need food"], "Different structures let them use different resources.")
H('13.A', 3, "A hawk has sharp talons and an owl has soft feathers for quiet flight. How do these structures help them?", "they help each catch prey in its own way", ["they help them become producers", "they help them make seeds", "they make them stop eating"], "Structures fit the way each hunts.")
H('13.A', 3, "A desert fox has large ears. How do they help it survive?", "they release body heat and help it hear prey", ["they store water", "they make food from sunlight", "they cause rain"], "Large ears cool the fox and sharpen hearing.")
H('13.A', 3, "A duck has webbed feet. What is the function?", "to help it swim", ["to dig for seeds", "to climb trees", "to fly higher"], "Webbed feet push against water.")
H('13.A', 3, "A woodpecker has a strong, sharp beak. What is the function?", "to drill into trees for insects", ["to catch fish", "to crack nuts only", "to filter water"], "The beak is used for drilling into wood.")
H('13.A', 3, "A frog and a heron both live at a pond. The frog catches insects with a sticky tongue and the heron spears fish. Why can both live there?", "they use different structures to get different food", ["they use the same structures", "they do not need food", "they are producers"], "Different structures reduce competition.")
H('13.A', 4, "Two plants grow in the same dry field. One has deep roots and the other has shallow roots that spread wide. How can both survive?", "they get water from different places in the soil", ["they compete for water at the exact same depth", "neither needs water", "they both live on air"], "Different root systems use different water sources.")

# ---- 13.B instinctual and learned behaviors
H('13.B', 2, "Which is an instinctive behavior?", "a baby sea turtle crawling to the ocean", ["a dog learning to roll over", "a chimp learning to use a stick", "a parrot copying words"], "Instincts are inborn.")
H('13.B', 2, "Which is a learned behavior?", "orcas hunting in groups as they are taught by their pod", ["a spider spinning a web", "a bird migrating by instinct", "a baby crying"], "Learned behaviors come from experience or teaching.")
H('13.B', 3, "How do instincts help animals survive?", "they let animals act correctly without being taught", ["they make animals unable to move", "they stop animals from eating", "they make animals sleep all the time"], "Instincts are inborn survival behaviors.")
H('13.B', 3, "A young bird learns where to find food by watching its parents. This is what kind of behavior?", "learned", ["instinctive", "inherited only", "random"], "Watching and practicing is learning.")
H('13.B', 3, "Birds flying south for winter without being taught shows what kind of behavior?", "instinctive", ["learned", "acquired by practice", "a game"], "Migration is inborn in many birds.")
H('13.B', 3, "A dog learns to open a door by pushing a lever after watching its owner. Which kind of behavior is this?", "learned", ["instinctive", "inherited", "not a behavior"], "It was learned from experience.")
H('13.B', 4, "A young otter is taught by its mother to crack shellfish with a rock. How does this increase its chance of survival?", "it can get food it could not otherwise reach", ["it makes the otter weaker", "it helps the otter avoid water", "it makes shellfish stronger"], "The learned skill provides food.")

B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g5_science.jsonl'))
print("saved", len(B.out), "questions")

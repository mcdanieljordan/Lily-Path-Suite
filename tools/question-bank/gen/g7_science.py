#!/usr/bin/env python3
"""Grade 7 Science (TEKS 112.27.b) - original questions, content strands 6-13. Written by hand, 7 per standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.27.b.', 602, own='g7_science.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 6.A elements and compounds
H('6.A', 2, "A substance made of only one kind of atom is called a(n)...", "element", ["compound", "mixture", "solution"], "Elements contain just one type of atom.")
H('6.A', 3, "Water (H2O) is made of hydrogen and oxygen atoms chemically bonded. Water is a...", "compound", ["element", "metal", "mixture of elements"], "Two or more elements bonded in a fixed ratio form a compound.")
H('6.A', 3, "Which is the chemical symbol for sodium?", "Na", ["So", "S", "N"], "Sodium comes from the Latin natrium, symbol Na.")
H('6.A', 3, "What does the chemical formula CO2 tell you?", "each molecule has one carbon atom and two oxygen atoms", ["it has two carbon atoms and one oxygen atom", "it is an element", "it has three carbon atoms"], "The subscript 2 applies to the oxygen only.")
H('6.A', 4, "How is an element different from a compound?", "a compound is made of two or more kinds of atoms bonded together", ["an element is always a gas", "a compound has only one kind of atom", "an element can be broken down by chemical changes into simpler elements"], "Compounds combine different elements; elements cannot be broken down chemically.")
H('6.A', 4, "Which of these is a molecule of an element?", "O2", ["H2O", "NaCl", "CO2"], "O2 has two atoms but both are oxygen.")
H('6.A', 4, "Which pair contains one element and one compound?", "iron (Fe) and table salt (NaCl)", ["gold (Au) and silver (Ag)", "water (H2O) and carbon dioxide (CO2)", "helium (He) and neon (Ne)"], "Fe is an element; NaCl is a compound.")

# ---- 6.B periodic table and formulas
H('6.B', 3, "How many atoms are in one molecule of H2O?", "3", ["2", "1", "4"], "Two hydrogen atoms plus one oxygen atom make three atoms.")
H('6.B', 3, "How many hydrogen atoms are in one molecule of CH4?", "4", ["1", "2", "5"], "The subscript 4 follows the H.")
H('6.B', 3, "Which elements are in the compound NaCl?", "sodium and chlorine", ["nitrogen and carbon", "sulfur and chlorine", "sodium and carbon"], "Na is sodium and Cl is chlorine.")
H('6.B', 4, "How many total atoms are in one molecule of C6H12O6?", "24", ["6", "18", "12"], "6 + 12 + 6 = 24 atoms.")
H('6.B', 4, "In the formula H2SO4, how many oxygen atoms are there?", "4", ["1", "2", "6"], "The subscript after O is 4.")
H('6.B', 4, "A formula contains the symbols C, H and O. Which tool lets you find each element's name and atomic number?", "the periodic table", ["a thermometer", "a ruler", "a graduated cylinder"], "The periodic table lists every element with its symbol and atomic number.")
H('6.B', 4, "In Ca(OH)2, how many hydrogen atoms are there?", "2", ["1", "4", "3"], "The 2 outside the parentheses multiplies both O and H, giving 2 H.")

# ---- 6.C physical and chemical changes
H('6.C', 2, "Which is a physical change?", "ice melting", ["wood burning", "iron rusting", "milk souring"], "Melting changes state but not the substance.")
H('6.C', 3, "Which is a chemical change?", "a nail rusting", ["water freezing", "paper being cut", "sugar dissolving in tea"], "Rust is a new substance.")
H('6.C', 3, "Which observation is a sign of a chemical change?", "bubbles of gas form and a new smell appears", ["a solid is broken into smaller pieces", "a liquid is poured into a new container", "a metal is bent"], "New gas and odor indicate new substances.")
H('6.C', 3, "Crushing a can is a...", "physical change", ["chemical change", "nuclear change", "decomposition"], "The can is the same material, only its shape changed.")
H('6.C', 4, "Baking a cake batter turns it into a solid cake that cannot go back to batter. This is a...", "chemical change", ["physical change", "state change only", "dissolving"], "New substances form that cannot be reversed easily.")
H('6.C', 4, "A student heats sugar and it turns black and smells burnt. What kind of change occurred?", "chemical change", ["physical change", "change in state only", "no change"], "Color change and odor show new substances formed.")
H('6.C', 4, "Which pair lists one physical and one chemical change?", "boiling water; burning a candle", ["melting butter; freezing juice", "rusting a bike; baking bread", "tearing paper; folding paper"], "Boiling is physical, burning is chemical.")

# ---- 6.D solutions
H('6.D', 2, "In salt water, the salt is the...", "solute", ["solvent", "solution", "compound only"], "The solute is what gets dissolved.")
H('6.D', 2, "In salt water, the water is the...", "solvent", ["solute", "mixture", "precipitate"], "The solvent does the dissolving.")
H('6.D', 3, "A student dissolves 5 g of sugar in 100 mL of water and another student dissolves 20 g in 100 mL. Which solution is more concentrated?", "the 20 g solution", ["the 5 g solution", "they are equal", "neither is a solution"], "More solute in the same volume means higher concentration.")
H('6.D', 3, "What happens to concentration when you add more water to a solution?", "it decreases", ["it increases", "it stays the same", "it becomes zero immediately"], "Diluting spreads the solute through more solvent.")
H('6.D', 4, "A drink mix is too strong. Which action dilutes it?", "adding more water", ["adding more mix", "boiling off water", "freezing it"], "Dilution adds solvent.")
H('6.D', 4, "A solution in which water is the solvent is called...", "an aqueous solution", ["a gas solution", "an alloy", "a suspension"], "Aqueous means water-based.")
H('6.D', 4, "One cup of lemonade has 2 spoons of sugar. Another cup of the same size has 4 spoons. What is true?", "the second cup has a higher concentration of sugar", ["the first cup has a higher concentration", "the cups have equal concentration", "the second cup has less solute"], "More solute per volume is more concentrated.")

# ---- 6.E dissolution rate
H('6.E', 3, "Which change makes sugar dissolve faster in water?", "stirring it", ["leaving it still", "using colder water", "using one big lump"], "Agitation brings fresh solvent to the solute.")
H('6.E', 3, "A student dissolves sugar in water at three different temperatures. Which dissolves it fastest?", "the warmest sample", ["the coldest sample", "the same in all three", "none of them"], "Faster-moving particles speed up dissolving.")
H('6.E', 3, "Which dissolves fastest in water?", "powdered sugar", ["a sugar cube", "a large sugar lump", "rock candy"], "Smaller pieces expose more surface area.")
H('6.E', 4, "A student tests how temperature affects dissolving rate. Which variable should stay the same?", "the amount of sugar and water", ["the water temperature", "the dissolving time", "the result"], "Only temperature should change.")
H('6.E', 4, "Crushing a tablet before putting it in water makes it dissolve faster because the crushed pieces have more...", "surface area exposed to the water", ["mass", "volume of water", "weight"], "More exposed surface means more contact with solvent.")
H('6.E', 4, "Which combination would dissolve a solid the fastest?", "warm water, stirring and crushed pieces", ["cold water, no stirring and a large chunk", "cold water, stirring and a large chunk", "warm water, no stirring and a large chunk"], "All three factors speed dissolving.")
H('6.E', 4, "Two cups of the same temperature water get the same amount of salt. One is stirred, one is not. What is the stirred cup showing?", "agitation increases the rate of dissolving", ["temperature affects solubility", "surface area has no effect", "salt is not soluble"], "Stirring was the only difference.")

# ---- 7.A average speed
H('7.A', 2, "What is the formula for average speed?", "distance divided by time", ["time divided by distance", "distance times time", "mass divided by volume"], "Speed = distance / time.")
H('7.A', 3, "A cyclist rides 30 km in 2 hours. What is the average speed?", "15 km/h", ["60 km/h", "32 km/h", "28 km/h"], "30 / 2 = 15.")
H('7.A', 3, "A runner travels 100 m in 20 seconds. What is the average speed?", "5 m/s", ["20 m/s", "2000 m/s", "0.2 m/s"], "100 / 20 = 5.")
H('7.A', 3, "A car goes 240 km at 60 km/h. How long does the trip take?", "4 hours", ["14,400 hours", "0.25 hours", "300 hours"], "Time = distance / speed = 240 / 60.")
H('7.A', 4, "A train travels 90 km in 1.5 hours. What is its average speed?", "60 km/h", ["135 km/h", "90 km/h", "6 km/h"], "90 / 1.5 = 60.")
H('7.A', 4, "A student walks 400 m in 5 minutes. What distance does the student walk in 1 minute at the same speed?", "80 m", ["2000 m", "395 m", "405 m"], "400 / 5 = 80.")
H('7.A', 4, "A boat moves at 12 km/h for 3 hours. How far does it travel?", "36 km", ["4 km", "15 km", "9 km"], "Distance = speed x time.")

# ---- 7.B speed vs velocity
H('7.B', 3, "Which statement describes velocity?", "speed in a given direction", ["speed without direction", "distance only", "acceleration only"], "Velocity includes direction.")
H('7.B', 3, "A car travels 50 km/h north. This describes the car's...", "velocity", ["speed only", "mass", "displacement only"], "A direction is included.")
H('7.B', 4, "A runner jogs once around a 400 m track and returns to the starting point. What is her displacement?", "0 m", ["400 m", "200 m", "800 m"], "Displacement is the straight-line change in position, which is zero.")
H('7.B', 4, "A person walks 3 m east and then 3 m west. How far did the person travel (distance)?", "6 m", ["0 m", "3 m", "9 m"], "Distance adds the path lengths.")
H('7.B', 4, "A person walks 3 m east and then 3 m west. What is the displacement?", "0 m", ["6 m", "3 m east", "3 m west"], "The person ends where they started.")
H('7.B', 4, "Two cars both go 60 km/h, one east and one west. What is true?", "they have the same speed but different velocities", ["they have the same velocity", "they have different speeds", "they are not moving"], "Direction differs.")
H('7.B', 3, "Which measurement needs a direction to be complete?", "displacement", ["distance", "time", "speed"], "Displacement is a vector.")

# ---- 7.C distance-time graphs
H('7.C', 2, "On a distance-time graph, a horizontal line means the object is...", "not moving", ["speeding up", "moving at constant speed", "moving backward"], "Distance is not changing.")
H('7.C', 3, "On a distance-time graph, a straight line sloping upward means the object moves at...", "constant speed", ["constant acceleration", "no speed", "decreasing speed"], "Equal distance in equal time.")
H('7.C', 3, "A steeper line on a distance-time graph shows a...", "faster speed", ["slower speed", "stopped object", "smaller distance"], "A greater slope is more speed.")
H('7.C', 4, "A graph shows 0 m at 0 s and 20 m at 4 s as a straight line. What is the speed?", "5 m/s", ["80 m/s", "24 m/s", "0.2 m/s"], "20 / 4 = 5.")
H('7.C', 4, "A distance-time graph rises, then goes flat, then rises again. What happened?", "the object moved, stopped, then moved again", ["the object slowed to a stop for good", "the object moved backward", "the object kept the same speed throughout"], "The flat part means no change in distance.")
H('7.C', 4, "The slope of a distance-time graph represents the object's...", "speed", ["mass", "weight", "energy"], "Slope = rise / run = distance / time.")
H('7.C', 4, "Two lines on one graph: Line A is steeper than Line B. Which object is faster?", "Object A", ["Object B", "neither", "they are equal"], "A steeper line means more distance per second.")

# ---- 7.D Newton's first law
H('7.D', 2, "Newton's First Law says an object at rest stays at rest unless acted on by a(n)...", "unbalanced force", ["balanced force", "small force", "magnet"], "A net force is needed to change motion.")
H('7.D', 3, "Balanced forces on an object cause the object's motion to...", "stay the same", ["speed up", "reverse", "stop immediately"], "Net force is zero.")
H('7.D', 3, "A book sits on a table. Gravity pulls down and the table pushes up equally. The forces are...", "balanced", ["unbalanced", "absent", "friction only"], "Equal and opposite forces cancel.")
H('7.D', 3, "A hockey puck slides on ice, slowly stopping. What unbalanced force slows it?", "friction", ["gravity pulling sideways", "balanced forces", "no force"], "Friction opposes sliding.")
H('7.D', 4, "Why do passengers lurch forward when a car brakes suddenly?", "their bodies tend to keep moving at the same speed", ["the seat pushes them forward", "gravity pulls them forward", "the car pulls them"], "Inertia keeps them moving.")
H('7.D', 4, "A cart is pushed with 10 N to the right and 10 N to the left. What happens?", "the cart does not change its motion", ["it speeds up right", "it speeds up left", "it spins"], "Net force is 0 N.")
H('7.D', 4, "A cart is pushed with 15 N to the right and 5 N to the left. What is the net force?", "10 N to the right", ["20 N to the right", "10 N to the left", "0 N"], "15 - 5 = 10 in the larger direction.")

# ---- 8.A thermal energy transfer
H('8.A', 2, "Heat transfer through direct contact between objects is called...", "conduction", ["convection", "radiation", "reflection"], "Particles collide and pass energy along.")
H('8.A', 3, "Heat transfer by the movement of fluids such as air or water is called...", "convection", ["conduction", "radiation", "friction"], "Warm fluid rises while cooler fluid sinks.")
H('8.A', 3, "Heat from the Sun reaches Earth by...", "radiation", ["conduction", "convection", "friction"], "Radiation can travel through empty space.")
H('8.A', 3, "A metal spoon in hot soup becomes hot. This is mainly...", "conduction", ["convection", "radiation", "evaporation"], "The spoon touches the hot soup.")
H('8.A', 4, "Warming your hands near a campfire without touching it is mostly...", "radiation", ["conduction", "convection", "condensation"], "Energy travels as waves.")
H('8.A', 4, "A pot of water is heated from below. Warm water rises and cool water sinks. This circulation is...", "a convection current", ["a conduction current", "radiation", "a density wave"], "Fluids move in loops when heated.")
H('8.A', 4, "Why are cooking pots often made of metal?", "metals conduct thermal energy well", ["metals radiate energy only", "metals are convection fluids", "metals never get hot"], "Good conductors transfer energy quickly.")

# ---- 8.B thermal equilibrium
H('8.B', 2, "Thermal energy naturally moves from...", "warmer objects to cooler objects", ["cooler to warmer objects", "equal temperatures only", "nowhere"], "Energy flows down the temperature difference.")
H('8.B', 3, "A hot cup of cocoa is left on a table. What happens to its temperature?", "it decreases until it matches the room", ["it increases", "it stays hot forever", "it drops below room temperature"], "It reaches thermal equilibrium with its surroundings.")
H('8.B', 3, "An ice cube is dropped in a glass of warm water. Which way does thermal energy move?", "from the water to the ice", ["from the ice to the water", "neither way", "out of the glass only"], "Warm water is the energy source.")
H('8.B', 3, "Thermal equilibrium means two objects in contact have the same...", "temperature", ["mass", "volume", "color"], "No net energy flows once temperatures are equal.")
H('8.B', 4, "A hot piece of metal at 90 C is placed in 20 C water. The final temperature of both will be...", "between 20 C and 90 C", ["above 90 C", "below 20 C", "exactly 90 C"], "They meet at an in-between temperature.")
H('8.B', 4, "Once two objects reach thermal equilibrium, thermal energy...", "has no net flow between them", ["flows faster", "moves toward the colder one", "stops existing"], "Energy transfer balances out.")
H('8.B', 4, "A can of soda is placed in a cooler of ice. Which is a correct prediction?", "the soda cools as it gives energy to the ice", ["the soda warms the ice and stays the same", "the ice cools the soda by taking cold from it", "the ice warms because it gains cold"], "Energy leaves the warmer soda.")

# ---- 8.C temperature and kinetic energy
H('8.C', 2, "Temperature measures the average...", "kinetic energy of the particles", ["mass of the particles", "volume of the sample", "color of the substance"], "Hotter means faster-moving particles.")
H('8.C', 3, "When the temperature of a gas rises, its particles...", "move faster", ["move slower", "stop moving", "disappear"], "Higher temperature means more kinetic energy.")
H('8.C', 3, "Particles in a cold liquid compared with a warm liquid move...", "more slowly", ["more quickly", "at the same speed", "in straight lines only"], "Less kinetic energy at lower temperature.")
H('8.C', 3, "As a solid is heated, its particles...", "vibrate faster", ["stop vibrating", "stay perfectly still", "turn into energy"], "Energy increases the vibration.")
H('8.C', 4, "Which sample has the highest average particle kinetic energy?", "water at 80 C", ["water at 40 C", "water at 10 C", "water at 0 C"], "The warmest sample has the fastest particles.")
H('8.C', 4, "Absolute zero is the temperature at which particle motion is...", "at a minimum", ["at a maximum", "random", "doubled"], "Particles have almost no kinetic energy.")
H('8.C', 4, "Two beakers hold equal masses of water: one at 25 C and one at 75 C. Which statement is correct?", "the particles in the 75 C beaker move faster on average", ["the particles in the 25 C beaker move faster", "particles in both move at the same speed", "particles in the 75 C beaker are larger"], "Higher temperature, faster particles.")

# ---- 9.A solar system objects
H('9.A', 2, "What is at the center of our solar system?", "the Sun", ["Jupiter", "Earth", "the Moon"], "All planets orbit the Sun.")
H('9.A', 3, "Which is the largest planet in our solar system?", "Jupiter", ["Earth", "Mars", "Neptune"], "Jupiter is the largest of all.")
H('9.A', 3, "Where is the asteroid belt located?", "between Mars and Jupiter", ["beyond Neptune", "between Earth and Venus", "around the Sun only"], "Rocky bodies orbit in that region.")
H('9.A', 3, "A comet gets a visible tail when it approaches the Sun because...", "ices vaporize and are pushed away by the solar wind", ["it spins faster", "its rocks melt", "it gets magnetized"], "Heat releases gas and dust.")
H('9.A', 4, "Which region is a band of icy objects beyond Neptune?", "the Kuiper belt", ["the asteroid belt", "the Oort cloud", "the inner planets"], "The Kuiper belt includes Pluto-like icy bodies.")
H('9.A', 4, "The Oort cloud is thought to be...", "a distant spherical shell of icy objects surrounding the solar system", ["a ring around Saturn", "a belt between Mars and Jupiter", "a cloud of gas near Earth"], "It is the source of some long-period comets.")
H('9.A', 4, "A meteor is...", "the streak of light from a space rock burning up in Earth's atmosphere", ["a rock on Earth's surface", "a planet", "a moon of Jupiter"], "Friction with air makes it glow.")

# ---- 9.B gravity
H('9.B', 2, "What force keeps planets in orbit around the Sun?", "gravity", ["magnetism", "friction", "wind"], "The Sun's gravity pulls the planets.")
H('9.B', 3, "Gravity between two objects depends on their...", "masses and the distance between them", ["colors", "temperatures", "ages"], "More mass or less distance means stronger gravity.")
H('9.B', 3, "What keeps the Moon in orbit around Earth?", "Earth's gravity", ["the Sun's magnetism", "friction", "solar wind"], "Gravity continually pulls the Moon toward Earth.")
H('9.B', 4, "As the distance between two objects increases, the gravitational force between them...", "decreases", ["increases", "stays the same", "doubles"], "Gravity weakens with distance.")
H('9.B', 4, "Why do planets closer to the Sun orbit faster?", "the Sun's gravity is stronger at shorter distances", ["they are made of denser rock", "they are lighter", "there is no gravity far away"], "Stronger pull requires faster motion to stay in orbit.")
H('9.B', 4, "Which object has the strongest gravitational pull on Earth?", "the Sun", ["the Moon", "Mars", "Jupiter"], "Its huge mass keeps Earth in orbit even at a great distance.")
H('9.B', 4, "If Earth's gravity suddenly vanished, what would happen to the Moon?", "it would travel in a straight line away", ["it would crash into Earth", "it would keep orbiting", "it would stop"], "Without a centripetal pull, inertia carries it straight.")

# ---- 9.C conditions for life
H('9.C', 2, "Which is needed for life as we know it?", "liquid water", ["extreme heat", "no atmosphere", "complete darkness"], "Life needs liquid water.")
H('9.C', 3, "Earth's distance from the Sun is important for life because it...", "allows liquid water to exist", ["makes Earth the largest planet", "keeps it frozen", "stops all radiation"], "Not too hot and not too cold.")
H('9.C', 3, "The ozone layer in Earth's atmosphere helps life by...", "absorbing harmful ultraviolet radiation", ["creating oxygen", "making rain", "warming the oceans"], "UV can damage living cells.")
H('9.C', 3, "Which gas makes up most of Earth's atmosphere?", "nitrogen", ["oxygen", "carbon dioxide", "hydrogen"], "About 78% is nitrogen.")
H('9.C', 4, "Why is the greenhouse effect important for life on Earth?", "it traps heat that keeps the planet warm enough", ["it blocks all sunlight", "it removes oxygen", "it cools the planet"], "Without it Earth would be far colder.")
H('9.C', 4, "Venus is too hot for liquid water because it is...", "close to the Sun and has a very thick carbon dioxide atmosphere", ["too far from the Sun", "too small", "made of ice"], "Its atmosphere traps heat.")
H('9.C', 4, "Mars is too cold for liquid water on the surface mainly because it...", "has a thin atmosphere and is farther from the Sun", ["is closer to the Sun", "has too much oxygen", "has no gravity"], "Little heat is retained.")

# ---- 10.A evidence Earth has changed
H('10.A', 2, "Remains or traces of ancient organisms preserved in rock are called...", "fossils", ["minerals", "magma", "sediments"], "Fossils show life in the past.")
H('10.A', 3, "The law of superposition says that in undisturbed rock layers, the oldest layer is...", "at the bottom", ["at the top", "in the middle", "always the thickest"], "New layers form on top of older ones.")
H('10.A', 3, "Fossils of sea creatures are found on a mountaintop. What does this suggest?", "the area was once under the ocean", ["the sea creatures climbed", "the mountain is new", "the fossils are fake"], "Land has been uplifted over time.")
H('10.A', 3, "South America and Africa have coastlines that fit together and matching fossils. This supports...", "plate tectonics", ["superposition", "the greenhouse effect", "tides"], "They were once joined.")
H('10.A', 4, "A scientist finds Layer A beneath Layer B in undisturbed rock. Which is true?", "Layer A is older than Layer B", ["Layer B is older than Layer A", "they are the same age", "the order cannot be known"], "The lower layer was deposited first.")
H('10.A', 4, "Why are fossils useful for studying Earth's history?", "they show what organisms and environments existed long ago", ["they change the age of rocks", "they are always in igneous rock", "they create new layers"], "They record ancient life.")
H('10.A', 4, "Identical rock types and mountain chains on different continents can be explained by...", "continents having once been connected", ["coincidence only", "volcanoes", "the Moon's pull"], "Plate motion split a former landmass.")

# ---- 10.B plate tectonics effects
H('10.B', 2, "Earth's crust is broken into large slabs called...", "tectonic plates", ["layers of the mantle", "ocean currents", "mineral veins"], "Plates float and move on the mantle.")
H('10.B', 3, "Where two plates collide, what can form?", "mountains", ["oceans only", "deserts", "tides"], "Collision crumples crust upward.")
H('10.B', 3, "Earthquakes mostly happen...", "along plate boundaries", ["in the center of plates only", "at the poles", "in oceans only"], "Plates stick, then slip along faults.")
H('10.B', 3, "Where two plates move apart under the ocean, what forms?", "new ocean crust and eventually an ocean basin", ["a mountain range", "a trench only", "a desert"], "Magma rises and cools in the gap.")
H('10.B', 4, "A chain of islands like Hawaii forms as a plate moves over a stationary...", "hot spot", ["trench", "fault", "glacier"], "Magma rises from deep in the mantle.")
H('10.B', 4, "A supervolcano is a volcano capable of...", "an extremely large eruption affecting the climate", ["a tiny eruption", "producing no ash", "forming only on the Moon"], "Ash can block sunlight globally.")
H('10.B', 4, "At a subduction zone, one plate sinks beneath another. Which feature often results?", "volcanoes and deep ocean trenches", ["sand dunes", "river deltas", "glaciers"], "Melting rock rises to form volcanoes.")

# ---- 11.A human activity and water
H('11.A', 2, "An area of land that drains into a river, lake or ocean is a...", "watershed", ["desert", "plateau", "glacier"], "All the water in it flows to one outlet.")
H('11.A', 3, "Fertilizer from lawns washing into a stream is an example of...", "a harmful influence on surface water", ["a benefit to water quality", "groundwater recharge", "evaporation"], "Nutrients can cause algae blooms.")
H('11.A', 3, "Which action benefits a watershed?", "planting trees along a stream", ["dumping oil down storm drains", "paving over wetlands", "overusing fertilizer"], "Roots hold soil and filter runoff.")
H('11.A', 3, "Pumping groundwater faster than it is replaced can cause...", "wells to run dry", ["floods", "more rain", "cleaner water"], "The water table drops.")
H('11.A', 4, "Why does paving large areas increase flooding?", "water cannot soak into the ground", ["pavement absorbs water", "pavement creates rain", "pavement filters runoff"], "More runoff reaches streams quickly.")
H('11.A', 4, "A dam can help a community by...", "storing water and providing electricity", ["increasing erosion downstream", "making rivers wider", "eliminating all fish"], "Dams store water and can power turbines.")
H('11.A', 4, "A leaking underground fuel tank is most likely to harm...", "groundwater", ["the atmosphere only", "the Moon", "the mantle"], "Pollutants seep through soil into aquifers.")

# ---- 11.B oceans
H('11.B', 2, "Which resource do people get from the ocean?", "food", ["coal", "lumber", "granite"], "Fish and shellfish are major food sources.")
H('11.B', 3, "Ocean currents affect climate because they...", "move heat around Earth", ["stop winds", "make rain only", "cool the Sun"], "Warm and cold currents change coastal temperatures.")
H('11.B', 3, "Plastic trash in the ocean harms marine life because animals may...", "eat it or get tangled in it", ["grow faster", "use it as food safely", "breathe it"], "Debris injures and kills animals.")
H('11.B', 4, "Oil spills at sea hurt wildlife by...", "coating feathers and fur and poisoning food webs", ["adding oxygen to the water", "cooling the water", "feeding plankton"], "Oil damages animals and ecosystems.")
H('11.B', 4, "Overfishing is a problem because it...", "reduces fish populations faster than they can recover", ["adds fish to the ocean", "cleans the water", "stops tides"], "Populations collapse.")
H('11.B', 4, "Rising levels of carbon dioxide are making oceans more acidic, which harms...", "organisms with shells and coral skeletons", ["sunlight", "the tides", "sand"], "Acid dissolves calcium carbonate.")
H('11.B', 3, "People depend on oceans for transportation by using...", "shipping routes", ["underwater tunnels only", "glaciers", "volcanoes"], "Most goods move across the sea by ship.")

# ---- 12.A energy pyramids
H('12.A', 2, "In a food chain, the organisms that make their own food are called...", "producers", ["consumers", "decomposers", "predators"], "Producers capture energy from sunlight.")
H('12.A', 3, "In an energy pyramid, the amount of available energy...", "decreases at each higher level", ["increases at each higher level", "stays the same", "doubles"], "Energy is lost as heat at each level.")
H('12.A', 3, "About how much energy is passed to the next trophic level?", "about 10 percent", ["about 90 percent", "about 50 percent", "100 percent"], "Roughly 90 percent is lost.")
H('12.A', 3, "In the chain grass, grasshopper, frog, hawk, which organism has the least available energy?", "the top predator", ["the producer", "the grasshopper", "the frog"], "It is at the top of the pyramid.")
H('12.A', 4, "If grass in a food chain has 10,000 units of energy, about how much reaches the secondary consumer?", "100 units", ["1,000 units", "10 units", "5,000 units"], "10,000 x 0.1 x 0.1 = 100.")
H('12.A', 4, "Why are there usually fewer top predators than herbivores?", "less energy is available at higher levels", ["predators are smaller", "predators eat only plants", "herbivores eat predators"], "The energy pyramid limits numbers.")
H('12.A', 4, "In which direction do arrows point in a food web diagram?", "from the organism eaten to the organism that eats it", ["from the eater to the eaten", "toward the Sun only", "randomly"], "Arrows show energy flow.")

# ---- 12.B energy flow and recycling
H('12.B', 2, "What is the original source of energy for most ecosystems?", "the Sun", ["the wind", "the soil", "the Moon"], "Producers capture sunlight.")
H('12.B', 3, "Which organisms break down dead matter and return nutrients to the soil?", "decomposers", ["producers", "herbivores", "predators"], "Fungi and bacteria recycle matter.")
H('12.B', 3, "Energy in an ecosystem flows in one direction, but matter is...", "recycled", ["destroyed", "created", "unchanged"], "Atoms are reused.")
H('12.B', 3, "Which process returns carbon dioxide to the atmosphere?", "cellular respiration", ["photosynthesis", "condensation", "erosion"], "Organisms release CO2 as they use energy.")
H('12.B', 4, "Plants take carbon dioxide from the air to make sugars by...", "photosynthesis", ["respiration", "decomposition", "evaporation"], "Light energy drives the process.")
H('12.B', 4, "What would happen if all decomposers in a forest disappeared?", "dead material would pile up and nutrients would not be recycled", ["the forest would grow faster", "more oxygen would form", "the soil would get richer"], "Nutrients would stay locked in dead matter.")
H('12.B', 4, "Nitrogen-fixing bacteria help ecosystems by...", "converting nitrogen gas into forms plants can use", ["producing sunlight", "removing carbon", "eating plants"], "Plants need usable nitrogen.")

# ---- 13.A human body systems
H('13.A', 2, "Which system carries blood throughout the body?", "circulatory system", ["skeletal system", "digestive system", "urinary system"], "The heart pumps blood through vessels.")
H('13.A', 2, "Which system takes in oxygen and releases carbon dioxide?", "respiratory system", ["muscular system", "excretory system", "skeletal system"], "The lungs exchange gases.")
H('13.A', 3, "The main function of the skeletal system is to...", "support the body and protect organs", ["digest food", "carry messages", "pump blood"], "Bones provide structure.")
H('13.A', 3, "Which system breaks food into nutrients the body can absorb?", "digestive system", ["urinary system", "circulatory system", "respiratory system"], "Digestion occurs in the stomach and intestines.")
H('13.A', 3, "Kidneys filter waste from blood. They belong to the...", "urinary system", ["digestive system", "muscular system", "skeletal system"], "The urinary system removes liquid waste.")
H('13.A', 4, "Muscles can only pull, not push. How do they move bones?", "muscles contract and pull on bones attached to them", ["muscles push bones", "bones move on their own", "muscles inflate"], "Pairs of muscles work in opposite directions.")
H('13.A', 4, "Which two systems work together to deliver oxygen to body cells?", "respiratory and circulatory", ["skeletal and digestive", "muscular and urinary", "digestive and reproductive"], "Lungs take in oxygen and blood carries it.")

# ---- 13.B levels of organization
H('13.B', 2, "What is the basic unit of structure and function in all living things?", "cell", ["tissue", "organ", "organism"], "Cells are the smallest living units.")
H('13.B', 3, "Which is the correct order from simplest to most complex?", "cell, tissue, organ, organ system", ["organ, cell, tissue, system", "tissue, cell, organ, system", "organ system, organ, tissue, cell"], "Each level is built from the previous one.")
H('13.B', 3, "A group of similar cells that work together is called a...", "tissue", ["organ", "organism", "system"], "Muscle tissue is one example.")
H('13.B', 3, "The heart is an example of a(n)...", "organ", ["cell", "tissue", "organism"], "Several tissues work together in the heart.")
H('13.B', 4, "In a plant, which of these is an organ?", "leaf", ["chloroplast", "cell wall", "guard cell"], "A leaf is made of several tissues.")
H('13.B', 4, "A stomach, small intestine and liver are parts of what?", "an organ system", ["a tissue", "a single cell", "a population"], "Together they carry out digestion.")
H('13.B', 4, "Which sequence correctly shows organization in an animal?", "muscle cell, muscle tissue, heart, circulatory system", ["heart, muscle cell, tissue, system", "circulatory system, heart, tissue, cell", "tissue, heart, cell, system"], "Each level contains the previous one.")

# ---- 13.C asexual vs sexual reproduction
H('13.C', 2, "Which type of reproduction involves only one parent?", "asexual", ["sexual", "both", "neither"], "A single parent produces offspring.")
H('13.C', 3, "Offspring of asexual reproduction are usually...", "genetically identical to the parent", ["very different from the parent", "twice as large", "always different from each other"], "No genetic mixing occurs.")
H('13.C', 3, "Sexual reproduction produces offspring with...", "a mix of traits from two parents", ["traits from one parent only", "no traits", "identical traits to one sibling"], "It increases variation.")
H('13.C', 3, "Which is an example of asexual reproduction?", "a strawberry plant sending out runners", ["a bird laying eggs after mating", "a dog giving birth", "a flower pollinated by bees"], "Runners grow into new plants.")
H('13.C', 4, "Why is variation from sexual reproduction helpful to a population?", "some individuals may survive changes in the environment", ["all offspring are identical", "it stops mutations", "it reduces the population"], "Diversity improves the chance of survival.")
H('13.C', 4, "A disease kills one clonal population of plants. Why might a sexually reproducing population survive better?", "some individuals may have resistance", ["they are all identical", "they never get sick", "they do not need water"], "Variation includes resistance.")
H('13.C', 4, "A bacterium divides into two cells. This is...", "asexual reproduction", ["sexual reproduction", "pollination", "fertilization"], "One cell makes two copies.")

# ---- 13.D selection
H('13.D', 2, "Farmers choosing the largest corn plants to breed is an example of...", "artificial selection", ["natural selection", "mutation", "extinction"], "Humans choose which organisms breed.")
H('13.D', 3, "Natural selection means organisms with helpful traits are more likely to...", "survive and reproduce", ["die before reproducing", "become identical", "stop changing"], "Their traits become more common.")
H('13.D', 3, "Dog breeds like greyhounds and bulldogs came about through...", "artificial selection", ["natural selection only", "hot spots", "photosynthesis"], "People bred for desired traits.")
H('13.D', 4, "Bacteria exposed to an antibiotic: a few survive and multiply. Over time the population is...", "mostly resistant", ["mostly vulnerable", "extinct", "unchanged"], "Resistant bacteria passed on their traits.")
H('13.D', 4, "Peppered moths in a polluted forest: dark moths were harder for birds to see. What happened over generations?", "dark moths became more common", ["light moths became more common", "all moths died", "no change occurred"], "Camouflaged individuals survived and reproduced.")
H('13.D', 4, "What is the main difference between natural and artificial selection?", "in artificial selection humans choose which individuals breed", ["natural selection needs humans", "artificial selection happens without choice", "there is no difference"], "Nature selects in the first, people in the second.")
H('13.D', 3, "Which trait would be an advantage for a desert plant?", "thick stems that store water", ["large thin leaves", "shallow roots only", "no waxy coating"], "Water conservation helps survival.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g7_science.jsonl'))
print("saved", len(B.out), "questions")

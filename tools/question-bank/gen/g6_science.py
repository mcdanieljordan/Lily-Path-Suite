#!/usr/bin/env python3
"""Grade 6 Science (TEKS 112.26.b) - original questions, content strands 6-13 (strands 1-5 are practices/themes, skipped).
   Run: python3 gen/g6_science.py  -> batches/g6_science.jsonl   Written by hand, 7 per standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.26.b.', 601, own='g6_science.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 6.A solids, liquids, gases
H('6.A', 2, "Which state of matter has a definite shape and a definite volume?", "solid", ["liquid", "gas", "plasma only"], "Particles in a solid are locked in place, so it keeps both its shape and its volume.")
H('6.A', 3, "A sealed balloon is squeezed into a smaller space and the gas inside takes up less volume. Why can the gas be compressed so easily?", "its particles are far apart", ["its particles are locked together", "its particles have no energy", "its particles are heavier than a solid's"], "Gas particles have lots of empty space between them.")
H('6.A', 3, "Water is poured from a tall glass into a wide bowl. What happens to its shape and volume?", "shape changes, volume stays the same", ["shape stays the same, volume changes", "both change", "neither changes"], "A liquid takes the shape of its container but keeps its volume.")
H('6.A', 3, "Compared with the particles in ice, the particles in water vapor have...", "more kinetic energy", ["less kinetic energy", "the same kinetic energy", "no kinetic energy"], "Gas particles move fastest, so they have the most kinetic energy.")
H('6.A', 3, "Which statement describes the particles in a liquid?", "they stay close together but slide past each other", ["they are fixed in rigid positions", "they are far apart and move freely", "they do not move at all"], "Liquid particles are close but can flow.")
H('6.A', 4, "A solid is heated until it melts. What happens to the motion of its particles as the thermal energy increases?", "they move faster and break free of fixed positions", ["they stop moving", "they move slower and pack tighter", "they disappear"], "Added energy speeds particles up so they can slide past each other.")
H('6.A', 4, "A student sees that a gas always fills its whole container, while a liquid does not. What explains the difference?", "gas particles spread out because they move freely with little attraction", ["gas particles are larger than liquid particles", "liquids have more kinetic energy", "gas particles are attracted strongly to each other"], "Weak attractions let gas particles spread out to fill any space.")

# ---- 6.B pure substances and mixtures
H('6.B', 2, "Which of these is a pure substance?", "distilled water", ["salt water", "soil", "trail mix"], "A pure substance has just one kind of matter; distilled water is only H2O.")
H('6.B', 3, "Sugar is stirred into water until it can no longer be seen. This kind of mixture is called a...", "solution", ["heterogeneous mixture", "pure substance", "compound"], "A homogeneous mixture (solution) looks the same throughout.")
H('6.B', 3, "A bowl of cereal with milk has separate pieces you can see. Which kind of matter is it?", "heterogeneous mixture", ["homogeneous mixture", "pure substance", "element"], "The parts are not evenly mixed and can be seen.")
H('6.B', 3, "Which is a homogeneous mixture?", "air", ["a salad", "a pizza", "gravel and sand"], "Air looks uniform throughout, with gases evenly mixed.")
H('6.B', 4, "Iron filings and sand are mixed together. Which method separates them using a physical property?", "using a magnet", ["boiling the mixture", "burning the mixture", "adding more sand"], "Iron is magnetic and sand is not.")
H('6.B', 3, "Which is a way to separate saltwater into salt and water?", "evaporating the water", ["using a magnet", "using a ruler", "adding more salt"], "Heating drives off the water and leaves the salt behind.")
H('6.B', 4, "Gold melts at a specific temperature, and the melted gold has the same properties as the solid. This suggests gold is a...", "pure substance", ["mixture", "solution of several metals", "heterogeneous mixture"], "Pure substances have fixed, consistent properties.")

# ---- 6.C periodic table
H('6.C', 2, "Most elements on the periodic table are...", "metals", ["nonmetals", "metalloids", "gases"], "The majority of elements are metals.")
H('6.C', 3, "A shiny element that is easily shaped and conducts electricity well is most likely a...", "metal", ["nonmetal", "noble gas", "gas"], "Luster, malleability and conductivity are metal properties.")
H('6.C', 3, "An element is brittle when solid, dull, and a poor conductor of heat. It is most likely a...", "nonmetal", ["metal", "metalloid", "rare Earth element"], "Brittle, dull and poor conductivity describe nonmetals.")
H('6.C', 3, "Silicon has properties between those of metals and nonmetals. It is classified as a...", "metalloid", ["metal", "nonmetal", "halogen only"], "Metalloids have mixed properties.")
H('6.C', 4, "Silicon is used in computer chips because it can conduct electricity under some conditions but not others. This is a property of a...", "metalloid", ["noble gas", "halogen", "alkali metal"], "Metalloids are semiconductors.")
H('6.C', 3, "Rare Earth elements are important in modern life because they are used in...", "magnets and electronics such as phones", ["paper and cardboard", "bread and pasta", "plain glass jars"], "Rare Earth elements are used in strong magnets, screens and batteries.")
H('6.C', 3, "Copper is used for electrical wires because it is...", "a good conductor of electricity", ["a poor conductor of electricity", "a nonmetal", "very brittle"], "Copper is a metal that conducts electricity well.")

# ---- 6.D density
H('6.D', 3, "A block of wood floats on water, but a rock of the same size sinks. Which has the greater density?", "the rock", ["the wood", "they are equal", "neither"], "Objects denser than the fluid sink; less dense objects float.")
H('6.D', 3, "An object has a mass of 20 g and a volume of 10 cm³. What is its density?", "2 g/cm³", ["0.5 g/cm³", "10 g/cm³", "30 g/cm³"], "Density = mass ÷ volume = 20 ÷ 10.")
H('6.D', 4, "Oil floats on top of water. What does this show?", "oil is less dense than water", ["oil is heavier than water", "water is lighter than oil", "oil has more mass in each cm³"], "Less dense liquids float on denser ones.")
H('6.D', 4, "A liquid has a density of 1.5 g/mL. A ball with a density of 1.2 g/mL is placed in it. What happens?", "the ball floats", ["the ball sinks", "the ball dissolves", "the ball stays at the bottom"], "The ball is less dense than the liquid.")
H('6.D', 4, "A student has 50 g of lead and 50 g of foam. The foam takes up much more space. What does this show?", "foam is less dense than lead", ["foam is denser than lead", "they have equal density", "lead has less mass"], "The same mass in a larger volume means lower density.")
H('6.D', 3, "A steel ship floats even though steel is denser than water. Why?", "the ship's overall shape holds air, lowering its average density", ["steel gets lighter in water", "water is denser than air", "the ship has no mass"], "The ship's hollow shape makes its overall density less than water.")
H('6.D', 4, "Three floating objects have densities of 0.2 g/cm³, 0.6 g/cm³ and 0.9 g/cm³. Which one floats highest in water?", "the 0.2 g/cm³ object", ["the 0.6 g/cm³ object", "the 0.9 g/cm³ object", "all float at the same height"], "The least dense object floats highest.")

# ---- 6.E chemical change
H('6.E', 2, "Which is evidence of a chemical change?", "bubbles of gas forming when two substances mix", ["ice melting", "paper being cut", "sugar dissolving"], "A new gas forming is a sign of a new substance.")
H('6.E', 3, "A match burns and gives off heat and light. What type of change is this?", "chemical change", ["physical change", "state change only", "no change"], "Burning forms new substances and releases energy.")
H('6.E', 3, "Mixing baking soda and vinegar makes fizzing bubbles. What does this show?", "a new substance, a gas, was formed", ["the vinegar evaporated", "a solid was cut", "a mixture was separated"], "Gas production is evidence of a chemical change.")
H('6.E', 3, "A cut apple turns brown. This is most likely a...", "chemical change", ["physical change", "change of state", "change in shape only"], "A color change from reacting with oxygen forms a new substance.")
H('6.E', 4, "Which is a physical change rather than a chemical change?", "chopping wood into small pieces", ["wood burning in a fire", "iron rusting", "a banana ripening"], "Chopping changes size, not the type of substance.")
H('6.E', 4, "Two clear liquids are mixed and a solid forms in the cup. What is the solid called?", "a precipitate", ["a solution", "a mixture", "an element"], "A solid formed from liquids in a chemical reaction is a precipitate.")
H('6.E', 4, "A cold pack gets cold when its chemicals are mixed. Which evidence of chemical change is this?", "a change in thermal energy", ["a change in shape", "a change in size", "a change in volume of the pack"], "Absorbing or releasing heat can show a chemical change.")

# ---- 7.A forces
H('7.A', 2, "What force pulls objects toward Earth?", "gravity", ["friction", "magnetism", "tension"], "Gravity is the force of attraction toward Earth's center.")
H('7.A', 3, "A book slides across a table and slows to a stop. Which force slows it down?", "friction", ["gravity", "magnetism", "an applied force"], "Friction opposes motion between surfaces.")
H('7.A', 3, "A book rests on a table. Which force from the table pushes up on the book?", "normal force", ["friction", "applied force", "magnetic force"], "The normal force is perpendicular to the surface and supports the object.")
H('7.A', 3, "A student pushes a shopping cart across the floor. The push is an example of a(n)...", "applied force", ["normal force", "gravitational force", "frictional force"], "An applied force comes from a person or object acting on something.")
H('7.A', 3, "A refrigerator magnet sticks to a metal door. Which force holds it there?", "magnetic force", ["gravity only", "friction only", "normal force only"], "Magnetic attraction pulls the magnet to the iron door.")
H('7.A', 4, "Why does a skater glide farther on smooth ice than on a rough sidewalk?", "there is less friction on ice", ["there is more gravity on ice", "ice has more mass", "the skater is lighter on ice"], "Smoother surfaces create less friction.")
H('7.A', 4, "Which action increases friction between a bike tire and the road?", "riding on a rougher surface", ["adding oil to the road", "riding on ice", "letting the tires wear completely smooth"], "Rough surfaces increase friction.")

# ---- 7.B net force
H('7.B', 3, "Two students push on a box in opposite directions, each with 20 N. What is the net force?", "0 N", ["20 N", "40 N", "10 N"], "Equal opposite forces cancel, so the forces are balanced.")
H('7.B', 3, "A box is pushed right with 30 N and left with 10 N. What is the net force?", "20 N to the right", ["40 N to the right", "20 N to the left", "30 N to the left"], "30 − 10 = 20, in the direction of the bigger force.")
H('7.B', 3, "When forces on an object are balanced, the object...", "stays at rest or keeps moving at constant velocity", ["speeds up", "always stops", "moves in a circle"], "Balanced forces do not change motion.")
H('7.B', 4, "A rope is pulled left with 50 N and right with 35 N. What is the net force and what will happen?", "15 N left; the rope accelerates left", ["15 N right; the rope accelerates right", "0 N; the rope stays still", "85 N left; the rope stays still"], "Unbalanced forces cause acceleration toward the bigger force.")
H('7.B', 4, "A book on a table has a 10 N weight pulling down and the table pushes up with 10 N. The forces are...", "balanced", ["unbalanced", "zero", "friction"], "Equal and opposite forces are balanced, so the book stays at rest.")
H('7.B', 4, "A cart is pushed forward with 25 N and friction pushes back with 5 N. What is the net force?", "20 N forward", ["30 N forward", "20 N backward", "5 N forward"], "25 − 5 = 20 in the forward direction.")
H('7.B', 4, "Which diagram shows unbalanced forces? An arrow of 8 N right and an arrow of 3 N left. The net force is...", "5 N to the right", ["11 N to the right", "0 N", "5 N to the left"], "8 − 3 = 5 toward the larger force.")

# ---- 7.C Newton's third law
H('7.C', 2, "According to Newton's Third Law, forces always come in...", "pairs", ["singles", "threes", "groups of four"], "For every action there is an equal and opposite reaction.")
H('7.C', 3, "A swimmer pushes backward on the water. What pushes the swimmer forward?", "the water pushes back on the swimmer", ["gravity", "friction with the air only", "nothing"], "The reaction force from the water is equal and opposite.")
H('7.C', 3, "When a rocket expels gas downward, the rocket moves upward. This is an example of...", "Newton's Third Law", ["Newton's First Law only", "friction", "conservation of mass"], "The gas is pushed down, so the rocket is pushed up.")
H('7.C', 3, "A person pushes on a wall with 30 N of force. How much force does the wall push back with?", "30 N", ["0 N", "15 N", "60 N"], "Action and reaction forces are equal in size.")
H('7.C', 4, "A bat hits a ball. The bat exerts a force on the ball. What also happens?", "the ball exerts an equal and opposite force on the bat", ["the ball exerts no force", "the ball exerts a larger force", "the bat feels no force"], "Force pairs act on different objects.")
H('7.C', 4, "A person jumps off a small boat and the boat moves backward. Why?", "the person pushes the boat backward as the boat pushes the person forward", ["the boat is lighter than the water", "gravity pulls the boat", "the water pushes the boat only"], "The two objects push on each other with equal and opposite forces.")
H('7.C', 4, "Why do the action and reaction forces not cancel each other?", "they act on different objects", ["they are unequal", "they act in the same direction", "one of them is not a real force"], "Cancelling needs forces on the same object.")

# ---- 8.A potential and kinetic energy
H('8.A', 2, "A ball held high above the ground has which type of energy?", "gravitational potential energy", ["elastic potential energy", "chemical energy", "sound energy"], "Height gives an object stored energy due to gravity.")
H('8.A', 3, "A stretched rubber band has which type of energy?", "elastic potential energy", ["gravitational potential energy", "kinetic energy", "nuclear energy"], "Stretching stores energy in the band.")
H('8.A', 3, "The energy stored in food and fuel is called...", "chemical potential energy", ["kinetic energy", "elastic potential energy", "thermal energy"], "Chemical bonds store energy.")
H('8.A', 3, "A moving skateboard has...", "kinetic energy", ["no energy", "only potential energy", "only chemical energy"], "Kinetic energy is the energy of motion.")
H('8.A', 4, "A roller coaster car is at the top of a hill. As it rolls down, its potential energy...", "decreases while its kinetic energy increases", ["increases while its kinetic energy decreases", "stays the same", "disappears completely"], "Stored energy changes into motion as it falls.")
H('8.A', 4, "Which has the most kinetic energy: a 2 kg ball moving at 5 m/s or a 2 kg ball moving at 10 m/s?", "the ball moving at 10 m/s", ["the ball moving at 5 m/s", "they have equal kinetic energy", "neither has kinetic energy"], "Faster objects have more kinetic energy.")
H('8.A', 4, "A compressed spring is released and a toy shoots forward. Which energy change occurred?", "elastic potential to kinetic", ["kinetic to gravitational", "chemical to nuclear", "thermal to elastic"], "Stored spring energy became motion.")

# ---- 8.B energy conservation
H('8.B', 3, "The law of conservation of energy says that energy...", "cannot be created or destroyed, only transformed", ["is always created in machines", "is destroyed by friction", "disappears when used"], "Total energy stays constant.")
H('8.B', 3, "In photosynthesis, plants transform light energy into...", "chemical energy", ["sound energy", "nuclear energy", "elastic energy"], "Plants store the energy in sugar molecules.")
H('8.B', 3, "In an electrical circuit with a light bulb, electrical energy is transformed mostly into...", "light and thermal energy", ["sound and elastic energy", "chemical energy", "nuclear energy"], "The bulb glows and gets warm.")
H('8.B', 4, "In a food web, a rabbit eats grass and a fox eats the rabbit. Energy from the Sun ends up where?", "stored in the grass, then passed to the rabbit and fox", ["created by the rabbit", "destroyed in the fox", "gone after the grass is eaten"], "Energy flows through the web by eating.")
H('8.B', 4, "A roller coaster never reaches a hill as high as the first one. Where does some of the energy go?", "it is transformed into thermal energy by friction", ["it is destroyed", "it is created again at the top", "it becomes potential energy only"], "Friction changes some mechanical energy into heat.")
H('8.B', 4, "A battery-powered toy car moves. Which energy transformation occurs?", "chemical to electrical to kinetic", ["kinetic to chemical", "nuclear to elastic", "sound to thermal"], "The battery's chemical energy powers a motor.")
H('8.B', 4, "A pendulum swings back and forth and eventually stops. Why?", "its mechanical energy is gradually transferred to thermal energy by air resistance and friction", ["energy is destroyed", "the pendulum becomes lighter", "gravity turns off"], "No energy is lost; it is transferred to the surroundings.")

# ---- 8.C waves
H('8.C', 2, "In a transverse wave, the particles of the medium move...", "at right angles to the direction the wave travels", ["parallel to the wave direction", "in the same direction as the wave", "not at all"], "Like a rope wave moving up and down while traveling across.")
H('8.C', 3, "In a longitudinal wave, the particles move...", "back and forth parallel to the direction the wave travels", ["up and down", "at right angles to the wave", "in circles"], "Compressions and expansions travel along the same line.")
H('8.C', 3, "Sound waves are an example of which kind of wave?", "longitudinal", ["transverse", "electromagnetic", "surface only"], "Sound is made of compressions and rarefactions.")
H('8.C', 3, "Waves transfer...", "energy without moving matter along with them", ["matter without energy", "both matter and energy permanently", "neither"], "A wave carries energy; the medium only vibrates.")
H('8.C', 4, "A water wave moves a floating cork. What does the cork mainly do?", "bob up and down in place", ["travel with the wave to shore", "sink at once", "move opposite to the wave"], "The medium moves in place while energy moves on.")
H('8.C', 4, "The highest point of a transverse wave is called the...", "crest", ["trough", "compression", "rarefaction"], "The crest is the top of the wave.")
H('8.C', 4, "The distance between two crests of a transverse wave is the...", "wavelength", ["amplitude", "frequency", "period"], "Wavelength is the crest-to-crest distance.")

# ---- 9.A seasons
H('9.A', 2, "What causes the seasons on Earth?", "the tilt of Earth's axis as it revolves around the Sun", ["Earth's distance from the Sun changing a lot", "the Moon's phases", "the Sun getting bigger and smaller"], "Tilt changes how directly sunlight hits each hemisphere.")
H('9.A', 3, "When the Northern Hemisphere is tilted toward the Sun, it is...", "summer in the Northern Hemisphere", ["winter in the Northern Hemisphere", "spring in the Southern Hemisphere", "night all day"], "Direct sunlight and longer days bring summer.")
H('9.A', 3, "It is winter in Texas. What season is it in Australia?", "summer", ["winter", "spring", "fall"], "Hemispheres have opposite seasons.")
H('9.A', 3, "About how long does it take Earth to revolve once around the Sun?", "one year", ["one day", "one month", "one week"], "A revolution takes about 365 days.")
H('9.A', 4, "If Earth's axis were not tilted, what would happen to the seasons?", "there would be little or no seasonal change", ["seasons would be more extreme", "it would always be winter", "day would last forever"], "Tilt causes seasons.")
H('9.A', 4, "On the summer solstice in the Northern Hemisphere, the Sun's rays are...", "most direct and the day is longest", ["least direct and the day is shortest", "equally spread over the planet", "blocked by the Moon"], "The Northern Hemisphere is tilted most toward the Sun.")
H('9.A', 4, "Why is it not hotter in the whole world when Earth is closest to the Sun in January?", "seasons are caused by tilt, not distance", ["the Sun turns off", "Earth stops moving", "the Moon blocks the Sun"], "Earth's tilt, not distance, drives seasons.")

# ---- 9.B tides
H('9.B', 2, "What mainly causes ocean tides?", "the gravity of the Moon and Sun", ["wind only", "earthquakes", "ocean currents only"], "Gravitational pull from the Moon and Sun creates tides.")
H('9.B', 3, "How many high tides do most coasts have each day?", "about two", ["one", "four", "none"], "Most places have two high and two low tides a day.")
H('9.B', 3, "Spring tides (very high and very low) occur when the Sun, Earth and Moon are...", "lined up", ["at right angles", "far apart", "on opposite sides of the galaxy"], "The combined pull is strongest at new and full moon.")
H('9.B', 3, "Neap tides (small tidal range) occur when the Sun and Moon are...", "at right angles to Earth", ["lined up with Earth", "behind Earth", "very close to Earth"], "Their pulls partly cancel at first and third quarter moon.")
H('9.B', 4, "At which Moon phase do spring tides occur?", "new moon and full moon", ["first and third quarter", "only a crescent", "only a gibbous"], "The Sun, Earth and Moon line up at new and full moon.")
H('9.B', 4, "At which Moon phase do neap tides occur?", "first quarter and third quarter", ["new moon", "full moon", "during eclipses only"], "The pulls act at right angles.")
H('9.B', 4, "Why does the tide go in and out about twice a day at a beach?", "Earth rotates under the tidal bulges", ["the Moon moves around the beach", "water evaporates twice a day", "winds turn on and off"], "Earth's rotation moves coasts through the bulges.")

# ---- 10.A Earth's systems
H('10.A', 2, "Which Earth system includes all living things?", "biosphere", ["hydrosphere", "atmosphere", "geosphere"], "The biosphere is all life on Earth.")
H('10.A', 2, "Which Earth system includes oceans, lakes and rivers?", "hydrosphere", ["biosphere", "atmosphere", "geosphere"], "Hydro means water.")
H('10.A', 2, "Which Earth system is the layer of gases surrounding the planet?", "atmosphere", ["hydrosphere", "geosphere", "biosphere"], "The atmosphere is made of air.")
H('10.A', 3, "Rocks, soil and mountains belong to which Earth system?", "geosphere", ["atmosphere", "hydrosphere", "biosphere"], "The geosphere is the solid Earth.")
H('10.A', 3, "A volcano erupts and sends ash into the air. Which two systems interact?", "geosphere and atmosphere", ["biosphere and hydrosphere only", "atmosphere and hydrosphere only", "no systems"], "Rock material from the geosphere enters the air.")
H('10.A', 4, "A tree absorbs water from soil and releases oxygen. Which systems are involved?", "biosphere, geosphere, hydrosphere and atmosphere", ["biosphere only", "geosphere only", "atmosphere only"], "All four interact.")
H('10.A', 4, "Which is part of the hydrosphere?", "glaciers", ["a canyon wall", "a cloud of oxygen", "a squirrel"], "Frozen water is part of the hydrosphere.")

# ---- 10.B layers of Earth
H('10.B', 2, "Which layer of Earth is the thin, outermost layer?", "crust", ["mantle", "outer core", "inner core"], "The crust is the thin outer shell.")
H('10.B', 3, "Which layer of Earth is the thickest?", "mantle", ["crust", "outer core", "inner core"], "The mantle makes up most of Earth's volume.")
H('10.B', 3, "Which layer of Earth is made of solid iron and nickel because of the huge pressure?", "inner core", ["outer core", "mantle", "crust"], "Pressure keeps the inner core solid despite the heat.")
H('10.B', 3, "Which layer of Earth is liquid metal?", "outer core", ["inner core", "mantle", "crust"], "The outer core is molten iron and nickel.")
H('10.B', 4, "From the surface moving toward the center, which order of layers is correct?", "crust, mantle, outer core, inner core", ["mantle, crust, inner core, outer core", "inner core, outer core, mantle, crust", "crust, outer core, mantle, inner core"], "Layers get hotter and deeper going inward.")
H('10.B', 4, "Which layer's slow flowing movement helps move Earth's tectonic plates?", "mantle", ["crust", "inner core", "atmosphere"], "Convection in the mantle drives plate movement.")
H('10.B', 4, "Earth's layers are sometimes modeled with a peach. What does the pit most likely represent?", "the core", ["the crust", "the atmosphere", "the mantle"], "The pit is the center, like the core.")

# ---- 10.C rock cycle
H('10.C', 2, "Rock formed from cooled magma or lava is called...", "igneous rock", ["sedimentary rock", "metamorphic rock", "mineral"], "Igneous means formed from fire/melt.")
H('10.C', 3, "Rock formed from layers of pressed sediment is called...", "sedimentary rock", ["igneous rock", "metamorphic rock", "magma"], "Layers of sediment get compacted and cemented.")
H('10.C', 3, "Rock changed by heat and pressure without melting is called...", "metamorphic rock", ["igneous rock", "sedimentary rock", "lava"], "Metamorphic means changed in form.")
H('10.C', 3, "Which rock is most likely to contain fossils?", "sedimentary rock", ["igneous rock", "metamorphic rock made at great depth", "obsidian"], "Fossils are preserved in sediment layers.")
H('10.C', 4, "Limestone is heated and squeezed deep underground and becomes marble. Marble is a...", "metamorphic rock", ["igneous rock", "sedimentary rock", "type of lava"], "Heat and pressure changed it.")
H('10.C', 4, "Which process turns rock into small pieces that can become sediment?", "weathering and erosion", ["melting and cooling", "compaction only", "metamorphism"], "Rocks break down and are moved.")
H('10.C', 4, "Granite cools slowly from magma. Over time it is weathered into sand. The sand is then pressed into sandstone. Which sequence of rock types is correct?", "igneous, then sedimentary", ["sedimentary, then igneous", "metamorphic, then igneous", "igneous, then metamorphic with no steps"], "Weathering and compaction produce sedimentary rock.")

# ---- 11.A resource management
H('11.A', 3, "Why is managing natural resources important?", "so people and ecosystems can keep having enough clean water, food and energy", ["so resources are used up faster", "so pollution increases", "so fewer people have energy"], "Careful use makes resources last.")
H('11.A', 3, "Burning fossil fuels for energy can cause what environmental problem?", "air pollution", ["fewer clouds", "more fresh water", "less carbon dioxide"], "Burning fuels releases pollutants.")
H('11.A', 3, "Poor management of water resources can lead to...", "water shortages and pollution", ["more clean water", "less disease", "greater food supply"], "Overuse and contamination hurt supplies.")
H('11.A', 4, "How can reducing energy waste help with global poverty?", "lower energy costs leave more money for food, health care and education", ["it raises energy bills", "it removes all jobs", "it makes food rot"], "Savings can be used for basic needs.")
H('11.A', 4, "Which is an effect of malnutrition that better food resource management may reduce?", "poor growth and health", ["better school results", "faster healing", "stronger immunity"], "Managing food supplies helps people get enough nutrients.")
H('11.A', 4, "Which resource problem is caused by polluted air?", "health problems like asthma", ["more clean drinking water", "more fertile soil", "cooler cities"], "Air pollution harms lungs.")
H('11.A', 4, "A city wastes much of its drinking water through leaky pipes. Which result is most likely?", "less water available for people and higher costs", ["more water in reservoirs", "lower water bills for everyone", "cleaner rivers"], "Wasted water reduces supply and raises costs.")

# ---- 11.B conservation
H('11.B', 2, "Which action conserves energy at home?", "turning off lights when leaving a room", ["leaving the TV on all day", "opening the refrigerator often", "running empty dishwashers"], "Using less energy conserves it.")
H('11.B', 3, "Which is a way to conserve water?", "taking shorter showers", ["leaving the faucet running", "watering lawns during rain", "washing small loads of laundry"], "Using less water saves it.")
H('11.B', 3, "An LED light bulb uses much less electricity than an older bulb to produce the same light. This is an example of...", "increased efficiency", ["more waste", "pollution", "energy creation"], "Efficiency means getting the same result using less energy.")
H('11.B', 3, "Planting cover crops helps protect which resource?", "soil", ["air only", "oil", "natural gas"], "Roots and plants hold soil and reduce erosion.")
H('11.B', 4, "A power plant adds scrubbers that remove pollutants from smoke before it is released. This technology helps manage...", "air quality", ["soil minerals", "tides", "the Moon's orbit"], "Scrubbers clean exhaust gases.")
H('11.B', 4, "Which technology helps manage energy resources by making use of the Sun?", "solar panels", ["coal furnaces", "diesel engines", "gas generators"], "Solar panels convert sunlight to electricity.")
H('11.B', 4, "Recycling aluminum cans saves energy because...", "making new cans from recycled metal takes far less energy than from raw ore", ["it makes cans heavier", "it uses more water", "it creates more ore"], "Recycling avoids energy-heavy mining and refining.")

# ---- 12.A ecosystems, biotic and abiotic factors
H('12.A', 2, "Which is an abiotic factor in an ecosystem?", "sunlight", ["a tree", "a fish", "bacteria"], "Abiotic factors are non-living.")
H('12.A', 2, "Which is a biotic factor in an ecosystem?", "a grasshopper", ["temperature", "water", "soil minerals"], "Biotic factors are living things.")
H('12.A', 3, "Two plants in the same patch compete for water and light. What happens if there is not enough of one resource?", "some plants grow poorly or die", ["all plants grow better", "competition stops", "the resource increases"], "Limited resources limit population size.")
H('12.A', 3, "If a drought reduces water in a pond ecosystem, what will most likely happen to fish populations?", "they will decrease", ["they will increase", "they will stay exactly the same", "they will turn into plants"], "Less water means less habitat and food.")
H('12.A', 4, "Rabbits in a field eat the available grass. What happens to the rabbit population if the grass supply drops sharply?", "the rabbit population will decrease", ["the rabbit population will increase", "the grass will grow faster", "nothing will change"], "Less food reduces how many rabbits can survive.")
H('12.A', 4, "A new species of fish is added to a lake and eats the same food as native fish. What is likely to occur?", "competition for food", ["more food for all", "the native fish eat less", "the lake dries up"], "Sharing a limited resource creates competition.")
H('12.A', 4, "Which change in an abiotic factor would most harm a coral reef ecosystem?", "warmer ocean temperatures", ["more fish", "more algae in a healthy balance", "more sunlight in the right range"], "Coral is sensitive to temperature.")

H('12.A', 3, "In a desert ecosystem, cactuses, snakes and sand are all present. Which of these is an abiotic part of the ecosystem?", "the sand", ["the cactuses", "the snakes", "the lizards"], "Sand is non-living; cactuses and animals are living.")
H('12.A', 4, "Coyotes and foxes in the same area both hunt rabbits. When rabbits become scarce, what is the most likely effect on the two predator populations?", "both populations face competition and may decline", ["both populations grow quickly", "neither population is affected", "the rabbits stop being prey"], "Fewer shared prey means more competition for food.")

# ---- 12.B relationships
H('12.B', 2, "An owl hunts and eats mice. The owl is the...", "predator", ["prey", "producer", "parasite"], "Predators hunt and eat prey.")
H('12.B', 3, "A tick feeds on a dog's blood and harms the dog. This is...", "parasitism", ["mutualism", "commensalism", "competition"], "One organism benefits, the other is harmed.")
H('12.B', 3, "Bees collect nectar from flowers and pollinate them. This is...", "mutualism", ["parasitism", "commensalism", "predation"], "Both organisms benefit.")
H('12.B', 3, "A barnacle attaches to a whale. The barnacle gets a ride and food, and the whale is not affected. This is...", "commensalism", ["mutualism", "parasitism", "predation"], "One benefits and the other is neither helped nor harmed.")
H('12.B', 4, "Two male deer fight for territory. This is an example of...", "competition", ["mutualism", "commensalism", "parasitism"], "Organisms compete for limited resources.")
H('12.B', 4, "A clownfish lives among a sea anemone's stinging tentacles, gaining protection, while it cleans the anemone and drives away fish that eat it. This is...", "mutualism", ["parasitism", "commensalism", "competition"], "Both species gain.")
H('12.B', 4, "A mistletoe plant grows on a tree, taking water and nutrients from it and weakening it. The mistletoe is a...", "parasite", ["predator", "mutualist", "decomposer"], "It benefits at the tree's expense.")

# ---- 12.C hierarchy
H('12.C', 2, "A single living thing is called a(n)...", "organism", ["population", "community", "ecosystem"], "Organism is the smallest level of ecological organization.")
H('12.C', 3, "All the deer living in one forest make up a...", "population", ["community", "ecosystem", "biosphere"], "A population is one species in one area.")
H('12.C', 3, "All the populations of different species living together in an area make up a...", "community", ["population", "organism", "cell"], "A community includes all species there.")
H('12.C', 3, "A community plus the non-living factors such as water, soil and sunlight is a(n)...", "ecosystem", ["population", "organism", "species"], "An ecosystem includes biotic and abiotic parts.")
H('12.C', 4, "Which list is in order from smallest to largest?", "organism, population, community, ecosystem", ["ecosystem, community, population, organism", "population, organism, ecosystem, community", "community, organism, population, ecosystem"], "Each level contains the one before it.")
H('12.C', 4, "A scientist counts all the frogs in a pond. What level of organization is she studying?", "population", ["community", "ecosystem", "organism"], "Frogs of one species form a population.")
H('12.C', 4, "A scientist studies the frogs, fish, plants and insects in a pond. She is studying a...", "community", ["population", "organism", "single species"], "Several species living together form a community.")

# ---- 13.A cell theory
H('13.A', 2, "What is the basic unit of structure and function in living things?", "the cell", ["the atom", "the tissue", "the organ"], "Cells are the building blocks of life.")
H('13.A', 3, "According to cell theory, new cells come from...", "pre-existing cells", ["nonliving matter", "air", "rocks"], "Cells divide to form new cells.")
H('13.A', 3, "According to cell theory, all living things are made of...", "one or more cells", ["only tissues", "only atoms", "only organs"], "Even single-celled organisms are made of a cell.")
H('13.A', 3, "Which scientist is credited with first observing and naming cells in cork?", "Robert Hooke", ["Isaac Newton", "Charles Darwin", "Gregor Mendel"], "Hooke used a microscope in the 1600s.")
H('13.A', 4, "Why was the invention of the microscope important for cell theory?", "it allowed scientists to see cells", ["it created cells", "it made cells larger permanently", "it removed the need for experiments"], "Cells are too small to see without magnification.")
H('13.A', 4, "A student sees a single cell that moves, eats and reproduces. What does this suggest about it?", "it is a complete living organism", ["it is just a part of a bigger animal", "it is not alive", "it is a rock"], "A single cell can carry out all life processes.")
H('13.A', 4, "Which statement is part of cell theory?", "cells are the basic unit of life", ["cells are made by the nucleus only", "cells are not found in plants", "cells can come from nonliving things"], "That is one of the three main ideas.")

# ---- 13.B characteristics of organisms
H('13.B', 3, "A cell without a nucleus, such as a bacterium, is called...", "prokaryotic", ["eukaryotic", "multicellular", "autotrophic"], "Prokaryotes lack a nucleus.")
H('13.B', 3, "Plant and animal cells have a nucleus. They are classified as...", "eukaryotic", ["prokaryotic", "viruses", "nonliving"], "Eukaryotic cells have a membrane-bound nucleus.")
H('13.B', 3, "A paramecium is made of a single cell. It is...", "unicellular", ["multicellular", "autotrophic only", "nonliving"], "Unicellular means one cell.")
H('13.B', 3, "An organism that makes its own food from sunlight is called...", "autotrophic", ["heterotrophic", "parasitic only", "unicellular only"], "Autotrophs produce their own food.")
H('13.B', 3, "An organism that must eat other organisms for food is called...", "heterotrophic", ["autotrophic", "prokaryotic", "a producer"], "Heterotrophs consume other organisms.")
H('13.B', 4, "A tree is a multicellular, eukaryotic autotroph. Which organism has the same set of characteristics?", "a sunflower", ["a bacterium", "a mushroom", "a cow"], "A sunflower is a plant, so it is multicellular, eukaryotic and photosynthetic.")
H('13.B', 4, "A mushroom has a nucleus, many cells, and absorbs food from decaying matter. It is...", "eukaryotic, multicellular and heterotrophic", ["prokaryotic and autotrophic", "unicellular and autotrophic", "prokaryotic and unicellular"], "Fungi are heterotrophic eukaryotes.")

# ---- 13.C variation and survival
H('13.C', 2, "Why are differences among organisms in a population important?", "some may survive better when the environment changes", ["they make all organisms identical", "they stop reproduction", "they remove predators"], "Variation gives a chance that some will survive.")
H('13.C', 3, "A beetle population has green and brown individuals. Birds see the green ones more easily against brown bark. Which are more likely to survive and reproduce?", "the brown ones", ["the green ones", "both equally", "neither"], "Camouflaged individuals avoid predators.")
H('13.C', 3, "A drought makes plants with deeper roots more likely to survive. This is an example of...", "a helpful variation", ["a harmful variation always", "no variation", "a change that cannot be inherited"], "Deep roots reach water.")
H('13.C', 4, "A disease kills most individuals in a population, but a few with a resistant trait survive. What is likely true of the next generation?", "more will have the resistant trait", ["fewer will have it", "none will have it", "all will die"], "Survivors pass the trait on.")
H('13.C', 4, "Why can a population with little variation be at risk when a disease appears?", "if all are vulnerable, all could die", ["it grows faster", "it gains new traits at once", "it becomes immune automatically"], "Without variation, there may be no resistant individuals.")
H('13.C', 4, "As an environment gets colder, which trait would be an advantage for a mammal?", "thicker fur", ["thin fur", "less body fat", "smaller body only"], "Insulation helps in the cold.")
H('13.C', 4, "A trait that helps an organism survive in one environment may be a disadvantage in another. Which example fits this?", "white fur helps in snow but stands out in a forest", ["green leaves help only in snow", "brown fur is always best", "all traits help everywhere"], "A trait's value depends on the environment.")

B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g6_science.jsonl'))
print("saved", len(B.out), "questions")

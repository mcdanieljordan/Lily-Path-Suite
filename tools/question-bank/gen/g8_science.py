#!/usr/bin/env python3
"""Grade 8 Science (TEKS 112.28.b) - original questions, content strands 6-13. Written by hand, 7 per standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.28.b.', 603, own='g8_science.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 6.A classifying matter
H('6.A', 2, "A mixture that has the same composition throughout, such as salt dissolved in water, is...", "homogeneous", ["heterogeneous", "an element", "a pure compound"], "Uniform throughout means homogeneous.")
H('6.A', 3, "Which is a heterogeneous mixture?", "a bowl of trail mix", ["sugar water", "air in a sealed jar", "a bar of pure gold"], "The parts of trail mix can be seen and separated.")
H('6.A', 3, "Which is a pure substance that is a compound?", "water", ["salad", "air", "orange juice with pulp"], "Water is a pure substance made of two elements bonded.")
H('6.A', 3, "A sample contains only one kind of atom. It is...", "an element", ["a compound", "a heterogeneous mixture", "a solution"], "Elements contain just one type of atom.")
H('6.A', 4, "A student models a substance as two different kinds of atoms bonded in a fixed ratio. What is it?", "a compound", ["an element", "a mixture", "a solution"], "Fixed-ratio bonded atoms of different elements form a compound.")
H('6.A', 4, "Which of these is a homogeneous mixture?", "vinegar", ["pizza", "granite", "a pile of sand and iron filings"], "Vinegar looks the same throughout.")
H('6.A', 4, "How does a mixture differ from a compound?", "the parts of a mixture are not chemically bonded", ["a mixture always has a fixed formula", "a mixture is a pure substance", "a compound can be separated by filtering"], "Mixtures keep the properties of their parts.")

# ---- 6.B periodic table and reactions
H('6.B', 2, "Elements on the periodic table are arranged by increasing...", "atomic number", ["color", "density", "state of matter at room temperature"], "Atomic number is the number of protons.")
H('6.B', 3, "In the reaction 2H2 + O2 -> 2H2O, which elements are the reactants made of?", "hydrogen and oxygen", ["helium and oxygen", "hydrogen and carbon", "nitrogen and oxygen"], "H is hydrogen and O is oxygen.")
H('6.B', 3, "Which group on the periodic table contains elements that rarely react?", "noble gases", ["alkali metals", "halogens", "alkaline earth metals"], "Their outer shells are full.")
H('6.B', 3, "Sodium (Na) and chlorine (Cl) react to form NaCl. Which tool tells you what the symbols stand for?", "the periodic table", ["a barometer", "a microscope", "a spring scale"], "It lists each element and its symbol.")
H('6.B', 4, "In the reaction CH4 + 2O2 -> CO2 + 2H2O, which atoms are involved?", "carbon, hydrogen and oxygen", ["carbon and nitrogen", "hydrogen and nitrogen only", "carbon and sulfur"], "The symbols C, H and O appear.")
H('6.B', 4, "Elements in the same column of the periodic table tend to have...", "similar chemical properties", ["identical masses", "the same number of protons", "the same color"], "They have the same number of outer electrons.")
H('6.B', 4, "In the periodic table, metals are generally found...", "on the left and center", ["on the far right", "only at the top", "only in one column"], "Nonmetals are on the right.")

# ---- 6.C cohesion, adhesion, surface tension
H('6.C', 2, "Water molecules sticking to each other is called...", "cohesion", ["adhesion", "evaporation", "condensation"], "Cohesion is attraction between like molecules.")
H('6.C', 2, "Water molecules sticking to other surfaces, like glass, is called...", "adhesion", ["cohesion", "melting", "diffusion"], "Adhesion is attraction between unlike substances.")
H('6.C', 3, "Why do small drops of water form beads on a waxy leaf?", "cohesion pulls water molecules together", ["water is repelled by gravity", "wax melts the water", "the leaf adds salt"], "Cohesion and surface tension hold the drop together.")
H('6.C', 3, "A water strider can walk on water because of...", "surface tension", ["low density of the strider only", "evaporation", "gravity"], "The surface behaves like a thin skin.")
H('6.C', 4, "Water travels up through plant roots, stems and leaves partly because of...", "cohesion and adhesion", ["wind pushing it", "gravity pulling it up", "the Moon"], "Water sticks to itself and to the vessel walls.")
H('6.C', 4, "A paper towel soaks up spilled water because water molecules...", "adhere to the fibers and pull other molecules along", ["repel the fibers", "evaporate instantly", "turn into gas"], "Adhesion plus cohesion draws water upward.")
H('6.C', 4, "Which observation is caused by surface tension?", "a drop of water forming a rounded dome on a coin", ["ice floating on water", "salt dissolving", "water boiling"], "Surface tension pulls the surface into a tight shape.")

# ---- 6.D acids and bases
H('6.D', 2, "A solution with a pH of 2 is...", "an acid", ["a base", "neutral", "pure water"], "pH below 7 is acidic.")
H('6.D', 2, "Pure water has a pH of about...", "7", ["1", "10", "14"], "Pure water is neutral.")
H('6.D', 3, "Which pH value is most basic?", "13", ["3", "7", "9"], "Higher pH means a stronger base.")
H('6.D', 3, "Which property is common to bases?", "they feel slippery", ["they taste sweet", "they turn blue litmus red", "they have a pH below 7"], "Bases feel slippery (like soap).")
H('6.D', 4, "Lemon juice has a pH of 2 and baking soda solution has a pH of 9. Which statement is correct?", "lemon juice is more acidic than water, and the baking soda solution is basic", ["both are acids", "both are bases", "lemon juice is a base"], "Below 7 is acid, above 7 is base.")
H('6.D', 4, "What happens to pH when a base is added to an acid?", "the pH rises toward 7", ["the pH falls", "the pH becomes 0", "the pH stays exactly the same"], "Neutralization moves toward neutral.")
H('6.D', 4, "How many times more acidic is a solution of pH 3 than one of pH 4?", "10 times", ["2 times", "3 times", "100 times"], "Each pH step is a factor of 10.")

# ---- 6.E conservation of mass
H('6.E', 2, "The law of conservation of mass says that in a chemical reaction, mass is...", "neither created nor destroyed", ["always lost", "always gained", "turned into energy only"], "Total mass stays the same.")
H('6.E', 3, "10 g of reactant A reacts completely with 15 g of reactant B. What is the total mass of the products?", "25 g", ["5 g", "10 g", "150 g"], "Mass of products equals mass of reactants.")
H('6.E', 3, "A chemical equation is balanced when...", "each type of atom has the same count on both sides", ["the reactants are heavier", "the products are fewer", "the arrows are equal"], "Atoms are only rearranged.")
H('6.E', 4, "Is the equation 2H2 + O2 -> 2H2O balanced?", "yes, 4 H and 2 O on each side", ["no, there are more H on the right", "no, there are more O on the right", "yes, but only the O is balanced"], "Count: 4 H and 2 O on both sides.")
H('6.E', 4, "Is the equation H2 + O2 -> H2O balanced?", "no, there are 2 O on the left and 1 on the right", ["yes", "no, there are more H on the right", "no, hydrogen is missing"], "Oxygen atoms are not equal.")
H('6.E', 4, "A student burns a candle in an open room and the candle seems to lose mass. Where did the mass go?", "into gases like carbon dioxide and water vapor released into the air", ["it was destroyed", "it turned into energy only", "it stayed in the wick"], "Mass is conserved when all products are counted.")
H('6.E', 4, "Balance: N2 + __H2 -> 2NH3. What number goes in the blank?", "3", ["1", "2", "6"], "6 H atoms are needed on the right so 3 H2.")

# ---- 7.A Newton's second law
H('7.A', 2, "Newton's Second Law can be written as...", "F = m x a", ["F = m / a", "a = F x m", "m = F x a"], "Force equals mass times acceleration.")
H('7.A', 3, "A 2 kg cart is pushed with a net force of 10 N. What is its acceleration?", "5 m/s2", ["20 m/s2", "0.2 m/s2", "12 m/s2"], "a = F / m = 10 / 2.")
H('7.A', 3, "If the net force on an object is made twice as large and the mass stays the same, the acceleration...", "doubles", ["halves", "stays the same", "becomes zero"], "Acceleration is proportional to force.")
H('7.A', 3, "If the mass of an object doubles and the force stays the same, the acceleration...", "is cut in half", ["doubles", "stays the same", "quadruples"], "Acceleration is inversely related to mass.")
H('7.A', 4, "What net force gives a 4 kg object an acceleration of 3 m/s2?", "12 N", ["7 N", "1.3 N", "0.75 N"], "F = 4 x 3.")
H('7.A', 4, "A 1,000 kg car accelerates at 2 m/s2. What is the net force on the car?", "2,000 N", ["500 N", "1,002 N", "998 N"], "F = 1000 x 2.")
H('7.A', 4, "Two carts get the same push. Cart A has a mass of 1 kg and Cart B has a mass of 3 kg. Which accelerates more?", "the lighter cart", ["the heavier cart", "they accelerate equally", "neither accelerates"], "Less mass means more acceleration.")

# ---- 7.B three laws acting together
H('7.B', 3, "A seat belt keeps a passenger in place during a sudden stop. This mostly demonstrates Newton's...", "First Law", ["Second Law", "Third Law", "Law of Gravitation"], "The passenger's body tends to keep moving.")
H('7.B', 3, "A swimmer pushes water backward and moves forward. This demonstrates Newton's...", "Third Law", ["First Law", "Second Law", "Law of Conservation of Mass"], "Action and reaction forces.")
H('7.B', 3, "A bigger force on a shopping cart makes it speed up more. This demonstrates Newton's...", "Second Law", ["First Law", "Third Law", "Law of Gravity"], "More force gives more acceleration.")
H('7.B', 4, "A car hits a wall. Which laws help explain why an unrestrained passenger is injured?", "First Law (inertia) and Second Law (large force over a short time)", ["only the Third Law", "none of the laws", "only the Law of Gravity"], "Inertia keeps the passenger moving; stopping quickly takes a large force.")
H('7.B', 4, "On a roller coaster, riders feel pressed into their seats on a sharp turn. Which idea explains this?", "inertia: their bodies tend to keep moving in a straight line", ["gravity turns off", "the seat creates mass", "friction speeds them up"], "The seat pushes inward to change their direction.")
H('7.B', 4, "A football player tackles another. Which statement is correct?", "each player exerts an equal and opposite force on the other", ["only the tackler exerts force", "forces cancel and neither moves", "the lighter player exerts more force"], "Third Law pairs are equal and opposite.")
H('7.B', 4, "Airbags in cars reduce injury by...", "increasing the time over which the passenger stops, so the force is smaller", ["increasing the speed of the car", "decreasing the passenger's mass", "removing inertia"], "Same change in motion over longer time means less force.")

# ---- 8.A wave characteristics
H('8.A', 2, "The distance between two crests of a transverse wave is the...", "wavelength", ["amplitude", "frequency", "period"], "Wavelength is crest to crest.")
H('8.A', 3, "The height of a wave from its rest position to its crest is its...", "amplitude", ["wavelength", "frequency", "speed"], "Greater amplitude means more energy.")
H('8.A', 3, "Frequency is the number of waves that pass a point per...", "second", ["meter", "kilogram", "degree"], "Measured in hertz.")
H('8.A', 3, "Which electromagnetic wave has the longest wavelength?", "radio waves", ["gamma rays", "X-rays", "ultraviolet"], "Radio waves are at the long-wavelength end.")
H('8.A', 4, "As the frequency of an electromagnetic wave increases, its wavelength...", "decreases", ["increases", "stays the same", "doubles"], "In a given medium, wavelength and frequency are inversely related.")
H('8.A', 4, "Which has the highest frequency?", "gamma rays", ["microwaves", "visible light", "radio waves"], "Gamma rays are at the high-energy end.")
H('8.A', 4, "Which color of visible light has the shortest wavelength?", "violet", ["red", "green", "yellow"], "Violet is at the short end.")

# ---- 8.B EM applications
H('8.B', 3, "Which type of electromagnetic wave is used in radiation therapy to kill cancer cells?", "gamma rays or X-rays", ["radio waves", "visible light only", "sound waves"], "High-energy rays can damage cells.")
H('8.B', 3, "Microwave ovens heat food using...", "microwaves", ["X-rays", "gamma rays", "sound waves"], "Microwaves make water molecules vibrate.")
H('8.B', 3, "Wi-Fi and cell phones send information using...", "radio waves and microwaves", ["X-rays", "gamma rays", "ultraviolet rays"], "These waves carry signals without wires.")
H('8.B', 4, "Fiber optic cables transmit information using...", "pulses of light", ["sound waves", "magnetism", "heat only"], "Light bounces along glass strands.")
H('8.B', 4, "Ultraviolet light is used to sterilize equipment because it...", "can damage the DNA of germs", ["makes metal softer", "creates heat only", "adds oxygen"], "UV breaks down microbes.")
H('8.B', 4, "Why should people wear sunscreen?", "to protect skin from harmful ultraviolet rays", ["to block radio waves", "to block sound", "to stop gravity"], "UV can cause sunburn and skin damage.")
H('8.B', 4, "A doctor uses X-rays to see a broken bone because X-rays...", "pass through soft tissue but are absorbed by bone", ["are sound waves", "are absorbed by all tissue equally", "pass through bone but not skin"], "Bone absorbs more.")

# ---- 9.A life cycle of stars
H('9.A', 2, "Stars form from clouds of gas and dust called...", "nebulae", ["comets", "asteroids", "planets"], "Gravity pulls the nebula together.")
H('9.A', 3, "What happens when a star the size of our Sun runs out of fuel?", "it becomes a red giant, then a white dwarf", ["it becomes a black hole", "it explodes as a supernova", "it turns into a planet"], "Medium-mass stars end as white dwarfs.")
H('9.A', 3, "A very massive star ends its life as a(n)...", "supernova", ["white dwarf only", "nebula", "comet"], "It explodes and may leave a neutron star or black hole.")
H('9.A', 4, "On the Hertzsprung-Russell diagram, most stars (like the Sun) fall in the...", "main sequence", ["white dwarf region", "giant region", "supergiant region"], "A diagonal band includes most stars.")
H('9.A', 4, "On an H-R diagram, which stars are hot but dim?", "white dwarfs", ["red giants", "main sequence stars", "supergiants"], "They are small, so dim despite high temperature.")
H('9.A', 4, "A star is cool but very bright. On the H-R diagram it is most likely a...", "red giant or supergiant", ["white dwarf", "main sequence dwarf", "neutron star"], "Large surface area makes it bright.")
H('9.A', 4, "The Sun produces energy by...", "fusing hydrogen into helium", ["burning coal", "splitting uranium", "chemical reactions"], "Nuclear fusion releases energy.")

# ---- 9.B galaxies
H('9.B', 2, "Our solar system is located in the...", "Milky Way galaxy", ["Andromeda galaxy", "Large Magellanic Cloud", "Orion Nebula"], "The Milky Way is our home galaxy.")
H('9.B', 3, "A galaxy with arms that wind around a bright center is a...", "spiral galaxy", ["elliptical galaxy", "irregular galaxy", "dwarf star"], "Spiral galaxies have arms.")
H('9.B', 3, "A galaxy shaped like a smooth oval with no clear arms is...", "elliptical", ["spiral", "irregular", "barred only"], "Smooth shape means elliptical.")
H('9.B', 3, "A galaxy with no regular shape is...", "irregular", ["spiral", "elliptical", "a nebula"], "Irregular galaxies lack a defined structure.")
H('9.B', 4, "The Milky Way is classified as a...", "spiral galaxy", ["elliptical galaxy", "irregular galaxy", "nebula"], "It has spiral arms.")
H('9.B', 4, "Where is our solar system located in the Milky Way?", "in one of the spiral arms, far from the center", ["at the exact center", "outside the galaxy", "in a separate cluster"], "We are in the Orion Arm region.")
H('9.B', 4, "Galaxies are held together by...", "gravity", ["magnetism", "friction", "wind"], "Gravity binds stars and gas.")

# ---- 9.C origin of the universe
H('9.C', 2, "Which theory describes the origin of the universe from a hot, dense beginning?", "the Big Bang theory", ["the cell theory", "the plate tectonics theory", "the germ theory"], "The universe has been expanding since.")
H('9.C', 3, "Galaxies are moving away from each other. This is evidence that the universe is...", "expanding", ["shrinking", "standing still", "made of ice"], "Redshift shows galaxies receding.")
H('9.C', 3, "Light from distant galaxies is shifted toward the red end of the spectrum. This is called...", "redshift", ["blueshift", "reflection", "refraction only"], "It shows the galaxies move away.")
H('9.C', 4, "Cosmic microwave background radiation is evidence for...", "the early hot universe after the Big Bang", ["plate tectonics", "evolution", "climate change"], "It is leftover radiation from early times.")
H('9.C', 4, "Why do scientists look at light from distant galaxies to study the early universe?", "light takes a long time to travel, so we see the galaxy as it was long ago", ["light speeds up with distance", "light never travels", "galaxies make no light"], "Looking far away is looking back in time.")
H('9.C', 4, "A scientific theory is best described as...", "an explanation supported by a large body of evidence", ["a guess", "an opinion", "a law that never changes"], "Theories are tested and supported repeatedly.")
H('9.C', 4, "Which evidence supports the Big Bang theory?", "the observed expansion of the universe", ["the existence of seasons", "the water cycle", "tides"], "Expansion implies a beginning.")

# ---- 10.A Sun, hydrosphere, atmosphere
H('10.A', 2, "What is the main energy source for Earth's weather?", "the Sun", ["the Moon", "volcanoes", "ocean tides"], "The Sun heats the air and water unevenly.")
H('10.A', 3, "Differences in heating between land and sea cause...", "winds", ["earthquakes", "tides", "volcanoes"], "Warm air rises and cooler air moves in.")
H('10.A', 3, "Water evaporating from the ocean adds what to the atmosphere?", "water vapor", ["oxygen only", "salt", "ozone"], "Water vapor condenses into clouds.")
H('10.A', 3, "Weather is the condition of the atmosphere over a short time. Climate is...", "the average weather in a region over a long time", ["tomorrow's forecast", "the weather today", "the wind speed"], "Climate is long-term.")
H('10.A', 4, "Why are coastal areas often milder than inland areas?", "water heats and cools more slowly than land", ["land holds heat better than water", "oceans produce heat", "wind is stronger inland"], "Water has a high specific heat.")
H('10.A', 4, "Which process transfers energy from the ocean to the atmosphere?", "evaporation", ["erosion", "deposition", "sedimentation"], "Evaporation carries energy in water vapor.")
H('10.A', 4, "A region near the equator is warmer than one near the poles because...", "sunlight strikes more directly at the equator", ["the equator is closer to the Moon", "the poles have no atmosphere", "the equator has more gravity"], "Direct rays are more concentrated.")

# ---- 10.B global atmospheric patterns
H('10.B', 2, "Winds are caused by differences in...", "air pressure", ["gravity", "salinity", "mass"], "Air flows from high to low pressure.")
H('10.B', 3, "The Coriolis effect is caused by...", "Earth's rotation", ["the Moon's gravity", "ocean tides", "solar flares"], "It curves moving air and water.")
H('10.B', 3, "In the Northern Hemisphere, the Coriolis effect deflects moving air to the...", "right", ["left", "up", "down"], "Winds curve clockwise-ish to the right.")
H('10.B', 4, "Most of the United States is in a belt of winds that blow mostly from the west. They are called the...", "prevailing westerlies", ["trade winds", "polar easterlies", "doldrums"], "Weather systems usually move west to east.")
H('10.B', 4, "Why do weather systems in Texas usually move from west to east?", "prevailing westerly winds", ["the Moon's pull", "ocean tides", "volcanoes"], "The global wind belt pushes them east.")
H('10.B', 4, "The jet stream is...", "a fast current of air high in the atmosphere", ["an ocean current", "a type of cloud", "a mountain wind"], "It steers weather systems.")
H('10.B', 4, "Warm moist air rising at the equator is part of a global pattern called...", "atmospheric circulation", ["plate tectonics", "tides", "erosion"], "Heat drives the movement of air around Earth.")

# ---- 10.C hurricanes
H('10.C', 2, "Hurricanes form over...", "warm ocean water", ["cold ocean water", "deserts", "mountains"], "They draw energy from warm water.")
H('10.C', 3, "What sea surface temperature is generally needed for hurricanes to form?", "above about 26 C (80 F)", ["below 10 C", "exactly 0 C", "below freezing"], "Warm water supplies heat and moisture.")
H('10.C', 3, "A hurricane weakens when it moves over land because it loses...", "its supply of warm, moist ocean air", ["its wind", "its gravity", "its rotation direction"], "Land cuts off the energy source.")
H('10.C', 4, "In the Northern Hemisphere, a hurricane spins...", "counterclockwise", ["clockwise", "straight", "up and down only"], "Because of the Coriolis effect.")
H('10.C', 4, "The calm center of a hurricane is called the...", "eye", ["wall", "front", "ridge"], "Winds are light in the eye.")
H('10.C', 4, "Storm surge is dangerous because it...", "pushes a wall of seawater onto land", ["creates snow", "creates lightning only", "stops tides"], "Surge floods coastal areas.")
H('10.C', 4, "Warm ocean currents like the Gulf Stream can affect hurricanes by...", "supplying warm water that feeds storms", ["cooling the air above", "blocking all winds", "removing moisture"], "Warm water adds energy.")

# ---- 11.A natural events and climate
H('11.A', 3, "A large volcanic eruption can cool Earth's climate temporarily because ash and gases...", "reflect sunlight", ["trap more heat only", "create ocean currents", "cool the core"], "Particles in the air block some sunlight.")
H('11.A', 3, "A large meteor impact could change climate by throwing dust into the atmosphere that...", "blocks sunlight", ["adds oxygen", "warms the oceans", "speeds up tides"], "Darker, cooler conditions could follow.")
H('11.A', 4, "A sudden change in a major ocean current, such as the Gulf Stream, could...", "change regional climates", ["change the Moon", "stop all weather", "make the Sun hotter"], "Currents move heat.")
H('11.A', 4, "Volcanoes release carbon dioxide. Over millions of years this can...", "warm the climate", ["end all seasons", "stop photosynthesis", "freeze oceans"], "CO2 is a greenhouse gas.")
H('11.A', 4, "Which natural event can quickly cool Earth for a year or two?", "a major volcanic eruption", ["a hurricane", "a rainstorm", "a tide"], "Sulfur aerosols reflect sunlight.")
H('11.A', 4, "Ice cores show gas bubbles from long ago. Scientists use them to study...", "past climate", ["future tides", "ocean salt", "plate motion"], "Trapped air shows ancient atmosphere.")
H('11.A', 4, "The release of methane from thawing permafrost could...", "increase warming", ["cool the planet", "stop volcanoes", "slow the Sun"], "Methane is a greenhouse gas.")

# ---- 11.B human activities and climate
H('11.B', 2, "Burning fossil fuels adds which greenhouse gas to the air?", "carbon dioxide", ["oxygen", "nitrogen", "helium"], "Burning carbon fuels makes CO2.")
H('11.B', 3, "Cutting down forests can raise CO2 levels because fewer trees remain to...", "absorb carbon dioxide", ["make rain", "release methane", "cool the Sun"], "Trees take in CO2 for photosynthesis.")
H('11.B', 3, "Cities are often warmer than nearby rural areas. This is called the...", "urban heat island effect", ["greenhouse gap", "El Nino", "coastal breeze"], "Pavement and buildings hold heat.")
H('11.B', 4, "Which human activity adds methane to the atmosphere?", "raising livestock and rice farming", ["planting trees", "using solar panels", "riding bicycles"], "These practices release methane.")
H('11.B', 4, "Which action would help reduce greenhouse gas emissions?", "switching from coal to wind and solar power", ["burning more oil", "clearing more forests", "building more coal plants"], "Renewables release little CO2.")
H('11.B', 4, "Scientific measurements show atmospheric CO2 has risen since the Industrial Revolution. The best explanation is...", "increased burning of fossil fuels", ["more volcanoes erupting daily", "a hotter Sun only", "tidal changes"], "The rise tracks human fuel use.")
H('11.B', 4, "Urbanization affects climate mainly by...", "replacing vegetation with surfaces that absorb heat", ["adding more forests", "reducing temperature", "creating ocean currents"], "Pavement and rooftops warm the area.")

# ---- 11.C carbon cycle
H('11.C', 2, "Plants take in carbon dioxide during...", "photosynthesis", ["respiration", "decomposition", "combustion"], "They use CO2 to make sugars.")
H('11.C', 3, "Which process returns carbon dioxide to the atmosphere?", "respiration", ["photosynthesis", "condensation", "erosion"], "Organisms release CO2 as they use sugars.")
H('11.C', 3, "Where is carbon stored for millions of years?", "fossil fuels and limestone", ["clouds", "the Moon", "sunlight"], "Dead organisms and shells became fuels and rock.")
H('11.C', 3, "When wood burns, carbon returns to the air as...", "carbon dioxide", ["oxygen", "nitrogen", "helium"], "Combustion releases CO2.")
H('11.C', 4, "The oceans take up CO2 from the air. This helps to...", "slow the buildup of CO2 in the atmosphere", ["increase the CO2 in the air", "destroy carbon", "end photosynthesis"], "Oceans act as a carbon sink.")
H('11.C', 4, "Which sequence correctly shows carbon moving through a food chain?", "air to plant to animal to decomposers to air", ["animal to plant to air only", "plant to Sun to animal", "air to animal to Moon"], "Carbon flows through organisms and back to the atmosphere.")
H('11.C', 4, "Decomposers help the carbon cycle by...", "breaking down dead matter and releasing CO2", ["creating new carbon atoms", "removing all carbon", "producing sunlight"], "Carbon is recycled.")

# ---- 12.A food webs disruptions
H('12.A', 3, "If a disease kills most of the rabbits in a food web, the foxes that eat rabbits will most likely...", "have less food and decline", ["increase", "stay the same", "turn into herbivores"], "Fewer prey means less energy for predators.")
H('12.A', 3, "A wildfire destroys many plants in a forest. What happens to the herbivores?", "they lose food and their numbers fall", ["they increase", "they photosynthesize", "nothing"], "Less producer energy.")
H('12.A', 4, "Removing wolves from an ecosystem can cause the deer population to...", "increase, then overgraze the plants", ["decrease right away", "stay the same forever", "disappear"], "No predator limits the deer.")
H('12.A', 4, "An invasive species eats a native insect that many birds eat. What is the likely effect on the birds?", "less food, so bird populations may decline", ["more food", "no effect", "birds will start photosynthesis"], "Energy transfer to birds is reduced.")
H('12.A', 4, "A keystone species is one that...", "has a large effect on its ecosystem relative to its numbers", ["is the largest animal", "is always a predator", "lives in the ocean only"], "Removing it can disrupt the whole web.")
H('12.A', 4, "A factory pollutes a lake and kills the algae. Which organisms are affected first?", "those that eat algae", ["top predators only", "decomposers only", "birds far away"], "The base of the food web is disrupted.")
H('12.A', 4, "How does a drought affect the transfer of energy in a food web?", "less plant growth means less energy for consumers", ["more energy for all", "energy is destroyed", "it makes no difference"], "Producers capture less energy.")

# ---- 12.B ecological succession
H('12.B', 2, "Succession that begins on bare rock where no soil exists is called...", "primary succession", ["secondary succession", "climax removal", "extinction"], "Soil must form first.")
H('12.B', 3, "Succession after a forest fire, where soil is still present, is called...", "secondary succession", ["primary succession", "no succession", "tertiary succession"], "Soil remains, so recovery is faster.")
H('12.B', 3, "Which organisms are usually the first to colonize bare rock?", "lichens and mosses", ["oak trees", "deer", "wolves"], "They break rock down and help form soil.")
H('12.B', 4, "A volcano creates new land from lava. The first stage of life that appears is...", "pioneer species such as lichens", ["a mature forest", "large mammals", "tall trees"], "Pioneer species begin soil formation.")
H('12.B', 4, "As succession proceeds, species diversity typically...", "increases", ["decreases", "stays zero", "disappears"], "More niches become available.")
H('12.B', 4, "After a farm field is abandoned, grasses are followed by shrubs and then trees. This is an example of...", "secondary succession", ["primary succession", "extinction", "mutation"], "The soil was already present.")
H('12.B', 4, "Why is secondary succession usually faster than primary succession?", "soil and seeds are already present", ["there is no sunlight in primary", "plants grow faster in lava", "no organisms are needed"], "Soil formation takes a long time.")

# ---- 12.C biodiversity
H('12.C', 2, "Biodiversity refers to...", "the variety of living things in an area", ["the number of rocks", "the amount of rainfall", "the temperature"], "More species means higher biodiversity.")
H('12.C', 3, "An ecosystem with high biodiversity is usually more...", "stable", ["fragile", "lifeless", "uniform"], "Many species can fill roles if one declines.")
H('12.C', 3, "A farm with only one crop is at risk because...", "one disease could destroy the entire crop", ["it is too diverse", "pests avoid it", "it grows too fast"], "Low diversity increases vulnerability.")
H('12.C', 4, "Why does biodiversity help an ecosystem recover after a disturbance?", "different species fill different roles and help rebuild", ["all species are identical", "species stop competing", "extinction makes it stronger"], "Redundancy provides resilience.")
H('12.C', 4, "A coral reef with many species is healthier than one with few because...", "species depend on each other in many ways", ["each species is the same", "reefs do not need fish", "diversity lowers oxygen"], "Complex interactions maintain balance.")
H('12.C', 4, "Which activity reduces biodiversity?", "destroying habitat by clearing forests", ["protecting wetlands", "planting native species", "restoring a prairie"], "Habitat loss is the leading cause.")
H('12.C', 4, "Why is protecting many species important for people?", "ecosystems provide food, clean air, clean water and medicines", ["ecosystems are useless to people", "species are not connected", "it reduces oxygen"], "Humans depend on healthy ecosystems.")

# ---- 13.A cell structures
H('13.A', 2, "Which cell part controls the cell's activities and holds the DNA?", "nucleus", ["vacuole", "cell wall", "ribosome"], "The nucleus is the control center.")
H('13.A', 3, "Which organelle releases energy from food for the cell?", "mitochondrion", ["chloroplast", "nucleus", "vacuole"], "Mitochondria carry out cellular respiration.")
H('13.A', 3, "Which organelle captures light energy to make sugar?", "chloroplast", ["mitochondrion", "ribosome", "cell membrane"], "Chloroplasts are found in plant cells.")
H('13.A', 3, "Which structure gives a plant cell its rigid shape?", "cell wall", ["cell membrane only", "ribosome", "nucleus"], "The cell wall surrounds the membrane.")
H('13.A', 4, "Ribosomes in a cell function to...", "make proteins", ["store water", "capture light", "control entry only"], "Ribosomes assemble amino acids into proteins.")
H('13.A', 4, "Which part of a cell regulates what enters and leaves?", "cell membrane", ["cell wall only", "vacuole", "ribosome"], "It is selectively permeable.")
H('13.A', 4, "Which cell part is found in plant cells but NOT in animal cells?", "chloroplast", ["nucleus", "mitochondrion", "cytoplasm"], "Plants perform photosynthesis.")

# ---- 13.B genes and chromosomes
H('13.B', 2, "Genes are located on...", "chromosomes", ["ribosomes", "cell walls", "vacuoles"], "Chromosomes carry many genes.")
H('13.B', 3, "A gene is a segment of DNA that determines a(n)...", "inherited trait", ["cell wall", "organ", "ecosystem"], "Genes code for traits.")
H('13.B', 3, "Offspring receive genetic information from...", "both parents in sexual reproduction", ["only the father", "only the mother", "neither parent"], "Each parent gives half.")
H('13.B', 4, "Humans have 46 chromosomes in body cells. How many does an egg cell have?", "23", ["46", "92", "12"], "Sex cells carry half the number.")
H('13.B', 4, "Different forms of a gene are called...", "alleles", ["chromosomes", "proteins", "tissues"], "Alleles can be dominant or recessive.")
H('13.B', 4, "A trait that shows up when only one dominant allele is present is a...", "dominant trait", ["recessive trait", "mutation", "chromosome"], "A dominant allele masks a recessive one.")
H('13.B', 4, "In a Punnett square of Bb x Bb (B dominant), what fraction of offspring are bb?", "1/4", ["1/2", "3/4", "all"], "One of four boxes is bb.")

# ---- 13.C adaptations
H('13.C', 2, "A physical feature that helps an organism survive is called a(n)...", "structural adaptation", ["behavioral adaptation", "mutation", "habitat"], "Examples: fur, claws, beaks.")
H('13.C', 3, "Birds migrating south for winter is an example of a...", "behavioral adaptation", ["structural adaptation", "physiological adaptation", "mutation"], "It is an action that helps survival.")
H('13.C', 3, "A camel storing fat in its hump to survive long periods without food is a...", "physiological adaptation", ["behavioral adaptation", "migration", "territory"], "It relates to body processes.")
H('13.C', 4, "Why are individuals with helpful adaptations more likely to pass on their genes?", "they are more likely to survive and reproduce", ["they live forever", "they never get sick", "they mate more often by design"], "Natural selection favors them.")
H('13.C', 4, "A population has some individuals with thick fur and some with thin fur. A cold winter occurs. What is likely to happen?", "those with thick fur survive more often", ["all die", "thin fur is selected", "nothing changes"], "The environment favors thick fur.")
H('13.C', 4, "Octopuses changing color to blend in is an example of a(n)...", "adaptation that helps avoid predators", ["mutation that is harmful", "migration", "hibernation"], "Camouflage increases survival.")
H('13.C', 4, "Which would help a polar bear survive in the Arctic?", "a thick layer of fat and white fur", ["thin fur", "large ears for cooling", "a long thin tail for gliding"], "Insulation and camouflage.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g8_science.jsonl'))
print("saved", len(B.out), "questions")

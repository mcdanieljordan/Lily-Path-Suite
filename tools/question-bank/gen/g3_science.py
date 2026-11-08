#!/usr/bin/env python3
"""Grade 3 Science (TEKS 112.5.b) - original questions, content strands 6-13 (strands 1-5 are practices/themes, skipped).
   Run: python3 gen/g3_science.py  -> batches/g3_science.jsonl   Written by hand, 7 per standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.5.b.', 501, own='g3_science.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 6.A measure, test, record properties: temperature, mass, magnetism, sink or float
H('6.A', 2, "Which tool measures the mass of a rock?", "a balance", ["a thermometer", "a ruler", "a rain gauge"], "A balance compares or measures mass.")
H('6.A', 2, "Which tool should a student use to find the temperature of warm water?", "a thermometer", ["a balance", "a magnet", "a hand lens"], "A thermometer measures temperature.")
H('6.A', 3, "A student drops a wooden block and a steel nut in water. The block floats and the nut sinks. What property was tested?", "ability to sink or float", ["magnetism", "temperature", "color"], "The test showed which objects sink or float in water.")
H('6.A', 3, "A student holds a magnet near a steel paper clip, a plastic spoon, and a wooden stick. Which is pulled to the magnet?", "the paper clip", ["the spoon", "the stick", "none of them"], "Steel is attracted to magnets, and plastic and wood are not.")
H('6.A', 3, "Three rocks have masses of 20 g, 55 g, and 35 g. Which has the greatest mass?", "the 55 g rock", ["the 20 g rock", "the 35 g rock", "they all have the same"], "55 g is the greatest mass.")
H('6.A', 3, "Water in a cup measures 20°C at 9:00 and 28°C at 11:00. What happened to the water?", "it got warmer", ["it got colder", "it stayed the same", "it turned to ice"], "A higher temperature means it got warmer.")
H('6.A', 4, "A student wants to know if a coin is magnetic. What should the student do?", "hold a magnet near the coin", ["weigh the coin", "put the coin in water", "measure the coin's color"], "A magnet test shows if an object is magnetic.")

# ---- 6.B solids, liquids, gases; shape
H('6.B', 2, "Which state of matter keeps its own shape?", "a solid", ["a liquid", "a gas", "none of them"], "A solid has a definite shape.")
H('6.B', 2, "Juice is poured from a tall glass into a wide bowl. What happens to the juice?", "it takes the shape of the bowl", ["it keeps the glass shape", "it turns into a solid", "it disappears"], "A liquid takes the shape of its container.")
H('6.B', 3, "Which of these is a gas?", "the air in a balloon", ["a puddle", "a rock", "a metal key"], "Air is a gas.")
H('6.B', 3, "Which state of matter fills its whole container and spreads out?", "a gas", ["a solid", "a liquid", "ice"], "Gases spread to fill all the space available.")
H('6.B', 3, "A student puts the same amount of water into a tall cup and a short, wide cup. What stays the same?", "the amount of water", ["the shape of the water", "the height of the water", "the look of the water"], "The amount of water is the same, but the shape changes with the container.")
H('6.B', 3, "Which list contains a solid, a liquid, and a gas in that order?", "ice, milk, steam", ["milk, ice, steam", "steam, milk, ice", "ice, steam, milk"], "Ice is a solid, milk is a liquid, and steam is a gas.")
H('6.B', 4, "Which is NOT true of a solid?", "it takes the shape of any container", ["it has a definite shape", "it has a definite volume", "it keeps its shape on a table"], "Solids keep their shape. Liquids and gases take the shape of a container.")

# ---- 6.C changes in state caused by heating or cooling
H('6.C', 2, "What happens to an ice cube in a warm room?", "it melts into liquid water", ["it turns into a gas at once", "it becomes a rock", "it stays the same"], "Heat makes ice melt into water.")
H('6.C', 3, "Water droplets form on the outside of a cold glass on a hot day. What is this called?", "condensation", ["evaporation", "freezing", "melting"], "Water vapor in the air cools and turns into liquid water.")
H('6.C', 3, "A pot of water is heated until it bubbles and makes steam. What state of matter is steam?", "a gas", ["a solid", "a liquid", "a metal"], "Heating water can turn it into water vapor, a gas.")
H('6.C', 3, "A puddle on a sunny sidewalk gets smaller and smaller. What is happening?", "the water is evaporating", ["the water is freezing", "the water is turning to rock", "the water is melting"], "Heat from the Sun turns liquid water into water vapor.")
H('6.C', 2, "Liquid water is put in a freezer. What does it become?", "ice", ["steam", "soil", "vapor"], "Cooling a liquid enough makes it freeze into a solid.")
H('6.C', 3, "A student predicts that melted chocolate will become solid again in the refrigerator. Why?", "cooling makes liquids freeze or harden", ["heating makes liquids harden", "cold makes solids melt", "the refrigerator adds heat"], "Taking away heat makes the chocolate harden.")
H('6.C', 4, "Which sequence shows water changing from liquid to solid to liquid?", "water, ice, water", ["ice, steam, water", "steam, water, ice", "water, steam, ice"], "Freezing then melting changes water from a liquid to a solid and back.")

# ---- 6.D combine materials by physical properties to create or modify objects
H('6.D', 2, "Why might a builder use steel to build a bridge?", "it is strong", ["it is soft", "it melts easily", "it floats on air"], "Steel is strong and can hold weight.")
H('6.D', 3, "A student adds clay to sand to make a brick. Why?", "the clay helps hold the sand together", ["the clay makes the sand lighter", "the clay makes the sand disappear", "the clay makes the brick melt"], "Clay sticks the sand grains together and makes a stronger brick.")
H('6.D', 3, "A student needs a material for a raincoat. Which property matters most?", "it keeps water out", ["it is magnetic", "it is shiny", "it is loud"], "A raincoat should block water.")
H('6.D', 3, "A student needs a cup that will keep a drink warm. Which material is best?", "foam", ["thin metal", "paper towel", "wire mesh"], "Foam slows the loss of heat.")
H('6.D', 3, "Which two materials could a student combine to make a stronger, harder building block?", "sand and clay", ["water and air", "paper and tissue", "feathers and foam"], "Sand and clay combine to make a harder brick.")
H('6.D', 3, "A student builds a tower with straws. Which choice makes the tower stronger?", "tape the straws together at the joints", ["use fewer straws", "leave the straws loose", "use bent straws only"], "Taping joints holds parts together.")
H('6.D', 4, "A student must pick a material for an insulating lunch bag. Which property should be tested?", "how well it keeps heat from passing through", ["how loud it sounds", "how shiny it looks", "how magnetic it is"], "Insulation depends on how well heat is blocked.")

# ---- 7.A forces: contact and at a distance (magnetism, gravity, push, pull)
H('7.A', 2, "What force pulls a dropped ball toward the ground?", "gravity", ["magnetism", "friction only", "light"], "Gravity pulls objects toward Earth.")
H('7.A', 3, "A magnet pulls a paper clip without touching it. What kind of force is this?", "a force at a distance", ["a force that needs touching", "no force", "a sound"], "Magnetic force can act without contact.")
H('7.A', 2, "A student kicks a soccer ball. What kind of force is a kick?", "a push", ["a pull", "gravity", "magnetism"], "Kicking pushes the ball.")
H('7.A', 3, "A child pulls a wagon by its handle. This is an example of what?", "a force that needs touching", ["a force at a distance", "gravity only", "magnetism only"], "The handle touches the wagon as the child pulls.")
H('7.A', 3, "A ball thrown up in the air slows down and falls back. Which force pulls it down?", "gravity", ["magnetism", "light", "sound"], "Gravity pulls the ball back to Earth.")
H('7.A', 3, "Which of these forces can act on an object without touching it?", "gravity and magnetism", ["pushing and pulling by hand", "kicking and throwing", "pushing a door"], "Gravity and magnetism can act from a distance.")
H('7.A', 4, "Two magnets are placed near each other and move apart. What force is acting?", "magnetic force pushing them apart", ["gravity pulling them together", "heat pushing them apart", "friction pulling them together"], "Magnets can push each other away.")

# ---- 7.B position and motion changed by pushes and pulls
H('7.B', 2, "A student gives a swing a push. What changes about the swing?", "its motion", ["its color", "its material", "its weight"], "A push changes the motion of the swing.")
H('7.B', 3, "A student pushes a ball with a small force and then a large force. Which push moves the ball farther?", "the large force", ["the small force", "both the same", "neither"], "A greater force changes the motion more.")
H('7.B', 3, "A student measures how far a toy car rolls after being pushed three times. What is the student measuring?", "the change in position", ["the color of the car", "the weight of the car", "the cost of the car"], "Distance traveled shows how the position changed.")
H('7.B', 3, "A child pulls a wagon with a rope. Which way does the wagon move?", "toward the child", ["away from the child", "straight up", "it does not move"], "A pull moves an object toward the puller.")
H('7.B', 3, "A rolling ball is stopped when a student presses a hand on it. What did the hand do?", "it changed the motion with a push", ["it added gravity", "it made a magnet", "it made light"], "A push can stop a moving object.")
H('7.B', 2, "A student wants to make a ball roll faster. What should the student do?", "push it harder", ["push it softly", "not push it", "pull it away slowly"], "A harder push gives more speed.")
H('7.B', 4, "A student records: push 1 moved a car 30 cm, push 2 moved it 60 cm, push 3 moved it 90 cm. What is the likely pattern?", "each push was stronger than the last", ["each push was weaker than the last", "each push was the same", "the car got lighter each time"], "More distance means a stronger push.")

# ---- 8.A everyday examples of energy: light, sound, thermal, mechanical
H('8.A', 2, "A lamp gives off what kind of energy?", "light energy", ["sound energy", "mechanical energy", "chemical energy"], "A lamp gives off light.")
H('8.A', 2, "A drum being hit gives off what kind of energy?", "sound energy", ["light energy", "thermal energy", "magnet energy"], "A drum gives off sound energy.")
H('8.A', 3, "A hot stove gives off what kind of energy?", "thermal energy", ["sound energy", "light energy only", "magnetic energy"], "Thermal energy is heat energy.")
H('8.A', 3, "A rolling bowling ball has what kind of energy?", "mechanical energy", ["thermal energy", "light energy", "sound energy"], "Moving objects have mechanical energy.")
H('8.A', 3, "A campfire gives off which two forms of energy?", "light and thermal", ["sound and mechanical", "mechanical and magnetic", "only sound"], "A fire gives off light and heat.")
H('8.A', 3, "A bell is rung. What energy can you hear?", "sound energy", ["thermal energy", "light energy", "mechanical energy only"], "Sound energy travels from the bell to your ears.")
H('8.A', 4, "A toaster gives off heat and a red glow. Which two forms of energy are these?", "thermal and light", ["sound and mechanical", "mechanical and sound", "magnetic and chemical"], "Heat is thermal energy and a glow is light energy.")

# ---- 8.B speed related to mechanical energy
H('8.B', 3, "A ball rolls faster down a steep ramp than a gentle one. Which has more mechanical energy at the bottom?", "the ball on the steep ramp", ["the ball on the gentle ramp", "they have the same", "neither has any"], "The faster-moving ball has more mechanical energy.")
H('8.B', 3, "A student pushes a toy car harder. What happens to its speed and energy?", "both increase", ["both decrease", "speed increases and energy decreases", "nothing changes"], "More force gives more speed and more mechanical energy.")
H('8.B', 3, "A toy car moves slowly across a rug. A second moves quickly. Which has more mechanical energy?", "the quick car", ["the slow car", "both the same", "neither"], "A faster object has more mechanical energy.")
H('8.B', 3, "A student releases a ball from a low height and then from a higher height. Which ball is going faster when it hits the floor?", "the ball dropped from higher", ["the ball dropped from lower", "they are the same", "neither one moves"], "A higher drop gives more speed.")
H('8.B', 2, "A ball rolls slowly and then speeds up. What happens to its mechanical energy?", "it increases", ["it decreases", "it stays the same", "it disappears"], "A faster object has more mechanical energy.")
H('8.B', 3, "A student tests how far a ball rolls from ramps of different heights. What does the student change?", "the height of the ramp", ["the color of the ball", "the day of the week", "the room's lights"], "Ramp height changes the ball's speed and energy.")
H('8.B', 4, "A student records the ball's speed on three ramps: 1 m/s, 2 m/s, 3 m/s. Which ramp gives the ball the most mechanical energy?", "the ramp with 3 m/s", ["the ramp with 1 m/s", "the ramp with 2 m/s", "they are all the same"], "Greater speed means more mechanical energy.")

# ---- 9.A orbits of Sun, Earth, Moon
H('9.A', 2, "What does Earth orbit?", "the Sun", ["the Moon", "Mars", "a star at night"], "Earth moves around the Sun.")
H('9.A', 2, "What orbits Earth?", "the Moon", ["the Sun", "Jupiter", "Mercury"], "The Moon orbits Earth.")
H('9.A', 3, "About how long does it take Earth to orbit the Sun once?", "one year", ["one day", "one week", "one month"], "Earth takes about 365 days.")
H('9.A', 3, "About how long does it take the Moon to orbit Earth once?", "about one month", ["one day", "one year", "one hour"], "The Moon orbits Earth in about 27 to 29 days.")
H('9.A', 3, "A student models the Sun with a lamp, Earth with a ball, and the Moon with a smaller ball. Which moves around Earth?", "the small ball", ["the lamp", "the large ball around the small ball", "none of them"], "The Moon orbits Earth.")
H('9.A', 3, "What causes day and night on Earth?", "Earth spinning on its axis", ["the Moon blocking the Sun", "Earth moving around the Moon", "clouds covering Earth"], "Earth's spin makes one side face the Sun at a time.")
H('9.A', 4, "In a model, the Sun is at the center. Which path does Earth follow?", "a path around the Sun", ["a path around the Moon", "a straight line away from the Sun", "a path around Mars"], "Earth orbits the Sun.")

# ---- 9.B order of planets
H('9.B', 2, "Which planet is closest to the Sun?", "Mercury", ["Earth", "Jupiter", "Neptune"], "Mercury is the planet closest to the Sun.")
H('9.B', 2, "Which planet do we live on?", "Earth", ["Mars", "Venus", "Saturn"], "People live on Earth.")
H('9.B', 3, "Which planet is third from the Sun?", "Earth", ["Venus", "Mars", "Jupiter"], "The order starts Mercury, Venus, Earth, Mars.")
H('9.B', 3, "Which planet is between Earth and Jupiter?", "Mars", ["Venus", "Saturn", "Mercury"], "Mars is fourth from the Sun, between Earth and Jupiter.")
H('9.B', 3, "Which planet is the farthest from the Sun?", "Neptune", ["Saturn", "Earth", "Venus"], "Neptune is the eighth planet.")
H('9.B', 3, "Which list shows the first four planets in order from the Sun?", "Mercury, Venus, Earth, Mars", ["Venus, Mercury, Mars, Earth", "Earth, Venus, Mercury, Mars", "Mars, Earth, Venus, Mercury"], "The inner planets are Mercury, Venus, Earth, and Mars.")
H('9.B', 4, "Jupiter is the fifth planet from the Sun. Which planet is sixth?", "Saturn", ["Mars", "Uranus", "Neptune"], "Saturn comes after Jupiter.")

# ---- 10.A weather in different locations at the same time
H('10.A', 2, "At the same time, it is snowing in one town and sunny in another town. What does this show?", "weather can differ from place to place", ["weather is the same everywhere", "weather only changes at night", "snow only falls in the sun"], "Different places can have different weather at once.")
H('10.A', 3, "A weather map shows 35°F in one town and 80°F in another town. Which town is warmer?", "the 80°F town", ["the 35°F town", "they are the same", "neither"], "80°F is warmer than 35°F.")
H('10.A', 3, "A wind vane points north. From which direction is the wind blowing?", "from the north", ["from the south", "from the east", "it is not blowing"], "A wind vane points into the wind.")
H('10.A', 3, "A rain gauge in Town A collected 3 cm. A gauge in Town B collected 0 cm. What can you say?", "it rained more in Town A", ["it rained more in Town B", "it rained the same in both", "it did not rain in Town A"], "3 cm is more than 0 cm.")
H('10.A', 3, "Which tool tells wind direction?", "a wind vane", ["a rain gauge", "a thermometer", "a balance"], "A wind vane shows the direction of the wind.")
H('10.A', 2, "Which kind of weather data is measured in degrees?", "air temperature", ["wind direction", "rainfall", "cloud cover"], "Temperature is measured in degrees.")
H('10.A', 4, "A student compares weather in Dallas, Denver, and Miami. Which should the student record to compare at the SAME time?", "the readings from each place at the same hour", ["readings from different days", "only the coldest town", "only the rainiest day"], "Comparisons need data taken at the same time.")

# ---- 10.B soils formed by weathering of rock and decomposition
H('10.B', 2, "Rocks can break into smaller pieces over time. What is this process called?", "weathering", ["freezing", "migration", "pollination"], "Wind, water, and ice break rocks into smaller pieces.")
H('10.B', 3, "How does sand form?", "rocks break into tiny pieces", ["clouds fall to the ground", "plants turn into rock", "water becomes solid"], "Weathered rock makes sand.")
H('10.B', 3, "How do dead plants and animals help make soil?", "they break down and mix into the ground", ["they turn to metal", "they float away", "they make the ground colder"], "Decomposition adds nutrients and organic matter to soil.")
H('10.B', 3, "Water freezes in a crack in a rock and the crack gets wider. What does this show?", "ice can weather rock", ["ice makes rock grow", "water makes rock lighter", "rock eats ice"], "Freezing water expands and can crack rock.")
H('10.B', 3, "Which helps form clay soil?", "very fine pieces of weathered rock", ["large boulders", "pieces of glass", "plastic bags"], "Clay forms from very small weathered rock pieces.")
H('10.B', 3, "Which is a living thing that helps break down dead leaves into soil?", "an earthworm", ["a rock", "a wind", "a puddle"], "Earthworms and other decomposers break down plant remains.")
H('10.B', 4, "Topsoil is dark and rich. What makes it dark?", "decayed plant and animal material", ["crushed glass", "melted metal", "ice crystals"], "Decayed living things add dark organic matter.")

# ---- 10.C rapid changes in Earth's surface
H('10.C', 2, "Which is a rapid change to Earth's surface?", "a volcanic eruption", ["a canyon forming over millions of years", "a mountain slowly wearing away", "soil forming over centuries"], "Eruptions happen quickly.")
H('10.C', 3, "What happens in an earthquake?", "the ground shakes", ["the ground freezes", "the sky turns dark", "the ocean dries up"], "Earthquakes shake the ground.")
H('10.C', 3, "After heavy rain, a hillside slides down. What is this called?", "a landslide", ["an earthquake", "an eruption", "a drought"], "A landslide is a rapid movement of soil and rock down a slope.")
H('10.C', 3, "What comes out of a volcano during an eruption?", "lava, ash, and gas", ["clear water", "snow", "plants"], "Eruptions release lava, ash, and gases.")
H('10.C', 3, "A student models a landslide by pouring water over a pile of sand on a slope. What does the model show?", "water can move soil quickly downhill", ["water makes soil rise", "sand can't move", "slopes stay flat"], "Water can loosen and move soil rapidly.")
H('10.C', 3, "Which change happens SLOWLY?", "a river carving a canyon", ["a volcanic eruption", "an earthquake", "a landslide"], "Carving a canyon takes a very long time.")
H('10.C', 4, "A model of an earthquake uses a table that shakes with blocks on top. What do the blocks show?", "buildings can shake and fall", ["buildings float away", "buildings melt", "buildings grow"], "Shaking the ground can damage buildings.")

# ---- 11.A how humans use natural resources
H('11.A', 2, "Farmers use soil and water to do what?", "grow crops", ["make electricity", "melt metal", "build roads"], "Soil and water help crops grow.")
H('11.A', 3, "Wood from trees is used to do what?", "build houses", ["make rain", "light the sky", "make wind"], "Wood is a building material.")
H('11.A', 3, "Oil is a natural resource used for what?", "making fuel for cars", ["growing plants", "making shade", "making soil"], "Oil is refined into gasoline and other fuels.")
H('11.A', 3, "Metal ores are used to do what?", "make cars and tools", ["make snow", "make food", "make rain"], "Metals from ores are used to make many products.")
H('11.A', 2, "Which natural resource do people drink?", "water", ["coal", "wood", "iron"], "People need drinking water.")
H('11.A', 3, "Which use of a natural resource is for transportation?", "gasoline for a car", ["wood in a fireplace", "water for a garden", "stone in a wall"], "Gasoline powers cars.")
H('11.A', 4, "Cotton is a plant grown by farmers. What product is made from it?", "cloth for clothing", ["gasoline", "glass", "steel"], "Cotton fibers are used to make cloth.")

# ---- 11.B why conservation of natural resources is important
H('11.B', 2, "Why is it important to conserve natural resources?", "so they last longer", ["so they disappear faster", "so people have less", "so they cost nothing"], "Conserving makes resources last.")
H('11.B', 3, "Some resources, like oil, cannot be replaced quickly. What can happen if we use them too fast?", "they could run out", ["they will refill right away", "there will be more of them", "nothing changes"], "Nonrenewable resources can run out.")
H('11.B', 3, "Which resource can be replaced by planting new ones?", "trees", ["coal", "oil", "natural gas"], "Trees are renewable because new ones can be grown.")
H('11.B', 3, "Why is clean water important to protect?", "all living things need it", ["only fish need it", "it is never used", "it is endless"], "All living things need clean water.")
H('11.B', 3, "What might happen to animals if forests are cut down too fast?", "they could lose their homes", ["they would get bigger", "they would find more food", "they would become plants"], "Cutting forests removes habitat.")
H('11.B', 2, "Which statement best explains conservation?", "using resources carefully", ["using as much as possible", "wasting resources", "ignoring resources"], "Conservation means using resources wisely.")
H('11.B', 4, "A city is running low on water in summer. Why should people conserve it?", "there may not be enough for everyone", ["water costs nothing", "water is made by people", "water never runs out"], "Water supplies can run low during dry times.")

# ---- 11.C ways to conserve: reduce, reuse, recycle
H('11.C', 2, "Which is an example of REDUCING?", "using fewer plastic bags", ["throwing away trash", "buying lots of items", "littering"], "Reducing means using less.")
H('11.C', 2, "Which is an example of REUSING?", "using a glass jar to hold crayons", ["throwing the jar away", "breaking the jar", "burying the jar"], "Reusing means using an item again.")
H('11.C', 3, "Which is an example of RECYCLING?", "turning old cans into new cans", ["throwing cans in a lake", "burying cans", "using cans as toys only"], "Recycling turns used items into new ones.")
H('11.C', 3, "Which material is made from recycled paper?", "a cardboard box", ["a glass bottle", "a metal can", "a plastic toy"], "Cardboard can be made from recycled paper.")
H('11.C', 3, "A student uses a cloth bag instead of a new paper bag each time. What is this?", "reusing and reducing", ["wasting", "littering", "burning"], "A cloth bag is used again and reduces waste.")
H('11.C', 3, "Which choice saves the most natural resources?", "reduce, reuse, and recycle", ["throw away often", "use things once", "buy new items often"], "These actions help conserve resources.")
H('11.C', 4, "A school collects used paper and sends it to a plant that makes new paper. What does this save?", "trees", ["metal", "plastic", "glass"], "Recycling paper reduces the need to cut trees.")

# ---- 12.A temperature and precipitation affect animals and plants: migration, hibernation, dormancy
H('12.A', 2, "Some birds fly south for the winter. What is this called?", "migration", ["hibernation", "dormancy", "metamorphosis"], "Migration is moving to another place for the season.")
H('12.A', 3, "A bear sleeps through much of the winter in a den. What is this called?", "hibernation", ["migration", "pollination", "dormancy"], "Hibernation is a long, deep sleep to survive winter.")
H('12.A', 3, "Maple trees lose their leaves and stop growing in winter. What is this called?", "dormancy", ["migration", "hibernation", "camouflage"], "Plants rest in dormancy when it is cold.")
H('12.A', 3, "Why do some animals migrate in the fall?", "to find warmer places with more food", ["to find colder weather", "to build ice dens", "to avoid all other animals"], "Cold temperatures reduce food supplies.")
H('12.A', 3, "A desert plant stays dormant during a long dry period. What does this help it do?", "survive until rain returns", ["grow faster", "make more shade", "move to a new place"], "Dormancy saves water and energy.")
H('12.A', 3, "Which animal is known for hibernating?", "a bear", ["a goose", "a butterfly", "a dolphin"], "Many bears hibernate in winter.")
H('12.A', 4, "A spring with lots of rain makes many wildflowers grow. What does this show?", "rain affects plant growth", ["rain stops plants from growing", "flowers prefer drought", "weather has no effect"], "Precipitation helps plants grow.")

# ---- 12.B flow of energy in a food chain; changes
H('12.B', 2, "Where does the energy in most food chains begin?", "the Sun", ["the Moon", "rocks", "wind"], "Plants use sunlight, and animals get energy from plants.")
H('12.B', 3, "In the food chain sun → grass → grasshopper → frog, what does the frog get energy from?", "eating the grasshopper", ["the grass directly", "the Sun directly", "the water only"], "The frog gets its energy by eating the grasshopper.")
H('12.B', 3, "All the frogs are removed from a pond. What may happen to the insects the frogs ate?", "there may be more insects", ["there may be fewer insects", "nothing will change", "the insects will turn into frogs"], "Without frogs eating them, insect numbers may grow.")
H('12.B', 3, "All the bees disappear from a field of flowers. What might happen to the plants?", "fewer seeds may be made", ["more seeds will be made", "nothing will change", "plants will move"], "Bees help pollinate flowers.")
H('12.B', 3, "Which living thing is a PRODUCER?", "grass", ["a rabbit", "a hawk", "a snake"], "Grass makes its own food.")
H('12.B', 3, "Which shows a food chain in the correct order, starting with the producer?", "seeds → mouse → snake → hawk", ["hawk → snake → mouse → seeds", "mouse → seeds → snake → hawk", "snake → hawk → seeds → mouse"], "Energy starts with the producer and passes to each consumer in order.")
H('12.B', 4, "Fish in a lake eat small water insects. If the insects are poisoned, what may happen to the fish?", "the fish may have less food", ["the fish will have more food", "the fish will become insects", "nothing will happen"], "Animals depend on the organisms they eat.")

# ---- 12.C natural changes (floods, droughts) cause some organisms to thrive, perish, or move
H('12.C', 2, "A long drought dries up a pond. What may happen to the fish there?", "they may die or the pond life must move", ["they will grow bigger", "they will turn into frogs", "they will multiply faster"], "Fish need water to live.")
H('12.C', 3, "A flood washes away a field of plants. What may happen to the animals that depended on them?", "they may move away to find food", ["they will find more food there", "they will stay and grow bigger", "they will turn into plants"], "Animals may relocate if food is gone.")
H('12.C', 3, "After a flood, new plants grow in the soil left behind. Which organisms benefit?", "plants that like wet, rich soil", ["plants that need no water", "desert plants only", "no plants"], "Flood deposits can enrich soil.")
H('12.C', 3, "During a drought, which plant is most likely to survive?", "a cactus", ["a water lily", "a fern", "a moss"], "A cactus stores water.")
H('12.C', 3, "Why might frogs thrive after a wet season?", "there are more ponds to live and breed in", ["there are fewer insects", "there are fewer plants", "there is less water"], "More water gives frogs more places to live.")
H('12.C', 3, "A drought makes grass turn brown. What might the deer that eat grass do?", "move to a new area with food", ["eat rocks", "grow wings", "turn into plants"], "Animals move to find food.")
H('12.C', 4, "Which natural change could cause some organisms to perish?", "a long flood or drought", ["a gentle breeze", "a sunny afternoon", "a light rain shower"], "Extreme changes can harm living things.")

# ---- 12.D fossils as evidence of past living organisms and environments
H('12.D', 2, "What is a fossil?", "the remains or traces of a living thing from long ago", ["a new plant", "a modern animal", "a kind of weather"], "Fossils are preserved evidence of past life.")
H('12.D', 3, "A fossil of a fish is found in the desert. What does this suggest?", "the area was once covered by water", ["fish live in deserts", "fish fell from the sky", "the desert was always dry"], "A fish fossil shows water used to be there.")
H('12.D', 3, "Where are fossils usually found?", "in layers of rock", ["in clouds", "in puddles", "in the air"], "Fossils are preserved in sedimentary rock.")
H('12.D', 3, "What can a scientist learn from a fossil leaf?", "what plants lived there long ago", ["what the weather is today", "how fast a car goes", "what time it is"], "Fossils show past life.")
H('12.D', 3, "Which is a fossil found in Texas?", "a dinosaur footprint", ["a modern cactus", "a new bird nest", "a tire track"], "Texas has dinosaur tracks, including at Dinosaur Valley State Park.")
H('12.D', 3, "Which fossils might be found in a limestone rock that was once an ocean floor?", "seashells", ["tree trunks", "cactus spines", "grass blades"], "Ocean animals leave fossil shells.")
H('12.D', 4, "A scientist finds fossil ferns in a dry area. What does this tell about long ago?", "the area was wetter then", ["the area was snowy", "the area was always dry", "ferns grow in deserts"], "Ferns need moist places.")

# ---- 13.A external structures and functions help animals survive
H('13.A', 2, "A giraffe has a long neck. How does this help it survive?", "it can reach leaves high in trees", ["it can swim", "it can dig", "it can hide in grass"], "A long neck reaches food high in trees.")
H('13.A', 2, "A duck has webbed feet. How does this help it?", "it can paddle through water", ["it can climb trees", "it can run fast on land", "it can dig burrows"], "Webbed feet push against water.")
H('13.A', 3, "A cheetah has long, strong legs. How does this help it?", "it can run fast to catch prey", ["it can fly", "it can swim", "it can climb walls"], "Long legs help it sprint.")
H('13.A', 3, "A porcupine has sharp quills. How do they help it?", "they protect it from predators", ["they help it fly", "they help it swim", "they help it see in the dark"], "Quills defend against attackers.")
H('13.A', 3, "A sloth has long, strong claws. How do they help it?", "they let it hang from tree branches", ["they let it swim", "they let it fly", "they let it dig deep tunnels"], "Claws hold branches.")
H('13.A', 3, "An owl has large eyes. How do large eyes help it?", "it can see well at night", ["it can swim", "it can smell better", "it can hear less"], "Large eyes gather more light in the dark.")
H('13.A', 4, "A hummingbird has a long, thin beak. What does this structure help it do?", "reach nectar deep inside flowers", ["crack open nuts", "catch fish", "dig for worms"], "A long thin beak fits deep into flowers.")

# ---- 13.B life cycles in organisms: beetles, crickets, radishes, lima beans
H('13.B', 2, "A beetle has four stages: egg, larva, pupa, adult. This is called what?", "complete metamorphosis", ["incomplete metamorphosis", "no change", "migration"], "Four stages means complete metamorphosis.")
H('13.B', 3, "A cricket nymph looks like a small adult cricket. Which type of life cycle does it have?", "incomplete metamorphosis", ["complete metamorphosis", "no life cycle", "plant cycle"], "Incomplete metamorphosis has egg, nymph, and adult stages.")
H('13.B', 3, "A lima bean seed is planted. Which stage comes next?", "a seedling sprouts", ["it becomes a flower first", "it becomes fruit first", "it becomes a seed again"], "A seed sprouts into a seedling.")
H('13.B', 3, "Which is the correct order for a radish plant?", "seed, seedling, adult plant, seed", ["adult plant, seed, seedling", "seedling, seed, adult plant", "seed, adult plant, seedling"], "Plants grow from seed to seedling to adult and make new seeds.")
H('13.B', 3, "How is a beetle larva different from an adult beetle?", "the larva looks very different", ["the larva looks the same", "the larva has wings", "the larva is larger"], "In complete metamorphosis, larvae differ from adults.")
H('13.B', 3, "What is the last stage of a beetle's life cycle?", "adult", ["egg", "pupa", "larva"], "The adult is the final stage.")
H('13.B', 4, "A student compares a bean plant and a beetle. What do both have?", "a life cycle with stages", ["the same number of stages", "no changes", "wings"], "All living things go through a life cycle.")

B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'g3_science.jsonl'))
print("saved", len(B.out), "questions")

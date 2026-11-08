#!/usr/bin/env python3
"""Kindergarten Science (TEKS 112.2.b) - original questions, content strands 6-13 (strands 1-5 are practices/themes, skipped like Math's process standards).
   Run: python3 gen/gk_science.py  -> batches/gk_science.jsonl   Written by hand, 7 per standard."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.2.b.', 201, own='gk_science.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# ---- 6 physical properties of objects (shape, color, texture, material), classify
H('6', 2, "Which word tells about the TEXTURE of a cotton ball?", "soft", ["loud", "cold", "heavy"], "Texture is how something feels. A cotton ball feels soft.")
H('6', 2, "Which material is a brick for building a wall made of?", "baked clay", ["paper", "cloth", "glass"], "Material is what an object is made of. A brick is made of baked clay.")
H('6', 3, "You sort blocks into two groups: RED and BLUE. What property did you use?", "color", ["shape", "texture", "material"], "Sorting into red and blue groups uses color.")
H('6', 2, "Which object is made of metal?", "a spoon", ["a paper cup", "a wool sock", "a wooden block"], "A spoon is usually made of metal. The others are paper, wool, and wood.")
H('6', 3, "Which two objects have the same SHAPE?", "a ball and an orange", ["a ball and a book", "a box and an orange", "a pencil and a ball"], "A ball and an orange are both round like a sphere.")
H('6', 3, "A sandpaper sheet feels rough. A glass window feels smooth. What property is different?", "texture", ["color", "shape", "size"], "Rough and smooth tell how things feel, which is texture.")
H('6', 4, "Which group could hold ONLY things made of wood?", "a pencil, a chair, a block", ["a spoon, a coin, a key", "a bottle, a cup, a bowl made of plastic", "a sock, a hat, a scarf"], "A pencil, a chair, and a block can all be made of wood.")

# ---- 7 magnets push and pull
H('7', 2, "Which object will a magnet pull toward it?", "a metal paper clip", ["a wooden spoon", "a rubber ball", "a paper cup"], "Magnets pull some metals, like iron. A paper clip is made of steel.")
H('7', 2, "Which object will a magnet NOT pick up?", "a plastic toy", ["a steel nail", "an iron key", "a steel paper clip"], "Magnets do not pull plastic.")
H('7', 3, "A magnet moves a toy car closer to it. What did the magnet do?", "pulled the car", ["pushed the car", "painted the car", "melted the car"], "Moving the car closer means the magnet pulled it.")
H('7', 3, "Two magnets are put together and move AWAY from each other. What happened?", "they pushed each other", ["they pulled each other", "they broke", "they got warm"], "Magnets can push each other away.")
H('7', 2, "A magnet can make some things move without touching them. What does a magnet do?", "pushes or pulls", ["makes light", "makes sound", "grows plants"], "A magnet pushes or pulls some objects.")
H('7', 3, "You predict a magnet will pick up a coin made of wood. Is it a good prediction?", "no, wood is not pulled by a magnet", ["yes, magnets pick up all things", "yes, wood is metal", "no, coins are too small"], "Magnets do not pull wood.")
H('7', 4, "Which tool could a magnet help you use to pick up pins spilled on the floor?", "a magnet on a stick", ["a wooden ruler", "a plastic comb", "a paper towel tube"], "Steel pins are pulled to a magnet.")

# ---- 8.A light needed to see; amounts of light
H('8.A', 2, "What do you need in order to see objects?", "light", ["silence", "wind", "water"], "Objects can only be seen when there is light.")
H('8.A', 2, "A closet has no light and the door is shut. What can you see inside?", "nothing", ["everything clearly", "only red things", "only big things"], "Without a light source, objects cannot be seen.")
H('8.A', 3, "Which is a source of light?", "the Sun", ["the Moon", "a mirror", "a white wall"], "The Sun makes its own light. The Moon and a mirror only reflect light.")
H('8.A', 3, "Which room is the BRIGHTEST?", "a room with the lamp on and the window open", ["a room with only a small night-light", "a room with the lights off", "a room with the curtains closed and no lights"], "More light makes things look brighter.")
H('8.A', 3, "It is dim in a room. What can you do to see a book better?", "turn on a lamp", ["close your eyes", "turn off the light", "cover the window"], "A lamp adds light so the book is easier to see.")
H('8.A', 2, "Which object makes its own light?", "a flashlight", ["a book", "a shoe", "a rock"], "A flashlight makes light. The others do not.")
H('8.A', 4, "Two pictures are on a wall. One is in bright light and one is in dim light. Which is easier to see?", "the one in bright light", ["the one in dim light", "they look the same", "neither one"], "More light makes objects easier to see.")

# ---- 8.B light through objects; shadows
H('8.B', 2, "Light goes through a clear window. What does the window do to light?", "lets light pass through", ["blocks all the light", "turns light into sound", "makes light heavier"], "Clear glass lets light pass through.")
H('8.B', 2, "What makes a shadow?", "something that blocks light", ["something that makes sound", "something that is cold", "something that is soft"], "A shadow forms when an object blocks light.")
H('8.B', 3, "Which object makes the DARKEST shadow?", "a wooden board", ["a clear glass cup", "a clear plastic bag", "clear plastic wrap"], "A wooden board blocks light. Clear things let light through.")
H('8.B', 3, "Where do you see your shadow on a sunny day?", "on the ground away from the Sun", ["inside the Sun", "in the sky", "behind a clear window"], "Your body blocks sunlight, so a shadow forms on the ground.")
H('8.B', 3, "Which object lets MOST light pass through?", "a clear glass jar", ["a metal pot", "a cardboard box", "a wooden door"], "A clear glass jar lets light through.")
H('8.B', 2, "A student holds a hand in front of a flashlight. What appears on the wall?", "a shadow", ["a rainbow", "a sound", "a plant"], "The hand blocks the light and makes a shadow.")
H('8.B', 4, "Which object blocks light, so it makes a shadow?", "a book", ["clear plastic wrap", "a clean glass window", "clear water in a glass"], "A book blocks light. The other choices are clear.")

# ---- 9.A patterns of day and night
H('9.A', 1, "When is the Sun seen in the sky?", "during the day", ["at night", "never", "only in winter"], "We see the Sun during the day.")
H('9.A', 2, "What comes after day?", "night", ["day again right away", "summer", "spring"], "Night follows day.")
H('9.A', 2, "Which is something you can see in the sky at night?", "stars", ["the Sun", "a rainbow", "a sunrise"], "Stars are seen at night. The Sun is seen during the day.")
H('9.A', 2, "When do most people sleep?", "at night when it is dark", ["at noon when it is bright", "in the morning sun", "when the Sun is highest"], "Most people sleep at night when it is dark.")
H('9.A', 3, "Is it warmer outside in the middle of a sunny day or in the middle of the night?", "in the middle of the day", ["in the middle of the night", "they are always the same", "it is warmer at night in every season"], "The Sun warms the Earth during the day.")
H('9.A', 3, "The pattern of day and night happens over and over. Which comes first, then second?", "day, then night, then day", ["night, night, night", "day, day, day", "night, then night, then day"], "Day and night take turns in a repeating pattern.")
H('9.A', 4, "A student sees the Sun coming up in the morning. What will happen later that day?", "the Sun will go down and it will get dark", ["the Sun will stay up all night", "the Moon will stay out all day", "the stars will come out first"], "After the Sun sets, it gets dark and night begins.")

# ---- 9.B Sun, Moon, stars, clouds
H('9.B', 2, "Which object in the sky gives us light and heat during the day?", "the Sun", ["the Moon", "a star at night", "a cloud"], "The Sun gives light and heat to Earth.")
H('9.B', 2, "Which of these can you see in the sky during the day?", "clouds", ["stars shining bright", "a dark sky", "a night-light"], "Clouds are seen in the sky during the day.")
H('9.B', 3, "Which sky object do people often see at night with a different shape on different nights?", "the Moon", ["the Sun", "a cloud", "a rainbow"], "The Moon looks different on different nights.")
H('9.B', 3, "Which sky objects look like tiny dots of light at night?", "stars", ["clouds", "rainbows", "birds"], "Stars look like tiny dots of light at night.")
H('9.B', 2, "Which sky object is white and fluffy?", "a cloud", ["the Sun", "a star", "the Moon"], "Many clouds look white and fluffy.")
H('9.B', 3, "A student draws the sky at night. Which picture shows a night sky?", "the Moon and stars", ["the Sun and a rainbow", "a bright blue sky with the Sun", "only a rainbow"], "Moon and stars are seen at night.")
H('9.B', 4, "Which sky object is closest to Earth?", "the Moon", ["the Sun", "a star", "a faraway star"], "The Moon is the closest object of these to Earth.")

# ---- 10.A rocks (size, shape, color, texture)
H('10.A', 2, "Which rock is the BIGGEST?", "a boulder as big as a car", ["a pebble you can hold", "a grain of sand", "a small stone"], "A boulder is the biggest of these rocks. A grain of sand is the smallest.")
H('10.A', 2, "Which word describes the SHAPE of a rock that looks like a ball?", "round", ["flat", "square", "long and thin"], "A ball shape is round. It has no flat sides or corners.")
H('10.A', 3, "Two rocks are the same size and shape. One is red and one is gray. What is different?", "color", ["size", "shape", "weight"], "The rocks match in size and shape. Only the color is different.")
H('10.A', 2, "Which rock feels SMOOTH when you touch it?", "a river stone worn down by water", ["a rock with many sharp points", "a rough rock with many bumps", "a broken rock with jagged edges"], "Water wears rocks smooth over time. Sharp, bumpy, and jagged rocks feel rough.")
H('10.A', 3, "A student sorts rocks into a SMOOTH group and a ROUGH group. Which rock goes in the SMOOTH group?", "a rock with a shiny, polished surface", ["a rock with pits and bumps", "a rock with sharp broken edges", "a rock covered in tiny grains"], "A shiny, polished rock feels smooth. The other three feel rough.")
H('10.A', 2, "Which rock has a FLAT shape, like a pancake?", "a flat slab", ["a round ball", "a long stick", "a pointed cone"], "A slab is flat. A ball is round, and a cone and a stick are not flat.")
H('10.A', 3, "Which list puts rocks in order from SMALLEST to BIGGEST?", "a grain of sand, a pebble, a boulder", ["a boulder, a pebble, a grain of sand", "a pebble, a boulder, a grain of sand", "a boulder, a grain of sand, a pebble"], "A grain of sand is the smallest, then a pebble, then a boulder.")

# ---- 10.B weather changes day to day and by season
H('10.B', 1, "Which is a kind of weather?", "rainy", ["round", "soft", "loud"], "Rainy tells what the weather is like.")
H('10.B', 2, "Which season is usually the coldest?", "winter", ["summer", "spring", "all seasons are the same"], "Winter is usually the coldest season.")
H('10.B', 2, "Which season usually has the hottest days?", "summer", ["winter", "fall", "spring"], "Summer usually has the hottest days.")
H('10.B', 3, "Monday was sunny. Tuesday was rainy. What does this show?", "weather can change from day to day", ["weather never changes", "it only rains on Tuesday", "it is always sunny on Monday"], "Weather can be different from one day to the next.")
H('10.B', 3, "Leaves change color and drop off many trees, and the days get cooler. Which season is it?", "fall", ["summer", "spring", "winter"], "Falling leaves and cooler days are signs of fall.")
H('10.B', 2, "What should you wear outside on a very cold, snowy day?", "a warm coat", ["shorts", "a swimsuit", "sandals"], "A warm coat keeps you warm in cold weather.")
H('10.B', 3, "A thermometer shows how hot or cold the air is. What does it tell about?", "temperature", ["wind direction", "the Moon", "rock color"], "A thermometer measures temperature.")

# ---- 10.C air is all around us; wind is moving air
H('10.C', 2, "What is wind?", "moving air", ["moving water", "moving light", "moving rock"], "Wind is air that is moving.")
H('10.C', 2, "A pinwheel spins when you blow on it. What makes it spin?", "moving air", ["water", "light", "sound only"], "Moving air pushes the pinwheel.")
H('10.C', 3, "A balloon gets bigger when you blow into it. What is inside?", "air", ["rocks", "light", "nothing"], "Air fills the balloon and makes it bigger.")
H('10.C', 3, "Which shows that wind is blowing?", "a flag waves", ["a rock sits still", "a book lies on a desk", "a pencil is on the floor"], "A waving flag shows moving air.")
H('10.C', 2, "Where is air found?", "all around us", ["only in clouds", "only inside balloons", "only on mountains"], "Air is all around us even though we cannot see it.")
H('10.C', 3, "Which tool shows which way the wind blows?", "a windsock", ["a ruler", "a magnet", "a scale"], "A windsock points the way the wind is blowing.")
H('10.C', 4, "A kite flies high on a day with strong wind. Why?", "moving air pushes it up", ["the Sun pulls it", "rocks hold it up", "the kite makes its own light"], "Moving air pushes against the kite and lifts it.")

# ---- 11 practical uses of rocks, soil, water
H('11', 2, "What do plants need from soil?", "nutrients and a place to grow", ["sound", "electricity", "magnets"], "Plants get nutrients and a place to grow from soil.")
H('11', 2, "Which is a way people use water?", "drinking", ["flying", "singing", "sleeping on it"], "People drink water to stay healthy.")
H('11', 3, "How can people use rocks?", "to build walls and roads", ["to make rain", "to make wind", "to make shadows"], "People use rocks to build walls, roads, and houses.")
H('11', 3, "Which use of water is for staying clean?", "washing hands", ["flying a kite", "kicking a ball", "sorting socks"], "Washing hands uses water to get clean.")
H('11', 2, "A farmer grows food in the ground. What material is used?", "soil", ["a magnet", "a mirror", "a flag"], "Farmers grow food in soil.")
H('11', 3, "Which job needs water?", "growing a garden", ["lighting a lamp", "painting with sand only", "sorting rocks by color"], "A garden needs water to grow.")
H('11', 4, "Which is a way to use sand and rocks?", "to make a path", ["to make a sound", "to make a cloud", "to make a shadow"], "People use sand and rocks to make paths and roads.")

# ---- 12.A plants depend on air, sunlight, water, nutrients, space
H('12.A', 1, "What do plants need to grow?", "water and sunlight", ["candy and juice", "toys and games", "a blanket"], "Plants need water, sunlight, air, nutrients, and space.")
H('12.A', 2, "A plant sits in a dark closet and is never watered. What will happen?", "it will not grow well", ["it will grow very fast", "it will turn into an animal", "it will grow bigger flowers"], "Plants need light and water to grow well.")
H('12.A', 3, "Where do plants get nutrients?", "from soil", ["from magnets", "from shadows", "from the Moon"], "Plant roots take in nutrients from the soil.")
H('12.A', 3, "Why do many plants grow toward a window?", "they need sunlight", ["they need sound", "they need cold", "they need sand"], "Plants grow toward light because they need sunlight.")
H('12.A', 2, "Seeds are planted too close together. What might the plants be missing?", "space to grow", ["a magnet", "a light bulb only", "a rock"], "Plants need space to grow.")
H('12.A', 3, "Which is NOT needed for a plant to live?", "toys", ["air", "water", "sunlight"], "Plants need air, water, and sunlight, but not toys.")
H('12.A', 4, "A student gives one plant water and sun and another plant only sun. Which plant will grow better?", "the plant with water and sun", ["the plant with only sun", "they will grow the same", "neither will grow"], "Plants need both water and sunlight.")

# ---- 12.B animals depend on air, water, food, space, shelter
H('12.B', 1, "What do animals need to live?", "air, water, and food", ["toys and candy", "TV and games", "books only"], "Animals need air, water, food, space, and shelter.")
H('12.B', 2, "A bird builds a nest. What does the nest give the bird?", "shelter", ["food", "water", "air"], "A nest is a shelter for the bird.")
H('12.B', 2, "A fish lives in water. What does water give the fish?", "a place to live and the air it needs", ["a place to nap on a bed", "sunlight only", "a tree"], "Fish live in water and take in air from it.")
H('12.B', 3, "A rabbit eats grass. What does grass give the rabbit?", "food", ["shelter only", "a magnet", "a shadow"], "The rabbit gets food from grass.")
H('12.B', 3, "A dog needs room to run and play. What is this need called?", "space", ["a toy", "a color", "a shadow"], "Animals need space to move and live.")
H('12.B', 2, "A squirrel hides in a hole in a tree during a storm. What does the hole give the squirrel?", "shelter", ["food", "light", "a map"], "A hole in a tree is a shelter.")
H('12.B', 4, "A pet has food, shelter, and space but no water. What will happen?", "it will not stay healthy", ["it will be fine for a year", "it will grow wings", "it will turn into a plant"], "Animals need water to live.")

# ---- 13.A plant structures
H('13.A', 1, "Which part of a plant grows under the ground?", "roots", ["flower", "leaf", "fruit"], "Roots grow under the ground.")
H('13.A', 2, "Which plant part holds the plant up?", "stem", ["root hair", "seed coat", "petal"], "The stem holds up the plant.")
H('13.A', 2, "Which plant part makes food using sunlight?", "leaf", ["root", "stem", "seed"], "Leaves use sunlight to make food for the plant.")
H('13.A', 2, "Which plant part is often colorful and smells nice?", "flower", ["root", "stem", "leaf"], "Flowers are often colorful and smell nice.")
H('13.A', 3, "Which plant part takes in water from the soil?", "roots", ["flowers", "leaves", "fruits"], "Roots take in water from the soil.")
H('13.A', 3, "An apple is the part of an apple tree that holds the seeds. What is it called?", "fruit", ["root", "stem", "leaf"], "A fruit holds the seeds.")
H('13.A', 3, "Which list names only plant parts?", "root, stem, leaf", ["beak, wing, tail", "paw, tail, fur", "fin, gill, scale"], "Roots, stems, and leaves are parts of a plant.")

# ---- 13.B animal structures for interacting with environment
H('13.B', 2, "Which body part helps a person see?", "eyes", ["ears", "hands", "feet"], "Eyes are used for seeing.")
H('13.B', 2, "Which body part helps an animal hear?", "ears", ["nose", "tail", "paws"], "Ears are used for hearing.")
H('13.B', 2, "A bird uses its wings to do what?", "fly", ["swim like a fish", "dig in soil", "climb walls"], "Wings help birds fly.")
H('13.B', 3, "A monkey uses its hands and tail to do what?", "grasp branches", ["swim underwater", "fly", "dig tunnels"], "Monkeys grasp branches with hands and tail.")
H('13.B', 3, "A fish uses its fins to do what?", "move in water", ["fly in the sky", "run on land", "climb trees"], "Fins help fish move in water.")
H('13.B', 3, "A dog sniffs the air. Which body part is it using?", "nose", ["eyes", "paws", "tail"], "A dog smells with its nose.")
H('13.B', 4, "Which animal body part helps it grab food?", "a bird's claws", ["a fish's tail", "a rabbit's ears", "a deer's eyes"], "A bird uses its claws to grab food.")

# ---- 13.C simple plant life cycle
H('13.C', 2, "What comes first in a plant life cycle?", "seed", ["fruit", "flower", "plant"], "A plant life cycle starts with a seed.")
H('13.C', 2, "A seed begins to grow and a tiny plant comes out. What is it called?", "seedling", ["fruit", "root", "flower"], "A tiny new plant is a seedling.")
H('13.C', 3, "Which shows the plant life cycle in order?", "seed, seedling, plant, flower, fruit", ["fruit, seed, flower, plant", "flower, seed, fruit, plant", "plant, seed, fruit, seedling"], "A plant grows from seed to seedling to plant, then makes flowers and fruit.")
H('13.C', 3, "What do flowers on a plant often turn into?", "fruit", ["roots", "rocks", "soil"], "Flowers can become fruit with seeds inside.")
H('13.C', 3, "A seedling grows bigger. What does it become?", "a plant", ["a seed", "a rock", "an animal"], "A seedling grows into a plant.")
H('13.C', 3, "What is inside many fruits?", "seeds", ["rocks", "shadows", "magnets"], "Many fruits have seeds inside.")
H('13.C', 4, "A student draws four pictures of a bean plant. Which picture should come SECOND?", "a small seedling", ["a plant with fruit", "a seed in a packet", "a big flower"], "The seed comes first, then the seedling.")

# ---- 13.D young plants resemble parent plant
H('13.D', 2, "A seed is taken from a parent plant and planted. What will the seed grow into?", "a young plant that looks like the parent", ["a rock", "an animal", "a plant of a very different kind"], "Seeds grow into the same kind of plant as the parent.")
H('13.D', 2, "A bean seed is planted. What will grow?", "a bean plant", ["a corn plant", "an apple tree", "a daisy"], "A bean seed grows into a bean plant.")
H('13.D', 3, "A young oak tree looks most like which plant?", "a grown oak tree", ["a rosebush", "a corn plant", "a cactus"], "Young plants look like their parent plants.")
H('13.D', 3, "A seedling has leaves that look like its parent's leaves. What does this show?", "young plants look like their parents", ["all plants look the same", "seedlings are rocks", "young plants have no leaves"], "Young plants resemble their parent plants.")
H('13.D', 3, "Which seed would grow into a plant with many yellow petals like its parent?", "a seed from a sunflower", ["a seed from a pumpkin", "a seed from a bean", "a seed from a pine tree"], "A sunflower seed grows into a sunflower.")
H('13.D', 2, "A tomato seed is planted. What will grow?", "a tomato plant", ["a lemon tree", "a cactus", "a grass plant"], "Seeds grow into the same kind of plant.")
H('13.D', 4, "A grown pine tree makes seeds. What will a pine seed grow into?", "a pine tree", ["an oak tree", "a flower", "a bush"], "A pine seed grows into a pine tree.")

B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'gk_science.jsonl'))
print("saved", len(B.out), "questions")

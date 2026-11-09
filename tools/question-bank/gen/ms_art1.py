import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.202.', 1040, own='ms_art1.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',2,"A sixth grader draws the folds of a real sweater she is holding in front of her. Her idea comes from ___.",
  "Direct observation",["A dream she forgot","A rule in a textbook","A photocopied worksheet"],"Looking at a real object is direct observation.")
H('c.1.A',2,"Which choice is an original source for a drawing idea?",
  "A sketch you make of a real plant in the garden",["A cartoon someone else drew","A copied logo","A coloring page"],"Original sources come from first-hand experience.")
H('c.1.B',2,"Which element of art describes how a surface feels or looks like it feels, such as rough or smooth?",
  "Texture",["Line","Value","Space"],"Texture is surface quality.")
H('c.1.B',2,"A student mixes white into blue paint to make it lighter. She is changing the ___ of the color.",
  "Value",["Shape","Form","Line"],"Value is how light or dark a color is.")
H('c.1.C',2,"A wallpaper design repeats the same flower again and again. This shows the principle of ___.",
  "Repetition or pattern",["Contrast","Scale","Balance only"],"Repeating an element makes a pattern.")
H('c.1.C',2,"An artist makes one bright red shape stand out in a gray painting. She uses ___ to draw the eye.",
  "Emphasis",["Unity","Rhythm","Proportion"],"Emphasis highlights the focal point.")
H('c.1.D',3,"A painting of a boat on a storm-tossed sea makes viewers feel worried. This is the work's ___ property.",
  "Expressive",["Mathematical","Chemical","Legal"],"Expressive properties convey feeling and meaning.")
H('c.1.D',3,"When artists borrow imagery from existing work and give it a new meaning, they use ___.",
  "Appropriation",["Erasing","Tracing only","Rubbing"],"Appropriation reuses imagery.")
H('c.2.A',3,"A student plans a drawing from an idea of her own about her family tradition. She is creating an artwork from ___.",
  "Personal experience",["Another artist's finished piece","A store ad","A worksheet answer"],"Original work can come from personal experience.")
H('c.2.A',3,"Which choice best describes an original artwork?",
  "It shows the artist's own ideas and choices",["It is a copy of a poster","It is a tracing of a photo","It is a printout"],"Originality means the artist's own vision.")
H('c.2.B',3,"A student sketches three different ideas for a poster, picks the best one and then improves it. She is using the ___ process.",
  "Art-making",["Memorizing","Guessing","Skipping"],"The art-making process includes planning and revising.")
H('c.2.B',3,"Solving a design problem like 'make a bag that is easy to carry' means applying ___.",
  "Creative thinking and planning",["Random luck","Copying a bag","Ignoring the need"],"Design solves problems.")
H('c.2.C',2,"Which of these is a printmaking technique?",
  "Carving a block, rolling ink and pressing it on paper",["Stirring watercolor","Molding clay","Sewing cloth"],"Relief printing uses a carved block.")
H('c.2.C',2,"A student shapes clay into a bowl, lets it dry and fires it in a kiln. She is making ___.",
  "Ceramics",["Printmaking","Watercolor","Photography"],"Clay fired in a kiln is ceramics.")
H('c.3.A',3,"A mural showing a city rebuilding after a flood reflects an influence of ___ on art.",
  "Historical events",["Weather forecasts","Lunch menus","Bus routes"],"Events shape what artists make.")
H('c.3.A',3,"An artwork protesting a law shows the influence of ___ events.",
  "Political",["Cooking","Sports scores","Fashion trends only"],"Art can respond to politics.")
H('c.3.B',3,"A painting that shows hope using a rising sun conveys a(n) ___ theme.",
  "Universal",["Private","Secret","Local only"],"Universal themes cross cultures.")
H('c.3.B',3,"Which of these is a universal theme found in art around the world?",
  "Family and community",["Parking rules","Tax forms","Bus numbers"],"Family appears across cultures.")
H('c.3.C',3,"Why do cathedrals, temples and mosques look different around the world?",
  "Societies' beliefs and resources shape their art and architecture",["They are all identical","Builders ignore culture","Weather decides everything"],"Culture shapes architecture.")
H('c.3.C',3,"A society that valued trade built large market halls with decorated walls. This explains the relationship between ___ and art.",
  "Society and architecture",["Math and sound","Food and sports","Money and sleep"],"Buildings reflect values.")
H('c.3.D',2,"Which job might an art student have as a career?",
  "Museum curator",["Pilot","Surveyor","Plumber"],"Curators care for museum collections.")
H('c.3.D',2,"An avocational art activity is ___.",
  "Painting for enjoyment on weekends",["A full-time job","A school test","A tax form"],"Avocational means pursued for love of it.")
H('c.4.A',2,"A student writes a response to a painting using words like 'texture' and 'balance.' She is using appropriate ___.",
  "Art vocabulary",["Slang only","Silence","Math symbols"],"Using art words makes responses precise.")
H('c.4.A',2,"Which sentence uses art vocabulary?",
  "The artist used diagonal lines to create movement",["It was nice","I like it","It looks cool"],"Specific terms add clarity.")
H('c.4.B',3,"A critique method often starts with ___ the artwork, then analyzing, interpreting and judging.",
  "Describing",["Ignoring","Selling","Copying"],"Describe, analyze, interpret, judge.")
H('c.4.B',3,"In a critique, 'interpreting' an artwork means ___.",
  "Explaining what you think it means",["Listing only the colors","Copying it","Selling it"],"Interpretation gives meaning.")
H('c.4.C',2,"A portfolio is a collection of ___.",
  "An artist's selected work over time",["Receipts","Tickets","Snack wrappers"],"Portfolios showcase artwork.")
H('c.4.C',2,"Which belongs in a student art portfolio?",
  "Finished pieces with sketches that show growth",["Random papers","Homework from other classes only","Blank sheets"],"A portfolio shows progress.")
H('c.4.D',2,"A field trip to a gallery lets a student see original artworks ___.",
  "In person, outside the classroom",["Only online","Only in a book","Only on a worksheet"],"Venues outside class expand learning.")
H('c.4.D',2,"Which place is a venue to see original art outside school?",
  "Art museum",["Gas station","Parking lot","Bus stop"],"Museums display art.")
H('c.4.E',2,"At a gallery opening, good exhibition etiquette is to ___.",
  "Keep hands off the artwork and speak quietly",["Touch the sculptures","Run through the room","Take items from the wall"],"Respect the art and others.")
H('c.4.E',2,"When displaying your own artwork at school, you should ___.",
  "Label it and present it neatly",["Hide it","Crumple it","Leave it unnamed"],"Neat display shows respect.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'ms_art1.jsonl'))

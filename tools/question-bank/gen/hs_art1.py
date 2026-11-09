import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.302.', 1015, own='hs_art1.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',2,"A student sketches a pair of old boots on a table while looking right at them. Which source of ideas is this?",
  "Direct observation",["Imagination only","A copied poster","A random guess"],"Drawing from life uses direct observation.")
H('c.1.A',3,"An artist builds a painting from memories of her grandmother's kitchen. Which source of ideas is she using?",
  "Experiences and imagination",["Only direct observation","A copied photograph","A required template"],"Memories and imagination are personal sources.")
H('c.1.B',2,"Which of these is an element of art?",
  "Line",["Balance","Emphasis","Unity"],"Line is an element; the others are principles.")
H('c.1.B',3,"A painter mixes blue with yellow to make green. Which element of art is she working with?",
  "Color",["Texture","Form","Space"],"Mixing hues is working with color.")
H('c.1.C',2,"Which of these is a principle of design?",
  "Balance",["Line","Texture","Shape"],"Balance is a principle; the others are elements.")
H('c.1.C',3,"A quilt repeats the same star shape in rows across the whole surface. Which principle of design is this?",
  "Repetition and pattern",["Contrast only","Emphasis only","Proportion only"],"Repeating a motif creates pattern.")
H('c.1.D',3,"A viewer reads a painting of a stormy sea as a symbol of struggle. She is making a judgment about the artwork's what?",
  "Expressive properties such as meaning and metaphor",["Paper weight","Frame price","Brush brand"],"Meaning and metaphor are expressive properties.")
H('c.1.D',3,"Two students disagree about the message of a sculpture. What is the best way to support a judgment about its meaning?",
  "Point to details such as subject, color and form as evidence",["Say it is just their opinion","Ignore the artwork","Count the pages in the book"],"Judgments rest on visible evidence.")
H('c.2.A',3,"A student must design a poster that clearly shows a recycling message. She tries three thumbnail sketches and picks the clearest. What is she doing?",
  "Solving a visual problem through trial and refinement",["Copying another poster","Skipping planning","Guessing"],"Problem solving explores several options.")
H('c.2.A',3,"Drawing a still life using real fruit and a vase relies on which problem-solving approach?",
  "Direct observation",["Pure imagination","Tracing","Random marks"],"Observation solves proportion and shading.")
H('c.2.B',3,"A graphic designer, an architect and a potter each solve problems with design. This shows that design solutions are used in what?",
  "A variety of applications and careers",["Only paintings","Only museums","Only schools"],"Design applies broadly.")
H('c.2.B',3,"A designer plans a chair that is both comfortable and attractive. This is an example of balancing what?",
  "Function and visual appearance",["Cost and weather","Noise and color","Time and distance"],"Design solutions meet needs and look good.")
H('c.2.C',3,"An artist wants to use a photograph from the internet in her collage. What should she understand about copyright?",
  "Copyrighted images generally need permission or must be transformed within the law",["All internet images are free","Copyright does not apply to students","Only paintings are protected"],"Copyright protects creators' work.")
H('c.2.C',3,"Which type of work can an artist use freely because its copyright has expired?",
  "A work in the public domain",["A new copyrighted photo","A licensed logo","A current album cover"],"Public domain works are free to use.")
H('c.2.D',3,"A student paints a bright, swirling sky to show how excited she felt at a concert. She is using art to do what?",
  "Communicate thoughts, feelings or impressions",["Record a map","Follow a recipe","Measure time"],"Original artwork can express feelings.")
H('c.2.D',3,"What makes an artwork original?",
  "It comes from the artist's own ideas rather than copying another work",["It is traced from a photo","It is copied from a poster","It uses no color"],"Originality means personal ideas.")
H('c.2.E',3,"A class paints a large mural, with each student designing one section that fits the theme. This is an example of what?",
  "Collaboration to create a work of art",["Working alone","Copying","Tracing"],"Many hands share the project.")
H('c.2.E',3,"What is an important skill when collaborating on an artwork?",
  "Listening to others' ideas and agreeing on a plan",["Ignoring teammates","Working in secret","Changing others' work without asking"],"Collaboration needs communication.")
H('c.2.F',2,"Which tool is best for creating a printmaking plate?",
  "A linoleum cutter and a block",["A paint roller only","A glue stick only","A pencil only"],"Cutters carve plates for printing.")
H('c.2.F',3,"A sculptor adds clay to a form and then smooths it. Which process is she using?",
  "Modeling",["Printmaking","Photography","Weaving"],"Adding and shaping clay is modeling.")
H('c.3.A',3,"A student compares a Renaissance portrait with a modern digital portrait. Which question helps compare them?",
  "How do the styles, materials and themes differ?",["Which is heavier?","Which is older by weight?","Which has a longer title?"],"Comparing looks at style, materials and themes.")
H('c.3.A',3,"A recurring theme in both ancient and modern art is what?",
  "The human figure and nature",["Only abstract lines","Only computers","Only advertising"],"Common themes appear across time.")
H('c.3.B',3,"Navajo weaving, Japanese woodblock prints and West African masks are examples of artwork from different what?",
  "Cultures",["Seasons","Sports","Grades"],"Art reflects cultural traditions.")
H('c.3.B',3,"Artworks from different cultures often reflect what about their makers?",
  "Beliefs, values and environment",["Only prices","Only birthdays","Only weather forecasts"],"Art reflects the culture.")
H('c.3.C',3,"A group creates a community mural on a library wall. This is a community-based art project because it does what?",
  "Connects artwork to the people and place it serves",["Is kept private","Is sold for profit only","Is hidden in a closet"],"Community art serves the public.")
H('c.3.C',3,"Which is a benefit of a community-based art project?",
  "It brings people together and beautifies a shared space",["It prevents all art","It isolates people","It removes public places"],"Community art builds connection.")
H('c.3.D',3,"A person who paints on weekends but works in a bank is pursuing art as what?",
  "An avocation",["A full-time career","A required class","A prize"],"An avocation is a hobby alongside a career.")
H('c.3.D',3,"Which is a career in art?",
  "Graphic designer",["Mail sorter","Farmhand only","Cashier only"],"Graphic design is an art career.")
H('c.4.A',3,"A student explains why she used dark blue in her self-portrait. She is doing what?",
  "Justifying an artistic decision",["Avoiding feedback","Hiding her work","Ignoring the process"],"Justifying choices explains the artwork.")
H('c.4.A',3,"Which statement is a helpful peer evaluation?",
  "The overlapping shapes create depth, but the background feels flat",["It is bad","I don't like it","Whatever"],"Specific, balanced feedback is useful.")
H('c.4.B',3,"A four-step critique uses description, analysis, interpretation and what?",
  "Evaluation",["Subtraction","Guessing","Hiding"],"The final step is evaluation.")
H('c.4.B',3,"During the description step of a critique, a student should do what?",
  "Name what she sees without judging",["Say whether it is good","Guess the price","Compare it to a friend's work"],"Description states observable facts.")
H('c.4.C',3,"A student chooses her best five pieces for a portfolio and writes a note about why each was selected. What is she doing?",
  "Evaluating and analyzing her own work to construct a portfolio",["Throwing work away","Copying others","Skipping reflection"],"Portfolios show selected work and reflection.")
H('c.4.C',3,"A digital portfolio is useful because it does what?",
  "Lets an artist share work online and show growth over time",["Hides her art","Prevents critique","Removes the need for art"],"Electronic portfolios are easy to share.")
H('c.4.D',3,"A student visits a gallery exhibition and writes a conclusion about how the artist uses color to create mood. She is doing what?",
  "Analyzing artwork to form precise conclusions",["Ignoring the exhibition","Counting frames","Guessing"],"Analysis supports conclusions with evidence.")
H('c.4.D',3,"Which evidence best supports a conclusion about an artist's style?",
  "Repeated use of similar colors, shapes and techniques across several works",["The size of the signature only","The weather at the exhibit","A friend's opinion only"],"Patterns across works support a conclusion.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_art1.jsonl'))

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.303.', 1016, own='hs_art2.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',3,"A student draws a seashell next to a photo of the same shell and notes how the spiral differs. This is an example of what?",
  "Using visual comparison to illustrate an idea",["Ignoring the subject","Copying a classmate","Choosing paint at random"],"Comparing two visual sources clarifies ideas.")
H('c.1.A',3,"Placing a sketch of a crumpled paper bag beside a smooth ceramic bowl helps show which concept?",
  "Contrast in texture",["Perfect symmetry","The rule of thirds","Linear perspective"],"Side by side comparisons reveal contrast.")
H('c.1.B',3,"A designer uses thick and thin diagonal strokes to suggest movement across a page. Which element of art is most active?",
  "Line",["Value only","Space only","Form only"],"Varied lines create movement.")
H('c.1.B',3,"Adding gradual shading to a flat circle makes it look like a sphere. Which elements of art are being applied?",
  "Value and form",["Pattern and rhythm","Balance and unity","Emphasis and contrast"],"Shading builds three-dimensional form.")
H('c.1.C',3,"A poster has one large, bright red shape on a field of small gray shapes so the eye goes there first. Which principle is applied?",
  "Emphasis",["Repetition","Rhythm only","Proportion only"],"A dominant element creates emphasis.")
H('c.1.C',3,"A painter arranges two equal trees on each side of a road so the picture feels stable. Which principle is used?",
  "Balance, specifically symmetry",["Movement","Variety","Contrast of color only"],"Matching sides create symmetrical balance.")
H('c.1.D',3,"Watercolor is often chosen for soft, flowing skies. This shows that artists consider what?",
  "How well a medium suits the idea being expressed",["The cheapest tool always","The brush color","The studio floor"],"Media should match the expressive goal.")
H('c.1.D',3,"A sculptor wants to express strength and permanence. Which medium might be most suitable?",
  "Carved stone",["Tissue paper","Soap bubbles","Thin thread"],"Stone suggests durability.")
H('c.2.A',3,"For a still life, a student draws the arrangement three ways: from above, from the side and up close. What is she doing?",
  "Creating multiple solutions from direct observation",["Copying a poster","Skipping planning","Using only one idea"],"Several views provide multiple solutions.")
H('c.2.A',3,"Why is it helpful to develop more than one solution for an art problem?",
  "It lets the artist choose the strongest idea",["It wastes supplies","It avoids decisions","It ends the project"],"Exploring options improves results.")
H('c.2.B',3,"A student designs a clear symbol for a school recycling bin so everyone understands it. This is a practical application of what?",
  "Design skills",["Photography","Weaving","Pottery wheel use"],"Design makes ideas clear and practical.")
H('c.2.B',3,"Which task is an example of applying design to clarify a presentation?",
  "Choosing a readable font and clear layout for a slide",["Adding random clip art","Using tiny crowded text","Using a very bright background with pale text"],"Good layout improves clarity.")
H('c.2.C',3,"A student remixes a famous painting into a new composition, changing the subject and style. What should she consider about the source?",
  "Whether the source is protected by copyright or in the public domain",["Only whether it is popular","Whether it is large","Whether it is old by weight"],"Appropriation depends on legal status.")
H('c.2.C',3,"Which of these best describes fair, ethical use of a source image?",
  "Transforming it so the new work is original and giving credit",["Copying it exactly and signing it","Selling it unchanged","Claiming it as your own"],"Transformation and credit are ethical practices.")
H('c.2.D',3,"An artist makes a collage of torn blue paper to show loneliness. This is an example of what?",
  "Communicating a feeling through original artwork",["Following a tutorial exactly","Copying a logo","Tracing a map"],"Original art expresses personal ideas.")
H('c.2.D',3,"Which piece best communicates an impression of a busy city?",
  "A layered painting of overlapping buildings and bright lights",["A blank sheet","A single dot","A random smudge only"],"Layered, active images suggest a busy place.")
H('c.2.E',3,"Two students plan a diptych in which each paints one panel that answers the other. What skill is most needed?",
  "Collaboration and agreement on shared ideas",["Working in secret","Painting over each other","Ignoring the theme"],"Collaboration needs shared planning.")
H('c.2.E',3,"When a team creates a sculpture, who decides on the design?",
  "The team, through discussion and compromise",["No one","Only the loudest member","The teacher alone with no input"],"Collaborative design is a group decision.")
H('c.2.F',3,"Which medium is best for a student who wants to print multiple copies of an image?",
  "Linocut or another printmaking process",["Watercolor wash","Single clay pinch pot","Pencil sketch"],"Printmaking produces editions.")
H('c.2.F',3,"A student chooses charcoal to create deep, dramatic shadows. This shows what?",
  "Selecting a medium to communicate a specific idea",["Random choice","Avoiding planning","Following no rules"],"Medium choice supports the idea.")
H('c.3.A',3,"A student studies Impressionism and notes that artists painted outdoors to capture changing light. This is an example of what?",
  "Identifying a theme and trend in a historical style",["Memorizing prices","Copying one painting","Studying unrelated music"],"Styles share themes and trends.")
H('c.3.A',3,"Comparing Baroque and Modernist art, a student looks for differences in what?",
  "Subject matter, technique and the ideas they express",["Frame colors only","Museum hours","Painter's height"],"Comparison focuses on style and meaning.")
H('c.3.B',3,"A student studies how Maori carving uses spirals and patterns to tell family stories. She is analyzing what?",
  "Specific characteristics of artwork from a culture",["A random doodle","A modern advertisement","A weather map"],"Cultural analysis looks at symbols and techniques.")
H('c.3.B',3,"Which feature might you analyze when comparing art from different cultures?",
  "Materials, symbols and purpose of the work",["The price of the frame","The size of the signature","The distance from home"],"Materials and symbols reflect culture.")
H('c.3.C',3,"A class works with a city to paint a mural at a bus stop. What do they need to consider?",
  "The community's needs, safety and permission",["Only personal taste","Ignoring the neighbors","Painting over other work"],"Community art needs buy-in.")
H('c.3.C',3,"Community-based art can help a neighborhood by doing what?",
  "Expressing shared identity and improving public space",["Removing all art","Raising noise levels","Hiding local history"],"Public art builds identity.")
H('c.3.D',3,"A student researches how an illustrator starts a freelance business. This is an example of exploring what?",
  "Entrepreneurial opportunities in art",["Only hobbies","School sports","Medical careers"],"Freelancing is an entrepreneurial path.")
H('c.3.D',3,"Which job requires strong art and design skills?",
  "Animator",["Electrician only","Accountant only","Truck dispatcher only"],"Animation is an art career.")
H('c.4.A',3,"During a class discussion, a student justifies her choice of a cool palette by saying it creates a calm mood. She is doing what?",
  "Interpreting and justifying artistic decisions",["Avoiding the question","Insulting a peer","Skipping reflection"],"Justification links choices to intent.")
H('c.4.A',3,"Which kind of feedback best helps an artist improve?",
  "Specific comments tied to what is visible in the work",["Vague praise","Silent looks","Personal attacks"],"Specific feedback guides revision.")
H('c.4.B',3,"In a critique, a student explains how the artist arranged shapes and then says what the work might mean. Which steps is she using?",
  "Analysis and interpretation",["Only measuring","Only describing","Only judging"],"These are middle steps in a critique.")
H('c.4.B',3,"Which question belongs in the evaluation step of a critique?",
  "How successful is the work in communicating its idea?",["What colors do I see?","Who owns it?","How big is the canvas?"],"Evaluation judges effectiveness.")
H('c.4.C',3,"After a critique says her composition feels crowded, a student simplifies the background. She is doing what?",
  "Using responses to critique to make decisions about her work",["Ignoring feedback","Quitting the project","Copying another student"],"Critique guides revisions.")
H('c.4.C',3,"Why is it useful to keep notes from critiques?",
  "They help plan future directions for personal work",["They replace artwork","They prevent revision","They lower grades"],"Notes track growth.")
H('c.4.D',3,"A portfolio shows sketches, final pieces and a short reflection on each. This helps a viewer see what?",
  "The artist's growth and thinking over time",["Only finished work","Only prices","Only the artist's name"],"Portfolios show process and progress.")
H('c.4.D',3,"A student photographs her sculptures to make an electronic portfolio. What is one advantage?",
  "It makes the work easy to share and update",["It deletes the originals","It prevents feedback","It lowers quality always"],"Digital portfolios are shareable.")
H('c.4.E',3,"A student visits an exhibit and writes about how the curator groups the works. She is analyzing what?",
  "How an exhibition communicates ideas",["Parking rules","Ticket prices","The gift shop"],"Exhibition analysis considers arrangement and theme.")
H('c.4.E',3,"Which is the best basis for a precise conclusion about an artist's body of work?",
  "Details from several works, such as subjects, techniques and themes",["One quick glance","A friend's guess","The title alone"],"Evidence from multiple works supports conclusions.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_art2.jsonl'))

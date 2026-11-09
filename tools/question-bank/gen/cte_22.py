import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('127.', 1099, own='cte_22.jsonl')
def H(code, d, q, right, wrong, e):
    return B.hand(code, d, q, right, wrong, e)

# ---------- 127.149 Masonry I ----------
H('149.d.1.A',3,"A mason spreads a mortar bed on a footing before laying the first course. The usual bed joint thickness is about:",
  "3/8 inch",["2 inches","1 inch","1/16 inch"],"Standard mortar joints are 3/8 inch.")
H('149.d.1.A',4,"A mortar bed is spread with a trowel so that it is full and:",
  "Even along the length of the bed",["Thin in the middle","Wet and runny","Lumpy at the ends"],"A uniform bed keeps units level.")
H('149.d.1.B',3,"When spreading mortar for a course at chest height, the mason should keep the mortar:",
  "Within reach so it does not dry out before units are set",["Far from the wall","Spread for the whole day","On the scaffold edge"],"Spread only a few units ahead.")
H('149.d.1.B',4,"On a high lift, the mason spreads only a few feet of bed at a time mainly so the mortar:",
  "Stays plastic and bonds",["Turns black","Freezes","Dries solid"],"Mortar that stiffens bonds poorly.")
H('149.d.1.C',3,"Spreading mortar for concrete block is different from brick because block is wider and often has:",
  "Face shell mortar bedding",["No mortar at all","Mortar on the inside only","Mortar on the top only"],"CMU is bedded on the face shells.")
H('149.d.1.C',4,"A mason lays 8-inch CMU on face-shell bedding. Mortar is applied to the:",
  "Two long face shells",["Center web only","Entire inside cell","Back of the unit only"],"Face shells carry the mortar.")
H('149.d.1.D',3,"The size of a trowel chosen for spreading mortar on large block is usually:",
  "Larger than for brick",["Smaller than for brick","The same always","A pointing tool"],"Bigger units need more mortar.")
H('149.d.1.D',4,"Spreading mortar on a 12-inch block compared with a modular brick requires:",
  "A longer, heavier bed spread",["No spreading","A thinner bed than brick","Only head joints"],"Block beds are longer.")
H('149.d.1.E',3,"Buttering a masonry unit means applying mortar to its:",
  "End or side before placing it",["Top face only","Inside cells","Back only"],"Buttering forms the head joint.")
H('149.d.1.E',4,"A brick laid as a header needs buttering on the end that will:",
  "Meet the next unit in the course",["Face the sky","Face the ground","Stay dry"],"The end forms the vertical joint.")
H('149.d.2.A',3,"A brick lead is built at the end of a wall to:",
  "Guide the line for the courses between leads",["Replace the footing","Hold the scaffolding","Mark the property"],"Leads set the line and heights.")
H('149.d.2.A',4,"While building a lead, the mason checks each course with a level for plumb, level, and:",
  "Alignment with the line",["Color match","Weight","Moisture only"],"Leads must be true.")
H('149.d.2.B',3,"To keep a brick wall straight between leads, the mason stretches a:",
  "Line",["Hose","Rope ladder","Fishing pole"],"A mason's line shows the face plane.")
H('149.d.2.B',4,"A level placed vertically on the wall face checks that the wall is:",
  "Plumb",["Dry","Cured","Colored"],"Plumb means vertical.")
H('149.d.2.C',3,"An outside corner of a brick wall is a corner that:",
  "Projects outward from the building",["Turns into the building","Is on the roof","Is under the ground"],"Outside corners stick out.")
H('149.d.2.C',4,"When building an outside corner, the mason checks the corner is plumb on:",
  "Both faces",["One face only","The top only","Neither"],"Both faces must be plumb.")
H('149.d.2.D',3,"An inside corner is formed where two walls meet and form a corner that:",
  "Turns in toward the building",["Sticks out","Is round","Is on the roof"],"Inside corners recess.")
H('149.d.2.D',4,"Which tool best checks that an inside corner is square?",
  "A framing square or corner check",["A rubber band","A paintbrush","A trowel edge only"],"Squares verify 90 degrees.")
H('149.d.2.E',3,"A double wythe brick wall has:",
  "Two layers of brick separated by a collar joint",["One layer only","Four layers","No mortar"],"Two wythes with a joint between them.")
H('149.d.2.E',4,"The space between two wythes is called the:",
  "Collar joint",["Cap joint","Footing","Head joint"],"Collar joints sit between wythes.")
H('149.d.3.A',3,"A stretcher is a brick laid with its:",
  "Long narrow face exposed in the wall",["Short end exposed","Flat face up","Bottom up"],"Stretchers show the long face.")
H('149.d.3.A',4,"In running bond, most of the bricks in the wall face are:",
  "Stretchers",["Soldiers","Sailors","Headers"],"Running bond uses stretchers.")
H('149.d.3.B',3,"A header brick is laid with its:",
  "Short end exposed on the wall face",["Long face exposed","Flat face up","Standing on end"],"Headers tie wythes together.")
H('149.d.3.B',4,"Header courses in a double wythe wall help:",
  "Tie the two wythes together",["Make the wall lighter","Save mortar","Add color only"],"Headers cross the collar joint.")
H('149.d.3.C',3,"A rowlock brick is laid on its:",
  "Edge with the short end showing",["Flat face","Long end","Back"],"Rowlocks are on edge.")
H('149.d.3.C',4,"A rowlock course is often found at a:",
  "Sill or the top of a wall",["Footing only","Floor drain","Door handle"],"Rowlocks shed water.")
H('149.d.3.D',3,"A sailor is a brick laid:",
  "Standing on end with the broad face showing",["Flat on its bed","On its long edge","In a pile"],"Sailors are on end, broad face out.")
H('149.d.3.D',4,"Which brick position stands on its end with the broad (bed) face out?",
  "Sailor",["Stretcher","Header","Rowlock"],"Sailors have broad faces showing.")
H('149.d.3.E',3,"A soldier is a brick laid:",
  "Standing on end with the narrow face showing",["Flat","On its long edge","Sideways in a pile"],"Soldiers stand on end.")
H('149.d.3.E',4,"A soldier course is often used above a door or window as a:",
  "Decorative lintel course",["Footing","Floor","Drain"],"Soldier courses cap openings.")
H('149.d.3.F',3,"A shiner is also called a:",
  "Rowlock stretcher",["Soldier","Sailor","Corbel"],"Another name for a shiner.")
H('149.d.3.F',4,"A shiner is laid with the brick resting on its:",
  "Long edge",["Short end","Flat bed","Top corner"],"Shiners lie on their edge.")
H('149.d.4.A',3,"A column labeled 2 by 2 in brick has how many bricks in each course?",
  "Four",["One","Eight","Twelve"],"A 2 by 2 column has four units per course.")
H('149.d.4.A',4,"The first thing a mason checks on a column is that each course is:",
  "Level and plumb",["Colored","Painted","Weighed"],"Check every course.")
H('149.d.4.B',3,"A six-brick column is built with how many bricks per course?",
  "Six",["Two","Ten","Sixteen"],"Count per course.")
H('149.d.4.B',4,"Alternating each course of a column so joints are not stacked is called:",
  "Bonding the courses",["Painting","Capping","Frosting"],"Offset joints strengthen.")
H('149.d.4.C',3,"A column that is 2 bricks by 4 bricks has how many bricks per course?",
  "Eight",["Four","Two","Twelve"],"2 x 4 = 8 per course.")
H('149.d.4.C',4,"A taller column is most likely to go out of plumb if the mason:",
  "Skips checking with a level",["Uses fresh mortar","Wears gloves","Cleans tools"],"Check often.")
H('149.d.4.D',3,"A ten-brick column has how many bricks in each course?",
  "Ten",["Two","Six","Sixteen"],"Ten per course.")
H('149.d.4.D',4,"Which course layout keeps vertical joints from lining up in a brick column?",
  "Rotating the pattern every other course",["Stacking each course the same","Using all headers","Using no mortar"],"Alternate the pattern.")
H('149.d.5.A',3,"A CMU lead is built at the end of a block wall to:",
  "Set the line for the courses between leads",["Replace the footing","Mark the grade","Cool the mortar"],"Leads guide the wall.")
H('149.d.5.A',4,"When laying a block lead, the first course is set in a full mortar bed and checked for:",
  "Level and alignment",["Color","Weight","Texture"],"Foundation for the lead.")
H('149.d.5.B',3,"A block wall is checked with a level to ensure it is:",
  "Plumb and level",["Dry","Loud","Colored"],"Level and plumb.")
H('149.d.5.B',4,"On a block wall, head joints are normally:",
  "3/8 inch thick",["1 inch thick","1/8 inch thick","3 inches thick"],"Uniform joint thickness.")
H('149.d.5.C',3,"A block corner is built first so that the mason can:",
  "Run a line between the corners",["Skip the line","Avoid the level","Save mortar"],"Corners set the line.")
H('149.d.5.C',4,"Corner block is used to:",
  "Finish the end of a wall with a flat face",["Add color","Cut cost","Reduce weight"],"Special shapes.")
H('149.d.6.A',3,"A 2 by 2 column of 8-inch CMU is built with how many blocks in each course?",
  "Four",["One","Eight","Twelve"],"2 x 2 = 4 blocks per course.")
H('149.d.6.A',4,"An 8-inch CMU nominally measures 8 by 8 by:",
  "16 inches",["12 inches","8 inches","24 inches"],"Standard block size.")
H('149.d.6.B',3,"A six-block column is how many blocks tall if it has six courses?",
  "Six",["Twelve","Three","One"],"One block per course in height.")
H('149.d.6.B',4,"Each course of 8-inch block is how tall including the joint?",
  "8 inches",["4 inches","12 inches","16 inches"],"Nominal height 8.")
H('149.d.6.C',3,"A ten-course block column stands about how tall?",
  "80 inches",["40 inches","100 inches","160 inches"],"10 x 8 = 80.")
H('149.d.6.C',4,"Ten courses of 8-inch block make a column nearly:",
  "6 feet 8 inches",["4 feet","10 feet","12 feet"],"80 inches = 6 ft 8 in.")
H('149.d.6.D',3,"4-inch CMU is mostly used for:",
  "Partition or veneer backup walls",["Heavy footings","Foundations","Roads"],"Thin block for light uses.")
H('149.d.6.D',4,"Compared with 8-inch block, 4-inch block is:",
  "Half as thick",["Twice as thick","The same","Heavier"],"Nominal thickness 4 vs 8.")
H('149.d.6.E',3,"6-inch CMU has a nominal thickness of:",
  "6 inches",["4 inches","8 inches","10 inches"],"Nominal thickness.")
H('149.d.6.E',4,"A 6-inch block is thicker than 4-inch block and thinner than:",
  "8-inch block",["2-inch block","Brick veneer","Floor tile"],"Size order.")
H('149.d.7.A',3,"A composite wall of brick and block combines two:",
  "Different masonry materials",["Roofs","Floors","Doors"],"Composite means combined.")
H('149.d.7.A',4,"In a composite wall, metal ties join the brick to the block backup to:",
  "Help them act together",["Add color","Add weight","Reduce mortar"],"Ties connect the wythes.")
H('149.d.7.B',3,"In a brick and 4-inch block wall, the block wythe is the:",
  "Backup",["Facing","Cap","Footing"],"Block backs up brick.")
H('149.d.7.B',4,"The collar joint of a composite wall is filled with mortar or left as:",
  "An air space",["A paint coat","A roof","A door"],"Cavity design.")
H('149.d.8.A',3,"Coping is placed on top of a masonry wall to:",
  "Shed water and protect the wall",["Decorate the footing","Hold scaffolding","Mark the wall"],"Copings cap walls.")
H('149.d.8.A',4,"A single brick rowlock coping uses bricks laid:",
  "On edge across the wall top",["Flat on the face","Standing on end","In the footing"],"Rowlock coping.")
H('149.d.8.B',3,"A double brick rowlock coping has how many rows across the wall width?",
  "Two",["One","Four","Six"],"Double equals two.")
H('149.d.8.B',4,"Double rowlock coping is used on a wall about how thick?",
  "8 inches",["2 inches","24 inches","40 inches"],"Two rowlocks cover about 8 inches.")
H('149.d.8.C',3,"A 12-inch bonded brick rowlock coping covers a wall:",
  "12 inches wide",["12 feet wide","1 inch wide","4 inches wide"],"Width matches the coping.")
H('149.d.8.C',4,"Bonded coping bricks are laid with joints that are:",
  "Offset like other bonded courses",["Aligned in a stack","Left open","Dry"],"Bonding gives strength.")
H('149.d.8.D',3,"A 16-inch bonded rowlock coping is used on a wall:",
  "Wider than a 12-inch wall",["Narrower than 4 inches","With no width","Under the floor"],"Larger width.")
H('149.d.8.D',4,"Coping should slope slightly to:",
  "Drain water away from the wall",["Pool water","Hold dirt","Hide mortar"],"Slope sheds water.")
H('149.d.8.E',3,"Limestone coping is a type of:",
  "Natural stone cap",["Painted wood","Plastic strip","Rubber pad"],"Limestone is natural.")
H('149.d.8.E',4,"Limestone coping pieces are set with a mortar bed and:",
  "Sealed joints to keep water out",["Open joints","No joints","Painted edges only"],"Water protection.")
H('149.d.8.F',3,"Cast stone is made by:",
  "Casting concrete mixed with fine aggregates in molds",["Carving granite","Cutting plastic","Weaving fibers"],"Cast stone imitates natural stone.")
H('149.d.8.F',4,"Cast stone coping is chosen because it is:",
  "Consistent in color and shape",["Always random","Made of metal","Free of cost"],"Manufactured consistency.")
H('149.d.8.G',3,"Prefab concrete coping is delivered to the site:",
  "Precast in standard lengths",["As liquid","As powder only","As bricks"],"Prefab means pre-made.")
H('149.d.8.G',4,"The joints between prefab coping pieces should be:",
  "Sealed with an appropriate sealant",["Left open","Painted over","Filled with sand only"],"Watertight.")
H('149.d.9.A',3,"Setting natural stone in a random pattern means the pieces are placed:",
  "Without a regular course lines",["In straight perfect rows","In a repeating grid","Only vertically"],"Random is irregular.")
H('149.d.9.A',4,"When setting random stone, each stone should be seated on:",
  "A full bed of mortar",["Dry sand","Loose gravel","Tape"],"Bedding gives stability.")
H('149.d.9.B',3,"An ashlar pattern uses stone cut into:",
  "Rectangular pieces laid in courses",["Round balls","Triangular only","Random chunks"],"Ashlar is squared stone.")
H('149.d.9.B',4,"Ashlar can be coursed or random-coursed. The stones always have:",
  "Squared faces and edges",["Round corners","Jagged breaks","No shape"],"Ashlar is dressed stone.")
H('149.d.9.C',3,"Flat work of natural stone is used for items such as:",
  "Patios and walkways",["Chimney flues","Roofs","Wall footings"],"Flat work is horizontal.")
H('149.d.9.C',4,"Flagstone for flat work is commonly laid in a random pattern over a:",
  "Prepared base",["Wet sand only","Open air","Wall"],"Base prep.")
H('149.d.10.A',3,"Manufactured stone is made from:",
  "Concrete shaped and colored to look like stone",["Real granite","Wood","Plastic only"],"Man-made veneer.")
H('149.d.10.A',4,"Manufactured stone veneer is installed over a surface prepared with:",
  "A scratch coat and lath where required",["Wet paint","Bare plastic","Sand"],"Substrate prep.")
H('149.d.10.B',3,"When installing manufactured stone in an ashlar pattern, the pieces are laid in:",
  "Level horizontal courses",["Random angles","Vertical stacks","Circles"],"Ashlar is coursed.")
H('149.d.10.B',4,"A mason cuts manufactured stone with a:",
  "Masonry saw or hammer and chisel",["Pencil","Paint brush","Spoon"],"Cutting tools.")
H('149.d.11.A',3,"Modular brick has a nominal size of:",
  "4 by 2-2/3 by 8 inches",["12 by 12 by 12 inches","1 by 1 by 1 inch","16 by 16 by 8 inches"],"Standard modular unit.")
H('149.d.11.A',4,"Three courses of modular brick with joints equal how many inches of wall height?",
  "8 inches",["3 inches","12 inches","24 inches"],"Modular coursing 3 = 8.")
H('149.d.11.B',3,"King-size brick compared with modular brick is generally:",
  "Longer",["Shorter","Smaller overall","Square"],"Larger unit.")
H('149.d.11.B',4,"A mason laying king-size brick to a line adjusts the course height because the brick is:",
  "A different height than modular",["Bigger on the ceiling","Painted","Heavy"],"Modular rules change.")
H('149.d.11.C',3,"Queen-size brick is similar to king-size brick but typically:",
  "A bit narrower in height",["Wider by double","Made of metal","Round"],"Different dimension.")
H('149.d.11.C',4,"Queen brick used with a line needs course heights checked with a:",
  "Story pole or gauge",["Thermometer","Calendar","Paint chart"],"Gauge keeps coursing.")
H('149.d.11.D',3,"Utility brick measures nominally:",
  "4 by 4 by 12 inches",["2 by 2 by 4 inches","8 by 8 by 8 inches","1 by 1 by 1 inch"],"Utility is large.")
H('149.d.11.D',4,"Because utility brick is taller, one course gains height of:",
  "4 inches nominally",["1 inch","12 inches","16 inches"],"Utility course = 4 in.")
H('149.d.12.A',3,"When laying 8-inch CMU to a line, the top outside edge of each block touches the:",
  "Line without pushing it",["Floor","Roof","Ladder"],"Line gauges position.")
H('149.d.12.A',4,"The mason uses a level along the block course to check it is:",
  "Level and in the same plane",["Wet","Dirty","New"],"Alignment.")
H('149.d.12.B',3,"4-inch CMU laid to a line must be handled with care because it is:",
  "Thinner and more fragile than 8-inch",["Thicker than brick","Always solid","Made of steel"],"Thin units crack easily.")
H('149.d.12.B',4,"A 4-inch block wall without lateral support can be:",
  "Unstable at height",["Very strong","Fireproof only","Waterproof only"],"Needs bracing.")
H('149.d.12.C',3,"6-inch CMU laid to a line is often used for:",
  "Interior walls",["Footings","Roads","Bridge decks"],"Mid-size block.")
H('149.d.12.C',4,"Compared with 8-inch block, a 6-inch wall uses:",
  "Less material per square foot",["More material","The same","No block"],"Thinner wall.")
H('149.d.12.D',3,"12-inch CMU is chosen for walls that need:",
  "More thickness and strength",["Less weight only","Lower cost only","Color only"],"Heavy-duty block.")
H('149.d.12.D',4,"Because 12-inch block is heavy, masons often use:",
  "Two people or lifting aids",["Their teeth","Rope ladders","Water balloons"],"Safe lifting.")

# ---------- 127.150 Masonry II (Practicum) ----------
H('150.d.2',3,"A mason finds a wall racked out of line. A strong problem-solving first step is to:",
  "Check the line and level to find the cause",["Ignore it","Add paint","Remove the line"],"Diagnose before fixing.")
H('150.d.2',4,"Critical thinking on a masonry site means weighing options before deciding. When mortar sets too fast in hot weather, a good decision is to:",
  "Mix smaller batches and keep the mortar tempered",["Add dry cement","Let it harden fully","Use it as is"],"Adjust to conditions.")
H('150.d.1.A',3,"On a masonry job, clear spoken communication prevents:",
  "Mistakes in layout and coursing",["Pay","Weather","Mortar"],"Communicate clearly.")
H('150.d.1.A',4,"When a lead mason says \"check your line,\" the helper should:",
  "Confirm the line is tight and in place",["Move the level","Leave","Ignore it"],"Respond to directions.")
H('150.d.1.B',3,"A bricklayer who winces while watching a helper lift a block may be signaling:",
  "A concern about technique",["Delight","Boredom","Nothing"],"Read cues.")
H('150.d.1.B',4,"A foreman's silence while looking at your joints may mean:",
  "They want you to check the work",["They love it","The work is perfect","Lunch is ready"],"Interpret cues.")
H('150.d.1.C',3,"Active listening on a masonry crew includes:",
  "Repeating the instructions to confirm",["Interrupting","Texting","Walking away"],"Confirm.")
H('150.d.1.C',4,"Before building a corner, the mason asks the foreman a question about the plan to:",
  "Clarify the layout",["Waste time","Avoid work","Delay lunch"],"Questions help.")
H('150.d.3.A',3,"Masonry workers should wear safety glasses because chipped brick and block create:",
  "Flying fragments",["Cold air","Extra light","Sound"],"Eye protection.")
H('150.d.3.A',4,"Silica dust from cutting masonry is controlled with wet cutting or a:",
  "Dust collection system and respirator",["Fan blowing it around","Open flame","Paint"],"Protect lungs.")
H('150.d.3.B',3,"After a minor injury from a sharp brick edge, the worker should:",
  "Report it and get first aid",["Hide it","Ignore it","Wait a week"],"Report.")
H('150.d.3.B',4,"Why is a workplace injury report important?",
  "It documents what happened so it can be prevented",["It cuts pay","It slows the job","It is for fun"],"Documentation.")
H('150.d.4.A',3,"A positive work ethic on a masonry crew is shown by arriving:",
  "On time ready to work",["Late","Without tools","Unprepared"],"Reliable.")
H('150.d.4.A',4,"Cleaning mortar splatter from a finished wall without being asked shows:",
  "Pride in the work",["Laziness","Fear","Carelessness"],"Initiative.")
H('150.d.4.B',3,"A mason notices a coworker skipping wall ties. Ethical reasoning says to:",
  "Report it since it affects safety",["Say nothing","Laugh","Copy them"],"Safety matters.")
H('150.d.4.B',4,"Using the wrong mortar type to save money on a load-bearing wall is:",
  "Unethical and unsafe",["Smart","Required","Allowed"],"Honesty and safety.")
H('150.d.4.C',3,"Complying with building codes in masonry means building walls that:",
  "Meet the required strength and design",["Look nice only","Cost less only","Are fast only"],"Compliance.")
H('150.d.4.C',4,"If an inspector fails a masonry wall, the mason should:",
  "Correct the work to meet code",["Ignore the report","Paint over it","Argue loudly"],"Fix noncompliance.")
H('150.d.5.A',3,"In a supervised masonry practicum, a student keeps a log of:",
  "Tasks done and skills practiced",["Jokes","Songs","Gossip"],"Document learning.")
H('150.d.5.A',4,"A practicum supervisor evaluates the student by observing:",
  "Work quality and safe habits",["Weather","Lunch","Hair"],"Evaluation.")
H('150.d.5.B',3,"Advanced technical knowledge for a mason includes understanding:",
  "Mortar types and bond patterns",["Hair care","Cooking","Music"],"Technical depth.")
H('150.d.5.B',4,"Type S mortar is often chosen for below-grade or heavier-load work because it has:",
  "Higher compressive strength",["Lower strength","No cement","More water"],"Mortar types.")
H('150.d.5.C',3,"Advanced mortar spreading is judged by whether the bed is:",
  "Uniform and full",["Thin and patchy","Lumpy","Dry"],"Skill.")
H('150.d.5.C',4,"A mason who spreads mortar too far ahead of the units risks:",
  "Mortar drying before the unit is placed",["Wet bricks","Cold hands","Loud noise"],"Setting time.")
H('150.d.5.D',3,"A single wythe brick wall has:",
  "One layer of brick",["Two layers","Three layers","No bricks"],"Single wythe is one thickness.")
H('150.d.5.D',4,"The wall face of a single wythe is checked with a level for:",
  "Plumb and straight alignment",["Smell","Color","Sound"],"Quality control.")
H('150.d.5.E',3,"A wall with stretchers, headers, and rowlocks shows several:",
  "Brick positions",["Roof types","Paint colors","Door styles"],"Bond variety.")
H('150.d.5.E',4,"Using different brick positions in a wall helps create:",
  "Pattern and detail",["Mud","Less strength only","Higher cost only"],"Decorative patterns.")
H('150.d.5.F',3,"Advanced column work requires each course to be:",
  "Plumb and aligned with the course below",["Random","Colored","Dry"],"Precision.")
H('150.d.5.F',4,"If a column leans after several courses, the mason should:",
  "Take down and rebuild the affected courses",["Leave it","Add more mortar","Paint it"],"Fix early.")
H('150.d.5.G',3,"Laying CMU with advanced proficiency means block courses are:",
  "Level, plumb, and consistent in joint thickness",["Rough","Uneven","Crooked"],"Skill measures.")
H('150.d.5.G',4,"In a block wall, a control joint is placed to allow for:",
  "Movement from shrinkage and temperature change",["Decoration","Color","Lighting"],"Control joints prevent cracks.")
H('150.d.5.H',3,"A block column reinforced with steel rebar and grout is called a:",
  "Reinforced column",["Hollow shell","Veneer","Mockup"],"Reinforcement.")
H('150.d.5.H',4,"Grout is placed in block cores to:",
  "Bond the reinforcement and add strength",["Decorate the wall","Cool the block","Add color only"],"Grouting.")
H('150.d.5.I',3,"A composite masonry wall of brick and block must have:",
  "Ties across the cavity",["No ties","Loose blocks","Wooden stakes"],"Ties connect.")
H('150.d.5.I',4,"The air space in a cavity wall helps keep moisture from:",
  "Passing through to the interior",["Entering the cavity at all times","Flowing upward","Making mortar"],"Drainage cavity.")
H('150.d.5.J',3,"Coping on a masonry wall is installed with advanced skill when it:",
  "Sheds water and aligns evenly",["Tilts inward","Leaves gaps","Is unlevel"],"Quality coping.")
H('150.d.5.J',4,"Flashing under coping directs water:",
  "Out of the wall",["Into the wall","Upward","Nowhere"],"Flashing protects.")
H('150.d.5.K',3,"Building a natural stone wall with advanced skill means each stone:",
  "Fits tightly with stable bearing",["Floats loose","Is stacked dry only","Is angled randomly"],"Stable stonework.")
H('150.d.5.K',4,"Stone in a dry-stacked wall relies on weight and fit instead of:",
  "Mortar",["Gravity","Friction","Shape"],"Dry stack has no mortar.")
H('150.d.5.L',3,"Advanced installation of manufactured stone includes keeping joints:",
  "Consistent in width",["Random widths","Dry","Open"],"Quality.")
H('150.d.5.L',4,"Before installing manufactured stone, the wall must have a moisture barrier to:",
  "Protect the structure from water",["Add color","Cool the stone","Hold paint"],"Weather barrier.")
H('150.d.5.M',3,"Laying brick and CMU to a line with advanced proficiency means the:",
  "Unit edges touch the line without moving it",["Units press the line out","Line is slack","Line is cut"],"Line accuracy.")
H('150.d.5.M',4,"A story pole helps the mason keep:",
  "Course heights consistent",["Paint wet","Tools clean","Mortar cold"],"Gauge.")
H('150.d.5.N',3,"Growth in masonry skill is shown by:",
  "Faster, cleaner, more accurate work over time",["More mistakes","More breaks","Less practice"],"Progress.")
H('150.d.5.N',4,"A student shows growth by comparing early walls with:",
  "Later walls",["Nothing","Other trades","Photos of trucks"],"Compare work.")
H('150.d.5.O',3,"Evaluating strengths and weaknesses helps a student:",
  "Decide what to practice next",["Quit","Hide errors","Blame others"],"Self-assess.")
H('150.d.5.O',4,"A student who lays level walls but struggles with plumb corners should:",
  "Practice building and checking corners",["Stop building corners","Ignore it","Quit"],"Target weakness.")
H('150.d.5.P',3,"Representative work samples in masonry might include:",
  "Photos of finished walls and columns",["Poems","Songs","Jokes"],"Documentation.")
H('150.d.5.P',4,"A work-sample photo of a corner should show the:",
  "Level and plumb of the finished work",["Weather only","Parking lot","Truck"],"Evidence.")

# ---------- 127.151 Architectural Design / Communication ----------
H('151.d.1.A',3,"An architectural student presenting a floor plan to a client should speak:",
  "Clearly and use correct terms",["Quietly","Vaguely","Quickly without pausing"],"Effective communication.")
H('151.d.1.A',4,"Written communication in architecture, such as a design brief, should be:",
  "Concise, accurate, and organized",["Long and vague","Unrelated","Poetic only"],"Written skills.")
H('151.d.1.B',3,"A scale of 1/4 inch = 1 foot shows a 16-foot wall as how many inches on paper?",
  "4",["16","1/4","8"],"16 x 1/4 = 4.")
H('151.d.1.B',4,"A room measures 3 inches by 2 inches on a 1/4-inch scale drawing. The real room is:",
  "12 feet by 8 feet",["3 feet by 2 feet","6 feet by 4 feet","24 feet by 16 feet"],"3 / 0.25 = 12; 2 / 0.25 = 8.")
H('151.d.1.C',3,"A beam bends under load because of the forces of:",
  "Tension and compression",["Color","Smell","Sound"],"Structural forces.")
H('151.d.1.C',4,"Thermal mass in a building wall helps by:",
  "Storing and releasing heat slowly",["Making noise","Blocking all light","Producing electricity"],"Science applied to design.")
H('151.d.1.D',3,"On a set of plans, a section view shows:",
  "A slice through the building",["Only the roof","A color picture","The yard"],"Reading drawings.")
H('151.d.1.D',4,"A legend on a drawing sheet explains:",
  "The meaning of symbols",["The owner's name","The weather","The price"],"Read symbols.")
H('151.d.2.A',3,"Basic materials used in architectural models include foam board, balsa wood, and:",
  "Cardstock",["Concrete blocks","Steel beams","Glass blocks"],"Model-making supplies.")
H('151.d.2.A',4,"A student chooses foam board for a quick study model because it is:",
  "Easy to cut and inexpensive",["Brittle and expensive","Heavy","Hard to cut"],"Material selection.")
H('151.d.2.B',3,"A tool used to cut model materials precisely is a:",
  "Hobby knife with a straightedge",["Sledgehammer","Garden hose","Paint roller"],"Model tools.")
H('151.d.2.B',4,"Safety with a hobby knife includes cutting:",
  "Away from your body on a cutting mat",["Toward your hand","Without a mat","On your lap"],"Safe habits.")
H('151.d.2.C',3,"Used spray adhesive and solvents in a studio should be handled by:",
  "Following the safety data sheet",["Pouring in drains","Burning","Ignoring labels"],"Hazard handling.")
H('151.d.2.C',4,"Leftover paint and solvents from model making should be:",
  "Disposed of as hazardous waste per rules",["Poured down the sink","Burned","Given to students"],"Disposal.")
H('151.d.2.D',3,"Building information modeling and 3D printing are examples of:",
  "New and emerging technologies",["Outdated tools","Hand tools","Toys only"],"Emerging tech.")
H('151.d.2.D',4,"An architect might use virtual reality to let clients:",
  "Walk through a design before it is built",["Pour concrete","Order lunch","Pay taxes"],"VR walkthroughs.")
H('151.d.3.A',3,"Multimedia communication in architecture can combine drawings, renderings, and:",
  "Animations",["Rumors","Recipes","Songs"],"Multimedia.")
H('151.d.3.A',4,"A rendering helps a client understand a design by showing:",
  "A realistic image of the finished building",["The budget","The code","The permit"],"Visualization.")
H('151.d.3.B',3,"The interpretation of an architectural drawing can depend on the viewer's:",
  "Training and experience",["Height","Hair","Shoes"],"Factors.")
H('151.d.3.B',4,"A drawing in plan view may be misread by a client who has never seen:",
  "Technical drawing conventions",["Pencils","Paper","Rulers"],"Audience matters.")
H('151.d.3.C',3,"One role of communication in architecture is to:",
  "Inform the client of design decisions",["Hide design decisions","Confuse the client","Delay the work"],"Roles.")
H('151.d.3.C',4,"A pitch to win a client's approval is an example of communication that:",
  "Persuades",["Entertains only","Informs only","Warns only"],"Persuade.")
H('151.d.4.A',3,"To improve a communication product such as a brochure, a designer first:",
  "Identifies what the audience needs",["Picks a color","Prints more","Hides content"],"Needs first.")
H('151.d.4.A',4,"If a client says a presentation board is too cluttered, the designer should:",
  "Simplify the layout",["Add more text","Add more colors","Make it smaller"],"Respond to feedback.")
H('151.d.4.B',3,"A project portfolio in architecture includes sketches, drawings, and:",
  "Photos of models",["Receipts","Menus","Gossip"],"Portfolio content.")
H('151.d.4.B',4,"Entries in a portfolio are most useful when they include:",
  "Titles, dates, and descriptions",["Nothing","Blank pages","Random notes"],"Organized evidence.")
H('151.d.5.A',3,"Architects and students use plotters and printers as:",
  "Output equipment",["Furniture","Roofing","Plumbing"],"Equipment.")
H('151.d.5.A',4,"A laser cutter in a design lab is useful for cutting:",
  "Precise model parts",["Concrete slabs","Steel beams","Grass"],"Laser use.")
H('151.d.5.B',3,"Producing an architectural project with multimedia techniques might mean creating:",
  "A model and a digital presentation",["Only a note","A single scribble","Nothing"],"Production.")
H('151.d.5.B',4,"A good multimedia project communicates the design:",
  "Through more than one format",["With no pictures","Only by speaking","Only by text"],"Multiple formats.")
H('151.d.6.A',3,"An architect checks the building code to learn the maximum:",
  "Building height allowed",["Paint brand","Roof color","Landscaping style"],"Code areas.")
H('151.d.6.A',4,"Accessibility rules in the ADA affect the design of:",
  "Ramps, doors, and restrooms",["Roof shingles","Paint colors","Light bulbs"],"Regulation topic.")
H('151.d.6.B',3,"To find the zoning rules for a lot, an architect checks with the:",
  "City planning department",["Weather service","School bus company","Phone store"],"Locate rules.")
H('151.d.6.B',4,"The International Building Code is a model code that cities may:",
  "Adopt with local changes",["Ignore always","Use only for toys","Print for fun"],"Model code.")
H('151.d.6.C',3,"Complying with code includes getting the plans reviewed and:",
  "Approved before building",["Painted","Photographed","Ignored"],"Plan review.")
H('151.d.6.C',4,"A building that violates fire codes may be:",
  "Required to be corrected or closed",["Praised","Given a prize","Painted"],"Penalty.")
H('151.d.7.A',3,"Improving a product, such as a chair design, with a problem-solving strategy starts by:",
  "Defining the problem to be solved",["Selling it","Painting it","Packaging it"],"Problem first.")
H('151.d.7.A',4,"A student tests a model bridge, sees it sag, and then adjusts the design. This is an example of:",
  "Iterative problem solving",["Giving up","Guessing","Copying"],"Test and revise.")
H('151.d.7.B',3,"Critical thinking when comparing two floor plans involves checking:",
  "Which one better meets the requirements",["Which looks fancier","Which is bigger","Which is cheaper only"],"Analysis.")
H('151.d.7.B',4,"To evaluate a design critically, a student gathers:",
  "Evidence such as measurements and feedback",["Rumors","Guesses","Slogans"],"Evidence.")
H('151.d.7.C',3,"A decision matrix for choosing a material compares options using:",
  "Criteria such as cost and durability",["Names","Colors","Moods"],"Decision-making.")
H('151.d.7.C',4,"When the criteria of cost and strength conflict, the designer decides by:",
  "Weighing which criteria matter most",["Flipping a coin","Ignoring both","Choosing randomly"],"Prioritize.")
H('151.d.8.A',3,"Using written, verbal, and visual communication together helps an architect:",
  "Reach different audiences",["Confuse clients","Delay work","Hide details"],"Multiple modes.")
H('151.d.8.A',4,"A drawing with a clear title block and notes combines:",
  "Visual and written communication",["Only audio","Only video","Nothing"],"Consistency.")
H('151.d.8.B',3,"An architect calculates the area of a 14 ft by 10 ft room as:",
  "140 square feet",["24 square feet","48 square feet","1,400 square feet"],"14 x 10 = 140.")
H('151.d.8.B',4,"A drawing scale is a ratio, so a 1:50 scale means 1 unit on paper equals how many units real?",
  "50",["5","500","10"],"Ratio meaning.")
H('151.d.8.C',3,"Daylight design uses windows placed to bring in:",
  "Natural light",["Noise","Dust","Heat only"],"Science principle.")
H('151.d.8.C',4,"In cold climates, designers add insulation to lower:",
  "Heat loss through walls",["Light levels","Window sizes","Paint cost"],"Thermal principles.")
H('151.d.9.A',3,"Entry-level architecture jobs often require at least:",
  "A high school diploma and training",["A pilot license","A law degree","No training"],"Preparation.")
H('151.d.9.A',4,"To become a licensed architect, a person must pass the:",
  "Architect Registration Examination",["SAT only","Driving test","Bar exam"],"Licensing.")
H('151.d.9.B',3,"The demand for architects tends to follow the:",
  "Construction market",["Weather forecast","Sports season","Fashion trends"],"Outlook.")
H('151.d.9.B',4,"A source for job outlook data in architecture is the:",
  "Bureau of Labor Statistics",["Weather channel","Music charts","Sports page"],"Data source.")
H('151.d.9.C',3,"Starting your own design firm is an example of:",
  "Entrepreneurship",["Retirement","Volunteering","Internship"],"Entrepreneurial path.")
H('151.d.9.C',4,"A small firm owner must handle design work and also:",
  "Business tasks such as billing and marketing",["Only designing","Only cleaning","Nothing else"],"Business skills.")
H('151.d.9.D',3,"A person who prefers working in a team may choose an architecture career in:",
  "A large firm",["A solo hermit job","An isolated cabin","A remote island"],"Personal interests.")
H('151.d.9.D',4,"Family responsibilities may affect career choice by influencing:",
  "Hours and location a person can work",["Eye color","Hair color","Shoe size"],"Priorities.")
H('151.d.9.E',3,"Compared with a drafter, a licensed architect usually has:",
  "More responsibility and often higher pay",["Less responsibility","No duties","Lower training"],"Rewards vs demands.")
H('151.d.9.E',4,"A demand of senior design roles often includes:",
  "Long hours near deadlines",["No deadlines","No clients","No meetings"],"Demands.")
H('151.d.9.F',3,"Architects keep their licenses current through:",
  "Continuing education",["Holidays","Paint classes","Sleeping"],"Continuing ed.")
H('151.d.9.F',4,"Learning new software is an example of professional:",
  "Development",["Decline","Rest","Retirement"],"Development.")
H('151.d.10.A',3,"An employer's responsibility to employees includes providing a:",
  "Safe workplace",["Free car","Private jet","Vacation home"],"Rights.")
H('151.d.10.A',4,"An employee's responsibility includes:",
  "Following safety rules and company policies",["Ignoring policies","Hiding errors","Skipping meetings"],"Responsibilities.")
H('151.d.10.B',3,"An ethical architect protects the public by:",
  "Designing safe buildings",["Cutting corners","Ignoring codes","Hiding defects"],"Ethics.")
H('151.d.10.B',4,"Giving credit to a coworker whose idea you use is:",
  "An ethical practice",["Wasteful","Required by paint","Optional by law"],"Honest credit.")
H('151.d.10.C',3,"Copyright protects a designer's:",
  "Original drawings",["Receipts","Parking","Tools"],"Legal aspects.")
H('151.d.10.C',4,"Using a licensed software copy for a project avoids:",
  "Legal penalties for piracy",["Tax","Costs of paper","Deadlines"],"Legal.")
H('151.d.10.D',3,"A school-based learning activity for architecture could involve:",
  "Designing a small structure for a real client need",["Watching videos only","Doing nothing","Napping"],"Collaboration.")
H('151.d.10.D',4,"When collaborating with a teacher, a student should agree on:",
  "Goals and a timeline",["The color of pens","Lunch menu","Music"],"Plan.")
H('151.d.10.E',3,"Presenting a project in at least two formats might mean a model and a:",
  "Graphic board",["Rumor","Song","Joke"],"Formats.")
H('151.d.10.E',4,"A video presentation of a design is useful because it can show:",
  "Movement through spaces",["Only text","Only color","Nothing"],"Format benefit.")
H('151.d.10.F',3,"A portfolio that documents experience may include graphics, photographs, and:",
  "Written reflections",["Rumors","Games","Songs"],"Documentation.")
H('151.d.10.F',4,"Reflecting on what a project taught you helps you:",
  "Improve future work",["Forget it","Skip tasks","Avoid work"],"Reflection.")
H('151.d.10.G',3,"A professional resume lists education, skills, and:",
  "Work experience",["Hobbies only","Recipes","Songs"],"Resume.")
H('151.d.10.G',4,"A resume should be updated whenever you:",
  "Gain new skills or experience",["Eat lunch","Take a nap","Change shoes"],"Keep current.")

# ---------- 127.152 Architectural Practicum ----------
H('152.d.1.A',3,"In an architectural practicum, a student explaining a design to a team should use:",
  "Clear, consistent language",["Vague slang","Whispers","Random words"],"Communication.")
H('152.d.1.A',4,"Consistent verbal and nonverbal communication means your words and body language:",
  "Support each other",["Contradict each other","Are unrelated","Are ignored"],"Alignment.")
H('152.d.1.B',3,"An intern uses active listening to understand a supervisor's:",
  "Design comments",["Paycheck","Parking","Lunch"],"Active listening.")
H('152.d.1.B',4,"After a supervisor gives feedback, the intern should:",
  "Paraphrase to confirm understanding",["Argue","Ignore","Walk away"],"Confirm.")
H('152.d.1.C',3,"Formal presentations differ from informal ones in that they:",
  "Follow a prepared structure for a set audience",["Have no audience","Skip visuals","Are random"],"Presentations.")
H('152.d.1.C',4,"An informal presentation might be a quick desk crit between:",
  "Two coworkers",["A crowd of thousands","A jury of strangers","A TV audience"],"Informal.")
H('152.d.1.D',3,"Interpreting data from a site survey requires reading:",
  "Measurements and drawings",["Menus","Posters","Songs"],"Data.")
H('152.d.1.D',4,"A chart showing energy use of three building designs helps the team:",
  "Compare the designs",["Pick a name","Paint walls","Order supplies"],"Communicate data.")
H('152.d.1.E',3,"If a client frowns at a rendering, the designer should:",
  "Ask what concerns them",["Ignore the frown","Leave","Argue"],"Cues.")
H('152.d.1.E',4,"A client who nods and leans forward during a presentation is likely:",
  "Engaged and interested",["Asleep","Angry","Bored"],"Cues.")
H('152.d.2.A',3,"Independent critical thinking means evaluating a plan:",
  "On your own using evidence",["By copying others","By guessing","By luck"],"Critical.")
H('152.d.2.A',4,"A team evaluating design options critically should share:",
  "Reasons and evidence",["Only opinions","Only votes","Only jokes"],"Team analysis.")
H('152.d.2.B',3,"To solve a tight-site problem creatively, an architect might first:",
  "Sketch several layout options",["Pick one at once","Quit","Ignore the site"],"Creative solutions.")
H('152.d.2.B',4,"A site with a steep slope can be an opportunity to design:",
  "Stepped levels that follow the land",["A flat shoebox only","No building","A floating roof"],"Innovate.")
H('152.d.2.C',3,"A weighted decision matrix with scores for cost, function, and appearance helps the team:",
  "Choose among options fairly",["Avoid deciding","Hide scores","Delay"],"Decision-making.")
H('152.d.2.C',4,"In a weighted matrix, a criterion with a higher weight:",
  "Has more influence on the final score",["Has less influence","Is ignored","Is removed"],"Weighting.")
H('152.d.2.D',3,"To improve a product by a problem-solving strategy, a team first:",
  "Names the problem clearly",["Paints it","Prints it","Hides it"],"Strategy.")
H('152.d.2.D',4,"After testing a prototype, the team uses the results to:",
  "Refine the design",["Throw it away","Hide the test","Skip the next step"],"Iterate.")
H('152.d.2.E',3,"Critical-thinking strategies for evaluating a product include asking:",
  "Does it meet the stated needs?",["Is it pretty?","Is it loud?","Is it blue?"],"Evaluate.")
H('152.d.2.E',4,"When analyzing why a prototype failed, the team should look for:",
  "The root cause",["Someone to blame","A new color","A bigger budget"],"Root cause.")
H('152.d.2.F',3,"Technical research for a design decision may use:",
  "Manufacturer data and codes",["Gossip","Guesswork","Social posts"],"Research.")
H('152.d.2.F',4,"Which source is most reliable for a material's fire rating?",
  "The manufacturer's tested data sheet",["A rumor","A random comment","A stranger's opinion"],"Reliable sources.")
H('152.d.3.A',3,"Workplace safety rules in a design studio include keeping walkways:",
  "Clear of cords and boxes",["Blocked","Dark","Wet"],"Studio safety.")
H('152.d.3.A',4,"Ergonomic safety at a drafting workstation includes adjusting:",
  "Chair height and monitor position",["Paper color","Pencil brand","Room number"],"Ergonomics.")
H('152.d.3.B',3,"Hazardous materials such as spray adhesive are disposed of:",
  "According to safety data sheet instructions",["In any trash can","Down the drain","Outside"],"Disposal.")
H('152.d.3.B',4,"Before using a new chemical in the model shop, check the:",
  "Safety data sheet",["Price tag","Brand","Color"],"Hazards.")
H('152.d.3.C',3,"A laser cutter must be used with:",
  "Ventilation and supervision",["No guard","Wet floors","Open flame"],"Equipment safety.")
H('152.d.3.C',4,"Before operating any shop tool, a student should receive:",
  "Training and permission",["A prize","A day off","A snack"],"Training first.")
H('152.d.4.A',3,"A positive work ethic in an architecture office means meeting:",
  "Deadlines",["Nobody","Strangers","Birds"],"Work ethic.")
H('152.d.4.A',4,"Taking responsibility for a mistake in a drawing means:",
  "Admitting it and fixing it",["Blaming others","Hiding it","Deleting it"],"Accountability.")
H('152.d.4.B',3,"Ethical reasoning in architecture means considering the effect on:",
  "Public safety and the client",["Only profit","Only fame","Only speed"],"Ethical reasoning.")
H('152.d.4.B',4,"If a client asks you to leave out a required fire exit, you should:",
  "Decline and explain the code",["Remove it","Hide it","Ignore the code"],"Ethics.")
H('152.d.4.C',3,"Ethical practice as defined by the architectural industry includes protecting the:",
  "Health, safety, and welfare of the public",["Architect's fame","Competition","Paint stock"],"Professional ethics.")
H('152.d.4.C',4,"Plagiarism in design means:",
  "Passing off someone else's work as your own",["Giving credit","Citing sources","Sketching"],"Ethics.")
H('152.d.4.D',3,"Complying with rules consistently includes following the:",
  "Building code on every project",["Code on some projects","Code never","Code when watched"],"Compliance.")
H('152.d.4.D',4,"A design that does not meet the required setback may need to be:",
  "Revised before approval",["Built anyway","Painted","Hidden"],"Compliance.")
H('152.d.5.A',3,"In a supervised practicum with an architect, a student documents:",
  "Tasks, hours, and skills learned",["Gossip","Songs","Jokes"],"Documentation.")
H('152.d.5.A',4,"A practicum student's supervisor evaluates progress using:",
  "Observations and the student's documentation",["Luck","Rumors","Weather"],"Evaluation.")
H('152.d.5.B',3,"Advanced technical knowledge may include understanding:",
  "Structural systems and building envelope",["Hair care","Cooking","Music"],"Technical.")
H('152.d.5.B',4,"The building envelope refers to the building's:",
  "Exterior shell separating inside from outside",["Floor plan","Parking","Furniture"],"Envelope.")
H('152.d.5.C',3,"Reading a set of construction documents requires understanding:",
  "Symbols, scales, and notes",["Recipes","Poems","Songs"],"Reading drawings.")
H('152.d.5.C',4,"A detail callout on a plan refers the reader to:",
  "A more detailed drawing elsewhere",["The owner","The weather","The budget"],"Callouts.")
H('152.d.5.D',3,"Designing a multimedia rendering product starts with:",
  "Understanding the message and audience",["Choosing a font","Buying paper","Hiding data"],"Design process.")
H('152.d.5.D',4,"A good rendering design emphasizes the:",
  "Key features of the building",["Backgrounds only","Colors only","Credits"],"Focus.")
H('152.d.5.E',3,"Producing a rendering uses software that applies:",
  "Materials, lighting, and camera views",["Paint","Fabric","Wood"],"Production.")
H('152.d.5.E',4,"Before sharing a final rendering, the student should check it for:",
  "Accuracy and quality",["Smells","Time of day","Parking"],"Quality.")
H('152.d.5.F',3,"Evaluating strengths and weaknesses in technical skill helps the student:",
  "Plan improvement",["Quit","Hide errors","Blame others"],"Self-evaluation.")
H('152.d.5.F',4,"A student strong at sketching but slower at CAD should:",
  "Practice CAD with timed exercises",["Stop sketching","Avoid CAD","Quit"],"Target weakness.")
H('152.d.5.G',3,"Representative work samples in an architectural practicum include:",
  "Plans, sketches, and renderings",["Gossip","Songs","Menus"],"Samples.")
H('152.d.5.G',4,"A portfolio piece should be selected because it shows:",
  "Your best, representative skill",["The worst work","Nothing","Random scribbles"],"Selection.")

H('150.d.5.O',5,"A student's wall passes level checks but fails on joint consistency. The best self-evaluation response is to:",
  "Record the weakness and practice uniform joints",["Hide the result","Blame the mortar","Stop laying brick"],"Honest self-evaluation drives improvement.")
H('151.d.10.A',5,"Under workplace rights in an architecture firm, an intern who sees an unsafe studio condition should:",
  "Report it to a supervisor",["Ignore it","Fix wiring alone","Leave quietly"],"Employees may report hazards.")
H('151.d.10.G',5,"Which resume entry best fits an architectural design student?",
  "Built a scale model and presented it to a panel",["Likes movies","Owns a car","Enjoys naps"],"Relevant, specific experience.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_22.jsonl'))

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('127.', 1095 + 1, own='cte_19.jsonl')
def H(code, d, q, right, wrong, e):
    return B.hand(code, d, q, right, wrong, e)

# ---------- 127.110 Electrical (advanced / commercial-industrial) ----------
H('110.d.1.A',3,"Which habit shows safe work on a commercial construction site?",
  "Inspecting tools and the work area before starting",["Skipping inspections to save time","Working alone with no communication","Removing guards to work faster"],"Safe procedures begin with inspecting tools and the area.")
H('110.d.1.A',4,"A crew lead sees a frayed cord on a power tool. What is the correct action?",
  "Tag it out of service and replace it",["Wrap it with tape and keep using it","Use it only for short jobs","Let the next shift handle it"],"Damaged tools are removed from service.")
H('110.d.1.B',3,"OSHA is a federal agency whose main job is to:",
  "Set and enforce workplace safety rules",["Collect income taxes from workers","License all new buildings","Set prices for electrical materials"],"OSHA protects workers.")
H('110.d.1.B',4,"A worker can contact OSHA to report:",
  "An unsafe condition at the job site",["A late paycheck only","A broken vending machine","A noisy neighbor"],"Workers may report hazards.")
H('110.d.1.C',3,"Which situation is an electrical hazard on a jobsite?",
  "Exposed energized conductors within reach",["A tool belt hanging on a hook","Clean and dry floors","A posted safety sign"],"Exposed live parts can shock.")
H('110.d.1.C',4,"Working with wet hands near a live panel greatly raises the risk of:",
  "Severe electric shock",["Better conductivity of tools","Faster work","Lower voltage"],"Moisture lowers body resistance.")
H('110.d.1.D',3,"The purpose of a lockout device on a disconnect is to:",
  "Prevent the equipment from being energized during service",["Speed up the power restore","Identify the cheapest breaker","Keep the panel cool"],"Locks keep power off.")
H('110.d.1.D',4,"After locking out a circuit, the technician should next:",
  "Verify with a meter that the circuit is dead",["Assume it is dead","Remove the lock","Ask a coworker to turn it on"],"Always test for zero energy.")
H('110.d.2.A',3,"A branch circuit is the wiring that runs from the:",
  "Final overcurrent device to the outlets it serves",["Utility pole to the meter","Meter to the street","Panel to the grounding rod"],"Branch circuits feed loads.")
H('110.d.2.A',4,"Ampacity is best defined as the:",
  "Current a conductor can carry without overheating",["Voltage a battery stores","Length of a wire run","Resistance of a motor"],"Ampacity limits heat.")
H('110.d.2.B',3,"A totally enclosed motor enclosure is used where the motor must be protected from:",
  "Dust and moisture entering the frame",["Operators seeing it","Cool air","Mounting hardware"],"Enclosures protect the motor.")
H('110.d.2.B',4,"An open drip-proof motor is generally best suited to:",
  "Clean indoor areas",["Wet washdown rooms","Dusty grain mills","Explosive atmospheres"],"Open motors need clean air.")
H('110.d.2.C',3,"A motor nameplate lists 230 V while the system supplies 240 V. This difference shows that motor rated voltage:",
  "May differ slightly from system voltage",["Must always be exactly equal","Is ignored by the code","Is a measure of speed"],"Ratings differ from nominal system voltage.")
H('110.d.2.C',4,"Running a motor far below its rated voltage usually causes:",
  "Higher current and overheating",["Lower current and cooling","Faster speed","No change"],"Low voltage raises current.")
H('110.d.2.D',3,"The moving part of a squirrel-cage induction motor is the:",
  "Rotor",["Stator","Frame","Terminal block"],"The rotor turns.")
H('110.d.2.D',4,"The stator of a three-phase induction motor contains:",
  "Windings that create a rotating magnetic field",["Permanent bars only","A fuel tank","Brushes and a commutator"],"Stator windings create the field.")
H('110.d.2.E',3,"When supply frequency rises while the pole count is unchanged, synchronous speed will:",
  "Go up",["Go down","Stay at zero","Reverse direction"],"Speed is proportional to frequency.")
H('110.d.2.E',4,"A 60 Hz, 4-pole motor has a synchronous speed of:",
  "1800 rpm",["900 rpm","3600 rpm","1200 rpm"],"120 x 60 / 4 = 1800.")
H('110.d.2.F',3,"Torque in an induction motor is developed by the interaction of the rotor currents and the:",
  "Rotating stator magnetic field",["Frame paint","Cooling fan only","Nameplate"],"Field and current make torque.")
H('110.d.2.F',4,"An induction motor produces torque only when the rotor turns:",
  "Slower than synchronous speed",["Exactly at synchronous speed","Faster than synchronous speed","In a vacuum"],"Slip is required.")
H('110.d.2.G',3,"When slip grows in an induction motor, rotor current generally:",
  "Rises",["Drops to zero","Stays the same","Reverses"],"More slip, more induced current.")
H('110.d.2.G',4,"High rotor reactance at starting tends to make the starting power factor:",
  "Low",["Perfect","Unity","Negative"],"Reactance lowers power factor.")
H('110.d.2.H',3,"Percent slip is found by dividing the speed difference by the:",
  "Synchronous speed",["Frame size","Voltage","Wire gauge"],"Slip = (Ns - N)/Ns.")
H('110.d.2.H',4,"A motor with synchronous speed 1800 rpm and full-load speed 1740 rpm has a percent slip of:",
  "3.3 percent",["6.6 percent","0.33 percent","33 percent"],"60/1800 = 0.033.")
H('110.d.2.I',3,"To reverse a three-phase induction motor, swap any:",
  "Two of the three line leads",["One ground wire","All three leads","The nameplate"],"Swapping two reverses rotation.")
H('110.d.2.I',4,"Swapping two supply leads reverses the motor because it reverses the:",
  "Phase sequence",["Frequency","Voltage level","Frame size"],"Sequence sets direction.")
H('110.d.2.J',3,"A synchronous motor runs at a speed that is:",
  "Locked to the supply frequency",["Dependent on load slip","Random","Always zero"],"No slip at steady state.")
H('110.d.2.J',4,"Compared with induction motors, synchronous motors can be used to:",
  "Correct a lagging power factor",["Reduce frame size to zero","Run without any supply","Avoid all maintenance"],"They can supply leading current.")
H('110.d.2.K',3,"Armature reaction in a DC motor is the effect of armature current on the:",
  "Main field flux",["Wire insulation","Bearing grease","Nameplate size"],"It distorts the field.")
H('110.d.2.K',4,"At the instant a DC motor starts, armature current is very high because:",
  "There is no counter EMF yet",["The brushes are new","The voltage is lowest","The load is zero"],"No back EMF at standstill.")
H('110.d.2.L',3,"The rotation of a DC motor is reversed by changing the polarity of the:",
  "Armature or the field, but not both",["Frame","Nameplate","Fuse"],"Reverse one only.")
H('110.d.2.L',4,"If both armature and field polarity are reversed at once, the DC motor will:",
  "Keep turning in the same direction",["Reverse direction","Stop forever","Overspeed immediately"],"Two reversals cancel.")
H('110.d.2.M',3,"A series DC motor is known for very high:",
  "Starting torque",["Speed regulation","Frequency","Power factor"],"Series field carries load current.")
H('110.d.2.M',4,"A shunt DC motor is well suited to jobs needing:",
  "Nearly constant speed",["Extreme starting torque","No field winding","Variable frequency"],"Shunt speed is stable.")
H('110.d.2.N',3,"A dual-voltage motor can be connected to:",
  "Either of two supply voltages by changing leads",["Only one voltage ever","Any voltage at all","DC and AC at once"],"Winding groups reconnect.")
H('110.d.2.N',4,"A motor wired for the higher of its two voltages draws:",
  "Less current than at the lower voltage",["More current","The same current","No current"],"Higher voltage, lower current.")
H('110.d.2.O',3,"Motor lead markings such as T1 through T9 are used to:",
  "Identify winding ends for connections",["Show the price","Rate the paint","Label bearings"],"Leads are numbered.")
H('110.d.2.O',4,"An ohmmeter is useful for finding motor connections because it can:",
  "Show which leads belong to the same winding",["Create voltage","Measure rpm","Set the frequency"],"Continuity identifies windings.")
H('110.d.2.P',3,"The NEC requires motor circuits to have overload protection to guard against:",
  "Sustained overcurrent that heats the windings",["Spelling errors","Loud noise","Dim lights"],"Overloads damage motors.")
H('110.d.2.P',4,"Motor branch-circuit short-circuit protection is generally allowed to be sized:",
  "Higher than the motor running current to permit starting",["Exactly at running current","At zero amperes","Lower than running current"],"Starting current is higher.")
H('110.d.3.A',3,"A main purpose of grounding electrical systems is to:",
  "Limit voltage and provide a path for fault current",["Increase the cost","Raise the voltage","Slow down breakers"],"Grounding improves safety.")
H('110.d.3.A',4,"The NEC rules on grounding are found mainly in Article:",
  "250",["90","310","430"],"Article 250 covers grounding and bonding.")
H('110.d.3.B',3,"A short circuit is an unintended path between:",
  "Two conductors of different potential",["A wire and its insulation","A box and a cover","A switch and a lamp"],"Conductors touch each other.")
H('110.d.3.B',4,"A ground fault occurs when a live conductor touches:",
  "Grounded metal or earth",["Another live phase","A plastic cover","Open air"],"Ground fault goes to ground.")
H('110.d.3.C',3,"In NEC terms, a grounded conductor is one that is:",
  "Intentionally connected to earth",["Always bare","Never carrying current","Colored red"],"Usually the neutral.")
H('110.d.3.C',4,"Bonding in NEC terms means:",
  "Joining metal parts to form a conductive path",["Gluing insulation","Painting metal","Cooling wire"],"Bonding keeps parts at equal potential.")
H('110.d.3.D',3,"System grounding connects the:",
  "Electrical system's current-carrying conductor to earth",["Metal enclosures to each other only","Lamps to switches","Meters to poles"],"It stabilizes system voltage.")
H('110.d.3.D',4,"Equipment grounding is intended mainly to:",
  "Keep metal parts safe and carry fault current",["Reduce wire size","Raise system voltage","Light the room"],"It helps breakers trip.")
H('110.d.3.E',3,"The grounding electrode conductor size is chosen from the NEC based on the size of the:",
  "Largest service-entrance conductor",["Fixture","Building height","Panel color"],"Table 250.66 uses service size.")
H('110.d.3.E',4,"A larger service-entrance conductor will generally require a grounding electrode conductor that is:",
  "Larger, up to the maximum allowed",["Smaller always","Unrelated","Removed"],"Tables step up with size.")
H('110.d.3.F',3,"An NEC requirement for a grounding electrode conductor is that it be:",
  "Properly protected and continuous or spliced only as allowed",["Hidden under paint","Left loose","Made of string"],"Installation must be secure.")
H('110.d.3.F',4,"A grounding electrode conductor is typically attached to the electrode with:",
  "An approved clamp or exothermic weld",["Electrical tape","Staples","Plain knots"],"Connections must be approved.")
H('110.d.3.G',3,"A grounding electrode system can include a metal underground water pipe and:",
  "Concrete-encased electrodes",["A mailbox","Roof shingles","A TV antenna"],"Several electrodes are bonded together.")
H('110.d.3.G',4,"When several electrodes are present at a building, the NEC generally requires them to be:",
  "Bonded together into one system",["Kept isolated","Painted differently","Removed"],"They form a grounding electrode system.")
H('110.d.3.H',3,"A made electrode such as a ground rod must meet a limit on its:",
  "Resistance to earth",["Paint color","Brand","Weight in tons"],"Resistance is limited, or a second electrode is added.")
H('110.d.3.H',4,"If a single rod's resistance to earth exceeds 25 ohms, the NEC calls for:",
  "An additional electrode",["Removing the rod","A thicker rod only","No action"],"Add a second electrode.")
H('110.d.3.I',3,"The size of an equipment grounding conductor depends on the rating of the:",
  "Overcurrent device protecting the circuit",["Light bulb","Wall color","Floor type"],"Table 250.122 is used.")
H('110.d.3.I',4,"For a circuit protected by a 20-ampere breaker, the minimum copper equipment grounding conductor is generally:",
  "12 AWG",["8 AWG","2 AWG","18 AWG"],"NEC Table 250.122 lists 12 AWG for 20 A.")
H('110.d.3.J',3,"The main bonding jumper connects the grounded service conductor to the:",
  "Service equipment enclosure",["Roof","Light switch","Water heater only"],"It bonds neutral to enclosure at service.")
H('110.d.3.J',4,"The system bonding jumper is used in a:",
  "Separately derived system",["Battery flashlight","Doorbell","Garage door"],"It bonds the derived neutral to ground.")
H('110.d.3.K',3,"When a service has multiple disconnects in separate enclosures, the main bonding jumper is sized by the:",
  "Largest service-entrance conductor per NEC table",["Panel's paint","Number of windows","Building age"],"Size follows the service conductors.")
H('110.d.3.K',4,"For parallel service conductors, the bonding jumper size is based on the:",
  "Total area of the parallel conductors in each set combined",["Smallest wire only","Cable color","Meter brand"],"Combined area is used.")
H('110.d.3.L',3,"Metal raceways and enclosures are bonded to ensure:",
  "Fault current has a low-impedance path back to the source",["Higher resistance","Lower safety","Less noise only"],"A solid path lets breakers trip.")
H('110.d.3.L',4,"Locknuts and bonding bushings on service raceways help:",
  "Maintain bonding continuity",["Cool the wire","Seal paint","Hold labels"],"Service raceways need reliable bonding.")
H('110.d.3.M',3,"Effective grounding means the path from circuit conductors to ground has low enough impedance to:",
  "Let the overcurrent device clear the fault quickly",["Raise voltage","Avoid inspection","Weaken breakers"],"Fault current must be large enough.")
H('110.d.3.M',4,"A high-impedance ground path during a fault can leave exposed metal:",
  "Energized at a dangerous voltage",["Cold","Painted","Grounded perfectly"],"Poor path leaves hazard.")
H('110.d.3.N',3,"The neutral conductor in a grounded system serves to carry:",
  "Unbalanced current back to the source",["All line current","No current","Only ground faults"],"It carries the imbalance.")
H('110.d.3.N',4,"In a balanced three-phase wye system with equal loads, neutral current is approximately:",
  "Zero",["Double","Triple","Infinite"],"Balanced loads cancel.")
H('110.d.3.O',3,"A separately derived system, such as a transformer secondary, is grounded at:",
  "Its source or first disconnect",["Every outlet","The roof","The driveway"],"One point of grounding is made.")
H('110.d.3.O',4,"Grounding a separately derived system at more than one point can cause:",
  "Objectionable current on the grounding paths",["Lower cost","Cooler transformers","Brighter lamps"],"Parallel neutral paths are a problem.")
H('110.d.3.P',3,"Grounding at more than one building supplied by a feeder is done by installing at each building a:",
  "Grounding electrode system",["Neon sign","Carpet","Paint stripe"],"Each building needs electrodes.")
H('110.d.3.P',4,"A building fed by a feeder with a separate equipment grounding conductor generally has the neutral and ground:",
  "Kept separate at the second building",["Joined at the second building","Eliminated","Bonded to plumbing only"],"Avoid parallel neutral paths.")
H('110.d.3.Q',3,"For a high-impedance grounded system, the grounding impedance limits ground-fault:",
  "Current",["Voltage drop of lamps","Wall thickness","Panel color"],"It limits fault current.")
H('110.d.3.Q',4,"An ungrounded system is often used where a first ground fault should:",
  "Not shut down the process",["Cause an explosion","Add cost","Remove all power instantly"],"Continuity of operation.")
H('110.d.4.A',3,"Power benders for conduit are used mainly for:",
  "Larger conduit sizes",["Wire stripping","Painting","Cutting tape"],"They bend large sizes.")
H('110.d.4.A',4,"Using a hydraulic bender helps the user:",
  "Make bends with less manual effort",["Skip measuring","Avoid safety rules","Bend glass"],"Hydraulics supply force.")
H('110.d.4.B',3,"The part of a bender that forms the curve in the conduit is the:",
  "Shoe",["Frame leg only","Handle grip","Foot pedal cord"],"Shoe defines radius.")
H('110.d.4.B',4,"On a hydraulic bender, the ram pushes the conduit against the:",
  "Bending shoe",["Floor plate","Wire reel","Tape measure"],"The ram drives the bend.")
H('110.d.4.C',3,"To avoid wasting conduit, an electrician should:",
  "Measure carefully and plan bends before cutting",["Cut first and guess","Bend at random","Use extra on every run"],"Planning reduces scrap.")
H('110.d.4.C',4,"Marking a conduit with the take-up and bend locations helps:",
  "Prevent mistakes that waste material",["Create more scrap","Delay the job","Hide the bends"],"Careful marks save conduit.")
H('110.d.4.D',3,"A saddle bend is used when conduit must:",
  "Cross over an obstruction",["Run straight","End in a box","Be buried"],"Saddles clear obstacles.")
H('110.d.4.D',4,"Parallel bends in side-by-side conduits keep the runs:",
  "Evenly spaced and neat",["Touching","Random","Crossed"],"Parallel bends match.")
H('110.d.4.E',3,"The NEC limits the number of bends in one run between pull points to:",
  "360 degrees total",["90 degrees total","900 degrees total","No limit"],"Four quarter bends maximum.")
H('110.d.4.E',4,"The NEC sets minimum bending radius so that conduit:",
  "Is not damaged and conductors can be pulled",["Looks tall","Costs more","Is lighter"],"Radius tables protect wires.")
H('110.d.4.F',3,"The developed length of a bend is the length of:",
  "Conduit used along the curve",["The whole building","The bender handle","The pulling rope"],"It is the arc length.")
H('110.d.4.F',4,"Gain in a 90-degree bend is the amount by which the bend:",
  "Shortens the overall run compared with square corners",["Adds extra length","Equals zero always","Changes voltage"],"Gain saves conduit.")
H('110.d.4.G',3,"Conduit that has a kink should be:",
  "Replaced because the kink damages the pull path",["Pulled anyway","Painted","Taped"],"Kinks harm wires.")
H('110.d.4.G',4,"To modify an existing bend, the electrician may:",
  "Reshape it carefully with the proper bender without kinking",["Hammer it flat","Cut it with a torch","Heat it with a lighter"],"Use correct tools.")
H('110.d.5.A',3,"A common nonmetallic box material is:",
  "PVC or other plastic",["Cast iron only","Glass","Wood"],"Nonmetallic boxes are plastic.")
H('110.d.5.A',4,"A metal box must be grounded, while a nonmetallic box generally does not need:",
  "To be bonded itself",["Any cover","Any conductors","Any support"],"Plastic is nonconductive.")
H('110.d.5.B',3,"Box fill depends on the number and size of the conductors, devices, and:",
  "Clamps and fittings inside the box",["Paint","Floor type","Ceiling height"],"Fill counts volume allowances.")
H('110.d.5.B',4,"A box holding more conductors than the NEC allows can cause:",
  "Overheating from crowding",["Better cooling","Lower voltage","Faster pulling"],"Overfill is unsafe.")
H('110.d.5.C',3,"NEC box volume allowances are given in:",
  "Cubic inches per conductor size",["Square feet","Miles","Pounds"],"Table 314.16(B).")
H('110.d.5.C',4,"A 14 AWG conductor requires how much volume allowance in a box?",
  "2.00 cubic inches",["5.00 cubic inches","0.25 cubic inches","8.00 cubic inches"],"Table lists 2.00 for 14 AWG.")
H('110.d.5.D',3,"Boxes must be installed so they are:",
  "Securely supported and accessible",["Buried in concrete without access","Loose in the wall","Hidden behind paneling"],"Boxes must be reachable.")
H('110.d.5.D',4,"A box installed in a masonry wall is typically supported by:",
  "Anchors suited to masonry",["Drywall tape","Hot glue","Spray foam"],"Anchors give strength.")
H('110.d.5.E',3,"The NEC sets minimum pull-box size for large conductors so wires can be:",
  "Pulled and bent without damage",["Hidden","Cut shorter","Colored"],"Sizing reduces stress.")
H('110.d.5.E',4,"For a straight pull of conductors 4 AWG or larger, the box length must be at least how many times the largest raceway trade diameter?",
  "Eight",["Two","Four","Twenty"],"Straight pull is 8 times.")
H('110.d.5.F',3,"The radius rule in a pull box prevents conductors from being:",
  "Bent too sharply",["Painted","Labeled","Cooled"],"Minimum bending radius protects insulation.")
H('110.d.5.F',4,"Under the radius rule, large cable should not be forced into a corner that is:",
  "Tighter than the permitted bend radius",["Painted white","Wider than the cable","Labeled in black"],"Bend radius is limited.")
H('110.d.5.G',3,"Heavy luminaires must be supported by a box that is:",
  "Listed for the weight",["Any size","Painted","Open"],"Boxes carry loads.")
H('110.d.5.G',4,"A ceiling fan box is different from a basic light box because it is:",
  "Rated to carry the fan weight and motion",["Smaller","Made of paper","Open on one side"],"Fan boxes are listed for fans.")
H('110.d.5.H',3,"A conduit body, like an LB, is used to:",
  "Provide a pulling access point at a bend",["Replace the panel","Cut wire","Measure voltage"],"Conduit bodies give access.")
H('110.d.5.H',4,"A Type FS box is commonly used with:",
  "Surface-mounted rigid or EMT conduit",["Flat cable only","Underground cable","Plumbing pipe"],"FS boxes are for conduit.")
H('110.d.5.I',3,"Fittings used with boxes should be:",
  "Listed for the conduit and box type",["Any scrap","Painted","Homemade"],"Match the fitting.")
H('110.d.5.I',4,"Connectors that enter a box through a knockout must be secured with a:",
  "Locknut or equivalent",["Rubber band","Tape","String"],"Locknuts hold fittings.")
H('110.d.5.J',3,"Boxes and fittings in hazardous areas must be:",
  "Listed for the classified location",["Plastic only","Open","Unmarked"],"Hazardous locations need listed gear.")
H('110.d.5.J',4,"Explosionproof fittings are required to:",
  "Contain an internal explosion and cool escaping gases",["Look decorative","Vent sparks outward","Be lightweight"],"They stop flame propagation.")
H('110.d.5.K',3,"Selecting a box includes checking the number of conductors, device type, and the:",
  "Location conditions",["Brand of coffee","Date","Owner's age"],"Environment matters.")
H('110.d.5.K',4,"A box in a damp location should be:",
  "Listed for damp or wet use",["Open","Unlisted","Cardboard"],"Moisture needs ratings.")
H('110.d.5.L',3,"Box supports include bar hangers, brackets, and:",
  "Threaded rod supports",["String","Tape","Glue sticks"],"Hangers hold boxes.")
H('110.d.5.L',4,"A ceiling box between joists is often supported by a:",
  "Adjustable bar hanger",["Paper clip","Rope","Drywall"],"Bar hangers span joists.")
H('110.d.6.A',3,"Conductors can be installed in conduit by pushing them or by:",
  "Pulling them with a pull line",["Throwing them","Heating them","Taping to a vehicle"],"Pull lines are standard.")
H('110.d.6.A',4,"For long runs with large conductors, pulling is usually done with a:",
  "Mechanical puller",["Bare hand","Paper rope","Kite string"],"Machines reduce effort.")
H('110.d.6.B',3,"Before a cable pull, the crew should:",
  "Plan the route, equipment, and communication",["Start without a plan","Skip safety","Block the exits"],"Planning prevents damage.")
H('110.d.6.B',4,"A pulling plan should identify the maximum allowed:",
  "Pulling tension",["Wall color","Truck brand","Paint finish"],"Tension limits protect cable.")
H('110.d.6.C',3,"Heavy cable reels are moved safely using:",
  "Proper lifting equipment and reel trailers",["Bare hands","Rope only","Rolling down stairs"],"Reels are heavy.")
H('110.d.6.C',4,"When rolling a reel, the correct direction is the one shown by the:",
  "Arrow on the reel flange",["Color of the cable","Manufacturer logo","Driver's choice"],"Arrows prevent loosening.")
H('110.d.6.D',3,"Reel stands and spindles allow the reel to:",
  "Turn freely as cable is pulled",["Stand still","Burn","Lock"],"Free turning prevents tangles.")
H('110.d.6.D',4,"The reel should be positioned so the cable pays off the:",
  "Top of the reel in line with the conduit",["Bottom in a heap","Side onto the floor","Center out"],"Alignment prevents kinks.")
H('110.d.6.E',3,"A mandrel is pulled through a conduit to:",
  "Check for obstructions or damage",["Add voltage","Color the conduit","Seal the end"],"A mandrel proves the path.")
H('110.d.6.E',4,"A swab or brush is used to:",
  "Clean debris and moisture from conduit",["Paint the inside","Cut wires","Bend the pipe"],"Clean conduit protects insulation.")
H('110.d.6.F',3,"A pull line can be installed in conduit by blowing a lightweight line with:",
  "Compressed air and a foam piston",["Water pumps","Hammer blows","Electric shock"],"A piston carries the line.")
H('110.d.6.F',4,"A pull line for a heavy cable should be strong enough for the expected:",
  "Pulling tension",["Color","Weight of the box","Age of the building"],"Rope rating matters.")
H('110.d.6.G',3,"A power fish tape system helps to:",
  "Push or pull a line through long conduit runs",["Cut wire","Paint walls","Measure voltage"],"Power fish tapes help routing.")
H('110.d.6.G',4,"Before using a power fish tape, check that the conduit is:",
  "De-energized and free of live conductors",["Full of wires","Wet","Locked"],"Avoid contact with live parts.")
H('110.d.6.H',3,"The end of a conductor is prepared for pulling by attaching a:",
  "Pulling eye or grip",["Label","Plug","Lamp"],"Grips connect to the line.")
H('110.d.6.H',4,"A basket grip on a cable end holds by:",
  "Tightening as tension increases",["Melting","Glue","Magnets"],"Mesh squeezes the cable.")
H('110.d.6.I',3,"A cable puller can be powered by an electric motor or:",
  "Hydraulics",["A candle","A wind-up key","A flashlight"],"Pullers vary.")
H('110.d.6.I',4,"A tugger is a small puller commonly used to:",
  "Pull cable through conduit",["Cut conduit","Test voltage","Weld pipe"],"Tuggers pull.")
H('110.d.6.J',3,"High-force cable pulling is used for:",
  "Large, heavy cables in long runs",["Lamp cords","Phone wires","Doorbell wires"],"Heavy loads need force.")
H('110.d.6.J',4,"During a high-force pull, a tension monitor helps to:",
  "Stay below the cable's maximum pulling tension",["Add speed","Change color","Reduce voltage"],"Monitors prevent overload.")
H('110.d.6.K',3,"In a vertical conduit run, conductors are supported to prevent:",
  "Their own weight from stressing the cable",["Cooling","Rain","Painting"],"NEC requires support.")
H('110.d.6.K',4,"Cable supports in a vertical run are installed at intervals set by the:",
  "NEC based on conductor size",["Installer's mood","Truck brand","Color"],"Spacing is code-based.")
H('110.d.6.L',3,"In a cable tray, power conductors are often laid in rather than:",
  "Pulled through a closed pipe",["Laid down flat","Placed loose","Tied with tape"],"Tray cable is laid in.")
H('110.d.6.L',4,"When pulling cable in a tray, rollers are used to:",
  "Reduce friction and protect the jacket",["Add friction","Cut cable","Melt cable"],"Rollers ease pulls.")
H('110.d.6.M',3,"Good communication during a pull helps the crew to:",
  "Coordinate speed and stop if there is a problem",["Ignore each other","Work in silence","Skip checking"],"Radios help.")
H('110.d.6.M',4,"If someone at the feed end sees a jam, they should:",
  "Call out to stop the pull immediately",["Pull harder","Wait silently","Leave the area"],"Stop before damage.")
H('110.d.6.N',3,"Pulling tension is calculated using the cable weight, the coefficient of friction, and the:",
  "Length and bends of the run",["Color","Brand","Noise"],"Geometry affects tension.")
H('110.d.6.N',4,"Adding more bends to a conduit run makes the pulling tension generally:",
  "Climb",["Fall to zero","Stay unchanged","Become negative"],"Bends multiply tension.")
H('110.d.7.A',3,"A cable tray assembly is made of straight sections, fittings, and:",
  "Supports",["Paint cans","Drain pipes","Gutters"],"Tray needs supports.")
H('110.d.7.A',4,"Cable tray rungs or solid bottoms support the:",
  "Cables laid in the tray",["Ceiling tiles","Light fixtures only","Water pipes"],"Trays carry cable.")
H('110.d.7.B',3,"Cable trays are hung from the ceiling using:",
  "Threaded rod hangers",["String","Tape","Glue"],"Rods suspend trays.")
H('110.d.7.B',4,"Hanger spacing for a cable tray depends on the tray's:",
  "Load rating and span",["Color","Brand of paint","Owner's name"],"Load limits spacing.")
H('110.d.7.C',3,"Cable enters and leaves a tray through a:",
  "Conduit or cable fitting at the side or bottom",["Wall mirror","Window","Door hinge"],"Entry fittings protect cable.")
H('110.d.7.C',4,"A bushing or fitting at a tray entrance protects the cable from:",
  "Sharp edges",["Rain only","Cool air","Sunlight"],"Edges can cut jackets.")
H('110.d.7.D',3,"A horizontal elbow in a tray changes the run:",
  "Direction in the same plane",["Voltage","Color","Weight"],"Elbows turn.")
H('110.d.7.D',4,"A vertical tray fitting is used to move the tray:",
  "Up or down between levels",["Sideways only","Underground","Into the wall"],"Vertical elbows change elevation.")
H('110.d.7.E',3,"NEMA standards for cable trays cover tray:",
  "Load classes and dimensions",["Paint brands","Song lists","Shoe sizes"],"NEMA VE1 sets classes.")
H('110.d.7.E',4,"The NEMA load rating of a tray tells the:",
  "Weight per foot it can support on a given span",["Cost per mile","Age","Color of the tray"],"Ratings guide selection.")
H('110.d.7.F',3,"NEC rules for cable tray require that cables be:",
  "Of types permitted for tray use",["Any wire","Bare wire only","Painted"],"Use tray-rated cable.")
H('110.d.7.F',4,"Where cable tray passes through a wall, the opening must be:",
  "Firestopped as required",["Left open","Sealed with tape","Covered with paper"],"Firestopping maintains rating.")
H('110.d.7.G',3,"A metal cable tray can serve as an equipment grounding conductor if it is:",
  "Listed and properly bonded across joints",["Painted","Unlisted","Loose"],"Continuity matters.")
H('110.d.7.G',4,"Bonding jumpers are installed across tray expansion joints to:",
  "Keep electrical continuity",["Allow breaks","Add noise","Cool the cable"],"Jumpers bridge gaps.")
H('110.d.7.H',3,"Working drawings show cable tray fittings with:",
  "Symbols and dimensions",["Photographs of lunch","Songs","Recipes"],"Drawings use symbols.")
H('110.d.7.H',4,"A drawing note for tray elevation helps installers know the:",
  "Height above finished floor",["Color","Brand","Cost of lunch"],"Elevation is shown on plan.")
H('110.d.7.I',3,"To size a tray, the installer adds up the cross-sectional area of the cables and compares it with the tray's:",
  "Allowable fill area",["Color","Weight in grams","Age"],"NEC limits fill.")
H('110.d.7.I',4,"If cables fill more than the allowable area in a tray, the installer should:",
  "Choose a wider or additional tray",["Squash the cables","Ignore the limit","Remove the cover"],"Fill rules protect cable.")
H('110.d.7.J',3,"Rollers and sheaves in a tray reduce friction and:",
  "Protect cable from damage during a pull",["Cause scraping","Add tension","Slow the job"],"They guide cable.")
H('110.d.7.J',4,"The size of a sheave should match the cable's:",
  "Minimum bending radius",["Color","Price","Brand"],"Sheaves avoid sharp bends.")
H('110.d.7.K',3,"Rollers are placed in a tray at changes of direction and:",
  "At regular intervals along straight runs",["Nowhere","Only at the ends","In the roof"],"Intervals keep cable off tray.")
H('110.d.7.K',4,"A roller should be placed at the outside of a horizontal turn to:",
  "Guide the cable around the curve",["Stop the pull","Cut cable","Hold the lights"],"Rollers guide turns.")
H('110.d.8.A',3,"A good conductor termination is one that is:",
  "Clean, tight, and made with proper tools",["Loose","Dirty","Taped over"],"Quality connections prevent heat.")
H('110.d.8.A',4,"A poor termination typically causes:",
  "Heat at the connection",["Cool wire","Lower resistance","Extra voltage"],"Resistance makes heat.")
H('110.d.8.B',3,"Before a termination, the cable end is prepared by:",
  "Removing insulation to the proper length",["Cutting the conductor in half","Painting it","Soaking it"],"Strip to length.")
H('110.d.8.B',4,"When stripping insulation, the installer must avoid:",
  "Nicking the conductor",["Using strippers","Wearing gloves","Measuring"],"Nicks weaken wire.")
H('110.d.8.C',3,"A lug is installed on a conductor by:",
  "Inserting the stripped end and securing it",["Gluing","Taping","Knotting"],"Lugs connect wire to equipment.")
H('110.d.8.C',4,"Large lugs are commonly attached to conductors using a:",
  "Compression crimp tool",["Hammer","Saw","Pencil"],"Crimping makes a solid joint.")
H('110.d.8.D',3,"Training cable at a termination point means:",
  "Shaping it neatly to reach its terminal without strain",["Cutting it short","Painting it","Burying it"],"Neat routing reduces stress.")
H('110.d.8.D',4,"When training cable, the installer should maintain the correct:",
  "Bending radius",["Wall color","Brand","Voltage of lamps"],"Avoid sharp bends.")
H('110.d.8.E',3,"The NEC requires terminations to be rated for the conductor:",
  "Temperature and material",["Color only","Brand only","Smell"],"Terminals have ratings.")
H('110.d.8.E',4,"If a terminal is rated for copper only, the installer must not use:",
  "Aluminum conductors",["Copper conductors","Any wire","Insulated wire"],"Material compatibility.")
H('110.d.8.F',3,"Mechanical stress on a termination can:",
  "Loosen the connection over time",["Improve it","Cool it","Seal it"],"Stress damages joints.")
H('110.d.8.F',4,"Pulling the cable tight against a lug may:",
  "Strain the termination and cause failure",["Strengthen it","Reduce current","Remove heat"],"Slack prevents strain.")
H('110.d.8.G',3,"Bolting a lug requires torque that is:",
  "Specified by the manufacturer",["Random","Maximum possible","Zero"],"Use the specified torque.")
H('110.d.8.G',4,"Using a torque wrench on lug bolts prevents:",
  "Loose or overtightened connections",["Correct torque","Cooling","Paint damage"],"Both extremes cause failure.")
H('110.d.8.H',3,"Crimping squeezes a connector onto a conductor to form a:",
  "Solid mechanical and electrical connection",["Weak joint","Hole","Spring"],"Crimps hold tightly.")
H('110.d.8.H',4,"The crimp die must match the connector and the:",
  "Conductor size",["Truck","Voltage of the sun","Paint"],"Dies are sized.")
H('110.d.8.I',3,"Choosing a lug requires knowing the conductor size and the:",
  "Conductor material",["Color of the room","Date","Lunch menu"],"Material matters.")
H('110.d.8.I',4,"A lug marked AL9CU is suitable for:",
  "Both aluminum and copper conductors",["Aluminum only","Copper only","Neither"],"AL9CU is dual-rated.")
H('110.d.8.J',3,"A splice joins two conductors to make:",
  "One continuous conductor",["A switch","A fuse","A motor"],"Splices join.")
H('110.d.8.J',4,"Splices must be made in an approved:",
  "Box or enclosure that stays accessible",["Wall cavity","Soil","Buried vault with no access"],"Splices need access.")
H('110.d.8.K',3,"A hydraulic crimper is typically used for:",
  "Large lugs and connectors",["Small lamp wire","Phone wire","Doorbell wire"],"Hydraulics give force.")
H('110.d.8.K',4,"Before crimping, the tool should be checked for the correct:",
  "Die and pressure setting",["Paint color","Handle color","Brand sticker"],"Proper setup is essential.")
H('110.d.9.A',3,"A commercial building with high electrical demand is typically served by a:",
  "Three-phase service",["Battery pack","Single outlet","Solar toy"],"Three-phase suits large loads.")
H('110.d.9.A',4,"Industrial plants often have services at a higher voltage such as:",
  "480 volts",["12 volts","5 volts","1 volt"],"Larger systems use 480 V.")
H('110.d.9.B',3,"A one-line diagram shows the service as:",
  "A single line representing the entire system",["A photo","Song lyrics","A recipe"],"One-lines simplify.")
H('110.d.9.B',4,"On a one-line diagram, the main disconnect appears:",
  "Between the utility source and the distribution equipment",["After the lights","On the roof","Underground only"],"It is at the service entrance.")
H('110.d.9.C',3,"Service-entrance equipment is selected based on calculated:",
  "Load",["Color","Height","Brand of paint"],"Load determines size.")
H('110.d.9.C',4,"A 400-ampere, 480-volt, three-phase service can supply about how many kVA?",
  "332 kVA",["192 kVA","48 kVA","900 kVA"],"1.732 x 480 x 400 = 332,000 VA.")
H('110.d.9.D',3,"The NEC article that covers services is:",
  "Article 230",["Article 1","Article 90 only","Article 700"],"Services are Article 230.")
H('110.d.9.D',4,"The NEC requires each service to have a:",
  "Disconnecting means",["Doorbell","Mailbox","Fountain"],"A disconnect is required.")
H('110.d.9.E',3,"A main disconnect switch is used to:",
  "Shut off all power to the building",["Light a room","Cool a motor","Pump water"],"Main switch removes service.")
H('110.d.9.E',4,"Panelboards contain overcurrent devices for the:",
  "Branch circuits and feeders",["Roof","Pipes","Windows"],"Panels distribute power.")
H('110.d.9.F',3,"To plan a panel, the electrician lists the connected loads and the:",
  "Number of circuits needed",["Wall colors","Window sizes","Paint brands"],"Circuits follow loads.")
H('110.d.9.F',4,"A continuous load is one expected to run for:",
  "Three hours or more",["Ten seconds","One minute","Two minutes"],"NEC defines it as 3 hours.")
H('110.d.9.G',3,"Service grounding connects the system to the earth through:",
  "A grounding electrode system",["A mailbox","A shingle","A light bulb"],"Electrodes tie to earth.")
H('110.d.9.G',4,"At the service, the neutral and the equipment grounding conductors are:",
  "Bonded together",["Kept separate forever","Removed","Cut"],"Bonded at the main.")
H('110.d.9.H',3,"The NEC requires GFCI protection in locations such as:",
  "Bathrooms and rooftops",["Bedroom closets","Hallway ceilings","Attic floors"],"Wet or hazardous areas.")
H('110.d.9.H',4,"A GFCI trips when it senses a difference of about how many milliamperes between hot and neutral?",
  "5 milliamperes",["500 milliamperes","50 amperes","5 amperes"],"Class A trips near 5 mA.")
H('110.d.9.I',3,"A single-phase three-wire service supplies 120 volts and:",
  "240 volts",["480 volts","12 volts","1000 volts"],"Residential split-phase.")
H('110.d.9.I',4,"The neutral in a single-phase three-wire system carries:",
  "Only the unbalanced current between legs",["All current","No current ever","Double current"],"Balanced legs cancel.")
H('110.d.9.J',3,"A wye three-phase service has a:",
  "Neutral point where the three windings join",["Triangle shape with no neutral","Single winding","Battery"],"Wye has a center point.")
H('110.d.9.J',4,"A 208Y/120-volt wye system provides 120 volts line-to-neutral and 208 volts:",
  "Line-to-line",["Neutral-to-ground","Ground-to-pipe","Motor-to-wall"],"208 = 120 x 1.732.")
H('110.d.10.A',3,"Overcurrent protection is needed to prevent:",
  "Damage from excessive current",["Nice lighting","Better sound","Lower bills"],"Protects wires and equipment.")
H('110.d.10.A',4,"Without overcurrent protection, a short circuit could cause:",
  "Fire or equipment destruction",["Cooler wires","Longer life","Better efficiency"],"Large currents heat wires.")
H('110.d.10.B',3,"The interrupting rating of a breaker is the maximum:",
  "Fault current it can safely interrupt",["Weight","Voltage of the sun","Color"],"Rating must exceed available fault current.")
H('110.d.10.B',4,"A fuse's ampere rating is the current it can carry:",
  "Continuously without opening",["For one second only","Only on Sundays","With no load"],"Ratings are continuous.")
H('110.d.10.C',3,"A thermal-magnetic circuit breaker trips on overloads by means of a:",
  "Bimetal strip that heats and bends",["Magnet only","Spring only","Fuse link"],"Thermal element handles overloads.")
H('110.d.10.C',4,"The magnetic part of a breaker responds to:",
  "Large short-circuit currents instantly",["Slow overloads only","Voltage dips","Cold weather"],"Magnetic trip is fast.")
H('110.d.10.D',3,"Selecting an overcurrent device requires considering the conductor ampacity and the:",
  "Load type",["Paint","Time of day","Owner's mood"],"Match device to load.")
H('110.d.10.D',4,"A breaker protecting a 12 AWG copper branch circuit is limited by the NEC to:",
  "20 amperes",["60 amperes","100 amperes","200 amperes"],"12 AWG small-conductor rule.")
H('110.d.10.E',3,"In a motor circuit, a dual-element time-delay fuse lets the circuit tolerate:",
  "Brief motor-starting surges without opening",["Instant opening always","No overload","Reverse flow"],"Dual-element handles motors.")
H('110.d.10.E',4,"A single-element fuse differs from a time-delay fuse in that it:",
  "Opens quickly on overloads",["Never opens","Resists surges","Is rechargeable"],"No delay.")
H('110.d.10.F',3,"GFCIs can save lives by detecting:",
  "Small leakage currents to ground",["Light levels","Sound","Temperature of wire"],"They detect ground faults.")
H('110.d.10.F',4,"A GFCI protects people but does not protect against:",
  "Shock from touching both hot and neutral",["Ground faults","Leakage to ground","Wet-area shock"],"Hot-to-neutral contact is not detected.")
H('110.d.10.G',3,"Available short-circuit current at a point depends mainly on the source and the circuit:",
  "Impedance",["Color","Length of tape","Weight"],"Lower impedance, higher current.")
H('110.d.10.G',4,"If a transformer secondary is 480 V with an impedance of 0.1 ohm per phase, the approximate fault current is:",
  "2,771 amperes",["48 amperes","4,800 amperes","27 amperes"],"(480/1.732)/0.1 is about 2,771.")
H('110.d.10.H',3,"A breaker that trips repeatedly should be:",
  "Investigated for an overload or fault",["Taped closed","Replaced with a larger one","Ignored"],"Find the cause.")
H('110.d.10.H',4,"Routine maintenance on breakers includes:",
  "Exercising them and checking connections",["Painting them","Soaking them","Hammering them"],"Maintenance prevents failure.")
H('110.d.11.A',3,"A contactor is used to:",
  "Switch a power circuit using a control signal",["Measure voltage","Cool wires","Cut conductors"],"Contactors switch loads.")
H('110.d.11.A',4,"A relay differs from a contactor mainly because a relay is generally used for:",
  "Lower-current control switching",["Heavy motor loads","Welding","Power plants"],"Relays are for light loads.")
H('110.d.11.B',3,"To select a contactor, you must know the load voltage, current, and the:",
  "Coil voltage",["Wall color","Truck","Height"],"Coil must match control.")
H('110.d.11.B',4,"A contactor for a motor must be rated for the motor's:",
  "Horsepower or full-load current",["Paint","Brand","Color"],"Ratings match the load.")
H('110.d.11.C',3,"A mechanical contactor closes its contacts when its coil is:",
  "Energized",["Cold","Painted","Open"],"Coil pulls contacts closed.")
H('110.d.11.C',4,"When a contactor coil is de-energized, a spring:",
  "Opens the contacts",["Closes the contacts","Burns the coil","Reverses flow"],"Springs return contacts.")
H('110.d.11.D',3,"A solid-state contactor switches with:",
  "Semiconductor devices instead of moving contacts",["Moving blades","Springs","Water"],"No moving parts.")
H('110.d.11.D',4,"One advantage of a solid-state contactor is:",
  "Silent, fast switching",["Loud clicking","Contact bounce","Visible arcing"],"No arcing.")
H('110.d.11.E',3,"The NEC requires contactors and relays to be installed:",
  "In suitable enclosures and as listed",["Anywhere","Unlabeled","Outdoors unprotected"],"Follow listing.")
H('110.d.11.E',4,"Contactors installed outdoors need an enclosure rated for:",
  "Weather exposure",["Shade","Silence","Paint"],"Outdoor ratings.")
H('110.d.11.F',3,"A lighting contactor is often used to control:",
  "Large groups of lights at once",["One doorbell","Phones","Radios"],"Lighting contactors switch banks.")
H('110.d.11.F',4,"Lighting contactors can be operated by a time clock or a:",
  "Photocell",["Hammer","Radio brand","Pen"],"Automated controls.")
H('110.d.11.G',3,"An overload relay protects a motor from:",
  "Prolonged overcurrent",["Light","Paint","Sound"],"Heater elements sense current.")
H('110.d.11.G',4,"When an overload relay trips, it opens the:",
  "Control circuit to drop out the contactor",["Water line","Lights","Phone line"],"It breaks the coil circuit.")
H('110.d.11.H',3,"A simple start-stop control circuit uses a normally closed stop button and a normally open:",
  "Start button",["Fuse","Lamp","Ground"],"Start and stop pair.")
H('110.d.11.H',4,"A holding contact in a start-stop circuit keeps the coil energized after the start button is:",
  "Released",["Pressed","Removed from the wall","Painted"],"Seal-in contact.")
H('110.d.11.I',3,"A control circuit can be tested by checking for voltage across the:",
  "Coil when the start button is pressed",["Wall","Floor","Window"],"Coil voltage proves control.")
H('110.d.11.I',4,"A coil that does not pull in when voltage is present is probably:",
  "Defective",["Working normally","Overfilled","Painted"],"Replace the coil.")
H('110.d.12.A',3,"Light enters the eye through the:",
  "Pupil",["Heel","Lens cap","Knee"],"The pupil admits light.")
H('110.d.12.A',4,"The part of the eye that senses light and sends signals to the brain is the:",
  "Retina",["Iris","Cornea only","Eyelid"],"Retina has rods and cones.")
H('110.d.12.B',3,"Light is a form of:",
  "Electromagnetic energy",["Sound energy","Chemical fuel","Heat only"],"Visible radiation.")
H('110.d.12.B',4,"The unit used to measure illumination on a surface is the:",
  "Footcandle",["Ohm","Ampere","Hertz"],"Footcandles measure light level.")
H('110.d.12.C',3,"LED lamps are known for their:",
  "Long life and efficiency",["Short life","High heat","High cost of power"],"LEDs are efficient.")
H('110.d.12.C',4,"Compared with incandescent lamps, fluorescent lamps are more:",
  "Efficient, but need a ballast",["Heat-producing","Short-lived","Silent without parts"],"Ballasts regulate current.")
H('110.d.12.D',3,"When replacing a lamp, always check that the new lamp has the correct:",
  "Wattage and base type",["Color of the box","Brand of tape","Name"],"Match ratings.")
H('110.d.12.D',4,"Before changing a lamp in a fixture, the circuit should be:",
  "Turned off",["Left on","Overloaded","Painted"],"Safety first.")
H('110.d.12.E',3,"Recessed lighting fixtures are installed:",
  "Into the ceiling so the housing is hidden",["On top of the roof","Under the floor","On the street"],"Recessed are flush.")
H('110.d.12.E',4,"A fixture marked IC may be installed:",
  "In direct contact with insulation",["Only in the open","Under water","Where insulation is not allowed"],"Insulation contact rated.")

# ---------- 127.111 HVAC and Refrigeration ----------
H('111.d.1.A',3,"The basic purpose of an HVAC system is to control indoor:",
  "Temperature, humidity, and air quality",["Wall color","Floor texture","Furniture style"],"HVAC conditions air.")
H('111.d.1.A',4,"The three basic HVAC functions are heating, cooling, and:",
  "Ventilation",["Painting","Sanding","Plumbing"],"Ventilation refreshes air.")
H('111.d.1.B',3,"The Clean Air Act affects HVAC technicians because it limits:",
  "The release of refrigerants",["Paint colors","Thermostat styles","Duct shapes"],"Refrigerants harm ozone.")
H('111.d.1.B',4,"Technicians who handle refrigerants must be:",
  "Certified under EPA rules",["Unlicensed","Under age","Unpaid"],"EPA 608 certification.")
H('111.d.1.C',3,"A drawing that shows duct sizes and layout is a:",
  "Mechanical plan",["Landscape plan","Menu","Poster"],"Mechanical plans show HVAC.")
H('111.d.1.C',4,"An equipment schedule lists the HVAC units with their:",
  "Capacities and specifications",["Colors of walls","Names of owners","Songs"],"Schedules tabulate data.")
H('111.d.2.A',3,"Length in the English system is measured in feet and inches, while the International System uses:",
  "Meters",["Gallons","Pounds","Degrees"],"Meter is SI.")
H('111.d.2.A',4,"A pound in the English system corresponds to what unit in the SI system for mass?",
  "Kilogram",["Meter","Liter","Joule"],"Mass uses kg.")
H('111.d.2.B',3,"To convert 12,000 BTU per hour into tons of cooling, divide by:",
  "12,000",["120","1,200,000","24"],"One ton equals 12,000 BTU/h.")
H('111.d.2.B',4,"A room measures 10 ft by 12 ft by 8 ft. Its volume is:",
  "960 cubic feet",["120 cubic feet","30 cubic feet","96 cubic feet"],"10 x 12 x 8 = 960.")
H('111.d.2.C',3,"Water freezes at 0 degrees Celsius, which is how many degrees Fahrenheit?",
  "32",["0","100","212"],"Freezing is 32 F.")
H('111.d.2.C',4,"A temperature of 68 degrees Fahrenheit is how many degrees Celsius?",
  "20",["68","36","40"],"(68-32) x 5/9 = 20.")
H('111.d.3.A',3,"When installing refrigerant piping, the lines should be kept:",
  "Clean and dry inside",["Wet","Dirty","Open to the air"],"Contamination damages systems.")
H('111.d.3.A',4,"Moisture inside a refrigerant line can cause:",
  "Acid formation and freeze-ups",["Better cooling","Extra capacity","Lower pressure"],"Moisture harms systems.")
H('111.d.3.B',3,"Copper tubing for refrigerant is cut with a:",
  "Tubing cutter",["Hacksaw only","Axe","Chisel"],"Cutters make square cuts.")
H('111.d.3.B',4,"Soft copper tubing is bent using a:",
  "Tubing bender or spring",["Hammer","Torch alone","Vise only"],"Benders prevent kinks.")
H('111.d.3.C',3,"A flare fitting connects tubing by:",
  "Flaring the tube end against a seat",["Gluing","Welding","Taping"],"Flare seals metal-to-metal.")
H('111.d.3.C',4,"Before flaring a tube, slip the flare nut on:",
  "First, over the tube end",["After flaring","Never","On the compressor"],"Nut must be on first.")
H('111.d.3.D',3,"Refrigerant pipes are supported with:",
  "Hangers or clamps at proper spacing",["Tape","Rope","Glue"],"Supports prevent sagging.")
H('111.d.3.D',4,"Refrigerant lines should be supported so vibration does not:",
  "Crack the tubing at fittings",["Cool the room","Reduce noise","Add efficiency"],"Vibration causes leaks.")
H('111.d.3.E',3,"Piping that carries refrigerant to an outdoor unit is called the:",
  "Line set",["Gas stove","Drain pan","Filter"],"Line sets connect units.")
H('111.d.3.E',4,"Insulation on the larger suction line prevents:",
  "Sweating and heat gain",["Cooling","Pressure drop to zero","Corrosion of the roof"],"Cold line sweats.")
H('111.d.3.F',3,"After installation, a refrigerant system is often tested with:",
  "Dry nitrogen under pressure",["Water","Oxygen","Air with oil"],"Nitrogen is safe and dry.")
H('111.d.3.F',4,"Pressure testing with oxygen is dangerous because oxygen can:",
  "React violently with oil",["Cool the line","Seal leaks","Clean tubing"],"Never use oxygen.")
H('111.d.3.G',3,"Which plastic pipe is typically used to carry away air-conditioner condensate?",
  "PVC",["Cast iron","Lead","Glass"],"PVC is common for drains.")
H('111.d.3.G',4,"CPVC differs from PVC in that CPVC can withstand:",
  "Higher temperatures",["Lower temperatures only","No water","Gas only"],"CPVC is heat-rated.")
H('111.d.3.H',3,"Plastic pipe is joined using primer and:",
  "Solvent cement",["Tape","Rope","Wax"],"Cement bonds plastic.")
H('111.d.3.H',4,"After applying solvent cement, the joint should be held for a few seconds to:",
  "Let it start to set",["Add water","Heat it","Paint it"],"Hold to prevent push-out.")
H('111.d.4.A',3,"A common soldering heat source for copper tubing is a:",
  "Propane torch",["Candle","Hair dryer","Lighter"],"Torches heat copper.")
H('111.d.4.A',4,"A technician soldering near a wall should use a:",
  "Heat shield to protect combustible surfaces",["Larger flame","Plastic cover","Cloth"],"Prevent fires.")
H('111.d.4.B',3,"Before soldering, tubing ends are cleaned with:",
  "Sand cloth or a fitting brush",["Paint","Oil","Water only"],"Clean metal bonds.")
H('111.d.4.B',4,"Flux is applied to the cleaned joint to:",
  "Prevent oxidation and help solder flow",["Make it dirty","Cool the pipe","Hide the joint"],"Flux aids wetting.")
H('111.d.4.C',3,"Soft solder melts at a temperature:",
  "Below 840 degrees Fahrenheit",["Above 1500 degrees","Above 2000 degrees","At 0 degrees"],"Brazing starts above 840 F.")
H('111.d.4.C',4,"Lead-free solder is required on:",
  "Potable water lines",["Refrigerant lines only","Gas lines","Drain lines"],"Safe water systems.")
H('111.d.4.D',3,"When soldering, heat the:",
  "Fitting and tube evenly, then touch solder to the joint",["Solder directly","Flame on solder","Wall only"],"Capillary action draws solder.")
H('111.d.4.D',4,"Solder is drawn into the joint by:",
  "Capillary action",["Gravity only","Wind","Magnetism"],"Capillary pulls it in.")
H('111.d.4.E',3,"Brazing is done with a torch that burns oxygen and:",
  "Acetylene",["Nitrogen","Argon","Water"],"Oxy-acetylene is common.")
H('111.d.4.E',4,"Before lighting an oxy-acetylene torch, the technician should check for:",
  "Leaks at fittings and hoses",["Color of tanks","Time","Weather forecast"],"Leak checks prevent fires.")
H('111.d.4.F',3,"For brazing, tube and fittings must be cleaned and:",
  "Fitted snugly with no gaps",["Loose","Wet","Greased"],"Gap affects flow.")
H('111.d.4.F',4,"Brazing flux is generally needed with filler metals when joining:",
  "Copper to brass or steel",["Copper to copper with phos-copper","Nothing","Glass"],"Copper to copper with BCuP needs none.")
H('111.d.4.G',3,"Brazing filler metals melt at temperatures:",
  "Above 840 degrees Fahrenheit",["Below 200 degrees","At 100 degrees","At room temperature"],"Brazing is high-temp.")
H('111.d.4.G',4,"A silver-bearing filler such as BAg is often used when brazing:",
  "Dissimilar metals",["Plastic","Rubber","Wood"],"Silver bonds mixed metals.")
H('111.d.4.H',3,"When brazing, move the flame so the fitting heats:",
  "Evenly until the filler flows into the joint",["Unevenly","Not at all","Only the filler"],"Even heat is key.")
H('111.d.4.H',4,"The joint is ready for filler metal when the flux:",
  "Turns clear and the copper glows a dull cherry red",["Turns black","Boils over","Is wet"],"Visual cue.")
H('111.d.4.I',3,"An inert gas used to purge tubing while brazing is:",
  "Nitrogen",["Oxygen","Acetylene","Propane"],"Nitrogen prevents scale.")
H('111.d.4.I',4,"Flowing nitrogen inside copper during brazing prevents:",
  "Oxide scale inside the tube",["Cooling","Leaks outside","Flame"],"Purge keeps tube clean.")
H('111.d.4.J',3,"Black steel pipe is an example of:",
  "Ferrous metal pipe",["Plastic pipe","Copper pipe","Glass pipe"],"Ferrous has iron.")
H('111.d.4.J',4,"Galvanized pipe is steel pipe coated with:",
  "Zinc",["Copper","Lead","Plastic"],"Zinc resists rust.")
H('111.d.4.K',3,"Pipe size is expressed as nominal size, which refers to the pipe's approximate:",
  "Inside diameter",["Weight","Length","Color"],"Nominal size is by ID.")
H('111.d.4.K',4,"A pipe thread gauge or tape measure helps find the pipe's:",
  "Outside diameter and thread size",["Cost","Color","Age"],"Measure to size.")
H('111.d.4.L',3,"A malleable iron fitting used to change direction by 90 degrees is a:",
  "Elbow",["Union only","Cap","Plug"],"Elbows turn.")
H('111.d.4.L',4,"A union is used to:",
  "Join pipe so it can be disconnected later",["Seal a pipe forever","Change direction","Reduce pressure"],"Unions allow service.")
H('111.d.4.M',3,"After cutting steel pipe, the inside edge is smoothed with a:",
  "Reamer",["Hammer","Torch","Sander for wood"],"Reaming removes burrs.")
H('111.d.4.M',4,"Threads are cut on pipe using a:",
  "Die stock",["Level","Square","Tape"],"Dies cut threads.")
H('111.d.4.N',3,"Pipe threads should be sealed with:",
  "Joint compound or thread tape",["Paint","Glue only","Nothing"],"Sealant stops leaks.")
H('111.d.4.N',4,"When tightening threaded pipe, use a:",
  "Pipe wrench",["Hammer","Screwdriver","Pliers only"],"Wrench gives grip.")
H('111.d.4.O',3,"When installing pipe runs, supports should be spaced to prevent:",
  "Sagging",["Cooling","Painting","Shortening"],"Spacing holds the load.")
H('111.d.4.O',4,"Pipe runs must allow for thermal:",
  "Expansion",["Color","Brand","Sound"],"Heat expands pipe.")
H('111.d.4.P',3,"Grooved piping is joined with:",
  "Couplings that engage grooves",["Torch","Glue","Soldering"],"Grooved couplings clamp.")
H('111.d.4.P',4,"A grooved joint includes a gasket that:",
  "Seals the connection",["Cuts the pipe","Melts","Heats the pipe"],"Gasket seals.")
H('111.d.5.A',3,"Electrical power reaches buildings through:",
  "Transmission and distribution lines",["Water pipes","Gas lines","Roads"],"Utilities distribute power.")
H('111.d.5.A',4,"A transformer on a pole is used to:",
  "Step voltage down for customers",["Increase energy","Store heat","Pump water"],"Transformers adjust voltage.")
H('111.d.5.B',3,"If voltage stays the same and resistance goes up, current:",
  "Goes down",["Goes up","Stays at zero","Doubles"],"Ohm's law.")
H('111.d.5.B',4,"Electrical power is the product of voltage and:",
  "Current",["Resistance","Length","Time"],"P = V x I.")
H('111.d.5.C',3,"A 24-volt circuit with 8 ohms of resistance carries a current of:",
  "3 amperes",["192 amperes","16 amperes","0.33 amperes"],"24/8 = 3.")
H('111.d.5.C',4,"A circuit has 5 amperes through 6 ohms. The voltage is:",
  "30 volts",["11 volts","1.2 volts","0.83 volts"],"5 x 6 = 30.")
H('111.d.5.D',3,"A 10-ampere, 120-volt load consumes:",
  "1,200 watts",["12 watts","130 watts","110 watts"],"120 x 10.")
H('111.d.5.D',4,"A 2,400-watt heater on 240 volts draws:",
  "10 amperes",["100 amperes","1 ampere","0.1 amperes"],"2400/240 = 10.")
H('111.d.5.E',3,"In a parallel circuit, if one load is removed, the others:",
  "Continue to operate",["All stop","Burn out","Reverse"],"Branches are independent.")
H('111.d.5.E',4,"Total resistance of two 6-ohm resistors in series is:",
  "12 ohms",["3 ohms","6 ohms","36 ohms"],"Series adds.")
H('111.d.5.F',3,"A capacitor in an HVAC motor circuit helps the motor to:",
  "Start or run efficiently",["Cool the pipe","Seal ducts","Filter air"],"Capacitors give phase shift.")
H('111.d.5.F',4,"A contactor in an air conditioner switches the:",
  "Compressor and fan power",["Thermostat only","Drain line","Refrigerant"],"Contactor switches loads.")
H('111.d.5.G',3,"Before servicing electrical equipment, the technician should:",
  "Disconnect and lock out power",["Work live","Wet the hands","Remove a ground"],"Lockout first.")
H('111.d.5.G',4,"A technician must verify power is off by using a:",
  "Voltmeter or tester",["Ruler","Level","Stopwatch"],"Test before touching.")
H('111.d.5.H',3,"A multimeter set to measure resistance should be used only on a circuit that is:",
  "De-energized",["Live","Wet","Loaded"],"Ohm tests need power off.")
H('111.d.5.H',4,"A clamp-on ammeter measures current by:",
  "Sensing the magnetic field around one conductor",["Cutting the wire","Touching both terminals","Measuring resistance"],"Clamp around one wire.")
H('111.d.5.I',3,"On a wiring diagram, a coil symbol represents a:",
  "Relay or contactor coil",["Fan","Filter","Duct"],"Symbol identification.")
H('111.d.5.I',4,"A ladder diagram shows control circuits with power rails on the:",
  "Left and right sides",["Top only","Floor","Wall"],"Ladder rails.")
H('111.d.6.A',3,"Heat naturally flows from a:",
  "Warmer object to a cooler one",["Cooler to warmer","Nowhere","Up only"],"Heat moves downhill.")
H('111.d.6.A',4,"In a cooling system, the evaporator:",
  "Absorbs heat from the indoor air",["Gives off heat to the outside","Cools the compressor oil","Filters dust"],"Evaporator absorbs heat.")
H('111.d.6.B',3,"For a given refrigerant, raising the pressure also raises the:",
  "Boiling (saturation) temperature",["Weight","Color","Smell"],"Pressure-temperature relationship.")
H('111.d.6.B',4,"A pressure-temperature chart lets a technician find the:",
  "Saturation temperature at a measured pressure",["Cost of refrigerant","Weight of the unit","Height of the duct"],"PT charts link pressure and temperature.")
H('111.d.6.C',3,"A manifold gauge set measures:",
  "Refrigerant pressures",["Voltage","Humidity","Wind speed"],"Gauges show pressure.")
H('111.d.6.C',4,"Under supervision, a thermometer clamped on a line reads:",
  "Line temperature",["Pressure","Voltage","Humidity"],"Used for superheat checks.")
H('111.d.6.D',3,"Refrigerants must be recovered rather than vented because venting:",
  "Is illegal and harms the environment",["Is cheaper","Is encouraged","Improves cooling"],"EPA rules.")
H('111.d.6.D',4,"Refrigerant is removed from a system into a certified:",
  "Recovery cylinder",["Bucket","Paper bag","Sink"],"Recovery uses approved tanks.")
H('111.d.6.E',3,"The component that raises refrigerant pressure and moves it through the system is the:",
  "Compressor",["Filter drier","Thermostat","Duct"],"Compressor is the pump.")
H('111.d.6.E',4,"The condenser:",
  "Releases heat from the refrigerant to the outside",["Absorbs indoor heat","Stores oil","Filters air"],"Condensers reject heat.")
H('111.d.6.F',3,"A filter drier in a refrigeration line removes:",
  "Moisture and particles",["Heat","Voltage","Sound"],"Driers protect the system.")
H('111.d.6.F',4,"A sight glass on a liquid line lets the technician see:",
  "Whether liquid refrigerant is flowing",["The temperature","The voltage","The room color"],"Bubbles can show low charge.")
H('111.d.6.G',3,"A thermostat controls a cooling system by:",
  "Turning equipment on and off to hold a set temperature",["Making noise","Changing the color","Moving ducts"],"Thermostats cycle equipment.")
H('111.d.6.G',4,"A low-pressure switch shuts off the compressor to protect it when pressure is too:",
  "Low",["High only","Neutral","Hot"],"Protects against loss of charge.")
H('111.d.6.H',3,"Refrigeration piping must be sloped and sized to ensure:",
  "Oil returns to the compressor",["Water stays out","Noise","Heat loss"],"Oil return is critical.")
H('111.d.6.H',4,"A trap in a vertical suction line helps:",
  "Carry oil up toward the compressor",["Stop flow","Hold water","Create noise"],"Traps aid oil return.")
H('111.d.7.A',3,"The three methods of heat transfer are conduction, convection, and:",
  "Radiation",["Insulation","Ventilation","Evaporation"],"Radiation is heat by waves.")
H('111.d.7.A',4,"Feeling heat from the sun on your skin is an example of:",
  "Radiation",["Conduction","Convection","Condensation"],"Solar energy radiates.")
H('111.d.7.B',3,"Combustion requires fuel, oxygen, and:",
  "Heat",["Water","Ice","Wind alone"],"Fire triangle.")
H('111.d.7.B',4,"A dangerous by-product of incomplete combustion is:",
  "Carbon monoxide",["Oxygen","Nitrogen","Water vapor"],"CO is toxic.")
H('111.d.7.C',3,"Fuels used for heating include natural gas, propane, and:",
  "Fuel oil",["Water","Sand","Air"],"Common fuels.")
H('111.d.7.C',4,"Propane is stored as a liquid under:",
  "Pressure in a tank",["Vacuum","Water","Sand"],"LP is pressurized.")
H('111.d.7.D',3,"An induced draft furnace uses a fan to:",
  "Pull flue gases through the heat exchanger",["Cool the room","Fill the tank","Pump water"],"Inducer moves gases.")
H('111.d.7.D',4,"A heat exchanger separates combustion gases from the:",
  "Air being delivered to the building",["Gas supply","Thermostat","Filter"],"Keeps gases out of the house.")
H('111.d.7.E',3,"When installing a furnace, the installer must provide proper clearances and:",
  "Venting and combustion air",["Paint","Ornaments","Flowers"],"Safe operation.")
H('111.d.7.E',4,"Clearance to combustibles is listed on the furnace:",
  "Data plate",["Cover art","Box","Filter"],"Follow the label.")
H('111.d.7.F',3,"In a gas furnace, the gas valve controls the flow of gas to the:",
  "Burners",["Filter","Duct","Thermostat"],"Valve opens on call for heat.")
H('111.d.7.F',4,"A flame sensor proves to the control that:",
  "The burners have lit",["The room is cool","The filter is clean","The duct is open"],"Prevents gas flow without flame.")
H('111.d.7.G',3,"A manometer is used to measure:",
  "Gas pressure",["Voltage","Humidity","Weight"],"Manometers read low pressures.")
H('111.d.7.G',4,"Natural gas manifold pressure is commonly set near how many inches of water column?",
  "3.5",["35","0.35","350"],"Typical NG manifold is 3.5 in. w.c.")
H('111.d.7.H',3,"An oil furnace burns fuel oil sprayed through a:",
  "Nozzle",["Filter only","Duct","Coil"],"Atomizing nozzle.")
H('111.d.7.H',4,"The oil burner ignites the spray with a:",
  "Spark from electrodes",["Lighter","Match","Candle"],"Electrodes ignite oil.")
H('111.d.7.I',3,"Preventive furnace maintenance includes replacing the:",
  "Air filter",["Windows","Roof","Floor"],"Dirty filters hurt flow.")
H('111.d.7.I',4,"Cleaning burners and checking the flue helps ensure:",
  "Safe, efficient combustion",["Higher noise","Lower safety","Poor draft"],"Regular maintenance.")
H('111.d.8.A',3,"In a forced-air system, a blower moves air through:",
  "Supply and return ducts",["Water pipes","Gas lines","Electric wire"],"Ducts carry air.")
H('111.d.8.A',4,"Air pressure in the supply duct is generally:",
  "Positive compared with the room",["Negative","Zero","Random"],"Supply is pressurized.")
H('111.d.8.B',3,"A centrifugal fan moves air by:",
  "Throwing it outward from a rotating wheel",["Pushing straight with a prop","Burning it","Heating it"],"Centrifugal action.")
H('111.d.8.B',4,"A propeller fan is best for moving:",
  "Large volumes at low pressure",["Air through long ducts","Water","Gas"],"Propeller fans are low pressure.")
H('111.d.8.C',3,"A duct system that branches from a main trunk is a:",
  "Trunk-and-branch system",["Radiator","Boiler","Tank"],"Common design.")
H('111.d.8.C',4,"Flexible duct is useful for:",
  "Short connections to registers",["Underground mains","Fuel lines","Flue gas"],"Flex is easy to route.")
H('111.d.8.D',3,"Metal duct sections are joined with seams and then sealed with:",
  "Mastic or approved tape",["Paper","Wax","Water"],"Sealing prevents leaks.")
H('111.d.8.D',4,"Fiberboard duct is cut using a:",
  "Special knife and straightedge",["Torch","Hammer","Axe"],"Fiberboard is knife-cut.")
H('111.d.8.E',3,"A transition in a duct system is used to change:",
  "Duct size or shape",["Voltage","Fuel","Color"],"Transitions adapt ducts.")
H('111.d.8.E',4,"A smooth transition reduces air:",
  "Turbulence and pressure loss",["Flow rate","Capacity","Noise"],"Gradual changes help.")
H('111.d.8.F',3,"A diffuser delivers air into a room and:",
  "Spreads it to avoid drafts",["Removes air","Heats gas","Stores water"],"Diffusers distribute.")
H('111.d.8.F',4,"Return grilles are generally placed where they can:",
  "Draw room air back to the system",["Blow air out","Heat water","Hold dust"],"Returns collect air.")
H('111.d.8.G',3,"A damper in a duct is used to:",
  "Regulate or stop air flow",["Make noise","Heat air","Filter dust"],"Dampers control airflow.")
H('111.d.8.G',4,"A fire damper closes automatically when:",
  "Heat melts its fusible link",["The thermostat is set","Lights turn on","Fan stops"],"Prevents fire spread.")
H('111.d.8.H',3,"Duct insulation helps:",
  "Reduce heat loss or gain",["Raise noise","Lower strength","Block light"],"Insulation saves energy.")
H('111.d.8.H',4,"A vapor barrier on cold duct insulation prevents:",
  "Condensation on or in the insulation",["Heat flow","Fire","Rust of fans"],"Barriers block moisture.")
H('111.d.8.I',3,"An anemometer is used to measure:",
  "Air velocity",["Voltage","Gas pressure","Temperature of metal"],"Anemometers measure speed.")
H('111.d.8.I',4,"A pitot tube with a manometer measures air:",
  "Velocity pressure in a duct",["Sound","Humidity","Weight"],"Used for air balancing.")
H('111.d.8.J',3,"To find the air volume in a duct, multiply the velocity by the duct's:",
  "Cross-sectional area",["Color","Length","Weight"],"CFM = velocity x area.")
H('111.d.8.J',4,"Air moving at 600 feet per minute through a 2-square-foot duct delivers:",
  "1,200 cubic feet per minute",["300 cfm","602 cfm","12 cfm"],"600 x 2 = 1200.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_19.jsonl'))

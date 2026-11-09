import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('127.', 1097, own='cte_20.jsonl')
def H(code, d, q, right, wrong, e):
    return B.hand(code, d, q, right, wrong, e)

# ---------- 127.112 HVAC/R Technology II ----------
H('112.d.1.A',3,"A packaged rooftop unit differs from a split system because all its components are in:",
  "One cabinet",["Separate rooms","Underground vaults","Two buildings"],"Packaged units are self-contained.")
H('112.d.1.A',4,"A commercial chilled-water system cools air by circulating:",
  "Cold water to coils in air handlers",["Hot gas to the roof","Steam to the walls","Sand through ducts"],"Chilled water carries cooling.")
H('112.d.1.B',3,"A large office tower is most likely served by a:",
  "Central chilled-water plant",["Window unit per floor","Single portable fan","Fireplace"],"Large buildings use central plants.")
H('112.d.1.B',4,"A small strip-mall store is commonly cooled by a:",
  "Rooftop packaged unit",["Cooling tower plant","Steam boiler loop","Absorption chiller for the whole block"],"Small stores use rooftop units.")
H('112.d.1.C',3,"Commercial air system capacity is usually stated in:",
  "Tons or BTU per hour",["Gallons per mile","Volts per foot","Pounds per inch"],"Capacity is cooling output.")
H('112.d.1.C',4,"A 5-ton unit provides how many BTU per hour of cooling?",
  "60,000",["5,000","12,000","600,000"],"5 x 12,000 = 60,000.")
H('112.d.2.A',3,"Complete combustion of natural gas produces carbon dioxide and:",
  "Water vapor",["Soot","Carbon monoxide","Sulfur"],"Complete burn yields CO2 and H2O.")
H('112.d.2.A',4,"Incomplete combustion is a hazard mainly because it creates:",
  "Carbon monoxide",["Extra oxygen","Cooler flames","More nitrogen"],"CO is poisonous.")
H('112.d.2.B',3,"Flue gas from a gas furnace contains mostly nitrogen, carbon dioxide, and:",
  "Water vapor",["Fresh oxygen only","Ammonia","Chlorine"],"Flue gas composition.")
H('112.d.2.B',4,"Flue gases are vented outdoors to keep them from:",
  "Entering the occupied space",["Cooling the burners","Raising voltage","Wetting the duct"],"Venting protects occupants.")
H('112.d.2.C',3,"A furnace vent system includes a vent pipe, connector, and a:",
  "Termination cap",["Fuse box","Humidifier","Condensate pump only"],"Terminations finish the vent.")
H('112.d.2.C',4,"A draft hood on a natural-draft furnace helps by:",
  "Relieving excess draft and back-drafts",["Heating the room","Filtering air","Storing fuel"],"The hood stabilizes draft.")
H('112.d.2.D',3,"When selecting a vent for a furnace, the installer follows the:",
  "Manufacturer instructions and fuel gas code",["Color of the furnace","Neighbor's advice","Lowest price"],"Codes govern venting.")
H('112.d.2.D',4,"A Category I vent is used with furnaces that operate with:",
  "Non-positive vent pressure and flue gas above dew point",["Condensing flue gases","Positive pressure at all times","No flue at all"],"Category definitions.")
H('112.d.2.E',3,"Proper combustion in a gas burner is judged by flame color, which should be mostly:",
  "Blue",["Yellow and sooty","Black","Red"],"Blue flame is efficient.")
H('112.d.2.E',4,"A burner with a lazy yellow flame often needs more:",
  "Primary air",["Gas pressure","Fuel oil","Water"],"Yellow flame means too little air.")
H('112.d.2.F',3,"A condensing furnace vent is usually made of:",
  "PVC plastic",["Single-wall galvanized steel","Cast iron","Aluminum foil"],"Cool flue gas allows plastic.")
H('112.d.2.F',4,"Venting for a high-efficiency furnace must be sloped to:",
  "Drain condensate back to the furnace",["Fill the vent","Pool water","Heat the attic"],"Condensate drains properly.")
H('112.d.2.G',3,"A barometric damper on a flue pipe controls:",
  "Draft",["Voltage","Fuel pressure","Humidity only"],"Dampers regulate draft.")
H('112.d.2.G',4,"A draft inducer is a fan that:",
  "Pulls flue gases through the heat exchanger",["Cools the room","Pumps refrigerant","Mixes fuel"],"Inducers create draft.")
H('112.d.2.H',3,"Vent size for a gas appliance is chosen from tables based on input rating and vent:",
  "Height and lateral length",["Paint color","Brand","Location of thermostat"],"Tables set sizes.")
H('112.d.2.H',4,"A vent that is too large for a small appliance can cause:",
  "Condensation and poor draft",["Faster heating","Stronger draft","Lower pressure"],"Oversized vents cool gases.")
H('112.d.2.I',3,"A heat anticipator in a thermostat is set to match the:",
  "Current draw of the control circuit",["Room color","Fuel type","Duct size"],"Anticipator matches amps.")
H('112.d.2.I',4,"Setting the anticipator too low can cause the furnace to:",
  "Short cycle",["Run constantly","Stay off","Overheat the thermostat"],"Wrong setting changes cycling.")
H('112.d.3.A',3,"A closed hydronic system recirculates:",
  "The same water in a sealed loop",["Fresh water each time","Steam only","Air"],"Closed means sealed.")
H('112.d.3.A',4,"The unit of heat energy commonly used in hydronic work is the:",
  "BTU",["Volt","Newton","Lumen"],"BTU measures heat.")
H('112.d.3.B',3,"Major parts of a hot-water heating system include the boiler, pump, and:",
  "Radiators or baseboard units",["Spark plugs","Compressor","Condenser coil"],"Emitters deliver heat.")
H('112.d.3.B',4,"The expansion tank in a hot-water system absorbs:",
  "Water volume changes as it heats",["Gas leaks","Voltage spikes","Sound"],"Tanks cushion expansion.")
H('112.d.3.C',3,"The circulator pump in a hot-water system moves:",
  "Heated water through the piping",["Fuel to the burner","Air through filters","Refrigerant"],"Pumps circulate water.")
H('112.d.3.C',4,"An air vent on a hydronic loop removes:",
  "Trapped air that blocks flow",["Fuel","Water","Heat only"],"Air stops circulation.")
H('112.d.3.D',3,"Before working on a hot boiler, a technician should let the system:",
  "Cool and relieve pressure",["Run hotter","Stay under pressure","Be filled with air"],"Scalding is a hazard.")
H('112.d.3.D',4,"The relief valve on a boiler discharges to prevent:",
  "Dangerous over-pressure",["Low flow","Cold rooms","Wet floors"],"Safety valve.")
H('112.d.3.E',3,"To start a hot-water system after service, the technician first makes sure the system is:",
  "Filled with water and purged of air",["Empty","Wet with oil","Disconnected"],"Never fire a dry boiler.")
H('112.d.3.E',4,"A boiler aquastat controls:",
  "Water temperature",["Gas pressure","Air speed","Duct size"],"It holds temperature setpoint.")
H('112.d.3.F',3,"Low-pressure boilers operate at no more than:",
  "15 psi for steam",["150 psi","500 psi","1000 psi"],"Low-pressure steam limit.")
H('112.d.3.F',4,"Before blowing down a low-water cutoff, the technician must make sure that:",
  "Everyone clear of the discharge and procedures are followed",["The boiler is hot and unattended","All valves are closed","The burner is firing high"],"Safe procedure.")
H('112.d.3.G',3,"Common hydronic piping layouts include series loop, one-pipe, and:",
  "Two-pipe systems",["Zero-pipe","Seven-pipe","Open-top"],"Standard layouts.")
H('112.d.3.G',4,"A primary-secondary piping arrangement lets boilers and loads:",
  "Have independent flow",["Share the same pump only","Use the same gas line","Run without water"],"Hydraulic separation.")
H('112.d.3.H',3,"The pressure difference across a circulator pump is read with:",
  "Two gauges, one at each side",["A thermometer","An ohmmeter","A level"],"Differential pressure.")
H('112.d.3.H',4,"If the pressure drop across a pump is zero, the pump may be:",
  "Not moving water",["Working perfectly","Too small","Overheated"],"Zero differential suggests no flow.")
H('112.d.3.I',3,"Heating water flow in gallons per minute is found by dividing the heat load by 500 times the:",
  "Temperature drop",["Pipe length","Pump color","Boiler weight"],"GPM = BTUH / (500 x delta T).")
H('112.d.3.I',4,"A 60,000 BTUH load with a 20-degree drop needs how many gpm?",
  "6",["60","3","12"],"60,000 / (500 x 20) = 6.")
H('112.d.3.J',3,"A pump is selected by matching the flow rate needed to the:",
  "Head loss of the system",["Pipe color","Fuel brand","Building age"],"Pump curve meets system curve.")
H('112.d.3.J',4,"A pump curve plots head against:",
  "Flow rate",["Voltage","Temperature","Noise"],"Pump curves show head vs flow.")
H('112.d.4.A',3,"Very low indoor humidity in winter can cause:",
  "Dry skin and static shocks",["Mold on windows","Condensation","Stronger breathing"],"Dry air is uncomfortable.")
H('112.d.4.A',4,"Too much indoor humidity can promote:",
  "Mold growth",["Static shocks","Dry throats","Cracked skin"],"Moisture grows mold.")
H('112.d.4.B',3,"A bypass humidifier uses air from the furnace to:",
  "Evaporate water into the airstream",["Cool the burner","Filter dust","Recover refrigerant"],"Bypass types add moisture.")
H('112.d.4.B',4,"A steam humidifier makes moisture by:",
  "Boiling water with electric elements",["Spraying cold water","Freezing water","Condensing gas"],"Steam humidifiers boil water.")
H('112.d.4.C',3,"The water supply to a humidifier should include a:",
  "Shutoff valve and drain",["Light bulb","Thermostat","Spark plug"],"Service valves needed.")
H('112.d.4.C',4,"Mineral buildup in a humidifier is cleaned to restore:",
  "Proper output",["Fuel supply","Voltage","Duct size"],"Scale lowers performance.")
H('112.d.4.D',3,"A MERV rating describes how well a filter:",
  "Captures particles",["Cools air","Dries air","Heats air"],"Higher MERV catches more.")
H('112.d.4.D',4,"Compared with a MERV 4 filter, a MERV 13 filter captures:",
  "Smaller particles",["Only large lint","Less dust","Nothing"],"Higher ratings capture smaller particles.")
H('112.d.4.E',3,"When installing a furnace filter, the airflow arrow should point:",
  "Toward the blower",["Away from the blower","Toward the room","Toward the ceiling"],"Arrow shows flow direction.")
H('112.d.4.E',4,"A clogged filter reduces airflow and can cause the coil to:",
  "Freeze up",["Run hotter","Cool faster","Save energy"],"Low airflow freezes coils.")
H('112.d.4.F',3,"A manometer measuring across a filter shows the filter's:",
  "Pressure drop",["Cost","Age","Color"],"Static pressure drop.")
H('112.d.4.F',4,"If the pressure drop across a filter climbs well above its rated value, the filter should be:",
  "Changed",["Painted","Ignored","Moved"],"High drop means loaded.")
H('112.d.4.G',3,"An accessory that improves indoor air by killing microbes on a coil is a:",
  "UV light",["Fuse","Thermostat","Gas valve"],"UV disinfects surfaces.")
H('112.d.4.G',4,"An energy recovery ventilator transfers heat and moisture between:",
  "Exhaust and incoming fresh air",["Fuel and air","Water and oil","Two rooms"],"ERVs reclaim energy.")
H('112.d.4.H',3,"Before cleaning an electronic air cleaner, the technician should:",
  "Turn off the power",["Add water while on","Open the fuel line","Touch the plates live"],"High-voltage cell.")
H('112.d.4.H',4,"Collector plates of an electronic air cleaner are usually washed with:",
  "Mild detergent and water",["Gasoline","Bleach on live cells","Sand"],"Gentle cleaning.")
H('112.d.5.A',3,"A common refrigerant leak detector uses a:",
  "Soap bubble solution",["Ruler","Hammer","Glue gun"],"Bubbles show leaks.")
H('112.d.5.A',4,"An electronic leak detector senses refrigerant by detecting:",
  "Halogen in the air sample",["Heat","Color","Pressure"],"Halogen detectors sniff refrigerant.")
H('112.d.5.B',3,"Pressurizing with nitrogen and checking with soap bubbles is a:",
  "Leak test",["Charge check","Recovery","Evacuation"],"Standing pressure test.")
H('112.d.5.B',4,"A pressure that drops steadily on a gauge after charging with nitrogen suggests:",
  "A leak",["A full charge","A good seal","Cooler gas only"],"Falling pressure means leak.")
H('112.d.5.C',3,"A vacuum pump is used to remove air and moisture from a:",
  "Refrigerant system",["Duct","Furnace flue","Water heater"],"Evacuation.")
H('112.d.5.C',4,"A micron gauge measures:",
  "Deep vacuum levels",["Voltage","Gas flow","Temperature of air"],"Microns indicate vacuum.")
H('112.d.5.D',3,"Evacuation boils moisture out of a system by:",
  "Lowering pressure so water vaporizes",["Heating the room","Adding oil","Chilling the pump"],"Low pressure lowers boiling point.")
H('112.d.5.D',4,"A system is considered dry when the vacuum holds below about:",
  "500 microns",["29 inches only","50,000 microns","760 mm only"],"Deep vacuum target.")
H('112.d.5.E',3,"A recovery machine pulls refrigerant into a:",
  "Recovery cylinder",["Water tank","Fuel can","Toolbox"],"Recovered refrigerant is stored.")
H('112.d.5.E',4,"A recovery cylinder must never be filled beyond:",
  "80 percent of its capacity",["100 percent","120 percent","50 liters"],"Leave expansion space.")
H('112.d.5.F',3,"During recovery, the technician should wear gloves and:",
  "Safety glasses",["Sandals","A tie","A scarf"],"Liquid refrigerant can freeze skin.")
H('112.d.5.F',4,"Recovery is complete when the system reaches the:",
  "Required vacuum level for that refrigerant",["Same pressure as the shop","Highest pressure","Lowest temperature"],"EPA specifies levels.")
H('112.d.5.G',3,"A deep vacuum is achieved with a vacuum pump rated for:",
  "Low micron performance",["High pressure","High voltage","Fuel use"],"Pump capability matters.")
H('112.d.5.G',4,"Using large-diameter hoses for evacuation helps by:",
  "Speeding the process",["Slowing it","Adding moisture","Cooling the pump"],"Bigger hoses flow better.")
H('112.d.5.H',3,"A charging scale is used to measure the:",
  "Weight of refrigerant added",["Speed of fan","Voltage drop","Room humidity"],"Weigh in the charge.")
H('112.d.5.H',4,"A manifold gauge set connects to the system's:",
  "Service ports",["Thermostat","Filter","Air vent"],"Gauges attach at ports.")
H('112.d.5.I',3,"Purging with dry nitrogen helps remove:",
  "Moisture and contaminants",["Voltage","Oil only","Heat only"],"Nitrogen sweeps the lines.")
H('112.d.5.I',4,"When brazing, nitrogen flows through the line so that:",
  "No scale forms inside the tube",["The tube melts","Flux dries","The torch cools"],"Prevents oxidation.")
H('112.d.5.J',3,"The most accurate way to charge many systems is by:",
  "Weight",["Guesswork","Touch","Sound"],"Weighing is precise.")
H('112.d.5.J',4,"Charging by superheat or subcooling relies on:",
  "Pressure and temperature readings",["Thermostat color","Duct length","Filter size"],"Measured values guide charge.")
H('112.d.6.A',3,"A step-down transformer produces a secondary voltage that is:",
  "Lower than the primary",["Higher than the primary","Equal always","Zero"],"Step-down reduces voltage.")
H('112.d.6.A',4,"A common HVAC control transformer converts line voltage to:",
  "24 volts",["480 volts","1,000 volts","6 volts"],"Control circuits use 24 V.")
H('112.d.6.B',3,"AC voltage is produced by a generator whose coil rotates in a:",
  "Magnetic field",["Water bath","Vacuum tube","Oil sump"],"Rotation induces voltage.")
H('112.d.6.B',4,"One full cycle of an AC sine wave consists of a positive alternation and a:",
  "Negative alternation",["Zero alternation","Square wave","Double positive"],"Sine waves alternate.")
H('112.d.6.C',3,"A 120/208 volt wye service from the utility feeds a commercial rooftop unit with how many hot conductors?",
  "3",["1","2","6"],"Three phases.")
H('112.d.6.C',4,"Single-phase 240 volt service has two hot legs that are:",
  "180 degrees apart",["90 degrees apart","In phase","120 degrees apart"],"Split-phase.")
H('112.d.6.D',3,"In an inductive circuit, the current:",
  "Lags the voltage",["Leads the voltage","Is in phase","Is zero"],"Inductors lag.")
H('112.d.6.D',4,"In a capacitive circuit, the current:",
  "Leads the voltage",["Lags the voltage","Equals zero","Is steady DC"],"Capacitors lead.")
H('112.d.6.E',3,"A run capacitor stays in the circuit to improve motor:",
  "Efficiency while running",["Fuel mix","Duct size","Humidity"],"Run caps are continuous duty.")
H('112.d.6.E',4,"A start capacitor is in the circuit only:",
  "For a brief time while the motor starts",["All the time","Never","After shutdown"],"Start caps are intermittent.")
H('112.d.6.F',3,"A three-phase induction motor does not need a start capacitor because the three phases create:",
  "A rotating magnetic field",["A steady DC field","No field","A frozen field"],"Phases self-start.")
H('112.d.6.F',4,"Single-phase motors need a starting mechanism because a single-phase field:",
  "Pulses rather than rotates",["Rotates fast","Is DC","Is absent"],"No starting torque without help.")
H('112.d.6.G',3,"A permanent split-capacitor motor is often used in:",
  "Fan applications",["Welding","Arc lighting","Large chillers"],"PSC motors drive fans.")
H('112.d.6.G',4,"A shaded-pole motor is a low-torque motor often found in:",
  "Small fans and appliances",["Industrial pumps","Chillers","Elevators"],"Simple, low-cost motor.")
H('112.d.6.H',3,"When testing a capacitor, always first:",
  "Discharge it safely",["Charge it more","Heat it","Cut it"],"Stored charge is dangerous.")
H('112.d.6.H',4,"Capacitors can hold a shock hazard even when the power is:",
  "Off",["On only","At 5 volts","Disconnected from the earth"],"Stored energy remains.")
H('112.d.6.I',3,"A capacitor is tested with a meter set to measure:",
  "Capacitance in microfarads",["Humidity","Frequency of gas","Speed"],"Compare to rating.")
H('112.d.6.I',4,"A transformer winding that reads infinite resistance is:",
  "Open",["Good","Shorted","Grounded"],"Open circuit.")
H('112.d.7.A',3,"Semiconductor materials such as silicon conduct:",
  "Better than insulators but less than metals",["Better than copper","Exactly like rubber","Only when frozen"],"Semiconductors are in between.")
H('112.d.7.A',4,"Adding impurities to silicon to change its conductivity is called:",
  "Doping",["Melting","Soldering","Plating"],"Doping creates N and P types.")
H('112.d.7.B',3,"A diode allows current to flow:",
  "In one direction",["In both directions","In no direction","Only at night"],"Diodes are one-way valves.")
H('112.d.7.B',4,"An LED emits light when current passes:",
  "Forward through it",["In reverse","Never","Across a gap"],"Forward bias lights it.")
H('112.d.7.C',3,"Resistors are marked with:",
  "Color bands",["Letters of the alphabet only","Sound waves","Magnets"],"Bands give value.")
H('112.d.7.C',4,"A variable resistor used to adjust volume is a:",
  "Potentiometer",["Diode","Fuse","Relay"],"Pots change resistance.")
H('112.d.7.D',3,"A thermistor changes resistance with:",
  "Temperature",["Voltage","Color","Sound"],"Thermal sensor.")
H('112.d.7.D',4,"A cad cell changes resistance with:",
  "Light",["Heat","Pressure","Humidity"],"Cad cells sense light.")
H('112.d.7.E',3,"A diode is tested with a meter on the:",
  "Diode test or resistance setting",["Amps setting live","Frequency setting only","Gas setting"],"Check forward and reverse.")
H('112.d.7.E',4,"A good diode reads low resistance one way and:",
  "Very high resistance the other way",["Low both ways","Zero both ways","Infinite both ways"],"One-way conduction.")
H('112.d.7.F',3,"The connector commonly used for a computer monitor today includes HDMI and:",
  "DisplayPort",["Coaxial dish","Phone jack","Banana plug"],"Video ports.")
H('112.d.7.F',4,"A USB port is mainly used to connect:",
  "Peripheral devices",["Water lines","Gas valves","Ducts"],"Universal Serial Bus.")
H('112.d.8.A',3,"A thermostat's function is to:",
  "Sense temperature and control equipment",["Create heat","Store air","Filter water"],"Controls the system.")
H('112.d.8.A',4,"A thermostat is typically located:",
  "On an interior wall away from drafts and sun",["Over a heating register","In direct sunlight","Outdoors in the rain"],"Placement affects accuracy.")
H('112.d.8.B',3,"A programmable thermostat saves energy by:",
  "Changing setpoints on a schedule",["Running constantly","Ignoring the schedule","Blocking air"],"Setback saves energy.")
H('112.d.8.B',4,"A bimetal thermostat senses temperature using:",
  "Two metals that expand differently",["A battery","Gas","Radio"],"Bimetal bends.")
H('112.d.8.C',3,"Before removing an old thermostat, the technician should:",
  "Turn off power to the system",["Leave the power on","Cut wires randomly","Remove the furnace"],"Prevent shorts.")
H('112.d.8.C',4,"Thermostat wires are labeled with letters such as R, W, and Y to show the:",
  "Function of each terminal",["Brand of the wire","Age","Weight"],"Terminal codes.")
H('112.d.8.D',3,"A basic control system includes a sensor, a controller, and a:",
  "Controlled device",["Roof","Brick","Foundation"],"Sense, decide, act.")
H('112.d.8.D',4,"In a control loop, feedback tells the controller:",
  "How the system is responding",["The cost of the unit","The color of the room","The owner's name"],"Closed loop.")
H('112.d.8.E',3,"Controls that use compressed air to operate are called:",
  "Pneumatic",["Electronic","Hydraulic","Manual"],"Pneumatic uses air.")
H('112.d.8.E',4,"A relay is an example of an:",
  "Electromechanical control",["Pneumatic control","Optical control","Manual valve"],"Coil and contacts.")
H('112.d.8.F',3,"A systematic approach to troubleshooting starts with:",
  "Gathering information about the complaint",["Replacing parts at random","Guessing","Doing nothing"],"Information first.")
H('112.d.8.F',4,"After finding and fixing a fault, the technician should:",
  "Verify the system works properly",["Leave immediately","Skip checks","Break something else"],"Confirm repair.")
H('112.d.8.G',3,"Manufacturer troubleshooting charts are found in the unit's:",
  "Service literature",["Warranty card only","Shipping label","Brochure photo"],"Use the factory info.")
H('112.d.8.G',4,"A wiring diagram attached inside the panel helps the technician to:",
  "Trace circuits",["Paint the cover","Count fins","Order lunch"],"Diagrams guide diagnosis.")
H('112.d.8.H',3,"A technician isolates a no-power problem by first checking the:",
  "Main power supply and disconnect",["Duct size","Filter color","Fuel price"],"Start at the source.")
H('112.d.8.H',4,"If the control transformer secondary has no voltage but the primary has voltage, the transformer is:",
  "Likely bad",["Working","New","Overloaded"],"No output with input.")
H('112.d.8.I',3,"A tool used to check for voltage in HVAC work is a:",
  "Multimeter",["Hammer","Plumb bob","Tape measure"],"Meters measure electricity.")
H('112.d.8.I',4,"A clamp-on ammeter measures current without:",
  "Breaking the circuit",["Using batteries","Any training","Power"],"Clamp jaws sense field.")
H('112.d.8.J',3,"When checking a motor winding for continuity, power should be:",
  "Off",["On","Doubled","Reversed"],"Ohm checks need power off.")
H('112.d.8.J',4,"A winding that reads very high resistance to ground when it should be isolated is:",
  "Good",["Grounded","Shorted","Burned"],"Isolation to ground is good.")
H('112.d.8.K',3,"A cooling unit with a running fan but no compressor may have a bad:",
  "Contactor or run capacitor",["Drain pan","Filter","Duct"],"Compressor circuit check.")
H('112.d.8.K',4,"When a contactor coil gets 24 volts but the contacts do not close, the likely fault is:",
  "A defective contactor",["A dirty filter","A low charge","A kinked duct"],"Replace the contactor.")
H('112.d.9.A',3,"In a gas furnace sequence, a call for heat first starts the:",
  "Draft inducer",["Gas valve open","Humidifier","Filter"],"Pre-purge.")
H('112.d.9.A',4,"The blower on a gas furnace starts after the heat exchanger warms up, controlled by a:",
  "Timed delay or fan switch",["Spark","Drain","Filter"],"Prevents cold air.")
H('112.d.9.B',3,"On a ladder diagram, switches are shown in series with the load to indicate they:",
  "All must close for the load to run",["Operate in any order","Do nothing","Are decorative"],"Series logic.")
H('112.d.9.B',4,"A limit switch in a furnace control circuit opens when temperature is:",
  "Too high",["Too low","Normal","Zero"],"Safety shutoff.")
H('112.d.9.C',3,"A hot surface igniter lights a burner by:",
  "Glowing hot enough to ignite gas",["Making a spark in air","Burning oil","Using a pilot flame"],"Hot surface.")
H('112.d.9.C',4,"A standing pilot burner stays:",
  "Lit continuously",["Off until needed","Cold","Underwater"],"Always on.")
H('112.d.9.D',3,"Instruments used for gas heat troubleshooting include a multimeter and a:",
  "Manometer",["Metronome","Ruler","Hammer"],"Gas pressure measure.")
H('112.d.9.D',4,"A combustion analyzer helps check the furnace for:",
  "Carbon monoxide and oxygen levels in the flue",["Room color","Water pH","Voltage only"],"Combustion test.")
H('112.d.9.E',3,"When using a manometer on a gas valve, connect it to the valve's:",
  "Pressure tap",["Drain","Vent","Door"],"Test port.")
H('112.d.9.E',4,"After checking gas pressure, the technician must:",
  "Close the test port and check for leaks",["Leave it open","Smell for gas only","Heat the tap"],"Leak check.")
H('112.d.9.F',3,"If a furnace lights briefly and shuts off, a likely cause is a:",
  "Dirty flame sensor",["Full filter","New thermostat","Cold room"],"Sensor needs cleaning.")
H('112.d.9.F',4,"A furnace that short cycles on the high limit often has:",
  "Restricted airflow",["Too much fuel","A cold room","A new filter"],"Overheats.")
H('112.d.10.A',3,"A good troubleshooting approach for cooling systems begins by:",
  "Verifying the complaint and checking the basics",["Pulling the compressor","Replacing parts first","Waiting a week"],"Start simple.")
H('112.d.10.A',4,"The first checks on a cooling system with no cold air are the thermostat, power, and:",
  "Air filter",["Brand of unit","Paint","Roof"],"Basic checks.")
H('112.d.10.B',3,"A problem where the compressor hums but does not start is likely:",
  "Electrical",["Duct size","Refrigerant color","Filter"],"Hard start indicator.")
H('112.d.10.B',4,"Low suction pressure with a frosted evaporator coil often points to:",
  "Low airflow or low charge",["High charge","Cold weather","Wide ducts"],"Mechanical symptom.")
H('112.d.10.C',3,"Many manufacturers provide a troubleshooting chart that lists:",
  "Symptoms, causes, and fixes",["Prices","Jokes","Weather"],"Use the chart.")
H('112.d.10.C',4,"A service facts label on the unit gives:",
  "Operating data and wiring",["Owner's address","Lunch menu","Local news"],"Factory info.")
H('112.d.10.D',3,"A technician measures superheat using a temperature probe and a:",
  "Pressure gauge",["Level","Ruler","Hammer"],"Superheat needs P and T.")
H('112.d.10.D',4,"Subcooling is measured on the:",
  "Liquid line",["Return duct","Flue","Gas line"],"Liquid-line reading.")
H('112.d.10.E',3,"A dirty condenser coil typically causes:",
  "High head pressure",["Low head pressure","No change","Frozen indoor coil"],"Poor heat rejection.")
H('112.d.10.E',4,"Restricted metering device symptoms include a cold liquid line and:",
  "Low suction pressure",["High suction pressure","Normal operation","High voltage"],"Restriction.")
H('112.d.10.F',3,"A basic safety rule when servicing cooling units is to:",
  "Lock out power before opening panels",["Work live always","Remove guards","Ignore labels"],"Lockout first.")
H('112.d.10.F',4,"Refrigerant liquid on skin can cause:",
  "Frostbite",["Sunburn","Rash from heat","Nothing"],"Liquid refrigerant freezes tissue.")
H('112.d.11.A',3,"A heat pump in heating mode moves heat from:",
  "Outdoors to indoors",["Indoors to outdoors","Ground to roof","Fuel to air"],"Even cold air has heat.")
H('112.d.11.A',4,"The reversing valve in a heat pump changes:",
  "The direction of refrigerant flow",["Voltage","Filter","Duct shape"],"It switches modes.")
H('112.d.11.B',3,"A heat pump that uses the earth or water as its heat source is a:",
  "Geothermal heat pump",["Air-source unit","Furnace","Boiler"],"Ground source.")
H('112.d.11.B',4,"A split-system heat pump has indoor and outdoor sections connected by:",
  "Refrigerant lines",["Ducts only","Wire only","Hoses of water"],"Line set.")
H('112.d.11.C',3,"A closed-loop geothermal system circulates:",
  "Antifreeze solution in buried pipe",["Natural gas","Oil","Air"],"Sealed loop.")
H('112.d.11.C',4,"An open-loop geothermal system uses:",
  "Well or surface water",["Roof air","Sand","Gasoline"],"Water source.")
H('112.d.11.D',3,"Besides the compressor, a heat pump has an outdoor coil, an indoor coil, and a:",
  "Reversing valve",["Spark plug","Chimney","Heat anticipator"],"Heat pump parts.")
H('112.d.11.D',4,"The accumulator on a heat pump protects the compressor from:",
  "Liquid refrigerant returning",["High voltage","Dust","Noise"],"Prevents slugging.")
H('112.d.11.E',3,"Electric strip heat in a heat pump system is used as:",
  "Supplemental or backup heat",["Primary cooling","A filter","A humidifier"],"Backup heat.")
H('112.d.11.E',4,"During defrost, the heat pump may energize strip heat to:",
  "Prevent cold air from blowing indoors",["Cool the coil","Add humidity","Save energy"],"Tempers the air.")
H('112.d.11.F',3,"COP stands for coefficient of:",
  "Performance",["Production","Pressure","Power"],"COP is efficiency ratio.")
H('112.d.11.F',4,"A heat pump with a COP of 3 delivers how many units of heat for each unit of electricity used?",
  "3",["1","0.3","30"],"COP is output over input.")
H('112.d.11.G',3,"The outdoor unit of a heat pump should be placed on a stand so that snow and water:",
  "Do not block airflow or the coil",["Pile up","Freeze solid","Cover it"],"Install above grade.")
H('112.d.11.G',4,"The refrigerant line set for a heat pump should be:",
  "Sized and insulated per instructions",["Any size","Uninsulated","Pinched"],"Proper line set.")
H('112.d.11.H',3,"A suction line accumulator is an accessory that:",
  "Stores liquid before it reaches the compressor",["Heats the room","Filters air","Starts the fan"],"Protects compressor.")
H('112.d.11.H',4,"A check valve in a heat pump circuit allows refrigerant to flow:",
  "One way only",["Both ways","Neither way","Backward"],"Check valves direct flow.")
H('112.d.11.I',3,"A defrost control is a part of the heat pump:",
  "Control circuit",["Duct system","Filter bank","Gas line"],"Defrost logic.")
H('112.d.11.I',4,"A heat pump that stays in defrost too long may have a faulty:",
  "Defrost sensor or board",["Filter","Duct","Chimney"],"Sensor failure.")
H('112.d.11.J',3,"A heat pump that blows cold air in heating mode might have a bad:",
  "Reversing valve or its solenoid",["Filter","Roof","Window"],"Valve fault.")
H('112.d.11.J',4,"Low airflow across the indoor coil in heating mode causes:",
  "High head pressure",["Low head pressure","No change","Cold liquid line"],"Dirty coil or filter.")
H('112.d.12.A',3,"Threaded fasteners include bolts, screws, and:",
  "Studs",["Rivets","Pins","Staples"],"Threads grip.")
H('112.d.12.A',4,"A lock washer under a nut helps prevent:",
  "Loosening from vibration",["Rust only","Overheating","Leaks"],"Locking.")
H('112.d.12.B',3,"A gasket is used to:",
  "Seal between two mating surfaces",["Join two pipes","Measure flow","Cool oil"],"Gaskets seal.")
H('112.d.12.B',4,"A shaft seal keeps lubricant in and contaminants:",
  "Out",["Hot","In","Wet"],"Seals protect.")
H('112.d.12.C',3,"Lubricants reduce friction and:",
  "Wear",["Voltage","Humidity","Noise only"],"Oil protects parts.")
H('112.d.12.C',4,"Grease is generally used on bearings that are:",
  "Not oil-fed",["Always dry","Submerged in oil","Made of wood"],"Grease stays in place.")
H('112.d.12.D',3,"A grease gun is used to lubricate bearings through a:",
  "Zerk fitting",["Spark plug","Valve stem","Drain cap"],"Fitting accepts grease.")
H('112.d.12.D',4,"Over-greasing a motor bearing can cause:",
  "Overheating and seal damage",["Longer life","Cooler operation","Better efficiency"],"More is not better.")
H('112.d.12.E',3,"A V-belt is a belt with a cross-section shaped like a:",
  "Trapezoid",["Circle","Square","Star"],"V shape.")
H('112.d.12.E',4,"Proper belt tension is checked by pressing the belt and measuring:",
  "Deflection",["Color","Length","Weight"],"Tension check.")
H('112.d.12.F',3,"A coupling connects a motor shaft to the:",
  "Driven shaft",["Roof","Filter","Duct"],"Shaft connection.")
H('112.d.12.F',4,"A flexible coupling allows for small:",
  "Misalignment",["Voltage changes","Flow changes","Temperature changes"],"Flex absorbs offset.")
H('112.d.12.G',3,"Shaft alignment is checked with a:",
  "Straightedge or dial indicator",["Thermometer","Voltmeter","Flow meter"],"Alignment tools.")
H('112.d.12.G',4,"Misaligned couplings cause:",
  "Vibration and premature wear",["Quiet running","Cooler bearings","Longer life"],"Alignment matters.")
H('112.d.12.H',3,"Ball bearings reduce friction using:",
  "Rolling balls",["Sliding blocks","Rubber","Glue"],"Rolling elements.")
H('112.d.12.H',4,"A sleeve bearing supports a shaft with a:",
  "Film of oil on a bushing surface",["Row of balls","Steel rollers","Magnets"],"Plain bearings.")
H('112.d.12.I',3,"A leading cause of bearing failure is:",
  "Lack of lubrication",["Over-cleaning","Cool air","Quiet running"],"Dry bearings fail.")
H('112.d.12.I',4,"A bearing that runs hot and noisy likely has:",
  "Contamination or poor lubrication",["Perfect fit","New grease","Good alignment"],"Signs of failure.")
H('112.d.12.J',3,"A bearing puller is used to:",
  "Remove a bearing without damaging the shaft",["Install a belt","Cut a pipe","Measure flow"],"Proper tool.")
H('112.d.12.J',4,"When installing a bearing, force should be applied to the:",
  "Inner race if pressed onto the shaft",["Outer race on a shaft fit","Balls directly","Cage only"],"Press the correct race.")
H('112.d.12.K',3,"Preventive maintenance includes inspecting, cleaning, and:",
  "Lubricating equipment on a schedule",["Ignoring parts","Waiting for failure","Painting only"],"PM prevents breakdowns.")
H('112.d.12.K',4,"Cleaning a condenser coil during PM improves:",
  "Efficiency",["Noise","Color","Weight"],"Clean coils work better.")
H('112.d.12.L',3,"Good customer relations include being:",
  "Courteous and explaining the work",["Rude","Silent","Messy"],"Professionalism.")
H('112.d.12.L',4,"After a service call, the technician should leave the work area:",
  "Clean",["Dirty","Open","Unlocked"],"Respect property.")
H('112.d.13.A',3,"Sheet metal used in ducts is commonly:",
  "Galvanized steel",["Lead","Copper foil","Brass sheet"],"Zinc-coated steel.")
H('112.d.13.A',4,"Sheet metal thickness is expressed as:",
  "Gauge",["Pounds","Meters","Volts"],"Lower gauge is thicker.")
H('112.d.13.B',3,"Aluminum is lighter and more corrosion resistant than:",
  "Steel",["Feathers","Air","Paper"],"Property comparison.")
H('112.d.13.B',4,"An alloy is a metal made by:",
  "Combining two or more elements",["Painting","Heating air","Cooling water"],"Alloys mix metals.")
H('112.d.13.C',3,"A common tool for cutting sheet metal by hand is:",
  "Aviation snips",["Pliers","Wrench","Hammer"],"Snips cut sheet.")
H('112.d.13.C',4,"A layout line on sheet metal is marked with a:",
  "Scribe",["Marker only","Crayon","Pencil on aluminum only"],"Scribes mark metal.")
H('112.d.13.D',3,"A Pittsburgh seam is commonly used on:",
  "Duct corners",["Roofs","Floors","Water pipes"],"Longitudinal seam type.")
H('112.d.13.D',4,"S-slips and drive cleats join:",
  "Rectangular duct sections",["Round ducts only","Pipes","Wires"],"Connectors.")
H('112.d.13.E',3,"Ductwork is hung from the structure using:",
  "Strap or rod hangers",["Tape","Rope","String"],"Hangers support.")
H('112.d.13.E',4,"Hanger spacing for ducts is set by the:",
  "Duct size and local code",["Weather","Color","Brand"],"Spacing rules.")
H('112.d.13.F',3,"Thermal insulation reduces:",
  "Heat transfer",["Airflow","Pressure","Voltage"],"Insulation resists heat.")
H('112.d.13.F',4,"Acoustic duct lining helps reduce:",
  "Noise",["Light","Weight","Cost"],"Sound absorption.")
H('112.d.13.G',3,"Duct insulation on cold ducts should have a:",
  "Vapor barrier on the outside",["Hole every foot","Bare metal","Flammable cover"],"Prevents condensation.")
H('112.d.13.G',4,"Seams in ductwork are sealed with:",
  "Mastic or UL-listed tape",["Masking tape","Paper","Wax"],"Leak prevention.")
H('112.d.13.H',3,"A register or diffuser is attached to the duct with:",
  "A boot or collar",["Rope","Glue","Wire"],"Proper boot.")
H('112.d.13.H',4,"Registers should be installed to avoid blowing air directly:",
  "At people seated nearby",["At the ceiling","At the floor","At the wall"],"Avoid drafts.")
H('112.d.13.I',3,"A takeoff fitting connects a branch duct to the:",
  "Main trunk duct",["Roof","Furnace flue","Condensate drain"],"Takeoff.")
H('112.d.13.I',4,"Flexible duct is attached to a collar using a:",
  "Clamp or strap",["Nail","Staple","Glue only"],"Secure joint.")
H('112.d.14.A',3,"Fiberglass duct board is made of:",
  "Compressed glass fibers with a facing",["Steel","Plastic","Wood"],"Fiberglass.")
H('112.d.14.A',4,"Flexible duct has a wire helix that holds its:",
  "Round shape",["Color","Length","Weight"],"Helix.")
H('112.d.14.B',3,"Fiberglass duct board is cut with a:",
  "Special knife and straightedge",["Hammer","Torch","Axe"],"Knife cutting.")
H('112.d.14.B',4,"A V-groove cut in duct board allows it to be:",
  "Folded into a corner",["Burned","Hung","Painted"],"Folds into shape.")
H('112.d.14.C',3,"Fiberglass duct joints are closed with:",
  "Aluminum foil tape with a heat-activated or pressure seal",["Paper tape","String","Rubber bands"],"Approved tape.")
H('112.d.14.C',4,"Staples used to close duct board are:",
  "Outward clinch type",["Pinned","Glued","Welded"],"Correct staple.")
H('112.d.14.D',3,"To make a duct module, the fabricator measures, cuts, and:",
  "Folds and seals the pieces",["Burns the edges","Paints the inside","Stretches it"],"Fabrication steps.")
H('112.d.14.D',4,"A shiplap edge is cut to help the joint:",
  "Overlap and seal tightly",["Rattle","Leak","Slide"],"Closure method.")
H('112.d.14.E',3,"Fiberglass duct hangers are installed to support the duct without:",
  "Crushing it",["Removing it","Painting it","Cutting it"],"Support method.")
H('112.d.14.E',4,"Duct board hangers are often wide straps spaced:",
  "At intervals set by the maker",["Randomly","Never","Only at ends"],"Spacing.")
H('112.d.14.F',3,"Minor damage to fiberglass duct, such as a small tear, is repaired with:",
  "Approved tape or patch",["Nothing","Glue gun","Paint"],"Repair method.")
H('112.d.14.F',4,"Major damage to a section of fiberglass duct usually requires:",
  "Replacing the damaged section",["Painting it","Ignoring it","Taping once"],"Replace.")
H('112.d.14.G',3,"Flexible duct attaches to fiberglass duct board using a:",
  "Sheet metal collar and clamp",["Nail","String","Wire only"],"Takeoff.")
H('112.d.14.G',4,"When attaching flex duct, the inner liner is secured over the collar with a:",
  "Draw band",["Tack","Paper clip","Rubber band"],"Draw band.")

# ---------- 127.113 Plumbing I ----------
H('113.d.1.A',3,"A common unsafe act that leads to accidents is:",
  "Skipping personal protective equipment",["Reading the instructions","Wearing safety glasses","Using a ladder correctly"],"Unsafe acts cause injuries.")
H('113.d.1.A',4,"An example of an unsafe condition is:",
  "A wet floor with no warning sign",["A clear walkway","A posted exit","A dry shop"],"Conditions create hazards.")
H('113.d.1.B',3,"If a worker sees an unsafe condition, the best action is to:",
  "Report it and help correct it",["Ignore it","Hide it","Walk around it"],"Report hazards.")
H('113.d.1.B',4,"An unsafe act by a coworker should be handled by:",
  "Speaking up or telling a supervisor",["Laughing","Imitating","Staying silent"],"Correct unsafe behavior.")
H('113.d.1.C',3,"Besides medical bills, accidents cost a company through lost time and:",
  "Reduced productivity",["More profit","Faster work","Lower rates"],"Accidents have costs.")
H('113.d.1.C',4,"Direct costs of an injury include medical care and:",
  "Workers' compensation",["Extra vacation","Paint","Cheaper tools"],"Direct costs.")
H('113.d.1.D',3,"Hard hats protect the head from:",
  "Falling objects",["Hunger","Rain on skin","Light"],"PPE use.")
H('113.d.1.D',4,"PPE should be inspected before use for:",
  "Damage or wear",["Brand","Color","Price"],"Check gear.")
H('113.d.1.E',3,"A hazard that plumbers face working with soldering is:",
  "Burns from hot tools and pipe",["Frostbite","Dizziness from cold","Sunburn indoors"],"Heat hazard.")
H('113.d.1.E',4,"Working in a crawl space can expose a plumber to:",
  "Confined space hazards",["Sunlight","Open fields","High-rise winds"],"Specific hazards.")
H('113.d.1.F',3,"A ladder used to reach a roof should extend:",
  "At least 3 feet above the edge",["Level with the edge","Below the edge","No height"],"Ladder rule.")
H('113.d.1.F',4,"For a straight ladder, the 4-to-1 rule means the base is placed 1 foot out for every:",
  "4 feet of height",["1 foot of height","10 feet of height","2 feet of height"],"Angle guideline.")
H('113.d.1.G',3,"Trenches over 5 feet deep generally require:",
  "Shoring or sloping",["A rope","A sign only","Nothing"],"Cave-in protection.")
H('113.d.1.G',4,"Spoil piles from a trench should be kept:",
  "At least 2 feet from the edge",["At the edge","In the trench","Beneath equipment"],"Prevent cave-ins.")
H('113.d.1.H',3,"Lockout/tagout ensures that equipment is:",
  "De-energized during repair",["Running","Ignored","Hot"],"Energy control.")
H('113.d.1.H',4,"Only the person who put on a lock should:",
  "Remove it",["Cut it","Ignore it","Paint it"],"Personal lock.")
H('113.d.1.I',3,"An MSDS, now called an SDS, lists information about:",
  "A chemical's hazards and handling",["Wages","Tool prices","Weather"],"Safety data.")
H('113.d.1.I',4,"Before using a product like PVC cement, a worker should read its:",
  "Safety data sheet",["Warranty","Receipt","Catalog"],"Know hazards.")
H('113.d.2.A',3,"A plumbing career job title is:",
  "Journeyman plumber",["Pastry chef","Pilot","Dancer"],"Trade titles.")
H('113.d.2.A',4,"A worker who has completed an apprenticeship and passed the exam is a:",
  "Journeyman",["Beginner","Helper only","Retiree"],"Career path.")
H('113.d.2.B',3,"To become a plumber, one usually completes an:",
  "Apprenticeship",["Cooking class","Art class","Game"],"Training path.")
H('113.d.2.B',4,"A plumbing license shows that a person has met:",
  "State qualification requirements",["Age only","Height only","Color rules"],"Licensing.")
H('113.d.2.C',3,"A trade association for plumbers is the:",
  "Plumbing-Heating-Cooling Contractors Association",["Music Teachers Club","Garden Society","Art Guild"],"Industry groups.")
H('113.d.2.C',4,"Industries that employ plumbers include construction and:",
  "Building maintenance",["Opera","Fashion modeling","Farming only"],"Where plumbers work.")
H('113.d.2.D',3,"When working in a customer's home, a plumber should:",
  "Protect floors and furniture",["Ignore messes","Use their towels","Move belongings carelessly"],"Respect property.")
H('113.d.2.D',4,"A drop cloth in a customer's bathroom is used to:",
  "Protect surfaces from damage",["Hide tools","Mop floors","Block doors"],"Care for property.")
H('113.d.2.E',3,"Keeping the work area clean helps prevent:",
  "Accidents and lost tools",["Efficiency","Quality","Pride"],"Tidy site.")
H('113.d.2.E',4,"A clean job site reflects well on the plumber's:",
  "Professionalism",["Hair","Shoes","Truck"],"Clean work shows care.")
H('113.d.2.F',3,"Using industry standards ensures that work is:",
  "Safe and acceptable to inspectors",["Cheap only","Fast only","Unseen"],"Standards matter.")
H('113.d.2.F',4,"Plumbing codes are enforced to protect:",
  "Public health and safety",["Paint","Contractors' profits only","Weather"],"Code purpose.")
H('113.d.3.A',3,"A low-flow toilet saves water by using:",
  "Less water per flush",["More water per flush","No water","Hot water"],"Water efficiency.")
H('113.d.3.A',4,"A faucet aerator reduces water use by mixing air into the:",
  "Stream",["Drain","Pipe wall","Tank"],"Aerators.")
H('113.d.3.B',3,"Graywater reuse systems collect water from sinks and showers to use for:",
  "Irrigation or toilet flushing",["Drinking","Cooking","Bathing infants"],"Reuse.")
H('113.d.3.B',4,"A rainwater harvesting system collects water from the:",
  "Roof",["Sewer","Well","Pool only"],"Harvest.")
H('113.d.3.C',3,"Designing a reuse system involves choosing storage, filtration, and:",
  "Distribution piping",["Paint","Wall color","Carpet"],"System design.")
H('113.d.3.C',4,"Reclaimed water pipes are often marked with the color:",
  "Purple",["Blue","Red","Yellow"],"Color coding.")
H('113.d.4.A',3,"A pipe wrench is used to:",
  "Grip and turn pipe",["Cut wire","Drive nails","Measure"],"Tool function.")
H('113.d.4.A',4,"A tubing cutter makes a clean cut on:",
  "Copper tubing",["Concrete","Wood","Glass"],"Cutter use.")
H('113.d.4.B',3,"When using a hacksaw, the blade teeth should point:",
  "Away from the handle on the forward stroke",["Toward the handle","Sideways","Upward"],"Cutting direction.")
H('113.d.4.B',4,"A level is used to check whether a pipe is:",
  "Plumb or level",["Hot","Dirty","New"],"Alignment.")
H('113.d.4.C',3,"Selecting the right tool for the job helps prevent:",
  "Damage and injury",["Success","Quality","Accuracy"],"Choose well.")
H('113.d.4.C',4,"Using a screwdriver as a chisel is an example of:",
  "Misusing a tool",["Good practice","Safe practice","Required practice"],"Wrong tool.")
H('113.d.4.D',3,"Tools should be kept clean and:",
  "Sharp and in good repair",["Wet","Rusty","Loose"],"Maintenance.")
H('113.d.4.D',4,"A mushroomed chisel head should be:",
  "Ground or replaced",["Hit harder","Painted","Ignored"],"Hazard.")
H('113.d.4.E',3,"Before drilling a wall, check for hidden:",
  "Pipes and wiring",["Paint","Color","Flowers"],"Check first.")
H('113.d.4.E',4,"Marking a drill location with a center punch keeps the bit from:",
  "Walking off the spot",["Heating","Shining","Squeaking"],"Prepare surface.")
H('113.d.4.F',3,"When using power tools, you should wear:",
  "Safety glasses",["Sandals","Loose scarf","Rings"],"Eye protection.")
H('113.d.4.F',4,"A damaged power cord should be:",
  "Repaired or replaced before use",["Wrapped in tape","Ignored","Used briefly"],"Cord safety.")
H('113.d.4.G',3,"A tape measure reads in feet and:",
  "Inches",["Gallons","Ounces","Volts"],"Linear measure.")
H('113.d.4.G',4,"A rule marked in sixteenths shows the smallest division of:",
  "1/16 inch",["1/2 inch","1 inch","1 foot"],"Fractions.")
H('113.d.5.A',3,"Adding 1/2 and 1/4 gives:",
  "3/4",["1/8","2/6","1/3"],"1/2 + 1/4 = 3/4.")
H('113.d.5.A',4,"Multiplying 3/4 by 8 gives:",
  "6",["24","2","5"],"3/4 x 8 = 6.")
H('113.d.5.B',3,"The fraction 1/4 as a decimal is:",
  "0.25",["0.4","0.14","2.5"],"1 divided by 4.")
H('113.d.5.B',4,"The decimal 0.375 as a fraction is:",
  "3/8",["3/5","1/3","3/10"],"0.375 = 3/8.")
H('113.d.5.C',3,"One meter equals how many centimeters?",
  "100",["10","1,000","12"],"Metric.")
H('113.d.5.C',4,"A pipe measuring 2,500 millimeters is how many meters?",
  "2.5",["25","0.25","250"],"Divide by 1,000.")
H('113.d.5.D',3,"The square of 7 is:",
  "49",["14","21","77"],"7 x 7.")
H('113.d.5.D',4,"The square root of 144 is:",
  "12",["72","14","24"],"12 x 12 = 144.")
H('113.d.5.E',3,"The end of a pipe that fits into a fitting is called the:",
  "Spigot or male end",["Hub","Cap","Union"],"Fitting parts.")
H('113.d.5.E',4,"The face-to-face measurement of a fitting is also called its:",
  "Center-to-end or face dimension",["Color","Brand","Wall"],"Fitting dimension.")
H('113.d.5.F',3,"Fitting allowance is found in:",
  "A fitting dimension table",["A coupon","A menu","A paycheck"],"Look up allowance.")
H('113.d.5.F',4,"Thread engagement is the length of pipe that:",
  "Goes into the fitting",["Stays outside","Is cut off","Is painted"],"Engagement.")
H('113.d.5.G',3,"End-to-end measurement is taken from:",
  "One pipe end to the other",["Wall to wall","Center to center","Top to bottom"],"Measurement type.")
H('113.d.5.G',4,"Center-to-center measurement is used to:",
  "Locate fittings in a run",["Check the weather","Count pipes","Pay invoices"],"Layout.")
H('113.d.6.A',3,"An isometric drawing shows a pipe system with:",
  "Three dimensions on 30-degree axes",["Only a front view","A flat map","Words only"],"Isometric.")
H('113.d.6.A',4,"A pictorial drawing resembles a:",
  "3D view of the system",["Table","List","Chart"],"Pictorial drawing.")
H('113.d.6.B',3,"A symbol on a pipe drawing represents a:",
  "Fitting or valve",["Person","Time","Cost"],"Symbols.")
H('113.d.6.B',4,"A gate valve symbol on a schematic shows the valve is used to:",
  "Start and stop flow",["Measure flow","Cool flow","Filter flow"],"Valve symbol.")
H('113.d.6.C',3,"A plumbing drawing set may include floor plans, riser diagrams, and:",
  "Details",["Poetry","Recipes","Menus"],"Types of drawings.")
H('113.d.6.C',4,"A riser diagram shows piping between:",
  "Floors",["Rooms in the yard","Cars","Lights"],"Vertical piping.")
H('113.d.6.D',3,"The title block of a plumbing drawing includes the sheet:",
  "Number and project name",["Lunch order","Weather","Song"],"Info.")
H('113.d.6.D',4,"A drawing note often explains special:",
  "Instructions or materials",["Pictures","Songs","Colors of cars"],"Notes.")
H('113.d.6.E',3,"An orthographic drawing shows an object from:",
  "Separate views such as top and front",["One angle in 3D","A photo","A map"],"Orthographic.")
H('113.d.6.E',4,"The three common orthographic views are top, front, and:",
  "Right side",["Corner","Diagonal","Hidden"],"Views.")
H('113.d.6.F',3,"An architect's scale of 1/4 inch = 1 foot means that a 3/4 inch line represents:",
  "3 feet",["1 foot","6 feet","12 feet"],"Scale.")
H('113.d.6.F',4,"On a 1/8-inch scale, a 12-foot wall is drawn how many inches long?",
  "1.5",["12","0.5","3"],"12 x 1/8 = 1.5.")
H('113.d.6.G',3,"Code requirements on drawings specify things like:",
  "Pipe size and slope",["Brand of paint","Lunch time","Wall art"],"Code on plans.")
H('113.d.6.G',4,"A plumber must make sure that the installation matches both the drawings and the:",
  "Plumbing code",["Neighbor's wishes","Weather","Dress code"],"Compliance.")
H('113.d.7.A',3,"Common plastic piping materials include PVC and:",
  "ABS",["Brass","Cast iron","Clay"],"Plastic types.")
H('113.d.7.A',4,"Schedule 40 and schedule 80 describe plastic pipe:",
  "Wall thickness",["Color","Length","Brand"],"Schedule.")
H('113.d.7.B',3,"PVC pipe should not be used for:",
  "Hot water lines over its temperature rating",["Cold water supply","Drainage","Irrigation"],"Improper use.")
H('113.d.7.B',4,"PVC pipe exposed to sunlight should be:",
  "Protected or painted",["Left bare","Buried unprotected","Heated"],"UV damage.")
H('113.d.7.C',3,"Fittings for plastic pipe include couplings, elbows, and:",
  "Tees",["Wrenches","Hammers","Saws"],"Fittings.")
H('113.d.7.C',4,"A ball valve made for plastic piping is often joined by:",
  "Solvent cement or threads",["Soldering","Brazing","Welding"],"Valves.")
H('113.d.7.D',3,"Plastic pipe needs hangers placed closer together than metal pipe because plastic is:",
  "More flexible",["Heavier","Stronger","Hotter"],"Support spacing.")
H('113.d.7.D',4,"Hangers used with plastic pipe should be:",
  "Smooth to avoid damaging the pipe",["Sharp","Rough","Tight enough to crush"],"Support type.")
H('113.d.7.E',3,"Plastic pipe must be allowed to move for:",
  "Expansion and contraction",["Painting","Cutting","Color"],"Thermal movement.")
H('113.d.7.E',4,"Over-tightening a clamp on plastic pipe can:",
  "Restrict movement and cause stress",["Help it","Cool it","Seal it"],"Hanging technique.")
H('113.d.7.F',3,"Before cementing PVC, the pipe end should be:",
  "Cut square and deburred",["Left rough","Painted","Greased"],"Prep.")
H('113.d.7.F',4,"The proper order for solvent welding PVC is primer first, then:",
  "Cement",["Water","Oil","Paint"],"Joining.")
H('113.d.7.G',3,"Plastic pipe should be stored:",
  "Supported along its full length",["Standing in the sun","On a point","Under water"],"Storage.")
H('113.d.7.G',4,"Cement and primer should be kept away from:",
  "Heat and flame",["Shade","Cool rooms","Bins"],"Flammable.")
H('113.d.7.H',3,"Plumbing codes list which plastic pipes are approved for:",
  "Specific uses",["Any use","No use","Decor"],"Code.")
H('113.d.7.H',4,"Pipe marked with NSF and a standard number shows it was:",
  "Tested for that application",["Colored","Cheap","Used"],"Marking.")
H('113.d.8.A',3,"Copper tubing types K, L, and M differ in:",
  "Wall thickness",["Color only","Length","Brand"],"Types.")
H('113.d.8.A',4,"The thickest wall of the three common copper tube types is:",
  "Type K",["Type M","Type L","Type D"],"K is thickest.")
H('113.d.8.B',3,"Copper tubing should be stored so that it is not:",
  "Bent or dented",["Straight","Clean","Dry"],"Handling.")
H('113.d.8.B',4,"Rigid copper tube ends should be capped during storage to keep out:",
  "Dirt",["Light","Heat","Sound"],"Storage.")
H('113.d.8.C',3,"Copper fittings are joined to tubing by:",
  "Soldering or brazing",["Gluing","Taping","Stapling"],"Joining.")
H('113.d.8.C',4,"A gate valve in copper piping is used to:",
  "Shut off the water supply",["Meter flow","Cool water","Filter water"],"Valves.")
H('113.d.8.D',3,"Copper tubing is supported with:",
  "Hangers spaced per code",["String","Nails through it","Tape"],"Support.")
H('113.d.8.D',4,"When copper touches steel hangers, the technician should isolate them to avoid:",
  "Galvanic corrosion",["Noise","Heat","Light"],"Dissimilar metals.")
H('113.d.8.E',3,"Before soldering, the tube end and fitting cup are cleaned until:",
  "Bright and shiny",["Dull","Green","Black"],"Prep.")
H('113.d.8.E',4,"Solder joints in potable water must use:",
  "Lead-free solder",["Lead solder","Any solder","Tin foil"],"Safe.")
H('113.d.8.F',3,"After cutting copper tube, the inside edge is reamed to remove:",
  "Burrs",["Color","Zinc","Water"],"Reaming.")
H('113.d.8.F',4,"A tube cutter should be tightened a little at a time to prevent:",
  "Deforming the tube",["Cooling","Rusting","Singing"],"Cutting.")
H('113.d.8.G',3,"A hazard when soldering is:",
  "Fire from the open flame",["Frostbite","Noise","Drips of water"],"Torch safety.")
H('113.d.8.G',4,"A heat shield behind a joint protects nearby:",
  "Combustible materials",["Tools","Hands","Gloves"],"Precaution.")
H('113.d.8.H',3,"Plumbing code specifies which copper tube types are allowed for:",
  "Water supply and drainage uses",["Roofing","Painting","Cooking"],"Code.")
H('113.d.8.H',4,"Type DWV copper is made for:",
  "Drain, waste, and vent systems",["Hot water supply","Gas lines","Refrigeration"],"DWV tube.")
H('113.d.9.A',3,"Carbon steel pipe is often used for:",
  "Gas and fire sprinkler lines",["Drinking fountains","Wiring","Decor"],"Applications.")
H('113.d.9.A',4,"Black iron pipe is commonly used for:",
  "Natural gas piping",["Drinking water","Drains","Wastewater"],"Gas.")
H('113.d.9.B',3,"Carbon steel pipe should be stored off the ground to prevent:",
  "Rust and contamination",["Cooling","Shaping","Growth"],"Storage.")
H('113.d.9.B',4,"Galvanized steel pipe is coated to resist:",
  "Corrosion",["Fire","Noise","Light"],"Coating.")
H('113.d.9.C',3,"Steel pipe hangers are spaced according to pipe:",
  "Size and code",["Color","Brand","Weight of the crew"],"Support.")
H('113.d.9.C',4,"Vertical steel pipe is supported at:",
  "Each floor or as required",["Never","Random points","One end only"],"Risers.")
H('113.d.9.D',3,"Threads on steel pipe are cut with:",
  "A die and threader",["A wrench only","Pliers","A drill"],"Threading.")
H('113.d.9.D',4,"Cutting oil is used when threading pipe to reduce:",
  "Friction and heat",["Noise only","Flow","Weight"],"Oil helps.")
H('113.d.9.E',3,"Codes for gas piping specify that steel pipe joints must be:",
  "Leak tested",["Painted","Covered","Hidden"],"Testing.")
H('113.d.9.E',4,"Threaded steel gas pipe joints are sealed with a compound rated for:",
  "Gas",["Water only","Paint","Wood"],"Compound.")
H('113.d.10.A',3,"Corrugated stainless steel tubing (CSST) is a flexible pipe used for:",
  "Fuel gas",["Drains","Sewage","Rainwater"],"CSST.")
H('113.d.10.A',4,"CSST must be installed by someone who is:",
  "Trained and certified by the manufacturer",["Unqualified","Any helper","A customer"],"Training.")
H('113.d.10.B',3,"CSST must be properly bonded to reduce risk from:",
  "Lightning",["Rain","Cold","Sun"],"Bonding.")
H('113.d.10.B',4,"CSST should not be used where it can be:",
  "Damaged by sharp objects",["Hung","Insulated","Labeled"],"Improper use.")
H('113.d.10.C',3,"CSST is supported at intervals set by the:",
  "Manufacturer and code",["Customer","Weather","Truck"],"Hanging.")
H('113.d.10.C',4,"CSST passing through a stud should be protected with a:",
  "Striker plate or sleeve",["Tape","Paint","Rope"],"Protection.")
H('113.d.10.D',3,"CSST is cut with a:",
  "Tubing cutter",["Hacksaw only","Torch","Axe"],"Cutting.")
H('113.d.10.D',4,"CSST fittings are attached with:",
  "Mechanical fittings supplied by the maker",["Glue","Solder","Wire"],"Joining.")
H('113.d.10.E',3,"CSST is shipped on:",
  "Coils or reels",["Boards","Sheets","Barrels"],"Handling.")
H('113.d.10.E',4,"CSST jacketing should be protected from:",
  "Damage and sunlight",["Dryness","Air","Cool"],"Storage.")
H('113.d.10.F',3,"Local codes may require CSST to be:",
  "Bonded and installed per listing",["Hidden","Ignored","Painted red"],"Code.")
H('113.d.10.F',4,"A pressure test is run on a gas line to prove it is:",
  "Free of leaks",["Hot","Cold","Dirty"],"Test.")
H('113.d.11.A',3,"Waste leaves a fixture through the drain and flows by:",
  "Gravity to the building drain",["A pump always","A motor","Pressure"],"DWV flow.")
H('113.d.11.A',4,"A building drain carries waste to the:",
  "Building sewer",["Roof","Attic","Fixture"],"Path.")
H('113.d.11.B',3,"A vent pipe lets air into the drainage system to prevent:",
  "Siphoning of traps",["Heating","Cooling","Noise only"],"Venting.")
H('113.d.11.B',4,"A cleanout provides access to:",
  "Clear a clogged drain",["Light a room","Fill a tank","Cool a pipe"],"Cleanouts.")
H('113.d.11.C',3,"A trap holds a water seal that blocks:",
  "Sewer gas",["Water","Light","Heat"],"Traps.")
H('113.d.11.C',4,"A P-trap is commonly found under a:",
  "Sink",["Roof","Furnace","Window"],"Trap type.")
H('113.d.11.D',3,"A sanitary tee is used to:",
  "Connect a branch to a drain",["Reduce water pressure","Heat pipe","Measure flow"],"Fittings.")
H('113.d.11.D',4,"A wye fitting is used to:",
  "Join two drains while keeping smooth flow",["Make a sharp turn","Shut off flow","Meter flow"],"Fittings.")
H('113.d.11.E',3,"Sewer gas leaking into a building is a:",
  "Health hazard",["Benefit","Saving","Feature"],"Health issues.")
H('113.d.11.E',4,"A plumber who violates the code may face:",
  "Fines or loss of license",["Prizes","Raises","Holidays"],"Consequences.")
H('113.d.11.F',3,"A line type on a plan for waste piping is often drawn as:",
  "A solid heavy line",["Wavy line","Dotted star","No line"],"DWV symbols.")
H('113.d.11.F',4,"A vent line on a drawing is commonly shown as:",
  "A dashed line",["A solid fat line","A circle","A box"],"Symbols.")
H('113.d.11.G',3,"An isometric DWV drawing helps a plumber to prepare a:",
  "Materials list",["Menu","Playlist","Score card"],"Takeoff.")
H('113.d.11.G',4,"The slope of a horizontal drain is typically:",
  "1/4 inch per foot",["1 inch per foot","Zero","3 inches per foot"],"Slope.")
H('113.d.11.H',3,"Common DWV pipe materials include PVC, ABS, and:",
  "Cast iron",["Rubber","Wood","Brass tubes"],"Materials.")
H('113.d.11.H',4,"Cast iron pipe for drains is valued for being:",
  "Quiet and fire resistant",["Light","Cheap","Flexible"],"Properties.")
H('113.d.11.I',3,"Code requires drain lines to be tested by:",
  "Water or air test",["Weather","Paint","Colors"],"Code.")
H('113.d.11.I',4,"A water test fills the DWV system to the:",
  "Top of the highest joint being tested",["Bottom","Middle","No level"],"Testing.")
H('113.d.12.A',3,"In the water cycle, water vapor cools and forms:",
  "Clouds",["Mountains","Roads","Rocks"],"Cycle.")
H('113.d.12.A',4,"Water falling from clouds is called:",
  "Precipitation",["Evaporation","Condensation","Runoff"],"Cycle.")
H('113.d.12.B',3,"A common water source for a home is a:",
  "Well or municipal supply",["Gas line","Power line","Fire"],"Sources.")
H('113.d.12.B',4,"Groundwater is water found:",
  "Beneath the surface in soil and rock",["In clouds","In the sky","On roofs"],"Sources.")
H('113.d.12.C',3,"Water from a municipal supply passes through a meter and a:",
  "Main shutoff valve",["Chimney","Furnace","Drain"],"Service.")
H('113.d.12.C',4,"A well pump delivers water to a:",
  "Pressure tank",["Chimney","Roof","Drain"],"Well water.")
H('113.d.12.D',3,"A pressure reducing valve protects plumbing from:",
  "High water pressure",["Low pressure","Noise only","Cold"],"Valves.")
H('113.d.12.D',4,"A backflow preventer stops water from:",
  "Flowing backward into the supply",["Moving forward","Freezing","Evaporating"],"Devices.")
H('113.d.13.A',3,"On a floor plan, hot water lines are often drawn as:",
  "Solid lines",["Dashed lines only","No lines","Dotted blue"],"Symbols.")
H('113.d.13.A',4,"A cold water line is often shown with a:",
  "Dashed or distinct line type",["Same as hot","Red color only","No symbol"],"Distinguish.")
H('113.d.13.B',3,"To draw water lines on a plan, a plumber uses a:",
  "Scale and straightedge",["Hammer","Paint","Saw"],"Drawing.")
H('113.d.13.B',4,"Fixtures are shown on the plan with:",
  "Standard symbols",["Photos","Random doodles","Words only"],"Symbols.")
H('113.d.13.C',3,"Sizing a water system starts with counting the:",
  "Fixture units",["Windows","Doors","Floors only"],"Sizing.")
H('113.d.13.C',4,"Higher flow demand requires a:",
  "Larger pipe size",["Smaller pipe","Closed valve","Shorter pipe only"],"Sizing.")
H('113.d.14.A',3,"Open-close valves are used to:",
  "Start and stop flow",["Throttle flow","Reduce pressure","Measure flow"],"Gate and ball valves.")
H('113.d.14.A',4,"A ball valve is shut off with:",
  "A quarter turn",["Ten turns","No motion","A key"],"Quarter-turn.")
H('113.d.14.B',3,"A globe valve is used to:",
  "Regulate flow",["Block flow forever","Measure flow","Heat flow"],"Throttling.")
H('113.d.14.B',4,"Flow regulation valves are not ideal for:",
  "Full-open service with minimal pressure drop",["Throttling","Balancing","Adjusting"],"Selection.")
H('113.d.14.C',3,"A pressure reducing valve is installed where:",
  "Supply pressure is higher than fixtures can handle",["Pressure is already low","No water","Gas is used"],"PRV.")
H('113.d.14.C',4,"A typical house water pressure target is about:",
  "50 to 60 psi",["5 psi","500 psi","1,000 psi"],"Normal.")
H('113.d.14.D',3,"A temperature and pressure relief valve on a water heater opens when:",
  "Pressure or temperature gets too high",["Water is cold","Tank is empty","Power is off"],"Relief.")
H('113.d.14.D',4,"The discharge pipe of a relief valve should point:",
  "Downward to a safe location",["Upward","Toward people","Into the wall"],"Safety.")

# ---------- 127.114 Plumbing II ----------
H('114.d.1.A',3,"A 6-foot folding rule is read to the nearest:",
  "Smallest marked division",["Foot","Yard","Mile"],"Measuring.")
H('114.d.1.A',4,"A 25-foot tape measure has a hook on the end that moves to account for its:",
  "Thickness when measuring inside or outside",["Color","Age","Brand"],"Tape hook.")
H('114.d.1.B',3,"A steel rule is divided into fractions of an inch such as:",
  "1/32 and 1/16",["1/7","1/11","1/13"],"Rule.")
H('114.d.1.B',4,"A micrometer is used when a measurement must be:",
  "Very precise",["Rough","Quick only","Visual"],"Precision.")
H('114.d.1.C',3,"Center-to-center measurement is taken from the middle of:",
  "One fitting to the middle of the other",["The wall","The pipe end","The floor"],"Method.")
H('114.d.1.C',4,"The end-to-center measure is taken from the pipe end to:",
  "The center of a fitting",["The wall","The ceiling","The valve handle"],"Method.")
H('114.d.1.D',3,"A plumber who uses a drill should clamp the work to keep it:",
  "Stable",["Moving","Spinning","Loose"],"Safety.")
H('114.d.1.D',4,"Power saws should be used with the guard in place to prevent:",
  "Injury",["Cooling","Noise","Friction"],"Safe use.")
H('114.d.2.A',3,"A masonry bit is used for drilling:",
  "Concrete or brick",["Glass tubing","Wood only","Steel plate"],"Bits.")
H('114.d.2.A',4,"A hole saw cuts:",
  "Large round holes",["Square holes","Slots","Threads"],"Bits.")
H('114.d.2.B',3,"Twist drill bits are used for drilling:",
  "Metal and wood",["Concrete only","Paper","Water"],"Use.")
H('114.d.2.B',4,"Using a drill bit with the wrong speed for the material can:",
  "Dull the bit and damage the work",["Improve it","Cool the work","Do nothing"],"Application.")
H('114.d.3.A',3,"The volume of a cylinder is found by multiplying pi times radius squared times:",
  "Height",["Weight","Color","Age"],"Formula.")
H('114.d.3.A',4,"A cylinder with a radius of 1 foot and a height of 2 feet has a volume near:",
  "6.28 cubic feet",["3.14 cubic feet","12.56 cubic feet","2 cubic feet"],"3.14 x 1 x 2 = 6.28.")
H('114.d.3.B',3,"A cubic foot of water holds about how many gallons?",
  "7.48",["1","3","10"],"Conversion.")
H('114.d.3.B',4,"A tank 2 ft by 3 ft by 4 ft has a volume of:",
  "24 cubic feet",["9 cubic feet","12 cubic feet","18 cubic feet"],"2 x 3 x 4.")
H('114.d.3.C',3,"A drain pipe that falls 1/4 inch per foot over 20 feet drops a total of:",
  "5 inches",["2 inches","1 inch","20 inches"],"20 x 1/4.")
H('114.d.3.C',4,"Grade is usually expressed as inches of fall per:",
  "Foot",["Mile","Ounce","Gallon"],"Grade.")
H('114.d.3.D',3,"An offset in piping is used to:",
  "Go around an obstruction",["Stop flow","Increase flow","Cool flow"],"Offsets.")
H('114.d.3.D',4,"For parallel offsets, the travel is figured using the offset and the:",
  "Fitting angle",["Color","Price","Weather"],"Travel.")
H('114.d.3.E',3,"Flow rate in a pipe is commonly measured in:",
  "Gallons per minute",["Pounds per inch","Feet","Volts"],"Flow.")
H('114.d.3.E',4,"Friction in a pipe tends to:",
  "Reduce pressure",["Raise pressure","Stop gravity","Heat the sun"],"Friction.")
H('114.d.3.F',3,"Water velocity in pipes is limited to prevent:",
  "Noise and erosion",["Cooling","Saving","Quality"],"Velocity limit.")
H('114.d.3.F',4,"Sizing a pipe too small will make pressure drop:",
  "Greater",["Smaller","Zero","Negative"],"Sizing.")
H('114.d.4.A',3,"A building maintenance technician is a job that may:",
  "Repair plumbing and other systems",["Fly planes","Cook meals","Sing"],"Jobs.")
H('114.d.4.A',4,"A pipefitter installs piping in:",
  "Commercial and industrial settings",["Only farm fields","Only schools","Only parks"],"Pipefitting.")
H('114.d.4.B',3,"Careers in plumbing may require continuing education to:",
  "Stay current with codes",["Learn dances","Paint","Sing"],"Education.")
H('114.d.4.B',4,"Experience and licenses often lead to advancement to:",
  "Master plumber",["Intern forever","Clerk","Helper only"],"Career ladder.")
H('114.d.4.C',3,"The plumbing industry includes contractors, suppliers, and:",
  "Inspectors",["Poets","Models","Actors"],"Industry.")
H('114.d.4.C',4,"A union apprenticeship is sponsored by a:",
  "Joint committee of labor and employers",["Newspaper","School band","Movie studio"],"Associations.")
H('114.d.4.D',3,"Treating company property well includes:",
  "Taking care of tools and vehicles",["Losing tools","Ignoring damage","Using them for hobbies"],"Respect.")
H('114.d.4.D',4,"Customer property should be:",
  "Protected during the work",["Moved without asking","Ignored","Damaged"],"Property.")
H('114.d.4.E',3,"A tidy work area helps a plumber to:",
  "Work safely and efficiently",["Lose items","Slip","Delay"],"Clean.")
H('114.d.4.E',4,"At the end of a job, the plumber should remove:",
  "Debris and packaging",["Customer's furniture","Doors","Light fixtures"],"Cleanup.")
H('114.d.4.F',3,"Using proper methods when installing pipe prevents:",
  "Leaks and rework",["Quality","Safety","Pride"],"Methods.")
H('114.d.4.F',4,"Following the code when installing pipe protects:",
  "The customer and the public",["The paint","The tools","The vans"],"Code.")
H('114.d.5.A',3,"A volt/ohm meter is used on plumbing equipment such as a water heater to check:",
  "Electrical power and elements",["Pipe slope","Water hardness","Pipe size"],"Meters.")
H('114.d.5.A',4,"An electric water heater element is tested for:",
  "Continuity",["Taste","Odor","Color"],"Testing.")
H('114.d.5.B',3,"Hangers are installed to support piping and to allow for:",
  "Expansion",["Rust","Noise","Heat loss"],"Hangers.")
H('114.d.5.B',4,"Holes cut through joists must follow code to avoid:",
  "Weakening the structure",["Strengthening","Cooling","Drying"],"Penetrations.")
H('114.d.5.C',3,"The type of hanger chosen depends on the pipe material, size, and:",
  "Location",["Color","Brand","Age"],"Selecting.")
H('114.d.5.C',4,"A clevis hanger supports pipe from:",
  "Above on a rod",["Below on a floor","Beside only","Inside the pipe"],"Hanger.")
H('114.d.5.D',3,"Pipe supports can be built from:",
  "Strut channel and clamps",["Paper","String","Foam"],"Building supports.")
H('114.d.5.D',4,"A trapeze hanger supports:",
  "Several pipes on one frame",["One valve","One wire","A drain"],"Trapeze.")
H('114.d.5.E',3,"Where pipes pass through a fire-rated wall, the opening must be:",
  "Fire-stopped",["Left open","Covered with paper","Painted"],"Penetration.")
H('114.d.5.E',4,"Sleeves through foundation walls protect the pipe and allow:",
  "Movement",["Rust","Noise","Leaks"],"Code.")
H('114.d.5.F',3,"A roof drain collects:",
  "Rainwater from a flat roof",["Sewage","Gas","Hot water"],"Roof drains.")
H('114.d.5.F',4,"Roof drain size depends on the roof area and local:",
  "Rainfall rate",["Paint color","Truck type","Brand"],"Sizing.")
H('114.d.6.A',3,"Before installing a toilet, the flange should be checked to see that it is:",
  "Secure and level",["Missing","Bent","Rusted through"],"Toilet.")
H('114.d.6.A',4,"A wax ring seals the toilet to the:",
  "Flange",["Wall","Tank","Seat"],"Seal.")
H('114.d.6.B',3,"A faucet is connected to the supply lines with:",
  "Compression or threaded fittings",["Glue","Nails","Tape alone"],"Faucets.")
H('114.d.6.B',4,"A sink drain requires a trap and a:",
  "Tailpiece",["Compressor","Burner","Fan"],"Sinks.")
H('114.d.7.A',3,"Piping plan types include plan view, elevation, and:",
  "Isometric",["Poem","Menu","Calendar"],"Types.")
H('114.d.7.A',4,"An elevation drawing shows a view from the:",
  "Side",["Top","Below","Inside only"],"Types.")
H('114.d.7.B',3,"A piping symbol for a tee shows a:",
  "Branch connection",["Valve stop","Pump","Tank"],"Symbols.")
H('114.d.7.B',4,"A detail drawing shows a:",
  "Close-up of a specific connection",["Whole city","Weather","Calendar"],"Detail.")
H('114.d.7.C',3,"A field sketch is a quick drawing made:",
  "On the job site",["In a museum","At a bank","In a movie"],"Sketch.")
H('114.d.7.C',4,"A good field sketch includes dimensions and:",
  "Notes",["Jokes","Colors only","Songs"],"Sketch.")
H('114.d.7.D',3,"A line list tells the size, material, and service of each:",
  "Pipe line",["Employee","Truck","Tool"],"Lists.")
H('114.d.7.D',4,"A drawing index lists:",
  "All sheets in the set",["Employees","Hours","Fuel"],"Index.")
H('114.d.8.A',3,"Valves that start and stop flow include gate valves and:",
  "Ball valves",["Check valves","Globe valves","Pressure valves"],"On-off valves.")
H('114.d.8.A',4,"A butterfly valve closes with a:",
  "Rotating disc",["Plunger","Spring","Plug"],"Types.")
H('114.d.8.B',3,"Valves that regulate flow include globe valves and:",
  "Needle valves",["Gate valves","Ball valves","Check valves"],"Throttle.")
H('114.d.8.B',4,"A needle valve is used for:",
  "Fine adjustment of small flow",["Fast shutoff","Large flow","Draining"],"Flow control.")
H('114.d.8.C',3,"A relief valve opens to:",
  "Relieve excess pressure",["Increase pressure","Block flow","Measure pressure"],"Relief.")
H('114.d.8.C',4,"A safety valve is typically used on:",
  "Steam and boiler systems",["Rainwater","Toilets","Fountains"],"Safety valve.")
H('114.d.8.D',3,"A check valve allows flow in:",
  "One direction only",["Both directions","No direction","Circles"],"Check.")
H('114.d.8.D',4,"A swing check valve uses a:",
  "Hinged disc",["Rotating ball","Diaphragm only","Gear"],"Types.")
H('114.d.8.E',3,"A valve actuator opens and closes a valve using a:",
  "Motor, air, or hydraulic power",["Hand only","String","Wind"],"Actuators.")
H('114.d.8.E',4,"An electric actuator is controlled by a:",
  "Switch or control signal",["Hose","Blade","Gear oil"],"Control.")
H('114.d.8.F',3,"Valves should be stored with the ends:",
  "Capped to keep out debris",["Open","Wet","Bent"],"Storage.")
H('114.d.8.F',4,"A large valve should be lifted using:",
  "Proper rigging",["Bare hands","Rope on the handle","Foot"],"Handling.")
H('114.d.8.G',3,"A valve installed in the line near a fixture is often called a:",
  "Stop valve",["Pump","Tank","Filter"],"Locations.")
H('114.d.8.G',4,"A valve position indicator shows whether it is:",
  "Open or closed",["Hot or cold","Wet or dry","New or used"],"Position.")
H('114.d.8.H',3,"Valve selection depends on the pressure, temperature, and:",
  "Fluid being carried",["Color","Brand","Age"],"Selection.")
H('114.d.8.H',4,"A valve for steam service must be rated for:",
  "High temperature and pressure",["Low temperature only","Sunlight","Sound"],"Rating.")
H('114.d.8.I',3,"Valve nameplate data includes size, pressure rating, and:",
  "Material",["Owner","Weather","Color of truck"],"Nameplate.")
H('114.d.8.I',4,"The letters WOG on a valve stand for:",
  "Water, oil, gas",["Wood, oak, glass","Wind, oxygen, gravity","Water, oxygen, ground"],"Markings.")
H('114.d.9.A',3,"An oxy-fuel torch has a regulator, hoses, and a:",
  "Torch handle with tips",["Mirror","Drill","Saw"],"Parts.")
H('114.d.9.A',4,"The regulator on a gas cylinder reduces:",
  "Cylinder pressure to working pressure",["Temperature","Volume","Weight"],"Regulator.")
H('114.d.9.B',3,"Before opening a cylinder valve, the regulator adjusting screw should be:",
  "Backed out (released)",["Tightened fully","Removed","Painted"],"Procedure.")
H('114.d.9.B',4,"When lighting a torch, always use a:",
  "Striker",["Match near fuel","Cigarette lighter in a cylinder","Candle"],"Lighting.")
H('114.d.9.C',3,"A flux is used when soldering to:",
  "Clean oxides and help solder flow",["Cool metal","Add color","Add weight"],"Flux.")
H('114.d.9.C',4,"Brazing filler metals melt above:",
  "840 degrees Fahrenheit",["200 degrees","400 degrees","32 degrees"],"Brazing.")
H('114.d.9.D',3,"Gas cylinders must be stored upright and:",
  "Chained or secured",["Loose","On their side","Open"],"Cylinder safety.")
H('114.d.9.D',4,"Welding goggles protect the eyes from:",
  "Bright light and sparks",["Cold","Water","Dust only"],"Safety.")
H('114.d.10.A',3,"Water pressure and flow are critical for sizing a water system, along with the pipe:",
  "Length and fittings",["Color","Brand","Weight"],"Factors.")
H('114.d.10.A',4,"Developed length of pipe includes the straight pipe and the equivalent length of:",
  "Fittings",["Paint","Hangers","Sleeves"],"Developed length.")
H('114.d.10.B',3,"Fixture units are values that represent a fixture's:",
  "Demand on the system",["Cost","Color","Age"],"Fixture units.")
H('114.d.10.B',4,"A bathtub has a higher fixture unit value than a:",
  "Lavatory",["Shower valve only","Hose","Tub"],"Values.")
H('114.d.10.C',3,"Water pipe is installed with the proper:",
  "Slope for draining and supports",["Color","Smell","Noise"],"Installation.")
H('114.d.10.C',4,"Piping should be protected from freezing by:",
  "Insulating or routing in heated spaces",["Painting","Leaving bare outdoors","Sealing tight"],"Protection.")
H('114.d.10.D',3,"A water piping system is tested with water or air at a pressure of at least:",
  "The working pressure",["Zero","1 psi","Double the sun"],"Test.")
H('114.d.10.D',4,"During a pressure test, the gauge should:",
  "Hold steady for the required time",["Fall to zero","Rise forever","Be removed"],"Test.")
H('114.d.11.A',3,"Backflow caused by a vacuum in the supply is called:",
  "Back-siphonage",["Back-pressure","Overflow","Condensation"],"Backflow.")
H('114.d.11.A',4,"Back-pressure backflow occurs when pressure downstream is:",
  "Greater than supply pressure",["Lower","Equal","Zero"],"Backflow.")
H('114.d.11.B',3,"A pollutant that can make people sick is called a:",
  "Contaminant",["Fixture","Valve","Strainer"],"Hazard.")
H('114.d.11.B',4,"A high hazard connection involves a substance that is:",
  "Toxic",["Harmless","Clean water","Pure"],"Degree of hazard.")
H('114.d.11.C',3,"An air gap protects a cross connection by providing:",
  "A physical separation in air",["A longer pipe","A valve only","A filter"],"Protection.")
H('114.d.11.C',4,"A reduced-pressure zone device is a:",
  "Backflow assembly for high hazards",["Faucet","Tank","Trap"],"RPZ.")
H('114.d.12.A',3,"When sizing a natural gas system, factors include appliance demand and pipe:",
  "Length",["Color","Smell","Brand"],"Gas sizing.")
H('114.d.12.A',4,"Gas appliance input is rated in:",
  "BTU per hour",["Gallons","Pounds","Volts"],"Demand.")
H('114.d.12.B',3,"A gas pipe system is tested by pressurizing with air or an inert gas and checking:",
  "For leaks",["For color","For smell only","For sound"],"Testing.")
H('114.d.12.B',4,"Gas piping must never be tested with:",
  "Oxygen",["Nitrogen","Dry air","Inert gas"],"Test safe.")
H('114.d.13.A',3,"A DWV fitting that makes a long sweep turn is a:",
  "Long-turn elbow",["Tee","Cap","Plug"],"Fittings.")
H('114.d.13.A',4,"A closet flange connects a toilet to the:",
  "Drain",["Vent","Supply","Roof"],"Fittings.")
H('114.d.13.B',3,"A DWV system is sized by the drainage fixture units and pipe:",
  "Slope and length",["Color","Brand","Hangers"],"Sizing.")
H('114.d.13.B',4,"A 3-inch drain is chosen over a 2-inch when the load in fixture units is:",
  "Greater",["Smaller","Zero","Negative"],"Sizing.")
H('114.d.13.C',3,"Common DWV materials include PVC, ABS, and:",
  "Cast iron",["Brass pipe","Paper","Foam"],"Materials.")
H('114.d.13.C',4,"ABS pipe is typically black and is joined with:",
  "ABS solvent cement",["PVC primer","Solder","Brazing"],"Material.")
H('114.d.13.D',3,"The slope of a pipe is found by dividing the fall by the:",
  "Run",["Diameter","Weight","Cost"],"Slope formula.")
H('114.d.13.D',4,"A 40-foot horizontal drain with 1/4 inch per foot slope falls:",
  "10 inches",["4 inches","40 inches","1 inch"],"40 x 1/4.")
H('114.d.13.E',3,"DWV systems are commonly tested with a water test or an:",
  "Air test",["Color test","Weight test","Smell test"],"Testing.")
H('114.d.13.E',4,"A test tee or plug is used to:",
  "Seal openings for the test",["Open pipes","Cool pipes","Drain pipes"],"Test.")
H('114.d.13.F',3,"The vent stack extends through the:",
  "Roof",["Foundation","Basement slab","Window"],"Vent.")
H('114.d.13.F',4,"A vent terminal must be placed away from:",
  "Windows and air intakes",["Roofs","Walls","Chimneys"],"Vent location.")
H('114.d.14.A',3,"A storage tank water heater keeps hot water in a:",
  "Insulated tank",["Open pit","Coil only","Filter"],"Heaters.")
H('114.d.14.A',4,"A tankless water heater heats water:",
  "On demand as it flows",["All day","Never","In a tank"],"Point of use.")
H('114.d.14.B',3,"An electric water heater has heating elements, a thermostat, and a:",
  "Relief valve",["Chimney","Burner","Flue"],"Parts.")
H('114.d.14.B',4,"A gas water heater has a burner, a thermocouple, and a:",
  "Flue",["Element","Heat pump","Solar panel"],"Parts.")
H('114.d.14.C',3,"A water heater installation includes a T&P relief valve and a:",
  "Discharge pipe",["Doorbell","Hose bib","Mixer"],"Install.")
H('114.d.14.C',4,"A gas water heater requires combustion air and:",
  "Proper venting",["A drain only","Electric elements","Solar panels"],"Install.")
H('112.d.8.B',5,"A programmable thermostat with a night setback of several degrees in winter mainly reduces:",
  "Heating energy use during the setback period",["Duct leakage","Filter pressure drop","Refrigerant charge"],"Setback lowers load.")
H('112.d.8.I',5,"To measure the current draw of one conductor safely, a technician uses a clamp meter around:",
  "A single conductor",["Both conductors together","The ground wire only","The whole cable bundle"],"Fields cancel if both are enclosed.")
H('113.d.4.A',5,"Jaws of a pipe wrench are designed to bite when pressure is applied in the direction of the:",
  "Open hook jaw movement",["Handle's blank side","Closed knuckle","Adjusting nut"],"Pull toward the hook jaw.")
H('113.d.6.E',5,"In orthographic projection of a pipe offset, the true length of the angled run appears in:",
  "The view where the run is parallel to the plane",["Every view","Never in any view","Only the top view always"],"True length requires parallel view.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_20.jsonl'))

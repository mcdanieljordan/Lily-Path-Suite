#!/usr/bin/env python3
"""High school Integrated Physics and Chemistry (TEKS 112.44.c). Original questions. Strands 5-8."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.44.c.', 988, own='hs_ipc.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 5.A motion
H('5.A', 2, "A runner covers 60 m in 10 s at a steady pace. What is the speed?", "6 m/s", ["600 m/s", "0.17 m/s", "50 m/s"], "Speed = distance ÷ time.")
H('5.A', 3, "A car speeds up from 10 m/s to 30 m/s in 5 s. What is its acceleration?", "4 m/s²", ["20 m/s²", "6 m/s²", "100 m/s²"], "a = (30 − 10) ÷ 5.")
H('5.A', 3, "On a distance-time graph, a straight line that slopes upward shows what?", "constant speed", ["constant acceleration", "no motion", "speeding up faster and faster"], "Equal distances are covered in equal times.")
H('5.A', 2, "On a distance-time graph, what does a flat horizontal line show?", "the object is at rest", ["the object moves at constant speed", "the object is accelerating", "the object is turning"], "Distance does not change.")

# 5.B mass, force, acceleration
H('5.B', 3, "A 5 kg cart is pushed with a net force of 20 N. What is its acceleration?", "4 m/s²", ["100 m/s²", "0.25 m/s²", "15 m/s²"], "a = F ÷ m.")
H('5.B', 3, "The same net force pushes a light cart and a heavy cart. Which accelerates more?", "the light cart", ["the heavy cart", "both the same", "neither moves"], "Acceleration is inversely related to mass.")
H('5.B', 3, "If the net force on an object doubles and its mass stays the same, what happens to its acceleration?", "it doubles", ["it is halved", "it stays the same", "it quadruples"], "Acceleration is proportional to net force.")
H('5.B', 4, "What net force is needed to give a 12 kg object an acceleration of 2 m/s²?", "24 N", ["6 N", "14 N", "0.17 N"], "F = ma.")

# 5.C momentum and impulse
H('5.C', 3, "What is the momentum of a 3 kg ball moving at 4 m/s?", "12 kg·m/s", ["7 kg·m/s", "0.75 kg·m/s", "1.3 kg·m/s"], "p = mv.")
H('5.C', 3, "Why does a helmet's soft inner foam reduce injury in a crash?", "it lengthens the time of impact, lowering the force", ["it raises the force of impact", "it reduces the head's mass", "it speeds up the head"], "A longer stopping time means a smaller force for the same change in momentum.")
H('5.C', 3, "Which design feature of a car lowers the force on passengers during a crash?", "crumple zones that collapse gradually", ["a rigid frame that never bends", "a lighter steering wheel", "a faster engine"], "They extend the collision time.")
H('5.C', 4, "A catcher pulls a mitt backward while catching a fast ball. Why?", "to increase the stopping time and reduce the force on the hand", ["to increase the ball's momentum", "to make the ball heavier", "to speed up the ball"], "Impulse equals force times time.")

# 5.D four fundamental forces
H('5.D', 2, "Which fundamental force holds protons and neutrons together in a nucleus?", "the strong nuclear force", ["gravity", "friction", "the weak nuclear force"], "It overcomes the repulsion between protons.")
H('5.D', 3, "Which fundamental force is responsible for some types of radioactive decay?", "the weak nuclear force", ["gravity", "the strong nuclear force", "friction"], "It governs processes such as beta decay.")
H('5.D', 2, "Which fundamental force keeps planets in orbit around the Sun?", "gravitation", ["electromagnetic force", "the weak nuclear force", "magnetism only"], "Mass attracts mass.")
H('5.D', 3, "Which force acts between charged particles?", "the electromagnetic force", ["gravity only", "the strong nuclear force only", "no force"], "Like charges repel and opposite charges attract.")

# 5.E mass, charge, distance
H('5.E', 3, "If the distance between two objects doubles, what happens to the gravitational force between them?", "it becomes one-fourth", ["it is halved", "it doubles", "it stays the same"], "The force follows an inverse square law.")
H('5.E', 3, "If the mass of one of two objects doubles, what happens to the gravitational force between them?", "it doubles", ["it is halved", "it becomes one-fourth", "it stays the same"], "Force is proportional to mass.")
H('5.E', 3, "If the distance between two charged objects triples, what happens to the electric force?", "it becomes one-ninth", ["it becomes one-third", "it triples", "it is nine times larger"], "Electric force also follows an inverse square law.")
H('5.E', 3, "Two charged objects repel each other. What is true about their charges?", "they are the same sign", ["they are opposite signs", "one of them is neutral", "they have no mass"], "Like charges repel.")

# 6.A circuits
H('6.A', 3, "In a series circuit, what happens when one bulb is removed?", "the circuit is broken and all bulbs go out", ["the other bulbs stay lit", "the other bulbs get brighter", "nothing changes"], "There is only one path.")
H('6.A', 3, "Why are the outlets in a home wired in parallel?", "so each device works independently at full voltage", ["so all devices share one path", "so that voltage is divided", "so that current does not flow"], "Each branch has its own path.")
H('6.A', 3, "Two resistors of 4 Ω and 6 Ω are in series. What is the total resistance?", "10 Ω", ["2.4 Ω", "24 Ω", "5 Ω"], "Resistances add in series.")
H('6.A', 3, "A 12 V source drives a 6 Ω resistor. What is the current?", "2 A", ["72 A", "0.5 A", "18 A"], "I = V ÷ R.")

# 6.B generating electrical energy
H('6.B', 3, "How does a generator produce electricity?", "a coil moves in a magnetic field", ["a magnet is heated", "a battery is recharged", "a bulb is lit"], "Moving conductors in a magnetic field induce a current.")
H('6.B', 3, "Which energy conversion happens in a wind turbine generator?", "kinetic energy of wind to electrical energy", ["chemical energy to light", "nuclear energy to sound", "heat to wind"], "The blades turn a generator.")
H('6.B', 4, "A hand-crank flashlight lights up while you turn the handle. What energy change occurs?", "mechanical energy into electrical energy into light", ["light into mechanical energy", "sound into heat", "electrical energy into mass"], "Cranking spins a small generator.")

# 6.C conservation of energy
H('6.C', 3, "What does the law of conservation of energy say?", "energy cannot be created or destroyed, only transformed", ["energy is created when objects move", "energy disappears as heat", "energy is used up completely"], "The total energy of a closed system stays constant.")
H('6.C', 3, "A pendulum swings back and forth and gradually stops. Where does its mechanical energy go?", "into thermal energy through air resistance and friction", ["it is destroyed", "it is stored as mass", "it becomes magnetic"], "The energy spreads out as heat.")
H('6.C', 3, "A ball at the top of a hill has 100 J of gravitational potential energy. If it rolls to the bottom without friction, how much kinetic energy does it have there?", "all 100 joules of the starting potential energy", ["none of it", "half of it", "twice as much"], "Energy is conserved.")
H('6.C', 4, "A closed system contains 40 J of kinetic energy and 60 J of potential energy. What is the total energy later if nothing enters or leaves?", "100 J", ["40 J", "60 J", "20 J"], "Total energy stays constant.")

# 6.D thermal energy transfer
H('6.D', 2, "How does thermal energy move through a solid metal spoon placed in hot soup?", "conduction", ["convection", "radiation", "evaporation"], "Heat passes from particle to particle.")
H('6.D', 3, "How does thermal energy move in a pot of boiling water?", "convection", ["conduction only", "radiation only", "reflection"], "Warm fluid rises and cooler fluid sinks.")
H('6.D', 3, "How does heat from the Sun reach Earth?", "radiation", ["conduction", "convection", "condensation"], "Radiation does not need a medium.")
H('6.D', 3, "Why do metal handles feel colder than wood handles at the same temperature?", "metal conducts heat away from your hand faster", ["metal is actually colder", "wood produces heat", "metal blocks heat flow"], "Metals are good thermal conductors.")

# 6.E transfer of energy through materials
H('6.E', 3, "Which kind of material is a good electrical conductor?", "copper", ["rubber", "glass", "plastic"], "Metals have free-moving electrons.")
H('6.E', 3, "Which material is the best electrical insulator?", "rubber", ["copper", "silver", "iron"], "Rubber does not allow current to flow easily.")
H('6.E', 3, "Why are electrical wires covered with plastic?", "plastic is an insulator that prevents shocks and short circuits", ["plastic makes electricity travel faster", "plastic stores electricity", "plastic is a conductor"], "It keeps charge on the wire.")
H('6.E', 4, "Fiber-optic cables carry information using what?", "pulses of light", ["pulses of sound", "heat waves", "magnetic poles"], "Light signals travel through glass fibers.")

# 6.F waves
H('6.F', 3, "When two waves meet and combine to form a larger wave, this is called what?", "constructive interference", ["destructive interference", "refraction", "reflection"], "Crests line up with crests.")
H('6.F', 3, "Noise-canceling headphones work mainly by using what?", "destructive interference", ["constructive interference", "reflection", "refraction"], "A wave that is opposite to the noise cancels it out.")
H('6.F', 3, "A straw looks bent in a glass of water. What causes this?", "refraction of light", ["reflection of light", "interference of sound", "diffraction of sound"], "Light changes speed and bends between water and air.")
H('6.F', 3, "An echo is caused by which wave behavior?", "reflection", ["refraction", "diffraction", "absorption only"], "Sound bounces off a hard surface.")

# 6.G energy sources
H('6.G', 2, "Which of these energy sources is renewable?", "solar", ["coal", "natural gas", "petroleum"], "The Sun is a continuing source.")
H('6.G', 2, "Which of these energy sources is nonrenewable?", "coal", ["wind", "solar", "hydroelectric"], "Fossil fuels take millions of years to form.")
H('6.G', 3, "What is one disadvantage of wind power?", "it depends on wind being available", ["it releases large amounts of carbon dioxide", "it uses up fossil fuels", "it produces radioactive waste"], "Output varies with weather.")
H('6.G', 3, "What is one advantage of nuclear power plants?", "they produce electricity without releasing carbon dioxide during operation", ["they produce no waste", "they run on coal", "they are cheap to build"], "But they create radioactive waste that must be stored.")

# 7.A atomic structure
H('7.A', 2, "Which particle in an atom has a positive charge?", "proton", ["electron", "neutron", "photon"], "Protons are in the nucleus.")
H('7.A', 2, "What determines the identity of an element?", "the number of protons", ["the number of neutrons", "the number of electrons only", "the mass only"], "Atomic number equals the number of protons.")
H('7.A', 3, "An atom has 6 protons and 6 neutrons. What is its mass number?", "12", ["6", "18", "0"], "Mass number is protons plus neutrons.")
H('7.A', 3, "Why are the noble gases generally unreactive?", "their outer energy level is full", ["they have no electrons", "they have only one electron", "they have a positive charge"], "A full outer shell is stable.")

# 7.B periodic table patterns
H('7.B', 2, "Elements in the same group of the periodic table share what?", "the same number of valence electrons", ["the same mass", "the same number of protons", "the same state at room temperature"], "This gives them similar chemical properties.")
H('7.B', 3, "Moving from left to right across a period, what happens to atomic number?", "it increases", ["it decreases", "it stays the same", "it becomes zero"], "Each element has one more proton.")
H('7.B', 3, "Which group of elements is the most reactive metals?", "alkali metals", ["noble gases", "halogens", "transition metals"], "They easily lose one electron.")
H('7.B', 3, "Which of these elements is expected to be most like sodium in its chemical behavior?", "potassium", ["chlorine", "helium", "oxygen"], "They are in the same group.")

# 7.C properties and uses
H('7.C', 3, "Why is aluminum often used to make drink cans?", "it is lightweight and resists corrosion", ["it is magnetic", "it is a gas", "it is a good insulator"], "Its properties suit the use.")
H('7.C', 3, "Why is copper used in electrical wiring?", "it is a good conductor of electricity and is ductile", ["it is brittle", "it is an insulator", "it is very light"], "It can be drawn into wires.")
H('7.C', 3, "Why is helium used to fill party balloons?", "it is less dense than air and unreactive", ["it is heavier than air", "it is very reactive", "it is a liquid"], "It floats safely.")
H('7.C', 4, "Why is diamond used in cutting tools?", "it is extremely hard", ["it is very soft", "it conducts electricity", "it is a liquid"], "Its covalent network structure makes it very hard.")

# 7.D electron transitions
H('7.D', 3, "What happens when an excited electron falls to a lower energy level?", "a photon is emitted", ["a proton is absorbed", "the nucleus splits", "a neutron is released"], "The energy difference is given off as light.")
H('7.D', 3, "Why do different elements produce different colors in a flame test?", "their electrons have different energy-level gaps", ["they have the same protons", "they have different densities", "they have the same mass"], "Different gaps give different photon energies.")
H('7.D', 4, "A larger energy drop between levels produces a photon with what?", "higher frequency", ["lower frequency", "no energy", "longer wavelength"], "E = hf.")
H('7.D', 3, "Neon signs glow because of what process?", "excited gas atoms emit light as electrons return to lower levels", ["the gas burns", "the gas melts", "the gas turns into a solid"], "An electric current excites the gas.")

# 7.E atomic energy levels and wave-particle duality
H('7.E', 4, "Atomic emission spectra show only certain wavelengths. What does this suggest about electron energy?", "it is quantized", ["it is continuous", "it is random", "it is zero"], "Only specific energy changes are allowed.")
H('7.E', 4, "Which property of light does the photon model highlight?", "it comes in discrete packets of energy", ["it has no energy", "it needs a medium", "it is a sound wave"], "Each photon has energy E = hf.")
H('7.E', 4, "An electron diffraction pattern shows that electrons can behave like what?", "waves", ["sound", "heat", "magnets only"], "Matter shows wave properties.")
H('7.E', 3, "Wave-particle duality means that light and matter can show what?", "both wave and particle behavior", ["only wave behavior", "only particle behavior", "neither behavior"], "The behavior seen depends on the experiment.")

# 7.F reaction rate
H('7.F', 3, "How does raising the temperature usually affect the rate of a reaction?", "it speeds it up", ["it slows it down", "it stops it", "it has no effect"], "Particles collide more often and with more energy.")
H('7.F', 3, "Which sugar dissolves fastest in water?", "powdered sugar", ["a large sugar cube", "a single large crystal", "rock candy"], "Greater surface area speeds up dissolving.")
H('7.F', 3, "How does stirring affect the rate of dissolving?", "it increases the rate", ["it decreases the rate", "it has no effect", "it stops dissolving"], "Fresh solvent contacts the solute.")
H('7.F', 4, "How does a catalyst change a reaction?", "it speeds the reaction without being used up", ["it is used up as a reactant", "it slows the reaction", "it changes the products"], "It lowers the activation energy.")

# 8.A evidence of chemical reactions
H('8.A', 2, "Which of these is a sign of a chemical reaction?", "a gas is produced and bubbles form", ["ice melts", "a sheet of paper is folded", "sugar dissolves in water"], "A new substance is formed.")
H('8.A', 3, "Which change is a physical change?", "water freezing", ["iron rusting", "wood burning", "milk souring"], "No new substance forms.")
H('8.A', 3, "Which observation is the best evidence that a chemical change took place?", "a new substance with different properties formed", ["a substance changed shape", "a substance changed size", "a substance was cut"], "Chemical changes make new substances.")
H('8.A', 3, "Hydrochloric acid is added to a metal and bubbles appear. What does this most likely indicate?", "a chemical reaction producing a gas", ["a physical change", "a change of state only", "a dissolving process only"], "Gas formation is evidence of a reaction.")

# 8.B conservation of mass
H('8.B', 3, "In a balanced chemical equation, what must be the same on both sides?", "the number of each type of atom", ["the number of molecules", "the volume", "the color"], "Atoms are conserved.")
H('8.B', 3, "Hydrogen and oxygen react to form water. If 4 g of hydrogen react with 32 g of oxygen, what mass of water forms?", "36 g", ["28 g", "32 g", "128 g"], "Mass is conserved.")
H('8.B', 4, "Which is the correctly balanced equation?", "2H₂ + O₂ → 2H₂O", ["H₂ + O₂ → H₂O", "2H₂ + 2O₂ → 2H₂O", "H₂ + 2O₂ → 2H₂O"], "Each side has 4 H atoms and 2 O atoms.")
H('8.B', 3, "A student burns a candle in an open container and the mass seems to decrease. Why?", "gaseous products escaped into the air", ["mass was destroyed", "the flame has negative mass", "the wax became energy"], "Mass is conserved when all products are counted.")

# 8.C nuclear reactions
H('8.C', 3, "What is nuclear fission?", "the splitting of a large nucleus into smaller nuclei", ["the joining of small nuclei", "the burning of fuel", "the freezing of a gas"], "It releases a great deal of energy.")
H('8.C', 3, "What is nuclear fusion?", "the joining of small nuclei to form a larger nucleus", ["the splitting of a nucleus", "the burning of coal", "the melting of a solid"], "It powers the Sun.")
H('8.C', 3, "Which technology uses radioactive isotopes?", "medical imaging and cancer treatment", ["bicycle brakes", "wind turbines", "solar panels"], "Isotopes can be used as tracers and for treatment.")
H('8.C', 4, "What is one disadvantage of using nuclear fission for electricity?", "it produces radioactive waste that must be stored safely", ["it releases large amounts of carbon dioxide", "it uses up all the wind", "it requires sunlight"], "Waste stays radioactive for a long time.")

# 8.D environmental impact
H('8.D', 3, "Burning fossil fuels releases which gas that contributes to climate change?", "carbon dioxide", ["helium", "argon", "neon"], "It traps heat in the atmosphere.")
H('8.D', 3, "What causes acid rain?", "sulfur and nitrogen oxides reacting with water in the air", ["too much oxygen", "too much helium", "ice melting"], "These oxides form acids in the atmosphere.")
H('8.D', 3, "Which practice helps reduce the environmental impact of chemical products?", "recycling and proper disposal", ["pouring chemicals down storm drains", "burning all waste", "dumping waste in streams"], "Proper handling prevents pollution.")
H('8.D', 4, "A catalytic converter in a car reduces what?", "harmful exhaust gases", ["the car's mass", "the number of wheels", "the engine's noise only"], "It converts pollutants into less harmful substances.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_ipc.jsonl'))

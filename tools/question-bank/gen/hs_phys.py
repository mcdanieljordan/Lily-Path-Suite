#!/usr/bin/env python3
"""High school Physics (TEKS 112.45.c). Original questions. Strands 1-4 (practices) skipped; content strands 5-9."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.45.c.', 987, own='hs_phys.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 5.A motion graphs
H('5.A', 2, "On a position-versus-time graph, what does the slope of the line represent?", "velocity", ["acceleration", "displacement", "force"], "Change in position divided by change in time is velocity.")
H('5.A', 3, "On a velocity-versus-time graph, what does the slope of the line represent?", "acceleration", ["position", "distance", "mass"], "Change in velocity divided by change in time is acceleration.")
H('5.A', 3, "On a velocity-versus-time graph, what does the area between the line and the time axis represent?", "displacement", ["acceleration", "force", "power"], "Velocity times time gives displacement.")
H('5.A', 2, "What does a horizontal line on a position-versus-time graph show?", "the object is at rest", ["constant acceleration", "constant velocity greater than zero", "the object is speeding up"], "The position does not change.")
H('5.A', 3, "A velocity-versus-time graph shows a straight line sloping upward from the origin. What kind of motion is this?", "constant acceleration from rest", ["constant velocity", "no motion", "constant deceleration"], "Velocity increases steadily.")

# 5.B scalars and vectors
H('5.B', 2, "Which of these is a vector quantity?", "velocity", ["speed", "mass", "distance"], "A vector has both magnitude and direction.")
H('5.B', 2, "Which of these is a scalar quantity?", "speed", ["displacement", "force", "velocity"], "A scalar has magnitude only.")
H('5.B', 3, "A 3 N force acts east and a 4 N force acts north on an object. What is the magnitude of the net force?", "5 N", ["7 N", "1 N", "12 N"], "√(3² + 4²) = 5.")
H('5.B', 3, "A 6 N force acts east and a 2 N force acts west on an object. What is the net force?", "4 N east", ["8 N east", "4 N west", "12 N east"], "Subtract opposite forces.")
H('5.B', 3, "A runner completes one lap around a 400 m track and returns to the start. What is the runner's displacement?", "0 m", ["400 m", "200 m", "800 m"], "Displacement compares the final position with the starting position.")

# 5.C one-dimensional motion
H('5.C', 2, "A cyclist travels 100 m in 20 s at a constant speed. What is the speed?", "5 m/s", ["2000 m/s", "0.2 m/s", "80 m/s"], "Speed = distance ÷ time.")
H('5.C', 3, "A car goes from 0 to 20 m/s in 5 s. What is its acceleration?", "4 m/s²", ["100 m/s²", "0.25 m/s²", "15 m/s²"], "a = Δv ÷ t.")
H('5.C', 3, "A car starts from rest and accelerates at 2 m/s² for 5 s. How far does it travel?", "25 m", ["10 m", "50 m", "5 m"], "d = ½at² = ½(2)(25).")
H('5.C', 3, "Ignoring air resistance, about how fast is an object falling after 3 s of free fall from rest? (g ≈ 9.8 m/s²)", "29.4 m/s", ["9.8 m/s", "3.3 m/s", "88 m/s"], "v = gt.")
H('5.C', 3, "A person walks 3 m east and then 3 m west. What is the total distance traveled?", "6 m", ["0 m", "3 m", "9 m"], "Distance adds up all of the path length.")

# 5.D circular and projectile motion
H('5.D', 3, "In uniform circular motion, in which direction does the acceleration point?", "toward the center of the circle", ["along the direction of motion", "away from the center", "it is zero"], "Centripetal acceleration points inward.")
H('5.D', 3, "An object moves at 4 m/s on a circle of radius 2 m. What is its centripetal acceleration?", "8 m/s²", ["2 m/s²", "16 m/s²", "0.5 m/s²"], "a = v² ÷ r = 16 ÷ 2.")
H('5.D', 3, "Ignoring air resistance, what happens to the horizontal velocity of a horizontally launched projectile?", "it stays constant", ["it increases", "it decreases", "it reverses"], "No horizontal force acts on it.")
H('5.D', 4, "One ball is dropped and another is launched horizontally from the same height at the same moment. Ignoring air resistance, which lands first?", "they land at the same time", ["the dropped ball", "the launched ball", "it depends on mass"], "Vertical motion is identical for both.")
H('5.D', 4, "An object moves in a circle at constant speed. Why is it accelerating?", "its direction of velocity keeps changing", ["its speed keeps changing", "no force acts on it", "its mass keeps changing"], "Velocity is a vector, and its direction changes.")

# 5.E Newton's first law
H('5.E', 2, "According to Newton's first law, what happens to a moving object with no net force on it?", "it continues moving at constant velocity", ["it slows down", "it stops immediately", "it speeds up"], "Objects keep their motion unless acted on by a net force.")
H('5.E', 2, "What is inertia?", "the tendency of an object to resist changes in its motion", ["the force of gravity", "the speed of an object", "the energy of an object"], "More mass means more inertia.")
H('5.E', 3, "Which quantity is a measure of an object's inertia?", "mass", ["velocity", "acceleration", "weight only"], "Greater mass resists change in motion more.")
H('5.E', 3, "A passenger lurches forward when a car brakes suddenly. Which idea explains this?", "inertia", ["friction increases", "gravity pulls forward", "action and reaction"], "The body tends to keep moving.")
H('5.E', 3, "What is true about the net force on an object in equilibrium?", "it is zero", ["it is greater than zero", "it points downward", "it equals the weight"], "Forces balance.")

# 5.F forces
H('5.F', 3, "What is the net force on a 10 kg object accelerating at 3 m/s²?", "30 N", ["3.3 N", "13 N", "7 N"], "F = ma.")
H('5.F', 3, "What is the weight of a 5 kg object near Earth's surface? (g ≈ 9.8 m/s²)", "49 N", ["5 N", "0.5 N", "4.9 N"], "W = mg.")
H('5.F', 3, "A 20 N force pushes a box right and a 5 N friction force pushes left. What is the net force?", "15 N right", ["25 N right", "15 N left", "100 N right"], "Subtract the opposing force.")
H('5.F', 2, "Which force acts perpendicular to a surface and supports an object resting on it?", "the normal force", ["friction", "tension", "centripetal force"], "It pushes away from the surface.")
H('5.F', 3, "Which force keeps a car moving in a circle on a flat curve?", "friction between the tires and the road, acting as a centripetal force", ["the engine force forward", "gravity pulling outward", "a force pointing away from the center"], "A center-directed force is needed.")

# 5.G Newton's third law
H('5.G', 2, "According to Newton's third law, forces between two objects are what?", "equal in size and opposite in direction", ["equal and in the same direction", "different in size", "always zero"], "For every action there is an equal and opposite reaction.")
H('5.G', 3, "A rocket moves forward when it pushes exhaust gas backward. Which law explains this?", "Newton's third law", ["Newton's first law", "Newton's second law", "the law of conservation of charge"], "The gas pushes the rocket in return.")
H('5.G', 3, "When you push on a wall, what does the wall do?", "pushes back with an equal force", ["pushes back with a smaller force", "does nothing", "absorbs the force"], "Action-reaction forces are equal.")
H('5.G', 4, "Why don't the action and reaction forces cancel each other out?", "they act on different objects", ["they are different sizes", "they act in the same direction", "they happen at different times"], "A net force requires forces on the same object.")

# 5.H gravitation
H('5.H', 3, "If the distance between two masses doubles, what happens to the gravitational force between them?", "it becomes one-fourth", ["it is halved", "it doubles", "it quadruples"], "Gravity follows an inverse square law.")
H('5.H', 3, "If one of two masses doubles, what happens to the gravitational force between them?", "it doubles", ["it is halved", "it quadruples", "it stays the same"], "Force is proportional to each mass.")
H('5.H', 3, "What is the approximate value of the universal gravitational constant G?", "6.67 × 10⁻¹¹ N·m²/kg²", ["6.67 × 10¹¹ N·m²/kg²", "9.8 m/s²", "3.0 × 10⁸ m/s"], "A very small number, so gravity is weak between everyday objects.")
H('5.H', 4, "If both masses and the distance between them are all doubled, what happens to the gravitational force?", "it stays the same", ["it doubles", "it becomes one-fourth", "it quadruples"], "Masses give a factor of 4 and distance gives a factor of 1/4.")

# 6.A Coulomb's law
H('6.A', 3, "If the distance between two charges doubles, what happens to the electric force between them?", "it becomes one-fourth", ["it is halved", "it doubles", "it quadruples"], "The electric force also follows an inverse square law.")
H('6.A', 2, "How do two objects with opposite charges interact?", "they attract each other", ["they repel each other", "they have no force between them", "they merge"], "Opposite charges attract.")
H('6.A', 3, "If one charge triples while the other charge and distance stay the same, what happens to the electric force?", "it triples", ["it becomes one-third", "it is nine times as large", "it stays the same"], "Force is proportional to each charge.")
H('6.A', 4, "The Coulomb constant k is about 9 × 10⁹ N·m²/C². What is this number in standard form?", "9,000,000,000", ["900,000,000", "90,000,000,000", "9,000,000"], "10⁹ means 9 followed by 9 zeros.")

# 6.B electric and magnetic forces in everyday life
H('6.B', 3, "What does an electric generator do?", "converts mechanical energy into electrical energy using a magnetic field", ["converts electrical energy into heat only", "stores charge permanently", "converts light into sound"], "A coil spins in a magnetic field.")
H('6.B', 3, "What does an electric motor do?", "converts electrical energy into mechanical energy using magnetic forces", ["converts motion into electricity", "produces static charge", "makes magnets weaker"], "Current in a magnetic field experiences a force.")
H('6.B', 2, "Why does the needle of a compass point north?", "it aligns with Earth's magnetic field", ["it is attracted by the Moon", "it is pulled by gravity", "it is charged"], "Earth acts like a giant magnet.")
H('6.B', 3, "Which everyday device uses electromagnets to lift scrap metal?", "a junkyard crane magnet", ["a flashlight", "a thermometer", "a mirror"], "Current through a coil creates a magnetic field that can be switched on and off.")

# 6.C conservation of charge
H('6.C', 3, "A balloon rubbed on hair becomes negative and the hair becomes positive. What does this show?", "electrons moved from the hair to the balloon", ["protons moved to the balloon", "charge was created", "charge was destroyed"], "Electrons are transferred and total charge stays the same.")
H('6.C', 3, "Charging by conduction requires what?", "direct contact between a charged object and a neutral object", ["no contact at all", "a magnet", "a battery only"], "Charge flows during contact.")
H('6.C', 4, "Charging by induction results in a final charge on the neutral object that is what?", "opposite to the charged object that was brought near", ["the same as the charged object", "always neutral", "random"], "Charges rearrange and then the object is grounded.")
H('6.C', 3, "What does the law of conservation of charge say?", "the total charge in an isolated system stays the same", ["charge can be created from nothing", "charge disappears over time", "charge is only positive"], "Charge is transferred, not created or destroyed.")

# 6.D series and parallel circuits
H('6.D', 3, "In a series circuit, how many paths are there for current?", "one", ["two", "as many as there are bulbs", "none"], "All components are connected in a single loop.")
H('6.D', 3, "In a series circuit, what happens if one bulb burns out?", "all bulbs go out", ["only that bulb goes out", "the other bulbs get brighter", "nothing changes"], "The circuit is broken.")
H('6.D', 3, "In a parallel circuit, what is the same across each branch?", "the voltage", ["the current", "the resistance", "the power"], "Each branch connects to the same two points.")
H('6.D', 3, "Two resistors of 2 Ω and 3 Ω are connected in series. What is the total resistance?", "5 Ω", ["1.2 Ω", "6 Ω", "1 Ω"], "Resistances add in series.")
H('6.D', 4, "Two identical 6 Ω resistors are connected in parallel. What is the total resistance?", "3 Ω", ["12 Ω", "6 Ω", "36 Ω"], "Equal resistors in parallel divide the resistance by the number of resistors.")
H('6.D', 3, "Why are household outlets wired in parallel?", "each device gets the full voltage and works independently", ["so that all devices turn off together", "so that voltage is split", "so that no current flows"], "One device can be off while others stay on.")

# 6.E Ohm's law and power
H('6.E', 3, "A 12 V battery is connected to a 4 Ω resistor. What is the current?", "3 A", ["48 A", "0.33 A", "8 A"], "I = V ÷ R.")
H('6.E', 3, "A device carries 2 A at 10 V. How much power does it use?", "20 W", ["5 W", "12 W", "0.2 W"], "P = IV.")
H('6.E', 3, "A circuit has 9 V and 3 A. What is the resistance?", "3 Ω", ["27 Ω", "12 Ω", "0.33 Ω"], "R = V ÷ I.")
H('6.E', 3, "What is the unit of electric power?", "watt", ["volt", "ohm", "ampere"], "One watt is one joule per second.")
H('6.E', 4, "If the voltage across a fixed resistor doubles, what happens to the current?", "it doubles", ["it is halved", "it stays the same", "it quadruples"], "Current is proportional to voltage.")

# 7.A work and power
H('7.A', 3, "How much work does a 10 N force do pushing a box 5 m in the direction of the force?", "50 J", ["2 J", "15 J", "0.5 J"], "W = Fd.")
H('7.A', 3, "A person holds a heavy box without moving it. How much work is done on the box?", "none, because there is no displacement", ["a lot, because the force is large", "work equal to its weight", "work equal to its mass"], "Work needs displacement in the direction of the force.")
H('7.A', 3, "A machine does 100 J of work in 5 s. What is its power?", "20 W", ["500 W", "0.05 W", "95 W"], "P = W ÷ t.")
H('7.A', 4, "A waiter carries a tray at constant speed across a flat room. Does the waiter's upward force on the tray do work?", "No, because the force is perpendicular to the motion", ["Yes, because the tray moves", "Yes, because the tray has weight", "Yes, because there is a force"], "Work depends on the component of force along the motion.")

# 7.B kinetic and potential energy
H('7.B', 3, "What is the kinetic energy of a 2 kg object moving at 3 m/s?", "9 J", ["6 J", "18 J", "3 J"], "KE = ½mv².")
H('7.B', 3, "What is the gravitational potential energy of a 2 kg object at a height of 10 m? (g ≈ 9.8 m/s²)", "196 J", ["20 J", "19.6 J", "98 J"], "PE = mgh.")
H('7.B', 4, "If a car's speed doubles, its kinetic energy is multiplied by what factor?", "4", ["2", "8", "16"], "Kinetic energy is proportional to speed squared.")
H('7.B', 3, "Mechanical energy of a system is the sum of what?", "kinetic and potential energy", ["force and distance", "mass and speed", "work and power"], "ME = KE + PE.")

# 7.C conservation of energy
H('7.C', 3, "A ball falls from a shelf. What happens to its energy as it falls?", "gravitational potential energy changes into kinetic energy", ["kinetic energy changes into potential energy", "energy is destroyed", "its energy stays potential"], "Total mechanical energy stays about the same without friction.")
H('7.C', 3, "On a roller coaster without friction, where is the kinetic energy greatest?", "at the lowest point", ["at the highest point", "at the start of the climb only", "it is the same everywhere"], "The speed is greatest at the bottom.")
H('7.C', 4, "The work-energy theorem states that the net work done on an object equals what?", "its change in kinetic energy", ["its change in mass", "its change in volume", "its final position"], "W = ΔKE.")
H('7.C', 3, "When a sliding box stops because of friction, where does its kinetic energy go?", "into thermal energy", ["it disappears", "into gravitational potential energy", "into magnetic energy"], "Friction transforms motion energy into heat.")
H('7.C', 4, "A ball dropped from 5 m has about what speed just before it hits the ground? (g ≈ 9.8 m/s², ignore air)", "9.9 m/s", ["49 m/s", "5 m/s", "98 m/s"], "v = √(2gh).")

# 7.D impulse and momentum
H('7.D', 3, "What is the momentum of a 1000 kg car moving at 20 m/s?", "20,000 kg·m/s", ["50 kg·m/s", "1020 kg·m/s", "980 kg·m/s"], "p = mv.")
H('7.D', 3, "Impulse is equal to what?", "the change in momentum", ["the change in energy", "the change in mass", "the total work"], "J = FΔt = Δp.")
H('7.D', 3, "How does an airbag reduce injury in a collision?", "it increases the time over which the person stops, reducing the force", ["it increases the force on the person", "it decreases the person's mass", "it makes the car go faster"], "The same change in momentum over a longer time means less force.")
H('7.D', 4, "Why do crumple zones on cars help protect passengers?", "they lengthen the stopping time, reducing the average force", ["they make the car heavier", "they stop the car instantly", "they increase momentum"], "Impulse is the same but force is smaller.")

# 7.E conservation of momentum
H('7.E', 3, "In an inelastic collision, what happens to the total kinetic energy?", "some is converted to other forms such as heat", ["it is conserved exactly", "it doubles", "it disappears from the universe"], "Momentum is conserved but kinetic energy is not.")
H('7.E', 3, "In a perfectly elastic collision, what is conserved?", "both momentum and kinetic energy", ["only mass", "only kinetic energy", "neither"], "No kinetic energy is lost.")
H('7.E', 4, "A 2 kg cart moving at 3 m/s hits a 1 kg cart at rest, and they stick together. What is their speed afterward?", "2 m/s", ["3 m/s", "1 m/s", "6 m/s"], "6 kg·m/s ÷ 3 kg.")
H('7.E', 3, "A gun fires a bullet forward and recoils backward. Which principle explains the recoil?", "conservation of momentum", ["conservation of charge", "Ohm's law", "Snell's law"], "Total momentum starts at zero and stays at zero.")

# 8.A simple harmonic motion
H('8.A', 3, "On what does the period of a simple pendulum mainly depend (for small angles)?", "its length", ["its mass", "the color of the bob", "how far it started from the middle only"], "Longer pendulums swing more slowly.")
H('8.A', 3, "A wave has a period of 0.5 s. What is its frequency?", "2 Hz", ["0.5 Hz", "0.25 Hz", "5 Hz"], "f = 1 ÷ T.")
H('8.A', 3, "A mass on a spring moves fastest at what point?", "the equilibrium position", ["the maximum displacement", "the top of the motion only", "it moves at constant speed"], "All of the energy is kinetic at equilibrium.")
H('8.A', 4, "What kind of force acts on an object in simple harmonic motion?", "a restoring force toward the equilibrium position", ["a constant force in one direction", "a force away from the center", "no force"], "The force is proportional to displacement.")
H('8.A', 3, "What does a wave transfer from one place to another?", "energy", ["matter", "mass", "charge only"], "The medium vibrates but does not travel with the wave.")

# 8.B transverse and longitudinal waves
H('8.B', 2, "Which of these waves is longitudinal?", "sound", ["light", "radio waves", "X-rays"], "Sound consists of compressions and rarefactions.")
H('8.B', 3, "In a transverse wave, how does the medium vibrate?", "perpendicular to the direction the wave travels", ["parallel to the direction the wave travels", "in a circle", "it does not vibrate"], "Like a wave on a rope.")
H('8.B', 3, "Which type of wave can travel through a vacuum?", "electromagnetic waves", ["sound waves", "water waves", "waves on a rope"], "They do not need a medium.")
H('8.B', 3, "What are the regions of high pressure in a sound wave called?", "compressions", ["rarefactions", "crests", "nodes"], "Particles are pushed close together.")

# 8.C wave characteristics
H('8.C', 3, "A wave has a frequency of 5 Hz and a wavelength of 2 m. What is its speed?", "10 m/s", ["2.5 m/s", "7 m/s", "0.4 m/s"], "v = fλ.")
H('8.C', 3, "What property of a sound wave determines how loud it is?", "amplitude", ["wavelength", "speed only", "period"], "Greater amplitude carries more energy.")
H('8.C', 3, "What property of a sound wave determines its pitch?", "frequency", ["amplitude", "mass of the medium", "color"], "Higher frequency sounds higher.")
H('8.C', 4, "A wave's speed stays the same while its frequency doubles. What happens to the wavelength?", "it is halved", ["it doubles", "it stays the same", "it quadruples"], "v = fλ.")

# 8.D wave behaviors
H('8.D', 2, "What is it called when a wave bounces off a surface?", "reflection", ["refraction", "diffraction", "absorption"], "The law of reflection applies.")
H('8.D', 3, "What causes refraction?", "a change in wave speed when entering a different medium", ["a change in frequency", "the wave stopping", "amplitude doubling"], "The wave bends as its speed changes.")
H('8.D', 3, "What is diffraction?", "the bending of waves around obstacles or through openings", ["the bouncing of waves", "the stopping of waves", "the making of waves"], "It is strongest when the opening is similar in size to the wavelength.")
H('8.D', 3, "When two waves overlap and make a larger amplitude, this is called what?", "constructive interference", ["destructive interference", "refraction", "reflection"], "Crests align with crests.")
H('8.D', 4, "An ambulance siren sounds higher in pitch as it approaches. This is called what?", "the Doppler effect", ["refraction", "total internal reflection", "polarization"], "The waves are compressed in front of the moving source.")

# 8.E electromagnetic spectrum applications
H('8.E', 3, "Radio telescopes detect what kind of waves from space?", "radio waves", ["X-rays", "sound waves", "ultraviolet waves"], "Large dishes collect radio signals.")
H('8.E', 3, "Which electromagnetic waves are used to cook food in a microwave oven?", "microwaves", ["X-rays", "gamma rays", "ultraviolet rays"], "They make water molecules vibrate.")
H('8.E', 3, "Which electromagnetic waves are used for medical imaging of bones?", "X-rays", ["radio waves", "infrared waves", "microwaves"], "They pass through soft tissue more easily than bone.")
H('8.E', 3, "Night-vision devices detect which type of electromagnetic radiation?", "infrared", ["gamma", "ultraviolet", "radio"], "Warm objects emit infrared.")

# 8.F emission spectra
H('8.F', 3, "Why does each element have a unique emission spectrum?", "its electrons have a unique set of energy levels", ["its protons have different colors", "its neutrons emit light", "it has a different mass"], "Each atom emits only certain wavelengths.")
H('8.F', 3, "How is a photon emitted by an atom?", "an electron drops to a lower energy level", ["an electron moves to a higher energy level", "a proton leaves the nucleus", "the nucleus splits"], "The energy difference is released as light.")
H('8.F', 4, "How do astronomers learn what elements a star contains?", "by analyzing the spectrum of its light", ["by weighing it", "by touching it", "by measuring its temperature only"], "The spectral lines match known elements.")

# 8.G mirrors and lenses
H('8.G', 3, "What kind of image does a plane mirror form?", "a virtual image, the same size as the object, behind the mirror", ["a real, enlarged image", "a real, inverted image", "no image"], "The image appears as far behind the mirror as the object is in front.")
H('8.G', 3, "What does the law of reflection state?", "the angle of incidence equals the angle of reflection", ["the angle of incidence is twice the reflection angle", "light bends toward the normal", "light speeds up"], "Both angles are measured from the normal.")
H('8.G', 3, "Light entering glass from air slows down. How does it bend?", "toward the normal", ["away from the normal", "it does not bend", "it reflects completely"], "Light bends toward the normal in a slower medium.")
H('8.G', 4, "What does a converging (convex) lens do to parallel light rays?", "bends them toward a focal point", ["spreads them apart", "reflects them", "absorbs them"], "It focuses light.")
H('8.G', 4, "Why does light stay inside an optical fiber?", "total internal reflection at the walls", ["absorption by the walls", "diffraction at the walls", "polarization"], "Light hits the boundary at angles greater than the critical angle.")

# 9.A photoelectric effect
H('9.A', 4, "In the photoelectric effect, electrons are ejected from a metal only if the light has what?", "frequency above a threshold value", ["intensity above a threshold value", "wavelength above a threshold value", "any color"], "Photon energy must exceed the work function.")
H('9.A', 4, "Increasing the brightness of light below the threshold frequency has what effect on the photoelectric effect?", "no electrons are ejected", ["more electrons are ejected", "faster electrons are ejected", "electrons are ejected only at first"], "Each photon must carry enough energy on its own.")
H('9.A', 3, "Which model of light explains the photoelectric effect?", "light as photons with energy E = hf", ["light as a continuous wave only", "light as sound", "light as heat"], "Einstein proposed light comes in quanta.")
H('9.A', 4, "Emission spectra show only specific wavelengths. What does this indicate about atomic energy levels?", "they are quantized", ["they are continuous", "they are random", "they do not exist"], "Only certain energy differences are possible.")

# 9.B polarization
H('9.B', 4, "What does the polarization of light show about its nature?", "light is a transverse wave", ["light is a longitudinal wave", "light is a sound wave", "light has no direction"], "Only transverse waves can be polarized.")
H('9.B', 4, "Two polarizing filters are crossed at 90°. How much light passes through both?", "almost none", ["all of it", "half of it", "a quarter of it"], "cos²(90°) = 0.")
H('9.B', 4, "Light of intensity 100 passes through a polarizer whose axis is 30° from the light's polarization. By Malus's law, about what intensity passes?", "75", ["50", "87", "25"], "100 × cos²30° = 100 × 0.75.")
H('9.B', 3, "Why do polarized sunglasses reduce glare?", "they block horizontally polarized reflected light", ["they block all light", "they change the color of light", "they increase frequency"], "Reflected glare is mostly polarized.")
H('9.B', 3, "How do 3-D movie glasses create separate images for each eye?", "each lens polarizes light in a different direction", ["each lens changes the frequency", "each lens is a mirror", "each lens makes images bigger"], "Two differently polarized images are shown on the screen.")

# 9.C wave-particle duality and superposition
H('9.C', 3, "What is wave-particle duality?", "matter and light show both wave and particle behavior", ["light is only a particle", "matter is only a wave", "waves cannot have energy"], "The behavior depends on the experiment.")
H('9.C', 4, "Electrons sent through two slits form an interference pattern. What does this show?", "electrons can behave like waves", ["electrons are not particles at all", "electrons are heavier than protons", "electrons are charged only"], "A wave-like pattern builds up from individual electrons.")
H('9.C', 4, "What does superposition of quantum states mean?", "a system can exist in a combination of states until measured", ["a system can only be in one state", "a system is always at rest", "a system cannot be measured"], "Measurement gives one outcome.")
H('9.C', 3, "What is a photon?", "a quantum (packet) of light energy", ["a type of sound", "a negative ion", "a unit of mass"], "Its energy depends on frequency.")

# 9.D quantum applications
H('9.D', 4, "The Heisenberg uncertainty principle says that you cannot do what?", "know the exact position and momentum of a particle at the same time", ["measure energy at all", "see any particle", "use light"], "There is a limit to how precisely both can be known.")
H('9.D', 4, "What do quantum computers use in place of ordinary bits?", "qubits that can be in superposition", ["transistors that cannot switch", "analog gears", "ordinary bits only"], "A qubit can be in a combination of 0 and 1.")
H('9.D', 3, "Which everyday devices rely on quantum mechanics?", "LEDs, lasers and transistors", ["bicycles", "wooden chairs", "plain mirrors"], "Their operation depends on quantized energy levels.")
H('9.D', 3, "What principle allows an electron microscope to see very small objects?", "electrons have wave properties with very short wavelengths", ["light has long wavelengths", "electrons are heavy", "electrons are positive"], "Shorter wavelength gives better resolution.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_phys.jsonl'))

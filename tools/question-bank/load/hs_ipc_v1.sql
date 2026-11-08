insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_ipc_v1'
from (values
('112.44.c.5.A',2,'A runner covers 60 m in 10 s at a steady pace. What is the speed?','["6 m/s", "50 m/s", "0.17 m/s", "600 m/s"]'::jsonb,0,'Speed = distance ÷ time.','original'),
('112.44.c.5.A',3,'A car speeds up from 10 m/s to 30 m/s in 5 s. What is its acceleration?','["6 m/s²", "4 m/s²", "20 m/s²", "100 m/s²"]'::jsonb,1,'a = (30 − 10) ÷ 5.','original'),
('112.44.c.5.A',3,'On a distance-time graph, a straight line that slopes upward shows what?','["constant acceleration", "speeding up faster and faster", "constant speed", "no motion"]'::jsonb,2,'Equal distances are covered in equal times.','original'),
('112.44.c.5.A',2,'On a distance-time graph, what does a flat horizontal line show?','["the object is turning", "the object moves at constant speed", "the object is accelerating", "the object is at rest"]'::jsonb,3,'Distance does not change.','original'),
('112.44.c.5.B',3,'A 5 kg cart is pushed with a net force of 20 N. What is its acceleration?','["4 m/s²", "0.25 m/s²", "15 m/s²", "100 m/s²"]'::jsonb,0,'a = F ÷ m.','original'),
('112.44.c.5.B',3,'The same net force pushes a light cart and a heavy cart. Which accelerates more?','["both the same", "the light cart", "neither moves", "the heavy cart"]'::jsonb,1,'Acceleration is inversely related to mass.','original'),
('112.44.c.5.B',3,'If the net force on an object doubles and its mass stays the same, what happens to its acceleration?','["it stays the same", "it is halved", "it doubles", "it quadruples"]'::jsonb,2,'Acceleration is proportional to net force.','original'),
('112.44.c.5.B',4,'What net force is needed to give a 12 kg object an acceleration of 2 m/s²?','["14 N", "0.17 N", "6 N", "24 N"]'::jsonb,3,'F = ma.','original'),
('112.44.c.5.C',3,'What is the momentum of a 3 kg ball moving at 4 m/s?','["12 kg·m/s", "1.3 kg·m/s", "0.75 kg·m/s", "7 kg·m/s"]'::jsonb,0,'p = mv.','original'),
('112.44.c.5.C',3,'Why does a helmet''s soft inner foam reduce injury in a crash?','["it speeds up the head", "it lengthens the time of impact, lowering the force", "it raises the force of impact", "it reduces the head''s mass"]'::jsonb,1,'A longer stopping time means a smaller force for the same change in momentum.','original'),
('112.44.c.5.C',3,'Which design feature of a car lowers the force on passengers during a crash?','["a faster engine", "a rigid frame that never bends", "crumple zones that collapse gradually", "a lighter steering wheel"]'::jsonb,2,'They extend the collision time.','original'),
('112.44.c.5.C',4,'A catcher pulls a mitt backward while catching a fast ball. Why?','["to speed up the ball", "to make the ball heavier", "to increase the ball''s momentum", "to increase the stopping time and reduce the force on the hand"]'::jsonb,3,'Impulse equals force times time.','original'),
('112.44.c.5.D',2,'Which fundamental force holds protons and neutrons together in a nucleus?','["the strong nuclear force", "the weak nuclear force", "friction", "gravity"]'::jsonb,0,'It overcomes the repulsion between protons.','original'),
('112.44.c.5.D',3,'Which fundamental force is responsible for some types of radioactive decay?','["friction", "the weak nuclear force", "the strong nuclear force", "gravity"]'::jsonb,1,'It governs processes such as beta decay.','original'),
('112.44.c.5.D',2,'Which fundamental force keeps planets in orbit around the Sun?','["the weak nuclear force", "electromagnetic force", "gravitation", "magnetism only"]'::jsonb,2,'Mass attracts mass.','original'),
('112.44.c.5.D',3,'Which force acts between charged particles?','["no force", "gravity only", "the strong nuclear force only", "the electromagnetic force"]'::jsonb,3,'Like charges repel and opposite charges attract.','original'),
('112.44.c.5.E',3,'If the distance between two objects doubles, what happens to the gravitational force between them?','["it becomes one-fourth", "it is halved", "it stays the same", "it doubles"]'::jsonb,0,'The force follows an inverse square law.','original'),
('112.44.c.5.E',3,'If the mass of one of two objects doubles, what happens to the gravitational force between them?','["it becomes one-fourth", "it doubles", "it stays the same", "it is halved"]'::jsonb,1,'Force is proportional to mass.','original'),
('112.44.c.5.E',3,'If the distance between two charged objects triples, what happens to the electric force?','["it triples", "it becomes one-third", "it becomes one-ninth", "it is nine times larger"]'::jsonb,2,'Electric force also follows an inverse square law.','original'),
('112.44.c.5.E',3,'Two charged objects repel each other. What is true about their charges?','["they are opposite signs", "they have no mass", "one of them is neutral", "they are the same sign"]'::jsonb,3,'Like charges repel.','original'),
('112.44.c.6.A',3,'In a series circuit, what happens when one bulb is removed?','["the circuit is broken and all bulbs go out", "nothing changes", "the other bulbs get brighter", "the other bulbs stay lit"]'::jsonb,0,'There is only one path.','original'),
('112.44.c.6.A',3,'Why are the outlets in a home wired in parallel?','["so all devices share one path", "so each device works independently at full voltage", "so that voltage is divided", "so that current does not flow"]'::jsonb,1,'Each branch has its own path.','original'),
('112.44.c.6.A',3,'Two resistors of 4 Ω and 6 Ω are in series. What is the total resistance?','["5 Ω", "2.4 Ω", "10 Ω", "24 Ω"]'::jsonb,2,'Resistances add in series.','original'),
('112.44.c.6.A',3,'A 12 V source drives a 6 Ω resistor. What is the current?','["18 A", "0.5 A", "72 A", "2 A"]'::jsonb,3,'I = V ÷ R.','original'),
('112.44.c.6.B',3,'How does a generator produce electricity?','["a coil moves in a magnetic field", "a bulb is lit", "a battery is recharged", "a magnet is heated"]'::jsonb,0,'Moving conductors in a magnetic field induce a current.','original'),
('112.44.c.6.B',3,'Which energy conversion happens in a wind turbine generator?','["heat to wind", "kinetic energy of wind to electrical energy", "chemical energy to light", "nuclear energy to sound"]'::jsonb,1,'The blades turn a generator.','original'),
('112.44.c.6.B',4,'A hand-crank flashlight lights up while you turn the handle. What energy change occurs?','["sound into heat", "electrical energy into mass", "mechanical energy into electrical energy into light", "light into mechanical energy"]'::jsonb,2,'Cranking spins a small generator.','original'),
('112.44.c.6.C',3,'What does the law of conservation of energy say?','["energy disappears as heat", "energy is created when objects move", "energy is used up completely", "energy cannot be created or destroyed, only transformed"]'::jsonb,3,'The total energy of a closed system stays constant.','original'),
('112.44.c.6.C',3,'A pendulum swings back and forth and gradually stops. Where does its mechanical energy go?','["into thermal energy through air resistance and friction", "it is stored as mass", "it becomes magnetic", "it is destroyed"]'::jsonb,0,'The energy spreads out as heat.','original'),
('112.44.c.6.C',3,'A ball at the top of a hill has 100 J of gravitational potential energy. If it rolls to the bottom without friction, how much kinetic energy does it have there?','["half of it", "all 100 joules of the starting potential energy", "none of it", "twice as much"]'::jsonb,1,'Energy is conserved.','original'),
('112.44.c.6.C',4,'A closed system contains 40 J of kinetic energy and 60 J of potential energy. What is the total energy later if nothing enters or leaves?','["60 J", "40 J", "100 J", "20 J"]'::jsonb,2,'Total energy stays constant.','original'),
('112.44.c.6.D',2,'How does thermal energy move through a solid metal spoon placed in hot soup?','["convection", "evaporation", "radiation", "conduction"]'::jsonb,3,'Heat passes from particle to particle.','original'),
('112.44.c.6.D',3,'How does thermal energy move in a pot of boiling water?','["convection", "radiation only", "reflection", "conduction only"]'::jsonb,0,'Warm fluid rises and cooler fluid sinks.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Science' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_ipc_v1'
from (values
('112.44.c.6.D',3,'How does heat from the Sun reach Earth?','["condensation", "radiation", "convection", "conduction"]'::jsonb,1,'Radiation does not need a medium.','original'),
('112.44.c.6.D',3,'Why do metal handles feel colder than wood handles at the same temperature?','["metal blocks heat flow", "metal is actually colder", "metal conducts heat away from your hand faster", "wood produces heat"]'::jsonb,2,'Metals are good thermal conductors.','original'),
('112.44.c.6.E',3,'Which kind of material is a good electrical conductor?','["rubber", "plastic", "glass", "copper"]'::jsonb,3,'Metals have free-moving electrons.','original'),
('112.44.c.6.E',3,'Which material is the best electrical insulator?','["rubber", "silver", "iron", "copper"]'::jsonb,0,'Rubber does not allow current to flow easily.','original'),
('112.44.c.6.E',3,'Why are electrical wires covered with plastic?','["plastic makes electricity travel faster", "plastic is an insulator that prevents shocks and short circuits", "plastic is a conductor", "plastic stores electricity"]'::jsonb,1,'It keeps charge on the wire.','original'),
('112.44.c.6.E',4,'Fiber-optic cables carry information using what?','["pulses of sound", "heat waves", "pulses of light", "magnetic poles"]'::jsonb,2,'Light signals travel through glass fibers.','original'),
('112.44.c.6.F',3,'When two waves meet and combine to form a larger wave, this is called what?','["destructive interference", "reflection", "refraction", "constructive interference"]'::jsonb,3,'Crests line up with crests.','original'),
('112.44.c.6.F',3,'Noise-canceling headphones work mainly by using what?','["destructive interference", "reflection", "refraction", "constructive interference"]'::jsonb,0,'A wave that is opposite to the noise cancels it out.','original'),
('112.44.c.6.F',3,'A straw looks bent in a glass of water. What causes this?','["interference of sound", "refraction of light", "reflection of light", "diffraction of sound"]'::jsonb,1,'Light changes speed and bends between water and air.','original'),
('112.44.c.6.F',3,'An echo is caused by which wave behavior?','["absorption only", "refraction", "reflection", "diffraction"]'::jsonb,2,'Sound bounces off a hard surface.','original'),
('112.44.c.6.G',2,'Which of these energy sources is renewable?','["petroleum", "coal", "natural gas", "solar"]'::jsonb,3,'The Sun is a continuing source.','original'),
('112.44.c.6.G',2,'Which of these energy sources is nonrenewable?','["coal", "wind", "solar", "hydroelectric"]'::jsonb,0,'Fossil fuels take millions of years to form.','original'),
('112.44.c.6.G',3,'What is one disadvantage of wind power?','["it produces radioactive waste", "it depends on wind being available", "it uses up fossil fuels", "it releases large amounts of carbon dioxide"]'::jsonb,1,'Output varies with weather.','original'),
('112.44.c.6.G',3,'What is one advantage of nuclear power plants?','["they run on coal", "they are cheap to build", "they produce electricity without releasing carbon dioxide during operation", "they produce no waste"]'::jsonb,2,'But they create radioactive waste that must be stored.','original'),
('112.44.c.7.A',2,'Which particle in an atom has a positive charge?','["electron", "photon", "neutron", "proton"]'::jsonb,3,'Protons are in the nucleus.','original'),
('112.44.c.7.A',2,'What determines the identity of an element?','["the number of protons", "the mass only", "the number of electrons only", "the number of neutrons"]'::jsonb,0,'Atomic number equals the number of protons.','original'),
('112.44.c.7.A',3,'An atom has 6 protons and 6 neutrons. What is its mass number?','["0", "12", "6", "18"]'::jsonb,1,'Mass number is protons plus neutrons.','original'),
('112.44.c.7.A',3,'Why are the noble gases generally unreactive?','["they have no electrons", "they have only one electron", "their outer energy level is full", "they have a positive charge"]'::jsonb,2,'A full outer shell is stable.','original'),
('112.44.c.7.B',2,'Elements in the same group of the periodic table share what?','["the same mass", "the same number of protons", "the same state at room temperature", "the same number of valence electrons"]'::jsonb,3,'This gives them similar chemical properties.','original'),
('112.44.c.7.B',3,'Moving from left to right across a period, what happens to atomic number?','["it increases", "it becomes zero", "it decreases", "it stays the same"]'::jsonb,0,'Each element has one more proton.','original'),
('112.44.c.7.B',3,'Which group of elements is the most reactive metals?','["transition metals", "alkali metals", "noble gases", "halogens"]'::jsonb,1,'They easily lose one electron.','original'),
('112.44.c.7.B',3,'Which of these elements is expected to be most like sodium in its chemical behavior?','["chlorine", "helium", "potassium", "oxygen"]'::jsonb,2,'They are in the same group.','original'),
('112.44.c.7.C',3,'Why is aluminum often used to make drink cans?','["it is a good insulator", "it is a gas", "it is magnetic", "it is lightweight and resists corrosion"]'::jsonb,3,'Its properties suit the use.','original'),
('112.44.c.7.C',3,'Why is copper used in electrical wiring?','["it is a good conductor of electricity and is ductile", "it is brittle", "it is very light", "it is an insulator"]'::jsonb,0,'It can be drawn into wires.','original'),
('112.44.c.7.C',3,'Why is helium used to fill party balloons?','["it is heavier than air", "it is less dense than air and unreactive", "it is a liquid", "it is very reactive"]'::jsonb,1,'It floats safely.','original'),
('112.44.c.7.C',4,'Why is diamond used in cutting tools?','["it conducts electricity", "it is very soft", "it is extremely hard", "it is a liquid"]'::jsonb,2,'Its covalent network structure makes it very hard.','original'),
('112.44.c.7.D',3,'What happens when an excited electron falls to a lower energy level?','["a neutron is released", "a proton is absorbed", "the nucleus splits", "a photon is emitted"]'::jsonb,3,'The energy difference is given off as light.','original'),
('112.44.c.7.D',3,'Why do different elements produce different colors in a flame test?','["their electrons have different energy-level gaps", "they have different densities", "they have the same protons", "they have the same mass"]'::jsonb,0,'Different gaps give different photon energies.','original'),
('112.44.c.7.D',4,'A larger energy drop between levels produces a photon with what?','["no energy", "higher frequency", "lower frequency", "longer wavelength"]'::jsonb,1,'E = hf.','original'),
('112.44.c.7.D',3,'Neon signs glow because of what process?','["the gas burns", "the gas turns into a solid", "excited gas atoms emit light as electrons return to lower levels", "the gas melts"]'::jsonb,2,'An electric current excites the gas.','original'),
('112.44.c.7.E',4,'Atomic emission spectra show only certain wavelengths. What does this suggest about electron energy?','["it is random", "it is zero", "it is continuous", "it is quantized"]'::jsonb,3,'Only specific energy changes are allowed.','original'),
('112.44.c.7.E',4,'Which property of light does the photon model highlight?','["it comes in discrete packets of energy", "it needs a medium", "it is a sound wave", "it has no energy"]'::jsonb,0,'Each photon has energy E = hf.','original'),
('112.44.c.7.E',4,'An electron diffraction pattern shows that electrons can behave like what?','["magnets only", "waves", "heat", "sound"]'::jsonb,1,'Matter shows wave properties.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Science' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_ipc_v1'
from (values
('112.44.c.7.E',3,'Wave-particle duality means that light and matter can show what?','["only wave behavior", "neither behavior", "both wave and particle behavior", "only particle behavior"]'::jsonb,2,'The behavior seen depends on the experiment.','original'),
('112.44.c.7.F',3,'How does raising the temperature usually affect the rate of a reaction?','["it stops it", "it has no effect", "it slows it down", "it speeds it up"]'::jsonb,3,'Particles collide more often and with more energy.','original'),
('112.44.c.7.F',3,'Which sugar dissolves fastest in water?','["powdered sugar", "a large sugar cube", "a single large crystal", "rock candy"]'::jsonb,0,'Greater surface area speeds up dissolving.','original'),
('112.44.c.7.F',3,'How does stirring affect the rate of dissolving?','["it decreases the rate", "it increases the rate", "it stops dissolving", "it has no effect"]'::jsonb,1,'Fresh solvent contacts the solute.','original'),
('112.44.c.7.F',4,'How does a catalyst change a reaction?','["it is used up as a reactant", "it changes the products", "it speeds the reaction without being used up", "it slows the reaction"]'::jsonb,2,'It lowers the activation energy.','original'),
('112.44.c.8.A',2,'Which of these is a sign of a chemical reaction?','["sugar dissolves in water", "ice melts", "a sheet of paper is folded", "a gas is produced and bubbles form"]'::jsonb,3,'A new substance is formed.','original'),
('112.44.c.8.A',3,'Which change is a physical change?','["water freezing", "milk souring", "wood burning", "iron rusting"]'::jsonb,0,'No new substance forms.','original'),
('112.44.c.8.A',3,'Which observation is the best evidence that a chemical change took place?','["a substance changed size", "a new substance with different properties formed", "a substance changed shape", "a substance was cut"]'::jsonb,1,'Chemical changes make new substances.','original'),
('112.44.c.8.A',3,'Hydrochloric acid is added to a metal and bubbles appear. What does this most likely indicate?','["a change of state only", "a physical change", "a chemical reaction producing a gas", "a dissolving process only"]'::jsonb,2,'Gas formation is evidence of a reaction.','original'),
('112.44.c.8.B',3,'In a balanced chemical equation, what must be the same on both sides?','["the number of molecules", "the volume", "the color", "the number of each type of atom"]'::jsonb,3,'Atoms are conserved.','original'),
('112.44.c.8.B',3,'Hydrogen and oxygen react to form water. If 4 g of hydrogen react with 32 g of oxygen, what mass of water forms?','["36 g", "128 g", "32 g", "28 g"]'::jsonb,0,'Mass is conserved.','original'),
('112.44.c.8.B',4,'Which is the correctly balanced equation?','["2H₂ + 2O₂ → 2H₂O", "2H₂ + O₂ → 2H₂O", "H₂ + 2O₂ → 2H₂O", "H₂ + O₂ → H₂O"]'::jsonb,1,'Each side has 4 H atoms and 2 O atoms.','original'),
('112.44.c.8.B',3,'A student burns a candle in an open container and the mass seems to decrease. Why?','["mass was destroyed", "the wax became energy", "gaseous products escaped into the air", "the flame has negative mass"]'::jsonb,2,'Mass is conserved when all products are counted.','original'),
('112.44.c.8.C',3,'What is nuclear fission?','["the freezing of a gas", "the joining of small nuclei", "the burning of fuel", "the splitting of a large nucleus into smaller nuclei"]'::jsonb,3,'It releases a great deal of energy.','original'),
('112.44.c.8.C',3,'What is nuclear fusion?','["the joining of small nuclei to form a larger nucleus", "the burning of coal", "the splitting of a nucleus", "the melting of a solid"]'::jsonb,0,'It powers the Sun.','original'),
('112.44.c.8.C',3,'Which technology uses radioactive isotopes?','["bicycle brakes", "medical imaging and cancer treatment", "solar panels", "wind turbines"]'::jsonb,1,'Isotopes can be used as tracers and for treatment.','original'),
('112.44.c.8.C',4,'What is one disadvantage of using nuclear fission for electricity?','["it requires sunlight", "it releases large amounts of carbon dioxide", "it produces radioactive waste that must be stored safely", "it uses up all the wind"]'::jsonb,2,'Waste stays radioactive for a long time.','original'),
('112.44.c.8.D',3,'Burning fossil fuels releases which gas that contributes to climate change?','["argon", "helium", "neon", "carbon dioxide"]'::jsonb,3,'It traps heat in the atmosphere.','original'),
('112.44.c.8.D',3,'What causes acid rain?','["sulfur and nitrogen oxides reacting with water in the air", "too much helium", "ice melting", "too much oxygen"]'::jsonb,0,'These oxides form acids in the atmosphere.','original'),
('112.44.c.8.D',3,'Which practice helps reduce the environmental impact of chemical products?','["burning all waste", "recycling and proper disposal", "dumping waste in streams", "pouring chemicals down storm drains"]'::jsonb,1,'Proper handling prevents pollution.','original'),
('112.44.c.8.D',4,'A catalytic converter in a car reduces what?','["the engine''s noise only", "the number of wheels", "harmful exhaust gases", "the car''s mass"]'::jsonb,2,'It converts pollutants into less harmful substances.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Science' and d.language = 'en'
on conflict (fingerprint) do nothing;

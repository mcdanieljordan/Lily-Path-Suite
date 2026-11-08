#!/usr/bin/env python3
"""High school Chemistry (TEKS 112.43.c). Original questions. Strands 1-4 (practices) skipped; content strands 5-14."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.43.c.', 986, own='hs_chem.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 5.A development of the periodic table
H('5.A', 3, "Mendeleev left gaps in his periodic table. What did he do with those gaps?", "predicted that undiscovered elements would fill them", ["declared that they were errors", "filled them with noble gases", "removed those columns"], "He predicted properties of missing elements, and later discoveries matched.")
H('5.A', 3, "The modern periodic table is arranged by increasing what?", "atomic number", ["atomic mass", "number of neutrons", "density"], "Moseley's work showed that atomic number orders the elements.")
H('5.A', 3, "Why do elements in the same column of the periodic table have similar chemical properties?", "they have the same number of valence electrons", ["they have the same number of neutrons", "they have the same mass", "they have the same number of shells"], "Valence electrons drive chemical behavior.")
H('5.A', 4, "What does the periodic law state?", "element properties repeat in a pattern as atomic number increases", ["all elements have equal properties", "properties depend only on mass", "elements cannot be grouped"], "Properties are a periodic function of atomic number.")

# 5.B chemical families
H('5.B', 2, "Which family of elements is highly reactive and forms 1+ ions?", "alkali metals", ["noble gases", "halogens", "transition metals"], "They have one valence electron to lose.")
H('5.B', 2, "Which family of elements is generally unreactive because it has a full valence shell?", "noble gases", ["halogens", "alkali metals", "alkaline earth metals"], "A complete outer shell is very stable.")
H('5.B', 3, "Which element should behave most like magnesium?", "calcium", ["sodium", "chlorine", "neon"], "They are in the same group.")
H('5.B', 3, "Halogens typically form which kind of ion?", "1− ions", ["1+ ions", "2+ ions", "no ions at all"], "They gain one electron to fill the valence shell.")
H('5.B', 3, "Which statement describes alkaline earth metals?", "they are reactive metals that form 2+ ions", ["they are unreactive gases", "they form 1− ions", "they are nonmetals"], "They have two valence electrons.")

# 5.C periodic trends
H('5.C', 3, "As you move left to right across a period, what generally happens to atomic radius?", "it decreases", ["it increases", "it stays the same", "it doubles"], "A growing nuclear charge pulls the electrons closer.")
H('5.C', 3, "As you move down a group, what generally happens to atomic radius?", "it increases", ["it decreases", "it stays the same", "it is not related to group"], "Each period adds another electron shell.")
H('5.C', 3, "Which of these elements has the largest atomic radius: Li, Na, K or Cs?", "Cs", ["Li", "Na", "K"], "Cs is lowest in the group.")
H('5.C', 3, "Which element has the highest electronegativity?", "fluorine", ["cesium", "sodium", "helium"], "Fluorine pulls shared electrons the most strongly.")
H('5.C', 4, "Which of these elements has the highest first ionization energy: Na, Mg, Al or Cl?", "Cl", ["Na", "Mg", "Al"], "Ionization energy generally increases across a period.")

# 6.A atomic models
H('6.A', 2, "Which scientist's gold foil experiment showed that atoms have a small, dense, positive nucleus?", "Rutherford", ["Dalton", "Thomson", "Bohr"], "Most particles passed through, but a few were deflected sharply.")
H('6.A', 3, "Thomson's discovery of the electron led to what model of the atom?", "a positive sphere with electrons embedded in it", ["a solid indivisible sphere", "electrons in fixed energy levels", "a nucleus with an electron cloud"], "This was nicknamed the plum pudding model.")
H('6.A', 3, "What did Bohr's model add to the picture of the atom?", "electrons in fixed energy levels around the nucleus", ["a nucleus with no charge", "indivisible atoms", "electrons that are not in the atom"], "Electrons occupy specific orbits with set energies.")
H('6.A', 3, "Dalton's model described atoms as what?", "tiny, indivisible spheres", ["mostly empty space", "a nucleus surrounded by an electron cloud", "made of protons and neutrons"], "Dalton did not know about subatomic particles.")
H('6.A', 3, "The modern model of the atom describes electrons as being where?", "in probability clouds called orbitals", ["in fixed circular paths", "inside the nucleus", "in a solid shell"], "Electrons are found by likelihood, not set paths.")

# 6.B structure of atoms and ions
H('6.B', 2, "Where are protons and neutrons found in an atom?", "in the nucleus", ["in the electron cloud", "in the outer shell", "in the orbitals"], "Nearly all of the atom's mass is in the nucleus.")
H('6.B', 2, "What is the charge of a neutron?", "zero", ["positive", "negative", "variable"], "Neutrons are neutral.")
H('6.B', 3, "A sodium atom has atomic number 11 and mass number 23. How many neutrons does it have?", "12", ["11", "23", "34"], "Neutrons = mass number − atomic number.")
H('6.B', 3, "How many protons and electrons does a Mg²⁺ ion have (atomic number 12)?", "12 protons and 10 electrons", ["12 protons and 14 electrons", "10 protons and 12 electrons", "14 protons and 12 electrons"], "A 2+ charge means two electrons were lost.")
H('6.B', 3, "How many electrons does a Cl⁻ ion have (atomic number 17)?", "18", ["16", "17", "35"], "The ion has gained one electron.")

# 6.C light
H('6.C', 3, "A photon of which visible color carries the most energy?", "violet", ["red", "orange", "yellow"], "Higher frequency means higher energy.")
H('6.C', 3, "If the wavelength of light increases, what happens to its frequency?", "it decreases", ["it increases", "it stays the same", "it doubles"], "c = λν, so they vary inversely.")
H('6.C', 3, "Which electromagnetic waves have the highest energy?", "gamma rays", ["radio waves", "microwaves", "visible light"], "Gamma rays have the shortest wavelengths.")
H('6.C', 4, "Which equation relates a photon's energy to its frequency?", "E = hν", ["E = mc", "E = λ/ν", "E = h/ν"], "h is Planck's constant.")

# 6.D average atomic mass
H('6.D', 3, "An element has 75% of an isotope with mass 35 and 25% of an isotope with mass 37. What is its average atomic mass?", "35.5", ["36.0", "35.0", "37.0"], "0.75(35) + 0.25(37).")
H('6.D', 3, "An element has two isotopes of equal abundance, with masses 79 and 81. What is its average atomic mass?", "80", ["79", "81", "160"], "The average of the two masses.")
H('6.D', 4, "Boron is 20% boron-10 and 80% boron-11. What is its average atomic mass?", "10.8", ["10.5", "10.2", "11.0"], "0.20(10) + 0.80(11).")
H('6.D', 3, "What are isotopes?", "atoms of the same element with different numbers of neutrons", ["atoms with different numbers of protons", "ions with different charges", "atoms with different electrons only"], "Isotopes have the same atomic number but different mass numbers.")

# 6.E electron configuration
H('6.E', 3, "What is the electron configuration of sodium (atomic number 11)?", "1s² 2s² 2p⁶ 3s¹", ["1s² 2s² 2p⁶ 3s²", "1s² 2s² 2p⁵", "1s² 2s¹ 2p⁶ 3s²"], "Eleven electrons fill orbitals in order.")
H('6.E', 3, "How many valence electrons does oxygen have?", "6", ["2", "8", "16"], "Oxygen is in group 16, with 6 valence electrons.")
H('6.E', 3, "How many valence electrons does chlorine have?", "7", ["1", "17", "8"], "Chlorine is in group 17.")
H('6.E', 4, "Which statement is true of the Mg²⁺ ion?", "its electron configuration is the same as neon's", ["it has the same configuration as magnesium", "it has the same configuration as sodium atom's valence shell", "it has no electrons"], "Losing two valence electrons gives 1s² 2s² 2p⁶.")
H('6.E', 4, "According to Hund's rule, how do electrons fill orbitals of equal energy?", "one per orbital first, with parallel spins", ["two per orbital first", "in the nucleus first", "randomly, with opposite spins"], "Electrons spread out before pairing up.")

# 7.A bonding and electronegativity
H('7.A', 3, "A large electronegativity difference between two atoms usually leads to what type of bond?", "ionic", ["nonpolar covalent", "metallic", "no bond"], "Electrons are effectively transferred.")
H('7.A', 3, "Two identical atoms (as in Cl₂) form what type of bond?", "nonpolar covalent", ["ionic", "polar covalent", "metallic"], "There is no difference in electronegativity.")
H('7.A', 4, "Why is the bond in HCl polar covalent?", "chlorine attracts the shared electrons more strongly than hydrogen", ["electrons are fully transferred to hydrogen", "the atoms share electrons equally", "the bond is made of metal atoms"], "Unequal sharing creates partial charges.")
H('7.A', 3, "Which pair is most likely to form an ionic bond?", "sodium and chlorine", ["carbon and oxygen", "nitrogen and hydrogen", "chlorine and chlorine"], "A metal and a nonmetal usually form ionic bonds.")

# 7.B naming compounds
H('7.B', 2, "What is the name of NaCl?", "sodium chloride", ["sodium chlorine", "natrium chlorate", "salt chloride"], "Metal name followed by the nonmetal name ending in -ide.")
H('7.B', 3, "What is the formula for calcium chloride?", "CaCl₂", ["CaCl", "Ca₂Cl", "CaCl₃"], "Ca²⁺ needs two Cl⁻ ions.")
H('7.B', 3, "What is the name of CO₂?", "carbon dioxide", ["carbon oxide", "carbonic oxygen", "monocarbon dioxide"], "A covalent compound uses prefixes.")
H('7.B', 3, "What is the formula for aluminum oxide?", "Al₂O₃", ["AlO", "Al₃O₂", "AlO₃"], "Two Al³⁺ balance three O²⁻.")
H('7.B', 4, "What is the formula for iron(III) oxide?", "Fe₂O₃", ["FeO₃", "Fe₃O₂", "FeO"], "The Roman numeral gives the 3+ charge on iron.")
H('7.B', 4, "What is the formula for potassium sulfate?", "K₂SO₄", ["KSO₄", "K(SO₄)₂", "K₂S"], "Two K⁺ balance one SO₄²⁻.")

# 7.C Lewis structures and molecular shape
H('7.C', 3, "What is the shape of a water molecule?", "bent", ["linear", "tetrahedral", "trigonal planar"], "Two lone pairs push the bonds into a bent shape.")
H('7.C', 3, "What is the shape of a methane (CH₄) molecule?", "tetrahedral", ["bent", "trigonal pyramidal", "linear"], "Four bonding pairs and no lone pairs.")
H('7.C', 3, "What is the shape of a carbon dioxide molecule?", "linear", ["bent", "tetrahedral", "trigonal pyramidal"], "Two double bonds on opposite sides of carbon.")
H('7.C', 4, "What is the shape of an ammonia (NH₃) molecule?", "trigonal pyramidal", ["trigonal planar", "tetrahedral", "bent"], "Three bonds and one lone pair on nitrogen.")
H('7.C', 4, "How many valence electrons are shown in the Lewis structure of CO₂?", "16", ["12", "18", "8"], "4 + 6 + 6.")
H('7.C', 3, "BF₃ has three bonding pairs and no lone pairs on the central atom. What is its shape?", "trigonal planar", ["trigonal pyramidal", "tetrahedral", "bent"], "Three regions spread out flat.")

# 7.D properties of substances
H('7.D', 3, "Why do ionic compounds have high melting points?", "strong attractions between oppositely charged ions", ["weak attractions between molecules", "free-moving electrons in the structure", "mostly nonpolar bonds"], "A lot of energy is needed to break the crystal.")
H('7.D', 3, "Why can metals conduct electricity?", "their valence electrons move freely", ["their ions are free to move", "they have no electrons", "they have covalent bonds"], "A sea of electrons carries charge.")
H('7.D', 4, "What explains the unusually high boiling point of water for its size?", "hydrogen bonding between molecules", ["ionic bonding between H and O", "metallic bonding", "weak London forces only"], "Hydrogen bonds hold molecules together strongly.")
H('7.D', 3, "How do the forces between molecules compare with the covalent bonds inside them?", "forces between molecules are generally weaker", ["they are always stronger", "they are exactly equal", "forces between molecules do not exist"], "That is why molecular substances melt easily.")
H('7.D', 3, "Which type of substance generally conducts electricity when dissolved in water?", "ionic compounds", ["sugar", "oil", "nonpolar gases"], "The ions are free to move in solution.")

# 8.A mole and molar mass
H('8.A', 3, "What is the molar mass of water (H₂O)? (H = 1, O = 16)", "18 g/mol", ["17 g/mol", "16 g/mol", "34 g/mol"], "2(1) + 16.")
H('8.A', 3, "How many moles are in 36 g of water (molar mass 18 g/mol)?", "2 mol", ["0.5 mol", "18 mol", "648 mol"], "36 ÷ 18.")
H('8.A', 3, "What is the mass of 0.5 mol of CO₂ (molar mass 44 g/mol)?", "22 g", ["44 g", "88 g", "2 g"], "0.5 × 44.")
H('8.A', 3, "How many moles are in 58.5 g of NaCl (molar mass 58.5 g/mol)?", "1 mol", ["58.5 mol", "0.1 mol", "2 mol"], "One molar mass equals one mole.")
H('8.A', 3, "What is the mass of 3 mol of carbon (12 g/mol)?", "36 g", ["4 g", "15 g", "12 g"], "3 × 12.")

# 8.B Avogadro's number
H('8.B', 2, "What is Avogadro's number?", "6.02 × 10²³", ["6.02 × 10¹²", "3.00 × 10⁸", "1.60 × 10⁻¹⁹"], "The number of particles in one mole.")
H('8.B', 3, "About how many molecules are in 2 mol of a substance?", "1.2 × 10²⁴", ["6.02 × 10²³", "3.0 × 10²³", "12 × 10²²"], "2 × 6.02 × 10²³.")
H('8.B', 3, "About how many molecules are in 0.5 mol of a substance?", "3.01 × 10²³", ["6.02 × 10²³", "1.2 × 10²⁴", "0.5 × 10²³"], "Half of 6.02 × 10²³.")
H('8.B', 4, "About how many water molecules are in 18 g of water?", "6.02 × 10²³", ["18", "3.0 × 10²³", "1.1 × 10²⁵"], "18 g is one mole.")

# 8.C percent composition
H('8.C', 3, "What is the percent hydrogen by mass in H₂O? (H = 1, O = 16)", "11.1%", ["5.6%", "88.9%", "33.3%"], "2/18 × 100.")
H('8.C', 3, "What is the percent carbon by mass in CO₂? (C = 12, O = 16)", "27.3%", ["50%", "12%", "72.7%"], "12/44 × 100.")
H('8.C', 3, "What do the percent compositions of all elements in a compound add up to?", "100%", ["50%", "1000%", "a different value for each compound"], "They account for all the mass.")
H('8.C', 4, "What is the percent oxygen by mass in MgO? (Mg = 24, O = 16)", "40%", ["60%", "16%", "24%"], "16/40 × 100.")

# 8.D empirical vs molecular formulas
H('8.D', 3, "What is the empirical formula of glucose, C₆H₁₂O₆?", "CH₂O", ["C₆H₁₂O₆", "C₂H₄O₂", "CHO"], "Divide all subscripts by 6.")
H('8.D', 3, "What does an empirical formula show?", "the simplest whole-number ratio of atoms", ["the exact number of atoms in a molecule", "the shape of the molecule", "the number of electrons"], "The molecular formula is a multiple of it.")
H('8.D', 4, "A compound has empirical formula CH₂ and a molar mass of 56 g/mol. What is its molecular formula?", "C₄H₈", ["C₂H₄", "CH₂", "C₈H₁₆"], "CH₂ is 14 g/mol, and 56 ÷ 14 = 4.")
H('8.D', 3, "What is the empirical formula of hydrogen peroxide, H₂O₂?", "HO", ["H₂O₂", "H₂O", "HO₂"], "Divide both subscripts by 2.")

# 9.A chemical equations
H('9.A', 3, "Which is the balanced equation for the formation of water?", "2H₂ + O₂ → 2H₂O", ["H₂ + O₂ → H₂O", "H₂ + 2O₂ → 2H₂O", "2H₂ + 2O₂ → 2H₂O"], "Four hydrogen atoms and two oxygen atoms on each side.")
H('9.A', 3, "Which is the balanced equation for making ammonia?", "N₂ + 3H₂ → 2NH₃", ["N₂ + H₂ → NH₃", "N₂ + 2H₂ → 2NH₃", "2N₂ + 3H₂ → 2NH₃"], "Two N and six H on each side.")
H('9.A', 3, "What type of reaction is 2H₂O → 2H₂ + O₂?", "decomposition", ["synthesis", "single replacement", "double replacement"], "One compound breaks down into simpler substances.")
H('9.A', 3, "What type of reaction is Zn + CuSO₄ → ZnSO₄ + Cu?", "single replacement", ["synthesis", "decomposition", "combustion"], "One element replaces another in a compound.")
H('9.A', 4, "In the balanced equation 2C₂H₆ + 7O₂ → 4CO₂ + 6H₂O, what is the coefficient of oxygen?", "7", ["2", "4", "6"], "The coefficient in front of O₂ is 7.")
H('9.A', 3, "What are the products of complete combustion of a hydrocarbon?", "carbon dioxide and water", ["carbon monoxide and hydrogen", "oxygen and methane", "ash only"], "The carbon and hydrogen are oxidized.")

# 9.B reaction classes
H('9.B', 3, "Which equation is an acid-base reaction?", "HCl + NaOH → NaCl + H₂O", ["2Na + Cl₂ → 2NaCl", "CaCO₃ → CaO + CO₂", "Zn + 2HCl → ZnCl₂ + H₂"], "An acid and a base form a salt and water.")
H('9.B', 3, "Mixing AgNO₃(aq) and NaCl(aq) forms solid AgCl. What kind of reaction is this?", "precipitation", ["acid-base", "oxidation-reduction", "combustion"], "An insoluble solid forms from solution.")
H('9.B', 3, "What happens in an oxidation-reduction reaction?", "electrons are transferred between species", ["protons are shared equally", "neutrons are exchanged", "no change in oxidation numbers"], "One species loses electrons while another gains them.")
H('9.B', 3, "In a redox reaction, the substance that loses electrons is said to be what?", "oxidized", ["reduced", "neutralized", "precipitated"], "Oxidation is loss of electrons.")

# 9.C stoichiometry
H('9.C', 3, "In N₂ + 3H₂ → 2NH₃, how many moles of NH₃ form from 3 mol of N₂ (with enough H₂)?", "6 mol", ["3 mol", "1.5 mol", "9 mol"], "The ratio of N₂ to NH₃ is 1 to 2.")
H('9.C', 3, "In 2H₂ + O₂ → 2H₂O, how many moles of O₂ are needed to react with 4 mol of H₂?", "2 mol", ["4 mol", "8 mol", "1 mol"], "The ratio of H₂ to O₂ is 2 to 1.")
H('9.C', 4, "A reaction should give 10 g of product but actually gives 8 g. What is the percent yield?", "80%", ["125%", "20%", "8%"], "8 ÷ 10 × 100.")
H('9.C', 3, "At STP, what volume does 2 mol of any ideal gas occupy?", "44.8 L", ["22.4 L", "11.2 L", "2 L"], "One mole occupies 22.4 L at STP.")
H('9.C', 4, "In 2H₂ + O₂ → 2H₂O, how many grams of water form from 2 mol of H₂? (molar mass of water = 18 g/mol)", "36 g", ["18 g", "72 g", "2 g"], "2 mol of H₂ makes 2 mol of water.")

# 9.D limiting reactants
H('9.D', 3, "What is a limiting reactant?", "the reactant that is used up first and limits the amount of product", ["the reactant that is left over", "the product that forms first", "the catalyst of the reaction"], "The reaction stops when it runs out.")
H('9.D', 4, "In 2H₂ + O₂ → 2H₂O, 4 mol of H₂ are mixed with 1 mol of O₂. Which is limiting?", "O₂", ["H₂", "H₂O", "neither"], "1 mol of O₂ needs only 2 mol of H₂.")
H('9.D', 3, "What is an excess reactant?", "a reactant that remains after the reaction is finished", ["a reactant that is used up first", "a product that forms in excess", "a reactant that has no mass"], "Some of it is left unreacted.")
H('9.D', 4, "A recipe needs 2 slices of bread and 1 slice of cheese per sandwich. With 10 slices of bread and 8 slices of cheese, how many sandwiches can be made, and what limits it?", "5 sandwiches, limited by the bread", ["8 sandwiches, limited by the bread", "5 sandwiches, limited by the cheese", "10 sandwiches, limited by the cheese"], "10 ÷ 2 = 5, which is fewer than 8.")

# 10.A kinetic molecular theory
H('10.A', 3, "According to kinetic molecular theory, how do gas particles move?", "constantly and randomly in straight lines", ["in fixed positions", "in circles around the nucleus", "only when heated"], "Particles move until they collide.")
H('10.A', 3, "According to kinetic molecular theory, how do the collisions of ideal gas particles behave?", "they are perfectly elastic", ["they always lose energy", "they stop the particles", "they create new particles"], "No kinetic energy is lost in collisions.")
H('10.A', 3, "Temperature of a gas is directly related to what?", "the average kinetic energy of the particles", ["the number of particles only", "the size of the particles", "the color of the gas"], "Hotter gas has faster-moving particles.")
H('10.A', 4, "In the ideal gas model, what is assumed about the volume of the gas particles themselves?", "it is negligible compared to the container", ["it equals the volume of the container", "it increases with pressure", "it is zero for all gases"], "Gas particles are far apart.")

# 10.B ideal gas relationships
H('10.B', 3, "A gas at constant temperature is compressed from 2 L to 1 L. What happens to its pressure?", "it doubles", ["it halves", "it stays the same", "it quadruples"], "Boyle's law: pressure and volume are inversely related.")
H('10.B', 3, "At constant pressure, what happens to the volume of a gas when its Kelvin temperature doubles?", "it doubles", ["it halves", "it stays the same", "it quadruples"], "Charles's law: volume is directly proportional to Kelvin temperature.")
H('10.B', 3, "What is 25°C on the Kelvin scale?", "298 K", ["248 K", "25 K", "373 K"], "Add 273 to the Celsius value.")
H('10.B', 3, "Which equation is the ideal gas law?", "PV = nRT", ["P = nRT/V²", "PV = T", "P/V = nR"], "Pressure times volume equals moles times R times temperature.")
H('10.B', 4, "At constant volume, what happens to a gas's pressure when its Kelvin temperature doubles?", "it doubles", ["it halves", "it stays the same", "it becomes zero"], "Pressure is directly proportional to temperature at constant volume.")

# 10.C Dalton's law
H('10.C', 3, "A container holds 2 atm of nitrogen and 1 atm of oxygen. What is the total pressure?", "3 atm", ["2 atm", "1 atm", "0.5 atm"], "Total pressure is the sum of partial pressures.")
H('10.C', 4, "Oxygen is 21% of the gas in air at a total pressure of 1 atm. What is its partial pressure?", "0.21 atm", ["21 atm", "0.79 atm", "1 atm"], "Mole fraction times total pressure.")
H('10.C', 3, "What does Dalton's law of partial pressures state?", "the total pressure of a gas mixture is the sum of each gas's partial pressure", ["gas pressure is always constant", "each gas has the same pressure", "pressure depends only on temperature"], "Each gas acts independently.")

# 11.A water and polarity
H('11.A', 3, "Why is water a good solvent for ionic compounds?", "its polar molecules attract and surround ions", ["its molecules are nonpolar", "it contains many ions", "it is a metal"], "Partial charges on water pull ions apart.")
H('11.A', 3, "Why do oil and water not mix?", "oil is nonpolar and water is polar", ["both are ionic", "oil is heavier than water", "water is a gas"], "Like dissolves like.")
H('11.A', 2, "Why is a water molecule polar?", "its shape is bent and oxygen attracts electrons more strongly", ["it is linear with equal sharing", "it contains ions", "it has no lone pairs"], "Partial negative charge on O and partial positive on H.")
H('11.A', 3, "What does the phrase 'like dissolves like' mean?", "polar solvents dissolve polar solutes and nonpolar solvents dissolve nonpolar solutes", ["solids dissolve solids", "all substances dissolve in water", "similar colors dissolve"], "Similar intermolecular forces allow mixing.")

# 11.B types of solutions
H('11.B', 3, "What is an electrolyte?", "a substance that conducts electricity when dissolved in water", ["a substance that is a solid at room temperature", "a substance that does not dissolve", "a gas"], "Ions carry the current.")
H('11.B', 3, "Sugar dissolved in water does not conduct electricity. What type of substance is sugar?", "a nonelectrolyte", ["an electrolyte", "an ionic compound", "a metal"], "It dissolves as molecules, not ions.")
H('11.B', 3, "What is a saturated solution?", "one that holds the maximum amount of solute at that temperature", ["one that can still dissolve more solute", "one with no solute", "one that is a gas"], "No more solute can dissolve.")
H('11.B', 4, "What is a supersaturated solution?", "one that holds more solute than normal, which is unstable", ["one that holds no solute", "one with less than the maximum solute", "a stable solution"], "It is usually made by cooling a hot saturated solution carefully.")

# 11.C solubility and temperature
H('11.C', 3, "What generally happens to the solubility of most solids as temperature increases?", "it increases", ["it decreases", "it stays the same", "it becomes zero"], "More sugar dissolves in hot tea than in cold.")
H('11.C', 3, "What generally happens to the solubility of gases in water as temperature increases?", "it decreases", ["it increases", "it stays the same", "it doubles"], "Warm soda goes flat faster.")
H('11.C', 3, "Which of these will speed up the rate at which a solid dissolves?", "crushing it and stirring", ["leaving it as a large chunk and not stirring", "cooling the mixture", "adding more solid"], "More surface area and mixing help.")

# 11.D solubility rules
H('11.D', 3, "According to the solubility rules, which type of salt is always soluble?", "nitrates", ["carbonates", "sulfides", "hydroxides"], "Nitrates are soluble in water.")
H('11.D', 3, "Silver chloride is insoluble in water. What would you expect to see if AgNO₃ and NaCl solutions are mixed?", "a white solid forms", ["a gas forms", "no change at all", "the solution boils"], "AgCl precipitates.")
H('11.D', 4, "When solutions of Pb(NO₃)₂ and KI are mixed, which product is the precipitate?", "PbI₂", ["KNO₃", "Pb(NO₃)₂", "KI"], "KNO₃ is soluble, but PbI₂ is not.")
H('11.D', 3, "Compounds containing group 1 metal ions (such as Na⁺ or K⁺) are generally what?", "soluble in water", ["insoluble in water", "gases", "unreactive"], "They are soluble in almost all cases.")

# 11.E molarity
H('11.E', 3, "What is the molarity of a solution with 2 mol of solute in 4 L of solution?", "0.5 M", ["2 M", "8 M", "4 M"], "M = moles ÷ liters.")
H('11.E', 3, "How many moles of solute are in 0.25 L of a 2 M solution?", "0.5 mol", ["8 mol", "2 mol", "0.125 mol"], "Moles = M × L.")
H('11.E', 4, "58.5 g of NaCl (molar mass 58.5 g/mol) is dissolved to make 1 L of solution. What is the molarity?", "1 M", ["58.5 M", "0.5 M", "2 M"], "One mole per liter.")
H('11.E', 3, "Which unit is used for molarity?", "moles per liter", ["grams per mole", "liters per mole", "moles per gram"], "mol/L.")

# 11.F dilutions
H('11.F', 3, "If 50 mL of a 2 M solution is diluted to 100 mL, what is the new concentration?", "1 M", ["4 M", "2 M", "0.5 M"], "M₁V₁ = M₂V₂.")
H('11.F', 4, "How much 5 M stock is needed to make 500 mL of 0.5 M solution?", "50 mL", ["500 mL", "5 mL", "250 mL"], "5(V) = 0.5(500).")
H('11.F', 3, "When a solution is diluted by adding water, what happens to the amount of solute?", "it stays the same", ["it doubles", "it decreases", "it disappears"], "Only the volume increases.")

# 12.A naming acids and bases
H('12.A', 2, "What is the name of HCl in water?", "hydrochloric acid", ["chloric acid", "hydrogen chlorine", "perchloric acid"], "Binary acids use the hydro- prefix and -ic ending.")
H('12.A', 3, "What is the formula for sulfuric acid?", "H₂SO₄", ["HSO₄", "H₂SO₃", "H₂S"], "It contains the sulfate ion.")
H('12.A', 2, "What is the name of NaOH?", "sodium hydroxide", ["sodium oxide", "sodium hydride", "sodium hydrogen"], "Hydroxides contain the OH⁻ ion.")
H('12.A', 3, "What is the formula for calcium hydroxide?", "Ca(OH)₂", ["CaOH", "CaOH₂", "Ca₂OH"], "One Ca²⁺ needs two OH⁻ ions.")
H('12.A', 3, "What is the name of HNO₃?", "nitric acid", ["nitrous acid", "nitrate acid", "hydronitric acid"], "The nitrate ion gives an -ic acid.")

# 12.B acid and base definitions
H('12.B', 3, "By the Arrhenius definition, what does an acid produce in water?", "hydrogen ions (H⁺)", ["hydroxide ions (OH⁻)", "electrons", "neutrons"], "Arrhenius acids increase H⁺.")
H('12.B', 3, "By the Brønsted-Lowry definition, what does an acid do?", "donates a proton", ["accepts a proton", "donates an electron", "accepts an electron"], "Brønsted-Lowry acids are proton donors.")
H('12.B', 3, "By the Brønsted-Lowry definition, what does a base do?", "accepts a proton", ["donates a proton", "donates an electron", "accepts a neutron"], "Bases are proton acceptors.")
H('12.B', 4, "Why is NH₃ a base by the Brønsted-Lowry definition but not by the Arrhenius definition?", "it accepts protons but does not contain OH⁻", ["it releases H⁺", "it has no nitrogen", "it donates protons"], "The Brønsted-Lowry definition is broader.")

# 12.C strong and weak
H('12.C', 3, "What makes an acid strong?", "it ionizes completely in water", ["it is very concentrated", "it has a high pH", "it ionizes only slightly"], "Strong acids fully dissociate.")
H('12.C', 3, "Which of these is a strong acid?", "HCl", ["CH₃COOH", "H₂CO₃", "NH₃"], "HCl is one of the common strong acids.")
H('12.C', 3, "Acetic acid ionizes only slightly in water. What type of acid is it?", "weak", ["strong", "neutral", "a base"], "Only a small fraction forms ions.")
H('12.C', 4, "How does 'strong' differ from 'concentrated' for acids?", "strength is about ionization, while concentration is about amount dissolved", ["they mean the same thing", "strength is about volume", "concentration is about ionization"], "A weak acid can be concentrated and a strong acid can be dilute.")

# 12.D neutralization
H('12.D', 3, "What are the products of an acid reacting with a base?", "a salt and water", ["a salt and hydrogen gas", "an acid and a base", "oxygen and water"], "This is neutralization.")
H('12.D', 3, "What are the products of HNO₃ + KOH?", "KNO₃ and H₂O", ["K and HNO₃", "NO₂ and KOH", "KH and O₂"], "The metal ion pairs with the anion to form the salt.")
H('12.D', 4, "What is the balanced equation for sulfuric acid reacting with potassium hydroxide?", "H₂SO₄ + 2KOH → K₂SO₄ + 2H₂O", ["H₂SO₄ + KOH → KSO₄ + H₂O", "H₂SO₄ + 2KOH → K₂SO₄ + H₂O", "2H₂SO₄ + KOH → K₂SO₄ + 2H₂O"], "Two OH⁻ are needed for each H₂SO₄.")

# 12.E pH
H('12.E', 3, "What is the pH of a solution with [H⁺] = 1 × 10⁻³ M?", "3", ["−3", "11", "0.001"], "pH = −log[H⁺].")
H('12.E', 3, "What is the pH of a neutral solution at 25°C?", "7", ["0", "14", "1"], "[H⁺] = 1 × 10⁻⁷ M.")
H('12.E', 4, "A solution has pH 3. Another has pH 5. Which is more acidic, and by how much?", "pH 3, by a factor of 100", ["pH 5, by a factor of 2", "pH 3, by a factor of 2", "they are equally acidic"], "Each pH unit is a factor of 10 in [H⁺].")
H('12.E', 3, "What is the pH of a solution with [H⁺] = 1 × 10⁻¹⁰ M?", "10", ["−10", "4", "1"], "−log(10⁻¹⁰).")
H('12.E', 3, "A solution has a pH of 9. What type of solution is it?", "basic", ["acidic", "neutral", "strongly acidic"], "pH above 7 is basic.")

# 13.A laws of thermodynamics
H('13.A', 3, "A hot cup of cocoa cools to room temperature. Which idea does this illustrate?", "heat flows from hot to cold until equilibrium", ["heat flows from cold to hot", "energy is destroyed", "the temperature never changes"], "Thermal equilibrium.")
H('13.A', 3, "What does the first law of thermodynamics state?", "energy cannot be created or destroyed", ["entropy always decreases", "heat flows from cold to hot", "temperature is constant"], "Energy is conserved.")
H('13.A', 4, "What does the second law of thermodynamics say about the entropy of an isolated system?", "it tends to increase", ["it tends to decrease", "it stays exactly the same", "it is always zero"], "Spontaneous processes increase disorder.")
H('13.A', 4, "What does the third law of thermodynamics imply about absolute zero?", "it cannot be reached in a finite number of steps", ["it is easily reached", "it is 100°C", "matter becomes infinite"], "Entropy approaches a minimum at absolute zero.")

# 13.B calorimetry
H('13.B', 3, "What does a calorimeter measure?", "heat transferred in a physical or chemical change", ["mass of a sample", "length of a sample", "voltage of a battery"], "It is an insulated container for measuring heat.")
H('13.B', 3, "A hot metal is dropped into cool water in an insulated cup. What happens to the water's temperature?", "it rises as the metal cools", ["it falls", "it stays exactly the same", "it freezes"], "Heat lost by the metal equals heat gained by the water.")
H('13.B', 4, "In calorimetry, why is the cup insulated?", "to keep heat from escaping to the surroundings", ["to make the reaction faster", "to add heat", "to remove water"], "It lets the heat exchange be measured within the system.")

# 13.C exothermic and endothermic
H('13.C', 2, "Which process is exothermic?", "burning wood", ["melting ice", "boiling water", "evaporating a puddle"], "Combustion releases heat.")
H('13.C', 3, "What does a negative ΔH indicate?", "heat is released (exothermic)", ["heat is absorbed (endothermic)", "no energy change", "an error"], "The products have lower energy than the reactants.")
H('13.C', 3, "An instant cold pack gets cold when activated. What type of process is this?", "endothermic", ["exothermic", "nuclear", "neither"], "It absorbs heat from its surroundings.")
H('13.C', 3, "In an endothermic reaction, how does the energy of the products compare with the reactants?", "the products have more energy", ["the products have less energy", "they have equal energy", "the products have no energy"], "Energy is absorbed.")

# 13.D heat calculations
H('13.D', 3, "How much heat is needed to raise 100 g of water by 10°C? (c = 4.18 J/g°C)", "4180 J", ["418 J", "41.8 J", "1000 J"], "q = mcΔT.")
H('13.D', 4, "How much heat does 50 g of a metal (c = 0.50 J/g°C) release when it cools by 20°C?", "500 J", ["50 J", "1250 J", "25 J"], "q = 50 × 0.50 × 20.")
H('13.D', 4, "2090 J of heat raises the temperature of 50 g of water (c = 4.18 J/g°C). By how many degrees?", "10°C", ["5°C", "100°C", "41.8°C"], "ΔT = q ÷ (mc).")
H('13.D', 3, "What does specific heat measure?", "the heat needed to raise 1 g of a substance by 1°C", ["the heat needed to melt 1 g", "the total energy in a substance", "the temperature of a substance"], "Different materials have different specific heats.")

# 14.A radioactive decay
H('14.A', 3, "What is an alpha particle?", "a helium nucleus (2 protons and 2 neutrons)", ["an electron", "a high-energy photon", "a neutron"], "Alpha decay reduces the mass number by 4.")
H('14.A', 3, "In beta decay, a neutron changes into what?", "a proton, with an electron emitted", ["an alpha particle", "a gamma ray only", "a helium nucleus"], "The atomic number increases by 1.")
H('14.A', 4, "In the decay of uranium-238 by alpha emission, what is the product? (U-238 → ? + He-4)", "thorium-234", ["thorium-242", "protactinium-238", "lead-206"], "Mass 238 − 4 = 234 and atomic number 92 − 2 = 90.")
H('14.A', 3, "Which type of radiation is stopped by a sheet of paper but is the least penetrating?", "alpha", ["beta", "gamma", "x-ray"], "Alpha particles are large and slow.")
H('14.A', 3, "Gamma rays change the atomic number and the mass number of a nucleus how?", "they change neither", ["they raise the atomic number by 2", "they lower the mass number by 4", "they double both"], "Gamma rays are energy released from the nucleus.")

# 14.B fission and fusion
H('14.B', 2, "What happens in nuclear fission?", "a heavy nucleus splits into smaller nuclei", ["two light nuclei combine", "electrons are shared", "atoms are ionized"], "For example, uranium-235 splitting.")
H('14.B', 2, "What happens in nuclear fusion?", "light nuclei combine to form a heavier nucleus", ["a heavy nucleus splits", "an electron is lost", "a neutron decays"], "Hydrogen fuses to helium in the Sun.")
H('14.B', 3, "Why does fusion require extremely high temperatures?", "to overcome the repulsion between positive nuclei", ["to melt the electrons", "to cool the nuclei", "to make neutrons heavier"], "Nuclei must get close enough to fuse.")
H('14.B', 3, "Where does the energy released in nuclear reactions come from?", "a small amount of mass converted to energy", ["chemical bonds breaking", "electrons moving", "friction"], "E = mc².")

# 14.C applications of nuclear phenomena
H('14.C', 3, "A sample with a half-life of 5 days starts at 80 g. How much remains after 10 days?", "20 g", ["40 g", "10 g", "0 g"], "Two half-lives leave one quarter.")
H('14.C', 3, "Which nuclear application is used to estimate the age of ancient organic materials?", "carbon-14 dating", ["fission power plants", "fusion in the Sun", "alpha decay of uranium only"], "C-14 decays at a known rate.")
H('14.C', 3, "How is radiation used in cancer therapy?", "it is aimed at tumors to damage and kill cancer cells", ["it heals all cells", "it makes cells grow", "it is applied only to healthy tissue"], "Focused radiation damages the DNA of tumor cells.")
H('14.C', 3, "Radioactive tracers are used in PET scans for what purpose?", "to create images of processes inside the body", ["to measure bone length", "to heat tissue", "to repair DNA"], "Detectors track the emitted radiation.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_chem.jsonl'))

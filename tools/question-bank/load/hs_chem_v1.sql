insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_chem_v1'
from (values
('112.43.c.5.A',3,'Mendeleev left gaps in his periodic table. What did he do with those gaps?','["predicted that undiscovered elements would fill them", "filled them with noble gases", "declared that they were errors", "removed those columns"]'::jsonb,0,'He predicted properties of missing elements, and later discoveries matched.','original'),
('112.43.c.5.A',3,'The modern periodic table is arranged by increasing what?','["number of neutrons", "atomic number", "atomic mass", "density"]'::jsonb,1,'Moseley''s work showed that atomic number orders the elements.','original'),
('112.43.c.5.A',3,'Why do elements in the same column of the periodic table have similar chemical properties?','["they have the same mass", "they have the same number of neutrons", "they have the same number of valence electrons", "they have the same number of shells"]'::jsonb,2,'Valence electrons drive chemical behavior.','original'),
('112.43.c.5.A',4,'What does the periodic law state?','["elements cannot be grouped", "properties depend only on mass", "all elements have equal properties", "element properties repeat in a pattern as atomic number increases"]'::jsonb,3,'Properties are a periodic function of atomic number.','original'),
('112.43.c.5.B',2,'Which family of elements is highly reactive and forms 1+ ions?','["alkali metals", "noble gases", "transition metals", "halogens"]'::jsonb,0,'They have one valence electron to lose.','original'),
('112.43.c.5.B',2,'Which family of elements is generally unreactive because it has a full valence shell?','["halogens", "noble gases", "alkali metals", "alkaline earth metals"]'::jsonb,1,'A complete outer shell is very stable.','original'),
('112.43.c.5.B',3,'Which element should behave most like magnesium?','["neon", "chlorine", "calcium", "sodium"]'::jsonb,2,'They are in the same group.','original'),
('112.43.c.5.B',3,'Halogens typically form which kind of ion?','["2+ ions", "no ions at all", "1+ ions", "1− ions"]'::jsonb,3,'They gain one electron to fill the valence shell.','original'),
('112.43.c.5.B',3,'Which statement describes alkaline earth metals?','["they are reactive metals that form 2+ ions", "they are unreactive gases", "they are nonmetals", "they form 1− ions"]'::jsonb,0,'They have two valence electrons.','original'),
('112.43.c.5.C',3,'As you move left to right across a period, what generally happens to atomic radius?','["it doubles", "it decreases", "it increases", "it stays the same"]'::jsonb,1,'A growing nuclear charge pulls the electrons closer.','original'),
('112.43.c.5.C',3,'As you move down a group, what generally happens to atomic radius?','["it is not related to group", "it stays the same", "it increases", "it decreases"]'::jsonb,2,'Each period adds another electron shell.','original'),
('112.43.c.5.C',3,'Which of these elements has the largest atomic radius: Li, Na, K or Cs?','["Li", "Na", "K", "Cs"]'::jsonb,3,'Cs is lowest in the group.','original'),
('112.43.c.5.C',3,'Which element has the highest electronegativity?','["fluorine", "cesium", "helium", "sodium"]'::jsonb,0,'Fluorine pulls shared electrons the most strongly.','original'),
('112.43.c.5.C',4,'Which of these elements has the highest first ionization energy: Na, Mg, Al or Cl?','["Al", "Cl", "Na", "Mg"]'::jsonb,1,'Ionization energy generally increases across a period.','original'),
('112.43.c.6.A',2,'Which scientist''s gold foil experiment showed that atoms have a small, dense, positive nucleus?','["Dalton", "Thomson", "Rutherford", "Bohr"]'::jsonb,2,'Most particles passed through, but a few were deflected sharply.','original'),
('112.43.c.6.A',3,'Thomson''s discovery of the electron led to what model of the atom?','["electrons in fixed energy levels", "a nucleus with an electron cloud", "a solid indivisible sphere", "a positive sphere with electrons embedded in it"]'::jsonb,3,'This was nicknamed the plum pudding model.','original'),
('112.43.c.6.A',3,'What did Bohr''s model add to the picture of the atom?','["electrons in fixed energy levels around the nucleus", "a nucleus with no charge", "electrons that are not in the atom", "indivisible atoms"]'::jsonb,0,'Electrons occupy specific orbits with set energies.','original'),
('112.43.c.6.A',3,'Dalton''s model described atoms as what?','["made of protons and neutrons", "tiny, indivisible spheres", "mostly empty space", "a nucleus surrounded by an electron cloud"]'::jsonb,1,'Dalton did not know about subatomic particles.','original'),
('112.43.c.6.A',3,'The modern model of the atom describes electrons as being where?','["in a solid shell", "in fixed circular paths", "in probability clouds called orbitals", "inside the nucleus"]'::jsonb,2,'Electrons are found by likelihood, not set paths.','original'),
('112.43.c.6.B',2,'Where are protons and neutrons found in an atom?','["in the electron cloud", "in the outer shell", "in the orbitals", "in the nucleus"]'::jsonb,3,'Nearly all of the atom''s mass is in the nucleus.','original'),
('112.43.c.6.B',2,'What is the charge of a neutron?','["zero", "positive", "negative", "variable"]'::jsonb,0,'Neutrons are neutral.','original'),
('112.43.c.6.B',3,'A sodium atom has atomic number 11 and mass number 23. How many neutrons does it have?','["23", "12", "11", "34"]'::jsonb,1,'Neutrons = mass number − atomic number.','original'),
('112.43.c.6.B',3,'How many protons and electrons does a Mg²⁺ ion have (atomic number 12)?','["14 protons and 12 electrons", "12 protons and 14 electrons", "12 protons and 10 electrons", "10 protons and 12 electrons"]'::jsonb,2,'A 2+ charge means two electrons were lost.','original'),
('112.43.c.6.B',3,'How many electrons does a Cl⁻ ion have (atomic number 17)?','["35", "16", "17", "18"]'::jsonb,3,'The ion has gained one electron.','original'),
('112.43.c.6.C',3,'A photon of which visible color carries the most energy?','["violet", "red", "yellow", "orange"]'::jsonb,0,'Higher frequency means higher energy.','original'),
('112.43.c.6.C',3,'If the wavelength of light increases, what happens to its frequency?','["it stays the same", "it decreases", "it doubles", "it increases"]'::jsonb,1,'c = λν, so they vary inversely.','original'),
('112.43.c.6.C',3,'Which electromagnetic waves have the highest energy?','["radio waves", "visible light", "gamma rays", "microwaves"]'::jsonb,2,'Gamma rays have the shortest wavelengths.','original'),
('112.43.c.6.C',4,'Which equation relates a photon''s energy to its frequency?','["E = mc", "E = h/ν", "E = λ/ν", "E = hν"]'::jsonb,3,'h is Planck''s constant.','original'),
('112.43.c.6.D',3,'An element has 75% of an isotope with mass 35 and 25% of an isotope with mass 37. What is its average atomic mass?','["35.5", "36.0", "37.0", "35.0"]'::jsonb,0,'0.75(35) + 0.25(37).','original'),
('112.43.c.6.D',3,'An element has two isotopes of equal abundance, with masses 79 and 81. What is its average atomic mass?','["81", "80", "160", "79"]'::jsonb,1,'The average of the two masses.','original'),
('112.43.c.6.D',4,'Boron is 20% boron-10 and 80% boron-11. What is its average atomic mass?','["10.5", "11.0", "10.8", "10.2"]'::jsonb,2,'0.20(10) + 0.80(11).','original'),
('112.43.c.6.D',3,'What are isotopes?','["atoms with different numbers of protons", "atoms with different electrons only", "ions with different charges", "atoms of the same element with different numbers of neutrons"]'::jsonb,3,'Isotopes have the same atomic number but different mass numbers.','original'),
('112.43.c.6.E',3,'What is the electron configuration of sodium (atomic number 11)?','["1s² 2s² 2p⁶ 3s¹", "1s² 2s² 2p⁵", "1s² 2s² 2p⁶ 3s²", "1s² 2s¹ 2p⁶ 3s²"]'::jsonb,0,'Eleven electrons fill orbitals in order.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Science' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_chem_v1'
from (values
('112.43.c.6.E',3,'How many valence electrons does oxygen have?','["8", "6", "16", "2"]'::jsonb,1,'Oxygen is in group 16, with 6 valence electrons.','original'),
('112.43.c.6.E',3,'How many valence electrons does chlorine have?','["1", "8", "7", "17"]'::jsonb,2,'Chlorine is in group 17.','original'),
('112.43.c.6.E',4,'Which statement is true of the Mg²⁺ ion?','["it has the same configuration as magnesium", "it has the same configuration as sodium atom''s valence shell", "it has no electrons", "its electron configuration is the same as neon''s"]'::jsonb,3,'Losing two valence electrons gives 1s² 2s² 2p⁶.','original'),
('112.43.c.6.E',4,'According to Hund''s rule, how do electrons fill orbitals of equal energy?','["one per orbital first, with parallel spins", "in the nucleus first", "randomly, with opposite spins", "two per orbital first"]'::jsonb,0,'Electrons spread out before pairing up.','original'),
('112.43.c.7.A',3,'A large electronegativity difference between two atoms usually leads to what type of bond?','["nonpolar covalent", "ionic", "metallic", "no bond"]'::jsonb,1,'Electrons are effectively transferred.','original'),
('112.43.c.7.A',3,'Two identical atoms (as in Cl₂) form what type of bond?','["metallic", "ionic", "nonpolar covalent", "polar covalent"]'::jsonb,2,'There is no difference in electronegativity.','original'),
('112.43.c.7.A',4,'Why is the bond in HCl polar covalent?','["electrons are fully transferred to hydrogen", "the atoms share electrons equally", "the bond is made of metal atoms", "chlorine attracts the shared electrons more strongly than hydrogen"]'::jsonb,3,'Unequal sharing creates partial charges.','original'),
('112.43.c.7.A',3,'Which pair is most likely to form an ionic bond?','["sodium and chlorine", "carbon and oxygen", "nitrogen and hydrogen", "chlorine and chlorine"]'::jsonb,0,'A metal and a nonmetal usually form ionic bonds.','original'),
('112.43.c.7.B',2,'What is the name of NaCl?','["natrium chlorate", "sodium chloride", "sodium chlorine", "salt chloride"]'::jsonb,1,'Metal name followed by the nonmetal name ending in -ide.','original'),
('112.43.c.7.B',3,'What is the formula for calcium chloride?','["CaCl₃", "Ca₂Cl", "CaCl₂", "CaCl"]'::jsonb,2,'Ca²⁺ needs two Cl⁻ ions.','original'),
('112.43.c.7.B',3,'What is the name of CO₂?','["carbon oxide", "monocarbon dioxide", "carbonic oxygen", "carbon dioxide"]'::jsonb,3,'A covalent compound uses prefixes.','original'),
('112.43.c.7.B',3,'What is the formula for aluminum oxide?','["Al₂O₃", "Al₃O₂", "AlO₃", "AlO"]'::jsonb,0,'Two Al³⁺ balance three O²⁻.','original'),
('112.43.c.7.B',4,'What is the formula for iron(III) oxide?','["FeO", "Fe₂O₃", "Fe₃O₂", "FeO₃"]'::jsonb,1,'The Roman numeral gives the 3+ charge on iron.','original'),
('112.43.c.7.B',4,'What is the formula for potassium sulfate?','["K₂S", "KSO₄", "K₂SO₄", "K(SO₄)₂"]'::jsonb,2,'Two K⁺ balance one SO₄²⁻.','original'),
('112.43.c.7.C',3,'What is the shape of a water molecule?','["tetrahedral", "linear", "trigonal planar", "bent"]'::jsonb,3,'Two lone pairs push the bonds into a bent shape.','original'),
('112.43.c.7.C',3,'What is the shape of a methane (CH₄) molecule?','["tetrahedral", "bent", "trigonal pyramidal", "linear"]'::jsonb,0,'Four bonding pairs and no lone pairs.','original'),
('112.43.c.7.C',3,'What is the shape of a carbon dioxide molecule?','["tetrahedral", "linear", "bent", "trigonal pyramidal"]'::jsonb,1,'Two double bonds on opposite sides of carbon.','original'),
('112.43.c.7.C',4,'What is the shape of an ammonia (NH₃) molecule?','["trigonal planar", "tetrahedral", "trigonal pyramidal", "bent"]'::jsonb,2,'Three bonds and one lone pair on nitrogen.','original'),
('112.43.c.7.C',4,'How many valence electrons are shown in the Lewis structure of CO₂?','["18", "12", "8", "16"]'::jsonb,3,'4 + 6 + 6.','original'),
('112.43.c.7.C',3,'BF₃ has three bonding pairs and no lone pairs on the central atom. What is its shape?','["trigonal planar", "trigonal pyramidal", "tetrahedral", "bent"]'::jsonb,0,'Three regions spread out flat.','original'),
('112.43.c.7.D',3,'Why do ionic compounds have high melting points?','["weak attractions between molecules", "strong attractions between oppositely charged ions", "free-moving electrons in the structure", "mostly nonpolar bonds"]'::jsonb,1,'A lot of energy is needed to break the crystal.','original'),
('112.43.c.7.D',3,'Why can metals conduct electricity?','["they have no electrons", "they have covalent bonds", "their valence electrons move freely", "their ions are free to move"]'::jsonb,2,'A sea of electrons carries charge.','original'),
('112.43.c.7.D',4,'What explains the unusually high boiling point of water for its size?','["weak London forces only", "ionic bonding between H and O", "metallic bonding", "hydrogen bonding between molecules"]'::jsonb,3,'Hydrogen bonds hold molecules together strongly.','original'),
('112.43.c.7.D',3,'How do the forces between molecules compare with the covalent bonds inside them?','["forces between molecules are generally weaker", "forces between molecules do not exist", "they are exactly equal", "they are always stronger"]'::jsonb,0,'That is why molecular substances melt easily.','original'),
('112.43.c.7.D',3,'Which type of substance generally conducts electricity when dissolved in water?','["nonpolar gases", "ionic compounds", "sugar", "oil"]'::jsonb,1,'The ions are free to move in solution.','original'),
('112.43.c.8.A',3,'What is the molar mass of water (H₂O)? (H = 1, O = 16)','["17 g/mol", "16 g/mol", "18 g/mol", "34 g/mol"]'::jsonb,2,'2(1) + 16.','original'),
('112.43.c.8.A',3,'How many moles are in 36 g of water (molar mass 18 g/mol)?','["0.5 mol", "18 mol", "648 mol", "2 mol"]'::jsonb,3,'36 ÷ 18.','original'),
('112.43.c.8.A',3,'What is the mass of 0.5 mol of CO₂ (molar mass 44 g/mol)?','["22 g", "88 g", "2 g", "44 g"]'::jsonb,0,'0.5 × 44.','original'),
('112.43.c.8.A',3,'How many moles are in 58.5 g of NaCl (molar mass 58.5 g/mol)?','["2 mol", "1 mol", "0.1 mol", "58.5 mol"]'::jsonb,1,'One molar mass equals one mole.','original'),
('112.43.c.8.A',3,'What is the mass of 3 mol of carbon (12 g/mol)?','["4 g", "12 g", "36 g", "15 g"]'::jsonb,2,'3 × 12.','original'),
('112.43.c.8.B',2,'What is Avogadro''s number?','["3.00 × 10⁸", "6.02 × 10¹²", "1.60 × 10⁻¹⁹", "6.02 × 10²³"]'::jsonb,3,'The number of particles in one mole.','original'),
('112.43.c.8.B',3,'About how many molecules are in 2 mol of a substance?','["1.2 × 10²⁴", "12 × 10²²", "3.0 × 10²³", "6.02 × 10²³"]'::jsonb,0,'2 × 6.02 × 10²³.','original'),
('112.43.c.8.B',3,'About how many molecules are in 0.5 mol of a substance?','["1.2 × 10²⁴", "3.01 × 10²³", "0.5 × 10²³", "6.02 × 10²³"]'::jsonb,1,'Half of 6.02 × 10²³.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Science' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_chem_v1'
from (values
('112.43.c.8.B',4,'About how many water molecules are in 18 g of water?','["18", "3.0 × 10²³", "6.02 × 10²³", "1.1 × 10²⁵"]'::jsonb,2,'18 g is one mole.','original'),
('112.43.c.8.C',3,'What is the percent hydrogen by mass in H₂O? (H = 1, O = 16)','["33.3%", "88.9%", "5.6%", "11.1%"]'::jsonb,3,'2/18 × 100.','original'),
('112.43.c.8.C',3,'What is the percent carbon by mass in CO₂? (C = 12, O = 16)','["27.3%", "12%", "72.7%", "50%"]'::jsonb,0,'12/44 × 100.','original'),
('112.43.c.8.C',3,'What do the percent compositions of all elements in a compound add up to?','["1000%", "100%", "a different value for each compound", "50%"]'::jsonb,1,'They account for all the mass.','original'),
('112.43.c.8.C',4,'What is the percent oxygen by mass in MgO? (Mg = 24, O = 16)','["24%", "60%", "40%", "16%"]'::jsonb,2,'16/40 × 100.','original'),
('112.43.c.8.D',3,'What is the empirical formula of glucose, C₆H₁₂O₆?','["C₆H₁₂O₆", "C₂H₄O₂", "CHO", "CH₂O"]'::jsonb,3,'Divide all subscripts by 6.','original'),
('112.43.c.8.D',3,'What does an empirical formula show?','["the simplest whole-number ratio of atoms", "the number of electrons", "the shape of the molecule", "the exact number of atoms in a molecule"]'::jsonb,0,'The molecular formula is a multiple of it.','original'),
('112.43.c.8.D',4,'A compound has empirical formula CH₂ and a molar mass of 56 g/mol. What is its molecular formula?','["C₂H₄", "C₄H₈", "C₈H₁₆", "CH₂"]'::jsonb,1,'CH₂ is 14 g/mol, and 56 ÷ 14 = 4.','original'),
('112.43.c.8.D',3,'What is the empirical formula of hydrogen peroxide, H₂O₂?','["H₂O", "H₂O₂", "HO", "HO₂"]'::jsonb,2,'Divide both subscripts by 2.','original'),
('112.43.c.9.A',3,'Which is the balanced equation for the formation of water?','["2H₂ + 2O₂ → 2H₂O", "H₂ + O₂ → H₂O", "H₂ + 2O₂ → 2H₂O", "2H₂ + O₂ → 2H₂O"]'::jsonb,3,'Four hydrogen atoms and two oxygen atoms on each side.','original'),
('112.43.c.9.A',3,'Which is the balanced equation for making ammonia?','["N₂ + 3H₂ → 2NH₃", "N₂ + H₂ → NH₃", "N₂ + 2H₂ → 2NH₃", "2N₂ + 3H₂ → 2NH₃"]'::jsonb,0,'Two N and six H on each side.','original'),
('112.43.c.9.A',3,'What type of reaction is 2H₂O → 2H₂ + O₂?','["synthesis", "decomposition", "double replacement", "single replacement"]'::jsonb,1,'One compound breaks down into simpler substances.','original'),
('112.43.c.9.A',3,'What type of reaction is Zn + CuSO₄ → ZnSO₄ + Cu?','["decomposition", "combustion", "single replacement", "synthesis"]'::jsonb,2,'One element replaces another in a compound.','original'),
('112.43.c.9.A',4,'In the balanced equation 2C₂H₆ + 7O₂ → 4CO₂ + 6H₂O, what is the coefficient of oxygen?','["6", "4", "2", "7"]'::jsonb,3,'The coefficient in front of O₂ is 7.','original'),
('112.43.c.9.A',3,'What are the products of complete combustion of a hydrocarbon?','["carbon dioxide and water", "carbon monoxide and hydrogen", "oxygen and methane", "ash only"]'::jsonb,0,'The carbon and hydrogen are oxidized.','original'),
('112.43.c.9.B',3,'Which equation is an acid-base reaction?','["CaCO₃ → CaO + CO₂", "HCl + NaOH → NaCl + H₂O", "Zn + 2HCl → ZnCl₂ + H₂", "2Na + Cl₂ → 2NaCl"]'::jsonb,1,'An acid and a base form a salt and water.','original'),
('112.43.c.9.B',3,'Mixing AgNO₃(aq) and NaCl(aq) forms solid AgCl. What kind of reaction is this?','["acid-base", "oxidation-reduction", "precipitation", "combustion"]'::jsonb,2,'An insoluble solid forms from solution.','original'),
('112.43.c.9.B',3,'What happens in an oxidation-reduction reaction?','["no change in oxidation numbers", "protons are shared equally", "neutrons are exchanged", "electrons are transferred between species"]'::jsonb,3,'One species loses electrons while another gains them.','original'),
('112.43.c.9.B',3,'In a redox reaction, the substance that loses electrons is said to be what?','["oxidized", "neutralized", "reduced", "precipitated"]'::jsonb,0,'Oxidation is loss of electrons.','original'),
('112.43.c.9.C',3,'In N₂ + 3H₂ → 2NH₃, how many moles of NH₃ form from 3 mol of N₂ (with enough H₂)?','["1.5 mol", "6 mol", "3 mol", "9 mol"]'::jsonb,1,'The ratio of N₂ to NH₃ is 1 to 2.','original'),
('112.43.c.9.C',3,'In 2H₂ + O₂ → 2H₂O, how many moles of O₂ are needed to react with 4 mol of H₂?','["4 mol", "8 mol", "2 mol", "1 mol"]'::jsonb,2,'The ratio of H₂ to O₂ is 2 to 1.','original'),
('112.43.c.9.C',4,'A reaction should give 10 g of product but actually gives 8 g. What is the percent yield?','["125%", "20%", "8%", "80%"]'::jsonb,3,'8 ÷ 10 × 100.','original'),
('112.43.c.9.C',3,'At STP, what volume does 2 mol of any ideal gas occupy?','["44.8 L", "2 L", "11.2 L", "22.4 L"]'::jsonb,0,'One mole occupies 22.4 L at STP.','original'),
('112.43.c.9.C',4,'In 2H₂ + O₂ → 2H₂O, how many grams of water form from 2 mol of H₂? (molar mass of water = 18 g/mol)','["72 g", "36 g", "18 g", "2 g"]'::jsonb,1,'2 mol of H₂ makes 2 mol of water.','original'),
('112.43.c.9.D',3,'What is a limiting reactant?','["the reactant that is left over", "the product that forms first", "the reactant that is used up first and limits the amount of product", "the catalyst of the reaction"]'::jsonb,2,'The reaction stops when it runs out.','original'),
('112.43.c.9.D',4,'In 2H₂ + O₂ → 2H₂O, 4 mol of H₂ are mixed with 1 mol of O₂. Which is limiting?','["H₂O", "H₂", "neither", "O₂"]'::jsonb,3,'1 mol of O₂ needs only 2 mol of H₂.','original'),
('112.43.c.9.D',3,'What is an excess reactant?','["a reactant that remains after the reaction is finished", "a reactant that has no mass", "a reactant that is used up first", "a product that forms in excess"]'::jsonb,0,'Some of it is left unreacted.','original'),
('112.43.c.9.D',4,'A recipe needs 2 slices of bread and 1 slice of cheese per sandwich. With 10 slices of bread and 8 slices of cheese, how many sandwiches can be made, and what limits it?','["10 sandwiches, limited by the cheese", "5 sandwiches, limited by the bread", "5 sandwiches, limited by the cheese", "8 sandwiches, limited by the bread"]'::jsonb,1,'10 ÷ 2 = 5, which is fewer than 8.','original'),
('112.43.c.10.A',3,'According to kinetic molecular theory, how do gas particles move?','["only when heated", "in circles around the nucleus", "constantly and randomly in straight lines", "in fixed positions"]'::jsonb,2,'Particles move until they collide.','original'),
('112.43.c.10.A',3,'According to kinetic molecular theory, how do the collisions of ideal gas particles behave?','["they create new particles", "they stop the particles", "they always lose energy", "they are perfectly elastic"]'::jsonb,3,'No kinetic energy is lost in collisions.','original'),
('112.43.c.10.A',3,'Temperature of a gas is directly related to what?','["the average kinetic energy of the particles", "the number of particles only", "the color of the gas", "the size of the particles"]'::jsonb,0,'Hotter gas has faster-moving particles.','original'),
('112.43.c.10.A',4,'In the ideal gas model, what is assumed about the volume of the gas particles themselves?','["it is zero for all gases", "it is negligible compared to the container", "it increases with pressure", "it equals the volume of the container"]'::jsonb,1,'Gas particles are far apart.','original'),
('112.43.c.10.B',3,'A gas at constant temperature is compressed from 2 L to 1 L. What happens to its pressure?','["it halves", "it stays the same", "it doubles", "it quadruples"]'::jsonb,2,'Boyle''s law: pressure and volume are inversely related.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Science' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_chem_v1'
from (values
('112.43.c.10.B',3,'At constant pressure, what happens to the volume of a gas when its Kelvin temperature doubles?','["it stays the same", "it halves", "it quadruples", "it doubles"]'::jsonb,3,'Charles''s law: volume is directly proportional to Kelvin temperature.','original'),
('112.43.c.10.B',3,'What is 25°C on the Kelvin scale?','["298 K", "248 K", "25 K", "373 K"]'::jsonb,0,'Add 273 to the Celsius value.','original'),
('112.43.c.10.B',3,'Which equation is the ideal gas law?','["P/V = nR", "PV = nRT", "P = nRT/V²", "PV = T"]'::jsonb,1,'Pressure times volume equals moles times R times temperature.','original'),
('112.43.c.10.B',4,'At constant volume, what happens to a gas''s pressure when its Kelvin temperature doubles?','["it halves", "it becomes zero", "it doubles", "it stays the same"]'::jsonb,2,'Pressure is directly proportional to temperature at constant volume.','original'),
('112.43.c.10.C',3,'A container holds 2 atm of nitrogen and 1 atm of oxygen. What is the total pressure?','["1 atm", "0.5 atm", "2 atm", "3 atm"]'::jsonb,3,'Total pressure is the sum of partial pressures.','original'),
('112.43.c.10.C',4,'Oxygen is 21% of the gas in air at a total pressure of 1 atm. What is its partial pressure?','["0.21 atm", "0.79 atm", "21 atm", "1 atm"]'::jsonb,0,'Mole fraction times total pressure.','original'),
('112.43.c.10.C',3,'What does Dalton''s law of partial pressures state?','["each gas has the same pressure", "the total pressure of a gas mixture is the sum of each gas''s partial pressure", "pressure depends only on temperature", "gas pressure is always constant"]'::jsonb,1,'Each gas acts independently.','original'),
('112.43.c.11.A',3,'Why is water a good solvent for ionic compounds?','["it contains many ions", "it is a metal", "its polar molecules attract and surround ions", "its molecules are nonpolar"]'::jsonb,2,'Partial charges on water pull ions apart.','original'),
('112.43.c.11.A',3,'Why do oil and water not mix?','["water is a gas", "oil is heavier than water", "both are ionic", "oil is nonpolar and water is polar"]'::jsonb,3,'Like dissolves like.','original'),
('112.43.c.11.A',2,'Why is a water molecule polar?','["its shape is bent and oxygen attracts electrons more strongly", "it is linear with equal sharing", "it contains ions", "it has no lone pairs"]'::jsonb,0,'Partial negative charge on O and partial positive on H.','original'),
('112.43.c.11.A',3,'What does the phrase ''like dissolves like'' mean?','["solids dissolve solids", "polar solvents dissolve polar solutes and nonpolar solvents dissolve nonpolar solutes", "similar colors dissolve", "all substances dissolve in water"]'::jsonb,1,'Similar intermolecular forces allow mixing.','original'),
('112.43.c.11.B',3,'What is an electrolyte?','["a substance that is a solid at room temperature", "a gas", "a substance that conducts electricity when dissolved in water", "a substance that does not dissolve"]'::jsonb,2,'Ions carry the current.','original'),
('112.43.c.11.B',3,'Sugar dissolved in water does not conduct electricity. What type of substance is sugar?','["a metal", "an ionic compound", "an electrolyte", "a nonelectrolyte"]'::jsonb,3,'It dissolves as molecules, not ions.','original'),
('112.43.c.11.B',3,'What is a saturated solution?','["one that holds the maximum amount of solute at that temperature", "one that is a gas", "one that can still dissolve more solute", "one with no solute"]'::jsonb,0,'No more solute can dissolve.','original'),
('112.43.c.11.B',4,'What is a supersaturated solution?','["a stable solution", "one that holds more solute than normal, which is unstable", "one with less than the maximum solute", "one that holds no solute"]'::jsonb,1,'It is usually made by cooling a hot saturated solution carefully.','original'),
('112.43.c.11.C',3,'What generally happens to the solubility of most solids as temperature increases?','["it stays the same", "it becomes zero", "it increases", "it decreases"]'::jsonb,2,'More sugar dissolves in hot tea than in cold.','original'),
('112.43.c.11.C',3,'What generally happens to the solubility of gases in water as temperature increases?','["it doubles", "it stays the same", "it increases", "it decreases"]'::jsonb,3,'Warm soda goes flat faster.','original'),
('112.43.c.11.C',3,'Which of these will speed up the rate at which a solid dissolves?','["crushing it and stirring", "cooling the mixture", "adding more solid", "leaving it as a large chunk and not stirring"]'::jsonb,0,'More surface area and mixing help.','original'),
('112.43.c.11.D',3,'According to the solubility rules, which type of salt is always soluble?','["hydroxides", "nitrates", "sulfides", "carbonates"]'::jsonb,1,'Nitrates are soluble in water.','original'),
('112.43.c.11.D',3,'Silver chloride is insoluble in water. What would you expect to see if AgNO₃ and NaCl solutions are mixed?','["the solution boils", "a gas forms", "a white solid forms", "no change at all"]'::jsonb,2,'AgCl precipitates.','original'),
('112.43.c.11.D',4,'When solutions of Pb(NO₃)₂ and KI are mixed, which product is the precipitate?','["KI", "Pb(NO₃)₂", "KNO₃", "PbI₂"]'::jsonb,3,'KNO₃ is soluble, but PbI₂ is not.','original'),
('112.43.c.11.D',3,'Compounds containing group 1 metal ions (such as Na⁺ or K⁺) are generally what?','["soluble in water", "insoluble in water", "gases", "unreactive"]'::jsonb,0,'They are soluble in almost all cases.','original'),
('112.43.c.11.E',3,'What is the molarity of a solution with 2 mol of solute in 4 L of solution?','["2 M", "0.5 M", "8 M", "4 M"]'::jsonb,1,'M = moles ÷ liters.','original'),
('112.43.c.11.E',3,'How many moles of solute are in 0.25 L of a 2 M solution?','["8 mol", "0.125 mol", "0.5 mol", "2 mol"]'::jsonb,2,'Moles = M × L.','original'),
('112.43.c.11.E',4,'58.5 g of NaCl (molar mass 58.5 g/mol) is dissolved to make 1 L of solution. What is the molarity?','["58.5 M", "2 M", "0.5 M", "1 M"]'::jsonb,3,'One mole per liter.','original'),
('112.43.c.11.E',3,'Which unit is used for molarity?','["moles per liter", "grams per mole", "liters per mole", "moles per gram"]'::jsonb,0,'mol/L.','original'),
('112.43.c.11.F',3,'If 50 mL of a 2 M solution is diluted to 100 mL, what is the new concentration?','["2 M", "1 M", "0.5 M", "4 M"]'::jsonb,1,'M₁V₁ = M₂V₂.','original'),
('112.43.c.11.F',4,'How much 5 M stock is needed to make 500 mL of 0.5 M solution?','["500 mL", "250 mL", "50 mL", "5 mL"]'::jsonb,2,'5(V) = 0.5(500).','original'),
('112.43.c.11.F',3,'When a solution is diluted by adding water, what happens to the amount of solute?','["it doubles", "it disappears", "it decreases", "it stays the same"]'::jsonb,3,'Only the volume increases.','original'),
('112.43.c.12.A',2,'What is the name of HCl in water?','["hydrochloric acid", "chloric acid", "hydrogen chlorine", "perchloric acid"]'::jsonb,0,'Binary acids use the hydro- prefix and -ic ending.','original'),
('112.43.c.12.A',3,'What is the formula for sulfuric acid?','["H₂SO₃", "H₂SO₄", "HSO₄", "H₂S"]'::jsonb,1,'It contains the sulfate ion.','original'),
('112.43.c.12.A',2,'What is the name of NaOH?','["sodium hydrogen", "sodium oxide", "sodium hydroxide", "sodium hydride"]'::jsonb,2,'Hydroxides contain the OH⁻ ion.','original'),
('112.43.c.12.A',3,'What is the formula for calcium hydroxide?','["CaOH", "Ca₂OH", "CaOH₂", "Ca(OH)₂"]'::jsonb,3,'One Ca²⁺ needs two OH⁻ ions.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Science' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_chem_v1'
from (values
('112.43.c.12.A',3,'What is the name of HNO₃?','["nitric acid", "nitrous acid", "hydronitric acid", "nitrate acid"]'::jsonb,0,'The nitrate ion gives an -ic acid.','original'),
('112.43.c.12.B',3,'By the Arrhenius definition, what does an acid produce in water?','["hydroxide ions (OH⁻)", "hydrogen ions (H⁺)", "neutrons", "electrons"]'::jsonb,1,'Arrhenius acids increase H⁺.','original'),
('112.43.c.12.B',3,'By the Brønsted-Lowry definition, what does an acid do?','["accepts a proton", "accepts an electron", "donates a proton", "donates an electron"]'::jsonb,2,'Brønsted-Lowry acids are proton donors.','original'),
('112.43.c.12.B',3,'By the Brønsted-Lowry definition, what does a base do?','["donates a proton", "donates an electron", "accepts a neutron", "accepts a proton"]'::jsonb,3,'Bases are proton acceptors.','original'),
('112.43.c.12.B',4,'Why is NH₃ a base by the Brønsted-Lowry definition but not by the Arrhenius definition?','["it accepts protons but does not contain OH⁻", "it releases H⁺", "it has no nitrogen", "it donates protons"]'::jsonb,0,'The Brønsted-Lowry definition is broader.','original'),
('112.43.c.12.C',3,'What makes an acid strong?','["it ionizes only slightly", "it ionizes completely in water", "it has a high pH", "it is very concentrated"]'::jsonb,1,'Strong acids fully dissociate.','original'),
('112.43.c.12.C',3,'Which of these is a strong acid?','["NH₃", "CH₃COOH", "HCl", "H₂CO₃"]'::jsonb,2,'HCl is one of the common strong acids.','original'),
('112.43.c.12.C',3,'Acetic acid ionizes only slightly in water. What type of acid is it?','["a base", "neutral", "strong", "weak"]'::jsonb,3,'Only a small fraction forms ions.','original'),
('112.43.c.12.C',4,'How does ''strong'' differ from ''concentrated'' for acids?','["strength is about ionization, while concentration is about amount dissolved", "they mean the same thing", "concentration is about ionization", "strength is about volume"]'::jsonb,0,'A weak acid can be concentrated and a strong acid can be dilute.','original'),
('112.43.c.12.D',3,'What are the products of an acid reacting with a base?','["an acid and a base", "a salt and water", "a salt and hydrogen gas", "oxygen and water"]'::jsonb,1,'This is neutralization.','original'),
('112.43.c.12.D',3,'What are the products of HNO₃ + KOH?','["K and HNO₃", "KH and O₂", "KNO₃ and H₂O", "NO₂ and KOH"]'::jsonb,2,'The metal ion pairs with the anion to form the salt.','original'),
('112.43.c.12.D',4,'What is the balanced equation for sulfuric acid reacting with potassium hydroxide?','["H₂SO₄ + 2KOH → K₂SO₄ + H₂O", "2H₂SO₄ + KOH → K₂SO₄ + 2H₂O", "H₂SO₄ + KOH → KSO₄ + H₂O", "H₂SO₄ + 2KOH → K₂SO₄ + 2H₂O"]'::jsonb,3,'Two OH⁻ are needed for each H₂SO₄.','original'),
('112.43.c.12.E',3,'What is the pH of a solution with [H⁺] = 1 × 10⁻³ M?','["3", "−3", "0.001", "11"]'::jsonb,0,'pH = −log[H⁺].','original'),
('112.43.c.12.E',3,'What is the pH of a neutral solution at 25°C?','["0", "7", "14", "1"]'::jsonb,1,'[H⁺] = 1 × 10⁻⁷ M.','original'),
('112.43.c.12.E',4,'A solution has pH 3. Another has pH 5. Which is more acidic, and by how much?','["they are equally acidic", "pH 5, by a factor of 2", "pH 3, by a factor of 100", "pH 3, by a factor of 2"]'::jsonb,2,'Each pH unit is a factor of 10 in [H⁺].','original'),
('112.43.c.12.E',3,'A solution has a pH of 9. What type of solution is it?','["acidic", "strongly acidic", "neutral", "basic"]'::jsonb,3,'pH above 7 is basic.','original'),
('112.43.c.13.A',3,'A hot cup of cocoa cools to room temperature. Which idea does this illustrate?','["heat flows from hot to cold until equilibrium", "energy is destroyed", "heat flows from cold to hot", "the temperature never changes"]'::jsonb,0,'Thermal equilibrium.','original'),
('112.43.c.13.A',3,'What does the first law of thermodynamics state?','["entropy always decreases", "energy cannot be created or destroyed", "heat flows from cold to hot", "temperature is constant"]'::jsonb,1,'Energy is conserved.','original'),
('112.43.c.13.A',4,'What does the second law of thermodynamics say about the entropy of an isolated system?','["it tends to decrease", "it stays exactly the same", "it tends to increase", "it is always zero"]'::jsonb,2,'Spontaneous processes increase disorder.','original'),
('112.43.c.13.A',4,'What does the third law of thermodynamics imply about absolute zero?','["it is 100°C", "matter becomes infinite", "it is easily reached", "it cannot be reached in a finite number of steps"]'::jsonb,3,'Entropy approaches a minimum at absolute zero.','original'),
('112.43.c.13.B',3,'What does a calorimeter measure?','["heat transferred in a physical or chemical change", "length of a sample", "mass of a sample", "voltage of a battery"]'::jsonb,0,'It is an insulated container for measuring heat.','original'),
('112.43.c.13.B',3,'A hot metal is dropped into cool water in an insulated cup. What happens to the water''s temperature?','["it freezes", "it rises as the metal cools", "it falls", "it stays exactly the same"]'::jsonb,1,'Heat lost by the metal equals heat gained by the water.','original'),
('112.43.c.13.B',4,'In calorimetry, why is the cup insulated?','["to make the reaction faster", "to add heat", "to keep heat from escaping to the surroundings", "to remove water"]'::jsonb,2,'It lets the heat exchange be measured within the system.','original'),
('112.43.c.13.C',2,'Which process is exothermic?','["boiling water", "evaporating a puddle", "melting ice", "burning wood"]'::jsonb,3,'Combustion releases heat.','original'),
('112.43.c.13.C',3,'What does a negative ΔH indicate?','["heat is released (exothermic)", "no energy change", "an error", "heat is absorbed (endothermic)"]'::jsonb,0,'The products have lower energy than the reactants.','original'),
('112.43.c.13.C',3,'An instant cold pack gets cold when activated. What type of process is this?','["neither", "endothermic", "exothermic", "nuclear"]'::jsonb,1,'It absorbs heat from its surroundings.','original'),
('112.43.c.13.C',3,'In an endothermic reaction, how does the energy of the products compare with the reactants?','["the products have less energy", "the products have no energy", "the products have more energy", "they have equal energy"]'::jsonb,2,'Energy is absorbed.','original'),
('112.43.c.13.D',3,'How much heat is needed to raise 100 g of water by 10°C? (c = 4.18 J/g°C)','["1000 J", "418 J", "41.8 J", "4180 J"]'::jsonb,3,'q = mcΔT.','original'),
('112.43.c.13.D',4,'How much heat does 50 g of a metal (c = 0.50 J/g°C) release when it cools by 20°C?','["500 J", "25 J", "1250 J", "50 J"]'::jsonb,0,'q = 50 × 0.50 × 20.','original'),
('112.43.c.13.D',4,'2090 J of heat raises the temperature of 50 g of water (c = 4.18 J/g°C). By how many degrees?','["5°C", "10°C", "41.8°C", "100°C"]'::jsonb,1,'ΔT = q ÷ (mc).','original'),
('112.43.c.13.D',3,'What does specific heat measure?','["the temperature of a substance", "the heat needed to melt 1 g", "the heat needed to raise 1 g of a substance by 1°C", "the total energy in a substance"]'::jsonb,2,'Different materials have different specific heats.','original'),
('112.43.c.14.A',3,'What is an alpha particle?','["a neutron", "a high-energy photon", "an electron", "a helium nucleus (2 protons and 2 neutrons)"]'::jsonb,3,'Alpha decay reduces the mass number by 4.','original'),
('112.43.c.14.A',3,'In beta decay, a neutron changes into what?','["a proton, with an electron emitted", "an alpha particle", "a helium nucleus", "a gamma ray only"]'::jsonb,0,'The atomic number increases by 1.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Science' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_chem_v1'
from (values
('112.43.c.14.A',4,'In the decay of uranium-238 by alpha emission, what is the product? (U-238 → ? + He-4)','["protactinium-238", "thorium-234", "thorium-242", "lead-206"]'::jsonb,1,'Mass 238 − 4 = 234 and atomic number 92 − 2 = 90.','original'),
('112.43.c.14.A',3,'Which type of radiation is stopped by a sheet of paper but is the least penetrating?','["gamma", "beta", "alpha", "x-ray"]'::jsonb,2,'Alpha particles are large and slow.','original'),
('112.43.c.14.A',3,'Gamma rays change the atomic number and the mass number of a nucleus how?','["they raise the atomic number by 2", "they lower the mass number by 4", "they double both", "they change neither"]'::jsonb,3,'Gamma rays are energy released from the nucleus.','original'),
('112.43.c.14.B',2,'What happens in nuclear fission?','["a heavy nucleus splits into smaller nuclei", "electrons are shared", "two light nuclei combine", "atoms are ionized"]'::jsonb,0,'For example, uranium-235 splitting.','original'),
('112.43.c.14.B',2,'What happens in nuclear fusion?','["a heavy nucleus splits", "light nuclei combine to form a heavier nucleus", "a neutron decays", "an electron is lost"]'::jsonb,1,'Hydrogen fuses to helium in the Sun.','original'),
('112.43.c.14.B',3,'Why does fusion require extremely high temperatures?','["to make neutrons heavier", "to melt the electrons", "to overcome the repulsion between positive nuclei", "to cool the nuclei"]'::jsonb,2,'Nuclei must get close enough to fuse.','original'),
('112.43.c.14.B',3,'Where does the energy released in nuclear reactions come from?','["electrons moving", "friction", "chemical bonds breaking", "a small amount of mass converted to energy"]'::jsonb,3,'E = mc².','original'),
('112.43.c.14.C',3,'A sample with a half-life of 5 days starts at 80 g. How much remains after 10 days?','["20 g", "0 g", "40 g", "10 g"]'::jsonb,0,'Two half-lives leave one quarter.','original'),
('112.43.c.14.C',3,'Which nuclear application is used to estimate the age of ancient organic materials?','["fusion in the Sun", "carbon-14 dating", "alpha decay of uranium only", "fission power plants"]'::jsonb,1,'C-14 decays at a known rate.','original'),
('112.43.c.14.C',3,'How is radiation used in cancer therapy?','["it makes cells grow", "it is applied only to healthy tissue", "it is aimed at tumors to damage and kill cancer cells", "it heals all cells"]'::jsonb,2,'Focused radiation damages the DNA of tumor cells.','original'),
('112.43.c.14.C',3,'Radioactive tracers are used in PET scans for what purpose?','["to measure bone length", "to repair DNA", "to heat tissue", "to create images of processes inside the body"]'::jsonb,3,'Detectors track the emitted radiation.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Science' and d.language = 'en'
on conflict (fingerprint) do nothing;

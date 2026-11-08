#!/usr/bin/env python3
"""High school Biology (TEKS 112.42.c). Original questions. Strands 1-4 (practices) skipped; content strands 5-13."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('112.42.c.', 985, own='hs_bio.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 5.A biomolecules
H('5.A', 2, "Which class of biomolecule stores and passes on genetic information?", "nucleic acids", ["carbohydrates", "lipids", "proteins"], "DNA and RNA are nucleic acids made of nucleotides.")
H('5.A', 2, "Enzymes belong to which class of biomolecules?", "proteins", ["lipids", "carbohydrates", "nucleic acids"], "Enzymes are proteins folded into specific shapes.")
H('5.A', 3, "Why do phospholipids form a double layer in a cell membrane?", "Their heads are attracted to water and their tails avoid water", ["Both ends of the molecule repel water", "They are made of amino acids that bond tightly", "They store genetic information in the layer"], "The hydrophilic heads face the watery surroundings and the hydrophobic tails face inward.")
H('5.A', 2, "What are the building blocks (monomers) of proteins?", "amino acids", ["nucleotides", "simple sugars", "fatty acids"], "Amino acids join in chains to make proteins.")
H('5.A', 2, "Starch and cellulose are examples of which biomolecule class?", "carbohydrates", ["lipids", "proteins", "nucleic acids"], "They are long chains of sugar units.")
H('5.A', 3, "Which biomolecules are the best long-term energy storage in animals?", "lipids", ["nucleic acids", "enzymes", "amino acids"], "Fats store more energy per gram than carbohydrates.")

# 5.B prokaryotes vs eukaryotes
H('5.B', 2, "Which structure do bacterial cells lack?", "a membrane-bound nucleus", ["ribosomes", "a cell membrane", "DNA"], "Prokaryotes keep their DNA in a nucleoid region without a membrane.")
H('5.B', 2, "Which of these organisms is made of eukaryotic cells?", "a mushroom", ["a bacterium that lives in soil", "a cyanobacterium", "an archaeon from a hot spring"], "Fungi are eukaryotes, while bacteria and archaea are prokaryotes.")
H('5.B', 3, "Which structure do both prokaryotic and eukaryotic cells have?", "ribosomes", ["mitochondria", "a nuclear envelope", "an endoplasmic reticulum"], "All cells make proteins at ribosomes.")
H('5.B', 4, "According to the endosymbiotic theory, mitochondria originated from what?", "small prokaryotes engulfed by a larger cell", ["a part of the nucleus that pinched off", "viruses that infected early cells", "the Golgi apparatus"], "Evidence includes their own circular DNA and double membranes.")
H('5.B', 3, "How is the DNA of a typical bacterium organized?", "as a single circular chromosome in the cytoplasm", ["as many linear chromosomes inside a nucleus", "as RNA inside a protein coat", "as DNA packed in the mitochondria"], "Prokaryotic DNA is circular and lies in the nucleoid.")

# 5.C cellular transport and homeostasis
H('5.C', 2, "What is the diffusion of water across a selectively permeable membrane called?", "osmosis", ["active transport", "endocytosis", "photosynthesis"], "Water moves toward the side with more dissolved solute.")
H('5.C', 2, "In simple diffusion, molecules move in which direction?", "from high concentration to low concentration", ["from low concentration to high concentration", "only into the nucleus", "only out of the cell"], "Diffusion follows the concentration gradient and needs no energy.")
H('5.C', 3, "What does active transport require that passive transport does not?", "cellular energy (ATP)", ["a concentration gradient", "an open channel only", "a lower temperature"], "It moves substances against their gradient.")
H('5.C', 3, "A red blood cell is placed in distilled water. What most likely happens?", "It swells and may burst", ["It shrinks", "It stays exactly the same", "It divides"], "Water rushes into the cell because the outside has fewer solutes.")
H('5.C', 3, "How does facilitated diffusion move a molecule across a membrane?", "through a carrier or channel protein without using energy", ["by pumping it against its gradient with ATP", "by engulfing it in a vesicle", "by dissolving the membrane"], "The molecule still moves down its gradient.")

# 5.D viruses
H('5.D', 2, "Why are viruses not considered cells?", "They lack organelles and cannot reproduce without a host", ["They are too large to be seen", "They have a nucleus but no membrane", "They make their own food"], "Viruses are genetic material in a protein coat.")
H('5.D', 2, "What is the protein coat of a virus called?", "capsid", ["cell wall", "nucleus", "flagellum"], "The capsid protects the viral genetic material.")
H('5.D', 3, "Why don't antibiotics treat influenza?", "Antibiotics target bacteria, and viruses are not bacteria", ["Antibiotics only work on fungi", "Influenza is a parasite", "Antibiotics make viruses stronger"], "Viruses lack the structures that antibiotics attack.")
H('5.D', 3, "A virus enters a host cell and uses it to make more viruses. This is the virus's way of doing what?", "replicating", ["photosynthesizing", "digesting food", "respiring"], "Viruses hijack the host's machinery to reproduce.")

# 6.A cell cycle
H('6.A', 2, "During which part of the cell cycle is DNA copied?", "S phase of interphase", ["metaphase", "cytokinesis", "telophase"], "The S (synthesis) phase replicates the chromosomes.")
H('6.A', 3, "Mitosis produces how many cells, and how do they compare to the parent cell?", "two cells genetically identical to the parent", ["four cells with half the chromosomes", "two cells genetically different from each other", "one large cell with two nuclei"], "Mitosis makes identical diploid daughter cells.")
H('6.A', 3, "What is the correct order of the stages of mitosis?", "prophase, metaphase, anaphase, telophase", ["metaphase, prophase, telophase, anaphase", "anaphase, prophase, metaphase, telophase", "telophase, anaphase, metaphase, prophase"], "PMAT.")
H('6.A', 3, "In which stage of mitosis do the chromosomes line up along the center of the cell?", "metaphase", ["prophase", "anaphase", "telophase"], "The spindle fibers align them at the equator.")
H('6.A', 3, "Which part of the cell cycle takes up most of the time for a typical dividing cell?", "interphase", ["prophase", "anaphase", "cytokinesis"], "Cells grow and copy DNA during interphase.")

# 6.B differentiation
H('6.B', 3, "What is cell differentiation?", "the process by which cells become specialized in structure and function", ["the process by which a cell copies its DNA", "the breakdown of a cell by enzymes", "the movement of water across membranes"], "Different genes are switched on in different cell types.")
H('6.B', 3, "A muscle cell and a nerve cell in the same person differ mainly because of what?", "which genes are expressed in each", ["different amounts of DNA", "different species of DNA", "the number of chromosomes they have"], "Both contain the same DNA but use different parts of it.")
H('6.B', 2, "What is special about stem cells?", "They are unspecialized and can differentiate into other cell types", ["They can never divide", "They are always cancerous", "They contain no DNA"], "Stem cells can develop into specialized cells.")
H('6.B', 4, "Which is an example of an environmental factor that can influence cell differentiation?", "chemical signals from neighboring cells", ["the color of the organism's eyes", "the number of ribosomes in the cell", "the age of the parent's cells"], "Signals around a developing cell help turn genes on or off.")

# 6.C cell cycle disruption
H('6.C', 3, "Cancer is best described as what?", "uncontrolled cell division caused by a failure in cell cycle control", ["a virus that infects cells", "the death of too many cells", "the failure of cells to take in nutrients"], "Damaged control genes allow cells to keep dividing.")
H('6.C', 3, "What is the role of tumor suppressor genes?", "They slow cell division and repair DNA errors", ["They speed up cell division", "They create new mutations", "They make cells unable to die"], "When they are damaged, the cell loses a brake on division.")
H('6.C', 3, "Which is an example of a carcinogen?", "tobacco smoke", ["drinking water", "regular sleep", "vitamin C"], "Carcinogens cause DNA mutations that can lead to cancer.")
H('6.C', 3, "What makes a tumor malignant?", "its cells can invade other tissues and spread", ["it is made of fat cells", "it never grows", "it stays in one place"], "Spreading to other body parts is called metastasis.")

# 7.A DNA structure
H('7.A', 2, "What three parts make up a DNA nucleotide?", "a sugar, a phosphate group and a nitrogen base", ["an amino acid, a sugar and a lipid", "a phosphate, a protein and a fatty acid", "a sugar, an enzyme and water"], "Nucleotides are the units of DNA.")
H('7.A', 2, "In DNA, adenine pairs with which base?", "thymine", ["cytosine", "guanine", "uracil"], "A pairs with T and C pairs with G.")
H('7.A', 3, "What part of DNA contains the code that determines traits?", "the order of its nitrogen bases", ["the sugar-phosphate backbone", "the number of hydrogen atoms", "its color"], "The base sequence is read in groups of three to specify amino acids.")
H('7.A', 3, "One strand of DNA reads AATGC. What is the complementary strand?", "TTACG", ["AATGC", "UUACG", "CCGTA"], "A↔T and C↔G.")
H('7.A', 2, "What is the shape of a DNA molecule?", "a double helix", ["a single straight chain", "a flat sheet", "a hollow sphere"], "Two strands twist around each other.")

# 7.B protein synthesis
H('7.B', 3, "Where does transcription occur in a eukaryotic cell?", "in the nucleus", ["at the ribosome", "in the cell membrane", "in the lysosome"], "DNA is copied into mRNA inside the nucleus.")
H('7.B', 3, "Where does translation occur?", "at a ribosome", ["in the nucleolus", "in the Golgi apparatus", "inside the nucleus"], "Ribosomes read mRNA to build a protein.")
H('7.B', 2, "Which base does RNA use instead of thymine?", "uracil", ["adenine", "cytosine", "guanine"], "RNA contains A, U, C and G.")
H('7.B', 3, "What is a codon?", "a group of three mRNA bases that codes for one amino acid", ["a single DNA base", "a type of protein", "a sugar in RNA"], "The ribosome reads mRNA one codon at a time.")
H('7.B', 3, "What does a tRNA molecule do?", "it brings the matching amino acid to the ribosome", ["it copies DNA", "it stores the genetic code in the nucleus", "it cuts proteins into pieces"], "Its anticodon pairs with an mRNA codon.")
H('7.B', 4, "A DNA template strand reads TAC GGT. What is the mRNA made from it?", "AUG CCA", ["ATG CCA", "UAC GGU", "TAC GGT"], "T→A, A→U, C→G and G→C.")

# 7.C DNA changes
H('7.C', 2, "What is a point mutation?", "a change in a single nucleotide of DNA", ["the loss of an entire chromosome", "a copy of the whole genome", "a change in the cell membrane"], "One base is replaced, added or removed.")
H('7.C', 3, "Why is a frameshift mutation usually more harmful than a substitution?", "It shifts the reading frame and changes every codon after it", ["It only affects the first codon", "It never changes the protein", "It repairs the DNA"], "An insertion or deletion alters all the following codons.")
H('7.C', 3, "A mutation that does not change the amino acid sequence is called what?", "a silent mutation", ["a frameshift mutation", "a nonsense mutation", "a chromosomal deletion"], "Several codons can code for the same amino acid.")
H('7.C', 3, "A mutation in a body (somatic) cell, such as a skin cell, is passed on to offspring how?", "It is not passed on", ["It is always passed on", "It is passed on only to sons", "It is passed on to every cell in the offspring"], "Only mutations in gametes can be inherited.")

# 7.D molecular technologies
H('7.D', 2, "What does PCR do?", "makes many copies of a DNA segment", ["separates proteins by charge", "cuts DNA at random", "turns RNA into protein"], "Polymerase chain reaction amplifies DNA.")
H('7.D', 2, "What does gel electrophoresis separate?", "DNA fragments by size", ["cells by color", "proteins from lipids by temperature", "chromosomes by number"], "An electric current pulls DNA through a gel.")
H('7.D', 3, "In gel electrophoresis, which DNA fragments travel farthest?", "the smallest fragments", ["the largest fragments", "the red fragments", "the fragments with the most guanine only"], "Small pieces move more easily through the gel.")
H('7.D', 3, "Putting the human insulin gene into bacteria so they make insulin is an example of what?", "genetic engineering", ["natural selection", "meiosis", "mutation by sunlight"], "DNA from one species is inserted into another.")
H('7.D', 3, "What do restriction enzymes do?", "cut DNA at specific base sequences", ["join amino acids together", "copy RNA into DNA only", "make ATP"], "They are used to cut DNA for cloning.")

# 8.A meiosis
H('8.A', 3, "What does meiosis produce from one diploid cell?", "four genetically different haploid cells", ["two identical diploid cells", "one haploid cell", "four identical diploid cells"], "Meiosis halves the chromosome number and makes gametes.")
H('8.A', 3, "During which stage of meiosis does crossing-over occur?", "prophase I", ["metaphase II", "anaphase II", "telophase II"], "Homologous chromosomes swap segments while paired.")
H('8.A', 3, "What is independent assortment?", "the random way homologous pairs line up and separate", ["the copying of DNA", "the pairing of A with T", "the loss of a chromosome"], "It creates many different combinations of chromosomes in gametes.")
H('8.A', 4, "A human body cell has 46 chromosomes. How many chromosomes does a human sperm cell have?", "23", ["46", "92", "12"], "Meiosis reduces the number by half.")
H('8.A', 4, "Failure of chromosomes to separate properly during meiosis is called what?", "nondisjunction", ["crossing-over", "transcription", "mitosis"], "It can lead to conditions such as Down syndrome.")

# 8.B genetic crosses
H('8.B', 3, "In a cross of two heterozygous parents (Tt × Tt), what fraction of offspring are expected to be tt?", "1/4", ["1/2", "3/4", "0"], "The Punnett square gives TT, Tt, Tt, tt.")
H('8.B', 3, "A heterozygous parent (Tt) is crossed with a homozygous recessive parent (tt). What fraction of offspring are expected to be tt?", "1/2", ["1/4", "all", "none"], "Half of the offspring get t from the heterozygote.")
H('8.B', 4, "A cross of two parents that are both RrYy (two traits) gives which phenotype ratio when each trait shows complete dominance?", "9:3:3:1", ["3:1", "1:2:1", "1:1:1:1"], "This is the classic dihybrid ratio.")
H('8.B', 3, "A red snapdragon is crossed with a white snapdragon and all offspring are pink. This is an example of what?", "incomplete dominance", ["codominance", "sex linkage", "complete dominance"], "The heterozygote shows a blend.")
H('8.B', 3, "A person with type AB blood shows both A and B traits. This is an example of what?", "codominance", ["incomplete dominance", "recessive inheritance", "a mutation"], "Both alleles are fully expressed.")
H('8.B', 4, "Why are X-linked recessive disorders more common in males?", "Males have only one X chromosome, so one recessive allele is expressed", ["Males have two X chromosomes", "The Y chromosome carries the allele", "Males cannot be carriers"], "A single recessive allele on the X shows up in XY individuals.")

# 9.A common ancestry
H('9.A', 3, "The arm of a human and the wing of a bat have similar bone structures. What are these called?", "homologous structures", ["analogous structures", "vestigial structures", "adaptive traits"], "They suggest a common ancestor.")
H('9.A', 3, "What do the fossils in layers of rock show about life on Earth?", "how organisms have changed over time", ["that species never change", "that all organisms appeared at once", "that the Earth is flat"], "The fossil record records past life in order.")
H('9.A', 3, "Pelvic bones in a whale are very small and have no clear use. What type of structure are they?", "vestigial", ["homologous in function", "newly evolved", "analogous"], "They are remnants from ancestors that walked on land.")
H('9.A', 4, "Two species share a very high percentage of DNA. What does that suggest?", "they share a recent common ancestor", ["they live in the same habitat", "they have the same diet", "they look alike by chance"], "More similar DNA suggests closer relation.")
H('9.A', 4, "Marsupials are found mostly in Australia and nearby islands. How does biogeography explain this?", "Related groups spread and diversified after the continents separated", ["Marsupials were created there", "Marsupials cannot survive elsewhere", "Australia has no predators for them"], "Geographic isolation led to unique lineages.")

# 9.B rates of change
H('9.B', 2, "Which idea says that species change slowly and steadily over long periods?", "gradualism", ["stasis", "punctuated equilibrium", "extinction"], "Small changes accumulate over time.")
H('9.B', 3, "Which idea says that long periods of little change are interrupted by short bursts of rapid change?", "punctuated equilibrium", ["gradualism", "inheritance of acquired traits", "genetic drift"], "The fossil record often shows such bursts.")
H('9.B', 3, "What is stasis in the fossil record?", "a long period with little or no change in a species", ["a sudden extinction", "the formation of a fossil", "rapid change in many species"], "The species stays nearly the same.")

# 10.A natural selection
H('10.A', 3, "Which can evolve over generations?", "a population", ["a single organism", "a single cell during its life", "a single gene during an individual's life"], "Allele frequencies change in populations.")
H('10.A', 3, "Soot darkens tree bark, and dark peppered moths become more common than light ones. What explains this?", "Dark moths were better hidden and survived more often", ["Light moths turned dark", "Dark moths were created by the soot", "Light moths migrated away on their own"], "Natural selection favors traits that help survival.")
H('10.A', 3, "What does fitness mean in biology?", "how well an organism survives and reproduces", ["how strong an organism is", "how fast an organism is", "how large an organism is"], "Fitness is reproductive success.")
H('10.A', 4, "Why can't an individual organism evolve through natural selection?", "its genes stay the same during its life, so selection changes the population", ["individuals never change at all", "evolution only happens to cells", "natural selection acts on DNA only"], "Allele frequencies change across generations.")

# 10.B elements of natural selection
H('10.B', 3, "Which is NOT required for natural selection?", "traits acquired during an organism's life being passed on", ["variation among individuals", "more offspring than can survive", "traits that are inherited"], "Only inherited variation is acted on.")
H('10.B', 3, "Why do some bacteria become resistant to antibiotics over time?", "Resistant bacteria survive treatment and reproduce more", ["Bacteria choose to become resistant", "Antibiotics change the bacteria's DNA on purpose", "All bacteria are always resistant"], "Selection favors the resistant variants.")
H('10.B', 3, "What does it mean that populations have the potential to overproduce?", "they make more offspring than the environment can support", ["they produce exactly the number that survive", "they never reproduce", "all the offspring survive"], "That leads to competition.")
H('10.B', 3, "What is an adaptation?", "an inherited trait that improves survival and reproduction in an environment", ["a trait an organism learns", "a mutation that always helps", "a change in the habitat"], "Adaptations arise through natural selection.")

# 10.C speciation
H('10.C', 3, "Which event can lead to the formation of a new species?", "geographic isolation of populations", ["unchanging environments for all populations", "constant interbreeding among them", "learning new behaviors only"], "Isolated populations diverge.")
H('10.C', 3, "By the biological species concept, a species is a group that can do what?", "interbreed and produce fertile offspring", ["look exactly alike", "live in the same place", "eat the same food"], "Reproductive isolation defines separate species.")
H('10.C', 4, "A river splits a squirrel population, and over time the two groups can no longer mate. What is this an example of?", "speciation", ["extinction", "gene flow", "a single mutation"], "Isolation and different selection lead to new species.")
H('10.C', 4, "What is adaptive radiation?", "rapid diversification of one ancestral species into many forms for different niches", ["the movement of animals between populations", "the extinction of many species", "the loss of variation"], "Darwin's finches are an example.")

# 10.D other mechanisms
H('10.D', 3, "What is genetic drift?", "random changes in allele frequencies, especially in small populations", ["changes caused by the environment selecting traits", "movement of genes between populations", "changes due to learning"], "Chance events change allele frequencies.")
H('10.D', 3, "What is gene flow?", "the movement of alleles between populations through migration", ["random change in allele frequencies", "the death of a population", "the copying of DNA"], "Migrants carry alleles into new populations.")
H('10.D', 4, "A disease kills most of a population, leaving a few survivors with a limited set of alleles. What is this called?", "a bottleneck effect", ["gene flow", "natural selection only", "mutation"], "Genetic variation drops after a sharp population decline.")
H('10.D', 3, "What is the ultimate source of new alleles in a population?", "mutation", ["gene flow only", "natural selection", "genetic drift"], "Mutations create new versions of genes.")
H('10.D', 4, "A few individuals colonize a new island, and their small gene pool differs from the original. What is this called?", "the founder effect", ["a bottleneck effect", "gene flow", "adaptive radiation"], "A small starting group may not represent the whole population.")

# 11.A photosynthesis and respiration
H('11.A', 2, "What are the reactants of photosynthesis?", "carbon dioxide and water", ["glucose and oxygen", "oxygen and water", "ATP and glucose"], "Light energy is also needed.")
H('11.A', 2, "What are the products of photosynthesis?", "glucose and oxygen", ["carbon dioxide and water", "ATP and carbon dioxide", "lipids and water"], "Plants make sugar and release O₂.")
H('11.A', 2, "Where does most cellular respiration take place in a eukaryotic cell?", "mitochondria", ["chloroplasts", "ribosomes", "the cell wall"], "Mitochondria produce most of a cell's ATP.")
H('11.A', 3, "What are the products of aerobic cellular respiration?", "carbon dioxide, water and ATP", ["glucose and oxygen", "lactic acid and alcohol", "oxygen and protein"], "Glucose is broken down with oxygen.")
H('11.A', 3, "A student says that matter is lost during cellular respiration. What is the correct idea?", "atoms are rearranged into new molecules, so matter is conserved", ["atoms are destroyed", "atoms turn into energy", "atoms disappear as heat only"], "Conservation of matter holds in all chemical reactions.")
H('11.A', 3, "Which pigment in chloroplasts captures light for photosynthesis?", "chlorophyll", ["hemoglobin", "melanin", "keratin"], "Chlorophyll absorbs mostly red and blue light.")

# 11.B enzymes
H('11.B', 3, "How do enzymes speed up reactions?", "by lowering the activation energy", ["by adding heat to the reaction", "by being used up in the reaction", "by changing the products"], "Enzymes are catalysts and are not consumed.")
H('11.B', 3, "Where does the substrate bind on an enzyme?", "the active site", ["the cell wall", "the nucleus", "the membrane lipid"], "Its shape fits the substrate.")
H('11.B', 3, "Why does an enzyme stop working at very high temperature?", "its shape changes (denatures), so the active site no longer fits", ["it gets bigger and stronger", "it turns into a lipid", "it floats away from the cell"], "Denaturation destroys the active site shape.")
H('11.B', 3, "Pepsin works best in the acidic stomach. What does this show?", "enzymes have an optimum pH", ["enzymes work at any pH", "enzymes are alive", "enzymes are made of sugar"], "Different enzymes work best at different pH values.")

# 12.A animal body systems
H('12.A', 3, "Which two systems mainly regulate the body's activities through signals?", "nervous and endocrine", ["skeletal and muscular", "digestive and excretory", "integumentary and respiratory"], "Neurons use electrical signals and glands use hormones.")
H('12.A', 3, "After nutrients are absorbed in the small intestine, which system carries them to body cells?", "circulatory", ["skeletal", "respiratory", "integumentary"], "Blood transports absorbed nutrients.")
H('12.A', 3, "What is the role of villi in the small intestine?", "increase surface area for absorption", ["make bile", "grind food", "store waste"], "Folds and projections increase absorption.")
H('12.A', 4, "Blood sugar rises after a meal, and the pancreas releases insulin, which lowers it. This is an example of what?", "negative feedback", ["positive feedback", "mutation", "diffusion only"], "The response reverses the change.")
H('12.A', 3, "Which two systems work together to deliver oxygen to body cells?", "respiratory and circulatory", ["nervous and skeletal", "digestive and muscular", "endocrine and integumentary"], "Lungs bring in oxygen and blood carries it.")

# 12.B plant systems
H('12.B', 3, "Which plant tissue carries water and minerals upward from the roots?", "xylem", ["phloem", "epidermis", "pith only"], "Xylem moves water upward.")
H('12.B', 3, "Which plant tissue carries sugars made in the leaves to other parts?", "phloem", ["xylem", "root hairs", "bark only"], "Phloem transports sugar in sap.")
H('12.B', 3, "What do stomata do?", "allow gas exchange and water vapor loss", ["absorb water from soil", "make seeds", "hold the plant upright"], "Guard cells open and close them.")
H('12.B', 3, "Phototropism is a plant's growth response to what?", "light", ["gravity", "touch", "water"], "Stems bend toward light.")
H('12.B', 4, "Which plant hormone helps cause stems to bend toward light?", "auxin", ["insulin", "adrenaline", "thyroxine"], "Auxin builds up on the shaded side and lengthens those cells.")

# 13.A ecological relationships
H('13.A', 2, "Bees collect nectar from flowers while pollinating them. This is an example of what?", "mutualism", ["parasitism", "predation", "competition"], "Both species benefit.")
H('13.A', 2, "A tapeworm lives in the intestines of a dog and takes nutrients, harming it. This is an example of what?", "parasitism", ["mutualism", "commensalism", "competition"], "The parasite benefits and the host is harmed.")
H('13.A', 3, "Birds build nests in a tree, which benefits the birds but does not affect the tree. This is an example of what?", "commensalism", ["mutualism", "parasitism", "predation"], "One species benefits and the other is unaffected.")
H('13.A', 2, "Two species of plants compete for the same limited sunlight. This is an example of what?", "competition", ["mutualism", "commensalism", "predation"], "They use the same limited resource.")
H('13.A', 3, "A lynx hunts snowshoe hares. This relationship is an example of what?", "predation", ["mutualism", "parasitism", "commensalism"], "The predator kills and eats the prey.")

# 13.B energy flow and trophic levels
H('13.B', 3, "About how much energy is passed from one trophic level to the next?", "about 10 percent", ["about 90 percent", "100 percent", "about 50 percent"], "Most energy is lost as heat.")
H('13.B', 3, "Which organisms form the base of most food chains?", "producers", ["decomposers", "carnivores", "herbivores"], "Producers capture energy from sunlight.")
H('13.B', 4, "If the top predator in a food web is removed, what might happen to the herbivore population?", "it may grow and overgraze the producers", ["it will definitely go extinct", "it will stay exactly the same", "it will turn into producers"], "Predators limit prey populations.")
H('13.B', 3, "Which statement about energy and matter in an ecosystem is true?", "energy flows in one direction while matter is recycled", ["matter flows one way while energy is recycled", "both are completely recycled", "neither moves through the ecosystem"], "Energy enters as sunlight and leaves as heat.")
H('13.B', 3, "What role do decomposers play in an ecosystem?", "break down dead matter and return nutrients to the soil", ["make food from sunlight", "eat living plants", "hunt other animals"], "They recycle nutrients.")

# 13.C carbon and nitrogen cycles
H('13.C', 3, "What do nitrogen-fixing bacteria do?", "convert nitrogen gas into forms plants can use", ["make carbon dioxide", "remove oxygen", "turn plants into soil"], "They make ammonia from atmospheric N₂.")
H('13.C', 3, "Burning fossil fuels affects the carbon cycle in what way?", "it releases carbon dioxide into the atmosphere", ["it removes carbon from the air", "it creates nitrogen", "it makes oxygen only"], "Stored carbon is released as CO₂.")
H('13.C', 3, "What process removes carbon dioxide from the atmosphere into living things?", "photosynthesis", ["combustion", "decomposition", "evaporation"], "Plants convert CO₂ into sugars.")
H('13.C', 4, "Fertilizer runoff reaches a lake and causes a large algae bloom. What problem may follow?", "oxygen levels drop and aquatic life dies", ["more oxygen for fish", "less algae the next year", "colder water"], "Decomposing algae use up oxygen.")
H('13.C', 4, "Clearing large forests affects the carbon cycle how?", "less carbon dioxide is absorbed by plants", ["more carbon dioxide is absorbed", "carbon dioxide is destroyed", "oxygen increases"], "Fewer plants mean less photosynthesis.")

# 13.D biodiversity
H('13.D', 3, "What is the leading cause of biodiversity loss?", "habitat destruction", ["too much rain", "too many predators", "too much sunlight"], "Species lose the places where they live.")
H('13.D', 3, "How can an invasive species harm an ecosystem?", "it can outcompete native species for resources", ["it always helps native species", "it never competes", "it adds biodiversity every time"], "Invasive species often have no natural predators.")
H('13.D', 3, "Why are ecosystems with high biodiversity often more stable?", "if one species declines, others can fill its role", ["they have fewer species", "they have only producers", "they never change"], "Many species provide redundancy.")
H('13.D', 4, "What is a keystone species?", "a species with a large effect on its ecosystem relative to its numbers", ["the most abundant species", "the largest species", "the smallest species"], "Removing it can change the whole community.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_bio.jsonl'))

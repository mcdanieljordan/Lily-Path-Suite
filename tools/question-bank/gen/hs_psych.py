#!/usr/bin/env python3
"""High school Psychology (TEKS 113.45.c). Original questions."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('113.45.c.', 1000, own='hs_psych.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 1 field
H('1.A', 3, "What most clearly separates psychology from sociology?", "psychology focuses on individual behavior and mental processes", ["psychology studies only groups and institutions", "psychology studies only rocks", "psychology studies only governments"], "Sociology examines groups and society.")
H('1.B', 3, "Wilhelm Wundt is credited with doing what in 1879?", "opening the first psychology laboratory", ["writing the Bible", "inventing the telephone", "founding Harvard"], "He is considered the father of experimental psychology.")
H('1.B', 3, "Which perspective focuses on observable behavior and learning from the environment?", "behaviorism", ["psychoanalysis", "humanism", "structuralism"], "Watson and Skinner shaped it.")
H('1.B', 3, "Sigmund Freud emphasized which influence on behavior?", "unconscious drives and early experiences", ["only observable behavior", "only brain scans", "only genetics"], "He founded psychoanalysis.")
H('1.B', 3, "Humanistic psychologists such as Carl Rogers stressed what?", "free will and personal growth", ["unconscious conflict only", "conditioning only", "brain structure only"], "They emphasize self-actualization.")
H('1.C', 3, "A psychologist who helps people with mental health problems through therapy is called what?", "a clinical psychologist", ["an industrial engineer", "a geologist", "a statistician only"], "Clinical psychology treats disorders.")
H('1.C', 3, "A school psychologist most often does what?", "supports students' learning and emotional needs", ["designs bridges", "tests soil", "trains pilots"], "School psychologists assess and counsel.")

# 2 methods
H('2.A', 3, "A hypothesis is best described as what?", "a testable prediction", ["a proven fact", "an opinion with no test", "a final conclusion"], "A theory explains many findings; a hypothesis is tested.")
H('2.A', 3, "A scientific theory differs from a hunch because a theory does what?", "organizes and explains many tested observations", ["is a guess", "can never change", "needs no evidence"], "Theories are supported by evidence.")
H('2.B', 3, "In an experiment, the variable the researcher manipulates is called what?", "the independent variable", ["the dependent variable", "the control group", "the sample"], "It is the presumed cause.")
H('2.B', 3, "In an experiment, the variable that is measured for change is called what?", "the dependent variable", ["the independent variable", "the placebo", "the hypothesis"], "It is the outcome.")
H('2.B', 3, "A correlation between two variables shows what?", "that they are related, not that one causes the other", ["that one causes the other", "that there is no relation", "that the study was biased"], "Correlation is not causation.")
H('2.B', 3, "Random assignment helps researchers do what?", "make groups equivalent at the start of an experiment", ["choose only volunteers", "avoid collecting data", "prove the hypothesis"], "It reduces pre-existing differences.")
H('2.B', 3, "A control group in an experiment does what?", "does not receive the treatment, for comparison", ["receives the largest dose", "chooses its own treatment", "is the researchers"], "It provides a baseline.")
H('2.C', 3, "Under APA ethical standards, researchers must obtain what from participants?", "informed consent", ["payment only", "their grades", "their addresses"], "Participants must know the risks and agree.")
H('2.C', 3, "Debriefing after a study is used to do what?", "explain the true purpose and address any concerns", ["hide the results", "punish participants", "collect payment"], "It is an ethical requirement.")
H('2.D', 3, "The mean of 2, 4, 4, 6 and 9 is what?", "5", ["4", "6", "9"], "Sum 25 divided by 5 equals 5.")
H('2.D', 3, "The median of 3, 5, 7, 9 and 11 is what?", "7", ["5", "9", "35"], "It is the middle value.")
H('2.D', 3, "The mode of 2, 3, 3, 4, 5, 3 and 6 is what?", "3", ["4", "5", "2"], "It is the most frequent value.")
H('2.D', 4, "The standard deviation measures what?", "how spread out the scores are around the mean", ["the middle score", "the most common score", "the total of all scores"], "It is a measure of dispersion.")

# 3 biology
H('3.A', 3, "The central nervous system consists of what?", "the brain and spinal cord", ["the nerves in the limbs", "the heart and lungs", "the glands"], "The peripheral system connects to the body.")
H('3.A', 3, "A neuron's branching fibers that receive signals are called what?", "dendrites", ["axons", "myelin sheaths", "synapses"], "Axons send signals away.")
H('3.A', 3, "The part of the brain that controls balance and coordination is the what?", "cerebellum", ["hippocampus", "amygdala", "frontal lobe"], "It fine-tunes movement.")
H('3.A', 3, "The endocrine system uses which chemical messengers?", "hormones", ["neurotransmitters only", "enzymes", "antibodies"], "Glands release hormones into the blood.")
H('3.B', 3, "The fight-or-flight response is controlled by which system?", "the sympathetic nervous system", ["the parasympathetic nervous system", "the immune system", "the digestive system"], "It prepares the body for action.")
H('3.B', 3, "Adrenaline released by the adrenal glands does what?", "increases heart rate and alertness", ["lowers heart rate", "causes sleep", "slows breathing"], "It is a stress hormone.")

# 4 sensation and perception
H('4.A', 3, "A sensory receptor stops responding to a constant stimulus through what process?", "sensory adaptation", ["selective attention", "habituation to noise only", "perceptual set"], "You stop noticing a smell after a while.")
H('4.A', 3, "The smallest amount of stimulus a person can detect half the time is the what?", "absolute threshold", ["difference threshold", "perceptual constancy", "sensory memory"], "It marks the detection limit.")
H('4.B', 3, "Perceptual set is the tendency to do what?", "perceive things based on expectations and experience", ["ignore all stimuli", "see only colors", "hear only low sounds"], "Context and expectation shape perception.")
H('4.B', 3, "Depth perception is aided by which cue?", "retinal disparity (the slight difference between eyes' images)", ["the taste of food", "the weight of objects", "the temperature of air"], "Binocular cues help judge distance.")

# 5 development
H('5.A', 3, "The nature versus nurture debate asks about what?", "the relative influence of heredity and environment", ["whether brains exist", "whether memory is real", "whether stress is common"], "Most psychologists believe both matter.")
H('5.A', 3, "Studies of identical twins reared apart help psychologists examine what?", "genetic influences on traits", ["only environmental influence", "which twin is older", "birth weight only"], "Shared genes with different environments.")
H('5.B', 3, "Maturation refers to what?", "biological growth processes that follow a genetic timetable", ["learning by reward", "social pressure", "emotional stress"], "Walking is partly maturational.")
H('5.C', 3, "In Harry Harlow's monkey studies, infant monkeys preferred what?", "a soft cloth 'mother' over a wire one that gave food", ["the wire mother with food", "no mother", "other monkeys only"], "Contact comfort mattered more than feeding.")
H('5.C', 3, "Attachment is best described as what?", "an emotional bond between infant and caregiver", ["a type of memory", "a form of punishment", "a language skill"], "Bowlby and Ainsworth studied it.")
H('5.D', 3, "Piaget's first stage of cognitive development is the what?", "sensorimotor stage", ["formal operational stage", "concrete operational stage", "preoperational stage"], "Babies learn through senses and actions.")
H('5.D', 3, "Object permanence, understanding that objects exist when out of sight, develops in which stage?", "sensorimotor", ["formal operational", "concrete operational", "preoperational"], "Peekaboo plays with it.")
H('5.D', 3, "In Piaget's concrete operational stage, children can do what?", "think logically about concrete events and understand conservation", ["think abstractly about hypotheticals", "only use senses", "only use symbols without logic"], "Ages about 7 to 11.")
H('5.D', 3, "Abstract and hypothetical reasoning appears in which of Piaget's stages?", "formal operational", ["sensorimotor", "preoperational", "concrete operational"], "It typically emerges in adolescence.")
H('5.E', 3, "According to Erikson, the main crisis of adolescence is what?", "identity versus role confusion", ["trust versus mistrust", "integrity versus despair", "industry versus inferiority"], "Teens explore who they are.")
H('5.E', 3, "Erikson's first stage, in infancy, concerns what?", "trust versus mistrust", ["autonomy versus shame", "initiative versus guilt", "intimacy versus isolation"], "Caregivers help babies build trust.")
H('5.F', 4, "Using Erikson's theory, which outcome is most likely for a child whose efforts are consistently praised in school?", "a sense of industry and competence", ["role confusion", "despair", "mistrust"], "The industry-versus-inferiority stage occurs in school years.")
H('5.G', 4, "A common criticism of Piaget's theory is that it does what?", "underestimates children's abilities at young ages", ["overestimates their abilities", "ignores development", "ignores stages"], "Later research showed earlier competence.")
H('5.G', 4, "A strength of stage theories of development is that they do what?", "provide a framework to describe typical changes", ["prove every child develops the same", "ignore culture", "avoid evidence"], "But they may oversimplify individual differences.")

# 6 learning
H('6.A', 3, "In classical conditioning, a stimulus that triggers a response without learning is called what?", "an unconditioned stimulus", ["a conditioned stimulus", "a neutral stimulus", "a reinforcer"], "Food triggers salivation naturally.")
H('6.A', 3, "In Pavlov's experiment, the bell became a what after being paired with food?", "conditioned stimulus", ["unconditioned stimulus", "unconditioned response", "punishment"], "It then produced salivation by itself.")
H('6.A', 3, "In operant conditioning, behavior is strengthened by what?", "reinforcement", ["extinction only", "habituation", "punishment only"], "Skinner studied it.")
H('6.A', 3, "Taking away an unpleasant stimulus to increase a behavior is called what?", "negative reinforcement", ["positive punishment", "positive reinforcement", "extinction"], "Buckling a seat belt to stop the buzzer is an example.")
H('6.A', 3, "Which schedule of reinforcement produces the highest and steadiest response rate?", "variable ratio", ["fixed interval", "continuous", "fixed ratio"], "Slot machines use it.")
H('6.B', 3, "A teacher who gives stickers for completed homework is using what?", "positive reinforcement", ["negative reinforcement", "extinction", "classical conditioning"], "A pleasant stimulus is added to strengthen behavior.")
H('6.B', 3, "Learning by watching and imitating others is called what?", "observational learning", ["classical conditioning", "habituation", "extinction"], "Bandura's Bobo doll studies illustrate it.")

# 7 motivation and emotion
H('7.A', 3, "Maslow's hierarchy of needs places which needs at the base?", "physiological needs such as food and water", ["self-actualization", "esteem", "belonging"], "Basic needs come before higher ones.")
H('7.A', 3, "The James-Lange theory proposes that emotion results from what?", "bodily arousal", ["thoughts alone", "memories alone", "culture alone"], "We feel afraid because we tremble.")
H('7.A', 3, "The Schachter-Singer two-factor theory says emotion depends on arousal plus what?", "a cognitive label", ["a memory", "a hormone", "a reflex"], "Interpretation shapes the feeling.")
H('7.B', 3, "Display rules, which guide how emotions are shown, are shaped mostly by what?", "culture", ["genetics only", "hormones only", "weather"], "Cultures differ in what is acceptable to express.")
H('7.B', 3, "Hunger is influenced by both biological signals and what?", "learned cultural habits", ["language only", "weather only", "sleep only"], "Mealtimes and food preferences are learned.")

# 8 intelligence
H('8', 3, "Charles Spearman proposed a general factor of intelligence known as what?", "g", ["IQ", "EQ", "SAT"], "He saw intelligence as one underlying ability.")
H('8', 3, "Howard Gardner proposed that people have what?", "multiple intelligences", ["one general intelligence only", "no intelligence", "only emotional intelligence"], "He listed several, such as musical and spatial.")
H('8', 3, "Robert Sternberg's triarchic theory includes which three kinds of intelligence?", "analytical, creative and practical", ["verbal, math and spatial", "emotional, social and physical", "visual, auditory and kinesthetic"], "It broadens intelligence beyond school.")

# 9 testing
H('9.A', 3, "A test is reliable if it does what?", "gives consistent results over time", ["measures what it claims to measure", "is expensive", "is very short"], "Validity concerns accuracy of measurement.")
H('9.A', 3, "A test is valid if it does what?", "measures what it is supposed to measure", ["gives consistent results only", "is long", "is easy"], "Validity is about accuracy.")
H('9.A', 3, "Standardization means a test is what?", "given and scored the same way for all", ["written differently for each person", "scored by the test-taker", "never revised"], "Norms allow comparisons.")
H('9.B', 3, "An aptitude test is designed to predict what?", "future performance or potential", ["past achievement", "personality", "memory only"], "The SAT is intended to predict college success.")
H('9.B', 3, "An achievement test measures what?", "what a person has already learned", ["future potential only", "personality", "emotions"], "A final exam is an achievement test.")
H('9.B', 3, "Intelligence Quotient (IQ) scores are typically scaled so that the average is what?", "100", ["50", "150", "10"], "Standard deviation is about 15.")

# 10 personality
H('10.A', 3, "Personality is best defined as what?", "an individual's relatively stable pattern of thoughts, feelings and behaviors", ["a temporary mood", "a skill", "an IQ score"], "It makes each person distinctive.")
H('10.B', 3, "Freud's psychodynamic theory divides the personality into id, ego and what?", "superego", ["alter ego", "libido", "shadow"], "The superego represents conscience.")
H('10.B', 3, "The Big Five trait model includes openness, conscientiousness, extraversion, agreeableness and what?", "neuroticism", ["intelligence", "optimism", "sensitivity"], "It is often remembered as OCEAN.")
H('10.B', 3, "Which approach emphasizes personal growth and self-actualization?", "humanistic", ["psychodynamic", "behaviorist", "trait"], "Rogers and Maslow shaped it.")
H('10.C', 3, "The Minnesota Multiphasic Personality Inventory (MMPI) is what kind of tool?", "a self-report questionnaire", ["a brain scan", "an IQ test", "an inkblot"], "It assesses personality and psychopathology.")
H('10.C', 3, "The Rorschach test is what kind of assessment?", "a projective test using inkblots", ["an IQ test", "a lie detector", "a driving test"], "Responses are interpreted by clinicians.")

# 11 cognition
H('11.A', 3, "Concepts are best described as what?", "mental categories of objects, events or ideas", ["emotions", "reflexes", "dreams"], "They help us organize information.")
H('11.B', 3, "An algorithm in problem solving is what?", "a step-by-step procedure that guarantees a solution", ["a quick guess", "a rule of thumb", "a bias"], "Heuristics are mental shortcuts.")
H('11.B', 3, "Functional fixedness is an obstacle to problem solving because it does what?", "limits seeing objects used in new ways", ["increases creativity", "speeds solutions", "removes bias"], "A person cannot see a screwdriver as a wedge.")
H('11.B', 3, "Confirmation bias is the tendency to do what?", "seek information that supports existing beliefs", ["avoid all information", "change opinions instantly", "ignore your own ideas"], "It can distort decision making.")
H('11.C', 3, "A phoneme is what?", "the smallest unit of sound in a language", ["the smallest unit of meaning", "a sentence", "a word"], "A morpheme is the smallest meaningful unit.")
H('11.C', 3, "Syntax refers to what?", "the rules for combining words into sentences", ["the meaning of words", "the sounds of words", "the written form"], "Grammar includes syntax.")
H('11.D', 3, "Noam Chomsky argued that language acquisition is helped by what?", "an innate capacity for language", ["only reinforcement", "only imitation", "only classroom teaching"], "He proposed a language acquisition device.")
H('11.D', 3, "B. F. Skinner argued that language is learned mainly through what?", "reinforcement and shaping", ["innate grammar", "dreams", "instinct"], "A behaviorist view.")
H('11.E', 3, "In the information processing model, information first enters which memory?", "sensory memory", ["long-term memory", "short-term memory", "implicit memory"], "Then it moves to short-term, and then long-term, if encoded.")
H('11.E', 3, "Short-term memory can hold about how many items at once?", "7 plus or minus 2", ["20", "100", "1"], "George Miller's famous estimate.")
H('11.E', 3, "A limitation of the information processing model is that it does what?", "compares the mind to a computer and may oversimplify", ["ignores memory", "ignores attention", "is only about emotion"], "Human thinking is more flexible than a computer.")
H('11.F', 3, "Which of these is a state of consciousness?", "REM sleep", ["a neuron", "a hormone", "a reflex"], "Dreaming happens during REM sleep.")
H('11.F', 3, "Circadian rhythms are what?", "biological cycles of about 24 hours", ["monthly cycles", "yearly cycles", "hourly cycles"], "They regulate sleep and waking.")

# 12 stress and disorders
H('12.A', 3, "Hans Selye's general adaptation syndrome has three stages: alarm, resistance and what?", "exhaustion", ["recovery", "denial", "anger"], "Prolonged stress depletes resources.")
H('12.A', 3, "Stress is best described as what?", "the body's response to demands or threats", ["a mental illness", "a personality type", "a type of memory"], "Stressors vary.")
H('12.B', 3, "Which is an effective coping strategy for stress?", "regular exercise and social support", ["avoiding all problems", "using substances to escape", "ignoring sleep"], "Healthy coping reduces stress effects.")
H('12.B', 3, "Cognitive reappraisal as a stress strategy involves what?", "rethinking how you interpret a stressful event", ["denying it happened", "avoiding all people", "acting aggressively"], "Changing thoughts can change feelings.")
H('12.C', 4, "A challenge in defining abnormal behavior is that what?", "standards of normal vary across cultures and times", ["all behavior is always abnormal", "no one can define it", "it is the same everywhere"], "Context and culture matter.")
H('12.C', 4, "Which is commonly used as a criterion for judging behavior as a disorder?", "it causes distress or impairs daily functioning", ["it is merely unusual", "it is unpopular", "it is rare"], "Dysfunction and distress are central.")
H('12.D', 3, "The biopsychosocial approach explains disorders as resulting from what?", "biological, psychological and social factors together", ["biology alone", "thoughts alone", "society alone"], "Causes interact.")
H('12.E', 3, "Which category of disorders includes excessive fear or worry?", "anxiety disorders", ["mood disorders", "personality disorders", "sleep disorders"], "Phobias and panic disorder are examples.")
H('12.E', 3, "Major depressive disorder is classified as what?", "a mood disorder", ["an anxiety disorder", "a personality disorder", "a sleep disorder"], "It involves persistent low mood.")
H('12.E', 3, "Schizophrenia is characterized by symptoms such as what?", "hallucinations and disorganized thinking", ["fear of heights only", "love of routines", "shyness"], "It is a psychotic disorder.")
H('12.F', 3, "Cognitive-behavioral therapy (CBT) focuses on what?", "changing unhelpful thoughts and behaviors", ["uncovering unconscious conflicts only", "dream interpretation", "medication only"], "It has strong research support.")
H('12.F', 3, "Psychoanalysis, developed by Freud, aims to do what?", "bring unconscious conflicts into awareness", ["change behavior with rewards", "give medication", "teach relaxation only"], "It uses free association.")

# 13 social psychology
H('13.A', 3, "The fundamental attribution error is the tendency to do what?", "overestimate personality and underestimate situation in explaining others' behavior", ["blame the situation only", "blame yourself only", "ignore behavior"], "We judge others by traits, ourselves by situation.")
H('13.B', 3, "A prejudice is best defined as what?", "an unjustified negative attitude toward a group", ["a behavior", "a law", "a skill"], "Discrimination is the behavior.")
H('13.B', 3, "Discrimination is what?", "unfair treatment of people based on group membership", ["a negative attitude only", "a memory bias", "a personality trait"], "Prejudice is attitude; discrimination is action.")
H('13.C', 3, "In Stanley Milgram's studies, many participants did what?", "obeyed an authority figure even when they believed they were harming someone", ["refused immediately", "laughed", "left the room"], "It showed the power of obedience.")
H('13.C', 3, "In Solomon Asch's line studies, participants often did what?", "conformed to the group's wrong answer", ["always stood alone", "refused to answer", "changed the lines"], "They went along with confederates.")
H('13.D', 3, "The bystander effect is the tendency for people to be what?", "less likely to help when others are present", ["more likely to help", "unaffected by others", "always helpful"], "Responsibility is diffused.")
H('13.D', 3, "Social facilitation means that the presence of others does what?", "improves performance on easy or well-learned tasks", ["always worsens performance", "has no effect", "stops all behavior"], "It can hurt performance on hard tasks.")
H('13.E', 3, "Altruism is best described as what?", "helping others with no expectation of reward", ["helping for pay", "helping to avoid punishment", "avoiding others"], "It is unselfish concern for others.")
H('13.F', 3, "Which factor most strongly predicts attraction?", "proximity", ["birth month", "eye color", "handwriting"], "People like those they see often.")
H('13.F', 3, "The mere exposure effect says that people tend to like what?", "things they see repeatedly", ["new things", "rare things", "disliked things"], "Familiarity breeds liking.")
H('13.G', 3, "Cognitive dissonance occurs when what happens?", "behavior conflicts with beliefs, creating discomfort", ["beliefs match behavior", "people feel proud", "people forget"], "People may change attitudes to reduce it.")
H('13.G', 3, "Advertisers often use celebrities to influence attitudes through which route?", "the peripheral route to persuasion", ["the central route", "a placebo", "random assignment"], "They rely on attractiveness rather than arguments.")

# 14 skills
H('14.A', 3, "A good psychology product on a current issue should be based on what?", "credible research and clear reasoning", ["rumor", "one anecdote", "personal opinion only"], "Critical methods improve quality.")
H('14.B', 3, "Interviews and observations produce what kind of information?", "qualitative", ["quantitative", "statistical only", "random only"], "Qualitative data is descriptive.")
H('14.C', 3, "A study with a very small sample may produce results that are what?", "less reliable or hard to generalize", ["more reliable", "always valid", "automatically correct"], "Large, random samples are better.")
H('14.D', 3, "Putting events of a person's development in order is what skill?", "sequencing", ["averaging", "ignoring cause", "reversing"], "Analysis includes sequencing.")

# 15 communication
H('15.A', 3, "Which term describes the process by which we make sense of sensory input?", "perception", ["sensation", "adaptation", "attention"], "Sensation detects; perception interprets.")
H('15.B', 3, "Proofreading a psychology report for grammar and spelling is an example of what?", "using standard written conventions", ["gathering data", "designing an experiment", "memorizing facts"], "Clear writing aids communication.")
H('15.C', 3, "Turning a table of survey results into a bar graph is an example of what?", "transferring information from one medium to another", ["ignoring data", "creating bias", "sequencing"], "Visual formats can clarify data.")
H('15.D', 3, "A strong oral presentation about a psychology topic includes what?", "a clear organization and supporting evidence", ["no sources", "only opinions", "reading text with no eye contact"], "Evidence and organization matter.")

# 16 problem solving
H('16.A', 3, "In a problem-solving process, what should you do after identifying a problem?", "gather information and list possible solutions", ["choose a solution without thinking", "end the process", "ignore the facts"], "Information precedes choosing.")
H('16.B', 3, "In a decision-making process, after gathering information you should do what?", "consider options and their likely consequences", ["flip a coin", "ask no one", "wait indefinitely"], "Weigh alternatives.")
H('16.C', 3, "Which is a strategy for conflict resolution?", "compromise and negotiation", ["avoiding forever", "threats", "ignoring the issue"], "Both sides give a little.")

# 17 goals
H('17.A', 3, "Intermediate goals are best described as what?", "smaller steps that lead to a larger terminal goal", ["the final goal", "unrelated tasks", "unrealistic goals"], "Breaking goals down helps progress.")
H('17.B', 3, "Monitoring a long project for timelines and accuracy is an example of what?", "self-directed evaluation", ["procrastination", "peer pressure", "denial"], "Check progress against goals.")

# 18 technology
H('18.A', 3, "How have smartphones changed attitudes and behaviors?", "people communicate and share information more constantly", ["people no longer use phones", "face-to-face contact increased everywhere", "attention spans disappeared"], "Technology influences how we interact.")
H('18.B', 3, "A potential negative effect of heavy social media use on personal growth is what?", "increased social comparison and less sleep", ["better sleep for everyone", "less information", "fewer friends in all cases"], "Effects vary by use.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_psych.jsonl'))

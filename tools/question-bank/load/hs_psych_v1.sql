insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_psych_v1'
from (values
('113.45.c.1.A',3,'What most clearly separates psychology from sociology?','["psychology focuses on individual behavior and mental processes", "psychology studies only groups and institutions", "psychology studies only rocks", "psychology studies only governments"]'::jsonb,0,'Sociology examines groups and society.','original'),
('113.45.c.1.B',3,'Wilhelm Wundt is credited with doing what in 1879?','["writing the Bible", "opening the first psychology laboratory", "founding Harvard", "inventing the telephone"]'::jsonb,1,'He is considered the father of experimental psychology.','original'),
('113.45.c.1.B',3,'Which perspective focuses on observable behavior and learning from the environment?','["humanism", "structuralism", "behaviorism", "psychoanalysis"]'::jsonb,2,'Watson and Skinner shaped it.','original'),
('113.45.c.1.B',3,'Sigmund Freud emphasized which influence on behavior?','["only observable behavior", "only brain scans", "only genetics", "unconscious drives and early experiences"]'::jsonb,3,'He founded psychoanalysis.','original'),
('113.45.c.1.B',3,'Humanistic psychologists such as Carl Rogers stressed what?','["free will and personal growth", "brain structure only", "conditioning only", "unconscious conflict only"]'::jsonb,0,'They emphasize self-actualization.','original'),
('113.45.c.1.C',3,'A psychologist who helps people with mental health problems through therapy is called what?','["an industrial engineer", "a clinical psychologist", "a statistician only", "a geologist"]'::jsonb,1,'Clinical psychology treats disorders.','original'),
('113.45.c.1.C',3,'A school psychologist most often does what?','["tests soil", "trains pilots", "supports students'' learning and emotional needs", "designs bridges"]'::jsonb,2,'School psychologists assess and counsel.','original'),
('113.45.c.2.A',3,'A hypothesis is best described as what?','["an opinion with no test", "a final conclusion", "a proven fact", "a testable prediction"]'::jsonb,3,'A theory explains many findings; a hypothesis is tested.','original'),
('113.45.c.2.A',3,'A scientific theory differs from a hunch because a theory does what?','["organizes and explains many tested observations", "is a guess", "needs no evidence", "can never change"]'::jsonb,0,'Theories are supported by evidence.','original'),
('113.45.c.2.B',3,'In an experiment, the variable the researcher manipulates is called what?','["the dependent variable", "the independent variable", "the control group", "the sample"]'::jsonb,1,'It is the presumed cause.','original'),
('113.45.c.2.B',3,'In an experiment, the variable that is measured for change is called what?','["the placebo", "the hypothesis", "the dependent variable", "the independent variable"]'::jsonb,2,'It is the outcome.','original'),
('113.45.c.2.B',3,'A correlation between two variables shows what?','["that the study was biased", "that one causes the other", "that there is no relation", "that they are related, not that one causes the other"]'::jsonb,3,'Correlation is not causation.','original'),
('113.45.c.2.B',3,'Random assignment helps researchers do what?','["make groups equivalent at the start of an experiment", "avoid collecting data", "prove the hypothesis", "choose only volunteers"]'::jsonb,0,'It reduces pre-existing differences.','original'),
('113.45.c.2.B',3,'A control group in an experiment does what?','["is the researchers", "does not receive the treatment, for comparison", "receives the largest dose", "chooses its own treatment"]'::jsonb,1,'It provides a baseline.','original'),
('113.45.c.2.C',3,'Under APA ethical standards, researchers must obtain what from participants?','["their grades", "their addresses", "informed consent", "payment only"]'::jsonb,2,'Participants must know the risks and agree.','original'),
('113.45.c.2.C',3,'Debriefing after a study is used to do what?','["hide the results", "collect payment", "punish participants", "explain the true purpose and address any concerns"]'::jsonb,3,'It is an ethical requirement.','original'),
('113.45.c.2.D',3,'The mean of 2, 4, 4, 6 and 9 is what?','["5", "6", "4", "9"]'::jsonb,0,'Sum 25 divided by 5 equals 5.','original'),
('113.45.c.2.D',3,'The median of 3, 5, 7, 9 and 11 is what?','["35", "7", "9", "5"]'::jsonb,1,'It is the middle value.','original'),
('113.45.c.2.D',3,'The mode of 2, 3, 3, 4, 5, 3 and 6 is what?','["4", "2", "3", "5"]'::jsonb,2,'It is the most frequent value.','original'),
('113.45.c.2.D',4,'The standard deviation measures what?','["the most common score", "the middle score", "the total of all scores", "how spread out the scores are around the mean"]'::jsonb,3,'It is a measure of dispersion.','original'),
('113.45.c.3.A',3,'The central nervous system consists of what?','["the brain and spinal cord", "the glands", "the heart and lungs", "the nerves in the limbs"]'::jsonb,0,'The peripheral system connects to the body.','original'),
('113.45.c.3.A',3,'A neuron''s branching fibers that receive signals are called what?','["myelin sheaths", "dendrites", "axons", "synapses"]'::jsonb,1,'Axons send signals away.','original'),
('113.45.c.3.A',3,'The part of the brain that controls balance and coordination is the what?','["amygdala", "frontal lobe", "cerebellum", "hippocampus"]'::jsonb,2,'It fine-tunes movement.','original'),
('113.45.c.3.A',3,'The endocrine system uses which chemical messengers?','["neurotransmitters only", "enzymes", "antibodies", "hormones"]'::jsonb,3,'Glands release hormones into the blood.','original'),
('113.45.c.3.B',3,'The fight-or-flight response is controlled by which system?','["the sympathetic nervous system", "the parasympathetic nervous system", "the immune system", "the digestive system"]'::jsonb,0,'It prepares the body for action.','original'),
('113.45.c.3.B',3,'Adrenaline released by the adrenal glands does what?','["lowers heart rate", "increases heart rate and alertness", "causes sleep", "slows breathing"]'::jsonb,1,'It is a stress hormone.','original'),
('113.45.c.4.A',3,'A sensory receptor stops responding to a constant stimulus through what process?','["selective attention", "habituation to noise only", "sensory adaptation", "perceptual set"]'::jsonb,2,'You stop noticing a smell after a while.','original'),
('113.45.c.4.A',3,'The smallest amount of stimulus a person can detect half the time is the what?','["perceptual constancy", "sensory memory", "difference threshold", "absolute threshold"]'::jsonb,3,'It marks the detection limit.','original'),
('113.45.c.4.B',3,'Perceptual set is the tendency to do what?','["perceive things based on expectations and experience", "ignore all stimuli", "hear only low sounds", "see only colors"]'::jsonb,0,'Context and expectation shape perception.','original'),
('113.45.c.4.B',3,'Depth perception is aided by which cue?','["the temperature of air", "retinal disparity (the slight difference between eyes'' images)", "the taste of food", "the weight of objects"]'::jsonb,1,'Binocular cues help judge distance.','original'),
('113.45.c.5.A',3,'The nature versus nurture debate asks about what?','["whether memory is real", "whether brains exist", "the relative influence of heredity and environment", "whether stress is common"]'::jsonb,2,'Most psychologists believe both matter.','original'),
('113.45.c.5.A',3,'Studies of identical twins reared apart help psychologists examine what?','["only environmental influence", "birth weight only", "which twin is older", "genetic influences on traits"]'::jsonb,3,'Shared genes with different environments.','original'),
('113.45.c.5.B',3,'Maturation refers to what?','["biological growth processes that follow a genetic timetable", "learning by reward", "social pressure", "emotional stress"]'::jsonb,0,'Walking is partly maturational.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_psych_v1'
from (values
('113.45.c.5.C',3,'In Harry Harlow''s monkey studies, infant monkeys preferred what?','["the wire mother with food", "a soft cloth ''mother'' over a wire one that gave food", "no mother", "other monkeys only"]'::jsonb,1,'Contact comfort mattered more than feeding.','original'),
('113.45.c.5.C',3,'Attachment is best described as what?','["a type of memory", "a language skill", "an emotional bond between infant and caregiver", "a form of punishment"]'::jsonb,2,'Bowlby and Ainsworth studied it.','original'),
('113.45.c.5.D',3,'Piaget''s first stage of cognitive development is the what?','["concrete operational stage", "preoperational stage", "formal operational stage", "sensorimotor stage"]'::jsonb,3,'Babies learn through senses and actions.','original'),
('113.45.c.5.D',3,'Object permanence, understanding that objects exist when out of sight, develops in which stage?','["sensorimotor", "preoperational", "concrete operational", "formal operational"]'::jsonb,0,'Peekaboo plays with it.','original'),
('113.45.c.5.D',3,'In Piaget''s concrete operational stage, children can do what?','["think abstractly about hypotheticals", "think logically about concrete events and understand conservation", "only use senses", "only use symbols without logic"]'::jsonb,1,'Ages about 7 to 11.','original'),
('113.45.c.5.D',3,'Abstract and hypothetical reasoning appears in which of Piaget''s stages?','["sensorimotor", "preoperational", "formal operational", "concrete operational"]'::jsonb,2,'It typically emerges in adolescence.','original'),
('113.45.c.5.E',3,'According to Erikson, the main crisis of adolescence is what?','["industry versus inferiority", "trust versus mistrust", "integrity versus despair", "identity versus role confusion"]'::jsonb,3,'Teens explore who they are.','original'),
('113.45.c.5.E',3,'Erikson''s first stage, in infancy, concerns what?','["trust versus mistrust", "autonomy versus shame", "intimacy versus isolation", "initiative versus guilt"]'::jsonb,0,'Caregivers help babies build trust.','original'),
('113.45.c.5.F',4,'Using Erikson''s theory, which outcome is most likely for a child whose efforts are consistently praised in school?','["role confusion", "a sense of industry and competence", "despair", "mistrust"]'::jsonb,1,'The industry-versus-inferiority stage occurs in school years.','original'),
('113.45.c.5.G',4,'A common criticism of Piaget''s theory is that it does what?','["overestimates their abilities", "ignores development", "underestimates children''s abilities at young ages", "ignores stages"]'::jsonb,2,'Later research showed earlier competence.','original'),
('113.45.c.5.G',4,'A strength of stage theories of development is that they do what?','["ignore culture", "prove every child develops the same", "avoid evidence", "provide a framework to describe typical changes"]'::jsonb,3,'But they may oversimplify individual differences.','original'),
('113.45.c.6.A',3,'In classical conditioning, a stimulus that triggers a response without learning is called what?','["an unconditioned stimulus", "a conditioned stimulus", "a reinforcer", "a neutral stimulus"]'::jsonb,0,'Food triggers salivation naturally.','original'),
('113.45.c.6.A',3,'In Pavlov''s experiment, the bell became a what after being paired with food?','["unconditioned stimulus", "conditioned stimulus", "unconditioned response", "punishment"]'::jsonb,1,'It then produced salivation by itself.','original'),
('113.45.c.6.A',3,'In operant conditioning, behavior is strengthened by what?','["habituation", "extinction only", "reinforcement", "punishment only"]'::jsonb,2,'Skinner studied it.','original'),
('113.45.c.6.A',3,'Taking away an unpleasant stimulus to increase a behavior is called what?','["positive punishment", "extinction", "positive reinforcement", "negative reinforcement"]'::jsonb,3,'Buckling a seat belt to stop the buzzer is an example.','original'),
('113.45.c.6.A',3,'Which schedule of reinforcement produces the highest and steadiest response rate?','["variable ratio", "fixed interval", "continuous", "fixed ratio"]'::jsonb,0,'Slot machines use it.','original'),
('113.45.c.6.B',3,'A teacher who gives stickers for completed homework is using what?','["negative reinforcement", "positive reinforcement", "extinction", "classical conditioning"]'::jsonb,1,'A pleasant stimulus is added to strengthen behavior.','original'),
('113.45.c.6.B',3,'Learning by watching and imitating others is called what?','["extinction", "classical conditioning", "observational learning", "habituation"]'::jsonb,2,'Bandura''s Bobo doll studies illustrate it.','original'),
('113.45.c.7.A',3,'Maslow''s hierarchy of needs places which needs at the base?','["self-actualization", "esteem", "belonging", "physiological needs such as food and water"]'::jsonb,3,'Basic needs come before higher ones.','original'),
('113.45.c.7.A',3,'The James-Lange theory proposes that emotion results from what?','["bodily arousal", "thoughts alone", "culture alone", "memories alone"]'::jsonb,0,'We feel afraid because we tremble.','original'),
('113.45.c.7.A',3,'The Schachter-Singer two-factor theory says emotion depends on arousal plus what?','["a reflex", "a cognitive label", "a hormone", "a memory"]'::jsonb,1,'Interpretation shapes the feeling.','original'),
('113.45.c.7.B',3,'Display rules, which guide how emotions are shown, are shaped mostly by what?','["hormones only", "weather", "culture", "genetics only"]'::jsonb,2,'Cultures differ in what is acceptable to express.','original'),
('113.45.c.7.B',3,'Hunger is influenced by both biological signals and what?','["weather only", "sleep only", "language only", "learned cultural habits"]'::jsonb,3,'Mealtimes and food preferences are learned.','original'),
('113.45.c.8',3,'Charles Spearman proposed a general factor of intelligence known as what?','["g", "EQ", "IQ", "SAT"]'::jsonb,0,'He saw intelligence as one underlying ability.','original'),
('113.45.c.8',3,'Howard Gardner proposed that people have what?','["no intelligence", "multiple intelligences", "one general intelligence only", "only emotional intelligence"]'::jsonb,1,'He listed several, such as musical and spatial.','original'),
('113.45.c.8',3,'Robert Sternberg''s triarchic theory includes which three kinds of intelligence?','["emotional, social and physical", "verbal, math and spatial", "analytical, creative and practical", "visual, auditory and kinesthetic"]'::jsonb,2,'It broadens intelligence beyond school.','original'),
('113.45.c.9.A',3,'A test is reliable if it does what?','["is very short", "measures what it claims to measure", "is expensive", "gives consistent results over time"]'::jsonb,3,'Validity concerns accuracy of measurement.','original'),
('113.45.c.9.A',3,'A test is valid if it does what?','["measures what it is supposed to measure", "is easy", "is long", "gives consistent results only"]'::jsonb,0,'Validity is about accuracy.','original'),
('113.45.c.9.A',3,'Standardization means a test is what?','["never revised", "given and scored the same way for all", "scored by the test-taker", "written differently for each person"]'::jsonb,1,'Norms allow comparisons.','original'),
('113.45.c.9.B',3,'An aptitude test is designed to predict what?','["memory only", "past achievement", "future performance or potential", "personality"]'::jsonb,2,'The SAT is intended to predict college success.','original'),
('113.45.c.9.B',3,'An achievement test measures what?','["future potential only", "personality", "emotions", "what a person has already learned"]'::jsonb,3,'A final exam is an achievement test.','original'),
('113.45.c.9.B',3,'Intelligence Quotient (IQ) scores are typically scaled so that the average is what?','["100", "50", "10", "150"]'::jsonb,0,'Standard deviation is about 15.','original'),
('113.45.c.10.A',3,'Personality is best defined as what?','["an IQ score", "an individual''s relatively stable pattern of thoughts, feelings and behaviors", "a temporary mood", "a skill"]'::jsonb,1,'It makes each person distinctive.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_psych_v1'
from (values
('113.45.c.10.B',3,'Freud''s psychodynamic theory divides the personality into id, ego and what?','["alter ego", "libido", "superego", "shadow"]'::jsonb,2,'The superego represents conscience.','original'),
('113.45.c.10.B',3,'The Big Five trait model includes openness, conscientiousness, extraversion, agreeableness and what?','["sensitivity", "intelligence", "optimism", "neuroticism"]'::jsonb,3,'It is often remembered as OCEAN.','original'),
('113.45.c.10.B',3,'Which approach emphasizes personal growth and self-actualization?','["humanistic", "behaviorist", "trait", "psychodynamic"]'::jsonb,0,'Rogers and Maslow shaped it.','original'),
('113.45.c.10.C',3,'The Minnesota Multiphasic Personality Inventory (MMPI) is what kind of tool?','["an IQ test", "a self-report questionnaire", "a brain scan", "an inkblot"]'::jsonb,1,'It assesses personality and psychopathology.','original'),
('113.45.c.10.C',3,'The Rorschach test is what kind of assessment?','["a driving test", "a lie detector", "a projective test using inkblots", "an IQ test"]'::jsonb,2,'Responses are interpreted by clinicians.','original'),
('113.45.c.11.A',3,'Concepts are best described as what?','["emotions", "reflexes", "dreams", "mental categories of objects, events or ideas"]'::jsonb,3,'They help us organize information.','original'),
('113.45.c.11.B',3,'An algorithm in problem solving is what?','["a step-by-step procedure that guarantees a solution", "a bias", "a rule of thumb", "a quick guess"]'::jsonb,0,'Heuristics are mental shortcuts.','original'),
('113.45.c.11.B',3,'Functional fixedness is an obstacle to problem solving because it does what?','["speeds solutions", "limits seeing objects used in new ways", "removes bias", "increases creativity"]'::jsonb,1,'A person cannot see a screwdriver as a wedge.','original'),
('113.45.c.11.B',3,'Confirmation bias is the tendency to do what?','["avoid all information", "change opinions instantly", "seek information that supports existing beliefs", "ignore your own ideas"]'::jsonb,2,'It can distort decision making.','original'),
('113.45.c.11.C',3,'A phoneme is what?','["a sentence", "a word", "the smallest unit of meaning", "the smallest unit of sound in a language"]'::jsonb,3,'A morpheme is the smallest meaningful unit.','original'),
('113.45.c.11.C',3,'Syntax refers to what?','["the rules for combining words into sentences", "the meaning of words", "the written form", "the sounds of words"]'::jsonb,0,'Grammar includes syntax.','original'),
('113.45.c.11.D',3,'Noam Chomsky argued that language acquisition is helped by what?','["only reinforcement", "an innate capacity for language", "only imitation", "only classroom teaching"]'::jsonb,1,'He proposed a language acquisition device.','original'),
('113.45.c.11.D',3,'B. F. Skinner argued that language is learned mainly through what?','["instinct", "innate grammar", "reinforcement and shaping", "dreams"]'::jsonb,2,'A behaviorist view.','original'),
('113.45.c.11.E',3,'In the information processing model, information first enters which memory?','["implicit memory", "long-term memory", "short-term memory", "sensory memory"]'::jsonb,3,'Then it moves to short-term, and then long-term, if encoded.','original'),
('113.45.c.11.E',3,'Short-term memory can hold about how many items at once?','["7 plus or minus 2", "1", "100", "20"]'::jsonb,0,'George Miller''s famous estimate.','original'),
('113.45.c.11.E',3,'A limitation of the information processing model is that it does what?','["ignores memory", "compares the mind to a computer and may oversimplify", "is only about emotion", "ignores attention"]'::jsonb,1,'Human thinking is more flexible than a computer.','original'),
('113.45.c.11.F',3,'Which of these is a state of consciousness?','["a neuron", "a reflex", "REM sleep", "a hormone"]'::jsonb,2,'Dreaming happens during REM sleep.','original'),
('113.45.c.11.F',3,'Circadian rhythms are what?','["hourly cycles", "monthly cycles", "yearly cycles", "biological cycles of about 24 hours"]'::jsonb,3,'They regulate sleep and waking.','original'),
('113.45.c.12.A',3,'Hans Selye''s general adaptation syndrome has three stages: alarm, resistance and what?','["exhaustion", "denial", "anger", "recovery"]'::jsonb,0,'Prolonged stress depletes resources.','original'),
('113.45.c.12.A',3,'Stress is best described as what?','["a mental illness", "the body''s response to demands or threats", "a type of memory", "a personality type"]'::jsonb,1,'Stressors vary.','original'),
('113.45.c.12.B',3,'Which is an effective coping strategy for stress?','["ignoring sleep", "using substances to escape", "regular exercise and social support", "avoiding all problems"]'::jsonb,2,'Healthy coping reduces stress effects.','original'),
('113.45.c.12.B',3,'Cognitive reappraisal as a stress strategy involves what?','["avoiding all people", "denying it happened", "acting aggressively", "rethinking how you interpret a stressful event"]'::jsonb,3,'Changing thoughts can change feelings.','original'),
('113.45.c.12.C',4,'A challenge in defining abnormal behavior is that what?','["standards of normal vary across cultures and times", "no one can define it", "it is the same everywhere", "all behavior is always abnormal"]'::jsonb,0,'Context and culture matter.','original'),
('113.45.c.12.C',4,'Which is commonly used as a criterion for judging behavior as a disorder?','["it is merely unusual", "it causes distress or impairs daily functioning", "it is unpopular", "it is rare"]'::jsonb,1,'Dysfunction and distress are central.','original'),
('113.45.c.12.D',3,'The biopsychosocial approach explains disorders as resulting from what?','["society alone", "thoughts alone", "biological, psychological and social factors together", "biology alone"]'::jsonb,2,'Causes interact.','original'),
('113.45.c.12.E',3,'Which category of disorders includes excessive fear or worry?','["personality disorders", "mood disorders", "sleep disorders", "anxiety disorders"]'::jsonb,3,'Phobias and panic disorder are examples.','original'),
('113.45.c.12.E',3,'Major depressive disorder is classified as what?','["a mood disorder", "a personality disorder", "a sleep disorder", "an anxiety disorder"]'::jsonb,0,'It involves persistent low mood.','original'),
('113.45.c.12.E',3,'Schizophrenia is characterized by symptoms such as what?','["love of routines", "hallucinations and disorganized thinking", "fear of heights only", "shyness"]'::jsonb,1,'It is a psychotic disorder.','original'),
('113.45.c.12.F',3,'Cognitive-behavioral therapy (CBT) focuses on what?','["uncovering unconscious conflicts only", "medication only", "changing unhelpful thoughts and behaviors", "dream interpretation"]'::jsonb,2,'It has strong research support.','original'),
('113.45.c.12.F',3,'Psychoanalysis, developed by Freud, aims to do what?','["change behavior with rewards", "give medication", "teach relaxation only", "bring unconscious conflicts into awareness"]'::jsonb,3,'It uses free association.','original'),
('113.45.c.13.A',3,'The fundamental attribution error is the tendency to do what?','["overestimate personality and underestimate situation in explaining others'' behavior", "blame yourself only", "ignore behavior", "blame the situation only"]'::jsonb,0,'We judge others by traits, ourselves by situation.','original'),
('113.45.c.13.B',3,'A prejudice is best defined as what?','["a law", "an unjustified negative attitude toward a group", "a skill", "a behavior"]'::jsonb,1,'Discrimination is the behavior.','original'),
('113.45.c.13.B',3,'Discrimination is what?','["a negative attitude only", "a memory bias", "unfair treatment of people based on group membership", "a personality trait"]'::jsonb,2,'Prejudice is attitude; discrimination is action.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_psych_v1'
from (values
('113.45.c.13.C',3,'In Stanley Milgram''s studies, many participants did what?','["refused immediately", "left the room", "laughed", "obeyed an authority figure even when they believed they were harming someone"]'::jsonb,3,'It showed the power of obedience.','original'),
('113.45.c.13.C',3,'In Solomon Asch''s line studies, participants often did what?','["conformed to the group''s wrong answer", "refused to answer", "changed the lines", "always stood alone"]'::jsonb,0,'They went along with confederates.','original'),
('113.45.c.13.D',3,'The bystander effect is the tendency for people to be what?','["more likely to help", "less likely to help when others are present", "always helpful", "unaffected by others"]'::jsonb,1,'Responsibility is diffused.','original'),
('113.45.c.13.D',3,'Social facilitation means that the presence of others does what?','["has no effect", "always worsens performance", "improves performance on easy or well-learned tasks", "stops all behavior"]'::jsonb,2,'It can hurt performance on hard tasks.','original'),
('113.45.c.13.E',3,'Altruism is best described as what?','["avoiding others", "helping for pay", "helping to avoid punishment", "helping others with no expectation of reward"]'::jsonb,3,'It is unselfish concern for others.','original'),
('113.45.c.13.F',3,'Which factor most strongly predicts attraction?','["proximity", "birth month", "handwriting", "eye color"]'::jsonb,0,'People like those they see often.','original'),
('113.45.c.13.F',3,'The mere exposure effect says that people tend to like what?','["disliked things", "things they see repeatedly", "rare things", "new things"]'::jsonb,1,'Familiarity breeds liking.','original'),
('113.45.c.13.G',3,'Cognitive dissonance occurs when what happens?','["people forget", "beliefs match behavior", "behavior conflicts with beliefs, creating discomfort", "people feel proud"]'::jsonb,2,'People may change attitudes to reduce it.','original'),
('113.45.c.13.G',3,'Advertisers often use celebrities to influence attitudes through which route?','["the central route", "random assignment", "a placebo", "the peripheral route to persuasion"]'::jsonb,3,'They rely on attractiveness rather than arguments.','original'),
('113.45.c.14.A',3,'A good psychology product on a current issue should be based on what?','["credible research and clear reasoning", "rumor", "personal opinion only", "one anecdote"]'::jsonb,0,'Critical methods improve quality.','original'),
('113.45.c.14.B',3,'Interviews and observations produce what kind of information?','["quantitative", "qualitative", "random only", "statistical only"]'::jsonb,1,'Qualitative data is descriptive.','original'),
('113.45.c.14.C',3,'A study with a very small sample may produce results that are what?','["automatically correct", "always valid", "less reliable or hard to generalize", "more reliable"]'::jsonb,2,'Large, random samples are better.','original'),
('113.45.c.14.D',3,'Putting events of a person''s development in order is what skill?','["averaging", "reversing", "ignoring cause", "sequencing"]'::jsonb,3,'Analysis includes sequencing.','original'),
('113.45.c.15.A',3,'Which term describes the process by which we make sense of sensory input?','["perception", "attention", "sensation", "adaptation"]'::jsonb,0,'Sensation detects; perception interprets.','original'),
('113.45.c.15.B',3,'Proofreading a psychology report for grammar and spelling is an example of what?','["memorizing facts", "using standard written conventions", "designing an experiment", "gathering data"]'::jsonb,1,'Clear writing aids communication.','original'),
('113.45.c.15.C',3,'Turning a table of survey results into a bar graph is an example of what?','["sequencing", "ignoring data", "transferring information from one medium to another", "creating bias"]'::jsonb,2,'Visual formats can clarify data.','original'),
('113.45.c.15.D',3,'A strong oral presentation about a psychology topic includes what?','["only opinions", "reading text with no eye contact", "no sources", "a clear organization and supporting evidence"]'::jsonb,3,'Evidence and organization matter.','original'),
('113.45.c.16.A',3,'In a problem-solving process, what should you do after identifying a problem?','["gather information and list possible solutions", "ignore the facts", "end the process", "choose a solution without thinking"]'::jsonb,0,'Information precedes choosing.','original'),
('113.45.c.16.B',3,'In a decision-making process, after gathering information you should do what?','["ask no one", "consider options and their likely consequences", "flip a coin", "wait indefinitely"]'::jsonb,1,'Weigh alternatives.','original'),
('113.45.c.16.C',3,'Which is a strategy for conflict resolution?','["ignoring the issue", "threats", "compromise and negotiation", "avoiding forever"]'::jsonb,2,'Both sides give a little.','original'),
('113.45.c.17.A',3,'Intermediate goals are best described as what?','["unrelated tasks", "unrealistic goals", "the final goal", "smaller steps that lead to a larger terminal goal"]'::jsonb,3,'Breaking goals down helps progress.','original'),
('113.45.c.17.B',3,'Monitoring a long project for timelines and accuracy is an example of what?','["self-directed evaluation", "procrastination", "denial", "peer pressure"]'::jsonb,0,'Check progress against goals.','original'),
('113.45.c.18.A',3,'How have smartphones changed attitudes and behaviors?','["attention spans disappeared", "people communicate and share information more constantly", "face-to-face contact increased everywhere", "people no longer use phones"]'::jsonb,1,'Technology influences how we interact.','original'),
('113.45.c.18.B',3,'A potential negative effect of heavy social media use on personal growth is what?','["better sleep for everyone", "less information", "increased social comparison and less sleep", "fewer friends in all cases"]'::jsonb,2,'Effects vary by use.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;

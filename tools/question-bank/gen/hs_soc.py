import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('113.46.c.', 1001, own='hs_soc.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('1.A',3,'Who is credited with coining the term "sociology" in the 1830s?',
  'Auguste Comte',['Karl Marx','Emile Durkheim','Max Weber'],'Comte called for a science of society.')
H('1.A',3,'Sociology developed as a field largely in response to what changes?',
  'Industrialization, urbanization and political revolutions',['The invention of the printing press','Ancient trade routes','The discovery of electricity only'],'Rapid social change prompted systematic study of society.')
H('1.B',3,'Which sociologist studied suicide rates to show that social forces shape individual behavior?',
  'Emile Durkheim',['Herbert Spencer','Harriet Martineau','Auguste Comte'],'His study "Suicide" is a classic example of sociological method.')
H('1.B',3,'Max Weber is best known for introducing which research approach?',
  'Verstehen, or interpretive understanding of meaning',['Strict laboratory experiments','Ignoring subjective meaning','Counting only crime statistics'],'Weber stressed understanding the meanings people attach to actions.')
H('1.C',3,'W. E. B. DuBois contributed to sociology by doing what?',
  'Conducting early empirical studies of African American communities such as The Philadelphia Negro',['Inventing the census','Founding the field of anthropology','Writing the first sociology textbook in Europe'],'He used surveys and data to study race and society.')
H('1.C',3,'Jane Addams is linked to sociology through which work?',
  'Hull House and social reform for immigrants and the poor',['Developing IQ tests','Founding the first stock exchange','Writing the Communist Manifesto'],'Her settlement house work shaped applied social research.')
H('2.A',3,'Which type of society relies mainly on herding animals for food?',
  'Pastoral society',['Industrial society','Hunting and gathering society','Postindustrial society'],'Pastoral societies move with herds.')
H('2.A',3,'In which type of society do most people work in factories producing goods using machines?',
  'Industrial society',['Agrarian society','Pastoral society','Hunting and gathering society'],'Mass production defines industrial societies.')
H('2.B',3,'A society whose economy is based mainly on information and services is called what?',
  'Postindustrial society',['Agrarian society','Horticultural society','Pastoral society'],'The U.S. economy today is largely service-based.')
H('2.B',3,'Which society type still exists today in a few remote regions and relies on foraging?',
  'Hunting and gathering society',['Postindustrial society','Industrial society','Information society'],'Small groups still live this way in places.')
H('2.C',3,'Industrialization in the United States led to the growth of what?',
  'Cities and factory wage labor',['Fewer cities','More subsistence farming only','A decline in immigration'],'Workers moved from farms to urban jobs.')
H('2.C',3,'Urbanization means what?',
  'A growing share of a population living in cities',['People moving to rural areas','A decline in technology','Fewer people working for wages'],'Industrialization pulled people into cities.')
H('2.D',3,'Which change best describes cultural life in the United States over the last century?',
  'Mass media spread shared popular culture across regions',['Culture stopped changing','All regional differences disappeared','Immigration ended'],'Radio, television and the internet spread cultural trends.')
H('2.D',3,'Comparing cultural life across countries is called what?',
  'Cross-cultural comparison',['Random sampling','Participant observation only','Deviance analysis'],'It reveals similarities and differences.')
H('3.A',3,'Which element of culture is a shared system of spoken or written symbols?',
  'Language',['Mores','Sanctions','Roles'],'Language transmits culture.')
H('3.A',3,'Cultural values are best described as what?',
  'Shared ideas about what is good, right and desirable',['Rules with legal penalties','Physical objects','Group membership lists'],'Norms reflect values.')
H('3.B',3,'Which statement best explains how culture works as a whole?',
  'Language, symbols, norms and values reinforce each other',['Each element exists independently','Only norms matter','Culture is made of laws alone'],'The parts interact to form a coherent way of life.')
H('3.B',3,'A norm that carries strong moral weight and is strictly enforced is called what?',
  'Mores',['Folkways','Fads','Customs'],'Mores concern right and wrong.')
H('3.C',3,'A subculture is a group that does what?',
  'Shares some elements of the larger culture but has its own distinct norms or values',['Rejects all of society','Has no norms','Is always illegal'],'Skaters and bikers are examples of subcultures.')
H('3.C',3,'Which is an example of a subculture?',
  'Amish communities in the United States',['The entire U.S. population','A national government','A family reunion'],'They share U.S. life but keep distinct practices.')
H('4.A',3,'A primary group is characterized by what?',
  'Small size, close personal ties and long-lasting relationships',['Large size and impersonal ties','Short-term contracts','Anonymous interactions'],'Family and close friends are primary groups.')
H('4.A',3,'A secondary group is best illustrated by what?',
  'A work team or college class that forms around a goal',['A family','A close circle of childhood friends','A couple'],'Secondary groups are goal-oriented and often temporary.')
H('4.B',3,'Role conflict occurs when what happens?',
  'The demands of two roles a person holds clash',['A person has no roles','Everyone agrees on roles','A role is ascribed'],'A student who is also a parent may face it.')
H('4.B',3,'A reference group is one that people use to do what?',
  'Evaluate their own attitudes and behavior',['Elect leaders','Avoid all contact','Create laws'],'We compare ourselves with those groups.')
H('5.A',3,'Which of these is a source of cultural differences in norms within the United States?',
  'Ethnicity and socioeconomic status',['Time zones only','Alphabet differences','Currency rates'],'Norms vary among subgroups.')
H('5.A',3,'Ethnocentrism is the practice of what?',
  'Judging another culture by the standards of your own',['Studying cultures neutrally','Adopting a new culture','Avoiding all cultures'],'Cultural relativism is its counterpart.')
H('5.B',3,'A stereotype is best described as what?',
  'An oversimplified generalization about a group',['A tested scientific fact','A law','A voluntary choice'],'Stereotypes ignore individual differences.')
H('5.B',3,'Stereotypes about subcultures can be harmful because they do what?',
  'Lead to unfair treatment of individuals',['Increase accuracy','Improve communication','Eliminate bias'],'They shape attitudes and discrimination.')
H('5.C',3,'Which is a social problem often studied in subcultures?',
  'Gang violence',['Weather','Geology','Orbital mechanics'],'Sociologists examine causes and consequences.')
H('5.C',3,'A social problem is generally defined as what?',
  'A condition many people view as harmful to society and wish to change',['Any personal inconvenience','A law','A tradition'],'Poverty and crime are examples.')
H('5.D',3,'A counterculture is a group that does what?',
  'Rejects major values of the dominant culture',['Fully supports dominant norms','Has no members','Is formed by government'],'The 1960s hippie movement is an example.')
H('5.D',3,'The 1960s counterculture influenced American society by doing what?',
  'Challenging norms about war, authority and lifestyle',['Ending the Cold War','Abolishing the Constitution','Creating the stock market'],'Some changes were later absorbed into the mainstream.')
H('6.A',3,'Socialization is best defined as what?',
  'The lifelong process of learning the norms, values and roles of a society',['A genetic process','A government program','A type of crime'],'It is culturally shaped.')
H('6.A',3,'Why does socialization differ between cultures?',
  'Each culture teaches its own norms and values',['Humans are born with identical beliefs','Biology alone decides','Governments forbid it'],'What is learned depends on culture.')
H('6.B',3,'Which is the most important agent of socialization for young children?',
  'The family',['The workplace','The mass media','The military'],'Family provides the first lessons.')
H('6.B',3,'Peer groups are important agents of socialization because they do what?',
  'Teach norms among equals and influence adolescent behavior',['Replace schools','Make laws','Give grades'],'Peers matter strongly in adolescence.')
H('6.C',3,'Resocialization occurs when a person does what?',
  'Learns new norms and values, as in boot camp or prison',['Remains unchanged','Forgets language','Joins a primary group only'],'Adults can be socialized again.')
H('6.C',3,'Anticipatory socialization is learning what?',
  'The norms of a role you expect to take on later',['Skills you will never use','Laws of other countries','Past roles only'],'A student preparing for college is an example.')
H('7.A',3,'Adolescence as a distinct stage developed in part because of what?',
  'Compulsory education and child labor laws that kept youth out of the workforce',['The invention of the telephone','A decline in schooling','Longer working days for teens'],'These changes extended the time between childhood and adulthood.')
H('7.A',3,'The juvenile justice system, created around 1900, reflected the belief that young offenders should be what?',
  'Rehabilitated rather than punished as adults',['Executed','Ignored','Sent to adult prisons'],'It recognized adolescence as separate from adulthood.')
H('7.B',3,'Which is one of the characteristics of adolescence?',
  'Biological growth and development',['Retirement','Marriage by law','Complete financial independence'],'Puberty is a major biological change.')
H('7.B',3,'Identity formation during adolescence involves what?',
  'Exploring who one is and what one values',['Giving up all choices','Following only parents','Avoiding peers'],'It is a key developmental task.')
H('7.C',3,'Which is a contemporary issue facing adolescents?',
  'Dating violence and peer pressure',['Pensions','Retirement planning','Property taxes'],'Sociologists study these concerns.')
H('7.C',3,'Cyberbullying is a concern for teens because it does what?',
  'Can follow them anywhere online and reach large audiences',['Occurs only at school','Is always anonymous and harmless','Cannot be reported'],'Technology expands bullying.')
H('7.D',3,'Which skill helps adolescents make responsible life choices?',
  'Evaluating consequences before acting',['Acting on impulse','Ignoring advice','Avoiding goals'],'Decision-making skills reduce risk.')
H('7.D',3,'Resisting negative peer pressure is an example of what?',
  'Assertiveness',['Conformity','Deviance','Role conflict'],'Saying no confidently protects choices.')
H('8.A',3,'Which stage of life is typically associated with establishing a career and family?',
  'Early adulthood',['Late adulthood','Childhood','Infancy'],'Many take on work and partner roles.')
H('8.A',3,'A difference between men and women in adult development historically included what?',
  'Different expectations about work and caregiving roles',['Identical expectations','No differences in society','Different alphabets'],'Gender roles shaped adult paths.')
H('8.B',3,'One way the U.S. labor force has changed in recent decades is that what?',
  'Many more women now work outside the home',['Fewer people work in services','Manufacturing employs the majority','Women are barred from work'],'Women\'s participation rose sharply.')
H('8.B',3,'The shift from manufacturing to service jobs is called what?',
  'Deindustrialization',['Urbanization','Colonization','Socialization'],'Service work has replaced factory work in many places.')
H('8.C',3,'Retirement is a major life change in late adulthood because it does what?',
  'Alters income, roles and daily routines',['Ends all social roles','Guarantees wealth','Eliminates health needs'],'Adjusting to retirement can be difficult.')
H('8.C',3,'The aging of the U.S. population places pressure on what?',
  'Social Security and health care systems',['School sports leagues only','Space programs','Weather services'],'More retirees means higher demand.')
H('9.A',3,'The functionalist perspective views deviance as what?',
  'Serving certain functions, such as clarifying social boundaries',['Always meaningless','Caused only by biology','A product of class conflict only'],'Durkheim argued deviance is normal.')
H('9.A',3,'Labeling theory, an interactionist view, says deviance results from what?',
  'Society labeling certain acts or people as deviant',['Genetic traits only','Poverty only','Lack of laws'],'The label affects self-identity.')
H('9.B',3,'Why are crime and arrest rates different across social categories?',
  'Opportunity, poverty and differential enforcement all play a role',['Rates are identical','Race alone determines crime','Gender is irrelevant to any statistic'],'Interpretation requires considering social context.')
H('9.B',3,'Which is a limitation of official crime statistics?',
  'Many crimes go unreported',['They include every crime','They show motives for all crimes','They are gathered by sociologists only'],'The "dark figure of crime" is unreported crime.')
H('9.C',3,'The main components of the U.S. criminal justice system are police, courts and what?',
  'Corrections',['Libraries','Hospitals','Schools'],'Corrections includes prisons and probation.')
H('9.C',3,'Rehabilitation as a goal of corrections aims to do what?',
  'Help offenders return to society as law-abiding people',['Punish severely only','Remove all rights','Ignore the offender'],'It contrasts with retribution.')
H('10.A',3,'A caste system is one in which status is what?',
  'Ascribed at birth and rarely changeable',['Earned by wealth','Open to everyone','Chosen at age eighteen'],'Social mobility is very limited.')
H('10.A',3,'Social mobility in a class system means what?',
  'Movement of a person up or down in social position',['Moving to another state only','Staying in one class forever','Joining a club'],'Open class systems allow it.')
H('10.B',3,'Poverty in the United States is measured partly using what?',
  'A poverty line based on income and family size',['Zip code only','Car ownership','Number of siblings'],'The government sets thresholds.')
H('10.B',3,'A long-term effect of poverty on individuals can be what?',
  'Poorer health and fewer educational opportunities',['Better health outcomes','Higher guaranteed wages','Increased social mobility for all'],'Poverty limits life chances.')
H('10.C',3,'The functionalist theory of stratification claims that inequality does what?',
  'Motivates people to fill important jobs',['Is always harmful','Has no purpose','Is caused by nature'],'Davis and Moore proposed it.')
H('10.C',3,'Conflict theorists argue that stratification does what?',
  'Benefits powerful groups at the expense of others',['Benefits everyone equally','Is natural and fair','Does not exist'],'Marx emphasized class conflict.')
H('10.D',3,'Global stratification refers to what?',
  'Unequal distribution of wealth and power among nations',['Equal wealth worldwide','Inequality within one family','Weather patterns'],'It divides high-income and low-income countries.')
H('10.D',3,'Which is a characteristic of many low-income nations?',
  'Higher infant mortality and limited access to education',['High tech exports only','Universal health care','Very high literacy everywhere'],'Inequality shapes life chances worldwide.')
H('11.A',3,'A minority group in sociology is defined by what?',
  'Having less power and facing unequal treatment, not necessarily being smaller in number',['Always being fewer than half the population','Living in cities only','Having wealth'],'Power, not numbers, is the key.')
H('11.A',3,'Ethnicity refers to what?',
  'Shared cultural heritage such as language, ancestry and traditions',['Only skin color','A legal status','Occupation'],'Race is socially defined by physical traits.')
H('11.B',3,'Prejudice differs from discrimination because prejudice is what?',
  'An attitude, while discrimination is an action',['An action, while discrimination is an attitude','A law, while discrimination is a custom','A fact, while discrimination is a belief'],'Attitude versus behavior.')
H('11.B',3,'Bias in sociology refers to what?',
  'A tendency to favor or disfavor something without fair consideration',['A scientific measurement','A law','A group'],'Bias can be conscious or unconscious.')
H('11.C',3,'One ramification of stereotyping is what?',
  'The self-fulfilling prophecy in which people act as they are expected to',['Greater understanding','Reduced prejudice','Improved opportunity'],'Expectations can shape behavior.')
H('11.C',3,'Stereotyping can harm society by doing what?',
  'Limiting opportunities and reinforcing inequality',['Eliminating differences','Ending discrimination','Increasing trust'],'It justifies unequal treatment.')
H('11.D',3,'Which describes a pattern of treatment of minority groups, in which a group is kept apart by law or custom?',
  'Segregation',['Assimilation','Pluralism','Amalgamation'],'Jim Crow laws enforced it.')
H('11.D',3,'Assimilation occurs when what happens?',
  'A minority group adopts the culture of the dominant group',['The group is expelled','The group is separated','The group is eliminated'],'Immigrants often assimilate over generations.')
H('11.E',3,'Institutional racism is best illustrated by what?',
  'Discriminatory policies built into laws or practices such as redlining',['One individual\'s rude comment','A personal belief','A private preference'],'It operates through institutions.')
H('11.E',3,'Redlining was a practice that did what?',
  'Denied loans and insurance to residents of certain neighborhoods based on race',['Increased minority homeownership','Banned segregation','Equalized school funding'],'It shaped wealth gaps.')
H('12.A',3,'Gender roles affect opportunities by doing what?',
  'Shaping expectations about careers, education and household duties',['Eliminating differences','Ending discrimination','Guaranteeing equal pay'],'Roles have limited options.')
H('12.A',3,'The "glass ceiling" refers to what?',
  'Invisible barriers that keep women and minorities from top positions',['A building material','Actual window glass','A tax policy'],'Promotion barriers are often informal.')
H('12.B',3,'An effect of an aging society is what?',
  'Increased demand for health care and retirement benefits',['Fewer retirees','Lower health spending','A younger workforce'],'Policy must adapt.')
H('12.B',3,'Ageism is what?',
  'Prejudice or discrimination based on age',['Respect for elders','A study of age','A retirement plan'],'It affects older workers.')
H('12.C',3,'Which factor often differs in health care between nations?',
  'Whether the government pays for universal coverage',['The alphabet','Time zones','Temperature'],'Systems range from private to public.')
H('12.C',3,'People in low-income countries often face what health challenge?',
  'Limited access to doctors and clean water',['Excess specialists','Universal insurance','Abundant hospitals'],'Access affects life expectancy.')
H('12.D',3,'Differences in health care in the United States are often linked to what?',
  'Income, insurance coverage and location',['Hair color','Birth order','Favorite sport'],'Access is unequal.')
H('12.D',3,'Medicare in the United States primarily serves what group?',
  'Adults ages sixty-five and older',['Children only','Active military only','All adults'],'Medicaid serves low-income people.')
H('13.A',3,'One function of the family is what?',
  'Socializing children',['Printing money','Enforcing federal law','Building highways'],'Families teach norms and values.')
H('13.A',3,'Compared with a century ago, the American family has changed in that what is true?',
  'Smaller households and more dual-income families',['Larger households only','Fewer working mothers','No single-parent homes'],'Family structures have diversified.')
H('13.B',3,'A nuclear family consists of what?',
  'Parents and their children living together',['Several generations in one house','Only siblings','A couple with no children by law'],'Extended families include other relatives.')
H('13.B',3,'Monogamy is a marriage pattern in which a person has what?',
  'One spouse at a time',['Several spouses','No spouse','Many spouses by law'],'It is the legal norm in the U.S.')
H('13.C',3,'One trend in American family life is what?',
  'Later marriage and a rise in cohabitation',['Earlier marriage','Larger families','Fewer divorces than ever'],'Americans marry later than in the past.')
H('13.C',3,'Many families today need which support because of work demands?',
  'Child care',['Fewer schools','Longer vacations','Less income'],'Dual-income households rely on it.')
H('13.D',3,'Which can disrupt family life?',
  'Divorce, death or unemployment',['A birthday','A school holiday','A vacation'],'These events change roles and finances.')
H('13.D',3,'Domestic violence harms family life by doing what?',
  'Creating fear and damaging trust and safety',['Strengthening bonds','Improving communication','Reducing conflict'],'Resources exist to help victims.')
H('14.A',3,'In a free enterprise system, what is true?',
  'Private individuals own most businesses and compete for profit',['The government owns all property','Prices are set by the state','Competition is banned'],'Socialism emphasizes public ownership.')
H('14.A',3,'Socialism as an economic system emphasizes what?',
  'Collective or government ownership of major industries',['Unlimited private ownership','No government role','Barter only'],'It aims to reduce inequality.')
H('14.B',3,'A democracy is a government in which what is true?',
  'Power rests with the people, who choose leaders in elections',['One ruler holds absolute power','A few elites rule by birth','The military controls everything'],'Legitimacy comes from consent.')
H('14.B',3,'Max Weber\'s idea of legitimate authority includes which type?',
  'Charismatic authority based on personal qualities of a leader',['Authority from force alone','Authority from wealth only','Authority from age only'],'Traditional and legal-rational are the others.')
H('14.C',3,'The right to vote in the United States has expanded over time to include what?',
  'Women, African American men and eighteen-year-olds',['Only landowners','Only men','Only the wealthy'],'Amendments extended suffrage.')
H('14.C',3,'The Nineteenth Amendment is significant because it did what?',
  'Gave women the right to vote',['Abolished slavery','Lowered the voting age','Ended poll taxes'],'Ratified in 1920.')
H('15.A',3,'The functionalist theory of education says schools do what?',
  'Transmit culture and prepare people for roles in society',['Maintain class inequality only','Are unnecessary','Create conflict only'],'Education serves society\'s needs.')
H('15.A',3,'Conflict theorists argue that education does what?',
  'Reproduces social inequality through tracking and unequal funding',['Eliminates inequality','Is always fair','Has no effect'],'Funding disparities matter.')
H('15.B',3,'A current issue in American education is what?',
  'Funding gaps between wealthy and poor school districts',['Equal funding everywhere','No standardized tests','Universal agreement on curriculum'],'Debates include testing and school choice.')
H('15.B',3,'School choice programs allow families to do what?',
  'Select schools outside their assigned district, sometimes with public funds',['Avoid all schooling','Pay no taxes','Hire teachers directly'],'Supporters and critics disagree.')
H('15.C',3,'From a sociological viewpoint, religion is studied as what?',
  'A social institution that shapes beliefs and behavior',['Only a private feeling','A scientific theory','A form of government'],'Sociologists do not judge whether beliefs are true.')
H('15.C',3,'Durkheim argued that religion does what?',
  'Strengthens social solidarity through shared rituals',['Divides every group','Has no social effects','Is purely individual'],'He saw sacred symbols as expressing society.')
H('15.D',3,'Religion serves a basic societal need by doing what?',
  'Providing meaning, community and moral guidance',['Setting tax rates','Printing money','Enforcing traffic laws'],'It supports social cohesion.')
H('15.D',3,'A rite of passage in religion marks what?',
  'A transition in a person\'s life such as a baptism or bar mitzvah',['A sporting event','A trade agreement','A tax filing'],'These rituals mark status changes.')
H('15.E',3,'A feature of religion in the United States is what?',
  'Religious freedom protected by the First Amendment and great diversity',['A single state religion','A ban on religion','Government control of churches'],'Many other nations have established religions.')
H('15.E',3,'In some countries, an established or state religion means what?',
  'The government officially supports one faith',['Total religious freedom','No religion is allowed','Religions are equal'],'The U.S. separates church and state.')
H('16.A',3,'Science became institutionalized as a result of what?',
  'Universities, funding systems and the scientific method',['Folk tradition','Religious ritual','Military draft'],'Organized research expanded.')
H('16.A',3,'One social effect of scientific institutions is what?',
  'Technological change that alters work and daily life',['No change','Fewer discoveries','Loss of education'],'Science drives social change.')
H('16.B',3,'Which was the earliest form of mass media?',
  'Print such as books and newspapers',['Television','The internet','Radio'],'Printing technology came first.')
H('16.B',3,'The internet differs from earlier mass media because it allows what?',
  'Interactive, two-way communication among users',['Only one-way messages','No audience','Only print news'],'Social media is user-generated.')
H('16.C',3,'Functionalists see mass media as serving which role?',
  'Informing, entertaining and transmitting culture',['Exploiting audiences only','Hiding information','Causing deviance only'],'Media supports social integration.')
H('16.C',3,'Conflict theorists view mass media as what?',
  'A tool used by powerful groups to promote their interests',['A neutral mirror','A tool of the poor','Always beneficial to all'],'Ownership concentration is a concern.')
H('16.D',3,'A contemporary issue in mass media is what?',
  'Misinformation spreading rapidly online',['Absence of media','Slow communication','Lack of choices'],'Media literacy helps.')
H('16.D',3,'Media concentration means that what is true?',
  'A few corporations own many media outlets',['Many small owners','No ownership','The government owns none'],'It can limit diversity of viewpoints.')
H('17.A',3,'Demography is the study of what?',
  'Population size, composition and change',['Rocks','Weather','Languages only'],'It uses births, deaths and migration.')
H('17.A',3,'The birth rate is measured as what?',
  'The number of births per 1,000 people in a year',['The number of deaths per 1,000','The number of marriages per 1,000','The number of migrants per 100'],'It is a basic demographic measure.')
H('17.B',3,'Thomas Malthus argued that what would happen?',
  'Population grows faster than food supply, leading to famine and war',['Food supply outpaces population','Population always shrinks','Technology ends hunger'],'His theory was criticized as too pessimistic.')
H('17.B',3,'The demographic transition theory describes what?',
  'A shift from high birth and death rates to low ones as societies industrialize',['Rapid population decline','Constant birth rates','Migration only'],'Population growth slows in later stages.')
H('18.A',3,'A social movement is best described as what?',
  'An organized, long-term effort to promote or resist social change',['A spontaneous crowd','A fad','A random event'],'The civil rights movement is an example.')
H('18.A',3,'A fad differs from a social movement because a fad is what?',
  'Short-lived and focused on style rather than change',['Permanent','Political','Organized by law'],'Fads fade quickly.')
H('18.B',3,'Relative deprivation theory says that social movements arise when what?',
  'People feel they have less than they deserve compared with others',['Everyone is satisfied','People have equal wealth','Government is absent'],'Perceived gaps trigger action.')
H('18.B',3,'Resource mobilization theory emphasizes that movements need what?',
  'Money, organization and leadership to succeed',['Only anger','Only luck','Only media'],'Resources determine success.')
H('18.C',3,'Which social process contributes to social change?',
  'Innovation, such as new technology',['Stagnation','Isolation','Ritual only'],'Discovery and diffusion also contribute.')
H('18.C',3,'Diffusion as a source of social change means what?',
  'The spread of cultural traits from one society to another',['Invention of new ideas','Hidden discovery','Loss of culture'],'Trade and media spread culture.')
H('19.A',3,'A strong sociological product on a current issue relies on what?',
  'Credible sources and critical analysis',['Rumor','Personal bias only','One anecdote'],'Evidence supports conclusions.')
H('19.A',3,'In a survey, a random sample is used to do what?',
  'Represent the larger population fairly',['Include only friends','Prove a belief','Avoid data'],'Random selection reduces bias.')
H('19.B',3,'In a cause-and-effect analysis, a correlation does not necessarily show what?',
  'That one variable causes the other',['That variables are related','That data exist','That a pattern exists'],'Other factors may be involved.')
H('19.B',3,'Categorizing survey responses into groups is an example of what skill?',
  'Organizing data',['Ignoring data','Altering data','Hiding data'],'It helps find patterns.')
H('19.C',3,'A percentage helps interpret sociological data by doing what?',
  'Allowing comparison of groups of different sizes',['Hiding differences','Replacing data','Showing only totals'],'Rates standardize comparisons.')
H('19.C',3,'The median of a data set is what?',
  'The middle value when numbers are ordered',['The most common value','The sum of values','The highest value'],'It is less affected by extreme incomes.')
H('20.A',3,'Using the word "norm" correctly in sociology means what?',
  'An expected standard of behavior',['A mathematical average only','A crime','A building'],'Precise terms avoid confusion.')
H('20.A',3,'Which term refers to the position a person holds in society?',
  'Status',['Role conflict','Folkway','Sanction'],'Roles are the behaviors expected of it.')
H('20.B',3,'Which sentence uses correct punctuation?',
  'Sociologists study groups, institutions and social change.',['Sociologists study groups institutions, and social change','sociologists study groups, institutions and social change','Sociologists study, groups institutions and social change.'],'Commas separate items in a series.')
H('20.B',3,'Proofreading a sociology paper helps by doing what?',
  'Catching errors in spelling and grammar',['Adding data','Changing sources','Removing evidence'],'Clear writing improves communication.')
H('20.C',3,'Turning survey results into a pie chart is an example of what?',
  'Transferring information from written or numerical form to visual form',['Collecting data','Creating bias','Ignoring evidence'],'Visuals can clarify patterns.')
H('20.C',3,'Which medium best shows changes in population over time?',
  'A line graph',['A paragraph','A list of names','A single number'],'Line graphs show trends.')
H('20.D',3,'A good oral presentation on a sociological topic includes what?',
  'Clear organization and supporting evidence',['Only opinions','Reading with no eye contact','No sources'],'Evidence builds credibility.')
H('20.D',3,'Visual aids in a presentation should do what?',
  'Support the main points clearly',['Distract the audience','Replace the speaker','Hide information'],'Keep them simple and relevant.')
H('21.A',3,'After identifying a social problem and gathering facts, a group should next do what?',
  'List and consider possible solutions',['Declare it solved','Ignore the data','Pick a random fix'],'Options come before implementation.')
H('21.A',3,'Evaluating a solution to a problem means doing what?',
  'Judging how well it worked against its goals',['Ignoring results','Starting a new problem','Hiding mistakes'],'Evaluation closes the loop.')
H('21.B',3,'A good decision-making process begins with what?',
  'Identifying a situation that requires a decision',['Announcing the choice','Evaluating results','Ignoring options'],'Define the decision first.')
H('21.B',3,'Weighing costs and benefits of each option is part of what?',
  'Decision making',['Memorization','Role conflict','Bias'],'Options are compared before choosing.')
H('21.C',3,'Which is a conflict resolution approach?',
  'Negotiation in which each side compromises',['Threats','Silent treatment','Violence'],'Compromise yields mutual agreement.')
H('21.C',3,'In a debate, a strong argument is supported by what?',
  'Evidence and logic',['Volume','Insults','Rumors'],'Persuasion relies on reasons.')

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_soc.jsonl'))

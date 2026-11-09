#!/usr/bin/env python3
"""High school United States Government (TEKS 113.44.d). Original questions."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('113.44.d.', 998, own='hs_gov.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 1 origins
H('1.A', 3, "Which idea from the Enlightenment holds that people are born with rights that government cannot take away?", "natural rights", ["divine right", "mercantilism", "manifest destiny"], "John Locke wrote about life, liberty and property.")
H('1.A', 3, "The Declaration of Independence refers to 'the laws of Nature and of Nature's God' to argue what?", "that rights come from a source higher than government", ["that kings rule by law of heredity", "that colonies must obey Parliament", "that all taxes are fair"], "Natural law justified independence.")
H('1.B', 3, "Which ancient society's republic influenced the Framers' idea of representative government?", "Rome", ["Egypt", "Persia", "China"], "Roman institutions included a senate and elected officials.")
H('1.B', 3, "The Magna Carta influenced American government by establishing what idea?", "that even the ruler is bound by law", ["that kings are divine", "that nobles have no rights", "that taxes are never needed"], "It limited royal power in 1215.")
H('1.C', 3, "Baron de Montesquieu is known for advocating what idea?", "separation of powers into branches", ["absolute monarchy", "the divine right of kings", "a state religion"], "His ideas shaped the U.S. Constitution.")
H('1.C', 3, "John Locke's writings most influenced which American document?", "the Declaration of Independence", ["the Articles of Confederation", "the Mayflower Compact", "the Northwest Ordinance"], "Jefferson echoed Locke's natural rights.")
H('1.D', 4, "James Madison is often called the 'Father of the Constitution' mainly because he did what?", "drafted the Virginia Plan and took detailed notes at the Convention", ["wrote the Declaration of Independence", "served as the first president", "led the Continental Army"], "Madison shaped the framework and recorded debates.")
H('1.E', 3, "The Great Compromise at the Constitutional Convention created what?", "a Senate with equal representation and a House based on population", ["a single-house legislature", "a king as head of state", "a weak national government"], "It resolved the large-state versus small-state dispute.")
H('1.E', 3, "The Three-Fifths Compromise determined how enslaved people were counted for what?", "representation and taxation", ["voting rights", "citizenship", "military draft"], "It was a deeply unjust compromise between North and South.")
H('1.E', 3, "Federalists and Anti-Federalists disagreed mainly over what?", "how strong the national government should be", ["whether to have a flag", "which city should be the capital", "whether to fight England"], "Anti-Federalists feared concentrated power and wanted a bill of rights.")
H('1.F', 3, "Which individual is the author of the Declaration of Independence?", "Thomas Jefferson", ["Alexander Hamilton", "John Adams", "George Washington"], "Jefferson drafted it in 1776.")
H('1.F', 3, "Alexander Hamilton, James Madison and John Jay wrote what?", "the Federalist Papers", ["the Articles of Confederation", "the Bill of Rights", "the Declaration of Independence"], "They urged ratification of the Constitution.")

# 2 political change
H('2.A', 3, "Which method do interest groups commonly use to influence government?", "lobbying lawmakers", ["printing money", "declaring war", "appointing judges"], "Lobbying presents information and pressure to officials.")
H('2.A', 3, "Political parties try to gain power in government mainly by doing what?", "nominating candidates and winning elections", ["writing laws without voting", "appointing judges directly", "ignoring voters"], "Parties compete for votes.")
H('2.B', 3, "Which movement used marches and protests to push for the Civil Rights Act of 1964?", "the civil rights movement", ["the temperance movement", "the labor movement", "the Prohibition movement"], "Citizen action led to legal change.")

# 3 voting and districts
H('3.A', 3, "After each census, states with growing populations may do what?", "gain seats in the House of Representatives", ["lose Senate seats", "gain more senators", "elect more presidents"], "House seats are apportioned by population.")
H('3.A', 3, "How often does the U.S. Census occur?", "every 10 years", ["every 2 years", "every 4 years", "every 25 years"], "The Constitution requires a census each decade.")
H('3.B', 3, "Studying a map of congressional districts can help someone infer what?", "how voters are distributed", ["next year's weather", "the price of gas", "the age of the Constitution"], "Maps reveal political patterns.")
H('3.C', 3, "Drawing district lines to favor one party is called what?", "gerrymandering", ["filibustering", "lobbying", "impeaching"], "It can dilute voters' influence.")
H('3.C', 4, "Which Supreme Court principle requires districts to be roughly equal in population?", "one person, one vote", ["separate but equal", "clear and present danger", "judicial review"], "Cases such as Reynolds v. Sims established it.")

# 4 economy
H('4.A', 3, "Fiscal policy involves which government actions?", "taxing and spending", ["printing stamps", "choosing judges", "declaring war"], "Congress and the president set fiscal policy.")
H('4.A', 3, "Monetary policy is mainly managed by which institution?", "the Federal Reserve", ["the Supreme Court", "the Senate", "the Department of Defense"], "The Fed controls the money supply and interest rates.")
H('4.B', 3, "In the U.S. free enterprise system, the role of government is mainly to do what?", "protect property rights and regulate unfair practices", ["own all businesses", "set all prices", "decide what each person makes"], "Markets are mostly private.")
H('4.C', 3, "Raising taxes on businesses can cause what economic effect?", "less money available for investment or hiring", ["higher profits for everyone", "no effect ever", "lower prices always"], "Taxes affect business decisions.")
H('4.C', 3, "A regulation requiring factories to limit pollution is an example of what?", "government regulation of business", ["monetary policy", "a tariff", "a subsidy"], "Regulation protects public health.")

# 5 foreign policy
H('5.A', 3, "Why does the U.S. pay close attention to oil-producing regions in its foreign policy?", "energy resources are vital to the economy", ["oil is not important", "oil is only used for art", "it has no oil"], "Resources shape national interests.")
H('5.B', 3, "Who has the power to negotiate treaties?", "the president", ["the Supreme Court", "the Senate", "the House of Representatives"], "The president negotiates; the Senate approves.")
H('5.B', 3, "How many Senators must approve a treaty for it to take effect?", "two-thirds", ["a simple majority", "three-fourths", "all of them"], "The Constitution requires a two-thirds vote.")
H('5.B', 3, "Only Congress has the power to do what regarding war?", "declare war", ["command the troops", "negotiate peace", "appoint ambassadors"], "The president is commander in chief.")

# 6 constitution
H('6.A', 3, "A written constitution is important because it does what?", "sets clear rules and limits for government", ["makes laws change daily", "gives power to one ruler", "keeps rules secret"], "It provides stability and accountability.")
H('6.B', 3, "The Preamble states that one purpose of the Constitution is to 'establish justice.' Which institution mainly serves that purpose?", "the courts", ["the army", "the post office", "the cabinet"], "Justice is administered by the judicial system.")
H('6.B', 3, "The Preamble begins with the words 'We the People' to show what?", "that government gets its power from the people", ["that kings rule", "that states are above people", "that judges rule"], "It expresses popular sovereignty.")
H('6.C', 3, "Federalist No. 10 by James Madison warns about the dangers of what?", "factions", ["standing armies", "foreign trade", "state flags"], "A large republic can control factions.")
H('6.C', 3, "Federalist No. 51 argues that ambition must counteract ambition through what?", "checks and balances among branches", ["a single branch of power", "state control of all laws", "a powerful monarch"], "It explains separation of powers.")
H('6.D', 3, "Republicanism means that government power comes from what?", "elected representatives chosen by the people", ["inherited position", "military rule", "wealth only"], "Representatives act on behalf of citizens.")
H('6.D', 3, "Which principle limits government by dividing power among branches and levels?", "limited government", ["unlimited power", "absolute rule", "military rule"], "The Constitution restrains government.")
H('6.E', 3, "How many states must ratify a constitutional amendment for it to take effect?", "three-fourths", ["one-half", "two-thirds", "all of them"], "Amendment needs broad agreement.")
H('6.E', 3, "A proposed amendment must first be passed by what?", "two-thirds of both houses of Congress", ["a simple majority of the Senate", "the president only", "the Supreme Court"], "Or by a convention called by two-thirds of the states.")
H('6.F', 3, "The Declaration of Independence continues to shape American government by doing what?", "affirming that governments exist to protect individual rights", ["establishing a king", "creating the Senate", "setting tax rates"], "Its principles guide political debate.")

# 7 branches
H('7.A', 3, "The legislative branch of the U.S. government is called what?", "Congress", ["the Cabinet", "the Supreme Court", "the Electoral College"], "It makes federal laws.")
H('7.A', 3, "Which chamber of Congress has 100 members?", "the Senate", ["the House of Representatives", "the Cabinet", "the Supreme Court"], "Each state has two senators.")
H('7.A', 3, "Which chamber has the sole power to begin impeachment?", "the House of Representatives", ["the Senate", "the Supreme Court", "the Cabinet"], "The Senate holds the trial.")
H('7.A', 3, "Revenue bills must begin in which chamber?", "the House of Representatives", ["the Senate", "the Supreme Court", "the White House"], "The House is closest to the people.")
H('7.B', 3, "The president serves as head of state and what else?", "commander in chief of the armed forces", ["chief justice", "Speaker of the House", "leader of the Senate"], "The president directs the military.")
H('7.B', 3, "A president can serve a maximum of how many elected terms?", "two", ["one", "three", "four"], "The 22nd Amendment set the limit.")
H('7.B', 3, "Which official is president of the Senate and casts tie-breaking votes?", "the vice president", ["the Speaker of the House", "the chief justice", "the attorney general"], "The vice president votes only in ties.")
H('7.C', 3, "The Supreme Court has how many justices?", "nine", ["seven", "eleven", "twelve"], "The number is set by law.")
H('7.C', 3, "Judicial review, the power to declare laws unconstitutional, was established in which case?", "Marbury v. Madison", ["Plessy v. Ferguson", "Brown v. Board of Education", "Gideon v. Wainwright"], "Chief Justice Marshall wrote the 1803 decision.")
H('7.C', 3, "Federal judges are appointed by the president and approved by whom?", "the Senate", ["the House", "the Supreme Court", "the voters"], "They serve during good behavior.")
H('7.D', 3, "What is the main purpose of the National Aeronautics and Space Administration (NASA)?", "space exploration and research", ["collecting taxes", "running elections", "defending borders"], "It is an independent executive agency.")
H('7.D', 3, "The Environmental Protection Agency (EPA) was created to do what?", "enforce environmental laws", ["print money", "supervise elections", "inspect airplanes"], "It protects air and water.")
H('7.D', 3, "The Federal Reserve is mainly responsible for what?", "regulating the money supply", ["regulating the airlines", "collecting taxes", "enforcing laws"], "It sets monetary policy.")
H('7.E', 3, "The president's veto power is an example of what?", "a check on the legislative branch", ["a check on the states", "a check on the people", "a check on the courts"], "Congress can override with two-thirds.")
H('7.E', 3, "How can Congress override a presidential veto?", "by a two-thirds vote in both houses", ["by a simple majority in one house", "by the Supreme Court's approval", "by a state vote"], "It requires broad support.")
H('7.E', 3, "The Senate's power to confirm judges is an example of what?", "a check on the executive branch", ["a check on the states", "a check on voters", "a check on the press"], "Checks and balances limit each branch.")
H('7.F', 4, "Judicial activism refers to judges doing what?", "using their rulings to shape policy beyond a strict reading of law", ["refusing to decide cases", "always following precedent exactly", "never issuing opinions"], "Restraint favors deference to legislatures.")
H('7.F', 4, "Judicial restraint holds that courts should do what?", "defer to elected branches and precedent", ["create new policy", "overturn most laws", "ignore the Constitution"], "Restraint limits judicial power.")
H('7.G', 3, "Which is a responsibility of the federal government?", "national defense", ["running local schools", "issuing driver's licenses", "paving city streets"], "Defense and foreign policy are national.")
H('7.G', 3, "Printing money and regulating interstate commerce are powers of whom?", "the federal government", ["city governments", "school boards", "county governments"], "These are delegated to Congress.")
H('7.H', 3, "Which level of government typically runs public schools directly?", "local school districts", ["the Department of Defense", "the Supreme Court", "Congress"], "States set rules; districts operate schools.")
H('7.H', 3, "Which official leads a state government?", "the governor", ["the mayor", "the president", "the senator"], "Governors are the chief executives of states.")

# 8 federalism
H('8.A', 3, "Federalism is a system in which what happens?", "power is divided between national and state governments", ["all power rests in the national government", "all power rests with states", "power is held by a monarch"], "It was created to balance power.")
H('8.A', 3, "The Articles of Confederation were replaced because they did what?", "created a national government that was too weak", ["created a king", "were too long", "were written by Britain"], "It could not tax or regulate trade.")
H('8.B', 3, "Coining money is a power given to whom?", "the national government", ["states only", "cities only", "counties only"], "It is an exclusive federal power.")
H('8.B', 3, "Which power is shared by national and state governments?", "taxing and building roads", ["declaring war", "coining money", "making treaties"], "Concurrent powers are held by both.")
H('8.B', 3, "Establishing local governments and public schools is generally a power of whom?", "the states", ["Congress", "the president", "foreign nations"], "Reserved powers belong to the states.")
H('8.C', 3, "The Tenth Amendment says that powers not given to the national government are reserved to whom?", "the states or the people", ["the president", "the courts", "foreign nations"], "It supports states' rights.")
H('8.C', 4, "Which conflict illustrates a dispute over states' rights versus national authority?", "the Civil War", ["the Spanish-American War", "World War I", "the Cold War"], "Secession was challenged by the Union.")
H('8.D', 3, "The Constitution limits state power by saying what?", "federal law is supreme over conflicting state law", ["states can overrule federal law", "states can coin money", "states may declare war"], "The Supremacy Clause settles conflicts.")
H('8.D', 3, "Which of these can neither a state nor the national government do?", "pass an ex post facto law", ["collect taxes", "build roads", "establish schools"], "Both are banned from punishing acts retroactively.")

# 9 elections
H('9.A', 3, "Which method fills a public office by selection by someone in authority?", "appointment", ["election", "referendum", "recall"], "The president appoints cabinet members.")
H('9.A', 3, "Federal judges are filled through which method?", "appointment", ["direct popular election", "lottery", "hereditary succession"], "The president nominates; the Senate confirms.")
H('9.B', 3, "The Electoral College has how many electors in total?", "538", ["435", "270", "100"], "A candidate needs 270 to win.")
H('9.B', 4, "A candidate wins the presidency by winning at least how many electoral votes?", "270", ["218", "300", "538"], "That is a majority of 538.")
H('9.B', 3, "In most states, all electoral votes go to whom?", "the candidate who wins the state's popular vote", ["the loser", "the House Speaker", "the Supreme Court"], "Most states use winner-take-all.")
H('9.C', 3, "The 17th Amendment changed how senators are chosen. How are they selected now?", "by direct popular vote", ["by state legislatures", "by the president", "by the Supreme Court"], "Before 1913, legislatures chose them.")

# 10 parties
H('10.A', 3, "Which is a function of political parties?", "recruiting and nominating candidates", ["writing court decisions", "printing money", "enforcing laws"], "Parties organize campaigns.")
H('10.A', 3, "A primary election is held to do what?", "choose a party's candidate for the general election", ["elect the final winner", "appoint judges", "set taxes"], "Parties use primaries and caucuses.")
H('10.B', 3, "The United States has a two-party system, dominated by which two parties?", "Democrats and Republicans", ["Federalists and Whigs", "Socialists and Greens", "Libertarians and Reform"], "Single-member districts favor two parties.")
H('10.B', 4, "A role of third parties in U.S. elections is often to do what?", "raise issues that major parties later adopt", ["win most seats", "control the Senate", "choose Supreme Court justices"], "They influence debate.")

# 11 comparative
H('11.A', 3, "A constitutional republic differs from an absolute monarchy because it does what?", "limits power by law and elects representatives", ["gives power to a king", "ends elections", "abolishes courts"], "Law and representation constrain rulers.")
H('11.A', 3, "In a totalitarian state, which statement is true?", "the government controls nearly all aspects of life", ["citizens elect all leaders freely", "courts are independent", "the press is free"], "Compare with limited government.")
H('11.B', 4, "A presidential system differs from a parliamentary system because in a presidential system the executive is what?", "separately elected and independent of the legislature", ["chosen by the legislature", "a monarch", "appointed by the courts"], "In parliamentary systems the legislature selects the prime minister.")
H('11.B', 4, "A potential disadvantage of presidential systems is what?", "gridlock when president and legislature are of different parties", ["too much unity", "frequent no-confidence votes", "no checks on power"], "Divided government can slow action.")

# 12 rights
H('12.A', 3, "How does limited government help protect individual rights?", "it restricts officials to powers granted by law", ["it gives officials unlimited power", "it removes all laws", "it ends the courts"], "The rule of law and limits on power guard against abuse.")
H('12.B', 3, "The Declaration of Independence names which three unalienable rights?", "life, liberty and the pursuit of happiness", ["speech, press and religion", "voting, jury and bearing arms", "property, taxes and trade"], "Unalienable means they cannot be taken away.")
H('12.C', 3, "The First Amendment protects which freedoms?", "religion, speech, press, assembly and petition", ["voting, jury and counsel", "bearing arms and quartering", "bail and due process"], "These five freedoms are in the First Amendment.")
H('12.C', 3, "The Fourth Amendment protects against what?", "unreasonable searches and seizures", ["double jeopardy", "cruel punishment", "quartering of soldiers"], "Warrants require probable cause.")
H('12.C', 3, "The Fifth Amendment includes protection against what?", "being forced to testify against yourself", ["unreasonable searches", "excessive bail", "cruel punishment"], "It also protects due process and bans double jeopardy.")
H('12.C', 3, "The Sixth Amendment guarantees what?", "a speedy and public trial by jury and the right to counsel", ["freedom of religion", "protection from quartering", "the right to bear arms"], "It protects the accused.")
H('12.C', 3, "The Eighth Amendment prohibits what?", "cruel and unusual punishments", ["unreasonable searches", "self-incrimination", "quartering of troops"], "It also bans excessive bail and fines.")
H('12.C', 3, "The Second Amendment concerns what right?", "the right to keep and bear arms", ["freedom of speech", "the right to a jury", "freedom of the press"], "It has been interpreted by the Supreme Court.")
H('12.D', 3, "The Founders protected religious freedom partly because many colonists had what experience?", "fled religious persecution in Europe", ["worshipped only one faith", "ruled by a state religion in America", "were all the same denomination"], "Many settlers sought freedom of conscience.")
H('12.E', 3, "In Tinker v. Des Moines, the Court held that students have what right?", "to symbolic speech at school unless it disrupts learning", ["no speech rights at school", "unlimited speech anywhere", "to disobey teachers"], "The Court protected black armbands worn in protest.")
H('12.E', 3, "In Gideon v. Wainwright, the Court ruled that states must do what?", "provide a lawyer for defendants who cannot afford one", ["end the death penalty", "allow school prayer", "abolish segregation"], "It extended the Sixth Amendment right to counsel.")
H('12.E', 3, "Brown v. Board of Education (1954) declared what unconstitutional?", "racial segregation in public schools", ["school prayer", "flag salutes", "loyalty oaths"], "It overturned the 'separate but equal' idea in schools.")
H('12.F', 3, "Due process of law means that government must do what?", "follow fair procedures before taking life, liberty or property", ["punish quickly", "act in secret", "ignore evidence"], "It appears in the Fifth and Fourteenth Amendments.")
H('12.F', 3, "The Miranda warning informs suspects of what?", "their right to remain silent and to an attorney", ["the charges against others", "the judge's name", "the trial date"], "Miranda v. Arizona required it.")

# 13 citizenship
H('13.A', 3, "Serving on a jury is an example of what?", "a duty that may require personal sacrifice for the common good", ["an optional hobby", "a way to avoid taxes", "a privilege only for the wealthy"], "Citizens set aside personal time for justice.")
H('13.A', 3, "Paying taxes is an example of what?", "a civic obligation", ["an optional gift", "a right only for citizens", "a punishment"], "Taxes fund public services.")
H('13.B', 3, "Which is a duty of citizens?", "obeying laws", ["voting", "running for office", "attending rallies"], "Laws must be obeyed by all.")
H('13.B', 3, "Which is a responsibility rather than a legal duty?", "voting", ["paying taxes", "obeying laws", "serving on a jury"], "Voting is voluntary.")
H('13.C', 3, "To vote in a U.S. election, a person must be at least how old?", "18", ["16", "21", "25"], "The 26th Amendment set the voting age.")
H('13.C', 3, "A person must be a U.S. citizen and what else to vote?", "registered to vote", ["a property owner", "a college graduate", "a taxpayer only"], "Most states require registration before voting.")

# 14 participation
H('14.A', 3, "Which is an effective method of political participation?", "contacting elected officials", ["ignoring elections", "avoiding the news", "hiding opinions"], "Citizens have many ways to engage.")
H('14.A', 3, "A petition is used to do what?", "ask government to take an action", ["ban newspapers", "declare war", "rewrite the Constitution"], "The First Amendment protects it.")
H('14.B', 3, "The women's suffrage movement worked to win what?", "the right of women to vote", ["an eight-hour workday", "an end to child labor", "free public schools"], "The 19th Amendment passed in 1920.")
H('14.B', 3, "The Montgomery bus boycott (1955-56) was an example of what?", "a citizen movement using nonviolent protest", ["a military coup", "a violent revolt", "a government program"], "It helped launch the modern civil rights movement.")
H('14.C', 3, "Which factor most influences a person's political attitudes?", "family and peers", ["the tides", "the length of day", "the number of planets"], "Socialization shapes views.")
H('14.C', 3, "The media influence political attitudes by doing what?", "shaping what issues people see and how they see them", ["writing laws", "enforcing laws", "counting votes"], "News coverage frames issues.")

# 15 points of view
H('15.A', 3, "An interest group is organized to do what?", "influence government policy on specific issues", ["nominate presidents", "decide court cases", "run schools"], "Examples include the NRA and AARP.")
H('15.A', 3, "Political action committees (PACs) raise money to do what?", "support candidates or causes", ["enforce laws", "count votes", "draw district lines"], "Their spending is regulated.")
H('15.B', 3, "The right of petition allows citizens to do what?", "ask government to correct grievances", ["break any law", "avoid taxes", "ignore courts"], "It is part of the First Amendment.")
H('15.B', 3, "Which kind of speech is NOT protected by the First Amendment?", "speech that incites imminent lawless action", ["unpopular political opinions", "criticism of the government", "peaceful protest"], "The Court allows limits on dangerous speech.")

# 16 policies and culture
H('16.A', 3, "The Civil Rights Act of 1964 banned what?", "discrimination based on race, color, religion, sex or national origin", ["private clubs", "voting by mail", "public schools"], "It outlawed segregation in public places.")
H('16.A', 3, "The Voting Rights Act of 1965 aimed to do what?", "end discriminatory practices that kept citizens from voting", ["lower the voting age", "limit campaign spending", "create the Electoral College"], "It targeted literacy tests and other barriers.")
H('16.B', 3, "The Americans with Disabilities Act of 1990 prohibits what?", "discrimination against people with disabilities", ["all disability benefits", "private school", "voting by mail"], "It requires accessibility.")
H('16.B', 3, "The 26th Amendment changed American politics by doing what?", "lowering the voting age to 18", ["giving women the vote", "ending poll taxes", "creating term limits"], "It passed in 1971.")

# 17 free enterprise, patents
H('17.A', 3, "A patent protects an inventor by doing what?", "giving the exclusive right to make and sell the invention for a period", ["banning new inventions", "making inventions free", "ending competition"], "The Constitution authorizes patents to promote progress.")
H('17.A', 3, "The Constitution allows Congress to grant patents and copyrights to do what?", "promote science and the useful arts", ["limit all ideas", "control newspapers", "tax inventors only"], "Intellectual property fosters innovation.")
H('17.B', 3, "The Internet began as a government project funded by which agency?", "ARPA (a Defense Department research agency)", ["NASA", "the Postal Service", "the Treasury"], "ARPANET became the basis of the Internet.")
H('17.B', 3, "GPS technology was developed with government support for what use?", "military navigation, later shared with private industry", ["farm subsidies", "education", "city planning only"], "Public research can yield private benefits.")

# 18 technology
H('18.A', 3, "Advances in biotechnology raise policy questions about what?", "ethics, safety and regulation", ["only weather", "only sports", "only fashion"], "Government must balance innovation and risk.")
H('18.A', 3, "Government regulation of drones is an example of what?", "adapting laws to new technology", ["ending technology", "repealing the Constitution", "banning all travel"], "New tools prompt new rules.")
H('18.B', 3, "How has the Internet changed political campaigns?", "it allows candidates to reach voters and raise money quickly", ["it banned campaigns", "it ended voting", "it ended debates"], "Digital media is central to campaigns.")
H('18.B', 3, "A risk of social media in politics is what?", "the rapid spread of misinformation", ["fewer opinions", "no engagement", "no communication"], "Citizens must evaluate sources.")

# 19 skills
H('19.A', 3, "Putting the steps of a bill becoming a law in order is an example of what?", "sequencing information", ["averaging data", "ignoring causes", "memorizing dates"], "Analysis includes sequencing.")
H('19.B', 3, "A good product on a government issue should be based on what?", "credible evidence and clear reasoning", ["rumors", "one opinion", "unsourced posts"], "Critical methods strengthen products.")
H('19.C', 3, "To defend a point of view on a political issue, a student should do what?", "support it with evidence and address counterarguments", ["shout louder", "ignore other views", "use no facts"], "Strong arguments consider opposing views.")
H('19.D', 3, "To judge a source's validity, a student should ask what?", "who wrote it, why, and what evidence it uses", ["how long it is", "what color it is", "how many ads it has"], "Credibility depends on the author and evidence.")
H('19.D', 3, "A source that clearly favors one side is said to show what?", "bias", ["objectivity", "neutrality", "fact"], "Bias shapes how information is presented.")
H('19.E', 3, "A bar graph of voter turnout by age group helps show what?", "which groups vote at higher or lower rates", ["the weather", "the date of elections", "the number of senators"], "Charts help evaluate government data.")
H('19.F', 3, "A claim in a civics essay should be supported by what?", "evidence and reasoning", ["opinions only", "assumptions", "guesses"], "Evidence supports claims.")

# 20 communication
H('20.A', 3, "Using the term 'bicameral' correctly describes what kind of legislature?", "one with two chambers", ["one with one chamber", "one led by a king", "one without elections"], "Congress is bicameral.")
H('20.A', 3, "A 'bill' is best defined as what?", "a proposed law", ["a court order", "a tax return", "an election result"], "A bill must pass both houses.")
H('20.B', 3, "An effective presentation about a government issue should include what?", "a clear thesis, evidence and a logical order", ["no sources", "only pictures", "only opinions"], "Organization and evidence make it effective.")
H('20.C', 3, "Civil discourse in a political discussion means what?", "respectful exchange of ideas supported by evidence", ["insulting those who disagree", "refusing to listen", "spreading rumors"], "Respect and evidence guide discussion.")

# 21 democracy
H('21.A', 3, "A caucus is a meeting in which what happens?", "party members gather to choose candidates or delegates", ["a jury hears a case", "a bill is signed", "a treaty is approved"], "Some states use caucuses instead of primaries.")
H('21.A', 3, "A jury trial is an example of what democratic process?", "citizens taking part in justice", ["a vote for president", "a primary election", "a tax audit"], "Jurors decide cases.")
H('21.B', 3, "A class has defined a local civic problem and collected facts. What should they do before choosing a solution?", "list and weigh the possible options", ["ignore the facts they collected", "wait for someone else to decide", "end the project"], "Evaluate options before choosing.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_gov.jsonl'))

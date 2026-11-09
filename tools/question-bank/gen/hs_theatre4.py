import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.318.', 1031, own='hs_theatre4.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',3,"A senior invents a new warm-up sequence for the company, then leads it before each tech rehearsal. She is doing what?",
  "Creating and demonstrating preparation techniques",["Auditing the budget","Painting a drop","Counting house seats"],"Leaders design and model warm-ups.")
H('c.1.A',3,"What should a well-designed company warm-up include?",
  "Physical, vocal and focus components",["Only a snack","Only a lecture","Only a costume fitting"],"Complete warm-ups prepare body, voice and mind.")
H('c.1.B',4,"A student choreographs a crowd transition in which twelve actors cross the stage in layered tempos, then teaches it to the cast. She is doing what?",
  "Devising and modeling stage movement",["Selling ads","Writing a review","Editing film"],"Devising creates the movement; modeling teaches it.")
H('c.1.B',4,"Which skill is essential for modeling a movement sequence for others?",
  "Clear demonstration and precise cues",["Silence","Vague gestures","Random changes"],"Models must be clear and repeatable.")
H('c.1.C',3,"A mentor actor shows a younger cast member how breath, inflection and clean consonants carry meaning. She is doing what?",
  "Modeling proper vocal techniques",["Hiding technique","Reading a review","Setting light cues"],"Modeling teaches technique by example.")
H('c.1.C',3,"Which change in inflection signals a question?",
  "A rising pitch at the end of the sentence",["A steady monotone","A dropped whisper only","A loud shout"],"Rising pitch often marks questions.")
H('c.1.D',4,"A student charts how a three-act play builds tension and how a one-hour TV episode places commercial breaks. She is comparing what?",
  "The structure of theatre with that of television",["Costume fabrics","Ticket stubs","Parking lots"],"Structures differ across media.")
H('c.1.D',4,"Which structural difference separates film from live theatre?",
  "Scenes can be assembled through editing rather than played continuously",["Actors never rehearse","There is no script","There are no characters"],"Editing is a film structure tool.")
H('c.1.E',4,"A student explains that Restoration comedy used asides and elaborate speech that audiences of that era expected. She is evaluating what?",
  "Theatrical conventions of a particular period",["Parking rules","Modern emojis","Lobby snacks"],"Conventions vary by period.")
H('c.1.E',4,"Which convention is associated with Greek tragedy?",
  "A chorus commenting on the action",["A realistic living room set","Film close-ups","A fourth wall"],"The chorus is a Greek convention.")
H('c.1.F',4,"A director realizes that changing the set's color has forced her to revise lighting, costume and makeup. She has evaluated what?",
  "The interdependence of all theatrical elements",["A scheduling error","A budget memo","A seating chart"],"Elements depend on each other.")
H('c.1.F',4,"Why do directors hold design meetings before rehearsals begin?",
  "To align all elements with one unified concept",["To lengthen the season","To avoid decisions","To cut actors"],"Alignment preserves unity.")
H('c.1.G',3,"A veteran actor teaches the cast to memorize by linking lines to physical actions and objectives. She is doing what?",
  "Modeling memorization skills",["Skipping lines","Ignoring scripts","Reading reviews"],"Modeling shares effective methods.")
H('c.1.G',3,"Which approach reinforces memory most effectively before opening night?",
  "Frequent short runs of lines with action",["One long cram","Skipping rehearsals","Ignoring cues"],"Spaced practice with action works best.")
H('c.2.A',3,"A lead actor invites the director to coordinate a safe way to perform a falling moment, including mats and spotters. She is modeling what?",
  "Safe, appropriate techniques for physical expression",["Careless risk","Showing off","Silence"],"Modeling safe practice sets a standard.")
H('c.2.A',3,"A company leader encourages members to name their limits before an emotional scene. This models what?",
  "Safe emotional expression",["Ignoring feelings","Forcing the scene","Cutting rehearsal"],"Naming limits supports safe expression.")
H('c.2.B',4,"A student ensemble member deliberately changes her pacing to reveal a character's hesitation and sees the audience grow quiet. She is demonstrating what?",
  "Creativity and its effect on an audience",["Boredom","Stage fright","Late arrival"],"Creative choices shape audience response.")
H('c.2.B',4,"What shows that a creative choice affected the audience?",
  "A visible shift in their attention or reaction",["Ticket price","Seat color","Program length"],"Reaction shows effect.")
H('c.2.C',4,"A student analyzes a character in a Brechtian epic play and a character in a realistic drama, then explains how each should be played. She is doing what?",
  "Analyzing and interpreting characters from various genres and styles",["Reading a menu","Listing props only","Cutting scenes"],"Interpretation depends on style.")
H('c.2.C',4,"How might an actor adapt physicality between farce and naturalism?",
  "Larger, faster gestures in farce and subtler behavior in naturalism",["Identical movement","No gestures at all","Only stillness"],"Style shapes physicality.")
H('c.2.D',4,"An actor studies a Chekhov scene's subtext and plays the unspoken tension while delivering polite lines. She is doing what?",
  "Interpreting a scripted scene to portray believable characters",["Ignoring the script","Improvising something else","Reading a review"],"Subtext supports believability.")
H('c.2.D',4,"Which choice adds believability in a stylized scripted scene?",
  "Committing to the style while grounding the character's goals",["Playing it as a joke","Ignoring the style","Dropping the script"],"Commitment plus motivation.")
H('c.2.E',4,"A playwriting team draws a set of scenarios from a local oral-history project and drafts an original script. They are doing what?",
  "Creating imaginative scripts and scenarios collaboratively",["Reciting a classic","Sewing costumes","Selling ads"],"Original scripts can be devised together.")
H('c.2.E',4,"What does a strong original scenario need?",
  "Clear characters, conflict and stakes",["Random events","No structure","Only description"],"Conflict drives scenarios.")
H('c.3.A',3,"A student designs a lighting look for an improvised scene, testing angles and intensity for safety and effect. She is doing what?",
  "Experimenting with technical elements safely and effectively",["Ignoring risk","Skipping tech","Breaking equipment"],"Safe experimentation informs design.")
H('c.3.A',3,"Which habit reflects safe experimentation with theatrical technology?",
  "Testing a new effect on a small scale first",["Plugging in everything at once","Skipping power checks","Blocking exits"],"Small-scale tests reduce risk.")
H('c.3.B',4,"A student reads a script closely, marks character wants and directs a three-minute scene from it. She is doing what?",
  "Analyzing and evaluating a dramatic text and directing a brief scene",["Selling tickets","Sewing a costume","Operating sound"],"Analysis leads to directing choices.")
H('c.3.B',4,"What is a first step in directing a brief scene?",
  "Identify each character's objective and the scene's turning point",["Order costumes","Print programs","Count seats"],"Objectives and turning points guide the staging.")
H('c.3.C',4,"A director avoids changing the playwright's central message while updating the setting. She is honoring what?",
  "Her responsibility to the author's intent",["The ticket price","The seating plan","A prop list"],"Directors serve the text.")
H('c.3.C',4,"A director's responsibility to the author includes what?",
  "Respecting the script and the playwright's purpose",["Rewriting without regard","Ignoring the text","Replacing the story"],"Fidelity to intent matters.")
H('c.3.D',4,"A student reviews a production plan including research notes, rehearsal schedule, technical designs and blocking. She is doing what?",
  "Analyzing production plans",["Painting scenery","Auditioning","Selling tickets"],"Plans coordinate all elements.")
H('c.3.D',4,"Why is a rehearsal schedule an important part of a production plan?",
  "It allocates time for each scene and technical element",["It decorates the lobby","It sells seats","It writes lines"],"Scheduling organizes the work.")
H('c.3.E',4,"A student casts a one-act, directs rehearsals and produces a performance for the school. She is demonstrating what?",
  "Leadership",["Avoidance","Isolation","Procrastination"],"Leading a production shows leadership.")
H('c.3.E',4,"Which responsibility belongs to a producer?",
  "Managing budget, schedule and resources",["Writing lyrics","Playing the lead","Running the lights alone"],"Producers coordinate resources.")
H('c.3.F',4,"A student devotes herself to becoming an expert in scenic design, taking on larger projects with discipline. She is applying what?",
  "Expertise in a production area with responsibility",["Disorder","Avoidance","Casual interest only"],"Expertise requires commitment.")
H('c.3.F',4,"Which demonstrates professional-level artistic discipline?",
  "Preparing thoroughly and following through on commitments",["Arriving unprepared","Missing deadlines","Avoiding feedback"],"Discipline is reliability.")
H('c.4.A',4,"A student evaluates how the Great Migration influenced African American theatre in northern cities. She is evaluating what?",
  "Historical and cultural influences on theatre",["Ticket revenue","Seat styles","Lighting gels"],"Social history shapes drama.")
H('c.4.A',4,"Evaluating the impact of the printing press on drama involves considering what?",
  "How wider access to scripts changed theatre",["Costume sizes","Set weight","Ticket booths"],"Printing spread plays.")
H('c.4.B',3,"A student shows how theatrical storytelling appears in advertising, news and video games. She is analyzing what?",
  "Theatre's role in daily life and its influence on other media",["Seating plans","Staging risks","Box office rules"],"Theatrical ideas permeate media.")
H('c.4.B',3,"Which example shows daily-life use of theatre skills?",
  "A manager using presentation skills in a meeting",["An empty theatre","A broken light","A closed stage"],"Skills carry over.")
H('c.4.C',4,"A student stages a scene live, records it, edits the recording and analyzes how each context shapes meaning. She is employing and evaluating what?",
  "Live theatre and film in contrasting contexts",["Parking","Merchandise","Ticket sales"],"Contrast shows differing impact.")
H('c.4.C',4,"What is a unique strength of live theatre compared with film?",
  "Shared real-time presence between actors and audience",["Retakes","Post-production","Camera angles"],"Live presence is distinctive.")
H('c.4.D',4,"A student researches how Brecht's epic theatre influenced political theatre worldwide. She is researching what?",
  "Influences of world drama and its key figures",["Parking policy","Costume prices","Lobby design"],"World drama shapes practice.")
H('c.4.D',4,"Which dramatist wrote A Doll's House?",
  "Henrik Ibsen",["Samuel Beckett","Sophocles","Anton Chekhov"],"Ibsen wrote A Doll's House.")
H('c.4.E',4,"A student researches Asian American theatre companies and their impact on U.S. stages. She is researching what?",
  "The multicultural heritage of drama in the United States",["Ancient Rome","One genre only","Costume cost"],"U.S. theatre includes diverse companies.")
H('c.4.E',4,"Which playwright is known for Fences?",
  "August Wilson",["Edward Albee","Eugene O'Neill","Neil Simon"],"Wilson wrote Fences.")
H('c.4.F',4,"The Group Theatre of the 1930s brought new acting approaches to American stages. This is an example of what?",
  "A U.S. innovation in the performing arts",["A film technique","An ancient ritual","A European tradition only"],"The Group Theatre advanced American acting.")
H('c.4.F',4,"Which technique was popularized in the U.S. by Lee Strasberg and the Actors Studio?",
  "Method acting",["Commedia lazzi","Noh mask work","Kabuki kata"],"The Actors Studio promoted Method acting.")
H('c.5.A',3,"A student evaluates audience behavior at an outdoor festival, a formal play and a school assembly, then practices behavior suited to each. She is doing what?",
  "Evaluating and practicing appropriate audience behavior",["Ignoring context","Acting disrespectfully","Avoiding events"],"Etiquette varies by setting.")
H('c.5.A',3,"Why does audience behavior matter to performers?",
  "It affects the energy and focus of the show",["It changes the script","It sets ticket prices","It moves the stage"],"Audiences affect performances.")
H('c.5.B',4,"A student writes an essay arguing that theatre builds empathy and civic awareness, citing performances she has seen. She is doing what?",
  "Defending theatre as an art form",["Dismissing theatre","Avoiding opinions","Copying a review"],"Arguments support the art form.")
H('c.5.B',4,"Valuing oneself as a creative being involves what?",
  "Recognizing one's ideas and contributions as meaningful",["Doubting every idea","Copying others","Avoiding risk"],"Self-valuing supports artistry.")
H('c.5.C',4,"A student compares how a novel and its stage adaptation convey a character's thoughts, noting what is gained and lost. She is doing what?",
  "Comparing literary and dramatic forms through evaluation",["Reviewing a menu","Counting acts","Reading a coupon"],"Adaptation shows differing techniques.")
H('c.5.C',4,"What is a challenge when adapting a novel's inner thoughts to the stage?",
  "Showing internal life through action, voice and design",["There are no characters","There is no story","Audiences cannot hear"],"Stage must externalize thoughts.")
H('c.5.D',4,"A student compares how a theme is communicated in a play, a film, a song and a mural. She is comparing what?",
  "Elements and communication methods across art forms",["Parking","Ticket stubs","Posters only"],"Each form uses distinct tools.")
H('c.5.D',4,"Which method of communication is shared by theatre and music?",
  "Live performance in real time",["Static imagery","Printed text only","Sculpture"],"Both are performed live.")
H('c.5.E',3,"A student interviews a theatre administrator and a high school drama teacher to compare their career paths. She is doing what?",
  "Evaluating career and avocational opportunities",["Ignoring options","Guessing","Skipping research"],"Interviews inform career evaluation.")
H('c.5.E',3,"Which is an avocational opportunity in theatre?",
  "Acting in a community theatre production on weekends",["Full-time teaching","Corporate producing","Union stage management"],"Avocations are pursued for enjoyment.")
H('c.5.F',4,"A senior publishes a website with annotated production photos, research findings and reflective essays. She is employing what?",
  "Technology to communicate and present theatre experiences",["A paper map","A coupon","A tuning fork"],"Digital portfolios present learning.")
H('c.5.F',4,"Which feature improves a digital theatre portfolio's usefulness for admissions?",
  "Organized work samples with clear descriptions",["Random uploads","No captions","Broken links"],"Organization helps reviewers.")
H('c.5.G',4,"A senior links her stage management experience to goals in project management and event planning. She is appraising what?",
  "Personal theatre skills in relation to higher education and careers",["Sports scores","Weather","Seat counts"],"Skills transfer to many fields.")
H('c.5.G',4,"Which theatre skill transfers best to a leadership career?",
  "Coordinating people and deadlines under pressure",["Hiding from tasks","Avoiding teams","Skipping planning"],"Production leadership transfers.")
H('c.5.H',3,"A graduating senior assembles a page listing roles, crew positions, awards and training. She is creating a ___.",
  "Theatrical resume",["Prompt book","Cue sheet","Playbill advertisement"],"A resume lists experience.")
H('c.5.H',3,"Which is an appropriate item in a theatre portfolio for an audition?",
  "Headshot, resume and recorded monologue",["Utility bills","Class schedules","Menu"],"Audition portfolios feature these materials.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_theatre4.jsonl'))

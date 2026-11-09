import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank
B = Bank('127.', 1105, own='cte_28.jsonl')
def H(code, d, q, right, wrong, e):
    return B.hand(code, d, q, right, wrong, e)

# ---------- 127.168 Practicum in Audio/Video Production ----------
H('168.d.1.A',3,"A practicum student enrolls in a studio-lighting workshop offered by a local community college. This is:",
  "Training that builds employable skills",["A way to avoid work","A hobby only","An unrelated class"],"Training/education/certification.")
H('168.d.1.A',4,"Earning a nationally recognized audio certification before graduation helps a graduate by:",
  "Showing employers verified skills",["Replacing a resume","Guaranteeing a salary","Avoiding interviews"],"Certification.")
H('168.d.1.B',3,"A practicum student who is punctual, prepared, and respectful to clients is showing:",
  "Professional standards",["Casual habits","Poor attitude","Indifference"],"Professional standards.")
H('168.d.1.B',4,"Which personal quality most helps a production assistant earn bigger responsibilities?",
  "Reliability under pressure",["Frequent excuses","Avoiding feedback","Hiding mistakes"],"Personal qualities.")
H('168.d.1.C',3,"Finding a part-time job at a local TV station by checking its careers page is:",
  "Seeking employment",["Wasting time","Quitting school","Avoiding work"],"Seeking employment.")
H('168.d.1.C',4,"Before an interview at a production company, a strong applicant should:",
  "Practice answers and bring work samples",["Arrive empty-handed","Skip research","Criticize past bosses"],"Applying for employment.")
H('168.d.1.D',3,"Updating a portfolio each semester means:",
  "Replacing weaker pieces with stronger recent work",["Deleting everything","Never changing it","Adding only drafts"],"Update career documents.")
H('168.d.1.D',4,"A cover letter updated for a new job posting should:",
  "Match the employer's stated needs",["Repeat the same letter","Be blank","List unrelated hobbies"],"Update documents.")
H('168.d.1.E',3,"Comparing pay, hours, benefits, and training when choosing between two offers is:",
  "Evaluating employment opportunities",["Gambling","Procrastinating","Daydreaming"],"Compare employment.")
H('168.d.1.E',4,"A studio job with lower pay but a strong mentor program may be better for:",
  "Rapid skill growth early in a career",["Immediate retirement","Skipping training","Avoiding experience"],"Evaluate opportunities.")
H('168.d.2.A',3,"Writing a clear production memo with correct spelling and punctuation shows:",
  "Consistent English language arts skills",["Weak writing","Random notes","Only drawing"],"ELA.")
H('168.d.2.A',4,"A practicum student writes a press release for a school film. It needs a clear headline, key facts, and:",
  "Correct grammar and a contact name",["Slang only","No details","Misspelled names"],"Writing for production.")
H('168.d.2.B',3,"A client is billed $65 per hour for 9 hours of editing. What is the invoice total?",
  "$585",["$74","$520","$650"],"65 x 9 = 585.")
H('168.d.2.B',4,"A 4-hour studio session starts at 10:30 a.m. When does it end?",
  "2:30 p.m.",["1:30 p.m.","3:30 p.m.","12:30 p.m."],"10:30 + 4 hours = 2:30 p.m.")
H('168.d.3.C',3,"A media class studies how film and TV can shape a viewer's sense of self, relationships, and the world. This develops:",
  "Perception of self, human relationships, and the environment",["Only camera skill","Only editing speed","Only budgeting"],"Perception of self through media.")
H('168.d.3.C',4,"A student reflects on how a documentary changed their view of their community. This is an example of media affecting:",
  "A viewer's understanding of the world",["Frame rate","File size","Cable length"],"Media and perception.")
H('168.d.3.C',3,"Exploring why a sad scene brings tears and a chase scene raises heartbeat studies the:",
  "Emotional and intellectual effects of visual media",["Weather","Storage","Voltage"],"Effects of visual media.")
H('168.d.3.C',4,"A close-up of a character's face with slow music mostly increases the viewer's:",
  "Emotional connection to the character",["Boredom","Confusion about plot","Awareness of cables"],"Emotional effect.")
H('168.d.3.A',3,"A voice actor practices clear pronunciation and breath control. This develops:",
  "Effective voice and diction",["Camera movement","Lighting skill","Set design"],"Voice and diction.")
H('168.d.3.A',4,"Speaking at a steady pace with distinct consonants helps a narrator's:",
  "Clarity and audience understanding",["Echo","File size","Frame rate"],"Diction.")
H('168.d.3.B',3,"Advertising that uses stereotypes to sell a product can:",
  "Shape viewers' attitudes in unfair ways",["Cause no effect","Reduce all bias","Improve accuracy"],"Media strategies.")
H('168.d.3.B',4,"A media-literate viewer asks who made a message and why in order to:",
  "Analyze persuasion strategies",["Skip the message","Accept everything","Hide the source"],"Analyze media.")
H('168.d.3.D',3,"A fast-cutting action trailer uses editing to create:",
  "A sense of energy and urgency",["A sense of calm","Silence","Empty frames"],"Visual and audio techniques.")
H('168.d.3.D',4,"A low rumble before a monster appears is a sound technique used to build:",
  "Suspense",["Humor","Boredom","Relief"],"Audio techniques.")
H('168.d.4.A',3,"A practicum student explains a camera test to the director using precise terms and to the client using plain terms. This is adapting language to:",
  "Audience, purpose, and situation",["A tripod","A battery","A file name"],"Adapt language.")
H('168.d.4.A',4,"A producer shortens a technical report into a one-page summary for sponsors. This adapts language to the:",
  "Purpose and intent",["Weather","Seat count","Cable length"],"Adapt language.")
H('168.d.4.B',3,"Grouping feedback comments into categories such as audio, picture, and pacing is:",
  "Analyzing and organizing information",["Deleting notes","Hiding notes","Printing notes"],"Analyze and organize.")
H('168.d.4.B',4,"Creating a clear outline before a sponsor pitch helps the speaker:",
  "Present ideas in a logical order",["Skip the point","Confuse the audience","Run overtime"],"Organize.")
H('168.d.4.C',3,"A producer studies audience-retention data and explains where viewers left. This is:",
  "Analyzing, interpreting, and communicating data",["Mixing sound","Building sets","Shooting B-roll"],"Interpret data.")
H('168.d.4.C',4,"An editor notes that 60 percent of viewers leave in the first ten seconds. A smart communication of this fact is:",
  "Recommend a stronger opening",["Ignore the result","Remove the ending","Add a slower intro"],"Communicate observations.")
H('168.d.4.D',3,"Designing a slide deck for a client pitch and presenting it live is a:",
  "Formal presentation",["Casual huddle","Private memo","Rehearsal only"],"Create and deliver presentations.")
H('168.d.4.D',4,"A quick stand-up report on the day's shoot is a(n):",
  "Informal presentation",["Keynote","Awards show","Press conference"],"Informal presentation.")
H('168.d.4.E',3,"When a client gives vague notes, a producer should:",
  "Ask questions to clarify what they want",["Guess","Ignore the note","Argue"],"Active listening.")
H('168.d.4.E',4,"Summarizing a director's notes back at the end of a meeting confirms:",
  "Shared understanding",["Disagreement","Confusion","Delay"],"Clarify information.")
H('168.d.4.F',3,"Interviewing a guest who is shy or uses a different dialect calls for:",
  "Respect and patient listening",["Teasing","Interrupting","Dismissal"],"Diverse individuals.")
H('168.d.4.F',4,"Working with colleagues from different cultures benefits a production by:",
  "Adding fresh perspectives to stories",["Limiting ideas","Creating conflict","Ending teamwork"],"Diversity.")
H('168.d.4.G',3,"On set, the person who performs in front of the camera is the:",
  "Talent",["Gaffer","Grip","Script supervisor"],"Production roles.")
H('168.d.4.G',4,"Collaborating well with the director means the talent:",
  "Takes direction and gives feedback respectfully",["Ignores the director","Changes the script silently","Refuses notes"],"Collaboration.")
H('168.d.4.H',3,"Internal customers for a studio include:",
  "Co-workers and departments that rely on your output",["Strangers","Competitors","Vendors only"],"Internal customers.")
H('168.d.4.H',4,"Public relations that increases external customer satisfaction might include:",
  "Responding promptly and politely to client questions",["Ignoring emails","Arguing with clients","Hiding delays"],"PR skills.")
H('168.d.5.A',3,"A team weighs two promotion ideas by cost, reach, and risk before choosing. That is:",
  "Critical thinking in a group",["Guessing","Flipping a coin","Copying a rival"],"Critical thinking.")
H('168.d.5.A',4,"Testing two title designs with sample viewers before deciding relies on:",
  "Evidence to support a choice",["A hunch","The loudest opinion","Chance"],"Critical thinking.")
H('168.d.5.B',3,"Mediating a disagreement between a camera operator and an editor needs:",
  "Fair listening and compromise",["Taking sides","Shouting","Ignoring it"],"Interpersonal skills.")
H('168.d.5.B',4,"A good way to solve a crew scheduling conflict is to:",
  "Meet, share constraints, and agree on a plan",["Leave it unresolved","Blame one person","Cancel the shoot"],"Group problem solving.")
H('168.d.5.C',3,"A student artist who revises a film after critique shows artistic discipline and:",
  "Responsibility for the quality of the work",["Carelessness","Avoidance","Indifference"],"Responsibility and discipline.")
H('168.d.5.C',4,"Facing a creative problem when a location falls through, a good producer:",
  "Brainstorms alternatives and tests them",["Gives up","Blames weather","Delays indefinitely"],"Creative problem solving.")
H('168.d.6.A',3,"A producer uses a shared calendar, email, and cloud folders to run a project. These are:",
  "Technology applications",["Obsolete tools","Hand tools","Paper maps"],"Technology applications.")
H('168.d.6.A',4,"Using a messaging channel to post daily shoot updates helps the crew:",
  "Stay informed in real time",["Lose information","Duplicate work","Avoid contact"],"Technology.")
H('168.d.6.B',3,"Setting up consistent folder structures for raw footage, audio, and exports is:",
  "File management",["Lens cleaning","Wardrobe","Casting"],"File management.")
H('168.d.6.B',4,"Keeping a master contact list in one shared document is an example of:",
  "Personal and information management",["Wasting memory","Duplicating errors","Hiding information"],"Information management.")
H('168.d.7.A',3,"Wearing proper footwear and following rules for heavy equipment throughout a practicum is:",
  "Implementing workplace safety rules",["Optional","Fashion","Ignoring rules"],"Safety rules.")
H('168.d.7.A',4,"A lift-and-carry rule for a heavy light kit is typically to:",
  "Use proper lifting technique or get help",["Lift alone with a twisted back","Drag it","Throw it"],"Safety.")
H('168.d.7.B',3,"A trip hazard from loose cables is recognized and resolved by:",
  "Taping or covering the cables",["Ignoring them","Hiding them under a rug","Moving them in front of exits"],"Resolve safety concerns.")
H('168.d.7.B',4,"Before filming near water, a crew should recognize hazards such as:",
  "Slippery surfaces and electrical risks",["Cheap lunches","Soft music","Bright logos"],"Recognize hazards.")
H('168.d.7.C',3,"If a fire alarm sounds during a shoot in a building, the crew should:",
  "Evacuate using the posted route",["Continue shooting","Hide equipment","Call the cast back"],"Emergency procedures.")
H('168.d.7.C',4,"A crew leader should know the location of:",
  "First-aid kit and emergency exits",["Snack bar","Best photo spot","Gift shop"],"Emergency procedures.")
H('168.d.8.A',3,"A student leader sets a goal, assigns roles, and checks in regularly. This leadership:",
  "Helps the team accomplish objectives",["Wastes resources","Confuses the crew","Delays work"],"Leadership.")
H('168.d.8.A',4,"A leader exhibits strong character by:",
  "Being honest and taking responsibility",["Blaming others","Hiding errors","Taking all credit"],"Leadership.")
H('168.d.8.B',3,"Working as a team toward a shared goal includes:",
  "Supporting each other and resolving conflicts",["Competing for credit","Withholding help","Working in silence"],"Teamwork.")
H('168.d.8.B',4,"An effective way to manage a team conflict is to:",
  "Focus on the problem and not the person",["Attack the person","Ignore the issue","Wait for it to vanish"],"Conflict management.")
H('168.d.8.C',3,"Good working relationships grow from:",
  "Respect and constructive feedback",["Gossip","Silence","Competition for credit"],"Working relationships.")
H('168.d.8.C',4,"Constructive feedback on a rough cut should:",
  "Point out strengths and name specific improvements",["Only criticize","Be vague","Be personal"],"Constructive feedback.")
H('168.d.8.D',3,"A meeting objective should be:",
  "Clear and measurable",["Hidden","Endless","Vague"],"Meeting objectives.")
H('168.d.8.D',4,"Preparing for a meeting includes setting goals and:",
  "Gathering the materials the group needs",["Arriving late","Skipping notes","Inviting nobody"],"Preparing for meetings.")
H('168.d.8.E',3,"A leader runs an effective meeting by:",
  "Following the agenda and recording decisions",["Letting it drift","Skipping notes","Ignoring input"],"Conduct meetings.")
H('168.d.8.E',4,"Participating in a meeting productively means:",
  "Contributing and listening respectfully",["Dominating","Staying silent","Using a phone"],"Participate in meetings.")
H('168.d.8.F',3,"A veteran sound engineer sharing tips with an apprentice is:",
  "Mentoring",["Competing","Hiding techniques","Delaying"],"Mentoring.")
H('168.d.8.F',4,"A good mentor teaches skills and also:",
  "Inspires confidence and professionalism",["Discourages risks","Takes credit","Criticizes harshly"],"Inspire and teach.")
H('168.d.9.A',3,"Not editing a witness's quote to mean something different is:",
  "Ethical conduct",["A budget choice","A technical error","Accidental"],"Ethical conduct.")
H('168.d.9.A',4,"Disclosing a paid sponsorship in a video is:",
  "An honest, ethical practice",["Optional","Harmful","Wasteful"],"Ethics.")
H('168.d.9.B',3,"A trademark protects:",
  "Brand names and logos",["Private journals","Public sidewalks","Weather"],"Trademark.")
H('168.d.9.B',4,"Using a short clip in a classroom critique is more likely to be fair use than:",
  "Selling a film built from that clip",["A discussion in class","A scholarly review","A parody review"],"Fair use.")
H('168.d.9.C',3,"Modeling respect for intellectual property includes:",
  "Crediting artists and following license terms",["Copying freely","Removing credits","Reselling others' work"],"Intellectual property.")
H('168.d.9.C',4,"A music license that covers only a school screening does NOT automatically cover:",
  "Commercial distribution",["The school screening","A classroom viewing","Rehearsal"],"License limits.")
H('168.d.9.D',3,"Acceptable use policies at a studio generally require users to:",
  "Use equipment and networks for approved work",["Install any app","Share passwords","Download anything"],"AUP.")
H('168.d.9.D',4,"Good network etiquette includes:",
  "Not tying up bandwidth during critical uploads",["Streaming games","Sharing passwords","Installing unknown software"],"Etiquette.")
H('168.d.10.A',3,"Breaking a project into daily tasks with deadlines is:",
  "Planning and time management",["Guessing","Delaying","Multitasking"],"Time management.")
H('168.d.10.A',4,"Doing the highest-priority tasks first helps a producer:",
  "Meet deadlines under pressure",["Add stress","Miss details","Run out of time"],"Planning.")
H('168.d.10.B',3,"A timeline app that shows tasks and who owns them is:",
  "Technology that boosts productivity",["A distraction","A waste of time","A hazard"],"Technology productivity.")
H('168.d.10.B',4,"Automating a repetitive export task with a preset saves:",
  "Time and reduces mistakes",["Quality","Footage","Storage"],"Productivity.")
H('168.d.11.A',3,"Setting up and testing a mixer, mics, and monitors before a session is part of:",
  "Set-up and execution of standard systems",["Casting","Costume design","Scoring"],"Set-up and troubleshooting.")
H('168.d.11.A',4,"If one channel has no sound, a good first troubleshooting step is to check the:",
  "Cable and input settings",["Wall paint","Lunch order","Parking pass"],"Troubleshooting.")
H('168.d.11.B',3,"Metering a recording means watching the:",
  "Signal level to avoid distortion",["Battery brand","Tripod height","Lens focus"],"Recording devices.")
H('168.d.11.B',4,"A level meter peaking at the top of the scale warns of:",
  "Clipping and distortion",["Perfect sound","Echo","Silence"],"Metering.")
H('168.d.11.C',3,"Using terms like \"slate,\" \"take,\" and \"wrap\" correctly is applying:",
  "Industry terminology",["Slang only","Foreign words","Random sounds"],"Terminology.")
H('168.d.11.C',4,"\"Room tone\" is recorded to:",
  "Fill gaps in editing with the room's natural sound",["Add music","Mute dialogue","Boost bass"],"Terminology.")
H('168.d.12.A',3,"Early planning of purpose, audience, and distribution is:",
  "Applying critical elements of pre-production",["Wasting time","Post-production","Marketing only"],"Critical elements.")
H('168.d.12.A',4,"If the distribution is a short social video, the production plan should favor:",
  "Brief, fast-paced content in the right format",["A two-hour edit","A silent film","Print layouts"],"Production planning.")
H('168.d.12.B',3,"Using scheduling software and shared storyboards to plan a shoot is:",
  "Advanced technology for pre-production",["Hand drawing only","Guesswork","Production delay"],"Pre-production technology.")
H('168.d.12.B',4,"Digital pre-visualization lets a director:",
  "Test shots before filming",["Edit after release","Skip planning","Avoid cameras"],"Advanced technology.")
H('168.d.12.C',3,"Documents of the scripting process include a treatment, a script, and a:",
  "Storyboard",["Menu","Receipt","Poster only"],"Scripting documents.")
H('168.d.12.C',4,"A shot list differs from a storyboard because it:",
  "Lists shots in words and order, often with technical notes",["Draws every frame","Has no order","Replaces the script"],"Production documents.")
H('168.d.12.D',3,"Using the proper screenplay format helps because it:",
  "Lets readers estimate length and understand scenes",["Hides dialogue","Adds errors","Increases cost"],"Formatting.")
H('168.d.12.D',4,"In a standard screenplay, one formatted page usually equals about:",
  "One minute of screen time",["Ten minutes","One second","One hour"],"Format conventions.")
H('168.d.12.E',3,"A call sheet is a production document that tells:",
  "Who needs to be where and when",["How to cook","Weather only","What to watch"],"Production documents.")
H('168.d.12.E',4,"A production document needed for a successful shoot includes a:",
  "Shooting schedule",["Lunch menu only","Fan letter","Trophy list"],"Production elements.")
H('168.d.12.F',3,"Determining the artistic impact of a production plan means asking how the finished work will:",
  "Affect and communicate with viewers",["Be stored","Be taxed","Be insured"],"Artistic impact.")
H('168.d.12.F',4,"A plan for a horror short favors lighting that builds:",
  "Mood and tension",["Cheerfulness","Comedy","Comfort"],"Artistic impact.")
H('168.d.12.G',3,"Color, texture, form, and line are:",
  "Art elements",["Hardware parts","Contracts","Cables"],"Art elements.")
H('168.d.12.G',4,"Strong horizontal lines in a frame often suggest:",
  "Calm and stability",["Chaos","Speed","Danger"],"Art elements in production.")
H('168.d.12.H',3,"Repeating shapes and colors in a scene to create unity is the design principle of:",
  "Pattern or continuity",["Friction","Static","Buffer"],"Principles of design.")
H('168.d.12.H',4,"A steady, repeated beat in editing creates:",
  "Rhythm",["Silence","Clutter","Confusion"],"Principles of design.")
H('168.d.12.I',3,"For a scripted scene in a hospital, the crew determines the cast, equipment, and:",
  "Location needs",["Pet needs","Sports plans","Fashion trends"],"Production requirements.")
H('168.d.12.I',4,"A permit may be required to film in a:",
  "Public park or street",["Backyard of a friend with consent","Studio you own","Closet"],"Location requirements.")
H('168.d.12.J',3,"Conducting auditions helps a director:",
  "Find actors who fit the roles",["Rewrite the script","Edit footage","Repair cameras"],"Auditions.")
H('168.d.12.J',4,"After an audition, securing the crew requires confirming:",
  "Availability, rates, and responsibilities",["Shoe sizes","Hair color","Music tastes"],"Securing crew.")
H('168.d.12.K',3,"A talent release form gives the producer permission to:",
  "Use a person's image or performance",["Delete the film","Sell the person's home","Rewrite laws"],"Contracts.")
H('168.d.12.K',4,"A crew agreement usually lists:",
  "Pay, schedule, and duties",["Favorite colors","Birth charts","Hobbies"],"Contracts.")
H('168.d.13.A',3,"Shooting scenes out of story order to use one location for several scenes is part of:",
  "A planned production sequence",["A random plan","A rewrite","A delay"],"Coherent sequence.")
H('168.d.13.A',4,"A production day usually follows a coherent sequence: set up, rehearse, shoot, and then:",
  "Review and wrap",["Delete","Start over","Skip"],"Production sequence.")
H('168.d.13.B',3,"Using a bounce card to fill shadows on a face is:",
  "A reflected light technique",["A sound technique","An editing trick","A costume choice"],"Lighting techniques.")
H('168.d.13.B',4,"In three-point lighting, the key light provides the:",
  "Main illumination of the subject",["Background only","Shadow only","Color grading"],"Three-point lighting.")
H('168.d.13.C',3,"For capturing speech in a noisy crowd, a producer would favor a:",
  "Directional microphone close to the speaker",["Distant omni mic","No mic","Speakerphone"],"Audio techniques.")
H('168.d.13.C',4,"A windscreen on a microphone outdoors reduces:",
  "Wind noise",["Brightness","Frame rate","Resolution"],"Microphone use.")
H('168.d.13.D',3,"Sound mixing balances voices, music, and effects so the audience hears:",
  "A clear, well-blended soundtrack",["Only music","Only noise","No dialogue"],"Sound mixing.")
H('168.d.13.D',4,"A final audio mix is checked on both speakers and:",
  "Headphones or common listening devices",["Light meters","Printers","Cameras"],"Final audio.")
H('168.d.13.E',3,"Executing the script on set with every department doing its part shows:",
  "Teamwork and production knowledge",["Chaos","Delay","Isolation"],"Execution.")
H('168.d.13.E',4,"If a scene runs long, the director and producer should:",
  "Adjust the schedule together",["Ignore the clock","Cancel the film","Blame the crew"],"Production execution.")
H('168.d.13.F',3,"Designing a classroom activity around a shoot, the teacher includes objectives and:",
  "Assessments tied to the production goals",["Random tasks","No evaluation","Hidden directions"],"Critical elements in activities.")
H('168.d.13.F',4,"A learning activity about a production is strongest when it has:",
  "A clear purpose and audience",["No goal","Unclear steps","No feedback"],"Activity design.")
H('168.d.13.G',3,"Digital editing allows an editor to cut footage for different:",
  "Distribution platforms",["Weather conditions","Personal tastes","Parking rules"],"Digital editing.")
H('168.d.13.G',4,"An editor prepares one version for broadcast and another for web, recognizing different:",
  "Distribution requirements",["Hair styles","Studio colors","Pet needs"],"Distribution considerations.")
H('168.d.13.H',3,"Ingesting media into an editing system means:",
  "Importing it for editing",["Deleting it","Printing it","Muting it"],"Ingest media.")
H('168.d.13.H',4,"During ingest, an editor should keep original files and work on:",
  "Copies or proxies",["The only copy","A blank file","Deleted files"],"Ingest and manipulation.")
H('168.d.13.I',3,"Monitoring equipment during a shoot ensures:",
  "Quality recordings",["Poor audio","Blurry video","Missing files"],"Monitor equipment.")
H('168.d.13.I',4,"Checking headphones during recording is a way to catch:",
  "Noise and dropouts as they happen",["Costume errors","Scheduling errors","Budget errors"],"Monitoring quality.")
H('168.d.13.J',3,"Before recording, setting levels with color bars and a tone uses:",
  "Broadcast standard test signals",["A random sound","A pop song","A film clip"],"Set levels.")
H('168.d.13.J',4,"A 1 kHz reference tone helps technicians:",
  "Match audio levels across equipment",["Adjust lighting","Pick a lens","Record video"],"Standard tools.")
H('168.d.13.K',3,"Logging notes during recording means writing down:",
  "Take numbers, timecodes, and comments",["Lunch orders","Social plans","Weather only"],"Logging standards.")
H('168.d.13.K',4,"A good log helps editors by:",
  "Showing which takes are best",["Hiding footage","Replacing the script","Adding noise"],"Logging.")
H('168.d.14.A',3,"A video system that records ones and zeros is called:",
  "Digital",["Mechanical","Analog","Magnetic only"],"Video systems.")
H('168.d.14.A',4,"Analog video signals are susceptible to:",
  "Noise degradation with copying",["Perfect copies","No loss","Higher quality"],"Analog vs digital.")
H('168.d.14.B',3,"A camera is an input device, an editing computer is a processor, and a monitor is an:",
  "Output device",["Input device","Storage only","Power source"],"Input, processing, output.")
H('168.d.14.B',4,"A hard drive that holds footage is a:",
  "Storage device",["Input device","Output device","Camera lens"],"Storage devices.")
H('168.d.14.C',3,"Playing an old video format on a new system can cause:",
  "Compatibility problems",["Better quality","Faster speed","Brighter color"],"Compatibility.")
H('168.d.14.C',4,"Digital compatibility issues often involve mismatched:",
  "Codecs or file formats",["Parking spots","Lunch orders","Pets"],"Compatibility issues.")
H('168.d.14.D',3,"High definition video compared to standard definition has:",
  "More detail and a wider picture",["Less detail","No color","No sound"],"HD vs SD.")
H('168.d.14.D',4,"1920 x 1080 describes a common:",
  "High-definition resolution",["Audio level","Frame rate","Color temperature"],"HD and SD.")
H('168.d.15.A',3,"Using a character generator, an editor adds a graphic that follows good composition by:",
  "Placing text where it is readable and balanced",["Covering faces","Using tiny fonts","Overlapping everything"],"Character generators and composition.")
H('168.d.15.A',4,"Choosing high-contrast colors for on-screen text helps:",
  "Viewers read it easily",["Hide the message","Confuse viewers","Lower resolution"],"Fonts and colors.")
H('168.d.15.B',3,"Closed captions help viewers who:",
  "Are deaf, hard of hearing, or watching without sound",["See perfectly","Dislike text","Are on mute only"],"Captions.")
H('168.d.15.B',4,"A title graphic should stay on screen long enough for the audience to:",
  "Read it comfortably",["Miss it","Ignore it","Forget it"],"Titles.")
H('168.d.16.A',3,"Outputting a finished program to an online platform requires:",
  "Choosing proper export settings",["Deleting the project","Muting audio","Resizing to a thumbnail"],"Output for distribution.")
H('168.d.16.A',4,"Selecting a standard codec such as H.264 for web delivery helps with:",
  "Wide compatibility and manageable file size",["Heavy files","Poor playback","Limited viewing"],"Output.")
H('168.d.16.B',3,"Higher-quality exports generally mean:",
  "Larger file sizes",["Smaller files","No file","Shorter video"],"File size and quality.")
H('168.d.16.B',4,"A producer lowers the bitrate to meet an upload limit and accepts:",
  "Some loss in image quality",["Better detail","Perfect clarity","No change"],"Tradeoff.")
H('168.d.16.C',3,"A production may be delivered on disc, broadcast, a cell phone, or a:",
  "Portable media player",["Television set only","Grocery list","Billboard"],"Delivery formats.")
H('168.d.16.C',4,"A vertical video format is best for:",
  "Mobile viewing",["Cinema screens","Radio","Print"],"Delivery.")
H('168.d.16.D',3,"The correct delivery method depends on the:",
  "Distribution needs of the project",["Weather","Color of the camera","Seat selection"],"Delivery method.")
H('168.d.16.D',4,"A corporate training video for employees may be delivered through a:",
  "Company learning portal",["Billboard","Movie theater","Radio"],"Delivery.")
H('168.d.16.E',3,"Sharing a project with remote classmates via a digital platform extends:",
  "The learning environment",["The deadline","The cost","The risk"],"Digital sharing.")
H('168.d.16.E',4,"Gathering feedback on a draft through an online form is an example of:",
  "Digitally gathering information",["Printing information","Losing information","Hiding information"],"Digital gathering.")
H('168.d.16.F',3,"A spreadsheet that tracks shoot costs and a document that holds scripts are:",
  "Computer-based productivity tools",["Hand tools","Paper tools","Garden tools"],"Productivity tools.")
H('168.d.16.F',4,"Using templates in a word processor helps produce:",
  "Consistent, professional documents",["Random layouts","Unreadable text","Wasted pages"],"Create and modify.")
H('168.d.16.G',3,"Linking a budget spreadsheet to a schedule helps solve problems like:",
  "Overspending during delays",["Making props","Choosing music","Casting"],"Integrate tools.")
H('168.d.16.G',4,"Integrating a project-management tool with calendars shows how technology can:",
  "Streamline coordination across a team",["Add confusion","Hide tasks","Duplicate effort"],"Integration.")
H('168.d.16.H',3,"Technical documentation for a project lists specifications such as:",
  "Resolution, frame rate, and audio format",["Menu items","Birthdays","Hobbies"],"Technical documentation.")
H('168.d.16.H',4,"Documenting equipment settings after a shoot helps:",
  "Future crews repeat or fix the setup",["Delete footage","Hide errors","Delay editing"],"Documentation.")
H('168.d.17.A',3,"Critiquing a finished production includes asking how elements like lighting and sound:",
  "Contributed to the final impact",["Increased cost","Added weight","Changed the weather"],"Critique.")
H('168.d.17.A',4,"A balanced critique names what worked and:",
  "What could improve, with reasons",["Only flaws","Only praise","Only personal opinion"],"Critique.")
H('168.d.17.B',3,"Evaluating a final production as an art form means judging its:",
  "Creativity, craft, and emotional effect",["Shipping cost","File name","Hard drive"],"Art form.")
H('168.d.17.B',4,"Recognizing film as an art form shows an appreciation of how storytelling and craft:",
  "Combine to move audiences",["Reduce meaning","Hide ideas","Limit viewers"],"Evaluate art.")

# ---------- 127.169 Audio Production ----------
H('169.d.9',3,"A student arrives early to the studio, takes ownership of tasks, and communicates problems. These are:",
  "Career-building characteristics",["Poor habits","Distractions","Time-wasters"],"Career-building characteristics.")
H('169.d.9',4,"Which habit most builds a long-term career in audio?",
  "Reliability and continued learning",["Skipping training","Avoiding feedback","Working only when watched"],"Career characteristics.")
H('169.d.1.A',3,"Writing a clear session notes document with correct punctuation uses:",
  "English language arts skills",["Welding","Gardening","Plumbing"],"ELA.")
H('169.d.1.A',4,"A producer proofreads liner notes for an album for accuracy and spelling. This is:",
  "Language arts applied in audio",["A mixing step","A mastering step","A recording step"],"ELA in audio.")
H('169.d.1.B',3,"A session engineer charges $75 per hour for 6 hours. What is the total?",
  "$450",["$81","$405","$480"],"75 x 6 = 450.")
H('169.d.1.B',4,"A song is 3 minutes 45 seconds long. How many seconds is that?",
  "225",["345","180","215"],"3 x 60 + 45 = 225.")
H('169.d.2.A',3,"Explaining an equalizer to a beginner artist with everyday words is:",
  "Adapting language to the audience",["Ignoring the audience","Using jargon only","Staying silent"],"Adapt language.")
H('169.d.2.A',4,"An engineer uses technical terms with other engineers and plain words with the band. This adapts to the:",
  "Situation and listener",["Cable","Console","Room"],"Adapt language.")
H('169.d.2.B',3,"Arranging session files in clearly named folders by song and date is:",
  "Organizing information",["Mixing","Mastering","Overdubbing"],"Organize information.")
H('169.d.2.B',4,"A session track sheet organizes:",
  "Which instruments are on which tracks",["Lunch orders","Tour dates","Gear prices"],"Organize information.")
H('169.d.2.C',3,"A mixer reads a meter and tells the band the vocal is too loud. This is:",
  "Interpreting and communicating data",["Editing video","Painting","Building sets"],"Interpret observations.")
H('169.d.2.C',4,"An engineer says, \"The left channel is 6 dB lower than the right.\" This communicates:",
  "A measurable observation",["A rumor","A joke","An opinion about food"],"Communicate data.")
H('169.d.2.D',3,"Playing a final mix for the client in the studio, with an explanation, is a(n):",
  "Formal presentation",["Casual joke","Noise test","Warm-up"],"Formal presentation.")
H('169.d.2.D',4,"A quick \"here's what we recorded\" talk with the band after a take is an:",
  "Informal presentation",["Keynote","Press conference","Awards speech"],"Informal presentation.")
H('169.d.2.E',3,"A producer who maintains eye contact and notes the artist's feedback is:",
  "Applying active listening",["Ignoring","Interrupting","Multitasking"],"Active listening.")
H('169.d.2.E',4,"After an artist describes a sound they want, the engineer repeats it back to:",
  "Confirm understanding",["Argue","End the session","Change the topic"],"Active listening.")
H('169.d.2.F',3,"Recording a singer from a culture different from yours requires:",
  "Respect and open communication",["Assumptions","Stereotypes","Interrupting"],"Diverse individuals.")
H('169.d.2.F',4,"Working with musicians of various backgrounds can enrich a project by:",
  "Bringing different styles and ideas",["Limiting sounds","Causing disputes","Reducing creativity"],"Diversity.")
H('169.d.2.G',3,"Good public relations for a studio include:",
  "Treating clients courteously and keeping promises",["Missing deadlines","Rude replies","Hiding fees"],"PR skills.")
H('169.d.2.G',4,"A studio builds its reputation when it:",
  "Delivers quality work and communicates clearly",["Cuts corners","Avoids clients","Delays without notice"],"Public relations.")
H('169.d.3.A',3,"An engineer compares two microphones on a singer and chooses the one that fits the voice. This is:",
  "Critical thinking",["Guessing","Luck","Copying"],"Critical thinking.")
H('169.d.3.A',4,"Making a mix decision by listening on several speakers relies on:",
  "Evidence from multiple references",["Guesses","Trends only","Rank"],"Critical thinking.")
H('169.d.3.B',3,"Two band members disagree on a song's tempo. A helpful interpersonal skill is:",
  "Listening and testing both ideas",["Yelling","Quitting","Blaming"],"Interpersonal skills.")
H('169.d.3.B',4,"Group problem solving in a session works best when members:",
  "Share ideas and respect decisions",["Work in secret","Argue loudly","Walk out"],"Group problem solving.")
H('169.d.4.A',3,"Using email, cloud storage, and sample-library websites in a session workflow are:",
  "Technology applications",["Hand tools","Obsolete tools","Print tools"],"Technology applications.")
H('169.d.4.A',4,"Sharing a rough mix through a secure link so the artist can listen at home is:",
  "Using technology to communicate",["Wasting data","Losing the mix","Printing the mix"],"Technology applications.")
H('169.d.4.B',3,"Keeping all takes for a song in a labeled folder is:",
  "File management",["Mixing","Mastering","Equalizing"],"File management.")
H('169.d.4.B',4,"Backing up session files nightly to another drive prevents:",
  "Losing recordings if one drive fails",["Clipping","Distortion","Latency"],"Backup.")
H('169.d.5.A',3,"The move from wax cylinders to vinyl to digital streaming is part of:",
  "The history and evolution of audio production",["Radio only","Film history","Print history"],"History of audio.")
H('169.d.5.A',4,"Multitrack recording changed music production because it allowed:",
  "Separate recording and mixing of instruments",["One-take recordings only","No editing","Only live shows"],"Evolution.")
H('169.d.5.B',3,"Podcasting and streaming audio are current trends that give audio producers:",
  "New markets and formats",["No audience","Fewer jobs only","Only radio"],"Current trends.")
H('169.d.5.B',4,"An audio producer who tracks trends can decide:",
  "Which skills and services to offer",["Which weather to expect","What time zone to use","Where to park"],"Analyze trends.")
H('169.d.6.A',3,"Wearing hearing protection around loud monitors is:",
  "A workplace safety rule",["Optional","A fashion item","A microphone"],"Safety rules.")
H('169.d.6.A',4,"Listening at extremely high volume for long periods can cause:",
  "Permanent hearing damage",["Better ears","Cleaner sound","Faster mixing"],"Safety regulation.")
H('169.d.6.B',3,"If the studio fire alarm sounds, the engineer should:",
  "Leave by the posted exit route",["Finish the take","Plug in more gear","Hide in the booth"],"Emergency procedures.")
H('169.d.6.B',4,"Studio electrical safety includes:",
  "Not overloading outlets or power strips",["Daisy-chaining many strips","Tangling cables","Removing ground pins"],"Safety.")
H('169.d.7.A',3,"A student who organizes a recording session and assigns roles is:",
  "Employing leadership skills",["Delaying","Avoiding","Dominating"],"Leadership.")
H('169.d.7.A',4,"A leader in the studio keeps the session on track by:",
  "Setting goals and checking progress",["Ignoring time","Doing everything alone","Avoiding feedback"],"Leadership.")
H('169.d.7.B',3,"Band and engineer working together on a mix demonstrate:",
  "Teamwork",["Rivalry","Isolation","Delay"],"Teamwork.")
H('169.d.7.B',4,"The first step to resolve a conflict over a mix note is to:",
  "Listen to each viewpoint",["Take sides","Ignore it","Raise voices"],"Conflict management.")
H('169.d.7.C',3,"A good participant in a pre-production meeting:",
  "Shares ideas and listens to others",["Interrupts","Checks phone","Leaves early"],"Participate in meetings.")
H('169.d.7.C',4,"Writing down action items at a session meeting keeps everyone:",
  "Clear about next steps",["Confused","Late","Uninformed"],"Meetings.")
H('169.d.7.D',3,"An experienced mixing engineer guiding an intern is:",
  "Mentoring",["Competing","Hiding","Delaying"],"Mentoring.")
H('169.d.7.D',4,"Participating in mentoring helps a beginner by:",
  "Giving guidance and feedback",["Limiting growth","Raising costs","Reducing skill"],"Mentoring.")
H('169.d.8.A',3,"Not altering a recording of an interview to change its meaning is:",
  "Ethical conduct",["Poor mixing","A technical error","Accidental"],"Ethical conduct.")
H('169.d.8.A',4,"An engineer keeps a client's unreleased song confidential. This is:",
  "Ethical professional behavior",["Optional","A mistake","Unfair"],"Ethical conduct.")
H('169.d.8.B',3,"Crediting a songwriter and obtaining a license for a cover song shows:",
  "Respect for intellectual property",["Disrespect","Ignorance","Carelessness"],"Intellectual property.")
H('169.d.8.B',4,"Using a sample from another artist's record without permission can:",
  "Violate copyright law",["Be free of rules","Improve legal standing","Be required"],"IP respect.")
H('169.d.8.C',3,"The audio industry affects society by shaping:",
  "Music, news, and entertainment people hear",["Weather","Traffic","Soil"],"Ethical impact.")
H('169.d.8.C',4,"Loudness wars in mastering raise an ethical issue about:",
  "Sacrificing sound quality for volume",["Better dynamics","Faster releases","Tax rules"],"Industry impact.")
H('169.d.8.D',3,"Copyright law gives creators control over:",
  "Copying and public use of their work",["Weather","Tides","Taxes"],"Copyright.")
H('169.d.8.D',4,"Fair use allows limited use of copyrighted material for purposes like:",
  "Commentary, criticism, or education",["Any reuse","Selling copies","Rebroadcasting"],"Fair use.")
H('169.d.8.E',3,"A broadcast audio engineer must comply with applicable rules from the:",
  "Federal Communications Commission",["Postal service","Park service","Weather service"],"Regulations.")
H('169.d.8.E',4,"Following agency rules on radio content and licensing helps stations avoid:",
  "Fines and loss of license",["Audiences","Awards","Profits"],"Compliance.")
H('169.d.10.A',3,"Creating a recording-day schedule with set times for setup, tracking, and breaks uses:",
  "Planning and time management",["Guesswork","Delay","Luck"],"Time management.")
H('169.d.10.A',4,"Allowing extra time for troubleshooting in a schedule is smart because:",
  "Technical problems often happen",["Time is unlimited","Gear never fails","Clients prefer delays"],"Planning.")
H('169.d.10.B',3,"A session-notes app that stores take numbers and comments is a:",
  "Technology that boosts productivity",["Distraction","Hazard","Delay"],"Technology productivity.")
H('169.d.10.B',4,"Using templates in a DAW for common session types saves:",
  "Setup time",["Hard drive space","Wiring","Speakers"],"Productivity.")
H('169.d.11.A',3,"Careers in audio production include roles in:",
  "Recording studios, broadcasting, live sound, and post-production",["Only radio","Only retail","Only banking"],"Career pathways.")
H('169.d.11.A',4,"A live-sound engineer works mainly:",
  "At concerts and events",["In a bank","In a hospital","In a farm"],"Career opportunities.")
H('169.d.11.B',3,"The person who guides the creative direction of a recording is the:",
  "Producer",["Caterer","Guard","Driver"],"Industry audio professionals.")
H('169.d.11.B',4,"A mastering engineer is responsible for:",
  "Preparing the final mix for distribution",["Setting up cables","Hiring crews","Writing songs"],"Roles.")
H('169.d.11.C',3,"Understanding the history and future of audio helps professionals:",
  "Prepare for changes in technology",["Avoid learning","Ignore trends","Resist progress"],"History and trends.")
H('169.d.11.C',4,"Immersive audio formats such as spatial audio are a growing trend in:",
  "Music, film, and gaming",["Weather","Cooking","Plumbing"],"Future trends.")
H('169.d.11.D',3,"Software-based recording replaced much hardware because it:",
  "Lowered cost and increased access",["Increased noise","Raised cost","Blocked creativity"],"Changing technology.")
H('169.d.11.D',4,"Artificial-intelligence tools in audio might help with tasks like:",
  "Noise reduction and stem separation",["Painting walls","Cooking","Typing taxes"],"Technology impact.")
H('169.d.11.E',3,"In audio, \"gain staging\" means:",
  "Managing signal level at each stage of the chain",["Booking a stage","Raising rent","Adding lights"],"Terminology.")
H('169.d.11.E',4,"\"Latency\" in digital recording refers to:",
  "The delay between input and output",["Volume","Pitch","Color"],"Terminology.")
H('169.d.12.A',3,"A dynamic microphone is known for being:",
  "Rugged and good for loud sources",["Fragile","Needing no cable","Only for whispers"],"Microphone types.")
H('169.d.12.A',4,"A condenser microphone typically requires:",
  "Phantom power",["A battery pack of 100 volts","Wind","Sunlight"],"Microphone application.")
H('169.d.12.B',3,"A cardioid pickup pattern is most sensitive to sound from the:",
  "Front",["Back","Sides only","Top only"],"Pick-up patterns.")
H('169.d.12.B',4,"A figure-eight microphone picks up sound from the front and:",
  "Back",["Left only","Top only","Floor"],"Pick-up patterns.")
H('169.d.12.C',3,"An audio console (mixer) lets the engineer:",
  "Blend, adjust, and route multiple signals",["Cook meals","Charge phones","Record video"],"Audio consoles.")
H('169.d.12.C',4,"A fader on a mixer controls the:",
  "Level of a channel",["Color of lights","Room temperature","Cable length"],"Console operation.")
H('169.d.12.D',3,"A compressor reduces the difference between:",
  "Loud and quiet parts of a signal",["High and low frequencies","Left and right only","Wet and dry only"],"Audio processing.")
H('169.d.12.D',4,"An equalizer adjusts:",
  "The balance of frequencies",["The speed of tape","The length of cable","The brightness of a monitor"],"Processing equipment.")
H('169.d.12.E',3,"An audio interface converts:",
  "Analog signals to digital and back",["Pictures to text","Words to speech","Voltage to light"],"Recorders.")
H('169.d.12.E',4,"Compared with analog tape, digital recording lets engineers:",
  "Edit non-destructively",["Lose all edits","Avoid copying","Reduce choices"],"Analog and digital recorders.")
H('169.d.12.F',3,"Balanced XLR cables reduce:",
  "Interference over long runs",["Volume","Pitch","Speed"],"Audio cabling.")
H('169.d.12.F',4,"A TS (tip-sleeve) 1/4-inch cable is typically used for:",
  "Unbalanced instrument signals",["Video","Power","Network"],"Connectors.")
H('169.d.12.G',3,"A direct box (DI) lets a guitarist connect:",
  "An instrument to a mixer or interface cleanly",["A phone to a TV","A car to a house","A TV to a lamp"],"Additional hardware.")
H('169.d.12.G',4,"A headphone amplifier lets several people:",
  "Monitor a session at the same time",["Cook","Print","Charge"],"Audio hardware.")
H('169.d.12.H',3,"Studio monitor speakers are designed to provide:",
  "A flat, accurate sound for mixing",["Hyped bass","Colored sound","Maximum volume"],"Speakers.")
H('169.d.12.H',4,"Public address (PA) speakers are built to:",
  "Fill larger spaces with sound for audiences",["Be quiet","Block sound","Record voices"],"Speakers.")
H('169.d.13.A',3,"The stems of an audio production often include:",
  "Dialogue, music, and sound effects",["Prices","Locations","Contracts"],"Key elements.")
H('169.d.13.A',4,"Delivering stems separately lets a mixer later:",
  "Adjust each group without remixing everything",["Delete the project","Raise the cost","Hide errors"],"Stems.")
H('169.d.13.B',3,"A slow string section in a film scene usually conveys:",
  "Sadness or reflection",["Excitement","Comedy","Chaos"],"Music and emotion.")
H('169.d.13.B',4,"Adding the sound of footsteps on gravel to a quiet scene:",
  "Creates realism and atmosphere",["Reduces story","Removes mood","Hides action"],"Sound effects.")
H('169.d.13.C',3,"Reverb is used to create the sense of:",
  "A space or room",["A color","A taste","A temperature"],"Technical elements.")
H('169.d.13.C',4,"Panning a sound to the left speaker makes it seem to come from the:",
  "Left side of the stereo image",["Right side","Back only","Top only"],"Audio effects.")
H('169.d.13.D',3,"MP3 and AAC are examples of:",
  "Compressed audio formats",["Lighting formats","Camera lenses","Printed formats"],"Codecs.")
H('169.d.13.D',4,"A lossless codec such as FLAC differs from MP3 because it:",
  "Preserves all original audio data",["Discards data","Cannot play","Is smaller always"],"Compression standards.")
H('169.d.14.A',3,"An audio script for a radio commercial should include:",
  "Spoken lines and cues for music or effects",["Camera angles","Set design","Costume notes"],"Audio script elements.")
H('169.d.14.A',4,"Timing marks in a radio script help the engineer:",
  "Keep the spot to the required length",["Add a visual","Hide mistakes","Skip lines"],"Script elements.")
H('169.d.14.B',3,"Writing for the ear means using:",
  "Short, clear sentences",["Long, complex ones","Silent text","Footnotes"],"Writing audio scripts.")
H('169.d.14.B',4,"A good audio script reads aloud:",
  "Naturally and clearly",["Awkwardly","With hidden meaning","With no pauses"],"Audio script writing.")
H('169.d.14.C',3,"Audio assets can be obtained by recording, synthesizing, or:",
  "Licensing from a library",["Painting","Printing","Weaving"],"Audio assets.")
H('169.d.14.C',4,"Creating a sound effect by synthesizing it differs from recording it because it:",
  "Is generated electronically rather than captured from the real source",["Requires no software","Cannot be edited","Always sounds identical"],"Audio asset creation.")
H('169.d.15.A',3,"Importing a stereo WAV file into a DAW is an example of:",
  "Bringing audio content into a project",["Deleting tracks","Muting a mic","Printing a mix"],"Record or import audio.")
H('169.d.15.A',4,"Recording a vocal while listening to a backing track uses:",
  "Overdubbing",["Mastering","Bouncing","Rendering video"],"Recording content.")
H('169.d.15.B',3,"A track dedicated to guitar is an:",
  "Instrument track",["Master bus","Video track","Plug-in"],"Audio tracks.")
H('169.d.15.B',4,"A track that hosts a reverb effect shared by several instruments is an:",
  "Auxiliary or effects track",["Mic track","Video track","Master only"],"Track types.")
H('169.d.15.C',3,"Trimming the silence from the start of a clip uses:",
  "An audio editing tool",["A lens","A fader on a lamp","A paint brush"],"Editing tools.")
H('169.d.15.C',4,"A crossfade between two clips helps to:",
  "Smooth the transition and avoid clicks",["Create a pop","Delete a clip","Raise volume"],"Transitions.")
H('169.d.15.D',3,"A plug-in such as EQ or a compressor is used to:",
  "Process audio in a DAW",["Print a poster","Charge a phone","Cook food"],"Plug-ins.")
H('169.d.15.D',4,"A de-esser reduces:",
  "Harsh sibilance in vocals",["Bass","Reverb","Stereo width"],"Software plug-ins.")
H('169.d.15.E',3,"Automation in a DAW lets you:",
  "Program changes like volume over time",["Delete a session","Remove tracks","Disable plug-ins"],"Automation.")
H('169.d.15.E',4,"Automating a fader to rise at the chorus makes the section feel:",
  "Bigger and louder",["Smaller","Silent","Muddy"],"Software automation.")
H('169.d.15.F',3,"After mixing, audio can be delivered on disc, for broadcast, or for:",
  "Streaming services",["Printing","Painting","Cooking"],"Delivery formats.")
H('169.d.15.F',4,"A podcast producer delivers an MP3 with proper:",
  "Loudness and metadata",["Pixels","Fonts","Cables"],"Delivery.")

H('168.d.9.B',5,"A studio wants to use a famous brand's logo in a client's promo video without asking the owner. The main legal risk is:",
  "Trademark infringement",["Fair weather","Frame drops","Lens flare"],"Trademark.")
H('168.d.9.C',5,"A producer wants to remix a pop song for a paid ad. Respecting the song's rights holders means first:",
  "Obtaining a license for the commercial use",["Changing the key only","Posting it unlabeled","Lowering the volume"],"Respect IP.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'cte_28.jsonl'))

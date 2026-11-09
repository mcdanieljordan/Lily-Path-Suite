import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('117.317.', 1030, own='hs_theatre3.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('c.1.A',3,"A company member designs a pre-show routine that raises energy, loosens the voice and focuses the ensemble. She is applying what?",
  "Preparation and warm-up techniques effectively",["Ticket policies","Costume budgets","Set storage"],"Effective warm-ups prepare body, voice and mind.")
H('c.1.A',3,"Why might an ensemble add a focus game to the warm-up before a tense scene?",
  "To sharpen concentration and group connection",["To reduce rehearsal","To skip notes","To avoid blocking"],"Focus games unify the cast.")
H('c.1.B',3,"An actor tries walking a scene at three different tempos and with different centers of gravity to see what feels true. She is doing what?",
  "Experimenting with stage movement",["Painting scenery","Copying a film","Skipping rehearsal"],"Experimentation finds expressive choices.")
H('c.1.B',3,"Which choice is an experiment with stage movement?",
  "Trying the same line while crossing, then while standing still",["Memorizing a different play","Changing the lighting cue","Repainting a flat"],"Testing movement options reveals meaning.")
H('c.1.C',3,"An actor lifts her pitch at the end of a line to show uncertainty. This vocal technique is ___.",
  "Inflection",["Projection","Diction","Cueing"],"Inflection is change in pitch.")
H('c.1.C',3,"Which technique helps lines carry to the last row without shouting?",
  "Projection supported by breath",["Mumbling","Speaking into the floor","Holding the breath"],"Projection uses support, not volume alone.")
H('c.1.D',4,"A student argues that a play's tragic ending results from the hero's fatal flaw. She is evaluating its ___.",
  "Dramatic structure and genre",["Costume budget","Playbill order","Ticket pricing"],"Hamartia is a tragic feature.")
H('c.1.D',4,"Which structural element marks the turning point of a play?",
  "The climax",["The playbill","The strike","The preset"],"The climax is the high point and turn.")
H('c.1.E',3,"A soliloquy on stage is replaced in film by a close-up voice-over. This shows differences in what?",
  "Theatrical conventions across media",["Costume sizes","Seat prices","Lobby design"],"Media use different conventions.")
H('c.1.E',3,"Which convention is distinctive to film rather than live theatre?",
  "Editing between camera shots",["Live audience presence","Curtain call","Intermission"],"Editing is a film technique.")
H('c.1.F',4,"A critic notes that the production's costumes, lighting and sound all reinforced the same theme. She is evaluating what?",
  "The interdependence of theatrical elements",["Seat comfort","Ticket cost","Parking"],"Elements work together.")
H('c.1.F',4,"Which situation shows interdependence of theatrical elements?",
  "A fog effect changes how lighting and costume colors read",["A program is misprinted","A ticket is sold","A seat is empty"],"One element alters another.")
H('c.1.G',3,"A cast member records her scene partner's lines and plays them back while rehearsing her responses. She is practicing what?",
  "Memorization skills",["Costume changes","Poster design","Ticket sales"],"Recorded cues aid memorization.")
H('c.1.G',3,"Why do actors learn lines in the context of action?",
  "Movement and intention help anchor memory",["It slows learning","It confuses cues","It removes feeling"],"Action supports recall.")
H('c.2.A',3,"Before a scene that demands screaming, an actor works with the director on a technique that protects her voice. She is using what?",
  "Safe, appropriate techniques for vocal expression",["Careless habits","Strain","Silence"],"Safe vocal technique prevents injury.")
H('c.2.A',3,"Which approach supports emotional safety in an intense rehearsal?",
  "Agreeing on check-ins and a way to pause",["Ignoring discomfort","Pushing through every limit","Rehearsing in secret"],"Check-ins protect well-being.")
H('c.2.B',4,"An ensemble notices that audiences lean forward when the cast moves in unison. The group is analyzing creativity and its what?",
  "Effect on the audience",["Cost to the box office","Weight of the set","Length of the run"],"Creative choices affect audiences.")
H('c.2.B',4,"Which question analyzes how a creative choice affects an audience?",
  "How did the sudden blackout change the audience's reaction?",["How long was the line?","What did tickets cost?","Where did crew park?"],"Reaction to choices matters.")
H('c.2.C',3,"A student compares a naturalistic character with a highly stylized commedia character, noting differences in physicality. She is analyzing what?",
  "Characters from various genres and styles",["Costume sizes","Box office hours","Seat maps"],"Analysis spans styles.")
H('c.2.C',3,"Which detail describes a character's emotional attributes?",
  "She hides her fear behind a confident smile",["She is five feet tall","She wears boots","She carries a bag"],"Emotions are internal traits.")
H('c.2.D',3,"A group tries the same scene improvised, then scripted, then in a heightened style, to find believable choices. They are experimenting with what?",
  "Improvisation and scripted scenes of various styles",["Painting a mural","Reading a playbill","Selling tickets"],"Varied approaches build believability.")
H('c.2.D',3,"What makes an improvised character believable?",
  "Specific wants, history and consistent choices",["Random shouting","No reaction","Copying a movie scene"],"Specifics create believability.")
H('c.2.E',4,"A playwright writes a line in which a nervous character reveals her secret while also telling the audience what happened before the scene. The dialogue does what?",
  "Reveals motivation and provides exposition",["Describes lighting","Lists the cast","Sets ticket prices"],"Dialogue can serve several functions.")
H('c.2.E',4,"Which feature makes dialogue advance the plot?",
  "A line that changes what a character wants or does next",["A line about the weather","A repeated greeting","A long stage direction"],"Plot-advancing dialogue shifts events.")
H('c.2.F',3,"A group combines live music, projected images and movement in one scene. They are doing what?",
  "Integrating two or more art or media forms",["Avoiding collaboration","Reciting lines only","Using one medium"],"Multimedia work blends forms.")
H('c.2.F',3,"Which pairing integrates art forms in a performance?",
  "Dance with spoken poetry and live percussion",["A script alone","A seating chart","A ticket booth"],"Combining forms enriches meaning.")
H('c.3.A',3,"A student experiments with a gel color on a spotlight during an improvised scene to see how mood changes. She is doing what?",
  "Experimenting with technical elements safely and effectively",["Ignoring tech","Damaging equipment","Skipping safety"],"Safe experiments inform design.")
H('c.3.A',3,"Before hanging a light, a student should do what?",
  "Check the safety cable, clamps and power off",["Hang it quickly","Skip checking","Stand on a chair"],"Safe rigging prevents accidents.")
H('c.3.B',4,"A designer analyzes a script's setting, themes and cultural context to determine the set's style. She is treating the text as what?",
  "A basis for technical discussions",["A distraction","A puzzle only","A budget"],"Texts guide design.")
H('c.3.B',4,"Why should a designer consider a play's themes when choosing color palettes?",
  "Color can reinforce the message and mood",["Color is unimportant","Themes never matter","Color is random"],"Design supports theme.")
H('c.3.C',3,"A student casts two actors in a duet scene and guides them through blocking and character choices. She is doing what?",
  "Casting and directing a duet scene",["Selling tickets","Painting the set","Designing posters"],"Directing includes casting and staging.")
H('c.3.C',3,"When casting a duet scene, a director should consider what?",
  "Chemistry and range suited to the roles",["Only height","Only hair color","Only seat location"],"Casting considers fit and chemistry.")
H('c.3.D',3,"A student serves as lighting designer for a one-act, choosing cues with the director. She is doing what?",
  "Performing a role in production decisions",["Watching","Ignoring","Selling"],"Roles shape production decisions.")
H('c.3.D',3,"The costume designer's chief task is to do what?",
  "Create costumes that fit the characters and concept",["Operate the sound board","Direct actors","Write dialogue"],"Costume design supports story.")
H('c.3.E',3,"A student stage manager keeps a calm tone, calls cues accurately and solves a missing-prop crisis. She is showing what?",
  "Responsibility, artistic discipline and creative problem solving",["Panic","Avoidance","Disorder"],"Reliable calm supports a show.")
H('c.3.E',3,"Artistic discipline means doing what?",
  "Showing up prepared and committing to the work",["Skipping when tired","Missing notes","Ignoring the schedule"],"Discipline sustains quality.")
H('c.4.A',4,"A student evaluates how the Harlem Renaissance shaped plays of its time. She is evaluating what?",
  "Historical and cultural influences on theatre",["A set malfunction","A casting error","A ticket price"],"Culture shapes theatre.")
H('c.4.A',4,"Evaluating the influence of the Industrial Revolution on stage technology involves what?",
  "Considering how new machinery changed staging",["Ignoring technology","Counting seats","Selling playbills"],"Technology shaped staging.")
H('c.4.B',3,"A student observes that actors in commercials, series and school plays use similar emotional tools. This shows what?",
  "Theatre, television and film influence daily life",["Isolation","Silence","No overlap"],"Acting appears across media.")
H('c.4.B',3,"Which example shows media influencing daily life?",
  "Slang from a popular show entering everyday speech",["A bare stage","A closed theatre","An empty seat"],"Media shape language.")
H('c.4.C',4,"A group performs a scene live, films it, then compares audience reactions to each. They are employing and evaluating the impact of what?",
  "Live theatre and film in contrasting contexts",["Seat cushions","Ticket sales","Lobby art"],"Contexts change impact.")
H('c.4.C',4,"Which advantage does a film version have over live performance?",
  "Close-ups can show subtle facial expressions",["A shared live space","Live audience reactions","Real-time risk"],"Film can magnify detail.")
H('c.4.D',3,"A student researches how Sanskrit drama and Chinese opera influenced theatre. She is researching what?",
  "World drama and its influences",["Costume sizing","Parking","Ticket sales"],"World theatre shapes practice.")
H('c.4.D',3,"Which Greek playwright wrote Antigone?",
  "Sophocles",["Molière","Shakespeare","Ibsen"],"Sophocles wrote Antigone.")
H('c.4.E',3,"A student investigates the contributions of Latino playwrights to U.S. theatre. She is researching what?",
  "The multicultural heritage of drama in the United States",["One genre only","Ancient theatre only","Costume history only"],"U.S. theatre includes many heritages.")
H('c.4.E',3,"Which dramatist wrote Zoot Suit, a landmark Chicano play?",
  "Luis Valdez",["Neil Simon","August Wilson","Arthur Miller"],"Valdez wrote Zoot Suit.")
H('c.4.F',3,"The Federal Theatre Project of the 1930s is an example of what?",
  "A U.S. contribution to the performing arts",["A European tradition","An ancient ritual","A film studio"],"It was a U.S. program supporting theatre.")
H('c.4.F',3,"Which American form combines song, dance and story on Broadway?",
  "The musical",["Kabuki","Noh","Passion play"],"The musical is a U.S. innovation.")
H('c.5.A',2,"A student compares behavior at a rock concert and at a quiet recital, then chooses behavior that fits each. She is doing what?",
  "Practicing appropriate audience etiquette",["Ignoring context","Disrespecting performers","Acting randomly"],"Etiquette depends on the event.")
H('c.5.A',2,"Why is etiquette different for a school assembly and a formal play?",
  "Each event has its own expectations",["Etiquette never changes","Rules are random","Only actors matter"],"Different events call for different behavior.")
H('c.5.B',3,"A student describes how a role pushed her to grow as a performer and where she wants to improve next. She is doing what?",
  "Evaluating herself as a creative being",["Avoiding reflection","Copying others","Ignoring feedback"],"Self-evaluation builds artistry.")
H('c.5.B',3,"What makes theatre count as an art form rather than only a pastime?",
  "It uses creative expression to communicate ideas and emotions",["It sells snacks","It involves no communication","It requires no practice"],"Art communicates meaning.")
H('c.5.C',4,"A student applies a rubric about clarity of storytelling and use of design to review a film and a school play. She is applying what?",
  "Concepts of evaluation to different performances",["Gossip","Guessing","Ignoring criteria"],"Evaluation uses criteria.")
H('c.5.C',4,"Which statement applies evaluation concepts to a TV drama?",
  "The editing rhythm heightened tension in the chase sequence",["It was fine","I do not know","It was on late"],"Specific evaluation cites technique.")
H('c.5.D',4,"A student contrasts how a story is told in a play, a painting and a dance. She is comparing what?",
  "Communication methods across art forms",["Ticket prices","Seat counts","Parking rules"],"Each form communicates differently.")
H('c.5.D',4,"Which feature is unique to theatre compared with a painting?",
  "Live performers conveying story over time",["A fixed canvas","A static image","Brush texture"],"Theatre unfolds in time.")
H('c.5.E',3,"A student weighs pay, training and job outlook for being a lighting designer or drama teacher. She is doing what?",
  "Making judgments about career opportunities",["Ignoring options","Guessing","Avoiding research"],"Judging careers uses evidence.")
H('c.5.E',3,"Which factor should be weighed when judging a theatre career?",
  "Training required and job availability",["Favorite color","Shoe size","Weather forecast"],"Career choices rely on realistic factors.")
H('c.5.F',3,"A student builds a website with a research paper, rehearsal videos and journals about her theatre work. She is using what?",
  "Technology to document and present theatre experiences",["A paper airplane","A coupon","A lighting gel"],"Portfolios present experiences.")
H('c.5.F',3,"Which is a strong use of a digital theatre journal?",
  "Recording reflections and goals after each rehearsal",["Storing coupons","Hiding scripts","Deleting notes"],"Journals track growth.")
H('c.5.G',3,"Collaboration, communication and problem solving learned in theatre are valued in which setting?",
  "College and many careers",["Only theatres","Nowhere","Only schools"],"These skills transfer.")
H('c.5.G',3,"How might theatre training help a future lawyer?",
  "It builds confident public speaking and persuasion",["It teaches carpentry","It prevents reading","It removes research"],"Speaking skills transfer to law.")
H('c.5.H',3,"A student compiles a one-page list of her roles, crew jobs and training. She is creating a ___.",
  "Theatre resume",["Set model","Ticket stub","Cue sheet"],"Resumes summarize experience.")
H('c.5.H',3,"Which belongs in a personal theatre portfolio?",
  "Headshot, resume and performance clips",["Receipts","Weather logs","Bus schedules"],"Portfolios document experience.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_theatre3.jsonl'))

#!/usr/bin/env python3
"""Kindergarten Health Education (TEKS 115.12.b) - original questions, hand written."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lines import load
B = Bank('115.12.b.', 930, own='gk_health.jsonl')

load(B, """
1|2|Which body part pumps blood around your body?|heart|elbow|toe|ear|The heart pumps blood.
1|2|Which body part helps you breathe air in and out?|lungs|knees|hair|teeth|Lungs take in air.
1|2|Which body part helps you think and feel?|brain|toe|elbow|hair|The brain controls the body.
1|2|Which body part do you use to chew food?|teeth|ears|elbows|toes|Teeth break up food.
2.A|2|Who is a trusted adult who can help you when you feel sick?|a parent or a school nurse|a stranger on the street|a toy|a pet rock|Trusted adults give health help.
2.A|2|If you do not feel well at school, you should tell...|your teacher|nobody|a stranger|the wall|Teachers can get you help.
2.B|2|Which habit helps keep your teeth healthy?|brushing twice a day|eating candy all day|never brushing|sharing toothbrushes|Brushing removes germs and food.
2.B|2|When should you wash your hands?|before you eat and after using the bathroom|only on holidays|never|only on Mondays|Washing stops germs from spreading.
2.B|2|What do you use with water to wash your hands well?|soap|sand|mud|glue|Soap helps remove germs.
2.C|2|Germs can spread when someone...|coughs without covering their mouth|waves hello|smiles|reads a book|Coughs spread germs through the air.
2.C|2|A good way to cover your cough is to cough into your...|elbow|bare hand|friend's face|food|An elbow keeps germs from spreading.
2.C|2|A shot from a doctor that helps protect you from certain sicknesses is called a...|vaccine|snack|toy|book|Vaccines help prevent disease.
2.D|2|If you see tiny bugs in your hair that make your head itch, tell...|a grown-up or the nurse|a stranger|your pet|the wall|Adults know how to treat lice.
2.D|2|After a mosquito bites you, you can help stop the itching by...|telling a grown-up and washing the bite|scratching hard|eating more bugs|ignoring it forever|Clean bites and tell an adult.
3.A|2|Feeling happy, sad, or mad are all...|feelings|foods|toys|colors|Feelings are emotions.
3.A|2|When you smile and laugh at a party, you are likely feeling...|happy|angry|sleepy|hungry|Smiling shows happiness.
3.B|2|Taking slow, deep breaths can help you feel...|calm|angrier|louder|dizzy all day|Deep breaths relax your body.
3.B|2|When you feel mad, a good calm-down idea is to...|count to ten|hit someone|throw things|yell|Counting helps you pause.
3.C|2|A friend can influence you. A good friend would encourage you to...|do something kind|do something unsafe|tease others|break rules|Good friends encourage good choices.
3.D|2|To make a new friend, you can say...|"Hi, my name is ... Do you want to play?"|"Go away."|nothing and hide|"You can't play."|Friendly words start friendships.
3.E|2|Showing respect when talking to someone means you...|listen and use kind words|interrupt|shout|ignore them|Respect includes listening.
3.F|2|If you and a friend want the same toy, you can...|take turns|grab it|yell|hit|Sharing solves problems.
4.A|2|Telling the truth shows the quality of being...|honest|sneaky|mean|silly|Truth-telling is honesty.
4.A|2|Being kind means you...|help and speak nicely|push others|ignore friends|tease|Kindness helps others.
4.B|2|A goal is something you...|want to do or get better at|forget|lose|throw away|Goals are things you work toward.
4.B|2|A healthy goal for a kindergartner could be...|brush my teeth every night|stay up all night|eat only sweets|skip lunch|Healthy goals support good habits.
5|2|When you feel very worried, who can you talk to?|a trusted adult|nobody|a stranger|a toy only|Trusted adults can help.
5|2|When you feel sad, a helpful thing to do is...|talk about it with someone you trust|keep it a secret forever|yell|hit a wall|Sharing feelings helps.
6.A|2|What do you need to drink every day to stay healthy?|water|soda only|candy|nothing|Water keeps your body working.
6.A|2|Your body is made mostly of...|water|candy|sand|paper|The human body is mostly water.
6.B|2|A healthy portion of a snack is...|a small handful|a giant bucket|a whole cake|ten bags|Small portions are healthy.
6.C|2|Which food helps your body grow strong?|vegetables and fruits|candy|soda|chips|Fruits and vegetables help growth.
6.C|2|Milk, cheese, and yogurt are foods in which group?|dairy|vegetable|meat|grain|Dairy comes from milk.
6.C|2|Which group includes chicken, eggs, and beans?|protein|dairy|fruit|candy|Protein builds muscles.
6.D|2|Which is a healthy snack?|apple slices|candy bar|soda|cookies only|Fruit is a healthy snack.
6.D|2|Which is an unhealthy snack?|a bag of candy|carrot sticks|banana|cheese|Candy has lots of sugar.
7.A|2|If a friend has a food allergy, you should not...|share your food with them|ask what they can eat|wash your hands|be kind|Sharing food can cause harm.
7.A|2|Respecting someone with a food allergy means you...|do not tease them|laugh|trade food with them|tell them to eat it|Respect keeps everyone safe.
7.B|2|Which habit helps you stay healthy?|getting enough sleep|staying up all night|never moving|skipping meals|Sleep helps your body rest.
7.B|2|Playing outside every day helps your...|body stay strong|bed|toys|crayons|Active play builds strength.
8.A|2|If there is an emergency, you should tell...|a trusted adult right away|nobody|a stranger|your pet|Adults can call for help.
8.A|2|In an emergency, a grown-up may call...|911|your friend|your toy|a restaurant|911 connects to emergency help.
8.B|2|A seat belt in a car helps...|keep you safe in a crash|make the car faster|play music|clean the car|Seat belts protect riders.
8.B|2|When riding a bike, you wear a...|helmet|swimsuit|blindfold|scarf|Helmets protect heads.
8.B|2|A booster seat helps a young child...|sit high enough for the seat belt to fit|play games|sleep|stand|Boosters make the belt fit.
9.A|2|A trusted adult is someone who...|helps keep you safe|hurts you|is a stranger|asks you to keep secrets|Trusted adults keep kids safe.
9.A|2|Which person is likely a trusted adult?|your teacher|someone you just met online|a stranger at the park|a person who offers candy|Teachers are trusted.
9.B|2|If someone asks you to do something unsafe, you can say...|"No!" and tell a trusted adult|"Okay"|nothing|"Maybe"|Saying no protects you.
9.C|2|Personal space is...|the space around your body|the whole room|a toy|a car|Personal space is your own area.
9.C|2|Appropriate boundaries mean...|you decide who touches you|everyone can touch you|you must hug everyone|you keep secrets|Your body belongs to you.
10.A|2|Which is a safe place to play?|a fenced playground with grown-ups|a busy road|a parking lot|a construction site|Safe places keep you protected.
10.B|2|Which object can be dangerous for a young child?|scissors|a pillow|a book|a crayon|Sharp objects can cut.
10.B|2|If you find a knife, you should...|not touch it and tell an adult|play with it|hide it|throw it|Tell a grown-up.
10.C|2|You should know your home...|address|favorite color|snack|pet's name only|Knowing your address helps in emergencies.
11|2|If you see something online that scares you, you should...|tell a trusted adult|keep it secret|click more|share it|Adults can help.
11|2|Before using a tablet, you should ask...|a parent or teacher|a stranger|nobody|the wall|Grown-ups supervise screen time.
12.A|2|Bullying is when someone...|is mean to another on purpose again and again|helps a friend|shares a toy|says hello|Bullying is repeated unkind behavior.
12.A|2|A bystander is someone who...|sees bullying happen|does the bullying|is the one bullied|is a teacher|Bystanders can help.
12.B|2|You can discourage bullying by...|being kind and telling an adult|joining in|laughing|watching quietly|Kindness stops bullying.
12.C|2|If someone bullies you, you should...|tell a parent or trusted adult|hit back|keep it secret|run away forever|Adults can help.
12.D|2|If someone makes you feel unsafe or uncomfortable, you should...|get help from a trusted adult|keep quiet|hide|pretend nothing happened|Tell someone you trust.
13.A|2|Medicine should be taken only when...|a parent or doctor says it is okay|you feel like it|a friend gives it|you find it|Medicine must be given by a trusted adult.
13.A|2|If you find a pill on the floor, you should...|not touch it and tell an adult|eat it|hide it|share it|Unknown pills can harm.
13.B|2|Smoking is harmful because it hurts your...|lungs|elbows|hair|toes|Smoke harms the lungs.
13.B|2|Which is unsafe for children?|alcohol|water|milk|juice|Alcohol harms the body.
14|2|A person who cares for you and helps you make healthy choices is a...|protective factor|danger|risk|problem|Caring adults protect kids.
14|2|Having a trusted adult to talk to helps you stay...|safe|lonely|worried|hidden|Support keeps you safer.
""")
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'gk_health.jsonl'))
print("saved", len(B.out), "questions")

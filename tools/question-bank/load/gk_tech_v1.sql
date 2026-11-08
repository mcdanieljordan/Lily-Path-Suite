insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'gk_tech_v1'
from (values
('126.1.c.2',2,'You write steps to get a friend to the door: forward, forward, turn, forward. These steps are a...','["sequence of directions", "poem", "song", "picture"]'::jsonb,0,'Code is a list of steps in order.','original'),
('126.1.c.2',3,'In a maze game, you drag blocks that tell the character to move. What are you making?','["a song", "code", "a drawing", "a snack"]'::jsonb,1,'Drag-and-drop blocks make a program.','original'),
('126.1.c.2',3,'Which order of steps is right for getting to the door?','["Jump, then hide, then nap", "Turn, then sleep, then walk", "Walk forward, then turn, then walk forward", "Sing, then sit, then stop"]'::jsonb,2,'Steps must be in the right order.','original'),
('126.1.c.5',2,'You are playing on a tablet and a classmate wants a turn. A responsible thing to do is...','["hide it", "grab it", "yell", "take turns kindly"]'::jsonb,3,'Responsible behavior is kind and fair.','original'),
('126.1.c.5',3,'In an online class, you should speak to others...','["politely", "by shouting", "with mean words", "rudely"]'::jsonb,0,'Be kind online.','original'),
('126.1.c.1.A',2,'To make a sandwich, you first break the job into small...','["clouds", "steps", "toys", "songs"]'::jsonb,1,'Decomposing means breaking into smaller pieces.','original'),
('126.1.c.1.A',3,'Cleaning your room is a big job. Putting books away is one small piece. This is called...','["making a mess", "hiding a job", "breaking a problem into parts", "breaking a toy"]'::jsonb,2,'Decomposing a task.','original'),
('126.1.c.1.B',2,'Sun, moon, sun, moon, sun, ... What comes next?','["the sun again", "a cloud", "a star", "the moon"]'::jsonb,3,'Patterns repeat.','original'),
('126.1.c.1.B',3,'Two claps, one stomp, two claps, one stomp, two claps. You predict what comes next is...','["a single foot stomp", "silence", "three claps", "a jump"]'::jsonb,0,'Use the pattern to predict.','original'),
('126.1.c.1.C',2,'Instructions that tell what to do one step after another are an...','["apple", "algorithm", "animal", "album"]'::jsonb,1,'Algorithms are step-by-step instructions.','original'),
('126.1.c.1.C',3,'Which words help put steps in order?','["cat, dog, fish, bird", "up, down, left, right only", "first, next, then, last", "big, red, soft, fast"]'::jsonb,2,'Sequence words show order.','original'),
('126.1.c.3.A',2,'Listening and following directions helps you...','["lose a project", "skip a project", "forget a project", "do a project well"]'::jsonb,3,'Following directions is a design skill.','original'),
('126.1.c.3.B',3,'Asking questions and drawing a plan before building something is part of a...','["design process", "recess", "snack time", "nap time"]'::jsonb,0,'Design processes include asking and planning.','original'),
('126.1.c.3.B',3,'Drawing pictures of your idea in order before you make it is called...','["erasing", "storyboarding", "sleeping", "hiding"]'::jsonb,1,'A storyboard plans steps in pictures.','original'),
('126.1.c.4.A',2,'Facts that are collected about the weather are called...','["toys", "shoes", "data", "snacks"]'::jsonb,2,'Data is information collected.','original'),
('126.1.c.4.A',3,'Counting how many students picked each fruit gives us...','["a shoe", "a song", "a toy", "data"]'::jsonb,3,'Counting collects information.','original'),
('126.1.c.4.B',2,'A computer can help you look for information. This is called...','["searching", "painting", "dancing", "sleeping"]'::jsonb,0,'Devices can search for information.','original'),
('126.1.c.6.A',2,'The rules for using school computers and tablets tell you how to use them...','["never", "the right way", "any way", "wrong"]'::jsonb,1,'Acceptable use policies set the rules.','original'),
('126.1.c.6.A',3,'Following the acceptable use rules means using school devices...','["for anything", "for games all day", "only for school work and rules", "without asking"]'::jsonb,2,'Use devices as the policy says.','original'),
('126.1.c.6.B',3,'A picture or song online was made by someone. That means it has an...','["ear", "oven", "ocean", "owner"]'::jsonb,3,'Digital content has owners.','original'),
('126.1.c.7.A',2,'To keep your account safe, you should not share your...','["password", "shoes", "pet''s name tag", "favorite color"]'::jsonb,0,'Never share login information.','original'),
('126.1.c.7.A',3,'When you finish using a device, you should...','["tell a friend your password", "log off", "break it", "leave it on and walk away"]'::jsonb,1,'Logging off protects your account.','original'),
('126.1.c.7.B',3,'Which is safe to share online?','["your home address", "your password", "a favorite animal", "your phone number"]'::jsonb,2,'Hobbies and likes are safe; identifying information is not.','original'),
('126.1.c.7.B',3,'Which is NOT safe to share online?','["a favorite food", "a favorite game", "a favorite color", "where you live"]'::jsonb,3,'Do not share identifying information.','original'),
('126.1.c.8.A',2,'A tablet, a laptop and a school website are all ways to...','["learn and do activities", "swim", "sleep", "bake"]'::jsonb,0,'Devices and sites can be used to learn.','original'),
('126.1.c.8.B',2,'A mouse or keyboard that sends information to a computer is an...','["window", "input device", "output device", "sandwich"]'::jsonb,1,'Input devices send information in.','original'),
('126.1.c.8.B',3,'A screen or a printer that shows information from a computer is an...','["input device", "snack", "output device", "bed"]'::jsonb,2,'Output devices show results.','original'),
('126.1.c.8.B',3,'The programs on a computer, like a drawing app, are called...','["a chair", "a desk", "hardware", "software"]'::jsonb,3,'Software is a program.','original'),
('126.1.c.8.C',2,'To use a drawing app, you first...','["open the app", "turn it upside down", "walk away", "close the lid"]'::jsonb,0,'Open the application to use it.','original'),
('126.1.c.8.C',3,'After you make a picture on the computer, you should...','["throw it", "save it", "hide the computer", "forget it"]'::jsonb,1,'Saving keeps your work.','original'),
('126.1.c.8.D',2,'Good keyboarding means sitting...','["slumped over", "on the table", "up tall with feet on the floor", "upside down"]'::jsonb,2,'Ergonomics protects the body.','original'),
('126.1.c.8.D',3,'When you type, your hands should rest...','["on your head", "behind your back", "under the desk", "on the home row keys"]'::jsonb,3,'Good hand position.','original'),
('126.1.c.8.E',2,'The long key at the bottom that makes a space between words is the...','["space bar", "backspace", "enter", "tab"]'::jsonb,0,'The space bar makes spaces.','original'),
('126.1.c.8.E',3,'The key that erases the last letter you typed is the...','["shift", "backspace", "space bar", "caps lock"]'::jsonb,1,'Backspace deletes the previous character.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Technology Applications' and d.language = 'en'
on conflict (fingerprint) do nothing;

insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'gap_pe_v1'
from (values
('116.12.b.7',2,'Which is a fun outdoor activity a kindergartner can do at a park?','["playing on a playground", "watching TV", "sleeping in a closet", "doing homework in bed"]'::jsonb,0,'Parks offer outdoor play.','original'),
('116.12.b.7',2,'When you play outside on a hot day, it is smart to take breaks in the...','["hot sun", "shade", "oven", "car"]'::jsonb,1,'Shade helps you cool down.','original'),
('116.13.b.7',2,'Which outdoor activity is a good way to explore nature with a grown-up?','["sleeping", "staying in a dark room", "walking on a trail", "playing video games"]'::jsonb,2,'Trails show you nature.','original'),
('116.13.b.7',2,'On a nature walk, you should stay on the trail so you...','["pick every flower", "run into traffic", "hide", "do not get lost"]'::jsonb,3,'Trails keep you safe.','original'),
('116.16.b.5',3,'Which dance style uses a group pattern like a line or a square set to music?','["a folk dance", "a nap", "a race", "a quiz"]'::jsonb,0,'Folk dances use set patterns.','original'),
('116.16.b.5',3,'When you keep your movements in time with music, you are showing...','["sleep", "rhythm", "silence", "stillness"]'::jsonb,1,'Rhythm matches the beat.','original'),
('116.16.b.5',3,'A jump rope routine done to music uses...','["random jumping", "no beat", "a rhythm pattern", "a race"]'::jsonb,2,'Routines follow a rhythm.','original'),
('116.17.b.5',4,'A dance routine that repeats steps in a set pattern to music is a...','["nap", "rest", "random shuffle", "choreographed sequence"]'::jsonb,3,'Choreography organizes movement.','original'),
('116.17.b.5',4,'Keeping the tempo of a dance means you...','["move at the speed of the music", "run away", "stop", "move randomly"]'::jsonb,0,'Tempo is the speed of the beat.','original'),
('116.17.b.5',4,'Working with a group to create a rhythmic routine requires...','["ignoring the music", "cooperating and counting beats together", "working alone", "arguing"]'::jsonb,1,'Groups count the beat.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Physical Education' and d.language = 'en'
on conflict (fingerprint) do nothing;

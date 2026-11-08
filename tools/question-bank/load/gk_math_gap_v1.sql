insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'gk_math_gap_v1'
from (values
('111.2.b.4',2,'Which coin is called a penny?','["the brown coin worth 1 cent", "the silver coin worth 10 cents", "the silver coin worth 25 cents", "the silver coin worth 5 cents"]'::jsonb,0,'A penny is brown and worth 1 cent.','original'),
('111.2.b.4',2,'Which coin is the smallest silver coin?','["a nickel", "a dime", "a quarter", "a penny"]'::jsonb,1,'The dime is the smallest silver coin.','original'),
('111.2.b.4',2,'What is the name of the biggest coin you can pay with that is worth 25 cents?','["a nickel", "a dime", "a quarter", "a penny"]'::jsonb,2,'A quarter is worth 25 cents.','original'),
('111.2.b.4',2,'Which coin is a nickel?','["the smallest silver coin", "the coin worth 25 cents", "the brown coin worth 1 cent", "the silver coin worth 5 cents"]'::jsonb,3,'A nickel is worth 5 cents.','original'),
('111.2.b.4',2,'Why do people use coins?','["to pay for things", "to build a house", "to cook food", "to make shadows"]'::jsonb,0,'Coins are money used to buy things.','original'),
('111.2.b.4',3,'A girl has a coin that is brown. What is it?','["a dime", "a penny", "a nickel", "a quarter"]'::jsonb,1,'Only the penny is brown.','original'),
('111.2.b.4',3,'Which group has only coins?','["dime, shell, penny", "penny, button, dime", "penny, nickel, dime", "nickel, key, quarter"]'::jsonb,2,'All three are U.S. coins.','original'),
('111.2.b.5',2,'What number comes next? 10, 20, 30, __','["50", "31", "13", "40"]'::jsonb,3,'Counting by tens adds 10 each time.','original'),
('111.2.b.5',2,'Count by tens. What number is missing? 20, 30, __, 50','["40", "45", "60", "35"]'::jsonb,0,'40 comes between 30 and 50.','original'),
('111.2.b.5',3,'Start at 48. What number comes next when counting by ones?','["47", "49", "58", "50"]'::jsonb,1,'One more than 48 is 49.','original'),
('111.2.b.5',3,'What number comes next? 98, 99, __','["90", "89", "100", "101"]'::jsonb,2,'After 99 comes 100.','original'),
('111.2.b.5',3,'Count by tens from 60. What numbers come next?','["65, 70, 75", "80, 100, 120", "61, 62, 63", "70, 80, 90"]'::jsonb,3,'Adding 10 each time gives 70, 80, 90.','original'),
('111.2.b.5',3,'Which group is counting by ones?','["35, 36, 37, 38", "35, 45, 55, 65", "35, 37, 39, 41", "35, 40, 45, 50"]'::jsonb,0,'Counting by ones goes up one each time.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Mathematics' and d.language = 'en'
on conflict (fingerprint) do nothing;

insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'g8_ela_v2'
from (values
('110.24.b.10.D.i',3,'Which group of words is a run-on sentence?','["The concert ended we walked to the car.", "The concert ended, and we walked to the car.", "The concert ended; we walked to the car.", "After the concert ended, we walked to the car."]'::jsonb,0,'Two independent clauses with no punctuation or conjunction.','original'),
('110.24.b.10.D.i',3,'Which group of words is a fragment?','["Fans stood and clapped.", "Although the pitcher threw a perfect game.", "The crowd cheered the pitcher.", "The pitcher threw a perfect game."]'::jsonb,1,'A dependent clause is not a complete sentence.','original'),
('110.24.b.10.D.i',4,'Which sentence fixes this comma splice? ''The lights flickered, the room went dark.''','["The lights flickered the room, went dark.", "The lights flickered, the room went dark, quickly.", "The lights flickered, and the room went dark.", "The lights, flickered the room went dark."]'::jsonb,2,'A comma plus conjunction joins two independent clauses.','original'),
('110.24.b.9.D',3,'''The old car coughed and groaned up the hill'' is an example of...','["hyperbole", "simile", "an idiom", "personification"]'::jsonb,3,'A machine is given human actions.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'English Language Arts and Reading' and d.language = 'en'
on conflict (fingerprint) do nothing;

"""Turns checked batches into one SQL file that loads them into public.question_bank.
   Usage: python3 qb_sql.py "Mathematics" batch_name out.sql batches/g3_math.jsonl [more.jsonl]
   The SQL looks each TEKS code up in teks_items (so the link is real), skips questions already in the bank, and marks them 'checked'."""
import sys, json
from qb_check import check_files
def q(s): return "'" + str(s).replace("'", "''") + "'"
subject, batch, out, files = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
items, bad, warn = check_files(files)
if bad: sys.exit("fix the failures first: " + str(bad[:3]))
vals = []
for _, it in items:
    vals.append("(%s,%d,%s,%s::jsonb,%d,%s,%s)" % (q(it['c']), it['d'], q(it['q']), q(json.dumps(it['o'], ensure_ascii=False)), it['a'], q(it['e']), q(it.get('src', 'original'))))
CHUNK = 150
with open(out, 'w', encoding='utf8') as f:
    for i in range(0, len(vals), CHUNK):
        f.write(f"""insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', {q(batch)}
from (values
{(","+chr(10)).join(vals[i:i+CHUNK])}
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = {q(subject)} and d.language = 'en'
on conflict (fingerprint) do nothing;
""")
print(f"wrote {out}: {len(vals)} questions in {-(-len(vals)//CHUNK)} statement(s)")

# Zynth question bank

Original, TEKS-tagged practice questions for every Zynth app (Battleship Jeopardy first). They live in the Supabase table
`public.question_bank` (project `aiczpuoskwzqtzvoomll`). Anyone can read checked questions; only the owner can write.

No released STAAR items are copied here. Released tests and blueprints are used only as a private map of what gets tested.

## Files
- `schema.sql` – creates the table, its read-only security rule and the `question_bank_coverage` view. Run once in the Supabase SQL editor.
- `gen/*.py` – question writers. `python3 gen/g3_math.py` rebuilds `batches/g3_math.jsonl` (same seed = same file). Same for `gk_math.py`, `g1_math.py`, `g2_math.py`, `g4_math.py` and `g5_math.py`, and for the Science writers `gk_science.py`, `g1_science.py` … `g5_science.py` (hand-written, 7 questions per content standard); `gen/common.py` holds the shared helpers.
- `qb_check.py` – checks a batch (math answers recomputed, no duplicates, one right answer, answer not given away, no two choices with the same value). Exit code 1 = fix first.
- `qb_sql.py` – turns a checked batch into the SQL in `load/`. Usage: `python3 qb_sql.py "Mathematics" g3_math_v1 load/g3_math_v1.sql batches/g3_math.jsonl`
- `load/*.sql` – ready-to-run inserts. Safe to run twice (duplicates are skipped).

## One question per line (JSONL)
`{"c":"111.5.b.3.A","d":2,"q":"prompt","o":["A","B","C","D"],"a":0,"e":"why","chk":"optional python that must equal the right option"}`
`d` is difficulty 1-5 (the five board rows use 3,2,3,4,2: row 1 comes from the grade below, row 5 previews the grade above).

## Status
- Math, status `checked` (script-verified, not yet teacher-verified): Kindergarten = 181 questions / 27 standards, Grade 1 = 279 / 43, Grade 2 = 189 / 33, Grade 3 = 255 / 46, Grade 4 = 241 / 41, Grade 5 = 410 / 39. Total 1,555 across 229 standards.
- A few generated questions repeated an existing prompt (e.g. "Which number is odd?") and were skipped on load; the bank never holds two questions with the same prompt text.
- Science, status `checked`: Kindergarten = 112 questions / 16 standards, Grade 1 = 147 / 21, Grade 2 = 154 / 22, Grade 3 = 154 / 22, Grade 4 = 140 / 20, Grade 5 = 133 / 19, Grade 6 = 168 / 24 (`g6_science_v1`, commit 3c24309), Grade 7 = 175 / 25 (`g7_science_v1`, commit 63b8847), Grade 8 = 165 / 24 (`g8_science_v1`, commit 478ad03). Total 1,348 across 193 standards (content strands 6-13; strands 1-5 are practices and themes, not written). Anon read access confirmed.
- Math gap fill (K coins and counting) added 13 questions: K = 194 / 29. Math total is now 1,568 across 231 standards.
- ELA (English Language Arts and Reading), status `checked`: Kindergarten = 140 questions / 76 standards, Grade 1 = 120 / 74, Grade 2 = 108 / 75, Grade 3 = 111 / 77, Grade 4 = 97 / 74, Grade 5 = 104 / 72, Grade 6 = 152 / 50 (`g6_ela_v1`, commit eabc3a4), Grade 7 = 151 / 51 (`g7_ela_v1`, commit eb302aa), Grade 8 = 142 + 4 / 50 (`g8_ela_v1` commit f288304, `g8_ela_v2` supplement commit d70efcd). Total 1,129. Skipped on purpose because multiple choice cannot test them: speaking and listening (strand 1), independent reading and fluency (4-5), research (12-15 depending on grade), and the writing-process steps that are projects (drafting, sharing). Foundational skills (decoding, spelling, alphabetizing, plurals) are covered by the `gen/gap_ela.py` gap-fill batch. Anon read access confirmed: 680 ELA, 1,568 Math, 840 Science.
- Social Studies (K-5), status `checked`: Kindergarten = 72 questions, Grade 1 = 75, Grade 2 = 70, Grade 3 = 73, Grade 4 = 111 (Texas history), Grade 5 = 126 (U.S. history), plus a 19-question gap fill (`gen/gap_ss.py`) for skills standards (facts, oral/written/visual communication, civil discourse). Total 546; every leaf standard K-5 now has at least one question. Skipped: nothing assessable.
- Physical Education (K-5, TEKS 116.12-116.17), status `checked`: Kindergarten = 61 questions, Grade 1 = 69, Grade 2 = 62, Grade 3 = 59, Grade 4 = 61, Grade 5 = 57, plus a 10-question gap fill (`gen/gap_pe.py`) for outdoor pursuits and rhythmic activities. Total 379; every leaf standard K-5 has at least one question. These test knowledge (technique cues, safety, fitness vocabulary, sportsmanship); the movement itself cannot be tested by multiple choice.
- Health Education (K-5, TEKS 115.12.b-115.17.b), status `checked`: Kindergarten = 67 questions, Grade 1 = 94, Grade 2 = 98, Grade 3 = 108, Grade 4 = 127, Grade 5 = 142. Total 636; every leaf standard K-5 has at least one question (checked 2026-11-08: 0 uncovered). Topics include body systems, hygiene and germs, emotions and relationships, nutrition, safety, digital citizenship, bullying, alcohol/tobacco/drugs and (Grades 4-5) puberty, reproduction and personal boundaries, all worded for children.
- Fine Arts (K-5, Art/Music/Theatre, TEKS 117.102-117.119), status `checked`: Kindergarten = 62 questions (43 standards), Grade 1 = 69 (50), Grade 2 = 80 (51), Grade 3 = 81 (54), Grade 4 = 86 (61), Grade 5 = 89 (61). Total 467; every leaf standard K-5 has at least one question (checked 2026-11-08: 0 uncovered). Knowledge only: elements of art and principles of design, media, careers, instrument families, tempo/dynamics/form and notation, theatre terms, audience behaviour and playmaking. Use `Bank('117.', seed)` with relative codes like `105.b.1.A`.
- Bank total: 7,722 questions readable by anon (Math 2,646, Science 1,348, ELA 1,129, Social Studies 886, Physical Education 379, Health Education 636, Fine Arts 467, Technology Applications 231). Math 6-8 is finished: Grade 6 = 469 (`g6_math_v1`, 52 standards, commit 3f81db7), Grade 7 = 254 (`g7_math_v1`, 43 standards, commit a9edfc5), Grade 8 = 355 (`g8_math_v1`, 44 standards, commit b840a40). Every K-5 leaf is covered in all 8 subjects, and every leaf standard in Math 6-8 and in the Science content strands 6-8.
- Social Studies 6-8 is finished: Grade 6 = 115 (`g6_ss_v1`, 66 standards, commit 7f2cb4c), Grade 7 = 102 (`g7_ss_v1`, 71, commit fed0486), Grade 8 = 123 (`g8_ss_v1`, 97, commit b2371e0); total Social Studies 886.
- Next (in order): PE, Health and Tech for grades 6-8, then high school, then the obscure TEKS.
- Battleship reads the bank already (commit 706637e) and falls back to its built-in questions when the table is missing or empty.

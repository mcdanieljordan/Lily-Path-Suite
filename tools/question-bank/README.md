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
- Science, status `checked`: Kindergarten = 112 questions / 16 standards, Grade 1 = 147 / 21, Grade 2 = 154 / 22, Grade 3 = 154 / 22, Grade 4 = 140 / 20, Grade 5 = 133 / 19. Total 840 across 120 standards (content strands 6-13; strands 1-5 are practices and themes, not written). Anon read access confirmed.
- Next (in order): ELA K-5, then Social Studies, PE, Health, Fine Arts, Tech for K-5; then middle school, high school, and the more obscure TEKS. Grade 6 Math (`gen/g6_math.py`, standards 2.A-3.E so far) resumes after K-5 is done.
- Battleship reads the bank already (commit 706637e) and falls back to its built-in questions when the table is missing or empty.

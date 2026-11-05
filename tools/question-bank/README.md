# Zynth question bank

Original, TEKS-tagged practice questions for every Zynth app (Battleship Jeopardy first). They live in the Supabase table
`public.question_bank` (project `aiczpuoskwzqtzvoomll`). Anyone can read checked questions; only the owner can write.

No released STAAR items are copied here. Released tests and blueprints are used only as a private map of what gets tested.

## Files
- `schema.sql` – creates the table, its read-only security rule and the `question_bank_coverage` view. Run once in the Supabase SQL editor.
- `gen/*.py` – question writers. `python3 gen/g3_math.py` rebuilds `batches/g3_math.jsonl` (same seed = same file).
- `qb_check.py` – checks a batch (math answers recomputed, no duplicates, one right answer, answer not given away). Exit code 1 = fix first.
- `qb_sql.py` – turns a checked batch into the SQL in `load/`. Usage: `python3 qb_sql.py "Mathematics" g3_math_v1 load/g3_math_v1.sql batches/g3_math.jsonl`
- `load/*.sql` – ready-to-run inserts. Safe to run twice (duplicates are skipped).

## One question per line (JSONL)
`{"c":"111.5.b.3.A","d":2,"q":"prompt","o":["A","B","C","D"],"a":0,"e":"why","chk":"optional python that must equal the right option"}`
`d` is difficulty 1-5 (the five board rows use 3,2,3,4,2: row 1 comes from the grade below, row 5 previews the grade above).

## Status
- Grade 3 Math: 255 questions, all 46 content standards, status `checked` (script-verified, not yet teacher-verified).
- Battleship reads the bank already (commit 706637e) and falls back to its built-in questions when the table is missing or empty.

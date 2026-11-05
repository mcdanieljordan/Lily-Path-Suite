-- Shared TEKS-tagged question bank for every Zynth app (Battleship Jeopardy first).
-- No student data lives here. Anyone can READ checked questions; only the service role / SQL editor can write.
create table if not exists public.question_bank (
  id            uuid primary key default gen_random_uuid(),
  teks_code     text not null,                       -- official TEKS code, same as teks_items.code
  teks_item_id  uuid references public.teks_items(id) on delete set null,
  subject       text not null,                       -- same names as teks_documents.subject
  grade_num     smallint check (grade_num between 0 and 12),   -- 0 = Kindergarten; null for course-based (high school)
  course        text,                                -- high school course title when there is no grade
  difficulty    smallint not null check (difficulty between 1 and 5),  -- matches the 5 board rows (100..500)
  qtype         text not null default 'mc' check (qtype in ('mc','tf','numeric')),
  prompt        text not null check (length(prompt) between 5 and 600),
  choices       jsonb not null check (jsonb_typeof(choices) = 'array' and jsonb_array_length(choices) between 2 and 4),
  answer_idx    smallint not null check (answer_idx between 0 and 3),
  explanation   text not null default '' check (length(explanation) <= 400),
  source        text not null default 'original' check (source in ('original','generator')),
  status        text not null default 'draft' check (status in ('draft','checked','verified','flagged','retired')),
  gen_batch     text,                                -- which batch wrote it (for undo / audit)
  fingerprint   text generated always as (md5(lower(regexp_replace(prompt, '[^a-zA-Z0-9]', '', 'g')))) stored,
  times_asked   integer not null default 0,
  times_correct integer not null default 0,
  flags         integer not null default 0,
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now(),
  constraint qb_answer_in_range check (answer_idx < jsonb_array_length(choices)),
  constraint qb_unique_prompt unique (fingerprint)
);
comment on table public.question_bank is 'Original, TEKS-tagged practice questions shared by all apps. status: draft -> checked (script checks passed) -> verified (blind second pass agreed). Apps read checked + verified only.';
create index if not exists qb_pick_idx on public.question_bank (subject, grade_num, difficulty) where status in ('checked','verified');
create index if not exists qb_teks_idx on public.question_bank (teks_code);
create index if not exists qb_status_idx on public.question_bank (status);

alter table public.question_bank enable row level security;
drop policy if exists "read checked questions" on public.question_bank;
create policy "read checked questions" on public.question_bank for select to anon, authenticated using (status in ('checked','verified'));
-- no insert/update/delete policies on purpose: writes come only from the service role (loader scripts / SQL editor).

create or replace view public.question_bank_coverage with (security_invoker = true) as
  select subject, grade_num, course, count(*) as questions, count(distinct teks_code) as standards
  from public.question_bank where status in ('checked','verified')
  group by subject, grade_num, course;

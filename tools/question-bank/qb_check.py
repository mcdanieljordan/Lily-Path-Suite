"""Checks question batches (JSON lines) before they go anywhere near the database.
   One question per line: {"c":TEKS code,"d":1-5,"q":prompt,"o":[4 choices],"a":index of right choice,"e":one-line explanation,"chk":optional python expr that must equal the right choice}
   Usage: python3 qb_check.py batches/g3_math.jsonl [more files]   (exit code 1 if anything fails)"""
import sys, json, re, itertools
from fractions import Fraction as F
from collections import Counter

def norm(s): return re.sub(r'[^a-z0-9]', '', str(s).lower())
def onorm(s): return re.sub(r'\s+', '', str(s).lower())   # keeps symbols so '7 × 9' and '7 ÷ 9' differ
def words(s): return set(re.findall(r'[a-z0-9]+', str(s).lower()))
def fr(x):
    x = F(x); return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def check_files(paths, strict_codes=None):
    bad, warn, items, seen = [], [], [], {}
    for p in paths:
        for n, line in enumerate(open(p, encoding='utf8'), 1):
            line = line.strip()
            if not line or line.startswith('#'): continue
            where = f"{p}:{n}"
            try: it = json.loads(line)
            except Exception as e: bad.append((where, f"not JSON: {e}")); continue
            miss = [k for k in ('c', 'd', 'q', 'o', 'a', 'e') if k not in it]
            if miss: bad.append((where, f"missing {miss}")); continue
            o, a = it['o'], it['a']
            if not isinstance(o, list) or not (2 <= len(o) <= 4): bad.append((where, "options must be 2-4")); continue
            if not isinstance(a, int) or not 0 <= a < len(o): bad.append((where, "answer index out of range")); continue
            if it['d'] not in (1, 2, 3, 4, 5): bad.append((where, "difficulty must be 1-5")); continue
            if not (5 <= len(it['q']) <= 600): bad.append((where, "prompt length")); continue
            if len(it['e']) > 400: bad.append((where, "explanation too long")); continue
            if len({onorm(x) for x in o}) != len(o): bad.append((where, f"duplicate options {o}")); continue
            if any(not str(x).strip() for x in o): bad.append((where, "empty option")); continue
            right = str(o[a]).strip()
            if len(norm(right)) >= 4 and norm(right) in norm(it['q']) and not re.fullmatch(r'[\d.,/$%\s-]+', right):
                bad.append((where, f"answer given away in the question: {right!r}")); continue
            if re.search(r'\b(all|none) of the above\b|\bboth [a-d] and [a-d]\b', ' '.join(map(str, o)), re.I):
                bad.append((where, "no 'all/none of the above' style options")); continue
            if it.get('chk'):
                try:
                    v = eval(it['chk'], {'F': F, 'fr': fr, '__builtins__': {'str': str, 'int': int, 'round': round, 'abs': abs, 'sum': sum, 'min': min, 'max': max, 'len': len, 'sorted': sorted, 'range': range, 'float': float}})
                    v = str(v).strip()
                except Exception as e: bad.append((where, f"chk failed to run: {e}")); continue
                if v != right: bad.append((where, f"MATH CHECK: computed {v!r} but key says {right!r}")); continue
                if sum(1 for x in o if str(x).strip() == v) != 1: bad.append((where, "computed value appears more than once among options")); continue
            fp = norm(it['q'])
            if fp in seen: bad.append((where, f"duplicate of {seen[fp]}")); continue
            seen[fp] = where
            items.append((where, it))
    # near-duplicates inside the same standard
    by = {}
    for where, it in items: by.setdefault(it['c'], []).append((where, it))
    for c, lst in by.items():
        for (w1, i1), (w2, i2) in itertools.combinations(lst, 2):
            a, b = words(i1['q']), words(i2['q'])
            if a and b and len(a & b) / len(a | b) > 0.85: warn.append((w2, f"very similar to {w1}"))
    if strict_codes is not None:
        for where, it in items:
            if it['c'] not in strict_codes: bad.append((where, f"TEKS code {it['c']} is not in the standards list"))
    return items, bad, warn

if __name__ == '__main__':
    items, bad, warn = check_files(sys.argv[1:])
    pos = Counter(it['a'] for _, it in items); dif = Counter(it['d'] for _, it in items)
    print(f"{len(items)} questions OK | answer positions {dict(sorted(pos.items()))} | difficulty {dict(sorted(dif.items()))} | standards {len({it['c'] for _, it in items})}")
    for w, m in warn[:20]: print("WARN", w, m)
    for w, m in bad: print("FAIL", w, m)
    sys.exit(1 if bad else 0)

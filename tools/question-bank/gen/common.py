"""Shared helpers for question generators.
   mk() builds one multiple-choice item, shuffles the options, refuses fractions that equal the right answer,
   and keeps a prompt from being added twice. Everything is seeded so a rerun gives the same file."""
import random, json, re
from fractions import Fraction as F

class Bank:
    def __init__(self, prefix, seed, no_neg=False, norm_dup=False):
        self.no_neg = no_neg
        self.norm_dup = norm_dup
        self.P = prefix
        self.R = random.Random(seed)
        self.out = []
        self.seen = set()

    def mk(self, code, d, q, right, wrong, e, chk=None, need=3):
        R = self.R
        right = str(right)
        wrong = list(dict.fromkeys(str(w) for w in wrong if str(w) != right))
        if self.no_neg: wrong = [w for w in wrong if not re.match(r'^-\d', w)]
        fr = re.compile(r'^(\d+)/(\d+)$')
        mr = fr.match(right)
        if mr:   # never leave an equivalent fraction among the wrong answers
            keep = []
            for w in wrong:
                mw = fr.match(w)
                if mw and int(mw.group(2)) and F(int(mw.group(1)), int(mw.group(2))) == F(int(mr.group(1)), int(mr.group(2))):
                    continue
                keep.append(w)
            wrong = keep
        key = re.sub(r'[^a-z0-9]', '', q.lower()) if self.norm_dup else q
        if len(wrong) < need or key in self.seen:
            return False
        opts = R.sample(wrong, need) + [right]
        R.shuffle(opts)
        self.seen.add(key)
        it = {"c": self.P + code, "d": d, "q": q, "o": opts, "a": opts.index(right), "e": e}
        if chk: it["chk"] = chk
        self.out.append(it)
        return True

    def hand(self, code, d, q, right, wrong, e, need=3):
        return self.mk(code, d, q, right, wrong, e, None, need)

    def rep(self, n, fn, tries=80):
        got = t = 0
        while got < n and t < tries:
            t += 1
            if fn(): got += 1
        return got

    def balance(self):
        """Spread the right answers evenly over positions A-D (keeps the shuffle, just swaps the right option into a rotating slot)."""
        slots = {}
        for it in self.out:
            n = len(it['o']); k = slots.get(n, 0); slots[n] = k + 1
            tgt = (k * 3 + 1) % n if n > 1 else 0
            tgt = self.R.randrange(n) if False else (k % n)
            a = it['a']; o = it['o']
            o[a], o[tgt] = o[tgt], o[a]; it['a'] = tgt

    def save(self, path):
        self.balance()
        with open(path, 'w', encoding='utf8') as f:
            for it in self.out:
                f.write(json.dumps(it, ensure_ascii=False) + "\n")
        return len(self.out)

def cm(n): return f"{n:,}"
def CK(expr): return "f'{" + expr + ":,}'"          # chk text for comma-formatted numbers
def CS(expr): return "str(" + expr + ")"            # chk text for plain numbers
def pl(n, w): return f"{n} {w}{'' if n == 1 else 's'}"
def money(c): return f"{c}¢" if c < 100 else f"${c // 100}.{c % 100:02d}"
def mchk(expr, total):
    if total < 100: return "f'{%s}¢'" % expr
    return "f'${(%s)//100}.{(%s)%%100:02d}'" % (expr, expr)
def clock(tm): return f"{tm // 60}:{tm % 60:02d}"

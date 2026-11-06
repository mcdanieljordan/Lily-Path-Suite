(() => {
const $ = (s, r = document) => r.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const uid = () => Math.random().toString(36).slice(2, 9);
const IS_APP = !!window.lily;
if (IS_APP && /Mac/.test(navigator.platform)) document.body.classList.add('mac');

/* ---------------- icons ---------------- */
const I = (d, extra = '') => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" ${extra}>${d}</svg>`;
const ICON = {
  home: I('<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>'),
  video: I('<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10 9.5v5l4.5-2.5z" fill="currentColor"/>'),
  image: I('<rect x="3" y="4" width="18" height="16" rx="3"/><circle cx="9" cy="10" r="1.6"/><path d="M4 18l5-5 4 4 3-3 4 4"/>'),
  pdf: I('<path d="M6 3h8l5 5v13H6z"/><path d="M14 3v5h5"/>'),
  audio: I('<path d="M4 10v4M8 7v10M12 4v16M16 8v8M20 11v2"/>'),
  link: I('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'),
  back: I('<path d="M15 5l-7 7 7 7"/>'),
  fwd: I('<path d="M9 5l7 7-7 7"/>'),
  reload: I('<path d="M20 11a8 8 0 10-2.3 5.7"/><path d="M20 4v7h-7"/>'),
  ext: I('<path d="M14 4h6v6M20 4l-9 9"/><path d="M18 14v5H5V6h5"/>'),
  play: I('<path d="M7 4.5v15L19 12z" fill="currentColor"/>'),
  edit: I('<path d="M4 20h4L19 9l-4-4L4 16z"/>'),
};
const TYPE_ICON = { channel: 'video', video: 'video', image: 'image', pdf: 'pdf', audio: 'audio', ai: 'link', tool: 'link', link: 'link', page: 'link' };

/* ---------------- state ---------------- */
const KEY = 'lily-path-v2';
const DAYS = [['mon', 'Mon'], ['tue', 'Tue'], ['wed', 'Wed'], ['thu', 'Thu'], ['fri', 'Fri']];
const POND = '/Users/jordanmcdaniel/Documents/the-pond/';

const G = 'https://mcdanieljordan.github.io/';
function seedLib() {
  const app = (id, name, url, local) => ({ id, type: 'tool', name, url, local, seeded: 1 });
  const ai = (id, name, url) => ({ id, type: 'ai', name, url, seeded: 1 });
  const ch = (id, name, url) => ({ id, type: 'channel', name, url, seeded: 1 });
  return [
    app('a0', 'Ribbit-Leader', G + 'Lily-Path-Suite/apps/ribbit-rabbit.html', 'apps/ribbit-rabbit.html'),
    app('a1', 'Ribbit Rabbit', G + 'Lily-Path-Suite/apps/ribbit-rabbit.html', 'apps/ribbit-rabbit.html'),
    app('a2', 'Leader Locator', G + 'Lily-Path-Suite/apps/leader-locator.html', 'apps/leader-locator.html'),
    app('a3', 'Turn 2 Learn', G + 'turn-2-learn/', 'apps/turn-2-learn.html'),
    app('a4', 'Wave Lab', G + 'tempo-wavlab/', 'apps/wave-lab.html'),
    app('a5', 'BASIS Olympics', G + 'Lily-Path-Suite/apps/basis-olympics.html', 'apps/basis-olympics.html'),
    app('a6', 'Great Prompts', G + 'GreatPrompts-TeachersEdition/', 'apps/great-prompts.html'),
    app('a7', 'Tons of Teaching Tools', '', 'apps/tons-of-teaching-tools.html'),
    app('a8', 'Battleship Jeopardy', G + 'Lily-Path-Suite/apps/battleship-in-jeopardy.html', 'apps/battleship-in-jeopardy.html'),
    ai('a9', 'Gemini', 'https://gemini.google.com/app'),
    ai('a10', 'Claude', 'https://claude.ai/new'),
    ai('a11', 'ChatGPT', 'https://chatgpt.com/'),
    ch('c1', 'The Body Coach TV', 'https://www.youtube.com/@TheBodyCoachTV'),
    ch('c2', 'Peekaboo Kidz', 'https://www.youtube.com/user/Peekaboo'),
    ch('c3', 'Kids Academy', 'https://www.youtube.com/@KidsAcademyCom'),
    ch('c4', 'Little Sports', 'https://www.youtube.com/@LittleSports'),
    ch('c5', 'Colossal Cranium', 'https://www.youtube.com/@ColossalCranium'),
    ch('c6', 'Astra Nova School', 'https://www.youtube.com/@astranovaschool'),
    ch('c7', 'Yoga Guppy', 'https://www.youtube.com/@yogaguppy'),
  ];
}
function seed() {
  const periods = [
    ['U1', '8:40 – 9:30', 'Movement K (KB) · Gym D'],
    ['U2', '9:35 – 10:25', 'Movement K (KC) · Gym C'],
    ['ADA', '10:25 – 10:35', ''],
    ['U3', '10:40 – 11:30', 'PE 3 (3Zn) · Gym D'],
    ['U4', '11:35 – 12:25', 'Movement K (KI) · Gym C'],
    ['U5', '12:30 – 1:20', 'PE 3 (3Zr) · Gym D'],
    ['U6', '1:25 – 2:15', 'Movement K (KS) · Gym D'],
  ].map(([label, time, cls], i) => ({ id: 'p' + i, label, time, cls }));
  const plan = {};
  for (const [d] of DAYS) { plan[d] = {}; for (const p of periods) plan[d][p.id] = { cls: p.cls, items: [] }; }
  return {
    day: defaultDay(),
    periods, plan,
    seedV: 9,
    lib: seedLib(),
  };
}
function defaultDay() { const d = new Date().getDay(); return d >= 1 && d <= 5 ? DAYS[d - 1][0] : 'mon'; }
const FRESH = !localStorage.getItem(KEY);
let S;
try { S = JSON.parse(localStorage.getItem(KEY)); } catch (e) {}
if (!S || !S.periods) S = seed();
if (!S.seedV) { S.lib = S.lib.filter(i => !/^t\d$/.test(i.id)).concat(seedLib()); S.seedV = 2; }
if (S.seedV < 3) { const have = new Set(S.lib.map(i => i.id)); S.lib = seedLib().filter(i => i.id === 'a0' && !have.has(i.id)).concat(S.lib); S.seedV = 3; }
if (S.seedV < 4) { if (!S.lib.find(i => i.id === 'a8')) { const b = seedLib().find(i => i.id === 'a8'); const k = S.lib.findIndex(i => i.id === 'a2'); S.lib.splice(k < 0 ? 0 : k + 1, 0, b); } S.seedV = 4; }
if (S.seedV < 5) { const g = S.lib.find(i => i.id === 'a6'); if (g && !g.local) g.local = 'apps/great-prompts.html'; S.seedV = 5; }
if (S.seedV < 6) { const have = new Set(S.lib.map(i => i.id)); S.lib.push(...seedLib().filter(i => i.type === 'ai' && !have.has(i.id))); S.seedV = 6; }
if (S.seedV < 7) { const o = S.lib.find(i => i.id === 'a5'); if (o && o.seeded && /basisolympics/.test(o.url || '')) o.url = G + 'Lily-Path-Suite/apps/basis-olympics.html'; S.seedV = 7; }
if (S.seedV < 8) { const fresh = seedLib(); for (const id of ['a0', 'a1', 'a2']) { const o = S.lib.find(i => i.id === id), n = fresh.find(i => i.id === id); if (o && o.seeded && n) { o.url = n.url; o.local = n.local; } } S.seedV = 8; }
/* v9: Battleship Jeopardy now opens the suite copy (class sharing + saved boards), not the old standalone page */
if (S.seedV < 9) { const o = S.lib.find(i => i.id === 'a8'), n = seedLib().find(i => i.id === 'a8'); if (o && n && /Battleship-in-Jeopardy\/?$/i.test(o.url || '')) { o.url = n.url; o.local = n.local; } S.seedV = 9; }
if (!S.at) S.at = FRESH ? 0 : Date.now();
let syncSoon = () => {};
const save = () => { S.at = Date.now(); try { localStorage.setItem(KEY, JSON.stringify({ ...S, wk: undefined, lib: S.lib.filter(i => !i.blob && !i.temp) })); } catch (e) {} syncSoon(); };
const item = id => S.lib.find(i => i.id === id);
/* weeks: each Monday-dated week keeps its own plan, so past lessons are never overwritten */
const pad2 = n => String(n).padStart(2, '0');
const isoDate = d => `${d.getFullYear()}-${pad2(d.getMonth() + 1)}-${pad2(d.getDate())}`;
const mondayOf = d => { const x = new Date(d.getFullYear(), d.getMonth(), d.getDate()); x.setDate(x.getDate() - ((x.getDay() + 6) % 7)); return isoDate(x); };
const parseISO = k => { const [y, m, d] = k.split('-').map(Number); return new Date(y, m - 1, d); };
const shiftWeek = (k, n) => { const d = parseISO(k); d.setDate(d.getDate() + 7 * n); return isoDate(d); };
const dayDate = (wk, day) => { const d = parseISO(wk); d.setDate(d.getDate() + DAYS.findIndex(x => x[0] === day)); return d; };
function migrateWeeks(o) {
  o.weeks ||= {};
  if (o.plan) { const k = mondayOf(new Date()); o.weeks[k] ||= o.plan; delete o.plan; }
  return o;
}
migrateWeeks(S); S.wk = mondayOf(new Date());
function prevCls(pid, day, wk) {
  const ks = Object.keys(S.weeks).filter(k => k < wk).sort();
  for (let i = ks.length - 1; i >= 0; i--) { const c = ((S.weeks[ks[i]][day] || {})[pid]); if (c && c.cls) return c.cls; }
  return '';
}
const slot = (pid, day = S.day, wk = S.wk) => {
  const w = ((S.weeks[wk] ||= {})[day] ||= {});
  return w[pid] ||= { cls: prevCls(pid, day, wk), items: [] };
};

/* ---------------- helpers ---------------- */
const EXT = {
  video: 'mp4 mov m4v webm', image: 'jpg jpeg png gif webp svg heic', audio: 'mp3 wav m4a aac', pdf: 'pdf', page: 'html htm',
};
function typeOf(name) {
  const e = (name.split('.').pop() || '').toLowerCase();
  for (const t in EXT) if (EXT[t].split(' ').includes(e)) return t;
  return null;
}
const fileUrl = p => 'file://' + p.split('/').map(encodeURIComponent).join('/');
const localUrl = it => it.local ? new URL(it.local, location.href).href : '';
const itemUrl = it => it.blob || (it.path ? fileUrl(it.path) : it.url || localUrl(it));
const isWeb = it => ['tool', 'link', 'page', 'channel', 'ai'].includes(it.type);
const normUrl = u => { u = (u || '').trim(); if (!u) return ''; return /^[a-z]+:\/\//i.test(u) ? u : 'https://' + u; };
const hostOf = u => { try { return new URL(u).hostname.replace(/^www\./, ''); } catch (e) { return u; } };
const hue = s => { let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) % 360; return h; };
const tile = (name, size) => { const h = [8, 24, 200, 262, 152, 330, 176, 230][hue(name) % 8]; return `<span class="fav" style="${size ? `width:${size}px;height:${size}px;border-radius:6px;font-size:${size * .56}px;` : ''}background:linear-gradient(135deg,hsl(${h} 82% 60%),hsl(${(h + 30) % 360} 80% 48%));color:#fff;display:grid;place-items:center;font-weight:800">${esc(name.trim()[0] || '?').toUpperCase()}</span>`; };
const fav = (it, size) => it.icon ? `<span class="fav" style="${size ? `width:${size}px;height:${size}px;border-radius:6px;` : ''}display:grid;place-items:center;overflow:hidden"><img src="${it.icon}" draggable="false" style="width:100%;height:100%;object-fit:cover"></span>` : tile(it.name, size);
function pickIcon(id) {
  const it = item(id); if (!it) return;
  const i = document.createElement('input'); i.type = 'file'; i.accept = 'image/*';
  i.onchange = () => {
    const f = i.files[0]; if (!f) return;
    const url = URL.createObjectURL(f), im = new Image();
    im.onload = () => {
      const c = document.createElement('canvas'); c.width = c.height = 128;
      const x = c.getContext('2d'), m = Math.min(im.width, im.height);
      x.drawImage(im, (im.width - m) / 2, (im.height - m) / 2, m, m, 0, 0, 128, 128);
      it.icon = c.toDataURL('image/png'); URL.revokeObjectURL(url);
      save(); renderToday(); renderTabs(); toast('Icon set');
    };
    im.onerror = () => toast("Can't read that image");
    im.src = url;
  };
  i.click();
}
function toast(msg) { const t = $('#toast'); t.textContent = msg; t.hidden = false; clearTimeout(toast.t); toast.t = setTimeout(() => t.hidden = true, 1800); }

/* ---------------- dialog ---------------- */
function ask({ title, name = '', url = '', showUrl = true, canDelete = false, namePh = 'Name' }) {
  return new Promise(res => {
    const d = $('#dlg');
    $('#dlgTitle').textContent = title;
    $('#dName').value = name; $('#dName').placeholder = namePh;
    $('#dUrl').value = url; $('#dUrlWrap').style.display = showUrl ? '' : 'none';
    $('#dDel').style.visibility = canDelete ? 'visible' : 'hidden';
    let out = null;
    const done = v => { out = v; d.close(); };
    $('#dDel').onclick = () => done('delete');
    $('#dCancel').onclick = () => done(null);
    $('#dlgForm').onsubmit = e => { e.preventDefault(); done({ name: $('#dName').value.trim(), url: normUrl($('#dUrl').value) }); };
    d.onclose = () => res(out);
    d.showModal();
    (showUrl && !name ? $('#dUrl') : $('#dName')).focus();
  });
}

/* ---------------- library actions ---------------- */
async function addLink(kind) {
  const r = await ask({ title: { tool: 'Add a tool', channel: 'Add a channel', ai: 'Add an AI tool' }[kind] || 'Add a link', namePh: 'Name (optional)' });
  if (!r || !r.url) return;
  S.lib.push({ id: uid(), type: kind, name: r.name || hostOf(r.url), url: r.url });
  save(); renderToday();
}
async function editItem(id) {
  const it = item(id); if (!it) return;
  const r = await ask({ title: 'Edit', name: it.name, url: it.url || '', showUrl: isWeb(it) && !it.path, canDelete: true });
  if (!r) return;
  if (r === 'delete') {
    S.lib = S.lib.filter(i => i.id !== id);
    for (const w in S.weeks) for (const d in S.weeks[w]) for (const p in S.weeks[w][d]) S.weeks[w][d][p].items = S.weeks[w][d][p].items.filter(c => c.id !== id);
    closeTab(id);
  } else {
    it.name = r.name || it.name;
    if (isWeb(it) && !it.path && r.url !== it.url) { it.url = r.url; const was = active === id; closeTab(id); if (was && it.url) openItem(id); }
    renderTabs();
  }
  save(); renderToday();
}
async function addFiles(files, target) {
  const added = [];
  for (const f of files) {
    const path = typeof f === 'string' ? f : (IS_APP ? window.lily.pathFor(f) : '');
    const name = typeof f === 'string' ? f.split('/').pop() : f.name;
    const type = typeOf(name);
    if (!type) { toast(`Can't use ${name}`); continue; }
    const it = { id: uid(), type, name: name.replace(/\.[^.]+$/, '') };
    if (path) it.path = path; else { it.blob = URL.createObjectURL(f); }
    S.lib.push(it); added.push(it);
  }
  if (target && added.length) slot(target.pid).items.splice(target.idx, 0, ...added.map(a => ({ k: uid(), id: a.id })));
  if (added.length) { save(); renderToday(); }
}
async function pickFiles() {
  if (IS_APP) addFiles(await window.lily.pickFiles());
  else { const i = document.createElement('input'); i.type = 'file'; i.multiple = true; i.onchange = () => addFiles([...i.files]); i.click(); }
}

/* ---------------- Today view ---------------- */
function resHTML(it) {
  const u = itemUrl(it);
  let th = ICON[TYPE_ICON[it.type]];
  if (it.type === 'image') th = `<img src="${esc(u)}" draggable="false" loading="lazy">`;
  if (it.type === 'video') th = `<video src="${esc(u)}#t=0.6" preload="metadata" muted></video>`;
  return `<div class="res" draggable="true" data-lib="${it.id}" data-act="open" title="${esc(it.name)}">
    <div class="th">${th}</div><div class="nm">${esc(it.name)}</div>
    <button class="edit" data-act="edit" title="Edit">${ICON.edit}</button></div>`;
}
function chipHTML(c, idx) {
  const it = item(c.id); if (!it) return '';
  const ic = isWeb(it) ? fav(it, 18) : ICON[TYPE_ICON[it.type]];
  return `<div class="chip" draggable="true" data-chip="${idx}" data-act="open" data-id="${it.id}"><span class="ic">${ic}</span><span class="nm">${esc(it.name)}</span><button class="rm" data-act="rm" title="Remove from this class">✕</button></div>`;
}
function periodHTML(p, i) {
  const s = slot(p.id);
  const chips = s.items.map(chipHTML).join('');
  return `<div class="period" data-pid="${p.id}" style="--c:var(--pc${i % 7})">
    <div class="ph">
      <div class="row1"><span class="grip" draggable="true" data-grip title="Drag to reorder">⋮⋮</span><input class="badge" data-f="label" value="${esc(p.label)}" style="width:${Math.max(44, p.label.length * 10 + 22)}px"><input class="time" data-f="time" value="${esc(p.time)}" placeholder="Time"></div>
      <input class="cls" data-f="cls" value="${esc(s.cls)}" placeholder="Class">
    </div>
    <div class="items">${chips || '<span class="hint">Drop things here</span>'}</div>
    <button class="teach" data-act="teach" ${s.items.some(c => item(c.id)) ? '' : 'disabled'}>${ICON.play} Teach</button>
    <button class="del" data-act="delp" title="Remove period">✕</button>
  </div>`;
}
const dayHas = d => Object.values((S.weeks[S.wk] || {})[d] || {}).some(c => c.items && c.items.length);
function greet() { const h = new Date().getHours(); return h < 12 ? 'Good morning ☀️' : h < 17 ? 'Good afternoon 🌤️' : 'Good evening 🌙'; }
function renderToday() {
  const tools = S.lib.filter(i => i.type === 'tool' || i.type === 'page');
  const ais = S.lib.filter(i => i.type === 'ai');
  const chans = S.lib.filter(i => i.type === 'channel');
  const res = S.lib.filter(i => !['tool', 'channel', 'page', 'ai'].includes(i.type) && !i.temp);
  const dayName = DAYS.find(d => d[0] === S.day)[1];
  $('#today').innerHTML = `
  <aside class="lib" id="lib">
    <section>
      <h4>Tools <span><button data-act="add-html" title="Add an HTML file you made">+ HTML</button> <button data-act="add-tool">+ Link</button></span></h4>
      <div class="tools">${tools.map(t => `
        <div class="tool" draggable="true" data-lib="${t.id}" data-act="open" title="${esc(t.url ? hostOf(t.url) : t.path ? 'Local file' : 'Click to add a link')}">
          ${fav(t)}
          <div class="nm">${esc(t.name)}${t.url || t.path || t.local ? '' : '<small>Add link</small>'}</div>
          <button class="edit" data-act="edit" title="Edit">${ICON.edit}</button>
        </div>`).join('') || '<div class="empty">Add the apps you use.</div>'}</div>
    </section>
    <section>
      <h4>AI <button data-act="add-ai">+ Add</button></h4>
      <div class="tools">${ais.map(t => `
        <div class="tool" draggable="true" data-lib="${t.id}" data-act="open" title="${esc(hostOf(t.url))}">
          ${fav(t)}<div class="nm">${esc(t.name)}</div>
          <button class="edit" data-act="edit" title="Edit">${ICON.edit}</button>
        </div>`).join('') || '<div class="empty">Add your AI tools.</div>'}</div>
    </section>
    <section>
      <h4>YouTube <button data-act="add-chan">+ Add</button></h4>
      <div class="tools">${chans.map(t => `
        <div class="tool" draggable="true" data-lib="${t.id}" data-act="open" title="${esc(hostOf(t.url))}">
          ${fav(t)}<div class="nm">${esc(t.name)}</div>
          <button class="edit" data-act="edit" title="Edit">${ICON.edit}</button>
        </div>`).join('') || '<div class="empty">Add channels you use.</div>'}</div>
    </section>
    <section>
      <h4>Videos, images &amp; files <button data-act="add-link">+ Link</button></h4>
      ${res.length ? `<div class="res-grid">${res.map(resHTML).join('')}</div>` : ''}
      <div class="drop">Drop files or links here,<br>paste a link, or <b data-act="add-files">browse</b></div>
    </section>
  </aside>
  <div class="day">
    <div class="hero">
      <div class="hero-t"><span class="hi">${greet()}</span><h1>${dayName}</h1><span class="date">${dayDate(S.wk, S.day).toLocaleDateString(undefined, { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' })}</span></div>
      <div class="hero-r">
        <div class="wknav"><button data-act="wk" data-n="-1" title="Previous week">◀</button><span>Week of ${parseISO(S.wk).toLocaleDateString(undefined, { month: 'short', day: 'numeric' })}</span><button data-act="wk" data-n="1" title="Next week">▶</button>${S.wk === mondayOf(new Date()) ? '' : '<button data-act="wk0">This week</button>'}<button data-act="export" title="Save this week as a file">Export week</button></div>
        <div class="seg">${DAYS.map(([k, n]) => `<button data-act="day" data-d="${k}" class="${k === S.day ? 'on' : ''}">${n} ${dayDate(S.wk, k).getDate()}${dayHas(k) ? ' •' : ''}</button>`).join('')}</div>
      </div>
    </div>
    ${S.periods.map((p, i) => periodHTML(p, i)).join('')}
    <button class="addp" data-act="addp">+ Add period</button>
  </div>`;
  markNow();
}

function exportWeek() {
  const wk = S.wk, w = S.weeks[wk] || {};
  const days = DAYS.map(([k, n]) => ({
    day: n, date: isoDate(dayDate(wk, k)),
    periods: S.periods.map(p => { const c = (w[k] || {})[p.id]; return { period: p.label, time: p.time, class: c ? c.cls : '', lessons: c ? c.items.map(i => item(i.id)).filter(Boolean).map(it => ({ name: it.name, type: it.type, link: it.url || '' })) : [] }; }).filter(p => p.lessons.length),
  }));
  const out = { app: 'Lily Path', weekOf: wk, exported: new Date().toISOString(), days };
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([JSON.stringify(out, null, 2)], { type: 'application/json' }));
  a.download = `lily-path-week-${wk}.json`; document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000); toast('Week exported');
}
function parseRange(t) {
  const m = String(t).match(/(\d{1,2})[:.](\d{2})\s*(am|pm)?\s*[–\-—to]+\s*(\d{1,2})[:.](\d{2})\s*(am|pm)?/i);
  if (!m) return null;
  const conv = (h, mi, ap) => { h = +h; ap = (ap || '').toLowerCase(); if (ap === 'pm' && h < 12) h += 12; else if (ap === 'am' && h === 12) h = 0; else if (!ap && h < 7) h += 12; return h * 60 + +mi; };
  return [conv(m[1], m[2], m[3]), conv(m[4], m[5], m[6])];
}
function markNow() {
  const d = new Date(), mins = d.getHours() * 60 + d.getMinutes();
  const isToday = S.wk === mondayOf(d) && d.getDay() >= 1 && d.getDay() <= 5 && DAYS[d.getDay() - 1][0] === S.day;
  S.periods.forEach(p => {
    const el = $(`.period[data-pid="${p.id}"]`); if (!el) return;
    const r = parseRange(p.time);
    el.classList.toggle('now', !!(isToday && r && mins >= r[0] && mins < r[1]));
  });
}
setInterval(markNow, 30000);

function urlItem(u) {
  u = normUrl(u);
  const yt = /youtube\.com\/(@|user\/|channel\/|c\/)/i.test(u);
  let name = hostOf(u); const h = u.match(/\/(@[^/?#]+)/); if (h) name = h[1].slice(1);
  return { id: uid(), type: yt ? 'channel' : 'link', name, url: u };
}
function addUrls(urls, target) {
  const its = urls.map(urlItem); S.lib.push(...its);
  if (target) slot(target.pid).items.splice(target.idx ?? slot(target.pid).items.length, 0, ...its.map(a => ({ k: uid(), id: a.id })));
  save(); renderToday(); toast(its.length > 1 ? `Added ${its.length} links` : `Added ${its[0].name}`);
}
/* ---- Today interactions ---- */
let drag = null;
const todayEl = $('#today');
let hoverP = null;
todayEl.addEventListener('mouseover', e => { hoverP = e.target.closest('.period')?.dataset.pid || null; });
todayEl.addEventListener('mouseleave', () => hoverP = null);
window.addEventListener('paste', e => {
  if (active !== 'today' || e.target.matches('input,textarea')) return;
  const urls = (e.clipboardData.getData('text') || '').split(/\s+/).filter(Boolean);
  if (!urls.length || !urls.every(x => URLRE.test(x))) return;
  e.preventDefault(); addUrls(urls, hoverP ? { pid: hoverP } : null);
});

todayEl.addEventListener('click', e => {
  const a = e.target.closest('[data-act]'); if (!a) return;
  const act = a.dataset.act, host = a.closest('[data-lib],[data-chip]'), pEl = a.closest('.period');
  if (act === 'edit') { e.stopPropagation(); return editItem(host.dataset.lib); }
  if (act === 'rm') { e.stopPropagation(); slot(pEl.dataset.pid).items.splice(+host.dataset.chip, 1); save(); return renderToday(); }
  if (act === 'open') return openItem(host.dataset.lib || host.dataset.id);
  if (act === 'day') { S.day = a.dataset.d; save(); return renderToday(); }
  if (act === 'wk') { S.wk = shiftWeek(S.wk, +a.dataset.n); return renderToday(); }
  if (act === 'wk0') { S.wk = mondayOf(new Date()); return renderToday(); }
  if (act === 'export') return exportWeek();
  if (act === 'add-tool') return addLink('tool');
  if (act === 'add-link') return addLink('link');
  if (act === 'add-ai') return addLink('ai');
  if (act === 'add-html') return pickFiles();
  if (act === 'add-chan') return addLink('channel');
  if (act === 'add-files') return pickFiles();
  if (act === 'teach') return startPresent(pEl.dataset.pid);
  if (act === 'addp') { const id = 'p' + uid(); S.periods.push({ id, label: 'New', time: '', cls: '' }); save(); return renderToday(); }
  if (act === 'delp') { const id = pEl.dataset.pid; S.periods = S.periods.filter(p => p.id !== id); save(); return renderToday(); }
});
todayEl.addEventListener('change', e => {
  const f = e.target.dataset.f; if (!f) return;
  const pid = e.target.closest('.period').dataset.pid;
  if (f === 'cls') slot(pid).cls = e.target.value;
  else { S.periods.find(p => p.id === pid)[f] = e.target.value; if (f === 'label') renderToday(); }
  save(); markNow();
});
todayEl.addEventListener('keydown', e => { if (e.key === 'Enter' && e.target.matches('input')) e.target.blur(); });

todayEl.addEventListener('dragstart', e => {
  const el = e.target.closest('[data-lib],[data-chip],[data-grip]'); if (!el) return;
  if (el.dataset.grip !== undefined) {
    const pe = el.closest('.period'); drag = { from: 'period', pid: pe.dataset.pid };
    e.dataTransfer.effectAllowed = 'move'; e.dataTransfer.setData('text/plain', 'lily');
    e.dataTransfer.setDragImage(pe, 24, 24); setTimeout(() => pe.style.opacity = '.4'); return;
  }
  drag = el.dataset.chip !== undefined
    ? { from: 'chip', pid: el.closest('.period').dataset.pid, idx: +el.dataset.chip }
    : { from: 'lib', id: el.dataset.lib };
  e.dataTransfer.effectAllowed = 'copyMove';
  e.dataTransfer.setData('text/plain', 'lily');
  setTimeout(() => el.style.opacity = '.45');
});
const clearMarks = () => todayEl.querySelectorAll('.before,.end,.over,.pbefore,.pafter,.tbefore,.tafter').forEach(n => n.classList.remove('before', 'end', 'over', 'pbefore', 'pafter', 'tbefore', 'tafter'));
const tileAfter = (t, e) => { const r = t.getBoundingClientRect(); return t.classList.contains('res') ? e.clientX >= r.left + r.width / 2 : e.clientY >= r.top + r.height / 2; };
todayEl.addEventListener('dragend', () => { drag = null; clearMarks(); todayEl.querySelectorAll('[draggable],.period').forEach(n => n.style.opacity = ''); });
const hasFiles = e => [...(e.dataTransfer?.types || [])].includes('Files');
const hasUrl = e => !drag && [...(e.dataTransfer?.types || [])].includes('text/uri-list');
const URLRE = /^(https?:\/\/|www\.)\S+$/i;
const dropUrls = e => [e.dataTransfer.getData('text/uri-list'), e.dataTransfer.getData('text/plain')].join('\n').split(/\r?\n/).map(x => x.trim()).filter(x => URLRE.test(x)).filter((x, i, a) => a.indexOf(x) === i);
function dropIndex(period, x, y) {
  const chips = [...period.querySelectorAll('.chip')];
  const i = chips.findIndex(c => { const r = c.getBoundingClientRect(); return y < r.top || (y < r.bottom && x < r.left + r.width / 2); });
  return i < 0 ? chips.length : i;
}
todayEl.addEventListener('dragover', e => {
  if (!drag && !hasFiles(e) && !hasUrl(e)) return;
  e.preventDefault(); clearMarks();
  const p = e.target.closest('.period');
  if (p && drag && drag.from === 'period') {
    const r = p.getBoundingClientRect(); p.classList.add(e.clientY < r.top + r.height / 2 ? 'pbefore' : 'pafter');
  } else if (p) {
    p.classList.add('over');
    const i = dropIndex(p, e.clientX, e.clientY), chips = p.querySelectorAll('.chip');
    if (i < chips.length) chips[i].classList.add('before'); else p.querySelector('.items').classList.add('end');
  } else if (drag && drag.from === 'lib' && e.target.closest('#lib .tool,#lib .res') && e.target.closest('#lib .tool,#lib .res').dataset.lib !== drag.id) {
    const t = e.target.closest('#lib .tool,#lib .res'); t.classList.add(tileAfter(t, e) ? 'tafter' : 'tbefore');
  } else if (e.target.closest('#lib')) $('#lib').classList.add('over');
});
todayEl.addEventListener('drop', e => {
  e.preventDefault(); e.stopPropagation(); clearMarks();
  const p = e.target.closest('.period');
  const target = p ? { pid: p.dataset.pid, idx: dropIndex(p, e.clientX, e.clientY) } : null;
  if (hasFiles(e)) { document.body.classList.remove('filedrag'); return addFiles([...e.dataTransfer.files], target); }
  if (!drag) { const u = dropUrls(e); if (u.length) addUrls(u, target); return; }
  if (drag.from === 'period') {
    if (p && p.dataset.pid !== drag.pid) {
      const r = p.getBoundingClientRect(), after = e.clientY >= r.top + r.height / 2;
      const [m] = S.periods.splice(S.periods.findIndex(x => x.id === drag.pid), 1);
      S.periods.splice(S.periods.findIndex(x => x.id === p.dataset.pid) + (after ? 1 : 0), 0, m);
      save(); renderToday();
    }
    drag = null; return;
  }
  const tile = !p && drag.from === 'lib' ? e.target.closest('#lib .tool,#lib .res') : null;
  if (tile && tile.dataset.lib !== drag.id) {
    const [mv] = S.lib.splice(S.lib.findIndex(i => i.id === drag.id), 1);
    S.lib.splice(S.lib.findIndex(i => i.id === tile.dataset.lib) + (tileAfter(tile, e) ? 1 : 0), 0, mv);
    drag = null; save(); renderToday(); return;
  }
  if (p && drag.from === 'lib') slot(target.pid).items.splice(target.idx, 0, { k: uid(), id: drag.id });
  else if (p && drag.from === 'chip') {
    const src = slot(drag.pid).items, [moved] = src.splice(drag.idx, 1);
    let idx = target.idx; if (drag.pid === target.pid && drag.idx < idx) idx--;
    slot(target.pid).items.splice(idx, 0, moved);
  } else if (!p && drag.from === 'chip' && e.target.closest('#lib')) slot(drag.pid).items.splice(drag.idx, 1);
  else return;
  drag = null; save(); renderToday();
});
// files dropped anywhere else on the window go to the library instead of navigating away
window.addEventListener('dragover', e => { e.preventDefault(); if (hasFiles(e)) document.body.classList.add('filedrag'); });
window.addEventListener('dragleave', e => { if (!e.relatedTarget) document.body.classList.remove('filedrag'); });
window.addEventListener('drop', e => { e.preventDefault(); document.body.classList.remove('filedrag'); if (hasFiles(e)) addFiles([...e.dataTransfer.files]); });

/* ---------------- tabs & views ---------------- */
let open = [];           // [{id, el}]
let active = 'today';
const TODAY_TAB = 'today';

let renaming = null;
const ent = id => open.find(o => o.id === id);
function groupOf(id) {
  const o = ent(id); if (!o) return [];
  const m = o.mate && ent(o.mate); if (!m) return [o];
  return open.indexOf(o) < open.indexOf(m) ? [o, m] : [m, o];
}
function unitsOf() {
  const seen = new Set(), out = [];
  for (const o of open) { if (seen.has(o.id)) continue; const g = groupOf(o.id); g.forEach(x => seen.add(x.id)); out.push(g); }
  return out;
}
function unpair(o) { if (!o || !o.mate) return; const m = ent(o.mate); if (m) delete m.mate; delete o.mate; }
function pairTabs(aId, dId, side) {            // side "a": dragged tab goes on the left
  const a = ent(aId), d = ent(dId); if (!a || !d || a === d) return;
  if (a.mate !== d.id) { unpair(a); unpair(d); }
  a.mate = d.id; d.mate = a.id;
  open.splice(open.indexOf(d), 1);
  const ai = open.indexOf(a); open.splice(side === 'a' ? ai : ai + 1, 0, d);
  activate(aId);
}
function moveUnit(id, targetId, after) {
  const us = unitsOf(), from = us.find(u => u.some(o => o.id === id)), to = us.find(u => u.some(o => o.id === targetId));
  if (!from || !to || from === to) return;
  from.forEach(o => open.splice(open.indexOf(o), 1));
  const last = to[to.length - 1], idx = after ? open.indexOf(last) + 1 : open.indexOf(to[0]);
  open.splice(idx, 0, ...from);
  activate(active);
}
function stepUnit(id, dir) {
  const us = unitsOf(), i = us.findIndex(u => u.some(o => o.id === id)), j = i + dir;
  if (i < 0 || j < 0 || j >= us.length) return;
  moveUnit(id, us[j][0].id, dir > 0);
}
function renderTabs() {
  if (renaming) return;
  const btn = o => { const it = item(o.id); return `<button class="tab ${active === o.id ? 'on' : ''}" draggable="true" data-id="${o.id}" title="${esc(it?.name)} — double-click to rename, right-click for more">${it && isWeb(it) ? `<span class="ti">${fav(it, 14)}</span>` : ''}<span class="t">${esc(it?.name)}</span><span class="x" data-x="1">✕</span></button>`; };
  $('#tabs').innerHTML = `<button class="tab home ${active === TODAY_TAB ? 'on' : ''}" data-id="${TODAY_TAB}">${ICON.home}<span>Today</span></button>` +
    unitsOf().map(g => g.length > 1
      ? `<div class="pair ${g.some(o => o.id === active) ? 'on' : ''}" data-unit="${g[0].id}">${g.map(btn).join('<i class="psep"></i>')}</div>`
      : btn(g[0])).join('');
}
$('#tabs').addEventListener('click', e => {
  const t = e.target.closest('.tab'); if (!t || renaming) return;
  if (e.target.closest('[data-x]')) return closeTab(t.dataset.id);
  if (t.dataset.id === active && !t.classList.contains('pair')) return;
  activate(t.dataset.id);
});
$('#tabs').addEventListener('auxclick', e => { const t = e.target.closest('.tab'); if (t && e.button === 1 && t.dataset.id !== TODAY_TAB) closeTab(t.dataset.id); });
$('#tabs').addEventListener('dblclick', e => { const t = e.target.closest('.tab'); if (t && t.dataset.id !== TODAY_TAB && !e.target.closest('[data-x]')) inlineRename(t); });
function inlineRename(tabEl) {
  tabEl = document.querySelector(`#tabs .tab[data-id="${tabEl.dataset.id}"]`) || tabEl;
  const id = tabEl.dataset.id, it = item(id), s = tabEl.querySelector('.t'); if (!it || !s) return;
  renaming = id; tabEl.draggable = false; s.contentEditable = 'true'; s.focus();
  const r = document.createRange(); r.selectNodeContents(s); const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
  let done = false;
  const end = ok => { if (done) return; done = true; const v = (s.textContent || '').trim().slice(0, 60); renaming = null; if (ok && v) { it.name = v; save(); renderToday(); } renderTabs(); };
  s.addEventListener('keydown', e => { e.stopPropagation(); if (e.key === 'Enter') { e.preventDefault(); end(true); } else if (e.key === 'Escape') { e.preventDefault(); end(false); } });
  s.addEventListener('blur', () => end(true));
}
$('#newtab').addEventListener('click', async () => {
  const r = await ask({ title: 'Open a link', showUrl: true, namePh: 'Name (optional)' });
  if (!r || !r.url) return;
  const it = { id: uid(), type: 'link', name: r.name || hostOf(r.url), url: r.url, temp: true };
  S.lib.push(it); openItem(it.id);
});

/* drag tabs: reorder in the bar, or drop on the page to pair (split view) */
let tdrag = null;
const dropz = $('#dropz');
const clearTM = () => document.querySelectorAll('#tabs .tb,#tabs .ta').forEach(n => n.classList.remove('tb', 'ta'));
$('#tabs').addEventListener('dragstart', e => {
  const t = e.target.closest('.tab');
  if (!t || t.dataset.id === TODAY_TAB) { e.preventDefault(); return; }
  tdrag = t.dataset.id; e.dataTransfer.effectAllowed = 'move'; e.dataTransfer.setData('text/plain', 'lily-tab');
  setTimeout(() => { if (tdrag && active !== TODAY_TAB && active !== tdrag && !(ent(tdrag)?.mate === active)) document.body.classList.add('tabdrag'); }, 0);
});
$('#tabs').addEventListener('dragover', e => {
  if (!tdrag) return;
  const el = e.target.closest('.pair') || e.target.closest('.tab'); if (!el || el.classList.contains('home')) return;
  e.preventDefault(); clearTM();
  const r = el.getBoundingClientRect(); el.classList.add(e.clientX < r.left + r.width / 2 ? 'tb' : 'ta');
});
$('#tabs').addEventListener('drop', e => {
  if (!tdrag) return;
  const el = e.target.closest('.pair') || e.target.closest('.tab'); if (!el || el.classList.contains('home')) return;
  e.preventDefault(); e.stopPropagation();
  const r = el.getBoundingClientRect(), after = e.clientX >= r.left + r.width / 2;
  const tid = el.classList.contains('pair') ? el.dataset.unit : el.dataset.id, id = tdrag;
  tdEnd(); moveUnit(id, tid, after);
});
function tdEnd() { tdrag = null; clearTM(); document.body.classList.remove('tabdrag'); dropz.querySelectorAll('.hot').forEach(n => n.classList.remove('hot')); }
window.addEventListener('dragend', tdEnd);
dropz.addEventListener('dragover', e => { if (!tdrag) return; e.preventDefault(); const h = e.target.closest('[data-side]'); dropz.querySelectorAll('[data-side]').forEach(n => n.classList.toggle('hot', n === h)); });
dropz.addEventListener('drop', e => {
  if (!tdrag) return; e.preventDefault(); e.stopPropagation();
  const h = e.target.closest('[data-side]'), id = tdrag, a = active; tdEnd();
  if (h && a !== TODAY_TAB) pairTabs(a, id, h.dataset.side);
});

/* drag the divider between two panes */
(() => {
  const sd = $('#sdiv'), vs = $('#views'); let on = false;
  sd.addEventListener('pointerdown', e => { on = true; sd.setPointerCapture(e.pointerId); vs.classList.add('resizing'); e.preventDefault(); });
  sd.addEventListener('pointermove', e => { if (!on) return; const r = vs.getBoundingClientRect(); vs.style.setProperty('--sp', Math.min(80, Math.max(20, (e.clientX - r.left) / r.width * 100)).toFixed(1)); });
  const up = () => { on = false; vs.classList.remove('resizing'); };
  sd.addEventListener('pointerup', up); sd.addEventListener('pointercancel', up);
  sd.addEventListener('dblclick', () => vs.style.setProperty('--sp', 50));
})();

function activate(id) {
  active = id;
  const g = id === TODAY_TAB ? [] : groupOf(id), ids = g.map(o => o.id);
  $('#today').classList.toggle('show', id === TODAY_TAB);
  document.querySelectorAll('#views .view').forEach(v => {
    const on = ids.includes(v.dataset.id);
    v.classList.toggle('show', on); v.classList.toggle('focus', on && ids.length > 1 && v.dataset.id === id);
  });
  g.forEach((o, i) => { o.el.style.order = i; });
  $('#views').classList.toggle('split', ids.length > 1); $('#sdiv').hidden = ids.length < 2;
  renderTabs();
}
function closeTab(id) {
  const o = ent(id); if (!o) return;
  const i = open.indexOf(o); unpair(o);
  o.el.remove(); open.splice(i, 1);
  const it = item(id);
  if (it && it.temp) { S.lib = S.lib.filter(x => x.id !== id); }
  if (active === id) activate((open[i] || open[i - 1])?.id || TODAY_TAB); else activate(active);
}
function openItem(id, beside) {
  const it = item(id); if (!it) return;
  if (!open.find(o => o.id === id)) {
    const el = mkView(it); $('#views').appendChild(el); open.push({ id, el });
  }
  if (beside && beside !== id && ent(beside)) { pairTabs(beside, id, 'b'); activate(id); return; }
  activate(id);
}

function mkView(it) {
  const el = document.createElement('section');
  el.className = 'view'; el.dataset.id = it.id;
  const u = itemUrl(it);
  if (isWeb(it) && !u) {
    el.innerHTML = `<div class="setup"><div><div style="font-size:18px;font-weight:600;color:var(--ink)">${esc(it.name)}</div><div>Paste its link once and it opens right here.</div><button class="primary" data-w="seturl">Add link</button></div></div>`;
    el.addEventListener('click', e => { if (e.target.closest('[data-w="seturl"]')) editItem(it.id); });
    return el;
  }
  if (isWeb(it)) {
    el.innerHTML = `<div class="wbar"><button data-w="back" title="Back">${ICON.back}</button><button data-w="fwd" title="Forward">${ICON.fwd}</button><button data-w="reload" title="Reload">${ICON.reload}</button><div class="addr">${esc(u)}</div>${isLL(it) ? '<button class="bijbtn" data-w="bij" title="Send these groups to Battleship Jeopardy">⚓ Send to Battleship</button>' : ''}<i class="spin"></i><button data-w="ext" title="Open in Chrome">${ICON.ext}</button></div>`;
    let wv;
    if (IS_APP) {
      wv = document.createElement('webview');
      wv.setAttribute('partition', 'persist:lily'); wv.setAttribute('allowpopups', '');
      wv.setAttribute('src', u);
    } else { wv = document.createElement('iframe'); wv.src = u; wv.allow = 'fullscreen; camera; microphone; autoplay'; }
    el.appendChild(wv);
    const bar = $('.wbar', el), addr = $('.addr', el);
    if (IS_APP) {
      const upd = e => { if (e.url && e.isMainFrame !== false) addr.textContent = e.url; };
      wv.addEventListener('dom-ready', () => { el._ready = 1; });
      wv.addEventListener('focus', () => { if (active !== it.id && groupOf(active).some(o => o.id === it.id)) { active = it.id; document.querySelectorAll('#views .view').forEach(v => v.classList.toggle('focus', v.dataset.id === it.id && v.classList.contains('show'))); renderTabs(); } });
      wv.addEventListener('did-start-loading', () => { el._ready = 0; bar.classList.add('loading'); });
      wv.addEventListener('did-stop-loading', () => bar.classList.remove('loading'));
      wv.addEventListener('did-fail-load', e => {
        const lu = localUrl(it);
        if (e.isMainFrame && e.errorCode !== -3 && lu && !el._fell && wv.getAttribute('src') !== lu) { el._fell = 1; wv.src = lu; toast('Offline — opened saved copy'); }
      });
      wv.addEventListener('did-navigate', upd); wv.addEventListener('did-navigate-in-page', upd);
    }
    el.addEventListener('click', e => {
      const b = e.target.closest('[data-w]'); if (!b) return;
      const w = b.dataset.w;
      try {
        if (w === 'back') IS_APP ? wv.goBack() : history.back();
        if (w === 'fwd') IS_APP && wv.goForward();
        if (w === 'reload') IS_APP ? wv.reload() : (wv.src = wv.src);
        if (w === 'bij') sendGroups(wv);
        if (w === 'ext') IS_APP ? window.lily.openExternal(IS_APP && wv.getURL ? wv.getURL() : u) : window.open(u, '_blank');
      } catch (err) {}
    });
    el._wv = wv;
    return el;
  }
  const media = { image: `<img src="${esc(u)}">`, video: `<video src="${esc(u)}" controls autoplay></video>`, audio: `<audio src="${esc(u)}" controls autoplay></audio>`, pdf: `<embed src="${esc(u)}" type="application/pdf">` }[it.type];
  el.innerHTML = `<div class="wbar"><span class="addr" style="margin-left:0">${esc(it.name)}</span></div><div class="media">${media}</div>`;
  return el;
}

/* ---------------- Teach (present) mode ---------------- */
let P = null;
const pill = $('#pill');
function presentList() { return slot(P.pid).items.map(c => item(c.id)).filter(Boolean); }
function startPresent(pid) {
  P = { pid, i: 0 };
  if (!presentList().length) { P = null; return; }
  document.body.classList.add('present'); pill.hidden = false;
  showPresent();
}
function showPresent() {
  const list = presentList(), it = list[P.i], p = S.periods.find(x => x.id === P.pid), s = slot(P.pid);
  openItem(it.id);
  pill.innerHTML = `<button data-p="prev" title="Back (←)">${ICON.back}</button>
    <div class="mid"><span>${esc(it.name)}</span><small>${esc(p.label)}${s.cls ? ' · ' + esc(s.cls.split('·')[0].trim()) : ''} — ${P.i + 1} of ${list.length}</small></div>
    <div class="dots">${list.map((_, i) => `<i data-p="go" data-i="${i}" class="${i === P.i ? 'on' : ''}"></i>`).join('')}</div>
    <button data-p="next" title="Next (→)">${ICON.fwd}</button><button class="exit" data-p="exit">Done</button>`;
}
function stepPresent(d) { if (!P) return; const n = presentList().length; P.i = Math.max(0, Math.min(n - 1, P.i + d)); showPresent(); }
function endPresent() { P = null; pill.hidden = true; document.body.classList.remove('present'); activate(TODAY_TAB); }
pill.addEventListener('click', e => {
  const b = e.target.closest('[data-p]'); if (!b) return;
  const a = b.dataset.p;
  if (a === 'prev') stepPresent(-1); if (a === 'next') stepPresent(1); if (a === 'exit') endPresent();
  if (a === 'go') { P.i = +b.dataset.i; showPresent(); }
});
window.addEventListener('keydown', e => {
  if (e.target.matches('input,textarea')) return;
  if (P && (e.key === 'ArrowRight' || e.key === 'PageDown')) stepPresent(1);
  else if (P && (e.key === 'ArrowLeft' || e.key === 'PageUp')) stepPresent(-1);
  else if (P && e.key === 'Escape') endPresent();
  else if (!IS_APP && (e.metaKey || e.ctrlKey) && e.key === 'w') { e.preventDefault(); if (active !== TODAY_TAB) closeTab(active); }
});

/* ---------------- right-click / option-click menus ---------------- */
const ctx = $('#ctx');
const mi = (a, label, id, o) => `<button data-c="${a}" data-id="${esc(id || '')}"${o ? ` data-o="${esc(o)}"` : ''}>${label}</button>`;
function showCtx(html, x, y) {
  ctx.innerHTML = html; ctx.hidden = false;
  ctx.style.left = Math.max(8, Math.min(x, innerWidth - ctx.offsetWidth - 8)) + 'px';
  ctx.style.top = Math.max(8, Math.min(y, innerHeight - ctx.offsetHeight - 8)) + 'px';
}
const hideCtx = () => { ctx.hidden = true; };
function tabMenu(id, x, y) {
  const o = ent(id), it = item(id); if (!o || !it) return;
  const others = open.filter(q => q.id !== id && !q.mate && !o.mate);
  let h = mi('rename', 'Rename', id) + (isWeb(it) && !it.path ? mi('edit', 'Edit link…', id) : '') + (o.el._wv ? mi('reload', 'Reload', id) : '') + mi('icon', 'Change icon…', id) + (it.icon ? mi('noicon', 'Remove icon', id) : '') + '<hr>';
  if (o.mate) h += mi('unpair', 'Separate from “' + esc(item(o.mate)?.name) + '”', id) + mi('swap', 'Swap sides', id);
  else if (others.length) h += '<div class="mh">Split view with</div>' + others.map(q => mi('pair', esc(item(q.id)?.name), id, q.id)).join('');
  else h += '<div class="mh">Open a second tab to split</div>';
  h += '<hr>' + mi('left', 'Move left', id) + mi('right', 'Move right', id) + '<hr>' + mi('close', 'Close tab', id);
  showCtx(h, x, y);
}
function tileMenu(id, x, y) {
  const it = item(id); if (!it) return;
  const cand = open.filter(q => !q.mate && q.id !== id);
  let h = mi('open', 'Open', id) + mi('rename', 'Rename', id) + mi('edit', 'Edit…', id) + mi('icon', 'Change icon…', id) + (it.icon ? mi('noicon', 'Remove icon', id) : '');
  if (cand.length) h += '<hr><div class="mh">Open in split with</div>' + cand.map(q => mi('besideof', esc(item(q.id)?.name), id, q.id)).join('');
  showCtx(h, x, y);
}
async function renameItem(id) {
  const it = item(id); if (!it) return;
  const r = await ask({ title: 'Rename', name: it.name, showUrl: false });
  if (!r || r === 'delete' || !r.name) return;
  it.name = r.name; save(); renderTabs(); renderToday();
}
function menuFor(el, x, y) {
  if (el.classList.contains('tab')) return tabMenu(el.dataset.id, x, y);
  const id = el.dataset.lib || el.dataset.id; if (id) tileMenu(id, x, y);
}
const MENU_SEL = '.tab:not(.home),#today .tool,#today .res,#today .chip';
document.addEventListener('contextmenu', e => { const el = e.target.closest(MENU_SEL); if (!el) return; e.preventDefault(); menuFor(el, e.clientX, e.clientY); });
document.addEventListener('click', e => {
  if (!e.altKey) return;
  const el = e.target.closest(MENU_SEL); if (!el) return;
  e.preventDefault(); e.stopPropagation(); menuFor(el, e.clientX, e.clientY);
}, true);
document.addEventListener('click', e => {
  const b = e.target.closest('#ctx [data-c]');
  if (!b) { if (!e.target.closest('#ctx')) hideCtx(); return; }
  const a = b.dataset.c, id = b.dataset.id, o = b.dataset.o; hideCtx();
  if (a === 'rename') { const t = document.querySelector(`#tabs .tab[data-id="${id}"]`); if (t && ent(id)) setTimeout(() => inlineRename(t), 0); else renameItem(id); }
  else if (a === 'edit') editItem(id);
  else if (a === 'icon') pickIcon(id);
  else if (a === 'noicon') { const q = item(id); if (q) { delete q.icon; save(); renderToday(); renderTabs(); } }
  else if (a === 'reload') { try { ent(id)?.el._wv?.reload(); } catch (err) {} }
  else if (a === 'unpair') { unpair(ent(id)); activate(active); }
  else if (a === 'swap') { const x = ent(id), y = x && ent(x.mate); if (y) { const i = open.indexOf(x), j = open.indexOf(y); open[i] = y; open[j] = x; activate(active); } }
  else if (a === 'pair') pairTabs(id, o, 'b');
  else if (a === 'left') stepUnit(id, -1);
  else if (a === 'right') stepUnit(id, 1);
  else if (a === 'close') closeTab(id);
  else if (a === 'open') openItem(id);
  else if (a === 'besideof') openItem(id, o);
});
window.addEventListener('keydown', e => { if (e.key === 'Escape') hideCtx(); });
window.addEventListener('blur', hideCtx);

/* ---------------- Leader Locator groups -> Battleship Jeopardy squads ---------------- */
const isLL = it => it && (it.id === 'a2' || /leader-locator/i.test((it.url || '') + (it.local || '')));
const BIJ_TEAMS = 12;
function parseCsv(t) {
  t = String(t || '').replace(/^\uFEFF/, ''); const rows = []; let r = [], f = '', q = false;
  for (let i = 0; i < t.length; i++) {
    const c = t[i];
    if (q) { if (c === '"') { if (t[i + 1] === '"') { f += '"'; i++; } else q = false; } else f += c; }
    else if (c === '"') q = true;
    else if (c === ',') { r.push(f); f = ''; }
    else if (c === '\n' || c === '\r') { if (c === '\r' && t[i + 1] === '\n') i++; r.push(f); f = ''; rows.push(r); r = []; }
    else f += c;
  }
  if (f || r.length) { r.push(f); rows.push(r); }
  return rows.filter(x => x.some(v => String(v).trim()));
}
async function sendGroups(wv) {
  if (!IS_APP) { toast('This works in the Lily Path app'); return; }
  window.lily.expectGroups();
  let found = false;
  try { found = await wv.executeJavaScript(`(() => { const b = [...document.querySelectorAll('button')].find(x => /export groups/i.test(x.textContent || '')); if (!b) return false; b.click(); return true; })()`); } catch (e) {}
  if (!found) toast('Make groups in Leader Locator first, then tap this again');
}
function gradeFor(cls) { if (/^k/i.test(cls.trim())) return 0; const m = cls.match(/\d/); return m ? Math.min(10, +m[0]) : 3; }
function importGroups(text, fname) {
  const map = new Map();
  parseCsv(text).slice(1).forEach(r => { const g = String(r[0] || '').trim(), n = String(r[1] || '').trim(); if (!g || !n) return; if (!map.has(g)) map.set(g, []); map.get(g).push(n); });
  let teams = [...map].map(([n, m]) => ({ name: n.slice(0, 28), members: m }));
  if (teams.length < 2) { toast('Need at least 2 groups to send'); return; }
  const over = teams.length > BIJ_TEAMS; teams = teams.slice(0, BIJ_TEAMS);
  const cls = String(fname || '').replace(/_groups_.*$/i, '').replace(/_+/g, ' ').trim().slice(0, 24) || 'Class 1';
  const gr = gradeFor(cls); teams.forEach(t => { t.grade = gr; });
  sendToBij({ cls, teams }, over);
}
const BIJ_WRITE = d => { try {
  let m = null; try { m = JSON.parse(localStorage.getItem('bj3-meta') || 'null'); } catch (e) {}
  if (!m || !Array.isArray(m.list) || !m.list.length) m = { current: d.cls, list: [] };
  if (m.list.indexOf(d.cls) < 0) m.list.push(d.cls);
  m.current = d.cls; localStorage.setItem('bj3-meta', JSON.stringify(m));
  const k = 'bj3-setup-' + d.cls; let o = null; try { o = JSON.parse(localStorage.getItem(k) || 'null'); } catch (e) {}
  const s = { teams: d.teams }; if (o && o.cfg) s.cfg = o.cfg;
  localStorage.setItem(k, JSON.stringify(s)); return true;
} catch (e) { return false; } };
function sendToBij(data, over) {
  let it = item('a8') || S.lib.find(i => /battleship/i.test(i.name || ''));
  if (!it) { it = { id: 'a8', type: 'tool', name: 'Battleship Jeopardy', url: G + 'Lily-Path-Suite/apps/battleship-in-jeopardy.html', local: 'apps/battleship-in-jeopardy.html', seeded: 1 }; S.lib.push(it); save(); renderToday(); }
  const had = ent(it.id), cur = active;
  openItem(it.id, had ? null : (cur !== TODAY_TAB ? cur : null));
  const o = ent(it.id), wv = o && o.el._wv; if (!wv) { toast('Battleship needs its link first'); return; }
  const js = `(${BIJ_WRITE.toString()})(${JSON.stringify(data)})`;
  let tries = 0;
  const run = () => wv.executeJavaScript(js).then(ok => {
    if (ok) { wv.reload(); toast(`Sent ${data.teams.length} groups to Battleship` + (over ? ` (it holds ${BIJ_TEAMS} at most)` : '')); }
    else if (++tries < 3) wv.addEventListener('dom-ready', run, { once: true });
    else toast('Could not send. Open Battleship once, then try again.');
  }).catch(() => { if (++tries < 3) wv.addEventListener('dom-ready', run, { once: true }); });
  if (o.el._ready) run(); else wv.addEventListener('dom-ready', run, { once: true });
}

/* ---------------- app hooks ---------------- */
if (IS_APP) {
  window.lily.on('open-url', url => { const it = { id: uid(), type: 'link', name: hostOf(url), url, temp: true }; S.lib.push(it); openItem(it.id); });
  window.lily.on('groups-csv', d => importGroups(d.text, d.name));
  window.lily.on('close-tab', () => { if (active !== TODAY_TAB) closeTab(active); });
  window.lily.on('reload-tab', () => { const o = open.find(x => x.id === active); try { o?.el._wv?.reload(); } catch (e) {} });
}

/* ---------------- go ---------------- */
S.lib = S.lib.filter(i => !i.temp);
const THEMES = [['purple', 'Champion Purple'], ['fire', 'Fire Red'], ['ocean', 'Ocean Blue'], ['jungle', 'Jungle Green'], ['sunset', 'Sunset Orange'], ['candy', 'Candy Pink'], ['galaxy', 'Galaxy'], ['gold', 'Gold Rush'], ['arctic', 'Arctic Ice']];
const applyTheme = () => document.documentElement.dataset.theme = S.theme || 'purple';
$('#themebtn').addEventListener('click', e => { e.stopPropagation(); $('#themes').hidden = !$('#themes').hidden; });
$('#themes').innerHTML = THEMES.map(([k, n]) => `<button class="th-card" data-t="${k}" data-theme="${k}"><span>${n}</span></button>`).join('');
$('#themes').addEventListener('click', e => { const b = e.target.closest('[data-t]'); if (!b) return; S.theme = b.dataset.t; save(); applyTheme(); $('#themes').hidden = true; });
document.addEventListener('click', e => { if (!e.target.closest('#themes')) $('#themes').hidden = true; });
applyTheme();
renderTabs(); renderToday();

/* ---------------- sync across devices (Supabase) ---------------- */
const SEEDV = 9;
const SYNC_URL = G + 'Lily-Path-Suite/apps/sync.html';
const sy = { el: null, loaded: null, in: false, timer: 0 };
const syb = $('#syncbtn');
const syState = (s, tip) => { syb.dataset.s = s; syb.title = tip; };
function syMount() {
  if (sy.el) return sy.loaded;
  let el;
  if (IS_APP) {
    el = document.createElement('webview'); el.setAttribute('partition', 'persist:lily'); el.setAttribute('src', SYNC_URL);
    sy.loaded = new Promise(r => el.addEventListener('dom-ready', () => r(), { once: true }));
  } else {
    el = document.createElement('iframe'); el.src = SYNC_URL;
    sy.loaded = new Promise(r => el.addEventListener('load', () => r(), { once: true }));
  }
  el.style.cssText = 'position:fixed;left:-20px;top:-20px;width:2px;height:2px;opacity:0;pointer-events:none;border:0';
  document.body.appendChild(el); sy.el = el; return sy.loaded;
}
const withTimeout = (p, ms) => Promise.race([p, new Promise((_, j) => setTimeout(() => j(new Error('timeout')), ms))]);
async function syCall(fn, arg) {
  await withTimeout(syMount(), 20000);
  if (IS_APP) return withTimeout(sy.el.executeJavaScript(`(async()=>{await window.__ready;return await window.lilySync.${fn}(${arg === undefined ? '' : JSON.stringify(arg)});})()`), 30000);
  const w = sy.el.contentWindow; await w.__ready; return w.lilySync[fn](arg);
}
const syPayload = () => { const o = { ...S, lib: S.lib.filter(i => !i.path && !i.blob && !i.temp) }; delete o.day; delete o.wk; return o; };
async function syPush() {
  if (!sy.in) return;
  try { await syCall('push', syPayload()); syState('ok', 'Synced'); } catch (e) { syState('err', 'Sync failed: ' + e.message); }
}
syncSoon = () => { if (!sy.in) return; clearTimeout(sy.timer); sy.timer = setTimeout(syPush, 3000); };
function applyRemote(r) {
  const keep = S.lib.filter(i => i.path || i.blob || i.temp);
  const ids = new Set((r.lib || []).map(i => i.id));
  r.lib = (r.lib || []).concat(keep.filter(i => !ids.has(i.id)));
  r.day = S.day; migrateWeeks(r); r.wk = S.wk;
  S = r;
  try { localStorage.setItem(KEY, JSON.stringify({ ...S, lib: S.lib.filter(i => !i.blob && !i.temp) })); } catch (e) {}
  for (const o of [...open]) if (!item(o.id)) closeTab(o.id);
  applyTheme(); renderToday(); renderTabs();
}
async function syPull() {
  if (!sy.in) return;
  try {
    const r = await syCall('pull');
    if (r && (r.seedV || 0) >= SEEDV && (r.at || 0) > (S.at || 0)) {
      if (renaming || $('#dlg').open) return;
      applyRemote(r); syState('ok', 'Synced');
    } else if (!r || (S.at || 0) > (r.at || 0)) await syPush();
    else syState('ok', 'Synced');
  } catch (e) { syState('err', 'Sync failed: ' + e.message); }
}
async function syInit() {
  try {
    const st = await syCall('status');
    sy.in = !!(st && st.signedIn && st.allowed);
    if (!sy.in) return syState('out', st && st.signedIn ? 'That Google account is not allowed' : 'Click to sign in and sync your layout');
    syState('ok', 'Syncing…'); await syPull();
  } catch (e) { syState('err', 'Sync unavailable: ' + e.message); }
}
syb.addEventListener('click', async () => {
  if (syb.dataset.s === 'out' || syb.dataset.s === 'err') {
    await syInit();
    if (!sy.in && syb.dataset.s === 'out') {
      if (IS_APP) { if (!item('sync')) S.lib.push({ id: 'sync', type: 'tool', name: 'Sign in (sync)', url: SYNC_URL, temp: true }); openItem('sync'); }
      else window.open(SYNC_URL, '_blank');
    }
  } else { await syPull(); toast('Synced'); }
});
window.addEventListener('focus', () => { sy.in ? syPull() : syInit(); });
setInterval(() => { sy.in ? syPull() : syInit(); }, 60000);
setTimeout(syInit, 1200);
})();

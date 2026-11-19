/* Runs inside every web page opened in Lily Path (Electron only).
   Suggests saved usernames while you type, fills in the password when you pick one,
   and offers to save a login after you sign in. Everything stays on this Mac. */
const { ipcRenderer } = require('electron');
let box = null, bar = null, curUser = null;
const setVal = (el, v) => {
  const d = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value');
  d.set.call(el, v);
  el.dispatchEvent(new Event('input', { bubbles: true }));
  el.dispatchEvent(new Event('change', { bubbles: true }));
};
const visible = el => !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
function pwField(root) { return [...(root || document).querySelectorAll('input[type=password]')].find(visible) || null; }
function userField(pw) {
  const form = pw.form || document;
  const all = [...form.querySelectorAll('input')].filter(i => visible(i) && /^(text|email|tel|)$/i.test(i.type || ''));
  let best = null;
  for (const i of all) { if (i.compareDocumentPosition(pw) & Node.DOCUMENT_POSITION_FOLLOWING) best = i; }
  return best;
}
function hideBox() { if (box) { box.remove(); box = null; } }
async function showBox(input, pw) {
  const typed = (input.value || '').toLowerCase();
  let list = [];
  try { list = await ipcRenderer.invoke('cred:list'); } catch (e) {}
  list = list.filter(u => u.toLowerCase().startsWith(typed) && u.toLowerCase() !== typed);
  hideBox();
  if (!list.length) return;
  box = document.createElement('div');
  const r = input.getBoundingClientRect();
  box.style.cssText = 'position:fixed;z-index:2147483647;left:' + r.left + 'px;top:' + (r.bottom + 2) + 'px;min-width:' + Math.max(r.width, 200) + 'px;background:#fff;color:#111;border:1px solid #bbb;border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,.25);font:14px system-ui,sans-serif;overflow:hidden';
  list.forEach(u => {
    const row = document.createElement('div');
    row.style.cssText = 'display:flex;align-items:center;gap:8px;padding:8px 10px;cursor:pointer';
    const nm = document.createElement('span'); nm.textContent = u; nm.style.flex = '1';
    const x = document.createElement('span'); x.textContent = '✕'; x.title = 'Forget this login'; x.style.cssText = 'opacity:.5;padding:0 4px';
    row.append(nm, x);
    row.onmouseenter = () => row.style.background = '#eef3ff'; row.onmouseleave = () => row.style.background = '';
    row.onmousedown = async e => {
      e.preventDefault();
      if (e.target === x) { await ipcRenderer.invoke('cred:delete', u); hideBox(); return; }
      const pass = await ipcRenderer.invoke('cred:get', u);
      setVal(input, u); if (pass != null) setVal(pw, pass); hideBox();
    };
    box.appendChild(row);
  });
  document.documentElement.appendChild(box);
}
function wire(pw) {
  if (pw._lily) return; pw._lily = 1;
  const u = userField(pw);
  if (u && !u._lily) {
    u._lily = 1;
    u.addEventListener('focus', () => showBox(u, pw));
    u.addEventListener('input', () => showBox(u, pw));
    u.addEventListener('blur', () => setTimeout(hideBox, 150));
    u.addEventListener('keydown', e => { if (e.key === 'Escape') hideBox(); });
  }
  const remember = () => {
    const user = u ? u.value.trim() : '', pass = pw.value;
    if (user && pass) ipcRenderer.send('cred:pending', { user, pass });
  };
  if (pw.form) pw.form.addEventListener('submit', remember, true);
  pw.addEventListener('keydown', e => { if (e.key === 'Enter') remember(); });
  document.addEventListener('click', e => { const b = e.target.closest && e.target.closest('button,input[type=submit],[role=button]'); if (b && pw.isConnected) remember(); }, true);
}
function scan() { const pw = pwField(); if (pw) wire(pw); }
new MutationObserver(scan).observe(document, { childList: true, subtree: true });
document.addEventListener('DOMContentLoaded', scan); scan();

/* after a sign-in, the next page asks: save this login? */
ipcRenderer.on('cred:offer', (_e, info) => {
  if (pwField()) return; /* password box still showing: the sign-in probably failed */
  if (bar) bar.remove();
  bar = document.createElement('div');
  bar.style.cssText = 'position:fixed;z-index:2147483647;top:10px;right:10px;background:#1f1b3a;color:#fff;border-radius:12px;padding:12px 14px;box-shadow:0 8px 28px rgba(0,0,0,.4);font:14px system-ui,sans-serif;max-width:320px';
  bar.innerHTML = '<div style="margin-bottom:8px">Save login for <b></b>?</div><div style="opacity:.8;margin-bottom:10px;font-size:13px"></div>';
  bar.querySelector('b').textContent = info.host; bar.children[1].textContent = info.user;
  const mk = (t, f, c) => { const b = document.createElement('button'); b.textContent = t; b.style.cssText = 'margin-right:8px;padding:6px 12px;border-radius:8px;border:0;cursor:pointer;font-weight:600;background:' + c + ';color:#111'; b.onclick = () => { f(); bar.remove(); bar = null; }; return b; };
  bar.append(mk('Save', () => ipcRenderer.send('cred:save-pending'), '#ffd166'), mk('Not now', () => ipcRenderer.send('cred:drop-pending'), '#ddd'), mk('Never here', () => ipcRenderer.send('cred:never'), '#ddd'));
  document.documentElement.appendChild(bar);
  setTimeout(() => { if (bar) { bar.remove(); bar = null; } }, 30000);
});

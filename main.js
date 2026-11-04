const { app, BrowserWindow, Menu, ipcMain, dialog, shell, session } = require('electron');
const path = require('path');
const fs = require('fs');
const os = require('os');

let win;

function chromeUA(ua) {
  return ua.replace(/\s?Electron\/\S+/, '').replace(/\s?lily-path\/\S+/i, '').replace(/\s?Lily Path\/\S+/i, '');
}

function createWindow() {
  win = new BrowserWindow({
    width: 1440, height: 900, minWidth: 900, minHeight: 600,
    backgroundColor: '#f5f4ef',
    titleBarStyle: 'hiddenInset',
    trafficLightPosition: { x: 16, y: 14 },
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      webviewTag: true,
      contextIsolation: true,
      nodeIntegration: false,
    },
  });
  win.loadFile('index.html');
}

app.whenReady().then(() => {
  const ses = session.fromPartition('persist:lily');
  ses.setUserAgent(chromeUA(ses.getUserAgent()));
  ses.setPermissionRequestHandler((_wc, _perm, cb) => cb(true));
  app.userAgentFallback = chromeUA(app.userAgentFallback);

  // "Send to Battleship": catch the groups CSV that Leader Locator exports and hand it to the app instead of saving it.
  let expectUntil = 0;
  ipcMain.on('expect-groups', () => { expectUntil = Date.now() + 20000; });
  ses.on('will-download', (_e, item) => {
    const name = item.getFilename();
    if (Date.now() < expectUntil && /_groups_.*\.csv$/i.test(name)) {
      expectUntil = 0;
      const tmp = path.join(os.tmpdir(), 'lily-' + Date.now() + '-' + name.replace(/[^\w.-]/g, '_'));
      item.setSavePath(tmp);
      item.once('done', (_ev, state) => {
        if (state === 'completed') { try { const text = fs.readFileSync(tmp, 'utf8'); if (win) win.webContents.send('groups-csv', { text, name }); } catch (err) {} }
        try { fs.unlinkSync(tmp); } catch (err) {}
      });
    }
  });

  // Links that try to open a new window become a new tab instead.
  app.on('web-contents-created', (_e, wc) => {
    if (wc.getType() === 'webview') {
      wc.setWindowOpenHandler(({ url }) => {
        let h = ''; try { h = new URL(url).hostname; } catch (e) {}
        if (/(^|\.)(accounts\.google\.com|appleid\.apple\.com|login\.microsoftonline\.com|login\.live\.com|auth0\.com|openai\.com)$/.test(h)) return { action: 'allow' };
        if (win) win.webContents.send('open-url', url);
        return { action: 'deny' };
      });
    }
  });

  ipcMain.handle('pick-files', async () => {
    const r = await dialog.showOpenDialog(win, {
      properties: ['openFile', 'multiSelections'],
      filters: [{ name: 'Media & documents', extensions: ['mp4', 'mov', 'm4v', 'webm', 'mp3', 'wav', 'm4a', 'jpg', 'jpeg', 'png', 'gif', 'webp', 'svg', 'pdf', 'html'] }],
    });
    return r.canceled ? [] : r.filePaths;
  });
  ipcMain.on('open-external', (_e, url) => { if (/^https?:\/\//i.test(url)) shell.openExternal(url); });

  Menu.setApplicationMenu(Menu.buildFromTemplate([
    { role: 'appMenu' },
    { label: 'File', submenu: [
      { label: 'Close Tab', accelerator: 'CmdOrCtrl+W', click: () => win && win.webContents.send('close-tab') },
    ] },
    { role: 'editMenu' },
    { label: 'View', submenu: [
      { label: 'Reload Tab', accelerator: 'CmdOrCtrl+R', click: () => win && win.webContents.send('reload-tab') },
      { role: 'togglefullscreen' },
      { role: 'toggleDevTools' },
    ] },
    { role: 'windowMenu' },
  ]));

  createWindow();
  app.on('activate', () => { if (!BrowserWindow.getAllWindows().length) createWindow(); });
});

app.on('window-all-closed', () => app.quit());

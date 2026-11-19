const { contextBridge, ipcRenderer, webUtils } = require('electron');
contextBridge.exposeInMainWorld('lily', {
  pathFor: (file) => webUtils.getPathForFile(file),
  credPreload: ipcRenderer.sendSync('cred-preload-path'),
  pickFiles: () => ipcRenderer.invoke('pick-files'),
  expectGroups: () => ipcRenderer.send('expect-groups'),
  openExternal: (url) => ipcRenderer.send('open-external', url),
  on: (channel, cb) => ipcRenderer.on(channel, (_e, ...a) => cb(...a)),
});

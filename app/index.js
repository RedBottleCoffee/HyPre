const { app, Menu, BrowserWindow, Tray, systemPreferences } = require('electron');
const menubar = require('menubar')
const path = require('path');
const url = require('url');


let mainWindow;

function createWindow() {
  const mb = menubar({
    icon: systemPreferences.isDarkMode() ? __dirname + '/images/icon_white.png' : __dirname + '/images/icon_black.png',
    dir: __dirname,
    width: 500,
    height: 325
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});

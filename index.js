const { app, BrowserWindow } = require('electron')

const createWindow = () => {
  const win = new BrowserWindow({
    width: 500,
    height: 700,
    frame: false,
    transparent: true,
    icon: 'base.png',
    resizable: false,
  })

  win.loadFile('index.html')
}

app.whenReady().then(() => {
  createWindow()
})
import { Hypre } from "./dist/js/libs/hypre"
import { Pyproc } from './dist/js/libs/pyproc'
import { SoundSetting } from './dist/js/libs/sound_setting'


const electron = require('electron').remote
const app = electron.app
const hyper = new Hypre()
const soundSetting = new SoundSetting()

// hyper.exit()

// Initilize
document.querySelectorAll('[name^=sound]').forEach((elem) => {
  console.log(elem.name)

  var sound = elem.name.match(/finger_snapping|bell|applause|gong/)
  soundSetting.param(camelCase(sound.toString()), elem.value)
})


var pyproc = new Pyproc('./pyproc/predicator.py')
pyproc.asyncRun((data) => {
  console.log(data.toString())
})

// 閉じるボタン押したときの処理
document.querySelector('.js-close').addEventListener('click', () => {
  app.quit()
})

// 音声のアクション設定
document.querySelectorAll('[name^=sound]').forEach((elem) => {
  elem.addEventListener('change', function () {
    console.log(this.name)

    var sound = this.name.match(/finger_snapping|bell|applause|gong/)
    soundSetting.param(camelCase(sound.toString()), this.value)
  })
})

// Utility
function camelCase(str){
  str = str.charAt(0).toLowerCase() + str.slice(1)
  return str.replace(/[-_](.)/g, function(match, group1) {
      return group1.toUpperCase()
  })
}

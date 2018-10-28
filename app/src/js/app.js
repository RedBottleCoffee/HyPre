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
  var sound = elem.name.match(/finger|bell|applause|gong/)
  soundSetting.param(camelCase(sound.toString()), elem.value)
})


const pyproc = new Pyproc('./pyproc/predicator.py')
pyproc.asyncRun((data) => {
  var label = data.toString().toLowerCase().replace(/\r?\n/g,"");
  console.log(label)
  if(soundSetting.usableParams.includes(label)){
    const action = eval(`soundSetting.params.${label}`)
    console.log(action)
    eval(`hyper.${action}()`)
  }
})

// 閉じるボタン押したときの処理
document.querySelector('.js-close').addEventListener('click', () => {
  app.quit()
})

// 音声のアクション設定
document.querySelectorAll('[name^=sound]').forEach((elem) => {
  elem.addEventListener('change', function () {
    console.log(camelCase(this.name))

    var sound = this.name.match(/finger|bell|applause|gong/)
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

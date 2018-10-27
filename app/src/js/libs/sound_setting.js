export class SoundSetting {
  constructor(params = {'fingerSnapping': 'next', 'bell': 'esc', 'applause': 'next', 'gong': 'esc'}) {
    this.defaultParams = {'fingerSnapping': 'next', 'bell': 'esc', 'applause': 'next', 'gong': 'esc'}
    this.usableParams =  ['fingerSnapping', 'bell', 'applause', 'gong']

    this.params = this.defaultParams
    this.usableParams.forEach((key) => {
      this.params[key] = params[key]
    })
  }

  param(sound) {
   return this.params[sound]
  }

  param(sound, action) {
    this.params[sound] = action
  }
}

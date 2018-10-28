import { exec } from "child_process";

export class Hypre {
  constructor(presentationSoftware = 'Keynote') {
    this.presentationSoftware = presentationSoftware
  }

  buildAppleScript(keystroke) {
    return `osascript -e '
              tell application "${this.presentationSoftware}"
                activate
                tell application "System Events"
                  keystroke ${keystroke}
                end tell
              end tell'`
  }

  buildAppleScriptWithKeyCode(keycode) {
    return `osascript -e '
              tell application "${this.presentationSoftware}"
                activate
                tell application "System Events"
                  key code ${keycode}
                end tell
              end tell'`
  }

  next() {
    exec(this.buildAppleScript('(ASCII character 29)'))
  }

  previous() {
    exec(this.buildAppleScript('(ASCII character 28)'))
  }

  esc() {
    exec(this.buildAppleScript('"b"'))
  }
}

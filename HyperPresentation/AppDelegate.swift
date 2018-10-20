//
//  AppDelegate.swift
//  HyperPresentation
//
//  Created by arabian9ts on 2018/10/20.
//  Copyright © 2018 RedBottleCoffee. All rights reserved.
//

import Cocoa
import Foundation
import ScriptingBridge

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {
  let statusItem = NSStatusBar.system.statusItem(withLength:NSStatusItem.squareLength)



  func applicationDidFinishLaunching(_ aNotification: Notification) {
    if let button = statusItem.button {
      button.image = NSImage(named: "icon")
      button.action = #selector(runScript(_:))
    }
  }

  func applicationWillTerminate(_ aNotification: Notification) {
      // Insert code here to tear down your application
  }


  @objc func runScript(_ sender: Any?) {
    let appleScript = """
      tell application \"Keynote\"
        activate
        tell application \"System Events\"
          keystroke return
        end tell
      end tell
      """

    var error: NSDictionary?
    if let scriptObject = NSAppleScript(source: appleScript) {
      if let output: NSAppleEventDescriptor = scriptObject.executeAndReturnError(
        &error) {
        print(output.stringValue!)
      } else if (error != nil) {
        print("error: \(String(describing: error))")
      }
    }
  }
  
}


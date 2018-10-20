//
//  AppDelegate.swift
//  HyperPresentation
//
//  Created by arabian9ts on 2018/10/20.
//  Copyright © 2018 RedBottleCoffee. All rights reserved.
//

import Cocoa

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {
  let statusItem = NSStatusBar.system.statusItem(withLength:NSStatusItem.squareLength)



  func applicationDidFinishLaunching(_ aNotification: Notification) {
    if let button = statusItem.button {
      button.image = NSImage(named: "icon")
      button.action = #selector(printQuote(_:))
    }
  }

  func applicationWillTerminate(_ aNotification: Notification) {
      // Insert code here to tear down your application
  }


  @objc func printQuote(_ sender: Any?) {
    let quoteText = "Never put off until tomorrow what you can do the day after tomorrow."
    let quoteAuthor = "Mark Twain"
    
    print("\(quoteText) — \(quoteAuthor)")
  }
}


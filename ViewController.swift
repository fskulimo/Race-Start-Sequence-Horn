//
//  ViewController.swift
//  MQTTDemo
//
//  Created by Filip Skulimowski on 11/6/21.
//

import UIKit
import CocoaMQTT

class ViewController: UIViewController {
    
    
    //Instantiate CocoaMQTT as mqttClient.
    let mqttClient = CocoaMQTT(clientID: "iOS Device", host: "raspberrypi.local", port: 1883)

    override func viewDidLoad() {
        super.viewDidLoad()
        //Do any additional setup after loading the view.
        pauseButton.isEnabled = false //disables the pause button before we press the
        self.startButton.isEnabled = true
    
    
    }
    //Executes when switch changes states (ON or OFF).
    @IBAction func gpio40SW(_ sender: UISwitch) {
        //If switch is ON, publish to topic "rpi/gpio" with message "on".
        if sender.isOn {
            mqttClient.publish("rpi/gpio", withString: "on")
        }
        //If switch is OFF, publish to topic "rpi/gpio" with message "off".
        else {
            mqttClient.publish("rpi/gpio", withString: "off")
        }
        
    }
    
    //Executes when connect button gets pressed.
    @IBAction func connectButton(_ sender: UIButton) {
        mqttClient.connect()
        print("Button pressed")
    }
    
    //Executes when disconnect button gets pressed
    @IBAction func disconnectButton(_ sender: UIButton) {
        mqttClient.disconnect()
    }
    
    @IBOutlet weak var timerLabel: UILabel!
    
    var seconds = 60 //This variable will hold a starting value of seconds. It could be any amount above 0.
    var resetSeconds = 60
    var timer = Timer()
    var isTimerRunning = false //This will be used to make sure only one timer is created at a time, look to make sure this variable has been declared in the View Controller class.
    var resumeTapped = false//Variable used for pause button
    
    @IBOutlet weak var startButton: UIButton!
    
    
    @IBAction func startButtonTapped(_ sender: UIButton) {
        if isTimerRunning == false {
            runTimer()
            self.startButton.isEnabled = false
        }
        
        if self.fiveminButton.isEnabled == false {
            mqttClient.publish("rpi/gpio", withString: "start5minSequence")
        }
        
        if self.threeminButton.isEnabled == false {
            mqttClient.publish("rpi/gpio", withString: "start3minSequence")
        }
        
        if self.twominButton.isEnabled == false {
            mqttClient.publish("rpi/gpio", withString: "start2minSequence")
        }
    }
    
    func runTimer() {
        isTimerRunning = true
        timer = Timer.scheduledTimer(timeInterval: 1, target: self,   selector: (#selector(ViewController.updateTimer)), userInfo: nil, repeats: true)
        pauseButton.isEnabled = true //This ensures that the pause button is enabled when the timer is running already.
    }
    
    
    @IBOutlet weak var pauseButton: UIButton!
    
    @IBAction func pauseButtonTapped(_ sender: UIButton) {
        if self.resumeTapped == false {
            timer.invalidate()
            self.resumeTapped = true
    
        } else {
            runTimer()
            self.resumeTapped = false
        }
    }
    
    @IBAction func resetButton(_ sender: UIButton) {
        timer.invalidate()
        seconds = resetSeconds //Here we manually enter the restarting point for the seconds, but it would be wiser to make this a variable or constant.
        timerLabel.text = timeString(time: TimeInterval(seconds))
        isTimerRunning = false
        pauseButton.isEnabled = false //if reset is tapped then pause should be disabled
        self.startButton.isEnabled = true
        self.fiveminButton.isEnabled = true
        self.threeminButton.isEnabled = true
        self.twominButton.isEnabled = true
        
    }
    
    @objc func updateTimer() {
         if seconds < 1 {
             timer.invalidate()
            //Send alert to indicate "time's up!"
         } else {
             seconds -= 1//This will decrement(count down)the seconds.
             timerLabel.text = timeString(time: TimeInterval(seconds))//This will update the label.
         }
    }
    
    func timeString(time:TimeInterval) -> String {
        let minutes = Int(time) / 60 % 60
        let seconds = Int(time) % 60
        return String(format:"%02i:%02i", minutes, seconds)
    }
    
    
    @IBOutlet weak var fiveminButton: UIButton!
    
    @IBAction func fiveminButtonTapped(_ sender: UIButton) {
        timer.invalidate()
        seconds = 315
        timerLabel.text = timeString(time: TimeInterval(seconds))
        isTimerRunning = false
        self.fiveminButton.isEnabled = false
        self.threeminButton.isEnabled = true
        self.twominButton.isEnabled = true
        self.startButton.isEnabled = true
        
        
    }
    
    
    @IBOutlet weak var threeminButton: UIButton!
    
    @IBAction func threeminButtonTapped(_ sender: UIButton) {
        timer.invalidate()
        seconds = 195
        timerLabel.text = timeString(time: TimeInterval(seconds))
        isTimerRunning = false
        self.threeminButton.isEnabled = false
        self.fiveminButton.isEnabled = true
        self.twominButton.isEnabled = true
        self.startButton.isEnabled = true
        
    }
    
    
    @IBOutlet weak var twominButton: UIButton!
    
    @IBAction func twominbuttonTapped(_ sender: UIButton) {
        timer.invalidate()
        seconds = 135
        timerLabel.text = timeString(time: TimeInterval(seconds))
        isTimerRunning = false
        self.twominButton.isEnabled = false
        self.fiveminButton.isEnabled = true
        self.threeminButton.isEnabled = true
        self.startButton.isEnabled = true
        
    }
    
   
    
    @IBAction func hornButtonTapped(_ sender: UIButton) {
        mqttClient.publish("rpi/gpio", withString: "hornBlow")
    }
}


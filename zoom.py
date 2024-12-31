import serial
import time
import pyautogui

ArduinoSerial = serial.Serial('com9',9600)
'''Create Serial port object called arduinoSerialData.
Arduino serial port can depend on the Arduino Version.
The port '9600' is set for Arduino Uno implemented for this specific project.'''
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print(incoming)
    if 'ZoomOut' in incoming:
        pyautogui.hotkey('ctrl', '-')  
    if 'Zoomin' in incoming:
        pyautogui.hotkey('ctrl', '+')
    if 'Rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')  
    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right') 
    if 'Vup' in incoming:
        pyautogui.hotkey('ctrl', 'down')
    if 'Vdown' in incoming:
        pyautogui.hotkey('ctrl', 'up')
    incoming = "";
import os
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
data = list(input("type in the thing you want to say"))
times = int(input("how many times do you want to say it"))
os.system("open -a messages")
def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def keystroke():
    for temp in data:
        if temp.islower():
            keyboard.press(temp)
            keyboard.release(temp)
            time.sleep(0.03)
        else:
            with keyboard.pressed(Key.shift):
                keyboard.press(temp.lower())
                keyboard.release(temp.lower())


time.sleep(5)
for i in range(times):
    keystroke()
    enter()


import keyboard
import time


print('online')

message = input('what message do you want letter by letter')
print('running in 3 seconds')
time.sleep(3)
for letter in message:
    keyboard.press(letter)
    keyboard.press_and_release('space')
    keyboard.press_and_release('enter')

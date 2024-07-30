import pydirectinput
import utils
import time
from pynput import keyboard
import mouse
import ctypes

# Get the current screen resolution
user32 = ctypes.windll.user32
current_screen_width = user32.GetSystemMetrics(0)
current_screen_height = user32.GetSystemMetrics(1)

positions = utils.loadJson()

original_screen_width = 1728
original_screen_height = 1080

clicks = 0

def scale_coordinates(x, y):
    scaled_x = x * (current_screen_width / original_screen_width)
    scaled_y = y * (current_screen_height / original_screen_height)
    return int(scaled_x), int(scaled_y)

def execute_actions():
    global clicks
    for event in positions:
        if clicks == 4:
            pydirectinput.press('e')
            time.sleep(0.2)
        if event[0] == 'click':
            _, x, y = event
            scaled_x, scaled_y = scale_coordinates(x, y)
            pydirectinput.moveTo(scaled_x, scaled_y)
            time.sleep(0.25)
            pydirectinput.click()
            clicks += 1
        elif event[0] == 'scroll':
            _, x, y, dx, dy = event
            scaled_x, scaled_y = scale_coordinates(x, y)
            pydirectinput.moveTo(scaled_x, scaled_y)
            time.sleep(0.25)
            mouse.wheel(dy)
        time.sleep(0.25)

def on_press(key):
    if key == keyboard.Key.f1:
        execute_actions()
    
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


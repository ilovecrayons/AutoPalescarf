import utils
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller
import mouse
import ctypes
from mousekey import MouseKey
import pydirectinput
import os
from dotenv import load_dotenv
load_dotenv()

mkey = MouseKey()
mkey.enable_failsafekill('ctrl+e')
kb = Controller()
positions = utils.loadJson()

user32 = ctypes.windll.user32
current_screen_width = user32.GetSystemMetrics(0)
current_screen_height = user32.GetSystemMetrics(1)
original_screen_width = int(os.getenv('SCREEN_WIDTH'))
original_screen_height = int(os.getenv('SCREEN_HEIGHT'))
print (current_screen_width, current_screen_height, original_screen_width, original_screen_height)

clicks = 0
def scale_coordinates(x, y):
    scaled_x = x * (current_screen_width / original_screen_width)
    scaled_y = y * (current_screen_height / original_screen_height)
    return int(scaled_x), int(scaled_y)

def execute_actions():
    ePressed = False;
    try:
        global clicks
        for event in positions:
            if clicks == 4 and not ePressed:
                pydirectinput.press('e')
                time.sleep(0.2)
                ePressed = True
            if event[0] == 'click':
                _, x, y = event
                scaled_x, scaled_y = scale_coordinates(x, y)
                mkey.left_click_xy_natural(
                    scaled_x,
                    scaled_y,
                    delay=.3, 
                    min_variation=-2,
                    max_variation=2, 
                    use_every=4, 
                    sleeptime=(0.005, 0.009), 
                    print_coords=True, 
                    percent=90,
                )
                clicks += 1
            elif event[0] == 'scroll':
                _, x, y, dx, dy = event
                scaled_x, scaled_y = scale_coordinates(x, y)
                mkey.left_click_xy_natural(
                    scaled_x,
                    scaled_y,
                    delay=.3, 
                    min_variation=-2,
                    max_variation=2, 
                    use_every=4, 
                    sleeptime=(0.005, 0.009), 
                    print_coords=True, 
                    percent=90,
                )
                mouse.wheel(dy)
            time.sleep(0.2)
    except:
        pass

def on_press(key):
    if key == keyboard.Key.f1:
        execute_actions()
    
try:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
except:
    pass

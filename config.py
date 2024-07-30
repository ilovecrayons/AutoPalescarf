import utils
import pyautogui
from pynput import mouse

positions = []
clicks = 0

def on_click(x, y, button, pressed):
    global clicks
    if pressed:
        positions.append(('click', x, y))
        print(f"Recorded click position: {x}, {y}")
        clicks += 1
        if clicks >= 8:
            return False

def on_scroll(x, y, dx, dy):
    positions.append(('scroll', x, y, dx, dy))
    print(f"Recorded scroll at position: {x}, {y} with offset: {dx}, {dy}")

with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()

print("Recorded positions:", positions)
utils.saveJson(positions)

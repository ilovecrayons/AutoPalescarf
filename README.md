
# AutoPalescarf
Customizable automation script that performs the Pale Scarf Instinct instance bug with one keypress.



## Usage

- Prerequisites: any python3 installation
- Clone and install dependencies:
```bash
  pip install -r requirements.txt
```
- Input the resolution of your primary monitor in the .env environment variable file. My resolution is scaled to 1728x1080, so it would look like this:
```env
SCREEN_WIDTH=1728
SCREEN_HEIGHT=1080
```
- Join a BF server and pick a side, then:  
    1. Run **config.py**
    2. Alt-tab to roblox (Do NOT click on taskbar icon) 
    3. You should currently be using your main accessory. Perform the Pale Scarf instance bug as follows:
    - **Click 1**: "Menu" button to the bottom left.  
    - **Click 2**: "Items" button following the click for "Menu".
    - **Click 3**: scroll down and click on Pale Scarf.  
    - **Click 4**: click "Equip".  
    - **Click 5**: scroll and click on your main accessory. In my case, It would be Pilot Helmet.    
    - **Click 6**: click "Equip" for your main accessory. After this step, you should also scroll all the way up, that way your items window scroll bar is reset the next time you perform the above actions.   
    - **Click 7**: click the red "X" on the items window to close out of the window.  
    - **Click 8**: click on "Close" on the bottom left to contract menu options.  
    
    **You should have clicked on screen no more or less than 8 times by the end of this process. Debug information on the coordinates and order of recorded keypresses are logged to the console.**

- **You are now able to automate your actions by running **main.py**. Press the **f1** key once to execute the recorded actions. Happy bounty hunting!**

    





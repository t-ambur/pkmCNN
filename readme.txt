

--Software Required--
>> python 3.6 or 3.7
>> python modules:
ahk
pyscreenshot
pillow
ctypes, time
os, subprocess, threading, random (should install by default with python)
>> AutoHotkey.exe installed (to default install location OR PATH configured properly)
>> VisualBoyAdvance-M (version 2.1.4) emulator (SPECIFIC VERSION, ALSO MUST BE THE GITHUB M VARIANT)
If you have modified the control scheme for VBA-M, reset one of the schemes to the default keybindings
You will need to go to Options -> Key Shortcuts, then find the command: Screen capture...
Map this shortcut to the = key
>> A terminal or command line tool to execute python scripts.

------Run------
Please note the AI will take control of your keyboard input and will require you to be "hands free"
while it runs the game. It will run on its own unless you start monkeying around.
This is because this AI is a "blackbox" approach to simulate a human playing the game. The AI knows nothing
of the internal code of the game. It will use your keyboard for input and take screenshots of the game window
in order to get feedback from the game. The neural network uses the images received to make decisions on key input.

>> You will need to acquire a pokemon blue ROM
Name the ROM: blue.zip
If your ROM is not a zip file, I can't guarantee that is will work, but you can try changing the ROM name in
constants.py
If you want to start a new game, do not include any save files in this directory, as it will mess with the
timing of the keystroke injection.

If you plan to continue an existing game, make sure you set text speed to fast in the options and battle style to set.
The new game scripts automatically sets up the options for you. After saving a new game, they will automatically
be configured when you run a continued game.
If you want to continue an existing save, make sure to give the continue command as an argument to the command line.

The AI never saves on its own. You will have to stop the script and manually save a game.
(When at the world screen, press ENTER and then use the S-key to go down to the save command, press L to accept the
save.)

Please refrain from resizing the window after launch, the width and height of the screen is important

Place the blue.zip ROM and the emulator in the emulator folder
In your terminal, to start a new game, Run: python pkmblue.py
to start an existing game (after you configure the options), Run: python pkmblue.py continue

Enjoy watching the AI run into walls and faint frequently.

-- training required software --
>> python modules:
opencv-python

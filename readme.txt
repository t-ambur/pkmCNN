

--Software Required--
>> python 3.6 or 3.7
>> python modules:
ahk
ctypes
time
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

create a folder called emulator inside pkmNN (if it doesn't already exist)
Place the blue.zip ROM and the emulator in the emulator folder
In your terminal, Run: python pkmblue.py

Enjoy watching the AI run into walls and faint frequently.

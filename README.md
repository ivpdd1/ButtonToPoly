VIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIV\
VIVIVIVIVI~ REQUIREMENTS ~VIVIVIV\
VIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIV\
Rasberry pi pico - ~5$\
Arduino button - ~1$<\
Arduino wires - ~1$<\
Wire for rasberry pi pico - ~10$\
A computer that is not a potato

VIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIV\
VIVIVIVIVI~ REQUIREMENTS2 ~IVIVIV\
VIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIV\
Node.js - with dgram and http installed(npm install dgram http in cmd)\
https://nodejs.org/en

Python - with pyserial installed(pip install pyserial in cmd)\
https://www.python.org/

CircuitPython 10.1.4(for the rasberry pi pico)
https://circuitpython.org/board/raspberry_pi_pico/

CircuitPython libraries bundle for 10.x version\
https://circuitpython.org/libraries

Playit.gg UDP server\
https://playit.gg/

VIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIV\
VIVIVIVIVI~ TUTORIAL ~VIVIVIVIVIVIV\
VIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIVIV

Connect via breadboard(or just solder)\
Rasberry pi pico GP6---->Arduino button(any pin)
Rasberry pi pico GND---->Arduino button(any pin)

Connect to the pc(Rasberry pi pico---->Wire---->pc)\
Drop the uf2 file of circuitpython to your pico, it should reboot\
Open "lib" folder in explorer\
Drag adafruit_hid and adafruit_ticks.mpy from libraries bundle

Open code.py in rasberry pi pico and paste this:

```python
import board
import digitalio
import time

button = digitalio.DigitalInOut(board.GP6)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

last = None

while True:
    current = not button.value
    if current != last:
        if current:
            print("down")
        else:
            print("up")
        last = current
    time.sleep(0.01)
```

Dont run it yourself, and dont use repl(it should run automatically)

Open this folder\
Edit buttonbridge.py and include your port with the url of the tunnel\
Run playit.gg, wait for it to load\
Click the path\
Enter cmd\
It should open a command prompt\
Enter bridge.js in it\
Repeat\
Enter buttonbridge.py

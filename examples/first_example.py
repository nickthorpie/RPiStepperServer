# Awkward patch for running examples inside the project folder
import sys, os
sys.path.insert(1,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.rpi_stepper_server import motorClient
del sys.path[0]

import numpy as np
from time import sleep

dir_pin=1
step_pin=2
enable_pin=3
freq = 10000 #hz


motor = motorClient(dir_pin,step_pin,enable_pin,freq)

# Send
try:
    while True:
        # pick a random location between -1000 to 1000, ask motor to move
        random_loc = int((np.random.rand()*2-1)*1000)
        motor.move_to(random_loc)
        sleep(1)
except KeyboardInterrupt:
    # motor.close_pipe()
    pass
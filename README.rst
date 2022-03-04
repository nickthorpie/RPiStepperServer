# RPiStepperServer

A Raspberry Pi package to run a stepper motor parallel with a python process

## Description

Running a stepper motor with a raspberry Pi and python in one process has several drawbacks. Current libraries have one
of two problems:
  1. the code blocks until the stepper reaches its destination
  2. the stepper runs in series with the code, and its speed is limited by the total loop time.

This package aims to solve this problem by creating a parallel c++ script to run the stepper. The python front-end
initializes the motor server, and communicates with it through a fifo IPC. This project also serves as a straightforward
example for IPC between c++ and python processes.

## Getting Started

### Dependencies
- Raspberry Pi with Raspbian Buster
- python ~= 3.7.2
- tested on unix systems (mac, linux)

### Installing
Simply git-clone the project into your working directory.
[Will finish this when ready]

### Executing program

Currently, this project is in development. Try running the example code from any computer to see the user interface.
At the moment, C++ server script has empty placeholders functions for pin-writing.
TODO:
    - Replace the server digitalwrite function with wiringPi functions
    - Acceleration support
    - Second pipe to return position updates
    - Verbosity toggle

## Help
not tested on windows.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info
Nick Thorpe

## Version History

* 0.0
    Development code (prerelease)


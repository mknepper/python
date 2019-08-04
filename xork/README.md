# Introduction

![Banner](https://github.com/mknepper/master/python/xork/images/logo.png)

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/agpl-3.0)

A text adventure written in Python 3, set in a space station! Can you outwit the terror that lurks between the walls?

## Story

You are a technician aboard a large towing vessel in deep space, heading to the nearest spaceport. The system's power appears to be down, you're alone and something else is lurking in the ship's corridors with you. Originally, I intended to have the user escape their bedroom, but I'm going to leave it as-is; I think it illustrates the purpose of using `While` loops fairly well.

## Running

Below is a list of instructions to install, run and play Xork. Operating sytem specific instructions are also listed below. Dependencies include:

- Python 3+

If new dependencies are required, they will be listed here. Operating systems specific dependencies are listed below in their respective subcategories. Note that Mac OS X, or any version thereof Mac, is not officially supported, though it should work as well as any other platform for Python 3.x.

### Windows (XP & Newer)

To run the game, simply install Python 3. For now, the game runs only in a terminal. On Windows (XP+), you can use CMD.

To run, navigate to the directory of xork's src:

`cd C:\xork\src`

Then use Python 3 to run the script.

`python main.py`

You're all set! Enjoy.

### Linux (Debian Based Systems)

Install Python 3 if it has not already been installed. You can use Python 3 or 3.5, or which ever 3.x is available on your system. Open a terminal and run this to install Python:

`sudo apt install python3`

Afterward, navigate to the xork directory:

`cd ~/xork/`

This is how you'd execute the game inside the terminal. Enter this command:

`python3 src/main.py`

You must specify `python3` as Python 2.x is incompatible with Xork.

#!/usr/bin/env python3

# This is a very basic PyGame program importing and initializing the pygame library.
# It also opens a PyGame window, but doesn't draw anything there yet.

import pygame

SCREEN_X = 640
SCREEN_Y = 480

pygame.init()

# Setting the display mode also opens the PyGame window that will be used later.
pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)

print("hello")

# Inifinite loop that will be terminated when the QUIT event is returned from pygame.event.wait().
# The wait function will wait until any event happens inside the pygame window (keyboard, mouse, etc).
while True:
    event = pygame.event.wait()
    # Inspect the event by reading the "type" attribute of the event object.
    if event.type == pygame.QUIT:
        print("got a quit event")
        exit()   # Terminate the Python process.
    else:
        # Just out of curiosity: print the other events.
        print(event)

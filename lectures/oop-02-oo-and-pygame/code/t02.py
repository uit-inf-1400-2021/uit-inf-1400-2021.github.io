#!/usr/bin/env python3

# This one expands on t01.py by loading a background image that we draw (using screen.blit).
# Screen.blit only renders to a background buffer. To see that buffer, we need to use pygame.display.update().
# See PyGame introductoin and documentation for more information.

import pygame

SCREEN_X = 640
SCREEN_Y = 480
BG_FNAME = "Chapter03/sushiplate.jpg"

pygame.init()

# Setting the display mode also opens the PyGame window that will be used later.
# set_mode() returns an object that represents the window that was opened.
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)

# Load the background image into an image object.
background = pygame.image.load(BG_FNAME)

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

    # Draw the background image into a back buffer. By rendering into back buffer first, we
    # finish drawing everything before we expose it to the viewer on the screen.
    screen.blit(background, (0, 0))

    # Drawing done. Now we can make it visible to the user by flipping the back buffer to be visible
    # (or rendered) in the window.
    pygame.display.update()

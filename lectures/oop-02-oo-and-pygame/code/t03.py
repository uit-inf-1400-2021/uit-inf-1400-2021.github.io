#!/usr/bin/env python3

# This program expands on t02.py by displaying a fish that follows the mouse pointer/cursor.

# For those that know what docstrings are: we will introduce them a bit later, so there will be no docstrings yet.

# The program also demonstrates tuple unpacking as we will find it in code soon anyway
# (see pygame.mouse.get_pos() in the main loop at the end of the program).
# If you find this confusing, don't worry. It will become clearer later in the semester.
#
# To summarize quickly :
# 1) As a quick introduction to tuples: think about them as the read-only equivalent to lists.
# 2) 1, 2 is a short-hand for creating a tuple: (1, 2)
#    This is similar to the lsit [1, 2] except you can't add or remove items from a tuple.
# 3) "tuple unpacking" basically means that you can assign each of the values from a tuple on the
#    right side of a equal sign to each of the variables on the left side:
#       x, y = (1, 2)
#    is equivalent to
#      (x, y) = (1, 2)
#    which pretty much does the same thing as
#      t = (1, 2)
#      x = t[0]
#      y = t[1]
#    but with fewer lines of code and fewer places to introduce bugs.
#    It also avoids adding a temporary variable ("t").
# 4) get_pos() returns a tuple with the x and y coordinate of the mouse.
#    so x, y = get_pos()  unpacks the coordinates and assigns them to the
#    variables of x, y.


import pygame

SCREEN_X = 640
SCREEN_Y = 480
BG_FNAME = "Chapter03/sushiplate.jpg"
MOUSE_FNAME = "Chapter03/fugu.png"
BALL_FNAME = "ball.png"

pygame.init()

# Setting the display mode also opens the PyGame window that will be used later.
# set_mode() returns an object that represents the window that was opened.
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)

# Load the background image into an image object.
background = pygame.image.load(BG_FNAME)

# Load mouse and ball images. These contain alpha components (invisible/transparent pixels)
# and must be converted to a format that is more efficient for PyGame to work with.
# To do this, we first load the image like with the background image.
# Then we use the convert_alpha() method of the image object to create a new
# image object with the more efficient representation.
mouse_img = pygame.image.load(MOUSE_FNAME)
mouse_img = mouse_img.convert_alpha()
ball_img = pygame.image.load(BALL_FNAME)
ball_img = ball_img.convert_alpha()


# Example function. Not used for anything in particular, it was just addded to compare
# functions with methods (the equivalent inside classes/objects).
def f(x):
    print("this is f with x=", x)


# The first example class. A ball object that has a few attributes, but not much else.
# It shows how to
# - define a class,
# - initiallize objects created from that class (using __init__())
# - create methods  (move and draw)
class Ball:
    def __init__(self):
        self.x = 42
        self.y = 20
        self.img = ball_img

    def move(self):
        pass

    def draw(self):
        pass


print("hello")

# Inifinite loop that will be terminated when the QUIT event is returned from pygame.event.wait().
# The wait function will wait until any event happens inside the pygame window (keyboard, mouse, etc).
while True:
    event = pygame.event.wait()

    # Inspect the event by reading the "type" attribute of the event object.
    if event.type == pygame.QUIT:
        print("got a quit event")
        exit()   # Terminate the Python process.

    # Get position of the mouse.
    # See discussion a the top of the file for an explanation of tuple unpacking.
    x, y = pygame.mouse.get_pos()

    # To draw the fish centered on the mouse cursor, we need to offset the drawing position with
    # half of the image width and height.
    # We use two methods on the image to read the height and width of the image, and use
    # // to get integer division (to avoid getting floating point values).
    mx = x - mouse_img.get_width() // 2
    my = y - mouse_img.get_height() // 2

    # Draw the background image into a back buffer. By rendering into back buffer first, we
    # finish drawing everything before we expose it to the viewer on the screen.
    screen.blit(background, (0, 0))

    # Draw the "mouse cursor" fugu in front of the background image.
    screen.blit(mouse_img, (mx, my))

    # Drawing done. Now we can make it visible to the user by flipping the back buffer to be visible
    # (or rendered) in the window.
    pygame.display.update()

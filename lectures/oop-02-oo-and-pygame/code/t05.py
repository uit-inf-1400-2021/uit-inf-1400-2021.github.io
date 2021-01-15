#!/usr/bin/env python3

# This version adds a new type of moving objects: Circle.
# The interface of the Ball and Circle objects are the same, while the implementation differs.
# This allows us to call move() and draw() on any ball or circle object, ignoring which type of object is
# (see the objs list and the move and draw loops towards the end of the file).
# We will expand on this concept later, introducing Polymorphy.

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
import random

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


# The first example class.
# It shows how to
# - define a class with attributes.
# - initiallize objects created from that class (using __init__())
# - methods for moving the ball around and drawing the ball.
class Ball:
    def __init__(self):
        # Add a random part to the speed and position to let us see the objects moving
        # separately.
        self.x = 42 + random.random() * 90
        self.y = 20 + random.random() * 90
        self.speed_x = 40 + random.random() * 90
        self.speed_y = 40 + random.random() * 90
        self.img = ball_img

    def move(self, time_passed):
        # If the ball is outside the window, make sure the speed points back into the
        # window again.
        if self.x < 0:
            self.speed_x = abs(self.speed_x)
        if self.y < 0:
            self.speed_y = abs(self.speed_y)
        if self.x > SCREEN_X:
            self.speed_x = -abs(self.speed_x)
        if self.y > SCREEN_Y:
            self.speed_y = -abs(self.speed_y)

        self.x = self.x + self.speed_x * time_passed
        self.y = self.y + self.speed_y * time_passed

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


# A first example of the usefulness of having the same interface for multiple classes and objects.
# This draws a circle instead of rendering a ball image. It also has a different speed than the Ball objects.
class Circle:
    def __init__(self):
        # Add a random part to the speed and position to let us see the objects moving
        # separately.
        self.x = 42 + random.random() * 90
        self.y = 20 + random.random() * 90
        self.speed_x = 40 + random.random() * 180
        self.speed_y = 40 + random.random() * 180
        self.size = 30
        self.col = (255, 255, 0)

    def move(self, time_passed):
        # If the circle is outside the window, make sure the speed points back into the
        # window again.
        if self.x < 0:
            self.speed_x = abs(self.speed_x)
        if self.y < 0:
            self.speed_y = abs(self.speed_y)
        if self.x > SCREEN_X:
            self.speed_x = -abs(self.speed_x)
        if self.y > SCREEN_Y:
            self.speed_y = -abs(self.speed_y)

        self.x = self.x + self.speed_x * time_passed
        self.y = self.y + self.speed_y * time_passed

    def draw(self):
        pygame.draw.circle(screen, self.col,
                           (round(self.x), round(self.y)),
                           self.size // 2)


# Just to illustrate the flexibility of keeping the interface the same but doing different things:
# this class looks the same to the main loop, but it doesn't actually do anything useful in the
# move() and draw() methods.
class Sneaky:
    def __init__(self):
        pass

    def move(self, time_passed):
        pass

    def draw(self):
        # print("sneaky")
        pass


# For this program, it will be better to have a list of objects (possibly of different types)
# than to have a variable for each object.
# To see why, look at where we call move() and draw() in the main loop.
# Using a list like this, it's easy to add or remove objects that have to be handled in the game.
objects = [
    Ball(),
    Ball(),
    Ball(),
    Circle(),
    Circle(),
    Sneaky(),
]


print("hello")

# Create a clock object that can be used to keep track of time in the game and
# control the frame rate / game update rate.
clock = pygame.time.Clock()

# Inifinite loop that will be terminated when the QUIT event is returned from pygame.
# The main problem with using event.wait() is that the loop is blocked waiting for any event to happen.
# Effectively, the game is frozen until the user moves the mouse.
#
# The wait function will wait until any event happens inside the pygame window (keyboard, mouse, etc).
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("got a quit event")
            exit()

    # This does two things:
    # a) limits the framerate to 30 Hz by checking how much time passed since the last time
    #    tick() was called and sleeping until it's time for the next frame.
    # b) tick() returns the number of miliseconds since the last time tick() was called.
    #    divide by 1000 to get the number of seconds, which can then be used to compute a smoother movement
    #    (focusing on how much an object has moved in real time rather than per tick).
    time_passed = clock.tick(30) / 1000.0

    # Get position of the mouse.
    # See discussion a the top of the file for an explanation of tuple unpacking.
    x, y = pygame.mouse.get_pos()

    # To draw the fish centered on the mouse cursor, we need to offset the drawing position with
    # half of the image width and height.
    # We use two methods on the image to read the height and width of the image, and use
    # // to get integer division (to avoid getting floating point values).
    mx = x - mouse_img.get_width() // 2
    my = y - mouse_img.get_height() // 2

    # Instead of handling each object (and object) type individually, we can just iterate
    # over each object and focus on them having a move() method we can call.
    for obj in objects:
        obj.move(time_passed)

    # Draw the background image into a back buffer. By rendering into back buffer first, we
    # finish drawing everything before we expose it to the viewer on the screen.
    screen.blit(background, (0, 0))

    # Similar to the move phase, we can now iterate over the objecs and ask them to draw() themselves,
    # whatever that means for each of the objects.
    for obj in objects:
        obj.draw()

    # Draw the "mouse cursor" fugu in front of the background image.
    screen.blit(mouse_img, (mx, my))

    # Drawing done. Now we can make it visible to the user by flipping the back buffer to be visible
    # (or rendered) in the window.
    pygame.display.update()

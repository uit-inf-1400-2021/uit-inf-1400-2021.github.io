Event-driven programming
========================

Programming styles
------------------

Batch-oriented programming style:

* Program flows in a preplanned way
* It may wait for input from the user

Event-driven programming:

* Program decides what to do next based on events that occur (mouse clicks, keyboard inputs, timers, communication over networks...)
* Graphical user interfaces (GUI) are often programmed using event-driven programming

Event-driven programming:
-------------------------

Not a part of object-oriented programming, but can be seen in OO programs:

* Useful way to write many programs (GUI...)
* Objects are useful for modeling events and event handlers


Basics of event-driven programming
----------------------------------

You have already used an example. PyGame main loops use event-driven programming:

```python
while not finished:
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True
    ...
```

`pygame.event.get()` fetches all events that have happened since the last call. Returns a sequence of events.

Events
--------

An event typically represents something that has happened or should
happen. Examples could be key presses, mouse movements, arriving
network packets or spaceships firing lasers.

Events are often represented as objects in OO systems. This provides
several useful properties, including:

* The type of the event object can be used to decide how to handle it.
* The objects can contain additional information about the event (ex: which key was pressed)
* Events may have methods that can be useful for handling them.
* Subclassing can be used to provide events with additional attributes and methods


Event queues
-------------

One important property is that the part that creates the event does
not necessarily need to know where or how the event is handled. The
triggering, or firing, of events is disconnected from the handling of
events.

To do this, it's useful to have an *event queue*. The queue is somewhere
to store events (for the part of the program that fires off events)
and a place to retrieved queued events (for the part that handles
events).

A simplified event queue:

```python
class EventQueue:
    def __init__(self):
        self.__queue = []
    def add(self, event):
        """Adds an event to the queue."""
        self.__queue.append(event)
    def get(self):
        """Removes all events from the queue and returns a list of the removed events."""
        events = self.__queue
        self.__queue = []
        return events
```

In PyGame, the event queue is handled internally in PyGame:

`pygame.event.get()` transfers control over to PyGame. It:
* Does bookkeeping and detects new events
* Stores new events on an event queue (temporarily)
* Removes and returns the events as a sequence


Event handling
--------------

Determining the type of event and responding with appropriate action is called event handling:

```python
for event in pygame.event.get():
    if event.type == QUIT:
        finished = True
```

Events can also be handled by event-handlers. These can be implemented as functions or objects.

Determining which handler to call is called dispatching:

```python
for event in pygame.event.get():
    if event.type == FOO:
        # event handler function
        foo_handler(event)
    if event.type == BAR:
        # calling handle() method on object
        bar_handler.handle(event)
```

Event dispatchers
-----------------

A dispatcher routes events to event handlers. Can be implemented as an object. A simple example:

```python
class Dispatcher:
    def __init__(self):
        self.__handlers = {}

    def register_handler(self, etype, handler):
        self.__handlers[etype] = handler
    def dispatch(self, event):
        if event.type in self.__handlers:
            self.__handlers[event.type](event)
        else:
            print("Unknown event type", event.type, pygame.event.event_name(event.type))
```

Using it with PyGame code:

```python
def mouse_motion_handler(event):
    print("Moving mouse", event.pos, event.rel)

dispatcher = Dispatcher()
dispatcher.register_handler(MOUSEMOTION, mouse_motion_handler)

finished = False
while not finished:
    for event in pygame.event.get()
        if event.type == QUIT:
            finished = True
        else:
            dispatcher.dispatch(event)
```

Why event dispatchers and handlers?
-----------------------------------

Extensible concept: users can extend program by adding handlers to dispatcher.

No need to modify event dispatcher source code to add new event types.

Generating events
-----------------

* Event-based systems often provide a method for adding events to the event queue.
* This lets users add new event types to programs as well as handlers.
* NB: Can also be used for scripted testing.
* In PyGame, this is done using `pygame.event.post`

Common event types in PyGame
----------------------------

Mouse events:
* `event.pos`: xy-position that the mouse moved to
* `event.rel`: relative motion since last event
* `event.buttons`: state of buttons when the event was created

Keyboard events:
* KeyDown (when a key is pressed) and KeyUp (when the key is released)
* The event contains information about the key pressed and modifiers (shift, alt etc.)

Timer events
--------------

Timers are events that are set to fire off after a certain amount of time.
Can be one-shot or periodic.
PyGame timers are periodic, and fire off an event of a specified type every N milliseconds.

```python
# fires an event of type MY_EVENT (USEREVENT+1) every 2000 milliseconds
MY_EVENT = USEREVENT+1
pygame.time.set_timer(MY_EVENT, 2000)
```

Example use: periodic update of information, such as the arms of a clock.

Event-driven programming problems
----------------------------------

Allowing handlers to change state: requires access to the state. (Example: variable in object or method).
Some solutions:

* Global variables
* Default params to functions
* Storing state or methods in event handler objects

How do you reason about the program?

* What happens when and in which order?
* When did somebody change this state?

Links
------

* [Pygame events](http://www.pygame.org/docs/ref/event.html)
* [Event-driven programming](http://en.wikipedia.org/wiki/Event-driven_programming)

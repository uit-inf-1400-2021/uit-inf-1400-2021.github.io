Summary lecture
------------------

This lecture summarizes key points of the corriculum.

Object-oriented programming
-------------------------

The idea of modeling code around objects - entities with state and methods.

state - something that describes the object (attributes): 
* "The *wooden* door is *open*"
* "Your bank account has *1300* NOK in it"

methods - operations interacting with, and belonging to, the object
* "*Close* the door"
* "*Withdraw* 100 NOK from your bank account"

Inheritance
----------------

When a class extends another.

Hint that inheritance is the correct framework:
When you need a class that is a specialized version of a different class.

Car is-a vehicle:

```python
class Vehicle:
  def __init__(self, direction, speed, position):
    self.speed = speed
    self.position = position
    self.direction = direction

  def move(self):
    self.position += self.speed * self.direction

class Car(Vehicle):
  def accelerate(self, speed):
    self.speed += speed
```

Composition
---------------

Hint that composition is the correct framework:
- When only one of the methods in a class needs
  to access the attributes or methods from another class.
- When an instance of a class has ownership of instances
  of another class.
- When it's not natural to access the "child" object's attributes
  as attributes on the "parent"
- "Are you a wheel, or do you have a wheel?"

Car has-a wheel:

```python
class Car(Vehicle):
  def __init__(self, ...):
    ...
    self.wheels = [Wheel() for x in range(4)]

  def accelerate(self, speed):
    self.speed += speed
```

Abstraction
-------------------

Wrapping something complex in a simple interface.
Hiding implementation.

"It is not the car's responsibility to turn the wheels,
but to apply force to the wheels"

Interface
-------------------

The method of interacting with something.
What you look up when looking at documentation.
The interface of a class is exposed through methods and public attributes.
API (Application Programming Interface) is a type of interface.
The implementation of an abstraction.
Java interfaces are a specific language feature.


Polymorphism
-------------------

"Many forms"
Where the behavior depends on the type.

Overriding:
When a child changes behavior from the parent.

```python
class Car(Vehicle):
  ...
  def move(self):
    self.speed *= 0.9
    self.position += self.speed * self.direction
```

Duck typing:
- When type is not the determinant for interface.
- When the specific type of an object is not important, as long
as they expose the same subset of an interface


```python
def ducktyped_func(target):
  return str(target)

ducktyped_func("Hello world")
ducktyped_func(Car())
```

Multiple inheritance
-------------------

When a class combines and/or extends multiple parent classes.
- Watch out for the diamond problem!

Hints that multiple inheritance may be the correct framework:
- When you need a hybrid of multiple classes
- Mixins

```python

class Hakkespett(Fjerkre, Flyvende):
```


Exceptions
-------------------

Delegating error handling to where the error can be handled.
- Pass an error through some code to where it should be handled
- Differentiate different errors (handle different errors in different places)
- Catch specific errors
- Seperate error handling for specific errors from code that causes the error

```python
# Where to handle the error?
def read_file(filename)
  result = ""
  try:
    result = open(filename).read()
  except:
    pass
  return result

# Maybe we could handle the exception here?
def get_user_file():
  fn = get_filename_from_user()
  return read_file(fn)
```

```python
# Alternative
def read_file(filename)
  return open(filename).read()

# Maybe we could handle the exception here?
def get_user_file():
  fn = get_filename_from_user()
  try:
    return read_file(fn)
  except FileNotFoundError:
    get_new_filename()
```


When OOP makes sense
-------------------

When modeling objects.  

Understanding when modeling objects is difficult.

This is modeling objects: https://docs.python.org/3.8/library/heapq.html

When passing in objects as an argument to a function that modifies the
object, this is perhaps a hint that there should be a class. 

Or should it? Take a look at `heapq.heapify`.


When OOP doesn't make sense
-------------------

When not modeling objects!
When a class has a method and an init, it might not model an object.


Design patterns
-------------------

* Iterating through a data structure - Iterator
* Wrap some code inside some other code - Wrapper
* Only allow a single instance of a class (huge code smell) - Singleton
* Adapt an interface to another interface - Adapter
* Simplify a complex interface - Facade
* Selecting an implementation - Abstract factory


Testing
------------------

Unit testing basics.

```python
def my_func(x, y):
  return x + y

def test_my_func():
  assert my_func(10,5) == 15
```

Exceptions
===========

What we'll look at today
------------------------

- What are exceptions
- Why use exceptions over other error handling methods
- How to raise exceptions
- How to handle exceptions

Background
------------

C-style error handling:
- return values (need to remember to check)
- halting program if serious errors that we cannot fix

Some issues:
- Information necessary for handling an error might not be available where the error occurs
- People forget to check errors
- What was the context of the error?


Exceptions:
- Automatically triggered by the language/runtime when errors occur
- Can be raised by the programmer to signify particular problems or situations
- Exception objects used to keep information about the exception
  - Human readable error message
  - Type of exception
  - Context
  - ...

Exception mechanisms are commonly supported in object-oriented languages. Classes and objects are also used to implement the exception mechanisms in the language and lets the programmer extend the usage in their own programs.


Some of the code examples below are from the textbook.


Triggering an exception
---------------------

```python
>>> x = 5 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

```python
>>> lst = [1,2,3]
>>> print(lst[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

- Some languages distinguishes errors from exceptions.
- Python handles them in the same way.


Raising exceptions
------------------

Exception raised by using `raise` with an Exception object.


```python
class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)

e = EvenOnly()
```


```python
>>> e.append("A string")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "t.py", line 4, in append
    raise TypeError("Only integers can be added")
TypeError: Only integers can be added
```

Triggering an exception:
- halts the program
- Unwinds the call stack until a handler for that exception (or a general handler) is found
- If no handler found: Python prints the call stack and some exception information before halting


```python
>>> e.append(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "t.py", line 6, in append
    raise ValueError("Only even numbers can be added")
ValueError: Only even numbers can be added
```

```python
>>> e.append(2)
>>>
```

```python
def foo():
    e = EvenOnly()
    print("Here")
    e.append(3)
    print("But never here")

foo()
```


Handling exceptions
-------------------

Simple pattern, catching all types of exceptions:

```python
try:
    foo()
except:
    print("Got an exception, but which one?")
```

Some languages use `try .. catch ` to do the same (Java, Javascript, C++, ...).

Two main problems:
- don't know which exception we caught
- may have caught too many. Was it correct to catch and suppress every exception?


Can check for the type/class of the exception object:

```python
def funny_division(anumber):
    try:
        return 100 / anumber
    except ZeroDivisionError:
        return "Silly wabbit, you can't divide by zero!"
print(funny_division(0))
print(funny_division(50.0))
print(funny_division("hello"))
```

```python
Silly wabbit, you can't divide by zero!
2.0
Traceback (most recent call last):
  File "t.py", line 40, in <module>
    print(funny_division("hello"))
  File "t.py", line 35, in funny_division
    return 100 / anumber
TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

Catching several types:

```python
except (ZeroDivisionError, TypeError):
```

```python

except ZeroDivisionError:
    return "Enter a number other than zero"
except TypeError:
    return "Enter a numerical value"
except ValueError:
    print("No, No, not 13!")
    raise raise
```

`raise raise` re-raises the current exception. Allows us to do such things as cleaning up or print information before passing on the exception.


#### Capturing the exception object

Can be used to inspect the exception and the context.


```python
try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were", e.args)
```

Defining your own
-----------------

Python has a hierarchy of exception classes.

You can inherit from Exception or any of the others to create your own.

```python
class FooNotAllowed(Exception):
    pass

raise FooNotAllowed("Exactly")
```


When to use (or not to use)
---------------------------

Don't use them for common concepts such as returning values. There is an overhead with exception that may be expensive in some languages.

```python
# Bad idea

class RetVal(Exception):
    def __init__(self, val):
        super().__init__("Returned {}".format(val))
        self.val = val

def smallest(lst):
    minval = min(lst)
    raise RetVal(minval)

try:
    smallest([3, 1, 4])
except RetVal as e:
    print("Smallest value is {}".format(e.val))
```

Better to use for
- errors
- exceptional situations
- situations where it may be complicated to unwind and return values correctly

The latter thinking is often used in Python for iterations (see below), but can
also be used for decision making, branching and message passing.


Iterating over a sequence and creating an iterator object
---------------------------------------------------------

We need the following to iterate over a sequence (such as lists, tuples, strings, ... ):
* Keep track of the current position in the sequence
* A method of advancing our position to the next position in the sequence (potentially returning the next item in the sequence)

An iterator is an object that does this and provides a standard interface that can be used by, for instance, loop constructs such as "for".


In Python, sequence objects have an `__iter__` method that returns an iterator object. One way of getting access to the iterator is to use the `iter` operator:

```python
>>> iter([1,2,3])
<list_iterator object at 0x7fb266a01400>
```

A `for` construct, such as the one below, first calls `iter()` on the sequence to get the iterator object, then it continuously calls `next()` on the iterator object to fetch values from the sequence (through the iterator). The iterator's main task is to keep track of the current location in the sequence and to fetch the next value:

```python
for v in [1,2,3]:
    print(v)

# Is equivalent to:
i = iter([1,2,3])
while True:
    print(next(i))
```



The iterator object again has a `__next__` method that is called by Python's `next()` operator to fetch the next object in a sequence.

We need some method for terminating the iteration over the sequence. Any object can be returned by the iterator. Using specific tokens as return values from `__next__` is fragile as this may break code that needs to iterate over such tokens. Python solves this by using a `StopIteration` exception to terminate iterations.

We can implement our own sequence classes and iterators as follows:


```python
class SomeIterator:
    def __init__(self, prefix):
        self.prefix = prefix
        self.i = 0

    def __iter__(self):
        """This object can be it's own iterator"""
        return self

    def __next__(self):
        self.i += 1
        if self.i < 10:
            return "{} - {}".format(self.prefix, self.i)
        if self.i == 10:
            return "Warning: You're overdoing it"
        raise StopIteration("You did it. Now I'm done.")


for val in SomeIterator("Yay"):
    print(val)
print("Done")


Yay - 1
Yay - 2
Yay - 3
Yay - 4
Yay - 5
Yay - 6
Yay - 7
Yay - 8
Yay - 9
Warning: You're overdoing it
Done
```


Further exception logic
-----------------------

```python
try:
    f = open("somefile")
except:
    print("Could not open file")
else:
    print("No problems with the file")
    f.close()
finally:
    print("Done with everything")
```

- try - code block to attempt executing
- except - code block executed when an exception is raised
- else - code block executed when an exception is _not_ raised
- finally - code block always executed after the other blocks


Context manager preview
------------------------

Context managers simplify the try - finally pattern:

```python
# Without context manager
try:
    f = open("test.py")
    do_something(f)
finally:
    f.close()

with open("test.py") as f:
    do_something(f)

```

Used for other things as well:

```python
# Without context manager
lock = threading.Lock()

lock.acquire()
do_something()
lock.release()

# With context manager
lock = threading.Lock()

with lock:
    do_something()


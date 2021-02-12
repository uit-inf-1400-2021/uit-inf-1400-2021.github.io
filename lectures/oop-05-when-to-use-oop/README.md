When to Use Object-oriented Programming (OOP 5)
==============================================

What we'll look at this lecture
--------------------------------

- What is an object?
- What are getters and setters, and how to avoid them.
- Some hints that can help you design better code.
- When _not_ to use objects and classes covered later.

Treating objects as objects
---------------------------

One view:
- objects have both data and behaviour
- if you only need data, uses lists, sets, dictionaries etc.
- no need to add extra levels of abstraction if it doesn't help organize your code


The following code has informally defined objects and functions that act specifically on them.

```python
import math

square = [(1,1), (1,2), (2,2), (2,1)]

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i+1])
    return perimeter
```

This is reasonable for explorative programming (strictly speaking, square _is_ an object), but can be clearly expressed using classes.


```python
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)

class Polygon:
    def __init__(self):
        self.vertices = []
    def add_point(self, point):
        self.vertices.append((point))
    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter
```

It is easier for the programmer to make the right representation for Point and Square/Polygon objects when we have defined classes.


Using properties to add behaviour to class data (and how to avoid using getters/setters)
-----------------------------------------------

Many languages encourage the use of getters and setters early (some guides say always).

```python
class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name
```

In Java and many other languages, you can't change your mind at a later point. You need to future-proof your code.

At a future point:
```python
    def set_name(self, name):
        if not name or not legal_name(name):
            raise Exception("Invalid name")
        self._name = name
```


Getters and setters are clumsy notations for someting that can syntactically be expressed clearer with equal signs/assignment. They are often encouraged because some languages don't provide a better alternative.

```python
c = Color("#ff0000", "bright red")

# consider
print(c.get_name())
c.set_name("red")

# vs.
print(c.name)
c.name = "red"


# consider
c2.set_name(c.get_name())

# vs
c2.name = c.name
```

Python's property mechanism supports future proofing without having to throw out the natural syntax.

```python
# Original class
class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name

# Using properties for "name"
class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)


>>> c = Color("#0000ff", "bright red")
>>> print(c.name)
bright red
>>> c.name = "red"
>>> print(c.name)
red
>>> c.name = ""
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "setting_name_property.py", line 8, in _set_name
raise Exception("Invalid Name")
Exception: Invalid Name
```

One way to think about this: `property` constructs a `name` object that uses the two specified get/set methods instead of the normal attribute set/get methods.

The property constructor can also accept a delete function and a docstring for the property.


### Properties using decorators

_Sneak peak at decorators. Will be covered more later._

Python has a simpler way of defining properties using decorators:

```python
class Foo:
   @property
   def foo(self):
      return self._foo

   @foo.setter
   def foo(self, value):
      self._foo = value
```

Decorators are defined using the `@`-syntax. The internals of decorators work because functions and methods in Python are first class objects. You can treat it like any other object, and also wrap it inside other functions. We will look into this in another lecture.

A More complete example. Note that the docstring of the first method becomes the docstring of the property/attribute:
```python
class Silly:
   def __init__(self):
      self._silly = 42
   @property
   def silly(self):
      "This is a silly property"
      print("You are getting silly")
      return self._silly

   @silly.setter
   def silly(self, value):
      print("You are making silly {}".format(value))
      self._silly = value

   @silly.deleter
   def silly(self):
      print("Whoah, you killed silly!")
      del self._silly
```

### When to use properties

- Methods and functions should represent actions
- Data should be represented as attributes
- When you need to add attribute control (like filtering) or other internal representation, use properties.


Managing objects
----------------

Lots of details in the code in the book, but in general the ideas are as follows:

### Delegating

Rather than making a large method that "does everything" in a class

```
   a
   b
   c
```

we delegate to helper methods
```
   a()
   b()
   c()
```

We can now inherit from the base class and replace the functionality of some of these helper methods. Examples: supporting different compression/file formats, and doing other operations.
Avoids duplicating code to provide other functionality.

Example from the book:

```python
import os
import shutil
import zipfile

class ZipProcessor:
   def __init__(self, zipname):
       self.zipname = zipname
       self.temp_directory = "unzipped-{}".format(zipname[:-4])

    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)

    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()

    def zip_files(self):
        file = zipfile.ZipFile(self.zipname, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
            shutil.rmtree(self.temp_directory)
```

```python
from zip_processor import ZipProcessor
import sys
import os

class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        '''perform a search and replace on all files
        in the temporary directory'''
        for filename in os.listdir(self.temp_directory):
            with open(self._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(
                self.search_string, self.replace_string)
            with open(self._full_filename(filename), "w") as file:
                file.write(contents)

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).process_zip()
```

```python
from zip_processor import ZipProcessor
import os
import sys
from pygame import image
from pygame.transform import scale

class ScaleZip(ZipProcessor):
    def process_files(self):
        '''Scale each image in the directory to 640x480'''
        for filename in os.listdir(self.temp_directory):
            im = image.load(self._full_filename(filename))
            scaled = scale(im, (640,480))
            image.save(scaled, self._full_filename(filename))

if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4]).process_zip()
```

### Supporting reuse through composition

```python
import os
import shutil
import zipfile

class ZipProcessor:
    def __init__(self, zipname, processor):
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(zipname[:-4])
        self.processor = processor

    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)

    def process_zip(self):
        self.unzip_files()
        self.processor.process(self)
        self.zip_files()

    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()

    def zip_files(self):
        file = zipfile.ZipFile(self.zipname, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)
```

```python
from zip_processor import ZipProcessor
import sys
import os

class ZipReplace:
    def __init__(self, search_string, replace_string):
        self.search_string = search_string
        self.replace_string = replace_string

    def process(self, zipprocessor):
        '''perform a search and replace on all files in the
        temporary directory'''
        for filename in os.listdir(zipprocessor.temp_directory):
            with open(zipprocessor._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with open(zipprocessor._full_filename(filename), "w") as file:
                file.write(contents)

if __name__ == "__main__":
    zipreplace = ZipReplace(*sys.argv[2:4])
    ZipProcessor(sys.argv[1], zipreplace).process_zip()
```



More about this later in the course (look at CH 7):
---------------------------------------------------

The wrong question: Can I make a class for this?
Easily leads you astray:
- Too many classes
- Complex class hierarchy
- Support classes adding even more complexity

Better question: will my code be easier to read and extend if I transform this into a class?

Some control questions:
- Do you really need a class?
- Does the class add clarity?
- What are the implications of introducing a class?
- What are the alternatives?

Tell-tale patterns:
-------------------

Function calls that look like this:

```
f(a, b)
f2(a, c)
f3(a, d)
```

Could potentially make more sense as

```
a.f(b)
a.f2(c)
a.f3(d)
```

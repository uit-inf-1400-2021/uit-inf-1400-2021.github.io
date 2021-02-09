class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)

def t():
    e = EvenOnly()        

    e.append("A string")

    e.append(3)


    


def foo():
    e = EvenOnly()
    print("Here")
    e.append(3)
    print("But never here")


try:
    foo()
except:
    print("Got an exception, but which one?")


def t2(): 
    def funny_division(anumber):
        try:
            return 100 / anumber
        except ZeroDivisionError:
            return "Silly wabbit, you can't divide by zero!"
    print(funny_division(0))
    print(funny_division(50.0))
    print(funny_division("hello"))



try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were", e.args)
    print(dir(e))
    print(repr(e))
    print("Handling done")


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

def testiterator():
    for val in SomeIterator("Yay"):
        print(val)
    print("Done")

    t = SomeIterator("kdjfk")
    print(next(t))
    
testiterator()


def testiter2():
    i = iter([1,2,3])
    while True:
        print(next(i))
testiter2()

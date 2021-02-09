
# This is the EvenOnly class that we used in the lecture
class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)

# Code example from the lecture... What does this print?         
def foo():
    e = EvenOnly()
    print("Here")
    e.append(3)
    print("But never here")


foo()    

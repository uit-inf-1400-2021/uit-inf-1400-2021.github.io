
import math
from random import randint

# Oppgave 1

def oppg1a():
    for number in range(0, 100):
        print(number)

def oppg1b():
    for number in range(0, 100, 2):
        #også greit med if test for elevene
        print(number)

def oppg1c():
    OS_list = ["panther", "tiger", "leopard", "snow leopard", "windows vista"]
    for OS in OS_list:
        print(OS)

def oppg1d():
    OS_list = ["panther", "tiger", "leopard", "snow leopard", "windows vista"]
    for number, OS in enumerate(OS_list):
        print(number, OS)

def oppg1e():
    OS_list = ["panther", "tiger", "leopard", "snow leopard", "windows vista"]
    OS_list.pop()
    for OS in OS_list:
        print(OS)

def oppg1f():
    OS_list = ["panther", "tiger", "leopard", "snow leopard", "windows vista"]
    OS_list.sort()
    for OS in OS_list:
        print(OS)

# Oppgave 2

def oppg2b():
    print(math.cos(54))

def oppg2c():
    for number in range(20, 40):
        print(math.sqrt(number))

# Oppgave 3

def make_phonebook():
    return {"Hans": 24528243, "Trude": 72531063, "Ole": 26911036}

def oppg3b():
    new_phonebook = make_phonebook()    
    for name in new_phonebook:
        print(name)

def oppg3c():
    new_phonebook = make_phonebook()    
    for number in new_phonebook.values():
        print(number)

def print_phonebook(phonebook):
    for name, number in phonebook.items():
        print(name, "has number: ", number)

def add_ccodes(phonebook):
    for name, number in phonebook.items():
        phonebook[name] = number + 4700000000

# Oppgave 4

class Account(object):
    def __init__(self):
        self.value = 0

    def deposit(self, number):
        self.value += number

    def whitdrawal(self, number):
        self.value -= number

    def status(self):
        print(self.value)

class Phonebook():
    def __init__(self):
        self.contacts = {"Hans": 24528243, "Trude": 72531063, "Ole": 26911036}

    def print_phonebook(self):
        for name, number in enumerate(self.contacts):
            print(name, " has number: ", number)
            #print("{} has number {}".format(name, number))
    def add_ccodes(self):
        for name, number in enumerate(self.contacts):
            self.contacts[name] = number + 4700000000

# Oppgave 5

class Guess(object):
    def __init__(self):
        self.number = randint(0, 100)

    def guess(self):
        valid_input = False        
        while not valid_input:
            try:
                new_input   = int(input('Guess a number between 0 and 100: '))
                valid_input = True
            except ValueError:
                print("Invalid number")
        
        return self.number - new_input 
        
    def run(self):
        play = True
        while play:           
            result = self.guess()            
            if result > 0:
                print("Your number is too low.")
            elif result < 0:
                print("Your number is too high.")
            else:
                print("Correct!")
                play = False 
           

if __name__ == '__main__':

    # Oppgave 1
    #oppg1a()
    #oppg1b()
    #oppg1c()
    #oppg1d()
    #oppg1e()
    #oppg1f()

    # Oppgave 2
    #oppg2b()
    #oppg2c()

    # Oppgave 3
    #oppg3b()
    #oppg3c()
    #mybook = make_phonebook()
    #add_ccodes(mybook)
    #print_phonebook(mybook)

    # Oppgave 4
    #my_account = Account()
    #my_account.deposit(100)
    #my_account.whitdrawal(40)
    #my_account.status()

    # Oppgave 5
    new = Guess()
    new.run()

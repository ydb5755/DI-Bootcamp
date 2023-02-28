
# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.


# 🌟 Exercise 2: Currencies
# Instructions
import math
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

#     Your code starts HERE

    def __int__(self):
        return self.amount

    def __str__(self):
        if self.amount > 1:
            return f'{self.amount} {self.currency}s'
        return f'{self.amount} {self.currency}'

    def __repr__(self):
            return f"{self.__class__.__name__} ('{self.currency}', {self.amount})"
    
    def __add__(self,other):
        if other.__class__.__name__ != Currency:
            return self.amount + other
        
        x = Currency(self.currency, self.amount + other.amount)
        return x.amount
    
    def __iadd__(self, other):
        if other.__class__.__name__ != Currency:
            self.amount = self.amount + other
            return self.amount
        else:
            x = Currency(self.currency, self.amount + other.amount)
            x.amount
        


# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)




# print(c1+=c2)
# 15

# c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
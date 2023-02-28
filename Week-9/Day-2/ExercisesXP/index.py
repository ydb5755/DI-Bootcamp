
# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

def absolute(num):
    '''this function returns the absolute value of the argument given'''
    return abs(num)

def make_int(num):
    '''Takes a number or string of number and turns it into an integer'''
    return int(num)

def take_input():
    '''Requests input from user and returns the input'''
    x = input('please enter something')
    return x


# print(input().__doc__)
# 🌟 Exercise 2: Currencies
# Instructions
# import math


# class Currency:
# 	def __init__(self, currency, amount):
# 		self.currency = currency
# 		self.amount = amount

# 	#     Your code starts HERE

# 	def __int__(self):
# 		return self.amount

# 	def __str__(self):
# 		if self.amount > 1:
# 			return f'{self.amount} {self.currency}s'
# 		return f'{self.amount} {self.currency}'

# 	def __repr__(self):
# 		return f"{self.__class__.__name__} ('{self.currency}', {self.amount})"

# 	def __add__(self, other):
# 		if isinstance(other, int):
# 			return self.amount + other

# 		if isinstance(other, Currency):
# 			if self.currency != other.currency:
# 				raise TypeError(f'Cannot add between Currency type {self.currency} and {other.currency}')
# 			return self.amount + other.amount

# 	def __iadd__(self, other):
# 		if isinstance(other, int):
# 			self.amount += other

# 		else:
# 			self.amount += other.amount

# 		return self


# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# c1 += 5
# c1 += c2
# print(c1)
# 15

# c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
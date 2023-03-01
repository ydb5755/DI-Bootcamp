# Instructions :
# Create a Person class which will have three properties:
# Name
# List of foods they like
# List of foods they hate
# Note: A person can have an empty list for foods they hate and/or love.

# In this class, create the method taste():
# It will take in a food name as a string.
# Return {person_name} eats the {food_name}.
# If the food is in the person’s like list, add ‘and loves it!’ to the end.
# If it is in the person’s hate list, add ‘and hates it!’ to the end.
# If it is in neither list, simply add an exclamation mark to the end.
# Examples

# p1 = Person("Sam", ["ice cream"], ["carrots"])
# p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"

# p1.taste("cheese") ➞ "Sam eats the cheese!"

# p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"
class Person():
    def __init__(self, name, list_of_likes:list=[], list_of_hates:list=[]):
        self.name = name
        self.list_of_likes = list_of_likes
        self.list_of_hates = list_of_hates
    
    def taste(self, food:str):
        add_on = ''
        if food in self.list_of_likes:
            add_on = ' and loves it'
        elif food in self.list_of_hates:
            add_on = ' and hates it'
        else:
            add_on = ''
        return f'{self.name} eats the {food}{add_on}!'

p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste('ice cream'))
print(p1.taste('cheese'))
print(p1.taste('carrots'))
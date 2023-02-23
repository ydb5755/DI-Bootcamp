# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.

class Family():
    def __init__(self, members:list, last_name:str):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
    
    def is_18(self, name):
        for person in self.members:
            for value in person.values():
                if value == name and person['age'] > 18:
                    return True
        return False
    
    def family_presentation(self):
        print(self.last_name)
        for person in self.members:
            print(person['name'])
                    

Rogers = Family([{'name':'Michael','age':35,'gender':'Male','is_child':False},{'name':'Sarah','age':32,'gender':'Female','is_child':False}], 'Rogers')

Rogers.born(name='Jojo',age=0,gender='Male',is_child=True)
# print(Rogers.is_18('Michael'))
# Rogers.family_presentation()

# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:

# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]


# 2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# 3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.


# 4. Call the incredible_presentation method.
# 5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# 6. Call the incredible_presentation method again.
class TheIncredibles(Family):
    def __init__(self, members: list, last_name: str):
        super().__init__(members, last_name)
    
    def use_power(self, name):
        for person in Dursley.members:
            for value in person.values():
                if value == name and person['age'] > 18:
                    print(person['power'])
                    return 
        raise Exception('Youre not over 18 yet!!')
    
    def incredible_presentation(self):
        super().family_presentation()
        for person in self.members:
            print(person['incredible_name'], person['power'])


Dursley = TheIncredibles([{'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},{'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}], 'Dursley')

# Dursley.use_power('Michael')
Dursley.incredible_presentation()
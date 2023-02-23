
# 🌟 Exercise 1 : Pets
# Instructions
# Using this code:

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# bingo = Bengal('bingo', 2)
# bango = Chartreux('bango',5)
# bongo = Siamese('bongo',10)
# all_cats = [bingo,bango,bongo]
# sara_pets = Pets(all_cats)
# sara_pets.walk()

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.power = self.run_speed()*self.weight
    
    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        return (self.weight/(self.age*10))
    
    def fight(self, other_dog):
        if self.power > other_dog.power:
            return f'{self.name} is the winner!'
        else:
            return f'{other_dog.name} is the winner!'
        
reggie = Dog('reggie', 4, 15)
ronald = Dog('ronald', 2, 10)
ruby = Dog('ruby', 7, 30)

# print(reggie.run_speed())

# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

import random
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *args):
        dog_names = self.name
        for arg in args:
            dog_names += ' ' + arg.name
        print(f'{dog_names} all play together')

    def do_a_trick(self):
        tricks = [f'{self.name} does a barrel roll', f'{self.name} stands on his back legs', f'{self.name} shakes your hand', f'{self.name} plays dead']
        n = random.randint(0,3)
        if self.trained:
            print(tricks[n])
        else:
            print('This dog cant do tricks, its not trained')


regina = PetDog('regina', 6, 18)

regina.train()
regina.do_a_trick()

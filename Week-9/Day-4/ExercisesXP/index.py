# 🌟 Exercise 1 : Human
# Instructions
# Create a class Human, it has the following attributes:
# name (str)
# age (int)
# living_place (Building - Default is None)

# Create another class Building, it has the following attributes:
# address (str)
# inhabitants (List of Human objects - Default is empty)

# Create a class City, it has the following attributes:
# name (str)
# buildings (List of Building objects - Default is empty)

# Add the move(self, building) method to the Human class, it sets the living place of this human to the building and add this human to the building inhabitants.
# Add the construct(self, address) method to the City class, it adds a building at the referenced address.
# Add the info(self, address) method to the City class, it displays the number of buildings and the mean age of the citizens.
# Created objects and call the methods


class Building():
    # use List type annotations from typing
    def __init__(self, address:str, inhabitants:list=[]) -> None:
        self.address = address
        self.inhabitants = inhabitants

class Human():
    def __init__(self, name:str, age:int, living_place:Building=None):
        self.name = name
        self.age = age
        self.living_place = living_place
    
    def move(self, building):
        self.living_place = building
        building.inhabitants.append(self)

class City():
    def __init__(self, name:str, buildings:list=[]) -> None:
        self.name = name
        self.buildings = buildings
    
    def construct(self, address):
        '''it adds a building at the referenced address.'''
        self.buildings.append(Building(address))

    def info(self):
        '''it displays the number of buildings and the mean age of the citizens'''
        ages_added_up = 0
        num_of_humans = 0
        for building in self.buildings:
            for human in building.inhabitants:
                num_of_humans += 1
                ages_added_up += human.age
        avg_age = ages_added_up/num_of_humans
        return f'There are {len(self.buildings)} buildings in {self.name} and the average age of all inhabitants is {avg_age}'
    

brooklyn = City('Brooklyn')
brooklyn.construct('2000 Nostrand ave')
brooklyn.construct('2048 New York ave')
brooklyn.construct('1500 Bedford ave')

richard = Human('richard', 25, )
richard.move(Building('2000 Nostrand ave'))
henry = Human('henry', 40)
henry.move(Building('2048 New York ave'))
rebbeca = Human('rebbeca', 29)
rebbeca.move(Building('2048 New York ave'))
donald = Human('donald', 33)
donald.move(Building('2048 New York ave'))
robert = Human('robert', 48)
robert.move(Building('2000 Nostrand ave'))
bob = Human('bob', 51)
bob.move(Building('2000 Nostrand ave'))
gary = Human('gary', 18)
gary.move(Building('1500 Bedford ave'))

print(brooklyn.info())

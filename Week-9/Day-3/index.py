# Description
# Create a class called Character with the following attributes and methods:
# attribute name
# attribute life – starts with a default value of 20
# attribute attack – the base attack of a character (integer) will be a default of 10
# method basic_attack() - accepts another Character instance as a parameter. Your character will <attack> the other character so his <life> points should drop.
class Character():
    def __init__(self, name, life=20, attack:int=10):
        self.name = name
        self.life = life
        self.attack = attack
    
    def basic_attack(self, Character):
        Character.life -= self.attack

class Druid(Character):
    def __init__(self, name, life=20, attack: int = 10):
        super().__init__(name, life, attack)
        print(f'Welcome {self.name}, to the world of peace....')

    def meditate(self):
        self.life += 10
        self.attack -= 2
    
    def animal_help(self):
        self.attack += 5
    
    def fight(self, Character):
        Character.life - (0.75*self.life + 0.75*self.attack)

class Warrior(Character):
    def __init__(self, name, life=20, attack: int = 10):
        super().__init__(name, life, attack)
        print(f'{self.name}! Get ready to FIGHT!')
    
    def brawl(self, Character):
        Character.life -= 2*self.attack
        self.life += .5*self.attack

    def train(self):
        self.attack += 2
        self.life += 2

    def roar(self, Character):
        Character.attack -= 3

class Mage(Character):
    def __init__(self, name, life=20, attack: int = 10):
        super().__init__(name, life, attack)
        print(f'Magic, {self.name}... magic at the tips of your fingers...')

    def curse(self, Character):
        Character.attack -= 2
    
    def summon(self):
        self.attack += 3
    
    def cast_spell(self, Character):
        Character.life -= self.attack/self.life


gimli = Warrior('Gimli',100)
gandalf = Mage('Gandalf',150)
radagast = Druid('Radagast',75)

gimli.basic_attack(radagast)
gimli.brawl(gandalf)
gimli.roar(gandalf)
gimli.train()
gandalf.basic_attack(gimli)
gandalf.cast_spell(radagast)
gandalf.curse(gimli)
gandalf.summon()
radagast.basic_attack(gimli)
radagast.animal_help()
radagast.fight(gimli)
radagast.meditate()
print('gimli',gimli.life)
print('gimli',gimli.attack)
print('gandalf',gandalf.life)
print('gandalf', gandalf.attack)
print('radagast',radagast.life)
print('radagast', radagast.attack)
# Instructradagastions
# Now create 3 different classes that inherit from Character:
# Every character type should say (ie. print) something when they are created, get creative :)
# Druid:
# meditate() - increases life by 10, decrease attack by 2
# animal_help()- increases attack by 5
# fight() - accepts another Character instance as a parameter and subtracts (0.75*life + 0.75*attack) from the other character’s life.
# Example:
# druid.fight(other_char): other_char.life - (0.75*self.life + 0.75*self.attack)

# Warrior:
# brawl() - accepts another Character instance as a parameter, subtracts (2*attack) to the other characters life and adds (0.5*attack) to his own life.
# train() - increases both your attack and life points by 2.
# roar() - accepts another Character instance as a parameter and subtracts their attack points by 3.

# Mage:
# curse() – accepts another Character instance as a parameter and subtracts their attack points by 2.
# summon() - increases attack attribute by 3 points.
# cast_spell() - accepts another Character instance as a parameter and subtracts attack/life to the other character’s life points (eg if your attack is 20 and life is 5 you will subtract 4 life points).

# Once all your classes are created start testing them, create one of each character and use each of their method.
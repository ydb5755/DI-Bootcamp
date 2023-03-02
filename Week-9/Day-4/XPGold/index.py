# Create a Door class, it has only the following attributes:
# id (int) : An id number, use a class variable objs that counts how many door have been created so far and use this number as the id of the door.
# locked (boolean)
# next (List of Door obs) : The next doors available from this one

# Create a method can_go_to(self, other_door) in the Door class that checks if the path from this door to other_door can be made (the locked doors cannot be opened !).

# Bonus: Display the path
# Bonus 2: Add an integer variable KEYS that holds a limited number of keys available to open locked doors (each key can be used only once).

class Door():
    objs = 0
    keys = 3
    next = []
    def __init__(self, locked:bool):
        Door.objs += 1
        self.id = Door.objs
        self.locked = locked
        Door.next.append(self)
    
    def unlock(self):
        if Door.keys < 1:
            print("You dont have enough keys to open the door!")
            return 
        if self.locked == False:
            print('This door is already unlocked, you dont need to use a key')
            return
        self.locked = False
        Door.keys -= 1
        
    def can_go_to(self, other):
        for count, item in enumerate(Door.next):
            if self.id < other.id:
                if self.id -1 <= count <= other.id - 1:
                    if item.locked == True:
                        return False
            else:
                if other.id -1 <= count <= self.id - 1:
                    if item.locked == True:
                        return False
        path = []
        for count, item in enumerate(Door.next):
            if self.id < other.id:
                if self.id -1 <= count <= other.id - 1:
                    path.append(item.id)
            else:
                if other.id -1 <= count <= self.id - 1:
                    path.append(item.id)
        print(path)
        return True


red = Door(True)
blue = Door(False)
green = Door(True)
orange = Door(False)
yellow = Door(False)
# print(Door.next)
# print(Door.keys)
orange.unlock()
yellow.unlock()
green.unlock()
blue.unlock()
print(yellow.can_go_to(green))

    

    
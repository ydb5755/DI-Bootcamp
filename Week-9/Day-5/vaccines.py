# Vaccines Management System
# Your goal is to create a program to help a city with the vaccination of its citizens.



# Part 1
# You will have to create two classes:
# Human
# Queue


# Human
# Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), priority (bool) and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.

# This class has no methods.
import random
class Human():
    id = 0
    def __init__(self, name:str, age:int, priority:bool, blood_type:str):
        Human.id += 1
        self.id = Human.id
        self.name = name
        self.age = age
        self.priority = priority
        self.family = []
        while True:
            if blood_type == "A" or blood_type == "B" or blood_type == "AB" or blood_type == "O":
                self.blood_type = blood_type
                break
            else:
                blood_type = input(f"Please enter a valid blood type for {self.name}(A, B, AB, or O)")
            self.blood_type = blood_type
    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)




# Queue
# Represents a queue of humans waiting for their vaccine.
# It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.
class Queue():
    def __init__(self, humans:list=[]) -> None:
        self.humans = humans

    def add_person(self, person:Human): 
        # Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the list (at index 0) before every other.
        if person.age > 60 or person.priority:
            self.humans = [person] + self.humans
        else:
            self.humans.append(person)

    def find_in_queue(self, person:str):
        #Returns the index of a human in the queue.
        for counter, human in enumerate(self.humans):
            if human.name == person:
                return counter

    def swap(self, person1, person2):
        #Swaps person1 with person2
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        temp = self.humans[index1]
        self.humans[index1] = self.humans[index2]
        self.humans[index2] = temp
        return f"Swap complete, {self.humans[index2].name} has changed spots with {self.humans[index1].name} "

    def get_next(self):
        # Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.
        # Every human returned by get_next and get_next_blood_type is removed from the list.
        temp = self.humans[0]
        self.humans.remove(self.humans[0])
        return temp.name

    def get_next_blood_type(self, blood_type):
        # Returns the first human with this specific blood type.
        # Every human returned by get_next and get_next_blood_type is removed from the list.
        for human in self.humans:
            if human.blood_type == blood_type:
                temp = human
                self.humans.remove(human)
                return temp.name
        

    def sort_by_age(self):
        # first the priority people
        # then, the older people
        # then the younger people
        temp_list = []
        for human in self.humans:
            if human.priority:
                temp_list.append(human)
        for human in self.humans:
            if human.age >= 60:
                temp_list.append(human)
        for human in self.humans:
            if human.age < 60:
                temp_list.append(human)
        self.humans = temp_list

    def rearange_queue(self):
        pass
    # Add the rearange_queue(self) method to the Queue class, so that there won’t be two members of the same family one after the other in the line.

        

main = Queue()
jeff = Human('jeff', 12, False, "B")
john = Human('john', 59, False, "A")
jake = Human('jake', 78, False, "AB")
judith = Human('judith', 58, True, "O")
main.add_person(jeff)
main.add_person(john)
main.add_person(jake)
main.add_person(judith)
# print(main.find_in_queue('john'))
# print(main.swap('jeff', 'john'))
# print(main.find_in_queue('john'))
# print(main.get_next())
# print(main.get_next_blood_type("A"))
# main.sort_by_age()
# print(main.get_next_blood_type("A"))
# print(main.humans[0].name)
judith.add_family_member(jake)
judith.add_family_member(john)
print(jake.family[0].name)

# This class is useful to manage who will get vaccinated in priority. It has the following methods:

# add_person(self, person) : Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the list (at index 0) before every other.

# find_in_queue(self, person) : Returns the index of a human in the queue.

# swap(self, person1, person2): Swaps person1 with person2.

# get_next(self) : Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.

# get_next_blood_type(self, blood_type) : Returns the first human with this specific blood type.

# sort_by_age(self) : Sorts the queue
# first the priority people
# then, the older people
# then the younger people

# Every human returned by get_next and get_next_blood_type is removed from the list.
# Those functions return None if the list is empty (ie. no one in the list).

# Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.



# Part 2
# Human
# Create an attribute family for the Human class.

# Initialized as empty, family is a list of all the humans that are living in the same house with this human.
# Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.



# Queue
# Add the rearange_queue(self) method to the Queue class, so that there won’t be two members of the same family one after the other in the line.


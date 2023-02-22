# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color = "blue"

# nc = NewCircle
# print(nc.color)
# >> What will be the output ?
# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1)
# print(nc.diameter)

# nc.grow()

# print(nc.diameter)
# class MyClass(object):
#     def func(self):
#         print("I'm being called from the Parent class")


# class ChildClass(MyClass):
#     def func(self):
#         print("I'm actually being called from the Child class")
#         print("But...")
#         # Calling the `func()` method from the Parent class.
#         super(ChildClass, self).func()

# my_instance_2 = ChildClass()
# my_instance_2.func()

# class Door:
#     def __init__(self, is_opened:bool):
#         self.is_opened = is_opened
#     def open_door(self):
#         self.is_opened == True
#     def close_door(self):
#         self.is_opened == False

# class BlockedDoor(Door):
#     def __init__(self):
#         super().__init__(False)
#     def open_door(self):
#         raise Exception('sorry the blocked door cannot be opened')
#     def close_door(self):
#         raise Exception('sorry the blocked door cannot be closed')
    
# blocked = BlockedDoor()
# print(blocked.is_opened)
# print(blocked.open_door())

# class A():

#     def dothis(self):
#         print("doing this in A")


# class B(A):
#     pass


# class C():
#     def dothis(self):
#         print("doing this in C")


# class D(B, C):
#     pass

# d_instance = D()
# d_instance.dothis() 

class Book():
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')

class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awesome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awesome = is_awesome
        if self.is_awesome:
            self.bored = False
            print('Woow this is an awesome book')
        else:
            self.bored = True
            print('I am very bored')

if __name__ == '__main__':
    foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
    foundation.present()
    print(foundation.price)
    print(foundation.bored)
    boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
    print(boring_book.bored)
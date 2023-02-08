
# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# my_fav_numbers = {1, 5, 8}
# my_fav_numbers.add(14)
# my_fav_numbers.add(15)
# my_fav_numbers.remove(15)
# friend_fav_numbers = {1,2,3,5}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(my_fav_numbers)
# print(friend_fav_numbers)
# print(our_fav_numbers)


# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple? 

## No


# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove('Banana')
# basket.remove('Blueberries')
# basket.append('Kiwi')
# basket.insert(0, 'Apples')
# print(basket.count("Apples"))
# print(basket)
# basket.clear()
# print(basket)

# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?

## float is a number with a decimal point and an integer is a whole number w/o a decimal point

# Can you think of another way to generate a sequence of floats?

# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# import math
# float_list = []
# start = 1
# for num in range(8):
#     start += .5
#     if math.ceil(start) == start:
#         start = int(start)
#     float_list.append(start)
# print(float_list)

# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
# for itm in range(21):
#     print(itm)
# for itm in range(21):
#     if itm%2 == 0:
#         print(itm)


# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
# name = input("please enter MY name: ")
# while name != "Yisroel":
#     name = input("wrong answer, you need to enter MY name, try again: ")


# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# fav_fruit = input("Please enter a list of your favorite fruits seperated by a space: ")
# fav_fruit = fav_fruit.split()
# check_fruit = input("please enter a fruit youd like to check for: ")

# if check_fruit in fav_fruit:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

# toppings = []
# while True:
#     new_topping = input("Enter a topping youd like to add to your pizza(press quit to exit): ")
#     if new_topping == "quit":
#         break
#     print(f"Sure I\'m adding {new_topping} to your pizza")
#     toppings.append(new_topping)
# print("Heres a list of all your toppings")
# for itm in toppings:
#     print(itm)
# print(f'Your total price is {10 + (len(toppings) * .25)}')

# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# total = 0
# while True:
#     age = input("Please enter the age of the person for whom the ticket is for (enter done when you're finished): ")
#     if age == 'done':
#         break
#     age = int(age)
#     if age < 3:
#         continue
#     if 3 <= age < 12:
#         total += 10
#     if age >= 12:
#         total += 15
# print(f"Your total is ${total}")

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

# guest_list = ["Jack", "Henry", "Richard", "Daniel"]
# approved_list = []
# for name in guest_list:
#     age = input(f"How old are you {name}? ")
#     age = int(age)
#     if 16 <= age <= 21:
#         print(f"Ok {name} you're old enough to watch")
#         approved_list.append(name)
#     else:
#         print(f"Sorry {name} this movie isnt for you")
# print(approved_list)


# Exercise 10 : Sandwich Orders
# Instructions
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# finished_sandwiches = []
# while len(sandwich_orders) > 0:
#     print("Heres the rest of the sandwiches that need to be made")
#     print(sandwich_orders)
#     order = input("Which sandwich are you going to make next? ")
#     sandwich_orders.remove(order)
#     finished_sandwiches.append(order)
#     print(f"Ok your {order} is done")
# print("All the sandwiches are finished")

# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"]
print("We're sorry but the deli has run out of pastrami so there will be no pastrami sandwiches today")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)
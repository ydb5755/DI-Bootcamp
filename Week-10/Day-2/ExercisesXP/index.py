
# 🌟 Exercise 1: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:

# import module_name 

# OR 

# from module_name import function_name 

# OR 

# from module_name import function_name as fn 

# OR

# import module_name as mn


# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.
# import random
# import math
# def matchRandom(user_input:int) -> int:
#     computer_input = random.random()*100
#     computer_input = math.floor(computer_input)
#     while True:
#         if 0 < user_input < 101:
#             break
#         else:
#             user_input = input('Please enter a number between 1 and 100')
#     if user_input == computer_input:
#         return print(user_input, computer_input, "It's a match!")
        
#     else:
#         return print(user_input, computer_input, "No match")
# matchRandom(50)

# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module
# import string
# import math
# import random
# every_letter = [*string.ascii_letters]
# def indexGenerator():
#     return math.floor(random.random()*52)
# end_string = ''
# for i in range(5):
#     end_string += every_letter[indexGenerator()]
# print(end_string)

# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

# import datetime
# def currentDate():
#     return datetime.datetime.now()
# print(currentDate())

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

# import datetime
# def untilJan1():
#     return datetime.datetime(2024,1,1) - datetime.datetime.now()
# print(untilJan1())


# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

# import datetime
# def lifeLived(birthday):
#     birthdayDate = datetime.datetime.strptime(birthday, '%d-%m-%Y')
#     days = datetime.datetime.now() - birthdayDate
#     return days.total_seconds()
# print(lifeLived('4-3-1995'))

# Exercise 7 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

# import datetime
# def timeToHoliday():
#     now = datetime.datetime.now()
#     passover = datetime.datetime(2023, 4, 5)
#     delta = passover - now
#     return f"Todays date is {now.date()} and Passover is in {delta} "

# print(timeToHoliday())


# Exercise 8 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

# import datetime
# def years(seconds):
#     yearsEarth = seconds/31557600
#     yearsMercury = yearsEarth/0.2408467
#     return print(yearsEarth, yearsMercury)

# years(1000000000)



# Exercise 9 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

import faker
users = []
faked = faker.Faker()

print(faked.name())
def addUser():
    users.append({
        'name':faked.name(),
        'address':faked.address(),
        'language_code': faked.language_code()

    })
addUser()
addUser()
addUser()
addUser()
addUser()
addUser()


print(users)
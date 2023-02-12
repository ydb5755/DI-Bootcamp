
# 🌟 Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# x= zip(keys, values)
# print(dict(x))

# 🌟 Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 1, 'summer': 8}
# individual_cost = {}
# total = 0
# for person in family:
#     if family[person] <= 3:
#         individual_cost[person] = 0
#         continue
#     elif 3 < family[person] <= 12:
#         individual_cost[person] = 10
#         total += 10
#     elif family[person] > 12:
#         individual_cost[person] = 15
#         total += 15
# print(total)
# print(individual_cost)

# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).


# 🌟 Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# brand = {
#     'name': 'Zara',
#     'creation_date': 1975,
#     'creator_name': 'Amancio Ortega Gaona', 
#     'type_of_clothes': 'men, women, children, home',
#     'international_competitors': [
#         'Gap', 
#         'H&M', 
#         'Benetton'
#         ],
#     'number_stores': 7000,
#     'major_color':{ 
#         'France': 'blue', 
#         'Spain': 'red', 
#         'US': 'pink, green'
#         }
# }
# 3. Change the number of stores to 2.
# brand['number_stores'] = 2
# 4. Print a sentence that explains who Zaras clients are.
# print('Zaras clients are familys')
# 5. Add a key called country_creation with a value of Spain.
# brand['country_creation'] = 'Spain'
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# if 'international_competitors' in brand:
#     brand['international_competitors'].append('Desigual')
# 7. Delete the information about the date of creation.
# del brand['creation_date']
# 8. Print the last international competitor.
# print(brand['international_competitors'][-1])
# 9. Print the major clothes colors in the US.
# print(brand['major_color']['US'])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# print(len(brand.keys()))
# 11. Print the keys of the dictionary.
# print(brand.keys())
# 12. Create another dictionary called more_on_zara with the following details:

# creation_date: 1975 
# number_stores: 10 000
# more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000
# }


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

# brand.update(more_on_zara)

# 14. Print the value of the key number_stores. What just happened ?

# print(brand['number_stores'])
# the value of number_stores was overwritten by the value contained within the number_stores key in more_on_zara


# Exercise 4 : Disney Characters
# Instructions
# Use this list :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
users_dict = {}
i = 0
# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# for char in users:
#     users_dict[char] = i
#     i += 1
# print(users_dict)
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# for char in users:
#     users_dict[i] = char
#     i += 1
# print(users_dict)
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# users.sort()
# for char in users:
#     users_dict[char] = i
#     i += 1
# print(users_dict)

# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.

# new_list = []
# for char in users:
#     if 'i' in char:
#         new_list.append(char)
# for char in new_list:
#     users_dict[char] = i
#     i += 1
# print(users_dict)
# The characters, which names start with the letter “m” or “p”.
new_list = []
for char in users:
    if char[0] == 'M' or char[0] == 'P':
        new_list.append(char)
for char in new_list:
    users_dict[char] = i
    i += 1
print(users_dict)
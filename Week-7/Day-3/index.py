


# def highest_even(li):
#     highest = 0
#     for num in li:
#         if num%2 == 0:
#             if num > highest:
#                 highest = num
#     return highest
# print(highest_even([2,3,4,8,11]))

# my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

# def sum (list):
#     total = 0
#     for num in list:
#         try:
#             total += num
#         except:
#             pass
#     return total

# print(sum(my_list))
# valid_flag = False
# while not valid_flag:
#     userage = input("How old are you?")
#     try:    # TRY THIS
#         userage    = int(userage)
#     except: # IF YOU GOT AN ERROR
#         print("Wrong age!")
#     else:   # ELSE
#         valid_flag = True
# print("Next year, your age will be",userage+1)

# valid_flag = False
# while not valid_flag:
#     userage = input("How old are you?")
#     try:    # TRY THIS
#         userage    = int(userage)
#     except: # IF YOU GOT AN ERROR
#         print("Wrong age!")
#     else:   # ELSE
#         valid_flag = True
#     finally:
#         print('There may or may not have been an exception.')

# print("Next year, your age will be",userage+1)

# z = 9
# try:
#     assert 1 == z
# except AssertionError:
#     print("Error: Those are not equals")


people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters
filtered = list(filter(lambda name: len(name) <= 4, people))
mapped = list(map(lambda name: print(f"Hello {name}"), filtered))
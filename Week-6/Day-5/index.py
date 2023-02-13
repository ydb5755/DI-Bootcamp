# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sample_dict['class']['student']['marks']['history'])

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# del sample_dict['name']
# del sample_dict['salary']
# print(sample_dict)
# keys_to_remove = ["name", "salary"]

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

# print(duplicates)

# Scroll down to see the answers!
# 1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
# user = {
#     "age":25,
#     'username':'Jacko',
#     'weapons':['knife', 'spoon'],
#     'is_active': True,
#     'clan': "jhsjsjsj"
# }
# 2 iterate and print all the keys in the above user.
# print(user.keys())
# 3 Add a new weapon to your user
# user['weapons'].append('fork')
# 4 Add a new key to include 'is_banned'. Set it to false
# user['is_banned'] = False
# 5 Ban the user by setting the previous key to True
# user['is_banned'] = True
# 6 create a new user2 my copying the previous user and update the age value and username value. 
# user2 = user.copy()
# user2['age'] = 30
# user2['username'] = 'kkkkkaaaaaa'
# print(user2)

import re
pattern = re.compile(r"[A-Za-z0-9@#$%]{8}")
# Download this text file http://www.practicepython.org/assets/nameslist.txt and do the following steps

# Read the file line by line
# Read only the 5th line of the file
# Read only the 5th first characters of the file
# Read all the file and return it as a list of strings. Then split each word
# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# Append your first name at the end of the file
# Append "SkyWalker" next to each first name "Luke"


# with open('nameslist.txt') as f:
#     replacement_list = []
#     for line in f.readlines():
#         line = line.strip()
#         if line == 'Luke':
#             line = 'Luke Skywalker'
#         replacement_list.append(f'{line}\n')

# with open('nameslist.txt', 'w') as f:
#     f.writelines(replacement_list)

# Retrieve the data into the python file, inside a variable called family
# Print nicely the details about Jane's children
# Inside the family variable, add to each children, a key 'favorite_color' with a value
# Then, save back all the new data into the json file
# Use the indent argument inside the dump function. Check out the documentation and the video in the Useful Resources
# Run the python file
import json
# json_file = 'file.json'
# with open(json_file) as json_obj:
#     family = json.load(json_obj)
# for child in family['children']:
#     child['fav_color'] = 'red'
# with open(json_file, 'w') as json_obj:
#     json.dump(family, json_obj, indent=2)
# print(family)
import requests

# response = requests.get('https://api.chucknorris.io/jokes/random')
# print(response.json())
from translate import Translator
translator = Translator(to_lang='he')
print(translator.translate('Hi my name is Yisroel'))
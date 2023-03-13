
# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# from random import randint
# def get_words_from_file():
#     with open('word_list.txt')as f:
#         list_of_words = []
#         for line in f:
#             line = line.strip()
#             list_of_words.append(line)
#     return list_of_words

# def get_random_sentence(length):
#     sentence = ''
#     for i in range(length):
#         sentence += get_words_from_file()[randint(0, len(get_words_from_file()))] + ' '
#     return sentence.lower()

# print(get_random_sentence(5))


# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# def main():
#     print('This function will make a sentence of a length that you will decide, but it will make zero sense and will not be grammatically correct')
#     num = input('How long would you like the sentence to be? Please enter an integer between 2 and 20  ')
#     try:
#         num = int(num)
#     except ValueError:
#         return print('Thats not a valid entry, i clearly said, "an integer between 2 and 20". Goodbye')
#     if 1 < num < 21:
#         return print(get_random_sentence(num))
#     else:
#         return print('Thats not a valid entry, i clearly said, "an integer between 2 and 20". Goodbye')

# main()

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.


# 🌟 Exercise 2: Working With JSON
# Instructions
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


# Access the nested “salary” key from the JSON-string above.
new_jason = json.loads(sampleJson)
print(new_jason['company']['employee']['payable']['salary'])
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
new_jason['company']['employee']['birth_date'] = '13/05/2021'
print(new_jason)
# Save the dictionary as JSON to a file.
with open('file.json', 'w') as f:
    json.dump(new_jason, f, indent=2)
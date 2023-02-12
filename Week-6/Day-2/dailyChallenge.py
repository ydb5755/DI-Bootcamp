# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# Then, print the first and last characters of the given text.

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World


# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod
import random
the_string = input("please input a string 10 characters long ")
the_string_length = len(the_string)
while the_string_length != 10:
    if the_string_length < 10:
        print("string not long enough")
    else:
        print("string too long")
    the_string = input("please input a string 10 characters long ")
    the_string_length = len(the_string)
print(the_string[0])
print(the_string[-1])
construct_string = ""
for x in the_string:
    construct_string += x
    print(construct_string)
sr = ''.join(random.sample(the_string, the_string_length))
print(sr)

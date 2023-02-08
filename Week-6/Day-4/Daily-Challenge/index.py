# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

# number = int(input("Please input a number: "))
# length = int(input("Please input a length: "))
# counter = 0
# output = []
# while counter < length:
#     output.append(number * (counter + 1))
#     counter += 1
# print(output)



# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).
# word = input("please enter your weird mutated word that you need me to fix because you cant do it yourself: ")
# word = list(word)
word = ['t','t','t','w','w','i','s','t']
output = []
previous_value = None
for elem in word:
   if elem != previous_value:
       output.append(elem)
       previous_value = elem
output = ''.join(output)
print(output)
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}
# x = input("Please enter a word: ")
# indx = {}
# i = 0
# for char in x:
#     if char in indx:
#         indx[char].append(i)
#         i += 1
#     else:
#         indx[char] = [x.index(char)]
#         i += 1
# print(indx)

# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Examples

# The key is the product, the value is the price

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

# ➞ ["Bread", "Fertilizer", "Water"]

items_purchase = {}
while True:
    grocery = input("What would you like to buy from the store? (type done to finish)")
    if grocery == 'done':
        break
    price = int(input("And how much does it cost?"))
    items_purchase[grocery] = price
cash = int(input("Ok, and how much money do you have in your wallet?"))
print("Ok heres what you can buy")
potential = []
for item in items_purchase:
    if cash > items_purchase[item]:
        potential.append(item)
    else:
        print('nope')
print(potential)
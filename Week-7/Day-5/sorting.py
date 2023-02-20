# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,worl



def sorting(str):
    lowercase_str = str.lower()
    split_list = lowercase_str.split(',')
    sorted_list = sorted(split_list)
    return ','.join(sorted_list)


print(sorting('without,hello,bag,world'))
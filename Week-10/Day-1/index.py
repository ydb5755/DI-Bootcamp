import itertools

my_list = [0, 0, 1, 2, 0]

result = itertools.dropwhile(lambda x: x == 0, my_list)

for elements in result:
  print (elements)
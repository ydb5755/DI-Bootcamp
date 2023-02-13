    
import re
matrix = [
    ['7','i','3'],
    ['T','s','i'],
    ['h','%','x'],
    ['i','','#'],
    ['s','M',''],
    ['$','a',''],
    ['#','t','%'],
    ['^','r','!']
]


arr = []
for item in range(0, len(matrix[0])):
    for unit in range(0,len(matrix)):
        arr.append(matrix[unit][item])



# final = []
# for unit in arr:
#     if unit.isalpha():
#         final.append(unit)
#     else:
#         final.append(' ')
# final = ''.join(final)
# print(final)


#Below is part of another solution to this problem using regex, this results in ThisisMatrix with no spaces
newlist = [re.sub('[^a-zA-Z]+', '', x) for x in arr]
final = ' '.join(newlist)
print(final)


#Longer way of making the same result as lines 15-18
# arr = []
# for index1, unit in enumerate(matrix):
#     arr.append(matrix[index1][0])
# for index1, unit in enumerate(matrix):
#     arr.append(matrix[index1][1])
# for index1, unit in enumerate(matrix):
#     arr.append(matrix[index1][2])
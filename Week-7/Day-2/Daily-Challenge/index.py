    
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
for index1, unit in enumerate(matrix):
    arr.append(matrix[index1][0])
for index1, unit in enumerate(matrix):
    arr.append(matrix[index1][1])
for index1, unit in enumerate(matrix):
    arr.append(matrix[index1][2])
# newlist = [re.sub(r'[^a-zA-Z]+', '', x) for x in arr]
# for item in newlist:
#     if item == '':
#         newlist.remove(item)
# final = ''.join(newlist)
final = []
for unit in arr:
    if unit.isalpha():
        final.append(unit)
    else:
        final.append(' ')
final = ''.join(final)
print(final)
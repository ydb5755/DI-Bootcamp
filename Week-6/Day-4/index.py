#Scroll to bottom to see solution
# You are working for the school Principal. We have a database of school students:
# school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list. 
# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

#using what you learned about sets, create a piece of code that the school principal 
# can use to immediately find out who missed class so they can call the parents. 
# (Imagine if the list had 1000s of students. The principal can use the lists generated 
# by the teachers + the school database to use python and make his/her job easier): 
# Find the students that miss class!
# missing = school.difference(attendance_list)
# print(missing)

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
    counter = counter + item
print(counter)
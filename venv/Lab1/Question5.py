'''
5. A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks that can be purchased.
 The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
  In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
   The second group has 21 students, so they can get by with no fewer than 11 desks.
 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
'''
class1 = int(input("Enter total number of student in the first class  :"))
class2 = int(input("Enter total number of student in the second class  :"))
class3 = int(input("Enter total number of student in the third class  :"))
students= class1//2
desk= class1%2
total= students+desk

students2= class2//2
desk2= class2%2
total2= students2+desk2

students3 = class3//2
desk3 = class3%2
total3 = students3+desk3

totaldesk = total+total2+total3
print()
print(f"The total number of required desks in the first class is : {total} ")
print(f"The total number of required desks in the second class is : {total2}")
print(f"The total number of required desks in the third class is : {total3}")

print(f" We need {totaldesk} desks in total")




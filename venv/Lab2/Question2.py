'''
2. WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
'''
sub1=int(input("Enter the marks of the first subject :"))
sub2=int(input("Enter the marks of the second subject :"))
sub3=int(input("Enter the marks of the third subject :"))
sub4=int(input("Enter the marks of the fourth subject :"))
Total=(sub1+sub2+sub3+sub4)/400*100
if (Total>=70):
    print("Grade = Distinction")
elif(Total>=60 and Total<70) :
    print("Grade = First")
elif(Total>=40 and Total<60):
    print("Grade = Pass")
else:
    print("Grade = Fail")



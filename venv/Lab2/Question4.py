'''
4. Enter three integers, print the smallest one.
'''
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
num3=int(input("Enter the third number :"))
smallest=0
if num1<num2 and num1<num3 :
    smallest = num1
elif num2<num3:
    smallest = num2
else :
    smallest = num3
print(smallest," is the smallest one")
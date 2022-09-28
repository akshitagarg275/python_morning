'''
conditional statements -> It allows to make certain decisions
only if
if else pair
if elif else
'''

# TODO: only if 
'''
if condition : 
    //if statements
'''

# age = int(input("enter your age: "))

# if age >= 18 :
#     print("You can drive")

# print("other lines of code")


# TODO: if else pair

'''
if condition:
    # if statements
else:
    # else statements
'''

# age = int(input("enter your age: "))

# if age >= 18:
#     print("You can drive")
# else:
#     print("You cannot drive")

# TODO : WAP to find given num is even or odd

# num = int(input("enter the number: "))

# if num % 2 == 0:
#     print("It is even")
# else:
#     print("It is odd")

# TODO: if elif
'''
if condition:
    # if statements
elif condtion:
    # elif statements
elif condition:
    # elif statements
elif condition:
    # elif statements
.
.
.
.

else:
    # else statements
'''

# TODO: WAP to find whether a given num is +ve, -ve or 0
# num = int(input("enter a num: "))

# if num > 0 :
#     print("+ve")
# elif num < 0 :
#     print("-ve")
# else:
#     print("0")


# TODO : Grading system
# marks = float(input("Enter the marks: "))

# if marks > 90 and marks <= 100:
#     print("A+")
# elif marks > 80 and marks <= 90:
#     print("A")
# elif marks > 70 and marks <= 80:
#     print("B+")
# elif marks > 60 and marks <=70:
#     print("B")
# elif marks > 50 and marks <= 60:
#     print("C")
# elif marks > 40 and marks <= 50:
#     print("D")
# elif marks <=40 and marks >=0:
    # print("F")

# TODO: WAP to create a rating system
# 1 - 5


# if marks > 90:
#     print("A+")
# if marks > 80:
#     print("A")
# if marks > 70:
#     print("B+")
# if marks > 60 :
#     print("B")
# if marks > 50 :
#     print("C")


# TODO: Nested if else
'''
if condition:
    if condition:
        # if statement
    else:
        # else statement
else:
    if condition:
        # if statement
    else:
        # else statement
'''

n1 = 4
n2 = 19
n3 = 10


if n1 >= n2:
    if n1 >= n3:
        print(n1, " is greatest")
    else:
        print(n3, " is greatest")

else:
    if n2 >= n3:
        print(n2, " is greatest")
    else:
        print(n3, " is greatest")

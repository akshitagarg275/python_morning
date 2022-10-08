'''
DRY -> Donot Repeat Yourself
functions -> A function is a set of code which executes only when we call that function

def function_name():
    #function_statements

'''
# function defination
def greeting():
    print("Hello")

# function callling
# greeting()
# greeting()

#TODO: parameterised fucntions

def calc(n1 , n2):
    print(f"sum of {n1} and {n2} is {n1+n2}")

# calc(2, 5)

def profile(name , age):
    print(f"Name is {name} and age is {age}")

# profile("John", 23)
# profile("Rahul", 13)
# profile(14, "Jane")
# n="Jane"
# a = 13
# profile(n , a)

# TODO: Keyword arguments
def profile(name , age):
    print(f"Name is {name} and age is {age}")

# profile(age=14, name="Jane")
# n = input("enter name: ")
# a = int(input("enter age: "))

# profile(age = a , name = n)

# TODO: Default parameters
# NOTE: default parameters will follow non-default parameters
# def profile(name   , age = "Na"):
#     print(f"Name is {name} and age is {age}")

def profile(name = "NA", age = "Na"):
    print(f"Name is {name} and age is {age}")

# profile()

# TODO: return statement

def calc(n1 , n2):
    sum = n1 + n2
    return sum

# ans = calc(2 , 3)
# print(ans)

# print(calc(4,5))

def func(n1 , n2):
    sum = n1 + n2
    sub = n1 - n2
    return sum , sub

# print(func(5 , 3))
ans1 , ans2 = func(5,3)
print(ans1)
print(ans2)
# TODO: variable length arguments

# TODO: variable length keyword arguments

# TODO: Anonymous functions

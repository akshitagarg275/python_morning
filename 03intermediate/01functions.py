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
# ans1 , ans2 = func(5,3)
# print(ans1)
# print(ans2)

# def is_even(num):
#     return num%2 ==0 

# if is_even(4):
#     print("It is even")

# TODO: variable length arguments

# def func(*args):
    # print(args)
    # print(type(args))
    # for i in args:
    #     print(i)

# func(1,2,3,4,5,6)
# func(1,2,3)

def func(n1, n2 , *args ,**kwargs):
    print("n1 is :", n1)
    print("n2 is :", n2)
    print("args is :", args)
    print("kwargs is :", kwargs)

# func(1,2,3,4,5,fname="john")
# TODO: variable length keyword arguments
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

# func(fname = "John" , lname= "Doe")

# TODO: Anonymous functions

# def sqr(num):
#     return num **2

# sqr = lambda num : num**2
# print(sqr(7))

# is_even = lambda num : num%2==0

# print(is_even(4))
# print(is_even(47))

# func = lambda num : num**2 if num%2==0 else num**3

# print(func(3))
# print(func(2))


# TODO: map

nums = [2,3,4,5,6]

# sqr_list = list(map(lambda num : num**2 , nums ))
# print(sqr_list)

#TODO: filter
# even = list(filter(lambda num : num%2==0 , nums))
# print(even)

# TODO: reduce

from functools import reduce
print(reduce(lambda a,b : a+b , nums))

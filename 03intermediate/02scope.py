'''
Scope: where that variable is accessible

global -> which can accessed throughout the program
local -> accessible to a certain scope
nonlocal 
'''
# global
a = 20
b = 10

def func():
    # local variable of func
    # a = 50

    # accessing global variable
    global a
    a = 90
    # print(globals()['b'])
    print("Line 12 func: ",a)

# func()
# print("Line 14 outer: ",a)
# func()


def outer():
    age = 20 
    
    def inner():
        nonlocal age
        age = 50
        print("inner: ",age)
    inner()
    print("Outer : ", age)

outer()
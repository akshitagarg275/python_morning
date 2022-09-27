'''
input ()
By default datatype of value enetered using input function
is string
For anyother datatype we need to typecast it.
'''

name = input("Enter your name: ")
print("Your name is: ",name)
print(type(name))

age = int(input("Enter your age: "))
print("Your age is :",age)
print(type(age))



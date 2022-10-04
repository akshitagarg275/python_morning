'''
dictionary - {}
mutable , ordered , iterable
{key : value}
key can only be immutable(int, string, tuple, frozen_set) datattype 
'''

user = {
    "fname" : "John",
    "lname" : "Doe",
    "age" : 12,
    "courses" : ["python" , "HTML"],
    "isPaid" : True
}

# print(user)
# print(type(user))

# print(user['fname'])

# user["age"] = 18

# user["country"] = "India"
# print(user)

# TODO: will give KeyError
# print(user['gen'])

# print(user.get('gen'))
# print(user.get('gen', '-1'))


# print(user.keys())
# print(type(user.keys()))

# print(user.values())
# print(type(user.values()))

# print(user.items())
# print(type(user.items()))

# for k,v in user.items():
#     print("key is : ",k)
#     print("value is: ",v)

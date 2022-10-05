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


user = {
    "fname" : "John",
    "lname" : "Doe",
    "age" : 12,
    "courses" : ["python" , "HTML"],
    "isPaid" : True
}

# print(user)
# print(user.pop("age"))
# print(user.popitem())
# print(user)

# user.setdefault("age" , 15)
# user.setdefault("gender" , "male")
# print(user)

# TODO: WAP to find freq of each char
# HAHA -  {'H' : 2 , 'A' : 2}

# input_str = "HAhA"
# freq = {}
# for s in input_str:
#     if freq.get(s) == None :
#         freq[s] = 1
#     else:
#         freq[s] = freq[s] + 1
# print(freq)

# para ="we are learning python"
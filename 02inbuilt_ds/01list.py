'''
list() or []
mutable -> changable
orderd -> each element have a spaecific position
iterbale -> for in loop could be executed
'''

# fruits = ["apple", "banana", "mango", "pear", "grapes"]
# print(fruits)
# print(type(fruits))

# print("Length of elements is: ", len(fruits))

# print(fruits[0])
# fruits[0] = "pineapple"
# print(fruits)
# fruits = ["apple", "banana", "mango", "pear", "grapes"]

# for fruit in fruits:
#     print(fruit)

# for i in range(len(fruits)):
    # print(i)
    # print(fruits[i])

# TODO: slicing -> to fetch a apart of the list
# list_name[start_idx : end_idx : step]
# start_idx is included
# end_indx is not included

# print(fruits[1 : 3])

# print(fruits[ : :])
# print(fruits[ : : 2])
# print(fruits[ : : -2])
# print(fruits[: : -1])
# print(fruits[: 4])
# print(fruits[1: ])

# print(fruits[-4 : -1])

# fruits.append("guava")
# print(fruits)

# fruits.extend(["cherry" , "pineapple"])
# print(fruits)


# WAP to write custom list
# size = int(input("enter the size of the list"))
# myList = []

# for i in range(size):
#     val = int(input("enter a num: "))

#     myList.append(val)
# else:
#     print(myList)


fruits = ["apple", "banana", "mango", "pear", "grapes"]

# print(fruits.pop())

# print(fruits.pop(0))

# print(fruits.count("apple"))

# print(fruits.index("mango"))

# fruits.remove("banana")
# print(fruits)

# fruits.insert(1 , "cherry")
# print(fruits)

# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)

# print(sorted(fruits))

# print(fruits)
# fruits.reverse()
# print(fruits)

# fruits.clear()
# print(fruits)


nums = [1, 2, 3, 4, 2, 2, 2]
# [1, 3, 4]

while 2 in nums:
    nums.remove(2)
else:
    print(nums)
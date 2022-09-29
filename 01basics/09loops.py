'''
Loops -> It allows to perform certaiin task for certain no of times
while 
for in

while loop
initialization
condition
re-initialization (updation)
'''

# TODO: printing hello 5 times
# i = 1

# while i <= 5 :
#     print("Hello, ", i)
#     i = i + 1


# TODO : printing even nums 0-10

# i = 0

# while i <= 10:
#     print(i)
#     i = i + 2


# i = 0 
# while i <= 10:
#     if i%2 == 0:
#         print(i)
#     i = i +1

# TODO: reverse counting 5-1

# i = 5

# while i >= 1:
#     print(i)
#     i = i - 1

# TODO: Infinite loop
# while True:
#     print("1")

# TODO: for in loop
'''
for loop works directly on the iterables (list,tuple,string,set,dictionary,range)
for loop internally is aware, from where to start and when to end
'''

# fruits = ["mango", "banana", "apple", "guava", "pineapple"]

# for i in fruits:
#     print(i)

# full_name = "John Doe"

# for n in full_name:
#     print(n, end = "")

# for idx in range(5):
#     print(idx)

'''
loops also contain else block
in case of loops else block will execute 
only if your loop executes completely 
and there is no explicit termination
'''

# for i in range(1 , 6):
#     if i == 3:
#         # break
#         # continue
#         pass
#     print(i)
# else:
#     print("Else part executed")

# TODO: WAP to count no of digits entered by a user
# 345 -> 3
# 12345 -> 5

num = int(input("enter a number: "))
count = 0

while num > 0:
    rem = num % 10
    count = count + 1
    num = num // 10
else:
    print("No of digits is: ",count)

# TODO: WAP to add digits in a give num
# 345 -> 3 + 4 + 5 = 12





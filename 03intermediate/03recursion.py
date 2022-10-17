'''
Recursion -> function calling itself

base case
smaller problem solution
'''

# 1+2+3+4+5
# add(5) = add(4) + 5
# add(4) = add(3) + 4
# add(2) = add(1) + 2
# add(1) = 1

# def add(num):
#     # base case
#     if num == 1:
#         return num
#     return add(num-1) + num

# print(add(5))

# TODO: factorial of a num
# fact(5) = 5*4*3*2*1 =120

# TODO: pow of a num
# pow(num , p)
# pow(2,3 ) =8

# TODO: Fiboannaci series
# 0 1 1 2 3 5 8 13

# def fib(n):
#     if n == 1 or n == 0:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(5))
# print(fib(0))

# for i in range(5):
#     print(fib(i) , end=" ")

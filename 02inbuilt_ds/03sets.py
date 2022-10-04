'''
set -> {}
set()
unordered
iterable
duplicate values not there
mutable
'''

# s = {}
# s = set()
# print(type(s))

# s = {1,2,4,3,2,1,7,6,7,6}
# print(s)

s ={1,2,3,4}
# s.add(23)
# print(s)

# s.update([22,33])
# print(s)

# s.discard(12)
# print(s)

# s.remove(12)
# print(s)

# s.pop()
# print(s)

a = {1,2,3,4,5}
b ={4,5,6,7}

# print(a.union(b))
# print(a | b)

# print(a.intersection(b))
# print(a&b)

print(a.difference(b))
print(a - b)
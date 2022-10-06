'''
strings : '' ," " , ''' '''
str()

iterable
ordered
immutable
'''

s = 'python'

# for i in s:
#     print(i, end=" ")
# print(s[0])

# i = 0

# while i < len(s):
#     print(s[i])
#     i = i + 1

# TODO: will give TypeError
# s[0] = "C"


# TODO: slicing
# print(s[ : : ])
# print(s[ : : -1])
# print(s[: : 2])
# print(s[1: 4])
# print(s[-4 : -1])

s = 'python is funny'

# print(s.upper())
# print(s.lower())

# print(s.startswith('py'))
# print(s.endswith('py'))

# print(s.capitalize())
# print(s.title())

# print(s.count('o'))

# TODO: WAP to find no of vowels 

# print(s.find('t'))
# print(s.find('y'))
# print(s.find('you'))

# print(s.index("you"))

# s = 'python12'
# print(s.isalpha())
# print(s.isalnum())

# contact = '12142s'
# print(contact.isdigit())

# password = "       "
# print(password.isspace())

# print(s.isidentifier())
# print('for'.isidentifier())


'''
\b -> backspace
\t -> tab
\\ -> \
\' ->'
\-> new line
'''
# path =r"C:\navin\tmp"
# print(path)

# TODO: format strings

n1 = 2
n2 = 3
ans = 5
#  2 + 3 = 5
# print(str(n1) + " + " + str(n2) + " = " + str(ans))
# print("{1} + {0} = {2}".format(n1,n2,ans))

# f-strings
# print(f"{n1} + {n2} = {ans}")


# TODO: split(delimiter)

s = "we are learning pthon"
# print(s.split())
# print(s.split('e'))
# email = 'john.doe@abc.com'
# print(email.split('@')[0])
# print(email.split('@')[1])

# nums = input("enter the nums").split()
# print(nums)

# TODO: replace(old_string, new_string, count)
# s = "we are learning pthon"

# print(s.replace('a' , '@' , 1))


# TODO: join

# fname = "john"
# lname = "doe"

# uname = '.'.join([fname, lname])
# print(uname)

# company = "abc.com"

# email = '@'.join([uname, company])
# print(email)
# TODO: strip()

# password = "      abc123     "
# print(password.lstrip())
# print(password.rstrip())
# print(password.strip())


# TODO : WAP to remove all the spaces from the given string
s = "we are learning python"
# print(s.replace(" ", ""))
# for i in range(len(s)):
#     if s[i] == " ":
#         s.replace(s[i] , "" )


# TODO: WAP to reverse a string
# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)

# print(s[: : -1])


# TODO: reverse each word
# s = "we are learning python"
# "ew rea gninrael nohtyp"
# s_list = s.split()
# for i in range(len(s_list)):
#     s_list[i] = s_list[i][: : -1]
# rev_words = " ".join(s_list)
# print(rev_words)
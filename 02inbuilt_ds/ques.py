'''
# 1:A:0, 2:B:1, 3:C:1, 4:D:2, 5:E:2, 6:F:3 - input string
# Output:
# A - B,C
# B - D,E
# C - F
# D -
# E -
# F -
'''

from operator import itruediv


def create_dict(input_str):
    output_dict ={}
    # print(input_str.split(", "))
    for item in input_str.split(", "):
        # print(item.split(":"))
        emp_dict = {}
        emp_dict["emp_name"] = item.split(":")[1]
        emp_dict["manager_id"] = item.split(":")[2] 
        output_dict[item.split(":")[0]] = emp_dict

    print(output_dict)

    return output_dict

input_dict = create_dict("1:A:0, 2:B:1, 3:C:1, 4:D:2, 5:E:2, 6:F:3")

test_dict = {'a' : [5, 6, 7, 8],
             'b' : [10, 11, 7, 5],
             'c' : [6, 12, 10, 8],
             'd' : [1, 2, 5]}
output = set()
for val in test_dict.values():
    # print(val)
    for i in val:
        output.add(i)

# print(list(output))



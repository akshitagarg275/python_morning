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

# {'A' : 'B,C' , 'B' : 'D , E' , 'C' : 'F'}

'''
{
    '1': {'emp_name': 'A', 'manager_id': '0'}, 
    '2': {'emp_name': 'B', 'manager_id': '1'}, 
    '3': {'emp_name': 'C', 'manager_id': '1'}, 
    '4': {'emp_name': 'D', 'manager_id': '2'}, 
    '5': {'emp_name': 'E', 'manager_id': '2'}, 
    '6': {'emp_name': 'F', 'manager_id': '3'}
}
'''

def findManager(input_dict):
    emp_manager = {}
    # print(input_dict)
    for empId , empDetail in input_dict.items():
        # print(f"id: {empId} ----- emp: {empDetail}")
        # print(empDetail["manager_id"])
        if empDetail['manager_id'] == '0' :
            pass
        else:
            # employeee name
            employee_name = empDetail['emp_name']
            # manager id
            manager_id = empDetail['manager_id']
            for employee_id , employee_detail in input_dict.items():
                if employee_id == manager_id:
                    # manager name
                    manager_name = employee_detail['emp_name']
            # if we get manager name for the first time
            if emp_manager.get(manager_name) is None:
                emp_manager[manager_name] = employee_name
            else:
                # concatenating employee name if manager is same
                emp_manager[manager_name] += ', ' +employee_name
    print(emp_manager)
                    


def create_dict(input_str):
    output_dict ={}
    # print(input_str.split(", "))
    for item in input_str.split(", "):
        # print(item.split(":"))
        emp_dict = {}
        emp_dict["emp_name"] = item.split(":")[1]
        emp_dict["manager_id"] = item.split(":")[2] 
        output_dict[item.split(":")[0]] = emp_dict

    # print(output_dict)

    return output_dict

input_dict = create_dict("1:A:0, 2:B:1, 3:C:1, 4:D:2, 5:E:2, 6:F:3")

findManager(input_dict)



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



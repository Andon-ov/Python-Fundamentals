#
# company_and_employees = {}
#
# command = input()
# while not command == 'End':
#     company,employees = command.split(' -> ')
#     if company not in company_and_employees:
#         company_and_employees[company] = []
#         company_and_employees[company].append(employees)
#     elif employees not in company_and_employees[company]:
#         company_and_employees[company].append(employees)
#
#     command = input()
#
# for key,value in company_and_employees.items():
#     print(f'{key}')
#     for i in value:
#         print(f'-- {i}')

def company_users(dict, company, id):
    if company not in dict:
        dict[company] = []
    if id not in dict[company]:
        dict[company].append(id)
    return dict


company_employees = {}
command = input()
while not command == "End":

    company_names, employees_id = command.split(' -> ')
    company_users(company_employees, company_names, employees_id)

    command = input()

for key, value in company_employees.items():
    print(f"{key}")
    for i in value:
        print(f"-- {i}")

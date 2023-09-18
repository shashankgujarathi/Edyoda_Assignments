import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

def read_employee_data(file_path):
    employee_list = []
    file = open('employee.json', 'r')
    data = json.load(file)
    for entry in data:
            employee = Employee(
                entry["Name"],
                entry["DOB"],
                entry["Height"],
                entry["City"],
                entry["State"]
            )
            employee_list.append(employee)
    return employee_list

file_path = "employee.json"
employees = read_employee_data(file_path)
for employee in employees:
    print(f"Name: {employee.name}")
    print(f"DOB: {employee.dob}")
    print(f"Height: {employee.height}")
    print(f"City: {employee.city}")
    print(f"State: {employee.state}")
    print()

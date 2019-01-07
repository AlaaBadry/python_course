from empoyees2 import Employee

employees = []

with open("emps.csv") as f:
    for t in f:
        data = t.split(",")
        emp = Employee(data[0], data[1], int(data[2]), float(data[3]))
        emp.working_hours = int(data[4])
        employees += [emp]
        

for e in employees:
    print(e, e.calc_salary())
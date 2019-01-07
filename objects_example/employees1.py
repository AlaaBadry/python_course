import datetime as dt

emp1 = {
    "name": "Mohamed",
    "job": "Accountant",
    "hour_rate": 100,
    "working_hours": 45,
    "hiring_year": 2005
}

emp2 = {
    "name": "Ahmed",
    "job": "Developer",
    "hour_rate": 150,
    "working_hours": 40,
    "hiring_year": 2010
}

def calc_salary(emp):
    return emp["working_hours"] * emp["hour_rate"]

def working_years(emp):
    now = dt.datetime.now()
    return now.year - emp["hiring_year"]

if __name__ == "__main__":
    print("emp ", emp1["name"], ", salary =", calc_salary(emp1))
    print("emp ", emp2["name"], ", salary =", calc_salary(emp2))
    print("emp ", emp1["name"], ", working years =", working_years(emp1))
    print("emp ", emp2["name"], ", working years =", working_years(emp2))

import datetime as dt

class Employee:
    def __init__(self, name, job, hiring_year, hour_rate=100):
        self.name = name
        self.job = job
        self.hiring_year = hiring_year
        self.hour_rate = hour_rate
        self.working_hours = 0

    def calc_salary(self):
        return self.working_hours * self.hour_rate

    def working_years(self):
        now = dt.datetime.now()
        return now.year - self.hiring_year
    
    def __str__(self):
        return "(" + self.name + ", " + self.job + ")"


if __name__ == "__main__":        
    emp1 = Employee("Mohamed", "Accountant", 2005)
    emp2 = Employee("Ahmed", "Developer", 2010, 150)
    
    emp1.working_hours = 45
    emp2.working_hours = 20
    
    print("emp ", emp1, "salary =", emp1.calc_salary())
    print("emp ", emp2, "salary =", emp2.calc_salary())
    
    print("emp ", emp1, "working years =", emp1.working_years())
    print("emp ", emp2, "working years =", emp2.working_years())

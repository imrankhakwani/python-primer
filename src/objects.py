class Employee:

    num_of_employees = 0
    increment_ratio = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.io'

        Employee.num_of_employees += 1

    def get_name(self):
        return f"{self.last_name}, {self.first_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.increment_ratio)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.increment_ratio = amount


emp1 = Employee("Imran", "Saeed", 5000)
emp2 = Employee('Tanveer', 'Ahmed', 3000)

print(Employee.num_of_employees)

print(emp1.email)
print(emp2.email)

print(emp1.get_name())
print(emp2.get_name())

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

emp1.set_raise_amount(1.02)

print(Employee.increment_ratio)
print(emp1.increment_ratio)
print(emp2.increment_ratio)

# Employee.increment_ratio = 1.05
print(Employee.increment_ratio)
print(emp1.increment_ratio)
print(emp2.increment_ratio)

# 1.05
# 1.05
# 1.05

emp1.increment_ratio = 1.05
print(Employee.increment_ratio)
print(emp1.increment_ratio)
print(emp2.increment_ratio)

# 1.04
# 1.05
# 1.04

print(Employee.__dict__)
print(emp1.__dict__)
print(emp2.__dict__)

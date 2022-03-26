import sys
class InvalidAgeError(Exception):
    def __init__(self,age,message="Age must be in the range of (18,40)"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.age}->{self.message}'

age = int(input("Enter the age:"))
if not 18<age<40:
    raise InvalidAgeError(age)
print('Valid Age')

sys.exit(0)
class SalaryNotInRangeError(Exception):
    def __init__(self,salary,message="Salary is not in (5000, 15000) range"):
        self.salary=salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.salary}->{self.message}'

salary = int(input('Enter the Salary:'))
if not 5000<salary<15000:
    raise SalaryNotInRangeError(salary)



sys.exit(0)
class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

number = 10
while True:
    try:
        n = int(input("Enter the Number:"))
        if n < number:
            raise ValueTooSmallError
        elif n>10:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print('THe value is Small')
        print()
    except ValueTooLargeError:
        print('THe value is Large')
        print()
print('You Entered Right.....')

from application import salary
from application.db import people
from datetime import datetime


if __name__ == '__main__':
    now = datetime.now()
    print(now.strftime("%d-%m-%Y"))
    salary.calculate_salary()
    people.get_employees()
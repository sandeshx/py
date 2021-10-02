
def get_actual_salary(number):
    return number - number*0.3


salaries = [100000, 200000, 220000]

salaries_actual = list(map(get_actual_salary, salaries))
print(salaries_actual)
# CTI-110
# P4HW2 - Salary Calculator
# Rina Moody
# Date May 03, 2023
#

numEmployee = 0
total_overtime = 0
total_regHour_pay = 0
total_gross_pay = 0
while True:
    employee_name = (input(f'\nEnter employee\'s name or "Done" to terminate: '))  
    if employee_name == 'Done':
        break
    hours_worked = float(input(f'How many hours did {employee_name} work? '))
    pay_rate = float(input(f'What is {employee_name}\'s pay rate? '))

    print('-------------------------------------')
    print(f'{"Employee name:":<17}{employee_name}\n')

    numEmployee = numEmployee +1
    overtime = 0
    overtimePay = regHour_pay = gross_pay = 0.0
    if hours_worked > 40:
        overtime = hours_worked - 40
        overtimePay = overtime * (pay_rate*1.5)
        regHour_pay = 40 * pay_rate
        gross_pay = overtimePay + regHour_pay
       
        
    else:
        overtimePay = 0.0
        regHour_pay = hours_worked * pay_rate
        gross_pay = regHour_pay
       
    total_overtime = total_overtime + overtimePay
    total_regHour_pay = total_regHour_pay + regHour_pay
    total_gross_pay = total_gross_pay + gross_pay
      


    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<13}{"OverTime Pay":<18}{"RegHour Pay":<18}{"Gross Pay":<18}')
    print('-----------------------------------------------------------------------------------------')
    print(f'{hours_worked:<15.1f}{pay_rate:<12}{overtime:<13.1f}{overtimePay:<18.2f}${regHour_pay:<18.2f}${gross_pay:<18.2f}')
  
print("\nTotal number of employees entered: ",numEmployee)
print("Total amount paid for overtime: ", total_overtime)
print("Total amount paid for regular hours: ", total_regHour_pay)
print("Total amount paid in gross: ", total_gross_pay)

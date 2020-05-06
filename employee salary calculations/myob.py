# _*_ coding: utf-8 _*_

"""importing needed modules"""
import sys
import csv
import os

"""defining schemas, Tables, input and output dictionaries"""
TBL_INPUT = 'input.csv'
TBL_OUTPUT = 'output.csv'
EMPLOYEES_SCHEMA_INPUT = ['first_name', 'last_name', 'annual_salary', 'super_rate', 'payment_start_date']
EMPLOYEES_SCHEMA_OUTPUT = ['name', 'payment_start_date', 'gross_income', 'income_t', 'net_income', 'supeer']
employees = []
employees_output = []


def _initialize_employees_from_file():
    """We are bringing from the input csv all registers to be procesed"""
    with open(TBL_INPUT, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=EMPLOYEES_SCHEMA_INPUT)
        
        for row in reader:
            employees.append(row)


def _save_clients_to_storage():
    """We are saving the date already processed to the output field"""
    tmp_table_name = '{}.tmp'.format(TBL_OUTPUT)

    with open(tmp_table_name, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=EMPLOYEES_SCHEMA_OUTPUT)
        writer.writerows(employees_output)

    os.remove(TBL_OUTPUT)
    os.rename(tmp_table_name, TBL_OUTPUT)

def _calculate_output():
    """Calling the function calculate() to process the input data and puting the data inside the list employees_output"""

    global employees_output
    global employees

    for employee in employees:
        employees_output.append(
        calculate(str(employee["first_name"]),
        str(employee["last_name"]),
        int(employee["annual_salary"]),
        int(employee["super_rate"].replace('%', '')) / 100,
        str(employee["payment_start_date"])
        )
        )


def list_clients():
    """listing employee payslip"""
    for employee in employees:
        print("{first_name} | {last_name} | {annual_salary} | {super_rate} | {payment_start_date}".format(
            first_name= employee["first_name"],
            last_name= employee["last_name"],
            annual_salary = employee["annual_salary"],
            super_rate = employee["super_rate"],
            payment_start_date = employee["payment_start_date"]            
        )
        )


def income_tax(annual_salary):
    if annual_salary <= 18200:
        return 0
    elif 18201 <= annual_salary and annual_salary <= 37000:
        return ((annual_salary - 18200) * 0.19) / 12
    elif 37001 <= annual_salary and annual_salary <= 87000:
        return (3572 + (annual_salary - 37000) * 0.325) / 12
    elif 87001 <= annual_salary and annual_salary <= 180000:
        return (19822 + (annual_salary - 87000) * 0.37) / 12
    elif 180001 <= annual_salary:
        return (54232 + (annual_salary - 180000) * 0.45) / 12

def pay_slip():
    print(" ")
    print("Please insert the following Employee information: ")
    print(" ")
    first_name = str(input("What is the employee first name: "))
    last_name = str(input("What is the employee last name: "))
    annual_salary = int(input("What is the employee annual salary (positive integer): "))
    super_rate = (int(input("What is the employee super rate (0 - 50 percentage): "))) / 100
    payment_start_date = str(input("What is the payment period (sample: 01 February - 29 February):  "))
    

    name = first_name + " " + last_name
    gross_income = round(annual_salary / 12)
    income_t = round(income_tax(annual_salary))
    net_income = round(gross_income - income_t)
    supeer = int(round(gross_income * super_rate))
    
    print("-" * 100)
    _print(name, payment_start_date, gross_income, income_t, net_income, supeer)
    print("-" * 100)

def calculate(first_name, last_name, annual_salary, super_rate, payment_start_date):

    name = first_name + " " + last_name
    gross_income = round(annual_salary / 12)
    income_t = round(income_tax(annual_salary))
    net_income = round(gross_income - income_t)
    supeer = int(round(gross_income * super_rate))

    employeev = {'name' : name,
        'payment_start_date' : payment_start_date,
        'gross_income' : gross_income,
        'income_t' : income_t,
        'net_income' : net_income,
        'supeer' : supeer
    }

    return employeev

    
def _print(name, payment_start_date, gross_income, income_t, net_income, supeer):

    print("{name} | {payment_start_date} | {gross_income} | {income_t} | {net_income} |{supeer} |".format(            
            name= name,
            payment_start_date= payment_start_date,
            gross_income = gross_income,
            income_t = income_t,
            net_income = net_income,
            supeer = supeer
    )
    )


def _print_welcome():
    print(" Employee monthly pay slip")
    print('*' * 50)
    print("What would you like to do?")
    print("[G]enerate Pay Slip")
    print("[P]rocess a csv file")
    print("[E]xit")


while True:

    if __name__ == "__main__":

        _print_welcome()

        command = input()
        command = command.upper()

        if command == "G":
            pay_slip()
        elif command == "P":
            _initialize_employees_from_file()
            _calculate_output()
            _save_clients_to_storage()
            print(employees_output)
        elif command == "E":
            break
        else:
            print('Invalid command')
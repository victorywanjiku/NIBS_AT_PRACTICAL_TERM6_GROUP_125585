#Salary Calculator

allowances={'J :5000,'}
{'k :5500,'}
{'L :6000,'}
{'M :65000,'}

payroll=input("Enter payrool Number:")
name=input("Enter name:")
gender=input("Enter gender:")
job_group=input("Enter Job Group (j/k/l/m):")
basic_salary=float(input("Enter basic salary:"))

if job_group=="J":
    allowances=5000
elif job_group=="K":
    allowances=5500
elif job_group=="L":
    allowances=6000
elif job_group=="M":
    allowances=6500
else:
    allowances=0
print("Invalid Job Group Entered . Allowance set to 0.")

gross_pay=basic_salary+allowances
taxes=0.12 * basic_salary
net_pay=gross_pay-taxes

print("\n----Employee Payroll Details---")
print("Payroll_No=:"+payroll)
print("Gender:"+gender)
print("job group:"+job_group)
print("basic salary: KES:"+basic_salary)
print("House Allowance:KES:"+allowances)
print("Gross Pay:KES:"+gross_pay)
print("Taxes:"+taxes)
print(" Net Pay:"+net_pay)

    
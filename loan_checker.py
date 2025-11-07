#LOAN CHECKER
customer_name=str(input("enter the name"))
age=int(input("enter the age"))
monthly_income=float(input("enter the income:"))
credit_score=float(input("enter the credit_score:"))

if monthly_income >=30000 and credit_score >=700:
    print("decision=Approved")
    reason="fully paid bills,Eligible"
else:
    decision="Rejected"
    reason="not fully paid bills,Not eligible"

 
print(f"\ncustomer_name:{customer_name}")
print(f"decision:{decision}")
print(f"reason:{reason}")



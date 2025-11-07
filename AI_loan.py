def loan_checker():
    name=str(input("Enter customername:"))
    age=int(input("Enter Age:"))
    income=float(input("Enter monthlyincome: "))
    creditscore=int(input("Enter your creditscore:"))
    if income>=1000 and creditscore>=700:
        print 
        decision="Aproved"
        print 
        decision="Meets income and credit score requirements"
    else:
        print 
        decision="Rejected"
        print 
        reason="Does not meet"
        print("\n---Loan Eligibility Reason---")
        print(f" Customername+{name}")
        print(f" Decision+{decision}")
        print(f"Reason+{reason}")
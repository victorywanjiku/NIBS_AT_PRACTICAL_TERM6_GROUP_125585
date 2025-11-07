food=float(input("enter food expense:"))
transport=float(input("enter transport expenses:"))
utilities=float(input("enter utilities expenses:"))


total=food+transport+utilities
p_food =(food/total)*100
p_transport=(transport/total)*100
p_utilities=(utilities/total)*100


print("\nCategory   Amount    Percentage")
print(f"Food         {food}     {p_food: .2f}%")
print(f"Transport     {transport}   {p_transport: .2f}%")  
print(f"utilities      {utilities}   {p_utilities:.2f}%")
print(f"total            {total}")


if p_food >50:
    print("Advice=You are overspending on food")
if utilities<20:
    print("Advice=Utilities spending is minimal")

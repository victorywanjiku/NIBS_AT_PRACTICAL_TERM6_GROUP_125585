#input details
name=str(input("enter student_name:"))
mark1=float(input("enter the mark 1:"))
mark2=float(input("enter the mark 2:"))
mark3=float(input("enter the mark 3:"))
grade=""
average=(mark1+mark2+mark3)/5
if average>=80:
    print(grade="A",comment="Excellent")
elif average>=70:
    print(grade="B",comment="Good")
elif average>=60:
    print(grade="C",comment="Good")
elif average>=50:
    print(grade="D",comment="improve")
else:
    print(comment="fail")

print("\n___Student Report___")
print(f"Name:{name}")
print(f"Average Mark:{average}")
print(f"grade:{grade}")


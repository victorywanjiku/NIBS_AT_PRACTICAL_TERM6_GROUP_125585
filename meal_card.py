# AI Complex Meal Card System for NIBS Technical College

# Meal prices
meal_prices = {
    "Breakfast": 100,
    "Lunch": 200,
    "Supper": 250
}

# Initial balance
initial_balance = 1000

# Collect student details
student_name = input("Enter Student Name: ")
admission_number = input("Enter Admission Number: ")
meal_type = input("Enter Meal Type (Breakfast, Lunch, Supper): ").capitalize()
payment_amount = int(input("Enter Payment Amount (KES): "))

# Validate meal type
if meal_type not in meal_prices:
    print("Invalid meal type selected.")
else:
    meal_cost = meal_prices[meal_type]
    balance = initial_balance

    # Check if payment matches meal cost
    if payment_amount < meal_cost:
        print("Insufficient payment for selected meal.")
    elif balance < meal_cost:
        print("Transaction Denied – Insufficient Balance.")
    else:
        balance = balance - meal_cost
        print("Meal purchased:", meal_type, "for KES", meal_cost)
        print("Remaining Balance:", "KES", balance)

        # Low balance warning
        if balance < 150:
            print("Low Balance – Please Top Up")

        # AI recommendation
        print("AI Recommendation:", "Consider weekly meal planning to manage your budget effectively.")

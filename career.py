# AI Career Path Recommendation System

# Career suggestions based on subject
career_paths = {
    "Math": ["Data Analyst", "Engineer"],
    "Science": ["Lab Technician", "Researcher"],
    "Art": ["Designer", "Animator"],
    "Business": ["Marketer", "Accountant"],
    "Home Science": ["Catering & Accommodation"]
}

# Get user input
name = input("Enter your name: ")
subject = input("Enter your preferred subject (Math, Science, Art, Business, Home Science): ").title()

# Generate recommendation
if subject in career_paths:
    careers = career_paths[subject]
    print("Hello", name + ", based on your interest in", subject + ", you might consider a career as a", " or ".join(careers) + ".")
else:
    print("Sorry,", name + ", we don't have recommendations for that subject at the moment.")

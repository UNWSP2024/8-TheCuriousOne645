# Predefined list of courses
courses = {
    "ACC2101": "Principles of Financial Accounting",
    "BIB2005": "Survey of the Old Testament",
    "COS2005": "Python Programming",
    "DAL2012": "Introduction to Data Analysis",
    "ECO2201": "Principles of Economics I",
    "FIN2025": "Personal Money Management",
    "GEO1007": "Principles of Geography",
    "HIS1005": "Historical Perspectives on Culture, Belief, & Civilization",
    "ICS2015": "World Religions",
    "LDR1015": "Leadership for Transformation",
    "MAT1035": "Business Mathematics"
}

# Ask the user to specify a subject
subject = input("Enter a subject (e.g., COS): ").strip().upper()

# Find and display courses that match the subject
matching_courses = {id: name for id, name in courses.items() if id.startswith(subject)}

if matching_courses:
    print(f"Courses under the subject '{subject}':")
    for course_id, course_name in matching_courses.items():
        print(f"{course_id}: {course_name}")
else:
    print(f"No courses found for the subject '{subject}'.")

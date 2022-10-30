stuFirstName = input("Enter your first name: ")
stuLastName = input("Enter your last name: ")
stuNumber = input("Enter your student number: ")
courseInfo = {
    "PROG1783": "IT Support Programming Fundament",
    "INFO1250": "Computer Systems Fundamentals",
    "INFO1385": "Network Infastructure I",
    "INFO1145": "Information Technology Documenta"
}
print("CourseCode   CourseName")
for key in courseInfo:
    print(key + "     "+ courseInfo[key])

registerCourses = input("Enter course codes to register : ").split(", ")

# OUTPUT
# Students information: full name and student number
print(stuFirstName + " " + stuLastName + " "+ stuNumber)
# List of selected courses:the course name and course code for each
for code in registerCourses:
    print(code + " " + courseInfo[code])
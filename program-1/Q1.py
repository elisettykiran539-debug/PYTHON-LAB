# Student Information and Academic Summary

# Accept student details
student_name = input("Enter Student Name: ")
usn = input("Enter USN: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

# Accept marks
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Calculate total and average
total_marks = mark1 + mark2 + mark3
average_marks = total_marks / 3

# Display student information
print("\n========== STUDENT INFORMATION ==========")
print(f"Student Name : {student_name}")
print(f"USN          : {usn}")
print(f"Branch       : {branch}")
print(f"Semester     : {semester}")

print("\n========== ACADEMIC SUMMARY ==========")
print(f"Subject 1 Marks : {mark1}")
print(f"Subject 2 Marks : {mark2}")
print(f"Subject 3 Marks : {mark3}")
print(f"Total Marks     : {total_marks}")
print(f"Average Marks   : {average_marks:.2f}")

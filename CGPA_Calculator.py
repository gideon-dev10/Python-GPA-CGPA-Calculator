name=input("Please enter your full name: ")
print(f"Welcome @{name}")
print("This Program allows you to calculate your grade point average(gpa) and your cumulative grade point average (cgpa)")
grand_total_unit = 0
grand_total_quality_point = 0
num_semesters=int(input("How many semesters do you want to calculate?: "))


for semester in range (num_semesters):
    semester_name = input("Enter Semester name: ")
    print(f"\n{semester_name}")

    total_unit= 0
    total_quality_point = 0
    
    num_courses = int(input("How many courses did you take this semester?: "))
    for i in range (num_courses):
             
        course_code = input("Enter the course code: ")
        course_unit = int(input("Enter the course unit: "))
        course_score = int(input("Enter course score:"))

        while course_score < 0 or course_score > 100:
         print("Score must be between 0 and 100")
         course_score = int(input("Enter course score: "))


        if course_score >=80:
         grade = "A"
         points = 5
        elif course_score >= 60:
         grade = "B"
         points = 4  
        elif course_score >= 50:
         grade = "C"
         points = 3
        elif course_score >= 45:
         grade = "D"
         points = 2
        elif course_score >= 40:
         grade = "E"
         points = 1
        else: 
         grade = "F"
         points = 0

        quality_point = (course_unit * points)
        total_unit+=course_unit
        total_quality_point+=quality_point
    

        print(f"Course: {course_code}")
        print(f"Course unit: {course_unit}")
        print(f"Grade: {grade}")
        print(f"Grade Point: {points}")
        print(f"Quality Point: {quality_point}")

        semester_gpa = total_quality_point / total_unit 

    print("\nSEMESTER RESULT")
    print(f"Total Units: {total_unit}")
    print(f"Total Quality Points: {total_quality_point}")
    print(f"GPA: {semester_gpa:.2f}")   

    grand_total_unit += total_unit
    grand_total_quality_point += total_quality_point

    semester_cgpa = grand_total_quality_point / grand_total_unit

print("\nFINAL SEMESTER RESULT")
print(f"Grand Total Units: {grand_total_unit}")
print(f"Grand Total Quality Points: {grand_total_quality_point}")
print(f"CGPA: {semester_cgpa:.2f}")

print(f"\nThank you for using the GPA & CGPA Calculator, {name}!")


   


                   







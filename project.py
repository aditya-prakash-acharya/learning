# STUDENT MARKS ANALYZER 

def analyze_student_marks():
    """Complete working student marks analyzer"""
    print("\n" + "="*50)
    print("   STUDENT MARKS ANALYZER")
    print("="*50)
    
    # Store all student data as one string
    all_students = ""
    
    # Input loop - add students
    while True:
        print("\n--- Add Student ---")
        name = input("Enter student name (or 'done' to finish): ").strip()
        
        if name.lower() == 'done':
            break
        
        if name == "":
            print("Name cannot be empty!")
            continue
        
        # Get marks for 4 subjects
        print(f"Enter marks for {name}:")
        
        # Subject 1 - Math
        while True:
            math = input("  Math (0-100): ")
            if math.isdigit():
                math = int(math)
                if 0 <= math <= 100:
                    break
            print("Please enter a number between 0 and 100!")
        
        # Subject 2 - Science
        while True:
            science = input("  Science (0-100): ")
            if science.isdigit():
                science = int(science)
                if 0 <= science <= 100:
                    break
            print("Please enter a number between 0 and 100!")
        
        # Subject 3 - English
        while True:
            english = input("  English (0-100): ")
            if english.isdigit():
                english = int(english)
                if 0 <= english <= 100:
                    break
            print("Please enter a number between 0 and 100!")
        
        # Subject 4 - Hindi
        while True:
            hindi = input("  Hindi (0-100): ")
            if hindi.isdigit():
                hindi = int(hindi)
                if 0 <= hindi <= 100:
                    break
            print("Please enter a number between 0 and 100!")
        
        # Calculate total
        total = math + science + english + hindi
        
        # Calculate percentage
        percentage = total / 4
        
        # Grade calculation as per new criteria
        if percentage >= 80:
            grade = "A+"
            grade_points = 10
            grade_description = "Excellent"
        elif percentage >= 70:
            grade = "A"
            grade_points = 9
            grade_description = "Very Good"
        elif percentage >= 60:
            grade = "B+"
            grade_points = 8
            grade_description = "Good"
        elif percentage >= 55:
            grade = "B"
            grade_points = 7
            grade_description = "Above Average"
        elif percentage >= 50:
            grade = "C"
            grade_points = 6
            grade_description = "Average"
        elif percentage >= 45:
            grade = "D"
            grade_points = 5
            grade_description = "Pass"
        else:
            grade = "F"
            grade_points = 0
            grade_description = "Fail"
        
        # Create student record as string
        student_record = f"{name}|{math}|{science}|{english}|{hindi}|{total}|{percentage:.2f}|{grade}|{grade_points}|{grade_description}"
        
        # Add to main string
        if all_students == "":
            all_students = student_record
        else:
            all_students = all_students + ";" + student_record
        
        print(f"\n[ADDED] {name}: Total={total}, Percentage={percentage:.2f}%, Grade={grade} ({grade_description})")
    
    # Check if any students were added
    if all_students == "":
        print("\nNo students entered! Exiting...")
        return
    
    # DISPLAY ALL STUDENT RESULTS
    print("\n" + "="*90)
    print("   STUDENT RESULT SUMMARY")
    print("="*90)
    
    # Split the string into individual student records
    student_list = all_students.split(";")
    
    # Print header
    print(f"{'Name':12} {'Math':6} {'Sci':6} {'Eng':6} {'Hindi':6} {'Total':6} {'%':7} {'Grade':6} {'GP':4} {'Description':12}")
    print("-"*90)
    
    # Variables for statistics
    total_students = 0
    sum_percentages = 0
    highest_percentage = 0
    topper_name = ""
    total_grade_points = 0
    
    # Grade counters
    grade_a_plus = 0
    grade_a = 0
    grade_b_plus = 0
    grade_b = 0
    grade_c = 0
    grade_d = 0
    grade_f = 0
    
    # Loop through each student and display

    for student in student_list:
        parts = student.split("|")
        
        name = parts[0]
        math = parts[1]
        science = parts[2]
        english = parts[3]
        hindi = parts[4]
        total = parts[5]
        percentage = float(parts[6])
        grade = parts[7]
        grade_points = int(parts[8])
        grade_description = parts[9]
        
        # Print student row
        print(f"{name:12} {math:6} {science:6} {english:6} {hindi:6} {total:6} {percentage:6.1f} {grade:6} {grade_points:4} {grade_description:12}")
        
        # Update statistics
        total_students = total_students + 1
        sum_percentages = sum_percentages + percentage
        total_grade_points = total_grade_points + grade_points
        
        # Find topper
        if percentage > highest_percentage:
            highest_percentage = percentage
            topper_name = name
        
        # Count grades
        if grade == "A+":
            grade_a_plus = grade_a_plus + 1
        elif grade == "A":
            grade_a = grade_a + 1
        elif grade == "B+":
            grade_b_plus = grade_b_plus + 1
        elif grade == "B":
            grade_b = grade_b + 1
        elif grade == "C":
            grade_c = grade_c + 1
        elif grade == "D":
            grade_d = grade_d + 1
        else:
            grade_f = grade_f + 1
    
    # DISPLAY CLASS STATISTICS

    print("\n" + "="*90)
    print("   CLASS STATISTICS")
    print("="*90)
    
    class_average = sum_percentages / total_students
    average_grade_points = total_grade_points / total_students
    
    print(f"Total Students: {total_students}")
    print(f"Class Average: {class_average:.2f}%")
    print(f"Average Grade Points: {average_grade_points:.2f}")
    print(f"Class Topper: {topper_name} with {highest_percentage:.2f}%")
    
    print("\nGrade Distribution:")
    print(f"  A+ (80-100%): {grade_a_plus} student(s)")
    print(f"  A  (70-79%): {grade_a} student(s)")
    print(f"  B+ (60-69%): {grade_b_plus} student(s)")
    print(f"  B  (55-59%): {grade_b} student(s)")
    print(f"  C  (50-54%): {grade_c} student(s)")
    print(f"  D  (45-49%): {grade_d} student(s)")
    print(f"  F  (0-39%): {grade_f} student(s)")
    
    # GRADE POINT SUMMARY
    print("\n" + "="*90)
    print("   GRADE POINT SUMMARY")
    print("="*90)
    print("Grade Points Guide:")
    print("  A+ (80-100): 10 points (Excellent)")
    print("  A  (70-79): 9 points (Very Good)")
    print("  B+ (60-69): 8 points (Good)")
    print("  B  (55-59): 7 points (Above Average)")
    print("  C  (50-54): 6 points (Average)")
    print("  D  (45-49): 5 points (Pass)")
    print("  F  (0-39): 0 points (Fail)")
    
    # FIND STUDENTS NEEDING ATTENTION
    print("\n" + "="*90)
    print("   STUDENTS NEEDING ATTENTION")
    print("="*90)
    
    fail_students = ""
    pass_students = ""
    excellent_students = ""
    
    for student in student_list:
        parts = student.split("|")
        name = parts[0]
        percentage = float(parts[6])
        grade = parts[7]
        
        # Students who failed (F grade)
        if grade == "F":
            if fail_students == "":
                fail_students = name + f" ({percentage:.1f}%)"
            else:
                fail_students = fail_students + ", " + name + f" ({percentage:.1f}%)"
        
        # Students who just passed (D grade)
        elif grade == "D":
            if pass_students == "":
                pass_students = name + f" ({percentage:.1f}%)"
            else:
                pass_students = pass_students + ", " + name + f" ({percentage:.1f}%)"
        
        # Excellent students (A+ and A)
        if grade == "A+" or grade == "A":
            if excellent_students == "":
                excellent_students = name + f" ({percentage:.1f}%)"
            else:
                excellent_students = excellent_students + ", " + name + f" ({percentage:.1f}%)"
    
    if fail_students != "":
        print(f"\n[FAIL] Students who failed (Below 45%):")
        print(f"  {fail_students}")
    else:
        print("\n[GOOD] No students failed!")
    
    if pass_students != "":
        print(f"\n[PASS] Students who just passed (45-49%):")
        print(f"  {pass_students}")
        print("  [NOTE] These students need extra support!")
    
    if excellent_students != "":
        print(f"\n[EXCELLENT] Students with A+ or A grade:")
        print(f"  {excellent_students}")
    
    # PASS/FAIL SUMMARY
    print("\n" + "="*90)
    print("   PASS/FAIL SUMMARY")
    print("="*90)
    
    pass_count = total_students - grade_f
    fail_count = grade_f
    
    print(f"Total Students: {total_students}")
    print(f"Passed: {pass_count} ({ (pass_count/total_students)*100:.1f}%)")
    print(f"Failed: {fail_count} ({ (fail_count/total_students)*100:.1f}%)")
    
    if fail_count > 0:
        print("\n[ACTION REQUIRED] Failed students need remedial classes!")
    else:
        print("\n[SUCCESS] All students passed!")
    
    # TOP PERFORMERS
    print("\n" + "="*90)
    print("   TOP PERFORMERS")
    print("="*90)
    
    if grade_a_plus > 0 or grade_a > 0:
        print("Top performers (A+ and A grades):")
        count = 0
        for student in student_list:
            parts = student.split("|")
            name = parts[0]
            grade = parts[7]
            percentage = float(parts[6])
            
            if grade == "A+" or grade == "A":
                count = count + 1
                print(f"  #{count}: {name} - {grade} ({percentage:.1f}%)")
    else:
        print("No top performers (A+ or A grade)")
    
    print("\n" + "="*90)

# MAIN MENU

def main():
    print("="*50)
    print("   STUDENT MARKS MANAGEMENT SYSTEM")
    print("="*50)
    print("This tool helps you:")
    print("  - Add student marks for 4 subjects")
    print("  - Calculate totals and percentages")
    print("  - Assign grades (A+ to F)")
    print("  - Grade Points: 0-10")
    print("  - View class statistics")
    print("  - Identify toppers and struggling students")
    print("="*50)
    
    while True:
        print("\n1. Analyze Student Marks")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            analyze_student_marks()
        elif choice == '2':
            print("\nThank you for using the Student Marks Management System!")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

# RUN THE PROGRAM

if __name__ == "__main__":
    main()
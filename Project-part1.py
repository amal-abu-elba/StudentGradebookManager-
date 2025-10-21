# Name: Amal Ahmed Abu Elba , ID: 220231850 , Section ID: 201 , Subject Name: Programming language (Lab)


import numpy as np

students = {
    "Alice": np.array([85, 92, 88]),
    "Bob": np.array([78, 85, 91]),
    "Charlie": np.array([92, 90, 95])
}


assignments = ["Homework 1", "Quiz 1", "Final Exam"]


def calculate_student_average(grades):
    return np.nanmean(grades)


def calculate_class_average(students):
    grades = np.array(list(students.values()))
    return np.nanmean(grades, axis=0)


def calculate_max_min(students):
    grades = np.array(list(students.values()))
    return np.nanmax(grades, axis=0), np.nanmin(grades, axis=0)


def calculate_std_deviation(students):
    grades = np.array(list(students.values()))
    return np.nanstd(grades, axis=0)


def main_menu():
    while True:
        print("\nWelcome to the Student Gradebook Manager!")
        print("1. View Grades")
        print("2. Add/Remove Student")
        print("3. Add/Remove Assignment")
        print("4. Show Class Stats")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")



        if choice == "1":
            display_results(students, assignments)

        elif choice == "2":
            modify_students()

        elif choice == "3":
            modify_assignments()

        elif choice == "4":
            display_Class_Stats(students, assignments)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")




def modify_students():
    action = input("Do you want to add or remove a student? (add/remove): ").strip().lower() ###############
    name = input("Enter student name: ").strip()

    if action == "add":
        if name.lower() in [s.lower() for s in students]:
            print(f"Student '{name}' already exists.")
            return
        

        grades = []
        for assignment in assignments:
            # To check from input 
            while True:
                try:
                    grade_input = input(f"Enter '{name}' grade for {assignment}: ").strip()
                    if grade_input == '':
                        grade = np.nan
                        break
                    grade = int(grade_input)
                    if grade < 0:
                        print("Grade cannot be negative. Please enter a valid grade.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            grades.append(grade)
         
        students[name] = np.array(grades)
        print(f"Student '{name}' added successfully.")


    elif action == "remove":   
        matched_name = None
        for student_name in students:
            if student_name.lower() == name.lower():
                matched_name = student_name
                break

        if matched_name:
            del students[matched_name]
            print(f"Student '{matched_name}' removed successfully.")

        else:
            print("Student not found.")

    else:
        print("Invalid action.")




def modify_assignments():
    action = input("Do you want to add or remove an assignment? (add/remove): ").strip().lower() #############
    name = input("Enter assignment name: ").strip()
    if action == "add":
        if name.lower() in [s.lower() for s in assignments]:
            print(f"Assignment '{name}' already exists.")
            return
        
        assignments.append(name)
        for student in students:
            while True:
                try:
                    grade_input = input(f"Enter grade for '{student}' in {name}: ").strip()
                    if grade_input == '':
                        grade = np.nan
                        break
                    grade = int(grade_input)
                    if grade < 0:
                        print("Grade cannot be negative. Please enter a valid grade.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            students[student] = np.append(students[student], grade)

        print(f"Assignment '{name}' added successfully for each Student.")



    elif action == "remove":
        matched_index = None
        for i, a in enumerate(assignments):
            if a.lower() == name.lower():
                matched_index = i
                break

        if matched_index is not None:
            removed_assignment = assignments.pop(matched_index)
            for student in students:
                students[student] = np.delete(students[student], matched_index)
            print(f"Assignment '{removed_assignment}' removed successfully.")

        else:
            print(f"'{name}' Assignment Not Exist.")


    else:
        print("Invalid action.")
        


def display_results(students, assignments):
    if not students:
        print("No students to display.")
        return

    print("\n🍀 Viewing Grades:\n")
    print("Student Gradebook\n")
    print(f"{'Student':<15} {'Grades':<30} {'Average':<12}")
    print("-------------------------------------------------------")

    for name, grades in students.items():
        avg = calculate_student_average(grades)
        print(f"{name:<15}  {str(grades):<30}  {'{:.2f}'.format(avg):<12}")

    print("\nClass Averages for Assignments:")
    class_avg = calculate_class_average(students)
    for i, avg in enumerate(class_avg):
        print(f"{assignments[i]:<15} {avg:.2f}")

    print("\nMax/Min Grades for Assignments:")
    max_grades, min_grades = calculate_max_min(students)
    for i in range(len(assignments)):
        print(f"{assignments[i]:<15} Max: {int(max_grades[i])} Min: {int(min_grades[i])} ")




def display_Class_Stats(students, assignments):
    std_devs = calculate_std_deviation(students)
    display_results(students, assignments)
    print("\nStandard Deviation for Assignemnts: ")
    for i in range(len(assignments)):
        print(f"{assignments[i]:<15} Std Dev: {std_devs[i]:.2f}")

        


main_menu()


 

 # لما ما ادخل علامة طالب لمادة
 # الحذف في ال student و ال assingnment
def get_student_name():
    return input("Please enter the name of the student you would like to add: ")

def get_all_students(students):
    for student in students:
        print(student)

def remove_student(students):
    student = input("Please enter the name of the student you would like to remove: ")
    if student in students:
        return students.remove(student)
    else: 
        return students

def main():
    students = []
    while True: 
        menu = input("Welcome. Please enter a valid oprion:\n1. Add a student\n2. View all students\n3. Remove a student\n->")
        if menu.isnumeric():
            menu=int(menu)
            if menu == 1:
                students.append(get_student_name())
            elif menu == 2:
                get_all_students(students)
            elif menu == 3:
                remove_student(students)           
        
main()
class StudentSystem:
    def __init__(self):
        self.students = []
    
    def calculate_grade(self, marks):
        if marks >= 85:
            return 'A'
        elif marks >= 70:
            return 'B'
        elif marks >= 55:
            return 'C'
        else:
            return 'Fail'
        
    def add_student(self):
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name:")
        marks = int(input("Enter Marks: "))

        self.students.append({roll_no, name, marks})
        self.students.sort(key=lambda x: x[0])  # Sort by roll number
        
        print("Student record added successfully.\n")

    def display_student(self):
        if not self.students:
            print("No student records available.\n")
            return

        print("\t\t\tStudent Records")
        print("\nRoll No\tName\tMarks\tGrade")
        for student in self.students:
            grade = self.calculate_grade(student[2])
            print(f"{student[0]}\t{student[1]}\t{student[2]}\t{grade}")
        print()
    
    def binary_search(self, roll_no):
        low = 0
        high = len(self.students) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.students[mid][0] == roll_no:
                return mid
            elif self.students[mid][0] < roll_no:
                low = mid + 1
            else:
                high = mid - 1

        return None
    
    def search_student(self):
        if not self.students:
            print("No student records available.\n")
            return
        
        roll = int(input("Enter Roll Number to Search:"))
        result = self.binary_search(roll)

        if result:
            grade = self.calculate_grade(self.students[result][2])
            print("\nStudent Found:")
            print("\n--------------------------------")
            print(f"Roll No: {self.students[result][0]}")
            print(f"Name: {self.students[result][1]}")
            print(f"Marks: {self.students[result][2]}")
            print(f"Grade: {grade}")
        else:
            print("Student record not found.\n")

# Main Program
system = StudentSystem()

while True:
    print("====== Student Result Finder System ======")
    print("1. Add Student Record")
    print("2. Display All Students")
    print("3. Search Student Result")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        system.add_student()
    elif choice == '2':
        system.display_student()
    elif choice == '3':
        system.search_student()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
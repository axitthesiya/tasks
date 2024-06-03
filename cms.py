import csv
from datetime import datetime

# Define the base class Person with methods to get name and ID
class Person:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    
    def get_name(self):
        return self.name
    
    def get_ID(self):
        return self.ID

# Define a class Student inheriting from Person with additional attributes
class Student(Person):
    def __init__(self, name, ID, student_class, roll_number):
        super().__init__(name, ID)
        self.student_class = student_class
        self.roll_number = roll_number
    
    def get_class(self):
        return self.student_class
    
    def get_roll_number(self):
        return self.roll_number

# Define a class Teacher inheriting from Person with additional attributes
class Teacher(Person):
    def __init__(self, name, ID, subject_taught):
        super().__init__(name, ID)
        self.subject_taught = subject_taught
    
    def get_subject(self):
        return self.subject_taught

# Define the Attendance class for managing attendance records
class Attendance:
    def __init__(self, school_name):
        self.school_name = school_name
        self.attendance_records = {}
        # Print the school name 
        print(f"School Name: {self.school_name}")
        if not self.school_name:
            raise Exception("School Name Is Not Found In Database SO Please Fill The School Name.... ")

    # Method to mark attendance for a student on a specific date
    def mark_attendance(self, student_id, date):
        # Check if the student ID is valid
        if student_id not in students:
            raise ValueError(f"Invalid Student ID: {student_id}. Student name: {students.get(student_id, 'Unknown')}")
        
        # Add the attendance record for the student
        if student_id in self.attendance_records:
            self.attendance_records[student_id].append(date)
        else:
            self.attendance_records[student_id] = [date]

    # Method to generate attendance report for a specific teacher and time period
    def generate_report(self, start_date, end_date, teacher_id=None):
        # Check if the teacher ID is provided and valid
        if teacher_id is None:
            raise ValueError("Teacher ID is required to generate the report.")
        
        if teacher_id not in teachers:
            raise ValueError(f"Invalid Teacher ID: {teacher_id}. Teacher name: {teachers.get(teacher_id, 'Unknown')}")

        # Write attendance report to a CSV file
        filename = f'attendance_report_{self.school_name}.csv'
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Student ID', 'Name', 'Date'])

            for student_id, dates in self.attendance_records.items():
                student_name = students[student_id].get_name()
                for date in dates:
                    # Write attendance record for each student within the specified time period
                    if start_date <= date <= end_date:
                        writer.writerow([student_id, student_name, date])

# Create instances of students and teachers
students = {
    'S001': Student('Alice', 'S001', 'Class 10', '101'),
    'S002': Student('Bob', 'S002', 'Class 10', '102'),
    'S003': Student('Charlie', 'S003', 'Class 10', '103')
}

teachers = {
    'T001': Teacher('Mr. Smith', 'T001', 'Maths'),
    'T002': Teacher('Ms. Johnson', 'T002', 'English')
}

# Create an instance of the Attendance class for each school
attendance_school_1 = Attendance("EDU School")

# Marking attendance for students in each school
try:
    attendance_school_1.mark_attendance('S001', datetime(2024, 5, 2)) 
    attendance_school_1.mark_attendance('S002', datetime(2024, 5, 2))  
    attendance_school_1.mark_attendance('S003', datetime(2024, 5, 2))   
except ValueError as e:
    print(e)

# Generating report for each school
try:
    attendance_school_1.generate_report(datetime(2024, 5, 1), datetime(2024, 5, 31), teacher_id='T002') 
    print("Report Generated Successfully.....")
except ValueError as e:
    print(e)

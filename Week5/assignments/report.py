# Define the Student class 
class Student:
    # __init__ runs when we create a new student object
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    # Method to calculate the average mark
    def average(self):
        total = sum(self.marks)
        count = len(self.marks)
        return total / count
    
    # Method to determine the grade based on average
    def grade(self):
        # Getting the average by calling the average() method
        avg = self.average()
        # Check which grade range the average falls into
        if avg >= 80:
            return "A"
        elif avg >= 65:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"
    
    # Method to display all student information
    def display(self):
        avg = self.average()
        grd = self.grade()
        # Determine if student passed or failed
        if avg >= 40:
            status = "Pass"
        else:
            status = "Fail"
        
        # Print all the student information
        print("Name: " + self.name)
        print("Average: " + str(round(avg, 1)))
        print("Grade: " + grd)
        print("Status: " + status)
        print("-" * 25) 

# Create a list of tuples with student data
students = [
    ("Aarav",  [78, 85, 60, 90, 72]),  # Student 1
    ("Sita",   [45, 50, 38, 60, 55]),  # Student 2
    ("Bishal", [30, 25, 40, 35, 28]),  # Student 3
    ("Priya",  [90, 88, 95, 92, 87]),  # Student 4
]

# An empty list to store student objects
student_objects = []

# Loop through each student in the students list
for name, marks in students:
    student = Student(name, marks)
    student_objects.append(student)

# Print 
print("-" * 30)
print("STUDENT REPORT CARDS")
print("-" * 30)
print()

# Loop through each student object in our list
for student in student_objects:
    student.display()
    print() 

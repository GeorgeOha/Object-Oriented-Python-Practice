"""
Python OOP Practice Assignment
-------------------------------
This script demonstrates Object-Oriented Programming concepts such as:
- Class creation and methods
- Working with objects, lists, sets, dictionaries, and tuples
- Email validation using Regular Expressions
"""

import re  # For email validation


# -------------------------------
# Part 1: Class Definition
# -------------------------------
class Student:
    def __init__(self, name, email, grades=None):
        """Initialize a Student object with name, email, and grades."""
        self.name = name
        self.email = email
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        """Adds a grade to the grades list."""
        self.grades.append(grade)

    def average_grade(self):
        """Returns the average of all grades."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """Prints the student's name, email, and grades."""
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")
        print("-" * 40)

    def grades_tuple(self):
        """Returns the grades as a tuple."""
        return tuple(self.grades)


# -------------------------------
# Part 2: Working with Objects
# -------------------------------

# Create 3 student objects
student1 = Student("Alice Johnson", "alice@example.com", [85, 90, 78])
student2 = Student("Bob Smith", "bob@example.com", [92, 88, 95])
student3 = Student("Charlie Brown", "charlie@example.com", [70, 75, 80])

# Add 2 new grades to each student
for s in (student1, student2, student3):
    s.add_grade(89)
    s.add_grade(94)

# Display info for each student
student1.display_info()
student2.display_info()
student3.display_info()


# -------------------------------
# Part 3: Dictionary & Set Integration
# -------------------------------

# Map each student's email to their object
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

def get_student_by_email(email):
    """Retrieve a student safely using dictionary .get()."""
    return student_dict.get(email, None)

# Example usage
search_email = "bob@example.com"
found_student = get_student_by_email(search_email)
if found_student:
    print(f"Student found for {search_email}: {found_student.name}")
else:
    print(f"No student found for {search_email}")

print("\nAll students’ emails:", list(student_dict.keys()))

# Create a set of all unique grades
unique_grades = set(student1.grades + student2.grades + student3.grades)
print(f"\nUnique grades across all students: {unique_grades}")
print("-" * 40)


# -------------------------------
# Part 4: Tuple Practice
# -------------------------------

# Get tuple of grades for student1
grades_tuple = student1.grades_tuple()
print(f"{student1.name}'s grades as tuple: {grades_tuple}")

# Demonstrate tuple immutability
try:
    grades_tuple[0] = 100  # Attempt to modify tuple
except TypeError:
    print("Error: Tuples are immutable — you cannot change their contents!\n")


# -------------------------------
# Part 5: List Operations
# -------------------------------

for s in (student1, student2, student3):
    if s.grades:
        s.grades.pop()  # Remove

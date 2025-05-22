# Student Performance Tracking System using Encapsulation

class Student:
    # Constructor to initialize student name, ID, GPA, and internal grade storage
    def __init__(self, name, student_id):
        self.name = name                         
        self.student_id = student_id             
        self.__gpa = 0.0                         
        self.__grades_dictionary = {}          

    # method to add a grade for a subject
    def add_grade(self, subject, grade):
        # Check that the grade is within a valid range (0 to 100)
        if grade >= 0 and grade <= 100:
            self.__grades_dictionary[subject] = grade  
        else:
            print("Invalid Grade. Must be between 0 and 100")  

    # method to generate a performance report
    def get_report(self):
        # If no grades are recorded, return a message
        if len(self.__grades_dictionary) == 0:
            return "No Grades available"

        # Calculate GPA by averaging all recorded grades
        sum_of_grades = sum(self.__grades_dictionary.values())
        self.__gpa = sum_of_grades / len(self.__grades_dictionary)

        # Return a dictionary containing student details and GPA
        return {
            "name": self.name,
            "student id": self.student_id,
            "grades": self.__grades_dictionary,
            "GPA": round(self.__gpa, 2)  
        }

student1 = Student("Nithin", "111")

student1.add_grade("Maths", 99)
student1.add_grade("Science", 99)


print(student1.get_report())

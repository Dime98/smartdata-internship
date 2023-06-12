# ## Resources ##
# - https://medium.com/pythoneers/a-quick-look-at-object-oriented-programming-oop-in-python-975fc3cb9618
# - https://medium.com/geekculture/getting-started-with-object-oriented-programming-in-python-3-e0a87d38acfc
# - https://medium.com/techtofreedom/10-remarkable-python-oop-tips-that-will-optimize-your-code-significantly-a47e4103b44d
# - https://www.informit.com/articles/article.aspx?p=453682&seqNum=6


# 1. Choose a topic to create a project on.
# 2. Your project should contain the following stuff:
# - A class with the following criteria:
#     * an initialization method (some fields should be private and/or protected);
#     * at least three Python special functions;
#     * some methods with different accessing criteria (public protected, private);
#     * fields should be of minimum 3 different data types.
# - Two or more classes that inheirit the the basic class described above and should contain some overriden or overloaded methods from the parent class.
# 3. Create objects of each type described in your project. 
# 4. Show the differences between the objects of different types (their creation, usage, output, so on).
# 5. Create a GitHub repository whaere you will be posting all homeworks during your studying period and send me the link to it.
# 6. Deadline for submission: 21:00.

# School Management System:
# Create a class for managing student records with private fields like name, age, and grade.
# Implement methods for calculating average grades, updating student information, and displaying student details.
# Use protected fields for attributes like parent contact information and attendance records.
# ======================================

# Method Overriding:
# Student Class:
# Override the display_details method in the Student class to provide a customized display of student-specific information.

# Course Class:
# Override the display_details method in the Course class to include additional details specific to the course, such as prerequisites or textbook information.

# Teacher Class:
# Override the display_details method in the Teacher class to display additional information specific to teachers, such as their qualifications or teaching experience.

# Method Overloading:
# Course Class:
# Implement multiple versions of the enroll_student method in the Course class that accept different parameters. For example, you can have an enroll_student method that takes just the student object, as well as an overloaded version that also accepts an enrollment date or a grade for the student.

# Student Class:
# Implement overloaded methods in the Student class for calculating the average grade. You can have one version of the method that calculates the average grade for all courses, and another version that calculates the average grade for a specific semester or year.

# School Class:
# Implement overloaded methods in the School class for managing courses and teachers. For example, you can have methods to add a single course or multiple courses at once, or to assign a single teacher or multiple teachers to a course.


# ======================================
class Employee:
    def __init__(self, first_name, last_name, department):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    def display_info(self):
        print("\nEmployee info:")
        print(f"name:          {self.first_name} {self.last_name}")
        print(f"department:    {self.department}")

# ======================================
class Teachers(Employee):
    def __init__(self, first_name, last_name, department, social_number, phone_number, age, exp):
        super().__init__(first_name, last_name, department,)
        # public attr
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.age = age
        self.exp = exp

        # protected attr
        self._phone_number = phone_number
        # private attr
        self.__social_number = social_number

    def display_info(self):
        print("\nEmployee info (Override)")
        print(f"name:          {self.first_name} {self.last_name}")
        print(f"department:    {self.department}")
        print(f"phone:         {self._phone_number}")
        print(f"age:           {self.age}")
        print(f"exp:           {self.exp}")

    def change_social_number(self, new_social_number):
        self.__social_number = new_social_number

# ======================================
class Students:
    def __init__(self, first_name, last_name, age, coueses, scholarship = False):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.coueses = coueses
        self.scholarship = scholarship
    
    def __str__(self):
        # full_name = f"{self.first_name} {self.last_name}"
        return f"Student full name: {self.first_name} {self.last_name}"

    def __len__(self):
        return len(self.coueses)

    def __del__(self):
        print(f"Student {self.first_name} {self.last_name} deleted")

# ======================================
class Course:
    all_coueses = []
    def __init__(self, course_name, teacher = None):
        self.course_name = course_name
        self.teacher = teacher

        Course.all_coueses.append(self.course_name)

# ======================================
# create course objects
crs_bio = Course("Biology")
crs_it = Course("Computer science")
crs_design = Course("UX")

# print all courses
print("Available courses:")
for course in Course.all_coueses:
    print(f"\t{course}")

# ======================================
print()
teacher1 = Teachers("Dan", "Clinton", "biology", 12346789, "555-1212" ,35, 15)
# # teacher2 = Teachers("teach2", "teach2 last name")

# change protected field
# print(teacher1.__social_number) # this line would give an error because __social_number is private
print("\nchanging private variable __social_number within class using change_social_number()")
print(teacher1.__dict__)
teacher1.change_social_number(98765432)
print(teacher1.__dict__)

# partially private var
print("\nchanging partially private variable _phone_number")
print(teacher1._phone_number)
teacher1._phone_number = "444-1212"
print(teacher1._phone_number)


# Method Overriding
# print(teacher1.display_info())
print()
emp_1 = Employee("Mick", "Thompson", "assistant")
print(emp_1.display_info())
print(teacher1.display_info())

# ======================================
print()
# create Student obj and add courses
s1_courses = [crs_bio, crs_it, crs_design]
s1 = Students("Alex", "winston", 25, s1_courses, True)
s2 = Students("john", "snow", 25, crs_it)

# using __str__ to print out full name
print(s1)

# using __len__ to print number of courses student is attending
print(f"{s1.first_name} if taking {len(s1)} courses")

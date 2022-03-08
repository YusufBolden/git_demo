manuel = {
    "name":"Manuel",
    'homework':[],
    'quizzes':[],
    'tests':[]
}
yuyan = {
    "name":"Yuyan",
    'homework':[],
    'quizzes':[],
    'tests':[]
}
tyler = {
    "name":"Tyler",
    'homework':[],
    'quizzes':[],
    'tests':[]
}

# print(manuel)
# print(yuyan)
# print(tyler)

# Input student grades
manuel['homework'] = [90,97,75,92]
manuel['quizzes'] = [88, 40, 94]
manuel['tests'] = [75, 90]

yuyan['homework'] = [100, 92, 98, 100]
yuyan['quizzes'] = [82, 83, 91]
yuyan['tests'] = [89, 97]

tyler['homework'] = [0, 87, 75, 22]
tyler['quizzes'] = [0, 75, 78]
tyler['tests'] = [100, 100]


# Create a list called students that contains your three students and print the list

students = [manuel, yuyan, tyler]

# print(students)



# Loop over your students list and print out the following for each student:
#   - Name: (print out the student's name)
#   - Homework: (print out the student's homework)
#   - Quizzes: (print out the student's quizzes)
#   - Tests: (print out the student's tests)

for student in students:
    print('Student: ', student['name'])
    print(f"Homework: {student['homework']}")
    print(f"Quizzes: {student['quizzes']}")
    print(f"Tests: {student['tests']}")

# We can now comment out everything above and import all the functions from logic_review.py using the wildcard *
from logic_functions import *

print(average(yuyan['tests']))

for student in students:
     print('Name: ', student['name'])
     print('Weighted average: ', get_weighted_average(student))



# The class now has a new student, Walden, with the following grades:
#   Homework: 90, 85, 80, 0
#   Quizzes: 80, 100, 87
#   Tests: 85, 90
#   a. Create a dictionary for Walden
#   b. add him to the class, by appending the dictionary to your list of students
#   c. Calculate the new class average and print your results

# Add Walden
walden = {
    'name':'Walden',
    'homework':[90, 85, 80, 0],
    'quizzes':[80, 100, 87],
    'tests':[85, 90]
}

# Part B. Add thomas to class
students.append(walden)
print(students)

# Part C. Calculate new class average
print(get_class_average(students))

# print(get_letter_grade(91))
# print(get_letter_grade(81))
# print(get_letter_grade(31))

for student in students:
    print('Name: ', student['name'])
    print('Weighted average: ', get_weighted_average(student))
    final_grade = get_weighted_average(student)
    print('Letter grade: ', get_letter_grade(final_grade))

print(get_class_average(students))

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# Add the grades to student_grades.👇
student_grades = {}

for student in student_scores:
    grades = student_scores[student]
    if grades > 90:
        grades = "Outstanding"
    elif grades > 80:
        grades = "Exceeds Expectations"
    elif grades > 70:
        grades = "Acceptable"
    else:
        grades = "Fail"

    student_grades[student] = grades

'''
for student in student_scores:
    grades = student_scores[student]
    if grades > 90:
        student_grades[student] = "Outstanding"
    elif grades > 80:
        student_grades[student] = "Exceeds Expectations"
    elif grades > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
'''

print(student_grades)
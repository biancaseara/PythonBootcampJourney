student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_height = 0
count = 0
for height in student_heights:
    sum_height += height
    count += 1

average = round(sum_height / count)

print(average)
students = {
    "A" : [80, 90, 75],
    "B" : [60, 70, 65],
    "C" : [95, 88, 92]
}
Grand_total = 0
for student in students:
    marks = students[student]
    total =0
    for i in range(len(marks)):
        total += marks[i]
        Avg = total/(len(marks))
    print(f"Average score of {student} is {Avg}")
    if Avg >= 85:
        print(f"{student} is in the topper list with {Avg}")
    Grand_total += Avg
    Grand_total_Avg = Grand_total/len(students)
print(f"Average of all students in the class is {Grand_total_Avg}")

student_score = {
        'Harry':88,
        'Ron' : 78,
        'Hermione' :95,
        'Draco' : 75,
        'Neville' : 60
}
student_grades = {}

for grade in student_score:
    if student_score[grade] >= 91 and student_score[grade] <= 100:
        student_grades[grade]="Outstanding"

    elif student_score[grade] >= 81 and student_score[grade] <= 90:
        student_grades[grade] ="Exceeds Expectation"

    elif student_score[grade] >= 71 and student_score[grade] <= 80:
        student_grades[grade] = "Acceptable"

    elif student_score[grade] <= 70:
        student_grades[grade] = "Fail"

for grades in student_grades:
    print(grades+ "  "+student_grades[grades])

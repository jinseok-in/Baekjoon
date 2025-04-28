N = int(input())
students = []

for _ in range(N):
    name, korean, english, math = input().split()
    korean, english, math = int(korean), int(english), int(math)
    students.append((name, korean, english, math))

students.sort(key=lambda student: (-student[1], student[2], -student[3], student[0]))

for student in students:
    print(student[0])
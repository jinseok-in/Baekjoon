student = []
for i in range(1, 31) :
    student.append(i)

for submit in range(28) :
    send_st = int(input())
    student[send_st-1] = 0
while 0 in student :
    student.remove(0)
print(f'{student[0]}\n{student[1]}')
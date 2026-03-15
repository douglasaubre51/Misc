num = int(input('enter subject score: '))

grade = 'F'

if num >= 90:
    grade = 'S'
elif num < 90 and num >= 80:
    grade = 'A'
elif num < 80 and num >= 70:
    grade = 'B'
elif num < 70 and num >= 60:
    grade = 'C'
elif num < 60 and num >= 50:
    grade = 'D'
elif num < 50 and num >= 40:
    grade = 'E'

print(f'subject grade is: {grade}')

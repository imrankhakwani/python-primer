# Student Grades
# Calculate grade on the following scheme
#
# >= 90 ---> A+
# >= 80 and < 90 ---> A
# >= 70 and < 80 ---> B
# >= 60 and < 70 ---> C
# >= 50 and < 60 ---> D
# >= 40 and < 50 ---> E
# >= 30 and < 40 ---> F
#

score = 2
grade = ''

if score >= 90:
    grade = 'A+'
elif 80 <= score < 90:
    grade = 'A'
elif 70 <= score < 80:
    grade = 'B'
elif 60 <= score < 70:
    grade = 'C'
elif 50 <= score < 60:
    grade = 'D'
elif 40 <= score < 50:
    grade = 'E'
elif score < 40:
    grade = 'F'

print('The student obtained the following grade: ', grade)

# uninitialized variables are treated as False
condition = {}

print(type(condition))

if condition:
    print('True')
else:
    print('False')

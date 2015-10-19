from statistics import mean as m

admins = {'rogster':'pass1', 'user2':'pass2'}

studentDict = {'Jeff': [78, 88, 93],
               'Alex': [92, 76, 88],
               'Sam': [89, 92, 93]}

def enterGrades():
    name_to_enter = input("Student Name: ")
    grade_to_enter = input("Grade: ")

    if name_to_enter in studentDict:
        print('Adding grade...')
        studentDict[name_to_enter].append(int(grade_to_enter))
    else:
        print('Student does not exist bitch...')

    print(studentDict)

def removeStudent():
    name_to_remove = input("What student should we kick out?: ")
    if name_to_remove in studentDict:
        print("removing student...")
        del studentDict[name_to_remove]

    print(studentDict)

def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent,"has an avereage grade of: ",avgGrade)

def main():
    print("""
        Welcome to Grade Central!

        [1] - Enter Grades
        [2] - Remove a Student
        [3] - Student Average Grades
        [4] - Exit
    """)

    action = input("What would you like to do today? (Enter a number) ")

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        exit()
    else:
        print("No valid choice was given, try again")

login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome,',login)
        while True:
            main()
    else:
        print('Invalid password, dickhead')
else:
    print('Invalid username, fuckface')

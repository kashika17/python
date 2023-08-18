
import json
users_data = {'kashika':1234,'lavisha':1235,'yashi':1236}
count=0
recordAttendance={}
studentId=""
studentName=""
present_count = {}
studentData={}
with open("students.txt", "r") as file:
        for line in file:
            studentId, studentName = line.strip().split(' - ')
            studentData[studentId]=studentName
with open("attendance.txt", "r") as file:
        for line in file:
                    if line.startswith("Student ID: "):
                        studentId = line.strip().split(":")[1].strip()
                        recordAttendance[studentId] = {}
                    elif line.startswith("("):
                        date,status = line.strip()[1:-1].split(", ")
                        date = date.strip("'")  
                        status = status.strip("'")
                        recordAttendance[studentId][date]=status
print(recordAttendance)
a = ''
def login():
    for i in range(3):
        username = input("Enter your username ")
        password = int(input("Enter your password "))

        if username in users_data and users_data[username]==password:
            print("access granted")
            global a 
            a = 'access granted'
            break
        else:
            if i < 2 :
                print("-----------------try again!---------------")
            else:
                print("-----------------//access denied//------------")

ans=input("DO YOU WANT TO LOGIN? enter yes or no  ")
if ans=='yes':
    login()

def addStudent():
    print('---------------------ADD STUDENT DATA----------------------')
    n=int(input("How many records do you want to enter?"))
    for i in range(n):
        studentId=(input("Enter id- "))
        studentName = input("Enter name- ")
        if studentId not in studentData:
            studentData[studentId]=studentName
        else:
            print('Record already exists')
    with open("students.txt","w") as file:
                for studentId, studentName in studentData.items():
                    file.write(f"{studentId} - {studentName}\n")

def viewStudent():
    print('---------------------STUDENT DATA----------------------------')
    with open("students.txt", "r") as file:
        for line in file:
            student_id, student_name = line.strip().split('-')
            print(f"Student ID -> {student_id}")
            print(f"Name -> {student_name}")

def updateStudent():
    studentId=input("Enter id- ")
    studentName = input("Enter name- ")
    studentData[studentId]=studentName
    with open("students.txt", "w") as file:
        for studentId, studentName in studentData.items():
            file.write(f"{studentId} - {studentName}\n")
    print('UPDATE DONE!')

def deleteStudent():
    studentId=(input("Enter id- "))
    if studentId in studentData:
        del studentData[studentId]
    else:
        print("Record not found ")
    with open("students.txt", "w") as file:
            for studentId,studentName in studentData.items():
                file.write(f"{studentId} - {studentName}\n")
def markAttendance():
    print('---------------------ATTENDANCE RECORD----------------------')
    res='yes'
    while res=='yes':
        res=input('Do you want to mark attendance? ')
        if res=='yes':
            studentId=input("Enter id- ")
            if studentId in studentData:
                n = int(input("How many days you want to enter attendance for?  "))
                for i in range(n):
                    date=(input("Enter the date in format DD/MM/YYYY  "))
                    status=(input("Mark your attendance  "))
                    if studentId not in recordAttendance:
                        recordAttendance[studentId] = {}
                    recordAttendance[studentId][date] = status
                    if status == "P":
                        if studentId not in present_count:
                            present_count[studentId] = 1
                        else:
                            present_count[studentId] += 1
            else:
                print("Record not found!")
    with open("attendance.txt","w") as file:
        for studentId, status in recordAttendance.items():
            file.write(f"Student ID:  {studentId}\n")
            file.write(f"status:\n")   
            for status in status.items():
                file.write(f"{status}\n")


def reportAttendance():
    print('--------------------------REPORT--------------------------')
    print("Attendance:")
    for studentId, status in recordAttendance.items():
        print("Student ID:  ",studentId)
        print(   "    date:  status")   
        for date, status in status.items():
            print(f"    {date}: {status}")

if a=="access granted":
    while True:
        print("\nAVAILABLE TASKS\n")
        print("1. Add Student \n2. View Student Data \n3. Update Student Data \n4. Delete a Student Record \n5. Mark Attendance \n6. Attendance Report \n7. EXIT\n")
        choice=int(input("SELECT THE TASK YOU WANT TO PERFORM "))
        if choice==1:
            addStudent()
        elif choice==2:
            viewStudent()
        elif choice==3:
            updateStudent()
        elif choice==4:
            deleteStudent()
        elif choice==5:
            markAttendance()
        elif choice==6:
            reportAttendance()
        elif choice==7:
            break
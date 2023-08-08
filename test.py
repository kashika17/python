recordAttendance={}
def loadStatus():
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

loadStatus()
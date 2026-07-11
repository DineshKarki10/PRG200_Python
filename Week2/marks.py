marks = []
names = []
num = int(input("Enter the number of students: "))
for i in range(num):
    name = input(f"Enter the name of the student {i+1}: ")
    mark= float(input(f"Enter the marks of {i+1} Student: "))
    names.append(name)
    marks.append(mark)
for m in range(len(marks)):
    if(marks[m]>=90):
        print(f"{names[m]} : Distinction")
    elif(marks[m]>=75):
        print(f"{names[m]} : First Division")
    elif(marks[m]>=65):
        print(f"{names[m]} : Second Division")
    elif(marks[m]>=35):
        print(f"{names[m]} : Third Division")
    else:
        print(f"{names[m]} : Failed")
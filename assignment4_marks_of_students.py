n=int(input("enter number of students:"))
if(n>=0):
    student=["member"]
    for i in range(0,n):
        name=input("enter the name of the student:")
        print(name)
        mark=float(input("enter the marks:"))
        print(mark)
        if(mark<40):
            student.append(name)
            print("this student has failed")
        else:
            print("this student has passed")
    for i in range(1,len(student)):
        print(student[i])
else:
    print("invalid input")

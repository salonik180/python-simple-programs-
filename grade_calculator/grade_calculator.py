print("STUDENT GRADE CALCULATOR")
name=input("enter student name: ")
maths=float(input("enter math marks: "))
english=float(input("Enter English marks:"))
science=float(input("Enter science marks:"))


total = maths + english + science
average = total/3
if average >= 70:
    grade = "A"

elif average >= 60:
    grade = "B"

elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"


print("\n ---------RESULT---------")
print("name:",name)
print ("total marks",total)
print("Average:",average)
print("Grade:",grade)
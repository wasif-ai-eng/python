a = int(input("Enter 1st Subject Marks: "))
b = int(input("Enter 2nd Subject Marks: "))
c = int(input("Enter 3rd Subject Marks: "))

total = a + b + c

print("Total Marks:", total)

percentage = total / 3
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
elif percentage >= 50:
    print("Grade: E")
elif percentage >= 40:
    print("Grade: F")
else:
    print("Fail")
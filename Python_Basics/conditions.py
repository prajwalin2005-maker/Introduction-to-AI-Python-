# Python Conditional Statements

age = 21

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# if, elif, else example

marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Marks:", marks)
print("Grade:", grade)


# Even or Odd

number = 10

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

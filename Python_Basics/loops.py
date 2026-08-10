# Python Loops

# For loop

print("For Loop:")

for i in range(1, 6):
    print(i)


# Loop through a list

print("\nSubjects:")

subjects = ["AI", "Python", "Machine Learning"]

for subject in subjects:
    print(subject)


# While loop

print("\nWhile Loop:")

count = 1

while count <= 5:
    print(count)
    count += 1


# Sum using a loop

total = 0

for i in range(1, 11):
    total += i

print("\nSum of numbers from 1 to 10:", total)


# Break statement

print("\nBreak Example:")

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# Continue statement

print("\nContinue Example:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Python Lists

# Creating a list

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:", fruits)


# Accessing elements

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])


# Adding an element

fruits.append("Grapes")

print("After append:", fruits)


# Inserting an element

fruits.insert(1, "Pineapple")

print("After insert:", fruits)


# Removing an element

fruits.remove("Banana")

print("After remove:", fruits)


# Changing an element

fruits[0] = "Watermelon"

print("After changing:", fruits)


# List length

print("Number of fruits:", len(fruits))


# Loop through list

print("\nFruits:")

for fruit in fruits:
    print(fruit)


# Sorting a list

numbers = [5, 2, 8, 1, 9, 3]

numbers.sort()

print("\nSorted numbers:", numbers)


# Reverse a list

numbers.reverse()

print("Reversed numbers:", numbers)

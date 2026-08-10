# Number Guessing Game

secret_number = 7
print("===== Number Guessing Game =====")
print("Guess a number between 1 and 10.")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Congratulations! You guessed the correct number.")

elif guess < secret_number:
    print("Your guess is too low.")

else:
    print("Your guess is too high.")

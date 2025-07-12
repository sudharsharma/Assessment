import random

def number_guess():
    print("Welcome to number guessing game")
    
    min_guess = 1
    max_guess = 100
    hidden_num = random.randint(min_guess, max_guess)
    max_attempts = 5
    attempts = 0

    print(f"Guess number between {min_guess} and {max_guess}")
    print(f"You have maximum 5")

    while attempts < max_attempts:
        guess_input = input(f"Attempts {attempts + 1}: Enter your guess:\t")

        if guess_input.isdigit():
            guess = int(guess_input)
        else:
            print("Plese enter the integer.")
            continue

        attempts += 1

        if guess < hidden_num:
            print("Too low. Try again\n")
        elif guess > hidden_num:
            print("Too high. Try again\n")
        else:
            print(f"Correct guess. You geeuessed the number {hidden_num} in {attempts} attempts.")
            break
    
    else:
        print(f"No guess left. The hidden number was {hidden_num}")

number_guess()
import random

n = int(input("Enter the number upto which you have to guess: "))
number_to_guess = random.randint(1,n)
guess = None
print("Welcome, To the Guessing Game")
while number_to_guess != guess:
  guess = int(input(f"Guess the number between 1 to {n}: "))
  if guess < number_to_guess:
    print("Your Guess is too low")
  elif guess > number_to_guess:
    print("Your Guess is too high")
  else:  # guess == number_to_guess
    print("You Guessed it right")

import random


def guess_the_number():
  """Plays the 'Guess the Number' game with the user."""
  number = random.randint(1, 100)  # Generate a random number between 1 and 100
  guesses_left = 7  # Allow 7 guesses
  print("I'm thinking of a number between 1 and 100.")
  while guesses_left > 0:
    try:
      guess = int(input(f"Take a guess ({guesses_left} guesses left): "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue
    if guess < number:
      print("Too low!")
    elif guess > number:
      print("Too high!")
    else:
      print(f"Congratulations! You guessed it in {7 - guesses_left} tries.")
      return
    guesses_left -= 1
  print(f"Sorry, you ran out of guesses. The number was {number}.")


if __name__ == "__main__":
  guess_the_number()

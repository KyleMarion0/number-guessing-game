import random

user_attempts_easy = 10
user_attempts_hard = 5

#Create a function for difficulty.
def set_difficulty():
  easy_or_hard = input('Choose a difficulty. Type "easy" or "hard": ')
  easy_or_hard.lower()
  if easy_or_hard == 'easy':
    return user_attempts_easy
  elif easy_or_hard == 'hard':
    return user_attempts_hard

#Function to check the users guess.
def check_user_guess(user_guess, random_num, attempts):
  ''' Checks random number against user guess. Returns remaining attempts.'''
  if user_guess > random_num:
    print('Too high.')
    return attempts - 1
  elif user_guess < random_num:
    print('Too low.')
    return attempts - 1
  else:
    print(f'You got it! The answer was {random_num}.')

#Choosing a random number between 1 and 100.
random_num = random.randint(1, 100)

def game():
  #Welcome messages.
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100.")
  print(f"Pssst, cheater! The correct answer is {random_num}.")

  #Keep track of guesses remaining.
  tries_remaining = set_difficulty()
  user_guess = 0
  attempts = 0
  while user_guess != random_num:
    print(f'You have {tries_remaining} attempts remaining to guess the number.')
    user_guess = int(input("Make a guess: "))
    tries_remaining = check_user_guess(user_guess, random_num, tries_remaining)
    if tries_remaining == 0:
      print("You've run out of guesses, you lose.")
      return
    
game()

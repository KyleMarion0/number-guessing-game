import random

user_attempts = 0

def pick_random_num():
  random_num = random.randint(1, 100)
  return random_num

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, cheater! The correct answer is {pick_random_num()}.")

easy_or_hard = input('Choose a difficulty. Type "easy" or "hard": ')
if easy_or_hard == 'easy' or easy_or_hard == 'Easy':
  #Give the user 10 attempts
  user_attempts = 10
elif easy_or_hard == 'hard' or easy_or_hard == 'Hard':
  #Give the user 5 attempts
  user_attempts = 5
else:
  print('Invalid input.')

def easy_difficulty():
  while user_attempts > 0:
    user_guess = input("Make a guess: ")

import random

user_attempts_easy = 10
user_attempts_hard = 5

#Create a function for difficulty.
def set_difficulty():
  easy_or_hard = input('Choose a difficulty. Type "easy" or "hard": ')
  if easy_or_hard == 'easy':
    return user_attempts_easy
  elif easy_or_hard == 'hard':
    return user_attempts_hard

#Function to check the users guess.
def check_user_guess(user_guess, random_num):
  if user_guess > random_num:
    print('Too high.')
  elif user_guess < random_num:
    print('Too low.')
  else:
    print(f'You got it! The answer was {random_num}.')

#Choosing a random number between 1 and 100.
random_num = random.randint(1, 100)

#Welcome messages.
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, cheater! The correct answer is {random_num}.")

#Choose difficulty.
tries_remaining = set_difficulty()
print(f'You have {tries_remaining} attempts remaining to guess the number.')

#User guess.
user_guess = int(input("Make a guess: "))

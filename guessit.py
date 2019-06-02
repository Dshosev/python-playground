# This little script will ask you to guess a number that was randomly generated and give you some hints if you are off

import random

userAnswerIsWrong = True
numberToGuess = random.randint(1,100)
numberFromUser = None


print("Let's guess the Number...")

while userAnswerIsWrong:
  print('What do you think is the number?')
  numberFromUser = input('Your Answer: ')
  # Validate the user input and handle the exceptions
  try:
    numberFromUser = int(numberFromUser)
  except ValueError:
    print('Please enter an integer!')

  if numberFromUser == numberToGuess:
    print('That is the correct answer! Great!')
    break
  elif numberFromUser > numberToGuess:
    print('You are too high!')
  elif numberFromUser < numberToGuess:
    print('You are too low!')
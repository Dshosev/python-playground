# This litte script is spitting out some random numbers from 1 to 6
# After printing the number the user will be asked for retry or leave

import random

userWantsMore = 'Y'

while userWantsMore in ['Y', 'y', 'Yes', 'yes', 'YES']:
  print
  print('###################################')
  print
  print('The first Number is ' + str(random.randint(1,6)) + ' and the second Number is ' + str(random.randint(1,6)))
  print('Do you want to retry this?')
  userWantsMore = input('Your answer: ')

print
print('###################################')
print
print('Have a nice day!')
print
print('###################################')
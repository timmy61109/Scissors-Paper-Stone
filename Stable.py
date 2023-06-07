import random
score = 0
lives = 3
print('© 2023 Lucas Thiam')
while lives > 0:
  computer = random.randint(1,3)
  print('The computer has chosen.')
  userans = int(input('So now, choose: scissors, paper, or stone? 1 for scissors, 2 for paper, 3 for stone. '))
  if computer == 1:
    compans = ('scissors')
  elif computer == 2:
    compans = ('paper')
  else:
    compans = ('stone')
  print('The computer has chosen '+(compans)+' .')
  if userans == 1:
    user = ('scissors')
  elif userans == 2:
    user = ('paper')
  elif userans == 3:
    user = ('stone')
  else:
    print('Do not play a fool.')
    user = ('nothing')
  print('You have chosen '+(user)+'. ')
  if computer == 1:
    if userans == 1:
      print('You tied!')
    elif userans == 2:
      print('You lose!')
      lives = lives - 1
    elif userans == 3:
      score = score + 1
      print('You win!')
  elif computer == 2:
    if userans == 1:
      score = score + 1
      print('You win!')
    elif userans == 2:
      print('You tied!')
    elif userans == 3:
      print('You lose!')
      lives = lives - 1
  else:
    if userans == 1:
      print('You lose!')
      lives = lives - 1
    elif userans == 2:
      print('You win!')
      score = score + 1
    elif userans == 3:
      print('You tied!')
  print('Your score is '+(str(score))+' .')
  print('You have '+(str(lives)+' lives left.'))
print('Game Over!')
if score < 5:
  print("Don't blame it on yourself. Try harder!")
elif score < 10:
  print('You did ok! Not bad!')
else:
  print('You did very well! 99% people cannot even reach here')

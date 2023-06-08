
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install ipywidgets
import random
import ipywidgets as widgets
import time
from IPython.display import display, Javascript
display(Javascript('''
google.colab.widgets.installCustomManager('https://ssl.gstatic.com/colaboratory-static/widgets/colab-cdn-widget-manager/158219452c5c5bf9/manager.min.js');
'''))
score = 0
lives = 3
print('© 2023 Lucas Thiam')
while lives > 0:
  computer = random.randint(1,3)
  print('The computer has chosen.')
  print('Now, you have 5 seconds to choose.')
  scissors = 'Scissors'
  paper = 'Paper'
  stone = 'Stone'
  options = [scissors, paper, stone]
  dropdown = widgets.Dropdown(options=options)
  display(dropdown)
  time.sleep(5)
  def on_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
      global userans
      userans = change['new']
  dropdown.observe(on_change)
  print('Selected: '+userans)
  if computer == 1:
    compans = ('scissors')
  elif computer == 2:
    compans = ('paper')
  else:
    compans = ('stone')
  print('The computer has chosen '+(compans)+' .')
  if computer == 1:
    if userans == scissors:
      print('You tied!')
    elif userans == paper:
      print('You lose!')
      lives = lives - 1
    elif userans == stone:
      score = score + 1
      print('You win!')
  elif computer == 2:
    if userans == scissors:
      score = score + 1
      print('You win!')
    elif userans == paper:
      print('You tied!')
    elif userans == stone:
      print('You lose!')
      lives = lives - 1
  else:
    if userans == scissors:
      print('You lose!')
      lives = lives - 1
    elif userans == paper:
      print('You win!')
      score = score + 1
    elif userans == stone:
      print('You tied!')
  print('Your score is '+(str(score))+' .')
  print('You have '+(str(lives)+' lives left.'))
  print('---------------------------------------------------------------------------')
print('Game Over!')
if score < 5:
  print("Don't blame it on yourself. Try harder!")
elif score < 10:
  print('You did ok! Not bad!')
else:
  print('You did very well! 99% people cannot even reach here')

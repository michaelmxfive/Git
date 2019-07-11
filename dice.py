print('What is your name?')
name=input('> ')
print('Hello, '+name+'!')

import random

print('Rolling the dice...')
dice1=random.randint(1,6)
dice2=random.randint(1,6)
print('Die 1: '+str(dice1))
print('Die 2: '+str(dice2))

total = dice1 + dice2
print('Total value: '+str(total))

if total > 7:
    print(name+' won!')
else:
    print(name+' lost!')

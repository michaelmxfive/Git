print('What is your name?')
name=input('> ')
print('Hello, '+name+'!')

import random

print('Rolling the dice...')
dice1=random.randint(1,6)
dice2=random.randint(1,6)
dice3=random.randint(1,6)
print('Die 1: '+str(dice1))
print('Die 2: '+str(dice2))
print('Die 3: '+str(dice3)) #one more die

total = dice1 + dice2 + dice3
print('Total value: '+str(total))

#if three dice are equal, print message
if dice1==dice2 and dice2==dice3:
    print('The value of two dice are equal')


if total > 18:
    print(name+' won!')
else:
    print(name+' lost!')

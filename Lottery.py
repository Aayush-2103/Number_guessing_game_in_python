#lottery number
from random import randint
ll=int(input('Enter the lower limit of your range:- '))
ul=int(input('Enter the upper limit of your range:- '))
n=randint(ll,ul)
t=int(input('\n\nEnter number of times you wanna attempt:- '))

while t!=0:
    a=int(input('Enter any number between your provided range:- '))
    if a==n:
        print('Hurray! You did it champ\n')
        break

    elif a>n and a<=ul:
        print('You guessed it too high')
        t-=1
        print('Now you have', t, 'chances left.\n')

    elif a<n and a>=ll:
        print('You guessed it too low')
        t-=1
        print('Now you have', t, 'chances left.\n')

    else:
        print('Please enter within the range\n')
        t-=1
        print('Now you have', t, 'chances left.')

    
import random

die = [
    '''
    [¯¯¯]
    [ • ]
    [___]
    ''',
    '''
    [•¯¯]
    [   ]
    [__•]
    ''',
    '''
    [•¯¯]
    [ • ]
    [__•]
    ''',
    '''
    [•¯•]
    [   ]
    [•_•]
    ''',
    '''
    [•¯•]
    [ • ]
    [•_•]
    ''',
    '''
    [•¯•]
    [• •]
    [•_•]
    '''
]

response = input('do you want to roll a dice? y/n: ')

while response != "y" and response != "n":
    print("PLEASE SAY 'y' OR 'n'!!!")
    response = input('do you want to roll a dice? y/n: ')

if response == 'n':
    print('ok bye then')
else:
    num = random.randint(0,5)
    print(die[num])
    print('You got '+str(num+1)+'!')
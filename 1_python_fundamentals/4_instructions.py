# if instruction
if 1 == 1:
    print('It is true')
else:
    print('It is not true')

name = input('Enter your name: ')
if len(name) >= 3:
    print('Welcome, {}.'.format(name))
else:
    print('Incorrect name!')

name = input('Enter your language name: ')
if name == 'python':
    print('It is python!')
elif name == 'php':
    print('It is php!')
elif name == 'java':
    print('It is java!')
else:
    print('I do not know such a language :(')

a = 3
b = 5
if a == 3 or b == 4:
    print('condition fulfilled')

a = 123
if a:
    print('condition fulfilled')


# input
name = input('Yor name: ')
print('Hello, ' + name + '.')

# types conversion
# a = input('Number: ')
# a += 1                                    # string increment error
# print(a)
a = int(input('Enter a number: '))
a += 1
print(a)

# string formatting
pcs = 1000
price = 20
value = pcs * price
# s = 'Warehouse: ' + str(pcs) + ' pcs'
s = 'Warehouse: {} pieces with a total value of {} USD.'.format(pcs, value)
print(s)
from tkinter.messagebox import YES


shop_shelf = ['apple', 'orange', 'toy car', 'banana']
goods = len(shop_shelf)
basket = []

print('In our store: ')
for assortment in shop_shelf:
    print(assortment, end=', ')

watching_goods = 0
while watching_goods < goods:
    print('\nYou take it in your hand: {}'.format(shop_shelf[watching_goods]))
    decision = input('Do you want to put this product in the basket: ')
    if decision == 'YES':
        basket.append(shop_shelf[watching_goods])
        shop_shelf[watching_goods] = ''
    watching_goods += 1

print('In your basket: ')
for in_basket in basket:
    print(in_basket, end=', ')

print('\nIn our store: ')
for assortment in shop_shelf:
    if assortment == '':
        continue
    print(assortment, end=', ')
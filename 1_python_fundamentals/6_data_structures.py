# ==================================LIST==================================== #

# my_list = [1, 2, 3.5, 's', True]
# my_list[4] = 20
# print(my_list[4])

# my_list = [10, 20, 30, 40]
# for v in my_list:
#     print(v)
# my_list[4] = 50                           # error OUT OF RANGE
# my_list.append(60)
# my_list.append(50)
# my_list.append(35)
# print(my_list)

# my_list.reverse()
# print(my_list)

# my_list.sort()
# print(my_list)

# ==============================MORE ABOUT LIST=============================== #

my_list = [10, 20, 30, 40]
my_list2 = [50, 60]
main_list = my_list + my_list2 * 2

# print(my_list[0:2])
print(main_list)
print(len(main_list))
n = int(len(main_list) / 2)
if(len(main_list) % 2 == 0):
    print(main_list[n - 1])
else:
    print(main_list[n])

# if 10 in my_list:
#     print('10 is on my_list')
while True:
    num = int(input('Number to check (0 - EXIT): '))
    if num == 0:
        break
    elif num in main_list:
        print('{} is on the list'.format(num))
    else:
        print('{} is not on the list'.format(num))

# ==============================LIST COMPREHENSION============================== #

my_list = [v for v in range(10, 30) if v % 2 == 0]
print(my_list)

# ================================TUPLE================================ #

values = (1,2, 3, 'abc', True)
print(values)
for v in values:
    print(v)
print(values[2])
values[2] = 45

values = (1, 2, 3, 4, 5, 6, 7)
new_values = values[:3]
print(new_values)
print(2 in new_values)
print(new_values + (10, 20))
print(len(new_values + (10, 20)))

my_list = [10, 4, 5, 17, 7, 2, 5]
my_tuple = tuple(my_list)
print(my_tuple)
print(len(my_tuple))                    # length
print(max(my_tuple))                    # max value
print(min(my_tuple))                    # min value
print(sum(my_tuple))                    # sum of all values

a, b, c, d, e, f, g = my_tuple

# ================================DICTIONARY================================ #

options = {
    'env': 'production',
    'db': 'mysql',
    'version': 1.0,
    'show_errors': True
}
print(options)
options['version'] = 2.0
print(options['version'])

options['user'] = 'admin'
print(options)

del options['db']
print(options)
print(options.get('db'))

options.update({
    'user': 'admin',
    'app': 0,
    'version': 2.2
})
print(options)

for key in options:
    print(options[key])

print(options.values())
print(options.keys())

# ================================SET================================ #

a = set()
print(a)
print(type(a))

a = set([1, 2, 3, 4, 2, 4, 3])
print(a)

a = set([1, 2, 3, 4])
b = set([1, 3, 7, 9])
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(a.symmetric_difference(b))
# counter = 0

# while counter < 10:
#     counter += 1
#     if counter % 2 != 0:
#         continue
#     print(counter)

# while True:
#     num = int(input('Enter a number greater than 0: '))
#     if num > 0:
#         print('Your number: ', num)
#         break
#     else:
#         print('Incorrect number! Try again..')

# values = [1, 2, 3, 4, 5]
# for v in values:
#     # if v >= 4:
#         # break
#     if v % 2 == 0:
#         continue
#     print(v * 10)

values = []
for i in range(1, 50):
    # if i == 0:
    #     continue
    if i % 3 == 0:
        values.append(i)
print(values)
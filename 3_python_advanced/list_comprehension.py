# list1 = [10]*20
# print(list1)

# text = 'str'*7
# print(text)


# # list comprehension
# list_comp = [10 for i in range(10)]
# print(list_comp)

# list2 = [letter for letter in "Dawid"]
# print(list2)

# list3 = [int(num) for num in "0123456789"]
# print(list3)

# x, y = [int(num) for num in input("Add number to list: ").split()]
# print(f"x: {x}, y: {y}")

# dic = {x: x*x for x in range(10)}
# print(dic)

# list4 = [[x for x in range(3)] for y in range(10)]
# print(list4)

# list5 = [x.lower() for x in "Dawid"]
# print(list5)

# list6 = [x+y for x,y in ([2, 2], [3, 3])]
# print(list6)

# list7 = [x+y for x,y in ([a,a+1] for a in range(50))]
# print(list7)

even = [x*x for x in range(20) if x % 2 == 0]
print(even)

txt = "Dawid +48886000123"
list8 = [int(char) for char in txt if char.isdigit()]
print(list8)
# variables and values
a = 2
b = 4
c = a + b
print(a, b, c)

# elements
my_value = 100
print(my_value)

# int and float
a = 1
b = 4.5
print(a, b)
print(type(a))
print(type(b))

print(isinstance(a, int))
print(isinstance(b, int))

# arithmetic operations
a = 10
b = 4
c = a - b
d = a + b
e = a * b
f = a / b
m = a % b                           # modulo
k = a ** b                          # exponentiation (a to bth power)
print(m)
print(k)

# String in Py
prefix = 'kurs'
name = 'python'
print(prefix + ' - ' + name)                # concatenation (connection)

print(name[0])                              # index reference
print(name[1])
s = name[0: 2]
print(s)


text = 'concatenation'
print(len(text))
print(text[0:6])                            # snipping 
print(text[3:-3])
a = 'abc '
print(a * 10 + 'end')

#testing
s = 'siemai1'
print(s.islower())
print(s.isalpha())
print(s.isalnum())

print(s.find('i'))
print(s.find('h '))

print('b' in s)
print('b' not in s)
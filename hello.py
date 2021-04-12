# hello.py
food = "Python's favorite food is perl"
print(food)

food2 = 'test\ns \nis \ntest'
print(food2)

food3 = '''
test
a
is
none
'''
print(food3)
print("=" * 50)
print("My Programs")
print("=" * 50)
a = "Life is too short, You need Python"
print(a[0],a[1],a[2],a[3])
print(a[-1],a[-2],a[-3],a[-4])
print(a[0]+a[1]+a[2]+a[3])
print(a[0:3])
print("=" * 50)

b = "2021-04-12Rainy"
year = b[:4]
month = b[5:7]
date = b[:10]
weather = b[10:]
print("year: " + year)
print("month: " + month)
print(date)
print(weather)
print("=" * 50)

c = "Python"
print(c[1])

# error
# c[1] = 'i'
# print(c[1])

print(c[:1] + 'i' + c[2:])
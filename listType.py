#list
odd = [1, 2, 3, 7, 9]
print(odd)

a = []
a = list()
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is'] 
e = [1, 2, ['Life', 'is']]

print(b[0] + b[1])
print(c[0])
print(b[-1])
# 3
# Life
# 3

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])
# 1
# ['a', 'b', 'c']
# ['a', 'b', 'c']
# a
# b
# c

# 삼중 리스트에서 인덱싱
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0]) # 'Life'

# 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2]) # => [1, 2]

a = '12345'
print(a[0:2]) # => 12

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b) # => [1, 2]
print(c) # => [3, 4, 5]

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5]) # => [3, ['a', 'b', 'c'], 4]
print(a[3][:2]) # => ['a', 'b']

# 리스트 연산
# +
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # => [1, 2, 3, 4, 5, 6]

# *
a = [1, 2, 3]
print(a * 3) # => [1, 2, 3, 1, 2, 3, 1, 2, 3]

# len 길이
a = [1, 2, 3]
print(len(a)) # => 3

# str
a = [1, 2, 3]
# print(a[2] + 'hi') # => error
print(str(a[2]) + 'hi') # => 3hi

# list - modify
a = [1, 2, 3]
a[2] = 4
print(a) # => [1, 2, 4]

# list - del
a = [1, 2, 3]
del a[2]
print(a) # => [1, 2]

a = [1, 2, 3, 4, 5]
del a[2:]
print(a) # => [1, 2]

# list - append
a = [1, 2, 3]
a.append(4)
print(a) # => [1, 2, 3, 4]

a.append([5, 6])
print(a) # => [1, 2, 3, 4, [5, 6]]

# sort
a = [4, 1, 3, 2]
a.sort()
print(a) # => [1, 2, 3, 4]

a = ['a', 'c', 'b']
a.sort()
print(a) # => ['a', 'b', 'c']

# reverse
a = ['a', 'c', 'b']
a.reverse()
print(a) # => ['b', 'c', 'a']

# index
a = [1, 2, 3]
print(a.index(3)) # => 2
print(a.index(1)) # => 0
print(a.index(0)) # => error 

# insert
a = [1, 2, 3]
a.insert(0,4) # a[0] insert 4
print(a) # => [4, 1, 2, 3]

a.insert(3,5) # a[3] insert 5
print(a) # => [4, 1, 2, 5, 3]

# remove => remove(x)는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a) # => [1, 2, 1, 2, 3]
a.remove(3)
print(a)  # => [1, 2, 1, 2]

# pop() 리스트의 맨 마지막 요소를 꺼내오고 그 요소를 삭제
a = [1, 2, 3]
a.pop() # => 3
print(a) # => [1, 2]

# pop(x) 리스트의 x번째 요소를 꺼내오고 그 요소를 삭제
a = [1, 2, 3]
a.pop(1) # => 2
print(a) # => [1, 3]

# count(x) x가 몇개인지 조사
a = [1, 2, 3, 1]
a.count(1) # => 2

# extend(x) => extend(x)에서 x에는 리스트만 올수 있으며 a리스트에 x리스트를 추가
a = [1, 2, 3]
a.extend([4, 5])
print(a) # => [1, 2, 3, 4, 5]

b = [6, 7]
a.extend(b)
print(a) # => [1, 2, 3, 4, 5, 6, 7]

# a += [8, 9]  == a.extend([8, 9])
a += [8, 9] # => [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
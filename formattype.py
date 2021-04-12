# format 함수를 사용한 포매팅 
# 숫자
"I eat {0} apples".format(3)
# 문자
"I eat {0} apples".format("five")
# 숫자 의 변수
n = 3
"I eat {0} apples".format(n)

d = "there"
"I eat {0} apples. so I was sick {1} days".format(n, d)

"I eat {n} apples. so I was sick {d} days".format(n=10, d=3)

"I eat {0} apples. so I was sick {d} days".format(10, d="three")

# left align => 'hi        '
"{0:<10}".format("hi")

# right align => '        hi'
"{0:>10}".format("hi")

# center align = > '    hi    '
"{0:^10}".format("hi")

# fill the blank => '====hi===='
"{0:=^10}".format("hi")

# fill the blank => '!!!!hi!!!!'
"{0:!^10}" .format("hi")

# 소수점 => '3.4213'
y = 3.42134234
"{0:0.4f}".format(y)

# 소수점 => '    3.4213'
"{0:10.4f}".format(y)

# {{ }} => '{ and }'
"{{ and }}".format()

## 문자열 포매팅 : 파이썬 3.6버전부터 사용. f접두사를 붙여 사용
name = "Hong"
age = 30
f'I am is {name}. My age is {age}.'
f'I am is {name}. My age is {age+1}.'

d = {'name':'Park','age':30}
f'I am is {d["name"]}, My age is {d["age"]}.'

# align
f'{"hi":<10}' # => 'hi        '
f'{"hi":>10}' # => '        hi'
f'{"hi":^10}' # => '    hi    '

# fill the blank
f'{"hi":=^10}' # => '====hi===='
f'{"hi":!<10}' # => 'hi!!!!!!!!'

# 소수점
y = 3.42134234
f'{y:0.4f}' # => '3.4213'
f'{y:10.4f}' # => '    3.4213'

# {{ }}
f'{{ and }}' # => '{ and }'
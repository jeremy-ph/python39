# 문자열 포매팅

# %d 정수(숫자)
"I eat %d apple." %3

number = 4
"I eat %d apple." % number

# %c 문자 1개
"I eat %c apple." % "o"

# %s 문자열
"I eat %s apple." % "five"

# %f 부동소수(Floating-point)
# %o 8진수
# %x 16진수

# ex
n = 10
d = "three"
"I ate %d apple. so I was sick for %s days." %(n, d)

# ex
"I have %s apples" %3
"rate is %s " %3.14

# error
# "Error is %d%." %98

# correct
"Error is %d%%." %98 

# right align
#'        hi'
"%10s" % "hi"

#'hi        jane'
"%-10sjane" % 'hi'

#소수점 4번째 자리까지만 표시 => '3.1421'
"%0.4f" % 3.14214534

#소수점 4번째 자리까지만 표시하고,
#전체 길이가 10개인 문자열 공간에서 오른쪽 정렬하는 예 => '    3.4213'
"%10.4f" % 3.421341234

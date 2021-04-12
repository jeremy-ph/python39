# count 
a = "hobby"
a.count('b') # => 2

# location 1
a = "Python is the best choice"
a.find('b') # => 14
a.find('k') # does not exist => -1

# location 2
a = "Life is too short"
a.index('t')
a.index('k') # error

# join
",".join('abcd') # => 'a,b,c,d'
",".join(['a','b','c','d']) # => 'a,b,c,d'

#lower => 'hi'
a = "HI"
a.lower() 

#lstrip: remove the left blank => 'hi '
a = " hi "
a.lstrip()

#rstrip: remove the right blank => ' hi'
a = " hi "
a.rstrip()

# replace => 'Your leg is too short'
a = "Life is too short"
a.replace("Life", "Your leg")

#split => ['Life', 'is', 'too', 'short']
a = "Life is too short"
a.split()

b = "a:b:c:d"
b.split(":")
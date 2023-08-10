name = 'imran saeed'
print('Count of character \'a\': ', name.count('a'))
print('Split the string in words (separated by space characters)', name.split(sep=' '))
print('Capitalize the first character', name.capitalize())
print('Capitalize all characters', name.upper())
print(name.center(30, '-'))
print(name.index('saeed'))
print(name.title())
print(name[:])
print(name[2:])
print(name[:2])
print(name[3:7])

# 01234567890
# imran saeed
#  - - - -
# the range is 1-9 and skips one character
# print 'ma a'
print(name[1:9:2])

# reverse the string
print(name[::-1])

name = ' imran saeed '
print(name.rstrip())
print(name.lstrip())
print(name.strip())

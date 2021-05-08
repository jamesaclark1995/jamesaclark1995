# This is inspired by a Codecademy exercise. The exercise printed off a list
# of fruit which put "A" in front of fruit beginning with vowels instead of
# "An". This code changes this so it is more grammatically correct.
# (Created with Python 2)

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'

for f in fruits:
    if f[0] == 'a' or f[0] == 'e' or f[0] == 'i' or f[0] == 'o' or f[0] == 'u':
        print 'An', f
    else:
        print 'A', f

# The Spelling Bee Kid is a genius and can spell any word

word = raw_input('Suggest a word for our Spelling Bee Kid to spell: ')
# This creates a string

letters = []

for letter in word:
    letters.append(letter.upper())
    # This adds each letter of the string 'word' to the list 'letters'
    # This will also capitalise the letters you entered in 'word'

spelling = '-'.join(letters)
# e.g. CAT becomes C-A-T

print 'Spelling Bee Kid: "' + spelling + '...' + word + '!"'

# This is an example of what will be printed to the console:

# Suggest a word for our Spelling Bee Kid to spell: cat
# Spelling Bee Kid: "C-A-T...cat!"

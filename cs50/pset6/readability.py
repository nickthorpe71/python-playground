
text = raw_input("Text: ")

letters = 0
sentences = 0
words = 0

for letter in text:
    if letter.isalpha():
        letters += 1
    if letter.isspace():
        words += 1
    if letter in ['?', '.', '!']:
        sentences += 1

words += 1

L = (letters * 100.0) / words
S = (sentences * 100.0) / words

result = int(round(0.0588 * L - 0.296 * S - 15.8))
if result < 1:
    print('Before Grade 1')
elif result >= 16:
    print('Grade 16+')
else:
    print("Grade " + str(result))




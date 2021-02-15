with open('myfile','r', encoding='utf-8') as reader:
    text = reader.readlines()

print('Lines in file: ',len(text))

for j, i in enumerate(text, start = 1):
    print('Line',j,'contents',len(i.split(' ')),'words.')

# Lines in file:  4
# Line 1 contents 6 words.
# Line 2 contents 5 words.
# Line 3 contents 6 words.
# Line 4 contents 4 words.

# Я не токарь, я не пекарь.
# Я не повар, не доцент.
# Я не дворник и не слесарь,
# Я простой советский мент.

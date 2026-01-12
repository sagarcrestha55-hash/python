# Day 4 Exercises

# 1
s1 = 'Thirty'
s2 = 'Days'
s3 = 'Of'
s4 = 'Python'
print(s1 + ' ' + s2 + ' ' + s3 + ' ' + s4)

# 2
print('Coding' + ' ' + 'For' + ' ' + 'All')

# 3
company = 'Coding For All'

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company[7:])

# 10
print(company.find('Coding'))
print(company.index('Coding'))

# 11
print(company.replace('Coding', 'Python'))

# 12
print('Python for Everyone'.replace('Everyone', 'All'))

# 13
print(company.split(' '))

# 14
techs = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(techs.split(', '))

# 15
print(company[0])

# 16
print(len(company) - 1)

# 17
print(company[10])

# 18
pfe = 'Python For Everyone'
print(''.join(word[0] for word in pfe.split()))

# 19
cfa = 'Coding For All'
print(''.join(word[0] for word in cfa.split()))

# 20
print(company.index('C'))

# 21
print(company.index('F'))

# 22
people = 'Coding For All People'
print(people.rfind('l'))

# 23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 24
print(sentence.rindex('because'))

# 25
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])

# 26
print(company.startswith('Coding'))

# 27
print(company.endswith('coding'))

# 28
spaced = '   Coding For All      '
print(spaced.strip())

# 29
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 30
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libs))

# 31
print('I am enjoying this challenge.\nI just wonder what is next.')

# 32
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# 33
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')

# 34
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

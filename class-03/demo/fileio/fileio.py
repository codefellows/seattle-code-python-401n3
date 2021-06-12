# spam = open('assets/spam.txt', 'r')
# print('Is file closed', spam.closed)

# contents = spam.read()

# print(contents)q

# for char in contents:
#     print(char)

# print('Is file closed', spam.closed)
# spam.close()
# print('Is file closed', spam.closed)

# help(spam)

# print(dir(spam))

# with open('assets/spam.txt', 'r') as spam:
#     content = spam.read()

# print('Is file closed', spam.closed)
# print(content)

with open('assets/brain.jpg', 'rb') as file:
    content = file.read()

# for x in content:
#     print(type(x))

with open('assets/brain.copy.jpg', 'wb') as file2:
    file2.write(content)
    
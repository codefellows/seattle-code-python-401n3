from faker import Faker

fake = Faker('en_US')

# print(fake)

# print(dir(fake))
# print(fake.name())
# print(fake.first_name_female())
# print(fake.word())
# print(fake.words(1000))
# print(fake.sentence())
# print(fake.sentences())
# print(fake.paragraph(20))
# print(fake.paragraphs(20))
# for i in range(100):
#     print(fake.email())

# print(fake.phone_number())

content = ''

for i in range(100):
    content += fake.paragraph(2)
    content += fake.email()
    content += fake.paragraph()
    content += fake.phone_number()
    content += fake.paragraph()
    content += '\n'
# print(content)

with open('assets/notes.txt', 'w+') as file:
    file.write(content)

import shutil

shutil.move('assets/notes.txt', '.')

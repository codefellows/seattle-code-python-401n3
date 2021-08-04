import nltk
# Need to add via poetry

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()
# print(word_list)
# print(name_list)
# sdfj sdfp oijasf wperj weksdfp asdf ppidfm the sdf pasldfnasd is sdmfpoi we

string = 'ok'
word_count = 0
if string in word_list or string in name_list:
    word_count += 1
else:
    print('I am not here')


import nltk

example = ['Mary had a little lamb' , 'Jack went up the hill' , 'Jill followed soon after']

tokenized_sents = [nltk.word_tokenize(i) for i in example]
for i in tokenized_sents:
    print(i)


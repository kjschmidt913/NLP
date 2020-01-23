import nltk

SOS_token = 0
EOS_token = 1


class Vocabulary:

    def __init__(self, name):
        self.name = name
        self.word2index = {}
        self.word2count = {}
        self.index2word = {SOS_token: "SOS", EOS_token: "EOS"}
        self.num_words = 2
        self.num_sentences = 0

    def add_word(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.num_words
            self.word2count[word] = 1
            self.index2word[self.num_words] = word
            self.num_words += 1
        else:
            self.word2count[word] += 1

    def add_sentence(self, sentence):
        sentence_len = 0
        for word in sentence.split(' '):
            sentence_len += 1
            self.add_word(word)
        self.num_sentences += 1

    def to_word(self, index):
        return self.index2word[index]

    def to_index(self, word):
        return self.word2index[word]



# tokenized_sents = [nltk.word_tokenize(i) for i in example]
# for i in tokenized_sents:
#     print(i)

voc = Vocabulary('Train')

with open('group3_train.txt') as f:
    corpora = [word for line in f for word in line.split()]

for words in corpora:
    voc.add_word(words)

print(voc.index2word)
for word in range(voc.num_words):
    print(word," ",voc.to_word(word))


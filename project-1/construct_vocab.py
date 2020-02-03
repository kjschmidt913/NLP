import nltk
import pickle
import re


class Vocabulary:

    def __init__(self, name):
        self.name = name
        self.word2index = {}
        self.word2count = {}
        self.index2word = {}
        self.num_words = 0
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


voc = Vocabulary('Train')

with open('group3_train.txt') as f:
    corpora = [word for line in f for word in line.split()]

for words in corpora:
    tokenized_words = nltk.word_tokenize(words)
    for i in tokenized_words:
        voc.add_word(i)

train_vocab_list=[]
for word in range(voc.num_words):
    train_vocab_list.append(voc.to_word(word))
# print("train voc",len(train_vocab_list))

# print("Train freq", sum(voc.word2count.values()))

pickle_out = open("Final.pickle","wb")

pickle.dump(train_vocab_list, pickle_out)
pickle.dump(voc.word2index, pickle_out)

out_of_vocab = []
for i in voc.word2count:
    if voc.word2count[i] < 3:
        out_of_vocab.append(i)
print(len(train_vocab_list))

print(len(out_of_vocab))

# # Test <unk>
with open('group3_test.txt', 'r') as file :
  test_corpora = file.read()

word_replace = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, out_of_vocab)))
test_replaced = word_replace.sub("<unk>", test_corpora)

print(test_replaced)
with open('group3_test.txt', 'w') as file:
  file.write(test_replaced)

voc_test = Vocabulary('Test')

with open('group3_test.txt') as f:
    corpora_test = [word for line in f for word in line.split()]

for words in corpora_test:
    tokenized_words = nltk.word_tokenize(words)
    for i in tokenized_words:
        voc_test.add_word(i)

test_vocab_list=[]
for word in range(voc_test.num_words):
    test_vocab_list.append(voc_test.to_word(word))

print("test voc",len(test_vocab_list))
pickle.dump(test_vocab_list, pickle_out)

# Validation <unk>
with open('group3_valid.txt', 'r') as file :
  valid_corpora = file.read()


word_replace_valid = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, out_of_vocab)))
valid_replace = word_replace_valid.sub("<unk>", valid_corpora)


with open('group3_valid.txt', 'w') as file:
  file.write(valid_replace)

voc_valid = Vocabulary('Validation')

with open('group3_valid.txt') as f:
    corpora_valid = [word for line in f for word in line.split()]

for words in corpora_valid:
    tokenized_words = nltk.word_tokenize(words)
    for i in tokenized_words:
        voc_valid.add_word(i)

valid_vocab_list = []
for word in range(voc_valid.num_words):
    valid_vocab_list.append(voc_valid.to_word(word))
print("valid voc",len(valid_vocab_list))
pickle.dump(valid_vocab_list, pickle_out)

pickle_out.close()


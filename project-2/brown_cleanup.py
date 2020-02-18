from nltk import tokenize
import nltk
import re
import pickle
#nltk.download('punkt')

#remove quotes resulting from <p> elements of text scraping
fin = open("brown_tokenized.txt", "rt")
fout = open("out.txt", "wt")

for line in fin:
	fout.write(line.replace('``', '<quote>'))

fin.close()
fout.close()

fin = open("out.txt", "rt")
fout = open("out1.txt", "wt")

for line in fin:
	fout.write(line.replace('\'\'', '<quote>'))

fin.close()
fout.close()
#replace all the punctuations except .?!,:; with @-@
original_string = open('out1.txt').read()
new_string = re.sub('[ ](?=[ ])|[^-_,A-Za-z0-9 .?!,:;<>]+', ' @-@ ', original_string)
open('out.txt', 'w').write(new_string)

#add spaces between sentences which don't have a space between period and capital word due to the fetching pattern
fin = open("out.txt", "rt")
fout = open("out1.txt", "wt")
for line in fin:
    fout.write(re.sub('([.])([A-Z])', r'\1 \2', line))
fin.close()
fout.close()

#tokenise and add <s> </s> tags
fin = open("out1.txt", "rt")
fout = open("out_final.txt", "wt")
for line in fin:
    y = tokenize.sent_tokenize(line)

for line in y:
    fout.write('<s> ')
    fout.write(line)
    fout.write(' </s> ')
fin.close()
fout.close()

num_words = 0
num_lines = 0

with open("out_final.txt", 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

print("Number of total tokens",num_words)

num_words = 0
num_lines = 0


#dividing the corpus in three file
ftr = open("brown_train.txt", "wt")
fts = open("brown_test.txt", "wt")
fv = open("brown_valid.txt", "wt")



with open("out_final.txt", "rt") as f:
    data = f.read().split()

tr = round(0.8*len(data))
ts = round(0.9*len(data))

train_data = data[:tr]
test_data = data[tr+1:ts]
valid_data = data[ts+1:]

for line in train_data:
    ftr.write(line + ' ')

for line in test_data:
    fts.write(line + ' ')

for line in valid_data:
    fv.write(line + ' ')

ftr.close()
fts.close()
fv.close()

with open("out_final.txt", 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

print("Number of total tokens",num_words)

num_words = 0
with open("brown_train.txt", 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

print("Number of total tokens for train",num_words)

num_words = 0
with open("brown_test.txt", 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

print("Number of total tokens for test",num_words)

num_words = 0
with open("brown_valid.txt", 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

print("Number of total tokens for valid",num_words)

########################
#adding <unk> tags

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

with open('out_final.txt') as f:
    corpora = [word for line in f for word in line.split()]

for words in corpora:
    tokenized_words = nltk.word_tokenize(words)
    for i in tokenized_words:
        voc.add_word(i)

train_vocab_list=[]
for word in range(voc.num_words):
    train_vocab_list.append(voc.to_word(word))

out_of_vocab = []
for i in voc.word2count:
    if voc.word2count[i] < 3:
        out_of_vocab.append(i)
print(len(train_vocab_list))

print(len(out_of_vocab))

# # Test <unk>
with open('brown_test.txt', 'r') as file :
  test_corpora = file.read()

word_replace = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, out_of_vocab)))
test_replaced = word_replace.sub("<unk>", test_corpora)

print(test_replaced)
with open('brown_test.txt', 'w') as file:
  file.write(test_replaced)

voc_test = Vocabulary('Test')

with open('brown_test.txt') as f:
    corpora_test = [word for line in f for word in line.split()]

for words in corpora_test:
    tokenized_words = nltk.word_tokenize(words)
    for i in tokenized_words:
        voc_test.add_word(i)

test_vocab_list=[]
for word in range(voc_test.num_words):
    test_vocab_list.append(voc_test.to_word(word))

print("test voc",len(test_vocab_list))

# Validation <unk>
with open('brown_valid.txt', 'r') as file :
  valid_corpora = file.read()

word_replace_valid = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, out_of_vocab)))
valid_replace = word_replace_valid.sub("<unk>", valid_corpora)


with open('brown_valid.txt', 'w') as file:
  file.write(valid_replace)

voc_valid = Vocabulary('Validation')

with open('brown_valid.txt') as f:
    corpora_valid = [word for line in f for word in line.split()]



############
#doc tagging

def doc_tagging (textfile, train_test_valid):

    # This is solely for testing. Remove once using real corpus
    # stringthing = "Hello welcome to the world of to learn Categorizing and POS Tagging with NLTK and Python this should be a yeah 1992 and this a cardinal number 0.4"
    # text = nltk.word_tokenize(stringthing)

    file_content = open(textfile).read()
    text = nltk.word_tokenize(file_content)

    patterns = [
        (r'^(19|20)\d\d$', 'YY'),  # years
        (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
        (r'(The|the|A|a|An|an)$', 'AT'),   # articles
        (r'.*able$', 'JJ'),                # adjectives
        (r'.*ly$', 'RB'),                  # adverbs
        (r'(He|he|She|she|It|it|I|me|Me|You|you)$', 'PRP'), # pronouns
        (r'(His|his|Her|her|Its|its)$', 'PRP$'),    # possesive
        (r'(my|Your|your|Yours|yours)$', 'PRP$'),   # possesive
        # WARNING : Put the default value in the end
        (r'.*', 'NN')                      # nouns (default)
        ]


    # giving the tagger our patterns for the tags
    regexp_tagger = nltk.RegexpTagger(patterns)

    # tag our document
    tags = regexp_tagger.tag(text)
    ctr1 = 0
    ctr2 = 0
    ctr3 = 0
    ctr4 = 0

    # replace the words with their tags
    new_tokens = []
    for word, tag in tags:
        if tag == "JJ":
            ctr1+=1
            new_tokens.append("<ADJECTIVE>")
        elif tag == "CD":
            ctr2+=1
            new_tokens.append("<NUMBER>")
        elif tag == "YY":
            ctr3+=1
            new_tokens.append("<YEAR>")
        elif tag == "PRP":
            ctr4+=1
            new_tokens.append("<PRONOUN>")
        else:
            new_tokens.append(word)

        if (word != '<' and word != '/s' and word != 's' and word != '@' and word != '-'):
            new_tokens.append(" ")

    #writing the tagged content to a text file
    filename = "brown_"+train_test_valid+".txt"
    fff = open(filename, "wt")
    for xf in new_tokens:
        fff.write(xf)
    fff.close()

    voc = Vocabulary(train_test_valid)

    for sent in new_tokens:
        voc.add_sentence(sent)

    tagged_vocab = []

    for word in range(voc.num_words):
        tagged_vocab.append(voc.to_word(word))


    print("Vocab Count for ", train_test_valid,": ", len(tagged_vocab))


doc_tagging("brown_test.txt", "Test")
doc_tagging("brown_train.txt", "Train")
doc_tagging("brown_valid.txt", "Validation")

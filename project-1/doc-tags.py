import nltk



# TODO:
# 1. uncomment the actual corpus and remove dummy corpus
# 2. Do stats for patterns - import Vocabulary class once Nayan merges her branch

def doc_tagging (textfile, type):

    # This is solely for testing. Remove once using real corpus
    stringthing = "Hello welcome to the world of to learn Categorizing and POS Tagging with NLTK and Python this should be a yeah 1992 and this a cardinal number 0.4"
    text = nltk.word_tokenize(stringthing)

    # file_content = open(textfile).read()
    # text = nltk.word_tokenize(file_content)

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

    # replace the words with their tags
    new_tokens = []
    for word, tag in tags:
        if tag == "JJ":
            new_tokens.append("<ADJECTIVE>")
        elif tag == "CD":
            new_tokens.append("<NUMBER>")
        elif tag == "YY":
            new_tokens.append("<YEAR>")
        elif tag == "PRP":
            new_tokens.append("<PRONOUN>")
        else:
            new_tokens.append(word)

    print(new_tokens)

    voc = Vocabulary(type)

    for sent in new_tokens:
        voc.add_sentence(sent)

    print(voc.index2word)
    for word in range(voc.num_words):
        print(word," ",voc.to_word(word))

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




# UNCOMMENT TO USE ACTUAL CORPUS
# doc_tagging("group3_test.txt")
# doc_tagging("group3_train.txt")
# doc_tagging("group3_valid.txt")

doc_tagging("hi", "Train")



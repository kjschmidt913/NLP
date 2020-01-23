import nltk
from construct_vocab import Vocabulary
import pickle

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
    filename = "tagged-group3-"+train_test_valid+".txt"
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

    f = open("Final.pickle", "ab")
    pickle.dump(tagged_vocab, f)
    f.close()


    print(ctr1,ctr2,ctr3,ctr4,"number of tokens respectively for adj, number, year, pronoun for ", train_test_valid, " set." )

doc_tagging("group3_test.txt", "Test")
doc_tagging("group3_train.txt", "Train")
doc_tagging("group3_valid.txt", "Validation")

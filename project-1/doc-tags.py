import nltk
from construct_vocab import Vocabulary


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

    # print(new_tokens) 

    voc = Vocabulary(train_test_valid)

    for sent in new_tokens:
        voc.add_sentence(sent)

    print(voc.index2word)

    tagged_vocab = []

    vocab_count = 0
    for word in range(voc.num_words):
        vocab_count += 1
        tagged_vocab.append(word," ",voc.to_word(word))

    # print("Vocab Count for ", train_test_valid,": ", vocab_count)
    # print("Token Count ", train_test_valid, ": ", len(new_tokens))

    f = open("pickle-file.pkl", "a+")
    pickle_file_name = "vocab-tagged-" + train_test_valid
    pickle.dump(pickle_file_name, f)
    f.close()




# UNCOMMENT TO USE ACTUAL CORPUS
doc_tagging("group3_test.txt", "Test")
doc_tagging("group3_train.txt", "Train")
doc_tagging("group3_valid.txt", "Validation")

# doc_tagging("hi", "Train")



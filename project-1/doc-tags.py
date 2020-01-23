import nltk


# TODO:
# 1. uncomment the actual corpus and remove dummy corpus
# 2. Do stats for patterns - import Vocabulary class once Nayan merges her branch


# This is solely for testing. Remove once using real corpus
stringthing = "Hello welcome to the world of to learn Categorizing and POS Tagging with NLTK and Python this should be a yeah 1992 and this a cardinal number 0.4"
text = nltk.word_tokenize(stringthing)


# UNCOMMENT TO USE ACTUAL CORPUS
# file_content = open("raw_text.txt").read()
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

# tags is a list of tuples, we need lists
list_of_pairs = []
for word, tag in tags:
    list_of_pairs.append([word, tag])

# replace the words with their tags
new_tokens = []
for word, tag in list_of_pairs:
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


tr = 7000000
ts = 7700000

train = new_tokens[:tr]
test = new_tokens[tr+1:ts]
validation = new_tokens[ts+1:]






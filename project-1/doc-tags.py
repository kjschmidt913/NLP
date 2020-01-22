import nltk
nltk.download('punkt')
from nltk import tokenize
nltk.download('averaged_perceptron_tagger')

text = tokenize.word_tokenize("Hello welcome to the world of to learn Categorizing and POS Tagging with NLTK and Python this should be a yeah 1992 and this a cardinal number 0.4")

# nltk.pos_tag(text)

# TODO:
# 1. Open the tokenized file
# 2. Copy the tockenized file
# 3. Only use the copy for everything in this file

patterns = [
    (r'.*ing$', 'VBG'),               # gerunds
    (r'.*ed$', 'VBD'),                # simple past
    (r'.*es$', 'VBZ'),                # 3rd singular present
    (r'.*ould$', 'MD'),               # modals
    (r'.*\'s$', 'NN$'),               # possessive nouns
    (r'.*s$', 'NNS'),                 # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'^-?[0-9]+([0-9]+)?+([0-9]+)?+([0-9]+)?$', 'YY'),  # years
    (r'(The|the|A|a|An|an)$', 'AT'),   # articles 
    (r'.*able$', 'JJ'),                # adjectives 
    (r'.*ness$', 'NN'),                # nouns formed from adjectives
    (r'.*ly$', 'RB'),                  # adverbs
    (r'(He|he|She|she|It|it|I|me|Me|You|you)$', 'PRP'), # pronouns
    (r'(His|his|Her|her|Its|its)$', 'PRP$'),    # possesive
    (r'(my|Your|your|Yours|yours)$', 'PRP$'),   # possesive
    (r'(on|On|in|In|at|At|since|Since)$', 'IN'),# time prepopsitions
    (r'(for|For|ago|Ago|before|Before)$', 'IN'),# time prepopsitions
    (r'(till|Till|until|Until)$', 'IN'),        # time prepopsitions
    (r'(by|By|beside|Beside)$', 'IN'),          # space prepopsitions
    (r'(under|Under|below|Below)$', 'IN'),      # space prepopsitions
    (r'(over|Over|above|Above)$', 'IN'),        # space prepopsitions
    (r'(across|Across|through|Through)$', 'IN'),# space prepopsitions
    (r'(into|Into|towards|Towards)$', 'IN'),    # space prepopsitions
    (r'(onto|Onto|from|From)$', 'IN'),          # space prepopsitions    
    (r'\.$','.'), (r'\,$',','), (r'\?$','?'),    # fullstop, comma, Qmark
    (r'\($','('), (r'\)$',')'),             # round brackets
    (r'\[$','['), (r'\]$',']'),             # square brackets
    (r'(Sam)$', 'NAM'),
    # WARNING : Put the default value in the end
    (r'.*', 'NN')                      # nouns (default)
    ]


# method to tag the doc
regexp_tagger = nltk.RegexpTagger(patterns)

# tag our document
tags = regexp_tagger.tag(text)

print(tags)

# if word.tagmethod.tag == 'NN' word = "<noun>"
for word, tag in tags:
    if tag == "JJ":
        word = "<ADJECTIVE>"
    if tag == "CD":
        word = "<NUMBER>"
    if tag == "YY":
        word = "<YEAR>"
    if tag == "PRP":
        word = "<PRONOUN>"


print(tags)



import nltk
import re
import pprint
from nltk import word_tokenize

# open the text file
document = open("raw_text.txt", "r")


patterns = [
    (r'.*ing$', 'VBG'),                # gerunds
    (r'.*ed$', 'VBD'),                 # simple past
    (r'.*es$', 'VBZ'),                 # 3rd singular present
    (r'.*ould$', 'MD'),                # modals
    (r'.*\'s$', 'NN$'),                # possessive nouns
    (r'.*s$', 'NNS'),                  # plural nouns
    (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN'),                      # nouns (default)
    (r'^-?[0-9]+(\.[0-9]+)+(\.[0-9]+)+(\.[0-9]+)?$', 'YY') # year (default)
]

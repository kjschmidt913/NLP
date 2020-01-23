# Project-1
This is a web crawler that uses the [New York Times API](https://developer.nytimes.com/) to create a corpus.
## Getting Started
This uses a Python wrapper for the New York Times API called [NYTimesArticleAPI](https://github.com/MattDMo/NYTimesArticleAPI).

Currently, the Pip install command is broken, so we have manually imported the package for you. Plans to fork the wrapper repo and host the updated package on PyPi are underway, stay tuned. 

Install NLTK package using pip or conda
```
pip install nltk
conda install nltk
```
Install BeautifulSoup4 and other libraries to be able to scrape and clean the data
```
pip install beautifulsoup4
pip install requests
```
## Steps to run
1. nytimes.py
2. nytimes_foreign_relations.py
3. cleanup.py
4. construct_vocab.py
5. doc-tags.py

raw_text.txt is the main corpus without tags.
group3_train.txt, group3_test.txt, group3_valid.txt are splitted corpora files.
Final.pickle file has Vocab list, Vocab Dict, untagged_train_vocab_list, untagged_test_vocab_list, untagged_valid_vocab_list, tagged_train_vocab_list, tagged_test_vocab_list and tagged_valid_vocab_list in order.

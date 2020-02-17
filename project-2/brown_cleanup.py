from nltk import tokenize
import nltk
import re
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

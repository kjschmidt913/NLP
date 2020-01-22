from nltk import tokenize
import nltk
import re
nltk.download('punkt')

#remove quotes resulting from <p> elements of text scraping
fin = open("raw_text.txt", "rt")
fout = open("out.txt", "wt")

for line in fin:
	fout.write(line.replace('\'\'', ''))

fin.close()
fout.close()

#replace all the punctuations except .?!,:; with @-@
original_string = open('out.txt').read()
new_string = re.sub('[ ](?=[ ])|[^-_,A-Za-z0-9 .?!,:;]+', '@-@', original_string)
open('out2.txt', 'w').write(new_string)

#add spaces between sentences which don't have a space between period and capital word due to the fetching pattern
fin = open("out2.txt", "rt")
fout = open("out.txt", "wt")
for line in fin:
    fout.write(re.sub('([.])([A-Z])', r'\1 \2', line))
fin.close()
fout.close()

#tokenise and add <s> </s> tags
fin = open("out.txt", "rt")
fout = open("out2.txt", "wt")
for line in fin:
    y = tokenize.sent_tokenize(line)

for line in y:
    fout.write('<s> ')
    fout.write(line)
    fout.write(' </s> ')
fin.close()
fout.close()

#remove double hyphens with
fin = open("out2.txt", "rt")
fout = open("out_final.txt", "wt")

for line in fin:
    fout.write(line.replace('--', ''))
fin.close()
fout.close()

#final output file to consider is out_final.txt

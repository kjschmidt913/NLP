fin = open("raw_text.txt", "rt")
fout = open("out.txt", "wt")

for line in fin:
	fout.write(line.replace('\'\'', ' '))

fin.close()
fout.close()

import re
original_string = open('out.txt').read()
new_string = re.sub('[ ](?=[ ])|[^-_,A-Za-z0-9 .]+', '@-@', original_string)
open('out2.txt', 'w').write(new_string)

fin = open("out2.txt", "rt")
fout = open("out3.txt", "wt")

for line in fin:
    fout.write(line.replace('. ', '</s> <s>'))

fin.close()
fout.close()


#would be great to find a better of doing it without multiple files

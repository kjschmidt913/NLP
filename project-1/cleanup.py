fin = open("raw_text.txt", "rt")
fout = open("out.txt", "wt")

for line in fin:
	fout.write(line.replace('\'\'', ' '))

fin.close()
fout.close()

fin = open("out.txt", "rt")
fout = open("out2.txt", "wt")

for line in fin:
    fout.write(line.replace('. ', '</s>. <s>'))

fin.close()
fout.close()

#would be great to find a better of doing it without multiple files

file = open("/Users/nayanmehta/Desktop/Github Repo/NLP/project-1/group3_train_final.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in train file :', len(words))


file = open("/Users/nayanmehta/Desktop/Github Repo/NLP/project-1/group3_test_final.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in test file :', len(words))

file = open("/Users/nayanmehta/Desktop/Github Repo/NLP/project-1/group3_valid_final.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in valid file :', len(words))

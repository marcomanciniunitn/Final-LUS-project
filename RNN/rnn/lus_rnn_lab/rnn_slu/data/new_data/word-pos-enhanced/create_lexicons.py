import os 

def createWordDict(fileName, testFile):
	trainFile = open(fileName, "r")
	testFile = open(testFile, "r")
	wordFile = open("word_dict.txt","w")
	conceptFile = open("label_dict.txt", "w")
	index = 0

	lexicon = list()
	concepts = list()

	for line in trainFile:
		values = line.split( )
		if len(values) >= 2:
			if values[0] not in lexicon:
				lexicon.append(values[0])
			if values[1] not in concepts:
				concepts.append(values[1])

	for line in testFile:
		values = line.split( )
		if len(values) >= 2:
			if values[1] not in concepts:
				concepts.append(values[1])

	for word in lexicon:
		wordFile.write(word + "\t" + str(index) + "\n")
		index += 1
	wordFile.write("<UNK>" + "\t" + str(index) + "\n")

	index = 0

	for label in concepts:
		conceptFile.write(label + "\t" + str(index) + "\n")
		index += 1

	trainFile.close()
	wordFile.close()
	conceptFile.close()



createWordDict("NLSPARQL.train.data", "NLSPARQL.test.data")
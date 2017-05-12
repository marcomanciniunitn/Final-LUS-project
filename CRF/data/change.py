
file = open("test_tmp.txt", "r")
toWrite = open("test_lemma", "w")

for line in file:
	values = line.split("\t")
	if len(values) >= 4:
		lemma = values[2]
		label = values[3]
		toWrite.write(lemma + "\t" + label)
	else:
		toWrite.write("\n")

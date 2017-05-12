#Function used to change all the O concepts of the words into the words themselves
def changeAllO(file, out):
	w = open(out, "w")

	for line in (open(file).readlines()):
		v = line.split("\t")
		if(len(v)>1):
			if v[1][0:1] == "I" or v[1][0:1] == "B":
				w.write(line)
			else:
				w.write(v[0] + "\t" + "$-"+str(v[0])+"\n")
		else:
			w.write("\n")
			flag = 0
	w.close()

changeAllO("TRAIN.txt", "NLSPARQL.train.data")
changeAllO("TEST.txt", "NLSPARQL.test.data")
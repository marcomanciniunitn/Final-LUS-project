
train =  open("NLSPARQL.train.data", "w")
trainTmp = open("TRAIN.txt", "r")

test =  open("NLSPARQL.test.data", "w")
testTmp = open("TEST.txt", "r")

for line in trainTmp:
	val = line.split("\t")
	if len(val[0]) >= 1:
		train.write(val[0] + "#" + val[1] + "#" + val[2] + " " + val[3][0:len(val[3])-1] + "\n")
	else:
		train.write("\n")

for line in testTmp:
	val = line.split("\t")
	if len(val[0]) >= 1:
		test.write(val[0]+"#"+val[1]+"#"+val[2]+ " " + val[3])
	else:
		test.write("\n")

train.close()
trainTmp.close()
test.close()
testTmp.close()




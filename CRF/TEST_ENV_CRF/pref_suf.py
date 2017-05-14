
feat = open("NLSPARQL.train.feats.txt","r")
train = open("final_train_tmp", "w")
pref = "O"
suff = "O"

for line in feat:
	val = line.split("\t")
	if len(val) >= 3:
		if len(val[0]) >= 3:
			pref = val[0][0:3]
			suff = val[0][len(val[0]) -3: len(val[0])]
		else:
			pref = "O"
			suff = "O"
		train.write(val[0] + "\t" + val[2][0:len(val[2]) - 1] + "\t" + val[1] + "\t" + pref + "\t" + suff  + "\n")
	else:
		train.write("\n")


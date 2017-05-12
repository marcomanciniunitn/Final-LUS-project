
file = open("test_out.txt", "r")
toW = open("final_test.txt", "w")

for line in file:
	val = line.split( )
	if len(val) >= 2:
		if val[2].find("$") != -1 :
			toW.write(val[0] + " " + val[1] + " " + "O\n")
		else:
			toW.write(line)
	else:
		toW.write("\n")
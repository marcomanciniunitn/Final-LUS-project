

g = open("results.txt", "w")
with open("temp.txt", "r") as f:
  for line in f:
    if len(line) > 1:
      word = line.split('\t')[0]
      tag = line.split('\t')[1]
      predicted = line.split('\t')[2]
      g.write(word + '\t')
      if tag.find('$') < 0:
        g.write(tag + '\t')
        if predicted.find('$') < 0:
          g.write(predicted)
        else:
          g.write('O\n')
      else:
        g.write('O\t')
        if predicted.find('$') < 0:
          g.write(predicted)
        else:
          g.write('O\n')
    else:
      g.write('\n')
g.close()
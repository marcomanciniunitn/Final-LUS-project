cat NLSPARQL.train.data | cut -f 2 > only_label.data
paste final_train_tmp only_label.data > full.set.train


cat NLSPARQL.test.data | cut -f 2 > test.label.data
paste final_train_tmp test.label.data > full.set.test

crf_learn crf.template full.set.train crf.lm

crf_test -m crf.lm full.set.test > test.txt

perl conlleval.pl -d '\t' < test.txt



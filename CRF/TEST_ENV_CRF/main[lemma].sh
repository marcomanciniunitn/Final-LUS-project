cat NLSPARQL.train.feats.txt | cut -f 2 > POS.train.feats.txt
cat NLSPARQL.train.feats.txt | cut -f 3 > lemma.train.feats.txt
cat NLSPARQL.train.data | cut -f 2 > only_label.data
paste lemma.train.feats.txt POS.train.feats.txt only_label.data > with.pos.train.data

cat NLSPARQL.test.feats.txt | cut -f 2  > POS.test.feats.txt
cat NLSPARQL.test.feats.txt | cut -f 3  > lemma.test.feats.txt
cat NLSPARQL.test.data | cut -f 2 > test.label.data
paste lemma.test.feats.txt POS.test.feats.txt test.label.data > with.pos.test.data

crf_learn crf.template with.pos.train.data crf.lm

crf_test -m crf.lm with.pos.test.data > test.txt

perl conlleval.pl -d '\t' < test.txt

#!/bin/bash

python \
rnn_slu/lus/rnn_jordan_test.py \
model_jordan.G_basic \
rnn_slu/data/new_data/NLSPARQL.test.data \
rnn_slu/data/new_data/word_dict.txt \
rnn_slu/data/new_data/label_dict.txt \
rnn_slu/config.cfg \
model_jordan.G_basic/test_out.txt

./conlleval.pl < model_jordan.G_basic/test_out.txt 
./conlleval.pl < model_jordan.G_basic/test_out.txt > model_jordan.G_basic/performances.txt


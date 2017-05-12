#!/bin/bash

python \
rnn_slu/lus/rnn_jordan_train.py \
rnn_slu/data/new_data/NLSPARQL.train.data \
rnn_slu/data/new_data/NLSPARQL.validation.data \
rnn_slu/data/new_data/word_dict.txt \
rnn_slu/data/new_data/label_dict.txt \
rnn_slu/config.cfg \
model_jordan.G_basic


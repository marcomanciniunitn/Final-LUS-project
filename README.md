

   
# Final-LUS-project
This is the final project for the course of Language Understanding System of the Master Course in Computer Science at University of Trento [UNITN].  It consisted into the comparison between discriminative and generative models applied to the Language Understanding domain over the Movie dataset already used and analyzed by me on the previous project (https://github.com/marcomanciniunitn/LUS-Proj). A report containing all the specifics and the analysis of this project is provided.

## Getting Started
The project has beed suebdivided into 2 subprojects, one regarding the Conditional Random Fields (CRF) and the latter regarding the Recurrent Neural Networks.

* **CRF** <br />
The folder for this project is the CRF one. It contains the following subfolders: <br />
   - data: contains all the datasets and scripts to work on it<br />
   - models: contains some of the tested models <br />
   - results: contains some of the results, they are split into subfolders FEATURES (results using features) and NO_FEATURES (basic dataset used) <br />
   - templates: contains some of the tested templates. <br />
   - TEST_ENV_CRF: contains the test environment in which I've tested the CRFs. Some script is present in order to use different training and test sets <br />


* **RNN** <br />
The folder for this project is the RNN one. The main subfolders are: <br />
   - round_1: contains the models tested over all the datasets (basic and advanced ones), the models are configured with the best settings <br />
   - round_x[hyperparameter]: these subfolders contain different tests performed over the best results of the round 1 changing the hyperaparameter specified into the square brackets. Inside them is possible to find the models indicating on the names the value of the hyperparameter. <br />
   - rnn_slu/new_data: this folder contains all the dataset, spreaded into subfolders <br />
   - settings_test.sh/settings_train.sh: scripts used to train and test the models <br />


### Prerequisites

* Theano - http://deeplearning.net/software/theano/
* CRF++ - https://taku910.github.io/crfpp/


## Running the tests
* **CRF** <br />
Look for the CRF++ syntax in order to run and test the templates <br /> 

* **RNN** 
* Training Elman RNN: python rnn_slu/lus/rnn_elman_train.py <training_data> <validation_data> <word_dictionary> <label_dictionary> <config_file> <model_directory>

e.g.:
python rnn_slu/lus/rnn_elman_train.py rnn_slu/data/train_atis_samp.txt rnn_slu/data/dev_atis.txt rnn_slu/data/word_dict.txt rnn_slu/data/label_dict.txt rnn_slu/config.cfg model_elman

python rnn_slu/lus/rnn_elman_train.py rnn_slu/data/new_data/NLSPARQL.train.data rnn_slu/data/new_data/NLSPARQL.validation.data rnn_slu/data/new_data/word_dict.txt rnn_slu/data/new_data/label_dict.txt rnn_slu/config.cfg model_elman.1


* Testing Elman RNN: python rnn_slu/lus/rnn_elman_test.py <model_directory> <test_file> <word_dictionary> <label_dictionary> <config_file> <output_file>

e.g.:
python rnn_slu/lus/rnn_elman_test.py model_elman rnn_slu/data/test_atis.txt rnn_slu/data/word_dict.txt rnn_slu/data/label_dict.txt rnn_slu/config.cfg test_out.txt

* Training Jordan RNN: python rnn_slu/lus/rnn_jordan_train.py <training_data> <validation_data> <word_dictionary> <label_dictionary> <config_file> <model_directory>

e.g.:
python rnn_slu/lus/rnn_jordan_train.py rnn_slu/data/train_atis_samp.txt rnn_slu/data/dev_atis.txt rnn_slu/data/word_dict.txt rnn_slu/data/label_dict.txt rnn_slu/config.cfg model_elman

* Testing Jordan RNN: python rnn_slu/lus/rnn_jordan_test.py <model_directory> <test_file> <word_dictionary> <label_dictionary> <config_file> <output_file>

e.g.:
python rnn_slu/lus/rnn_jordan_test.py model_elman rnn_slu/data/test_atis.txt rnn_slu/data/word_dict.txt rnn_slu/data/label_dict.txt rnn_slu/config.cfg test_out.txt

## Authors

* **Marco Mancini** - https://www.linkedin.com/in/marco-mancini-6b2969108/

Regarding the RNN python file, it has been developed by ALi Orkan Bayer.

----- CRFs ----- <br />
The folder for this project is the CRF one. It contains the following subfolders: <br />
   - data: contains all the datasets and scripts to work on it<br />
   - models: contains some of the tested models <br />
   - results: contains some of the results, they are split into subfolders FEATURES (results using features) and NO_FEATURES (basic dataset used) <br />
   - templates: contains some of the tested templates. <br />
   - TEST_ENV_CRF: contains the test environment in which I've tested the CRFs. Some script is present in order to use different training and test sets <br />

----- RNNs ----- <br />
The folder for this project is the RNN one. The main subfolders are: <br />
   - round_1: contains the models tested over all the datasets (basic and advanced ones), the models are configured with the best settings <br />
   - round_x[hyperparameter]: these subfolders contain different tests performed over the best results of the round 1 changing the hyperaparameter specified into the square brackets. Inside them is possible to find the models indicating on the names the value of the hyperparameter. <br />
   - rnn_slu/new_data: this folder contains all the dataset, spreaded into subfolders <br />
   - settings_test.sh/settings_train.sh: scripts used to train and test the models <br />
   

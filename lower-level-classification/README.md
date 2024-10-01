## Instructions for lower-level classifications (Family to Phylum)

1. Run `generate_all_training_sets.py` This script will:
   
- This will create 4 directories for each taxa level. (Eg. phylum_testing)
- Create 5 trial folders for each taxa directory created (trial_01 to trial_05).
- It will then select a random 30 from different taxa with more than 30 representatives. For eg. In the dataset, the phylum Uroviricota has 1140 representatives, meaning a random 30 out of those 1140 will be selected.
  
2. After generating the training data, use Jellyfish to create k-mer count files for training. For detailed instructions on using Jellyfish and the Naive Bayes Classifier (NBC), refer to the manual at https://github.com/EESI/Naive_Bayes/tree/master.

3. Creating training lists

- Start by creating a new directory to store all training lists.
- Set your working directory to this newly created directory.
- Execute `create_training_lists.py`. This script will create 4 new directories for each taxa level. Each directory will have 5 `.txt` files (1 for each trial). Each txt file will contain classes that belong in the training set for each trial.

4. Upon completion of all tests, export all result files to your local machine. Then, run the provided Jupyter Notebook to modify outputs and generate graphs for analysis.


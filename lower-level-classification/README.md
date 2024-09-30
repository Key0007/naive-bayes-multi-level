Instructions for lower-level classifications (Family to Phylum)

1. Run everything.py
2. This will create 4 directories for each taxa level. (Eg. phylum_testing).
3. It will also subdirectories and 5 trial folders (trial_01 to trial_05). Modify as needed
4. It will then select a random 30 from different taxa that have more than 30 represetatives. For eg. In the dataset, the phylum Uroviricota has 1140 representatives, meaning a random 30 out of those 1140 will be selected. 
5. After generating the training data, use Jellyfish to create k-mer count files for training. For detailed instructions on using Jellyfish and the Naive Bayes Classifier (NBC), refer to the manual at https://github.com/EESI/Naive_Bayes/tree/master.

6. Creating training lists

Start by creating a new directory to store all training lists.

Make it the current working directory and run create_training_lists.py

This will create 4 new directories for each taxa level. Each directory will have 5 txt files (1 for each trial). Each txt file contains classes that belong in the training set for each trial. Export all the files locally to be used with the Jupyter Notebook


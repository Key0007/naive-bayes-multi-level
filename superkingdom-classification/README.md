**Instructions for Superkingdom Classification**

1. Create a new directory for training data.
2. Set your working directory to this newly created training directory.
3. Execute generate_training_sets.py. This script will:

- Generate training sets by selecting 2 out of 4 available superkingdom classes (archaea, eukaryota, bacteria, and viruses).
- Create 6 different folders, each representing a pair of superkingdoms.
- Populate each folder with 70 randomly sampled species from each of the two selected superkingdoms.
Example: The 'bacteria-archaea' folder will contain 70 randomly sampled bacterial species and 70 randomly sampled archaean species.

Modify the directory paths in the script as needed. They are located at the beginning of the main guard.
The training sets are balanced by sampling 70 species from each superkingdom. This sampling strategy ensures equal representation across all superkingdoms and prevents bias in the training process. The sample size of 70 was chosen because the master dataset contained only 70 eukaryote species, which became the limiting factor for balanced sampling across all superkingdoms.

4. After generating the training data, use Jellyfish to create k-mer count files for training. For detailed instructions on using Jellyfish and the Naive Bayes Classifier (NBC), refer to the manual at https://github.com/EESI/Naive_Bayes/tree/master.
5. Upon completion of all tests, export all result files to your local machine. Then, run the provided Jupyter Notebook to modify outputs and generate graphs for analysis.

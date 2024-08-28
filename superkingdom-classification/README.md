**Instructions for Superkingdom Classification**

1. Create a new directory for training data.
2. Set your working directory to this newly created training directory.
3. Execute generate_training_sets.py. This script will:

- Generate training sets by selecting 2 out of 4 available superkingdom classes (archaea, eukaryota, bacteria, and viruses).
- Create 6 different folders, each representing a pair of superkingdoms.
- Populate each folder with 70 randomly sampled species from each of the two selected superkingdoms.
Example: The 'bacteria-archaea' folder will contain 70 randomly sampled bacterial species and 70 randomly sampled archaean species.

Modify the directory paths in the script as needed. They are located at the beginning of the main guard.
The training sets are balanced with 70 species per superkingdom to ensure equal representation and prevent bias. This number was chosen based on the limited availability of eukaryote species in the master dataset.

4. After generating the training data, use Jellyfish to create k-mer count files for training. For detailed instructions on using Jellyfish and the Naive Bayes Classifier (NBC), refer to the manual at https://github.com/EESI/Naive_Bayes/tree/master.
5. Upon completion of all tests, export all result files to your local machine. Then, run the provided Jupyter Notebook to modify outputs and generate graphs for analysis.

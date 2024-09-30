import os
import pandas as pd
import random
import shutil

def random_30(list_):
    return random.sample(list_, 30)


def copy_folder(final_list, destination_path):
    source_dir = r'/ifs/groups/rosenMRIGrp/refSeq_db/basic/download/fna_grouped_by_species_tax'
    print(f"Attempting to copy directories to {destination_path}")

    for item in final_list:
        source_path = os.path.join(source_dir, str(item))
        if os.path.isdir(source_path):
            try:
                shutil.copytree(source_path, os.path.join(destination_path, str(item)), dirs_exist_ok=True)
                print(f"Successfully copied directory: {item}")
            except Exception as e:
                print(f"Error copying directory {item}: {str(e)}")
        else:
            print(f"Not a directory, skipping: {source_path}")


if __name__ == "__main__":

    # path to lineage_list.csv | modify as needed
    csv_file = r'/ifs/groups/rosenMRIGrp/kr3288/lineage_list.csv'
    # converts csv to df
    df = pd.read_csv(csv_file)
    # replace NaN with empty string
    df = df.fillna('')
    # remove trailing space
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    taxa_levels = ['Phylum', 'Class', 'Order', 'Family']

    path = os.getcwd()

    for taxa_level in taxa_levels:

        # MODIFY AS NEEDED
        training_directory = os.path.join(path, f'{taxa_level.lower()}_testing/Trials/raw-data/training')
        os.makedirs(training_directory, exist_ok=True)

        for trial in ['trial_01', 'trial_02', 'trial_03', 'trial_04', 'trial_05']:
            os.makedirs(os.path.join(training_directory, trial), exist_ok=True)

        # create species | taxa dataframe
        dx = df[['Species_ID', taxa_level]]
        # filter by phyla with >= 30 occurrences
        dx = dx[dx[taxa_level].isin(dx[taxa_level].value_counts()[dx[taxa_level].value_counts() >= 30].index)]
        # remove empty strings and rows
        dx = dx[dx[taxa_level] != '']

        # groups each taxa rep into groups of __ in a dictionary
        grouped_dfs = {name: group.reset_index(drop=True) for name, group in dx.groupby(taxa_level)}
        grouped_dfs = {key.lower(): value for key, value in grouped_dfs.items()}

        for folder_name in os.listdir(training_directory):

            try:
                training_taxa = random.sample(list(grouped_dfs.keys()), int(len(list(grouped_dfs.keys()))/2))
                training_data = []

                for taxa in training_taxa:
                    selected_list = random_30(grouped_dfs[taxa]['Species_ID'].tolist())
                    training_data.extend(selected_list)


                training_path = os.path.join(training_directory, str(folder_name))
                # copy training_data
                copy_folder(training_data, training_path)

            except Exception as e:
                print(f"Error processing folder {folder_name}: {str(e)}")
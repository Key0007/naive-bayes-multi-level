import os
import pandas as pd
import random
import shutil

# generates a list random 70 for a superkingdom, concatenated together
def random_70(list1, list2):
    return random.sample(list1, 70) + random.sample(list2, 70)

# makes copies of selected species_IDq
def copy_folder(final_list, destination_path):
    # path to ref seq
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


    # SPECIFY FILE PATHS

    # path to lookup_table.csv
    csv_file = r''

    
    path = os.getcwd()
    # creates training folders
    for combination in ['bacteria-archaea', 'viruses-archaea', 'viruses-eukaryota', 'viruses-bacteria', 'bacteria-eukaryota', 'archaea-eukaryota']:
        os.makedirs(os.path.join(path, combination), exist_ok=True)

    # converts csv to df
    df = pd.read_csv(csv_file)
    # removes trailing space from 3rd column
    df['Superkingdom'] = df['Superkingdom'].str.strip()

    # groups each superkingdom taxa into groups 4 in a dictionary
    grouped_dfs = {name: group.reset_index(drop=True) for name, group in df.groupby('Superkingdom')}
    grouped_dfs = {key.lower(): value for key, value in grouped_dfs.items()}

    for folder_name in os.listdir(path):

        try:

            list1 = grouped_dfs[folder_name.split("-")[0]]['Species_ID'].tolist()
            list2 = grouped_dfs[folder_name.split("-")[1]]['Species_ID'].tolist()

            final_list = random_70(list1, list2)

            destination_path = os.path.join(path, str(folder_name))
            copy_folder(final_list, destination_path)

            print(f"Copying files to {destination_path}")
            copy_folder(final_list, destination_path)
            print(f"Finished copying files to {destination_path}")

        except Exception as e:
            print(f"Error processing folder {folder_name}: {str(e)}")

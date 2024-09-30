import os

def create_txt(taxa, trial):

    # change folder path
    folder_path = f'/ifs/groups/rosenMRIGrp/kr3288/{taxa}_testing/Trials/3-mers/raw-data/training/{trial}'

    current_dir = os.getcwd()
    
    txt_string = ""
    for folder in os.listdir(folder_path):
        txt_string += folder + '\n'

    output_file_path = os.path.join(f'{current_dir}/{taxa}', f'{taxa}_{trial}_training_list.txt')
    with open(output_file_path, 'w') as outfile:
        outfile.write(txt_string)

if __name__ == "__main__":

    current_path = os.getcwd()

    for taxa in ['phylum', 'order', 'family', 'class']:
        os.makedirs(os.path.join(current_path, taxa), exist_ok=True)
        for trial in ['trial_01', 'trial_02', 'trial_03', 'trial_04', 'trial_05']:
            create_txt(taxa, trial)



    
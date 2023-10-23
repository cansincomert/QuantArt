import os
import random
import shutil

def split_paired_dataset(folder1, folder2, output_folder1, output_folder2, train_ratio=0.6, val_ratio=0.2):
    # Create output directories for train, val, and test data
    for out_folder in [output_folder1, output_folder2]:
        os.makedirs(os.path.join(out_folder, 'train'), exist_ok=True)
        os.makedirs(os.path.join(out_folder, 'val'), exist_ok=True)
        os.makedirs(os.path.join(out_folder, 'test'), exist_ok=True)

    # Assuming filenames are the same in both folders
    filenames = sorted(os.listdir(folder1))
    
    # Shuffle filenames
    random.shuffle(filenames)
    
    # Calculate sizes
    total = len(filenames)
    train_size = int(train_ratio * total)
    val_size = int(val_ratio * total)
    test_size = total - train_size - val_size

    # Split filenames
    train_files = filenames[:train_size]
    val_files = filenames[train_size:train_size + val_size]
    test_files = filenames[train_size + val_size:]

    # Copy files
    for name, files in zip(['train', 'val', 'test'], [train_files, val_files, test_files]):
        for f in files:
            shutil.copy(os.path.join(folder1, f), os.path.join(output_folder1, name, f))
            shutil.copy(os.path.join(folder2, f), os.path.join(output_folder2, name, f))

# Define folders
folder1 = '/home/cansin/Documents/codebase/QuantArt/datasets/AllPairedCMR/reCine-Q'
folder2 = '/home/cansin/Documents/codebase/QuantArt/datasets/AllPairedCMR/reT1Map-Q'
output_folder1 = '/home/cansin/Documents/codebase/QuantArt/datasets/content/'
output_folder2 = '/home/cansin/Documents/codebase/QuantArt/datasets/style/'

# Call function
split_paired_dataset(folder1, folder2, output_folder1, output_folder2)

import os

def compare_folders(folder1, folder2):
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))
    
    # Files present in both folders
    intersection = files1.intersection(files2)
    
    # Files unique to each folder
    only_in_folder1 = files1 - intersection
    only_in_folder2 = files2 - intersection

    # Print results
    print(f"Total files in {folder1}: {len(files1)}")
    print(f"Total files in {folder2}: {len(files2)}")
    print(f"Number of files present in both folders: {len(intersection)}")
    print(f"Number of files unique to {folder1}: {len(only_in_folder1)}")
    print(f"Number of files unique to {folder2}: {len(only_in_folder2)}")
    
    print(f"Files in both folders: {intersection}")
    print(f"Files only in {folder1}: {only_in_folder1}")
    print(f"Files only in {folder2}: {only_in_folder2}")

# Replace these with the paths to your folders
folder1 = '/home/cansin/Documents/codebase/QuantArt/datasets/AllPairedCMR/reCine-Q'
folder2 = '/home/cansin/Documents/codebase/QuantArt/datasets/AllPairedCMR/reT1Map-Q'

compare_folders(folder1, folder2)



# def delete_files_in_folder(folder, files_to_delete):
#     for file in files_to_delete:
#         file_path = os.path.join(folder, file)
#         try:
#             os.remove(file_path)
#             print(f"Deleted {file_path}")
#         except FileNotFoundError:
#             print(f"{file_path} not found")

# # Files you want to delete from each folder
# files_to_delete_folder1 = {'1684_0_03.png', '1684_0_04.png', '1684_0_06.png', '1684_0_05.png'}
# files_to_delete_folder2 = {'1536_0_07.png', '0096_0_0_08.png', '1536_0_10.png', '1536_0_19.png'}

# # Folder paths
# folder1 = "/home/cansin/Documents/codebase/QuantArt/datasets/AllPairedCMR/reCine-Q"
# folder2 = "/home/cansin/Documents/codebase/QuantArt/datasets/AllPairedCMR/reT1Map-Q"

# # Delete files
# delete_files_in_folder(folder1, files_to_delete_folder1)
# delete_files_in_folder(folder2, files_to_delete_folder2)

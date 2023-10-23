from PIL import Image 
import os


# Path to the directory containing PNG images
input_directory = "/home/cansin/Documents/codebase/QuantArt/datasets/AllPairedCMR/T1Map-Q"
output_directory = "/home/cansin/Documents/codebase/QuantArt/datasets/AllPairedCMR/reT1Map-Q"

def resize_images_with_PIL(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.endswith(".png"):
            img = Image.open(os.path.join(input_directory,filename))
            img_resized = img.resize((256,256),Image.ANTIALIAS)
            img_resized.save(os.path.join(output_directory,filename))

resize_images_with_PIL(input_directory, output_directory)

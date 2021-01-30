import os
import shutil

index_directory = input("Enter index directory : ")
others_directory = input("Enter others directory : ")

# Get index ID
index = index_directory.split("/")
index_id = index[-1]

# Get Others ID 
others = others_directory.split("/")
others_id = others[-1]
others_id, _ = others_id.split("_", 1)
others_id = others_id + ".jpg"

if (index_id == others_id) :
    
    # Create same directory
    same_dir = 'C:/Users/Public/Documents/same'
    if not os.path.exists(same_dir):
        os.makedirs(same_dir)
    # Move same images to same directory
    shutil.move(index_directory, same_dir)
    shutil.move(others_directory, same_dir)
    
else :
    
    # Create different directory
    different_dir = 'C:/Users/Public/Documents/different'
    if not os.path.exists(different_dir):
        os.makedirs(different_dir)
    # Move different images to different directory
    shutil.move(index_directory, different_dir)   
    shutil.move(others_directory, different_dir)  
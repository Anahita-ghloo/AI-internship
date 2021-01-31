import os
import shutil
import argparse

def get_index_ID(index_dir: str) -> str:
    # Get index ID
    index = index_dir.split('/')
    index_id = index[-1]
    return index_id

def get_others_ID(others_dir: str) -> str:
    # Get Others ID 
    others = others_dir.split('/')
    others_id = others[-1]
    others_id, _ = others_id.split('_', 1)
    others_id = others_id + ".jpg"
    return others_id

def compare_ID(
        index_id: str, others_id: str, index_directory: str,
        others_directory: str, output_directory: str) -> None:

    if (index_id == others_id) :
        # Create same directory
        same_dir = output_directory + '/same'
        if not os.path.exists(same_dir):
            os.makedirs(same_dir)
        # Move same images to same directory
        shutil.move(index_directory, same_dir)
        shutil.move(others_directory, same_dir)
        print("Files moved to same directory") 
    
    else :  
        # Create different directory
        different_dir = output_directory + '/different'
        if not os.path.exists(different_dir):
            os.makedirs(different_dir)
        # Move different images to different directory
        shutil.move(index_directory, different_dir)   
        shutil.move(others_directory, different_dir) 
        print("Files moved to different directory") 


def main():
   
    # Get input with argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('index_directory', help = 'Type index directory')
    parser.add_argument('others_directory', help = 'Type others directory')
    parser.add_argument('output_directory', help = 'Type output directory')
    args = parser.parse_args()
   
    index_directory = args.index_directory.replace('\\', '/')
    others_directory = args.others_directory.replace('\\', '/')
    output_directory = args.output_directory.replace('\\', '/')

    index_id = get_index_ID(index_directory)
    others_id = get_others_ID(others_directory)
    compare_ID(index_id, others_id, index_directory, others_directory, output_directory)

if __name__ == '__main__':
    main()


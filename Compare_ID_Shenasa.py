import os
import shutil
import argparse

def get_others_ID(others_name) -> str:
    # Get others ID
    others_name_id, _ = others_name.split('_', 1)
    others_name_id = others_name_id + '.jpg'
    return others_name_id

def move_images(same_images: str, index_id: str, others_name: str, index_directory: str,
        others_directory: str, output_directory: str) -> None:

    if same_images:       
        # Create a directory for same images
        same_dir = output_directory + '/same' + index_id

        if not os.path.exists(same_dir):
             os.makedirs(same_dir)
                    
        shutil.move(index_directory + '/' + index_id , same_dir)
        for f in same_images :
            shutil.move(others_directory + '/' + f , same_dir)
    else :
        different_dir = output_directory + '/different'

        if not os.path.exists(different_dir):
            os.makedirs(different_dir)
        shutil.move(index_directory + '/' + index_id , different_dir)


def main():
   
    # Get input with argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--index_directory', help = 'Type --index_directory')
    parser.add_argument('--others_directory', help = 'Type --others_directory')
    parser.add_argument('--output_directory', help = 'Type --output_directory')
    args = parser.parse_args()
   
    index_directory = args.index_directory.replace('\\', '/')
    others_directory = args.others_directory.replace('\\', '/')
    output_directory = args.output_directory.replace('\\', '/')

    for i, index_id in enumerate(os.listdir(index_directory)):
    
        same_images = []
    
        for j, others_name in enumerate(os.listdir(others_directory)): 
        
           others_id = get_others_ID(others_name)

           if (index_id == others_id) :
               same_images.append(others_name)

        move_images(same_images, index_id, others_name, index_directory, others_directory, output_directory)

        


if __name__ == '__main__':
    main()


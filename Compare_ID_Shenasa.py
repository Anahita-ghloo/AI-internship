import os
import shutil
import argparse
import random

def get_others_ID(others_name) -> str:
    """
    Get others ID
    """
    others_name_id, _ = others_name.split('_', 1)
    others_name_id = others_name_id + '.jpg'
    return others_name_id


def generate_same_pairs(index_directory: str, others_directory: str,
                        output_directory: str) -> int:
    """
    Generate all same pairs
    """
    all_same_names = []
    
    for i, index_id in enumerate(os.listdir(index_directory)):

        same_images = []
    
        for j, others_name in enumerate(os.listdir(others_directory)):  

            others_id = get_others_ID(others_name)

            if index_id == others_id:
                same_images.append(others_name)
            
        if same_images:
            # If image has same image in others
            same_images.append(index_id)
            for i in range(0, len(same_images)):
                for j in range(i+1, len(same_images)):
                    
                    # Create a directory for same images
                    same_dir = output_directory + '/same' + same_images[i] + '-' + same_images[j]

                    # Don't create the file if it already exists
                    if not os.path.exists(same_dir):
                        os.makedirs(same_dir)
                     
                        pair = [same_images[i], same_images[j]]  
                    
                        for f in pair :
                     
                            if f == index_id:
                                shutil.copy(index_directory + '/' + f , same_dir)   
                            else:
                                shutil.copy(others_directory + '/' + f , same_dir)

        all_same_names.extend(same_images)
    return len(all_same_pairs)
                
def generate_different_pairs(num_same_paires: int, index_directory: str,
                             others_directory: str, output_directory: str) -> int:
    """
    Generate random different pairs
    """
    
    # To have same number of same and different pairs
    num_different_pairs = 0
    while num_different_pairs < num_same_paires:
        index_id = random.choice(os.listdir(index_directory))
        others_name = random.choice(os.listdir(others_directory))
        others_id = get_others_ID(others_name)

        if index_id != others_id:
            different_dir = output_directory + '/different' + index_id + '-' + others_name
            
            # Don't create the file if it already exists
            if not os.path.exists(different_dir):
                os.makedirs(different_dir)
                            
                shutil.copy(index_directory + '/' + index_id, different_dir)
                shutil.copy(others_directory + '/' + others_name, different_dir)
                num_different_pairs += 1
    return num_different_pairs 

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

    num_same_pairs = generate_same_pairs(index_directory, others_directory, output_directory)
    num_different_pairs = generate_different_pairs(num_same_pairs, index_directory, others_directory, output_directory)
    print(num_same_pairs, ' same pairs & ', num_different_pairs, ' differnet pairs.')

if __name__ == '__main__':
    main()


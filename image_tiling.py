# installed split-image via "pip install split-image" before

import os


# needs split-image CLI https://pypi.org/project/split-image/
def tile_images(directory):
    img_directory = directory
    directory = os.fsencode(img_directory)
    not_split = []

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        try:
            os.system(f"split-image {img_directory}{filename} 10 10 --cleanup")
        except:
            print(f"file: {filename} could not be split.")
            not_split.append(filename)
        # else:
        #     file_to_remove = f"{img_directory}{filename}"
        #     os.remove(file_to_remove)
    print(not_split)


if __name__ == "__main__":
    tile_images("/Volumes/moar_memory/DOP_image_splitting/images/")

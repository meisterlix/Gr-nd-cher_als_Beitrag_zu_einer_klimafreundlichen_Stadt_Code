import os
from PIL import Image

# set working directory all files in wd will be converted from png to jp2
wd = "/Volumes/moar_memory/DOP_image_splitting/images/"
# set whether all files should be reconverted regardless of prefix
reload_all = False

directory = os.fsencode(wd)


def convert_png_to_jpg():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith("DS_Store"):
            continue
        else:
            im = Image.open(f"{wd}/{filename}")
            new_im = im.convert("RGB")
            # cutting off 8 instead of 4 chars from end because the files have a .jp2 ending still
            new_im.save(f"{wd}/{filename[:-8]}.jpg")
    # print(f"directory: {directory}")s
    # # iterate through directory
    # for file in os.listdir(directory):
    #     filename = os.fsdecode(file)
    #     print(filename)
    #     new_filename = f"{wd}/{filename[:-3]}.jpg"
    #     # skip files with jpg suffix
    #     if filename.endswith(".jpg"):
    #         continue
    #     if os.path.isfile(new_filename) and not reload_all:
    #         continue
    #     # convert jp2 images to png and add png prefix
    #     if filename.endswith(".png"):
    #         im = Image.open(f"{wd}/{filename}")
    #         im.save(f"{wd}/{filename}", format="jpeg")
    #     else:
    #         continue


convert_png_to_jpg()

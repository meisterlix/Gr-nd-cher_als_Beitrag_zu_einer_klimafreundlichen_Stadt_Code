import os
from PIL import Image

# set working directory all files in wd will be converted from png to jp2
wd = "/Volumes/moar_memory/coco_test/data/"
# set whether all files should be reconverted regardless of prefix
reload_all = False

directory = os.fsencode(wd)


def convert_jp2():
    print(f"directory: {directory}")
    # iterate through directory
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        new_filename = f"{wd}/IR_{filename}"
        # skip files with png prefix
        if filename.startswith("png_"):
            continue
        if os.path.isfile(new_filename) and not reload_all:
            continue
        # convert jp2 images to png and add png prefix
        if filename.endswith(".jp2"):
            im = Image.open(f"{wd}/{filename}")
            im.save(f"{wd}/png_{filename}", format="png")
        else:
            continue


convert_jp2()

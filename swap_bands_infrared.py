import os
from PIL import Image

# set working directory. All files in the wd will be bandswapped
wd = "/Volumes/moar_memory/DOP20_HH_fruehjahrsbefliegung_2021_rgbi/"
# set whether all images should be bandswapped regardless if marked by IR_ prefix
reload_all = False

directory = os.fsencode(wd)


def bandswap():
    print(f"directory: {directory}")
    # iterate through directory
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        new_filename = f"{wd}/IR_{filename}"
        print(filename)
        # skip files with IR prefix
        if filename.startswith("IR"):
            continue
        # if file already processed and reprocessing is not activated
        if os.path.isfile(new_filename) and not reload_all:
            continue
        # files with worldfile ending will be bandswapped
        if filename.endswith(".jp2"):
            im = Image.open(f"{wd}/{filename}")
            red, green, blue, infrared = im.split()
            im_swapped = Image.merge("RGB", (infrared, green, red))
            im_swapped.save(f"{wd}/IR_{filename}")
        else:
            continue


bandswap()

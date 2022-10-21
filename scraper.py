import requests
import data
import csv
import os.path
from joblib import Parallel, delayed

API_KEY = data.API
format = "png32"
mapType = "satellite"
resolution = "640x640"
zoom = 18
starting_x = 9969621
starting_y = 53578578
# Step Sizes sind durch Trial & Error plus Rechnung bestimmt
steps_size_x = 3438
steps_size_y = 2038
ending_x = 9983975
ending_y = 53587979

raster_coordinates = []
reload_all = False


def load_picture_for_coord(coord):
    coordinates = f"{coord[0]},{coord[1]}"
    filename = f"outputs/{coordinates}-{resolution}-{coord[2]}-{coord[3]}.png"
    if os.path.isfile(filename) and not reload_all:
        return
    try:
        url = f"https://maps.googleapis.com/maps/api/staticmap?center={coordinates}&zoom={zoom}&size={resolution}&maptype={mapType}&format={format}&key={API_KEY}"
        r = requests.get(url)
        png = r._content

        file = open(filename, "wb")
        file.write(png)
        file.close()
    except:
        print(f"Could not load {filename}")


with open("coordinates_bezirke.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    # skip header row
    for row in spamreader:
        # print(row)
        x, y, bezirk, stadtteil = row
        raster_coordinates.append((x, y, bezirk, stadtteil))


# 53.565811, 10.020954
# 53.565811, 10.022654 für X messung
# 53.566807, 10.021083 für y messung
# mit Maps ermittelte Step Size für exklusive Bilder X = 3400, Y = 2000
# Sternschanze von  53.557292, 9.959136 bis  53.567368, 9.977068
# anhand von pixelmator pro ermittelte nötige Verschiebung y = 12px, x = 7px
# x_step = 3438, y_step = 2038
# Hoheluft-Ost von  53.578578, 9.969621 bis  53.587979, 9.983975

# Parallel 8-fach ablaufen lassen, um die Scraping Zeit zu verringern.
Parallel(n_jobs=8)(
    delayed(load_picture_for_coord)(coord) for coord in raster_coordinates
)

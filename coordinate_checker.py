from shapely.geometry import Point, Polygon
import csv

# Create Point objects
p1 = Point(24.952242, 60.1696017)
p2 = Point(24.976567, 60.1612500)


# Create a Polygon
hamburg_cords = []
raster_cords = []
with open('Raster Hamburg.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    # skip header row
    spamreader.__next__()
    for row in spamreader:
        #print(row)
        _, x, y = row
        raster_cords.append(Point(float(x),float(y)))

with open('Raster Hamburg.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    # skip header row
    spamreader.__next__()
    for row in spamreader:
        #print(row)
        _, x, y = row
        hamburg_cords.append(Point(float(x),float(y)))
poly = Polygon(hamburg_cords)

for p in raster_cords:
    if p.within(poly):
        # write line to outputfile
        pass
    else:
        pass
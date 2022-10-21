raster_starting_x = 9701054
raster_starting_y = 53372917
steps_size_x = 3438
steps_size_y = 2038
raster_ending_x = 10320199
raster_ending_y = 53756474


# Hamburg südwest  53.372917, 9.701054  bis nordost  53.756474, 10.320199

# Einfügen: Raster vom Start ablaufen und wenn die Koordinaten in den snippet
# Koordinaten liegen Bilder speichern

i = 0
j = 0
n = 0

f = open("output.csv", "a")
f.write("number,y-coordinate,x-coordinate,\n")
f.close()


while True:
    x_coordinate = round((raster_starting_x + steps_size_x * i) * 1e-6, 6)
    y_coordinate = round((raster_starting_y + steps_size_y * j) * 1e-6, 6)
    coordinates = "{y:.6f},{x:.6f}".format(
        y=(raster_starting_y + steps_size_y * j) * 1e-6,
        x=(raster_starting_x + steps_size_x * i) * 1e-6,
    )
    f = open("output.csv", "a")
    f.write(str(n) + "," + str(y_coordinate) + "," + str(x_coordinate) + ",\n")
    f.close()
    n += 1
    if raster_starting_x + steps_size_x * i >= raster_ending_x:
        i = 0
        j += 1
    else:
        i += 1
    if raster_starting_y + steps_size_y * j >= raster_ending_y:
        break

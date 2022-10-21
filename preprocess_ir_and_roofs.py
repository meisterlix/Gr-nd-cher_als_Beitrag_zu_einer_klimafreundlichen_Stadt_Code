from shapely.geometry import Point, Polygon
import os
import geopandas

PICTURE_DIR = "/Volumes/moar_memory/ir_dach_data"
PICTURE_WIDTH_PX = 5000
PICTURE_HEIGHT_PX = 5000


class WorldFile:
    def __init__(self, lst, path) -> None:
        A = lst[0]
        D = lst[1]
        B = lst[2]
        E = lst[3]
        C = lst[4]
        F = lst[5]
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.x1 = C
        self.x2 = A * (PICTURE_WIDTH_PX-1) + C
        self.y1 = F
        self.y2 = E * (PICTURE_HEIGHT_PX-1) + F
        self.polygon = None
        self.path = path
    
    def getPolygon(self) -> Polygon:
        if self.polygon == None:
            self.polygon = Polygon([Point(self.x1, self.y1), Point(self.x1, self.y2), Point(self.x2, self.y2),Point(self.x2, self.y1)])
        return self.polygon


def parseWF(pathToFile):
    wf = open(pathToFile, "r")
    wf_content = wf.read()
    wf_val = list(map(float, wf_content.splitlines()))
    return WorldFile(wf_val, pathToFile)


poly_list = []
file_names = list(map(lambda y: y[:-3], filter(lambda x: x.endswith(".jp2"), os.listdir(PICTURE_DIR))))
for file_name in file_names:
    picture_file_name = file_name + "jp2"
    world_file_name = file_name + "j2w"
    world_file = parseWF(os.path.join(PICTURE_DIR, world_file_name))
    print(file_name)
    poly_list.append(world_file.getPolygon())
geoFrameIRImages = geopandas.GeoDataFrame({'image': list(map(lambda x: x + "jp2", file_names))}, geometry=poly_list)
geoFrameIRImages.set_crs("EPSG:32633")

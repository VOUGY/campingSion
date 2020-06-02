from builtins import print
import geopandas as gpd
# from shapely.geometry.multipolygon import MultiPolygon
import psycopg2
import geo_web.models
from geo_web.models import Tree, SwimmingPool, Location, CampingArea, Building

con = psycopg2.connect(database="GIS", user="postgres", password="postgres",
                       host="localhost", port="25432")

def polygon_obj_switcher(polygon_obj_type):
    switcher = {
        "building": "geo_web_building",
        "location": "geo_web_location",
        "pool": "geo_web_swimmingpool",
        "area": "geo_web_campingarea"
    }
    return switcher.get(polygon_obj_type)


def get_area(polygon_obj_type, polygon_obj_number):
    sql ="SELECT * FROM " + polygon_obj_switcher(polygon_obj_type) + " WHERE id = " + str(polygon_obj_number)
    df = gpd.GeoDataFrame.from_postgis(sql, con, geom_col="geom")
    for index, row in df.iterrows():
        poly_area = row['geom'].area
        print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))


def get_all_areas(polygon_obj_type):
    sql ="SELECT * FROM " + polygon_obj_switcher(polygon_obj_type)
    df = gpd.GeoDataFrame.from_postgis(sql, con, geom_col="geom")
    listing = []
    for index, row in df.iterrows():
        poly_area = row['geom'].area
        listing.append(poly_area)
        # print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))
    return listing

def get_area_objects(polygon_obj_type):
    if polygon_obj_type == 'building':
        objects = Building.objects.all()
    elif polygon_obj_type == 'location':
        objects = Location.objects.all()
    elif polygon_obj_type == 'pool':
        objects = SwimmingPool.objects.all()
    elif polygon_obj_type == ' area':
        objects = CampingArea.objects.all()
    area_objects_list = []
    for object in objects:
        area_objects_list.append("%.0f" % object.geom.area)
    return area_objects_list

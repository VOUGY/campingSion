import geopandas as gpd
from shapely.geometry import MultiPolygon, polygon, point, linestring, asLinearRing, multilinestring, multipoint
from geo_web.models import Tree, SwimmingPool, Location, CampingArea, Building

# con = psycopg2.connect(database="GIS", user="postgres", password="postgres",
#                        host="localhost", port="25432")
#
# def polygon_obj_switcher(polygon_obj_type):
#     switcher = {
#         "building": "geo_web_building",
#         "location": "geo_web_location",
#         "pool": "geo_web_swimmingpool",
#         "area": "geo_web_campingarea"
#     }
#     return switcher.get(polygon_obj_type)


# def get_area(polygon_obj_type, polygon_obj_number):
#     sql ="SELECT * FROM " + polygon_obj_switcher(polygon_obj_type) + " WHERE id = " + str(polygon_obj_number)
#     df = gpd.GeoDataFrame.from_postgis(sql, con, geom_col="geom")
#     for index, row in df.iterrows():
#         poly_area = row['geom'].area
#         print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))
#
#
# def get_all_areas(polygon_obj_type):
#     sql ="SELECT * FROM " + polygon_obj_switcher(polygon_obj_type)
#     df = gpd.GeoDataFrame.from_postgis(sql, con, geom_col="geom")
#     listing = []
#     for index, row in df.iterrows():
#         poly_area = row['geom'].area
#         listing.append(poly_area)
#         # print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))
#     return listing

def get_area_objects(polygon_obj_type):
    if polygon_obj_type == 'building':
        objects = Building.objects.all()
    elif polygon_obj_type == 'location':
        objects = Location.objects.all()
    elif polygon_obj_type == 'pool':
        objects = SwimmingPool.objects.all()
    elif polygon_obj_type == 'area':
        objects = CampingArea.objects.all()
    area_objects_list = []
    for object in objects:
        area_objects_list.append("%.0f" % object.geom.area)
    return area_objects_list

def get_area_object(polygon_obj_type, id):
    if polygon_obj_type == 'building':
        obj = Building.objects.get(id_0 = id)
    elif polygon_obj_type == 'location':
        obj = Location.objects.get(id_0 = id)
    elif polygon_obj_type == 'pool':
        obj = SwimmingPool.objects.get(id = id)
    elif polygon_obj_type == 'area':
        obj = CampingArea.objects.get(id_0 = id)
    area_object = ("%.0f" %  obj.geom.area)
    return area_object


def get_dist_rest(polygon_obj_type, id):
    if polygon_obj_type == 'building':
        object = Building.objects.get(id_0 = id)
    elif polygon_obj_type == 'location':
        object = Location.objects.get(id_0 = id)
    elif polygon_obj_type == 'pool':
        object = SwimmingPool.objects.get(id = id)
    elif polygon_obj_type == 'area':
        object = CampingArea.objects.get(id_0 = id)
    restaurant = Building.objects.get(name='Restaurant al italia')
    distRest = ("%.0f" % object.geom.distance(restaurant.geom))
    return distRest


def get_dist_swimPool(polygon_obj_type, id):
    if polygon_obj_type == 'building':
        object = Building.objects.get(id_0 = id)
    elif polygon_obj_type == 'location':
        object = Location.objects.get(id_0 = id)
    elif polygon_obj_type == 'pool':
        object = SwimmingPool.objects.get(id = id)
    elif polygon_obj_type == 'area':
        object = CampingArea.objects.get(id_0 = id)
    sp_ds = SwimmingPool.objects.all()
    nearest_sp = 999999
    for item in sp_ds:
        if object.geom.distance(item.geom) < nearest_sp:
            nearest_sp = item.geom.distance(object.geom)
    dist_swimPool = ("%.0f" % nearest_sp)
    return dist_swimPool

def is_any_tree(polygon_obj_type, id):
    if polygon_obj_type == 'building':
        object = Building.objects.get(id_0 = id)
    elif polygon_obj_type == 'location':
        object = Location.objects.get(id_0 = id)
    elif polygon_obj_type == 'pool':
        object = SwimmingPool.objects.get(id = id)
    elif polygon_obj_type == 'area':
        object = CampingArea.objects.get(id_0 = id)
    tree_ds = Tree.objects.all()
    count_tree = 0
    for item in tree_ds:
        if item.geom.within(object.geom):
            count_tree += 1
    return count_tree
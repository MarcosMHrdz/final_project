import shapely.geometry as geometry
import shapely.ops as ops
import pyproj
import pandas as pd

# https://www.keene.edu/campus/maps/tool/
coordinates = pd.read_csv('D:/Proyecto ironhack/files/spain_frontiers.csv', decimal=',', sep=';')
coordinates = coordinates.values.tolist()




# Convert to Shapely Polygon
polygon = geometry.Polygon(coordinates)

# Convert polygon to Cartesian coordinates (UTM)
proj = pyproj.Proj(proj='utm', zone=33, ellps='WGS84')
project = lambda x, y: proj(x, y, inverse=False)
polygon_utm = ops.transform(project, polygon)


def create_grid(polygon, grid_spacing):
    minx, miny, maxx, maxy = polygon.bounds
    grid_points = []
    x = minx
    while x < maxx:
        y = miny
        while y < maxy:
            point = geometry.Point(x, y)
            if polygon.contains(point):
                grid_points.append((x, y))
            y += grid_spacing
        x += grid_spacing
    return grid_points


polygon = geometry.Polygon(coordinates)

grid_spacing = 30 * 1609.34  # 30 miles in meters
grid_points_utm = create_grid(polygon_utm, grid_spacing)

project_inv = lambda x, y: proj(x, y, inverse=True)
grid_points_geo = [project_inv(x, y) for x, y in grid_points_utm]

df_country_coordinates = pd.DataFrame(grid_points_geo, columns=['longitude', 'latitude'])

df_country_coordinates.to_csv('D:/Proyecto ironhack/files/spain_coordenates_mesh.csv', index=False)
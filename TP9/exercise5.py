
import functools

def bounding_box(pts):
    x_coords = list(map(lambda pt: pt[0], pts))
    y_coords = list(map(lambda pt: pt[1], pts))
    
    xmin = functools.reduce(lambda a, b: a if a < b else b, x_coords)
    ymin = functools.reduce(lambda a, b: a if a < b else b, y_coords)
    xmax = functools.reduce(lambda a, b: a if a > b else b, x_coords)
    ymax = functools.reduce(lambda a, b: a if a > b else b, y_coords)
    
    return (xmin, ymin, xmax, ymax)

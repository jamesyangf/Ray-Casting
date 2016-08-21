import math
import data

def scale_vector(vector, scalar):
    scale = data.Vector((vector.x*scalar),(vector.y*scalar),(vector.z * scalar))
    return scale

def dot_vector(vector1, vector2):
    multi = (vector1.x*vector2.x)+(vector1.y*vector2.y)+(vector1.z*vector2.z)
    return multi

def length_vector(vector):
    length = math.sqrt((vector.x**2)+(vector.y**2)+(vector.z**2))
    return length

def normalize_vector(vector):
    length = math.sqrt((vector.x**2)+(vector.y**2)+(vector.z**2))
    newVector = data.Vector((vector.x/length),(vector.y/length),(vector.z/length))
    return newVector

def difference_point(point1, point2):
    pointDiff = data.Point((point1.x-point2.x),(point1.y-point2.y),(point1.z-point2.z))
    return pointDiff                                   

def difference_vector(vector1, vector2):
    vectorDiff = data.Vector((vector1.x-vector2.x),(vector1.y-vector2.y),(vector1.z-vector2.z))
    return vectorDiff

def translate_point(point, vector):
    translate = data.Point((point.x+vector.x),(point.y+vector.y),(point.z+vector.z))
    return translate

def vector_from_to(from_point, to_point):
    vectorFrom = data.Vector((to_point.x-from_point.x),(to_point.y-from_point.y),(to_point.z-from_point.z))
    return vectorFrom

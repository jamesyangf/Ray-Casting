import vector_math
from data import *
import math

def sphere_intersection_point(ray, sphere):
    A = vector_math.dot_vector(ray.dir, ray.dir)
    B = vector_math.dot_vector(vector_math.scale_vector((vector_math.difference_point(ray.pt, sphere.center)),2), ray.dir)
    C = (vector_math.dot_vector((vector_math.difference_point(ray.pt , sphere.center)) , (vector_math.difference_point(ray.pt , sphere.center)))) - sphere.radius**2
    disc = B*B +(-4)*A*C
    if disc < 0:
        return None

    t1 = ((-B+math.sqrt(disc))/(2.0*A))
    t2 = ((-B-math.sqrt(disc))/(2.0*A))
        
    if t1 > 0 and t2 > 0:
        if t1 < t2:
            return vector_math.translate_point(ray.pt , vector_math.scale_vector(ray.dir,t1))
        else:
            return vector_math.translate_point(ray.pt , vector_math.scale_vector(ray.dir,t2))

    elif t1 < 0 and t2 < 0:
        return None

    elif (t1 >0 and t2 < 0):
            return vector_math.translate_point(ray.pt , vector_math.scale_vector(ray.dir,t1))
    elif (t2 >0 and t1 < 0):
            return vector_math.translate_point(ray.pt , vector_math.scale_vector(ray.dir,t2))
    else:
        return None
    
def find_intersection_points(sphere_list, ray):
    newList = []
    for i in sphere_list:
        if sphere_intersection_point(ray,i) != None:
            newList.append((i,sphere_intersection_point(ray,i)))
    return newList

def sphere_normal_at_point(sphere, point):
    vectorFrom = vector_math.vector_from_to(sphere.center,point)
    vectNorm = vector_math.normalize_vector(vectorFrom)
    return vectNorm
        
        
        
    

    
    


    
    

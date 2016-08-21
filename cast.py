import math
import unittest
from data import *
from collisions import *
from vector_math import *
import sys


def color_converter(color):#ranges the color from 0 to 255
        return Color(min(int(color.r * 255), 255),
                     min(int(color.g * 255), 255),
                     min(int(color.b * 255), 255))


def spec(p, ray, sphere_list, color, light, mine):
        eye = Point(0.0, 0.0, -14.0)
        normal = sphere_normal_at_point(p[mine][0], p[mine][1])
        trans = translate_point(p[mine][1], scale_vector((normal), (0.01)))
        light_dir = normalize_vector(vector_from_to(trans, light.pt))
        dotProduct = dot_vector(normal, light_dir)
        ref = (difference_vector(normalize_vector(vector_from_to(trans, light.pt)),  
	      scale_vector(normal, 2 * dot_vector(normal, light_dir))))                      
        vect_dir = normalize_vector(vector_from_to(eye, trans))
        intense = dot_vector(ref, vect_dir)
        if intense > 0:
                return Color((light.color.r * p[mine][0].finish.specular * 
			     (intense ** (1/ p[mine][0].finish.roughness))),
                             (light.color.g * p[mine][0].finish.specular * 
			     (intense ** (1/ p[mine][0].finish.roughness))),
                             (light.color.b * p[mine][0].finish.specular * 
			     (intense ** (1/ p[mine][0].finish.roughness))))
        else:
                return Color(0.0, 0.0, 0.0)



def diffuse(p, sphere_list, ray, color, light, mine):
	normal = sphere_normal_at_point(p[mine][0], p[mine][1])
        trans = translate_point(p[mine][1], scale_vector((normal), (0.01)))
        light_dir = normalize_vector(vector_from_to(trans, light.pt))
        dot = dot_vector(normal, light_dir)
	r = Ray(trans, light_dir)
	sphere_int = sphere_intersection_point(r, p[mine][0])
        theList = find_intersection_points(sphere_list, r)
	newInt = spec(p, ray, sphere_list, color, light, mine)
	
	if theList != []:
		if (length_vector(vector_from_to(trans, theList[0][1])) < 
		    length_vector(vector_from_to(trans, light.pt))):
			return Color(0.0, 0.0, 0.0)
	
	else: 
		if dot <= 0:
                	return Color(0.0, 0.0, 0.0)

 		else:
			return Color((dot * light.color.r * 
				      p[mine][0].color.r * 
		                      p[mine][0].finish.diffuse) + newInt.r,
                             	     (dot * light.color.g * 
				      p[mine][0].color.g * 
				      p[mine][0].finish.diffuse) + newInt.g,
                             	     (dot * light.color.b * 
				      p[mine][0].color.b * 
				      p[mine][0].finish.diffuse) + newInt.b)
	


def find_color(p, sphere_list, ray, color, light):
	mine = 0
        for i in range(1, len(p)):
		if (length_vector(vector_from_to(ray.pt, p[mine][1])) > 
	            length_vector(vector_from_to(ray.pt, p[i][1]))):
			mine = i
	d = diffuse(p, sphere_list, ray, color, light, mine)
	return Color((p[mine][0].color.r  * 
		      p[mine][0].finish.ambient * color.r) + d.r,
                     (p[mine][0].color.g  * 
		      p[mine][0].finish.ambient * color.g) + d.g,
                     (p[mine][0].color.b  * 
		      p[mine][0].finish.ambient * color.b) + d.b)

def cast_ray(ray, sphere_list, color, light):
	
	p = find_intersection_points(sphere_list, ray)
	if p == []:
                return Color(1.0, 1.0, 1.0)
        else:	
		return find_color(p, sphere_list, ray, color, light)
		
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
        out = open('image.ppm','w')
        print >> out, 'P3'
        print >> out, width, height
        print >> out, 255
        y_interval = (max_y - min_y) / float(height)
        x_interval = (max_x - min_x) / float(width)
        for j in range(0, height):
                for i in range(0, width):
                        x = min_x + x_interval * i
                        y = max_y - y_interval * j
                        z = 0
                        point = Point(x, y, z)
                        vector = vector_from_to(eye_point, point)
                        theRay = Ray(eye_point, vector)
                        theColor = cast_ray(theRay, sphere_list, color, light)
                        result = color_converter(theColor)
                        print >> out, int(result.r), int(result.g), int(result.b)





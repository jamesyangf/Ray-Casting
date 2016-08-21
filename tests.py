import unittest
import data
import vector_math
import collisions
import cast

class TestData(unittest.TestCase):
    def test_point_1(self):
        test_point1 = data.Point(10,20,30)
        test_point2 = data.Point(15,25,35)
        
        self.assertEqual(test_point1.x,10)
        self.assertEqual(test_point1.y,20)
        self.assertEqual(test_point1.z,30)

        self.assertEqual(test_point2.x,15)
        self.assertEqual(test_point2.y,25)
        self.assertEqual(test_point2.z,35)

    def test_point_equal(self):
        eqPoint1 = data.Point.__eq__(data.Point(2.1,3.1,4.1),
                                     data.Point(2.1,3.1,4.1))
        eqPoint2 = data.Point.__eq__(data.Point(3.4,2.5,9.5),
                                     data.Point(5.5,7.6,8.5))

        self.assertAlmostEqual(eqPoint1,True)
        self.assertAlmostEqual(eqPoint2,False)

    def test_vector_1(self):
        test_vector1 = data.Vector(2,5,7)
        test_vector2 = data.Vector(4,7,9)
        
        self.assertEqual(test_vector1.x,2)
        self.assertEqual(test_vector1.y,5)
        self.assertEqual(test_vector1.z,7)

        self.assertEqual(test_vector2.x,4)
        self.assertEqual(test_vector2.y,7)
        self.assertEqual(test_vector2.z,9)

    def test_vector_equal(self):
        eqVector1 = data.Vector. __eq__(data.Vector(9.4,8.7,6.3),
                                        data.Vector(9.4,8.7,6.3))
        eqVector2 = data.Vector. __eq__(data.Vector(4.2,3.6,2.9),
                                        data.Vector(6.7,9.4,1.4))

        self.assertAlmostEqual(eqVector1,True)
        self.assertAlmostEqual(eqVector2,False)

    def test_ray_1(self):
        test_ray1 = data.Ray(data.Point(1,3,5),data.Vector(6,8,10))
        test_ray2 = data.Ray(data.Point(2,4,6),data.Vector(7,3,5))

        self.assertEqual(test_ray1.pt.x,1)
        self.assertEqual(test_ray1.pt.y,3)
        self.assertEqual(test_ray1.pt.z,5)

        self.assertEqual(test_ray1.dir.x,6)
        self.assertEqual(test_ray1.dir.y,8)
        self.assertEqual(test_ray1.dir.z,10)

        self.assertEqual(test_ray2.pt.x,2)
        self.assertEqual(test_ray2.pt.y,4)
        self.assertEqual(test_ray2.pt.z,6)

        self.assertEqual(test_ray2.dir.x,7)
        self.assertEqual(test_ray2.dir.y,3)
        self.assertEqual(test_ray2.dir.z,5)

    def test_ray_equal(self):
        eqRay1 = data.Ray.__eq__(data.Ray(data.Point(2.1,3.1,4.1), data.Vector(3.2,4.2,5.2)),
                                 data.Ray(data.Point(2.1,3.1,4.1), data.Vector(3.2,4.2,5.2)))
        eqRay2 = data.Ray.__eq__(data.Ray(data.Point(2.4,6.8,2.7), data.Vector(3.2,4.0,2.7)),
                                 data.Ray(data.Point(34.1,98.1,2.7), data.Vector(98.2,23.9,76.2)))


        self.assertAlmostEqual(eqRay1,True)
        self.assertAlmostEqual(eqRay2,False)
        

    def test_sphere_1(self):
        test_sphere1 = data.Sphere(data.Point(12,14,16),15,data.Color(1,1,1),data.Finish(1,1,1,1))
        test_sphere2 = data.Sphere(data.Point(13,17,19),23,data.Color(1,1,1),data.Finish(1,1,1,1))

        self.assertEqual(test_sphere1.center.x,12)
        self.assertEqual(test_sphere1.center.y,14)
        self.assertEqual(test_sphere1.center.z, 16)
        self.assertAlmostEqual(test_sphere1.radius, 15)

        self.assertEqual(test_sphere2.center.x,13)
        self.assertEqual(test_sphere2.center.y,17)
        self.assertEqual(test_sphere2.center.z, 19)
        self.assertAlmostEqual(test_sphere2.radius, 23)

 

    def test_scale_vector(self):
        test_scale_vector = vector_math.scale_vector(data.Vector(2,4,6),2)
        test_scale_vector2 = vector_math.scale_vector(data.Vector(3,6,8),1)

        self.assertEqual(test_scale_vector.x,4)
        self.assertEqual(test_scale_vector.y,8)
        self.assertEqual(test_scale_vector.z,12)

        self.assertEqual(test_scale_vector2.x,3)
        self.assertEqual(test_scale_vector2.y,6)
        self.assertEqual(test_scale_vector2.z,8)

        

    def test_dot_vector(self):
        test_dot_vector = vector_math.dot_vector(data.Vector(1,2,3),data.Vector(3,5,7))
        test_dot_vector2 = vector_math.dot_vector(data.Vector(5,3,7),data.Vector(1,6,3))


        self.assertEqual(test_dot_vector,34)
        self.assertEqual(test_dot_vector2,44)

    def test_length_vector(self):
        test_length_vector = vector_math.length_vector(data.Vector(2,7,8))

        self.assertAlmostEqual(test_length_vector, 10.81665382)

        test_length_vector2 = vector_math.length_vector(data.Vector(4,8,9))

        self.assertAlmostEqual(test_length_vector2, 12.68857754044952)


    def test_normalize_vector(self):
        test_normalize_vector = vector_math.normalize_vector(data.Vector(1,4,7))

        self.assertAlmostEqual(test_normalize_vector.x,0.12309149097933272)
        self.assertAlmostEqual(test_normalize_vector.y,0.4923659639173309)
        self.assertAlmostEqual(test_normalize_vector.z,0.8616404368553291)

        test_normalize_vector2 = vector_math.normalize_vector(data.Vector(4,7,12))

        self.assertAlmostEqual(test_normalize_vector2.x,0.27668578554642986)
        self.assertAlmostEqual(test_normalize_vector2.y,0.48420012470625223)
        self.assertAlmostEqual(test_normalize_vector2.z,0.8300573566392896)

    def test_difference_point(self):
        test_difference_point = vector_math.difference_point(data.Point(2,6,8),data.Point(1,4,3))

        self.assertEqual(test_difference_point.x,1)
        self.assertEqual(test_difference_point.y,2)
        self.assertEqual(test_difference_point.z,5)

        test_difference_point2 = vector_math.difference_point(data.Point(23,45,19),data.Point(23,12,34))

        self.assertEqual(test_difference_point2.x,0)
        self.assertEqual(test_difference_point2.y,33)
        self.assertEqual(test_difference_point2.z,-15)



    def test_difference_vector(self):
        test_difference_vector = vector_math.difference_vector(data.Vector(30,44,63), data.Vector(12,14,13))

        self.assertEqual(test_difference_vector.x,18)
        self.assertEqual(test_difference_vector.y,30)
        self.assertEqual(test_difference_vector.z,50)

        test_difference_vector2 = vector_math.difference_vector(data.Vector(23,14,83), data.Vector(9,4,93))

        self.assertEqual(test_difference_vector2.x,14)
        self.assertEqual(test_difference_vector2.y,10)
        self.assertEqual(test_difference_vector2.z,-10)

    def test_translate_point(self):
        testTransPoint = vector_math.translate_point(data.Point(24,43,65),data.Vector(3,4,5))

        self.assertEqual(testTransPoint.x,27)
        self.assertEqual(testTransPoint.y,47)
        self.assertEqual(testTransPoint.z,70)

        testTransPoint2 = vector_math.translate_point(data.Point(81,75,21),data.Vector(90,6,12))

        self.assertEqual(testTransPoint2.x,171)
        self.assertEqual(testTransPoint2.y,81)
        self.assertEqual(testTransPoint2.z,33)
        
    def test_vector_from_to(self):
        vectorFromTo = vector_math.vector_from_to(data.Point(3,6,10),data.Point(9,18,40))

        self.assertEqual(vectorFromTo.x,6)
        self.assertEqual(vectorFromTo.y,12)
        self.assertEqual(vectorFromTo.z,30)

        vectorFromTo2 = vector_math.vector_from_to(data.Point(25,72,11),data.Point(8,54,39))

        self.assertEqual(vectorFromTo2.x,-17)
        self.assertEqual(vectorFromTo2.y,-18)
        self.assertEqual(vectorFromTo2.z,28)

    def test_sphere_intersection_point(self):
        s_r1 = collisions.sphere_intersection_point((data.Ray(data.Point(-1,-1,3),data.Vector(1,1,1))),data.Sphere(data.Point(1,1,1),2,data.Color(1,1,1),data.Finish(1,1,1,1)))
        s_r2 = collisions.sphere_intersection_point((data.Ray(data.Point(2,4,7),data.Vector(9,5,8))),data.Sphere(data.Point(4,7,2),10,data.Color(1,1,1),data.Finish(1,1,1,1)))
        s_r3 = collisions.sphere_intersection_point((data.Ray(data.Point(0,0,0),data.Vector(1000,1000,1000))),data.Sphere(data.Point(5000,4002,2034),1,data.Color(1,1,1),data.Finish(1,1,1,1)))

        self.assertEqual(s_r1, None)
 

        self.assertAlmostEqual(s_r2.x, 7.077210596410908)
        self.assertAlmostEqual(s_r2.y, 6.820672553561616)
        self.assertAlmostEqual(s_r2.z, 11.513076085698586)

        self.assertEqual(s_r3, None)
 

    def test_find_intersection_points(self):

        fip2 = collisions.find_intersection_points([data.Sphere(data.Point(0,0,0),6,data.Color(1,1,1),data.Finish(0,0,0,0)),
                                                    data.Sphere(data.Point(250,370,400),2,data.Color(1,1,1),data.Finish(0,0,0,0))],
                                                    data.Ray(data.Point(0,-1,0),
                                                             data.Vector(0,7,0)))
        self.assertEqual(fip2,[(data.Sphere(data.Point(0,0,0),6,data.Color(1,1,1),data.Finish(0,0,0,0)), data.Point(0,6,0))])

        fip3 = collisions.find_intersection_points([data.Sphere(data.Point(5,5,0),6,data.Color(1,1,1),data.Finish(1,1,1,1)),
                                                    data.Sphere(data.Point(5,15,0),6,data.Color(1,1,1),data.Finish(1,1,1,1))],
                                                    data.Ray(data.Point(100,200,0),
                                                             data.Vector(0,20,0)))
        self.assertEqual(fip3,[])

 

   
    def test_sphere_normal_at_point(self):
        snap = collisions.sphere_normal_at_point(data.Sphere(data.Point(1,1,0),1,data.Color(1,1,1),data.Finish(1,1,1,1)),data.Point(2,2,2))
        snap2 = collisions.sphere_normal_at_point(data.Sphere(data.Point(2,2,2),3,data.Color(1,1,1),data.Finish(1,1,1,1)),data.Point(5,6,7))

        self.assertAlmostEqual(snap.x,.4082482905)
        self.assertAlmostEqual(snap.y,.4082482905)
        self.assertAlmostEqual(snap.z,.8164965809)


        self.assertAlmostEqual(snap2.x,.4242640687)
        self.assertAlmostEqual(snap2.y,.5656854249)
        self.assertAlmostEqual(snap2.z,.7071067812)


    def test_cast_ray(self):
        cr1 = cast.cast_ray(data.Ray(data.Point(0,-10,0),data.Vector(0,7,0)),[data.Sphere(data.Point(1000,1000,1000),1,data.Color(1,1,1),data.Finish(1,1,1,1)),data.Sphere(data.Point(0,0,0),1,data.Color(1,1,1),data.Finish(1,1,1,1))])

        self.assertEqual(cr1,0)
        
                               
if __name__ == "__main__":
    unittest.main()

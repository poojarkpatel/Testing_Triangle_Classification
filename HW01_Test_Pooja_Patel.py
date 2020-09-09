import unittest
from HW01_Pooja_Patel import Triangle
import math
class TestTriangles(unittest.TestCase):
    """ Helps to test all functions """

    def test__init__(self):
        t: Triangle = Triangle(1, 2, 3)
        self.assertEqual(t.side1, 1)
        self.assertEqual(t.side2, 2)
        self.assertEqual(t.side3, 3)

    def test_classify_triangle(self):
        """Tests classify triangle method"""

        self.assertEqual(Triangle(1, 1, 1).classify_triangle(), "Equilateral Triangle")
        self.assertEqual(Triangle(1, 2, 3).classify_triangle(), "Scalene Triangle")
        self.assertEqual(Triangle(1, 2, 2).classify_triangle(), "Isosceles Triangle")
        self.assertEqual(Triangle(3, 4, 5).classify_triangle(), "Right and Scalene Triangle")
        self.assertEqual(Triangle(1, 1, 1.41).classify_triangle(), "Right and Isosceles Triangle")
        self.assertNotEqual(Triangle(1, 1, 1).classify_triangle(), "Scalene Triangle")
        self.assertNotEqual(Triangle(1, 2, 3).classify_triangle(), "Isosceles Triangle")
        self.assertNotEqual(Triangle(1, 2, 2).classify_triangle(), "Equilateral Triangle")
        self.assertNotEqual(Triangle(1, 1, 1.41).classify_triangle(), "Right and Scalene Triangle")
        self.assertNotEqual(Triangle(3, 4, 5).classify_triangle(), "Right and Isosceles Triangle")
        with self.assertRaises(ValueError):
            Triangle(1, 6, 8).classify_triangle()

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

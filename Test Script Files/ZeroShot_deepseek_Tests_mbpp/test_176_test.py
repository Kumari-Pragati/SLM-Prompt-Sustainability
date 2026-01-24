import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):

    def test_perimeter_triangle(self):
        self.assertEqual(perimeter_triangle(3,4,5), 12)
        self.assertEqual(perimeter_triangle(5,12,13), 30)
        self.assertEqual(perimeter_triangle(7,8,9), 24)
        self.assertEqual(perimeter_triangle(10,20,30), 60)

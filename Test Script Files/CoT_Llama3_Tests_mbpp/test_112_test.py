import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):

    def test_perimeter_typical(self):
        self.assertEqual(perimeter(10,5), 30)

    def test_perimeter_zero_height(self):
        self.assertEqual(perimeter(10,0), 20)

    def test_perimeter_zero_diameter(self):
        self.assertEqual(perimeter(0,5), 10)

    def test_perimeter_negative_diameter(self):
        with self.assertRaises(TypeError):
            perimeter(-10,5)

    def test_perimeter_negative_height(self):
        with self.assertRaises(TypeError):
            perimeter(10,-5)

    def test_perimeter_non_numeric_diameter(self):
        with self.assertRaises(TypeError):
            perimeter('ten',5)

    def test_perimeter_non_numeric_height(self):
        with self.assertRaises(TypeError):
            perimeter(10,'five')

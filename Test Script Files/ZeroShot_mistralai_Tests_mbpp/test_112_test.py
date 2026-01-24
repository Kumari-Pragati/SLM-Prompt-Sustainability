import unittest
from112_code import perimeter

class TestPerimeter(unittest.TestCase):

    def test_perimeter_of_square(self):
        self.assertEqual(perimeter(4, 4), 24)

    def test_perimeter_of_rectangle(self):
        self.assertEqual(perimeter(4, 2), 16)

    def test_perimeter_of_circle(self):
        radius = 5
        diameter = 2 * radius
        height = radius
        self.assertAlmostEqual(perimeter(diameter, height), 31.41592653589793)

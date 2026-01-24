import unittest
from mbpp_163_code import tan, pi
from your_module import area_polygon  # Assuming the function is defined in a module named 'your_module'

class TestAreaPolygon(unittest.TestCase):

    def test_area_polygon_with_sides_and_sides_equal_to_3(self):
        self.assertAlmostEqual(area_polygon(3, 3), 4.5 * pi, delta=0.01)

    def test_area_polygon_with_sides_and_sides_equal_to_4(self):
        self.assertAlmostEqual(area_polygon(4, 4), (4 * pi ** 2) / 4, delta=0.01)

    def test_area_polygon_with_sides_and_sides_equal_to_5(self):
        self.assertAlmostEqual(area_polygon(5, 5), (5 * (5 ** 2) * (pi / 5)) / 2, delta=0.01)

    def test_area_polygon_with_sides_and_sides_not_equal(self):
        self.assertAlmostEqual(area_polygon(3, 4), (12 * (3 ** 2) * (pi / 6)) / tan(pi / 3), delta=0.01)

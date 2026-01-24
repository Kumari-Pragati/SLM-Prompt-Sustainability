import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (1, 4))
        self.assertEqual(find_Points(3, 4, 1, 2), (1, 4))
        self.assertEqual(find_Points(-1, 0, 1, 2), (-1, 2))
        self.assertEqual(find_Points(0, -1, 1, 2), (-1, 2))

    def test_equal_coordinates(self):
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, -1))
        self.assertEqual(find_Points(-1, -1, -1, -1), (-1, -1))

    def test_one_coordinate_equal(self):
        self.assertEqual(find_Points(1, 2, 1, 3), (-1, 3))
        self.assertEqual(find_Points(1, 2, -1, 2), (-1, 2))

    def test_one_coordinate_none(self):
        self.assertEqual(find_Points(1, None, 2, 3), (1, 3))
        self.assertEqual(find_Points(None, 2, 1, 3), (1, 3))

    def test_negative_values(self):
        self.assertEqual(find_Points(-5, -4, -3, -2), (-5, -4))
        self.assertEqual(find_Points(-5, -4, -3, -2), (-5, -4))

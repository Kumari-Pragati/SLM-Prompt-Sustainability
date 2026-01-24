import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_find_points_with_different_left_and_right(self):
        self.assertEqual(find_Points(1, 3, 5, 7), (1, 7))
        self.assertEqual(find_Points(-2, 0, 3, 5), (-2, 5))
        self.assertEqual(find_Points(0, 2, -1, 4), (-1, 4))

    def test_find_points_with_same_left_and_right(self):
        self.assertEqual(find_Points(1, 1, 3, 3), (-1, -1))
        self.assertEqual(find_Points(-2, -2, 0, 0), (-2, -2))
        self.assertEqual(find_Points(0, 0, 2, 2), (-1, -1))

    def test_find_points_with_one_side_equal(self):
        self.assertEqual(find_Points(1, 3, 1, 3), (-1, 3))
        self.assertEqual(find_Points(-2, 0, -2, 0), (-2, 0))
        self.assertEqual(find_Points(0, 2, 0, 2), (0, 2))

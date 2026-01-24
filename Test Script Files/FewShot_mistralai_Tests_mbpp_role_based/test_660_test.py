import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):
    def test_valid_points(self):
        self.assertEqual(find_Points(1, 3, 2, 4), (1, 4))
        self.assertEqual(find_Points(5, 7, 3, 9), (3, 9))
        self.assertEqual(find_Points(-2, 0, -1, 1), (-2, 1))

    def test_same_points(self):
        self.assertEqual(find_Points(2, 2, 3, 3), (-1, -1))

    def test_invalid_points(self):
        self.assertRaises(ValueError, find_Points, -1, 0, 1, 0)
        self.assertRaises(ValueError, find_Points, 1, 1, -1, -1)
        self.assertRaises(ValueError, find_Points, 0, 0, 0, 0)

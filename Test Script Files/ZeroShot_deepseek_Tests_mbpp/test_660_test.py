import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_same_range(self):
        self.assertEqual(find_Points(1, 2, 1, 2), (-1, -1))

    def test_different_range(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (1, 4))

    def test_same_left_point(self):
        self.assertEqual(find_Points(1, 2, 1, 3), (1, 3))

    def test_same_right_point(self):
        self.assertEqual(find_Points(2, 3, 2, 3), (2, 3))

    def test_same_left_and_right_point(self):
        self.assertEqual(find_Points(2, 2, 2, 2), (-1, -1))

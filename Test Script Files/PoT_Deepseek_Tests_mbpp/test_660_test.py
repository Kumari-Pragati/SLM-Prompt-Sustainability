import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Points(1, 3, 2, 4), (1, 4))

    def test_edge_case_same_left_right_values(self):
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, -1))

    def test_boundary_case_left_greater_than_right(self):
        self.assertEqual(find_Points(2, 1, 2, 1), (-1, 2))

    def test_boundary_case_right_greater_than_left(self):
        self.assertEqual(find_Points(1, 2, 1, 2), (1, -1))

    def test_corner_case_negative_values(self):
        self.assertEqual(find_Points(-1, 3, -2, 4), (-1, 4))

    def test_corner_case_zero_values(self):
        self.assertEqual(find_Points(0, 3, 0, 4), (0, 4))

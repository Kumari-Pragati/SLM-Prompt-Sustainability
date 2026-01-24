import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(closest_num(10), 9)
        self.assertEqual(closest_num(15), 14)
        self.assertEqual(closest_num(20), 19)

    def test_edge_cases(self):
        self.assertEqual(closest_num(0), -1)
        self.assertEqual(closest_num(-10), -11)

    def test_boundary_cases(self):
        self.assertEqual(closest_num(1), 0)
        self.assertEqual(closest_num(-1), -2)

    def test_corner_cases(self):
        self.assertEqual(closest_num(2), 1)
        self.assertEqual(closest_num(-2), -3)

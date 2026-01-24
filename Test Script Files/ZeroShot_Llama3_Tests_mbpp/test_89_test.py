import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):

    def test_positive_num(self):
        self.assertEqual(closest_num(1), 0)

    def test_negative_num(self):
        self.assertEqual(closest_num(-1), -2)

    def test_zero_num(self):
        self.assertEqual(closest_num(0), -1)

    def test_positive_num_edge_case(self):
        self.assertEqual(closest_num(2), 1)

    def test_negative_num_edge_case(self):
        self.assertEqual(closest_num(-2), -3)

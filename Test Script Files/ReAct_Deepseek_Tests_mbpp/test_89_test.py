import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(closest_num(10), 9)

    def test_boundary_case_zero(self):
        self.assertEqual(closest_num(0), -1)

    def test_negative_number(self):
        self.assertEqual(closest_num(-5), -6)

    def test_large_number(self):
        self.assertEqual(closest_num(1000000), 999999)

    def test_float_number(self):
        self.assertEqual(closest_num(10.5), 10.5 - 1)

    def test_edge_case_one(self):
        self.assertEqual(closest_num(1), 0)

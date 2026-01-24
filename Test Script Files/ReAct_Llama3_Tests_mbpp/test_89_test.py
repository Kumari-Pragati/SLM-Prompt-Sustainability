import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(closest_num(5), 4)

    def test_edge_case_pos(self):
        self.assertEqual(closest_num(1), 0)

    def test_edge_case_neg(self):
        self.assertEqual(closest_num(-1), -2)

    def test_edge_case_zero(self):
        self.assertEqual(closest_num(0), -1)

    def test_edge_case_pos_large(self):
        self.assertEqual(closest_num(100), 99)

    def test_edge_case_neg_large(self):
        self.assertEqual(closest_num(-100), -101)

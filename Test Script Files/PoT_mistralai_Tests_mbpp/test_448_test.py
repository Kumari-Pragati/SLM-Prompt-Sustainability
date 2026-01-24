import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)

    def test_typical_cases(self):
        self.assertEqual(cal_sum(3), 8)
        self.assertEqual(cal_sum(4), 13)
        self.assertEqual(cal_sum(5), 18)

    def test_edge_cases(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)
        self.assertEqual(cal_sum(3), 8)
        self.assertEqual(cal_sum(4), 13)
        self.assertEqual(cal_sum(5), 18)
        self.assertEqual(cal_sum(6), 23)
        self.assertEqual(cal_sum(7), 28)
        self.assertEqual(cal_sum(8), 33)
        self.assertEqual(cal_sum(9), 38)

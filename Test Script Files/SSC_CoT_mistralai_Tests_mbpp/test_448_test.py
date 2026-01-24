import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)
        self.assertEqual(cal_sum(3), 8)
        self.assertEqual(cal_sum(4), 11)
        self.assertEqual(cal_sum(5), 13)

    def test_edge_cases(self):
        self.assertEqual(cal_sum(6), 15)
        self.assertEqual(cal_sum(7), 17)
        self.assertEqual(cal_sum(8), 19)
        self.assertEqual(cal_sum(9), 21)
        self.assertEqual(cal_sum(10), 23)

    def test_negative_input(self):
        self.assertRaises(ValueError, cal_sum, -1)
        self.assertRaises(ValueError, cal_sum, -2)
        self.assertRaises(ValueError, cal_sum, -3)

    def test_zero_input(self):
        self.assertEqual(cal_sum(0), 3)

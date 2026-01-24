import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)

    def test_edge_inputs(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)
        self.assertEqual(cal_sum(3), 8)
        self.assertEqual(cal_sum(4), 11)
        self.assertEqual(cal_sum(5), 13)

    def test_complex_inputs(self):
        self.assertEqual(cal_sum(6), 15)
        self.assertEqual(cal_sum(7), 17)
        self.assertEqual(cal_sum(8), 19)
        self.assertEqual(cal_sum(9), 21)
        self.assertEqual(cal_sum(10), 23)
        self.assertEqual(cal_sum(11), 25)
        self.assertEqual(cal_sum(12), 27)
        self.assertEqual(cal_sum(13), 29)
        self.assertEqual(cal_sum(14), 31)
        self.assertEqual(cal_sum(15), 33)
        self.assertEqual(cal_sum(16), 35)
        self.assertEqual(cal_sum(17), 37)
        self.assertEqual(cal_sum(18), 39)
        self.assertEqual(cal_sum(19), 41)
        self.assertEqual(cal_sum(20), 43)

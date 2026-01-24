import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):

    def test_cal_sum_typical(self):
        self.assertEqual(cal_sum(3), 8)
        self.assertEqual(cal_sum(4), 9)
        self.assertEqual(cal_sum(5), 12)

    def test_cal_sum_edge(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)

    def test_cal_sum_invalid(self):
        with self.assertRaises(TypeError):
            cal_sum('a')

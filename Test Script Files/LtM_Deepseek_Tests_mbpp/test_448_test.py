import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)

    def test_boundary_conditions(self):
        self.assertEqual(cal_sum(3), 9)
        self.assertEqual(cal_sum(4), 17)
        self.assertEqual(cal_sum(5), 30)

    def test_complex_cases(self):
        self.assertEqual(cal_sum(6), 55)
        self.assertEqual(cal_sum(7), 96)
        self.assertEqual(cal_sum(8), 164)

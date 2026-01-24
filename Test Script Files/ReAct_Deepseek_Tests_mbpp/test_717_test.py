import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):

    def test_avg_calc_typical_case(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(avg_calc(data), 3.0)

    def test_avg_calc_single_element(self):
        data = [10]
        self.assertEqual(avg_calc(data), 10)

    def test_avg_calc_empty_list(self):
        data = []
        self.assertEqual(avg_calc(data), 0.0)

    def test_avg_calc_negative_numbers(self):
        data = [-1, -2, -3, -4, -5]
        self.assertAlmostEqual(avg_calc(data), -3.0)

    def test_avg_calc_mixed_numbers(self):
        data = [1, -2, 3, -4, 5]
        self.assertAlmostEqual(avg_calc(data), 1.0)

    def test_avg_calc_float_numbers(self):
        data = [1.5, 2.5, 3.5, 4.5, 5.5]
        self.assertAlmostEqual(avg_calc(data), 3.5)

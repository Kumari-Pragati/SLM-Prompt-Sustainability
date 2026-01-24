import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(avg_calc([]), None)

    def test_single_element_list(self):
        self.assertEqual(avg_calc([1]), 1.0)

    def test_positive_numbers_list(self):
        self.assertEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)

    def test_negative_numbers_list(self):
        self.assertEqual(avg_calc([-1, -2, -3, -4, -5]), -3.0)

    def test_mixed_numbers_list(self):
        self.assertEqual(avg_calc([1, -2, 3, -4, 5]), 1.0)

    def test_large_numbers_list(self):
        self.assertEqual(avg_calc([1000000, 2000000, 3000000, 4000000, 5000000]), 3000000.0)

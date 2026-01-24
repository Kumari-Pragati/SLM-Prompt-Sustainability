import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(avg_calc([5]), 5)

    def test_multiple_elements(self):
        self.assertAlmostEqual(avg_calc([1, 2, 3, 4, 5]), 3)

    def test_empty_list(self):
        self.assertEqual(avg_calc([]), 0)

    def test_large_numbers(self):
        self.assertAlmostEqual(avg_calc([1000000, 2000000, 3000000]), 2000000)

    def test_negative_numbers(self):
        self.assertAlmostEqual(avg_calc([-1, -2, -3, -4, -5]), -3)

    def test_float_numbers(self):
        self.assertAlmostEqual(avg_calc([1.5, 2.5, 3.5]), 2.5)

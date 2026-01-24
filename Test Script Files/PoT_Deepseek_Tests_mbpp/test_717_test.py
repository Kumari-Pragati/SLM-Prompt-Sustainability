import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(avg_calc([5]), 5)

    def test_typical_case(self):
        self.assertAlmostEqual(avg_calc([1, 2, 3, 4, 5]), 3)

    def test_empty_list(self):
        self.assertEqual(avg_calc([]), 0)

    def test_large_number_list(self):
        self.assertAlmostEqual(avg_calc(list(range(1, 1001))), 500.5)

    def test_negative_numbers(self):
        self.assertAlmostEqual(avg_calc([-1, -2, -3, -4, -5]), -3)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(avg_calc([-1, 2, -3, 4, -5]), 0)

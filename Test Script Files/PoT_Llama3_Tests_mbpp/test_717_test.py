import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)

    def test_single_element(self):
        self.assertEqual(avg_calc([1]), 1.0)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            avg_calc([])

    def test_negative_numbers(self):
        self.assertEqual(avg_calc([-1, -2, -3, -4, -5]), -3.0)

    def test_mixed_numbers(self):
        self.assertEqual(avg_calc([1, -2, 3, -4, 5]), 1.0)

    def test_float_numbers(self):
        self.assertEqual(avg_calc([1.0, 2.0, 3.0, 4.0, 5.0]), 3.0)

    def test_large_numbers(self):
        self.assertEqual(avg_calc([1000, 2000, 3000, 4000, 5000]), 3000.0)

    def test_small_numbers(self):
        self.assertEqual(avg_calc([0.1, 0.2, 0.3, 0.4, 0.5]), 0.3)

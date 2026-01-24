import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):
    def test_sum_in_range_positive_numbers(self):
        self.assertEqual(sum_in_Range(3, 7), 20)
        self.assertEqual(sum_in_Range(1, 9), 24)
        self.assertEqual(sum_in_Range(10, 20), 190)

    def test_sum_in_range_zero_and_negative_numbers(self):
        self.assertEqual(sum_in_Range(0, 0), 0)
        self.assertEqual(sum_in_Range(-1, 0), 0)
        self.assertEqual(sum_in_Range(-5, -1), 4)

    def test_sum_in_range_boundary_conditions(self):
        self.assertEqual(sum_in_Range(1, 1), 0)
        self.assertEqual(sum_in_Range(2, 2), 1)
        self.assertEqual(sum_in_Range(3, 3), 4)

    def test_sum_in_range_invalid_inputs(self):
        self.assertRaises(TypeError, sum_in_Range, 'a', 1)
        self.assertRaises(TypeError, sum_in_Range, 1, 'a')
        self.assertRaises(ValueError, sum_in_Range, -1, -2)
        self.assertRaises(ValueError, sum_in_Range, 0, -1)

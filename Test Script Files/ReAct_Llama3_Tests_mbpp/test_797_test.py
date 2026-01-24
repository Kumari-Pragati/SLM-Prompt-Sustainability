import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):

    def test_sum_in_Range_positive_range(self):
        self.assertEqual(sum_in_Range(1, 5), 9)

    def test_sum_in_Range_negative_range(self):
        self.assertEqual(sum_in_Range(-1, -5), 9)

    def test_sum_in_Range_zero_range(self):
        self.assertEqual(sum_in_Range(0, 0), 0)

    def test_sum_in_Range_single_element(self):
        self.assertEqual(sum_in_Range(1, 1), 0)

    def test_sum_in_Range_empty_range(self):
        with self.assertRaises(TypeError):
            sum_in_Range()

    def test_sum_in_Range_non_integer_range(self):
        with self.assertRaises(TypeError):
            sum_in_Range(1, 3.5)

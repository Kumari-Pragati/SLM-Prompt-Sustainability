import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(max_sum([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(max_sum([-1, -2, -3, -4, -5]), 15)

    def test_mixed_numbers(self):
        self.assertEqual(max_sum([1, -2, 3, -4, 5]), 12)

    def test_zero(self):
        self.assertEqual(max_sum([0, 1, 2, 3, 4]), 10)

    def test_large_numbers(self):
        self.assertEqual(max_sum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]), 4000000015)

    def test_negative_large_numbers(self):
        self.assertEqual(max_sum([-1000000001, -1000000002, -1000000003, -1000000004, -1000000005]), 4000000015)

    def test_invalid_input_empty_array(self):
        with self.assertRaises(TypeError):
            max_sum(())

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_sum("abc")

    def test_invalid_input_negative_length(self):
        with self.assertRaises(ValueError):
            max_sum([1, 2, 3], -1)

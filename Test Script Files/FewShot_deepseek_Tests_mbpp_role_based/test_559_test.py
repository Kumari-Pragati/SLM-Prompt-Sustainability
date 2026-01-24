import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 0)

    def test_all_positive(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 10)

    def test_all_negative(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 0)

    def test_mixed_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, 2, -3, 4], 4), 4)

    def test_empty_array(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sub_array_sum([5], 1), 5)

    def test_large_numbers(self):
        self.assertEqual(max_sub_array_sum([100, 200, 300, 400], 4), 1000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sub_array_sum("1, 2, 3, 4", 4)

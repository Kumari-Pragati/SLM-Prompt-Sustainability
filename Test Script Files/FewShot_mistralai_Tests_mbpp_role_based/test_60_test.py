import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 3), 3)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 4), 4)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_len_sub([-1, -2, -3, -4, -5], 3), 3)
        self.assertEqual(max_len_sub([-1, -2, -3, -4, -5], 4), 4)
        self.assertEqual(max_len_sub([-1, -2, -3, -4, -5], 5), 5)

    def test_mixed_numbers(self):
        self.assertEqual(max_len_sub([1, -2, 3, -4, 5], 3), 3)
        self.assertEqual(max_len_sub([1, -2, 3, -4, 5], 4), 4)
        self.assertEqual(max_len_sub([1, -2, 3, -4, 5], 5), 5)

    def test_empty_list(self):
        self.assertEqual(max_len_sub([], 1), 0)

    def test_single_element(self):
        self.assertEqual(max_len_sub([1], 1), 1)

    def test_two_elements(self):
        self.assertEqual(max_len_sub([1, 2], 2), 2)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            max_len_sub([1, 2, 3], 0)

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            max_len_sub(1, 2)

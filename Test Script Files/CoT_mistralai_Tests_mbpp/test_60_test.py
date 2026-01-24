import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_len_sub([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(max_len_sub([1], 1), 1)

    def test_consecutive_elements(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)

    def test_non_consecutive_elements(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 2], 6), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_len_sub([-1, -2, -3, -4, -5], 5), 1)

    def test_zero(self):
        self.assertEqual(max_len_sub([0, 1, 2, 3, 4, 0], 6), 3)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            max_len_sub([1, 2, 3], -1)

    def test_invalid_input_array(self):
        with self.assertRaises(TypeError):
            max_len_sub('1, 2, 3', 3)

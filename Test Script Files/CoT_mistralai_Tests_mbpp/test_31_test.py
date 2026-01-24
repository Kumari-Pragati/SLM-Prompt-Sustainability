import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(func([], 0), [])

    def test_single_list(self):
        self.assertListEqual(func([[1, 2, 3]], 1), [1, 2, 3])

    def test_multiple_lists(self):
        self.assertListEqual(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), [1, 2, 4, 5])

    def test_k_greater_than_nums_length(self):
        self.assertListEqual(func([[1, 2, 3]], 4), [1, 2, 3])

    def test_k_equal_to_nums_length(self):
        self.assertListEqual(func([[1, 2, 3]], 3), [1, 2, 3])

    def test_duplicate_numbers(self):
        self.assertListEqual(func([[1, 1, 2], [1, 2, 3]], 2), [1, 1, 2])

    def test_negative_numbers(self):
        self.assertListEqual(func([[-1, -2, -3], [4, 5, 6]], 2), [-1, -2, 4])

    def test_zero_numbers(self):
        self.assertListEqual(func([[0, 0, 0], [1, 2, 3]], 2), [0, 0, 1])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            func('not a list', 0)

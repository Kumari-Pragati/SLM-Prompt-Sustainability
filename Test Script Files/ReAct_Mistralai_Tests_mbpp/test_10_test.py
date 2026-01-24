import unittest
from mbpp_10_code import small_nnum

class TestSmallNNum(unittest.TestCase):

    def test_empty_list(self):
        """Tests small_nnum with an empty list"""
        with self.assertRaises(ValueError):
            small_nnum([], 1)

    def test_single_element(self):
        """Tests small_nnum with a single element list"""
        result = small_nnum([1], 1)
        self.assertEqual(result, [1])

    def test_multiple_elements(self):
        """Tests small_nnum with multiple elements list"""
        result = small_nnum([1, 2, 3, 4, 5], 3)
        self.assertListEqual(result, [1, 2, 3])

    def test_n_larger_than_list_length(self):
        """Tests small_nnum with n larger than list length"""
        with self.assertRaises(ValueError):
            small_nnum([1, 2, 3], 5)

    def test_negative_n(self):
        """Tests small_nnum with negative n"""
        with self.assertRaises(ValueError):
            small_nnum([1, 2, 3], -1)

    def test_non_iterable_input(self):
        """Tests small_nnum with non-iterable input"""
        with self.assertRaises(TypeError):
            small_nnum('abc', 1)

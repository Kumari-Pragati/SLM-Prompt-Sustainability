import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            small_nnum([], 1)

    def test_single_element_list(self):
        self.assertEqual(small_nnum([1], 1), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 3), [1, 2, 3])

    def test_n_greater_than_length_list(self):
        with self.assertRaises(ValueError):
            small_nnum([1, 2, 3, 4, 5], 6)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            small_nnum([1, 2, 3, 4, 5], -1)

    def test_duplicates(self):
        self.assertEqual(small_nnum([1, 1, 2, 3, 4, 4, 5], 3), [1, 1, 2])

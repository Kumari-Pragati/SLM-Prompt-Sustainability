import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(larg_nnum([], 2), [])

    def test_single_element(self):
        self.assertListEqual(larg_nnum([1], 1), [1])

    def test_multiple_elements(self):
        self.assertListEqual(larg_nnum([1, 2, 3, 4, 5], 3), [4, 3, 2])

    def test_n_larger_than_list_length(self):
        self.assertListEqual(larg_nnum([1, 2, 3], 5), [1, 2, 3])

    def test_duplicates(self):
        self.assertListEqual(larg_nnum([1, 2, 2, 3, 4], 3), [4, 3, 2])

    def test_negative_numbers(self):
        self.assertListEqual(larg_nnum([-1, -2, -3, 1, 2], 3), [2, 1, -1])

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            larg_nnum('string', 2)

    def test_invalid_input_n(self):
        with self.assertRaises(ValueError):
            larg_nnum([1, 2, 3], 'string')

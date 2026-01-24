import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(larg_nnum([], 1), [])

    def test_single_element(self):
        self.assertListEqual(larg_nnum([1], 1), [1])

    def test_multiple_elements(self):
        self.assertListEqual(larg_nnum([1, 2, 3, 4, 5], 3), [4, 3, 2])

    def test_n_greater_than_length(self):
        self.assertListEqual(larg_nnum([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertListEqual(larg_nnum([1, 1, 2, 3, 4, 4, 5], 3), [4, 4, 3])

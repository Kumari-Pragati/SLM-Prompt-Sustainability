import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(extract_even([]), [])

    def test_single_even_number(self):
        self.assertListEqual(extract_even([2]), [2])

    def test_single_odd_number(self):
        self.assertListEqual(extract_even([3]), [])

    def test_mixed_numbers(self):
        self.assertListEqual(extract_even([1, 2, 3, 4, 5]), [2, 4])

    def test_single_tuple(self):
        self.assertListEqual(extract_even([(1, 2), (3, 4)]), [(3, 4)])

    def test_mixed_tuples_and_numbers(self):
        self.assertListEqual(extract_even([(1, 2), (3, 4), 1, 2, 3]), [(3, 4)])

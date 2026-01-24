import unittest
from mbpp_580_code import extract_even, even_ele

class TestExtractEven(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(extract_even([]), [])

    def test_single_even_number(self):
        self.assertListEqual(extract_even([2]), [2])

    def test_single_odd_number(self):
        self.assertListEqual(extract_even([1]), [])

    def test_mixed_numbers(self):
        self.assertListEqual(extract_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 4, 6, 8, 10])

    def test_mixed_tuples(self):
        self.assertListEqual(extract_even([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]), [(2,), (4,), (6,), (8,), (10,)])

    def test_empty_tuple(self):
        self.assertListEqual(extract_even(()), [])

    def test_single_even_tuple(self):
        self.assertListEqual(extract_even((2,)), [(2,)])

    def test_single_odd_tuple(self):
        self.assertListEqual(extract_even((1,)), [])

    def test_mixed_tuples_and_numbers(self):
        self.assertListEqual(extract_even([1, (2, 3), 4, (5, 6), 7]), [(2,), (4,), (6,)])

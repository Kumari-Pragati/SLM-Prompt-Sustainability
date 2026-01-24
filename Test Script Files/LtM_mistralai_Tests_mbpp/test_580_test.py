import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):

    def test_simple_even_tuple(self):
        self.assertListEqual(extract_even((2, 4, 6)), (2, 4, 6))

    def test_simple_odd_tuple(self):
        self.assertListEqual(extract_even((1, 3, 5)), ())

    def test_simple_even_list(self):
        self.assertListEqual(list(extract_even([2, 4, 6])), [2, 4, 6])

    def test_simple_odd_list(self):
        self.assertListEqual(list(extract_even([1, 3, 5])), [])

    def test_empty_input(self):
        self.assertListEqual(list(extract_even([])), [])

    def test_single_input(self):
        self.assertListEqual(list(extract_even((1,))), [])
        self.assertListEqual(list(extract_even([1])), [])

    def test_min_max_values(self):
        self.assertListEqual(list(extract_even((-1000000, -1, 0, 1, 1000000))), [0])
        self.assertListEqual(list(extract_even([-1000000, -1, 0, 1, 1000000])), [0])

    def test_mixed_even_odd_tuple(self):
        self.assertListEqual(extract_even((1, 2, 3, 4, 5, 6)), (2, 4, 6))

    def test_mixed_even_odd_list(self):
        self.assertListEqual(list(extract_even([1, 2, 3, 4, 5, 6])), [2, 4])

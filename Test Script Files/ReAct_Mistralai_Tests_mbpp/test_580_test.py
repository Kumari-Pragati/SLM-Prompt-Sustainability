import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(extract_even([]), [])

    def test_single_even_number(self):
        self.assertListEqual(extract_even([2]), [2])

    def test_single_odd_number(self):
        self.assertListEqual(extract_even([1]), [])

    def test_single_mixed_tuple(self):
        self.assertListEqual(extract_even([(1, 2), 3]), [(2,)])

    def test_multiple_even_numbers(self):
        self.assertListEqual(extract_even([2, 4, 6]), [2, 4, 6])

    def test_multiple_odd_numbers(self):
        self.assertListEqual(extract_even([1, 3, 5]), [])

    def test_multiple_mixed_tuples(self):
        self.assertListEqual(extract_even([(1, 2), (3, 4), (5, 6)]), [(2,), (4,)])

    def test_nested_tuples(self):
        self.assertListEqual(extract_even([(1, (2, 3)), (4, 5), (6, 7)]), [(2,), (4, 5)])

    def test_empty_tuple(self):
        self.assertListEqual(extract_even((), lambda x: x % 2 == 0), [])

    def test_tuple_with_even_elements(self):
        self.assertListEqual(extract_even(((2,), (4, 6))), [(2,), (4, 6)])

    def test_tuple_with_odd_elements(self):
        self.assertListEqual(extract_even(((1,), (3, 5))), [])

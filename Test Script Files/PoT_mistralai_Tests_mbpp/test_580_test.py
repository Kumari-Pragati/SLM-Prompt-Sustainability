import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):
    def test_typical_even_input(self):
        self.assertListEqual(extract_even((2, 4, 6)), (2, 4, 6))
        self.assertListEqual(extract_even((1, 3, 5, 7, 9, 11)), ())

    def test_typical_odd_input(self):
        self.assertListEqual(extract_even((1, 3, 5)), (1, 3, 5))
        self.assertListEqual(extract_even((0, 2, 4, 6, 8)), ())

    def test_mixed_input(self):
        self.assertListEqual(extract_even((1, 2, 3, 4, 5, 6)), (2, 4))
        self.assertListEqual(extract_even((0, 1, 2, 3, 4, 5, 6)), ())

    def test_empty_input(self):
        self.assertListEqual(extract_even(()), ())

    def test_single_input(self):
        self.assertListEqual(extract_even((0,)), (0,))
        self.assertListEqual(extract_even((1)), ())

    def test_tuple_of_tuples(self):
        self.assertListEqual(extract_even(((1, 2), (3, 4), (5, 6))), (2, 4))
        self.assertListEqual(extract_even(((0, 1), (2, 3), (4, 5))), ())

    def test_nested_tuples(self):
        self.assertListEqual(extract_even(((1, (2, 3)), (4, (5, 6)))), (2, 3, 5))
        self.assertListEqual(extract_even(((0, (1, 2)), (3, (4, 5)))), ())

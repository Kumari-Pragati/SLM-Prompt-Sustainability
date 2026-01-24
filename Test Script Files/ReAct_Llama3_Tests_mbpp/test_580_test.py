import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(extract_even(()), ())

    def test_single_even(self):
        self.assertEqual(extract_even((2,)), (2,))

    def test_single_odd(self):
        self.assertEqual(extract_even((3,)), ())

    def test_multiple_even(self):
        self.assertEqual(extract_even((2, 4, 6)), (2, 4, 6))

    def test_multiple_odd(self):
        self.assertEqual(extract_even((1, 3, 5)), ())

    def test_mixed_even_odd(self):
        self.assertEqual(extract_even((2, 3, 4, 5, 6)), (2, 4, 6))

    def test_nested_tuples(self):
        self.assertEqual(extract_even(((2, 4), (6, 8))), ((2, 4), (6, 8)))

    def test_nested_odd(self):
        self.assertEqual(extract_even(((1, 3), (5, 7))), ())

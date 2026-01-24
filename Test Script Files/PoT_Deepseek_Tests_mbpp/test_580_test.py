import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_even((1, 2, 3, 4, 5)), (2, 4))

    def test_empty_tuple(self):
        self.assertEqual(extract_even(()), ())

    def test_all_even(self):
        self.assertEqual(extract_even((2, 4, 6)), (2, 4, 6))

    def test_all_odd(self):
        self.assertEqual(extract_even((1, 3, 5)), ())

    def test_mixed_numbers(self):
        self.assertEqual(extract_even((1, 2, 3, 4)), (2, 4))

    def test_nested_tuple(self):
        self.assertEqual(extract_even(((1, 2), (3, 4))), ((2,), (4,)))

    def test_nested_mixed_tuple(self):
        self.assertEqual(extract_even(((1, 2), (3, 4, 5))), ((2,), (4,)))

    def test_single_element_tuple(self):
        self.assertEqual(extract_even((2,)), (2,))

    def test_single_element_odd(self):
        self.assertEqual(extract_even((1,)), ())

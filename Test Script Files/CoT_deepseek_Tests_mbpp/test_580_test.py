import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):

    def test_even_numbers_in_tuple(self):
        self.assertEqual(extract_even((1, 2, 3, 4, 5, 6)), (2, 4, 6))

    def test_even_numbers_in_nested_tuple(self):
        self.assertEqual(extract_even(((1, 2, 3), (4, 5, 6))), ((2, 4), (6,)))

    def test_empty_tuple(self):
        self.assertEqual(extract_even(()), ())

    def test_tuple_with_non_integer_elements(self):
        self.assertEqual(extract_even((1, '2', 3.0, 4, None)), (4,))

    def test_tuple_with_non_integer_elements_and_even_numbers(self):
        self.assertEqual(extract_even((1, '2', 3.0, 4, None, 6)), (4, 6))

    def test_tuple_with_non_integer_elements_and_odd_numbers(self):
        self.assertEqual(extract_even((1, '2', 3.0, 5, None, 7)), ())

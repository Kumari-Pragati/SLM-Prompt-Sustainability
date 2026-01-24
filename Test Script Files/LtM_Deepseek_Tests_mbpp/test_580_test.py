import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(extract_even((1, 2, 3, 4)), (2, 4))

    def test_empty_input(self):
        self.assertEqual(extract_even(()), ())

    def test_single_element_input(self):
        self.assertEqual(extract_even((5,)), ())

    def test_all_even_input(self):
        self.assertEqual(extract_even((2, 4, 6)), (2, 4, 6))

    def test_all_odd_input(self):
        self.assertEqual(extract_even((1, 3, 5)), ())

    def test_mixed_even_odd_input(self):
        self.assertEqual(extract_even((1, 2, 3, 4, 5)), (2, 4))

    def test_nested_tuple_input(self):
        self.assertEqual(extract_even(((1, 2), (3, 4))), (2, 4))

    def test_nested_mixed_input(self):
        self.assertEqual(extract_even(((1, 2), (3, 4, 5))), (2, 4))

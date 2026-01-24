import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(extract_even((1, 2, 3, 4, 5)), (2, 4))

    def test_nested_tuples(self):
        self.assertEqual(extract_even(((1, 2), (3, 4), (5, 6))), ((2, 4),))

    def test_empty_input(self):
        self.assertEqual(extract_even(()), ())

    def test_single_element_input(self):
        self.assertEqual(extract_even((1,)), (1,))

    def test_all_even_input(self):
        self.assertEqual(extract_even((2, 4, 6, 8)), (2, 4, 6, 8))

    def test_all_odd_input(self):
        self.assertEqual(extract_even((1, 3, 5, 7)), ())

    def test_mixed_input(self):
        self.assertEqual(extract_even((1, 2, 3, 4, 5, 6)), (2, 4, 6))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_even("invalid input")

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            extract_even(None)

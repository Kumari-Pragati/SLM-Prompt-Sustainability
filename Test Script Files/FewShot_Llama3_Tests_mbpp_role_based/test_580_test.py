import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(extract_even(()), ())

    def test_single_even_element(self):
        self.assertEqual(extract_even((2,)), (2,))

    def test_single_odd_element(self):
        self.assertEqual(extract_even((3,)), (3,))

    def test_multiple_elements(self):
        self.assertEqual(extract_even((2, 4, 6, 3, 5)), (2, 4, 6))

    def test_nested_tuples(self):
        self.assertEqual(extract_even(((2, 4), (6, 8), (3, 5))), ((2, 4), (6, 8)))

    def test_mixed_types(self):
        self.assertEqual(extract_even((2, 'hello', 4, 3, 'world')), (2, 4))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_even('invalid_input')

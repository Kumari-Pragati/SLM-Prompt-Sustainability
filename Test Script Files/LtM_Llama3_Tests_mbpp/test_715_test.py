import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(str_to_tuple('1, 2, 3'), (1, 2, 3))

    def test_empty_input(self):
        self.assertEqual(str_to_tuple(''), ())

    def test_single_element_input(self):
        self.assertEqual(str_to_tuple('1'), (1,))

    def test_multiple_elements_input(self):
        self.assertEqual(str_to_tuple('1, 2, 3, 4, 5'), (1, 2, 3, 4, 5))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            str_to_tuple('abc')

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            str_to_tuple('1, 2, a, 4')

    def test_mixed_input(self):
        with self.assertRaises(ValueError):
            str_to_tuple('1, 2, 3, a, 4')

import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsInstance(str_to_tuple(''), tuple)
        self.assertListEqual(str_to_tuple(''), ())

    def test_single_element(self):
        self.assertIsInstance(str_to_tuple('1'), tuple)
        self.assertListEqual(str_to_tuple('1'), (1,))

    def test_multiple_elements(self):
        self.assertIsInstance(str_to_tuple('1, 2, 3'), tuple)
        self.assertListEqual(str_to_tuple('1, 2, 3'), (1, 2, 3))

    def test_spaces_around_comma(self):
        self.assertIsInstance(str_to_tuple(' 1 , 2 , 3   '), tuple)
        self.assertListEqual(str_to_tuple(' 1 , 2 , 3   '), (1, 2, 3))

    def test_leading_trailing_spaces(self):
        self.assertIsInstance(str_to_tuple('  1, 2, 3   '), tuple)
        self.assertListEqual(str_to_tuple('  1, 2, 3   '), (1, 2, 3))

    def test_invalid_input_empty_comma(self):
        self.assertRaises(ValueError, str_to_tuple, ',')

    def test_invalid_input_non_integer(self):
        self.assertRaises(ValueError, str_to_tuple, 'a,b,c')

    def test_invalid_input_no_comma(self):
        self.assertRaises(ValueError, str_to_tuple, '12345')

import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsInstance(tuple_str_int(''), tuple, "Empty string should return an empty tuple")

    def test_single_element(self):
        self.assertIsInstance(tuple_str_int('1'), tuple, "Single integer should return a tuple with one element")
        self.assertEqual(tuple_str_int('1'), (1,), "Single integer should return a tuple with one element")

    def test_multiple_elements(self):
        self.assertIsInstance(tuple_str_int('1, 2, 3'), tuple, "Multiple integers should return a tuple")
        self.assertEqual(tuple_str_int('1, 2, 3'), (1, 2, 3), "Multiple integers should return a tuple with the correct elements")

    def test_leading_trailing_whitespace(self):
        self.assertEqual(tuple_str_int('  1, 2, 3   '), (1, 2, 3), "Leading and trailing whitespace should be ignored")

    def test_leading_trailing_punctuation(self):
        self.assertEqual(tuple_str_int('!1, 2, 3!'), (1, 2, 3), "Leading and trailing punctuation should be ignored")

    def test_spaces_in_numbers(self):
        self.assertEqual(tuple_str_int('1 2, 3 4, 5 6'), (12, 34, 56), "Spaces in numbers should be treated as part of the number")

    def test_negative_numbers(self):
        self.assertEqual(tuple_str_int('-1, 0, 1'), (-1, 0, 1), "Negative numbers should be converted correctly")

    def test_empty_elements(self):
        self.assertIsInstance(tuple_str_int(', , '), tuple, "Empty elements should be allowed")
        self.assertEqual(tuple_str_int(' , , '), (None, None, None), "Empty elements should be represented as None")

    def test_invalid_characters(self):
        self.assertRaises(ValueError, tuple_str_int, 'a, b, c')
        self.assertRaises(ValueError, tuple_str_int, '1, 2...3')
        self.assertRaises(ValueError, tuple_str_int, '(1, 2)...(3, 4)')

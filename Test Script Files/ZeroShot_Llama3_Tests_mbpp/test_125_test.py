import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):

    def test_find_length_positive(self):
        self.assertEqual(find_length("0000000000", 10), 0)

    def test_find_length_negative(self):
        self.assertEqual(find_length("1111111111", 10), 10)

    def test_find_length_mixed(self):
        self.assertEqual(find_length("1010101010", 10), 5)

    def test_find_length_empty_string(self):
        self.assertEqual(find_length("", 0), 0)

    def test_find_length_zero_length(self):
        self.assertEqual(find_length("0000000000", 0), 0)

    def test_find_length_invalid_input(self):
        with self.assertRaises(TypeError):
            find_length(123, 10)

    def test_find_length_non_integer_input(self):
        with self.assertRaises(TypeError):
            find_length("123", "10")

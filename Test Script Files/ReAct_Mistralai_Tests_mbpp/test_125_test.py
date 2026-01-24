import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_length('', 10), 0)

    def test_all_zeros(self):
        self.assertEqual(find_length('0000000000', 10), 0)

    def test_all_ones(self):
        self.assertEqual(find_length('1111111111', 10), 10)

    def test_mixed_zeros_and_ones(self):
        self.assertEqual(find_length('0101010101', 10), 4)

    def test_short_string(self):
        self.assertEqual(find_length('01', 2), 1)

    def test_long_string(self):
        self.assertEqual(find_length('010101010101010101', 20), 10)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            find_length('0101010101', -1)

    def test_string_longer_than_n(self):
        with self.assertRaises(ValueError):
            find_length('010101010101010101', 5)

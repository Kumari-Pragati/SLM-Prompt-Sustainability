import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_length('01101', 5), 3)
        self.assertEqual(find_length('10101', 5), 2)
        self.assertEqual(find_length('11111', 5), 4)
        self.assertEqual(find_length('00000', 5), 0)

    def test_zero_length(self):
        self.assertEqual(find_length('', 0), 0)
        self.assertEqual(find_length('0', 1), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_length('11111', -1), 0)
        self.assertEqual(find_length('00000', -5), 0)

    def test_empty_string(self):
        self.assertEqual(find_length('', 5), 0)

    def test_string_longer_than_n(self):
        self.assertEqual(find_length('01101', 2), 0)
        self.assertEqual(find_length('10101', 3), 2)

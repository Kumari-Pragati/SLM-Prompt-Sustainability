import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_length('01010101', 8), 4)

    def test_all_zeros(self):
        self.assertEqual(find_length('00000000', 8), 8)

    def test_all_ones(self):
        self.assertEqual(find_length('11111111', 8), 0)

    def test_mixed_ones_and_zeros(self):
        self.assertEqual(find_length('01010101', 8), 4)
        self.assertEqual(find_length('10101010', 8), 4)

    def test_empty_string(self):
        self.assertEqual(find_length('', 0), 0)

    def test_negative_n(self):
        with self.assertRaises(IndexError):
            find_length('01010101', -1)

    def test_n_greater_than_length_of_string(self):
        self.assertEqual(find_length('01010101', 10), 4)

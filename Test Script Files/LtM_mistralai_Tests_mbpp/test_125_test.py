import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(find_length('01010', 5), 2)

    def test_simple_negative(self):
        self.assertEqual(find_length('10101', 5), 2)

    def test_empty_string(self):
        self.assertEqual(find_length('', 5), 0)

    def test_single_char(self):
        self.assertEqual(find_length('0', 1), 0)
        self.assertEqual(find_length('1', 1), 0)

    def test_min_length(self):
        self.assertEqual(find_length('01', 1), 1)

    def test_max_length(self):
        self.assertEqual(find_length('01' * 100, 100), 100)

    def test_all_zeros(self):
        self.assertEqual(find_length('0' * 100, 100), 100)

    def test_all_ones(self):
        self.assertEqual(find_length('1' * 100, 100), 0)

    def test_alternating(self):
        self.assertEqual(find_length('01010101', 8), 4)

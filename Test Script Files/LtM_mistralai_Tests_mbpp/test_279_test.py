import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(is_num_decagonal(1), 3)
        self.assertEqual(is_num_decagonal(2), 12)
        self.assertEqual(is_num_decagonal(3), 39)

    def test_edge_cases(self):
        self.assertEqual(is_num_decagonal(0), 0)
        self.assertEqual(is_num_decagonal(1000), 3999999)

    def test_negative_numbers(self):
        self.assertEqual(is_num_decagonal(-1), -39)
        self.assertEqual(is_num_decagonal(-2), -12)
        self.assertEqual(is_num_decagonal(-3), -39)

    def test_complex_cases(self):
        self.assertEqual(is_num_decagonal(1000000), 3999999000001)
        self.assertEqual(is_num_decagonal(-1000000), -3999999000001)

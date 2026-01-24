import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(odd_Equivalent('', 10), 0)

    def test_single_digit(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_multiple_digits(self):
        self.assertEqual(odd_Equivalent('101010', 6), 3)
        self.assertEqual(odd_Equivalent('010101', 6), 1)

    def test_long_string(self):
        self.assertEqual(odd_Equivalent('101010101010101010', 20), 10)

    def test_string_longer_than_n(self):
        self.assertEqual(odd_Equivalent('101010101010101010', 10), 10)

    def test_negative_n(self):
        self.assertRaises(ValueError, odd_Equivalent, '1', -1)

    def test_string_with_non_digit(self):
        self.assertRaises(ValueError, odd_Equivalent, '1a1', 3)

import unittest
from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_empty_list(self):
        """Test converting an empty list"""
        with self.assertRaises(ValueError):
            convert([])

    def test_single_digit_list(self):
        """Test converting a list with a single digit"""
        self.assertEqual(convert([1]), 1)

    def test_multi_digit_list(self):
        """Test converting a list with multiple digits"""
        self.assertEqual(convert([1, 2, 3, 4, 5]), 12345)

    def test_negative_numbers(self):
        """Test converting a list with negative numbers"""
        self.assertEqual(convert([-1, -2, -3]), 123)

    def test_leading_zero_list(self):
        """Test converting a list with leading zeros"""
        self.assertEqual(convert([0, 1, 2, 3]), 1230)

    def test_trailing_zero_list(self):
        """Test converting a list with trailing zeros"""
        self.assertEqual(convert([1, 2, 3, 0]), 1230)

    def test_mixed_sign_list(self):
        """Test converting a list with mixed signs"""
        self.assertEqual(convert([1, -2, 3, -4]), 13 - 2 * 4)

    def test_large_numbers(self):
        """Test converting a list with large numbers"""
        self.assertEqual(convert([1000000001, 2, 3, 4, 5]), 1000000001203045)

    def test_non_integer_list(self):
        """Test converting a list with non-integer values"""
        with self.assertRaises(TypeError):
            convert([1.1, 2, 3])

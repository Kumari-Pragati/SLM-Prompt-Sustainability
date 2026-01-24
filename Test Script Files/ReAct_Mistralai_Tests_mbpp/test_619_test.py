import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):

    def test_empty_string(self):
        """Test moving numbers in an empty string"""
        self.assertEqual(move_num(''), '')

    def test_single_digit(self):
        """Test moving a single digit"""
        self.assertEqual(move_num('5'), '5')

    def test_multiple_digits(self):
        """Test moving multiple digits"""
        self.assertEqual(move_num('12345'), '12345')

    def test_single_non_digit(self):
        """Test moving a single non-digit"""
        self.assertEqual(move_num('a'), 'a')

    def test_multiple_non_digits(self):
        """Test moving multiple non-digits"""
        self.assertEqual(move_num('abcdefg'), 'abcdefg')

    def test_mixed_digits_and_non_digits(self):
        """Test moving numbers in a mixed string"""
        self.assertEqual(move_num('1a2b3c4'), '1234a2b3c')

    def test_leading_digits(self):
        """Test moving numbers at the beginning of the string"""
        self.assertEqual(move_num('123abc'), '123abc')

    def test_trailing_digits(self):
        """Test moving numbers at the end of the string"""
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_digits_in_middle(self):
        """Test moving numbers in the middle of the string"""
        self.assertEqual(move_num('abc123defg'), 'abc123defg')

    def test_long_string(self):
        """Test moving numbers in a long string"""
        long_str = '1234567890123456789012345678901234567890'
        self.assertEqual(move_num(long_str), long_str)

    def test_negative_numbers(self):
        """Test moving negative numbers"""
        self.assertEqual(move_num('-123'), '-123')

    def test_leading_negative_numbers(self):
        """Test moving negative numbers at the beginning of the string"""
        self.assertEqual(move_num('-123abc'), '-123abc')

    def test_trailing_negative_numbers(self):
        """Test moving negative numbers at the end of the string"""
        self.assertEqual(move_num('abc-123'), 'abc-123')

    def test_negative_numbers_in_middle(self):
        """Test moving negative numbers in the middle of the string"""
        self.assertEqual(move_num('abc-123defg'), 'abc-123defg')

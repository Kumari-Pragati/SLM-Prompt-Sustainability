import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):

    def test_empty_string(self):
        """Test number_ctr with an empty string"""
        self.assertEqual(number_ctr(''), 0)

    def test_single_digit(self):
        """Test number_ctr with a single digit"""
        for digit in range(10):
            self.assertEqual(number_ctr(str(digit)), 1)

    def test_multiple_digits(self):
        """Test number_ctr with multiple digits"""
        for num in range(100):
            self.assertEqual(number_ctr(str(num)), len(str(num)))

    def test_leading_zero(self):
        """Test number_ctr with a leading zero"""
        self.assertEqual(number_ctr('0123'), 4)

    def test_trailing_zero(self):
        """Test number_ctr with a trailing zero"""
        self.assertEqual(number_ctr('1230'), 3)

    def test_leading_and_trailing_zero(self):
        """Test number_ctr with leading and trailing zeros"""
        self.assertEqual(number_ctr('01230'), 3)

    def test_negative_number(self):
        """Test number_ctr with a negative number"""
        self.assertEqual(number_ctr('-123'), 0)

    def test_alphabets(self):
        """Test number_ctr with alphabets"""
        self.assertEqual(number_ctr('abc'), 0)

    def test_special_characters(self):
        """Test number_ctr with special characters"""
        self.assertEqual(number_ctr('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 0)

import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):

    def test_empty_string(self):
        """Tests if the function returns 'No' for an empty string"""
        self.assertEqual(check(''), 'No')

    def test_single_digit(self):
        """Tests if the function returns 'Yes' for a single digit string"""
        for digit in '01':
            self.assertEqual(check(digit), 'Yes')

    def test_two_digits(self):
        """Tests if the function returns 'No' for a string of two digits"""
        for digit1 in '01':
            for digit2 in '01':
                self.assertEqual(check(f'{digit1}{digit2}'), 'No')

    def test_mixed_digits(self):
        """Tests if the function returns 'No' for a string of mixed digits"""
        for digit1 in '01':
            for digit2 in '01':
                self.assertEqual(check(f'{digit1}{digit2}0'), 'No')
                self.assertEqual(check(f'{digit1}0{digit2}'), 'No')

    def test_long_string(self):
        """Tests if the function returns 'No' for a long string of digits"""
        for _ in range(10):
            self.assertEqual(check('0' * _), 'No')
            self.assertEqual(check('1' * _), 'No')

    def test_special_characters(self):
        """Tests if the function correctly handles strings with special characters"""
        for char in ['!@#$%^&*()_+-=', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '.,;:/?']:
            self.assertEqual(check(char), 'No')

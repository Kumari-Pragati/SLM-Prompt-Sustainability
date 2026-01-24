import unittest
from mbpp_349_code import check

class TestCheck(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(check(''), 'No')

    def test_single_digit_string(self):
        self.assertEqual(check('0'), 'Yes')
        self.assertEqual(check('1'), 'Yes')
        self.assertEqual(check('9'), 'No')

    def test_multiple_digits_string(self):
        self.assertEqual(check('00'), 'Yes')
        self.assertEqual(check('11'), 'Yes')
        self.assertEqual(check('10'), 'No')
        self.assertEqual(check('01'), 'No')

    def test_string_with_non_digits(self):
        self.assertEqual(check('0a'), 'No')
        self.assertEqual(check('A1'), 'No')
        self.assertEqual(check('0123456789'), 'No')

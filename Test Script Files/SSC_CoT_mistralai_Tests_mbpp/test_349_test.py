import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(check(''), 'No')

    def test_single_digit(self):
        self.assertEqual(check('0'), 'Yes')
        self.assertEqual(check('1'), 'Yes')

    def test_multiple_digits(self):
        self.assertEqual(check('00'), 'Yes')
        self.assertEqual(check('11'), 'Yes')
        self.assertEqual(check('01'), 'No')
        self.assertEqual(check('10'), 'No')

    def test_mixed_digits(self):
        self.assertEqual(check('001'), 'No')
        self.assertEqual(check('100'), 'No')
        self.assertEqual(check('011'), 'No')
        self.assertEqual(check('110'), 'No')

    def test_long_string(self):
        self.assertEqual(check('0000000000'), 'Yes')
        self.assertEqual(check('1111111111'), 'Yes')
        self.assertEqual(check('0111111111'), 'No')
        self.assertEqual(check('1000000000'), 'No')

    def test_invalid_input(self):
        self.assertRaises(TypeError, check, 123)
        self.assertRaises(TypeError, check, [1, 2, 3])
        self.assertRaises(TypeError, check, None)
        self.assertRaises(TypeError, check, {})

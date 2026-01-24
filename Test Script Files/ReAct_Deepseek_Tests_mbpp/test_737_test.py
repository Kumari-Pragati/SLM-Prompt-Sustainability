import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):

    def test_valid_strings(self):
        self.assertEqual(check_str('a123_'), 'Valid')
        self.assertEqual(check_str('A456_'), 'Valid')
        self.assertEqual(check_str('e789_'), 'Valid')
        self.assertEqual(check_str('i101112_'), 'Valid')
        self.assertEqual(check_str('o131415_'), 'Valid')
        self.assertEqual(check_str('u161718_'), 'Valid')

    def test_invalid_strings(self):
        self.assertEqual(check_str('12345'), 'Invalid')
        self.assertEqual(check_str('abcde'), 'Invalid')
        self.assertEqual(check_str('ABCDE'), 'Invalid')
        self.assertEqual(check_str(''), 'Invalid')
        self.assertEqual(check_str('n0123456'), 'Invalid')

    def test_edge_cases(self):
        self.assertEqual(check_str(' '), 'Invalid')
        self.assertEqual(check_str('!@#$%^&*()'), 'Invalid')
        self.assertEqual(check_str('1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'), 'Invalid')

import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove_lowercase('HelloWorld'), 'HW')
        self.assertEqual(remove_lowercase('123abcABC'), '123ABC')
        self.assertEqual(remove_lowercase(''), '')

    def test_edge_cases(self):
        self.assertEqual(remove_lowercase('a'), '')
        self.assertEqual(remove_lowercase('A'), 'A')
        self.assertEqual(remove_lowercase('lowercase'), '')
        self.assertEqual(remove_lowercase('UPPERCASE'), 'UPPERCASE')

    def test_corner_cases(self):
        self.assertEqual(remove_lowercase('mixedCase123'), '123')
        self.assertEqual(remove_lowercase('!@#$%^&*()'), '!@#$%^&*()')
        self.assertEqual(remove_lowercase('1234567890'), '1234567890')

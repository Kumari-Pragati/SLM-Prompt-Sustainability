import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove_lowercase('Hello World'), 'HW')
        self.assertEqual(remove_lowercase('123abcABC'), '123ABC')
        self.assertEqual(remove_lowercase('aBcDeFgHiJkLmNoPqRsTuVwXyZ'), '')

    def test_edge_cases(self):
        self.assertEqual(remove_lowercase(''), '')
        self.assertEqual(remove_lowercase('lowercase'), '')
        self.assertEqual(remove_lowercase('UPPERCASE'), 'UPPERCASE')

    def test_corner_cases(self):
        self.assertEqual(remove_lowercase('lowercase123'), '123')
        self.assertEqual(remove_lowercase('UPPERCASE123'), 'UPPERCASE123')
        self.assertEqual(remove_lowercase('123lowercase'), '123')
        self.assertEqual(remove_lowercase('123UPPERCASE'), '123UPPERCASE')

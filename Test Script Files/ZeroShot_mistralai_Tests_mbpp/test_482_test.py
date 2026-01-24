import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):
    def test_uppercase_and_lowercase(self):
        self.assertEqual(match('CamelCase'), 'Yes')
        self.assertEqual(match('TitleCase'), 'Yes')
        self.assertEqual(match('lowerCase'), 'No')

    def test_special_cases(self):
        self.assertEqual(match(''), 'No')
        self.assertEqual(match('123'), 'No')
        self.assertEqual(match('A'), 'No')
        self.assertEqual(match('Aa'), 'Yes')
        self.assertEqual(match('AaB'), 'Yes')
        self.assertEqual(match('AaBb'), 'Yes')
        self.assertEqual(match('AaBbC'), 'Yes')
        self.assertEqual(match('AaBbCc'), 'Yes')

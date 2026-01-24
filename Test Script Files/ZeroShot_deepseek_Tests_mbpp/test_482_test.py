import unittest
from mbpp_482_code import match

class TestMatch(unittest.TestCase):

    def test_match_positive(self):
        self.assertEqual(match('HelloWorld'), 'Yes')
        self.assertEqual(match('PythonProgramming'), 'Yes')
        self.assertEqual(match('JavaScript'), 'Yes')

    def test_match_negative(self):
        self.assertEqual(match('helloWorld'), 'No')
        self.assertEqual(match('pythonprogramming'), 'No')
        self.assertEqual(match('javascript123'), 'No')
        self.assertEqual(match('123456'), 'No')
        self.assertEqual(match(''), 'No')

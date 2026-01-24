import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(match('HelloWorld'), 'Yes')
        self.assertEqual(match('PythonProgramming'), 'Yes')

    def test_edge_cases(self):
        self.assertEqual(match(''), 'No')
        self.assertEqual(match('a'), 'No')
        self.assertEqual(match('123'), 'No')
        self.assertEqual(match('ABC'), 'No')

    def test_boundary_cases(self):
        self.assertEqual(match('Aa'), 'Yes')
        self.assertEqual(match('Zz'), 'Yes')
        self.assertEqual(match('A'), 'No')
        self.assertEqual(match('Z'), 'No')

    def test_corner_cases(self):
        self.assertEqual(match('AZ'), 'Yes')
        self.assertEqual(match('az'), 'No')
        self.assertEqual(match('Az'), 'Yes')
        self.assertEqual(match('zZ'), 'Yes')

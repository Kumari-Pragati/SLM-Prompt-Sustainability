import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(is_lower('Hello'), 'hello')
        self.assertEqual(is_lower('WORLD'), 'world')
        self.assertEqual(is_lower('Python'), 'python')

    def test_edge_cases(self):
        self.assertEqual(is_lower(''), '')
        self.assertEqual(is_lower('123'), '123')
        self.assertEqual(is_lower('!@#'), '!@#')

    def test_boundary_cases(self):
        self.assertEqual(is_lower('A'), 'a')
        self.assertEqual(is_lower('z'), 'z')
        self.assertEqual(is_lower('aBcDeFgHiJkLmNoPqRsTuVwXyZ'), 'abcdefghijklmnopqrstuvwxyz')

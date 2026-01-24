import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove_char('Hello, World!'), 'HelloWorld')
        self.assertEqual(remove_char('Python is fun!'), 'Pythonisfun')

    def test_edge_cases(self):
        self.assertEqual(remove_char(''), '')
        self.assertEqual(remove_char('12345'), '12345')

    def test_boundary_conditions(self):
        self.assertEqual(remove_char('a' * 1000), 'a' * 1000)

    def test_corner_cases(self):
        self.assertEqual(remove_char('!@#$%^&*()'), '')
        self.assertEqual(remove_char('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

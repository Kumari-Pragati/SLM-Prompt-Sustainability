import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove_extra_char('Hello, World!'), 'HelloWorld')
        self.assertEqual(remove_extra_char('Python3 is awesome!'), 'Python3isawesome')

    def test_edge_cases(self):
        self.assertEqual(remove_extra_char(''), '')
        self.assertEqual(remove_extra_char('12345'), '12345')

    def test_boundary_conditions(self):
        self.assertEqual(remove_extra_char('a' * 10000), 'a' * 10000)

    def test_corner_cases(self):
        self.assertEqual(remove_extra_char('!@#$%^&*()'), '')
        self.assertEqual(remove_extra_char('Python3@#is$%awesome^&*()'), 'Python3isawesome')

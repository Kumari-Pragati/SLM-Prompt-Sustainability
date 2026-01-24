import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSpecialCharacters(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove_splchar('Hello, World!'), 'Hello World')
        self.assertEqual(remove_splchar('Python3.8'), 'Python38')
        self.assertEqual(remove_splchar('100@days#of#code'), '100daysofcode')

    def test_edge_cases(self):
        self.assertEqual(remove_splchar(''), '')
        self.assertEqual(remove_splchar('NoSpecialCharacters'), 'NoSpecialCharacters')

    def test_corner_cases(self):
        self.assertEqual(remove_splchar('  Leading and Trailing Spaces  '), 'Leading and Trailing Spaces')
        self.assertEqual(remove_splchar('Special Characters @#$%^&*()'), 'Special Characters ')

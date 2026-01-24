import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplChar(unittest.TestCase):

    def test_remove_splchar(self):
        self.assertEqual(remove_splchar('Hello, World!'), 'HelloWorld')
        self.assertEqual(remove_splchar('Python3.8'), 'Python38')
        self.assertEqual(remove_splchar('100@days#of$code'), '100daysofcode')
        self.assertEqual(remove_splchar('A1B2C3D4'), 'ABC1234')
        self.assertEqual(remove_splchar(''), '')
        self.assertEqual(remove_splchar('!@#$%^&*()'), '')

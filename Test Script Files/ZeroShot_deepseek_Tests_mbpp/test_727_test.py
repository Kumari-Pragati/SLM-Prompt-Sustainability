import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):

    def test_remove_char(self):
        self.assertEqual(remove_char('Hello, World!'), 'HelloWorld')
        self.assertEqual(remove_char('Python3.8'), 'Python38')
        self.assertEqual(remove_char('a1b2c3'), 'abc')
        self.assertEqual(remove_char(''), '')
        self.assertEqual(remove_char('!@#$%^&*()'), '')

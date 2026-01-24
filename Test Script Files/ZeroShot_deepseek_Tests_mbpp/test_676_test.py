import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):

    def test_remove_extra_char(self):
        self.assertEqual(remove_extra_char('Hello, World!'), 'HelloWorld')
        self.assertEqual(remove_extra_char('Python3.8'), 'Python38')
        self.assertEqual(remove_extra_char('100@success'), '100success')
        self.assertEqual(remove_extra_char('a!!b??c'), 'abc')
        self.assertEqual(remove_extra_char(''), '')

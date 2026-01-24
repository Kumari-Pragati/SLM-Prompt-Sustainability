import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_remove_spaces(self):
        self.assertEqual(remove_spaces('Hello World'), 'HelloWorld')
        self.assertEqual(remove_spaces('Python Programming'), 'PythonProgramming')
        self.assertEqual(remove_spaces(''), '')
        self.assertEqual(remove_spaces('1 2 3 4'), '1234')
        self.assertEqual(remove_spaces('a b c d'), 'abcd')

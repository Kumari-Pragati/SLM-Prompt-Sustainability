import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):

    def test_remove_uppercase(self):
        self.assertEqual(remove_uppercase('HelloWorld'), 'elloorld')
        self.assertEqual(remove_uppercase('PythonProgramming'), 'ythonrogramming')
        self.assertEqual(remove_uppercase('A1B2C3'), '123')
        self.assertEqual(remove_uppercase('NoUppercaseHere'), 'nouppercasehere')
        self.assertEqual(remove_uppercase(''), '')

import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_remove_whitespaces(self):
        self.assertEqual(remove_whitespaces('Hello World'), 'HelloWorld')
        self.assertEqual(remove_whitespaces('Python is fun'), 'Pythonisfun')
        self.assertEqual(remove_whitespaces('   Python   is   fun   '), 'Pythonisfun')
        self.assertEqual(remove_whitespaces(''), '')
        self.assertEqual(remove_whitespaces('123456'), '123456')
        self.assertEqual(remove_whitespaces('  123456   '), '123456')

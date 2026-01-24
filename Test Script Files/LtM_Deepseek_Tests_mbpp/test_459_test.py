import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(remove_uppercase('HelloWorld'), 'elloorld')
        self.assertEqual(remove_uppercase('PythonProgramming'), 'ythonrogramming')

    def test_edge_conditions(self):
        self.assertEqual(remove_uppercase(''), '')
        self.assertEqual(remove_uppercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), '')

    def test_complex_cases(self):
        self.assertEqual(remove_uppercase('AaBbCc'), 'aaBBcc')
        self.assertEqual(remove_uppercase('123ABC456'), '123456')
        self.assertEqual(remove_uppercase('The Quick Brown Fox'), 'he quick brown fox')

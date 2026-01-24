import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_remove_lowercase(self):
        self.assertEqual(remove_lowercase('HelloWorld'), 'HW')
        self.assertEqual(remove_lowercase('PythonProgramming'), 'PythonProgramming')
        self.assertEqual(remove_lowercase('aBcDeF'), 'BCDEF')
        self.assertEqual(remove_lowercase('123456'), '123456')
        self.assertEqual(remove_lowercase(''), '')

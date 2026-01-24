import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_remove_lowercase(self):
        self.assertEqual(remove_lowercase('HelloWorld'), 'HW')
        self.assertEqual(remove_lowercase('hElLOwOrLD'), 'HW')
        self.assertEqual(remove_lowercase('123abcABC'), '123ABC')
        self.assertEqual(remove_lowercase(''), '')
        self.assertEqual(remove_lowercase('aBcDeF'), '')

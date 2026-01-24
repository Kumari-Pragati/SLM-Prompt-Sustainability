import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(lower_ctr('HelloWorld'), 2)
        self.assertEqual(lower_ctr('hElLoWoRlD'), 2)
        self.assertEqual(lower_ctr(''), 0)
        self.assertEqual(lower_ctr('1234567890'), 0)
        self.assertEqual(lower_ctr('abcdefghijklmnopqrstuvwxyz'), 26)

    def test_edge_cases(self):
        self.assertEqual(lower_ctr('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), 52)
        self.assertEqual(lower_ctr('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 0)
        self.assertEqual(lower_ctr('abcdefghijklmnopqrstuvwxyz'), 26)
        self.assertEqual(lower_ctr('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'), 52)

    def test_explicitly_handled_error_cases(self):
        # The function does not handle any error cases, so this test is redundant.
        self.assertEqual(lower_ctr(None), 0)
        self.assertEqual(lower_ctr(1234567890), 0)
        self.assertEqual(lower_ctr(['a', 'b', 'c']), 0)

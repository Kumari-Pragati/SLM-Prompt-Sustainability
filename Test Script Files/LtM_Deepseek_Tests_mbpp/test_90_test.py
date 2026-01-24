import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(len_log(['abc', 'def']), 3)
        self.assertEqual(len_log(['123', '456']), 3)

    def test_edge_conditions(self):
        self.assertEqual(len_log(['']), 0)
        self.assertEqual(len_log(['a']), 1)
        self.assertEqual(len_log(['abcdefghijklmnopqrstuvwxyz']), 26)

    def test_complex_cases(self):
        self.assertEqual(len_log(['abcdefghijklmnopqrstuvwxyz', '1234567890']), 10)
        self.assertEqual(len_log(['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']), 3)

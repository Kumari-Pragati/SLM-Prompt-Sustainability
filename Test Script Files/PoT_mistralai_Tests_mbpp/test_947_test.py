import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(len_log([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), 3)

    def test_edge_case_single_item(self):
        self.assertEqual(len_log(['x']), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_edge_case_single_empty_string(self):
        self.assertEqual(len_log(['']), 0)

    def test_corner_case_mixed_types(self):
        self.assertEqual(len_log([1, 'x', 2]), 1)

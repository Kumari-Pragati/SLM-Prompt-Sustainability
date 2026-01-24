import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(len_log([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), 3)

    def test_edge_case_single_item(self):
        self.assertEqual(len_log(['x']), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_edge_case_single_item_longer(self):
        self.assertEqual(len_log([['x'] * 100]], 100)

    def test_corner_case_mixed_types(self):
        self.assertRaises(TypeError, len_log, [1, 2, 3])

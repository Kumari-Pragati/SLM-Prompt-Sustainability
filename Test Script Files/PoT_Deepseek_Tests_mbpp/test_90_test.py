import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(len_log(['abc', 'defgh', 'ijklm']), 5)

    def test_edge_case_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_boundary_case_single_element(self):
        self.assertEqual(len_log(['abc']), 3)

    def test_corner_case_longest_string_at_end(self):
        self.assertEqual(len_log(['abc', 'defgh', 'ijklmnop']), 8)

    def test_corner_case_longest_string_at_start(self):
        self.assertEqual(len_log(['abcdefgh', 'def', 'ijk']), 8)

import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(minimum_Length('aabcb'), 3)

    def test_edge_case_single_char(self):
        self.assertEqual(minimum_Length('a'), 1)

    def test_boundary_case_empty_string(self):
        self.assertEqual(minimum_Length(''), 0)

    def test_corner_case_all_same_chars(self):
        self.assertEqual(minimum_Length('aaaaa'), 5)

    def test_corner_case_all_different_chars(self):
        self.assertEqual(minimum_Length('abcdefghijklmnopqrstuvwxyz'), 26)

    def test_corner_case_mixed_chars(self):
        self.assertEqual(minimum_Length('abcdeffedcba'), 10)

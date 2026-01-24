import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Substrings("1011", 4), 4)
        self.assertEqual(count_Substrings("1111", 4), 10)
        self.assertEqual(count_Substrings("1357", 4), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Substrings("", 0), 0)
        self.assertEqual(count_Substrings("1", 1), 1)
        self.assertEqual(count_Substrings("0", 1), 0)

    def test_corner_cases(self):
        self.assertEqual(count_Substrings("1111111111", 10), 55)
        self.assertEqual(count_Substrings("0000000000", 10), 0)

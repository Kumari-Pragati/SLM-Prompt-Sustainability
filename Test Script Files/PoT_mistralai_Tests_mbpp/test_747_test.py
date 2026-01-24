import unittest
from mbpp_747_code import lcs_of_three

class TestLCSOfThree(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lcs_of_three('ABCD', 'ACDE', 'ABFG'), 2)
        self.assertEqual(lcs_of_three('ABC', 'BCD', 'DEF'), 0)
        self.assertEqual(lcs_of_three('AAA', 'BBB', 'CCC'), 1)

    def test_edge_case_empty_strings(self):
        self.assertEqual(lcs_of_three('', '', ''), 0)
        self.assertEqual(lcs_of_three('', 'ABC', ''), 0)
        self.assertEqual(lcs_of_three('ABC', '', ''), 0)

    def test_edge_case_single_char(self):
        self.assertEqual(lcs_of_three('A', 'A', 'B'), 1)
        self.assertEqual(lcs_of_three('A', 'B', 'A'), 1)
        self.assertEqual(lcs_of_three('A', 'B', 'B'), 0)

    def test_edge_case_single_string(self):
        self.assertEqual(lcs_of_three('ABC', '', ''), 0)
        self.assertEqual(lcs_of_three('', 'ABC', ''), 0)
        self.assertEqual(lcs_of_three('', '', 'ABC'), 0)

    def test_corner_case_different_lengths(self):
        self.assertEqual(lcs_of_three('ABC', 'DEF', 'GHI'), 0)
        self.assertEqual(lcs_of_three('ABC', 'ABCDEF', 'GHI'), 0)
        self.assertEqual(lcs_of_three('ABC', 'ABC', 'ABCDEFGHI'), 0)

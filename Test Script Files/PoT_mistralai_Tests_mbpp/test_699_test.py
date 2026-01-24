import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(min_Swaps("ABCD", "ACBD"), 1)
        self.assertEqual(min_Swaps("ABCD", "BCDA"), 3)
        self.assertEqual(min_Swaps("ABCD", "CDAB"), 2)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(min_Swaps("", ""), 0)
        self.assertEqual(min_Swaps("A", "A"), 0)
        self.assertEqual(min_Swaps("AA", "BB"), 2)
        self.assertEqual(min_Swaps("ABC", "ABC"), 0)
        self.assertEqual(min_Swaps("ABC", "CBA"), 2)
        self.assertEqual(min_Swaps("ABC", "ABX"), "Not Possible")
        self.assertEqual(min_Swaps("ABC", "CAB"), "Not Possible")

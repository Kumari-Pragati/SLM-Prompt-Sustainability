import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(min_Swaps("ABCD", "DCBA"), 2)
        self.assertEqual(min_Swaps("ABCD", "BCDA"), 1)
        self.assertEqual(min_Swaps("ABCD", "CDAB"), 2)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(min_Swaps("", ""), 0)
        self.assertEqual(min_Swaps("A", "A"), 0)
        self.assertEqual(min_Swaps("AA", "BB"), 2)
        self.assertEqual(min_Swaps("ABC", "ABC"), 0)
        self.assertEqual(min_Swaps("ABC", "CBA"), 1)
        self.assertEqual(min_Swaps("ABC", "ACB"), 1)
        self.assertEqual(min_Swaps("ABC", "BCA"), 2)

    def test_corner_cases(self):
        self.assertEqual(min_Swaps("ABCD", "ABCD"), "Not Possible")
        self.assertEqual(min_Swaps("ABCD", "ABC"), "Not Possible")
        self.assertEqual(min_Swaps("ABCD", "ACD"), "Not Possible")
        self.assertEqual(min_Swaps("ABCD", "ADBC"), "Not Possible")

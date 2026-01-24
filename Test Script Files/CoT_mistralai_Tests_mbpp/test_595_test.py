import unittest
from595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Swaps("ABCD", "DCBA"), 1)
        self.assertEqual(min_Swaps("ABCD", "ABCD"), 0)
        self.assertEqual(min_Swaps("ABCD", "ACBD"), 1)

    def test_edge_case_even(self):
        self.assertEqual(min_Swaps("ABCD", "BCDA"), 2)
        self.assertEqual(min_Swaps("ABCD", "CDAB"), 2)

    def test_edge_case_odd(self):
        self.assertEqual(min_Swaps("ABCD", "CDAB"), "Not Possible")
        self.assertEqual(min_Swaps("ABCD", "ACBD"), "Not Possible")

    def test_invalid_input_1(self):
        self.assertRaises(TypeError, min_Swaps, 1, 2)

    def test_invalid_input_2(self):
        self.assertRaises(TypeError, min_Swaps, "A", 2)

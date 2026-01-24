import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 2)

    def test_edge_case(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 1), 0)

    def test_edge_case2(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 2)

    def test_edge_case3(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 0), 0)

    def test_edge_case4(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)

    def test_edge_case5(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 2), 2)

    def test_edge_case6(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 3), 2)

    def test_edge_case7(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 4), 2)

    def test_edge_case8(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 2)

    def test_edge_case9(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 6), 2)

    def test_edge_case10(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 7), 2)

    def test_edge_case11(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 8), 2)

    def test_edge_case12(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 9), 2)

    def test_edge_case13(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 10), 2)

    def test_edge_case14(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 11), 2)

    def test_edge_case15(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 12), 2)

    def test_edge_case16(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 13), 2)

    def test_edge_case17(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 14), 2)

    def test_edge_case18(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 15), 2)

    def test_edge_case19(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 16), 2)

    def test_edge_case20(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 17), 2)

    def test_edge_case21(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 18), 2)

    def test_edge_case22(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 19), 2)

    def test_edge_case23(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 20), 2)

    def test_edge_case24(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 21), 2)

    def test_edge_case25(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 22), 2)

    def test_edge_case26(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 23), 2)

    def test_edge_case27(self):
        self.assertEqual(find_Odd_Pair([1
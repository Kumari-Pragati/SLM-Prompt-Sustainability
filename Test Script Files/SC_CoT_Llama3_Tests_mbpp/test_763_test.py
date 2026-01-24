import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(find_Min_Diff([1, 3, 5, 7, 9], 4), 2)

    def test_edge_case(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 4), 1)

    def test_edge_case2(self):
        self.assertEqual(find_Min_Diff([5, 5, 5, 5, 5], 4), 0)

    def test_edge_case3(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6], 5), 1)

    def test_edge_case4(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7], 6), 1)

    def test_edge_case5(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8], 7), 1)

    def test_edge_case6(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9], 8), 1)

    def test_edge_case7(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9), 1)

    def test_edge_case8(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 10), 1)

    def test_edge_case9(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11), 1)

    def test_edge_case10(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 12), 1)

    def test_edge_case11(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 13), 1)

    def test_edge_case12(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 14), 1)

    def test_edge_case13(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 15), 1)

    def test_edge_case14(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 16), 1)

    def test_edge_case15(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 17), 1)

    def test_edge_case16(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 18), 1)

    def test_edge_case17(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 19
import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 0)

    def test_edge_case(self):
        self.assertEqual(find_Diff([1, 1, 1, 1, 1], 5), 4)

    def test_edge_case2(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 5], 6), 1)

    def test_edge_case3(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 6], 6), 0)

    def test_edge_case4(self):
        self.assertEqual(find_Diff([1, 1, 1, 1, 1, 1], 6), 5)

    def test_edge_case5(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 6, 7], 7), 0)

    def test_edge_case6(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 6, 7, 8], 8), 0)

    def test_edge_case7(self):
        self.assertEqual(find_Diff([1, 1, 1, 1, 1, 1, 1, 1], 8), 7)

    def test_edge_case8(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 0)

    def test_edge_case9(self):
        self.assertEqual(find_Diff([1, 1, 1, 1, 1, 1, 1, 1, 1], 9), 8)

    def test_edge_case10(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 0)

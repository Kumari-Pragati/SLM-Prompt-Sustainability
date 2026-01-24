import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Min_Diff([1, 3, 5, 7, 9], 4), 2)

    def test_edge_case(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 4), 1)

    def test_edge_case2(self):
        self.assertEqual(find_Min_Diff([1, 3, 5, 7, 9], 1), 2)

    def test_edge_case3(self):
        self.assertEqual(find_Min_Diff([1, 3, 5, 7, 9], 5), 0)

    def test_edge_case4(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 1), 1)

    def test_edge_case5(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 0), 1)

    def test_edge_case6(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 6), 0)

    def test_edge_case7(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 0)

    def test_edge_case8(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 0), 1)

    def test_edge_case9(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 6), 0)

    def test_edge_case10(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 0)

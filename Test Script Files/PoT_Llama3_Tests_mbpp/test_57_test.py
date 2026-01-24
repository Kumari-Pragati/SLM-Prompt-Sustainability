import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max_Num([3, 2, 5, 7, 1], 5), 75321)

    def test_edge_case(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5], 5), 54321)

    def test_edge_case2(self):
        self.assertEqual(find_Max_Num([5, 4, 3, 2, 1], 5), 54321)

    def test_edge_case3(self):
        self.assertEqual(find_Max_Num([1, 1, 1, 1, 1], 5), 11111)

    def test_edge_case4(self):
        self.assertEqual(find_Max_Num([9, 9, 9, 9, 9], 5), 99999)

    def test_edge_case5(self):
        self.assertEqual(find_Max_Num([0, 0, 0, 0, 0], 5), 0)

    def test_edge_case6(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5, 6], 6), 654321)

    def test_edge_case7(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5, 6, 7], 7), 7654321)

    def test_edge_case8(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8], 8), 87654321)

    def test_edge_case9(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 987654321)

    def test_edge_case10(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10), 9876543210)

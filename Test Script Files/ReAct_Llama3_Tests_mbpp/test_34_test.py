import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_typical_case(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(find_missing(ar, 10), 11)

    def test_edge_case(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_missing(ar, 9), 10)

    def test_edge_case2(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(find_missing(ar, 8), 9)

    def test_edge_case3(self):
        ar = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(find_missing(ar, 7), 8)

    def test_edge_case4(self):
        ar = [1, 2, 3, 4, 5, 6]
        self.assertEqual(find_missing(ar, 6), 7)

    def test_edge_case5(self):
        ar = [1, 2, 3, 4, 5]
        self.assertEqual(find_missing(ar, 5), 6)

    def test_edge_case6(self):
        ar = [1, 2, 3, 4]
        self.assertEqual(find_missing(ar, 4), 5)

    def test_edge_case7(self):
        ar = [1, 2, 3]
        self.assertEqual(find_missing(ar, 3), 4)

    def test_edge_case8(self):
        ar = [1, 2]
        self.assertEqual(find_missing(ar, 2), 3)

    def test_edge_case9(self):
        ar = [1]
        self.assertEqual(find_missing(ar, 1), 2)

    def test_edge_case10(self):
        ar = []
        self.assertEqual(find_missing(ar, 0), 1)

    def test_error_case(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(find_missing(ar, 20), -1)

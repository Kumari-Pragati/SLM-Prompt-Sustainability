import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 3, 3, 3), (1, 4, 7))

    def test_edge_case(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 1, 1, 1), (1, 4, 7))

    def test_edge_case2(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 3, 3, 1), (1, 4, 7))

    def test_edge_case3(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 1, 3, 3), (1, 4, 7))

    def test_edge_case4(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 3, 1, 3), (1, 4, 7))

    def test_edge_case5(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 1, 3, 1), (1, 4, 7))

    def test_edge_case6(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 3, 1, 1), (1, 4, 7))

    def test_edge_case7(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 1, 1, 3), (1, 4, 7))

    def test_edge_case8(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 3, 3, 2), (1, 4, 7))

    def test_edge_case9(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 1, 2, 3), (1, 4, 7))

    def test_edge_case10(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 2, 3, 1), (1, 4, 7))

    def test_edge_case11(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 3, 2, 1), (1, 4, 7))

    def test_edge_case12(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 2, 1, 3), (1, 4, 7))

    def test_edge_case13(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 1, 3, 2), (1, 4, 7))

    def test_edge_case14(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 3, 1, 2), (1, 4, 7))

    def test_edge_case15(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 2, 3, 2), (1, 4, 7))

    def test_edge_case16(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 3
import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 1), [4, 5, 1, 2, 3])

    def test_edge_case1(self):
        self.assertEqual(rotate_right([1, 2, 3], 1, 0), [3, 1, 2])

    def test_edge_case2(self):
        self.assertEqual(rotate_right([1, 2, 3], 3, 0), [1, 2, 3])

    def test_edge_case3(self):
        self.assertEqual(rotate_right([1, 2, 3], 0, 0), [1, 2, 3])

    def test_edge_case4(self):
        self.assertEqual(rotate_right([1, 2, 3], 4, 0), [1, 2, 3])

    def test_edge_case5(self):
        self.assertEqual(rotate_right([1, 2, 3], 0, 1), [1, 2, 3])

    def test_edge_case6(self):
        self.assertEqual(rotate_right([1, 2, 3], 3, 1), [1, 2, 3])

    def test_edge_case7(self):
        self.assertEqual(rotate_right([1, 2, 3], 1, 3), [1, 2, 3])

    def test_edge_case8(self):
        self.assertEqual(rotate_right([1, 2, 3], 0, 3), [1, 2, 3])

    def test_edge_case9(self):
        self.assertEqual(rotate_right([1, 2, 3], 3, 3), [1, 2, 3])

    def test_edge_case10(self):
        self.assertEqual(rotate_right([1, 2, 3], 0, 2), [1, 2, 3])

    def test_edge_case11(self):
        self.assertEqual(rotate_right([1, 2, 3], 2, 3), [1, 2, 3])

    def test_edge_case12(self):
        self.assertEqual(rotate_right([1, 2, 3], 3, 2), [1, 2, 3])

    def test_edge_case13(self):
        self.assertEqual(rotate_right([1, 2, 3], 1, 2), [3, 1, 2])

    def test_edge_case14(self):
        self.assertEqual(rotate_right([1, 2, 3], 2, 1), [3, 1, 2])

    def test_edge_case15(self):
        self.assertEqual(rotate_right([1, 2, 3], 3, 2), [1, 2, 3])

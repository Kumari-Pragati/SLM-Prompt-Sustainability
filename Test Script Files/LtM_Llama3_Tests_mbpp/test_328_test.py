import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 1, 3), [2, 3, 4, 5, 1])
    def test_edge1(self):
        self.assertEqual(rotate_left([1, 2, 3], 0, 3), [1, 2, 3])
    def test_edge2(self):
        self.assertEqual(rotate_left([1, 2, 3], 1, 3), [2, 3, 1])
    def test_edge3(self):
        self.assertEqual(rotate_left([1, 2, 3], 2, 3), [3, 1, 2])
    def test_edge4(self):
        self.assertEqual(rotate_left([1, 2, 3], 3, 3), [1, 2, 3])
    def test_edge5(self):
        self.assertEqual(rotate_left([1, 2, 3], 0, 2), [1, 2, 3])
    def test_edge6(self):
        self.assertEqual(rotate_left([1, 2, 3], 1, 2), [2, 3, 1])
    def test_edge7(self):
        self.assertEqual(rotate_left([1, 2, 3], 2, 1), [3, 1, 2])
    def test_edge8(self):
        self.assertEqual(rotate_left([1, 2, 3], 3, 1), [1, 2, 3])
    def test_edge9(self):
        self.assertEqual(rotate_left([1, 2, 3], 0, 1), [1, 2, 3])
    def test_edge10(self):
        self.assertEqual(rotate_left([1, 2, 3], 1, 1), [2, 3, 1])
    def test_edge11(self):
        self.assertEqual(rotate_left([1, 2, 3], 2, 1), [3, 1, 2])
    def test_edge12(self):
        self.assertEqual(rotate_left([1, 2, 3], 3, 1), [1, 2, 3])
    def test_edge13(self):
        self.assertEqual(rotate_left([1, 2, 3], 0, 0), [1, 2, 3])
    def test_edge14(self):
        self.assertEqual(rotate_left([1, 2, 3], 1, 0), [1, 2, 3])
    def test_edge15(self):
        self.assertEqual(rotate_left([1, 2, 3], 2, 0), [1, 2, 3])
    def test_edge16(self):
        self.assertEqual(rotate_left([1, 2, 3], 3, 0), [1, 2, 3])
    def test_edge17(self):
        self.assertEqual(rotate_left([1, 2, 3], 0, 4), [1, 2, 3, 1, 2])
    def test_edge18(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 1, 5), [2, 3, 4, 5, 1])
    def test_edge19(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 5), [3, 4, 5, 1, 2])
    def test_edge20(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 3, 5), [4, 5, 1, 2, 3])
    def test_edge21(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 4, 5), [5, 1, 2, 3, 4])
    def test_edge22(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 5, 5), [1, 2, 3, 4, 5])

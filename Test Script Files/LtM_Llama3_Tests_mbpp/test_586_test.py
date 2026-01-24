import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 2, 1), [3, 4, 5, [1, 2]])

    def test_edge1(self):
        self.assertEqual(split_Arr([], 0, 0), [])

    def test_edge2(self):
        self.assertEqual(split_Arr([1], 1, 1), [[1]])

    def test_edge3(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 5), [[1, 2, 3, 4, 5]])

    def test_edge4(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 0, 0), [[1, 2, 3, 4, 5]])

    def test_edge5(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 0), [[1, 2, 3, 4, 5]])

    def test_edge6(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 0, 1), [[1, 2, 3, 4, 5]])

    def test_edge7(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 1), [[1, 2, 3, 4, 5]])

    def test_edge8(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 1, 5), [[1, 2, 3, 4, 5]])

    def test_edge9(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 5), [[1, 2, 3, 4, 5]])

    def test_edge10(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 0, 0), [[1, 2, 3, 4, 5]])

    def test_edge11(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 0), [[1, 2, 3, 4, 5]])

    def test_edge12(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 0, 1), [[1, 2, 3, 4, 5]])

    def test_edge13(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 1), [[1, 2, 3, 4, 5]])

    def test_edge14(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 1, 5), [[1, 2, 3, 4, 5]])

    def test_edge15(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 5), [[1, 2, 3, 4, 5]])

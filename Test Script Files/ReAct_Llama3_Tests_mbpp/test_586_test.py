import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):

    def test_typical_case(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 3
        k = 4
        expected = [5, 6, 7, 8, 9, 10, [1, 2, 3]]
        self.assertEqual(split_Arr(a, n, k), expected)

    def test_edge_case1(self):
        a = [1, 2, 3]
        n = 1
        k = 0
        expected = [[1, 2, 3]]
        self.assertEqual(split_Arr(a, n, k), expected)

    def test_edge_case2(self):
        a = [1, 2, 3]
        n = 3
        k = 3
        expected = [[1, 2, 3]]
        self.assertEqual(split_Arr(a, n, k), expected)

    def test_edge_case3(self):
        a = [1, 2, 3]
        n = 0
        k = 0
        expected = [[1, 2, 3]]
        self.assertEqual(split_Arr(a, n, k), expected)

    def test_error_case1(self):
        a = [1, 2, 3]
        n = 'a'
        k = 0
        with self.assertRaises(TypeError):
            split_Arr(a, n, k)

    def test_error_case2(self):
        a = [1, 2, 3]
        n = 3
        k = 'b'
        with self.assertRaises(TypeError):
            split_Arr(a, n, k)

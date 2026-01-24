import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):

    def test_typical_input(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 5
        k = 3
        result = split_Arr(a, n, k)
        self.assertEqual(result, [7, 8, 9, 10] + [1, 2, 3, 4])

    def test_edge_case1(self):
        a = [1, 2, 3, 4, 5]
        n = 1
        k = 0
        result = split_Arr(a, n, k)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_edge_case2(self):
        a = [1, 2, 3, 4, 5]
        n = 5
        k = 5
        result = split_Arr(a, n, k)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_edge_case3(self):
        a = [1, 2, 3, 4, 5]
        n = 0
        k = 0
        result = split_Arr(a, n, k)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_invalid_input1(self):
        a = [1, 2, 3, 4, 5]
        n = 'a'
        k = 3
        with self.assertRaises(TypeError):
            split_Arr(a, n, k)

    def test_invalid_input2(self):
        a = [1, 2, 3, 4, 5]
        n = 5
        k = 'b'
        with self.assertRaises(TypeError):
            split_Arr(a, n, k)

    def test_invalid_input3(self):
        a = [1, 2, 3, 4, 5]
        n = 5.5
        k = 3
        with self.assertRaises(TypeError):
            split_Arr(a, n, k)

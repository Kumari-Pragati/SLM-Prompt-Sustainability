import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_typical_case(self):
        a = [1, 2, 3, 4, 5]
        b = [2, 3, 4, 5, 6]
        n = 5
        self.assertEqual(find_Min_Sum(a, b, n), 9)

    def test_edge_case(self):
        a = [1, 2, 3]
        b = [2, 3, 4]
        n = 3
        self.assertEqual(find_Min_Sum(a, b, n), 2)

    def test_edge_case2(self):
        a = [1, 2, 3, 4, 5]
        b = [1, 2, 3, 4, 5]
        n = 5
        self.assertEqual(find_Min_Sum(a, b, n), 0)

    def test_error_case(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        n = 0
        with self.assertRaises(IndexError):
            find_Min_Sum(a, b, n)

    def test_error_case2(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        n = -1
        with self.assertRaises(IndexError):
            find_Min_Sum(a, b, n)

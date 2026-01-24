import unittest
from mbpp_275_code import get_Position

class TestGet_Position(unittest.TestCase):
    def test_simple(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        m = 2
        self.assertEqual(get_Position(a, n, m), 3)

    def test_edge_case1(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        m = 1
        self.assertEqual(get_Position(a, n, m), 5)

    def test_edge_case2(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        m = 5
        self.assertEqual(get_Position(a, n, m), 5)

    def test_edge_case3(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        m = 0
        with self.assertRaises(ZeroDivisionError):
            get_Position(a, n, m)

    def test_edge_case4(self):
        a = []
        n = len(a)
        m = 2
        with self.assertRaises(IndexError):
            get_Position(a, n, m)

    def test_edge_case5(self):
        a = [1, 2, 3, 4, 5]
        n = 0
        m = 2
        with self.assertRaises(IndexError):
            get_Position(a, n, m)

    def test_edge_case6(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        m = -2
        with self.assertRaises(ValueError):
            get_Position(a, n, m)

import unittest
from mbpp_275_code import get_Position

class TestGet_Position(unittest.TestCase):

    def test_typical_case(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 5)

    def test_edge_case(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 50
        self.assertEqual(get_Position(a, n, m), 5)

    def test_edge_case2(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 1
        self.assertEqual(get_Position(a, n, m), 5)

    def test_edge_case3(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 0
        with self.assertRaises(ZeroDivisionError):
            get_Position(a, n, m)

    def test_edge_case4(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = -1
        with self.assertRaises(ValueError):
            get_Position(a, n, m)

    def test_corner_case(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 5
        self.assertEqual(get_Position(a, n, m), 5)

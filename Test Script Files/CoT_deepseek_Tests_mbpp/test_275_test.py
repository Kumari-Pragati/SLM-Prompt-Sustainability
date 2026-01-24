import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):

    def test_typical_case(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 2)

    def test_edge_case_with_zero_m(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 0
        with self.assertRaises(ZeroDivisionError):
            get_Position(a, n, m)

    def test_edge_case_with_negative_m(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = -10
        with self.assertRaises(ValueError):
            get_Position(a, n, m)

    def test_edge_case_with_empty_list(self):
        a = []
        n = 0
        m = 10
        self.assertEqual(get_Position(a, n, m), -1)

    def test_typical_case_with_large_numbers(self):
        a = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000]
        n = len(a)
        m = 1000000000
        self.assertEqual(get_Position(a, n, m), 2)

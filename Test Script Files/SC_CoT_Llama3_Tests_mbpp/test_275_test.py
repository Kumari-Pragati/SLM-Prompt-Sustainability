import unittest
from mbpp_275_code import get_Position

class TestGet_Position(unittest.TestCase):
    def test_typical_inputs(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 5)

    def test_edge_cases(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 1
        self.assertEqual(get_Position(a, n, m), 5)
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 50
        self.assertEqual(get_Position(a, n, m), 5)

    def test_corner_cases(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 0
        with self.assertRaises(ZeroDivisionError):
            get_Position(a, n, m)

    def test_invalid_inputs(self):
        a = [10, 20, 30, 40, 50]
        n ='string'
        m = 10
        with self.assertRaises(TypeError):
            get_Position(a, n, m)

    def test_boundary_cases(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 20
        self.assertEqual(get_Position(a, n, m), 4)

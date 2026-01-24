import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):
    def test_typical_case(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case(self):
        a = [10]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 1)

    def test_boundary_case(self):
        a = [0, 0, 0, 0, 0]
        n = len(a)
        m = 1
        self.assertEqual(get_Position(a, n, m), 1)

    def test_invalid_input(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 0
        with self.assertRaises(ValueError):
            get_Position(a, n, m)

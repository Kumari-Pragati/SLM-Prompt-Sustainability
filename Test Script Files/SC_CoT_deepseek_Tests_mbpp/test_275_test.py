import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):

    def test_typical_case(self):
        a = [10, 20, 30, 40, 50]
        self.assertEqual(get_Position(a, 5, 2), 1)

    def test_edge_case(self):
        a = [10]
        self.assertEqual(get_Position(a, 1, 10), 1)

    def test_boundary_case(self):
        a = [10, 20, 30, 40, 50]
        self.assertEqual(get_Position(a, 5, 1), 5)

    def test_corner_case(self):
        a = [0, 0, 0, 0, 0]
        self.assertEqual(get_Position(a, 5, 0), 0)

    def test_invalid_input(self):
        a = [10, 20, 30, 40, 50]
        with self.assertRaises(ValueError):
            get_Position(a, -1, 2)
        with self.assertRaises(ValueError):
            get_Position(a, 5, 0)

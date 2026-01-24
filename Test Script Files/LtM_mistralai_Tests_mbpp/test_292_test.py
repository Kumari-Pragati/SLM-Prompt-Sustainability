import unittest
from mbpp_292_code import find

class TestFind(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find(10, 2), 5)
        self.assertEqual(find(15, 3), 5)
        self.assertEqual(find(20, 4), 5)

    def test_edge_cases(self):
        self.assertEqual(find(0, 2), 0)
        self.assertEqual(find(1, 2), 0)
        self.assertEqual(find(2, 1), 2)
        self.assertEqual(find(2, 2), 1)

    def test_boundary_cases(self):
        self.assertEqual(find(2147483647, 2), 1073741823)
        self.assertEqual(find(-2147483648, 2), -1073741824)

    def test_negative_division(self):
        self.assertRaises(ValueError, find, -5, 2)
        self.assertRaises(ValueError, find, 5, -2)

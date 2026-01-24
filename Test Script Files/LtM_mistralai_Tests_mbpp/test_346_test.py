import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(zigzag(0, 0), 1)
        self.assertEqual(zigzag(1, 0), 0)
        self.assertEqual(zigzag(1, 1), 1)
        self.assertEqual(zigzag(2, 1), 2)
        self.assertEqual(zigzag(2, 2), 3)

    def test_edge_cases(self):
        self.assertEqual(zigzag(-1, 0), None)
        self.assertEqual(zigzag(0, -1), None)
        self.assertEqual(zigzag(1, 2), 2)
        self.assertEqual(zigzag(2, 3), 5)
        self.assertEqual(zigzag(10, 10), 1023)

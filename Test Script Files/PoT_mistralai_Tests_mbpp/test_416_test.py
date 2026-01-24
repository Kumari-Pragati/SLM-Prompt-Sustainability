import unittest
from416_code import breakSum

class TestBreakSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(2), 1)
        self.assertEqual(breakSum(3), 1)
        self.assertEqual(breakSum(4), 2)
        self.assertEqual(breakSum(5), 2)
        self.assertEqual(breakSum(6), 1)
        self.assertEqual(breakSum(7), 2)
        self.assertEqual(breakSum(8), 3)
        self.assertEqual(breakSum(9), 4)
        self.assertEqual(breakSum(10), 5)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(breakSum(0), 0)
        self.assertEqual(breakSum(MAX), MAX)
        self.assertEqual(breakSum(1000001), MAX)
        self.assertEqual(breakSum(2**31 - 1), MAX)
        self.assertEqual(breakSum(2**31), MAX)

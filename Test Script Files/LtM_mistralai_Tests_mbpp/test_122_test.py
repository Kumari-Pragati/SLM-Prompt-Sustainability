import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)
        self.assertEqual(smartNumber(4), 7)
        self.assertEqual(smartNumber(5), 11)

    def test_edge_and_boundary(self):
        self.assertEqual(smartNumber(MAX - 1), MAX - 1)
        self.assertEqual(smartNumber(MAX), MAX)
        self.assertEqual(smartNumber(0), None)
        self.assertEqual(smartNumber(-1), None)
        self.assertEqual(smartNumber(MAX + 1), None)

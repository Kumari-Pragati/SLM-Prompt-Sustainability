import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(10), 29)
        self.assertEqual(smartNumber(30), 89)
        self.assertEqual(smartNumber(100), 269)

    def test_edge_cases(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(MAX - 1), MAX - 1)
        self.assertEqual(smartNumber(MAX), MAX)

    def test_boundary_cases(self):
        self.assertEqual(smartNumber(0), None)
        self.assertEqual(smartNumber(-1), None)
        self.assertEqual(smartNumber(MAX + 1), None)

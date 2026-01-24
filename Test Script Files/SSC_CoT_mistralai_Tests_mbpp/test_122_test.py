import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(10), 29)
        self.assertEqual(smartNumber(100), 293)
        self.assertEqual(smartNumber(1000), 2993)
        self.assertEqual(smartNumber(2000), 5897)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(smartNumber(0), 2)
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 2)
        self.assertEqual(smartNumber(MAX - 1), MAX - 1)
        self.assertEqual(smartNumber(MAX), MAX)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            smartNumber(-1)
        with self.assertRaises(ValueError):
            smartNumber(MAX + 1)
        with self.assertRaises(ValueError):
            smartNumber(float('nan'))
        with self.assertRaises(ValueError):
            smartNumber(complex(1, 2))

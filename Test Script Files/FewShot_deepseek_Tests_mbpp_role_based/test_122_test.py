import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)
        self.assertEqual(smartNumber(4), 7)
        self.assertEqual(smartNumber(5), 11)

    def test_boundary_conditions(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(MAX), 3001)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            smartNumber(0)
        with self.assertRaises(ValueError):
            smartNumber(-1)
        with self.assertRaises(ValueError):
            smartNumber(MAX + 1)

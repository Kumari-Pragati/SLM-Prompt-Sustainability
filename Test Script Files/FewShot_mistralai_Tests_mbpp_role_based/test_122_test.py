import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):
    def test_positive_index(self):
        self.assertEqual(smartNumber(10), 4)
        self.assertEqual(smartNumber(100), 19)
        self.assertEqual(smartNumber(3000), 3003)

    def test_zero_index(self):
        self.assertEqual(smartNumber(0), 2)

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            smartNumber(-1)

    def test_large_input(self):
        with self.assertRaises(ValueError):
            smartNumber(3001)

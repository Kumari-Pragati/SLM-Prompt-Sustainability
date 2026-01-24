import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):

    def test_smartNumber_with_valid_input(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)
        self.assertEqual(smartNumber(4), 7)
        self.assertEqual(smartNumber(5), 11)

    def test_smartNumber_with_large_input(self):
        self.assertEqual(smartNumber(10), 29)
        self.assertEqual(smartNumber(20), 79)
        self.assertEqual(smartNumber(30), 149)

    def test_smartNumber_with_invalid_input(self):
        with self.assertRaises(IndexError):
            smartNumber(0)
        with self.assertRaises(IndexError):
            smartNumber(3001)

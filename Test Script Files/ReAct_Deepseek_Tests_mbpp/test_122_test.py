import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)
        self.assertEqual(smartNumber(4), 7)
        self.assertEqual(smartNumber(5), 11)

    def test_edge_cases(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)
        self.assertEqual(smartNumber(4), 7)
        self.assertEqual(smartNumber(5), 11)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(IndexError):
            smartNumber(0)
        with self.assertRaises(IndexError):
            smartNumber(-1)
        with self.assertRaises(IndexError):
            smartNumber(3001)
